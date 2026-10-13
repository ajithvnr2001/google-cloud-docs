---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/custom-modules/etd/create/
title: gcloud alpha scc custom-modules etd create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:12.196657+00:00
---

# gcloud alpha scc custom-modules etd create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/custom-modules/etd/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc custom-modules etd create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc custom-modules etd create - create an Event Threat Detection custom module 
SYNOPSIS
    

`gcloud alpha scc custom-modules etd create` `--custom-config-from-file`=`PATH_TO_FILE` `--display-name`=`DISPLAY_NAME` `--enablement-state`=`ENABLEMENT_STATE` `--module-type`=`MODULE_TYPE` [`--folder`=`FOLDER` | `--organization`=`ORGANIZATION` | `--project`=`PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create an Event Threat Detection custom module. 
EXAMPLES
     To create an Event Threat Detection custom module for organization `123`, run: 
    
    
    gcloud alpha scc custom-modules etd create --organization=organizations/123 --display-name="test_display_name" --module-type="CONFIGURABLE_BAD_IP" --enablement-state="ENABLED" --custom-config-from-file=config.json

To create an Event Threat Detection custom module for folder `456`, run: 
    
    
    gcloud alpha scc custom-modules etd create --folder=folders/456 --display-name="test_display_name" --module-type="CONFIGURABLE_BAD_IP" --enablement-state="ENABLED" --custom-config-from-file=config.json

To create an Event Threat Detection custom module for project `789`, run: 
    
    
    gcloud alpha scc custom-modules etd create --project=projects/789 --display-name="test_display_name" --module-type="CONFIGURABLE_BAD_IP" --enablement-state="ENABLED" --custom-config-from-file=config.json

REQUIRED FLAGS
    

`--custom-config-from-file`=`PATH_TO_FILE`
     Path to a JSON file that contains the configuration for the Event Threat Detection custom module. Use a full or relative path to a local file containing the value of custom_config. 
`--display-name`=`DISPLAY_NAME`
     Sets the display name of the Event Threat Detection custom module. This display name becomes the finding category for all findings that are returned by this custom module. The display name must be between 1 and 128 characters, start with a lowercase letter, and contain alphanumeric characters or underscores only. 
`--enablement-state`=`ENABLEMENT_STATE`
     Sets the enablement state of the Event Threat Detection custom module. From the following list of possible enablement states, specify either enabled or disabled only. `ENABLEMENT_STATE` must be one of: `disabled`, `enabled`, `enablement-state-unspecified`, `inherited`. 
`--module-type`=`MODULE_TYPE`
     Sets the module type of the Event Threat Detection custom module. 
OPTIONAL FLAGS
    

At most one of these can be specified: 

`--folder`=`FOLDER`
     Folder where the Event Threat Detection custom module resides. Formatted as `folders/456` or just `456`. 
`--organization`=`ORGANIZATION`
     Organization where the Event Threat Detection custom module resides. Formatted as `organizations/123` or just `123`. 
`--project`=`PROJECT`
     ID or number of the project where the Event Threat Detection custom module resides. Formatted as `projects/789` or just `789`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `securitycenter/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
