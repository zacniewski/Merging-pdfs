## Merging pdf documents


#### :arrow_right: The idea behind this script is to merge documents that are similar with their names and differ only with number postfix after underscore.  


#### :arrow_right: Example of two file names, that are handled by this script:  

  * `TypeA_01.pdf`
  * `TypeA_02.pdf`  

#### :arrow_right: Requirements
  * The only requirement is [PyPDF2](https://pypi.org/project/PyPDF2/) library,  
  * You can install PyPDF2 via pip: `pip install PyPDF2`.  

#### :arrow_right: Basic usage
  * Starting content of 'pdfs' directory:  

    ![mp1](screenshots/mp1.png)

  * We have few groups of pdf documents. Every group has the same prefix (before `_`) and differs only with number after `_`,  

  * Every group is outlined in the separate rectangle,  

  * Some documents are single documents - they don't have any number, or they have unique name and single number after `_`,  

  * The `pdfs` directory contains all the documents, and this name is hardcoded in the last line of the script,  

  * To run a script simply type:  `python3 pdf_merger.py` (or `python pdf_merger.py` depending on your OS),  

  * Final content of the working directory:  

    ![mp2](screenshots/mp2.png)  

  * Interpretation of the final content:
      * all documents from given group are merged into one document,  
      * single document with `_` and the number before `.pdf` is also available in the output,  
      * documents without `_` in their names weren't merged and aren't available in the output,  
      * all output documents have the name of the group, without `_` and without number.
  




