---
url: https://docs.cloud.google.com/fault-injection-testing/access-control/
title: Manage Fault Injection Testing access \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:57.851074+00:00
---

# Manage Fault Injection Testing access  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/access-control/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Guides ](https://docs.cloud.google.com/fault-injection-testing/overview)



Send feedback 

#  Manage Fault Injection Testing access Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to use [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) to manage access to Fault Injection Testing features.

[Admins or Owners](https://docs.cloud.google.com/iam/docs/roles-overview#basic) for your Google Cloud resources can grant Fault Injection Testing roles and permissions.

Admins are responsible to ensure users have the access they need and nothing more (principle of least privilege). Because Fault Injection Testing requires accounts to both configure and run experiments, least privilege is especially important – fault experimentation can cause unexpected outages if run on incorrect resources, or operated by unauthorized or untrained users.

## Enable the APIs for Fault Injection Testing

To activate the Fault Injection Testing API for your project:

  1. Go to the API Library page for the [Google Cloud console](https://console.cloud.google.com/).
  2. Search for **faulttesting** and select the **Fault Testing API**.
  3. Select the **Enable** button.



A dialog showing the progress of the API activation appears.

## Set required permissions

Fault Injection Testing provides the following roles:

Role name | Description | Permissions  
---|---|---  
`roles/faulttesting.operator`Fault Testing Admin/Operator | Full access to fault testing resources. Operators must also have editor permissions to the affected Google Cloud resources. | `faulttesting.googleapis.com/operations.delete``faulttesting.googleapis.com/operations.cancel``faulttesting.googleapis.com/experiments.create``faulttesting.googleapis.com/experiments.update``faulttesting.googleapis.com/experiments.delete``faulttesting.googleapis.com/validations.create``faulttesting.googleapis.com/validations.delete``faulttesting.googleapis.com/validationResources.create``faulttesting.googleapis.com/validationResources.update``faulttesting.googleapis.com/validationResources.delete``faulttesting.googleapis.com/affectedResources.create``faulttesting.googleapis.com/affectedResources.update``faulttesting.googleapis.com/affectedResources.delete``faulttesting.googleapis.com/experimentTemplates.create``faulttesting.googleapis.com/experimentTemplates.update``faulttesting.googleapis.com/experimentTemplates.delete``faulttesting.googleapis.com/exclusionWindows.create``faulttesting.googleapis.com/exclusionWindows.update``faulttesting.googleapis.com/exclusionWindows.delete``cloudresourcemanager.googleapis.com/projects.get``cloudresourcemanager.googleapis.com/projects.list``faulttesting.googleapis.com/operations.list``faulttesting.googleapis.com/operations.get``faulttesting.googleapis.com/locations.list``faulttesting.googleapis.com/locations.get``faulttesting.googleapis.com/experiments.list``faulttesting.googleapis.com/experiments.get``faulttesting.googleapis.com/validations.list``faulttesting.googleapis.com/validations.get``faulttesting.googleapis.com/validationResources.list``faulttesting.googleapis.com/validationResources.get``faulttesting.googleapis.com/affectedResources.list``faulttesting.googleapis.com/affectedResources.get``faulttesting.googleapis.com/experimentTemplates.list``faulttesting.googleapis.com/experimentTemplates.get``faulttesting.googleapis.com/exclusionWindows.list``faulttesting.googleapis.com/exclusionWindows.get`  
`roles/faulttesting.viewer`Fault Testing Viewer | Read-only access to fault testing resources. | `cloudresourcemanager.googleapis.com/projects.get``cloudresourcemanager.googleapis.com/projects.list``faulttesting.googleapis.com/operations.list``faulttesting.googleapis.com/operations.get``faulttesting.googleapis.com/locations.list``faulttesting.googleapis.com/locations.get``faulttesting.googleapis.com/experiments.list``faulttesting.googleapis.com/experiments.get``faulttesting.googleapis.com/validations.list``faulttesting.googleapis.com/validations.get``faulttesting.googleapis.com/validationResources.list``faulttesting.googleapis.com/validationResources.get``faulttesting.googleapis.com/affectedResources.list``faulttesting.googleapis.com/affectedResources.get``faulttesting.googleapis.com/experimentTemplates.list``faulttesting.googleapis.com/experimentTemplates.get``faulttesting.googleapis.com/exclusionWindows.list``faulttesting.googleapis.com/exclusionWindows.get`  
  
Use the Google Cloud CLI to grant roles and permissions. To grant the `faulttesting.operator role`, run the following command:
    
    
    gcloud projects add-iam-policy-binding ${PROJECT_ID} \
      --member {USER|GROUP|SERVICE_ACCOUNT} \
      --role roles/faulttesting.operator
    

An example of the syntax for adding `faulttesting.operator` to user `anon@example.com in project`example-project` would look like this:
    
    
    gcloud projects add-iam-policy-binding example-project --member=user:anon@example.com --role=roles/faulttesting.operator
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
