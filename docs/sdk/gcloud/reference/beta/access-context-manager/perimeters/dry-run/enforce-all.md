---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/enforce-all/
title: gcloud beta access-context-manager perimeters dry-run enforce-all \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:01.830941+00:00
---

# gcloud beta access-context-manager perimeters dry-run enforce-all  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/enforce-all/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta access-context-manager perimeters dry-run enforce-all Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta access-context-manager perimeters dry-run enforce-all - enforces the dry-run mode configuration for all Service Perimeters 
SYNOPSIS
    

`gcloud beta access-context-manager perimeters dry-run enforce-all` [`--etag`=`etag`] [`--policy`=`policy`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` An enforce operation on a Service Perimeter involves copying its dry-run mode configuration (`spec`) to that Service Perimeter's enforcement mode configration (`status`). This command performs this operation for `all` Service Perimeters in the user's Access Policy. 

Note: Only Service Perimeters with an explicit dry-run mode configuration are affected by this operation. The overall operation succeeds once the dry-run configurations of all such Service Perimeters have been enforced. If the operation fails for any given Service Perimeter, it will cause the entire operation to be aborted. 

EXAMPLES
     To enforce the dry-run mode configurations for all Service Perimeter in an Access Policy, run the following command: 
    
    
    gcloud beta access-context-manager perimeters dry-run enforce-all

FLAGS
    

`--etag`=`etag`
     The etag for the version of the Access Policy that this operation is to be performed on. If, at the time of the operation, the etag for the Access Policy stored in Access Context Manager is different from the specified etag, then the commit operation will not be performed and the call will fail. If etag is not provided, the operation will be performed as if a valid etag is provided. 
`--policy`=`policy`
     The parent Access Policy which owns all Service Perimeters in scope for the commit operation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud access-context-manager perimeters dry-run enforce-all](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/enforce-all)
    
    
    [gcloud alpha access-context-manager perimeters dry-run enforce-all](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/dry-run/enforce-all)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
