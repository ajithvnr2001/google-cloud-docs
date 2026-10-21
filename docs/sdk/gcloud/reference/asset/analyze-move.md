---
url: https://docs.cloud.google.com/sdk/gcloud/reference/asset/analyze-move/
title: gcloud asset analyze-move \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:33:00.573803+00:00
---

# gcloud asset analyze-move  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/asset/analyze-move/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud asset analyze-move Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud asset analyze-move - analyzes resource move 
SYNOPSIS
    

`gcloud asset analyze-move` `--project`=`PROJECT_ID` (`--destination-folder`=`FOLDER_ID` | `--destination-organization`=`ORGANIZATION_ID`) [`--blockers-only`=`BLOCKERS_ONLY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Analyze resource migration from its current resource hierarchy. 
EXAMPLES
     To analyze the impacts of moving a project to a different organization, run: 
    
    
    gcloud asset analyze-move --project=YOUR_PROJECT_ID --destination-organization=ORGANIZATION_ID

To analyze the impacts of moving a project to a different folder, run: 
    
    
    gcloud asset analyze-move --project=YOUR_PROJECT_ID --destination-folder=FOLDER_ID

To analyze only the blockers of moving a project to a different folder, run: 
    
    
    gcloud asset analyze-move --project=YOUR_PROJECT_ID --destination-folder=FOLDER_ID --blockers-only=true

REQUIRED FLAGS
    

`--project`=`PROJECT_ID`
     The project ID or number to perform the analysis. 
Exactly one of these must be specified: 

`--destination-folder`=`FOLDER_ID`
     The destination folder ID to perform the analysis. 
`--destination-organization`=`ORGANIZATION_ID`
     The destination organization ID to perform the analysis. 
OPTIONAL FLAGS
    

`--blockers-only`=`BLOCKERS_ONLY`
     Determines whether to perform analysis against blockers only. Leaving it empty means the full analysis will be performed including warnings and blockers for the specified resource move. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
