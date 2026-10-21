---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/create/
title: gcloud dns response-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:36:50.160269+00:00
---

# gcloud dns response-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dns/response-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dns response-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dns response-policies create - creates a new Cloud DNS response policy 
SYNOPSIS
    

`gcloud dns response-policies create` `RESPONSE_POLICIES` `--description`=`DESCRIPTION` [`--gkeclusters`=[`GKECLUSTERS`,…]] [`--location`=`LOCATION`] [`--networks`=[`NETWORKS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command creates a new Cloud DNS response policy. 
EXAMPLES
     To create a new response policy with minimal arguments, run: 
    
    
    gcloud dns response-policies create myresponsepolicy --description='My new response policy.' --networks=''

To create a new response policy with all optional arguments, run: 
    
    
    gcloud dns response-policies create myresponsepolicy --description='My new response policy.' --networks=network1,network2

To create a new zonal response policy scoped to a GKE cluster in
    
    
    us-central1-a, run (alpha/beta):
    
    
    gcloud dns response-policies create beta myresponsepolicy --description='My new response
    policy.' --gkeclusters=cluster1 --location=us-central1-a

POSITIONAL ARGUMENTS
    

Response policy resource - The response policy to create. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `response_policies` on the command line with a fully specified name; 
  * set the property `core/project`. 



This must be specified. 

`RESPONSE_POLICIES`
     ID of the response_policy or fully qualified identifier for the response_policy. 

To set the `response-policy` attribute: 

  * provide the argument `response_policies` on the command line. 


REQUIRED FLAGS
    

`--description`=`DESCRIPTION`
     A description of the response policy. 
OPTIONAL FLAGS
    

`--gkeclusters`=[`GKECLUSTERS`,…]
     The comma-separated list of GKE cluster names to associate with the response policy. 
`--location`=`LOCATION`
     Specifies the desired service location the request is sent to. Defaults to Cloud DNS global service. Use --location=global if you want to target the global service. 
`--networks`=[`NETWORKS`,…]
     The comma-separated list of network names to associate with the response policy. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha dns response-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/response-policies/create)
    
    
    [gcloud beta dns response-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/response-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
