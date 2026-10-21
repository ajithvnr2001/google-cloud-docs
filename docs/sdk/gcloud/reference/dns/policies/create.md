---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/create/
title: gcloud dns policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:36:47.976831+00:00
---

# gcloud dns policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dns policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dns policies create - creates a new Cloud DNS policy 
SYNOPSIS
    

`gcloud dns policies create` `POLICY` `--description`=`DESCRIPTION` `--networks`=[`NETWORKS`,…] [`--alternative-name-servers`=[`NAME_SERVERS`,…]] [`--enable-dns64-all-queries`] [`--enable-inbound-forwarding`] [`--enable-logging`] [`--private-alternative-name-servers`=[`NAME_SERVERS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command creates a new Cloud DNS policy. 
EXAMPLES
     To create a new policy with minimal arguments, run: 
    
    
    gcloud dns policies create mypolicy --description='My new policy test policy 5' --networks=''

To create a new policy with all optional arguments, run: 
    
    
    gcloud dns policies create mypolicy --description='My new policy test policy 5' --networks=network1,network2 --alternative-name-servers=192.168.1.1,192.168.1.2 --enable-inbound-forwarding --enable-logging --enable-dns64-all-queries

POSITIONAL ARGUMENTS
    

Policy resource - The policy to create. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `policy` on the command line with a fully specified name; 
  * set the property `core/project`. 



This must be specified. 

`POLICY`
     ID of the policy or fully qualified identifier for the policy. 

To set the `policy` attribute: 

  * provide the argument `policy` on the command line. 


REQUIRED FLAGS
    

`--description`=`DESCRIPTION`
     A description of the policy. 
`--networks`=[`NETWORKS`,…]
     The comma separated list of network names to associate with the policy. 
OPTIONAL FLAGS
    

`--alternative-name-servers`=[`NAME_SERVERS`,…]
     List of alternative name servers to forward to. Non-RFC1918 addresses will forward to the target through the Internet.RFC1918 addresses will forward through the VPC. 
`--enable-dns64-all-queries`
     Specifies whether to allow networks bound to this policy to use DNS64 for IPv6-only VM instances. 
`--enable-inbound-forwarding`
     Specifies whether to allow networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. Defaults to False. 
`--enable-logging`
     Specifies whether to enable query logging. Defaults to False. 
`--private-alternative-name-servers`=[`NAME_SERVERS`,…]
     List of alternative name servers to forward to. All addresses specified for this parameter will be reached through the VPC. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha dns policies create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/policies/create)
    
    
    [gcloud beta dns policies create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
