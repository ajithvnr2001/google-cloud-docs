---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/networks/peerings/create/
title: gcloud beta compute networks peerings create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:57:02.136040+00:00
---

# gcloud beta compute networks peerings create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/networks/peerings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute networks peerings create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute networks peerings create - create a Compute Engine network peering 
SYNOPSIS
    

`gcloud beta compute networks peerings create` `NAME` `--network`=`NETWORK` `--peer-network`=`PEER_NETWORK` [`--async`] [`--auto-create-routes`] [`--export-custom-routes`] [`--export-subnet-routes-with-public-ip`] [`--import-custom-routes`] [`--import-subnet-routes-with-public-ip`] [`--peer-project`=`PEER_PROJECT`] [`--stack-type`=`STACK_TYPE`] [`--update-strategy`=`UPDATE_STRATEGY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute networks peerings create` is used to create peerings between virtual networks. Each side of a peering association is set up independently. Peering will be active only when the configuration from both sides matches. 
EXAMPLES
     To create a network peering with the name 'peering-name' between the network 'local-network' and the network 'peer-network' which exports and imports custom routes and subnet routes with public IPs, run: 
    
    
    gcloud beta compute networks peerings create peering-name --network=local-network --peer-network=peer-network --export-custom-routes --import-custom-routes --export-subnet-routes-with-public-ip --import-subnet-routes-with-public-ip

POSITIONAL ARGUMENTS
    

`NAME`
     The name of the peering. 
REQUIRED FLAGS
    

`--network`=`NETWORK`
     The name of the network in the current project to be peered with the peer network. 
`--peer-network`=`PEER_NETWORK`
     The name of the network to be peered with the current network. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--auto-create-routes`
     (DEPRECATED) If set, will automatically create routes for the network peering. Flag auto-create-routes is deprecated. Peer network subnet routes are always created in a network when peered. 

Flag --auto-create-routes is deprecated and will be removed in a future release. 

`--export-custom-routes`
     If set, the network will export custom routes to peer network. Use \--no-export-custom-routes to disable it. 
`--export-subnet-routes-with-public-ip`
     If set, the network will export subnet routes with addresses in the public IP ranges to peer network. Use --no-export-subnet-routes-with-public-ip to disable it. 
`--import-custom-routes`
     If set, the network will import custom routes from peer network. Use \--no-import-custom-routes to disable it. 
`--import-subnet-routes-with-public-ip`
     If set, the network will import subnet routes with addresses in the public IP ranges from peer network. Use --no-import-subnet-routes-with-public-ip to disable it. 
`--peer-project`=`PEER_PROJECT`
     The name of the project for the peer network. If not specified, defaults to current project. 
`--stack-type`=`STACK_TYPE`
     Stack type of the peering. If not specified, defaults to IPV4_ONLY. 

STACK_TYPE must be one of: 
    
    
    IPV4_ONLY
       Only IPv4 traffic and routes will be exchanged across this peering.
    
    
    IPV4_IPV6
       IPv4 traffic and routes will be exchanged across this peering.
       IPv6 traffic and routes will be exchanged if the matching peering
       configuration also has stack_type set to IPV4_IPV6.

`--update-strategy`=`UPDATE_STRATEGY`
     Update strategy of the peering. If not specified, defaults to INDEPENDENT. 

UPDATE_STRATEGY must be one of: 

INDEPENDENT Updates and deletes to the peering connection can be performed by either network admin. 

CONSENSUS Updates and deletes to the peering connection must be agreed upon by both network admins. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute networks peerings create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/peerings/create)
    
    
    [gcloud alpha compute networks peerings create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/networks/peerings/create)
    
    
    [gcloud preview compute networks peerings create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/networks/peerings/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
