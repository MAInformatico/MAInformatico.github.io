---
layout: post
title: No linear data structures
author: Migue
tags: [Technology]
---

This afternoon I remembered a subject of my degree. It is called Data Structures. To know the content of the subject is straightfoward.
   

In this subject we learn mainly the Standard Template Library (STL) of C++. This library content a lot of
structures: vector, queue, list ... many of them linear data structure. But also there are, non-linear 
structures: Maps, trees ...
   

In general, the latter used to be the least time dedicated to them. Luckily, I was lucky enough to have a great teacher that teach me all these data structures, including non-linear structures.

So, today in 2019 I found myself some situations while coding that show me the great importance of this kind of structures.
   

Eg: you need to explore the content of a directory. This sound so easy ... ok, explore the content of a 
directory and also find all the files with an specific condition. Now I ask you some questions:
   

Have you think if the directory contains another directory inside? What happen if there are more than one? or 
If there are some files in a deep directory or more?

Now we can think: the directory is so similar a tree TAD. Ok, but we need to filter the files too. So there is another structure called dictionary (in Python) that let us to associate a key with a value.

If we import walk function from the module os in Python 3.7 Just we need to give a path parameter and get the folders and files on the parameter.

So, we need to associate folder (key) --> files (values)
   
Maybe could be so many files. How can we "store" it? Now we can use a linear data structure called list. Call function give us the file on a list so, just we need to associate each folder with the correct file list.

After that we need to check our dictionary and get filter the file. A dictionary is non-linear How can we access to the info without an iterator or know the directory name?

Using the keys() function (in Python) this function returns the keys of a dictionary. By this way we have access to our data and we can filter or take the necessary actions for our purpose.

Just to say thank you to my teacher that these days I am remembering her.


> Happy coding!