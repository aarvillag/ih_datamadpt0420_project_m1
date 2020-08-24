# Data Project README file


### :raising_hand: **DATA PROJECT MODULE 1 IRONHACK 2020 JULY** 
Here we are going to analyze information in a database with three tables related to information about people and their jobs from European countries. 

To do that we have also connect and get information from a Eurostat API and web. With this complementary information we will get information about jobs and information about countries.

The first challenge is to get a summary table per country about all jobs there are in the database with its percentage. You can filter per country.

The second challenge is to get a summary table about answers in a survey with multichoice. 


### :baby: **Status**
Version 1.0

This is the first version produced. I hope we can improve it to release future versions with more information.


### :running: **One-liner**
With “main_scrypt.py” the party starts.

We have to include arguments,
--path (-p) is required for the path+file of database
--country (-c) is not required if you want to get the whole European countries analysis together. But if you indicate one country you will get the analysis of the country selected. Only the challenge 1 analysis consider the country selected.

The result will be presented on screen, but also you will get a csv file with details in the folder ./data/


### :computer: **Technology stack**
We use python language with several libraries (pandas, re, sys, argparse, datetime, os, sqlalchemy, requests)

The software can be executed from a computer terminal if the folder structure is replicated. 


### :boom: **Core technical concepts and inspiration**
This is the first project for IRONHACK data analysis boot camp.
Is the first software project I have made for years. I did several in the 90’s but totally different technology.

In my opinion, I have improved in my way to code.

I can demonstrate that with this technology we can manage massive information and automatize its analysis.

### :wrench: **Configuration**
To use this software, you must replicate the folder structure to avoid problems.

You have to install python 3.7 version and all libraries
•	pandas, 
•	re, 
•	sys, 
•	argparse, 
•	datetime, 
•	os, 
•	sqlalchemy, 
•	requests

### :see_no_evil: **Usage**
With “main_scrypt.py” the party starts.

We have to include arguments,
--path (-p) is required for the path+file of database. If the path or file doesn’t exist the program end with the error.
--country (-c) is not required if you want to get the whole European countries analysis together. But if you indicate one country you will get the analysis of the country selected. 
If the country indicated is not found in the database the program end with an error.
Only the challenge 1 analysis consider the country selected.

Output.

You will get the information on the screen of terminal and also some csv files in the folder ./data/

### :file_folder: **Folder structure**
```
└── project
    ├── __trash__
    ├── .gitignore
    ├── .env
    ├── requeriments.txt
    ├── README.md
    ├── main_script.py
    ├── notebooks
    │   └── my_notebook.ipynb
    ├── p_acquisition
    │   └── m_acquisition.py
    ├── p_wrangling
    │   └── m_wrangling.py
    ├── p_analysis
    │   └── m_analysis.py
    └── data
        ├── raw
        ├── processed
        └── results
```

> Do not forget to include `__trash__` and `.env` in `.gitignore` 

### :shit: **ToDo**
Next step will be finalizing challenge 3

### :information_source: **Further info**


### :love_letter: **Contact info**
Agustin Arvilla (aarvillag@gmail.com)
Getting help, getting involved, hire me please.

---


