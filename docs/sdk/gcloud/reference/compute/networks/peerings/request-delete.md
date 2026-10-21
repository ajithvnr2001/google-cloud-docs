---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/request-delete/
title: gcloud compute networks peerings request-delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:16:59.723652+00:00
---

# gcloud compute networks peerings request-delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/request-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute networks peerings request-delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute networks peerings request-delete - request deletion of a Compute Engine network peering 
SYNOPSIS
    

`gcloud compute networks peerings request-delete` `NAME` `--network`=`NETWORK` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute networks peerings request-delete` is used to request deletion of a consensus peering between virtual networks. The peering can be deleted if both sides request deletion. 
EXAMPLES
     To request deletion of a consensus peering with the name 'peering-name' between the network 'local-network' and the network 'peer-network', run: 
    
    
    gcloud compute networks peerings request-delete peering-name --network=local-network
    
    
    gcloud compute networks peerings request-delete peering-name --network=peer-network

To complete the deletion, run gcloud compute networks peerings delete for each side of the peering. 

POSITIONAL ARGUMENTS
    

`NAME`
     The name of the peering. 
REQUIRED FLAGS
    

`--network`=`NETWORK`
     The name of the network in the current project containing the peering. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute networks peerings request-delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/networks/peerings/request-delete)
    
    
    [gcloud beta compute networks peerings request-delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/networks/peerings/request-delete)
    
    
    [gcloud preview compute networks peerings request-delete](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/networks/peerings/request-delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
