---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging/operations/list/
title: gcloud beta logging operations list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:55:27.873919+00:00
---

# gcloud beta logging operations list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging/operations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta logging operations list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta logging operations list - list long running operations 
SYNOPSIS
    

`gcloud beta logging operations list` `--location`=`LOCATION` `--operation-filter`=`OPERATION_FILTER` [`--page-token`=`PAGE_TOKEN`] [`--billing-account`=`BILLING_ACCOUNT_ID` | `--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Return a list of long running operations in the given LOCATION. The operations were scheduled by other gcloud commands. 

For example, a CopyLogEntries operation may be scheduled by the command: `gcloud logging copy BUCKET_ID DESTINATION --location=LOCATION`. 

The `--operation-filter` flag is required and must specify the `request_type`. Supported request types include but are not limited to: `CopyLogEntries`, `CreateBucket` and `UpdateBucket`. 

Additional supported filter expressions include: `operation_start_time`, `operation_finish_time` and `operation_state`. These can be combined with the case-sensitive keyword `AND` between them. 

For `operation_start_time` and `operation_end_time`, the operators >=, >, <=, and < are supported. 

Timestamps must be in either RFC3339 or ISO8601 formats. If the timestamp contains a time value, then it must be quoted. For examples: "YYYY-MM-DDTHH:MM:SSZ", "YYYY-MM-DDTHH:MM:SS.mmmZ", "YY-MM-DD", "YYYY-MM-DDTHH:MM:SS-0000", "YYYY-MM-DDTHH:MM+0000", "YYYY-MM-DD", YYYY-MM-DD, YY-MM-DD, etc. 

The `operation_state` filter expression can be used to filter for operations that are in a specific state. The value can be one of the following: `SCHEDULED`, `WAITING_FOR_PRECONDITIONS`, `RUNNING`, `SUCCESS`, `FAILURE`, `CANCELLED`, `PENDING`. 

For `operation_state`, the operators = and != are supported. 

Other filter options are not supported. 

EXAMPLES
     To list CopyLogEntries operations, run: 
    
    
    gcloud beta logging operations list --location=LOCATION --operation-filter='request_type=CopyLogEntries'

To list CopyLogEntries operations that started after a specified time, run: 
    
    
    gcloud beta logging operations list --location=LOCATION --operation-filter='request_type=CopyLogEntries AND
    operation_start_time>="2023-11-20T00:00:00Z"'

To list CopyLogEntries operations that finished before a specified time, run: 
    
    
    gcloud beta logging operations list --location=LOCATION --operation-filter='request_type=CopyLogEntries AND
    operation_finish_time<="2023-11-20T00:00:00Z"'

To list CopyLogEntries operations that completed successfully, run: 
    
    
    gcloud beta logging operations list --location=LOCATION --operation-filter='request_type=CopyLogEntries AND
    operation_state=SUCCESS'

To list CopyLogEntries operations that have not failed, run: 
    
    
    gcloud beta logging operations list --location=LOCATION --operation-filter='request_type=CopyLogEntries AND
    operation_state!=FAILURE'

REQUIRED FLAGS
    

`--location`=`LOCATION`
     Location of the operations. 
`--operation-filter`=`OPERATION_FILTER`
     Filter expression that specifies the operations to return. 
FLAGS
    

`--page-token`=`PAGE_TOKEN`
     The next_page_token value returned from a previous List request, if any. 
At most one of these can be specified: 

`--billing-account`=`BILLING_ACCOUNT_ID`
     Billing account of the operations to list. 
`--folder`=`FOLDER_ID`
     Folder of the operations to list. 
`--organization`=`ORGANIZATION_ID`
     Organization of the operations to list. 
`--project`=`PROJECT_ID`
     Project of the operations to list. 

The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

LIST COMMAND FLAGS
    

`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud logging operations list](https://docs.cloud.google.com/sdk/gcloud/reference/logging/operations/list)
    
    
    [gcloud alpha logging operations list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging/operations/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
