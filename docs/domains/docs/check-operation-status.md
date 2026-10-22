---
url: https://docs.cloud.google.com/domains/docs/check-operation-status/
title: Check the status of management tasks \u00a0|\u00a0 Cloud Domains \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:54.286978+00:00
---

# Check the status of management tasks  |  Cloud Domains  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/domains/docs/check-operation-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Domains ](https://docs.cloud.google.com/domains/docs)
  * [ Guides ](https://docs.cloud.google.com/domains/docs/buy-register-domain)



Send feedback 

#  Check the status of management tasks Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** On September 7, 2023 Squarespace acquired all domain registrations and related customer accounts from Google Domains. For more information about how this change affects Cloud Domains, see [Cloud Domains feature deprecations](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations), [Renew an expired domain registration](https://support.google.com/a/answer/6152355), and [Squarespace purchase of Google Domains FAQ](https://docs.cloud.google.com/domains/docs/faq). 

This page explains how to check the status of long-running Cloud Domains operations. Checking the status of operations is useful if your operation gets interrupted for some reason.

The procedures in the following table use long-running operations.

`gcloud` commands | API methods  
---|---  
`register` | `register`  
`update` | `patch`  
`delete` | `delete`  
`configure contacts` | `configureContactSettings`  
`configure dns` | `configureDnsSettings`  
`configure management` | `configureManagementSettings`  
  
## Check operation status

To check the status of each operation, complete the following steps.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `domains.operations.get` to get (or wait for) a single operation
  * `domains.operations.list` to list operations



**Roles**

  * `roles/domains.viewer`
or 
  * `roles/domains.admin`



###  gcloud 

  * To list all the Cloud Domains operations in a project, use the [`gcloud domains registrations operations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/operations/list):
        
        gcloud domains registrations operations list
        

  * To get information about a Cloud Domains operation in a project, use the [`gcloud domains registrations operations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/operations/describe):
        
        gcloud domains registrations operations describe OPERATION_ID
        

Replace `OPERATION_ID` with the ID of the operation that you want to get information for.

  * To wait for a specified Cloud Domains operation to complete, use the [`gcloud domains registrations operations wait` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/operations/wait):
        
        gcloud domains registrations operations wait OPERATION_ID
        

Replace `OPERATION_ID` with the ID or fully qualified identifier for the operation that you want to wait to complete.




###  API 

  * To list all the Cloud Domains operations in a project, use the [`operations.list` method](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.operations/list) with an empty body:
        
        GET https://domains.googleapis.com/v1/projects/PROJECT_ID/locations/global/operations
        

Replace `PROJECT_ID` with the name of your project.

  * To get information about a Cloud Domains operation in a project, use the [`operations.get` method](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.operations/get) with an empty body:
        
        GET https://domains.googleapis.com/v1/projects/PROJECT_ID/locations/global/operations/OPERATION_ID
        

Replace the following:

    * `PROJECT_ID`: the name of your project
    * `OPERATION_ID`: the ID or fully qualified identifier for the operation that you want to get details for



## What's next

  * To view audit logs, see the [Cloud Domains audit logging information](https://docs.cloud.google.com/domains/docs/audit-logging).
  * To access API information, see the [Cloud Domains API](https://docs.cloud.google.com/domains/docs/reference/rest).
  * To find solutions for common issues that you might encounter when using Cloud Domains, see [Troubleshooting](https://docs.cloud.google.com/domains/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
