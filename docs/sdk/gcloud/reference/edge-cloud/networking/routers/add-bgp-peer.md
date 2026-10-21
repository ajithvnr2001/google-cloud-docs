---
url: https://docs.cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-bgp-peer/
title: gcloud edge-cloud networking routers add-bgp-peer \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:18:50.033676+00:00
---

# gcloud edge-cloud networking routers add-bgp-peer  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-bgp-peer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud edge-cloud networking routers add-bgp-peer Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud edge-cloud networking routers add-bgp-peer - add a BGP peer to a Distributed Cloud Edge Network router 
SYNOPSIS
    

`gcloud edge-cloud networking routers add-bgp-peer` (`ROUTER` : `--location`=`LOCATION` `--zone`=`ZONE`) `--interface`=`INTERFACE` `--peer-asn`=`PEER_ASN` `--peer-ipv4-range`=`PEER_IPV4_RANGE` `--peer-name`=`PEER_NAME` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a BGP peer to a Distributed Cloud Edge Network router 
EXAMPLES
     To create and add a BGP peer for the Distributed Cloud Edge Network router 'my-router' in edge zone 'us-central1-edge-den1' , run: 
    
    
    gcloud edge-cloud networking routers add-bgp-peer my-router --interface=my-int-r1 --peer-asn=33333 --peer-name=peer1 --peer-ipv4-range=208.117.254.232/31 --location=us-central1 --zone=us-central1-edge-den1

POSITIONAL ARGUMENTS
    

Router resource - The router to which we add a bgp peer. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `router` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ROUTER`
     ID of the router or fully qualified identifier for the router. 

To set the `router` attribute: 

  * provide the argument `router` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Cloud location for the router. 

To set the `location` attribute: 

  * provide the argument `router` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--zone`=`ZONE`
     The zone of the router. 

To set the `zone` attribute: 

  * provide the argument `router` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line. 


REQUIRED FLAGS
    

`--interface`=`INTERFACE`
     The name of the interface for this BGP peer. 
`--peer-asn`=`PEER_ASN`
     The BGP autonomous system number (ASN) for this BGP peer. Must be a 16-bit or 32-bit private ASN as defined in https://tools.ietf.org/html/rfc6996, for example `--asn=64512`. 
`--peer-ipv4-range`=`PEER_IPV4_RANGE`
     The IPv4 link-local address range of the peer router. 
`--peer-name`=`PEER_NAME`
     The name of the new BGP peer being added. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha edge-cloud networking routers add-bgp-peer](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud/networking/routers/add-bgp-peer)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
