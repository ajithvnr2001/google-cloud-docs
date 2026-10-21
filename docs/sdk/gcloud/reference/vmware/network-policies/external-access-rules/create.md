---
url: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create/
title: gcloud vmware network-policies external-access-rules create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:49:57.001786+00:00
---

# gcloud vmware network-policies external-access-rules create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud vmware network-policies external-access-rules create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud vmware network-policies external-access-rules create - create a VMware Engine external access firewall rule 
SYNOPSIS
    

`gcloud vmware network-policies external-access-rules create` (`EXTERNAL_ACCESS_RULE` : `--location`=`LOCATION` `--network-policy`=`NETWORK_POLICY`) `--destination-ranges`=`DESTINATION_IP_RANGES`,[…] `--ip-protocol`=`IP_PROTOCOL` `--priority`=`PRIORITY` `--source-ranges`=`SOURCE_IP_RANGES`,[…] [`--action`=`ACTION`; default="ALLOW"] [`--async`] [`--description`=`DESCRIPTION`] [`--destination-ports`=`DESTINATION_PORTS`,[…]] [`--source-ports`=`SOURCE_PORTS`,[…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a VMware Engine external access firewall rule. Check the progress of a VMware Engine external access firewall rule creation using `[gcloud vmware network-policies external-access-rules list](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/network-policies/external-access-rules/list)`. 
EXAMPLES
     To create an external access firewall rule called `my-external-access-rule` associated with the network policy `my-network-policy` in the `us-west2` region, run: 
    
    
    gcloud vmware network-policies external-access-rules create my-external-access-rule --network-policy=my-network-policy --priority=1000 --ip-protocol=TCP --source-ranges=34.148.30.114/32 --destination-ranges=projects/sample-project/locations/us-west2-a/privateClouds/my-private-cloud/externalAddresses/my-external-address --source-ports=22,10000-11000 --destination-ports=22 --action=ALLOW --location=us-west2 --project=sample-project

Or: 
    
    
    gcloud vmware network-policies external-access-rules create my-external-access-rule --network-policy=my-network-policy --priority=1000 --ip-protocol=TCP --source-ranges=34.148.30.114/32 --destination-ranges=projects/sample-project/locations/us-west2-a/privateClouds/my-private-cloud/externalAddresses/my-external-address --source-ports=22,10000-11000 --destination-ports=22

In the second example, the project and the location are taken from gcloud properties core/project and compute/region respectively. The `--action` field also isn't specified, so its value defaults to `ALLOW`. 

POSITIONAL ARGUMENTS
    

VMware Engine External Access Rule resource - external_access_rule. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `external_access_rule` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`EXTERNAL_ACCESS_RULE`
     ID of the VMware Engine External Access Rule or fully qualified identifier for the VMware Engine External Access Rule. 

To set the `external-access-rule` attribute: 

  * provide the argument `external_access_rule` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The resource name of the location. 

To set the `location` attribute: 

  * provide the argument `external_access_rule` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `compute/region`. 


`--network-policy`=`NETWORK_POLICY`
     VMware Engine network policy 

To set the `network-policy` attribute: 

  * provide the argument `external_access_rule` on the command line with a fully specified name; 
  * provide the argument `--network-policy` on the command line. 


REQUIRED FLAGS
    

`--destination-ranges`=`DESTINATION_IP_RANGES`,[…]
     A list of destination IP addresses that the rule applies to. Each entry in the list can be an ExternalAddress resource name or `0.0.0.0/0`. When the value is set to `0.0.0.0/0`, all IP addresses are allowed. 
`--ip-protocol`=`IP_PROTOCOL`
     Internet protocol covered by the rule. Valid values are TCP, UDP, and ICMP. `IP_PROTOCOL` must be one of: `TCP`, `UDP`, `ICMP`. 
`--priority`=`PRIORITY`
     Priority of this external access rule. Valid values are numbers between 100 and 4096, with 100 being the highest priority. Firewall rules are processed from highest to lowest priority. 
`--source-ranges`=`SOURCE_IP_RANGES`,[…]
     A list of source IP addresses that the rule applies to. Each entry in the list can be a CIDR notation or a single IP address. When the value is set to `0.0.0.0/0`, all IP addresses are allowed. 
OPTIONAL FLAGS
    

`--action`=`ACTION`; default="ALLOW"
     Whether the firewall rule allows or denies traffic based on a successful rule match. By default, the action is ALLOW. `ACTION` must be one of: `ALLOW`, `DENY`. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--description`=`DESCRIPTION`
     User-provided description of the external access rule. 
`--destination-ports`=`DESTINATION_PORTS`,[…]
     List of allowed destination ports. Each entry must be either an integer or a range. 
`--source-ports`=`SOURCE_PORTS`,[…]
     List of allowed source ports. Each entry must be either an integer or a range. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
