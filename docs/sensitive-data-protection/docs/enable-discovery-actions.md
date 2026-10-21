---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/enable-discovery-actions/
title: Enable discovery actions \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:38.044305+00:00
---

# Enable discovery actions  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/enable-discovery-actions/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Enable discovery actions Stay organized with collections  Save and categorize content based on your preferences. 

This section describes how to specify actions that you want Sensitive Data Protection to take after profiling a resource. These actions are useful if you want to send insights gathered from data profiles to other Google Cloud services.

**Note:** For information about how other Google Cloud services may charge you for configuring actions, see [Pricing for exporting data profiles](https://cloud.google.com/sensitive-data-protection/pricing#exporting-profiles-pricing). To enable discovery actions, [create](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#create) or [edit](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#edit-config) a discovery scan configuration. The following sections describe the different actions that you can enable in the **Add actions** section of the scan configuration. 

Not all actions on this page are available for each [discovery type](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#discovery-type). For example, you can't attach tags to resources if you are configuring discovery for resources from another cloud provider. For more information, see Supported actions on this page.

For more information about sensitive data discovery, see [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

Inspection and risk analysis operations have a different set of actions. For more information, see [Enable inspection or risk analysis actions](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions). 

## Publish to Google Security Operations

[Metrics](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference) gathered from data profiles can add context to your Google Security Operations findings. The added context can help you determine the most important security issues to address.

For example, if you're investigating a particular service agent, Google Security Operations can determine what resources the service agent accessed and whether any of those resources have high-sensitivity data.

To send your data profiles to your Google Security Operations instance, turn on **Publish to Google Security Operations**.

If you don't have a Google Security Operations instance enabled for your organization—through the [standalone product](https://cloud.google.com/security/products/security-operations) or through [Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs)—turning on this option has no effect. 

## Publish to Security Command Center

Findings from data profiles provide context when you triage and develop response plans for your vulnerability and threat findings in [Security Command Center](https://docs.cloud.google.com/security-command-center/docs).

**Note:** You can also configure Security Command Center to automatically prioritize resources for the [attack path simulation feature](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn) according to the calculated sensitivity of the data that the resources contain. For more information, see [Set resource priority values automatically by data sensitivity](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-auto-by-data-sensitivity). Before you can use this action, Security Command Center must be activated at the organization level. Turning on Security Command Center at the organization level enables the flow of findings from integrated services like Sensitive Data Protection. Sensitive Data Protection works with Security Command Center in all service tiers. 

If Security Command Center isn't activated at the organization level, Sensitive Data Protection findings won't appear in Security Command Center. For more information, see [Check the activation level of Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#check-scc-activation-level). 

To send the results of your data profiles to Security Command Center, make sure the **Publish to Security Command Center** option is turned on.

For more information, see [Publish data profiles to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc).

## Save data profile copies to BigQuery

Sensitive Data Protection saves a copy of each generated data profile in a BigQuery table. If you don't provide the details of your preferred table, Sensitive Data Protection creates a dataset and table in the service agent container. By default, the dataset is named `sensitive_data_protection_discovery` and the table is named `discovery_profiles`.

**Important:** The output table uses [`DataProfileBigQueryRowSchema`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileBigQueryRowSchema) as its schema. This schema can change as Sensitive Data Protection adds features. Make sure that your workflows can handle schema changes, for example, by ignoring unknown fields.

This action lets you keep a history of all of your generated profiles. This history can be useful for creating audit reports and [visualizing data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles). You can also load this information into other systems.

Also, this option lets you see all of your data profiles in a single view, regardless of which region your data resides in. Although you can also [view the data profiles through the Google Cloud console](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-data-profiles), the console displays the profiles in only one region at a time.

When Sensitive Data Protection fails to profile a resource, it periodically retries. To minimize noise in the exported data, Sensitive Data Protection exports only the successfully generated profiles to BigQuery.

Sensitive Data Protection starts exporting profiles from the time you turn on this option. Profiles that were generated before you turned on exporting aren't saved to BigQuery.

**Note:** Your service agent must have write access on the table where the profile copies will be saved. If you don't have a service agent yet, Sensitive Data Protection lets you create one later in the **Create scan configuration** page.

For example queries that you can use when analyzing data profiles, see [Analyze data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles).

## Save sample discovery findings to BigQuery

Sensitive Data Protection can add sample findings to a BigQuery table of your choice. Sample findings represent a subset of all findings and might not represent all infoTypes that were discovered. Normally, the system generates around 10 sample findings per resource, but this number can vary for each discovery run.

Each finding includes the actual string (also called _quote_) that was detected and its exact location.

This action is useful if you want to evaluate whether your [inspection configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#inspection-template) is correctly matching the type of information that you want to flag as sensitive. Using the exported data profiles and the exported sample findings, you can run queries to get more information about the specific items that were flagged, the infoTypes they matched, their exact locations, their calculated sensitivity levels, and other details.

**Important:** The output table uses [`DataProfileFinding`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileFinding) as its schema. This schema can change as Sensitive Data Protection adds features. Make sure that your workflows can handle schema changes, for example, by ignoring unknown fields.

##### Example query: Show sample findings related to file store data profiles

This example requires both **Save data profile copies to BigQuery** and **Save sample discovery findings to BigQuery** to be enabled.

The following query uses an `INNER JOIN` operation on both the table of exported data profiles and the table of exported sample findings. In the resulting table, each record shows the finding's quote, the infoType that it matched, the resource that contains the finding, and the calculated sensitivity level of the resource. 
    
    
    SELECT
     findings_table.quote,
     findings_table.infotype.name,
     findings_table.location.container_name,
     profiles_table.file_store_profile.file_store_path as bucket_name,
     profiles_table.file_store_profile.sensitivity_score as bucket_sensitivity_score
    FROM
     `FINDINGS_TABLE_PROJECT_ID.FINDINGS_TABLE_DATASET_ID.FINDINGS_TABLE_ID_latest_v1` AS findings_table
    INNER JOIN
     `PROFILES_TABLE_PROJECT_ID.PROFILES_TABLE_DATASET_ID.PROFILES_TABLE_ID_latest_v1` AS profiles_table
    ON
     findings_table.data_profile_resource_name=profiles_table.file_store_profile.name
     AND findings_table.timestamp.timestamp=profiles_table.file_store_profile.profile_last_generated.timestamp

##### Example query: Show sample findings related to table data profiles

This example requires both **Save data profile copies to BigQuery** and **Save sample discovery findings to BigQuery** to be enabled.

The following query uses an `INNER JOIN` operation on both the table of exported data profiles and the table of exported sample findings. In the resulting table, each record shows the finding's quote, the infoType that it matched, the resource that contains the finding, and the calculated sensitivity level of the resource. 
    
    
    SELECT
     findings_table.quote,
     findings_table.infotype.name,
     findings_table.location.container_name,
     findings_table.location.data_profile_finding_record_location.field.name AS field_name,
     profiles_table.table_profile.dataset_project_id AS project_id,
     profiles_table.table_profile.dataset_id AS dataset_id,
     profiles_table.table_profile.table_id AS table_id,
     profiles_table.table_profile.sensitivity_score AS table_sensitivity_score
     FROM
     `FINDINGS_TABLE_PROJECT_ID.FINDINGS_TABLE_DATASET_ID.FINDINGS_TABLE_ID_latest_v1` AS findings_table
    INNER JOIN
     `PROFILES_TABLE_PROJECT_ID.PROFILES_TABLE_DATASET_ID.PROFILES_TABLE_ID_latest_v1` AS profiles_table
    ON
     findings_table.data_profile_resource_name=profiles_table.table_profile.name
     AND findings_table.timestamp.timestamp=profiles_table.table_profile.profile_last_generated.timestamp

To save sample findings to a BigQuery table, follow these steps:

  1. Turn on **Save sample discovery findings to BigQuery**.

  2. Enter the details of the BigQuery table where you want to save the sample findings.

The table that you specify for this action must be different from the table used for the **Save data profile copies to BigQuery** action.

     * For **Project ID** , enter the ID of an existing project where you want to export the findings to.

     * For **Dataset ID** , enter the name of an existing dataset in the project.

     * For **Table ID** , enter the name of the BigQuery table where want to save the findings to. If this table doesn't exist, Sensitive Data Protection automatically creates it for you using the name that you provide.


**Note:** Your service agent must have write access on the table. If you don't have a service agent yet, Sensitive Data Protection lets you create one later in the **Create scan configuration** page.

For information about the contents of each finding that is saved in the BigQuery table, see [`DataProfileFinding`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileFinding).

## Attach tags to resources

Turning on **Attach tags to resources** instructs Sensitive Data Protection to automatically tag your data according to its calculated sensitivity level. This section requires you to first complete the tasks in [Control IAM access to resources based on data sensitivity](https://docs.cloud.google.com/sensitive-data-protection/docs/control-access-based-on-data-sensitivity).

To automatically tag a resource according to its calculated sensitivity level, follow these steps:

  1. Turn on the **Tag resources** option.
  2. For each sensitivity level (high, moderate, low, and unknown), enter the path of the tag value that you created for the given sensitivity level.

If you skip a sensitivity level, no tag is attached for it.

  3. To automatically lower the data risk level of a resource when the sensitivity level tag is present, select **When a tag is applied to a resource, lower the data risk of its profile to LOW**. This option helps you measure the improvement in your data security and privacy posture.

**Important:** This option overrides the [calculated data risk level](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation#data-risk) of the profiled resource.
  4. Select one or both of the following options:

     * **Tag a resource when it is profiled for the first time.**
     * **Tag a resource when its profile is updated.** Select this option if you want Sensitive Data Protection to overwrite the sensitivity level tag value on succeeding discovery runs. Consequently, a principal's access to a resource changes automatically as the calculated data sensitivity level for that resource increases or decreases.

Don't select this option if you plan to manually update the sensitivity level tag values that the discovery service attached to your resources. If you select this option, Sensitive Data Protection can overwrite your manual updates.




## Publish to Pub/Sub

Turning on **Publish to Pub/Sub** lets you take programmatic actions based on profiling results. You can use Pub/Sub notifications to develop a workflow for catching and remediating findings with significant data risk or sensitivity.

To send notifications to a Pub/Sub topic, follow these steps:

  1. Turn on **Publish to Pub/Sub**.

A list of options appears. Each option describes an event that causes Sensitive Data Protection to send a notification to Pub/Sub.

  2. Select the events that should trigger a Pub/Sub notification.

If you select **Send a Pub/Sub notification each time a profile is updated** , Sensitive Data Protection sends a notification when there's a change in the sensitivity level, data risk level, detected infoTypes, public access, and other important [metrics](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference) in the profile.

  3. For each event you select, follow these steps:

     1. Enter the name of the topic. The name must be in the following format:
            
            projects/PROJECT_ID/topics/TOPIC_ID
            

Replace the following:

        * PROJECT_ID: the ID of the project associated with the Pub/Sub topic.
        * TOPIC_ID: the ID of the Pub/Sub topic.
     2. Specify whether to include the full resource profile in the notification, or just the full resource name of the resource that was profiled.

     3. Set the minimum data risk and sensitivity levels that must be met for Sensitive Data Protection to send a notification.

     4. Specify whether only one or both of the data risk and sensitivity conditions must be met. For example, if you choose `AND`, then both the data risk and the sensitivity conditions must be met before Sensitive Data Protection sends a notification.


**Note:** Your service agent must have [ publishing access](https://docs.cloud.google.com/pubsub/docs/access-control#console) on the Pub/Sub topic. An example of a role that has publishing access is the Pub/Sub Publisher role (`roles/pubsub.publisher`). If you don't have a service agent yet, Sensitive Data Protection lets you create one later in the **Create scan configuration** page. If there are configuration or permission issues with the Pub/Sub topic, Sensitive Data Protection retries sending the Pub/Sub notification for up to two weeks. After two weeks, the notification is discarded. 

## Send to Knowledge Catalog as aspects

This action lets you add [Knowledge Catalog aspects](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata#aspects) to profiled resources based on insights from data profiles. This action is only applied to new and updated profiles. Existing profiles that aren't updated aren't sent to Knowledge Catalog. 

When you enable this action, Sensitive Data Protection attaches the `Sensitive Data Protection profile` aspect to the [Knowledge Catalog entry](https://docs.cloud.google.com/dataplex/docs/ingest-custom-sources#entries) for each new or updated resource that you profile. The generated aspects contain insights gathered from the data profiles. You can then search your organization and projects for entries with specific `Sensitive Data Protection profile` aspect values.

To send the data profiles to Knowledge Catalog, make sure that the **Send to Dataplex Catalog as aspects** option is turned on.

For more information, see [Add Knowledge Catalog aspects based on insights from data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects). 

## Supported actions

The following table shows which actions are supported for each [discovery type](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#discovery-type).

| Publish to Google Security Operations | Publish to Security Command Center | Save data profile copies to BigQuery | Save sample discovery findings to BigQuery | Attach tags to resources | Publish to Pub/Sub | Send to Knowledge Catalog as aspects  
---|---|---|---|---|---|---|---  
Amazon S3 | ✓ | ✓ | ✓ | ✓ |  | ✓ |   
Azure Blob Storage | ✓ | ✓ | ✓ | ✓ |  | ✓ |   
BigQuery | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  
Cloud SQL | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓  
Cloud Storage | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |   
Vertex AI | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓  
  
## What's next

  * Learn how to [use context data from data profiles in Google Security Operations](https://docs.cloud.google.com/chronicle/docs/detection/usecase-dlp-high-risk-user-download).
  * Learn about the [findings that Sensitive Data Protection can generate in Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc).
  * Learn how to [analyze data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles) in BigQuery and Data Studio.
  * Learn how to [control IAM access to resources based on data sensitivity](https://docs.cloud.google.com/sensitive-data-protection/docs/control-access-based-on-data-sensitivity).
  * Learn how to [receive and parse Pub/Sub messages about data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/dp-receive-pubsub-messages).
  * Learn how to [add Knowledge Catalog aspects based on insights from data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
