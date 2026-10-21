---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging/metrics/update/
title: gcloud beta logging metrics update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:55:28.229085+00:00
---

# gcloud beta logging metrics update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging/metrics/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta logging metrics update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta logging metrics update - update the definition of a logs-based metric 
SYNOPSIS
    

`gcloud beta logging metrics update` `METRIC_NAME` (`--config-from-file`=`PATH_TO_FILE` | `--bucket-name`=`BUCKET_NAME` `--description`=`DESCRIPTION` `--log-filter`=`LOG_FILTER`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update the description or the filter expression of an existing logs-based metric. 

For more information, see the logs-based metrics overview at: <https://cloud.google.com/logging/docs/logs-based-metrics>. 

EXAMPLES
     To update the description of a metric called high_severity_count, run: 
    
    
    gcloud beta logging metrics update high_severity_count --description="Count of high-severity log entries."

To update the filter expression of the metric, run: 
    
    
    gcloud beta logging metrics update high_severity_count --log-filter="severity >= WARNING"

Detailed information about filters can be found at: <https://cloud.google.com/logging/docs/view/logging-query-language>

For advanced features such as user-defined labels and distribution metrics, update using a config file: 
    
    
    gcloud beta logging metrics update high_severity_count --config-from-file=$PATH_TO_FILE

The config file should be in YAML format. Detailed information about how to configure metrics can be found at: <https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric>. 

For an example of the file structure for a distribution metric, see: <https://cloud.google.com/logging/docs/logs-based-metrics/distribution-metrics#example>. 

Any top-level fields in the LogMetric definition that aren't specified in the config file will not be updated in the metric. 

To update the bucket associated with a bucket log-based metric, run: 
    
    
    gcloud beta logging metrics update my-bucket-metric --bucket-name="NEW_BUCKET_NAME"

POSITIONAL ARGUMENTS
    

`METRIC_NAME`
     The name of the log-based metric to update. 
REQUIRED FLAGS
    

Data about the metric to update. 

Exactly one of these must be specified: 

`--config-from-file`=`PATH_TO_FILE`
     A path to a YAML file specifying the updates to be made to the logs-based metric. For an example of the file structure, see <https://cloud.google.com/logging/docs/logs-based-metrics/distribution-metrics#example>. Use a full or relative path to a local file containing the value of config. 
Or at least one of these can be specified: 

Arguments to specify information about simple counter logs-based metrics. 
`--bucket-name`=`BUCKET_NAME`
     The Log Bucket name which owns the log-based metric. 
`--description`=`DESCRIPTION`
     A new description for the metric. If omitted, the description is not changed. 
`--log-filter`=`LOG_FILTER`
     A new filter string for the metric. If omitted, the filter is not changed. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud logging metrics update](https://docs.cloud.google.com/sdk/gcloud/reference/logging/metrics/update)
    
    
    [gcloud alpha logging metrics update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging/metrics/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
