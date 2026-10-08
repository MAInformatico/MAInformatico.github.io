---
layout: post
title: Building an LLM-powered job analyzer architecture, trade-offs, and lessons learned
author: Migue
---

Job searching is a marathon. You keep reading offers, checking if they match your stack, your shift preferences, your remote/hybrid constraints, and deciding whether to apply. After dozens of them, you're tired. It's repetitive, and it drains time you could spend on actual applications.

So I built a previous filter to answer one question: **is this offer worth my time?**

That's what [job-analyzer](https://github.com/MAInformatico/job-offer-analyzer/tree/main) does. It's a backend tool that helps job seekers evaluate whether a job offer is worth applying to, using LLM-powered analysis of both the offer text and the company's reputation. Stack: **FastAPI, Docker, Github Actions, LLM, LangChain, RAG**.

My main goal was to build something useful, scalable, and maintainable. The first design decision was to **separate the user's criteria from the code**. Those criteria live in a YAML file — you can see an example [here](https://github.com/MAInformatico/job-offer-analyzer/blob/main/config.example.yaml).

## RAG vs fine-tuning

Fine-tuning a model to evaluate job offers would mean retraining every time the user's criteria change. That's expensive, slow, and brittle. With RAG, the criteria live in the vector store, and the model retrieves the most relevant ones at query time. Changing the criteria means updating the YAML file and re-indexing, not retraining a model. For a personal tool where priorities evolve, that was the obvious choice.

## How the pipeline works

The first version was a single endpoint that did everything: it received the offer, parsed it, and returned a score. It used Llama through an API, and the whole thing was too monolithic to iterate on. When I stopped using that model, I had to rethink the architecture anyway, so I took the opportunity to split the pipeline into stages.

Now the offer is cleaned and chunked into sections — role, requirements, stack, location, compensation. Each chunk is embedded and stored in a vector store. When a new offer comes in, the system queries the store with the user's criteria, retrieves the top-k relevant chunks, and sends them to the LLM with a structured prompt. The output is parsed into a Pydantic model with fields like score, matched_criteria, missing_criteria, and reasoning.

I now use OpenAI as the main LLM provider and Groq for fast inference on some tasks. Having two providers also gave me a fallback when one of them was slow or unavailable.

The tool is containerised with Docker and deployed locally. CI runs on GitHub Actions: tests run on every push. Nothing fancy, but it means I can iterate without breaking things.

## What I'd do differently

- **Start with evals.** I added the evaluation set later, and I regret not doing it earlier. Without it, I was guessing whether changes improved the tool.
- **Separate the parsing layer from the scoring layer.** They have different failure modes and should be tested independently.
- **Version the prompts.** Treat them like code. They change, and you need to know which version produced which result.

## What's next

The tool works, but there's room to grow:

- **Feedback loop**: let the user mark a score as correct or incorrect, and use that to improve the retrieval and prompt.
- **More sources**: integrate with more job boards and company review platforms.
- **Dashboard**: a simple UI to review past analyses and track applications.

The code is on [GitHub](https://github.com/MAInformatico/job-offer-analyzer/tree/main), and I write about backend and AI on my [blog](https://mainformatico.github.io).


> "If you can think it, you can code it"
