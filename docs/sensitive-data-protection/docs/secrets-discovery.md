---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/secrets-discovery/
title: Report secrets in environment variables to Security Command Center \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:50.241495+00:00
---

# Report secrets in environment variables to Security Command Center  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/secrets-discovery/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Report secrets in environment variables to Security Command Center Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can use the discovery service of Sensitive Data Protection to determine if secrets are present in your Cloud Run environment variables. Sensitive Data Protection reports any findings to Security Command Center as vulnerabilities.

## About Security Command Center

[Security Command Center](https://docs.cloud.google.com/security-command-center) is the centralized vulnerability and threat reporting service of Google Cloud. Security Command Center helps you strengthen your security posture by identifying misconfigurations, vulnerabilities, observations, and threats. It also provides recommendations for investigating and remediating the findings.

## Why to scan for secrets in environment variables

Storing secrets, such as passwords, in environment variables isn't a secure practice because environment variables aren't encrypted. Their values can be collected and exposed in various systems, such as logs. We recommend that you use [Secret Manager](https://docs.cloud.google.com/secret-manager) to store your secrets. For more information, see the [Cloud Run](https://docs.cloud.google.com/run/docs/configuring/services/secrets) and [Cloud Run functions](https://docs.cloud.google.com/functions/docs/configuring/secrets) documentation on configuring secrets.

## How it works

To perform secrets discovery, you create a discovery scan configuration at the organization or project level. Within your selected scope, Sensitive Data Protection periodically scans Cloud Run for secrets in build and runtime environment variables.

If a secret is present in an environment variable, Sensitive Data Protection sends a `Secrets in environment variables` vulnerability finding to Security Command Center. No data profiles are generated. Any findings are only available through Security Command Center.

Sensitive Data Protection generates a maximum of one finding per resource. For example, if secrets are found in two environment variables in the same Cloud Run function, only one finding is generated in Security Command Center.

In Security Command Center, you can view `Secrets in environment variables` findings when you do the following:

  * [Review Sensitive Data Protection findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#review-sdp-findings)
  * [View or export a compliance report](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#compliance_report_export) for the CIS 1.3 or CIS 2.0 standard.



![The generated findings in the Security Command Center findings list in the Google Cloud console](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/secrets-discovery-findings.png)

The following JSON shows an example of a `Secrets in environment variables` finding. This example shows only the fields relevant to this feature; it doesn't provide an [exhaustive list of fields](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings).

#### Secrets in environment variables
    
    
    {
      "finding": {
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "SECRETS_IN_ENVIRONMENT_VARIABLES",
        "compliances": [
          {
            "standard": "cis",
            "version": "1.3",
            "ids": [
              "1.18"
            ]
          }
        ],
        "createTime": "DATE_TIME",
        "description": "The affected resource is storing credentials or other secret information in its environment variables. This is a security vulnerability because environment variables are stored unencrypted, and accessible to all users who have access to the code.",
        "eventTime": "DATE_TIME",
        "findingClass": "VULNERABILITY",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/dlp",
        "mute": "MUTE_STATUS",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "parentDisplayName": "Sensitive Data Protection",
        "resourceName": "//cloudfunctions.googleapis.com/projects/PROJECT_ID/locations/REGION/functions/FUNCTION_ID",
      },
      "resource": {
        "name": "//cloudfunctions.googleapis.com/projects/PROJECT_ID/locations/REGION/functions/FUNCTION_ID",
        "display_name": "projects/PROJECT_ID/locations/REGION/functions/FUNCTION_ID",
        "type": "google.cloudfunctions.CloudFunction",
        "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "project_display_name": "PROJECT_DISPLAY_NAME",
        "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "parent_display_name": "PARENT_DISPLAY_NAME"
      }
    }
        

## Finding generation latency

Depending on the size of your organization, Sensitive Data Protection findings can start appearing in Security Command Center within a few minutes after you enable sensitive data discovery. For larger organizations or organizations with specific configurations that affect finding generation, it can take up to 12 hours before initial findings appear in Security Command Center.

Subsequently, Sensitive Data Protection generates findings in Security Command Center within a few minutes after the discovery service scans your resources.

## Types of secrets reported

Examples of secrets are passwords, authentication tokens, and Google Cloud credentials. For a full list of secret types that Sensitive Data Protection scans for in this feature, see [Credentials and secrets](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#credentials_and_secrets).

## Supported resources

For secrets discovery, Sensitive Data Protection supports [Cloud Run functions](https://docs.cloud.google.com/functions) (including 1st gen Cloud Functions) and [Cloud Run service revisions](https://docs.cloud.google.com/run).

## Pricing

This feature is free of Sensitive Data Protection charges. [Security Command Center charges](https://cloud.google.com/security-command-center/pricing) may apply, depending on your service tier. Sensitive Data Protection works with Security Command Center in all service tiers.

## Data residency

The first time you create a scan configuration, you specify where you want Sensitive Data Protection to store it. All subsequent scan configurations that you create are stored in that same region. Sensitive Data Protection exports your Cloud Run metadata to the region where your scan configuration is stored, but the function or service revision itself isn't exported.

If Sensitive Data Protection detects secrets in environment variables, the findings are sent to Security Command Center and are subject to its data handling processes.

## Required IAM roles

To perform secrets discovery, you need the Identity and Access Management roles required to profile data:

  * To perform secrets discovery at the organization level, see [Roles required to work with data profiles at the organization level](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#user-roles-org-folder).

  * To perform secrets discovery at the project level, see [Roles required to work with data profiles at the project level](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#user-roles-project).




In addition, you need the appropriate roles to work with Security Command Center findings. For more information, see [IAM for organization-level activations](https://docs.cloud.google.com/security-command-center/docs/access-control-org) in the Security Command Center documentation.

## Before you begin

  1. [Check the activation level of Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#check-scc-activation-level) for your organization. To send data profiles to Security Command Center, you must have Security Command Center activated at the organization level in any service tier. For more information, see [Overview of organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation).

If Security Command Center is activated at the project level only, findings from Sensitive Data Protection won't appear in Security Command Center.

  2. In Security Command Center, make sure that **Sensitive Data Protection** is enabled as an integrated service. For more information, see [Add a Google Cloud integrated service](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#gcp-source).




## Configure secrets discovery at the organization level

Perform these steps if you want to turn on secrets discovery in an entire organization. For project-level discovery, see Configure secrets discovery at the project level.

If you don't have the Organization Administrator (`roles/resourcemanager.organizationAdmin`) or Security Admin (`roles/iam.securityAdmin`) role, you can still create a scan configuration. However, after you create the scan configuration, someone with either of those roles must [grant discovery access](https://docs.cloud.google.com/sensitive-data-protection/docs/grant-data-profiling-access) to your service agent.

  1. Go to the **Create scan configuration** page.

[Go to Create scan configuration](https://console.cloud.google.com/security/sensitive-data-protection/create/discoveryConfiguration;source=7)

  2. Go to your organization. On the toolbar, click the project selector and select your organization.

After each step on this page, click **Continue**.

  3. For **Select a discovery type** , select **Secrets/credentials vulnerabilities**.

  4. For **Select scope** , select whether you want to scan the entire organization.

  5. For **Manage service agent container and billing** , specify the project to use as a [service agent container](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#service-agent-container). You can have Sensitive Data Protection automatically create a new project, or you can choose an existing project.

     * If you don't have a project to use as a service agent container, select **Create a new project as a service agent container**. Sensitive Data Protection creates a new project named **DLP Service Agent Container**. The service agent within this project will be used to authenticate to Sensitive Data Protection and other APIs. The system prompts you to select the account to bill for all billable operations related to this project, including operations that aren't related to discovery.

If you don't have the permissions needed to create projects, the **Create a new project as a service agent container** option is disabled. In this case, you must select an existing project or ask your Google Cloud administrator to grant you the Project Creator (`roles/resourcemanager.projectCreator`) role.

     * If you have an existing service agent container that you want to reuse, select **Select an existing service agent container**. Then click **Browse** to select the service agent container's project ID.

  6. For **Set location to store configuration** , select the region where you want to store this scan configuration. All scan configurations that you later create will also be stored in this location. For information about data residency considerations, see Data residency on this page.

**Note:** If you already have an existing scan configuration, you can't change the value set in this field. All scan configurations are stored in the same location. If you want to change the location of all your scan configurations, you must [delete](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#delete-config) them, recreate them, and store them in the new location.
  7. Optional: If you don't want the scan to begin shortly after you create the scan configuration, select **Create scan in paused mode**.

This option is useful in the following cases:

     * Your Google Cloud administrator still needs to [grant discovery access](https://docs.cloud.google.com/sensitive-data-protection/docs/grant-data-profiling-access) to the service agent.
     * You want to create multiple scan configurations and you want some configurations to [override](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#overriding-scan-configs) others.
  8. Click **Create**.




Sensitive Data Protection starts scanning your Cloud Run environment variables shortly after you create a scan configuration or resume a paused configuration. For information about how long it takes for findings to appear in Security Command Center, see Finding generation latency on this page.

If you don't have the Organization Administrator (`roles/resourcemanager.organizationAdmin`) or Security Admin (`roles/iam.securityAdmin`) role, someone with either of those roles must [grant discovery access](https://docs.cloud.google.com/sensitive-data-protection/docs/grant-data-profiling-access) to your service agent before discovery can begin.

## Configure secrets discovery at the project level

Perform these steps if you want to turn on secrets discovery for a single project. For organization-level discovery, see Configure secrets discovery at the organization level.

**Warning:** Secrets discovery is only supported for projects that are part of an organization. For more information about organizations, see [Creating and managing organization resources](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization).

  1. Go to the **Create scan configuration** page.

[Go to Create scan configuration](https://console.cloud.google.com/security/sensitive-data-protection/create/discoveryConfiguration;source=7)

  2. Go to your project. On the toolbar, click the project selector and select your project.

After each step on this page, click **Continue**.

  3. For **Select a discovery type** , select **Secrets/credentials vulnerabilities**.

  4. For **Select scope** , make sure **Scan entire project** is selected. If it's not selected, make sure that you're in the project view.

  5. For **Set location to store configuration** , select the region where you want to store this scan configuration. All scan configurations that you later create will also be stored in this location. For information about data residency considerations, see Data residency on this page.

**Note:** If you already have an existing scan configuration, you can't change the value set in this field. All scan configurations are stored in the same location. If you want to change the location of all your scan configurations, you must [delete](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#delete-config) them, recreate them, and store them in the new location.
  6. Click **Create**.




Sensitive Data Protection starts scanning your Cloud Run environment variables shortly after you create a scan configuration or resume a paused configuration. For information about how long it takes for findings to appear in Security Command Center, see Finding generation latency on this page.

## Query for `Secrets in environment variables` findings

The following are example queries that you can use to find `Secrets in environment variables` findings in Security Command Center. You can enter these queries in the **Query editor** field. For more information about the query editor, see [Edit a findings query in the Security Command Center dashboard](https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console).

### List all `Secrets in environment variables` findings
    
    
    state="ACTIVE"
    AND NOT mute="MUTED"
    AND category="SECRETS_IN_ENVIRONMENT_VARIABLES"
    

### List all `Secrets in environment variables` findings for a particular project
    
    
    state="ACTIVE"
    AND NOT mute="MUTED"
    AND category="SECRETS_IN_ENVIRONMENT_VARIABLES"
    AND resource.project_name="//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
    

Replace the following:

  * PROJECT_NUMBER: the numerical ID of the project that you want to query for



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
