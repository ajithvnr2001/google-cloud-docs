---
url: https://docs.cloud.google.com/service-infrastructure/docs/manage-tenancy-units/
title: Managing Tenancy Units \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:58:19.235117+00:00
---

# Managing Tenancy Units  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/manage-tenancy-units/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Managing Tenancy Units Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to manage [tenancy units](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenancy) for your service. A [tenancy unit](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenancy) is a lightweight resource that represents the relationship between a [service consumer](https://docs.cloud.google.com/service-infrastructure/docs/glossary#consumer) and a [managed service](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed). Each service consumer can have only one active tenancy unit for a managed service. This is a feature provided by Service Infrastructure.

The resource name of a tenancy unit has the following format:
    
    
    services/{your service name}/projects/{consumer project number}/tenancyUnits/{id}
    

The ID of a tenancy unit is auto-generated when you create it. You can also provide an ID when you call the [`services.tenancyUnits.create`](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/create) method. If you provide an ID, it must be globally unique within the scope of your managed service across all service consumers.

The examples on this page use direct calls to the Service Consumer Management [REST API](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest). For production usage, we recommend you use Google-provided client libraries for better usability and reliability.

## Before you begin

  * The Service Consumer Management API is intended for use with [managed services](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed) and [service producer](https://docs.cloud.google.com/service-infrastructure/docs/glossary#producer) projects. You'll need to already have a Google Cloud project and a managed service (such as a service created using [Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs)) in that project.
  * To use tenancy units, the Service Consumer Management API needs to create tenant projects in your service producer organization. Make sure that you have enough quota for the necessary number of tenant projects for your service's consumers.
  * To create and delete tenancy units, follow the initial setup instructions in [Getting Started with the Service Consumer Management API](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/getting-started).
  * Each tenant project created in a tenancy unit must also be in a [folder](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders) that you specify as part of the tenant project configuration. Because of this, you need an [Organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization) to use tenancy units.



## Authentication

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

## Creating a tenancy unit

Tenancy units and the tenant projects in them are normally created when resources in your own service are created that depend on additional Google Cloud resources to be provisioned for the consumers.

You create a tenancy unit using the [`services.tenancyUnits.create` method](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/create):
    
    
    POST https://serviceconsumermanagement.googleapis.com/v1/services/service.example.com/projects/12345678901/tenancyUnits
    

Here, 'projects/12345678901' represents the service consumer, and `service.example.com` is the name of your service.

The returned data structure has the name of the tenancy unit, with a generated unique id that can be used to access it. In this example, the generated name is `services/your-service.example.com/projects/12345678901/tenancyUnits/absdef`.

## Adding a tenant project

You can now add a project for the user. To add a new tenant project to the tenancy unit created in the previous step, use the [`services.tenancyUnits.addProject` method](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/addProject):
    
    
    POST https://serviceconsumermanagement.googleapis.com/v1/services/your-service.example.com/projects/12345678901/tenancyUnits/absdef:addProject
    

with the following data:
    
    
    {"tag":"tag1", "project_config":{"folder":"folders/9876543210", "tenant_project_policy":{"policy_bindings":{"role":"roles/owner", "members":"user:bob@example.com"}}, "billing_config":{"billing_account":"billingAccounts/123456-472F22-28F9AA"}}}
    

The `tag` value is an identifier you provide for the project within the tenancy unit: this can be anything you like (here it's `tag1`), such as a region, a consumer network, or just a string ID.

This call returns a long running operation that you can query to find if the project creation was successful.

If you need to apply a different configuration, for example to add new managed services, you can call the [`services.tenancyUnits.applyProjectConfig`](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/applyProjectConfig) method.

## Searching your tenancy units

### Find a tenancy unit for a service consumer

To find a tenancy unit for a particular service consumer, use the [`services.tenancyUnits.list` method](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/list), specifying their service consumer project number:
    
    
    GET https://serviceconsumermanagement.googleapis.com/v1/services/your-service.example.com/projects/12345678901/tenancyUnits
    

### Search tenancy units

You can use the [`services.search` method](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services/search) to search for tenancy units defined for your service. For example, the following query will return all units that contain a project with the tag 'tag1':
    
    
    GET https://serviceconsumermanagement.googleapis.com/v1/services/your-service.example.com:search?query=tenant_resources.tag=tag1
    

## Cleaning up tenancy units

When a service consumer stops using your service, you need to remove its tenancy unit to free up resources and ensure the user data is deleted.

### Remove tenant projects

You need to delete all tenant projects before you delete the corresponding tenancy unit. You should use the [`services.tenancyUnits.removeProject`](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/removeProject) method to delete a tenant project and all resources in it:
    
    
    POST https://serviceconsumermanagement.googleapis.com/v1/services/your-service.example.com/projects/12345678901/tenancyUnits/absdef:removeProject
    

### Delete a tenancy unit

After you have deleted all tenant projects in a tenancy unit, or all of them are in the `DELETED` state, you can delete the tenancy unit using the [`services.tenancyUnits.delete` method](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/delete):
    
    
    DELETE https://serviceconsumermanagement.googleapis.com/v1/services/your-service.example.com/projects/12345678901/tenancyUnits/absdef
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
