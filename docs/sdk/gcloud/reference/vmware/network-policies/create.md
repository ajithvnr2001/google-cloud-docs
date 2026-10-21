---
url: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/network-policies/create/
title: gcloud vmware network-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:49:56.031567+00:00
---

# gcloud vmware network-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/vmware/network-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud vmware network-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud vmware network-policies create - create a VMware Engine network policy 
SYNOPSIS
    

`gcloud vmware network-policies create` (`NETWORK_POLICY` : `--location`=`LOCATION`) `--edge-services-cidr`=`EDGE_SERVICES_CIDR` `--vmware-engine-network`=`VMWARE_ENGINE_NETWORK` [`--async`] [`--description`=`DESCRIPTION`] [`--external-ip-access`] [`--internet-access`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a VMware Engine network policy. Only one network policy applies to a VMware Engine network per region. Check the progress of a network policy creation using `[gcloud vmware network-policies list](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/network-policies/list)`. 
EXAMPLES
     To create a network policy called `my-network-policy` which connects to the VMware Engine network `my-vmware-engine-network` using the edge services address range `192.168.0.0/26` with the internet access service enabled and the external IP access service disabled, run: 
    
    
    gcloud vmware network-policies create my-network-policy --location=us-west2 --project=my-project --vmware-engine-network=my-vmware-engine-network --edge-services-cidr=192.168.0.0/26 --internet-access --no-external-ip-access

Or: 
    
    
    gcloud vmware network-policies create my-network-policy --vmware-engine-network=my-vmware-engine-network --edge-services-cidr=192.168.0.0/26 --internet-access

In the second example, the project and the location are taken from gcloud properties core/project and compute/region respectively. If the `--external-ip-access` flag is not specified, it is taken as `False`. 

POSITIONAL ARGUMENTS
    

VMware Engine Network Policy resource - network_policy. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `network_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`NETWORK_POLICY`
     ID of the VMware Engine Network Policy or fully qualified identifier for the VMware Engine Network Policy. 

To set the `network-policy` attribute: 

  * provide the argument `network_policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The resource name of the location. 

To set the `location` attribute: 

  * provide the argument `network_policy` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `compute/region`. 


REQUIRED FLAGS
    

`--edge-services-cidr`=`EDGE_SERVICES_CIDR`
     IP address range to use for internet access and external IP access gateways, in CIDR notation. An RFC 1918 CIDR block with a "/26" prefix is required. 
`--vmware-engine-network`=`VMWARE_ENGINE_NETWORK`
     Resource ID of the VMware Engine network to attach the new policy to. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--description`=`DESCRIPTION`
     User-provided description of the network policy. 
`--external-ip-access`
     Enable or disable network service that allows external IP addresses to be assigned to VMware workloads. To enable this service, `internet-access` must also be enabled. Use `--no-external-ip-access` to disable. If the flag is not provided, access to VMware workloads through external IP addresses is disabled. 
`--internet-access`
     Enable or disable network service that allows VMware workloads to access the internet. Use `--no-internet-access` to disable. If the flag is not provided, internet access is disabled. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
