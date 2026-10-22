---
url: https://docs.cloud.google.com/kms/docs/set-up-ekm-internet/
title: Set up Cloud EKM over the internet \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:06.297111+00:00
---

# Set up Cloud EKM over the internet  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/set-up-ekm-internet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Key Management Service ](https://docs.cloud.google.com/kms)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Set up Cloud EKM over the internet Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to use Cloud External Key Manager (Cloud EKM) to create and manage external keys accessed over the internet.

If you're migrating existing `EXTERNAL_VPC` keys to the `EXTERNAL` protection level, then you must complete these setup steps first.

## Before you begin

After you complete the steps below, you can begin using Cloud EKM keys to protect your data.

### Create a new project

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to Manage resources](https://console.cloud.google.com/project)

  2. Create a new Google Cloud project or select an existing project.

**Important:** The name you use must be between 4 and 30 characters. When you type the name, the form will suggest a project ID, which you can edit. The project ID you use must be between 6 and 30 characters, with a lowercase letter as the first character. You can use a dash, lowercase letter, or digit for the remaining characters, but the last character cannot be a dash. You should be aware that some resource identifiers (such as project IDs) might be retained beyond the life of your project. For this reason, avoid storing sensitive information in resource identifiers. ...see naming guidelines
  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

You can learn more about [Cloud EKM pricing](https://cloud.google.com/kms/pricing).




### Enable Cloud KMS

  1. Enable the Cloud Key Management Service API for the project.

[Enable the Cloud Key Management Service API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)

  2. Make a note of your project's Cloud EKM service account. In the following example, replace `PROJECT_NUMBER` with your Google Cloud project's [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). This information is also visible each time you use the Google Cloud console to create a Cloud EKM key.
         
         service-PROJECT_NUMBER@gcp-sa-ekms.iam.gserviceaccount.com
         




### Prepare the external key management partner system

In the external key management partner system, grant the Google Cloud service account access to use the external key. Treat the service account as an email address. Partners may use different terminology than that used in this document.

### Ensure gcloud CLI is up to date

If you're going to use the Google Cloud CLI, ensure that it's up-to-date with the following command:

###  gcloud 
    
    
    gcloud components update
    

## Troubleshooting errors

If you experience an error when creating or using a Cloud EKM key, an error is logged. For information about troubleshooting Cloud EKM errors, see the [Cloud EKM error reference](https://docs.cloud.google.com/kms/docs/reference/ekm_errors).

## What's next

  * [Create an external key](https://docs.cloud.google.com/kms/docs/create-external-key)
  * Optionally, [migrate external keys](https://docs.cloud.google.com/kms/docs/migrate-external-keys) between the `EXTERNAL` and `EXTERNAL_VPC` protection levels.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
