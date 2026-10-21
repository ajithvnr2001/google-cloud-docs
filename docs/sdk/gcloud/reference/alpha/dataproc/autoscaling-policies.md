---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/autoscaling-policies/
title: gcloud alpha dataproc autoscaling-policies \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:12:25.957667+00:00
---

# gcloud alpha dataproc autoscaling-policies  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/autoscaling-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataproc autoscaling-policies Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataproc autoscaling-policies - create and manage Dataproc autoscaling policies 
SYNOPSIS
    

`gcloud alpha dataproc autoscaling-policies` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create and manage Dataproc autoscaling policies. 
EXAMPLES
     To see the list of all autoscaling policies, run: 
    
    
    [gcloud alpha dataproc autoscaling-policies list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/autoscaling-policies/list)

To view the details of an autoscaling policy, run: 
    
    
    [gcloud alpha dataproc autoscaling-policies describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/autoscaling-policies/describe) my_policy

To view just the non-output only fields of an autoscaling policy, run: 
    
    
    [gcloud alpha dataproc autoscaling-policies export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/autoscaling-policies/export) my_policy --destination policy-file.yaml

To create or update an autoscaling policy, run: 
    
    
    [gcloud alpha dataproc autoscaling-policies import](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/autoscaling-policies/import) my_policy --source policy-file.yaml

To delete an autoscaling policy, run: 
    
    
    [gcloud alpha dataproc autoscaling-policies delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/autoscaling-policies/delete) my_policy

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/autoscaling-policies/delete)`
     `(ALPHA)` Delete an autoscaling policy. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/autoscaling-policies/describe)`
     `(ALPHA)` Describe an autoscaling policy. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/autoscaling-policies/export)`
     `(ALPHA)` Export an autoscaling policy. 
`[get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/autoscaling-policies/get-iam-policy)`
     `(ALPHA)` Get IAM policy for an autoscaling policy. 
`[import](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/autoscaling-policies/import)`
     `(ALPHA)` Import an autoscaling policy. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/autoscaling-policies/list)`
     `(ALPHA)` List autoscaling policies. 
`[set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataproc/autoscaling-policies/set-iam-policy)`
     `(ALPHA)` Set IAM policy for an autoscaling policy. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud dataproc autoscaling-policies](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies)
    
    
    [gcloud beta dataproc autoscaling-policies](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataproc/autoscaling-policies)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
