---
url: https://docs.cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/create/
title: gcloud services peered-dns-domains create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:45.509110+00:00
---

# gcloud services peered-dns-domains create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud services peered-dns-domains create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud services peered-dns-domains create - create a peered DNS domain for a private service connection 
SYNOPSIS
    

`gcloud services peered-dns-domains create` `NAME` `--dns-suffix`=`DNS_SUFFIX` `--network`=`NETWORK` [`--async`] [`--service`=`SERVICE`; default="servicenetworking.googleapis.com"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command creates a peered DNS domain for a private service connection which sends requests for records in a given namespace originating in the service producer VPC network to the consumer VPC network to be resolved. 
EXAMPLES
     To create a peered DNS domain called `example-com` which forwards DNS requests for the domain suffix `example.com.` for a private service connection between service `peering-service` and the consumer network `my-network` in the current project, run: 
    
    
    gcloud services peered-dns-domains create example-com --network=my-network --service=peering-service --dns-suffix=example.com.

To run the same command asynchronously (non-blocking), run: 
    
    
    gcloud services peered-dns-domains create example-com --network=my-network --service=peering-service --dns-suffix=example.com. --async

POSITIONAL ARGUMENTS
    

`NAME`
     The name of the peered DNS domain to create. 
REQUIRED FLAGS
    

`--dns-suffix`=`DNS_SUFFIX`
     The DNS domain name suffix of the peered DNS domain. 
`--network`=`NETWORK`
     The network in the consumer project peered with the service. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--service`=`SERVICE`; default="servicenetworking.googleapis.com"
     The name of the service to create a peered DNS domain for. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha services peered-dns-domains create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/peered-dns-domains/create)
    
    
    [gcloud beta services peered-dns-domains create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/peered-dns-domains/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
