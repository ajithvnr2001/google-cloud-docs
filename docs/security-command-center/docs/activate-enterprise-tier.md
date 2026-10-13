---
url: https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier/
title: Activate Security Command Center Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:46.389230+00:00
---

# Activate Security Command Center Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Activate Security Command Center Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

The Security Command Center Enterprise tier provides security enhancements, including the following:

  * Advanced security operations using Google Security Operations
  * Integrations with other Google Cloud products, such as Mandiant Attack Surface Management, Sensitive Data Protection, and Assured OSS
  * Multi-cloud support
  * Risk analysis
  * Compliance support ([Preview](https://cloud.google.com/products/#product-launch-stages))



For a description of the Enterprise tier features, see [Service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers).

You can complete the activation process for the Enterprise tier using the setup guide in the Google Cloud console. After the initial mandatory tasks, complete additional steps to set up optional features that your organization requires.

For information about pricing and getting a subscription, see [Security Command Center pricing](https://cloud.google.com/security-command-center/pricing).

For instructions on activating Security Command Center with a different service tier, see the following:

  * [Activate Security Command Center Standard tier](https://docs.cloud.google.com/security-command-center/docs/activate-standard-tier)

  * [Activate Security Command Center Premium tier](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier)




## Before you begin

Before you activate Security Command Center for the first time, complete the following:

  1. Plan for the activation
  2. Create an organization
  3. Create the management project
  4. Verify organization policies
  5. Configure permissions and APIs
  6. Configure notification contacts



### Plan for the activation

This section describes decisions and information you need to prepare for the activation.

#### Decide whether to enable data residency support

When you activate Security Command Center, you can enable support for [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support), which gives you more control over where your Security Command Center data is located. For Google SecOps, data residency is always enabled.

**Caution:** Security Command Center doesn't validate your data residency location against any organization policies that enforce the [resource locations constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations), `gcp.resourceLocations`. When you configure data residency, you must select a location that's consistent with your organization policies.  For the Enterprise service tier, before you activate Security Command Center with data residency controls, you must contact your Google Cloud account representative and schedule a date and time when you will activate Security Command Center. After activation, your account representative will help ensure that your Google SecOps instance is configured to fully support data residency controls. Contact your Google Cloud account representative if you have questions. 

After support for data residency is enabled in your organization, you cannot disable it.

If you use the Standard or Premium service tier, then upgrading to the Enterprise tier does not change the location of your Security Command Center data. If you did not enable Security Command Center data residency for the Standard or Premium tier, then you cannot enable it when you upgrade to the Enterprise tier. 

#### Determine the support contact

When you activate a new Google SecOps instance, you provide your company name and an email address of a point of contact. Identify a point of contact from your organization. This configuration is not related to Essential Contacts.

#### Choose the Google SecOps configuration

During activation, you connect Security Command Center Enterprise to a Google SecOps instance.

  * You can connect to an existing instance.

  * You can provision and connect to a new instance. You can provision and connect to a new instance even if you have an existing instance.




##### Connect to an existing instance

You can't connect Security Command Center Enterprise to an existing [Google SecOps SIEM standalone](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc) or [Google SecOps SOAR standalone](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc) instance. If you have questions about the type of Google SecOps instance you have, contact your Google Cloud sales representative.

When you select an existing Google SecOps instance, the **Connect to a SecOps instance** page provides a link to the instance so you can verify your selection. You must have access to that instance to verify it. You need at least the [Chronicle API Restricted Data Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.restrictedDataAccessViewer) (`roles/chronicle.restrictedDataAccessViewer`) role on the management project to sign in to the instance.

If you provision Security Command Center using an existing Google SecOps instance that is configured to use [Workforce Identity Federation](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication), you must update the workforce identity pools with additional permissions to access features in Security Operations console pages that are available with Security Command Center Enterprise. For more information, see [Control access to features in Security Operations console pages](https://docs.cloud.google.com/security-command-center/docs/configure-secops-users).

##### Provision a new instance

When you provision a new instance, only the new instance is associated with Security Command Center. When using Security Command Center, you navigate between [Google Cloud console and the newly provisioned Security Operations console](https://docs.cloud.google.com/security-command-center/docs/scce-consoles-overview) pages.

During activation, you specify the location where the new Google SecOps instance is to be provisioned. For a list of supported regions and multi-regions, see [SecOps Services Locations Page](https://cloud.google.com/terms/secops/data-residency). This location applies to only Google SecOps, and not other Security Command Center features or services.

Each Google SecOps instance must have a dedicated management project that you own and manage. This project must be in the same organization where you activate Security Command Center Enterprise. You can't use the same management project for multiple Google SecOps instances.

When you have an existing Google SecOps instance and provision a new instance for Security Command Center Enterprise, both instances use the same configuration for the [direct ingestion of Google Cloud data](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs). The same configuration settings control the ingestion to both Google SecOps instances and they receive the same data.

During activation of Security Command Center Enterprise, the activation process modifies the **Google Cloud log ingestion settings** to set all data type fields to enabled: **Google Cloud Logging** , **Cloud Asset Metadata** , and **Security Command Center Premium findings**. The export filter settings are not changed. Security Command Center Enterprise requires these data types for all features to function as designed. You can change the **Google Cloud log ingestion settings** after activation is complete.

### Create an organization

Security Command Center requires an organization resource that is associated with a domain. If you haven't created an organization, see [Creating and managing organizations](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization).

If you have multiple organizations, identify which organizations you will activate Security Command Center Enterprise in. You must follow these activation steps for each organization where you plan to activate Security Command Center Enterprise.

### Verify organization policies

If your organization policies are set to [restrict resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources), verify that the following APIs are permitted:

  * `chronicle.googleapis.com`
  * `cloudsecuritycompliance.googleapis.com`
  * `securitycenter.googleapis.com`
  * `securitycentermanagement.googleapis.com`



### Create a management project

Security Command Center Enterprise requires a project, which is called the _management project_ , to enable Google SecOps and Mandiant Attack Surface Management integration. We recommend that you use this project exclusively for Security Command Center Enterprise.

If you [enabled Google SecOps previously](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project), and you want to connect to the existing instance, use the existing management project that is connected to Google SecOps.

If you plan to provision a new Google SecOps instance, create a new management project that is dedicated to the new instance. Don't reuse a management project that is connected to another Google SecOps instance.

Google SecOps does not support using a management project that exists within a [VPC Service Controls service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

Learn more about [creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

### Configure permissions and APIs

Use information in this section to configure permissions required to activate Security Command Center Enterprise:

  * Optional: Enable the Security Center Management API
  * Configure permissions on the organization
  * Configure permissions and enable APIs on the management project
  * Create a service account if you plan to connect to an existing Google SecOps instance



Learn more about [Security Command Center roles](https://docs.cloud.google.com/security-command-center/docs/access-control) and [Google Cloud APIs](https://docs.cloud.google.com/apis).

#### Enable the Security Center Management API

If you plan to use the Security Center Management API, enable this API in the project where you plan to call it: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=securitycentermanagement.googleapis.com)

#### Configure permissions on the organization

Make sure that you have the following role or roles on the organization: 

  * [ Organization Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`)
  * [Cloud Asset Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.owner) (`roles/cloudasset.owner`)
  * [Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)
  * [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)
  * [Chronicle Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chroniclesm.viewer) (`roles/chroniclesm.viewer`)



#### Check for the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=organizationId)
  2. Select the organization. 
  3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

  4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 



#### Grant the roles

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=organizationId)
  2. Select the organization. 
  3. Click person_add **Grant access**. 
  4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

  5. Click **Select a role** , then search for the role. 
  6. To grant additional roles, click add **Add another role** and add each additional role. 
  7. Click **Save**. 



#### Configure permissions and enable APIs on the management project

  1. In the Google Cloud console, verify that you are viewing the organization where you want to activate the Security Command Center Enterprise tier.
  2. Select the management project that you created previously.
  3. Make sure that you have the following role or roles on the project: 

     * [Service Usage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
     * [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`)
     * [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin) (`roles/chronicle.admin`)
     * [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chroniclesm.admin) (`roles/chroniclesm.admin`)
     * [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin) (`roles/chronicle.soarAdmin`)
     * [Service Account Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountKeyAdmin) (`roles/iam.serviceAccountKeyAdmin`)
     * [Service Account Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 
  4. Enable the Cloud Asset, Cloud Pub/Sub, Cloud Resource Manager, Compute Engine, Policy Analyzer, and Recommender APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudasset.googleapis.com,pubsub.googleapis.com,cloudresourcemanager.googleapis.com,compute.googleapis.com,policyanalyzer.googleapis.com,recommender.googleapis.com)




#### Create a service account when using an existing Google SecOps instance

If you plan to connect to an existing Google SecOps instance, create a [user-managed service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and grant the service account the following roles:

  * [ Chronicle SOAR Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarServiceAgent) (`roles/chronicle.soarServiceAgent`) and [Pub/Sub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.admin) (`roles/pubsub.admin`) on the organization level where you plan to activate Security Command Center.
  * [ Chronicle Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.serviceAgent) (`roles/chronicle.serviceAgent`) on the management project.



### Configure notification contacts

Configure your Essential Contacts so that your security administrators can receive important notifications. For instructions, see [Managing contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

## Activate the Security Command Center Enterprise tier

The activation process automatically configures the service accounts, permissions, and services included with Security Command Center Enterprise. You can connect to an existing Google SecOps Standard, Enterprise, or Enterprise Plus instance or provision a new one.

**Important** :

  * You must use the jurisdictional Google Cloud console to activate Security Command Center with data residency controls and modify the data residency configuration after activation. For details, see [About the jurisdictional Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints#jurisdictional-console). 
  * For the Enterprise service tier, before you activate Security Command Center with data residency controls, you must contact your Google Cloud account representative and schedule a date and time when you will activate Security Command Center. After activation, your account representative will help ensure that your Google SecOps instance is configured to fully support data residency controls. Contact your Google Cloud account representative if you have questions. 



  1. In the Google Cloud console, go to Security Command Center. 

[Go to Security Command Center](https://console.cloud.google.com/projectselector2/security/command-center/welcome?supportedpurview=organizationId)

  2. Select the organization where you want to activate the Security Command Center Enterprise tier, and then click **Select**. 

  3. In the Security Command Center navigation menu, click **Setup Guide**.

**Note:** If you don't see **Setup Guide** , contact [Google Cloud sales](https://cloud.google.com/contact) to verify that your subscription entitlement is active.
  4. On the **Get started with Security Command Center Enterprise** page, review the service accounts and APIs that will be configured, and then click **Next**.

     * To view the service accounts that will be created, click **View service accounts and permissions**.
     * To view APIs that will be enabled, click **View Security Command Center Enterprise APIs**.
     * To view the terms and conditions, click **Security Command Center Enterprise terms and conditions**.

The next page displays a different view depending on your environment.

     * If you have an existing Google SecOps instance, you are prompted to use the existing one or create a new one. Continue with step 5 to choose the instance type.

     * If you don't have an existing Google SecOps instance, continue with step 6 to create a new Google SecOps instance.

  5. If the organization is linked to a Google SecOps instance, choose one of the following. If it's not linked to a Google SecOps instance, continue with step 6 to create a new Google SecOps instance. 

     * Select **Yes, connect to an existing Google Security Operations instance for me** , and then choose an instance from the menu. Continue with step 7 to start the activation.

The menu displays Google SecOps instances that are associated with the organization where you are activating Security Command Center Enterprise. Each item includes the Google SecOps customer ID, the region where it is provisioned, and the Google Cloud project name that it is associated with. You cannot select an instance that is incompatible with Security Command Center Enterprise.

The page provides a link to the selected Google SecOps instance so you can verify it. If you get an error when opening the instance, check that you have the required IAM permissions to access the instance.

     * Select **No, create a new Google Security Operations instance** , and then continue with step 6 to create a new Google SecOps instance.

  6. To create a new Google SecOps instance, provide additional setup details. 

     1. Specify your company contact information.

        * **Technical support contact** : enter an individual email address or group email address.
        * **Company name** : enter your company name.
     2. Select the **Location type** where Google SecOps will be provisioned.

        * **Region** : select a single region.
        * **Multi-region** : select a multi-regional location.

This location is used for only Google SecOps, and not for other Security Command Center features. For a list of supported regions and multi-regions, see [SecOps Services Locations Page](https://cloud.google.com/terms/secops/data-residency).

     3. Click **Next** , and then select the dedicated **Management project**. You created the dedicated management project in a previous step.

If you select a project that is linked to an existing Google SecOps instance, you will get an error when you start the activation.

     4. Continue with step 7 to start the activation.

  7. Click **Activate**.

Certain services are automatically enabled, such as Security Health Analytics, Event Threat Detection, and Virtual Machine Threat Detection. It can take some time before Google SecOps features are ready and findings become available. 

  8. Continue with Monitor activation progress and configure services.




## Monitor activation progress and configure services

The **Setup guide** displays the provisioning status and lets you view the services that are enabled. You can configure additional services and configure connections to other cloud service providers.

  1. In the Google Cloud console, go to the Security Command Center **Setup guide**.

[Go to Setup guide](https://console.cloud.google.com/projectselector2/security/command-center/setup-guide?supportedpurview=organizationId)

  2. Select the organization where you activated Security Command Center Enterprise.

  3. Expand the **Review security capabilities summary** panel. Each panel displays the enablement status of related services.

  4. To connect to Amazon Web Services (AWS) or Microsoft Azure, click add **Add connector**. This opens the **Connectors** tab on the **Settings** page.

For additional instructions, see the following:

     * [Connect to AWS for configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws)
     * [Connect to Microsoft Azure for configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure).
  5. Click **Set up** in any panel to configure additional services and capabilities. Use links in the following table to learn more about each capability.

Capabilities panel name | Learn more about these capabilities | **AI protection** | 
     * [AI Protection overview](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview)
     * [ Model Armor Overview](https://docs.cloud.google.com/security-command-center/docs/get-started-model-armor)  
---|---  
**Code security** | 
     * [ Google Cloud Armor Overview](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#cloud-armor)
     * [ Integrate with Assured OSS for code security](https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc).  
**Cloud threat detection** | 
     * [ Container Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview)
     * [ Overview of Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview)
     * [ Virtual Machine Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview)
     * [ Connect to AWS for configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws)
     * [ Cloud Run Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview)  
**Data security** | 
     * [Review and customize data security frameworks](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security)
     * [Enable Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview)
     * [Enable Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)
     * [Enable discovery](https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery)  
**Identity and access security** | 
     * [ Overview of the IAM recommender integrated service](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#iamrec-source)
     * [ Overview of Cloud Infrastructure Entitlement Management (CIEM)](https://docs.cloud.google.com/security-command-center/docs/ciem-enable-service)  
**Compliance** | 
     * [Apply a framework](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework)
     * [Grant roles in IAM](https://docs.cloud.google.com/security-command-center/docs/access-control-org#compliance-manager)
     * [Manage a security posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture)
     * [Overview of Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics)
     * [Overview of Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview)  
**Response platform** | 
     * [Map and authenticate users to enable SOAR-related features](https://docs.cloud.google.com/security-command-center/docs/map-users-in-secops)
     * [Integrate Security Command Center Enterprise with ticketing systems](https://docs.cloud.google.com/security-command-center/docs/integrate-ticketing-systems)
     * [ Update the Enterprise use case](https://docs.cloud.google.com/security-command-center/docs/enterprise-security-operations-software-update)
     * [Work with playbooks](https://docs.cloud.google.com/security-command-center/docs/playbooks-overview)  
**Vulnerability assessment** | 
     * [ Assess software vulnerabilities overview](https://docs.cloud.google.com/security-command-center/docs/assess-software-vulnerabilities-overview)  



## Configure permissions for ongoing Security Command Center Enterprise use

To change the configuration of your organization, you need both of the following roles at the organization level:

  * [ Organization Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`)
  * [ Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)



If a user doesn't require edit permissions, consider granting them viewer roles.

To view all assets, findings, and attack paths in Security Command Center, users need the [Security Center Admin Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`) role at the organization level.

To view settings, users need the [ Security Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`) role at the organization level.

To restrict access to individual folders and projects, don't grant all roles at the organization level. Instead, grant the following roles at the **folder** _or_ **project** level:

  * [ Security Center Assets Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.assetsViewer) (`roles/securitycenter.assetsViewer`)
  * [Security Center Findings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)



Each [detection service](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources) may require additional permissions to enable or configure it. See the documentation specific to each service for more information.

To use Security Operations console features that are [supported with Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs/secops-limits#enterprise-tier-secops-features), see [Control access to features in Security Operations console pages](https://docs.cloud.google.com/security-command-center/docs/configure-secops-users).

## Modify your Security Command Center service

For more information about tier management, see [Modify Security Command Center Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/modify-enterprise-tier).

## What's next

  * Learn how to work with [Security Command Center findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).
  * Learn about [Google Cloud security sources](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources).
  * [Investigate threats with curated detections](https://docs.cloud.google.com/security-command-center/docs/investigate-threat-findings).
  * [Apply frameworks to your environment](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework) to align your environment with your compliance and security requirements.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
