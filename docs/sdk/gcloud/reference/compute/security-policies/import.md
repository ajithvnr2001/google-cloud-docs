---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/import/
title: gcloud compute security-policies import \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:03:24.625467+00:00
---

# gcloud compute security-policies import  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute security-policies import Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute security-policies import - import security policy configs into your project 
SYNOPSIS
    

`gcloud compute security-policies import` `NAME` `--file-name`=`FILE_NAME` [`--file-format`=`FILE_FORMAT`] [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute security-policies import` imports a security policy to update an existing policy. To create a new policy from a file please use the create command instead. 
EXAMPLES
     To import a security policy from a YAML file run this: 
    
    
    gcloud compute security-policies import --file-name=myFile

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the security policy to import. 
REQUIRED FLAGS
    

`--file-name`=`FILE_NAME`
     The name of the JSON or YAML file to import the security policy config from. 
OPTIONAL FLAGS
    

`--file-format`=`FILE_FORMAT`
     The format of the file to import the security policy config from. Specify either yaml or json. Defaults to yaml if not specified. `FILE_FORMAT` must be one of: `json`, `yaml`. 
At most one of these can be specified: 

`--global`
     If set, the security policy is global. 
`--region`=`REGION`
     Region of the security policy to import. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute security-policies import](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/security-policies/import)
    
    
    [gcloud beta compute security-policies import](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/security-policies/import)
    
    
    [gcloud preview compute security-policies import](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/security-policies/import)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
