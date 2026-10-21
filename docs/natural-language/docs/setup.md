---
url: https://docs.cloud.google.com/natural-language/docs/setup/
title: Quickstart: Setup the Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:41:34.201394+00:00
---

# Quickstart: Setup the Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Guides ](https://docs.cloud.google.com/natural-language/docs/setup)



Send feedback 

#  Quickstart: Setup the Natural Language API Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides all required setup steps to start using Natural Language.

## About the Google Cloud console

The [Google Cloud console](https://support.google.com/cloud/answer/3465889?ref_topic=3340599), is a web UI used to provision, configure, manage, and monitor systems that use Google Cloud products. You use the Google Cloud console to set up and manage Natural Language resources.

## Create a project

To use services provided by Google Cloud, you must create a _project_.

A project organizes all your Google Cloud resources. A project consists of the following components:

  * a set of collaborators
  * enabled APIs (and other resources)
  * monitoring tools
  * billing information
  * authentication and access controls



You can create one project, or you can create multiple projects and use them to organize your Google Cloud resources in a [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). For more information on projects, see the [Resource Manager documentation](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

  * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
  * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 



[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

## Enable billing

A billing account is used to define who pays for a given set of resources, and it can be linked to one or more projects. Project usage is charged to the linked billing account. In most cases, you configure billing when you create a project. For more information, see the [Billing documentation](https://docs.cloud.google.com/billing/docs).

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

## Enable the API

You must enable the Cloud Natural Language API for your project. For more information on enabling APIs, see the [Service Usage documentation](https://docs.cloud.google.com/service-usage/docs/enable-disable).

Enable the Cloud Natural Language API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=language.googleapis.com)

## Install and initialize the gcloud CLI

If you plan to use the Natural Language API, you need to install and initialize the gcloud CLI. gcloud CLI is a set of tools that you can use to manage resources and applications hosted on Google Cloud. This includes the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). The following link provides instructions:

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
    
    
    gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

## Set up authentication

Any client application that uses the API must be authenticated and granted access to the requested resources. How you set up authentication depends on whether you are working in a local development environment or setting up a production environment. For more information, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

Select the tabs for how you plan to access the API:

### gcloud

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
    
    
    gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

### Client libraries

To use client libraries in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### REST

To use the REST API in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

For information about setting up authentication for a production environment, see [ Set up Application Default Credentials for code running on Google Cloud ](https://docs.cloud.google.com/docs/authentication/set-up-adc-attached-service-account) in the Google Cloud authentication documentation. 

## Install the Natural Language API client library

You have three options for calling the Natural Language API:

  * [Google supported client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries) (recommended)
  * [REST](https://docs.cloud.google.com/natural-language/docs/reference/rest)
  * [gRPC](https://docs.cloud.google.com/natural-language/docs/reference/rpc)



The client libraries are available for several popular languages. For information on installing the client libraries, see [Cloud Natural Language Client Libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries).

## IAM roles

To get the permissions that you need to access the Cloud Natural Language API, ask your administrator to grant you the [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) IAM role on your [quota project](https://docs.cloud.google.com/docs/quotas/quota-project#project-client-based). For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
