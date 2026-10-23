---
url: https://docs.cloud.google.com/service-infrastructure/docs/manage-tenant-projects/
title: Managing Tenant Projects \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:11.395760+00:00
---

# Managing Tenant Projects  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/manage-tenant-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Managing Tenant Projects Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create, remove, and delete [tenant projects](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenant).

You use the Service Consumer Management API to create and configure tenant projects, Google Cloud projects that are used to host your [managed service](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed) resources dedicated to a single [service consumer](https://docs.cloud.google.com/service-infrastructure/docs/glossary#consumer). Each tenant project is associated with a [tenancy unit](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenancy).

A tenancy unit can contain multiple tenant projects, each assigned a `tag: string` identifier that you can use to indicate the purpose of the project and to refer to it when deprovisioning.

After creation, a tenant project is just a Google Cloud project in your organization. You can use any management tools to work with it as you would normally use for Google Cloud project.

## Creating a tenant project

To create a tenant project and add it to a tenancy unit, call the [`services.tenancyUnits.addProject`](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/addProject) method.

The following example adds a new tenant project with the tag `tag1` to a tenancy unit using the REST API:
    
    
    POST https://serviceconsumermanagement.googleapis.com/v1/services/your-service.example.com/projects/12345678901/tenancyUnits/absdef:addProject
    

The call includes the following data:
    
    
    {"tag":"tag1", "project_config":{"folder":"folders/9876543210", "tenant_project_policy":{"policy_bindings":{"role":"roles/owner", "members":"user:bob@example.com"}}, "billing_config":{"billing_account":"billingAccounts/123456-472F22-28F9AA"}}}

This call returns a long running [operation](https://docs.cloud.google.com/service-infrastructure/docs/glossary#operation) that you can query to confirm the project creation was successful.

The new tenant project is configured with a project lien: a property set on the tenant project to prevent accidental deletion. You must call the [`services.tenancyUnits.removeProject`](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/removeProject) method to release the lien and delete the project. It is not recommended to bypass this protection.

The tenant project is created in the folder that you specified during [Setup and Configuration](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/getting-started). It is not recommended to move a project to a different folder after it is created.

The Service Consumer Management API service account is the creator and owner of tenant projects, in addition to any other owners that are specified in the tenant project configuration. It is not recommended to remove this account as an owner.

In some cases you might want to update an existing Google Cloud project to become a tenant project rather than create a new tenant project. To add an existing Google Cloud project to a tenancy unit, call the [`services.tenancyUnits.attachProject`](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/attachProject) method.

## Removing a tenant project

To remove a tenant project with the tag `abc`, call the [`services.tenancyUnits.removeProject`](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/removeProject) method as illustrated by the following example:
    
    
    POST https://serviceconsumermanagement.googleapis.com/v1/services/your-service.example.com/projects/12345678901/tenancyUnits/absdef:removeProject
    

The call includes the following data:
    
    
    {"tag":"abc"}

This operation removes the project lien, deletes the project and all resources in it, and deletes any associated metadata from the tenancy unit.

This deletes the project, and removes all metadata about it from the tenancy unit. If you wish to delete the project, but keep a record of it, call the [`services.tenancyUnits.deleteProject`](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/deleteProject) method instead. This method deletes the project and retains the metadata, annotating it with a state of `DELETED`. To undelete a deleted project, call the [`services.tenancyUnits.undeleteProject`](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/undeleteProject) method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
