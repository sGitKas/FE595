####
## User documentation for They Fight crime Character NLP Analysis Assignment 
####
### Synopsis
There are   3 scripts in the assignment -

- [x] The Merger script will scan given a directory for files and merge them into a single file.
- [x] Best and Worst script will assign a sentiment to each of the sentences and finds the best and the worst characters.
- [x] 10MostCOmmon script will group the sentences together and see if there is any pattern in the characters.

To run these scripts please follow the below instructions-
* Down load the data in the data folder into your local folder 
* In the line 14 of the merger data/*.* indicates the place where the files are kept  (This would be the path of the folder where your data resides)
* Now run the merger.py which will create a new file called the combined.txt in your working directory
* Now run the BestAndWorst.py which assumes that a 'combined.txt' is present in the working directory from the prior step. It prints the best and worst chracters.
* Finally run the 10MostCommon.py which prints the top 10 Most common characters and top 10 most common charecters using the third word. 