famous-last-words
==============================

Fiddling with GPT2 and other NLP models for interesting corpus text generation

To start run the bash script to setup the environment properly.

> . ./setup_env.sh

This will initialize a git repo and make a first commit. It will also create a conda environment and
kernel with the specified project name installing dependencies.

Be sure to uncomment lines:

> /data/

> reports/data-profiling/*

From .gitignore file if data should be ignored in versioning

To install various useful Jupyter Lab extensions, run:

> . ./jupyter-extensions.sh

If the project is finished and the environment is no longer needed 
(it can be rebuilt running setup_env.sh again), run:

> . ./teardown_env.sh

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `01.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
	|
    ├── setup.sh           <- Script to initiailize git repo, setup a conda virtual environment  
    │                         and install dependencies.
    ├── teardown_env.sh    <- Script to teardown the project conda virtual environment  
    │                         
    ├── setup.py           <- For installing src as a local package   
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   ├── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   │     └── visualize.py
    │   │ 
    │   └── utils          <- Utility code for various purposes and packages
    │	    ├── project_utils.py   <- For project specific utilities
    │       ├── gists              <- Code gists with commonly used code (change to root
    │       │                         directory, connect to database, profile data, etc)
    │       ├── io                 <- Code for input/output utilities
    │       ├── etl                <- For building reproducible ETL pipelines, including data
    │       │                         checks and transformers
    │       ├── ml                 <- Machine Learning utility code (feature engineering, etc) 
    │       ├── pandas             <- Pandas related utility code
    │       │   ├── analysis                  
    │       │   ├── cleaning
    │       │   ├── engineering
    │       │   ├── text    
    │       │   ├── datetime     
    │       │   ├── optimization       
    │       │   └── profiling      
    │       └── text               <- Code for dealing with text. Includes distributed loading of text corpus, 
    │                                 entity statement extraction, sentiment analysis, etc.	
    │       
    ├── LICENSE
    │       
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org



Much of the boilerplate code and structure for this comes from [Driven Data's Cookie Cutter Data Science](https://github.com/drivendata/cookiecutter-data-science)

--------