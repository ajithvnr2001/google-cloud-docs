---
url: https://docs.cloud.google.com/sdk/gcloud/reference/logging/read/
title: gcloud logging read \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:02.682923+00:00
---

# gcloud logging read  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/logging/read/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud logging read Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud logging read - read log entries 
SYNOPSIS
    

`gcloud logging read` [`LOG_FILTER`] [`--freshness`=`FRESHNESS`; default="1d"] [`--order`=`ORDER`; default="desc"] [`--billing-account`=`BILLING_ACCOUNT_ID` | `--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`] [`--resource-names`=[`RESOURCE`,…] | `--bucket`=`BUCKET` `--location`=`LOCATION` `--view`=`VIEW`] [`--limit`=`LIMIT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     gcloud logging read reads log entries. Log entries matching `log-filter` are returned in order of decreasing timestamps, most-recent entries first. If the log entries come from multiple logs, then entries from different logs might be intermingled in the results. 
EXAMPLES
     To read log entries from Google Compute Engine instances, run: 
    
    
    gcloud logging read "resource.type=gce_instance"

To read log entries with severity ERROR or higher, run: 
    
    
    gcloud logging read "severity>=ERROR"

To read log entries written in a specific time window, run: 
    
    
    gcloud logging read 'timestamp<="2015-05-31T23:59:59Z" AND
     timestamp>="2015-05-31T00:00:00Z"'

To read up to 10 log entries in your project's syslog log from Compute Engine instances containing payloads that include the word `SyncAddress` and format the output in `JSON` format, run: 
    
    
    gcloud logging read "resource.type=gce_instance AND logName=projects/[PROJECT_ID]/logs/syslog AND textPayload:SyncAddress" --limit=10 --format=json

To read a log entry from a folder, run: 
    
    
    gcloud logging read "resource.type=global" --folder=[FOLDER_ID] --limit=1

To read a log entry from a global log bucket, run: 
    
    
    gcloud logging read --bucket=<bucket-id> --location=[LOCATION] --limit=1

To read a log entry from the global `_Required` log bucket using the bucket's `_Default` log view: 
    
    
    gcloud logging read "" --bucket=_Required --location=global --view=_Default --limit=1

To read a log entry from a log bucket using the bucket's `_AllLogs` log view: 
    
    
    gcloud logging read "" --bucket=[BUCKET_ID] --location=[LOCATION] --view=_AllLogs --limit=1

To read a log entry from a log bucket using a custom log view that you have created for the bucket: 
    
    
    gcloud logging read "" --bucket=[BUCKET_ID] --location=[LOCATION] --view=[VIEW_ID] --limit=1

To read log entries from multiple resources, specify them as a comma-delimeted sequence with --resource-names. Each resource name can be specified either as a top-level resource (e.g., projects/[PROJECT_ID], folders/[FOLDER_ID], etc.) or as a Log View resource (e.g., projects/[PROJECT_ID]/locations/[LOCATION]/buckets/[BUCKET_NAME]/views/[VIEW_ID]). 
    
    
    gcloud logging read "" --resource-names=[RESOURCE-1],[RESOURCE-2]

POSITIONAL ARGUMENTS
    

[`LOG_FILTER`]
     Filter expression that specifies the log entries to return. Detailed information about filters can be found at: <https://cloud.google.com/logging/docs/view/logging-query-language>
FLAGS
    

`--freshness`=`FRESHNESS`; default="1d"
     Return entries that are not older than this value. Works only with DESC ordering and filters without a timestamp. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
`--order`=`ORDER`; default="desc"
     Ordering of returned log entries based on timestamp field. `ORDER` must be one of: `desc`, `asc`. 
At most one of these can be specified: 

`--billing-account`=`BILLING_ACCOUNT_ID`
     Billing account of the log entries to read. 
`--folder`=`FOLDER_ID`
     Folder of the log entries to read. 
`--organization`=`ORGANIZATION_ID`
     Organization of the log entries to read. 
`--project`=`PROJECT_ID`
     Project of the log entries to read. 

The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

At most one of these can be specified: 

`--resource-names`=[`RESOURCE`,…]
     Resource name(s) to read logs from. A resource can either be an top-level resource (e.g., "projects/my-project") or a full log view resource path (e.g., "projects/my-project/locations/my-location/buckets/my-bucket/views/my-view"). Multiple resources can be specified, separated by a comma. 
Or at least one of these can be specified: 

These arguments are used in conjunction with the parent to construct a view resource. 
`--bucket`=`BUCKET`
     Id of the log bucket. If this argument is provided then `--location` and `--view` must also be specified. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the log bucket. If this argument is provided then `--bucket` and `--view` must also be specified. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--view`=`VIEW`
     Id of the view. If this argument is provided then `--location` and `--bucket` must also be specified. 

This flag argument must be specified if any of the other arguments in this group are specified. 

LIST COMMAND FLAGS
    

`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha logging read](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging/read)
    
    
    [gcloud beta logging read](https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging/read)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
