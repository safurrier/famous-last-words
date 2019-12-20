#!/bin/bash 

# initialize git repo and make first commit
#git init
#git add .
#git commit -a -m 'first commit'

project_name=famous_last_words
printf "Project name is: "$project_name
printf "\nThis will be conda env name"
# Create conda environment with project name
conda create -y --name $project_name python=3.6
# Activate environment
source activate $project_name
# Attach kernel of this environment for use with jupyter 
#python -m ipykernel install --user --name $project_name --display-name $project_name

# Install Requirements  
# conda install -y --file requirements.txt
pip install -r requirements.txt

python -m spacy download en_core_web_sm

# Install src as local package
pip install -e .

