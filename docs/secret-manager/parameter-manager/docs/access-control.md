---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:09:43.922757+00:00
---

# Access control with IAM  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Identity and Access Management (IAM) roles for Parameter Manager users. Each IAM role has associated permissions. These permissions define the level of access that the member receives for resources. Grant the minimum set of permissions that are required to perform a given task.

You can control access to parameters by granting permissions at the project level. These permissions allow users or service accounts to create, manage, list, or access parameters. You can't grant IAM roles at a resource level for Parameter Manager.

To learn how to assign IAM roles to a user or service account, read [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the IAM documentation.

### Roles and permissions

The following table lists the necessary IAM roles and their permissions for Parameter Manager:

Role Name | Role Description | Permissions  
---|---|---  
Parameter Manager Admin  
(`roles/parametermanager.admin`) | Full access to all Parameter Manager resources. | resourcemanager.projects.get  
resourcemanager.projects.list  
parametermanager.*  
Parameter Manager Parameter Accessor  
(`roles/parametermanager.parameterAccessor`) | Render access to parameter versions. | resourcemanager.projects.get  
resourcemanager.projects.list  
parametermanager.parameterversions.render  
Parameter Manager Parameter Version Adder  
(`roles/parametermanager.parameterVersionAdder`) | Create access to parameter versions. | resourcemanager.projects.get  
resourcemanager.projects.list  
parametermanager.parameters.get  
parametermanager.parameters.list  
parametermanager.parameterversions.create  
Parameter Manager Parameter Version Manager  
(`roles/parametermanager.parameterVersionManager`) | Read and write access to parameter versions. Lets users view parameters, and create, update, and delete parameter versions. | resourcemanager.projects.get  
resourcemanager.projects.list  
parametermanager.parameters.get  
parametermanager.parameters.list  
parametermanager.parameterversions.get  
parametermanager.parameterversions.list  
parametermanager.parameterversions.create  
parametermanager.parameterversions.update  
parametermanager.parameterversions.delete  
Parameter Manager Parameter Viewer  
(`roles/parametermanager.parameterViewer`) | Read access to parameters and parameter versions. | resourcemanager.projects.get  
resourcemanager.projects.list  
parametermanager.parameters.get  
parametermanager.parameters.list  
parametermanager.parameterversions.get  
parametermanager.parameterversions.list  
  
## Resources with built-in identities

Some types of IAM resources have built-in identities. Resources with built-in identities can do the following: 

  * Be granted IAM roles using the resource's principal identifier 
  * Access other resources without using [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents)



The following IAM resource types have built-in identities: 

Resource type | Resource principal identifier  
---|---  
Parameters |  `principal://parametermanager.googleapis.com/projects/PROJECT_NUMBER/uid/locations/global/parameters/PARAMETER_UID`  
  
## What's next

  * [Create a parameter](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/create-parameter)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
