---
url: https://docs.cloud.google.com/spectrum-access-system/docs/create-new-deployments/
title: Create new deployments \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:12.988943+00:00
---

# Create new deployments  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/create-new-deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Create new deployments Stay organized with collections  Save and categorize content based on your preferences. 

You can provision the SAS service for additional deployments using the Google Cloud CLI. You can create a deployment in a new or existing SAS organization.

## Before you begin

Each SAS deployment can only be associated with a single Google Cloud project. If you have not already done som you must create a new Google Cloud project in which you then create a SAS deployment. For more information, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). Record the project ID of your new project - it is required to complete the steps in this guide.

The project must be linked to a billing account. For more information, see [Enable billing for a new project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_new_project).

**Note:** The project ID of the Google Cloud project used for provisioning becomes the default user ID of your first SAS deployment. Once you have registered CBSDs with SAS using a specific user ID, you cannot change that user ID without re-registering the devices to a new deployment.

### Update the Google Cloud CLI

  1. Go to the Google Cloud console.

  2. If you haven't installed the Google Cloud CLI, follow the instructions at [Initializing the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/initialize) to install it from the Google Cloud console.

  3. Update the Google Cloud CLI and get access to the Google SAS toolset:
         
         gcloud components update
         




## Create a new deployment in a new SAS organization

To create a new deployment in a new SAS organization, complete the steps in this section.

  1. Use the following command to set the target Google Cloud project as the active project:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the Google Cloud project ID of the project you created earlier in this guide.

  2. Provision your new deployment:
         
         gcloud alpha cbrs-spectrum-access provision \
             --organization-name="ORGANIZATION_NAME"
         

     * Replace ORGANIZATION_NAME with the name of your SAS organization as you want to appear in the SAS Portal. ORGANIZATION_NAME can include spaces, lowercase or uppercase letters, numbers, and punctuation.
  3. Follow the prompts that appear to enable the SAS Portal API on the project and create a new deployment in your SAS organization.

     1. If provisioning is successful, you see the following output:
            
            A new SAS deployment with userID: PROJECT_ID has been created. Go to g.co/sasportal to check
             spectrum availability, pre-register CBSDs, check
             CBSD status and manage users.
            

     2. If you see the message `You do not currently have this command group installed`, follow the prompts to install the missing components.

     3. If you see the message `ERROR: (gcloud.alpha) Invalid choice: 'cbrs-spectrum-access'` run `gcloud components update` and follow the prompts to install the updates and try again.

     4. If you see the message `FAILED_PRECONDITION: The project does not have a billing account associated with it.` see [How to enable billing on an existing project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#how-to-enable-billing) to enable billing for your SAS project.

     5. If you see the message `ALREADY_EXISTS: Your project id PROJECT_ID matches a user id already present in our system. Please create a new project with a different ID.`, do the following:

        * If you are a new customer, go return to Step 2 to create a new project with a different project ID and proceed.
        * If your Google Cloud administrator created the project for you, ask them to create a new project for SAS and grant you access as described in the Before you begin section. Return to Step 3 and proceed.



You are finished! Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas) to [add users](https://docs.cloud.google.com/spectrum-access-system/docs/users-sasportal), [create CBSD configurations](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/configure), and [view the status of your CBRS network](https://docs.cloud.google.com/spectrum-access-system/docs/portal#analyze-status).

## Create a new deployment in an existing SAS organization

Complete the steps in this section to retrieve your existing SAS organization ID, and provision the SAS service for a new deployment in your existing SAS organization.

### Retrieve your SAS organization ID

  1. Retrieve your SAS Portal organization ID.

     1. Go to the [Google SAS Portal](https://wirelessconnectivity.google.com/sas)

     2. Select **View deployments**.

     3. In the page that appears, click the name of the target SAS organization.

     4. Click **Open**.

     5. Retrieve your SAS organization ID from the URL. The organization ID is the number that follows the `org/` string. For example:

![Locate your SAS organization ID within the URL.](https://docs.cloud.google.com/static/spectrum-access-system/docs/images/retrieve-sas-portal-org-id-location.png)




### Provision your new SAS deployment

  1. Use the following command to set the target Google Cloud project as the active project:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the Google Cloud project ID of the project you created earlier in this guide.

  2. Provision your new deployment under the target SAS organization:
         
         gcloud alpha cbrs-spectrum-access provision \
         --organization-id=SAS_ORGANIZATION_ID
         

Replace `SAS_ORGANIZATION_ID` with the Portal organization ID that you retrieved earlier.

  3. Follow the prompts that appear to enable the SAS Portal API on the project and complete the provisioning of your deployment.




You are finished! Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas) to [add users](https://docs.cloud.google.com/spectrum-access-system/docs/users-sasportal), [create CBSD configurations](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/configure), and [view the status of your CBRS network](https://docs.cloud.google.com/spectrum-access-system/docs/portal#analyze-status).

## What's next

  * Learn about [Citizens Broadband Radio Service Devices (CBSDs)](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview).
  * Preruse product videos and training sessions at [SAS YouTube channel](https://www.youtube.com/channel/UCPRC_4Oip3BfdjHvMXNU4MQ/videos).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
