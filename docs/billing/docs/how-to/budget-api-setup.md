---
url: https://docs.cloud.google.com/billing/docs/how-to/budget-api-setup/
title: Cloud Billing Budget API Setup \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:08.078952+00:00
---

# Cloud Billing Budget API Setup  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/budget-api-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/billing/docs/apis)



Send feedback 

#  Cloud Billing Budget API Setup Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides all required setup steps to start using the Cloud Billing Budget API.

## Before you begin

You should do the following before reading this guide:

  1. Read [Cloud Billing Budget API Overview](https://docs.cloud.google.com/billing/docs/how-to/budget-api-overview).
  2. Read [Cloud Billing Budget API Prerequisites](https://docs.cloud.google.com/billing/docs/how-to/budget-api-prereqs).



## About the Google Cloud console

The Google Cloud console ([visit documentation](https://support.google.com/cloud/answer/3465889?hl=en&ref_topic=3340599), [open console](https://console.cloud.google.com/)) is a web UI used to provision, configure, manage, and monitor systems that use Google Cloud products. You use the Google Cloud console to set up and manage Google Cloud and Cloud Billing resources.

## 1\. Select or Create a project

To use services provided by Google Cloud, you must create a _project_. A project organizes all your Google Cloud resources. A project consists of a set of collaborators, enabled APIs (and other resources), monitoring tools, billing information, and authentication and access controls. You can create one project, or you can create multiple projects and use them to organize your Google Cloud resources in a [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). For more information on projects, see the [Resource Manager documentation](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

**Recommendation about projects** : We recommend that you create and use a separate Google Cloud project to contain all of your FinOps and billing administration needs for a Cloud Billing account, including your use of the Cloud Billing Budget API. [Learn more about the benefits to using a FinOps-focused project](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account#set-up-billing-project) for your billing administration use cases.

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

  * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
  * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 



[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

## 2\. Enable billing

You need to make sure that billing is enabled on the project you are using for calling the Cloud Billing Budget API. If you followed the recommendation in the project section, this is your _FinOps or billing administration_ Google Cloud project.

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

A Cloud Billing account is used to define who pays for a given set of Google Cloud resources. Resources, such as enabled APIs, are organized in projects. A Cloud Billing account can be linked to one or more projects. Project usage is charged to the linked billing account. In most cases, you configure billing when you create a project. For more information, see the [Cloud Billing documentation](https://docs.cloud.google.com/billing/docs/concepts).

#### Cost of use

You set up Cloud Billing budgets to monitor costs incurred in a Cloud Billing account. The Cloud Billing account you are monitoring can be the same Cloud Billing account that is linked to the project you use to call the Cloud Billing Budget API. Note that the Cloud Billing Budget API is [free to use](https://docs.cloud.google.com/billing/v1/pricing) for Google Cloud customers. If you choose to configure [programmatic budget notifications](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications), you will be charged the [standard Pub/Sub prices](https://cloud.google.com/pubsub/pricing).

## 3\. Enable the API

You must enable the Cloud Billing Budget API in the project you are using to call the Cloud Billing Budget API. If you followed the recommendation in the project section, this is your _FinOps or billing administration_ Google Cloud project.

For more information on enabling APIs, see the [Service Usage documentation](https://docs.cloud.google.com/service-usage/docs/enable-disable).

Enable the Cloud Billing Budget API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=billingbudgets.googleapis.com)

## 4\. Set up authentication and authorization

If you plan to use the Cloud Billing Budget API, you need to set up authentication. Any client application that uses the API must confirm its identity by authenticating. For details, see [Authenticate to Cloud Billing](https://docs.cloud.google.com/billing/docs/authentication).

You authenticate as a specific _principal_ , such as a Google Account or a service account. That principal must have Identity and Access Management (IAM) roles that contain the required permissions for the Cloud Billing Budget API.

To ensure that the principal has the necessary permissions to manage budgets, ask your administrator to grant the [Billing Account Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`) IAM role to the principal on your billing account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the principal the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To learn how to grant roles on a billing account, see [Update Cloud Billing permissions](https://docs.cloud.google.com/billing/docs/how-to/billing-access#update-cloud-billing-permissions).

## 5\. Install and initialize the gcloud CLI

If you plan to use the Cloud Billing Budget API, you need to install and initialize the Google Cloud CLI. Google Cloud CLI is a set of tools that you can use to manage resources and applications hosted on Google Cloud. This includes the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). The following link provides instructions:

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
    
    
    gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

## 6\. Test the SDK and authentication

If you have set up authentication in previous steps, you can use the gcloud CLI to test your authentication environment. Execute the following command to verify that no error occurs and that credentials are returned:
    
    
    gcloud auth print-access-token

That command is used by all Cloud Billing Budget API command line REST samples to authenticate API calls.

## 7\. Install the Cloud Billing Budget API client library

The Cloud Billing Budget API is built on HTTP and JSON, so any standard HTTP client can send requests to it and parse the responses.

You have three options for calling the API:

  * [Google supported client libraries](https://docs.cloud.google.com/billing/docs/reference/budget/libraries) (recommended)

Client libraries provide better language integration, improved security, and support for making calls that require user authorization. The Google supported client libraries are available for several popular languages, and these are the recommended option.

  * [REST](https://docs.cloud.google.com/billing/docs/reference/budget/rest)

  * [gRPC](https://docs.cloud.google.com/billing/docs/reference/budget/rpc)




[ Previous arrow_back  Prerequisites  ](https://docs.cloud.google.com/billing/docs/how-to/budget-api-prereqs)

[ Next Using the Budget API for alerts-only budgets  arrow_forward  ](https://docs.cloud.google.com/billing/docs/how-to/budget-api)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
