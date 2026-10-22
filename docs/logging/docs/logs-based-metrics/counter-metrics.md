---
url: https://docs.cloud.google.com/logging/docs/logs-based-metrics/counter-metrics/
title: Configure counter metrics \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:36.095878+00:00
---

# Configure counter metrics  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/logs-based-metrics/counter-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Configure counter metrics Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a counter-type log-based metric by using the Google Cloud console, the Logging API, and the Google Cloud CLI.

[_Counter metrics_](https://docs.cloud.google.com/logging/docs/logs-based-metrics#counter-metric) count the number of log entries that match a given filter. For example, you can create a log-based metric that counts the number of log entries that contain a specific error message. Log-based metrics can apply within a single Google Cloud project or within a log bucket.

For an overview of log-based metrics, see [Log-based metrics overview](https://docs.cloud.google.com/logging/docs/logs-based-metrics).

## Before you begin

  1. To use log-based metrics, you must have a Google Cloud project with billing enabled:

     1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
     2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

     4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Ensure that your Identity and Access Management role includes the permissions required to create and view log-based metrics, and to create alerting policies. For details, see [Permissions for log-based metrics](https://docs.cloud.google.com/logging/docs/access-control#metrics-permissions).




## Create a counter-type log-based metric

The metric counts the log entries identified by a filter you provide. You can use [regular expressions](https://docs.cloud.google.com/logging/docs/view/logging-query-language#regular-expressions) in your filter, and we recommend that you include a resource type. The length of a filter can't exceed 20,000 characters.

Don't put sensitive information in the filter. Filters are treated as service data.

**Note:** See the following [Troubleshooting](https://docs.cloud.google.com/logging/docs/logs-based-metrics/troubleshooting#undefined-resource) section if you're creating log-based metrics on audit logs.

### Console

Follow these steps to create a counter metric in the Google Cloud console in your Google Cloud project:

  1. In the Google Cloud console, go to the **Log-based Metrics** page: 

[Go to **Log-based Metrics**](https://console.cloud.google.com/logs/metrics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Click **Create metric**. The **Create logs metric** panel appears.

  3. Set the **Metric type** : Select **Counter**.

  4. Set the following fields in the **Details** section:

     * **Log metric name** : Choose a name that is unique among the log-based metrics in your Google Cloud project. Some naming restrictions apply; see [Troubleshooting](https://docs.cloud.google.com/logging/docs/logs-based-metrics/troubleshooting#metric-name-restrictions) for details.
     * **Description** : Enter a description for the metric.
     * **Units** : Leave this blank or insert the digit **1**.
  5. Define your metric filter in the **Filter selection** section.

     1. Us the **Select project or log bucket** menu to choose whether the metric counts the log entries in your Google Cloud project or only those log entries in a specific log bucket.

     2. Create a filter that collects only the log entries that you want to count in your metric using the [logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language). You can also use regular expressions to create your metric's filters.

     3. To see which log entries match your filter, click **Preview logs**.

  6. (Optional) Add a label in the **Labels** section. For instructions on creating labels, see [Creating a label](https://docs.cloud.google.com/logging/docs/logs-based-metrics/labels#create-label).

  7. Click **Create metric** to create the metric.




### gcloud

You can create a log-based metric with no custom labels by using the following command:
    
    
    gcloud logging metrics create METRIC_NAME \
      --description="METRIC_DESCRIPTION" \
      --log-filter="FILTER" \
      [--bucket-name="BUCKET_NAME"]
    

**Note:** Choose a metric name that is unique among log-based metrics in your Google Cloud project. Some naming restrictions apply; see [Troubleshoot log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/troubleshooting#metric-name-restrictions) for details.

For example, the following command creates a project-scoped log-based metric called `error_count`.
    
    
    gcloud logging metrics create error_count \
         --description "Errors in syslog." \
         --log-filter "resource.type=gce_instance AND log_id(\"syslog\") AND severity>=ERROR"
    

To create a bucket-scoped log-based metric instead, provide the `--bucket_name` flag:
    
    
    gcloud logging metrics create error_count \
        --description "Errors in syslog." \
        --log-filter "resource.type=gce_instance AND log_id(\"syslog\") AND severity>=ERROR" \
        --bucket-name projects/my-project/locations/global/buckets/my-test-bucket
    

For instructions on creating labels, see [Configure labels on log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/labels).

### API

To create a counter metric, use the [`projects.metrics.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/create) method of the Logging API. If you use the APIs Explorer pane on the reference page, then prepare the arguments as follows:

  1. Set the **parent** field to the project or bucket in which the metric is to be created:

     * For a project-scoped log-based metric, specify the project:
    
    projects/PROJECT_ID
    

     * For a bucket-scoped log-based metric, specify the bucket:
    
    projects/PROJECT_ID/locations/LOCATION/bucket/BUCKET_ID
    

  2. Set the request body to a [`LogMetric`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric) object. Following is a sample object for a counter metric:
         
         {
           name:        "my-metric"
           description: "This is my metric."
           filter:      "resource.type=gce_instance AND log_id(\"syslog\")",
           metricDescriptor: {
               labels: [
                 {
                   key: "my-label",
                   valueType: STRING,
                   description: "This is my label.",
                 }
               ]
           },
           labelExtractors: {
             "my-label":
               "REGEXP_EXTRACT(jsonPayload.someField, \"before ([0-9]+) after\")",
             ...
           },
         }
         




Notes:

  * Choose a metric name that is unique among log-based metrics in your project. Some naming restrictions apply; see [Troubleshooting](https://docs.cloud.google.com/logging/docs/logs-based-metrics/troubleshooting#metric-name-restrictions) for details.

  * For counter metrics, the [`LogMetric`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric) fields `valueExtractor` and `bucketOptions` have no purpose and are omitted.

  * If your metric has no labels, you can omit the `metricDescriptor` and `labelExtractors` fields. If your metric does have labels, then see [log-based metrics labels](https://docs.cloud.google.com/logging/docs/logs-based-metrics/labels) for an introduction to labels and details about creating them in the API.




For more details, see the [`LogMetric`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric) type.

## Latency of new metrics

Your new metric appears in the Logs Explorer list of metrics and in the relevant Monitoring menus right away. Data is usually available in less than a minute.

## Inspect log-based metrics

To list the user-defined log-based metrics in your Google Cloud project or to inspect a particular metric in your Google Cloud project, do the following:

### Console

  1. In the Google Cloud console, go to the **Log-based Metrics** page: 

[Go to **Log-based Metrics**](https://console.cloud.google.com/logs/metrics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. In the **User-defined metrics** pane, you see the user-defined log-based metrics in the current Google Cloud project:

  3. To view the data in a log-based metric, click the _more_vert_ **Menu** in the metric's row and select **View in Metrics Explorer**.




### gcloud

To list the user-defined log-based metrics in your Google Cloud project, use the following command:
    
    
    gcloud logging metrics list
    

To display a user-defined log-based metric in your Google Cloud project, use the following command:
    
    
    gcloud logging metrics describe METRIC_NAME
    

To get help, use the following command:
    
    
    gcloud logging metrics --help
    

You can't read a metric's time series data from the Google Cloud CLI.

### API

### List metrics

To list the user-defined log-based metrics in a Google Cloud project, use the [`projects.metrics.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/list) API method. Fill in the parameters to the method as follows:

  * **parent** : The resource name of the Google Cloud project: `projects/PROJECT_ID`.
  * **pageSize** : The maximum number of results.
  * **pageToken** : Gets the next page of results. For information about using page tokens, see [`projects.metrics.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/list).



### Retrieve metric definitions

To retrieve a single user-defined log-based metric, use the [`projects.metrics.get`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/get) API method. Fill in the parameters to the method as follows:

  * **metricName** : The resource name of the metric:
        
        projects/PROJECT_ID/metrics/METRIC_ID
        




### Read metric data

To read the time series data in a log-based metric, use the [`projects.timeseries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) in the Cloud Monitoring API. For details on time series data, see [Reading time series](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics).

To read a single user-defined log-based metric, fill in the method's parameters with this metric type and identifier:
    
    
    logging.googleapis.com/user/METRIC_ID
    

## Update log-based metrics

You can edit a user-defined log-based metric to change its description, filter, and the names of fields referenced in the metric. You can add new labels to the metric and you can change the regular expressions used to extract values for the metric and its labels. If you're using a bucket-scoped metric, you can also update the metric's bucket.

You can't change the names or types of user-defined log-based metrics or their labels, and you can't delete existing labels in a log-based metric.

To edit a log-based metric, do the following:

### Console

  1. In the Google Cloud console, go to the **Log-based Metrics** page: 

[Go to **Log-based Metrics**](https://console.cloud.google.com/logs/metrics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Click **Edit metric** in the _more_vert_ **Menu** for the log-based metric that you want to modify.

  3. Change the allowable items in the metric.

  4. Click **Update metric**.




### gcloud

Use the Google Cloud CLI to change a counter metric's description, filter query and bucket. You can update any or all of the fields at once.
    
    
    gcloud logging update METRIC_NAME \
      --description="METRIC_DESCRIPTION" \
      --log-filter="FILTER" \
      --bucket-name=BUCKET_NAME
    

If you change the bucket associated with a bucket-scoped metric, then any metric data collected before the change no longer reflects the current configuration. The metric data collected for the previous bucket is not removed.

**Note:** The METRIC_NAME value must match an existing log-based metric in your Google Cloud project, or the update command creates a new metric.

To update distribution metrics or other counter metric fields, excluding the METRIC_NAME, create a file that contains the revised specification of your [`LogMetric`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric) in JSON or YAML format. Then, update the metric by calling the `update` command with the --config-from-file field, replacing FILENAME with the name of your JSON or YAML file:
    
    
    gcloud logging update METRIC_NAME --config-from-file FILENAME
    

For more details, use the following command:
    
    
    gcloud logging metrics update --help
    

### API

To edit a log-based metric, use the [`projects.metrics.update`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/update) method in the API. Set the fields as follows:

  * **metricName** : The full resource name of the metric:
        
        projects/PROJECT_ID/metrics/METRIC_ID
        

For example:
        
        projects/my-gcp-project/metrics/my-error-metric
        

  * In the request body, include a [`LogMetric`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric) object that is exactly the same as the existing metric except for the changes and additions you want to make.




## Delete log-based metrics

To delete a user-defined log-based metric, do the following:

### Console

  1. In the Google Cloud console, go to the **Log-based Metrics** page: 

[Go to **Log-based Metrics**](https://console.cloud.google.com/logs/metrics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select the metric you want to delete and click **Delete**.

Alternatively, click **Delete metric** in the _more_vert_ **menu** of the log-based metric that you want to delete.




### gcloud

Use the following command to delete a user-defined log-based metric in the current Google Cloud project:
    
    
    gcloud logging metrics delete METRIC_NAME
    

For more details, use the following command:
    
    
    gcloud logging metrics delete --help
    

### API

To delete a user-defined log-based metric, use the [`projects.metrics.delete`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/delete) method in the API.

In addition, in the Google Cloud console **Log-based metric** page, the **User-defined metrics** pane of the log-based metrics interface provides more features to help you manage the user-defined metrics on your Google Cloud project. See [User-defined metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#user-defined_metrics) for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
