---
url: https://docs.cloud.google.com/audit-manager/docs/access-control/
title: Control access with IAM \u00a0|\u00a0 Audit Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:07.292780+00:00
---

# Control access with IAM  |  Audit Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/audit-manager/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Audit Manager ](https://docs.cloud.google.com/audit-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/audit-manager/docs/overview)



Send feedback 

#  Control access with IAM Stay organized with collections  Save and categorize content based on your preferences. 

Identity and Access Management (IAM) roles and permissions let you control who can set up Audit Manager and who can run audits.

User | Task | Roles and permissions | Administrator | Set up Audit Manager access | 

  * [**Audit Manager Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.admin) (`roles/auditmanager.admin`) This role grants the ability to enable auditing on an organization, folder, or project, generate an audit scope, and create or view Audit Manager reports.
  * [**Storage Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) or [**Storage Legacy Bucket Owner**](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`) These roles grant the ability to create, overwrite, and delete storage buckets. Users need to specify a storage bucket when enrolling a resource for auditing.
  * `resourcemanager.organizations.setIamPolicy` This additional permission is required to enroll an organization.
  * `resourcemanager.folders.setIamPolicy` This additional permission is required to enroll a folder.

  
---|---|---  
Auditor | Run audit and view reports | 

  * [**Audit Manager Auditor**](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.auditor) (`roles/auditmanager.auditor`) This role grants the ability to generate an audit scope, and to create or view Audit Manager reports.
  * [**Storage Legacy Object Reader**](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketReader) (`roles/storage.legacyObjectReader`) This role grants users the ability to read storage buckets.

  
  
For more information about granting roles, see the [IAM documentation](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

## What's next

  * [Enroll resources for audit](https://docs.cloud.google.com/audit-manager/docs/enroll-resource).
  * [Run an audit](https://docs.cloud.google.com/audit-manager/docs/run-audit).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
