---
url: https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/update/
title: gcloud logging sinks update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:00:00.339615+00:00
---

# gcloud logging sinks update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud logging sinks update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud logging sinks update - update a sink 
SYNOPSIS
    

`gcloud logging sinks update` `SINK_NAME` [`DESTINATION`] [`--add-exclusion`=[`description`=`DESCRIPTION`],[`disabled`=`DISABLED`],[`filter`=`FILTER`],[`name`=`NAME`]] [`--clear-exclusions`] [`--custom-writer-identity`=`SERVICE_ACCOUNT_EMAIL`] [`--description`=`DESCRIPTION`] [`--disabled`] [`--include-children`] [`--intercept-children`] [`--log-filter`=`LOG_FILTER`] [`--remove-exclusions`=[`EXCLUSION` `ID`,…]] [`--update-exclusion`=[`description`=`DESCRIPTION`],[`disabled`=`DISABLED`],[`filter`=`FILTER`],[`name`=`NAME`]] [`--use-partitioned-tables`] [`--billing-account`=`BILLING_ACCOUNT_ID` | `--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Change the `[DESTINATION]` or `--log-filter` associated with a sink. The new destination must already exist and Cloud Logging must have permission to write to it. 

Log entries are exported to the new destination immediately. 

EXAMPLES
     To only update a sink filter, run: 
    
    
    gcloud logging sinks update my-sink --log-filter='severity>=ERROR'

Detailed information about filters can be found at: <https://cloud.google.com/logging/docs/view/logging-query-language>

POSITIONAL ARGUMENTS
    

`SINK_NAME`
     The name of the sink to update. 
[`DESTINATION`]
     A new destination for the sink. If omitted, the sink's existing destination is unchanged. 
FLAGS
    

`--add-exclusion`=[`description`=`DESCRIPTION`],[`disabled`=`DISABLED`],[`filter`=`FILTER`],[`name`=`NAME`]
     Add an exclusion filter for log entries that are not to be routed to the sink' destination. This flag can be repeated. 

The ``name`` and ``filter`` attributes are required. The following keys are accepted: 

`name`
     Required. An identifier, such as ``load-balancer-exclusion``. Identifiers are limited to 100 characters and can include only letters, digits, underscores, hyphens, and periods. 
`description`
     Optional. A description of this exclusion. 
`filter`
     Required. Entries that match this advanced log filter will be excluded. Filter cannot be empty. 
`disabled`
     Optional. By default, an exclusion is not disabled. To disable an exclusion, include this key and specify any value. 
`--clear-exclusions`
     Remove all logging exclusions from the sink. 
`--custom-writer-identity`=`SERVICE_ACCOUNT_EMAIL`
     Writer identity for the sink. This flag can only be used if the destination is a log bucket in a different project. The writer identity is automatically generated when it is not provided for a sink. 
`--description`=`DESCRIPTION`
     Description of the sink. 
`--disabled`
     Disable the sink. Disabled sinks do not route logs to the sink destination. Specify --no-disabled to enable a disabled sink. If this flag is not specified, the value will not be updated. 
`--include-children`
     Whether to export logs from all child projects and folders. Only applies to sinks for organizations and folders. 
`--intercept-children`
     Whether to intercept logs from all child projects and folders. Only applies to sinks for organizations and folders. 
`--log-filter`=`LOG_FILTER`
     A new filter expression for the sink. If omitted, the sink's existing filter (if any) is unchanged. 
`--remove-exclusions`=[`EXCLUSION` `ID`,…]
     Specify the name of the Logging exclusion(s) to delete. 
`--update-exclusion`=[`description`=`DESCRIPTION`],[`disabled`=`DISABLED`],[`filter`=`FILTER`],[`name`=`NAME`]
     Update an exclusion filter for a log entry that is not to be exported. This flag can be repeated. 

The ``name`` attribute is required. The following keys are accepted: 

`name`
     Required. An identifier, such as ``load-balancer-exclusion``. Identifiers are limited to 100 characters and can include only letters, digits, underscores, hyphens, and periods. 
`description`
     Optional. A description of this exclusion. 
`filter`
     Optional. Entries that match this advanced log filter will be excluded. Filter cannot be empty. 
`disabled`
     Optional. To disable an exclusion, include this key and specify any value. To enable a disabled exclusion, include this key, but do not specify any value. Do not include this key unless you want to change its value. 
Settings for sink exporting data to BigQuery. 
`--use-partitioned-tables`
     If specified, use BigQuery's partitioned tables. By default, Logging creates dated tables based on the log entries' timestamps, e.g. 'syslog_20170523'. Partitioned tables remove the suffix and special query syntax (https://cloud.google.com/bigquery/docs/querying-partitioned-tables) must be used. 
At most one of these can be specified: 

`--billing-account`=`BILLING_ACCOUNT_ID`
     Billing account of the sink to update. 
`--folder`=`FOLDER_ID`
     Folder of the sink to update. 
`--organization`=`ORGANIZATION_ID`
     Organization of the sink to update. 
`--project`=`PROJECT_ID`
     Project of the sink to update. 

The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha logging sinks update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging/sinks/update)
    
    
    [gcloud beta logging sinks update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging/sinks/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
