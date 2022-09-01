# Generating-real-time-Indian-movie-news-and-publishing-the-data-using-Ansible-and-AWS

Developed this project for understanding the integration process of deploying a flask application using Ansible with AWS as the cloud platform configured within the playbook.

## Prerequsite
* To run the playbook, ansible and boto need to be installed on local machine. pip install ansible boto
* Following environment variables need to be configured for AWS credentials.

AWS_ACCESS_KEY_ID=AKIAQGSGI********* 
AWS_SECRET_ACCESS_KEY=ScBxDindD4ddVEMLSJi+1**********

## Steps while developing application

### I) Developed a Flask application for generating real time Indian movie news from a 3rd party NEWS API
* Designed the application for fetching top news related to the Indian Movie industry and also daily news articles from different news categories

### II) Built different roles in ansible for managing configuration for AWS Resources and Flask Application
* Designed an Ansible Playbook for managing infrastructure and its environment variables which creates the infrastructure and the next tasks for hosting the flask application on AWS Infrastructure
* AWS Roles contain detailed information of instructions needed for providing AWS resources such as VPC, Security Groups, Routing Tables, Internet Gateway and creating an EC2 Linux Instance
* Flask Roles contain detailed information of the application, the styling details of the application, library dependencies required for the application and the flask service details of the order in which the executables are stored

### III) Once these details are provisioned we need to configure the AWS Access Key and Secret Keys as environment variables and provision them to the AWS infrastructure instructions

### IV) Once these are provisioned we also define the details of the hosts on which the application is executed within the "ansible.cfg" configuration file

## Usage Instructions

* Without any existing infrastructure, the below command will configure VPC, Subnets, Internet Gateway, Key Pair and launch an EC2 Instance 

__Command: ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook ec2-provision.yml -u ubuntu

## Verifying the Web Application

Once the playbook execution is completed, launched EC2's Public IP will be showing

PLAY RECAP *********************************************************************

34.208.124.86              : ok=7    changed=2    unreachable=0    failed=0

localhost                  : ok=12   changed=4    unreachable=0    failed=0

This IP address will be serving a very simple webserver running on flask which will show us the web application deployed.

<img width="1402" alt="news" src="https://user-images.githubusercontent.com/29569453/187806368-160054ba-e542-4b7d-963d-1d609e4108c9.png">


