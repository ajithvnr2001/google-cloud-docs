---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/troubleshoot-data-profiles/
title: Troubleshoot issues with the discovery service \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:56:39.179861+00:00
---

# Troubleshoot issues with the discovery service  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/troubleshoot-data-profiles/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Troubleshoot issues with the discovery service Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with the discovery service of Sensitive Data Protection. For more information about the discovery service, see [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles). For information about how to view errors associated with your discovery scan configuration, see [View configuration errors](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#view-errors).

## The service agent container doesn't have the DLP API enabled

This issue occurs when you create an organization-level scan configuration and you don't have the [`serviceusage.services.enable`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.services.enable) permission on the project that you selected as your [service agent container](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#service-agent-container). Sensitive Data Protection is unable to automatically enable the DLP API on the project.
    
    
    Permission denied to enable service [dlp.googleapis.com]
    

To resolve this issue, do one of the following tasks. In both cases, you need to obtain the required permissions. For more information, see [Roles required to work with data profiles at the organization or folder level](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#user-roles-org-folder).

### Create a new service agent container

  1. Ask your administrator to grant you the Project Creator (`roles/resourcemanager.projectCreator`) role on the organization.
  2. [Edit](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#edit-config) your organization-level scan configuration.
  3. In the **Service agent container** section, create a new service agent container by clicking **Create** and following the prompts.
  4. Save your configuration.



### Update your service agent container

  1. Ask your administrator to grant you a role that has the `serviceusage.services.enable` permission on the project that you selected as your service agent container.
  2. [View the details of the scan configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#view-config) to see the active errors.
  3. Find this error and click **Repair**.



## The service agent doesn't have permission to read an access-controlled column

This issue occurs when profiling a table that enforces column-level security through policy tags. If the service agent doesn't have permission to access the restricted column, Sensitive Data Protection shows the following error:
    
    
    Permission denied for DLP API service account 'SERVICE_AGENT_ID'
    while accessing a BigQuery table. Access Denied: BigQuery BigQuery: User does
    not have permission to access policy tag "POLICY_TAG_ID" on column FIELD_NAME.
    

To resolve this issue, on the Identity and Access Management (IAM) page, grant your service agent the **[Fine-Grained Reader](https://docs.cloud.google.com/bigquery/docs/column-level-security#fine_grained_reader)** role.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

Sensitive Data Protection periodically retries profiling data that it failed to profile.

For more information on granting a role, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

## The service agent doesn't have data profiling access

This issue occurs after someone in your organization creates an organization- or folder-level scan configuration. When you [view the scan configuration details](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#view-config), you see that the value for **Scan status** is **Active with errors**. When you view the error, Sensitive Data Protection shows the following error message:
    
    
    None of the driver projects (PROJECT_ID) have MISSING_PERMISSION
    permission for organizations/ORGANIZATION_ID.

This error occurred because Sensitive Data Protection couldn't automatically grant the **DLP Organization Data Profiles Driver** role to your service agent while it was creating your scan configuration. The creator of the scan configuration doesn't have [permissions to grant data profiling access](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#permissions-to-grant-profiling-access), and so Sensitive Data Protection was unable to do it on their behalf.

To resolve this issue, see [Grant data profiling access to a service agent](https://docs.cloud.google.com/sensitive-data-protection/docs/grant-data-profiling-access).

## The service account doesn't have permission to query a table

This issue occurs when Sensitive Data Protection attempts to profile a table that the service agent doesn't have permission to query. Sensitive Data Protection shows the following error:
    
    
    Permission denied error: Permission denied for DLP API service account 'SERVICE_AGENT_ID'
    while accessing BigQuery table. Access Denied: Table TABLE: User does not have
    permission to query table TABLE. Permission denied for DLP API service account
    'SERVICE_AGENT_ID' while accessing BigQuery table. Access Denied: Table TABLE:
    User does not have permission to query TABLE. [TIMESTAMP]
    

Confirm that the table still exists. If the table exists, perform the following steps.

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Get the current IAM policy for the table, and print it to `stdout`:
         
         bq get-iam-policy TABLE
         

Replace TABLE with the full resource name of the BigQuery table, in the format PROJECT_ID:DATASET_ID.TABLE_ID—for example, `project-id:dataset-id.table-id`.

  3. Grant the **DLP API Service Agent** (`roles/dlp.serviceAgent`) role to the service agent:
         
         bq add-iam-policy-binding --member=serviceAccount:SERVICE_AGENT_ID \
             --role=roles/dlp.serviceAgent TABLE
         

Replace the following:

     * SERVICE_AGENT_ID: the ID of the service agent that needs to query the table—for example, `service-0123456789@dlp-api.iam.gserviceaccount.com`.
     * TABLE: the full resource name of the BigQuery table, in the format PROJECT_ID:DATASET_ID.TABLE_ID—for example, `project-id:dataset-id.table-id`.

The output is similar to the following:
    
    Successfully added member 'SERVICE_AGENT_ID' to role 'roles/dlp.serviceAgent' in IAM policy for table 'TABLE':
    
    {
     "bindings": [
       {
         "members": [
           "serviceAccount:SERVICE_AGENT_ID"
         ],
         "role": "roles/dlp.serviceAgent"
       }
     ],
     "etag": "BwXNAPbVq+A=",
     "version": 1
    }
    

Sensitive Data Protection periodically retries profiling data that it failed to profile.




## The service account doesn't have permission to publish to a Pub/Sub topic

This issue occurs when Sensitive Data Protection attempts to publish notifications to a Pub/Sub topic where the service agent has no publishing access. Sensitive Data Protection shows the following error:
    
    
    Permission missing to publish notifications on Cloud Pub/Sub topic 'TOPIC_NAME'.
    The DLP API service account 'SERVICE_AGENT_ID' must must have at least the Pub/Sub Publisher role.
    

To resolve this issue, [grant publishing access](https://docs.cloud.google.com/pubsub/docs/access-control#console), at a project or topic level, to your service agent. An example of a role that has publishing access is the **Pub/Sub Publisher** role.

If there are configuration or permission issues with the Pub/Sub topic, Sensitive Data Protection retries sending the Pub/Sub notification for up to two weeks. After two weeks, the notification is discarded. 

## The inspection template can't be used to profile data in a different region

This issue occurs when Sensitive Data Protection attempts to profile data that doesn't reside in the same region where the inspection template resides. Sensitive Data Protection shows the following error:
    
    
    Data in region DATA_REGION cannot be profiled using template in region
    TEMPLATE_REGION. Regional template can only be used to profile data
    in the same region. If profiling data in multiple regions, use a global template.
    

In this error message, DATA_REGION is the region where the data resides, and TEMPLATE_REGION is the region where the inspection template resides.

To resolve this issue, you can copy the region-specific template to the `global` region:

  1. [Copy the inspection template to the `global` region](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect#copy-to-global).

  2. On the **Inspection template details** page, copy the full resource name of the template. The full resource name follows this format:
         
         projects/PROJECT_ID/locations/REGION/inspectTemplates/TEMPLATE_ID

  3. [Edit the scan configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#edit-config) and enter the full resource name of the new inspection template.

  4. Click **Save**.




Sensitive Data Protection periodically retries profiling data that it failed to profile.

## Sensitive Data Protection attempted to profile an unsupported table

This issue occurs when Sensitive Data Protection attempts to profile a table that is not supported. For that table, you still get a partial profile containing the table's metadata. However, the partial profile shows the following error:
    
    
    Unimplemented error: Table of type `TABLE_TYPE` is not currently supported for inspection. [DATE_TIME].
    

If you don't want to get partial profiles and errors for unsupported tables, follow these steps:

  1. [Edit the scan configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#edit-config).
  2. In the **Manage schedules** step, click  edit  **Edit schedule**.
  3. In the pane that appears, click the **Conditions** tab.
  4. In the **Tables to profile** section, click **Profile supported tables**.



For more information, see [Manage schedules](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder#manage-schedules).

## The premade Data Studio report isn't loading properly

See [Troubleshoot errors with the premade report](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles#troubleshooting).

## Issues related to automatic tagging based on data sensitivity

See [Troubleshoot errors](https://docs.cloud.google.com/sensitive-data-protection/docs/control-access-based-on-data-sensitivity#troubleshooting) in the [documentation for controlling IAM access to resources based on data sensitivity](https://docs.cloud.google.com/sensitive-data-protection/docs/control-access-based-on-data-sensitivity).

## What's next

  * [View configuration errors](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#view-errors)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
