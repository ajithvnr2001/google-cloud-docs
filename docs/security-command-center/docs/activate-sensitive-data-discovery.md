---
url: https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery/
title: Enable sensitive data discovery \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:01.652505+00:00
---

# Enable sensitive data discovery  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Enable sensitive data discovery Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

[Sensitive data discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) from Sensitive Data Protection lets you locate, classify, and assess sensitive resources across your environment. The discovery service generates data profiles and evaluates security risk based on data sensitivity.

## Before you begin

To use sensitive data discovery with Security Command Center, complete these tasks.

### Activate Security Command Center

[Activate Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview). Depending on how you activate Security Command Center, you might incur additional charges for Sensitive Data Protection. For details, see [Discovery pricing for Security Command Center customers](https://cloud.google.com/sensitive-data-protection/pricing#discovery-scc).

### Make sure Security Command Center is configured to accept Sensitive Data Protection findings

By default, Security Command Center is configured to accept findings from Sensitive Data Protection. If your organization disabled Sensitive Data Protection as an integrated service, you must re-enable it to receive sensitive data discovery findings. For more information, see [Add a Google Cloud integrated service](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#gcp-configure-other-services).

### Set up permissions

To get the permissions that you need to configure sensitive data discovery, ask your administrator to grant you the following IAM roles on the organization:

Purpose | Predefined role | Relevant permissions  
---|---|---  
Create a discovery scan configuration and view data profiles | DLP Administrator (`roles/dlp.admin`)  | 

  * dlp.columnDataProfiles.list
  * dlp.fileStoreProfiles.list
  * dlp.inspectTemplates.create
  * dlp.jobs.create
  * dlp.jobs.list
  * dlp.jobTriggers.create
  * dlp.jobTriggers.list
  * dlp.projectDataProfiles.list
  * dlp.tableDataProfiles.list

  
Create a project to be used as the service agent container1 | Project Creator (`roles/resourcemanager.projectCreator`) | 

  * resourcemanager.organizations.get
  * resourcemanager.projects.create

  
Grant discovery access2 | One of the following: 

  * Organization Administrator (`roles/resourcemanager.organizationAdmin`)
  * Security Admin (`roles/iam.securityAdmin`)

| 

  * resourcemanager.organizations.getIamPolicy
  * resourcemanager.organizations.setIamPolicy

  
  
1 If you don't have the Project Creator (`roles/resourcemanager.projectCreator`) role, you can still create a scan configuration, but the [service agent container](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#service-agent-container) that you use must be an existing project.

2 If you don't have the Organization Administrator (`roles/resourcemanager.organizationAdmin`) or Security Admin (`roles/iam.securityAdmin`) role, you can still create a scan configuration. After you create the scan configuration, someone in your organization who has one of these roles must [grant discovery access to the service agent](https://docs.cloud.google.com/sensitive-data-protection/docs/grant-data-profiling-access).

For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Benefits

This feature offers the following benefits:

  * You can use Sensitive Data Protection findings to identify and remediate [vulnerabilities](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#sdp-vulnerabilities) and [misconfigurations](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#sdp-misconfigurations) in your resources that can expose sensitive data to the public or to malicious actors.

  * You can use Sensitive Data Protection findings to add context to the triage process and prioritize threats that target resources containing sensitive data.

  * You can configure the [attack path simulation feature](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn) to automatically prioritize resources according to the sensitivity of the data that the resources contain. For more information, see [Set resource priority values automatically by data sensitivity](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-auto-by-data-sensitivity).




## Sensitive data discovery in Security Command Center Enterprise

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

Security Command Center Enterprise includes an organization-level subscription to the Sensitive Data Protection discovery service. With this subscription, you don't incur Sensitive Data Protection charges when you run sensitive data discovery at the organization or folder level. For more information, see Discovery capacity in Enterprise and Premium in this document.

**Important:** When configuring sensitive data discovery, make sure that the scope of your configuration (also known as `parent`) is your organization and not a project. Your organization-level subscription includes discovery at the organization scope only. If you use a project-level scope, you incur separate discovery charges.

To use your organization-level subscription to run discovery on a single project, see [Profile select projects or data assets in an organization or folder](https://docs.cloud.google.com/sensitive-data-protection/docs/common-discovery-configurations#profile-select-projects-assets) in the Sensitive Data Protection documentation.

When you activate the Security Command Center Enterprise tier, the following occur:

  * The Cloud Data Loss Prevention API is automatically activated in the [management project](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier#management-project) that was used to activate Security Command Center Enterprise. This management project serves as the [service agent container](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#service-agent-container) for sensitive data discovery.

**Note:** In audit logs, the actor for this action is the principal in your organization who activated Security Command Center Enterprise.
  * Sensitive data discovery is automatically enabled for all [supported resource types](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#supported-resources) at the organization level. Sensitive Data Protection performs discovery scans across all projects in the organization, unless you modify the discovery scan configuration to [exclude certain projects](https://docs.cloud.google.com/sensitive-data-protection/docs/common-discovery-configurations#exclude-select-projects).

This automatic enablement process is a one-time operation that applies only to resource types that are supported at the time of the Enterprise tier activation. If Sensitive Data Protection adds discovery support for new resource types later, then you need to enable those discovery types manually. For instructions, see Enable discovery with default settings in an organization in this document.




## Sensitive data discovery in Security Command Center Premium

Premium [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

  * If you have an organization-level activation of Security Command Center Premium, then your Premium subscription includes an organization-level subscription to the Sensitive Data Protection discovery service. With this subscription, you don't incur Sensitive Data Protection charges when you run sensitive data discovery at the organization or folder level. For more information, see Discovery capacity in Enterprise and Premium in this document.

**Important:** When configuring sensitive data discovery, make sure that the scope of your configuration (also known as `parent`) is your organization and not a project. Your organization-level subscription includes discovery at the organization scope only. If you use a project-level scope, you incur separate discovery charges.

To use your organization-level subscription to run discovery on a single project, see [Profile select projects or data assets in an organization or folder](https://docs.cloud.google.com/sensitive-data-protection/docs/common-discovery-configurations#profile-select-projects-assets) in the Sensitive Data Protection documentation.

To perform sensitive data discovery at the organization level, see Enable discovery with default settings in an organization in this document.

  * If you have a project-level activation of Security Command Center Premium, you can enable sensitive data discovery at the project level and get the findings in Security Command Center. However, this feature is [priced separately](https://cloud.google.com/sensitive-data-protection/pricing#data_profiling_pricing). To enable discovery at the project level, see [Create a scan configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#create) in the Sensitive Data Protection documentation.




To determine the activation type of your Security Command Center instance, see [View your current activation type](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#check-scc-activation-level).

## Sensitive data discovery in Security Command Center Standard

Standard [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

If you have Security Command Center Standard, you can enable sensitive data discovery and get the findings in Security Command Center. However, this feature is [priced separately](https://cloud.google.com/sensitive-data-protection/pricing#data_profiling_pricing).

## How it works

The Sensitive Data Protection discovery service helps you protect data across your organization by identifying where sensitive and high-risk data reside.

  * In Sensitive Data Protection, the discovery service generates [data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles), which provide metrics and insights about your data at various levels of detail.
  * In Security Command Center, the discovery service generates findings.



### Findings generated

  * Sensitive Data Protection generates observation findings in Security Command Center that show the calculated sensitivity and data risk levels of your data. You can use these findings to inform your response when you encounter threats and vulnerabilities related to your data assets. For a list of finding types generated, see [Observation findings from the discovery service](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#observation-discovery).

These findings can inform the automatic designation of high-value resources based on data sensitivity and the enrichment of threat findings. For more information, see Use discovery insights to identify high-value resources and Use discovery insights to enrich threat findings in this document.

  * Sensitive Data Protection generates vulnerability and misconfiguration findings in Security Command Center when Sensitive Data Protection detects unprotected high-sensitivity or moderate-sensitivity data. For a list of finding types generated, see the following:

    * [Vulnerability findings from the Sensitive Data Protection discovery service](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#sdp-vulnerabilities)
    * [Misconfiguration findings from the Sensitive Data Protection discovery service](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#sdp-misconfigurations)



For a complete list of findings from Sensitive Data Protection, see [Sensitive Data Protection](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#dlp).

### Finding generation latency

Depending on the size of your organization, Sensitive Data Protection findings can start appearing in Security Command Center within a few minutes after you enable sensitive data discovery. For larger organizations or organizations with specific configurations that affect finding generation, it can take up to 12 hours before initial findings appear in Security Command Center.

Subsequently, Sensitive Data Protection generates findings in Security Command Center within a few minutes after the discovery service scans your resources.

## Enable discovery with default settings in an organization

To enable discovery, you create a discovery configuration for each [data source](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#supported-resources) that you want to scan. You can [edit the configurations](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#edit-config) after creating them. To customize settings in the process of creating a configuration, see [Create a scan configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#create) instead.

To enable discovery with default settings at the organization level, follow these steps:

  1. In the Google Cloud console, go to the Sensitive Data Protection **Enable discovery** page.

[Go to Enable discovery](https://console.cloud.google.com/security/sensitive-data-protection;p=3/landing;source=CSCC_ONBOARDING_SUBTASK/dataProfiles/dashboard)

  2. Verify that you are viewing the organization that you activated Security Command Center on.

  3. In the **Enable discovery** pane, in the **Service agent container** field, set the project to be used as a [service agent container](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#service-agent-container). Within this project, the system creates a service agent and automatically grants the required discovery roles to it.

     * To automatically create a project to use as your service agent container, follow these steps:

       1. Click **Create**.
       2. Specify the name, billing account, and parent organization of the new project. Optionally, edit the project ID.
       3. Click **Create**.

It can take a few minutes for the roles to be granted to the new project's service agent.

     * To select a project that you previously used for discovery operations, click the **Service agent container** field and select the project.

  4. To review the default settings, click the expand_more expand icon.

  5. In the **Enable discovery** section, for each discovery type that you want to enable, click **Enable**. Enabling a discovery type does the following:

     * **BigQuery** : Creates a discovery configuration for profiling BigQuery tables across the organization. Sensitive Data Protection starts profiling your BigQuery data and sends the profiles to Security Command Center.
     * **Cloud SQL** : Creates a discovery configuration for profiling Cloud SQL tables across the organization. Sensitive Data Protection starts creating default connections for each of your Cloud SQL instances. This process can take a few hours. When the default connections are ready, you must give Sensitive Data Protection access to your Cloud SQL instances by updating each connection with the proper database user credentials.
     * **Secrets/credentials vulnerabilities** : Creates a discovery configuration for detecting and reporting unencrypted secrets in Cloud Run environment variables. Sensitive Data Protection starts scanning your environment variables.
     * **Cloud Storage** : Creates a discovery configuration for profiling Cloud Storage buckets across the organization. Sensitive Data Protection starts profiling your Cloud Storage data and sends the profiles to Security Command Center.
     * **Vertex AI datasets** : Creates a discovery configuration for profiling Gemini Enterprise Agent Platform datasets across the organization. Sensitive Data Protection starts profiling your Agent Platform datasets and sends the profiles to Security Command Center.
     * **Amazon S3** : Creates a discovery configuration for profiling all Amazon S3 data that your AWS connector has access to.

**Note:** This feature requires Security Command Center Enterprise. You must first [create an AWS connector](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws) that has the AWS permissions needed for Sensitive Data Protection discovery.
     * **Azure Blob Storage** : Creates a discovery configuration for profiling all Azure Blob Storage data that your Azure connector has access to.

**Note:** This feature requires Security Command Center Enterprise. You must first [create an Azure connector](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure) that has the Azure permissions needed for Sensitive Data Protection discovery.
  6. To view the newly created discovery configurations, click **Go to discovery configuration**.

If you enabled Cloud SQL discovery, the discovery configuration is created in paused mode with errors indicating the absence of credentials. See [Manage connections for use with discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-connections) to grant the required IAM roles to your service agent and to provide database user credentials for each Cloud SQL instance.

  7. Close the pane.




To view the findings generated by Sensitive Data Protection, see [Review Sensitive Data Protection findings in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#review-sdp-findings).

## Customize the scan configurations

Each discovery type that you enable has a discovery scan configuration that you can [customize](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#edit-config). For example, you can do the following:

  * Adjust the scan frequency.
  * Specify filters for data assets that you don't want to reprofile.
  * Change the [inspection template](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#inspection-template), which defines the [information types](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) that Sensitive Data Protection scans for.
  * Publish the generated data profiles to other Google Cloud services.
  * Change the service agent container.



## Use discovery insights to identify high-value resources

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

Security Command Center can automatically designate a resource that contains high-sensitivity or medium-sensitivity data as a high-value resource. For high-value resources, Security Command Center provides attack exposure scores and attack path visualizations, which you can use to prioritize the security of resources that contain sensitive data. For more information, see [Set resource priority values automatically by data sensitivity](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-auto-by-data-sensitivity).

## Use discovery insights to enrich threat findings

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

[Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) is integrated with Sensitive Data Protection to enrich sensitive resource findings. If you configure Sensitive Data Protection discovery scans to [send results to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc), Event Threat Detection can use the sensitivity metadata of your BigQuery and Cloud Storage resources to adjust findings:

  * **Category changes** : If a resource is identified by Sensitive Data Protection as having high or moderate sensitivity, the finding category is updated to a specific category that indicates the resource is sensitive. For example, if a leaked service account key is used to access a sensitive bucket, the finding category changes from `Initial Access: Leaked Service Account Key Used` to `Initial Access: Leaked Service Account Key Affecting Sensitive Data`.
  * **Severity upgrades** : If the default severity of the finding is less than **High** (that is, **Low** or **Medium**), the severity is upgraded by one level (for example, from **Medium** to **High**).



For a list of rules that support sensitive data enrichment, see [Event Threat Detection default rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules).

## Discovery capacity in Enterprise and Premium

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (some features require [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

If your sensitive data discovery needs exceed the capacity allocated for Security Command Center Enterprise or Premium (organization-level) customers, then Sensitive Data Protection might increase your capacity temporarily. However, this increase is not guaranteed and is dependent on whether compute resources are available. If you require more discovery capacity, contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact). For more information, see [Monitor utilization](https://cloud.google.com/sensitive-data-protection/pricing#subscription-monitoring) in the Sensitive Data Protection documentation.

## Sensitive data discovery within service perimeters

If you use VPC Service Controls service perimeters and you want to discover sensitive data within those perimeters, see [Allow sensitive data discovery within service perimeters](https://docs.cloud.google.com/sensitive-data-protection/docs/allow-discovery-vpcsc). If you don't perform this task, you might receive warnings.

## What's next

  * [View Sensitive Data Protection findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#review-sdp-findings)
  * [View the data profiles in Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-data-profiles#view_the_data_profiles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
