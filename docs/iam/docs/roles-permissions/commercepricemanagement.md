---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement/
title: Commerce Price Management roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:58.539754+00:00
---

# Commerce Price Management roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Commerce Price Management roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Commerce Price Management. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Commerce Price Management roles

Role | Permissions  
---|---  
  
#### Commercepricemanagement Editor Beta

(`roles/commercepricemanagement.editor`) Editor role for commercepricemanagement  |  `commerceagreementpublishing.agreements.get` `commerceagreementpublishing.agreements.list` `commerceagreementpublishing.documents.get` `commerceagreementpublishing.documents.list` `commerceprice.privateoffers.*`

  * `commerceprice.privateoffers.cancel`
  * `commerceprice.privateoffers.create`
  * `commerceprice.privateoffers.delete`
  * `commerceprice.privateoffers.get`
  * `commerceprice.privateoffers.list`
  * `commerceprice.privateoffers.publish`
  * `commerceprice.privateoffers.sendEmail`
  * `commerceprice.privateoffers.update`

`commerceproducer.privateOfferDocuments.get` `commerceproducer.privateOfferDocuments.list` `commerceproducer.privateOffers.get` `commerceproducer.privateOffers.list` `commerceproducer.skuGroups.*`

  * `commerceproducer.skuGroups.get`
  * `commerceproducer.skuGroups.list`

`commerceproducer.skus.*`

  * `commerceproducer.skus.get`
  * `commerceproducer.skus.list`

`commerceproducer.standardOffers.*`

  * `commerceproducer.standardOffers.get`
  * `commerceproducer.standardOffers.list`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Commerce Price Management Viewer Beta

(`roles/commercepricemanagement.viewer`) Allows viewing offers, free trials, skus  |  `commerceagreementpublishing.agreements.get` `commerceagreementpublishing.agreements.list` `commerceagreementpublishing.documents.get` `commerceagreementpublishing.documents.list` `commerceprice.privateoffers.get` `commerceprice.privateoffers.list` `commerceproducer.privateOfferDocuments.get` `commerceproducer.privateOfferDocuments.list` `commerceproducer.privateOffers.get` `commerceproducer.privateOffers.list` `commerceproducer.skuGroups.*`

  * `commerceproducer.skuGroups.get`
  * `commerceproducer.skuGroups.list`

`commerceproducer.skus.*`

  * `commerceproducer.skus.get`
  * `commerceproducer.skus.list`

`commerceproducer.standardOffers.*`

  * `commerceproducer.standardOffers.get`
  * `commerceproducer.standardOffers.list`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Commerce Price Management Events Viewer Beta

(`roles/commercepricemanagement.eventsViewer`) Allows viewing key events for an offer  |  `commerceprice.events.*`

  * `commerceprice.events.get`
  * `commerceprice.events.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Commerce Price Management Private Offers Admin Beta

(`roles/commercepricemanagement.privateOffersAdmin`) Allows managing private offers  |  `commerceagreementpublishing.*`

  * `commerceagreementpublishing.agreements.create`
  * `commerceagreementpublishing.agreements.delete`
  * `commerceagreementpublishing.agreements.get`
  * `commerceagreementpublishing.agreements.list`
  * `commerceagreementpublishing.agreements.update`
  * `commerceagreementpublishing.documents.create`
  * `commerceagreementpublishing.documents.delete`
  * `commerceagreementpublishing.documents.get`
  * `commerceagreementpublishing.documents.list`
  * `commerceagreementpublishing.documents.update`

`commerceprice.*`

  * `commerceprice.events.get`
  * `commerceprice.events.list`
  * `commerceprice.privateoffers.cancel`
  * `commerceprice.privateoffers.create`
  * `commerceprice.privateoffers.delete`
  * `commerceprice.privateoffers.get`
  * `commerceprice.privateoffers.list`
  * `commerceprice.privateoffers.publish`
  * `commerceprice.privateoffers.sendEmail`
  * `commerceprice.privateoffers.update`

`commerceproducer.privateOfferDocuments.*`

  * `commerceproducer.privateOfferDocuments.create`
  * `commerceproducer.privateOfferDocuments.delete`
  * `commerceproducer.privateOfferDocuments.get`
  * `commerceproducer.privateOfferDocuments.list`
  * `commerceproducer.privateOfferDocuments.update`

`commerceproducer.privateOffers.*`

  * `commerceproducer.privateOffers.cancel`
  * `commerceproducer.privateOffers.create`
  * `commerceproducer.privateOffers.delete`
  * `commerceproducer.privateOffers.get`
  * `commerceproducer.privateOffers.list`
  * `commerceproducer.privateOffers.publish`
  * `commerceproducer.privateOffers.update`

`commerceproducer.skuGroups.*`

  * `commerceproducer.skuGroups.get`
  * `commerceproducer.skuGroups.list`

`commerceproducer.skus.*`

  * `commerceproducer.skus.get`
  * `commerceproducer.skus.list`

`commerceproducer.standardOffers.*`

  * `commerceproducer.standardOffers.get`
  * `commerceproducer.standardOffers.list`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
## Commerce Price Management permissions

Permission | Included in roles  
---|---  
  
#### `commerceprice.events.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Commerce Price Management Events Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.eventsViewer) (`roles/commercepricemanagement.eventsViewer`)  [Commerce Price Management Private Offers Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.privateOffersAdmin) (`roles/commercepricemanagement.privateOffersAdmin`)   
  
#### `commerceprice.events.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Commerce Price Management Events Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.eventsViewer) (`roles/commercepricemanagement.eventsViewer`)  [Commerce Price Management Private Offers Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.privateOffersAdmin) (`roles/commercepricemanagement.privateOffersAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `commerceprice.privateoffers.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Commercepricemanagement Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.editor) (`roles/commercepricemanagement.editor`)  [Commerce Price Management Private Offers Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.privateOffersAdmin) (`roles/commercepricemanagement.privateOffersAdmin`)   
  
#### `commerceprice.privateoffers.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Commercepricemanagement Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.editor) (`roles/commercepricemanagement.editor`)  [Commerce Price Management Private Offers Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.privateOffersAdmin) (`roles/commercepricemanagement.privateOffersAdmin`)   
  
#### `commerceprice.privateoffers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Commercepricemanagement Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.editor) (`roles/commercepricemanagement.editor`)  [Commerce Price Management Private Offers Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.privateOffersAdmin) (`roles/commercepricemanagement.privateOffersAdmin`)   
  
#### `commerceprice.privateoffers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Commercepricemanagement Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.editor) (`roles/commercepricemanagement.editor`)  [Commerce Price Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.viewer) (`roles/commercepricemanagement.viewer`)  [Commerce Price Management Private Offers Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.privateOffersAdmin) (`roles/commercepricemanagement.privateOffersAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `commerceprice.privateoffers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Commercepricemanagement Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.editor) (`roles/commercepricemanagement.editor`)  [Commerce Price Management Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.viewer) (`roles/commercepricemanagement.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Commerce Price Management Private Offers Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.privateOffersAdmin) (`roles/commercepricemanagement.privateOffersAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `commerceprice.privateoffers.publish`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Commercepricemanagement Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.editor) (`roles/commercepricemanagement.editor`)  [Commerce Price Management Private Offers Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.privateOffersAdmin) (`roles/commercepricemanagement.privateOffersAdmin`)   
  
#### `commerceprice.privateoffers.sendEmail`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Commercepricemanagement Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.editor) (`roles/commercepricemanagement.editor`)  [Commerce Price Management Private Offers Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.privateOffersAdmin) (`roles/commercepricemanagement.privateOffersAdmin`)   
  
#### `commerceprice.privateoffers.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Commercepricemanagement Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.editor) (`roles/commercepricemanagement.editor`)  [Commerce Price Management Private Offers Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.privateOffersAdmin) (`roles/commercepricemanagement.privateOffersAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
