---
url: https://docs.cloud.google.com/secure-source-manager/docs/delete-instance/
title: Delete an instance \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:55.878796+00:00
---

# Delete an instance  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/delete-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Delete an instance Stay organized with collections  Save and categorize content based on your preferences. 

## Required Roles

To get the permissions that you need to delete an instance, ask your administrator to grant you the [Secure Source Manager Instance Manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`) IAM role on the Secure Source Manager instance. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## Delete an instance

  1. To delete your Secure Source Manager instance and all associated data, run the following command:
         
         gcloud source-manager instances delete INSTANCE_NAME \
             --region=REGION
         

Replace the following:

     * `INSTANCE_NAME` with the name of the instance you want to delete.
     * `REGION` with the location of your instance. For information on supported locations, see [Locations](https://docs.cloud.google.com/secure-source-manager/docs/locations).
  2. Check the status of the operation with the following command:
         
         gcloud source-manager operations describe projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID
         

Where `OPERATION_ID` is the value of `name:` in the response from the `delete` command.




## What's next

  * [Disable the Secure Source Manager API](https://docs.cloud.google.com/secure-source-manager/docs/enable-disable#disable).
  * [List and view instances](https://docs.cloud.google.com/secure-source-manager/docs/list-view-instances).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
