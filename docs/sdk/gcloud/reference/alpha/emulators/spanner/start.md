---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/emulators/spanner/start/
title: gcloud alpha emulators spanner start \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:17:59.789528+00:00
---

# gcloud alpha emulators spanner start  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/emulators/spanner/start/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha emulators spanner start Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha emulators spanner start - start a local Cloud Spanner emulator 
SYNOPSIS
    

`gcloud alpha emulators spanner start` [`--enable-fault-injection`=`ENABLE_FAULT_INJECTION`] [`--host-port`=`HOST_PORT`] [`--remote-functions-host-port`=`REMOTE_FUNCTIONS_HOST_PORT`] [`--rest-port`=`REST_PORT`] [`--use-docker`=`USE_DOCKER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command starts a local Cloud Spanner emulator. 
EXAMPLES
     To start a local Cloud Spanner emulator, run: 
    
    
    gcloud alpha emulators spanner start

FLAGS
    

`--enable-fault-injection`=`ENABLE_FAULT_INJECTION`
     If true, the emulator will randomly inject faults into transactions. This facilitates application abort-retry testing. 
`--host-port`=`HOST_PORT`
     The host:port to which the emulator should be bound. The default value is localhost:9010. Note that this port serves gRPC requests. To override the default port serving REST requests, use --rest-port. If using Docker to run the emulator, the host must be specified as an ipaddress. 
`--remote-functions-host-port`=`REMOTE_FUNCTIONS_HOST_PORT`
     The host:port address of the Functions Framework instance hosting remote functions. Only localhost addresses are supported. 
`--rest-port`=`REST_PORT`
     The port at which REST requests are served. gcloud uses REST to communicate with the emulator. The default value is 9020. 
`--use-docker`=`USE_DOCKER`
     Use the Cloud Spanner emulator docker image even if the platform has a native binary available in the gcloud CLI. Currently we only provide a native binary for Linux. For other systems, you must install Docker for your platform before starting the emulator. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud emulators spanner start](https://docs.cloud.google.com/sdk/gcloud/reference/emulators/spanner/start)
    
    
    [gcloud beta emulators spanner start](https://docs.cloud.google.com/sdk/gcloud/reference/beta/emulators/spanner/start)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
