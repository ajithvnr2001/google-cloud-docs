---
url: https://docs.cloud.google.com/oracle/database/docs/set-up/
title: Set up gcloud CLI and enable the API \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:26:10.326037+00:00
---

# Set up gcloud CLI and enable the API  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/set-up/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Set up gcloud CLI and enable the API Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up a project. You need a project before you can create resources for Oracle Database@Google Cloud.

In order to create resources using Oracle Database@Google Cloud, you must have an active marketplace order on the same billing account that you want to create resources on and have the Oracle Database@Google Cloud API enabled. This guide walks you through how to set up your project.

## Before you begin

  * Confirm that you have an active marketplace order and that your Oracle Cloud Infrastructure (OCI) account is linked to the order. If you don't have an active order, [Place an order](https://docs.cloud.google.com/oracle/database/docs/overview#place-an-order) for more information.

  * [Install Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk) on your development machine.




## Set up a Google Cloud project

To install Google Cloud CLI on your Google Cloud project and to enable the Oracle Database@Google Cloud API, complete the following steps:

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

**Important:** The name you use must be between 4 and 30 characters. When you type the name, the form will suggest a project ID, which you can edit. The project ID you use must be between 6 and 30 characters, with a lowercase letter as the first character. You can use a dash, lowercase letter, or digit for the remaining characters, but the last character cannot be a dash. You should be aware that some resource identifiers (such as project IDs) might be retained beyond the life of your project. For this reason, avoid storing sensitive information in resource identifiers. ...see naming guidelines
  2. Open a terminal window, and set your project as the default project for the Google Cloud CLI using the following command:
         
         gcloud config set project 'MY_PROJECT_ID'
         

Replace the following:

     * `MY_PROJECT_ID`: the ID of your project (not the project name)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

This project must match the project that your Oracle Database@Google Cloud order is linked to. 
  4. Enable the Oracle Database@Google Cloud API for the project. 

[Enable the Oracle Database@Google Cloud API](https://console.cloud.google.com/apis/enableflow?apiid=oracledatabase.googleapis.com)




## What's next

  * Learn how to [create](https://docs.cloud.google.com/oracle/database/docs/create-instances) an instance.
  * Configure [Identity and Access Management roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles) for an instance. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
