---
url: https://docs.cloud.google.com/sdk/gcloud/reference/logging/write/
title: gcloud logging write \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:20.286261+00:00
---

# gcloud logging write  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/logging/write/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud logging write Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud logging write - write a log entry 
SYNOPSIS
    

`gcloud logging write` `LOG_NAME` `MESSAGE` [`--monitored-resource-labels`=[`KEY`=`VALUE`, …,…]] [`--monitored-resource-type`=`MONITORED_RESOURCE_TYPE`; default="global"] [`--payload-type`=`PAYLOAD_TYPE`; default="text"] [`--severity`=`SEVERITY`; default="DEFAULT"] [`--billing-account`=`BILLING_ACCOUNT_ID` | `--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Write a log entry. If the destination log does not exist, it will be created. By default, all log entries written with this command are written with the "global" resource type. 

gcloud logging write should be used for simple testing purposes. Check Cloud Logging agent for a proper way to send log entries: <https://cloud.google.com/logging/docs/agent/>

EXAMPLES
     To create a log entry in a given log, run: 
    
    
    gcloud logging write LOG_NAME "A simple entry"

To create a high severity log entry, run: 
    
    
    gcloud logging write LOG_NAME "Urgent message" --severity=ALERT

To create a structured log, run: 
    
    
    gcloud logging write LOG_NAME '{"key": "value"}' --payload-type=json

To create a log entry with a custom resource type, run: 
    
    
    gcloud logging write LOG_NAME "A simple entry" --monitored-resource-type=gce_instance --monitored-resource-labels=zone=us-centra1-a,instance_id=1234

POSITIONAL ARGUMENTS
    

`LOG_NAME`
     Name of the log where the log entry will be written. 
`MESSAGE`
     Message to put in the log entry. It can be JSON if you include `--payload-type=json`. 
FLAGS
    

`--monitored-resource-labels`=[`KEY`=`VALUE`, …,…]
     Monitored Resource labels to add to the payload 
`--monitored-resource-type`=`MONITORED_RESOURCE_TYPE`; default="global"
     Monitored Resource type to add to the payload 
`--payload-type`=`PAYLOAD_TYPE`; default="text"
     Type of the log entry payload. `PAYLOAD_TYPE` must be one of: `text`, `json`. 
`--severity`=`SEVERITY`; default="DEFAULT"
     Severity level of the log entry. `SEVERITY` must be one of: `DEFAULT`, `DEBUG`, `INFO`, `NOTICE`, `WARNING`, `ERROR`, `CRITICAL`, `ALERT`, `EMERGENCY`. 
At most one of these can be specified: 

`--billing-account`=`BILLING_ACCOUNT_ID`
     Billing account of the log entries to write. 
`--folder`=`FOLDER_ID`
     Folder of the log entries to write. 
`--organization`=`ORGANIZATION_ID`
     Organization of the log entries to write. 
`--project`=`PROJECT_ID`
     Project of the log entries to write. 

The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha logging write](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging/write)
    
    
    [gcloud beta logging write](https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging/write)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
