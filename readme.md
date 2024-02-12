This program runs reads the files and returns the sentence with the largest
number of n-grams on the first requirement

on second requirement 2 it finds the word with the most definitions which is
"head"

on requirement 3 it displays the definitions of the words by verifying the keys
with the nouns data

- Do not run the python file directly on it's own!! else it will give the error
  "[Errno 2] No such file or directory:"

- Extract "Akwasi_Lab2" from the zip file
- Open the "Akwasi_Lab2" folder as development environment before you run the
  program.
  - if you have VsCode, right click the folder "Akwasi_Lab2"
  - click "open with Code"
  - On windows 11 - right click folder
    - click "show more options"
    - Click "open with Code"
- Then you can run the python file

- it is important to leave the folders as they are and not move the text files
  out out of the "Nouns" folder. doing this will not allow the program to locate
  where they are.

[NOTE] - With requirement 1, i print out the one of the data that has has the
largest number of of N-grams(ie. several lines have 9 N-grams. the code just
displays one of them).

in essence, the code ran through every line in the "NounsIndex.txt" and returned
the last item it found where the number of sub parts was either equal or greater
than the previous one. When there were no new items to check it stops.

Requirement 3 all definitions were found but are not in
Chronological/Alphabetical order but instead the order that requirement 2 found
the keys. hence the order of outputs will be different from the sample in the
PDF. if i had done a sort on the output of requirement 2 and then ran the loop,
the order of output would be identical to the sample output found in the pdf.
