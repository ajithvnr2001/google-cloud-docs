---
url: https://docs.cloud.google.com/appengine/docs/flexible/run-flex-app-on-kubernetes/
title: Run App Engine apps on GKE \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:31:03.211736+00:00
---

# Run App Engine apps on GKE  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/run-flex-app-on-kubernetes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Run App Engine apps on GKE Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby .NET Custom

This guide shows you how to run an App Engine flexible environment app on GKE. To run your app on GKE, you need to create a Dockerfile for it, build a container with Cloud Build, and then run that container in GKE. No code changes are required.

## Before you begin

Before following the instructions on this page, take the following steps:

  1. Verify that your app deploys and runs successfully in the App Engine flexible environment.

  2. In these instructions, you'll use the same project that you used for your App Engine app. You can always create and use a new project, if you want.

  3. Enable the GKE, Cloud Build APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,cloudbuild.googleapis.com&redirect=https%3A//console.cloud.google.com)

  4. Download and install the Google Cloud CLI and then initialize the gcloud tool: [Download the Google Cloud SDK](https://docs.cloud.google.com/sdk/docs). 

Alternatively, you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell), which comes with the gcloud CLI, `git`, and other pre-installed [features](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works#tools), such as language support, tools, and editors. 

  5. Install the `kubectl` command-line tool:
         
         gcloud components install kubectl
         

  6. [Download and install git](https://git-scm.com/). 




## Creating a Dockerfile for your App Engine app

Build a Dockerfile for your app as described in [Create a Dockerfile](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build#docker).

## Building a container from the Dockerfile

To build a container:

  1. Ensure you are in the App Engine app directory that contains the Dockerfile.

  2. Change the default project used by the `gcloud` tool so it points to the project you are using to run your app in GKE:
         
         gcloud config set project [YOUR-PROJECT-ID]
         

Replace `[YOUR-PROJECT-ID]` with your GKE project ID.

  3. Build the container using the following command:
         
         gcloud builds submit --tag gcr.io/[YOUR-PROJECT-ID]/[YOUR-CONTAINER-NAME] .
         

Replace `[YOUR-PROJECT-ID]` with the project ID of your GKE project, and replace `[YOUR-CONTAINER-NAME]` with the name of the container you want to use for your app container.

  4. Wait for the container to build: it may take awhile. When it finishes successfully, it shows a message like this one:
         
         Created [https://cloudbuild.googleapis.com/v1/projects/YOUR-PROJECT-ID/builds/xxxxxxx-xxxx-xxx-xxx-xxxxxxxxxxxx].
         Logs are permanently available at [https://console.developers.google.com/logs/viewer?resource=build&project=YOUR-PROJECT-ID&filters=text:xxxx-xxx-xxx-xxxxxxxxxxxx]].
         
         ID  CREATE_TIME DURATION  SOURCE                                                     IMAGES                               STATUS
         xxxxxxx-xxxx-xxx-xxx-xxxxxxxxxxxx  2017-03-04T00:42:10+00:00  1M32S     gs://YOUR-PROJECT-ID_cloudbuild/source/xxxxxxx.08.tgz  gcr.io/YOUR-PROJECT-ID/YOUR-CONTAINER-NAME  SUCCESS<
         

Note the container name: you need to specify this when you run it in GKE.




## Running your app in GKE

To run the container that holds your app:

  1. Create the cluster (this may take a few minutes):
         
         gcloud container clusters create [YOUR-CLUSTER-NAME]
         

Replace `[YOUR-CLUSTER-NAME]` with the name you want to give the cluster.

  2. From the command line, set your compute zone:
         
         gcloud config set compute/zone us-central1-b
         

  3. Make sure the GKE `kubectl` tool is authorized:
         
         gcloud container clusters get-credentials [YOUR-CLUSTER-NAME]
         

Follow the prompts to authorize the tool.

  4. Run the container that holds your app:
         
         kubectl create deployment [YOUR-DEPLOYMENT-NAME] --image=gcr.io/[YOUR-PROJECT-ID]/[YOUR-CONTAINER-NAME]
         

Replace `[YOUR-DEPLOYMENT-NAME]` with the name you want to use for your deployment, replace `[YOUR-PROJECT-ID]` with your GKE project ID, and replace `[YOUR-CONTAINER-NAME]` with the name of the container you created for your app.

  5. Expose the container for public access:
         
         kubectl expose deployment [YOUR-DEPLOYMENT-NAME] --type="LoadBalancer" --port=8080
         

Replace `[YOUR-DEPLOYMENT-NAME]` with the name you used in the previous steps. You may need to wait several minutes before the external IP is viewable.

**Note:** The **type="LoadBalancer"** option in `kubectl` requests that Google Cloud Platform provision a load balancer for your container, which is billed per the regular Load Balancer pricing.
  6. View the external IP address for your app:
         
         kubectl get service [YOUR-DEPLOYMENT-NAME]
         

Replace `[YOUR-DEPLOYMENT-NAME]` with the name you used in the previous steps. If the `EXTERNAL IP` field is empty, wait for awhile, then re-invoke the command.

  7. View the app running in GKE:
         
         http://EXTERNAL-IP:8080
         

Replace `EXTERNAL-IP` with the external IP address you obtained in the previous step.




You've successfully deployed and run your App Engine app on GKE!

## What's next

You may want to learn more about Kubernetes and the `kubectl` command. Google Kubernetes Engine uses Kubernetes for container management, deployment and scaling. More information on Kubernetes is available on the external [Kubernetes site](http://kubernetes.io/).

This guide uses `kubectl`, the command line interface for managing Kubernetes clusters. More information on `kubectl` is available in the [kubectl reference](https://kubernetes.io/docs/reference/kubectl/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
