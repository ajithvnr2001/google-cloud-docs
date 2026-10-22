---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/iam/
title: Identity and Access Management (IAM) \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:18.368945+00:00
---

# Identity and Access Management (IAM)  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Identity and Access Management (IAM) Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can control AI Commerce Search access and permissions using Identity and Access Management (IAM).

## Overview

Google Cloud offers Identity and Access Management (IAM), which lets you give more granular access to specific Google Cloud resources and prevents unwanted access to other resources. This page describes the AI Commerce Search IAM roles and permissions. For a detailed description of Google Cloud IAM, see the [IAM documentation](https://docs.cloud.google.com/iam/docs).

AI Commerce Search provides a set of predefined roles designed for quick control over access to your AI Commerce Search resources. You can also create your own [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), if the predefined roles don't provide the sets of permissions you need. The prior basic roles (Editor, Viewer, and Owner) are also still available to you, although they don't provide the same fine-grained control as the AI Commerce Search roles. In particular, the basic roles provide access to resources across Google Cloud rather than just for AI Commerce Search. See the [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) documentation for more information.

## Predefined roles

The AI Commerce Search provides some predefined roles you can use to provide finer-grained permissions to principals. The role you grant to a principal controls what actions the principal can take. Principals can be individuals, groups, or service accounts.

You can grant multiple roles to the same principal, and you can change the roles granted to a principal at any time, provided you have the permissions to do so.

The broader roles include the more narrowly defined roles. For example, the Retail Editor role includes all of the permissions of the Retail Viewer role, along with the addition permissions of the Retail Editor role. Likewise, the Retail Admin role includes all of the permissions of the Retail Editor role, along with its additional permissions.

The basic roles (Owner, Editor, Viewer) provide permissions across Google Cloud. The roles specific to AI Commerce Search provide only AI Commerce Search permissions, except for the following Google Cloud (Google Cloud) permissions, which are needed for general Google Cloud usage:

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `serviceusage.services.list`
  * `serviceusage.services.get`



The following table lists the predefined roles available for AI Commerce Search, along with their AI Commerce Search permissions:

View table

Name | AI Commerce Search permissions | Description  
---|---|---  
Project > Owner | `All `retail` permissions` | Full access and control for all Google Cloud resources; manage user access and set up billing for a project.  
Project > Editor | All `retail` permissions except the permissions in the Retail Admin role. | Read-write access to all Google Cloud and AI Commerce Search resources (except the ability to modify permissions and billing).  
Project > Viewer |  `retail.*.get`  
`retail.*.list`  
| Read-only access to all Google Cloud resources, including AI Commerce Search resources.  
Retail Admin | `retail.retailProjects.acceptDataTerms`  
`retail.solutions.enroll`  
`retail.products.purge`  
`retail.places.purge`  
`retail.places.purgeInventoryActivities`  
`retail.places.purgeProductPrices`  
`retail.places.purgeProductSettings`  
`retail.orders.purge`  
`retail.products.setSponsorship`  
`retail.userEvents.purge`  
`retail.userEvents.rejoin`  
`retail.attributesConfigs.removeCatalogAttribute`  
`retail.attributesConfigs.batchRemoveCatalogAttributes`  
`retail.merchantConfigs.get`  
`retail.merchantConfigs.update`  
`retail.merchantControls.approverDelete`  
`retail.merchantControls.approverGet`  
`retail.merchantControls.approverList`  
`retail.merchantControls.approverUpdate`  
`retail.merchantControls.creatorCreate`  
`retail.merchantControls.creatorDelete`  
`retail.merchantControls.creatorGet`  
`retail.merchantControls.creatorList`  
`retail.merchantControls.creatorSubmit`  
`retail.merchantControls.creatorUpdate`  
`automlrecommendations.events.purge`  
`automlrecommendations.events.rejoin`  
This role also includes all permissions in the Retail Editor and Retail Viewer roles. | Full control for all AI Commerce Search resources.  
Retail Editor |  `retail.catalogs.import`  
`retail.catalogs.update`  
`retail.products.create`  
`retail.products.delete`  
`retail.products.update`  
`retail.products.import`  
`retail.userEvents.create`  
`retail.userEvents.import`  
`retail.servingConfigs.create`  
`retail.servingConfigs.update`  
`retail.servingConfigs.delete`  
`retail.controls.create`  
`retail.controls.update`  
`retail.controls.delete`  
`retail.controls.import`  
`retail.controls.export`  
`retail.attributesConfigs.update`  
`retail.attributesConfigs.addCatalogAttribute`  
`retail.attributesConfigs.importCatalogAttributes`  
`retail.attributesConfigs.exportCatalogAttributes`  
`retail.attributesConfigs.replaceCatalogAttribute`  
`retail.completionConfigs.update`  
`retail.models.create`  
`retail.models.delete`  
`retail.models.update`  
`retail.models.pause`  
`retail.models.resume`  
`retail.loggingConfigs.update`  
`retail.alertConfigs.update`  
`rretail.merchantCenterAccountLinks.create`  
`retail.merchantCenterAccountLinks.delete`  
`retail.metrics.writeMetricValue`  
`retail.merchantConfigs.get`  
`retail.merchantConfigs.update`  
`retail.merchantControls.approverDelete`  
`retail.merchantControls.approverGet`  
`retail.merchantControls.approverList`  
`retail.merchantControls.approverUpdate`  
`retail.merchantControls.creatorCreate`  
`retail.merchantControls.creatorDelete`  
`retail.merchantControls.creatorGet`  
`retail.merchantControls.creatorList`  
`retail.merchantControls.creatorSubmit`  
`retail.merchantControls.creatorUpdate`  
`automlrecommendations.apiKeys.create`  
`automlrecommendations.apiKeys.delete`  
`automlrecommendations.catalogItems.create`  
`automlrecommendations.catalogItems.delete`  
`automlrecommendations.catalogItems.update`  
`automlrecommendations.catalogs.update`  
`automlrecommendations.events.create`  
`automlrecommendations.placements.create`  
`automlrecommendations.placements.delete`  
`automlrecommendations.recommendations.create`  
`automlrecommendations.recommendations.delete`  
`automlrecommendations.recommendations.pause`  
`automlrecommendations.recommendations.resume`  
`automlrecommendations.recommendations.update`  
This role also includes all permissions in the Retail Viewer role. | Can read all AI Commerce Search resources and write `products`, `events`, and other resources.  
Retail Viewer |  `retail.retailProjects.get`  
`retail.attributesConfigs.exportCatalogAttributes`  
`retail.catalogs.completeQuery`  
`retail.catalogs.listProductAttributes`  
`retail.controls.export`  
`retail.merchantConfigs.get`  
`retail.placements.search`  
`retail.placements.predict`  
`retail.products.export`  
`retail.userEvents.export`  
`retail.*.get`  
`retail.*.list`  
| Read-only access to all AI Commerce Search resources.  
Retail Merchant Approver |  `retail.attributesConfigs.get`  
`retail.controls.get`  
`retail.controls.list`  
`retail.merchantConfigs.get`  
`retail.merchantConfigs.update`  
`retail.merchantControls.approverDelete`  
`retail.merchantControls.approverGet`  
`retail.merchantControls.approverList`  
`retail.merchantControls.approverUpdate`  
`retail.merchantControls.creatorCreate`  
`retail.merchantControls.creatorDelete`  
`retail.merchantControls.creatorGet`  
`retail.merchantControls.creatorList`  
`retail.merchantControls.creatorSubmit`  
`retail.merchantControls.creatorUpdate`  
`retail.products.get`  
`retail.servingConfigs.list`  
`retail.servingConfigs.search`  
| Can approve content in the Merchandising console.  
Retail Merchant Creator |  `retail.attributesConfigs.get`  
`retail.controls.get`  
`retail.controls.list`  
`retail.merchantConfigs.get`  
`retail.merchantControls.creatorCreate`  
`retail.merchantControls.creatorDelete`  
`retail.merchantControls.creatorGet`  
`retail.merchantControls.creatorList`  
`retail.merchantControls.creatorSubmit`  
`retail.merchantControls.creatorUpdate`  
`retail.products.get`  
`retail.servingConfigs.list`  
`retail.servingConfigs.search`  
| Can create content in the Merchandising console.  
  
### Migrate permissions from the Recommendations API

If you are migrating from the previous [Recommendations Engine API](https://docs.cloud.google.com/recommendations-ai/docs/apis) to AI Commerce Search, note that the following predefined roles also include [permissions for the previous API](https://docs.cloud.google.com/recommendations-ai/docs/iam#roles).

  * **Retail Admin** : Includes all the permissions of Recommendations Admin, except for `apiKeys` permissions.
  * **Retail Editor** : Includes all the permissions of Recommendations Editor, as well as `catalog.update`, and excluding `apiKeys` permissions.
  * **Retail Viewer** : Includes all the permissions of Recommendations Viewer.



## Manage AI Commerce Search IAM

You can get and set IAM policies and IAM roles using the Google Cloud console, the IAM methods of the API, or AI Commerce Search. For more information, see [Granting, Changing, and Revoking Access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## What's next

  * Learn how to [grant and revoke access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * Learn more about [IAM](https://docs.cloud.google.com/iam/docs).
  * Learn more about [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic).
  * Learn more about [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
