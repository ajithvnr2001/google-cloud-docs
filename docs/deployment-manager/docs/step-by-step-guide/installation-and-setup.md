---
url: https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/installation-and-setup/
title: Installation and Setup \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:53.515150+00:00
---

# Installation and Setup  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/installation-and-setup/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Installation and Setup Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial goes through Deployment Manager using the `gcloud` command-line tool. Follow the setup steps to prepare your local environment to use Deployment Manager.

## Create a project

  1. In the Google Cloud console, go to the project selector page.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.



## Enable the APIs for the Google Cloud resources that you want to manage

Deployment Manager uses the APIs of other Google Cloud services to create and manage your resources. To create these resources, you must first enable the services' APIs for your project.

For this walkthrough, you deploy Compute Engine resources, so you need to enable the Compute Engine API.

[Enable the Compute Engine API](https://console.cloud.google.com/start/api?id=compute.googleapis.com)

Next, enable Deployment Manager: 

[Enable the Deployment Manager API](https://console.cloud.google.com/start/api?id=deploymentmanager)

## Install Google Cloud CLI

The Google Cloud CLI offers a command-line tool, `gcloud`, that makes interacting with Deployment Manager easy.

To install gcloud CLI:

  1. [Download and authenticate `gcloud`](https://cloud.google.com/sdk/#Quick_Start).

Alternatively, use [Cloud Shell](https://console.cloud.google.com/?cloudshell=true), which comes with `gcloud` already installed.

  2. Set your project ID.

Every command requires a project ID. Set a default project ID so you do not need to provide it every time. **Remember to replace`myproject` with your own project ID**.
         
         gcloud config set project myproject
         

  3. Set your default zone and region. Some Google Cloud resources require a zone or a region, and you can set a default zone or region, similar to a default project. To set a default zone or region, use `gcloud config set`. In this case, use `us-central1` as the region and `us-central1-f` as the zone:
         
         gcloud config set compute/region us-central1
         gcloud config set compute/zone us-central1-f
         




## Clone the Deployment Manager GitHub repository

The Deployment Manager GitHub repository contains samples created by Google and the Deployment Manager community, including the samples used in this walkthrough.
    
    
    git clone https://github.com/GoogleCloudPlatform/deploymentmanager-samples
    
    # open the samples folder
    cd deploymentmanager-samples/examples/v2/step_by_step_guide
    

Now that you have set up your environment, you can start creating your deployment.

[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide)

[ Next Understanding configurations  arrow_forward  ](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/create-a-configuration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
