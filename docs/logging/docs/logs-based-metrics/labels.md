---
url: https://docs.cloud.google.com/logging/docs/logs-based-metrics/labels/
title: Configure labels on log-based metrics \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:36.015455+00:00
---

# Configure labels on log-based metrics  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/logs-based-metrics/labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Configure labels on log-based metrics Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses log-based metrics labels, and explains how to create and use labels on log metrics.

If you're familiar with labels, then you can go directly to Create a label on this page.

## Overview of labels for log-based metrics

Labels let log-based metrics contain multiple time series—one for each combination of label values. All log-based metrics come with some default labels.

You can create additional user-defined labels in both counter-type and distribution-type metrics by specifying extractor expressions. An extractor expression tells Cloud Logging how to extract the label's value from log entries. You can specify the label's value as either of the following:

  * The entire contents of a named field in the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) object.
  * A part of a named field that matches a regular expression (regexp).



You can extract labels from the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) built-in fields, such as `httpRequest.status`, or from one of the payload fields `textPayload`, `jsonPayload`, or `protoPayload`. However, you can't extract the ID of an error group from the `errorGroups` field.

For information on regular expressions, see [RE2 Syntax](https://github.com/google/re2/wiki/Syntax).

Don't put sensitive information in the extractor expression and don't extract sensitive data into labels. These are treated as service data.

**Note:** Create labels only when you need to identify values to categorize or summarize your metric data. Don't use labels to give names to data fields.

### Limitations of user-defined labels

The following limitations apply to user-defined labels:

  * You can create up to 10 user-defined labels per metric.

  * After you create a label, you can't delete it.

    * You can modify the extractor expression and description of the label you have already created.

    * You can't change the name or value type of a label you have already created.

  * Only the first 1,024 characters of a label value are kept.

  * Each log-based metric is limited to about 30,000 active time series, which is dependent upon the number of possible values for each label, including default labels.

For example, if your log entries come from 100 resources such as VM instances, and you define a label with 20 possible values, then you can have up to 2,000 time series for your metric.


**Caution:** Never extract a label value that is unique for each log entry, such as the full `insertId` or `timestamp` fields. You will have as many time series as there are log entries, each containing one point.

If you have too many time series or too many data points, your costs will rise and your activity might be throttled. For more information on the cost of log-based metrics, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing). For information on the limits that apply to log-based metrics, see [Quotas and limits: Log-based metrics](https://docs.cloud.google.com/logging/quotas#metric-limits) and [Troubleshoot log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/troubleshooting).

## Default labels

Most log-based metrics come with some predefined labels:

  * **Resource labels** : All metrics use a monitored resource object to identify the source of time series data. Each resource type includes a type name and one or more labels. Examples of types of resources include VM instances, Cloud SQL databases, and load balancers.

The resource and its labels are listed separately from other metric labels in Cloud Monitoring, but they have the same effect: they create additional time series in the metric. For more information, see [Metrics, Time Series, and Resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

  * **log** : This label holds the value of the `LOG_ID` portion of the `logName` field in log entries.

  * **severity** : This label holds the value of the `severity` field in log entries. The severity label is provided by default only in [system log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#system-defined_metrics).




## View labels by using the Metrics Explorer

To view the labels on a time series generated for a log-based metric, do the following:

  1. In the Google Cloud console, go to the **Log-based Metrics** page: 

[Go to **Log-based Metrics**](https://console.cloud.google.com/logs/metrics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Find the metric you want to view, and then select **View in Metrics Explorer** from the metric's _more_vert_ **More** menu.

Before proceeding, wait until the chart displays data, which might take several minutes when you've created a log-based metric.

  3. To view the available labels, expand the **Filter** field. You might see resource labels and metric labels. The list of labels is specific to the resource type and the metric type. For example:

     * The `gce_instance` resource type has three _resource labels_ : `project_id`, `instance_id`, and `zone`.

     * The `logging/log_entry_count` metric type has two _metric labels_ : `log` and `severity`. Your user-defined labels also appear in this section.

  4. To verify that a user-defined label is extracting the correct data from your log entries, do the following:

     1. Change the **Aggregation** element to **Unaggregated**.

     2. In the chart, select either **Table** or **Both**.

     3. In the toolbar, select _view_column_ **Column display menu** , and then select your labels. This menu displays all labels for which there is data.

If you don't see a label you created, then verify the field name and the extractor expression.




## Create a label

You create user-defined labels when you create the metric. Both counter metrics and distribution metrics can have labels. You can't add labels to the system log-based metrics.

To create a label, you specify the field in the log entry, and then you define an expression that extracts a value from the specified field.

### Console

  1. When you [create a log-based metric](https://docs.cloud.google.com/logging/docs/logs-based-metrics/distribution-metrics), the **Create log-based metric** panel includes an option to add labels.

  2. Click **Add label**.

**Tip** : To see the fields and values inside a log entry, do the following:

     1. In the **Filter selection** section, click **Preview logs**.
     2. In the **View logs** pane, choose a log entry and click the **expander** _navigate_next_ next to it.
     3. Click **Expand nested fields**.
  3. Set the following fields in the **Labels** section:

     1. **Label name** : Enter a name for the label. For example, `ID`.   


The name must meet the following criteria:

        * Be no more than 100 characters in length.
        * Match the regular expression **[a-zA-Z][a-zA-Z0-9_]** *.
        * Consist of more than just the string "log".
     2. **Description** : Describe the label. Try to be as specific as possible about the format of expected logs values. For example, `Instance number`.

     3. **Label type** : Choose **STRING** , **BOOLEAN** , or **INTEGER**.

For more information about the various types of data that can be used to create log-based metrics, see [Data types for log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#metric-types).

     4. **Field name** : Enter the name of the log entry field that contains the label's value. You are offered choices as you type. In this sample, the field is:
            
            labels."compute.googleapis.com/resource_id"
            

     5. **Regular expression** : If your label's value consists of the field's entire contents, then you can leave this field empty. Otherwise, specify a regexp _capture group_ that extracts the label value from the field value.

For example, suppose the field typically contains text like the following:
            
            The instance number is 0123456789; the ID is my-test-instance22
            

If you want the label value to be the instance number, there are many regular expressions that will extract the correct number. For example, in the following expression, the parentheses are a capture group identifying the part of the text that will be extracted:
            
            The instance number is ([0-9]+); .*
            

For more information about regular expressions, see [RE2 Syntax](https://github.com/google/re2/wiki/Syntax).

  4. Click **Done** to create the label. You can add more labels by repeating these steps.

  5. To finish creating the metric, click **Create metric**.




### gcloud

To create a log-based metric with custom labels, you must create a file that contains a representation of your [`LogMetric`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric) definition in JSON or YAML format, including the custom labels. Then, create the metric by calling the `create` command with the `--config-from-file` flag, replacing FILENAME with the name of your JSON or YAML file:
    
    
    gcloud logging metrics create METRIC_NAME --config-from-file FILENAME
    

For more information, see [`gcloud logging metrics create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/metrics/create).

### API

Labels are specified as part of the [`LogMetric`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric) object in the request body of calls to the [`projects.metrics.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/create) method of the Logging API. For information about the full method calls, see [Creating counter metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/counter-metrics) or [Creating distribution metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/distribution-metrics).

For each label, you must add a segment to both the `metricDescriptor` and the `labelExtractors` fields in the [`LogMetric`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric).

The syntax is the following:
    
    
    {
      ...
      metricDescriptor: {
          labels: [
            { key: LABEL_NAME, valueType: LABEL_TYPE,
              description: LABEL_DESCRIPTION },
            ...
          ]
      },
      labelExtractors: {
        LABEL_NAME: EXTRACTOR_EXPRESSION,
        ...
      },
    }
    

The syntax elements have the following meaning:

  * LABEL_NAME: The name of the label as a string.
  * VALUE_TYPE: The type of the label: `STRING`, `BOOL`, or `INT64`.
  * LABEL_DESCRIPTION: A description of the label.
  * EXTRACTOR_EXPRESSION: A string that combines the log entry field name with an optional regular expression. The extractor expression can be one of the following:
        
        EXTRACT(FIELD)
        
        
        REGEXP_EXTRACT(FIELD, REGEXP)
        




For more information on regular expressions, see [RE2 Syntax](https://github.com/google/re2/wiki/Syntax).

Following is an example with two labels:
    
    
    {
      ...
      metricDescriptor: {
          labels: [
            { key: "label_name_a", valueType: STRING },
            { key: "label_name_b", valueType: INT64 },
          ]
      },
      labelExtractors: {
        "label_name_a":
          "REGEXP_EXTRACT(jsonPayload.field_a, \"before ([a-zA-Z ]+) after\")",
        "label_name_b": "EXTRACT(jsonPayload.field_b)",
      },
    }
    

For more details, see the [`LogMetric`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric) type.

## Examples

This section provides a few examples that might help you get started with creating labels on your user-defined log-based metrics. After you create a label, we recommend that you verify the labels by using the Metrics Explorer.

Tips:

  * You must use a capture group when you specify an extractor expression.
  * If you don't specify an extractor expression, then the entire value of the field is extracted.
  * Ensure that the set of possible values for any label is constrained. A small set of discrete values (like "red", "green", and "blue") is the preferred approach. If, for example, you extract the 8-bit RGB values for a color label, you can have over 16 million different values. This means that you could have over 16 million time series.

Don't extract high-resolution values like timestamps, any kind of unique identifier, user IDs, IP addresses, unparameterized URLs, and so forth.




### Extract the status code from an audit log

If a field doesn't contain any special characters, then you can use the field name in the label for the log-based metric.

For example, for audit logs, the `protoPayload` field conforms to the [`AuditLog`](https://docs.cloud.google.com/logging/docs/audit/api/ref/rest/Shared.Types/AuditLog) structure. Therefore, to extract the `status` field from an audit log, you can set the field name to `protoPayload.status.code` and leave the extractor expression empty.

If you only want to extract the first digit of the error code, the you might set the extractor expression to `(\d)\d\d`.

### Extract value from a field with special characters

If a field in a log entry contains special characters, then wrap the field with double quotes.

For example, to extract the entire value of the `k8s-pod/k8s-app` label, set the field name to `labels."k8s-pod/k8s-app"` and leave the expression empty.

### Extract a value from a text payload

**Note:** To ensure that the set of possible values for the label is constrained, always specify an extractor expression for text payload fields.

Consider a log entry that has the following format:
    
    
    textPayload: "unfinished_task_instance_count.py:61 Unfinished task instance count metric value 0 for state: deferred"
    

To extract the value for the state, such as `deferred` from log entries with the previous format, you might do something like:

  * Field name: `textPayload`
  * Extractor expression: `^unfinished.*state: ([a-z]+)`



### Extract value from a repeated field

A log entry might contain a field with repeated fields. In JSON, these fields are displayed using square brackets (`[]`). From the perspective of labels, consider the repeated fields as a set and the label extractor as an iterator. You provide the criteria for the match when you define the label, and the extractor iterates over the set until a match is found. The first match is always returned, even when multiple members of the set match the criteria.

You decide to create a log-based metric that counts audit logs. Before configuring your label, you review several audit logs and notice that the format of the `protoPayload` conforms to the [`AuditLog`](https://docs.cloud.google.com/logging/docs/audit/api/ref/rest/Shared.Types/AuditLog) structure. The following illustrates a portion of an audit log entry.
    
    
    {
      ...
      protoPayload: {
        @type: "type.googleapis.com/google.cloud.audit.AuditLog"
        authenticationInfo: {1}
        authorizationInfo: [
          0: {
            granted: true
            permission: "io.k8s.coordination.v1.leases.get"
            resource: "coordination.k8s.io/v1/namespaces/kube-system/leases/maintenance-controller"
          }
        ]
        requestMetadata: {2}
        status: {1}
        ...
      }
      ...
    }
    

You decide to create a label for your log-based metric that stores information from the `permission` field. You notice that these fields are formatted like `io.k8s.xyz`, where `xyz` is a string that provides more detail about the request. This string might have a value like `get`, or it might have more complex formatting like `io.k8s.coordination.v1.leases.get`.

To minimize the number of label values, you don't want to extract the detailed information. You only want to store values like `get` or `coordination` in the label. Also, you decide that you don't want to include the common prefix, `io.k8s.`, in the label value.

Next, you configure the label. Because the `permission` field is a repeated field, with the parent being the `authorizationInfo` field, you set the field name as follows:
    
    
    protoPayload.authorizationInfo.permission
    

Lastly, you create the following regular expression:
    
    
    io.k8s.([a-z]+).*
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
