---
url: https://docs.cloud.google.com/security-command-center/docs/configure-ai-protection/
title: Configure AI Protection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:20.152716+00:00
---

# Configure AI Protection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/configure-ai-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Configure AI Protection Stay organized with collections  Save and categorize content based on your preferences. 

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

AI Protection helps you secure your AI assets and workflows by monitoring your models, data, and AI-related infrastructure. This guide describes how to configure AI Protection.

AI Protection uses the following services and features. AI Protection enables some services and features automatically, but you must configure others manually.

  * AI Discovery service
  * Attack Path Simulations created by [Risk Engine](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#risk-engine) (Premium and Enterprise (Deprecated) service tiers)
  * Cloud Audit Logs
  * Cloud Monitoring
  * Compliance Manager
  * Event Threat Detection (Premium and Enterprise (Deprecated) service tiers)
  * Agent Platform Threat Detection (Premium and Enterprise (Deprecated) service tiers)
  * Model Armor
  * Notebook Security Scanner ([Preview](https://cloud.google.com/products/#product-launch-stages)), which is automatically enabled on the Enterprise (Deprecated) service tier.
  * Sensitive Data Protection (Premium and Enterprise (Deprecated) service tiers)
  * Agent Platform Vulnerability Assessment, which is automatically enabled for new activations of AI Protection (Premium and Enterprise (Deprecated) service tiers).



You must configure the following required services for AI Protection:

  * [Compliance Manager framework for AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview#cm-framework)
  * Model Armor
  * App Hub (required for Model Context Protocol (MCP) server inventory)



For more information about each service and feature, see [Detection services in AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview#detection-services).

## Before you begin

  1. Get your organization or project ID.
  2. To create and grant roles, ensure you have the required permissions, such as the Identity and Access Management (IAM) Role Administrator (`roles/iam.roleAdmin`) and the Organization Administrator (`roles/resourcemanager.organizationAdmin`) or Project IAM Admin (`roles/resourcemanager.projectIamAdmin`) roles. For more information, see [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/roles-permissions).



## Required roles

After you complete the steps in Before you begin, follow the steps in one of the following sections to set up required roles for AI Protection access:

  * Predefined roles
  * Custom roles



### Predefined roles

To get the permissions that you need to configure AI Protection and view AI security dashboard data, ask your administrator to grant you the following IAM roles on your organization or project: 

  * Configure AI Protection and view dashboard data: [Security Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`) 
  * View AI security dashboard data only: [Security Center Admin Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

The following Google Cloud CLI commands can be used to assign the preceding roles to a user:

#### Assign roles using gcloud CLI

  * To grant the Security Center Admin role to a user, run the following command:
        
        gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID \
          --member=user:USER_EMAIL_ID \
          --role=roles/securitycenter.admin
        

  * To grant the Security Center Admin Viewer role to a user, run the following command:
        
        gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID \
          --member=user:USER_EMAIL_ID \
          --role=roles/securitycenter.adminViewer
        

Replace the following:

    * RESOURCE_TYPE: `organizations` or `projects`
    * RESOURCE_ID: your numeric organization or project ID
    * USER_EMAIL_ID: the email address of the user who requires access



### Custom roles

To adhere to the principle of least privilege, you can create custom IAM roles that grant only the necessary permissions for viewer or administrator access.

This document shows you how to create and grant custom roles for AI Protection.

#### Configure viewer access

Viewer access lets a user view the AI Protection dashboard and data. To configure viewer access, you create a custom `AIP Viewer` role and then grant that role to a user.

#### Create the AIP Viewer custom role

Create a custom role that contains all the permissions that are required for read-only access to AI Protection.

### Console

  1. In the Google Cloud console, go to the **Roles** page.



[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

  1. Click **Create role**.
  2. In the **Title** field, enter `AIP Viewer`.
  3. The **ID** field auto-populates. You can optionally change it to `aip.viewer`.
  4. In the **Description** field, enter `Grants permissions required to view the AI Security dashboard and data`.
  5. Set **Role launch stage** to **General Availability**.
  6. Click **Add permissions**.
  7. Filter for and select each of the following permissions:

     * **Asset discovery and cloud connections (`cloudasset.*`)**: 
       * `cloudasset.assets.exportResource`
       * `cloudasset.assets.searchAllIamPolicies`
       * `cloudasset.assets.searchAllResources`
       * `cloudasset.assets.searchEnrichmentResourceOwners`
       * `cloudasset.othercloudconnections.get`
       * `cloudasset.othercloudconnections.list`
     * **Compliance summaries (`cloudsecuritycompliance.*`)**: 
       * `cloudsecuritycompliance.controlComplianceSummaries.list`
       * `cloudsecuritycompliance.frameworkComplianceReports.get`
     * **Monitoring (`monitoring.*`)**: 
       * `monitoring.timeSeries.list`
     * **Resource management (`resourcemanager.*`)**: 
       * `resourcemanager.organizations.get`
       * `resourcemanager.projects.get`
     * **Security Command Center management (`securitycentermanagement.*`)**: 
       * `securitycentermanagement.securityCommandCenter.get`
     * **Security Command Center viewer (`securitycenter.*`)**: 
       * `securitycenter.assets.group`
       * `securitycenter.assets.list`
       * `securitycenter.attackpaths.list`
       * `securitycenter.complianceReports.aggregate`
       * `securitycenter.findings.group`
       * `securitycenter.findings.list`
       * `securitycenter.issues.get`
       * `securitycenter.issues.group`
       * `securitycenter.issues.list`
       * `securitycenter.issues.listFilterValues`
       * `securitycenter.simulations.get`
       * `securitycenter.sources.get`
       * `securitycenter.sources.list`
       * `securitycenter.userinterfacemetadata.get`
       * `securitycenter.valuedresources.list`
  8. Click **Add**.

  9. Click **Create**.




### gcloud

  1. In a terminal, run the following `gcloud` command to create the role:


    
    
    gcloud iam roles create aip.viewer \
        --RESOURCE_TYPE=RESOURCE_ID \
        --title="AIP Viewer" \
        --description="Grants permissions required to view AIP dashboard and data." \
        --permissions="cloudasset.assets.exportResource,cloudasset.assets.searchAllIamPolicies,cloudasset.assets.searchAllResources,cloudasset.assets.searchEnrichmentResourceOwners,cloudasset.othercloudconnections.get,cloudasset.othercloudconnections.list,cloudsecuritycompliance.controlComplianceSummaries.list,cloudsecuritycompliance.frameworkComplianceReports.get,monitoring.timeSeries.list,resourcemanager.organizations.get,resourcemanager.projects.get,securitycentermanagement.securityCommandCenter.get,securitycenter.assets.group,securitycenter.assets.list,securitycenter.attackpaths.list,securitycenter.complianceReports.aggregate,securitycenter.findings.group,securitycenter.findings.list,securitycenter.issues.get,securitycenter.issues.group,securitycenter.issues.list,securitycenter.issues.listFilterValues,securitycenter.simulations.get,securitycenter.sources.get,securitycenter.sources.list,securitycenter.userinterfacemetadata.get,securitycenter.valuedresources.list" \
    

Replace the following:

  * `RESOURCE_TYPE`: `organization` or `project`.
  * `RESOURCE_ID`: the numeric organization ID or the project ID. #### Grant viewer access to a user



After you create the `AIP Viewer` custom role, grant it to users who need viewer access.

### Console

  1. In the Google Cloud console, go to the **IAM** page.



[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  1. Click **Grant Access**.
  2. In the **New principals** field, enter the user's email address.
  3. In the **Select a role** drop-down, search for and select the **AIP Viewer** custom role.
  4. Click **Save**.



### gcloud

  1. In a terminal, run the following `gcloud` command:


    
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID \
        --member="user:USER_EMAIL" \
        --role="RESOURCE_TYPE/RESOURCE_ID/roles/aip.viewer"
    

Replace the following:

  * `RESOURCE_TYPE`: `organizations` or `projects`.
  * `RESOURCE_ID`: your organization or project ID.
  * `USER_EMAIL`: the user's email address.



#### Configure administrator access

Administrator access lets a user manage AI Protection features. To configure administrator access, you first create the `AIP Essentials` custom role. Then, you grant that role and the required predefined roles to a user.

#### Create the AIP Essentials custom role

Create a custom role that contains the essential supporting permissions required for AI Protection.

### Console

  1. In the Google Cloud console, go to the **Roles** page.



[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

  1. Click **Create role**.
  2. In the **Title** field, enter `AIP Essentials`.
  3. The **ID** field auto-populates. You can optionally change it to `aip.essentials`.
  4. In the **Description** field, enter `Grants supporting permissions required to view AIP dashboard and data`.
  5. Set **Role launch stage** to **General Availability**.
  6. Click **Add permissions**.
  7. Filter for and select each of the following permissions:

     * **Asset discovery and cloud connections (`cloudasset.*`)**: 
       * `cloudasset.assets.searchEnrichmentResourceOwners`
       * `cloudasset.othercloudconnections.get`
       * `cloudasset.othercloudconnections.list`
     * **Resource management (`resourcemanager.*`)**: 
       * `resourcemanager.organizations.get`
       * `resourcemanager.projects.get`
     * **Security Command Center management (`securitycentermanagement.*`)**: 
       * `securitycentermanagement.securityCommandCenter.get`
     * **Security Command Center viewer (`securitycenter.*`)**: 
       * `securitycenter.assets.group`
       * `securitycenter.assets.list`
       * `securitycenter.attackpaths.list`
       * `securitycenter.complianceReports.aggregate`
       * `securitycenter.findings.group`
       * `securitycenter.findings.list`
       * `securitycenter.simulations.get`
       * `securitycenter.userinterfacemetadata.get`
       * `securitycenter.valuedresources.list`
  8. Click **Add**.

  9. Click **Create**.




### gcloud

  1. In a terminal, run the following `gcloud` command to create the role:


    
    
    gcloud iam roles create aip.essentials \
        --RESOURCE_TYPE=RESOURCE_ID \
        --title="AIP Essentials" \
        --description="Grants supporting permissions required to view AIP dashboard and data." \
        --permissions="cloudasset.assets.searchEnrichmentResourceOwners,cloudasset.othercloudconnections.get,cloudasset.othercloudconnections.list,resourcemanager.organizations.get,resourcemanager.projects.get,securitycentermanagement.securityCommandCenter.get,securitycenter.assets.group,securitycenter.assets.list,securitycenter.attackpaths.list,securitycenter.complianceReports.aggregate,securitycenter.findings.group,securitycenter.findings.list,securitycenter.simulations.get,securitycenter.userinterfacemetadata.get,securitycenter.valuedresources.list" \
    

Replace the following:

  * `RESOURCE_TYPE`: `organization` or `project`.
  * `RESOURCE_ID`: your organization or project ID.



#### Grant administrator access to a user

After you create the `AIP Essentials` custom role, grant it along with the required predefined roles to users who need administrator access.

### Console

  1. In the Google Cloud console, go to the **IAM** page.



[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  1. Click **Grant Access**.
  2. In the **New principals** field, enter the user's email address.
  3. In the **Select a role** drop-down, search for and add each of the following roles: 
     * `Model Armor Admin` (`roles/modelarmor.admin`)
     * `Model Armor Floor Settings Admin` (`roles/modelarmor.floorSettingsAdmin`)
     * `Cloud Security Compliance Admin` (`roles/cloudsecuritycompliance.admin`)
     * `Security Center Findings Viewer` (`roles/securityCenter.findingsViewer`)
     * `Monitoring Viewer` (`roles/monitoring.viewer`)
     * `Cloud Asset Viewer` (`roles/cloudasset.viewer`)
     * The custom **AIP Essentials** role you created.
  4. Click **Save**.



### gcloud

  1. In a terminal, run the following commands, one for each role:


    
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID \
        --member="user:USER_EMAIL" \
        --role="roles/modelarmor.admin"
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID \
        --member="user:USER_EMAIL" \
        --role="roles/modelarmor.floorSettingsAdmin"
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID \
        --member="user:USER_EMAIL" \
        --role="roles/cloudsecuritycompliance.admin"
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID \
        --member="user:USER_EMAIL" \
        --role="roles/securityCenter.findingsViewer"
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID \
        --member="user:USER_EMAIL" \
        --role="roles/monitoring.viewer"
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID \
        --member="user:USER_EMAIL" \
        --role="roles/cloudasset.viewer"
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID \
        --member="user:USER_EMAIL" \
        --role="RESOURCE_TYPE/RESOURCE_ID/roles/aip.essentials"
    

Replace the following:

  * `RESOURCE_TYPE`: `organizations` or `projects`.
  * `RESOURCE_ID`: your organization or project ID.
  * `USER_EMAIL`: the user's email address.



## Supported regions

For a list of regions where AI Protection is supported, see [Regional endpoints](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints#locations-ai-protection).

## Access for service accounts

Ensure that organization policies don't block any service accounts mentioned in the following sections.

## Set up AI Protection

AI Protection is enabled by default for new Security Command Center activations. However, if you activated any Security Command Center tier before AI Protection was available, you must manually enable the feature.

To enable AI Protection at the organization or project level, complete the following:

###  Standard 

  1. If Security Command Center isn't activated in your organization or project, [activate Security Command Center Standard](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview).
  2. Check your AI security dashboard by going to **Risk Overview** > **AI Security**.



###  Premium 

  1. If you haven't activated Security Command Center in your organization or project, then see the instructions to [activate Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview).
  2. If you activated Premium previously, enable AI Protection by going to **Settings** > **Manage Settings** on the AI Protection card. 

[Go to AI Protection settings](https://console.cloud.google.com/projectselector2/security/command-center/config/services/ai-protection?supportedpurview=organizationId,project)

  3. To discover the AI resources that you want to protect, [enable sensitive data discovery](https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery).
  4. Check your AI security dashboard by going to **Risk Overview** > **AI Security**.



After you finish onboarding, if a critical service is disabled, the dashboard provides instructions for the specific service and where to configure it. For more information, see Configure Google Cloud services for AI Protection.

After all the required services are configured, the AI Security dashboard might take some time to reflect the data from your AI assets.

###  Enterprise 

  1. If you haven't activated Security Command Center in your organization, follow the instructions to [activate Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier).
  2. Set up AI Protection and verify dependent services by using the guidance in the **SCC Setup Guide**. 

[Go to Setup guide](https://console.cloud.google.com/projectselector2/security/command-center/setup-guide?supportedpurview=organizationId,project)

     1. Expand the **Review security capabilities** summary panel.
     2. From the **AI protection** panel, click **Set up**.
     3. Follow the directions to check whether required and dependent services for AI Protection are enabled and correctly configured. For more information, see Configure Google Cloud services for AI Protection.
  3. To discover the AI resources that you want to protect, enable discovery:

     * If you have the **Setup guide** open:

       1. Expand the **Data security** panel.
       2. On the **Sensitive data discovery** card, click **Set up** and follow the instructions.
     * If you don't have the Setup guide open:

       1. Go to the **Enable discovery** page in the console: 

[Go to Enable discovery](https://console.cloud.google.com/projectselector2/security/sensitive-data-protection;p=3/landing;source=CSCC_ONBOARDING_SUBTASK/dataProfiles/dashboard?supportedpurview=organizationId)

       2. Follow the instructions to [Enable discovery with default settings in an organization](https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery#enable-discovery).



After all the required services are activated and configured, the AI Security dashboard might take some time to reflect the data that comes from your AI assets.

## Manually configure services

After you enable AI Protection, complete the following sections to manually configure features.

### Configure the AI Discovery service

Security Command Center automatically enables the AI Discovery service as part of Security Command Center Enterprise onboarding. Verify that the Monitoring Viewer (`roles/monitoring.viewer`) IAM role is granted to the Security Command Center Enterprise organization or project service account.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Roles**

  * `roles/monitoring.viewer`



  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click **Grant Access**.

  3. In the **New principals** field, enter the Security Command Center Enterprise organization or project service account. The service account uses the format `service-org-ORG_ID@security-center-api.gserviceaccount.com` or `service-project-PROJECT_NUMBER@security-center-api.gserviceaccount.com`. Replace ORG_ID with your organization ID or PROJECT_NUMBER with your project number.

  4. In the **Select a role** field, select **Monitoring Viewer**.

  5. Click **Save**.




### Configure Model Armor

  1. Enable the `modelarmor.googleapis.com` service for each project that uses generative AI activity. For more information, see [Get started with Model Armor](https://docs.cloud.google.com/model-armor/manage-templates#enable-apis).
  2. Configure the following settings to define security and safety settings for large language model (LLM) prompts and responses: 
     * **[Model Armor templates](https://docs.cloud.google.com/model-armor/manage-templates)** : Create a Model Armor template. These templates define the types of risks to detect, such as sensitive data, prompt injections, and jailbreak detection. They also define the minimum thresholds for those filters.
     * **[Filters](https://docs.cloud.google.com/model-armor/overview#ma-filters)** : Model Armor uses various filters to identify risks, including malicious URL detection, prompt injection and jailbreak detection, and sensitive data protection.
     * **[Floor settings](https://docs.cloud.google.com/model-armor/configure-floor-settings)** : Configure the project-level floor settings to establish default protection for all Gemini models.

**Caution:** If you didn't configure Model Armor for any of the projects in the organization or project, or didn't create a template, the Model Armor widgets in the AI Security dashboard won't display any data.

### Configure Notebook Security Scanner

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Roles**

  * `Dataform Viewer`



  1. Premium service tier: Enable the Notebook Security Scanner service for your organization or project. For more information, see [Enable Notebook Security Scanner](https://docs.cloud.google.com/security-command-center/docs/enable-notebook-security-scanner#enable-nss).
  2. Grant the Dataform Viewer role (`roles/dataform.viewer`) to `notebook-security-scanner-prod@system.gserviceaccount.com` on all projects that contain Notebooks.



### Configure Sensitive Data Protection

Enable the `dlp.googleapis.com` API for your project and configure Sensitive Data Protection to scan for sensitive data.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Roles**

  * `DLP Reader`
  * `DLP Data Profiles Admin`



  1. Enable the Data Loss Prevention API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dlp.googleapis.com)

  2. Grant the `DLP Reader` and `DLP Data Profiles Admin` roles to AI Protection users.

  3. [Configure Sensitive Data Protection](https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery) to scan for sensitive data.




### Configure Agent Platform Vulnerability Assessment

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Agent Platform Vulnerability Assessment identifies software vulnerabilities (CVEs) in agentic workloads that are deployed with Gemini Enterprise Agent Platform. For new activations of AI Protection, Agent Platform Vulnerability Assessment is enabled by default.

If you are an existing customer, you can enable the scanner in the **AI Protection settings** page, which is available only in the organization or project view.

  1. In the Google Cloud console, go to the **Settings** > **Manage Settings** on the AI Protection card.

[Go to AI Protection settings](https://console.cloud.google.com/projectselector2/security/command-center/config/services/ai-protection?supportedpurview=organizationId,project)

  2. In the **Vulnerability Assessment for Agent Platform** section, click **Manage settings**.

  3. Enable the service for your organization or project.


**Note:** A notification appears on the AI Security dashboard if Agent Platform Vulnerability Assessment isn't enabled for your organization or project.

### Configure App Hub for MCP server inventory

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To view Model Context Protocol (MCP) servers in the AI Security dashboard, you must enable the App Hub API (`apphub.googleapis.com`) in each project that hosts MCP servers.

For more information, see [Set up App Hub](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub).

## Optional: Configure additional high-value resources

To create a resource value configuration, follow the steps in [Create a resource value configuration](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set#create_a_resource_value_configuration).

### Scope agentic resources

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To scope the resource value configuration to agentic resources, such as agents or Model Context Protocol (MCP) servers, select an agentic resource type from the **Select resource type** menu (for example, `aiplatform.googleapis.com/ReasoningEngine`), or specify labels or tags that identify agentic resources in your organization or project.

When the next attack path simulation runs, it covers the high-value resource set and generates attack paths.

## What's next

  * [Learn more about AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview)
  * [Review AI security](https://docs.cloud.google.com/security-command-center/docs/review-ai-security)
  * [Assess risk using dashboard data](https://docs.cloud.google.com/security-command-center/docs/assess-risk#ai-protection)
  * [Understand data residency implications](https://docs.cloud.google.com/security-command-center/docs/data-residency-support)
  * [Configure Model Armor](https://docs.cloud.google.com/model-armor/manage-templates)
  * [Learn about Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
