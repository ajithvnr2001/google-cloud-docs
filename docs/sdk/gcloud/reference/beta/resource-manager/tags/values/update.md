---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/tags/values/update/
title: gcloud beta resource-manager tags values update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:06.380293+00:00
---

# gcloud beta resource-manager tags values update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/tags/values/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta resource-manager tags values update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta resource-manager tags values update - updates the specified TagValue resource's description 
SYNOPSIS
    

`gcloud beta resource-manager tags values update` `RESOURCE_NAME` [`--async`] [`--description`=`DESCRIPTION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Updates the TagValue's description given the TagValue's namespaced name <parent_namespace>/<tagkey_short_name>/<short_name> or the TagValue's numeric id tagValues/<id>
EXAMPLES
     To update a TagValue with id ``123``, run: 
    
    
    gcloud beta resource-manager tags values update tagValues/123 --description="foobar"

To update a TagValue named ``dev`` with the tagKey ``env`` under organization ``456``, run: 
    
    
    gcloud beta resource-manager tags values update 465/env/dev --description="foobar"

POSITIONAL ARGUMENTS
    

`RESOURCE_NAME`
     Resource name or namespaced name. The resource name should be in the form {resource_type}/{numeric_id}. The namespaced name should be in the form {org_id}/{short_name} where short_name must be 1-63 characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores ( _ ), dots (.), and alphanumerics between. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     User-assigned description of the TagKey or TagValue. Must not exceed 256 characters. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud resource-manager tags values update](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/update)
    
    
    [gcloud alpha resource-manager tags values update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/tags/values/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
