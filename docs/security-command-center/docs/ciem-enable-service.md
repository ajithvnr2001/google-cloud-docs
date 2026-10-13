---
url: https://docs.cloud.google.com/security-command-center/docs/ciem-enable-service/
title: Enable the CIEM detection service \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:59.912399+00:00
---

# Enable the CIEM detection service  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/ciem-enable-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Enable the CIEM detection service Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes how to set up the Security Command Center Cloud Infrastructure Entitlement Management (CIEM) detection service to detect identity issues in Google Cloud and other cloud platforms, like Amazon Web Services (AWS) and Microsoft Azure ([Preview](https://cloud.google.com/products#product-launch-stages)).

The CIEM detection service generates findings that alert you to potential identity and access security issues, such as highly privileged identities (accounts).

## Before you begin

Before you enable the CIEM detection service, complete the following tasks:

  * Purchase and activate Security Command Center for your organization. For instructions, see one of the following:

    * [Activate the Security Command Center Standard tier](https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier) for an organization.
    * [Activate the Security Command Center Premium tier](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier) for an organization.
    * [Activate the Security Command Center Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier).
  * Learn about [Security Command Center's CIEM capabilities](https://docs.cloud.google.com/security-command-center/docs/ciem-overview).




## Set up permissions

The following sections describe the permissions required to configure CIEM.

### Permissions for Standard-legacy, Standard, and Premium tier activations

After you activate Security Command Center, no additional permissions are needed to configure CIEM. For more information, see Configure CIEM with Google Cloud.

### Permissions for Enterprise tier activations

To get the permissions that you need to enable CIEM, ask your administrator to grant you the following IAM roles on your Google Cloud organization: 

  * Chronicle API Admin (roles/chronicle.admin) 
  * Chronicle SOAR Admin (roles/chronicle.soarAdmin) 
  * Chronicle Service Admin (roles/chroniclesm.admin) 
  * Cloud Asset Owner (roles/cloudasset.owner) 
  * Create Service Accounts (roles/iam.serviceAccountCreator) 
  * Folder IAM Admin (roles/resourcemanager.folderIamAdmin) 
  * IAM Recommender Admin (roles/recommender.iamAdmin) 
  * Organization Administrator (roles/resourcemanager.organizationAdmin) 
  * Organization Role Administrator (roles/iam.roleAdmin) 
  * Project Creator (roles/resourcemanager.projectCreator) 
  * Project IAM Admin (roles/resourcemanager.projectIamAdmin) 
  * Security Admin (roles/iam.securityAdmin) 
  * Security Center Admin (roles/securitycenter.admin) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure CIEM for Google Cloud

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Cloud Infrastructure Entitlement Management services are enabled by default in your Google Cloud environment and don't require additional configuration.

After you activate Security Command Center, these services generate and publish findings related to Google Cloud resources to Security Command Center.

## Configure CIEM for AWS

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

To enable the CIEM detection service for AWS, do the following:

  * **Set up Amazon Web Services (AWS) integration** : Connect your AWS environment to Security Command Center. For instructions, see [Connect to AWS](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws).
  * **Configure integrations** : Set up optional Security Command Center integrations such as connecting to your ticketing systems: 
    * To connect your ticketing system, [integrate Security Command Center Enterprise with ticketing systems](https://docs.cloud.google.com/security-command-center/docs/integrate-ticketing-systems).
    * To synchronize case data, [enable synchronization for cases](https://docs.cloud.google.com/security-command-center/docs/synchronize-case-data#enable-case-sync).
  * **Configure log ingestion** : To configure log ingestion appropriately for CIEM, [Configure AWS log ingestion for CIEM](https://docs.cloud.google.com/security-command-center/docs/connect-secops-aws#ciem-log-ingestion).



## Configure CIEM for Microsoft Azure

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

To enable the CIEM detection service for Microsoft Azure, do the following:

  * **Set up Microsoft Azure integration** : Connect your Microsoft Azure environment to Security Command Center. For instructions, see [Connect to Microsoft Azure](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure).
  * **Configure integrations** : Set up optional Security Command Center integrations such as connecting to your ticketing systems: 
    * To connect your ticketing system, [Integrate Security Command Center Enterprise with ticketing systems](https://docs.cloud.google.com/security-command-center/docs/integrate-ticketing-systems).
    * To synchronize case data, [enable synchronization for cases](https://docs.cloud.google.com/security-command-center/docs/synchronize-case-data#enable-case-sync).
  * **Configure log ingestion** : See [Configure Microsoft Azure log ingestion for CIEM](https://docs.cloud.google.com/security-command-center/docs/connect-secops-azure#ciem-log-ingestion-azure).



## What's next

  * Learn how to [investigate identity and access findings](https://docs.cloud.google.com/security-command-center/docs/ciem-identity-access-findings).
  * Learn how to [review cases for identity and access issues](https://docs.cloud.google.com/security-command-center/docs/ciem-identity-access-cases).
  * Learn more about [Security Command Center roles](https://docs.cloud.google.com/security-command-center/docs/access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
