---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-cortex-xsoar/
title: Send Security Command Center data to Cortex XSOAR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:40:23.182218+00:00
---

# Send Security Command Center data to Cortex XSOAR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-cortex-xsoar/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Send Security Command Center data to Cortex XSOAR Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to automatically send [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) findings, assets, and security sources to [Cortex XSOAR](https://www.paloaltonetworks.com/cortex/xsoar). It also describes how to manage the exported data. Cortex XSOAR is a security orchestration, automation, and response (SOAR) platform that ingests security data from one or more sources and lets security teams manage responses to incidents. You can use Cortex XSOAR to view your Security Command Center findings and assets, and to update findings when issues are resolved.

In this guide, you ensure that the required Security Command Center and Google Cloud services are properly configured, and enable Cortex XSOAR to access findings and assets in your Security Command Center environment. Some of the instructions on this page are compiled from Cortex XSOAR's [integrations guide](https://github.com/demisto/content/tree/master/Packs/GoogleCloudSCC/Integrations/GoogleCloudSCC) on GitHub.

## Before you begin

This guide assumes you have a working version of Cortex XSOAR. To get started with Cortex XSOAR, [sign up](https://start.paloaltonetworks.com/sign-up-for-community-edition.html).

## Configure authentication and authorization

Before connecting to Security Command Center to Cortex XSOAR, you need to create an Identity and Access Management (IAM) service account in each Google Cloud organization and grant that account both the organization-level and project-level IAM roles that Cortex XSOAR needs.

### Create a service account and grant IAM roles

The following steps use the Google Cloud console. For other methods, see the links at the end of this section.

Complete these steps for each Google Cloud organization that you want to import Security Command Center data from.

  1. In the same project in which you create your Pub/Sub topics, use the **Service Accounts** page in the Google Cloud console to create a service account. For instructions, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts). 
  2. Grant the service account the following role:

     * **Pub/Sub Editor** (`roles/pubsub.editor`) 
  3. Copy the name of the service account that you just created.

  4. Use the project selector in the Google Cloud console to switch to the organization level.

  5. Open the **IAM** page for the organization:

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  6. On the IAM page, click **Grant access**. The grant access panel opens.

  7. In the **Grant access** panel, complete the following steps:

     1. In the **Add principals** section in the **New principals** field, paste the name of the service account.
     2. In the **Assign roles** section, use the **Role** field to grant the following IAM roles to the service account: 

     3. **Security Center Admin Editor** (`roles/securitycenter.adminEditor`) 
     4. **Security Center Notification Configurations Editor** (`roles/securitycenter.notificationConfigEditor`)
     5. **Organization Viewer** (`roles/resourcemanager.organizationViewer`)
     6. **Cloud Asset Viewer** (`roles/cloudasset.viewer`) 
  8. Click **Save**. The service account appears on the **Permissions** tab of the **IAM** page under **View by principals**.

By inheritance, the service account also becomes a principal in all child projects of the organization. The roles that are applicable at the project level are listed as inherited roles.




For more information about creating service accounts and granting roles, see the following topics:

  * [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts)
  * [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)



### Provide the credentials to Cortex XSOAR

Depending on where you are hosting Cortex XSOAR, how you provide the IAM credentials to Cortex XSOAR differs.

  * If you are hosting Cortex XSOAR in Google Cloud, consider the following:

    * The service account that you created and the organization-level roles that you granted to it are available automatically by inheritance from the parent organization. If you are using multiple Google Cloud organizations, add this service account to the other organizations and grant it the IAM roles that are described in steps 5 to 7 of Create a service account and grant IAM roles.

    * If you deploy Cortex XSOAR in a service perimeter, create the ingress and egress rules. For instructions, see [Granting perimeter access in VPC Service Controls](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications#grant-perimeter-access).

  * If you are hosting Cortex XSOAR in your on-premises environment, and your identity provider supports [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), [configure workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers) and [download the credentials configuration files](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation). Otherwise, [create a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) for each Google Cloud organization in JSON format.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  * If you are hosting Cortex XSOAR in Microsoft Azure or Amazon Web Services, [configure workload identity federation](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation) and [download the credentials configuration files](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation). If you are using multiple Google Cloud organizations, add this service account to the other organizations and grant it the IAM roles that are described in steps 5 to 7 of Create a service account and grant IAM roles.




## Configure notifications

Complete these steps for each Google Cloud organization that you want to import Security Command Center data from.

  1. [Set up finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) as follows:

     1. Enable the Security Command Center API.
     2. Create a filter to export findings.
     3. Create a [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) topic for findings. The `NotificationConfig` must use the Pub/Sub topic you create for findings.
  2. [Enable the Cloud Asset API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com) for your project.




You will need your organization ID, project ID, and the Pub/Sub subscription ID from this task to configure Cortex XSOAR. To retrieve your organization ID and project ID, see [Retrieving your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id) and [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects), respectively.

## Configure Cortex XSOAR

When granted access, Cortex XSOAR will receive findings and assets updates in real time.

To use Security Command Center with Cortex XSOAR, perform the following steps:

  1. [Install the Google Cloud SCC](https://xsoar.pan.dev/marketplace/details/GoogleCloudSCC/) content pack from the Cortex XSOAR Marketplace.

The content pack is a module maintained by Security Command Center that automates the process of scheduling Security Command Center API calls and regularly retrieves Security Command Center data for use in Cortext XSOAR.

  2. In the Cortex XSOAR application menu, navigate to **Settings** , and then click **Integrations**.

  3. Under **Integrations** , select **Servers & Services**.

  4. Search for and select **GoogleCloudSCC**.

  5. To create and configure a new integration instance, click **Add instance**.

  6. Enter information into the following fields as needed: 

**Parameter** | **Description** | **Required**  
---|---|---  
Service Account Configuration | One of the following, as described in Before you begin: 
     * The contents of the Service Account JSON file, if you created a service account key
     * The contents of the credential configuration file, if you are using workload identity federation
| True  
Organization ID | The ID for your organization | True  
Fetch incidents | Enables fetch incident | False  
Project ID | The ID of the project to use for fetching incidents; if empty, the ID of the project contained in the provided JSON file is used | False  
Subscription ID | The ID of your Pub/Sub subscription | True  
Max Incidents | The maximum number of incidents to fetch during each retrieval | False  
Incident type | The type of incident | False  
Trust any certificate (not secure) | Enables to trust on all certificates | False  
Use system proxy settings | Enables system proxy settings | False  
Incidents Fetch Interval | Time between retrievals for updated incident information | False  
Log Level | The log level for the content pack | False  
  7. Click **Test**.

If the configuration is valid, you see a "success" message. If invalid, you get an error message.

  8. Click **Save and exit**.

  9. Repeat steps 5 to 8 for each organization.




Cortex XSOAR automatically maps fields from Security Command Center findings to appropriate Cortex XSOAR fields. To override selections or learn more about Cortex XSOAR, read [product documentation](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin.html).

The configuration of Cortex XSOAR is complete. The Manage findings and assets section explains how to view and manage Security Command Center data in the service.

## Upgrade the Google Cloud SCC content pack

This section describes how to upgrade from a previous version.

  1. [Access the latest version of Google Cloud SCC](https://xsoar.pan.dev/marketplace/details/GoogleCloudSCC/) content pack from the Cortex XSOAR Marketplace.

  2. Click **Download with Dependencies**.

  3. Click **Install**.

  4. Click **Refresh content**.




The upgrade maintains your previous configuration information. To use workload identity federation, add the configuration file, as described in Configure Cortex XSOAR.

## Manage findings and assets

You can view and update assets and findings using Cortex XSOAR's command line interface (CLI). You can run commands as part of automated triaging and remediation, or in a playbook.

For names and descriptions of all supported methods and arguments for Cortex XSOAR's CLI, and output examples, see [Commands](https://github.com/demisto/content/tree/master/Packs/GoogleCloudSCC/Integrations/GoogleCloudSCC#commands).

Findings are compiled from Security Command Center's built-in services—[Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics), [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview), [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), and [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview)—and any integrated services you enable.

**Note:** You must be a [Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/service-tiers) customer to receive findings from certain Security Command Center services, such as Event Threat Detection and Container Threat Detection.

### List assets

To list your organization's assets, use Cortex XSOAR's `google-cloud-scc-asset-list` method. For example, the following command lists assets where `lifecycleState` is **Active** and limits the response to three assets:
    
    
    !google-cloud-scc-asset-list pageSize="3" activeAssetsOnly=TRUE
    

The exclamation symbol (`!`) in code samples is a required symbol to start commands in Cortex XSOAR. It doesn't represent negation or NOT.

**Note:** The `google-cloud-scc-asset-list` command is deprecated, but it continues to work as described. An alternative command is unavailable at this time.

### View asset resources

To list assets contained in parent resources, such as projects, use Cortex XSOAR's `google-cloud-scc-asset-resource-list` command. For example, the following command lists assets with an `assetType` of `compute.googleapis.com/Disk` and limits the response to two assets:
    
    
    !google-cloud-scc-asset-resource-list assetType="compute.googleapis.com/Disk" pageSize=2
    

Wildcards and regular expressions are supported. For example, `assetType=".*Instance"` lists assets where the asset type ends with "instance."

### View findings

To list findings for your organization or a security source, use Cortex XSOAR's `google-cloud-scc-finding-list` command. For example, the following command lists active findings with critical severity for all sources and limits the response to three findings:
    
    
    !google-cloud-scc-finding-list severity="CRITICAL" sourceTypeId="-" pageSize="3" state="ACTIVE"
    

You can filter your findings as well. The following command lists any findings that are classified as threats:
    
    
    !google-cloud-scc-finding-list filter="findingClass=\"THREAT\""
    

### Update findings

You can update a finding by using Cortex XSOAR's `google-cloud-scc-finding-update` command. You must provide the `name`, or relative resource name, of the finding, using the following format: `organizations/ORGANIZATION_ID/sources/SOURCE_ID</var>/finding/FINDING_ID`.

For example, the following command updates the severity of a finding:
    
    
    !google-cloud-scc-finding-update name="organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID" severity="CRITICAL"
    

Replace the following:

  * `<var>ORGANIZATION_ID</var>` with your organization ID. To retrieve your organization ID and project ID, see [Retrieving your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
  * `<var>SOURCE_ID</var>` with the ID of the security source. To find a source ID, see [Getting the source ID](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications#get-source-id).
  * `<var>FINDING_ID</var>` with the finding ID that is included in finding details.



### Update finding status

You can update the status of a finding by using Cortex XSOAR's `google-cloud-scc-finding-status-update` command. You must provide the `name`, or relative resource name, of the finding, using the following format: `organizations/ORGANIZATION_ID/sources/SOURCE_ID/finding/FINDING_ID`.

For example, the following command sets the finding status to active:
    
    
    !google-cloud-scc-finding-status-update name="organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID" state="ACTIVE"
    

Replace the following:

  * `<var>ORGANIZATION_ID</var>` with your organization ID. To retrieve your organization ID and project ID, see [Retrieving your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
  * `<var>SOURCE_ID</var>` with the ID of the security source. To find a source ID, see [Getting the source ID](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications#get-source-id).
  * `<var>FINDING_ID</var>` with the finding ID that is included in finding details.



### Get asset owners

To list the owners of an asset, use Cortex XSOAR's `google-cloud-scc-asset-owner-get` command. You must provide the project name in the form of `projects/PROJECT_NUMBER`. For example, the following command lists the owner of the provided project.
    
    
    !google-cloud-scc-asset-owner-get projectName="projects/PROJECT_NUMBER"
    

To add multiple projects to the command, use a comma separator, for example, `projectName="projects/123456789, projects/987654321"`

## What's next

  * Learn more about setting up [finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) in Security Command Center.

  * Read about [filtering finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications) in Security Command Center.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
