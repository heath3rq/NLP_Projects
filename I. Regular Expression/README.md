The goal of this project is to develop regular expressions that address the following prompts. 

## Q1 

Write a regular expression that matches people’s full names. Here are some example names:
* Quan Hongchan
* Philip Seymour Hoffman
* Dr. Nicki Washington
* Joseph Gordon-Levitt
* Ken Griffey, Jr.
* John von Neumann

It should not match single names like “Cher”, or non-name strings:
* Cher
* not a name
* happy feet
* The end

You should be able to do perfectly with a regular expression < 72 characters. You are not expected to solve this problem generally; it is impossible. Describe in what situations your solution will fail.

## Q2
Develop a regular expression that matches all gerunds within a text. For example, from the text 
`harry loves to sing while showering` your expression should match only showering. You may assume that:
* the input contains only lowercase letters, punctuation, and whitespace
* any non-letter character is not part of a word (there will be no contractions, hyphenated words, etc.).

State any other assumptions that you would like to make. Generate your own test cases and write a script testing your expression. Describe in what situations
your solution will fail.