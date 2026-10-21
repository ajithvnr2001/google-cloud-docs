---
url: https://docs.cloud.google.com/document-warehouse/docs/roles-and-permissions/
title: IAM roles and permissions \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:42:41.805859+00:00
---

# IAM roles and permissions  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/roles-and-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Reference ](https://docs.cloud.google.com/document-warehouse/docs/reference/rest)



Send feedback 

#  IAM roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

**Caution** : Document AI Warehouse is deprecated and will no longer be available on Google Cloud after January 16, 2025. To safeguard your data, migrate any documents currently saved in Document AI Warehouse to an alternative like Cloud Storage. Verify that your data migration is completed before the discontinuation date to prevent any data loss. See [Deprecations](https://docs.cloud.google.com/document-warehouse/docs/deprecations) for details.

## Predefined roles

The following table describes Identity and Access Management (IAM) [roles](https://cloud.google.com/iam/docs/understanding-roles) that are associated with Document AI Warehouse and lists the permissions that are contained in each role. Unless otherwise noted, these roles can be applied either to entire projects or specific documents.

Role | Permissions  
---|---  
`contentwarehouse.documentCreator` | resourcemanager.projects.get   
resourcemanager.projects.list   
contentwarehouse.documentSchemas.get   
contentwarehouse.documentSchemas.list   
contentwarehouse.documents.create  
`contentwarehouse.documentViewer` | resourcemanager.projects.get   
resourcemanager.projects.list   
contentwarehouse.documentSchemas.get   
contentwarehouse.documents.get   
contentwarehouse.documents.getIamPolicy  
`contentwarehouse.documentEditor` | **Role** `contentwarehouse.documentViewer`   
contentwarehouse.documents.update  
`contentwarehouse.documentAdmin` | **Role** `contentwarehouse.documentEditor`   
contentwarehouse.documents.create   
contentwarehouse.documents.delete   
contentwarehouse.documents.setIamPolicy  
`contentwarehouse.admin` | **Role** `contentwarehouse.documentAdmin`   
contentwarehouse.documentSchemas.create   
contentwarehouse.documentSchemas.delete   
contentwarehouse.ruleSets.create   
contentwarehouse.ruleSets.get   
contentwarehouse.ruleSets.list   
contentwarehouse.ruleSets.update   
contentwarehouse.ruleSets.delete  
**Note:** The role `roles/contentwarehouse.documentCreator` is a parent level role. Under Document AI Warehouse's current [resource hierarchy](https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) setting (Organization -> Folders -> Projects -> [Locations] -> Documents), this role will only be applied at the project level and not the document level. All the other roles can be applied at both the project level and the document level.

## Basic roles

Basic roles are roles that existed prior to IAM. These roles have unique characteristics:

  * Basic roles can only be granted for an entire project, not for individual objects within the project.
  * Basic roles contain additional permissions for other Google Cloud services that are not covered in this section. For a general discussion of the permissions that basic roles grant, see [basic roles](https://cloud.google.com/iam/docs/roles-overview#basic).
  * In some cases, basic roles can be used as if they were groups, which causes any principal that has the basic role to get additional access for some resources.



## Custom roles

You might want to define your own roles that contain bundles of permissions that you specify. To support this, IAM offers [custom roles](https://cloud.google.com/iam/docs/creating-custom-roles).

**Note:** Custom roles are not supported if you choose [Document-level access control](https://docs.cloud.google.com/document-warehouse/docs/manage-access-control#document-level-access-control) mode for your project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
