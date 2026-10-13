---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/custom-modules/sha/simulate/
title: gcloud alpha scc custom-modules sha simulate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:13.959206+00:00
---

# gcloud alpha scc custom-modules sha simulate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/custom-modules/sha/simulate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc custom-modules sha simulate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc custom-modules sha simulate - validates a Security Health Analytics custom module 
SYNOPSIS
    

`gcloud alpha scc custom-modules sha simulate` `--custom-config-from-file`=`PATH_TO_FILE` `--resource-from-file`=`PATH_TO_FILE` (`--folder`=`FOLDER` | `--organization`=`ORGANIZATION` | `--project`=`PROJECT`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Validates a given Security Health Analytics custom module and resource. 
EXAMPLES
     To validate a Security Health Analytics custom module against a custom resource for organization `123`, run: 
    
    
    gcloud alpha scc custom-modules sha simulate --organization=organizations/123 --custom-config-from-file=/tmp/custom_config.yaml --resource-from-file=/tmp/resource.yaml

To validate a Security Health Analytics custom module against a custom resource for folder `456`, run: 
    
    
    gcloud alpha scc custom-modules sha simulate --folder=folders/456 --custom-config-from-file=/tmp/custom_config.yaml --resource-from-file=/tmp/resource.yaml

To validate a Security Health Analytics custom module against a custom resource for project `789`, run: 
    
    
    gcloud alpha scc custom-modules sha simulate --project=projects/789 --custom-config-from-file=/tmp/custom_config.yaml --resource-from-file=/tmp/resource.yaml

REQUIRED FLAGS
    

`--custom-config-from-file`=`PATH_TO_FILE`
     Path to a YAML file that contains the configuration for the Security Health Analytics custom module. Use a full or relative path to a local file containing the value of custom_config. 
`--resource-from-file`=`PATH_TO_FILE`
     Path to a YAML file that contains the resource data to validate the Security Health Analytics custom module against. Use a full or relative path to a local file containing the value of resource. 
Exactly one of these must be specified: 

`--folder`=`FOLDER`
     Folder that will own the Security Health Analytics custom module. Formatted as `folders/456` or just `456`. 
`--organization`=`ORGANIZATION`
     Organization that will own the Security Health Analytics custom module. Formatted as `organizations/123` or just `123`. 
`--project`=`PROJECT`
     ID or number of the project that will own the Security Health Analytics custom module. Formatted as `projects/789` or just `789`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `securitycenter/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud scc custom-modules sha simulate](https://docs.cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/simulate)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
