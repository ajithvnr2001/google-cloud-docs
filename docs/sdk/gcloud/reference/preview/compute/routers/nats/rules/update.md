---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/routers/nats/rules/update/
title: gcloud preview compute routers nats rules update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T09:54:52.885079+00:00
---

# gcloud preview compute routers nats rules update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/routers/nats/rules/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute routers nats rules update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute routers nats rules update - update a Rule in a Compute Engine NAT 
SYNOPSIS
    

`gcloud preview compute routers nats rules update` `RULE_NUMBER` `--nat`=`NAT` `--router`=`ROUTER` [`--async`] [`--match`=`MATCH`] [`--region`=`REGION`] [`--source-nat-active-ips`=`IP_ADDRESS`,[`IP_ADDRESS`,…]] [`--source-nat-active-ranges`=`SUBNETWORK`,[`SUBNETWORK`,…]] [`--clear-source-nat-drain-ips` | `--source-nat-drain-ips`=`IP_ADDRESS`,[`IP_ADDRESS`,…]] [`--clear-source-nat-drain-ranges` | `--source-nat-drain-ranges`=`SUBNETWORK`,[`SUBNETWORK`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute routers nats rules update` is used to update a Rule in a Compute Engine NAT. 
EXAMPLES
     To drain connections established using address-1 and use address-2 for all new connections matching Rule 1 in NAT nat-1, run: 
    
    
    gcloud preview compute routers nats rules update 1 --nat=nat1 --router=my-router --region=us-central1 --source-nat-drain-ips=address-1 --source-nat-active-ips=address-2

POSITIONAL ARGUMENTS
    

`RULE_NUMBER`
     Number that uniquely identifies the Rule to update 
REQUIRED FLAGS
    

`--nat`=`NAT`
     Name of the NAT that contains the Rule 
`--router`=`ROUTER`
     Router to use for NAT. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--match`=`MATCH`
     CEL Expression used to identify traffic to which this rule applies. 

  * Supported attributes (Public NAT): destination.ip 
  * Supported attributes (Private NAT): nexthop.hub 
  * Supported methods (Public Nat): inIpRange 
  * Supported operators (Public NAT): ||, == 
  * Supported operators (Private NAT): == 



Examples of allowed Match expressions (Public NAT): 

  * 'inIpRange(destination.ip, "203.0.113.0/24")'' 
  * 'destination.ip == "203.0.113.7"' 
  * 'destination.ip == "203.0.113.7" || inIpRange(destination.ip, "203.0.113.16/25")' 



Example of allowed Match expression (Private NAT): 

  * nexthop.hub == "//networkconnectivity.googleapis.com/projects/p1/locations/global/hubs/h1" 


`--region`=`REGION`
     Region of the NAT containing the Rule to update. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--source-nat-active-ips`=`IP_ADDRESS`,[`IP_ADDRESS`,…]
     External IP Addresses to use for connections matching this rule. This flag is supported only for Public NAT and is required when creating a Public NAT gateway. 

These must be valid reserved external IP addresses in the same region. 

`--source-nat-active-ranges`=`SUBNETWORK`,[`SUBNETWORK`,…]
     Subnetworks from which addresses are used for connections matching this rule. This flag is supported only for Private NAT and is required when creating a Private NAT gateway. 

These must be subnetwork resources in the same region, with purpose set to PRIVATE_NAT. 

At most one of these can be specified: 

`--clear-source-nat-drain-ips`
     Clear drained IPs from the rule 
`--source-nat-drain-ips`=`IP_ADDRESS`,[`IP_ADDRESS`,…]
     External IP Addresses to drain connections on. 

These must be external IPs previously used as active IPs on this rule. No new connections will be established using these IPs. 

At most one of these can be specified: 

`--clear-source-nat-drain-ranges`
     Clear drained ranges from the rule 
`--source-nat-drain-ranges`=`SUBNETWORK`,[`SUBNETWORK`,…]
     Subnetwork ranges to drain connections on. 

These must be subnetworks previously used as active ranges on this rule. No new connections will be established using these ranges. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute routers nats rules update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update)
    
    
    [gcloud alpha compute routers nats rules update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/routers/nats/rules/update)
    
    
    [gcloud beta compute routers nats rules update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/routers/nats/rules/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
