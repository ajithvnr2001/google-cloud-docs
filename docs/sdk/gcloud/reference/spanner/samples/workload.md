---
url: https://docs.cloud.google.com/sdk/gcloud/reference/spanner/samples/workload/
title: gcloud spanner samples workload \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:30:22.167440+00:00
---

# gcloud spanner samples workload  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/spanner/samples/workload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud spanner samples workload Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud spanner samples workload - generate gRPC traffic for a given sample app's backend service 
SYNOPSIS
    

`gcloud spanner samples workload` `APPNAME` [`--duration`=`DURATION`; default="1h"] [`--port`=`PORT`] [`--target-qps`=`TARGET_QPS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Before sending traffic to the backend service, create the database and start the service with: 
    
    
    [gcloud spanner samples init](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/samples/init) APPNAME --instance-id=INSTANCE_ID
    [gcloud spanner samples backend](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/samples/backend) APPNAME --instance-id=INSTANCE_ID

To run all three steps together, use: 
    
    
    [gcloud spanner samples run](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/samples/run) APPNAME --instance-id=INSTANCE_ID

EXAMPLES
     To generate traffic for the 'finance' sample app, run: 
    
    
    gcloud spanner samples workload finance

POSITIONAL ARGUMENTS
    

`APPNAME`
     The sample app name, e.g. "finance". 
FLAGS
    

`--duration`=`DURATION`; default="1h"
     Duration of time allowed to run before stopping the workload. 
`--port`=`PORT`
     Port of the running backend service. 
`--target-qps`=`TARGET_QPS`
     Target requests per second. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha spanner samples workload](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/samples/workload)
    
    
    [gcloud beta spanner samples workload](https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/samples/workload)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
