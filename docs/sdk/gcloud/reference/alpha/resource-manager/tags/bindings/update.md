---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/tags/bindings/update/
title: gcloud alpha resource-manager tags bindings update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:57.966056+00:00
---

# gcloud alpha resource-manager tags bindings update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/tags/bindings/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha resource-manager tags bindings update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha resource-manager tags bindings update - updates TagBindings bound to the specified resource 
SYNOPSIS
    

`gcloud alpha resource-manager tags bindings update` `--resource-name`=`RESOURCE_NAME` (`--clear-tags` | `--replace-tags`=[`REPLACE_TAGS`,…] | `--remove-tags`=`REMOVE_TAGS`,[`REMOVE_TAGS`,…] `--update-tags`=[`UPDATE_TAGS`,…]) [`--async`] [`--location`=`LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Updates TagBindings bound to the specified resource. 
REQUIRED FLAGS
    

`--resource-name`=`RESOURCE_NAME`
     Full resource name of the resource to attach to the tagValue. 
Tags to update for a resource. 

Exactly one of these must be specified: 

`--clear-tags`
     Clear all tags on the resource. 
`--replace-tags`=[`REPLACE_TAGS`,…]
     Replace all existing tags on the resource with the specified key-value pairs. Sets `replace_tags` value. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --replace-tags=string=string

`JSON Example:`
    
    
    --replace-tags='{"string": "string"}'

`File Example:`
    
    
    --replace-tags=path_to_file.(yaml|json)

Or at least one of these can be specified: 

Tags to add/remove for a resource. 
`--remove-tags`=`REMOVE_TAGS`,[`REMOVE_TAGS`,…]
     Remove the specified tags from the resource. 
`--update-tags`=[`UPDATE_TAGS`,…]
     Add/update tags to the resource. Sets `update_tags` value. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --update-tags=string=string

`JSON Example:`
    
    
    --update-tags='{"string": "string"}'

`File Example:`
    
    
    --update-tags=path_to_file.(yaml|json)

OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--location`=`LOCATION`
     Region or zone of the resource to bind to the TagValue. This field is not required if the resource is a global resource like projects, folders and organizations. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
