---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/readerrevenuesubscriptionlinking/
title: Subscription Linking roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:10:45.293496+00:00
---

# Subscription Linking roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/readerrevenuesubscriptionlinking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Subscription Linking roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Subscription Linking. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Subscription Linking roles

Role | Permissions  
---|---  
  
#### Subscription Linking Admin 

(`roles/readerrevenuesubscriptionlinking.admin`) Full access to publication reader resources  |  `readerrevenuesubscriptionlinking.*`

  * `readerrevenuesubscriptionlinking.readerEntitlements.get`
  * `readerrevenuesubscriptionlinking.readerEntitlements.update`
  * `readerrevenuesubscriptionlinking.readers.delete`
  * `readerrevenuesubscriptionlinking.readers.get`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Subscription Linking Viewer 

(`roles/readerrevenuesubscriptionlinking.viewer`) This role can view all publication reader resources  |  `readerrevenuesubscriptionlinking.readerEntitlements.get` `readerrevenuesubscriptionlinking.readers.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Subscription Linking Entitlements Viewer 

(`roles/readerrevenuesubscriptionlinking.entitlementsViewer`) This role can view all publication reader entitlements  |  `readerrevenuesubscriptionlinking.readerEntitlements.get`  
  
## Subscription Linking permissions

Permission | Included in roles  
---|---  
  
#### `readerrevenuesubscriptionlinking.readerEntitlements.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Subscription Linking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/readerrevenuesubscriptionlinking#readerrevenuesubscriptionlinking.admin) (`roles/readerrevenuesubscriptionlinking.admin`)  [Subscription Linking Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/readerrevenuesubscriptionlinking#readerrevenuesubscriptionlinking.viewer) (`roles/readerrevenuesubscriptionlinking.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Subscription Linking Entitlements Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/readerrevenuesubscriptionlinking#readerrevenuesubscriptionlinking.entitlementsViewer) (`roles/readerrevenuesubscriptionlinking.entitlementsViewer`)   
  
#### `readerrevenuesubscriptionlinking.readerEntitlements.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Subscription Linking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/readerrevenuesubscriptionlinking#readerrevenuesubscriptionlinking.admin) (`roles/readerrevenuesubscriptionlinking.admin`)   
  
#### `readerrevenuesubscriptionlinking.readers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Subscription Linking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/readerrevenuesubscriptionlinking#readerrevenuesubscriptionlinking.admin) (`roles/readerrevenuesubscriptionlinking.admin`)   
  
#### `readerrevenuesubscriptionlinking.readers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Subscription Linking Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/readerrevenuesubscriptionlinking#readerrevenuesubscriptionlinking.admin) (`roles/readerrevenuesubscriptionlinking.admin`)  [Subscription Linking Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/readerrevenuesubscriptionlinking#readerrevenuesubscriptionlinking.viewer) (`roles/readerrevenuesubscriptionlinking.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
