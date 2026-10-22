---
url: https://docs.cloud.google.com/stackdriver/docs/deprecations/metadata-labels/
title: Obsolete resource metadata labels \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:17.829666+00:00
---

# Obsolete resource metadata labels  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/deprecations/metadata-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Resources ](https://docs.cloud.google.com/stackdriver/quotas)



Send feedback 

#  Obsolete resource metadata labels Stay organized with collections  Save and categorize content based on your preferences. 

Monitored resources in Cloud Monitoring come with a set of labels that are used to identify a particular instance of the monitored-resource type. These labels are documented for each monitored-resource type in the [Monitored resource list](https://docs.cloud.google.com/monitoring/api/resources).

In addition, Monitoring might create additional labels to capture metadata about a monitored resource. These system metadata labels are available to users as read-only values. Users can also create their own resource metadata labels. For more information, see [Resource metadata labels](https://docs.cloud.google.com/monitoring/api/v3/metric-model#meta-labels).

A group of monitored-resource metadata labels has been deprecated. The labels in the set are either redundant and can be replaced by existing equivalent labels, or they represent obsolete concepts that are no longer supported by Cloud Monitoring alerting policies, charts, scorecards, or resource groups.

## Effects of the deprecation

All alerting policies, charts, scorecards, and resource groups that specify a monitored resource and use metadata labels for which replacement labels could be determined were automatically migrated to use the replacements by July 31, 2020. **All other uses of deprecated labels must be manually migrated.** This page provides information about how to migrate them.

**Notes:**

  * If you have a filter that does not specify a monitored resource but uses metadata labels, it was not possible to determine if the metadata label is deprecated: metadata labels are not unique across monitored resources, and the deprecated labels are associated with specific monitored resources. You must evaluate such filters manually.
  * Metadata labels in filters in a secondary aggregation were not migrated automatically.
  * Metadata labels in queries written in Monitoring Query Language (MQL) were not migrated automatically.



Any alerting policies, charts, scorecards, and resource groups using metadata labels that were not migrated automatically or manually by July 31, 2020, are no longer supported and might stop working.

## Required action

To repair alerting policies, charts, scorecards, or resource groups that have stopped working because of deprecated metadata labels, you must take some action. You can remove the alerting policies, charts, scorecards, or groups, or you can modify any filters that use those deprecated labels to use labels that provide similar behavior.

Similarly, if you have filters that use metadata labels but do not specify monitored resources, it isn't possible to determine automatically if these labels are deprecated. You must evaluate and address them manually.

This page includes a script to help you identify uses of deprecated metadata labels.

## Deprecated metadata labels

The following table lists the resource metadata labels being deprecated and their replacements, if any.

**Note:** In filters, the label prefix `resource.metadata` is used where the table shows the prefix `metadata.system_labels`. For example, the label shown as `metadata.system_labels.name` in the table is referred as `resource.metadata.name` in filters.Monitored-resource type | Deprecated label | Equivalent label  
---|---|---  
All Google Cloud types | `metadata.system_labels.cloud_account`* | `resource.labels.project_id`  
`cloud_tasks_queue` | `metadata.system_labels.name`  
`metadata.system_labels.state` | `resource.labels.queue_id`  
**none**  
`dataflow_job` | `metadata.system_labels.name`  
`metadata.system_labels.state` | `resource.labels.job_name`  
**none**  
`gae_app` | `metadata.system_labels.gaeapp`  
`metadata.system_labels.gaemodule`  
`metadata.system_labels.gaeversion` | **none †**  
consider `resource.labels.project_id`  
**none †**  
consider `resource.labels.module_id`  
**none †**  
consider `resource.labels.version_id`  
  
`gce_disk` | `metadata.user_labels.name`‡ | `metadata.system_labels.name`  
`gce_instance` | `metadata.user_labels.name`‡ | `metadata.system_labels.name`  
`l7_lb_rule` | `metadata.system_labels.state` | **none**  
`pubsub_topic` | `metadata.system_labels.name`# | `metadata.system_labels.name`  
`pubsub_subscription` | `metadata.system_labels.name`#  
| `metadata.system_labels.name`  
`vpn_gateway` | `metadata.system_labels.region` | `resource.labels.region`  
  
* The Cloud Monitoring filter syntax does not allow the `resources.labels.project_id` label to be used as flexibly as the `metadata.system_labels.cloud_account` label could be used. For example, you can't do the following: 

  * Use `OR` to combine an expression using the `project_id` label and an expression using metadata labels.
  * Use the `!=` operation with the `project_id` label.
  * Use the functions `starts_with` or `has_substring` with the `project_id` label.



† For `gae_app` resources: The noted resource labels are similar to the deprecated metadata labels, so they might be good replacements. But because they are only similar, they were not migrated automatically.

‡ For `gce_disk` and `gce_instance` resources: If you do not otherwise set `metadata.user_labels.name`, it had been auto-populated with the value from `metadata.system_labels.name`. **This auto-population also ended on July 31, 2020.** Alerting policies, charts, scorecards, and resource groups that filter on auto-populated `metadata.user_labels.name` value were migrated to use `metadata.system_labels.name` instead.

# For `pubsub_topic` and `pubsub_subscription` resources: We have fixed a long-standing bug causing `metadata.system_labels.name` to be automatically converted to lowercase (for example, `"My-Subscription"` became `"my-subscription"`). This produced unexpected behavior in cases where users had multiple resources whose lowercase names are identical. **This behavior also ended on July 31, 2020.** After this date, the metadata system label `name` reflects the actual name of the topic or subscription (for example, `"My-Subscription"`).

## What do I need to do?

There are two high-level steps:

  1. Determine if you are using any metadata labels affected by this deprecation. See Find deprecated metadata labels for information on running the provided detector script.

  2. If you are using any affected metadata labels, update or remove them. See Update your filters for more detailed steps.




### Find deprecated metadata labels

You can use this Python script to identify references to deprecated metadata labels: [`metadata_label_detection.py`](https://docs.cloud.google.com/static/stackdriver/docs/deprecations/metadata_label_detection.py).

**Note:** The script can't detect metadata labels in filters in secondary aggregations.

**Syntax summary:** `python3 metadata_label_detection.py PROJECT_ID_OR_NUMBER`

`PROJECT_ID_OR_NUMBER` can be either a project ID (for example, `my-project`), or a project number (for example, `123456789`). Do not include the `projects/` prefix.

The following steps describe a way to use the script:

  1. Go to the Google Cloud console.

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. Click **Activate Cloud Shell** at the top of the Google Cloud console page for your project.

  3. Click **Open Editor** on the Cloud Shell toolbar. If the workspace for your home directory is not already open, open it by selecting **File** and then **Open Workspace**. Choose the workspace with your username.

  4. Create a new file called `metadata_label_detection.py` by selecting **File** and then **New File**. Paste the text of the [`metadata_label_detection.py`](https://docs.cloud.google.com/static/stackdriver/docs/deprecations/metadata_label_detection.py) into the editor. Save the file by selecting **File** and then **Save**.

  5. Go back to the terminal by clicking **Open Terminal** on the Cloud Shell toolbar.

  6. At the command-line prompt in Cloud Shell, install the script dependencies by running the following command:
         
         sudo pip3 install google-cloud-monitoring=="1.*" google-cloud-monitoring-dashboards
         

  7. After installing the dependencies, run the detector script:
         
         python3 metadata_label_detection.py $GOOGLE_CLOUD_PROJECT
         




The script generates a report like the following excerpt:
    
    
    Alert "Test alert" (projects/PROJECT_ID/alertPolicies/8401129027900817186) is affected.
    URL: https://console.cloud.google.com/monitoring/alerting/policies/8401129027900817186?project=PROJECT_ID
            metadata.system_labels.cloud_account is deprecated for non-AWS resource
    types. Please manually remove the reference.
    
    Group "Test group" (projects/PROJECT_ID/groups/4518177785663978371) might be affected,
    depending on the type of resources it is used for.
    URL: https://console.cloud.google.com/monitoring/groups/4518177785663978371?project=PROJECT_ID
            metadata.system_labels.name is deprecated for dataflow_job. Please
    manually remove the reference if this group is used for dataflow_job resources.
            metadata.system_labels.name is deprecated for cloud_tasks_queue. Please
    manually remove the reference if this group is used for cloud_tasks_queue resources.
    
    Xy_chart "Test chart" in dashboard "Demo dashboard" (projects/PROJECT_ID/dashboards/2826428163455705326) is affected.
    URL: https://console.cloud.google.com/monitoring/dashboards/custom/2826428163455705326?project=PROJECT_ID
            metadata.user_labels.name is deprecated for gce_instance. Please
    manually remove the reference.
    

**Note:** In filters, the label prefix `resource.metadata` is used where the script reports the prefix `metadata.system_labels`. For example, the label shown as `metadata.system_labels.name` in the output is referred as `resource.metadata.name` in filters.

### Update your filters

To update your alerting policies, charts, scorecards, and resource groups:

  1. Log into the Google Cloud console.

  2. Run the detector script as described in Find deprecated labels.

  3. Inspect each of your alerting policies, charts, and resource groups to check if the value you're retrieving comes from one of the deprecated labels identified by the script.

To check the all the charts, you must check each chart on each custom dashboard you have defined.

Remember that filters use the prefix `resource.metadata` instead of `metadata.system_labels`.

**Note:** If you created dashboards containing scorecards by using the API, you must use the API to check them. Scorecards can't be edited from the Google Cloud console.

For each deprecated label, do one of the following:

     * If the label has no replacement, remove the use of the label or delete the alerting policy, chart, or resource group.

     * If the label has a replacement, replace the deprecated label with the replacement.

If you do nothing, the affected alerting policy, chart, or resource group will not work.

For additional help on making updates by using the Google Cloud console, see the resources listed in Editing.

In some cases, you might need to use the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api/ref_v3/rest) rather than the Google Cloud console. The API can express some queries that can't otherwise be constructed.

  4. Run the detector script again, to verify that no deprecated labels remain.




## Additional information

For information on resource metadata labels, filters, or specific monitored-resource types, see the following:

  * Labels: [Resource metadata labels](https://docs.cloud.google.com/monitoring/api/v3/metric-model#meta-labels)
  * Filters: [Monitoring filters](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option)
  * Specific monitored-resource types: [Monitored resource list](https://docs.cloud.google.com/monitoring/api/resources)



### Editing

For information on updating alerting policies, charts, dashboards, and resources groups, see the following:

  * Alerting policies: [Managing policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#managing_policies)
  * Dashboards and charts by using the Google Cloud console: [Managing dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards)
  * Dashboards by using the Monitoring API: [Updating dashboards](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard#update)
  * Resource groups: [Editing a group](https://docs.cloud.google.com/monitoring/groups#editing_groups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
