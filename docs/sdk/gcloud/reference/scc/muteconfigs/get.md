---
url: https://docs.cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/get/
title: gcloud scc muteconfigs get \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:04.956187+00:00
---

# gcloud scc muteconfigs get  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/scc/muteconfigs/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud scc muteconfigs get Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud scc muteconfigs get - get a Security Command Center mute config 
SYNOPSIS
    

`gcloud scc muteconfigs get` `MUTE_CONFIG` [`--location`=`LOCATION`; default="global"] [`--folder`=`FOLDER` | `--organization`=`ORGANIZATION` | `--project`=`PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Get a Security Command Center mute config. 
EXAMPLES
     To get a mute config given organization ``123`` with id ``test-mute-config``, run: 
    
    
    gcloud scc muteconfigs get test-mute-config --organization=123

To get a mute config given folder ``456`` with id ``test-mute-config``, run: 
    
    
    gcloud scc muteconfigs get test-mute-config --folder=456

To get a mute config given project ``789`` with id ``test-mute-config``, run: 
    
    
    gcloud scc muteconfigs get test-mute-config --project=789

To get a mute config given organization ``123`` with id ``test-mute-config`` and `location=eu`, run: 
    
    
    gcloud scc muteconfigs get test-mute-config --organization=123 --location=eu

POSITIONAL ARGUMENTS
    

`MUTE_CONFIG`
     ID of the mute config or the full resource name of the mute config. 
FLAGS
    

`--location`=`LOCATION`; default="global"
     When data residency controls are enabled, this attribute specifies the location in which the resource is located and applicable. The `location` attribute can be provided as part of the fully specified resource name or with the `--location` argument on the command line. The default location is `global`. 

NOTE: If you override the endpoint to a [regional endpoint](https://cloud.google.com/security-command-center/docs/reference/rest/index.html?rep_location=global#regional-service-endpoint) you must specify the correct [data location](https://cloud.google.com/security-command-center/docs/data-residency-support#locations) using this flag. The default location on this command is unrelated to the default location that is specified when data residency controls are enabled for Security Command Center. 

NOTE: If no location is specified, the default location is `global` AND the request will be routed to the SCC V1 API. To use the SCC V2 API - please explicitly specify the flag. 

At most one of these can be specified: 

`--folder`=`FOLDER`
     Folder where the mute config resides. Formatted as ``folders/456`` or just ``456``. 
`--organization`=`ORGANIZATION`
     Organization where the mute config resides. Formatted as ``organizations/123`` or just ``123``. 
`--project`=`PROJECT`
     Project (id or number) where the mute config resides. Formatted as ``projects/789`` or just ``789``. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the Security Command Center API. For more information, see [Security Command Center API.](https://cloud.google.com/security-command-center/docs/reference/rest)
NOTES
     This variant is also available: 
    
    
    [gcloud alpha scc muteconfigs get](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/muteconfigs/get)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
