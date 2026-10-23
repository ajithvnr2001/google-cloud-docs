---
url: https://docs.cloud.google.com/vision/docs/setup/
title: Cloud Vision setup and cleanup \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:24:47.276217+00:00
---

# Cloud Vision setup and cleanup  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/docs/features-list)



Send feedback 

#  Cloud Vision setup and cleanup Stay organized with collections  Save and categorize content based on your preferences. 

To start using Cloud Vision to get image information you need to complete several steps using the Google Cloud console and command line. This includes:

  * **General tasks:** Creating a Google Cloud project, enabling billing, installing the Google Cloud CLI, setting up authentication and access control, and performing cleanup after testing the product.
  * **Vision API-specific tasks:** Enabling the Vision API and installing its client libraries.



## About the Google Cloud Console

The Google Cloud Console ([visit documentation](https://support.google.com/cloud/answer/3465889?hl=en&ref_topic=3340599), [open console](https://console.cloud.google.com/)) is a web UI used to provision, configure, manage, and monitor systems that use Google Cloud products. You use the Google Cloud Console to set up and manage Vision resources. 

## Create a project

To use services provided by Google Cloud, you must create a _project_. A project organizes all your Google Cloud resources. A project consists of a set of collaborators, enabled APIs (and other resources), monitoring tools, billing information, and authentication and access controls. You can create one project, or you can create multiple projects and use them to organize your Google Cloud resources in a [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). When creating a project, take note of the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). You will need this ID to make API calls. For more information on projects, see the [Resource Manager documentation](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). 

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

  * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
  * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 



[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

## Enable billing

A billing account is used to define who pays for a given set of resources, and it can be linked to one or more projects. Project usage is charged to the linked billing account. In most cases, you configure billing when you create a project. For more information, see the [Billing documentation](https://docs.cloud.google.com/billing/docs). 

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

## Enable the API

You must enable the Vision API for your project. For more information on enabling APIs, see the [Service Usage documentation](https://docs.cloud.google.com/service-usage/docs/enable-disable). 

Enable the Vision API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=vision.googleapis.com)

## Install and initialize the Google Cloud CLI

If you plan to use the Vision API, you need to install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud). The gcloud CLI is a set of tools that you can use to manage resources and applications hosted on Google Cloud. 

The following link provides instructions: 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
    
    
    gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

## Set up authentication and access control

If you plan to use the Vision API, you need to set up authentication. Any client application that uses the API must be authenticated and granted access to the requested resources. This section describes important authentication concepts and provides steps for setting it up. For more information, see the [Google Cloud authentication overview](https://docs.cloud.google.com/docs/authentication). 

### Authentication with user accounts

_User accounts_ are the best authentication option when learning the Vision API and for local development. You can utilize your user account to authenticate for either REST command line executions or client library calls. 

#### REST command line user account authentication

**Note:** If you're using [Cloud Shell](https://docs.cloud.google.com/shell/docs), you are automatically logged in to gcloud, so you do not need to execute `gcloud auth login`. 

To authenticate for REST command line calls, you use the gcloud CLI. The [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command logs you in to gcloud with your user account, which should be done before calling the API. The [`gcloud auth print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token) command is used throughout the REST command line samples in this documentation to authenticate REST calls. 

To create user credentials for your local environment: 
    
    
    gcloud auth login

#### Client library user account authentication

To authenticate for client library calls, you use the gcloud CLI. The [`gcloud auth application-default login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login) command logs you in to gcloud for application default credentials with your user account, which should be done before calling the API. The [`gcloud auth application-default set-quota-project`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/set-quota-project) command must be used to set your project for billing and quotas related to API calls. Normally, this is the same project used by your agent, and you supply the project ID for the project you created in steps above. 

The `GOOGLE_APPLICATION_CREDENTIALS` environment variable must not be set in order for your application default credentials to be used by client libraries. 

To create application default credentials for your local environment: 
    
    
    gcloud auth application-default login
    gcloud auth application-default set-quota-project PROJECT_ID

### Authentication with service accounts

_Service accounts_ provide credentials for applications, as opposed to end-users. Service accounts are owned by projects, and you can create many service accounts for a project. For more information, see: 

  * [The service account overview](https://docs.cloud.google.com/iam/docs/service-accounts)
  * [Service account best practices](https://docs.cloud.google.com/iam/docs/understanding-service-accounts)
  * [Create and manage service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts)



### Access control with roles

When a principal (user account, service account, and so on) calls an API, Google Cloud requires that the principal has the appropriate permissions. You can grant permissions by granting _roles_ to a principal. For more information, see the [role overview](https://docs.cloud.google.com/iam/docs/understanding-roles). 

If you have created your project with your user account, your user account has the [Owner basic role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) for the project. This role provides access to call any API for the project. However, if a different account created the project, you may need to have roles granted to your user account before you can call the API. 

## Install the Vision API client library

You have three options for calling the Vision API:

  * [Google supported client libraries](https://docs.cloud.google.com/vision/docs/libraries) (recommended)
  * [REST](https://docs.cloud.google.com/vision/docs/reference/rest)
  * [gRPC](https://docs.cloud.google.com/vision/docs/reference/rpc)



The client libraries are available for several popular languages. For information about installing the client libraries, see [Vision API client libraries](https://docs.cloud.google.com/vision/docs/reference/libraries).

## Cleanup

After setup and trying or testing Vision, you may want to delete resources you created: 

  * You may want to [shutdown your project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects). 
  * If you called `gcloud auth login`, this stores credentials in your user directory on your computer. You may want to delete these credentials by calling: 
        
        gcloud auth revoke

  * If you called `gcloud auth application-default login`, this stores credentials in your user directory on your computer. You may want to delete these credentials by calling: 
        
        gcloud auth application-default revoke




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
