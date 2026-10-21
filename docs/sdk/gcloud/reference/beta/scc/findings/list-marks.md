---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc/findings/list-marks/
title: gcloud beta scc findings list-marks \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:35.215222+00:00
---

# gcloud beta scc findings list-marks  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc/findings/list-marks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta scc findings list-marks Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta scc findings list-marks - list a finding's security marks 
SYNOPSIS
    

`gcloud beta scc findings list-marks` `FINDING` [`--location`=`LOCATION`; default="global"] [`--page-token`=`PAGE_TOKEN`] [`--read-time`=`READ_TIME`] [`--source`=`SOURCE`; default="-"] [`--folder`=`FOLDER` | `--organization`=`ORGANIZATION` | `--project`=`PROJECT`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` List a finding's security marks. 
EXAMPLES
     List all security marks for `testFinding` under organization `123456` and source `5678`: 
    
    
    gcloud beta scc findings list-marks `testFinding` --organization=123456 --source=5678

List all security marks for `testFinding` under project `example-project` and source `5678`: 
    
    
    gcloud beta scc findings list-marks projects/example-project/sources/5678/findings/testFinding

List all security marks for `testFinding` under folder `456` and source `5678`: 
    
    
    gcloud beta scc findings list-marks folders/456/sources/5678/findings/testFinding

List all security marks for `testFinding` under organization `123456`, source `5678` and `location=eu`: 
    
    
    gcloud beta scc findings list-marks `testFinding` --organization=123456 --source=5678 --location=eu

POSITIONAL ARGUMENTS
    

`FINDING`
     ID of the finding or fully qualified identifier for the finding. 
FLAGS
    

`--location`=`LOCATION`; default="global"
     When data residency controls are enabled, this attribute specifies the location in which the resource is located and applicable. The `location` attribute can be provided as part of the fully specified resource name or with the `--location` argument on the command line. The default location is `global`. 

NOTE: If you override the endpoint to a [regional endpoint](https://cloud.google.com/security-command-center/docs/reference/rest/index.html?rep_location=global#regional-service-endpoint) you must specify the correct [data location](https://cloud.google.com/security-command-center/docs/data-residency-support#locations) using this flag. The default location on this command is unrelated to the default location that is specified when data residency controls are enabled for Security Command Center. 

NOTE: If no location is specified, the default location is `global` AND the request will be routed to the SCC V1 API. To use the SCC V2 API - please explicitly specify the flag. 

`--page-token`=`PAGE_TOKEN`
     Response objects will return a non-null value for page-token to indicate that there is at least one additional page of data. User can either directly request that page by specifying the page-token explicitly or let gcloud fetch one-page-at-a-time. 
`--read-time`=`READ_TIME`
     (DEPRECATED) Time used as a reference point when filtering. Absence of this field will default to the API's version of NOW. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on supported time formats. 

The --read-time option is deprecated. For more information, [see the deprecation notice](https://cloud.google.com/security-command-center/docs/release-notes#April_15_2024) on the SCC release notes page. 

`--source`=`SOURCE`; default="-"
     Source id. Defaults to all sources. 
At most one of these can be specified: 

`--folder`=`FOLDER`
     The folder ID (e.g., 456) that contains the finding. 
`--organization`=`ORGANIZATION`
     The organization ID (e.g., 123) that contains the finding. 
`--project`=`PROJECT`
     The project ID (e.g., example-project) that contains the finding. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the Security Command Center API. For more information, see [Security Command Center API.](https://cloud.google.com/security-command-center/docs/reference/rest)
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud scc findings list-marks](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/list-marks)
    
    
    [gcloud alpha scc findings list-marks](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/findings/list-marks)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
