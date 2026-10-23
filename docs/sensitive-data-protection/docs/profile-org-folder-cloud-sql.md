---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder-cloud-sql/
title: Profile Cloud SQL data in an organization or folder \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:35.115957+00:00
---

# Profile Cloud SQL data in an organization or folder  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder-cloud-sql/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Profile Cloud SQL data in an organization or folder Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure Cloud SQL data discovery at the level of an organization or folder. If you want to profile a project, see [Profile Cloud SQL data in a single project](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project-cloud-sql). 

For more information about the discovery service, see [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

## How it works

The following is a high-level workflow for profiling Cloud SQL data:

  1. Create a scan configuration.

After you create a scan configuration, Sensitive Data Protection starts identifying your Cloud SQL instances and creating a default connection for each instance. Depending on the number of instances in scope of discovery, this process can take a few hours. You can exit the Google Cloud console and check your connections later.

  2. [Grant the required IAM roles to the service agent associated with your scan configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-connections#service-agent-roles).

  3. When the default connections are ready, give Sensitive Data Protection access to your Cloud SQL instances by [updating each connection](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-connections#provide-credentials) with the proper database user credentials. You can provide existing database user accounts or [create database users](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-connections#create-user).

**Note:** For Cloud SQL for PostgreSQL instances, you have the option to [use the service agent as the database user](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-connections#postgresql-iam) instead.
  4. Recommended: [Increase the maximum number of connections](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-connections#update-max-connections) that Sensitive Data Protection can use to profile your data. Increasing the connections can speed up discovery.




## Supported services

This feature supports the following:

  * Cloud SQL for MySQL
  * Cloud SQL for PostgreSQL



Cloud SQL for SQL Server isn't supported.

## Processing and storage regions

Sensitive Data Protection is a regional and multi-regional service; it doesn't distinguish between zones. When Sensitive Data Protection profiles a Cloud SQL instance, the data is processed in its current region, but not necessarily its current zone. For example, if a Cloud SQL instance is stored in the `us-central1-a` zone, then Sensitive Data Protection processes and stores the data profiles in the `us-central1` region.

For more information, see [Data residency considerations](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency).

## Before you begin

  1. Confirm that you have the IAM permissions that are required to configure data profiles at the [organization](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#permissions-to-configure-org) level.

If you don't have the Organization Administrator (`roles/resourcemanager.organizationAdmin`) or Security Admin (`roles/iam.securityAdmin`) role, you can still create a scan configuration. However, after you create the scan configuration, someone with either of those roles must [grant data profiling access](https://docs.cloud.google.com/sensitive-data-protection/docs/grant-data-profiling-access) to your service agent. 

  2. You must have an inspection template in each region where you have data to be profiled. If you want to use a single template for multiple regions, you can use a template that is stored in the `global` region. If organizational policies prevent you from creating an inspection template in the `global` region, then you must set a dedicated inspection template for each region. For more information, see [Data residency considerations](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency). 

This task lets you create an inspection template in the `global` region only. If you need dedicated inspection templates for one or more regions, you must [create those templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect#create_a_new_inspection_template) before performing this task. 

  3. To send Pub/Sub notifications to a topic when certain events occur—such as when Sensitive Data Protection profiles a new table—[create a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/admin#create_a_topic) before performing this task. 

  4. You can configure Sensitive Data Protection to automatically attach tags to your resources. This feature lets you conditionally grant access to those resources based on their calculated sensitivity levels. If you want to use this feature, you must first complete the tasks in [Control IAM access to resources based on data sensitivity](https://docs.cloud.google.com/sensitive-data-protection/docs/control-access-based-on-data-sensitivity). 

  5. You can configure Sensitive Data Protection to automatically attach aspects to the profiled Cloud SQL resources based on discovery insights. If you want to use this feature, you must enable the integration of universal catalog on your [Cloud SQL for MySQL instance](https://docs.cloud.google.com/sql/docs/mysql/dataplex-catalog-integration#enable-dataplex-catalog) or [Cloud SQL for PostgreSQL instance](https://docs.cloud.google.com/sql/docs/postgres/dataplex-catalog-integration#enable-dataplex-catalog). 




To generate data profiles, you need a [service agent container and a service agent](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#service-agent-container) within it. This task lets you create them automatically. 

## Create a scan configuration

  1. Go to the **Create scan configuration** page.

[Go to Create scan configuration](https://console.cloud.google.com/security/sensitive-data-protection/create/discoveryConfiguration;source=7)

  2. Go to your organization. On the toolbar, click the project selector and select your organization.




The following sections provide more information about the steps in the **Create scan configuration** page. At the end of each section, click **Continue**.

### Select a discovery type

Select **Cloud SQL**.

### Select scope

Do one of the following: 

  * To configure profiling at the organization level, select **Scan entire organization**.
  * To configure profiling at the level of a folder, select **Scan selected folder**. Click **Browse** and select the folder. 



### Manage schedules

If the [default profiling frequency](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#scan-frequency) suits your needs, you can skip this section of the **Create scan configuration** page.

Configure this section for the following reasons:

  * To make fine-grained adjustments to the profiling frequency of all your data or certain subsets of your data.
  * To specify the tables that you don't want to profile.
  * To specify the tables that you don't want profiled more than once.



To make fine-grained adjustments to profiling frequency, follow these steps:

  1. Click **Add schedule**.
  2. In the **Filters** section, you define one or more filters that specify which tables are in the schedule's scope. A table is considered to be in the schedule's scope if it matches at least one of the filters defined.

To configure a filter, specify at least one of the following:

     * A project ID or a regular expression that specifies one or more projects.
     * An instance ID or a regular expression that specifies one or more instances.
     * A database ID or a regular expression that specifies one or more databases.
     * A table ID or a regular expression that specifies one or more tables. Enter this value in the **Database resource name or regular expression** field.

Regular expressions must follow [RE2 syntax](https://github.com/google/re2/wiki/Syntax).

For example, if you want all tables in a database to be included in the filter, enter the database ID in the **Database ID** field.

To match a filter, a table must meet all the regular expressions specified within that filter.

If you want to add more filters, click **Add filter** and repeat this step.

  3. Click **Frequency**.

  4. In the **Frequency** section, specify whether the discovery service should profile the tables you selected and, if so, how often:

     * If you never want the tables to be profiled, turn off **Do profile this data**.

     * If you want the tables to be profiled at least once, leave **Do profile this data** on.

In the succeeding fields in this section, you specify whether the system should reprofile your data and what events should trigger a reprofile operation. For more information, see [Frequency of data profile generation](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#scan-frequency).

       1. For **On a schedule** , specify how often you want the the tables to be reprofiled. The tables are reprofiled regardless of whether they underwent any changes.
       2. For **When schema changes** , specify how often Sensitive Data Protection should check if the selected tables had _schema_ changes after they were last profiled. Only tables with schema changes will be reprofiled.
       3. For **Types of schema change** , specify which types of schema changes should trigger a reprofile operation. Select one of the following: 
          * **New columns** : Reprofile the tables that gained new columns. 
          * **Removed columns** : Reprofile the tables that had columns removed.

For example, suppose you have tables that gain new columns every day, and you need to profile their contents each time. You can set **When schema changes** to **Reprofile daily** , and set **Types of schema change** to **New columns**.

       4. For **When inspect template changes** , specify whether you want your data to be reprofiled when the associated inspection template is updated, and if so, how often. **Note:** You specify the inspection templates to use in the Select inspection template step on this page.

An inspection template change is detected when either of the following occurs:

          * The name of an inspection template changes in your scan configuration.
          * The [`updateTime`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.inspectTemplates#InspectTemplate.FIELDS.update_time) of an inspection template changes.

For example, if you set an inspection template for the `us-west1` region and you update that inspection template, then only data in the `us-west1` region will be reprofiled.



* Click **Conditions**.

In the **Conditions** section, you specify the types of database resources that you want to profile. By default, Sensitive Data Protection is set to profile all supported database resource types. When Sensitive Data Protection adds support for more database resource types, those types will automatically be profiled, too.

* Optional: If you want to explicitly set the database resource types that you want to profile, follow these steps:

  1. Click the **Database resource types** field.
  2. Select the database resource types that you want to profile.



If Sensitive Data Protection later adds discovery support for more Cloud SQL database resource types, those types will only be profiled if you return to this list and select them.

* Click **Done**.

* Optional: To add more schedules, click **Add schedule** and repeat the previous steps.

* To specify precedence between schedules, reorder them using the arrow_upward up and arrow_downward down arrows.

The order of the schedules specifies how conflicts between schedules are resolved. If a table matches the filters of two different schedules, the schedule higher in the schedules list dictates the profiling frequency for that table.

**Note:** If your discovery pricing mode is [subscription mode](https://cloud.google.com/sensitive-data-protection/pricing#discovery-subscription-mode-pricing), the rate at which Sensitive Data Protection profiles your data is affected by how much capacity you purchased. To determine your daily profiling capacity, see [Monitoring utilization](https://cloud.google.com/sensitive-data-protection/pricing#subscription-monitoring). If you have [under-provisioned capacity](https://cloud.google.com/sensitive-data-protection/pricing#underprovisioned), then the profiling frequencies that you set in your schedules might not be followed. If there is a backlog of data to be profiled, the schedule order doesn't dictate the order in which Sensitive Data Protection profiles the data in the backlog. Rather, all data resources in scope get a randomly assigned slot in the queue.
* Optional: Edit or turn off **Catch-all schedule**.

The last schedule in the list is the catch-all schedule. This schedule covers the tables in your selected scope that don't match any of the schedules that you created. The catch-all schedule follows the [system default profiling frequency](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#scan-frequency).

  * To adjust the catch-all schedule, click edit **Edit schedule** , and then adjust the settings as needed.
  * To prevent Sensitive Data Protection from profiling any resource that is covered by the catch-all schedule, turn off **Profile the resources that don't match any custom schedule**.



### Select inspection template

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

The inspection template that you enter must be in the same region as the data to be profiled.

To respect data residency, Sensitive Data Protection doesn't use an inspection template outside the region where that template is stored.

To find the full resource name of an inspection template, follow these steps:

     1. Go to your inspection templates list. This page opens on a separate tab. 

[Go to inspection templates](https://console.cloud.google.com/security/sensitive-data-protection/landing/configuration/templates)

     2. Select the project that contains the inspection template that you want to use.
     3. Select **Configuration > Templates > Inspect**, and then click the template ID of the template that you want to use.
     4. On the page that opens, copy the full resource name of the template. The full resource name follows this format: 
            
            projects/PROJECT_ID/locations/REGION/inspectTemplates/TEMPLATE_ID

     5. On the **Create scan configuration** page, in the **Template name** field, paste the full resource name of the template.
  3. To add an inspection template for another region, click **Add inspection template** and enter the template's full resource name. Repeat this for each region where you have a dedicated inspection template.
  4. Optional: Add an inspection template that's stored in the `global` region. Sensitive Data Protection automatically uses that template for data in regions where you don't have a dedicated inspection template.
**Caution:** If you don't include an inspection template that's stored in the `global` region, Sensitive Data Protection can't profile data in regions that don't have a dedicated inspection template. For more information, see [Data residency considerations](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency). 


### Add actions

This section describes how to specify actions that you want Sensitive Data Protection to take after profiling a table. These actions are useful if you want to send insights gathered from data profiles to other Google Cloud services.

**Note:** For information about how other Google Cloud services may charge you for configuring actions, see [Pricing for exporting data profiles](https://cloud.google.com/sensitive-data-protection/pricing#exporting-profiles-pricing).

#### Publish to Google Security Operations

[Metrics](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference) gathered from data profiles can add context to your Google Security Operations findings. The added context can help you determine the most important security issues to address.

For example, if you're investigating a particular service agent, Google Security Operations can determine what resources the service agent accessed and whether any of those resources have high-sensitivity data.

To send your data profiles to your Google Security Operations instance, turn on **Publish to Google Security Operations**.

If you don't have a Google Security Operations instance enabled for your organization—through the [standalone product](https://cloud.google.com/security/products/security-operations) or through [Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs)—turning on this option has no effect. 

#### Publish to Security Command Center

Findings from data profiles provide context when you triage and develop response plans for your vulnerability and threat findings in [Security Command Center](https://docs.cloud.google.com/security-command-center/docs).

**Note:** You can also configure Security Command Center to automatically prioritize resources for the [attack path simulation feature](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn) according to the calculated sensitivity of the data that the resources contain. For more information, see [Set resource priority values automatically by data sensitivity](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#priority-values-auto-by-data-sensitivity). Before you can use this action, Security Command Center must be activated at the organization level. Turning on Security Command Center at the organization level enables the flow of findings from integrated services like Sensitive Data Protection. Sensitive Data Protection works with Security Command Center in all service tiers. 

If Security Command Center isn't activated at the organization level, Sensitive Data Protection findings won't appear in Security Command Center. For more information, see [Check the activation level of Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#check-scc-activation-level). 

To send the results of your data profiles to Security Command Center, make sure the **Publish to Security Command Center** option is turned on.

For more information, see [Publish data profiles to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc).

#### Save data profile copies to BigQuery

Sensitive Data Protection saves a copy of each generated data profile in a BigQuery table. If you don't provide the details of your preferred table, Sensitive Data Protection creates a dataset and table in the service agent container. By default, the dataset is named `sensitive_data_protection_discovery` and the table is named `discovery_profiles`.

**Important:** The output table uses [`DataProfileBigQueryRowSchema`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileBigQueryRowSchema) as its schema. This schema can change as Sensitive Data Protection adds features. Make sure that your workflows can handle schema changes, for example, by ignoring unknown fields.

This action lets you keep a history of all of your generated profiles. This history can be useful for creating audit reports and [visualizing data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles). You can also load this information into other systems.

Also, this option lets you see all of your data profiles in a single view, regardless of which region your data resides in. Although you can also [view the data profiles through the Google Cloud console](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-data-profiles), the console displays the profiles in only one region at a time.

When Sensitive Data Protection fails to profile a table, it periodically retries. To minimize noise in the exported data, Sensitive Data Protection exports only the successfully generated profiles to BigQuery.

Sensitive Data Protection starts exporting profiles from the time you turn on this option. Profiles that were generated before you turned on exporting aren't saved to BigQuery.

**Note:** Your service agent must have write access on the table where the profile copies will be saved. If you don't have a service agent yet, Sensitive Data Protection lets you create one later in the **Create scan configuration** page.

For example queries that you can use when analyzing data profiles, see [Analyze data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles).

#### Save sample discovery findings to BigQuery

Sensitive Data Protection can add sample findings to a BigQuery table of your choice. Sample findings represent a subset of all findings and might not represent all infoTypes that were discovered. Normally, the system generates around 10 sample findings per table, but this number can vary for each discovery run.

Each finding includes the actual string (also called _quote_) that was detected and its exact location.

This action is useful if you want to evaluate whether your [inspection configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#inspection-template) is correctly matching the type of information that you want to flag as sensitive. Using the exported data profiles and the exported sample findings, you can run queries to get more information about the specific items that were flagged, the infoTypes they matched, their exact locations, their calculated sensitivity levels, and other details.

**Important:** The output table uses [`DataProfileFinding`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileFinding) as its schema. This schema can change as Sensitive Data Protection adds features. Make sure that your workflows can handle schema changes, for example, by ignoring unknown fields.

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

#### Attach tags to resources

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
     2. Specify whether to include the full table profile in the notification, or just the full resource name of the table that was profiled.

     3. Set the minimum data risk and sensitivity levels that must be met for Sensitive Data Protection to send a notification.

     4. Specify whether only one or both of the data risk and sensitivity conditions must be met. For example, if you choose `AND`, then both the data risk and the sensitivity conditions must be met before Sensitive Data Protection sends a notification.


**Note:** Your service agent must have [ publishing access](https://docs.cloud.google.com/pubsub/docs/access-control#console) on the Pub/Sub topic. An example of a role that has publishing access is the Pub/Sub Publisher role (`roles/pubsub.publisher`). If you don't have a service agent yet, Sensitive Data Protection lets you create one later in the **Create scan configuration** page. If there are configuration or permission issues with the Pub/Sub topic, Sensitive Data Protection retries sending the Pub/Sub notification for up to two weeks. After two weeks, the notification is discarded. 

#### Send to Knowledge Catalog as aspects

This action lets you add [Knowledge Catalog aspects](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata#aspects) to profiled tables based on insights from data profiles. This action is only applied to new and updated profiles. Existing profiles that aren't updated aren't sent to Knowledge Catalog. 

When you enable this action, Sensitive Data Protection attaches the `Sensitive Data Protection profile` aspect to the [Knowledge Catalog entry](https://docs.cloud.google.com/dataplex/docs/ingest-custom-sources#entries) for each new or updated table that you profile. The generated aspects contain insights gathered from the data profiles. You can then search your organization and projects for entries with specific `Sensitive Data Protection profile` aspect values.

To send the data profiles to Knowledge Catalog, make sure that the **Send to Dataplex Catalog as aspects** option is turned on.

For more information, see [Add Knowledge Catalog aspects based on insights from data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects). 

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

### Set location to store configuration

Click the **Resource location** list, and select the region where you want to store this scan configuration. All scan configurations that you later create will also be stored in this location.

Where you choose to store your scan configuration doesn't affect the data to be scanned. Your data is scanned in the same region where that data is stored. For more information, see [Data residency considerations](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency).

**Note:** If you already have an existing scan configuration, you can't change the value set in this field. All scan configurations are stored in the same location. If you want to change the location of all your scan configurations, you must [delete](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#delete-config) them, recreate them, and store them in the new location.

### Review and create

  1. If you want to make sure that profiling doesn't start automatically after you create the scan configuration, select **Create scan in paused mode**. 

This option is useful in the following cases:

     * Your Google Cloud administrator still needs to [grant data profiling access](https://docs.cloud.google.com/sensitive-data-protection/docs/grant-data-profiling-access) to the service agent.
     * You want to create multiple scan configurations and you want some configurations to [override](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#overriding-scan-configs) others.
     * You opted to save data profiles to BigQuery and you want to make sure the service agent has write access to the BigQuery table where the data profile copies will be saved.
     * You opted to save sample discovery findings to BigQuery and you want to make sure that the service agent has write access to the BigQuery table where the sample findings will be saved.
     * You configured Pub/Sub notifications and you want to [grant publishing access](https://docs.cloud.google.com/pubsub/docs/access-control#console) to the service agent.
     * You enabled the **Attach tags to resources** action and you need to [grant the service agent access to the sensitivity level tag](https://docs.cloud.google.com/sensitive-data-protection/docs/control-access-based-on-data-sensitivity#grant-service-agent-permission-on-tag).
  2. Review your settings and click **Create**. 

Sensitive Data Protection creates the scan configuration and adds it to the discovery scan configurations list.




To view or manage your scan configurations, see [Manage scan configurations](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations).

Sensitive Data Protection starts identifying your Cloud SQL instances and creating a default connection for each instance. Depending on the number of instances in scope of discovery, this process can take a few hours. You can exit the Google Cloud console and check your connections later. 

When the default connections are ready, update those connections with the database user credentials that you want Sensitive Data Protection to use to profile your Cloud SQL instances. For more information, see [Manage connections for use with discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-connections). 

**Note:** We regularly improve our detection algorithm. If we find that your organization or project would benefit from a new improvement that we implement, we might automatically regenerate your data profiles and redo the [actions in your scan configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder#manage-scan-outcome). You won't incur Sensitive Data Protection charges for this operation. However, because we will redo the actions, you might incur charges for your use of other Google Cloud services. For example, if you configured Sensitive Data Protection to save the data profiles to BigQuery, you might incur BigQuery charges.

## What's next

Learn how to [update your connections](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-connections).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
