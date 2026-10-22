---
url: https://docs.cloud.google.com/cloud-assist/manage-investigations/
title: Manage Gemini Cloud Assist investigations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:30.393780+00:00
---

# Manage Gemini Cloud Assist investigations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/manage-investigations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Manage Gemini Cloud Assist investigations Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** As of April 10, 2026, creating, running, and editing investigations are only available to users that have a [Premium Support contract](https://cloud.google.com/support/premium) or who have requested access through their account team. If you ran an investigation prior to April 10, 2026, the results of the investigation continue to be available to you in the Google Cloud console.   
  
Use of this Preview offering of Gemini Cloud Assist is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/services?e=48754805), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview?e=48754805).

This page shows you how to review, modify, and delete existing [Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations).

## Before you begin

  1. In order to get the required permissions to work with existing investigations in a project, ask your administrator to grant you one of the following IAM roles:

     * If you want to view investigations, you should be granted the [Investigation Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.investigationViewer) (`roles/geminicloudassist.investigationViewer`) IAM role on the project.

     * If you want to modify investigations, you should be granted the [Investigation Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.investigationEditor) (`roles/geminicloudassist.investigationEditor`) IAM role on the project. This role also lets you view investigations.

     * If you want to delete investigations, you should be granted the [Investigation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.investigationAdmin) (`roles/geminicloudassist.investigationAdmin`) IAM role on the project. This role also lets you modify and view investigations.

To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

     * `geminicloudassist.investigations.get`
     * `geminicloudassist.investigations.list`
     * `geminicloudassist.investigationRevisions.get`
     * `geminicloudassist.investigationRevisions.list`
     * The following permissions are only required if you intend to modify an investigation: 
       * `geminicloudassist.investigationRevisions.create`
       * `geminicloudassist.investigationRevisions.run`
     * The following permission is only required if you intend to delete an investigation: 
       * `geminicloudassist.investigations.delete`

You might be able to get these permissions with other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) or [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

  2. Have one or more investigations associated with your project. See [Create an investigation](https://docs.cloud.google.com/cloud-assist/create-investigation) for steps to create an investigation.




## List and view investigations

To list and view investigations associated with your project that are in progress or complete, complete the following steps:

### Console

  1. Go to the **Investigations** page.

[Go to Cloud Assist investigations](https://console.cloud.google.com/troubleshooting/investigations/list)

The investigations page lists the available investigations and shows the status of each.

  2. Click the name of the investigation you want to review.

For more information about the content of an investigation, see [Review an investigation](https://docs.cloud.google.com/cloud-assist/create-investigation#review)

  3. If you have edited and re-run the investigation, you can review earlier analyses for the investigation by clicking the **Revision** drop-down and selecting the revision you want to review.




### API

  1. Obtain an access token:
         
         TOKEN=$(gcloud auth print-access-token)

  2. Use the [`investigations.list` method](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations/list) to list investigations associated with a project:
         
         curl -X GET \
           -H "Authorization: Bearer $TOKEN" \
           "https://geminicloudassist.googleapis.com/v1alpha/projects/PROJECT_NAME/locations/global/investigations"
         

Replace `PROJECT_NAME` with the name of the project whose investigations you want to list. For example, `my-project`.

  3. Use the [`investigations.get` method](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations/get) to get the details of a specific investigation:
         
         curl -X GET \
           -H "Authorization: Bearer $TOKEN" \
           "https://geminicloudassist.googleapis.com/v1alpha/projects/PROJECT_NAME/locations/global/investigations/INVESTIGATION_NAME"
         

Replace the following:

     * `PROJECT_NAME`: Enter the name of the project in which the investigation is stored. For example, `my-project`.

     * `INVESTIGATION_NAME`: Enter the string identifier of the investigation that you want to review. For example, `8622ceec-8204-4bcf-aa22-7166e674d429`.

  4. If you have edited and re-run the investigation, you can list the revisions associated with the investigation by using the [`investigationRevisions.list` method](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/list), and you can review the information for a specific revision by using the [`investigationRevisions.get` method](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/get),




## Modify an investigation

### Console

  1. Go to the **Investigations** page.

[Go to Cloud Assist investigations](https://console.cloud.google.com/troubleshooting/investigations/list)

The investigations page lists the available investigations and shows the status of each.

  2. Click the name of the investigation you want to modify.

The investigation details page opens.

  3. Click the **_edit_ Edit** button.

The edit investigation page opens.

  4. Modify the details of the investigation as wanted, such as changing the description of the issue, the time range of the issue, or the relevant resources associated with the issue.

  5. Click **Save and run**.

A new analysis occurs based on your updated information, and results appear in the investigation details page as they become available. It can take up to several minutes for the investigation to complete. If you leave the investigation's details page, you can check the status of the investigation by clicking the **Notifications** button (_notifications_).




**Note:** Even if you make no changes to an investigation, if you re-run it there can be minor differences in the output when compared to the original run. For more information, see [investigation considerations](https://docs.cloud.google.com/cloud-assist/investigations#considerations).

## Delete an investigation

**Note:** Investigations can't be deleted while they're running.

To delete an investigation associated with your project, complete the following steps:

### Console

  1. Go to the **Investigations** page.

[Go to Cloud Assist investigations](https://console.cloud.google.com/troubleshooting/investigations/list)

The investigations page lists the available investigations and shows the status of each.

  2. Toggle the checkbox associated with the investigation you want to delete.

  3. Click **Delete**.

  4. In the dialog that appears, confirm you want to delete the investigation by clicking **Delete**.




### API

  1. Obtain an access token:
         
         TOKEN=$(gcloud auth print-access-token)

  2. Use the [`investigations.delete` method](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations/delete) to delete the investigation:
         
         curl -X DELETE \
           -H "Authorization: Bearer $TOKEN" \
           "https://geminicloudassist.googleapis.com/v1alpha/projects/PROJECT_NAME/locations/global/investigations/INVESTIGATION_NAME"
         

Replace the following:

     * `PROJECT_NAME`: Enter the name of the project in which the investigation is stored. For example, `my-project`.

     * `INVESTIGATION_NAME`: Enter the string identifier of the investigation that you want to delete. For example, `8622ceec-8204-4bcf-aa22-7166e674d429`.




## What's next

  * Learn more about [investigations](https://docs.cloud.google.com/cloud-assist/investigations).
  * [Create a new investigation](https://docs.cloud.google.com/cloud-assist/create-investigation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
