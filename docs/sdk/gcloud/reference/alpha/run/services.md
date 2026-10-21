---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/
title: gcloud alpha run services \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:18:51.124397+00:00
---

# gcloud alpha run services  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha run services Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha run services - view and manage your Cloud Run services 
SYNOPSIS
    

`gcloud alpha run services` `GROUP` | `COMMAND` [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This set of commands can be used to view and manage your existing Cloud Run services. 

To create new deployments, use `[gcloud alpha run deploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/deploy)`. 

EXAMPLES
     To list your deployed services, run: 
    
    
    [gcloud alpha run services list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/list)

FLAGS
    

`--region`=`REGION`
     Region in which the resource can be found. Alternatively, set the property [run/region]. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[dev](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/dev)`
     `(ALPHA)` Commands for development on Cloud Run Services. 
`[logs](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/logs)`
     `(ALPHA)` Read logs for Cloud Run services. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/add-iam-policy-binding)`
     `(ALPHA)` Add IAM policy binding to a Cloud Run service. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/delete)`
     `(ALPHA)` Delete a service. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/describe)`
     `(ALPHA)` Obtain details about a given service. 
`[get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/get-iam-policy)`
     `(ALPHA)` Get the IAM policy for a Cloud Run service. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/list)`
     `(ALPHA)` List available services. 
`[proxy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/proxy)`
     `(ALPHA)` Proxy a service to localhost authenticating as the active account or with the specified token. 
`[remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/remove-iam-policy-binding)`
     `(ALPHA)` Remove IAM policy binding of a Cloud Run service. 
`[replace](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/replace)`
     `(ALPHA)` Create or replace a service from a YAML service specification. 
`[set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/set-iam-policy)`
     `(ALPHA)` Set the IAM policy for a service. 
`[ssh](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/ssh)`
     `(ALPHA)` SSH into a service instance. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/update)`
     `(ALPHA)` Update Cloud Run environment variables and other configuration settings. 
`[update-traffic](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/services/update-traffic)`
     `(ALPHA)` Adjust the traffic assignments for a Cloud Run service. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud run services](https://docs.cloud.google.com/sdk/gcloud/reference/run/services)
    
    
    [gcloud beta run services](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/services)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
