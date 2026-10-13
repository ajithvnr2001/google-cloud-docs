---
url: https://docs.cloud.google.com/security-command-center/docs/activate-scc-for-a-project/
title: Activate Security Command Center for a project \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:45.871180+00:00
---

# Activate Security Command Center for a project  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/activate-scc-for-a-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Activate Security Command Center for a project Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, and Premium [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Security Command Center lets you identify vulnerabilities and detect threats across resources in an individual Google Cloud project. You can activate either the Standard or Premium tier for your project, with project-level Standard activations supporting the new Standard tier features.

  * For information about features in the Standard tier, see [Security Command Center service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers).

  * For information about differences between the Standard and Standard-legacy tiers, see [Standard tier enhanced and automatically activated for some customers](https://docs.cloud.google.com/security-command-center/docs/migrate-standard-legacy#feature-differences).


**Note:** If you are using an organization-level activation of Security Command Center Premium, set up project-level activations before the organization-level activation ends to avoid a lapse in your coverage. If you use an organization-level subscription, when the subscription expires, Security Command Center Premium coverage continues for only those projects for which the Premium tier is already selected. If you use pay-as-you-go pricing at the organization level, you must [downgrade the organization-level activation to the Standard tier](https://docs.cloud.google.com/security-command-center/docs/modify-premium-tier#premium-to-standard) for the project-level activations to take effect.

To activate Security Command Center for an entire organization, see one of the following:

  * [Activate the Security Command Center Standard tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier)
  * [Activate the Security Command Center Premium tier for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier)
  * [Activate the Security Command Center Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier)

**Note:** If your organization hasn't activated Security Command Center, you can activate Security Command Center Premium for a project with a 30-day free trial. For more information, see Activate for a project when Security Command Center is not active in the organization.

## Before you begin

To activate Security Command Center on a project, you need the following prerequisites, which are explained in the following subsections:

  * Read the prerequisite information to understand how a project-level activation of Security Command Center differs from an organization-level activation.
  * You need to have a Google Cloud project that is associated with an organization.
  * Your user account needs to be granted Identity and Access Management (IAM) roles that contain the required permissions.
  * Enable required APIs, depending on how you were onboarded to the Security Command Center Standard tier.
  * If your project inherits organization policies that are set to restrict identities by domain, your user and service accounts must be in an allowed domain.
  * If you will use Container Threat Detection, your Google Kubernetes Engine clusters must support Container Threat Detection. For more information, see Confirm software versions for Container Threat Detection.



### Prerequisite information

To understand how a project-level activation of Security Command Center differs from an organization-level activation, see [Overview of project-level enablement of Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#project-level-activation-overview).

To learn about the services and Security Command Center findings that are not supported with project-level activations, see [Project-level activation service limitations](https://docs.cloud.google.com/security-command-center/docs/activate-scc-project-level-limitations).

### Project requirements

To activate Security Command Center for a project, the project must be associated with an organization. If you need to create a project, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

### Required roles

To get the permissions that you need to activate Security Command Center for a project, ask your administrator to grant you the following IAM roles on your project: 

  * [Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)
  * [Security Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable required APIs

If your organization was automatically onboarded to Security Command Center as part of Google Cloud services, or if you plan to use the Security Command Center API, you must enable the API for your project. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=securitycenter.googleapis.com)

### Verify organization policies

If your project inherits organization policies that are set to [restrict identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains), you need to meet the following requirements:

  * You must be signed in to the Google Cloud console on an account that's in an allowed domain.
  * Your service accounts must be in an allowed domain or be members of a group within your domain. This requirement lets you allow `@*.gserviceaccount.com` services access to resources when domain-restricted sharing is enabled.



### Confirm software versions for Container Threat Detection

If you plan to use Container Threat Detection with Google Kubernetes Engine (GKE), make sure that your clusters are on a supported version of GKE and that the clusters are properly configured. For more information, see [Using Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection).

## Activation scenarios for a project

This page covers the following activation scenarios:

  * In an organization that has never activated Security Command Center, activate either the Premium or Standard tier of Security Command Center for a project.
  * In an organization that uses the Standard tier, activate the Security Command Center Premium tier for a project.
  * In an organization that uses an expiring Premium tier subscription, activate the Premium tier of Security Command Center for a project.



Depending on whether your organization is using Security Command Center, you activate Security Command Center for a project by using different methods.

If your organization is not using Security Command Center, the Google Cloud console guides you through a series of setup pages.

If your organization is using Security Command Center, you activate Security Command Center Premium for a project by using the **Tier Details** tab of the **Settings** page.

## Determine if Security Command Center is already active in your organization

How you activate Security Command Center for a project is different depending on whether Security Command Center is already active in your organization.

To check if Security Command Center is already active in your organization, complete the following steps:

  1. In the Google Cloud console, go to the Security Command Center **Overview** page.

[Go to Security Command Center](https://console.cloud.google.com/projectselector2/security/command-center/welcome?supportedpurview=project)

  2. Select the name of the project for which you need to activate Security Command Center.

After you select the project, one of the following pages opens:

     * If Security Command Center is active in your organization, the **Risk overview** page opens.
     * If Security Command Center has not been activated in the organization, the welcome page opens, where you can start the activation process for your project from.
  3. If Security Command Center is already active in your organization, check the service tier that's active.

     1. Open the Security Command Center **Settings** page:

[Go to Settings](https://console.cloud.google.com/projectselector2/security/command-center/config/services?supportedpurview=project)

     2. On the **Settings** page, click **Tier Details**. The **Tier** page opens.

     3. On the **Tier** row, the service tier that the project is inheriting is listed.

  4. To activate Security Command Center for a project, follow the procedure for the activation state of Security Command Center in the parent organization:

     * Activate for a project when Security Command Center is active in the organization
     * Activate for a project when Security Command Center is not active in the organization



## Activate for a project when Security Command Center is active in the organization

If Security Command Center is already active in an organization, the only service tier you would need to activate at the project level is the Premium tier, because, at a minimum, the project will inherit the use of the Standard tier.

To review the features that are included with each tier, see [Service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers).

**Note:** If you are using an organization-level activation of Security Command Center Premium, set up project-level activations before the organization-level activation ends to avoid a lapse in your coverage. If you use an organization-level subscription, when the subscription expires, Security Command Center Premium coverage continues for only those projects for which the Premium tier is already selected. If you use pay-as-you-go pricing at the organization level, you must [downgrade the organization-level activation to the Standard tier](https://docs.cloud.google.com/security-command-center/docs/modify-premium-tier#premium-to-standard) for the project-level activations to take effect.

To upgrade your project to the Premium tier, follow these steps:

  1. In the Google Cloud console, go to the **Tier details** page.

[Go to Tier details](https://console.cloud.google.com/projectselector2/security/command-center/config/tier-detail?supportedpurview=project)

  2. Select the project that you want to upgrade the Security Command Center tier for, and then click **Select**.

  3. Click **Manage project tier**.

  4. In the **Manage tier** pane, click **Select** for the Premium tier. Then, click **Update**.

**Note:** Your Premium free trial lasts for 30 days. When your trial ends, your project automatically transitions to the Premium pay-as-you-go plan, and your billing account is charged accordingly.  
  
To cancel your Premium trial and avoid pay-as-you-go charges, you must downgrade to the Standard tier before the trial period ends. You can downgrade at any time during the trial.



You have completed the activation of Security Command Center Premium for your project. Next, wait for the [initial scans to complete](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview).

## Activate for a project when Security Command Center is not active in the organization

If Security Command Center isn't active in your organization, the welcome page with tier details is displayed when you open Security Command Center in the Google Cloud console. You start the activation process by selecting a tier.

Security Command Center has three tiers: Standard, Premium, and Enterprise. The tier that you select determines the features that are available to you and the cost of using Security Command Center. You can only activate Enterprise tier at the organization level. For more information, see [Activate the Security Command Center Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier).

To review the features that are included with each tier, see [Service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers).

**Note:** If you want to enable [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) or [data encryption](https://docs.cloud.google.com/security-command-center/docs/cmek#set-up-cmek), you must enable Security Command Center at the organization level. For more information, see [Overview of organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#org-level-activation).

To activate Security Command Center for a project, select the service tier that you want to activate, Standard or Premium, and follow these steps:

###  Standard 

  1. In the Google Cloud console, go to the Security Command Center **Overview** page.

[Go to Security Command Center](https://console.cloud.google.com/projectselector2/security/command-center/welcome?supportedpurview=project)

  2. Select the project that you want to enable Security Command Center Standard for, and then click **Select**.

  3. On the welcome page, click **Get Standard**.

**Note:** If you want to try Security Command Center Premium, you can select **Start a Premium free trial** instead. Your Premium free trial lasts for 30 days. When your trial ends, your project will automatically transition to the Premium pay-as-you-go plan, and your billing account will be charged accordingly.  
  
To cancel your Premium trial and avoid pay-as-you-go charges, you must downgrade to the Standard tier before the trial period ends. You can downgrade at any time during the trial.
  4. Click **Activate**.




###  Premium 

  1. In the Google Cloud console, go to the Security Command Center **Overview** page.

[Go to Security Command Center](https://console.cloud.google.com/projectselector2/security/command-center/welcome?supportedpurview=project)

  2. Select the project that you want to enable Security Command Center Premium for, and then click **Select**.

  3. On the welcome page, select **Start a Premium free trial**.

**Note:** Your Premium free trial lasts for 30 days. When your trial ends, your project will automatically transition to the Premium pay-as-you-go plan, and your billing account will be charged accordingly.  
  
To cancel your Premium trial and avoid pay-as-you-go charges, you must downgrade to the Standard tier before the trial period ends. You can downgrade at any time during the trial.
  4. Click **Activate**.




Results are displayed in the Google Cloud console as they become available. After they're displayed, you can review and remediate Google Cloud security and data risks.

Security Command Center completes its first full scan within 24 hours. Some services might not start scanning right away. For more information, see [When to expect findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview).

### Services for Security Command Center

Security Command Center uses [detection services](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources) to detect security issues in your cloud environments. After you activate Security Command Center, specific services are automatically enabled, and service agents are created so that these services can act on your behalf.

Follow the steps in [Configure Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service) to enable or disable various services.

The services that are automatically enabled are determined by your service tier. Select your service tier to see what's automatically enabled.

###  Standard 

Activating Security Command Center Standard automatically enables [Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics) and grants its [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) the roles and permissions required for the service to function.

**Note:** If you use [service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/overview#isolate), you must [grant inbound access to the Cloud Security Command Center Service Agent](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics#service-perimeter).

###  Premium 

The following services are enabled when you activate Security Command Center Premium:

  * [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview)

For Container Threat Detection to function, make sure that your clusters are on a supported version of Google Kubernetes Engine (GKE) and that your GKE clusters are configured correctly. For more information, see [Use Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection).

  * [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview)

Event Threat Detection relies on logs generated by Google Cloud. To use Event Threat Detection, [enable logs](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#log_types) for your organization, folders, and projects.

  * [Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics)

  * [Security posture](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview)

  * [Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview)

  * [Vulnerability Assessment](https://docs.cloud.google.com/security-command-center/docs/assess-software-vulnerabilities-overview)

  * [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview)




#### Service agents

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



For usage and optimization instructions, refer to the documentation for each service. As an example, Event Threat Detection relies on logs generated by Google Cloud. Some logs are always on, so Event Threat Detection can start scanning these logs as soon as it is enabled. Other logs, such as most data access audit logs, must be activated before Event Threat Detection can scan them.

## What's next

Learn more about Security Command Center and its built-in services.

  * Learn how to review assets, findings, and vulnerabilities by [using Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center).
  * Learn about [Google Cloud security sources](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources).
  * Learn how to [add security sources to Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
