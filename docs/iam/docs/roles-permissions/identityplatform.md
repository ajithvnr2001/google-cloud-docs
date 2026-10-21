---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform/
title: Identity Platform roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:28:40.239374+00:00
---

# Identity Platform roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Identity Platform roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Identity Platform. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Identity Platform roles

Role | Permissions  
---|---  
  
#### Identity Platform Admin Beta

(`roles/identityplatform.admin`) Full access to Identity Platform resources.  |  `firebaseauth.*`

  * `firebaseauth.configs.create`
  * `firebaseauth.configs.get`
  * `firebaseauth.configs.getHashConfig`
  * `firebaseauth.configs.getSecret`
  * `firebaseauth.configs.update`
  * `firebaseauth.users.create`
  * `firebaseauth.users.createSession`
  * `firebaseauth.users.delete`
  * `firebaseauth.users.get`
  * `firebaseauth.users.sendEmail`
  * `firebaseauth.users.update`

`identitytoolkit.*`

  * `identitytoolkit.tenants.create`
  * `identitytoolkit.tenants.delete`
  * `identitytoolkit.tenants.get`
  * `identitytoolkit.tenants.getIamPolicy`
  * `identitytoolkit.tenants.list`
  * `identitytoolkit.tenants.setIamPolicy`
  * `identitytoolkit.tenants.update`

  
  
#### Identity Platform Viewer Beta

(`roles/identityplatform.viewer`) Read access to Identity Platform resources.  |  `firebaseauth.configs.get` `firebaseauth.users.get` `identitytoolkit.tenants.get` `identitytoolkit.tenants.getIamPolicy` `identitytoolkit.tenants.list`  
  
## Identity Platform permissions

There are no IAM permissions for this service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
