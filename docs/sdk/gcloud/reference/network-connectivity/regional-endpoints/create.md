---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create/
title: gcloud network-connectivity regional-endpoints create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:52:29.600613+00:00
---

# gcloud network-connectivity regional-endpoints create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-connectivity regional-endpoints create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-connectivity regional-endpoints create - create a new regional endpoint 
SYNOPSIS
    

`gcloud network-connectivity regional-endpoints create` (`REGIONAL_ENDPOINT` : `--region`=`REGION`) `--target-google-api`=`TARGET_GOOGLE_API` [`--address`=`ADDRESS`] [`--async`] [`--description`=`DESCRIPTION`] [`--enable-global-access`] [`--labels`=[`KEY`=`VALUE`,…]] [`--network`=`NETWORK`] [`--subnetwork`=`SUBNETWORK`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a new regional endpoint with the given name. 
EXAMPLES
     To create a regional endpoint with the name 'my-regional-endpoint' in us-central1 targeting my-target-endpoint, run: 
    
    
    gcloud network-connectivity regional-endpoints create my-regional-endpoint --region=us-central1 [--address=my-address] [--network=my-network] [--subnetwork=my-subnet] --target-google-api=my-target-endpoint [--enable-global-access]

POSITIONAL ARGUMENTS
    

RegionalEndpoint resource - Name of the regional endpoint to be created. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `regional_endpoint` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`REGIONAL_ENDPOINT`
     ID of the regionalEndpoint or fully qualified identifier for the regionalEndpoint. 

To set the `regional_endpoint` attribute: 

  * provide the argument `regional_endpoint` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The location Id. To set the `region` attribute: 

  * provide the argument `regional_endpoint` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


REQUIRED FLAGS
    

`--target-google-api`=`TARGET_GOOGLE_API`
     The service endpoint the regional endpoint will connect to. 
OPTIONAL FLAGS
    

`--address`=`ADDRESS`
     The IP Address of the Regional Endpoint. When no address is provided, an IP from the subnetwork is allocated. Use one of the following formats: 

  * IPv4 address as in ``10.0.0.1``
  * Address resource URI as in ``projects/{project}/regions/{region}/addresses/{address_name}`` for an IPv4 or IPv6 address. 


`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Description of the regional endpoint. 
`--enable-global-access`
     Whether the REGIONAL or GLOBAL access is enabled. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--network`=`NETWORK`
     Consumer's VPC network that this regional endpoint belongs to. 
`--subnetwork`=`SUBNETWORK`
     The name of the subnetwork from which the IP address will be allocated. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkconnectivity/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest>
NOTES
     This variant is also available: 
    
    
    [gcloud beta network-connectivity regional-endpoints create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/regional-endpoints/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
