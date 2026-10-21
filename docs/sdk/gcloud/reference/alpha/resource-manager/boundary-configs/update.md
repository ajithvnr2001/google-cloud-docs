---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/boundary-configs/update/
title: gcloud alpha resource-manager boundary-configs update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:27:48.153627+00:00
---

# gcloud alpha resource-manager boundary-configs update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/boundary-configs/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha resource-manager boundary-configs update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha resource-manager boundary-configs update - update a boundary configuration 
SYNOPSIS
    

`gcloud alpha resource-manager boundary-configs update` (`--clear-tag-key` | `--tag-key`=`TAG_KEY`) (`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID`) [`--async`] [`--etag`=`ETAG`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha resource-manager boundary-configs update` updates the boundary configuration under the specified organization or folder. 
EXAMPLES
     To update the tag key of the boundary configuration in an organization with ID `123456789012`, run: 
    
    
    gcloud alpha resource-manager boundary-configs update --organization=123456789012 --tag-key=123456789012/env

To update the tag key of the boundary configuration in a folder with ID `456789012345`, run: 
    
    
    gcloud alpha resource-manager boundary-configs update --folder=456789012345 --tag-key=123456789012/env

To clear the tag key of the boundary configuration in a folder with ID `456789012345`, run: 
    
    
    gcloud alpha resource-manager boundary-configs update --folder=456789012345 --clear-tag-key

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--clear-tag-key`
     Clear the tag key from the boundary config. 
`--tag-key`=`TAG_KEY`
     The namespaced name of the tag key (e.g. 123456789012/env). 
Exactly one of these must be specified: 

`--folder`=`FOLDER_ID`
     Folder ID. 
`--organization`=`ORGANIZATION_ID`
     Organization ID. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--etag`=`ETAG`
     The etag of the boundary config. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud resource-manager boundary-configs update](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/boundary-configs/update)
    
    
    [gcloud beta resource-manager boundary-configs update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/boundary-configs/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
