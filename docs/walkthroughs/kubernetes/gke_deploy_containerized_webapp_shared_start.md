---
url: https://docs.cloud.google.com/walkthroughs/kubernetes/gke_deploy_containerized_webapp_shared_start/
title: Deploy a containerized web application with GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:22.142789+00:00
---

# Deploy a containerized web application with GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/walkthroughs/kubernetes/gke_deploy_containerized_webapp_shared_start/




#  Deploy a containerized web application with GKE Stay organized with collections  Save and categorize content based on your preferences. 

## ![](https://walkthroughs.googleusercontent.com/content/images/intro-page.png)

Learn how to:

  * Package a sample web application into a Docker image.
  * Upload the Docker image to Artifact Registry.
  * Create a GKE cluster.
  * Deploy the sample app to the cluster.
  * Manage autoscaling for the deployment.
  * Expose the sample app to the internet.
  * Deploy a new version of the sample app.
  * Clean up the resources used in this walkthrough.



Estimated time to complete: 

Click **Start** to begin.

## Enable Google Kubernetes Engine in a Cloud project

For access to Google Kubernetes Engine, select or create a Cloud project to work in, then enable the required APIs:

  1.   2. 


Click **Next** to learn how to build a container image that can access the Kubernetes APIs.

## Get the source code

In this tutorial, you deploy a [sample web application](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/quickstarts/hello-app) called `hello-app`, a web server written in [Go](https://golang.org/) that responds to all requests with the message `Hello, World!` on port 8080.

  1. Click **Activate Cloud Shell**.

  2. Clone the `hello-app` source code and Dockerfile by running the following commands:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples
         cd kubernetes-engine-samples/quickstarts/hello-app
         

  3. Set the `PROJECT_ID` environment variable to your Google Cloud project ID in the `export` command below. The `PROJECT_ID` variable associates the container image with your project's **Artifact Registry**.
         
         export PROJECT_ID=YOUR_PROJECT_ID_GOES_HERE
         

  4. Confirm the `PROJECT_ID` environment variable has the correct value:
         
         echo ${PROJECT_ID}
         




Click **Next** to learn how to build a docker image for your app.

## Build your Docker image

### Create a repository

First, create a repository to store your container images.

  1. You will need to specify a region for your repository. Run the following command to see a list of possible regions, then select the one closest to you.
         
         gcloud artifacts locations list
         

  2. Create a **REGION** variable to hold your selected region. The following sets REGION to us-west1:
         
         export REGION=us-west1
         

  3. Run the following command to create your repository.
         
         gcloud artifacts repositories create hello-repo \
             --repository-format=docker \
             --location=${REGION} \
             --description="Docker repository"
         




## Build the image

GKE accepts Docker images as the application deployment format. Before deploying the `hello-app` application, you must package the source code as a Docker image.

To build a Docker image, you need source code and a Dockerfile. A Dockerfile contains instructions on how the image is built.

  1. Build and tag the Docker image for `hello-app`:
         
         docker build -t ${REGION}-docker.pkg.dev/${PROJECT_ID}/hello-repo/hello-app:v1 .
         

This command instructs Docker to build the image using the `Dockerfile` in the current directory and tag it with a name, such as `us-west1-docker.pkg.dev/my-project/hello-repo/hello-app:v1`. The image is pushed to Artifact Registry in the next section

  2. Authorize **Cloud Shell** to make Google Cloud API calls, if prompted.

  3. Run the `docker images` command to verify that the build was successful:
         
         docker images
         

Output:
         
         REPOSITORY                                                     TAG     IMAGE ID       CREATED          SIZE
         us-west1-docker.pkg.dev/your-project-id/hello-repo/hello-app    v1      25cfadb1bf28   10 seconds ago   54 MB
         




Click **Next** to learn how to push a docker image to **Artifact Registry**.

## Push the Docker image to Artifact Registry

  1. Ensure the Artifact Registry API is enabled for the Google Cloud project you are working on:
         
         gcloud services enable artifactregistry.googleapis.com
         

  2. Configure the Docker command-line tool to authenticate to **Artifact Registry** :
         
         gcloud auth configure-docker ${REGION}-docker.pkg.dev
         

  3. Push the Docker image you just built to the repository:
         
         docker push ${REGION}-docker.pkg.dev/${PROJECT_ID}/hello-repo/hello-app:v1
         




Now that the Docker image is stored in **Artifact Registry** , create a GKE cluster to run the hello-app, then deploy and expose an app.

Click **Next** to learn how to create a GKE cluster.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
