---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/manage/custom-modules/sha/simulate/
title: gcloud alpha scc manage custom-modules sha simulate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:18.259765+00:00
---

# gcloud alpha scc manage custom-modules sha simulate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/manage/custom-modules/sha/simulate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc manage custom-modules sha simulate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc manage custom-modules sha simulate - command to simulate a SHA custom module 
SYNOPSIS
    

`gcloud alpha scc manage custom-modules sha simulate` `--custom-config-from-file`=`CUSTOM_CONFIG` `--resource-from-file`=`TEST_DATA` (`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--parent`=`PARENT` | `--project`=`PROJECT_ID_OR_NUMBER`) [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To simulate a Security Health Analytics custom module with ID `123456` for organization `123`, run: 
    
    
    gcloud alpha scc manage custom-modules sha simulate 123456 --organization=123 --custom-config-from-file=custom_config.yaml --resource-from-file=test.yaml

To simulate a Security Health Analytics custom module with ID `123456` for folder `456`, run: 
    
    
    gcloud alpha scc manage custom-modules sha simulate 123456 --folder=456 --custom-config-from-file=custom_config.yaml --resource-from-file=test.yaml

To simulate a Security Health Analytics custom module with ID `123456` for project `789`, run: 
    
    
    gcloud alpha scc manage custom-modules sha simulate 123456 --project=789 --custom-config-from-file=custom_config.yaml --resource-from-file=test.yaml

You can also specify the parent more generally: 
    
    
    gcloud alpha scc manage custom-modules sha simulate 123456 --parent=organizations/123 --custom-config-from-file=custom_config.yaml --resource-from-file=test.yaml

Or just specify the fully qualified module name: 
    
    
    gcloud alpha scc manage custom-modules sha simulate organizations/123/locations/global/effectiveSecurityHealthAnalyticsCustomModules/123456 --custom-config-from-file=custom_config.yaml --resource-from-file=test.yaml

REQUIRED FLAGS
    

`--custom-config-from-file`=`CUSTOM_CONFIG`
     Path to a YAML custom configuration file. Use a full or relative path to a local file containing the value of custom_config. 
`--resource-from-file`=`TEST_DATA`
     Path to a YAML file that contains the resource data to validate the Security Health Analytics custom module against. Use a full or relative path to a local file containing the value of resource. 
Exactly one of these must be specified: 

`--folder`=`FOLDER_ID`
     Folder associated with the custom module. 
`--organization`=`ORGANIZATION_ID`
     Organization associated with the custom module. 
`--parent`=`PARENT`
     Parent associated with the custom module. Can be one of organizations/<id>, projects/<id or name>, folders/<id>
`--project`=`PROJECT_ID_OR_NUMBER`
     Project associated with the custom module. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud scc manage custom-modules sha simulate](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/simulate)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
