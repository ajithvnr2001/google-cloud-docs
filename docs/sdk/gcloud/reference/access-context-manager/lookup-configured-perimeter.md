---
url: https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/lookup-configured-perimeter/
title: gcloud access-context-manager lookup-configured-perimeter \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:35:12.956223+00:00
---

# gcloud access-context-manager lookup-configured-perimeter  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/lookup-configured-perimeter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud access-context-manager lookup-configured-perimeter Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud access-context-manager lookup-configured-perimeter - look up the configured VPC Service Controls service perimeter for a resource 
SYNOPSIS
    

`gcloud access-context-manager lookup-configured-perimeter` `--resource`=`RESOURCE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Looks up the configured VPC Service Controls service perimeter (both enforced and dry-run) that applies to the specified project or folder based on resource hierarchy ancestry. 
EXAMPLES
     To look up the configured perimeter for a project with number 1234567890: 
    
    
    gcloud access-context-manager lookup-configured-perimeter --resource=projects/1234567890

To look up the configured perimeter for a folder with number 9876543210: 
    
    
    gcloud access-context-manager lookup-configured-perimeter --resource=folders/9876543210

REQUIRED FLAGS
    

`--resource`=`RESOURCE`
     The resource to look up effective service perimeters for. Format: `projects/{project_number}` or `folders/{folder_number}`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha access-context-manager lookup-configured-perimeter](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/lookup-configured-perimeter)
    
    
    [gcloud beta access-context-manager lookup-configured-perimeter](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/lookup-configured-perimeter)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
