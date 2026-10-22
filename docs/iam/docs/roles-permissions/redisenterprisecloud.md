---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud/
title: Redis Enterprise Cloud roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:49.048669+00:00
---

# Redis Enterprise Cloud roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Redis Enterprise Cloud roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Redis Enterprise Cloud. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Redis Enterprise Cloud roles

Role | Permissions  
---|---  
  
#### Redis Enterprise Cloud Admin Beta

(`roles/redisenterprisecloud.admin`) This role is managed by Redis Labs, not Google.  |  `gcp.redisenterprise.com/*`

  * `gcp.redisenterprise.com/databases.create`
  * `gcp.redisenterprise.com/databases.delete`
  * `gcp.redisenterprise.com/databases.get`
  * `gcp.redisenterprise.com/databases.list`
  * `gcp.redisenterprise.com/databases.update`
  * `gcp.redisenterprise.com/subscriptions.create`
  * `gcp.redisenterprise.com/subscriptions.delete`
  * `gcp.redisenterprise.com/subscriptions.get`
  * `gcp.redisenterprise.com/subscriptions.list`
  * `gcp.redisenterprise.com/subscriptions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Redis Enterprise Cloud Viewer Beta

(`roles/redisenterprisecloud.viewer`) This role is managed by Redis Labs, not Google.  |  `gcp.redisenterprise.com/databases.get` `gcp.redisenterprise.com/databases.list` `gcp.redisenterprise.com/subscriptions.get` `gcp.redisenterprise.com/subscriptions.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Redis Enterprise Cloud permissions

Permission | Included in roles  
---|---  
  
#### `gcp.redisenterprise.com/databases.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Redis Enterprise Cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud#redisenterprisecloud.admin) (`roles/redisenterprisecloud.admin`)   
  
#### `gcp.redisenterprise.com/databases.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Redis Enterprise Cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud#redisenterprisecloud.admin) (`roles/redisenterprisecloud.admin`)   
  
#### `gcp.redisenterprise.com/databases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Redis Enterprise Cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud#redisenterprisecloud.admin) (`roles/redisenterprisecloud.admin`)  [Redis Enterprise Cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud#redisenterprisecloud.viewer) (`roles/redisenterprisecloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gcp.redisenterprise.com/databases.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Redis Enterprise Cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud#redisenterprisecloud.admin) (`roles/redisenterprisecloud.admin`)  [Redis Enterprise Cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud#redisenterprisecloud.viewer) (`roles/redisenterprisecloud.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gcp.redisenterprise.com/databases.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Redis Enterprise Cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud#redisenterprisecloud.admin) (`roles/redisenterprisecloud.admin`)   
  
#### `gcp.redisenterprise.com/subscriptions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Redis Enterprise Cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud#redisenterprisecloud.admin) (`roles/redisenterprisecloud.admin`)   
  
#### `gcp.redisenterprise.com/subscriptions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Redis Enterprise Cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud#redisenterprisecloud.admin) (`roles/redisenterprisecloud.admin`)   
  
#### `gcp.redisenterprise.com/subscriptions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Redis Enterprise Cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud#redisenterprisecloud.admin) (`roles/redisenterprisecloud.admin`)  [Redis Enterprise Cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud#redisenterprisecloud.viewer) (`roles/redisenterprisecloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gcp.redisenterprise.com/subscriptions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Redis Enterprise Cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud#redisenterprisecloud.admin) (`roles/redisenterprisecloud.admin`)  [Redis Enterprise Cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud#redisenterprisecloud.viewer) (`roles/redisenterprisecloud.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gcp.redisenterprise.com/subscriptions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Redis Enterprise Cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/redisenterprisecloud#redisenterprisecloud.admin) (`roles/redisenterprisecloud.admin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
