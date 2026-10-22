---
url: https://docs.cloud.google.com/marketplace/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:43.624640+00:00
---

# Access control with IAM  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Identity and Access Management (IAM) roles and permissions that you need to purchase and manage commercial products on Cloud Marketplace.

With IAM, you manage access control by defining _who_ (identity) has _what access_ (role) for _which resource_. For commercial apps on Cloud Marketplace, users in your Google Cloud organization require IAM roles to sign up for Cloud Marketplace plans, and to make changes to billing plans.

  * [Learn about managing billing for Cloud Marketplace products](https://docs.cloud.google.com/marketplace/docs/manage-billing).
  * [Learn about factors that affect your bill](https://docs.cloud.google.com/marketplace/docs/understanding-billing).
  * [Learn about the basic concepts of IAM](https://docs.cloud.google.com/iam/docs/overview).
  * [Learn about the hierarchy of Google Cloud resources](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).



## Before you begin

  * To grant Cloud Marketplace roles and permissions using `gcloud`, install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/downloads-interactive). Otherwise, you can grant roles using the Google Cloud console.



## Purchasing and managing roles

We recommend that you assign the [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing) IAM role to users who are purchasing services from Cloud Marketplace.

Users who want to access the services must have the [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) role, at a minimum.

For more granular control over users' permissions, you can create custom roles with the permissions that you want to grant.

### Product-specific requirements

To use the following services in a Google Cloud project, you must have the [Project Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) role:

  * Google Cloud Dataprep by Trifacta
  * Neo4j Aura Professional
  * Redis Enterprise Cloud



### List of IAM roles and permissions

You can grant users one or more of the following IAM roles. Depending on the role you are granting to users, you must also assign the role to a Google Cloud billing account, organization, or project. For details, see the section on Granting IAM roles to users.

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
  
## Granting IAM roles to users

From the roles in the preceding table, the `consumerprocurement.orderAdmin` and `consumerprocurement.orderViewer` roles must be assigned at the billing account or organization level, and the `consumerprocurement.entitlementManager` and `consumerprocurement.entitlementViewer` roles must be assigned at the project or organization level.

To grant roles to users using `gcloud`, run one of the following commands:

###  Organization 

You must have the [`resourcemanager.organizationAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager) role to assign roles at the organization level.
    
    
    gcloud organizations add-iam-policy-binding organization-id \
    --member=member --role=role-id
    

The placeholder values are:

  * organization-id: The numeric ID of the organization that you are granting the role for.
  * member: The user that you are granting access to.
  * role-id: The role ID, from the previous table.



###  Billing account 

You must have the [`billing.admin`](https://docs.cloud.google.com/iam/docs/roles-permissions/billing) role to assign roles at the billing account level.
    
    
    gcloud beta billing accounts set-iam-policy account-id \
    policy-file
    

The placeholder values are:

  * account-id: Your billing account ID, which you can get from the [Manage billing accounts page](https://console.cloud.google.com/billing).
  * policy-file: [An IAM policy file](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy), in JSON or YAML format. The policy file must contain the role IDs from the previous table, and the users that you are assigning the roles to.



###  Project 

You must have the [`resourcemanager.folderAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager) role to assign roles at the project level.
    
    
    gcloud projects add-iam-policy-binding project-id \
    --member=member --role=role-id
    

The placeholder values are:

  * project-id: The project that you are granting the role for.
  * member: The user that you are granting access to.
  * role-id: The role ID, from the previous table.



To grant roles to users using the Google Cloud console, see the IAM documentation on [Granting, changing, and revoking access for users](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Using custom roles with Cloud Marketplace

If you want granular control over the permissions you grant users, you can [create custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with the permissions that you want to grant.

If you're creating a custom role for users who purchase services from Cloud Marketplace, the role must include these permissions for the billing account they use to purchase services:

  * `billing.accounts.get`, which is typically granted with the [`roles/consumerprocurement.orderAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/billing) role.
  * `consumerprocurement.orders.get`, which is typically granted with the `roles/consumerprocurement.orderAdmin` role.
  * `consumerprocurement.orders.list`, which is typically granted with the `roles/consumerprocurement.orderAdmin` role.
  * `consumerprocurement.orders.place`, which is typically granted with the `roles/consumerprocurement.orderAdmin` role.
  * `consumerprocurement.accounts.get`, which is typically granted with the `roles/consumerprocurement.orderAdmin` role.
  * `consumerprocurement.accounts.list`, which is typically granted with the `roles/consumerprocurement.orderAdmin` role.
  * `consumerprocurement.accounts.create`, which is typically granted with the `roles/consumerprocurement.orderAdmin` role.
  * `consumerprocurement.consents.grant`, which is typically granted with the `roles/consumerprocurement.orderAdmin` role.



## Accessing partner websites with Single Sign-on (SSO)

Certain Cloud Marketplace API products support Single Sign-on (SSO) to a partner's external website. Authorized users within the organization have access to a "MANAGE ON PROVIDER" button on the product details page. This button directs users to the partner's website. In some cases, users are prompted to "Sign in with Google". In other cases, users are signed in a shared account context.

In order to access the SSO capability, users navigate to the product details page, and select an appropriate project. The project must be linked to a billing account where the plan has been purchased. For details about Cloud Marketplace API plan management, see [Managing billing plans](https://docs.cloud.google.com/marketplace/docs/manage-billing#manage_billing_plan).

Additionally, the user must have sufficient IAM permissions within the selected project. For most products, the `roles/consumerprocurement.entitlementManager` (or `roles/editor` [basic role](https://docs.cloud.google.com/iam/docs/roles-overview#basic)) is required.

### Minimal permissions for specific products

The following products can operate on a different set of permissions to access SSO capabilities:

  * Apache Kafka on Confluent Cloud
  * DataStax Astra for Apache Cassandra
  * Elastic Cloud
  * Neo4j Aura Professional
  * Redis Enterprise Cloud



For these products, you can use the following minimal permissions:

  * `consumerprocurement.entitlements.get`
  * `consumerprocurement.entitlements.list`
  * `serviceusage.services.get`
  * `serviceusage.services.list`
  * `resourcemanager.projects.get`



These permissions are typically granted with the `roles/consumerprocurement.entitlementManager` or `roles/consumerprocurement.entitlementViewer` roles.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
