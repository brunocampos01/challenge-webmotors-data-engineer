# Inverse Index

## Describe
Challenge for Data Engineer at [webmotors](https://www.webmotors.com.br/).

### Requirements
- java 1.8 openjdk<br/>
`sudo apt-get install openjdk-8-jdk`
- Python 3.6<br/>
`sudo apt-get install python3.6`
- pip<br/>
`sudo apt-get install python-pip`
- Libs<br/>
`pip install -r requirements.txt`<br/>
- Git<br/>
`sudo apt-get install git`

## Structure This Project

- I following [best pratices in Spark](https://www.slideshare.net/SparkSummit/pyspark-best-practices-by-juliet-hougland)
```
.
├── dataset
│   ├── 0
│   ├── 1
│   ├── ...
│   ├── 44
├── images
│   ├── figura_1.png
│   ├── figura_2.png
│   ├── figura_3.png
│   └── figura_4.png
├── README.md
├── solution
│   ├── configs
│   │   └── etl_config.ini
│   ├── environment
│   │   ├── create_virtual_env.sh
│   │   ├── __init__.py
│   │   ├── makefile
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── test_environment.py
│   │   ├── venv
│   │   └── virtualenv_requirements.txt
│   ├── jobs
│   │   ├── job_generate_dict.py
│   │   ├── job_map_wordid_documentid.py
│   │   ├── job_reduce.py
│   │   └── workflow_manager.py
│   ├── README.md
│   ├── tests
│   │   ├── __init__.py
│   │   └── integration_tests.py
    └── tmp
```

## Running
1. Clone this repository
```sh
git clone git@github.com:brunocampos01/challenge-webmotors-data-engineer.git
cd challenge-webmotors-data-engineer
```

2. Choose which environment to running
 - [local](environment/README.md)
 - [virtual environment](environment/README.md)

3. In terminal running command `spark-submit solution/jobs/job_generate_dict.py
` and `spark-submit solution/jobs/job_map_wordid_documentid.py`

##### NOTES
- All the development was done using **virtualenv**. 

---

#### Author
<a href="mailto:brunocampos01@gmail.com" target="_blank"><img class="" src="https://github.com/brunocampos01/devops/blob/master/images/gmail.png" width="28"></a>
<a href="https://github.com/brunocampos01" target="_blank"><img class="ai-subscribed-social-icon" src="https://github.com/brunocampos01/devops/blob/master/images/github.png" width="30"></a>
<a href="https://www.linkedin.com/in/brunocampos01/" target="_blank"><img class="ai-subscribed-social-icon" src="https://github.com/brunocampos01/devops/blob/master/images/linkedin.png" width="30"></a>
Bruno Aurélio Rôzza de Moura Campos 

---

#### Copyright
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br/>
