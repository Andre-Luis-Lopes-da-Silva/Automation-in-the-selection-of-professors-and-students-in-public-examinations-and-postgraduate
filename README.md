# Automation-in-the-selection-of-professors-and-students-in-public-examinations-and-postgraduate
Automated system for the selection of professors and students in postgraduate processes and public examinations using academic metrics from the international database SCOPUS using the pybliometrics REST API.

Nowadays, the selection of students and professors in Brazil are completely primitive and inefficient. These public examinations are done manually, artisanal and very time consuming, resembling more a test of resistance than of competence. Written test is extremely tendentious, which allows corrupt practices to be routinely employed. The didactic test is also another subjective assessment that can be used in corrupt practices. The use of metrics can eliminates the corruption practices and select the best applicants, the most competent. It is important for the university to acquire professors that can bring resources to the institution by approving projects in funding agencies, and only the most productive, those with the best indicators, are able to do this.
Therefore, the automated system for the selection of professors and students in postgraduate processes and public examinations was developed.
This system uses as an input, only the ID Scopus of the author (e.g. 26651881400). So, it uses a REST API  pybliometrics (Rose and  Kitchin, 2019) to obtain the SCOPUS’ data using a python algorithmic. The metrics employed are the (1) h-index, (2) number of citations, (3) i10-Index (the number of publications with at least 10 citations), (4)  i20-Index (the number of publications with at least 20 citations) and (5) the number of documents. The ranking is performed in this same order. An ordered list is presented according the classification of the applicants. 

Like this example below: 

![Tabela exemplo](https://user-images.githubusercontent.com/78765404/177054850-0d18ed8e-1130-4133-8808-3caf68601828.jpg)

Reference

Rose, Michael E. and John R. Kitchin: “pybliometrics: Scriptable bibliometrics using a Python interface to Scopus”, SoftwareX 10 (2019) 100263.
