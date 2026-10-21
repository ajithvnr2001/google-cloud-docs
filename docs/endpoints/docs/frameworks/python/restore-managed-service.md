---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/restore-managed-service/
title: Restoring a managed service \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:21.671607+00:00
---

# Restoring a managed service  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/restore-managed-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Restoring a managed service Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Endpoints uses Service Management to manage your API. When you deployed your OpenAPI document by using the `gcloud endpoints services deploy` command, the command used Service Management to create a managed service for your API.

If you deleted a managed service by using the `gcloud endpoints services delete` command, Service Management doesn't immediately delete the managed service. Service Management disables the managed service for 30 days, which allows you time to restore it if you need to. After 30 days, Service Management permanently deletes the managed service.

While the managed service is in the disabled state, Service Management doesn't allow the creation of another managed service with the same name.

To restore a managed service:

  1. Make sure that the Google Cloud CLI (`gcloud`) is authorized to access your data and services on Google Cloud:
         
         gcloud auth login
         

  2. Restore the managed service and assign it to the Google Cloud project that it was originally created in. Replace `[SERVICE_NAME]` with the name of your managed service.
         
         gcloud endpoints services undelete [SERVICE_NAME]
         




## Troubleshooting

If the `gcloud endpoints services undelete` command fails with a permission error similar to: 
    
    
    ERROR: (gcloud.endpoints.services.undelete) User [EMAIL] does not have permission to access service
    

  * Run `gcloud auth login` and make sure to choose a user account that has permission to access the project that the managed service is in.

  * Make sure you have been granted the Service Management Administrator IAM role (`roles/servicemanagement.admin`).




## What's next

  * [Roles that control access to services](https://docs.cloud.google.com/endpoints/docs/frameworks/api-access-overview#roles_that_control_access_to_services).

  * [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant_access).

  * See the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference) for more information on the `gcloud` commands used on this page.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
