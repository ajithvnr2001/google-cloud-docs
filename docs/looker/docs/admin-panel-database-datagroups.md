---
url: https://docs.cloud.google.com/looker/docs/admin-panel-database-datagroups/
title: Admin settings - Datagroups \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:29.200667+00:00
---

# Admin settings - Datagroups  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-database-datagroups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Datagroups Stay organized with collections  Save and categorize content based on your preferences. 

[Datagroups](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#specifying_caching_policies_with_datagroup_parameters) let you specify query caching policies and triggers for rebuilding PDTs. If you have [permissions to access the **Datagroups** page](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_datagroups) in the **Database** section of the Admin panel, you'll see a summary of datagroups defined in a model for which they have [data access](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management#controlling_feature_and_data_access).

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

## Datagroup information

The **Datagroups** page provides the following information for each datagroup:

Column | Definition  
---|---  
Name | The name of the datagroup, which you define in the model file.   
Label | Specifies an optional datagroup label, which you define for the `datagroup` parameter in the model file.  
Connection | The database connection of the datagroup.  
Model | The LookML model where the datagroup is defined. (Click the **LookML** button to open the LookML model file.)  
Type | The datagroup's trigger type, such as [`sql_trigger`](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup#sql_trigger) or [`interval_trigger`](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup#interval_trigger). If the datagroup has no specified trigger type, **Type** will be blank.  
Description | Specifies an optional datagroup description, which you define for the `datagroup` parameter in the model file. The datagroup description can be used to explain the datagroup's purpose and mechanism.  
Actions | Actions you can take on the datagroup (see the Datagroup actions section for more details).   
  
Depending on the datagroup status, the following detailed information may also appear under the name:

  * **Status** shows the current status of the datagroup. The status is also indicated by the colored dots next to each line for the datagroup:
    * **Green** — The datagroup is in a ready state.
    * **Orange** — The datagroup is in the triggered state, or the datagroup was recently deployed to production and the trigger check cycle has not yet started.
    * **Red** — The most recent trigger check errored, or there is an error with the datagroup's LookML. You can click the **LookML** button to open the LookML model file.
  * **Trigger value** shows the result of the [`sql_trigger`](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup#sql_trigger) query that triggered the datagroup. For example, if a datagroup uses a SQL trigger based on the maximum ETL log ID, the **Trigger value** would show the new ETL log ID that triggered the datagroup.
  * **Triggered since** is displayed for datagroups in the triggered state to show how long it has been since the datagroup was triggered. This provides information on how long it is taking to rebuild PDTs and run the queries that triggered by the datagroup. Once all PDTs are rebuilt, the datagroup's color will update to green to indicate that the datagroup is ready, and after several minutes the **Triggered since** information will disappear from the page since the datagroup is complete.
  * **Trigger error** provides error information for the datagroup triggers, such as a syntax error in the datagroup's SQL trigger. When you see an error, you can click the **LookML** button to open the LookML model file and correct the SQL syntax.
  * **Trigger last checked** shows the last time that the datagroup's `sql_trigger` SQL query was run. If the value returned by the query is different next time, that triggers the datagroup.
  * **Cache reset at** shows the time when the cache was last reset (when the cached data in the datagroup was last invalidated).



## Datagroup actions

If you have the [necessary permissions for updating datagroups](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#update_datagroups), you can perform the following actions on datagroups from the **Datagroups** Admin page:

  1. Click the **LookML** button to open the LookML model file where the datagroup is defined.
  2. Select **Reset Cache** from the gear menu settings to immediately invalidate the cached results for all Explores using that datagroup.
  3. Select **Trigger Datagroup** from the gear menu settings to invalidate the cached results for all Explores and rebuild all PDTs using that datagroup. The PDT rebuild will begin based on the next time specified in the connection's [**PDT and Datagroup Maintenance Schedule**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt_maintenance_schedule) field, such as every five minutes. Any scheduled data deliveries of [Looks](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#specifying_the_datagroup_trigger), [dashboards](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#schedules_triggered_by_datagroup_updates), and [LookML dashboards](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#schedules_triggered_by_datagroup_updates) that use the datagroup as a trigger will be sent when the triggered datagroup reaches the ready state.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
