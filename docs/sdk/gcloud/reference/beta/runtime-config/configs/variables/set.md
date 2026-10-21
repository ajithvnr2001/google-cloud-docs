---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/runtime-config/configs/variables/set/
title: gcloud beta runtime-config configs variables set \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:32:59.442507+00:00
---

# gcloud beta runtime-config configs variables set  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/runtime-config/configs/variables/set/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta runtime-config configs variables set Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta runtime-config configs variables set - create or update variable resources 
SYNOPSIS
    

`gcloud beta runtime-config configs variables set` `NAME` [`VALUE`] `--config-name`=`CONFIG_NAME` [`--is-text`] [`--fail-if-absent` | `--fail-if-present`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command creates or updates a variable resource, setting its value to the specified string or file contents. 
EXAMPLES
     To create or update a variable named "my-var", run: 
    
    
    gcloud beta runtime-config configs variables set --config-name=my-config my-var "my value"

To create or update a variable with a hierarchical name, such as "results/task1", run: 
    
    
    gcloud beta runtime-config configs variables set --config-name=my-config results/task1 "my value"

To create a variable, but fail if it already exists, run: 
    
    
    gcloud beta runtime-config configs variables set --config-name=my-config my-var "my-value" --fail-if-present

To update a variable, but fail if it does not exist, run: 
    
    
    gcloud beta runtime-config configs variables set --config-name=my-config my-var "my-value" --fail-if-absent

It is possible to provide --is-text flag if the value contains only text (UTF-8 encoded). This affects how the variable is transmitted on the wire and requires less quota on the backend. 
    
    
    gcloud beta runtime-config configs variables set --config-name=my-config --is-text my-var "my value"

If the variable's value parameter is not specified, the value will be read from standard input. This allows setting variables to large values or values that contain non-printable characters. The variable value will be automatically base64-encoded. For example, to set a variable's value to the contents of a file, run: 
    
    
    cat my-file | gcloud beta runtime-config configs variables set --config-name my-config my-var

POSITIONAL ARGUMENTS
    

`NAME`
     The variable name. 
[`VALUE`]
     The variable value. If absent, the value will be read from stdin. The value is automatically base64-encoded, unless --is-text flag is set. 
REQUIRED FLAGS
    

`--config-name`=`CONFIG_NAME`
     The name of the configuration resource to use. 
OPTIONAL FLAGS
    

`--is-text`
     If True, send and store the value as text. Can be used if the value contains only text (UTF-8 encoded). This affects how the variable is transmitted on the wire and requires less quota on the backend. 
At most one of these can be specified: 

`--fail-if-absent`
     Fail if a variable with the specified name does not exist. 
`--fail-if-present`
     Fail if a variable with the specified name already exists. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
