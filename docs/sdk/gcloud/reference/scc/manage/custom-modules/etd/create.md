---
url: https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create/
title: gcloud scc manage custom-modules etd create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:02.049213+00:00
---

# gcloud scc manage custom-modules etd create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/etd/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud scc manage custom-modules etd create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud scc manage custom-modules etd create - create an Event Threat Detection custom module 
SYNOPSIS
    

`gcloud scc manage custom-modules etd create` `--custom-config-file`=`CUSTOM_CONFIG` `--display-name`=`DISPLAY-NAME` `--enablement-state`=`ENABLEMENT_STATE` `--module-type`=`MODULE_TYPE` (`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--parent`=`PARENT` | `--project`=`PROJECT_ID_OR_NUMBER`) [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create an Event Threat Detection custom module for organization `123`, run: 
    
    
    gcloud scc manage custom-modules etd create --organization=organizations/123 --display-name="test_display_name" --module-type="CONFIGURABLE_BAD_IP" --enablement-state="ENABLED" --custom-config-file=config.json

REQUIRED FLAGS
    

`--custom-config-file`=`CUSTOM_CONFIG`
     Path to a JSON custom configuration file of the ETD custom module. Use a full or relative path to a local file containing the value of custom_config_file. 
`--display-name`=`DISPLAY-NAME`
     The display name of the custom module. 
`--enablement-state`=`ENABLEMENT_STATE`
     Sets the enablement state of the Event Threat Detection custom module. Valid options are ENABLED, DISABLED, OR INHERITED. 
`--module-type`=`MODULE_TYPE`
     Type of the custom module. For a list of valid module types please visit <https://cloud.google.com/security-command-center/docs/custom-modules-etd-overview#custom_modules_and_templates>. 
Exactly one of these must be specified: 

`--folder`=`FOLDER_ID`
     Folder associated with the custom module. 
`--organization`=`ORGANIZATION_ID`
     Organization associated with the custom module. 
`--parent`=`PARENT`
     Parent associated with the custom module. Can be one of organizations/<id>, projects/<id or name>, folders/<id>
`--project`=`PROJECT_ID_OR_NUMBER`
     Project associated with the custom module. 
OPTIONAL FLAGS
    

`--validate-only`
     If present, the request is validated (including IAM checks) but no action is taken. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha scc manage custom-modules etd create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/manage/custom-modules/etd/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
