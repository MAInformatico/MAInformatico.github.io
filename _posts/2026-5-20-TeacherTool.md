---
layout: post
title: Replacing a manual workflow with a Python backend service
author: Migue
---

When my girlfriend and I started dating, we talked a lot about our jobs. One topic that came up often was her grading workflow.
  
She used to manually correct exams, calculate averages for each assessment area, and write the results into a Word document. The process was repetitive and time-consuming.
  
I became curious about the constraints of the evaluation process:
  
What happens if a student only completes part of the exam?
Are there different scoring rules depending on language level (e.g. B1 vs C1)?
How is the “Use of English” criterion handled in higher levels?
  
A few months later, she moved in with me. Since I had a local server running 24/7 and she was using macOS, I decided to design a small REST API to simplify her workflow and avoid environment-related issues.
  
The main motivation was to decouple the execution environment from the client side. Instead of dealing with Python dependencies across different operating systems, all logic runs on a single server with a controlled environment.
  
I implemented a REST API using FastAPI and Pydantic for data validation. The service receives input such as:
  
number of students
exam identifiers
language level
scores per assessment area (correct answers / total questions)
  
The backend processes the data, computes the results, and stores them in a structured format. These values are then injected into a DOCX template, which generates the final report. The resulting file is made available for download via the API.
  
From a design perspective, I kept the system intentionally simple:
  
* single service architecture
* no unnecessary distributed components
* local server deployment using Docker
* isolated Python environment to ensure reproducibility
  
After deploying the solution, the time required for processing a group of students dropped significantly. What previously required several minutes of manual work was reduced to a short API call and a quick data entry step.
  

> "If you can think it, you can code it"
