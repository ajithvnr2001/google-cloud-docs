---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/access-control/iam-roles/
title: IAM roles for Enterprise Knowledge Graph \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:33:28.428787+00:00
---

# IAM roles for Enterprise Knowledge Graph  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/access-control/iam-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Reference ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries)



Send feedback 

#  IAM roles for Enterprise Knowledge Graph Stay organized with collections  Save and categorize content based on your preferences. 

The following table describes Identity and Access Management (IAM) roles that are associated with Enterprise Knowledge Graph and lists the permissions that are contained in each role. Unless otherwise noted, these roles can be applied either to entire projects or specific processors.

Role | Description | Permissions  
---|---|---  
**Enterprise Knowledge Graph Administrator** (`roles/enterpriseknowledgegraph.admin`) | Grants full access to all resources in Enterprise Knowledge Graph. | Role: `roles/enterpriseknowledgegraph.editor`  
**Enterprise Knowledge Graph Editor** (`roles/enterpriseknowledgegraph.editor`) | Grants access to use all resources in Enterprise Knowledge Graph. | Role: `roles/enterpriseknowledgegraph.viewer`  
`enterpriseknowledgegraph.entityReconciliationJobs.create`  
`enterpriseknowledgegraph.entityReconciliationJobs.cancel`  
`enterpriseknowledgegraph.entityReconciliationJobs.delete`  
**Enterprise Knowledge Graph Viewer** (`roles/enterpriseknowledgegraph.viewer`) | Grants access to view all resources and entity reconciliation job in Enterprise Knowledge Graph |    
Permissions: `cloudresourcemanager.projects.get`  
`cloudresourcemanager.projects.list`  
`enterpriseknowledgegraph.entityReconciliationJobs.get`  
`enterpriseknowledgegraph.entityReconciliationJobs.list`  
  
## Basic roles

Basic roles are roles that existed prior to IAM. These roles have unique characteristics:

  * Basic roles can only be granted for an entire project, not for individual buckets within the project. Like other roles that you grant for a project, basic roles apply to all buckets and objects in the project.

  * Basic roles contain additional permissions for other Google Cloud services that are not covered in this section. For a general discussion of the permissions that basic roles grant, see [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic).

  * In some cases, basic roles can be used as if they were groups, which causes any principal that has the basic role to get additional access for some resources.

    * A basic role can be used as if it were a group when granting roles for buckets.

    * A basic role can be used as if it were a group when setting ACLs on objects.

For a discussion of additional access that principals with basic roles typically gain due to this behavior, see modifiable behavior.




## What's next

  * Learn about each [IAM permission for Enterprise Knowledge Graph](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/access-control/iam-permissions).

  * For a reference of other Google Cloud roles, see [Understanding Roles](https://docs.cloud.google.com/iam/docs/understanding-roles).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
