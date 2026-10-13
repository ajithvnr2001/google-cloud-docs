---
url: https://docs.cloud.google.com/security-command-center/docs/dspm-use-data-security/
title: Use Data Security Posture Management \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:55.526868+00:00
---

# Use Data Security Posture Management  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/dspm-use-data-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Use Data Security Posture Management Stay organized with collections  Save and categorize content based on your preferences. 

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions.  Data Security Posture Management will be shut down on February 1, 2027. Learn more about the controls and [ alternative detection capabilities](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#data-security-framework). 

This document describes how you can enable and use [Data Security Posture Management (DSPM)](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security).

If you're on the Security Command Center Standard tier, [limited DSPM features](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security-standard) are available.

## Enable DSPM

You can enable DSPM during or after Security Command Center activation.

Complete the following to enable DSPM at the organization level:

  1. To get the permissions that you need to enable DSPM, ask your administrator to grant you the following IAM roles on your organization: 

     * [Organization Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`)
     * [Security Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  2. Enable DSPM using one of the following methods: Scenario | Instructions  
---|---  
You are new to or are migrating to Security Command Center Standard tier. | Enable DSPM by [activating Security Command Center Standard for an organization](https://docs.cloud.google.com/security-command-center/docs/migrate-standard-legacy).  
You haven't activated Security Command Center and want to use the Security Command Center Premium tier. | Enable DSPM by [activating Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/activate-scc-for-an-organization) for an organization.  
You haven't activated Security Command Center and want to use the Security Command Center Enterprise tier. | Enable DSPM by [activating Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier).  
You activated the Security Command Center Premium tier previously and want to enable DSPM. | Enable DSPM using the **Settings** page. [Go to the Settings page](https://console.cloud.google.com/security/command-center/config/services)  
You activated the Security Command Center Enterprise tier previously and want to enable DSPM. | Enable DSPM using the **Activate DSPM** page. [Go to Activate DSPM](https://console.cloud.google.com/security/command-center/config/service-activation;serviceName=dspm)  
  
For more information about Security Command Center tiers, see [Security Command Center service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers).

  3. [Enable discovery](https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery) of the resources that you want to protect with DSPM (Premium and Enterprise tiers only).



When you enable DSPM, the following services are also enabled (Premium and Enterprise tiers only):

  * [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview) to create, apply, and manage data security frameworks and cloud controls.
  * [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) to use data sensitivity signals for default data risk assessment.
  * [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) (part of Security Command Center) at the organization level to use the data access governance cloud control and the data flow governance cloud control. 
  * [AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) to help secure the lifecycle of your AI workloads (Security Command Center Enterprise tier only).



The [Data Security and Privacy Essentials framework](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#data-security-framework) is applied to the organization automatically (Premium and Enterprise tiers only).

(Premium and Enterprise tiers only) The DSPM service agent (`service-org-ORGANIZATION_ID@gcp-sa-dspm-hpsa.iam.gserviceaccount.com`) is created when you enable DSPM.

For information about the DSPM Identity and Access Management roles, see [Identity and Access Management for organization-level activations](https://docs.cloud.google.com/security-command-center/docs/access-control-org#dspm).

## Downgrading from the Premium or Enterprise tiers to the Standard tier

When you downgrade from the Premium or Enterprise tier to the [Standard](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security-standard) tier, your DSPM capabilities are affected as follows:

  * **Frameworks removed:** Deployed DSPM frameworks that depend on Premium or Enterprise features are removed.
  * **Feature access lost:** You lose access to advanced data security controls and custom data frameworks.
  * **Reverts to basic:** DSPM uses the basic data security checks included in the Security Essentials framework.
  * **Findings become inactive:** All findings previously generated by Premium or Enterprise tier frameworks become inactive. The only findings that remain available are those from the Security Essentials framework.



If you upgrade back to the Premium or Enterprise tier after downgrading to the Standard tier, framework deployments removed during the downgrade cannot be automatically recovered. You must manually re-deploy these frameworks and rebuild associated configurations.

## DSPM support for VPC Service Controls perimeters

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

When you enable DSPM in an organization that includes VPC Service Controls perimeters, consider the following:

  * Review the [limitations for Security Command Center](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_security_command_center).

  * You can't use a perimeter to help protect DSPM resources because all resources are at the organization level. To manage DSPM permissions, [use IAM](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  * Because DSPM is enabled at the organization level, it can't detect data risks and violations within a service perimeter. To permit access, complete the following:

    1. Make sure that you have the [required roles to configure VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/access-control) at the organization level.

    2. Configure the following ingress rule:
    
    - ingressFrom:
      identities:
      - serviceAccount: DSPM_SA_EMAIL_ADDRESS
      sources:
          - accessLevel: "*"
      ingressTo:
        operations: "*"
        resources: "*"
    

Replace DSPM_SA_EMAIL_ADDRESS with the email address of the DSPM service agent (`service-org-ORGANIZATION_ID@gcp-sa-dspm-hpsa.iam.gserviceaccount.com`).

The required IAM roles for the service agent are granted when you enable DSPM, and determine which operations the service agent can perform.

For more information about ingress rules, see [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).




## Create custom data security frameworks

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

If required, copy the [Data security and privacy essentials framework](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#data-security-framework) and customize it to meet your data security and compliance requirements. For instructions, see [Apply a framework](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework).

## Deploy advanced data security cloud controls

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

If required, add the advanced data security cloud controls to custom frameworks. These controls require additional configuration before you can deploy them. For instructions on deploying cloud controls and frameworks, see [Apply a framework](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework).

You can deploy frameworks that include advanced data security cloud controls to your organization, folders, projects, and App Hub applications in [folders configured for application management](https://docs.cloud.google.com/resource-manager/docs/manage-applications). To deploy the advanced data security cloud controls against applications, the framework can only include these controls. You must select the app-enabled folder and the application that you want the cloud controls to monitor. Applications in [host projects or a single-project boundary](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models) aren't supported.

Consider the following:

  * Review the information for each [advanced data security cloud control](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#data-security-cloud-controls-2) for limitations.

  * Complete the tasks for each rule, as described in the following table.

Rule | Additional configuration  
---|---  
[Data access governance cloud control](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#data-access) | 
    * Enable [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) for Cloud Storage and Agent Platform (where applicable in your environment). Set the data access permission type to `DATA_READ`. Enable the data access logs at the organization level or project level, depending on where you apply the Data access governance cloud control. Verify that only authorized principals are exempted from audit logging. Principals exempted from audit logging are also exempted from DSPM.
    * Add one or more allowed principals (up to a maximum of 200 principals), using one of the following formats: 
      * For a user, `principal://goog/subject/USER_EMAIL_ADDRESS` Example: `principal://goog/subject/alex@example.com`
      * For a group, `principalSet://goog/group/GROUP_EMAIL_ADDRESS` Example: `principalSet://goog/group/my-group@example.com`  
[Data flow governance cloud control](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#flow-governance) | 
    * Enable [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) for Cloud Storage and Agent Platform (where applicable in your environment). Set the data access permission type to `DATA_READ`. Enable the data access logs at the organization level or project level, depending on where you apply the Data access governance cloud control. Verify that only authorized principals are exempted from audit logging. Principals exempted from audit logging are also exempted from DSPM.
    * Specify allowed countries using the country codes that are defined in the [Unicode Common Locale Data Repository (CLDR)](https://www.unicode.org/cldr/charts/45/supplemental/territory_containment_un_m_49.html).  
[Data protection and key governance cloud control](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#data-protection) | Enable CMEK in [BigQuery](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption) and [Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/general/cmek).  
[Data deletion cloud controls](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#data-retention) | Set the retention periods. For example, to set a 90 day retention period in seconds, set the retention period to `777600`.  



## What's next

  * [Monitor your data security posture](https://docs.cloud.google.com/security-command-center/docs/use-dspm-dashboard).
  * [Review findings related to data security](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#dspm-findings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
