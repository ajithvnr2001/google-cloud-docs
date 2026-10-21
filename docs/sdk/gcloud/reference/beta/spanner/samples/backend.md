---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/samples/backend/
title: gcloud beta spanner samples backend \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:39:45.303887+00:00
---

# gcloud beta spanner samples backend  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/samples/backend/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta spanner samples backend Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta spanner samples backend - run the backend gRPC service for the given Cloud Spanner sample app 
SYNOPSIS
    

`gcloud beta spanner samples backend` `APPNAME` `--instance-id`=`INSTANCE_ID` [`--database-id`=`DATABASE_ID`] [`--duration`=`DURATION`; default="1h"] [`--port`=`PORT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command starts the backend gRPC service for the given sample application. Before starting the service, create the database and load any initial data with: 
    
    
    [gcloud beta spanner samples init](https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/samples/init) APPNAME --instance-id=INSTANCE_ID

After starting the service, generate traffic with: 
    
    
    [gcloud beta spanner samples workload](https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/samples/workload) APPNAME

To run all three steps together, use: 
    
    
    [gcloud beta spanner samples run](https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/samples/run) APPNAME --instance-id=INSTANCE_ID

EXAMPLES
     To run the backend gRPC service for the 'finance' sample app using instance 'my-instance', run: 
    
    
    gcloud beta spanner samples backend finance --instance-id=my-instance

POSITIONAL ARGUMENTS
    

`APPNAME`
     The sample app name, e.g. "finance". 
REQUIRED FLAGS
    

`--instance-id`=`INSTANCE_ID`
     The Cloud Spanner instance ID for the sample app. 
OPTIONAL FLAGS
    

`--database-id`=`DATABASE_ID`
     The Cloud Spanner database ID for the sample app. 
`--duration`=`DURATION`; default="1h"
     Duration of time allowed to run before stopping the service. 
`--port`=`PORT`
     Port on which to receive gRPC requests. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud spanner samples backend](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/samples/backend)
    
    
    [gcloud alpha spanner samples backend](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/samples/backend)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
