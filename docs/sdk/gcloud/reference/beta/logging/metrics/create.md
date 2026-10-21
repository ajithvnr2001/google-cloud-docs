---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging/metrics/create/
title: gcloud beta logging metrics create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:55:26.980022+00:00
---

# gcloud beta logging metrics create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging/metrics/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta logging metrics create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta logging metrics create - create a logs-based metric 
SYNOPSIS
    

`gcloud beta logging metrics create` `METRIC_NAME` (`--config-from-file`=`PATH_TO_FILE` | [`--description`=`DESCRIPTION` `--log-filter`=`LOG_FILTER` : `--bucket-name`=`BUCKET_NAME`]) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a logs-based metric to count the number of log entries that match a filter expression. Logs-based metrics can also be used to extract values from logs and create a distribution of the values. 

For more information, see the logs-based metrics overview at: <https://cloud.google.com/logging/docs/logs-based-metrics>. 

EXAMPLES
     To create a metric that counts the number of log entries with a severity level higher than WARNING, run: 
    
    
    gcloud beta logging metrics create high_severity_count --description="Number of high severity log entries" --log-filter="severity > WARNING"

Detailed information about filters can be found at: <https://cloud.google.com/logging/docs/view/logging-query-language>

To create a metric that uses advanced features like distribution or user-defined labels, run: 
    
    
    gcloud beta logging metrics create my_metric --config-from-file=$PATH_TO_FILE

The config file can be in YAML or JSON format. Detailed information about how to configure metrics can be found at: <https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric>. 

For an example of the file structure for a distribution metric, see: <https://cloud.google.com/logging/docs/logs-based-metrics/distribution-metrics#example>. 

To create a bucket log-based metric, run: 
    
    
    gcloud beta logging metrics create my_bucket_metric --description="DESCRIPTION" --log-filter="LOG_FILTER" --bucket-name="BUCKET_NAME"

POSITIONAL ARGUMENTS
    

`METRIC_NAME`
     The name of the new metric. 
REQUIRED FLAGS
    

Data about the new metric. 

Exactly one of these must be specified: 

`--config-from-file`=`PATH_TO_FILE`
     A path to a YAML or JSON file specifying the logs-based metric to create. For an example of the file structure, see <https://cloud.google.com/logging/docs/logs-based-metrics/distribution-metrics#example>. Use a full or relative path to a local file containing the value of config. 
Or at least one of these can be specified: 

A group of arguments to specify simple counter logs-based metrics. 
`--description`=`DESCRIPTION`
     The metric's description. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--log-filter`=`LOG_FILTER`
     The metric's filter expression. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--bucket-name`=`BUCKET_NAME`
     The Log Bucket name which owns the log-based metric. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud logging metrics create](https://docs.cloud.google.com/sdk/gcloud/reference/logging/metrics/create)
    
    
    [gcloud alpha logging metrics create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging/metrics/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
