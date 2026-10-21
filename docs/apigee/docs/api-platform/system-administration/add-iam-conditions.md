---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/add-iam-conditions/
title: Adding Apigee IAM Conditions to policies \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:38:57.051773+00:00
---

# Adding Apigee IAM Conditions to policies  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/add-iam-conditions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Adding Apigee IAM Conditions to policies Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to add IAM Conditions to your Apigee resources. An IAM Condition lets you have granular control over your Apigee resources.

## Before you begin

Apigee uses Google Cloud's [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) to manage roles and permissions for Apigee's resources. Therefore, before you specify or modify conditions in IAM for your Apigee resources, familiarize yourself with the following IAM concepts:

  * [Resource](https://docs.cloud.google.com/iam/docs/overview#resource)
  * [Resource hierarchy](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control)
  * [Roles](https://docs.cloud.google.com/iam/docs/understanding-roles)
  * [Custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles)
  * [Permissions](https://docs.cloud.google.com/iam/docs/overview#permissions)
  * [Parent-only permissions](https://docs.cloud.google.com/iam/docs/configuring-resource-based-access#parent-only)



## Adding IAM Conditions

To add an IAM condition to an Apigee resource, you need the following information:

  * **Named Resource URI** \- Every resource in Apigee has a unique resource URI. For example, URI for the API products resource is `organizations/{org}/apiproducts/{apiproduct}`. For the complete list of all the available URIs, see [Apigee REST resources](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest). To control access permissions for a resource at a granular level, you must name your resource according to a naming convention. Based on your requirements, you can decide on what naming convention you want to follow. For example, you can prefix the word `marketing` for all API products owned by the marketing team. In this example, the resource URI for the marketing team's API products, will begin with `organizations/{org}/apiproducts/marketing-`. 
  * **Parent only permissions** \- Check if a resource or any of its child resource(s) require the parent-only permission. For more information, see [Parent-only permissions](https://docs.cloud.google.com/iam/docs/configuring-resource-based-access#parent-only). 
  * **Resource type** \- You can further narrow the scope of resources, by filtering for a resource type in the condition. Apigee supports conditions for the following resources: Resource name | Resource type  
---|---  
API proxy | [apigee.googleapis.com/Proxy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis)  
API proxy revision | [apigee.googleapis.com/ProxyRevision](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.revisions)  
API proxy key-value map | [apigee.googleapis.com/KeyValueMap](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps)  
API product | [apigee.googleapis.com/ApiProduct](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts)  
API product attributes | [apigee.googleapis.com/ApiProductAttribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes)  
Developer | [apigee.googleapis.com/Developer](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers)  
Developer attributes | [apigee.googleapis.com/DeveloperAttribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.attributes)  
Developer app | [apigee.googleapis.com/DeveloperApp](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps)  
Developer app attributes | [apigee.googleapis.com/DeveloperAppAttribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.attributes)  
Key value entries (API proxy scope) | [apigee.googleapis.com/KeyValueEntry](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps.entries)  
Rate plan | [apigee.googleapis.com/RatePlan](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans)  
SharedFlow | [apigee.googleapis.com/SharedFlow](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows)  
SharedFlow revision | [apigee.googleapis.com/SharedFlowRevision](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.sharedflows.revisions)  



## Examples

The table lists a few sample resource conditions and the corresponding permissions:

Condition  | Description   
---|---  
`resource.name.startsWith("organizations/{org-name}/apis/catalog-") || resource.type == "cloudresourcemanager.googleapis.com/Project" ` | This condition provides the following permissions:

  * List all proxies
  * Get, Create, Update, and Delete operations on API proxies whose name starts with `catalog-`.
  * All operations on the `Revision` and `KeyValueMap` resources belonging to the `catalog-*` API proxies.

  
`(resource.name.startsWith("organizations/{org-name}/apis/catalog-proxy/keyvaluemaps") && resource.type == "apigee.googleapis.com/KeyValueMap") || resource.type == "cloudresourcemanager.googleapis.com/Project"` | This condition provides permissions for Get, Create, Update, and Delete operations on KeyValueMaps in the `catalog-proxy` API proxy.  
`resource.type == "apigee.googleapis.com/Proxy" || resource.type == "cloudresourcemanager.googleapis.com/Project"` | This condition provides permissions for List, Get, Create, Update, and Delete operations on all API proxies.  
**Note:** For all your resource conditions, you must include the following condition so that the Apigee UI can enforce the IAM conditions properly:  
`resource.type == "cloudresourcemanager.googleapis.com/Project"` **Note:** Users must have following additional permissions to view proxy deployments in the UI when providing fine-grained access for particular business unit or teams based on conditions: 

  * `apigee.deployments.get`
  * `apigee.deployments.list`
  * `apigee.environments.get`
  * `apigee.environments.list`



## What's next

Go through the following information in the IAM documentation:

  * [Adding a conditional role binding to a policy](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#add)
  * [Modify an existing conditional role binding](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#modify)
  * [Removing a conditional role binding](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#removing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
