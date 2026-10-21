---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/public-advertised-prefixes/create/
title: gcloud alpha compute public-advertised-prefixes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:19:21.387653+00:00
---

# gcloud alpha compute public-advertised-prefixes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/public-advertised-prefixes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute public-advertised-prefixes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute public-advertised-prefixes create - creates a Compute Engine public advertised prefix 
SYNOPSIS
    

`gcloud alpha compute public-advertised-prefixes create` `NAME` `--range`=`RANGE` [`--description`=`DESCRIPTION`] [`--dns-verification-ip`=`DNS_VERIFICATION_IP`] [`--ipv6-access-type`=`IPV6_ACCESS_TYPE`] [`--network-tier`=`NETWORK_TIER`] [`--pdp-scope`=`PDP_SCOPE`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create a public advertised prefix: 
    
    
    gcloud alpha compute public-advertised-prefixes create my-public-advertised-prefix --range=120.120.10.0/24 --dns-verification-ip=120.120.10.15

To create a v2 public advertised prefix: 
    
    
    gcloud alpha compute public-advertised-prefixes create my-v2-public-advertised-prefix --range=120.120.10.0/24 --dns-verification-ip=120.120.10.15 --pdp-scope=REGIONAL

To create an IPv4 v2 public advertised prefix in Standard tier: 
    
    
    gcloud alpha compute public-advertised-prefixes create my-v2-public-advertised-prefix --range=120.120.0.0/23 --network-tier=STANDARD --dns-verification-ip=120.120.10.15 --pdp-scope=REGIONAL

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the public advertised prefix to operate on. 
REQUIRED FLAGS
    

`--range`=`RANGE`
     IP range allocated to this public advertised prefix, in CIDR format. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     Description of this public advertised prefix. 
`--dns-verification-ip`=`DNS_VERIFICATION_IP`
     IP address to use for verification. It must be within the IP range specified in \--range. 
`--ipv6-access-type`=`IPV6_ACCESS_TYPE`
     Specifies the IPv6 access type of the public advertised prefix. `IPV6_ACCESS_TYPE` must be one of: `internal`, `external`. 
`--network-tier`=`NETWORK_TIER`
     The network tier to assign to the public advertised prefix. ``NETWORK_TIER`` must be one of: `PREMIUM`, `STANDARD`. The default value is `PREMIUM`. 
`--pdp-scope`=`PDP_SCOPE`
     Specifies how child public delegated prefix will be scoped. `PDP_SCOPE` must be one of: `GLOBAL`, `REGIONAL`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute public-advertised-prefixes create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/create)
    
    
    [gcloud beta compute public-advertised-prefixes create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/public-advertised-prefixes/create)
    
    
    [gcloud preview compute public-advertised-prefixes create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/public-advertised-prefixes/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
