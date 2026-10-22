---
url: https://docs.cloud.google.com/cortex/docs/prerequisites/
title: Prerequisites \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:51.272576+00:00
---

# Prerequisites  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/prerequisites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Prerequisites

This page guides you through the Cortex Framework deployment prerequisites. Take some time to configure each prerequisite before moving forward to the [Demo deployment](https://docs.cloud.google.com/cortex/docs/demo-deployment) or the [Production deployment](https://docs.cloud.google.com/cortex/docs/deployment).

## Installation artifacts

Clone the Google Cloud Cortex Framework repository: <https://github.com/GoogleCloudPlatform/cortex-framework>:
    
    
    git clone https://github.com/GoogleCloudPlatform/cortex-framework
    

Change directory to the folder where the repository has been cloned:
    
    
    cd DIRECTORY
    

## Install `uv`

[`uv`](https://docs.astral.sh/uv/) is an extremely fast Python package manager, written in Rust. Cortex Framework uses it to have consistent, isolated, and high-performance build deployment environments and to reduce time to install.

**Note:** If you are running this command from Cloud Shell, `uv` is already installed and you can skip the step of installation 

Install the manager package `uv` for Python virtual environments. Refer to [`uv` installation instructions](https://docs.astral.sh/uv/getting-started/installation/).

## Synchronize required dependencies

Execute the following command for synchronization of dependencies and for activation of a Python virtual environment:
    
    
    uv sync
    

## Configure Google Cloud SDK command line interface

**Note:** If you are executing `gcloud` commands for the first time in your local environment, or if you are getting authentication issues, use these commands to ensure authentication of Google Cloud SDK.
    
    
    gcloud auth login
    gcloud auth application-default login
    

## Prepare your Google Cloud project for Dataform hosting

Before running the deployment, you need to have access to a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#console) with an [attached billing account](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).

**Note:** This project is used as the default project for running `gcloud` commands and for hosting the Dataform repository. It is **not** automatically used as the target project in the Cortex Framework deployment itself. The deployment projects (such as build, source, and target projects) are configured separately in your deployment setup (for example, in the `config/config.yaml` file).

Next configure your Google Cloud CLI environment to point to your specific Google Cloud project.
    
    
    # Set current project and quota project
    gcloud config set project PROJECT_ID
    gcloud auth application-default set-quota-project PROJECT_ID
    

### Enable Google Cloud services

In this section we will enable the following Google Cloud services in your Google Cloud project:

  * BigQuery API
  * Dataform API
  * Cloud Resource Manager API



Enable these Google Cloud services using [Cloud Shell](https://shell.cloud.google.com/?fromcloudshell=true&show=ide%2Cterminal) by executing the following command in your terminal:

Replace `PROJECT_ID` with your project ID.
    
    
    gcloud config set project PROJECT_ID
    
    gcloud services enable cloudresourcemanager.googleapis.com \
                           bigquery.googleapis.com \
                           dataform.googleapis.com \
                           --project=PROJECT_ID
    

## Next steps

Ready to build and deploy? Explore the following guides to get your deployment up and running:

  * [Demo deployment](https://docs.cloud.google.com/cortex/docs/demo-deployment): Deploy sample data in a matter of minutes to see Cortex Framework in action.
  * [Production deployment](https://docs.cloud.google.com/cortex/docs/deployment): Follow step-by-step instructions to configure and deploy Cortex Framework for your enterprise data.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
