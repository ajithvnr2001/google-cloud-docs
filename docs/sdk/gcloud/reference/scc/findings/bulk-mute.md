---
url: https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/bulk-mute/
title: gcloud scc findings bulk-mute \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:00.152268+00:00
---

# gcloud scc findings bulk-mute  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/bulk-mute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud scc findings bulk-mute Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud scc findings bulk-mute - bulk mute Security Command Center findings based on a filter 
SYNOPSIS
    

`gcloud scc findings bulk-mute` `--filter`=`FILTER` (`--folder`=`FOLDER` | `--organization`=`ORGANIZATION` | `--project`=`PROJECT`) [`--location`=`LOCATION`; default="global"] [`--mute-state`=`MUTE_STATE`; default="muted"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Bulk mute Security Command Center findings based on a filter. 
EXAMPLES
     To bulk mute findings given organization ``123`` based on a filter on category that equals ``XSS_SCRIPTING``, run: 
    
    
    gcloud scc findings bulk-mute --organization=organizations/123 --filter="category=\"XSS_SCRIPTING\""

To bulk mute findings given folder ``123`` based on a filter on category that equals ``XSS_SCRIPTING``, run: 
    
    
    gcloud scc findings bulk-mute --folder=folders/123 --filter="category=\"XSS_SCRIPTING\""

To bulk mute findings given project ``123`` based on a filter on category that equals ``XSS_SCRIPTING``, run: 
    
    
    gcloud scc findings bulk-mute --project=projects/123 --filter="category=\"XSS_SCRIPTING\""

To bulk mute findings given organization ``123`` based on a filter on category that equals ``XSS_SCRIPTING`` and `location=eu` run: 
    
    
    gcloud scc findings bulk-mute --organization=organizations/123 --filter="category=\"XSS_SCRIPTING\"" --location=locations/eu

REQUIRED FLAGS
    

`--filter`=`FILTER`
     Expression that identifies findings that should be muted. 
Exactly one of these must be specified: 

`--folder`=`FOLDER`
     Folder where the findings reside. Formatted as ``folders/456`` or just ``456``. 
`--organization`=`ORGANIZATION`
     Organization where the findings reside. Formatted as ``organizations/123`` or just ``123``. 
`--project`=`PROJECT`
     Project (id or number) where the findings reside. Formatted as ``projects/789`` or just ``789``. 
OPTIONAL FLAGS
    

`--location`=`LOCATION`; default="global"
     When data residency controls are enabled, this attribute specifies the location in which the resource is located and applicable. The `location` attribute can be provided as part of the fully specified resource name or with the `--location` argument on the command line. The default location is `global`. 

NOTE: If you override the endpoint to a [regional endpoint](https://cloud.google.com/security-command-center/docs/reference/rest/index.html?rep_location=global#regional-service-endpoint) you must specify the correct [data location](https://cloud.google.com/security-command-center/docs/data-residency-support#locations) using this flag. The default location on this command is unrelated to the default location that is specified when data residency controls are enabled for Security Command Center. 

NOTE: If no location is specified, the default location is `global` AND the request will be routed to the SCC V1 API. To use the SCC V2 API - please explicitly specify the flag. 

`--mute-state`=`MUTE_STATE`; default="muted"
     Desired mute state of the finding. `MUTE_STATE` must be one of: `muted`, `undefined`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the Security Command Center API. For more information, see [Security Command Center API.](https://cloud.google.com/security-command-center/docs/reference/rest)
NOTES
     This variant is also available: 
    
    
    [gcloud alpha scc findings bulk-mute](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/findings/bulk-mute)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
