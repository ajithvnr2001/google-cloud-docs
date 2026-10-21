---
url: https://docs.cloud.google.com/sdk/gcloud/reference/logging/saved-queries/create/
title: gcloud logging saved-queries create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:14:30.452478+00:00
---

# gcloud logging saved-queries create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/logging/saved-queries/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud logging saved-queries create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud logging saved-queries create - create a Logging saved query 
SYNOPSIS
    

`gcloud logging saved-queries create` `--display-name`=`DISPLAY_NAME` `--location`=`LOCATION` `--visibility`=`VISIBILITY` (`--sql-query-text`=`SQL_QUERY_TEXT` | `--log-filter`=`LOG_FILTER` `--summary-fields`=`SUMMARY_FIELDS` `--summary-field-end`=`SUMMARY_FIELD_END` | `--summary-field-start`=`SUMMARY_FIELD_START`) [`--description`=`DESCRIPTION`] [`--id`=`ID`] [`--billing-account`=`BILLING_ACCOUNT_ID` | `--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a saved query. 
EXAMPLES
     To create a saved query in a project, run: 
    
    
    gcloud logging saved-queries create --id=my-saved-query --location=global --display-name="My saved query" --visibility=private --sql-query-text="SELECT * FROM my_table"

REQUIRED FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Display name for the saved query. 
`--location`=`LOCATION`
     Location to create the saved query in. 
`--visibility`=`VISIBILITY`
     Visibility of the saved query. `VISIBILITY` must be one of: `private`, `shared`. 
Exactly one of these must be specified: 

`--sql-query-text`=`SQL_QUERY_TEXT`
     SQL query text. 
Or at least one of these can be specified: 

`--log-filter`=`LOG_FILTER`
     Filter expression for the log-based query. 
`--summary-fields`=`SUMMARY_FIELDS`
     Comma-separated list of fields to include in the summary. This flag must be specified if --summary-field-start or --summary-field-end are provided. 
At most one of these can be specified: 

`--summary-field-end`=`SUMMARY_FIELD_END`
     Setting for number of characters to display for each summary field: characters will be counted from the end of the string. Requires the --summary-fields flag to be specified as well. 
`--summary-field-start`=`SUMMARY_FIELD_START`
     Setting for number of characters to display for each summary field: characters will be counted from the start of the string. Requires the --summary-fields flag to be specified as well. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     A textual description for the saved query. 
`--id`=`ID`
     ID of the saved query to create. 
At most one of these can be specified: 

`--billing-account`=`BILLING_ACCOUNT_ID`
     Billing account of the saved query to create. 
`--folder`=`FOLDER_ID`
     Folder of the saved query to create. 
`--organization`=`ORGANIZATION_ID`
     Organization of the saved query to create. 
`--project`=`PROJECT_ID`
     Project of the saved query to create. 

The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
