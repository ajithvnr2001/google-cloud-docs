---
url: https://docs.cloud.google.com/telecom-network-automation/docs/set-up-project/
title: Set up a project \u00a0|\u00a0 Telecom Network Automation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:45.214127+00:00
---

# Set up a project  |  Telecom Network Automation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/telecom-network-automation/docs/set-up-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Telecom Network Automation ](https://docs.cloud.google.com/telecom-network-automation/docs)
  * [ Guides ](https://docs.cloud.google.com/telecom-network-automation/docs/overview)



Send feedback 

#  Set up a project Stay organized with collections  Save and categorize content based on your preferences. 

Before you perform operations in Telecom Network Automation, you must set up a Google Cloud project. To set up a project, complete the following steps.

## Before you begin

Before continuing, ensure you have the following:

  * The latest version of the `gcloud` command line interface (CLI) tool. Do either of the following:

    * For full installation instructions, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install#linux).
    * Update your existing version using the following command:
          
          gcloud components update
          

  * Confirm you have version 1.25.8 of the `kubectl` CLI.

**Note:** Ensure you don't have the default `kubectl` version 1.26 or greater, as this version might not work with GDC clusters.
  * Have one or more GDC racks at target locations.

    * The software must run version 1.5.0. For more information, see [Installation requirements](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/requirements).



## Set up your Google Cloud project

Before you provision Telecom Network Automation, you must set up a Google Cloud project:

  1. Set your default project:
         
         gcloud config set project PROJECT_NAME
         

Replace PROJECT_NAME with a name for your project.

  2. In the default project, start the GKE compute endpoints:
         
         gcloud services enable compute.googleapis.com
         

  3. Assign the environment variables:
         
         export PROJECT_ID=$(gcloud config get-value project)
         export PROJECT_NUM=$(gcloud projects describe $PROJECT_ID
         --format="value(projectNumber)")
         export LOCATION=ZONE
         # create a /workdir to clone all repositories
         mkdir ~/workdir
         cd ~/workdir
         

Replace ZONE with the zone closest to your location, such as `us-central1-a`.

  4. Assign IAM roles to users in your organization to grant permission to your Google Cloud project:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID
         --member='user:EMAIL' --role='ROLE'
         

Replace the following:

     * EMAIL: the email of the user to bind the role to.
     * ROLE: the name of the role. For example, `roles/owner`. For a full list of Telecom Network Automation roles, see [Architecture and permissions](https://docs.cloud.google.com/telecom-network-automation/docs/permissions#roles-permissions).
  5. Enable Telecom Network Automation endpoints in the project:
         
         gcloud services enable telcoautomation.googleapis.com
         

  6. Set the default `gcloud` timeout:
         
         gcloud config set http_timeout 3600
         

  7. Resolve Telecom Network Automation deployments by granting the [Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging) role to the limited-access Telecom Network Automation monitoring group:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID
         --member=group:cloud-gmec-tna-monitoring-team@twosync.google.com --role=roles/logging.viewer
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
