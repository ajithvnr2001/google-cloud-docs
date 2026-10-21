---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription/
title: Payments Reseller Subscription roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:33:08.848935+00:00
---

# Payments Reseller Subscription roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Payments Reseller Subscription roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Payments Reseller Subscription. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Payments Reseller Subscription roles

Role | Permissions  
---|---  
  
#### Paymentsresellersubscription Admin Beta

(`roles/paymentsresellersubscription.admin`) Admin role for paymentsresellersubscription  |  `paymentsresellersubscription.*`

  * `paymentsresellersubscription.products.list`
  * `paymentsresellersubscription.promotions.list`
  * `paymentsresellersubscription.subscriptionLineItems.update`
  * `paymentsresellersubscription.subscriptions.cancel`
  * `paymentsresellersubscription.subscriptions.extend`
  * `paymentsresellersubscription.subscriptions.get`
  * `paymentsresellersubscription.subscriptions.provision`
  * `paymentsresellersubscription.subscriptions.resume`
  * `paymentsresellersubscription.subscriptions.suspend`
  * `paymentsresellersubscription.subscriptions.undoCancel`
  * `paymentsresellersubscription.userSessions.generate`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Paymentsresellersubscription Viewer Beta

(`roles/paymentsresellersubscription.viewer`) Viewer role for paymentsresellersubscription  |  `paymentsresellersubscription.products.list` `paymentsresellersubscription.promotions.list` `paymentsresellersubscription.subscriptions.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Payments Reseller Admin Beta

(`roles/paymentsresellersubscription.partnerAdmin`) Full access to all Payments Reseller resources, including subscriptions, products and promotions  |  `paymentsresellersubscription.*`

  * `paymentsresellersubscription.products.list`
  * `paymentsresellersubscription.promotions.list`
  * `paymentsresellersubscription.subscriptionLineItems.update`
  * `paymentsresellersubscription.subscriptions.cancel`
  * `paymentsresellersubscription.subscriptions.extend`
  * `paymentsresellersubscription.subscriptions.get`
  * `paymentsresellersubscription.subscriptions.provision`
  * `paymentsresellersubscription.subscriptions.resume`
  * `paymentsresellersubscription.subscriptions.suspend`
  * `paymentsresellersubscription.subscriptions.undoCancel`
  * `paymentsresellersubscription.userSessions.generate`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Payments Reseller Viewer Beta

(`roles/paymentsresellersubscription.partnerViewer`) Read access to all Payments Reseller resources, including subscriptions, products and promotions  |  `paymentsresellersubscription.products.list` `paymentsresellersubscription.promotions.list` `paymentsresellersubscription.subscriptions.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Payments Reseller Products Viewer Beta

(`roles/paymentsresellersubscription.productViewer`) Read access to Payments Reseller Product resource  |  `paymentsresellersubscription.products.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Payments Reseller Promotions Viewer Beta

(`roles/paymentsresellersubscription.promotionViewer`) Read access to Payments Reseller Promotion resource  |  `paymentsresellersubscription.promotions.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Payments Reseller Subscriptions Editor Beta

(`roles/paymentsresellersubscription.subscriptionEditor`) Write access to Payments Reseller Subscription resource  |  `paymentsresellersubscription.subscriptionLineItems.update` `paymentsresellersubscription.subscriptions.*`

  * `paymentsresellersubscription.subscriptions.cancel`
  * `paymentsresellersubscription.subscriptions.extend`
  * `paymentsresellersubscription.subscriptions.get`
  * `paymentsresellersubscription.subscriptions.provision`
  * `paymentsresellersubscription.subscriptions.resume`
  * `paymentsresellersubscription.subscriptions.suspend`
  * `paymentsresellersubscription.subscriptions.undoCancel`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Payments Reseller Subscriptions Viewer Beta

(`roles/paymentsresellersubscription.subscriptionViewer`) Read access to Payments Reseller Subscription resource  |  `paymentsresellersubscription.subscriptions.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Payments Partner UserSessions Editor Beta

(`roles/paymentsresellersubscription.userSessionEditor`) Editor of UserSessions for a Payments Partner  |  `paymentsresellersubscription.userSessions.generate`  
  
## Payments Reseller Subscription permissions

Permission | Included in roles  
---|---  
  
#### `paymentsresellersubscription.products.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Paymentsresellersubscription Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.admin) (`roles/paymentsresellersubscription.admin`)  [Paymentsresellersubscription Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.viewer) (`roles/paymentsresellersubscription.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Payments Reseller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.partnerAdmin) (`roles/paymentsresellersubscription.partnerAdmin`)  [Payments Reseller Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.partnerViewer) (`roles/paymentsresellersubscription.partnerViewer`)  [Payments Reseller Products Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.productViewer) (`roles/paymentsresellersubscription.productViewer`)   
  
#### `paymentsresellersubscription.promotions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Paymentsresellersubscription Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.admin) (`roles/paymentsresellersubscription.admin`)  [Paymentsresellersubscription Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.viewer) (`roles/paymentsresellersubscription.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Payments Reseller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.partnerAdmin) (`roles/paymentsresellersubscription.partnerAdmin`)  [Payments Reseller Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.partnerViewer) (`roles/paymentsresellersubscription.partnerViewer`)  [Payments Reseller Promotions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.promotionViewer) (`roles/paymentsresellersubscription.promotionViewer`)   
  
#### `paymentsresellersubscription.subscriptionLineItems.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Paymentsresellersubscription Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.admin) (`roles/paymentsresellersubscription.admin`)  [Payments Reseller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.partnerAdmin) (`roles/paymentsresellersubscription.partnerAdmin`)  [Payments Reseller Subscriptions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.subscriptionEditor) (`roles/paymentsresellersubscription.subscriptionEditor`)   
  
#### `paymentsresellersubscription.subscriptions.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Paymentsresellersubscription Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.admin) (`roles/paymentsresellersubscription.admin`)  [Payments Reseller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.partnerAdmin) (`roles/paymentsresellersubscription.partnerAdmin`)  [Payments Reseller Subscriptions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.subscriptionEditor) (`roles/paymentsresellersubscription.subscriptionEditor`)   
  
#### `paymentsresellersubscription.subscriptions.extend`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Paymentsresellersubscription Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.admin) (`roles/paymentsresellersubscription.admin`)  [Payments Reseller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.partnerAdmin) (`roles/paymentsresellersubscription.partnerAdmin`)  [Payments Reseller Subscriptions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.subscriptionEditor) (`roles/paymentsresellersubscription.subscriptionEditor`)   
  
#### `paymentsresellersubscription.subscriptions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Paymentsresellersubscription Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.admin) (`roles/paymentsresellersubscription.admin`)  [Paymentsresellersubscription Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.viewer) (`roles/paymentsresellersubscription.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Payments Reseller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.partnerAdmin) (`roles/paymentsresellersubscription.partnerAdmin`)  [Payments Reseller Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.partnerViewer) (`roles/paymentsresellersubscription.partnerViewer`)  [Payments Reseller Subscriptions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.subscriptionEditor) (`roles/paymentsresellersubscription.subscriptionEditor`)  [Payments Reseller Subscriptions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.subscriptionViewer) (`roles/paymentsresellersubscription.subscriptionViewer`)   
  
#### `paymentsresellersubscription.subscriptions.provision`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Paymentsresellersubscription Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.admin) (`roles/paymentsresellersubscription.admin`)  [Payments Reseller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.partnerAdmin) (`roles/paymentsresellersubscription.partnerAdmin`)  [Payments Reseller Subscriptions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.subscriptionEditor) (`roles/paymentsresellersubscription.subscriptionEditor`)   
  
#### `paymentsresellersubscription.subscriptions.resume`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Paymentsresellersubscription Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.admin) (`roles/paymentsresellersubscription.admin`)  [Payments Reseller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.partnerAdmin) (`roles/paymentsresellersubscription.partnerAdmin`)  [Payments Reseller Subscriptions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.subscriptionEditor) (`roles/paymentsresellersubscription.subscriptionEditor`)   
  
#### `paymentsresellersubscription.subscriptions.suspend`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Paymentsresellersubscription Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.admin) (`roles/paymentsresellersubscription.admin`)  [Payments Reseller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.partnerAdmin) (`roles/paymentsresellersubscription.partnerAdmin`)  [Payments Reseller Subscriptions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.subscriptionEditor) (`roles/paymentsresellersubscription.subscriptionEditor`)   
  
#### `paymentsresellersubscription.subscriptions.undoCancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Paymentsresellersubscription Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.admin) (`roles/paymentsresellersubscription.admin`)  [Payments Reseller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.partnerAdmin) (`roles/paymentsresellersubscription.partnerAdmin`)  [Payments Reseller Subscriptions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.subscriptionEditor) (`roles/paymentsresellersubscription.subscriptionEditor`)   
  
#### `paymentsresellersubscription.userSessions.generate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Paymentsresellersubscription Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.admin) (`roles/paymentsresellersubscription.admin`)  [Payments Reseller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.partnerAdmin) (`roles/paymentsresellersubscription.partnerAdmin`)  [Payments Partner UserSessions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/paymentsresellersubscription#paymentsresellersubscription.userSessionEditor) (`roles/paymentsresellersubscription.userSessionEditor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
