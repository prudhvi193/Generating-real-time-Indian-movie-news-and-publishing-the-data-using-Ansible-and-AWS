# Generating-real-time-Indian-movie-news-and-publishing-the-data-using-Ansible-and-AWS

Developed this project for understanding the integration process of deploying a flask application using Ansible with AWS as the cloud platform configured within the playbook.

### I) Developed a Flask application for generating real time Indian movie news from a 3rd party NEWS API
* Designed the application for fetching top news related to the Indian Movie industry and also daily news articles from different news categories

### II) Built different roles in ansible for managing configuration for AWS Resources and Flask Application
* Designed an Ansible Playbook for managing infrastructure and its environment variables which creates the infrastructure and the next tasks for hosting the flask application on AWS Infrastructure
* AWS Roles contain detailed information of instructions needed for providing AWS resources such as VPC, Security Groups, Routing Tables, Internet Gateway and creating an EC2 Linux Instance
* Flask Roles contain detailed information of the application, the styling details of the application, library dependencies required for the application and the flask service details of the order in which the executables are stored

* Once these details are provisioned we need to configure the AWS Access Key and Secret Keys as environment variables and provision them to the AWS infrastructure instructions

* Once these are provisioned we also define the details of the hosts on which the application is executed within the **ansible.cfg configuration file

* Lastly we run the playbook with the below command specified, which generates the required DNS information of the provided host over which the application is built
** Command: ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook ec2-provision.yml -u ubuntu
