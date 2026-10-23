---
url: https://docs.cloud.google.com/shell/docs/run-gcloud-commands/
title: Quickstart: Run gcloud commands with Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:46:41.052410+00:00
---

# Quickstart: Run gcloud commands with Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/run-gcloud-commands/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run `gcloud` commands with Cloud Shell

Learn how to run gcloud CLI commands in Cloud Shell.

* * *

To follow step-by-step guidance for this task directly in the Cloud Shell Editor, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/?walkthrough_id=sdk--cloud-cli-quickstart)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




## Set `gcloud` properties

  1. [Launch the Cloud Shell Editor](https://ide.cloud.google.com).
  2. Prevent color from being used when printing messages to the terminal by setting a core property:
         
         gcloud config set disable_color true
         

  3. Unset the `disable_color` property:
         
         gcloud config unset disable_color
         

  4. If you have the Compute Engine API enabled, set your preferred Compute Engine region. Replace `REGION` with a region name—for example, `us-east1`:
         
         gcloud config set compute/region REGION
         

Alternatively, you can set your preferred zone. Replace `ZONE` with a zone name—for example, `us-east1-b`:
         
         gcloud config set compute/zone ZONE
         

For information about Compute Engine regions and zones, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).

  5. Display a list of available properties:
         
         gcloud topic configurations
         




## Run core commands

  1. List accounts whose credentials are stored on the local system:
         
         gcloud auth list
         

The gcloud CLI displays a list of credentialed accounts, where `ACCOUNT_EMAIL` represents a list of one or more active accounts:
         
         Credentialed Accounts
         ACTIVE  ACCOUNT
         \*      ACCOUNT_EMAIL
         

  2. List the properties in your active gcloud CLI configuration:
         
         gcloud config list
         

The gcloud CLI displays the list of properties similar to the following, where `ACCOUNT_EMAIL` and `PROJECT_ID` display your email and project ID:
         
         [core]
         account = ACCOUNT_EMAIL
         disable_usage_reporting = False
         project = PROJECT_ID
         

  3. View information about your gcloud CLI installation and the active configuration:
         
         gcloud info
         




## View help for `gcloud` commands

  1. View the help for the `gcloud compute instances create` command:
         
         gcloud help compute instances create
         

  2. View available commands under `gcloud topic`:
         
         gcloud help topic
         

  3. View information on filtering:
         
         gcloud topic filters
         

  4. Learn more about `gcloud` command structure:
         
         gcloud topic command-conventions
         




## What's next

  * Learn [how Cloud Shell works](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works).
  * [Deploy a Cloud Run app by using Cloud Shell](https://docs.cloud.google.com/shell/docs/deploy-cloud-run-app).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
