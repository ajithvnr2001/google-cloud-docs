---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/vpc-peerings/update/
title: gcloud beta services vpc-peerings update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:44.336904+00:00
---

# gcloud beta services vpc-peerings update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/vpc-peerings/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta services vpc-peerings update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta services vpc-peerings update - update a private service connection to a service for a project network 
SYNOPSIS
    

`gcloud beta services vpc-peerings update` `--network`=`NETWORK` [`--async`] [`--force`] [`--ranges`=`RANGES`] [`--service`=`SERVICE`; default="servicenetworking.googleapis.com"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command updates a private service connection to a service via a VPC network. 
EXAMPLES
     To update connection for a network called `my-network` on the current project to a service called `your-service` with IP CIDR ranges `google-range-1,google-range-2` for the service to use, run: 
    
    
    gcloud beta services vpc-peerings update --network=my-network --service=your-service --ranges=google-range-1,google-range-2

To run the same command asynchronously (non-blocking), run: 
    
    
    gcloud beta services vpc-peerings update --network=my-network --service=your-service --ranges=google-range-1,google-range-2 --async

REQUIRED FLAGS
    

`--network`=`NETWORK`
     The network in the current project to be peered with the service 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--force`
     If specified, the update call will proceed even if the update can be destructive. 
`--ranges`=`RANGES`
     The names of IP CIDR ranges for service to use. 
`--service`=`SERVICE`; default="servicenetworking.googleapis.com"
     The service to connect to 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud services vpc-peerings update](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/update)
    
    
    [gcloud alpha services vpc-peerings update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/vpc-peerings/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
