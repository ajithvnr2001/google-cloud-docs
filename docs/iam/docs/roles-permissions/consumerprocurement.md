---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement/
title: Cloud Commerce Consumer Procurement roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:27.293626+00:00
---

# Cloud Commerce Consumer Procurement roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Commerce Consumer Procurement roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Commerce Consumer Procurement. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Commerce Consumer Procurement roles

Role | Permissions  
---|---  
  
#### Consumer Procurement Entitlement Manager 

(`roles/consumerprocurement.entitlementManager`) Allows managing entitlements and enabling, disabling, and inspecting service states for a consumer project.  |  `commerceoffercatalog.offers.get` `consumerprocurement.consents.check` `consumerprocurement.consents.grant` `consumerprocurement.consents.list` `consumerprocurement.consents.revoke` `consumerprocurement.entitlements.*`

  * `consumerprocurement.entitlements.get`
  * `consumerprocurement.entitlements.list`

`consumerprocurement.freeTrials.*`

  * `consumerprocurement.freeTrials.create`
  * `consumerprocurement.freeTrials.get`
  * `consumerprocurement.freeTrials.list`

`orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.operations.get` `serviceusage.services.disable` `serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Consumer Procurement Entitlement Viewer 

(`roles/consumerprocurement.entitlementViewer`) Allows inspecting entitlements and service states for a consumer project.  |  `commerceoffercatalog.offers.get` `consumerprocurement.consents.check` `consumerprocurement.consents.list` `consumerprocurement.entitlements.*`

  * `consumerprocurement.entitlements.get`
  * `consumerprocurement.entitlements.list`

`consumerprocurement.freeTrials.get` `consumerprocurement.freeTrials.list` `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Consumer Procurement Events Viewer 

(`roles/consumerprocurement.eventsViewer`) Allows viewing key events for an offer  |  `consumerprocurement.events.*`

  * `consumerprocurement.events.get`
  * `consumerprocurement.events.list`

  
  
#### Consumer Procurement License Pool Editor 

(`roles/consumerprocurement.licensePoolEditor`) Allows managing license pools and license assignments.  |  `consumerprocurement.licensePools.*`

  * `consumerprocurement.licensePools.assign`
  * `consumerprocurement.licensePools.enumerateLicensedUsers`
  * `consumerprocurement.licensePools.get`
  * `consumerprocurement.licensePools.unassign`
  * `consumerprocurement.licensePools.update`

  
  
#### Consumer Procurement License Pool Viewer 

(`roles/consumerprocurement.licensePoolViewer`) Allows viewing license pools and license assignments.  |  `consumerprocurement.licensePools.enumerateLicensedUsers` `consumerprocurement.licensePools.get`  
  
#### Consumer Procurement Order Administrator 

(`roles/consumerprocurement.orderAdmin`) Allows managing purchases.  |  `billing.accounts.get` `billing.accounts.getIamPolicy` `billing.accounts.list` `billing.accounts.redeemPromotion` `billing.credits.list` `billing.resourceAssociations.create` `commerceoffercatalog.*`

  * `commerceoffercatalog.agreements.get`
  * `commerceoffercatalog.agreements.list`
  * `commerceoffercatalog.documents.get`
  * `commerceoffercatalog.documents.list`
  * `commerceoffercatalog.offers.get`

`consumerprocurement.accounts.*`

  * `consumerprocurement.accounts.create`
  * `consumerprocurement.accounts.delete`
  * `consumerprocurement.accounts.get`
  * `consumerprocurement.accounts.list`

`consumerprocurement.consents.check` `consumerprocurement.consents.grant` `consumerprocurement.consents.list` `consumerprocurement.consents.revoke` `consumerprocurement.events.*`

  * `consumerprocurement.events.get`
  * `consumerprocurement.events.list`

`consumerprocurement.licensePools.*`

  * `consumerprocurement.licensePools.assign`
  * `consumerprocurement.licensePools.enumerateLicensedUsers`
  * `consumerprocurement.licensePools.get`
  * `consumerprocurement.licensePools.unassign`
  * `consumerprocurement.licensePools.update`

`consumerprocurement.orderAttributions.*`

  * `consumerprocurement.orderAttributions.get`
  * `consumerprocurement.orderAttributions.list`
  * `consumerprocurement.orderAttributions.update`

`consumerprocurement.orders.*`

  * `consumerprocurement.orders.cancel`
  * `consumerprocurement.orders.get`
  * `consumerprocurement.orders.list`
  * `consumerprocurement.orders.modify`
  * `consumerprocurement.orders.place`

`discoveryengine.billingAccountLicenseConfigs.*`

  * `discoveryengine.billingAccountLicenseConfigs.distribute`
  * `discoveryengine.billingAccountLicenseConfigs.get`
  * `discoveryengine.billingAccountLicenseConfigs.list`
  * `discoveryengine.billingAccountLicenseConfigs.retract`

  
  
#### Consumer Procurement Order Viewer 

(`roles/consumerprocurement.orderViewer`) Allows inspecting purchases.  |  `billing.accounts.get` `billing.accounts.getIamPolicy` `billing.accounts.list` `billing.credits.list` `commerceoffercatalog.*`

  * `commerceoffercatalog.agreements.get`
  * `commerceoffercatalog.agreements.list`
  * `commerceoffercatalog.documents.get`
  * `commerceoffercatalog.documents.list`
  * `commerceoffercatalog.offers.get`

`consumerprocurement.accounts.get` `consumerprocurement.accounts.list` `consumerprocurement.consents.check` `consumerprocurement.consents.list` `consumerprocurement.licensePools.enumerateLicensedUsers` `consumerprocurement.licensePools.get` `consumerprocurement.orderAttributions.get` `consumerprocurement.orderAttributions.list` `consumerprocurement.orders.get` `consumerprocurement.orders.list` `discoveryengine.billingAccountLicenseConfigs.get` `discoveryengine.billingAccountLicenseConfigs.list`  
  
#### Consumer Procurement Administrator 

(`roles/consumerprocurement.procurementAdmin`) Allows managing purchases, consents at both billing account and project level.  |  `billing.accounts.get` `billing.accounts.getIamPolicy` `billing.accounts.list` `billing.accounts.redeemPromotion` `billing.credits.list` `billing.resourceAssociations.create` `commerceoffercatalog.*`

  * `commerceoffercatalog.agreements.get`
  * `commerceoffercatalog.agreements.list`
  * `commerceoffercatalog.documents.get`
  * `commerceoffercatalog.documents.list`
  * `commerceoffercatalog.offers.get`

`consumerprocurement.*`

  * `consumerprocurement.accounts.create`
  * `consumerprocurement.accounts.delete`
  * `consumerprocurement.accounts.get`
  * `consumerprocurement.accounts.list`
  * `consumerprocurement.consents.allowProjectGrant`
  * `consumerprocurement.consents.check`
  * `consumerprocurement.consents.grant`
  * `consumerprocurement.consents.list`
  * `consumerprocurement.consents.revoke`
  * `consumerprocurement.entitlements.get`
  * `consumerprocurement.entitlements.list`
  * `consumerprocurement.events.get`
  * `consumerprocurement.events.list`
  * `consumerprocurement.freeTrials.create`
  * `consumerprocurement.freeTrials.get`
  * `consumerprocurement.freeTrials.list`
  * `consumerprocurement.licensePools.assign`
  * `consumerprocurement.licensePools.enumerateLicensedUsers`
  * `consumerprocurement.licensePools.get`
  * `consumerprocurement.licensePools.unassign`
  * `consumerprocurement.licensePools.update`
  * `consumerprocurement.orderAttributions.get`
  * `consumerprocurement.orderAttributions.list`
  * `consumerprocurement.orderAttributions.update`
  * `consumerprocurement.orders.cancel`
  * `consumerprocurement.orders.get`
  * `consumerprocurement.orders.list`
  * `consumerprocurement.orders.modify`
  * `consumerprocurement.orders.place`

`discoveryengine.billingAccountLicenseConfigs.*`

  * `discoveryengine.billingAccountLicenseConfigs.distribute`
  * `discoveryengine.billingAccountLicenseConfigs.get`
  * `discoveryengine.billingAccountLicenseConfigs.list`
  * `discoveryengine.billingAccountLicenseConfigs.retract`

`orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.operations.get` `serviceusage.services.disable` `serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Consumer Procurement Viewer 

(`roles/consumerprocurement.procurementViewer`) Allows inspecting purchases, consents and entitlements and service states for a consumer project.  |  `billing.accounts.get` `billing.accounts.getIamPolicy` `billing.accounts.list` `billing.credits.list` `commerceoffercatalog.*`

  * `commerceoffercatalog.agreements.get`
  * `commerceoffercatalog.agreements.list`
  * `commerceoffercatalog.documents.get`
  * `commerceoffercatalog.documents.list`
  * `commerceoffercatalog.offers.get`

`consumerprocurement.accounts.get` `consumerprocurement.accounts.list` `consumerprocurement.consents.check` `consumerprocurement.consents.list` `consumerprocurement.entitlements.*`

  * `consumerprocurement.entitlements.get`
  * `consumerprocurement.entitlements.list`

`consumerprocurement.freeTrials.get` `consumerprocurement.freeTrials.list` `consumerprocurement.licensePools.enumerateLicensedUsers` `consumerprocurement.licensePools.get` `consumerprocurement.orderAttributions.get` `consumerprocurement.orderAttributions.list` `consumerprocurement.orders.get` `consumerprocurement.orders.list` `discoveryengine.billingAccountLicenseConfigs.get` `discoveryengine.billingAccountLicenseConfigs.list` `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
## Cloud Commerce Consumer Procurement permissions

Permission | Included in roles  
---|---  
  
#### `consumerprocurement.accounts.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)   
  
#### `consumerprocurement.accounts.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)   
  
#### `consumerprocurement.accounts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`)  [Account Hierarchy Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.linkAdmin) (`roles/billing.linkAdmin`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Order Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderViewer) (`roles/consumerprocurement.orderViewer`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)  [Consumer Procurement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementViewer) (`roles/consumerprocurement.procurementViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `consumerprocurement.accounts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Account Hierarchy Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.linkAdmin) (`roles/billing.linkAdmin`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Order Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderViewer) (`roles/consumerprocurement.orderViewer`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)  [Consumer Procurement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementViewer) (`roles/consumerprocurement.procurementViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `consumerprocurement.consents.allowProjectGrant`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)   
  
#### `consumerprocurement.consents.check`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`)  [Account Hierarchy Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.linkAdmin) (`roles/billing.linkAdmin`)  [Consumer Procurement Entitlement Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementManager) (`roles/consumerprocurement.entitlementManager`)  [Consumer Procurement Entitlement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementViewer) (`roles/consumerprocurement.entitlementViewer`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Order Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderViewer) (`roles/consumerprocurement.orderViewer`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)  [Consumer Procurement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementViewer) (`roles/consumerprocurement.procurementViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `consumerprocurement.consents.grant`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Consumer Procurement Entitlement Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementManager) (`roles/consumerprocurement.entitlementManager`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)   
  
#### `consumerprocurement.consents.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Account Hierarchy Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.linkAdmin) (`roles/billing.linkAdmin`)  [Consumer Procurement Entitlement Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementManager) (`roles/consumerprocurement.entitlementManager`)  [Consumer Procurement Entitlement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementViewer) (`roles/consumerprocurement.entitlementViewer`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Order Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderViewer) (`roles/consumerprocurement.orderViewer`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)  [Consumer Procurement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementViewer) (`roles/consumerprocurement.procurementViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `consumerprocurement.consents.revoke`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Consumer Procurement Entitlement Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementManager) (`roles/consumerprocurement.entitlementManager`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)   
  
#### `consumerprocurement.entitlements.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Commerce Organization Governance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/commerceorggovernance#commerceorggovernance.admin) (`roles/commerceorggovernance.admin`)  [Commerce Organization Governance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/commerceorggovernance#commerceorggovernance.viewer) (`roles/commerceorggovernance.viewer`)  [Discovery Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) (`roles/discoveryengine.admin`)  [Governed Marketplace User](https://docs.cloud.google.com/iam/docs/roles-permissions/commerceorggovernance#commerceorggovernance.user) (`roles/commerceorggovernance.user`)  [Consumer Procurement Entitlement Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementManager) (`roles/consumerprocurement.entitlementManager`)  [Consumer Procurement Entitlement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementViewer) (`roles/consumerprocurement.entitlementViewer`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)  [Consumer Procurement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementViewer) (`roles/consumerprocurement.procurementViewer`)  [Gemini Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `consumerprocurement.entitlements.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Commerce Organization Governance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/commerceorggovernance#commerceorggovernance.admin) (`roles/commerceorggovernance.admin`)  [Commerce Organization Governance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/commerceorggovernance#commerceorggovernance.viewer) (`roles/commerceorggovernance.viewer`)  [Discovery Engine Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) (`roles/discoveryengine.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Governed Marketplace User](https://docs.cloud.google.com/iam/docs/roles-permissions/commerceorggovernance#commerceorggovernance.user) (`roles/commerceorggovernance.user`)  [Consumer Procurement Entitlement Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementManager) (`roles/consumerprocurement.entitlementManager`)  [Consumer Procurement Entitlement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementViewer) (`roles/consumerprocurement.entitlementViewer`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)  [Consumer Procurement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementViewer) (`roles/consumerprocurement.procurementViewer`)  [Gemini Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `consumerprocurement.events.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Consumer Procurement Events Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.eventsViewer) (`roles/consumerprocurement.eventsViewer`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)   
  
#### `consumerprocurement.events.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Consumer Procurement Events Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.eventsViewer) (`roles/consumerprocurement.eventsViewer`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `consumerprocurement.freeTrials.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Consumer Procurement Entitlement Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementManager) (`roles/consumerprocurement.entitlementManager`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)   
  
#### `consumerprocurement.freeTrials.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Consumer Procurement Entitlement Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementManager) (`roles/consumerprocurement.entitlementManager`)  [Consumer Procurement Entitlement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementViewer) (`roles/consumerprocurement.entitlementViewer`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)  [Consumer Procurement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementViewer) (`roles/consumerprocurement.procurementViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `consumerprocurement.freeTrials.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Consumer Procurement Entitlement Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementManager) (`roles/consumerprocurement.entitlementManager`)  [Consumer Procurement Entitlement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementViewer) (`roles/consumerprocurement.entitlementViewer`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)  [Consumer Procurement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementViewer) (`roles/consumerprocurement.procurementViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `consumerprocurement.licensePools.assign`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Consumer Procurement License Pool Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.licensePoolEditor) (`roles/consumerprocurement.licensePoolEditor`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)   
  
#### `consumerprocurement.licensePools.enumerateLicensedUsers`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Consumer Procurement License Pool Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.licensePoolEditor) (`roles/consumerprocurement.licensePoolEditor`)  [Consumer Procurement License Pool Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.licensePoolViewer) (`roles/consumerprocurement.licensePoolViewer`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Order Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderViewer) (`roles/consumerprocurement.orderViewer`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)  [Consumer Procurement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementViewer) (`roles/consumerprocurement.procurementViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `consumerprocurement.licensePools.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Consumer Procurement License Pool Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.licensePoolEditor) (`roles/consumerprocurement.licensePoolEditor`)  [Consumer Procurement License Pool Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.licensePoolViewer) (`roles/consumerprocurement.licensePoolViewer`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Order Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderViewer) (`roles/consumerprocurement.orderViewer`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)  [Consumer Procurement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementViewer) (`roles/consumerprocurement.procurementViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `consumerprocurement.licensePools.unassign`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Consumer Procurement License Pool Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.licensePoolEditor) (`roles/consumerprocurement.licensePoolEditor`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)   
  
#### `consumerprocurement.licensePools.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Consumer Procurement License Pool Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.licensePoolEditor) (`roles/consumerprocurement.licensePoolEditor`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)   
  
#### `consumerprocurement.orderAttributions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`)  [Account Hierarchy Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.linkAdmin) (`roles/billing.linkAdmin`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Order Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderViewer) (`roles/consumerprocurement.orderViewer`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)  [Consumer Procurement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementViewer) (`roles/consumerprocurement.procurementViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `consumerprocurement.orderAttributions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Account Hierarchy Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.linkAdmin) (`roles/billing.linkAdmin`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Order Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderViewer) (`roles/consumerprocurement.orderViewer`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)  [Consumer Procurement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementViewer) (`roles/consumerprocurement.procurementViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `consumerprocurement.orderAttributions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)   
  
#### `consumerprocurement.orders.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)   
  
#### `consumerprocurement.orders.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`)  [Account Hierarchy Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.linkAdmin) (`roles/billing.linkAdmin`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Order Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderViewer) (`roles/consumerprocurement.orderViewer`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)  [Consumer Procurement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementViewer) (`roles/consumerprocurement.procurementViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `consumerprocurement.orders.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Account Hierarchy Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.linkAdmin) (`roles/billing.linkAdmin`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Order Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderViewer) (`roles/consumerprocurement.orderViewer`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)  [Consumer Procurement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementViewer) (`roles/consumerprocurement.procurementViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `consumerprocurement.orders.modify`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)   
  
#### `consumerprocurement.orders.place`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Consumer Procurement Order Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.orderAdmin) (`roles/consumerprocurement.orderAdmin`)  [Consumer Procurement Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.procurementAdmin) (`roles/consumerprocurement.procurementAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
