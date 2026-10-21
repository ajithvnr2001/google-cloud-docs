---
url: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-enable/
title: Enable Compliance Manager \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:45.796868+00:00
---

# Enable Compliance Manager  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Enable Compliance Manager Stay organized with collections  Save and categorize content based on your preferences. 

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Enable Compliance Manager so that you can apply frameworks to your Google Cloud organization or project.

## Before you begin

Complete these tasks before you enable Compliance Manager.

To get the permissions that you need to enable Compliance Manager, ask your administrator to grant you the following IAM roles: 

  * Enable for an organization: 
    * [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) on the organization
    * [Security Center Admin Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`) on the organization
  * Enable for a project: 
    * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the project
    * [Security Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable Compliance Manager

Complete the following steps to enable Compliance Manager at the organization or project level:

  1. Enable Compliance Manager using one of the following methods: 

Scenario | Instructions  
---|---  
You haven't activated Security Command Center and want to use the Security Command Center Standard tier. | Enable Compliance Manager by [activating Security Command Center Standard](https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier). For new organizations that activate the Standard tier, Compliance Manager is automatically enabled.  
You are already using the Security Command Center Standard tier. | No action required.   
Compliance Manager is enabled through a backend upgrade. For more information, see [Migration and activation of the Standard tier](https://docs.cloud.google.com/security-command-center/docs/migrate-standard-legacy).  
You haven't activated Security Command Center and want to use the Security Command Center Premium tier. | Enable Compliance Manager by [activating Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/activate-scc-for-an-organization).  
You haven't activated Security Command Center and want to use the Security Command Center Enterprise tier. | Enable Compliance Manager by [activating Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier).  
You activated the Security Command Center Premium tier previously and want to enable Compliance Manager. | Enable Compliance Manager using the **Settings** page. [Go to the Settings page](https://console.cloud.google.com/security/command-center/config/services)  
You activated the Security Command Center Enterprise tier previously and want to enable Compliance Manager. | Enable Compliance Manager using the **Activate Compliance Manager** page. [Go to Activate Compliance Manager](https://console.cloud.google.com/security/command-center/config/service-activation;serviceName=complianceManager)  
You activated any Security Command Center service tier previously and want to enable Compliance Manager for a single project. | Select the project scope and enable Compliance Manager using the **Settings** page. [Go to the Settings page](https://console.cloud.google.com/security/command-center/config/services)  
  
For more information about Security Command Center tiers, see [Security Command Center service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers).

Compliance Manager doesn't support [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/security-command-center/docs/cmek).

When you enable Compliance Manager, the following services are also enabled:

     * (Premium and Enterprise tiers only) [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) to use data sensitivity signals for default data risk assessment.
     * (Premium and Enterprise tiers only) [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) (part of Security Command Center) at the organization level.
     * [Data Security Posture Management](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security) for data security frameworks.
     * (Premium and Enterprise tiers only) [AI protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) for AI security frameworks.

For the Standard tier, AI-related findings are evaluated by using the baseline security controls that are included in the default Security Essentials framework.

The Cloud Security Compliance service agent is created when you enable Compliance Manager. Compliance Manager uses a service agent at the organization-level (`service-org-`ORGANIZATION_ID`@gcp-sa-csc-hpsa.iam.gserviceaccount.com`) or the project-level (`service-`PROJECT_NUMBER`@gcp-sa-csc-hpsa.iam.gserviceaccount.com`) to access resources, depending on your activation scope.

  2. To complete audits with Compliance Manager, enable [Audit Manager](https://docs.cloud.google.com/audit-manager/docs/enable-audit-manager).




For Security Command Center Standard, the Security Essentials framework is applied to the organization automatically.

For Security Command Center Premium, frameworks are not applied to the organization automatically.

For Security Command Center Enterprise, the following frameworks are applied to the organization automatically:

  * Google Recommended AI Essentials - Gemini Enterprise Agent Platform
  * Data Security and Privacy Essentials

**Note:** You can deploy frameworks to individual projects based on your compliance needs.

## Manage service tiers in Compliance Manager

Compliance Manager features vary by Security Command Center [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers). The Standard tier provides a security baseline through the [Security Essentials](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#security-essentials) framework. The Premium and Enterprise tiers include advanced capabilities, such as [built-in regulatory frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview#frameworks-gcp), [audit capabilities](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit), and [custom cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls#create-custom-cloud-control).

### Downgrade to Security Command Center Standard service tier

If you downgrade your organization or project to the Standard tier, you lose access to advanced capabilities like [built-in regulatory frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview#frameworks-gcp), [audit capabilities](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit), and [custom cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls#create-custom-cloud-control). Review the effects before you downgrade because you may permanently lose or alter some data.

#### Impact on frameworks and deployments

When you downgrade to Security Command Center Standard, the following changes occur to frameworks and deployments:

  * The system automatically removes all built-in framework deployments (excluding [Security Essentials](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#security-essentials)) without warning or notification.
  * If a custom framework contains a [cloud control](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls) that isn't supported in the Standard tier, the system removes the entire framework.



#### Impact on findings

When you downgrade to Security Command Center Standard, the following changes occur to findings:

  * The system marks the findings associated with unsupported frameworks as inactive.
  * You have read-only access to inactive findings for seven days, after which they expire and become unavailable.



#### Impact on custom cloud controls

When you downgrade to Security Command Center Standard, the following changes occur to [custom cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-write-cel-expressions):

  * You can't create or manage custom cloud controls.
  * Custom cloud controls are preserved but become inactive and unusable. The system automatically removes any active framework deployments that contain custom cloud controls.
  * If you downgrade to Security Command Center Standard tier, the IAM permissions related to custom cloud controls become ineffective. You don't have to manually revoke them.



#### Impact on audit capabilities

[Audit capabilities](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit) are exclusive to Security Command Center Premium and Enterprise tiers.

Audit reports and evidence in your Cloud Storage buckets are managed by [Object Lifecycle Management rules](https://docs.cloud.google.com/storage/docs/lifecycle), not Security Command Center retention policies.

### Upgrade again to Security Command Center Premium or Enterprise service tiers

When you return to the Security Command Center Premium or Enterprise service tiers, the advanced features are restored. The upgrade has the following effects on your deployments:

  * Inactive custom controls become available again.
  * Framework deployments removed during the downgrade are not recoverable. You must manually re-deploy your frameworks.



## What's next

  * [Configure IAM roles for your compliance users](https://docs.cloud.google.com/security-command-center/docs/access-control-org#compliance-manager)
  * [Configure support for VPC Service Controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-configure-vpc-sc)
  * [Manage a framework](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework)
  * [Configure Data Security Posture Management](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security)
  * [Configure AI Protection](https://docs.cloud.google.com/security-command-center/docs/configure-ai-protection)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
