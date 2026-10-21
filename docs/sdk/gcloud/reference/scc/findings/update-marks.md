---
url: https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/update-marks/
title: gcloud scc findings update-marks \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:00.888441+00:00
---

# gcloud scc findings update-marks  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/update-marks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud scc findings update-marks Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud scc findings update-marks - update Security Command Center finding's security marks 
SYNOPSIS
    

`gcloud scc findings update-marks` `FINDING` [`--location`=`LOCATION`; default="global"] [`--security-marks`=[`KEY`=`VALUE`,…]] [`--source`=`SOURCE`; default="-"] [`--start-time`=`START_TIME`] [`--update-mask`=`UPDATE_MASK`] [`--folder`=`FOLDER` | `--organization`=`ORGANIZATION` | `--project`=`PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update Security Command Center finding's security marks. 
EXAMPLES
     Selectively update security mark `Key1` with value `v1` on testFinding. Note that other security marks on `testFinding` are untouched: 
    
    
    gcloud scc findings update-marks `testFinding` --organization=123456 --source=5678 --security-marks="key1=v1" --update-mask="marks.markKey1"

Update all security marks on `testFinding`, under project `example-project` and source `5678`: 
    
    
    gcloud scc findings update-marks projects/example-project/sources/5678/findings/testFinding --security-marks="key1=v1,key2=v2"

Update all security marks on `testFinding`, under folder `456` and source `5678`: 
    
    
    gcloud scc findings update-marks folders/456/sources/5678/findings/testFinding --security-marks="key1=v1,key2=v2"

Update all security marks on `testFinding`, under organization `123456` and source `5678`: 
    
    
    gcloud scc findings update-marks `testFinding` --organization=123456 --source=5678 --security-marks="key1=v1,key2=v2"

Delete all security marks on `testFinding`: 
    
    
    gcloud scc findings update-marks `testFinding` --organization=123456 --source=5678 --security-marks=""

Update all security marks on `testFinding`, under project `example-project`, source `5678` and `location=eu`: 
    
    
    gcloud scc findings update-marks projects/example-project/sources/5678/findings/testFinding --security-marks="key1=v1,key2=v2" --location=eu

POSITIONAL ARGUMENTS
    

`FINDING`
     ID of the finding or fully qualified identifier for the finding. 
FLAGS
    

`--location`=`LOCATION`; default="global"
     When data residency controls are enabled, this attribute specifies the location in which the resource is located and applicable. The `location` attribute can be provided as part of the fully specified resource name or with the `--location` argument on the command line. The default location is `global`. 

NOTE: If you override the endpoint to a [regional endpoint](https://cloud.google.com/security-command-center/docs/reference/rest/index.html?rep_location=global#regional-service-endpoint) you must specify the correct [data location](https://cloud.google.com/security-command-center/docs/data-residency-support#locations) using this flag. The default location on this command is unrelated to the default location that is specified when data residency controls are enabled for Security Command Center. 

NOTE: If no location is specified, the default location is `global` AND the request will be routed to the SCC V1 API. To use the SCC V2 API - please explicitly specify the flag. 

`--security-marks`=[`KEY`=`VALUE`,…]
     SecurityMarks resource to be passed as the request body. It's a key=value pair separated by comma (,). For example: --security-marks="key1=val1,key2=val2". 
`--source`=`SOURCE`; default="-"
     Source id. Defaults to all sources. 
`--start-time`=`START_TIME`
     Time at which the updated SecurityMarks take effect. See `$ [gcloud topic](https://docs.cloud.google.com/sdk/gcloud/reference/topic) datetimes` for information on supported time formats. 
`--update-mask`=`UPDATE_MASK`
     Use update-mask if you want to selectively update marks represented by \--security-marks flag. For example: --update-mask="marks.key1,marks.key2". If you want to override all the marks for the given finding either skip the update-mask flag or provide an empty value (--update-mask '') for it. 
At most one of these can be specified: 

`--folder`=`FOLDER`
     The folder ID (e.g., 456) that contains the finding. 
`--organization`=`ORGANIZATION`
     The organization ID (e.g., 123) that contains the finding. 
`--project`=`PROJECT`
     The project ID (e.g., example-project) that contains the finding. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the Security Command Center API. For more information, see [Security Command Center API.](https://cloud.google.com/security-command-center/docs/reference/rest)
NOTES
     These variants are also available: 
    
    
    [gcloud alpha scc findings update-marks](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/findings/update-marks)
    
    
    [gcloud beta scc findings update-marks](https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc/findings/update-marks)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
