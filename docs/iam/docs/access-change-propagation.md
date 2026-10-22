---
url: https://docs.cloud.google.com/iam/docs/access-change-propagation/
title: Access change propagation \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:23.383131+00:00
---

# Access change propagation  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/access-change-propagation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Access change propagation Stay organized with collections  Save and categorize content based on your preferences. 

In IAM, access changes, such as granting a role or denying a permission, are [eventually consistent](https://wikipedia.org/wiki/Eventual_consistency). This means that it takes time for access changes to propagate through the system. In the meantime, recent access changes might not be effective everywhere. For example, principals might still be able to use a recently revoked role or a recently denied permission. Alternatively, they might not be able to use a recently granted role or a permission they were, until recently, denied from using.

For information about how tag changes propagate and affect conditional access, see [Tag propagation](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#propagation).

The amount of time it takes for an access change to propagate depends on how you make the access change:

Method | Examples | Propagation time  
---|---|---  
**Change a policy** Change a principal's access by editing an allow or deny policy.  When making policy changes, you can't exceed the [limits on the number of principals allowed in a policy](https://docs.cloud.google.com/iam/quotas#limits).  | 

  * You edit your organization's allow policy to grant a principal the Organization Administrator role (`roles/resourcemanager.organizationAdmin`). 
  * You edit an organization-level deny policy to deny a principal the `cloudresourcemanager.googleapis.com/projects.setIamPolicy` permission. 
  * You edit an allow policy to add [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to a role binding. 

|  Typically 2 minutes, potentially 7 minutes or longer   
**Change a group's membership** Change a principal's access by adding or removing them from a Google group that's included in an allow or deny policy.  | 

  * You have a group, `org-admins@example.com`, that is granted the Organization Administrator role on your organization. You add a principal to the group to give them the Organization Administrator role. 
  * You have a group, `eng@example.com`, that is denied the `cloudresourcemanager.googleapis.com/projects.setIamPolicy` permission at the organization level. You add a principal to the group to deny them the `cloudresourcemanager.googleapis.com/projects.setIamPolicy` permission. 

|  Typically several minutes, potentially hours or longer   
**Change a nested group's membership** Change a principal's access by adding or removing them from a [nested group](https://support.google.com/a/answer/167100) whose parent group is included in an allow or deny policy.  | 

  * You have a group, `admins@example.com`, that is granted the Tag Viewer role (`roles/resourcemanager.tagViewer`) on your organization. This group's membership is made up of a number of other groups, including `org-admins@example.com`. You add a principal to the `org-admins@example.com` group to give them the Tag Viewer role. 
  * You have a group, `eng@example.com`, that is denied the `cloudresourcemanager.googleapis.com/projects.setIamPolicy` permission at the organization level. This group's membership is made up of a number of other groups, including `eng-prod@example.com`. You add a principal to the `eng-prod@example.com` group to deny them the `cloudresourcemanager.googleapis.com/projects.setIamPolicy` permission. 

|  Typically several minutes, potentially hours or longer   
  
Also keep in mind the following details for how group membership changes propagate:

  * In general, adding a principal to a group propagates faster than removing a principal from a group.
  * In general, group membership changes propagate faster than nested group membership changes.



You can use these propagation time estimates to inform the way you modify your principals' access.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
