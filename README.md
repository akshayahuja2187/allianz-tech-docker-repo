# git-jenkins-docker


## Overview
The purpose of this challenge is to know not only about your technical skills, but also:

- Know how do you approach the infrastructure design
- Know how do you explain the solution and communicate

As the position is based on the DevOps world, we ask you to set up a CI/CD pipeline. Basically, you need to set up a repository, connect it to a pipeline with some automation on it, so every time the repository is updated, a new Docker image is build, ready to use it in a deployment.

In this repository we provide you the [containerized application](./app), and the [Dockerfile](./Dockerfile). Is a simple Nginx webserver, serving a static HTML file.

The deadline is **7 days**, starting today (the day you got the email from HR with this information). Feel free to get back to us if you have any questions or concerns, or if for any reason you can't finish within the given timeline.


## Requirements
At least:
1. You must use [GitHub](https://github.com), [Gitlab](https://about.gitlab.com) or any other `git`-like repository for hosting the source code.
2. You must use [Jenkins](https://www.jenkins.io) automation tool for setting up the pipeline.
3. You must use [Docker Hub](https://hub.docker.com) or any other *Docker* container registres like ACR, ECR etc. to save the container images.
4. The pipeline should be triggered when a *Pull request* is merged into `main` or `master` branches of your repository. Direct commits into `main` or `master` are not allowed.
5. You must use as much configuration-as-code (CaC) as possible. Authentication secrets like usernames/passwords/tokens should be isolated from the tools you're using.
6. Deploy the image and run the app somewhere on AKS/EKS/Minikube/Your own Kubernetes cluster, if possible create the CD pipeline in Jenkins for the deployment to Kubernetes cluster and apply blue/green deployment and canary deployment.

## Steps
To achieve the requirements, you should follow this procedure:
1. Clone this repository to your repo
2. Set up the pipeline
3. Modify the `index.html` file, changing the content inside `<main></main>` tags for something else i.e. `Hello! I'm [YOUR_NAME]`.
4. Build the docker image and push it to a container registry
5. Deploy the image and run the app somewhere on AKS/EKS/Minikube/Your own Kubernetes cluster, if possible create the CD pipeline in Jenkins for the deployment to Kubernetes cluster and apply blue/green deployment and canary deployment.


## Deliverables
You must:
1. Provide the **source code** you used.
2. **Show us** how the CI/CD works with a real example.


Repos Created:

1. Terraform Repo: https://github.com/akshayahuja2187/allianz-tech-terraform
This contains terraform code to create resource group, vnet, subnet, NIC, Public IP, NSG, VM to host jenkins instance alongwith terraform state being maintained in azure storage account.
Also contains the terraform.yaml workflow using Github actions to run a pipeline to do az login, terraform init, terraform validate & terraform apply. More details on the repo's Readme.md file.

2. Jenkins instance has been created is accessible here http://20.xxx.x.xx:8080/ 
with guest user: Login ID: guest PWD: guest_user

I will be keeping the VM in Stopped(Deallocated State) as it's costly to keep it running on my personal subscription, Please share me a timeframe over email and I can turn it on for your review.

3. Dockerhub repos: https://hub.docker.com/repository/docker/akshayahuja2187/snapshots
https://hub.docker.com/repository/docker/akshayahuja2187/releases

4. App repo : https://github.com/akshayahuja2187/allianz-tech-docker-repo

This required some basic troubleshooting with the dockerfile and the nginx.conf
Build and deployment pipelines: Jenkinsfile.build & Jenkinsfile.deploy

- There are much more enhancements and improvements possible using various ways such as creating custom and repeatable groovy functions and adding them to the jenkins library which can be sourced in other Jenkinsfiles as well.

- The current pipelines are still rudimentary due to time-shortage (alongwith fulltime work), yet I have tried to cover the basic deliverables. Given some more time, these can be made much better. The triggering mechanism needs rework to better refine it.

- Adding one more comment to showcase the PR open status

