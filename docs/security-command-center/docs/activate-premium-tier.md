---
url: https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier/
title: Activate Security Command Center Premium tier for an organization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:11.874801+00:00
---

# Activate Security Command Center Premium tier for an organization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Activate Security Command Center Premium tier for an organization Stay organized with collections  Save and categorize content based on your preferences. 

Premium [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

Security Command Center Premium lets you evaluate your security posture, identify vulnerabilities, and detect threats across [supported cloud resources](https://docs.cloud.google.com/security-command-center/docs/supported-asset-types) in your organization. Activating the Premium tier in the Google Cloud console automatically turns on a suite of built-in detection services.

For feature capabilities across tiers, see [Security Command Center service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers). To configure a different scope or tier, see the guides for [Standard tier](https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier), [Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier), or [project-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-for-a-project).

## Before you begin

Before you activate Security Command Center Premium for an organization, you need to do the following:

  * Obtain specific Identity and Access Management (IAM) roles and permissions.
  * Optional: Enable additional APIs.
  * Review your organization policies, if applicable to your organization.
  * If you plan to enable data residency, review [Planning for data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) and determine which location to use.
  * If you plan to use a customer-managed encryption key (CMEK), complete the required tasks for [enabling CMEK for Security Command Center](https://docs.cloud.google.com/security-command-center/docs/cmek#before_you_begin).



You can configure data residency and data encryption when you activate Security Command Center. To change these settings after you activate Security Command Center Standard or Premium, see [Modify data residency or data encryption configuration](https://docs.cloud.google.com/security-command-center/docs/modify-data-residency-encryption).

### Required roles

To get the permissions that you need to activate Security Command Center for an organization, ask your administrator to grant you the following IAM roles on your organization: 

  * [Security Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)
  * [Organization Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable the Security Center Management API

If you plan to use the Security Center Management API, enable this API in the project where you plan to call it: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=securitycentermanagement.googleapis.com)

### Review organization policies

If your organization policies are set to [restrict identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains), confirm the following:

  * You must be signed in to the Google Cloud console on an account that's in an allowed domain.
  * Your service accounts must be in an allowed domain, or members of a group within your domain. This requirement lets you allow services that use the `@*.gserviceaccount.com` service account to access resources when domain-restricted sharing is enabled.



If your organization policies are set to [restrict resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources), verify that the following APIs are [allowed by your policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources#setting_the_organization_policy):

  * `cloudsecuritycompliance.googleapis.com`
  * `securitycenter.googleapis.com`
  * `securitycentermanagement.googleapis.com`



## Activate Security Command Center Premium

You can activate Security Command Center Premium for an organization through the Google Cloud console.

  1. In the Google Cloud console, go to the Security Command Center welcome page.

[Go to Security Command Center](https://console.cloud.google.com/projectselector2/security/command-center/welcome?supportedpurview=organizationId)

  2. If you want to [enable data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#locations), open a [jurisdictional console](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints#jurisdictional-console) using the URL that matches the location you plan to configure.

You must use the jurisdictional Google Cloud console to activate Security Command Center with data residency controls and modify the data residency configuration after activation. For details, see [About the jurisdictional Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints#jurisdictional-console).

**Caution:** Security Command Center doesn't validate your data residency location against any organization policies that enforce the [resource locations constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations), `gcp.resourceLocations`. When you configure data residency, you must select a location that's consistent with your organization policies. 
  3. Select the organization that you want to enable Security Command Center Premium for, and then click **Select**.

  4. On the welcome page, select **Start a Premium free trial**.

**Note:** Your Premium free trial lasts for 30 days. When your trial ends, your organization will automatically transition to the Premium pay-as-you-go plan, and your billing account will be charged accordingly.

To cancel your Premium trial and avoid pay-as-you-go charges, you must downgrade to the Standard tier before the trial period ends. You can downgrade at any time during the trial. For detailed instructions, see [Downgrade from the Premium tier to the Standard tier](https://docs.cloud.google.com/security-command-center/docs/modify-premium-tier#premium-to-standard).

If you want to purchase a Premium subscription, see [Premium tier: Subscription-based pricing](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) for details.

  5. Optional: To confirm the data residency configuration or change the data encryption configuration, click **Show more**.

     * If you are using a jurisdictional console, the **Data residency** field displays **Enable** and the **Location** field displays the same location as the jurisdictional console. To change the location, open the console using a URL that matches the location you want to configure. 
     * The default data encryption configuration uses Google-owned and Google-managed encryption keys. To use a Cloud Key Management Service key, click **Edit data encryption** , and then do the following: 
       1. Select **Cloud KMS key**.
       2. Select a project.
       3. Select a key. You can select a key from any Google Cloud project, including projects in other organizations. Only keys in compatible locations are displayed in the list.

To learn which key locations are compatible with Security Command Center, see [Determine the key location](https://docs.cloud.google.com/security-command-center/docs/cmek#key-location). 

If your organization uses [CMEK organization policies](https://docs.cloud.google.com/security-command-center/docs/cmek#org-policies), you might only have the option to choose CMEK or specific keys. 

During the activation process, Security Command Center grants the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role to the [Cloud Security Command Center Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#cloud-security-command-center-service-agent) on the Cloud KMS key.

  6. Click **Activate**.




As results become available, they are displayed in the console. Then you can use the Google Cloud console to review and remediate Google Cloud security and data risks.

Security Command Center completes its first full scan within 24 hours. There might be a delay before scans are started for some services. For more information, see [When to expect findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview).

## Services for Security Command Center Premium

After you activate Security Command Center Premium, specific services are automatically enabled, and service agents are created so that these services can act on your behalf.

### Services

Security Command Center uses [detection services](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources) to detect security issues in your cloud environments. The following services are enabled when you activate Security Command Center Premium:

  * [AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview)

  * [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview)

  * [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview)

For Container Threat Detection to function, make sure that your clusters are on a supported version of Google Kubernetes Engine (GKE) and that your GKE clusters are configured correctly. For more information, see [Use Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection).

  * [Data Security Posture Management (DSPM)](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security)

  * [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview)

Event Threat Detection relies on logs generated by Google Cloud. To use Event Threat Detection, [enable logs](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#log_types) for your organization, folders, and projects.

  * [Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics)

  * [Security posture](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview)

  * [Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview)

  * [Vulnerability Assessment](https://docs.cloud.google.com/security-command-center/docs/assess-software-vulnerabilities-overview)

  * [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview)




Refer to each service's documentation for usage and optimization instructions. As an example, Event Threat Detection relies on logs generated by Google Cloud. Some logs are always on, so Event Threat Detection can start scanning these logs as soon as it is enabled. Other logs, such as most data access audit logs, must be activated before Event Threat Detection can scan them.

The services outlined in this section, and additional services, can be enabled or disabled by following the steps in [Configure Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service).

### Service agents

A [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) is a service account created and managed by Google Cloud to access resources on your behalf. After a service agent is created, Security Command Center automatically grants required IAM roles to the service agent. Security Command Center Premium activation includes the following service agents:

  * [Cloud Security Command Center Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#cloud-security-command-center-service-agent) for Event Threat Detection, Security Health Analytics, Virtual Machine Threat Detection, and Vulnerability Assessment
  * [Cloud Security Compliance Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#cloud-security-compliance-service-agent-organization) for AI Protection and Compliance Manager
  * [Container Threat Detection Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#container-threat-detection-service-agent-gcp-sa-ktd-hpsa) for Container Threat Detection
  * Data Security Posture Management Service Agent for DSPM



**Note:** If you use [service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/overview#isolate), you must [configure ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) for service agents to allow them access to each service. See the following service-specific documentation for details:

  * [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-configure-vpc-sc)
  * [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#service-perimeter)
  * [DSPM](https://docs.cloud.google.com/security-command-center/docs/dspm-use-data-security#use-dspm-vpcsc)
  * [Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics#service-perimeter)
  * [Vulnerability Assessment](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud-vpcsc#create-ingress-egress-rules)



## Modify your Security Command Center service

For more information about tier management, see [Modify Security Command Center Premium tier for an organization](https://docs.cloud.google.com/security-command-center/docs/modify-premium-tier).

## What's next

  * Learn how to [configure Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center).
  * Learn how to [use Security Command Center in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center).
  * Learn how to work with [Security Command Center findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).
  * Learn about [Google Cloud security sources](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources).
  * Find out how [Model Armor](https://docs.cloud.google.com/model-armor/overview) can help protect your AI workloads.
  * Enable [Sensitive Data Protection](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#dlp) to help protect your sensitive data.
  * Learn how to [monitor your costs](https://docs.cloud.google.com/billing/docs/concepts#monitor_costs) using Cloud Billing.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
