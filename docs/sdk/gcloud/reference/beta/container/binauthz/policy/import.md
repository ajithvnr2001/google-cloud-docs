---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/binauthz/policy/import/
title: gcloud beta container binauthz policy import \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:38:27.468194+00:00
---

# gcloud beta container binauthz policy import  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/binauthz/policy/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container binauthz policy import Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container binauthz policy import - import a Binary Authorization policy to the current project 
SYNOPSIS
    

`gcloud beta container binauthz policy import` `POLICY_FILE` [`--strict-validation`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command accepts a description of the desired policy in the form of a YAML-formatted file. A representation of the current policy can be retrieved using the $ [gcloud beta container binauthz policy export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/binauthz/policy/export) command. One method of modifying the policy is to run `$ [gcloud beta container binauthz policy export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/binauthz/policy/export)`, dump the contents to a file, modify the policy file to reflect the desired new policy, and provide this modified file to `$ gcloud beta container binauthz policy import`. 
EXAMPLES
     To update the current project's policy: 
    
    
    [gcloud beta container binauthz policy export](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/binauthz/policy/export) > my_policy.yaml
    
    
    edit my_policy.yaml
    
    
    gcloud beta container binauthz policy import my_policy.yaml

POSITIONAL ARGUMENTS
    

`POLICY_FILE`
     The file containing the YAML-formatted policy description. 
FLAGS
    

`--strict-validation`
     Whether to perform additional checks on the validity of policy contents. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container binauthz policy import](https://docs.cloud.google.com/sdk/gcloud/reference/container/binauthz/policy/import)
    
    
    [gcloud alpha container binauthz policy import](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/binauthz/policy/import)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
