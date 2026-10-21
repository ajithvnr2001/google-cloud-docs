---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/tags/values/create/
title: gcloud alpha resource-manager tags values create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:05.715992+00:00
---

# gcloud alpha resource-manager tags values create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/tags/values/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha resource-manager tags values create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha resource-manager tags values create - creates a TagValue resource 
SYNOPSIS
    

`gcloud alpha resource-manager tags values create` (`SHORT_NAME` `--parent`=`PARENT`) [`--async`] [`--description`=`DESCRIPTION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Creates a TagValue resource given the short_name and description (optional) as well as the parent, the of the TagValue. The parent of the TagValue can be a TagKey or TagValue. The parent can be specified by its numeric ID or its namespaced name. 
EXAMPLES
     To create a TagValue with the short name `test` and the description `descriptio` under a TagKey with a short name `env` under `organizations/123`, run: 
    
    
    gcloud alpha resource-manager tags values create test --parent=123/env --description=description

To create a TagValue with the short name `test` under TagKey with id `456`, run: 
    
    
    gcloud alpha resource-manager tags values create test --parent=tagKeys/456 --description=description

POSITIONAL ARGUMENTS
    

TagValue. 

This must be specified. 

`SHORT_NAME`
     User specified, friendly name of the TagKey or TagValue. The field must be 1-63 characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores ( _ ), dots (.), and alphanumerics between. 

This positional argument must be specified if any of the other arguments in this group are specified. 

`--parent`=`PARENT`
     Parent of the TagValue in either in the form of tagKeys/{id} or {org_id}/{tagkey_short_name} 

This flag argument must be specified if any of the other arguments in this group are specified. 

FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     User-assigned description of the TagKey or TagValue. Must not exceed 256 characters. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud resource-manager tags values create](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/create)
    
    
    [gcloud beta resource-manager tags values create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/tags/values/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
