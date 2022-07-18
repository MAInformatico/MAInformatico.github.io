---
layout: post
title: How can I revert a commit in git
author: Migue
---
Imagine, you have completed your task successfully. All the tests work properly without problems at the first time (Remember, I have said: 'Imagine' :D ) and you perform a commit into team repo's git.
However you find an issue in your code and your code has been commited in the repo. Ok, Relax! you can fix it!

Git allow us to fix these kind of issues using the command:
`git revert <your last commit code>` 
This command allow us to remove our last commit, in case of our commit has been commited. 

* If we have not commited our changes
You can revert the change using this command:
`git reset --soft HEAD~1` (if you wish to keep your changes)

or

`git reset --soft HEAD~1` (if you do not want to keep your changes)

I hope these commands can be helpfull for you, specially on those moments that we feel stressed by a mistake.

> "Memento mori"
