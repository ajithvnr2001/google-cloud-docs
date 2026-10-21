---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started/
title: Getting Started with the Service Control API \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:09:34.810012+00:00
---

# Getting Started with the Service Control API  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Getting Started with the Service Control API Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the basic steps necessary to set up the Service Control API on your local machine and test it using the `curl` command.

## Initial setup

The Service Control API works with [managed services](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed). To use the Service Control API, you need to first create a managed service using the Service Management API. For more information, see [Service Management Getting Started](https://docs.cloud.google.com/service-infrastructure/docs/service-management/getting-started).

After you have created a managed service, you need to complete the following steps before using the Service Control API from your managed service.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Service Control API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable servicecontrol.googleapis.com

  8. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/servicemanagement.serviceController`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the Service Control API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable servicecontrol.googleapis.com

  15. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/servicemanagement.serviceController`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.




## Test with curl

First, define a convenient shell alias for calling Google REST APIs:
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" '
    

The following shell command sequence demonstrates the incremental steps to call the Service Control API.
    
    
    # Call with invalid service name "invalid.com". For security and privacy
    # reasons, the permission check typically happens before other checks.
    $ gcurl -d '{}' https://servicecontrol.googleapis.com/v1/services/invalid.com:check
    {
      "error": {
        "code": 403,
        "message": "Permission 'servicemanagement.services.check' denied on service 'invalid.com'.",
        "status": "PERMISSION_DENIED"
      }
    }
    
    # Call without proper permission on a service.
    $ gcurl -d '{}' https://servicecontrol.googleapis.com/v1/services/servicecontrol.googleapis.com:check
    {
      "error": {
        "code": 403,
        "message": "Permission 'servicemanagement.services.check' denied on service 'servicecontrol.googleapis.com'.",
        "status": "PERMISSION_DENIED"
      }
    }
    
    # Call with invalid request.
    $ gcurl -d '{}' https://servicecontrol.googleapis.com/v1/services/endpointsapis.appspot.com:check
    {
      "error": {
        "code": 400,
        "message": "Request contains an invalid argument.",
        "status": "INVALID_ARGUMENT"
      }
    }
    
    # This and following call assume that the service, operation name and
    # project being checked are "endpointsapis.appspot.com",
    # "google.example.hello.v1.HelloService.GetHello" and
    # "endpointsapis-consumer" correspondingly.
    # Change to the name of your managed service, operation, and project.
    # Call with invalid request.
    $ gcurl -d '{
      "operation": {
        "operationId": "123e4567-e89b-12d3-a456-426655440000",
        "consumerId": "project:endpointsapis-consumer",
        "startTime": "2016-06-12T22:00:15Z",
        "operationName": "google.example.hello.v1.HelloService.GetHello"
      }
    }' https://servicecontrol.googleapis.com/v1/services/endpointsapis.appspot.com:check
    {
      "checkErrors": [
      {
        "code": "SERVICE_NOT_ACTIVATED",
        "detail": "Service 'endpointsapis.appspot.com' is not enabled for consumer 'project:endpointsapis-consumer'."
      }
      ]
    }
    
    # Successful call to "services.check" method after the API is enabled for
    # the project.
    $ gcurl -d '{
      "operation": {
        "operationId": "123e4567-e89b-12d3-a456-426655440000",
        "consumerId": "project:endpointsapis-consumer",
        "startTime":"2016-07-31T05:20:00Z",
        "operationName":"google.example.hello.v1.HelloService.GetHello"
      }
    }' https://servicecontrol.googleapis.com/v1/services/endpointsapis.appspot.com:check
    {
      "operationId": "123e4567-e89b-12d3-a456-426655440000"
    }
    

After you have completed the preceding steps:

  * You have a functional local test setup that you can use to call any Google Cloud Platform APIs.
  * You have a functional service that you can use with the [Service Management API](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest) and the [Service Control API](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest).
  * You have a service account with correct permissions that you can use to run your service.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
