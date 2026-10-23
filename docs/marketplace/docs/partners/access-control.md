---
url: https://docs.cloud.google.com/marketplace/docs/partners/access-control/
title: Configure access control for Producer Portal users \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:14.497381+00:00
---

# Configure access control for Producer Portal users  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Configure access control for Producer Portal users Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Identity and Access Management (IAM) roles and permissions that you'll need to grant to members of your team who [use Producer Portal](https://docs.cloud.google.com/marketplace/docs/partners/get-started#integrate).

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic), such as the Project Editor role (`roles/editor`), might enable users to perform necessary tasks, but we recommend that you only grant the minimal necessary roles. You shouldn't grant basic roles in a production environment, although you can grant them in a development or test environment.

For more information about granting access to roles and resources, see the IAM documentation on [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). If you don't have the permissions you need to grant roles, contact your organization's administrator and request access.

## Access control for managing projects

For users to manage your Google Cloud Partner Network account and your organization-level settings, grant them one of the following two roles:

  * Commerce Business Enablement Configuration Admin (`roles/commercebusinessenablement.admin`)

  * Commerce Business Enablement Configuration Viewer (`roles/commercebusinessenablement.viewer`)




## Access control for viewing product listings

For users to view in-progress product listings that you create in Producer Portal, grant them the [Commerce Producer Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/commerceproducer) role.

## Access control for creating and managing product listings

For users to create and manage product listings in Producer Portal, grant them the following roles:

  * [Commerce Producer Admin](https://cloud.google.com/iam/docs/roles-permissions/commerceproducer#commerceproducer.admin)
  * [Service Management API Administrator](https://console.cloud.google.com/iam-admin/roles/details/roles%3Cservicemanagement.admin)

**Note:** The [Commerce Producer Admin](https://cloud.google.com/iam/docs/roles-permissions/commerceproducer#commerceproducer.admin) role provides full access to all resources for your products.

### Additional roles for software as a service (SaaS) products

For SaaS products, where you need to create a service account to interact with the Cloud Commerce Consumer Procurement API and report usage to us, grant your users the [Service Account Admin](https://console.cloud.google.com/iam-admin/roles/details/roles%3Ciam.serviceAccountAdmin) role.

#### Additional roles for virtual machine (VM) and Kubernetes products

For VM or Kubernetes products, grant your users the [Compute Cloud Storage Admin](https://console.cloud.google.com/iam-admin/roles/details/roles%3Ccompute.storageAdmin) role.

[VM guided configuration](https://cloud.google.com/marketplace/docs/partners/vm/create-deployment-package#simple-deployment) to create your VM product's deployment package, grant your users the following roles for the Cloud Storage bucket where you store your product's deployment package:

  * [Cloud Storage Object Viewer](https://console.cloud.google.com/iam-admin/roles/details/roles%3Cstorage.objectViewer)
  * [Cloud Storage Object Creator](https://console.cloud.google.com/iam-admin/roles/details/roles%3Cstorage.objectCreator)



## Access control for previewing products

If you want users to be able to preview your product's listing as your customers see it in Cloud Marketplace, you must grant them the following role:

  * [Service Management API Consumer](https://console.cloud.google.com/iam-admin/roles/details/roles%3Cservicemanagement.serviceConsumer)



## Manage private offers

For users to create and manage private offers in the [Private offers](https://console.cloud.google.com/producer-portal/private-offers) tab of Producer Portal, grant them the following roles:

  * [Commerce Price Management Private Offers Admin](https://console.cloud.google.com/iam-admin/roles/details/roles%3Ccommercepricemanagement.privateOffersAdmin)
  * [Commerce Producer Viewer](https://cloud.google.com/iam/docs/roles-permissions/commerceproducer)



### View key events for private offers

For users to [view the history of an offer](https://cloud.google.com/marketplace/docs/partners/offers/view-offer-status#key-events) that your organization has published, grant them the [Commerce Price Management Events Viewer](https://console.cloud.google.com/iam-admin/roles/details/roles%3Ccommercepricemanagement.eventsViewer) role.

## Manage disbursements and payments

For users to create payment profiles to manage disbursement and payment settings in the [Payments](https://console.cloud.google.com/producer-portal/payments) tab of Producer Portal, grant them the following roles:

  * Commerce Business Enablement PaymentConfig Admin
  * [Commerce Producer Viewer](https://cloud.google.com/iam/docs/roles-permissions/commerceproducer)

**Note:** These roles enable users to create payment profiles. To add users to an existing payment profile, see [Controlling access to payment profiles](https://cloud.google.com/marketplace/docs/partners/receive-payments#adding-users).

## Access control for reselling

If you've allowed resellers to resell your Cloud Marketplace products, you can refer to the following guidelines for granting roles within your Google Cloud organization.

### View allowed and disallowed resellers

For users to view which resellers are allowed to resell your Cloud Marketplace products, or which resellers have been disallowed from reselling your products, grant them one of the following roles:

  * Commerce Business Enablement Configuration Viewer (`roles/commercebusinessenablement.viewer`)
  * Commerce Business Enablement Configuration Admin (`roles/commercebusinessenablement.admin`)



### Manage allowed resellers

For users to manage which resellers are allowed to resell your Cloud Marketplace products, grant them the Commerce Business Enablement Configuration Admin (`roles/commercebusinessenablement.admin`) role.

### View reseller discounts

For users to view resources and configurations related to reseller discounts in Producer Portal, grant them the following roles:

  * Commerce Business Enablement Reseller Discount Viewer (`roles/commercebusinessenablement.resellerDiscountViewer`)

  * [Commerce Price Management Viewer](https://cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.viewer) (`roles/commercepricemanagement.viewer`)




### Manage discounts

For users to create and manage resources and configurations related to reseller discounts in Producer Portal, grant them the following roles:

  * Commerce Business Enablement Reseller Discount Admin (`roles/commercebusinessenablement.resellerDiscountAdmin`)

  * [Commerce Price Management Viewer](https://cloud.google.com/iam/docs/roles-permissions/commercepricemanagement#commercepricemanagement.viewer) (`roles/commercepricemanagement.viewer`)




## Manage analytics and reports

To let users manage analytics, test accounts, sales lead management, and reports for your products in the [**Analytics**](https://console.cloud.google.com/producer-portal/analytics), [**Test billing accounts**](https://console.cloud.google.com/producer-portal/test-billing-accounts), [**Sales lead management**](https://console.cloud.google.com/producer-portal/sales-lead-management), and [**Reports**](https://console.cloud.google.com/producer-portal/partner-report) tabs of Producer Portal, grant them the following roles:

  * Commerce Business Enablement Configuration Admin (`roles/commercebusinessenablement.admin`)

  * [Commerce Producer Viewer](https://cloud.google.com/iam/docs/roles-permissions/commerceproducer) (`roles/commerceproducer.viewer`)

  * [Project Viewer](https://console.cloud.google.com/iam-admin/roles/details/roles%3Cviewer) (`roles/viewer`)




## List of IAM roles and permissions

You can grant users one or more of the following IAM roles.

Role | Permissions  
---|---  
  
#### Commerce Business Enablement Configuration Admin Beta

(`roles/commercebusinessenablement.admin`) Admin of Various Provider Configuration resources  |  `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.datasets.update` `commercebusinessenablement.leadgenConfig.*`

  * `commercebusinessenablement.leadgenConfig.get`
  * `commercebusinessenablement.leadgenConfig.update`

`commercebusinessenablement.partnerAccounts.*`

  * `commercebusinessenablement.partnerAccounts.get`
  * `commercebusinessenablement.partnerAccounts.list`

`commercebusinessenablement.partnerInfo.get` `commercebusinessenablement.resellerConfig.*`

  * `commercebusinessenablement.resellerConfig.get`
  * `commercebusinessenablement.resellerConfig.update`

`commercebusinessenablement.resellerRestrictions.*`

  * `commercebusinessenablement.resellerRestrictions.list`
  * `commercebusinessenablement.resellerRestrictions.update`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.operations.get` `serviceusage.services.enable` `serviceusage.services.get`  
  
#### Commerce Business Enablement Configuration Viewer Beta

(`roles/commercebusinessenablement.viewer`) Viewer of Various Provider Configuration resource  |  `commercebusinessenablement.leadgenConfig.get` `commercebusinessenablement.partnerAccounts.*`

  * `commercebusinessenablement.partnerAccounts.get`
  * `commercebusinessenablement.partnerAccounts.list`

`commercebusinessenablement.partnerInfo.get` `commercebusinessenablement.resellerConfig.get` `commercebusinessenablement.resellerRestrictions.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Commerce Business Enablement PaymentConfig Admin Beta

(`roles/commercebusinessenablement.paymentConfigAdmin`) Administration of Payment Configuration resource  |  `commercebusinessenablement.partnerInfo.get` `commercebusinessenablement.paymentConfig.*`

  * `commercebusinessenablement.paymentConfig.get`
  * `commercebusinessenablement.paymentConfig.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Commerce Business Enablement PaymentConfig Viewer Beta

(`roles/commercebusinessenablement.paymentConfigViewer`) Viewer of Payment Configuration resource  |  `commercebusinessenablement.partnerInfo.get` `commercebusinessenablement.paymentConfig.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Commerce Business Enablement Rebates Admin Beta

(`roles/commercebusinessenablement.rebatesAdmin`) Provides admin access to rebates  |  `commercebusinessenablement.operations.*`

  * `commercebusinessenablement.operations.cancel`
  * `commercebusinessenablement.operations.delete`
  * `commercebusinessenablement.operations.get`
  * `commercebusinessenablement.operations.list`

`commercebusinessenablement.partnerInfo.get` `commercebusinessenablement.refunds.*`

  * `commercebusinessenablement.refunds.cancel`
  * `commercebusinessenablement.refunds.create`
  * `commercebusinessenablement.refunds.delete`
  * `commercebusinessenablement.refunds.get`
  * `commercebusinessenablement.refunds.list`
  * `commercebusinessenablement.refunds.start`
  * `commercebusinessenablement.refunds.update`

  
  
#### Commerce Business Enablement Rebates Viewer Beta

(`roles/commercebusinessenablement.rebatesViewer`) Provides read-only access to rebates  |  `commercebusinessenablement.operations.get` `commercebusinessenablement.operations.list` `commercebusinessenablement.partnerInfo.get` `commercebusinessenablement.refunds.get` `commercebusinessenablement.refunds.list`  
  
#### Commerce Business Enablement Reseller Discount Admin Beta

(`roles/commercebusinessenablement.resellerDiscountAdmin`) Provides admin access to reseller discount offers  |  `commercebusinessenablement.partnerAccounts.*`

  * `commercebusinessenablement.partnerAccounts.get`
  * `commercebusinessenablement.partnerAccounts.list`

`commercebusinessenablement.partnerInfo.get` `commercebusinessenablement.resellerConfig.get` `commercebusinessenablement.resellerDiscountConfig.get` `commercebusinessenablement.resellerDiscountOffers.*`

  * `commercebusinessenablement.resellerDiscountOffers.cancel`
  * `commercebusinessenablement.resellerDiscountOffers.create`
  * `commercebusinessenablement.resellerDiscountOffers.list`

`commercebusinessenablement.resellerPrivateOfferPlans.*`

  * `commercebusinessenablement.resellerPrivateOfferPlans.cancel`
  * `commercebusinessenablement.resellerPrivateOfferPlans.create`
  * `commercebusinessenablement.resellerPrivateOfferPlans.delete`
  * `commercebusinessenablement.resellerPrivateOfferPlans.get`
  * `commercebusinessenablement.resellerPrivateOfferPlans.list`
  * `commercebusinessenablement.resellerPrivateOfferPlans.publish`
  * `commercebusinessenablement.resellerPrivateOfferPlans.update`

`resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Commerce Business Enablement Reseller Discount Viewer Beta

(`roles/commercebusinessenablement.resellerDiscountViewer`) Provides read-only access to reseller discount offers  |  `commercebusinessenablement.partnerAccounts.*`

  * `commercebusinessenablement.partnerAccounts.get`
  * `commercebusinessenablement.partnerAccounts.list`

`commercebusinessenablement.partnerInfo.get` `commercebusinessenablement.resellerConfig.get` `commercebusinessenablement.resellerDiscountConfig.get` `commercebusinessenablement.resellerDiscountOffers.list` `commercebusinessenablement.resellerPrivateOfferPlans.get` `commercebusinessenablement.resellerPrivateOfferPlans.list` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
