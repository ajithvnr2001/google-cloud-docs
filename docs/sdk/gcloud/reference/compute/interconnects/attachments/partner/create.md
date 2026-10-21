---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create/
title: gcloud compute interconnects attachments partner create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:23:12.279860+00:00
---

# gcloud compute interconnects attachments partner create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/partner/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute interconnects attachments partner create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute interconnects attachments partner create - create a Compute Engine partner interconnect attachment 
SYNOPSIS
    

`gcloud compute interconnects attachments partner create` `NAME` `--edge-availability-domain`=`AVAILABILITY_DOMAIN` `--router`=`ROUTER` [`--candidate-cloud-router-ip-address`=`CANDIDATE_CLOUD_ROUTER_IP_ADDRESS`] [`--candidate-cloud-router-ipv6-address`=`CANDIDATE_CLOUD_ROUTER_IPV6_ADDRESS`] [`--candidate-customer-router-ip-address`=`CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS`] [`--candidate-customer-router-ipv6-address`=`CANDIDATE_CUSTOMER_ROUTER_IPV6_ADDRESS`] [`--description`=`DESCRIPTION`] [`--enable-admin`] [`--encryption`=`ENCRYPTION`] [`--ipsec-internal-addresses`=[`ADDRESSES`]] [`--mtu`=`MTU`] [`--region`=`REGION`] [`--resource-manager-tags`=[`KEY`=`VALUE`,…]] [`--stack-type`=`STACK_TYPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute interconnects attachments partner create` is used to create partner interconnect attachments. A partner interconnect attachment binds the underlying connectivity of a provider's Interconnect to a path into and out of the customer's cloud network. 
POSITIONAL ARGUMENTS
    

`NAME`
     Name of the interconnect attachment to create. 
REQUIRED FLAGS
    

`--edge-availability-domain`=`AVAILABILITY_DOMAIN`
     Desired edge availability domain for this attachment: `availability-domain-1`, `availability-domain-2`, `any`. 

In each metro where the Partner can connect to Google, there are two sets of redundant hardware. These sets are described as edge availability domain 1 and 2\. Within a metro, Google will only schedule maintenance in one availability domain at a time. This guarantee does not apply to availability domains outside the metro; Google may perform maintenance in (say) New York availability domain 1 at the same time as Chicago availability domain 1. 

`AVAILABILITY_DOMAIN` must be one of: 

`any`
     Any Availability Domain 
`availability-domain-1`
     Edge Availability Domain 1 
`availability-domain-2`
     Edge Availability Domain 2 
`--router`=`ROUTER`
     Google Cloud Router to use for dynamic routing. 
OPTIONAL FLAGS
    

`--candidate-cloud-router-ip-address`=`CANDIDATE_CLOUD_ROUTER_IP_ADDRESS`
     Single IPv4 address + prefix length to be configured on the cloud router interface for this interconnect attachment. Example: 203.0.113.1/29 
`--candidate-cloud-router-ipv6-address`=`CANDIDATE_CLOUD_ROUTER_IPV6_ADDRESS`
     Single IPv6 address + prefix length to be configured on the cloud router interface for this interconnect attachment. Example: 2001:db8::1/125 
`--candidate-customer-router-ip-address`=`CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS`
     Single IPv4 address + prefix length to be configured on the customer router interface for this interconnect attachment. Example: 203.0.113.2/29 
`--candidate-customer-router-ipv6-address`=`CANDIDATE_CUSTOMER_ROUTER_IPV6_ADDRESS`
     Single IPv6 address + prefix length to be configured on the customer router interface for this interconnect attachment. Example: 2001:db8::2/125 
`--description`=`DESCRIPTION`
     Human-readable plain-text description of attachment. 
`--enable-admin`
     Administrative status of the interconnect attachment. If not provided on creation, defaults to disabled. When this is enabled, the attachment is operational and will carry traffic. Use --no-enable-admin to disable it. 
`--encryption`=`ENCRYPTION`
     Indicates the user-supplied encryption option for this interconnect attachment (VLAN attachment). 

Possible values are: 

`NONE` \- This is the default value, which means the interconnect attachment carries unencrypted traffic. VMs can send traffic to or receive traffic from such interconnect attachment. 

`IPSEC` \- The interconnect attachment carries only traffic that is encrypted by an IPsec device; for example, an HA VPN gateway or third-party IPsec VPN. VMs cannot directly send traffic to or receive traffic from such an interconnect attachment. To use HA VPN over Cloud Interconnect, the interconnect attachment must be created with this option. 

`ENCRYPTION` must be one of: `IPSEC`, `NONE`. 

`--ipsec-internal-addresses`=[`ADDRESSES`]
     List of IP address range names that have been reserved for the interconnect attachment (VLAN attachment). Use this option only for an interconnect attachment that has its encryption option set as IPSEC. Currently only one internal IP address range can be specified for each attachment. When creating an HA VPN gateway for the interconnect attachment, if the attachment is configured to use a regional internal IP address, then the VPN gateway's IP address is allocated from the IP address range specified here. If this field is not specified when creating the interconnect attachment, then when creating any HA VPN gateways for this interconnect attachment, the HA VPN gateway's IP address is allocated from a regional external IP address pool. 
`--mtu`=`MTU`
     Maximum transmission unit (MTU) is the size of the largest IP packet passing through this interconnect attachment. Must be one of 1440, 1460, 1500, or 8896. If not specified, the value will default to 1440. 
`--region`=`REGION`
     Region of the interconnect attachment to create. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--resource-manager-tags`=[`KEY`=`VALUE`,…]
     A comma-separated list of Resource Manager tags to apply to the interconnect. 
`--stack-type`=`STACK_TYPE`
     Stack type of the protocol(s) enabled on this interconnect attachment. `STACK_TYPE` must be one of: 

`IPV4_IPV6`
     Both IPv4 and IPv6 protocols are enabled on this attachment. 
`IPV4_ONLY`
     Only IPv4 protocol is enabled on this attachment. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute interconnects attachments partner create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/partner/create)
    
    
    [gcloud beta compute interconnects attachments partner create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/attachments/partner/create)
    
    
    [gcloud preview compute interconnects attachments partner create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/attachments/partner/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
