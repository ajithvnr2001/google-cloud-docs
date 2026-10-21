---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/manage/billing-metadata/describe/
title: gcloud alpha scc manage billing-metadata describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:15.562874+00:00
---

# gcloud alpha scc manage billing-metadata describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/manage/billing-metadata/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc manage billing-metadata describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc manage billing-metadata describe - get the billing metadata for a specific resource 
SYNOPSIS
    

`gcloud alpha scc manage billing-metadata describe` (`--organization`=`ORGANIZATION_ID` | `--parent`=`PARENT` | `--project`=`PROJECT_ID_OR_NUMBER`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Get the billing metadata for a given Google Cloud resource, including the associated billing account, cost-related settings, and other relevant information. 
EXAMPLES
     To get the details of a billing metadata for organization `123`, run: 
    
    
    gcloud alpha scc manage billing-metadata describe --organization=123

To get the details of a billing metadata for project `456`, run: 
    
    
    gcloud alpha scc manage billing-metadata describe --project=456

You can also specify the parent more generally for organizations: 
    
    
    gcloud alpha scc manage billing-metadata describe --parent=organizations/123

Or you can specify the parent for projects: 
    
    
    gcloud alpha scc manage billing-metadata describe --parent=projects/123

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--organization`=`ORGANIZATION_ID`
     Organization associated with the billing metadata. 
`--parent`=`PARENT`
     Parent associated with the billing metadata. Can be one of organizations/<id>, projects/<id or name>
`--project`=`PROJECT_ID_OR_NUMBER`
     Project associated with the billing metadata. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
