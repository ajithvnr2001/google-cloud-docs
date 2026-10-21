---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging/tail/
title: gcloud alpha logging tail \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:13:11.983935+00:00
---

# gcloud alpha logging tail  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging/tail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha logging tail Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha logging tail - tail log entries 
SYNOPSIS
    

`gcloud alpha logging tail` [`LOG_FILTER`] [`--buffer-window`=`BUFFER_WINDOW`] [`--billing-account`=`BILLING_ACCOUNT_ID` | `--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`] [`--bucket`=`BUCKET` `--location`=`LOCATION` `--view`=`VIEW`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` gcloud alpha logging tail streams newly received log entries. Log entries matching `log-filter` are returned in the order that Cloud Logging received them. If the log entries come from multiple logs, then entries from different logs might be mixed in the results. To help return log entries in order, use `--buffer-window`. 

Before you can use gcloud alpha logging tail, you must complete the installation instructions at [Live tailing log entries](https://cloud.google.com/logging/docs/reference/tools/gcloud-logging#live-tailing). 

For the quotas and limits associated with gcloud alpha logging tail, see [Logging API quotas and limits](https://cloud.google.com/logging/quotas#api-limits). 

EXAMPLES
     To stream log entries from Google Compute Engine instances, run: 
    
    
    gcloud alpha logging tail "resource.type=gce_instance"

To stream log entries with severity ERROR or higher, run: 
    
    
    gcloud alpha logging tail "severity>=ERROR"

To stream log entries with severity ERROR but only output the timestamps and instance IDs, run: 
    
    
    gcloud alpha logging tail "severity>=ERROR" --format="default(timestamp,resource["labels"]["instance_id"])"

To stream with minimal latency but potentially incorrect ordering: 
    
    
    gcloud alpha logging tail "resource.type=gce_instance" --buffer-window=0s

To stream log entries in your project's syslog log from Compute Engine instances containing payloads that include the word `SyncAddress` and format the output in `JSON` format, run: 
    
    
    gcloud alpha logging tail "resource.type=gce_instance AND log_id(syslog) AND textPayload:SyncAddress" --format=json

To stream log entries from a folder, run: 
    
    
    gcloud alpha logging tail "resource.type=global" --folder=[FOLDER_ID]

Detailed information about filters can be found at: <https://cloud.google.com/logging/docs/view/logging-query-language>

POSITIONAL ARGUMENTS
    

[`LOG_FILTER`]
     Filter expression that specifies the log entries to return. A detailed guide on the Logging query language can be found at: <https://cloud.google.com/logging/docs/view/logging-query-language>. 
FLAGS
    

`--buffer-window`=`BUFFER_WINDOW`
     The duration of time for which entries should be buffered for ordering before being returned. A longer buffer window helps to return logs in chronological order, but it also increases the latency from when entries are received by Cloud Logging to when they are returned. If unset, Cloud Logging will use 2s by default. 
At most one of these can be specified: 

`--billing-account`=`BILLING_ACCOUNT_ID`
     Billing account of the log entries to tail. 
`--folder`=`FOLDER_ID`
     Folder of the log entries to tail. 
`--organization`=`ORGANIZATION_ID`
     Organization of the log entries to tail. 
`--project`=`PROJECT_ID`
     Project of the log entries to tail. 

The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

These arguments are used in conjunction with the parent to construct a view resource. 
`--bucket`=`BUCKET`
     Id of the bucket. If this argument is provided, then `--location` and `--view` must also be specified. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the bucket. If this argument is provided, then `--bucket` and `--view` must also be specified. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--view`=`VIEW`
     Id of the view. If this argument is provided, then `--location` and `--bucket` must also be specified. 

This flag argument must be specified if any of the other arguments in this group are specified. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta logging tail](https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging/tail)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
