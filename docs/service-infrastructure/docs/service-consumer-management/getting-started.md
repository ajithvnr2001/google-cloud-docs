---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/getting-started/
title: Getting Started with the Service Consumer Management API \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:03.181507+00:00
---

# Getting Started with the Service Consumer Management API  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Getting Started with the Service Consumer Management API Stay organized with collections  Save and categorize content based on your preferences. 

The page describes the steps that need to be completed before you can start to use the Service Consumer Management API. It assumes that you already have a Google Cloud project and a [managed service](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed) (such as a managed service created using [Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs)) in that project, and that you understand [Tenancy Units](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenancy).

## Activating the service

While the Service Consumer Management API helps you to manage the usage of your own [managed services](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed), it is also a service itself. Therefore, before you can use it, you must activate the Service Consumer Management API for the Google Cloud project that hosts your managed service. This project is known as a [service producer](https://docs.cloud.google.com/service-infrastructure/docs/glossary#producer) project.

The simplest way to enable the Service Consumer Management API for your service producer project is to use the [Google Cloud console](https://console.cloud.google.com/apis/api/serviceconsumermanagement.googleapis.com). Alternatively, you can enable it from the command line or programmatically. You can find out more in [Enabling and Disabling Services](https://docs.cloud.google.com/service-usage/docs/enable-disable).

## Setting permissions

After the Service Consumer Management API is enabled for your service producer project, you must create your own service identity and grant it permissions on your resources so that it can create [tenant projects](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenant) in your folders and set up the correct billing account on tenant projects. These actions are executed by a service account owned by the Service Consumer Management API, which is specified in the following format:
    
    
    service-_PROJECT_NUMBER_ @service-consumer-management.iam.gserviceaccount.com
    

where _PROJECT_NUMBER_ is the project number for your service producer project that activated the Service Consumer Management service.

The remainder of this guide uses _GCM_SA_ to represent the Service Consumer Management API service account.

You can use the following commands to generate the service identity.

  1. Login with your user account.


    
    
    gcloud auth login
    

  1. Generate the service identity.


    
    
    gcloud beta services identity create --service=serviceconsumermanagement.googleapis.com --project=_PROJECT_ID_
    

### Setting folder permissions

  1. Ensure that you have a folder for holding your tenant projects: you'll need to have an [Organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization) to create folders within your service producer project. If you don’t have a folder, follow the instructions in [Creating and Managing Folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#create-folder) to create one. Your folder will have an integer based _FOLDER_ID_.

  2. On your folder, assign the **Project Creator/Deleter** role to the Service Consumer Management API service account. Follow the instructions in [Configuring Access to Folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#configuring_access_to_folders) to add the **Project Creator** and **Project Deleter** role, using _GCM_SA_ as the user.




### Setting billing account permissions

  1. Ensure that you have a billing account that can be shared for tenant projects. If you don't have a billing account, see [Create, Modify, or Close a Billing Account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account) for instructions to create one.

  2. Follow the [instructions](https://docs.cloud.google.com/billing/docs/how-to/billing-access) to add the **Billing Account User** role to _GCM_SA_.




## Resource requirements

  * The Service Consumer Management API creates [tenant projects](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenant) on your behalf, so ensure you have enough quota to create them.
  * See the [project limits](https://cloud.google.com/resource-manager/docs/limits#project-limits) documentation to know how many projects can be created by default and to request increases to that limit.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
