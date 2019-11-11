# HOW TO CONTRIBUTE

This is a community project and contributing to it is highly appreciated.

**Step 1:**
Fork the repository to create a copy of the code under your own github account

**Step 2:**
Clone your repository fork into a location of your choice on your machine.

**Step 3:**
Install the development dependencies
```sh
pip install --upgrade autopep8
```
## Pull Request Guide

For a pull request to be merged, it has to be reviewed by the library maintainer.
To aid in the reveiwing process, kindly ensure your PR complies with the following rules.

**1:** Give your pull request a helpful title that summarises what the contribution does

**2:** Make sure your code passes all the tests

**3:** Ensure that your PR does not add PEP8 violations. In this library, autopep8 has been used to enforcce pep8 regulations.
       To modify a file using autopep8, run:
       
```sh
$ autopep8 --in-place --aggressive --aggressive <filename>
```
      
 This automatically edits the file to comply with pep8. Please check your code against other linting tools suck as flake8 to maintain code style and formatting consistency
      
 **4:** Make sure your code is properly commented and documented, and make sure the documentation renders properly. Refrain from unneccessary comments. The comments in this library are only for doc generation purposes
