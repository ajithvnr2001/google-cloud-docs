---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/profile-azure-blob-storage/
title: Profile Azure Blob Storage data \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:44.402678+00:00
---

# Profile Azure Blob Storage data  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/profile-azure-blob-storage/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Profile Azure Blob Storage data Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure Sensitive Data Protection discovery for Azure Blob Storage. This feature is available only to customers who have [activated Security Command Center at the Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier).

Sensitive Data Protection discovery helps you learn about the types of data that you're storing in Blob Storage and the sensitivity levels of your data. When you profile your Blob Storage data, you generate _file store data profiles_ , which provide insights and metadata about your Blob Storage containers. For each Blob Storage container, a file store data profile includes the following information:

  * The types of files that you're storing in the container, categorized into [file clusters](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#file_clusters)
  * The sensitivity level of the data in the container
  * A summary about each detected file cluster, including the types of sensitive information found



For a full list of insights and metadata in each file store data profile, see [File store data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#file-store-data-profile).

For more information about the discovery service, see [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

## Workflow

The high-level workflow for profiling Azure Blob Storage data is as follows:

  1. In Security Command Center, [create a connector for Microsoft Azure](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure). Make sure that you select **Grant permissions for Sensitive Data Protection discovery**.

  2. [Create an inspection template](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect#create_a_new_inspection_template) in the `global` region or the region where you plan to store the discovery scan configuration and all generated data profiles.

  3. Create a discovery scan configuration for Azure Blob Storage.

Sensitive Data Protection profiles your data according to the schedule that you specify.




## Data residency considerations

Consider the following when you plan to profile data from other cloud providers:

  * The data profiles are stored alongside the discovery scan configuration. In contrast, when you profile Google Cloud data, the profiles are stored in the same region as the data to be profiled.
  * If you store your inspection template in the `global` region, an in-memory copy of that template is read in the region where you store the discovery scan configuration.
  * Your data is not modified. An in-memory copy of your data is read in the region where you store the discovery scan configuration. However, Sensitive Data Protection makes no guarantees about where the data passes through after it reaches the public internet. The data is encrypted with SSL.



## Empty files and containers

Discovery doesn't scan empty Blob Storage files and containers and doesn't take these into account when listing file extensions seen. A container that has only empty files is also considered as empty.

## Before you begin

  1. In Security Command Center, create a connector for Microsoft Azure. For more information, see [Connect to Microsoft Azure for configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure) in the Security Command Center documentation. 

  2. Confirm that you have the IAM permissions that are required to configure data profiles at the [organization](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#permissions-to-configure-org) level.

If you don't have the Organization Administrator (`roles/resourcemanager.organizationAdmin`) or Security Admin (`roles/iam.securityAdmin`) role, you can still create a scan configuration. However, after you create the scan configuration, someone with either of those roles must [grant data profiling access](https://docs.cloud.google.com/sensitive-data-protection/docs/grant-data-profiling-access) to your service agent. 

  3. Confirm that you have an inspection template in the `global` region or the region where you plan to store the discovery scan configuration and all generated data profiles.

This task lets you automatically create an inspection template in the `global` region only. If organizational policies prevent you from creating an inspection template in the `global` region, then before you perform this task, you must [create an inspection template](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect#create_a_new_inspection_template) in the region where you plan to store the discovery scan configuration. 

  4. To send Pub/Sub notifications to a topic when certain events occur—such as when Sensitive Data Protection profiles a new container—[create a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/admin#create_a_topic) before performing this task. 




To generate data profiles, you need a [service agent container and a service agent](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#service-agent-container) within it. This task lets you create them automatically. 

## Create a scan configuration

  1. Go to the **Create scan configuration** page.

[Go to Create scan configuration](https://console.cloud.google.com/security/sensitive-data-protection/create/discoveryConfiguration;source=7)

  2. Go to your organization. On the toolbar, click the project selector and select your organization.




The following sections provide more information about the steps in the **Create scan configuration** page. At the end of each section, click **Continue**.

### Select a discovery type

Select **Azure Blob Storage**.

### Select scope

Do one of the following:

  * To scan all Blob Storage assets that your Azure connector has access to, select **Scan all Azure assets available through your connector**.
  * To scan the Blob Storage data in a single Azure subscription, select **Scan one Azure subscription**. Enter the subscription ID.
  * To scan a single Blob Storage container, select **Scan one Azure Blob Storage container**. Enter the details of the container that you want to scan.



### Manage schedules

If the [default profiling frequency](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#scan-frequency) suits your needs, you can skip this section of the **Create scan configuration** page.

Configure this section for the following reasons:

  * To make fine-grained adjustments to the profiling frequency of all your data or certain subsets of your data.
  * To specify the containers that you don't want to profile.
  * To specify the containers that you don't want profiled more than once.



To make fine-grained adjustments to profiling frequency, follow these steps:

  1. Click **Add schedule**.

**Note:** If you selected a single container as the scope of this configuration, then you can't add a schedule. You can only edit the catch-all schedule. In addition, you can't specify filters. You can only edit the frequency and conditions for profiling.
  2. In the **Filters** section, define one or more filters that specify which containers are in the schedule's scope. A container is considered to be in the schedule's scope if it matches at least one of the filters defined.

To configure a filter, specify at least one of the following:

     * A subscription ID or a regular expression that specifies one or more subscription IDs
     * A container name or a regular expression that specifies one or more containers

Regular expressions must follow [RE2 syntax](https://github.com/google/re2/wiki/Syntax).

For example, if you want all containers in an account to be included in the filter, enter the subscription ID in the **Subscription ID** field.

To match a filter, a container must meet all the regular expressions specified within that filter.

To add more filters, click **Add filter** and repeat this step.

  3. Click **Frequency**.

  4. In the **Frequency** section, specify whether to profile the containers that you selected and, if so, how often:

     * If you never want the containers to be profiled, turn off **Do profile this data**.

     * If you want the containers to be profiled at least once, leave **Do profile this data** on.

Specify whether to reprofile your data and what events should trigger a reprofile operation. For more information, see [Frequency of data profile generation](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#scan-frequency).

       1. For **On a schedule** , specify how often you want the the containers to be reprofiled. The containers are reprofiled regardless of whether they underwent any changes.
       2. For **When inspect template changes** , specify whether you want your data to be reprofiled when the associated inspection template is updated, and if so, how often. **Note:** You specify the inspection templates to use in the Select inspection template step on this page.

An inspection template change is detected when either of the following occurs:

          * The name of an inspection template changes in your scan configuration.
          * The [`updateTime`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.inspectTemplates#InspectTemplate.FIELDS.update_time) of an inspection template changes.

For example, if you set an inspection template for the `us-west1` region and you update that inspection template, then only data in the `us-west1` region will be reprofiled.



* Optional: Click **Conditions**.

In the **Conditions** section, you specify any conditions that the containers—defined in your filters—must meet before Sensitive Data Protection profiles them.

By default, Sensitive Data Protection scans all objects in a container. If you want to scan only the objects in a particular blob access tier, select those tiers. To include blobs that don't have an access tier, select **Not applicable**.

* Click **Done**.

* Optional: To add more schedules, click **Add schedule** and repeat the previous steps.

* To specify precedence between schedules, reorder them using the arrow_upward up and arrow_downward down arrows.

The order of the schedules specifies how conflicts between schedules are resolved. If a container matches the filters of two different schedules, the schedule higher in the schedules list dictates the profiling frequency for that container.

**Note:** If your discovery pricing mode is [subscription mode](https://cloud.google.com/sensitive-data-protection/pricing#discovery-subscription-mode-pricing), the rate at which Sensitive Data Protection profiles your data is affected by how much capacity you purchased. To determine your daily profiling capacity, see [Monitoring utilization](https://cloud.google.com/sensitive-data-protection/pricing#subscription-monitoring). If you have [under-provisioned capacity](https://cloud.google.com/sensitive-data-protection/pricing#underprovisioned), then the profiling frequencies that you set in your schedules might not be followed. If there is a backlog of data to be profiled, the schedule order doesn't dictate the order in which Sensitive Data Protection profiles the data in the backlog. Rather, all data resources in scope get a randomly assigned slot in the queue.
* Optional: Edit or turn off **Catch-all schedule**.

The last schedule in the list is the catch-all schedule. This schedule covers the containers in your selected scope that don't match any of the schedules that you created. The catch-all schedule follows the [system default profiling frequency](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#scan-frequency).

  * To adjust the catch-all schedule, click edit **Edit schedule** , and then adjust the settings as needed.
  * To prevent Sensitive Data Protection from profiling any resource that is covered by the catch-all schedule, turn off **Profile the resources that don't match any custom schedule**.



### Select an inspection template

Depending on how you want to provide an inspection configuration, choose one of the following options. Regardless of which option you choose, Sensitive Data Protection scans your data in the region where that data is stored. That is, your data doesn't leave its region of origin.

#### Option 1: Create an inspection template

Choose this option if you want to create a new inspection template in the `global` region.

  1. Click **Create new inspection template**.
  2. Optional: To modify the default selection of infoTypes, click **Manage infoTypes**.

For more information about how to manage built-in and custom infoTypes, see [Manage infoTypes through the Google Cloud console](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-infotypes-console).

You must have at least one infoType selected to continue.

  3. Optional: Configure the inspection template further by adding rulesets and setting a confidence threshold. For more information, see [Configure detection](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect#configure-detection).




When Sensitive Data Protection creates the scan configuration, it stores this new inspection template in the `global` region.

#### Option 2: Use an existing inspection template

Choose this option if you have existing inspection templates that you want to use.

  1. Click **Select existing inspection template**.
  2. Enter the full resource name of the inspection template that you want to use. The **Region** field is automatically populated with the name of the region where your inspection template is stored. 

The inspection template that you enter must be in the same region where you plan to store this discovery scan configuration and all the generated data profiles.

To respect data residency, Sensitive Data Protection doesn't use an inspection template outside the region where that template is stored.

To find the full resource name of an inspection template, follow these steps:

     1. Go to your inspection templates list. This page opens on a separate tab. 

[Go to inspection templates](https://console.cloud.google.com/security/sensitive-data-protection/landing/configuration/templates)

     2. Select the project that contains the inspection template that you want to use.
     3. Select **Configuration > Templates > Inspect**, and then click the template ID of the template that you want to use.
     4. On the page that opens, copy the full resource name of the template. The full resource name follows this format: 
            
            projects/PROJECT_ID/locations/REGION/inspectTemplates/TEMPLATE_ID

     5. On the **Create scan configuration** page, in the **Template name** field, paste the full resource name of the template.



### Add actions

This section describes how to specify actions that you want Sensitive Data Protection to take after profiling a container. These actions are useful if you want to send insights gathered from data profiles to other Google Cloud services.

**Note:** For information about how other Google Cloud services may charge you for configuring actions, see [Pricing for exporting data profiles](https://cloud.google.com/sensitive-data-protection/pricing#exporting-profiles-pricing).

#### Publish to Google Security Operations

[Metrics](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference) gathered from data profiles can add context to your Google Security Operations findings. The added context can help you determine the most important security issues to address.

For example, if you're investigating a particular service agent, Google Security Operations can determine what resources the service agent accessed and whether any of those resources have high-sensitivity data.

To send your data profiles to your Google Security Operations instance, turn on **Publish to Google Security Operations**.

If you don't have a Google Security Operations instance enabled for your organization—through the [standalone product](https://cloud.google.com/security/products/security-operations) or through [Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs)—turning on this option has no effect. 

#### Publish to Security Command Center

Findings from data profiles provide context when you triage and develop response plans for your vulnerability and threat findings in [Security Command Center](https://docs.cloud.google.com/security-command-center/docs).

**Note:** You can also configure Security Command Center to automatically prioritize resources for the [attack path simulation feature](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn) according to the calculated sensitivity of the data that the resources contain. For more information, see [Set resource priority values automatically by data sensitivity](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-auto-by-data-sensitivity).

To send the results of your data profiles to Security Command Center, make sure the **Publish to Security Command Center** option is turned on.

For more information, see [Publish data profiles to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc).

#### Save data profile copies to BigQuery

Sensitive Data Protection saves a copy of each generated data profile in a BigQuery table. If you don't provide the details of your preferred table, Sensitive Data Protection creates a dataset and table in the service agent container. By default, the dataset is named `sensitive_data_protection_discovery` and the table is named `discovery_profiles`.

**Important:** The output table uses [`DataProfileBigQueryRowSchema`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileBigQueryRowSchema) as its schema. This schema can change as Sensitive Data Protection adds features. Make sure that your workflows can handle schema changes, for example, by ignoring unknown fields.

This action lets you keep a history of all of your generated profiles. This history can be useful for creating audit reports and [visualizing data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles). You can also load this information into other systems.

Also, this option lets you see all of your data profiles in a single view, regardless of which region your data resides in. Although you can also [view the data profiles through the Google Cloud console](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-data-profiles), the console displays the profiles in only one region at a time.

When Sensitive Data Protection fails to profile a container, it periodically retries. To minimize noise in the exported data, Sensitive Data Protection exports only the successfully generated profiles to BigQuery.

Sensitive Data Protection starts exporting profiles from the time you turn on this option. Profiles that were generated before you turned on exporting aren't saved to BigQuery.

**Note:** Your service agent must have write access on the table where the profile copies will be saved. If you don't have a service agent yet, Sensitive Data Protection lets you create one later in the **Create scan configuration** page.

For example queries that you can use when analyzing data profiles, see [Analyze data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles).

#### Save sample discovery findings to BigQuery

Sensitive Data Protection can add sample findings to a BigQuery table of your choice. Sample findings represent a subset of all findings and might not represent all infoTypes that were discovered. Normally, the system generates around 10 sample findings per container, but this number can vary for each discovery run.

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

To save sample findings to a BigQuery table, follow these steps:

  1. Turn on **Save sample discovery findings to BigQuery**.

  2. Enter the details of the BigQuery table where you want to save the sample findings.

The table that you specify for this action must be different from the table used for the **Save data profile copies to BigQuery** action.

     * For **Project ID** , enter the ID of an existing project where you want to export the findings to.

     * For **Dataset ID** , enter the name of an existing dataset in the project.

     * For **Table ID** , enter the name of the BigQuery table where want to save the findings to. If this table doesn't exist, Sensitive Data Protection automatically creates it for you using the name that you provide.


**Note:** Your service agent must have write access on the table. If you don't have a service agent yet, Sensitive Data Protection lets you create one later in the **Create scan configuration** page.

For information about the contents of each finding that is saved in the BigQuery table, see [`DataProfileFinding`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileFinding).

#### Publish to Pub/Sub

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
     2. Specify whether to include the full container profile in the notification, or just the full resource name of the container that was profiled.

     3. Set the minimum data risk and sensitivity levels that must be met for Sensitive Data Protection to send a notification.

     4. Specify whether only one or both of the data risk and sensitivity conditions must be met. For example, if you choose `AND`, then both the data risk and the sensitivity conditions must be met before Sensitive Data Protection sends a notification.


**Note:** Your service agent must have [ publishing access](https://docs.cloud.google.com/pubsub/docs/access-control#console) on the Pub/Sub topic. An example of a role that has publishing access is the Pub/Sub Publisher role (`roles/pubsub.publisher`). If you don't have a service agent yet, Sensitive Data Protection lets you create one later in the **Create scan configuration** page. If there are configuration or permission issues with the Pub/Sub topic, Sensitive Data Protection retries sending the Pub/Sub notification for up to two weeks. After two weeks, the notification is discarded. 

### Manage service agent container and billing

In this section, you specify the project to use as a [service agent container](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#service-agent-container). You can have Sensitive Data Protection automatically create a new project, or you can choose an existing project.

Regardless of whether you're using a newly created service agent or reusing an existing one, make sure it has read access to the data to be profiled.

#### Automatically create a project

If you don't have the permissions needed to create a project in the organization, you need to select an existing project instead or obtain the required permissions. For information about the required permissions, see [Roles required to work with data profiles at the organization or folder level](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#user-roles-org-folder).

To automatically create a project to use as your service agent container, follow these steps:

  1. In the **Service agent container** field, review the suggested project ID and edit it as needed.
  2. Click **Create**.
  3. Optional: Update the default project name.
  4. Select the account to bill for all billable operations related to this new project, including operations that aren't related to discovery.

**Note:** If you already have an organization-level [discovery subscription](https://cloud.google.com/sensitive-data-protection/pricing#discovery-subscription-mode-pricing), this billing account is still required to create the project. However, for all discovery operations, you are billed through the project associated with your subscription.
  5. Click **Create**.




Sensitive Data Protection creates the new project. The service agent within this project will be used to authenticate to Sensitive Data Protection and other APIs.

#### Select an existing project

To select an existing project as your service agent container, click the **Service agent container** field and select the project.

### Set the location to store the configuration

Click the **Resource location** list, and select the region where you want to store this scan configuration. All scan configurations that you later create will also be stored in this location.

Where you choose to store your scan configuration doesn't affect the data to be scanned. Your data is scanned in the same region where that data is stored. For more information, see [Data residency considerations](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency).

**Note:** If you already have an existing scan configuration, you can't change the value set in this field. All scan configurations are stored in the same location. If you want to change the location of all your scan configurations, you must [delete](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#delete-config) them, recreate them, and store them in the new location.

### Review and create the configuration

  1. If you want to make sure that profiling doesn't start automatically after you create the scan configuration, select **Create scan in paused mode**. 

This option is useful in the following cases:

     * Your Google Cloud administrator still needs to [grant data profiling access](https://docs.cloud.google.com/sensitive-data-protection/docs/grant-data-profiling-access) to the service agent.
     * You want to create multiple scan configurations and you want some configurations to [override](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#overriding-scan-configs) others.
     * You opted to save data profiles to BigQuery and you want to make sure the service agent has write access to the BigQuery table where the data profile copies will be saved.
     * You opted to save sample discovery findings to BigQuery and you want to make sure that the service agent has write access to the BigQuery table where the sample findings will be saved.
     * You configured Pub/Sub notifications and you want to [grant publishing access](https://docs.cloud.google.com/pubsub/docs/access-control#console) to the service agent.
  2. Review your settings and click **Create**. 

Sensitive Data Protection creates the scan configuration and adds it to the discovery scan configurations list.




To view or manage your scan configurations, see [Manage scan configurations](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations).

**Note:** We regularly improve our detection algorithm. If we find that your organization or project would benefit from a new improvement that we implement, we might automatically regenerate your data profiles and redo the [actions in your scan configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder#manage-scan-outcome). You won't incur Sensitive Data Protection charges for this operation. However, because we will redo the actions, you might incur charges for your use of other Google Cloud services. For example, if you configured Sensitive Data Protection to save the data profiles to BigQuery, you might incur BigQuery charges.

## What's next

  * If you don't have the Organization Administrator (`roles/resourcemanager.organizationAdmin`) or Security Admin (`roles/iam.securityAdmin`) role, someone with one of those roles must [grant data profiling access](https://docs.cloud.google.com/sensitive-data-protection/docs/grant-data-profiling-access) to your service agent. 
  * Learn how to [manage data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-data-profiles).
  * Learn how to [manage scan configurations](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations).
  * Learn how to [receive and parse Pub/Sub messages published by the data profiler](https://docs.cloud.google.com/sensitive-data-protection/docs/dp-receive-pubsub-messages).
  * Learn how to [troubleshoot issues with data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/troubleshoot-data-profiles).
  * Look through the [data profiling limits](https://docs.cloud.google.com/sensitive-data-protection/limits#data-profiling-limits). 
  * Look through the [file clusters](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#file_clusters) that sensitive data discovery can scan. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
