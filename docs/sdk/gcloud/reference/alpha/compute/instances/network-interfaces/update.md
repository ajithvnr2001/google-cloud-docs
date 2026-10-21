---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/update/
title: gcloud alpha compute instances network-interfaces update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:43:07.611439+00:00
---

# gcloud alpha compute instances network-interfaces update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute instances network-interfaces update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute instances network-interfaces update - update a Compute Engine virtual machine network interface 
SYNOPSIS
    

`gcloud alpha compute instances network-interfaces update` `INSTANCE_NAME` [`--aliases`=`ALIASES`] [`--[no-]dns64-eligible`] [`--external-ipv6-address`=`EXTERNAL_IPV6_ADDRESS`] [`--external-ipv6-prefix-length`=`EXTERNAL_IPV6_PREFIX_LENGTH`] [`--igmp-query`=`IGMP_QUERY`] [`--internal-ipv6-address`=`INTERNAL_IPV6_ADDRESS`] [`--internal-ipv6-prefix-length`=`INTERNAL_IPV6_PREFIX_LENGTH`] [`--ipv6-address`=`IPV6_ADDRESS`] [`--ipv6-aliases`=`IPV6_ALIASES`] [`--ipv6-network-tier`=`IPV6_NETWORK_TIER`] [`--ipv6-prefix-length`=`IPV6_PREFIX_LENGTH`] [`--[no-]nat64-eligible`] [`--network`=`NETWORK`] [`--network-interface`=`NETWORK_INTERFACE`; default="nic0"] [`--private-network-ip`=`PRIVATE_NETWORK_IP`] [`--security-policy`=`SECURITY_POLICY`] [`--security-policy-region`=`SECURITY_POLICY_REGION`] [`--stack-type`=`STACK_TYPE`] [`--subnetwork`=`SUBNETWORK`] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute instances network-interfaces update` updates network interfaces of a Compute Engine virtual machine. For example: 
    
    
    gcloud alpha compute instances network-interfaces update example-instance --zone us-central1-a --aliases r1:172.16.0.1/32

sets 172.16.0.1/32 from range r1 of the default interface's subnetwork as the interface's alias IP. 

POSITIONAL ARGUMENTS
    

`INSTANCE_NAME`
     Name of the instance to operate on. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
FLAGS
    

`--aliases`=`ALIASES`
     The IP alias ranges to allocate for this interface. If there are multiple IP alias ranges, they are separated by semicolons. 

Can be specified together with --network and/or --subnetwork to choose IP alias ranges in the new subnetwork. If unspecified, then the previous IP alias ranges will be allocated in the new subnetwork. If the previous IP alias ranges are not available in the new subnetwork, then other available IP alias ranges of the same size will be allocated in the new subnetwork. 

For example: 
    
    
    --aliases="10.128.1.0/24;r1:/32"

`--[no-]dns64-eligible`
     If specified, indicates that this network interface is eligible for DNS64. Use `--dns64-eligible` to enable and `--no-dns64-eligible` to disable. 
`--external-ipv6-address`=`EXTERNAL_IPV6_ADDRESS`
     Assigns the given external IPv6 address to an instance. The address must be the first IP in the range. This option is not applicable to instances with stack-type=IPV4_ONLY. 
`--external-ipv6-prefix-length`=`EXTERNAL_IPV6_PREFIX_LENGTH`
     The prefix length of the external IPv6 address range. This flag should be used together with `--external-ipv6-address`. Currently only `/96` is supported and the default value is `96`. 
`--igmp-query`=`IGMP_QUERY`
     Determines if the Compute Engine instance can receive and respond to IGMP query packets on the specified network interface. `IGMP_QUERY` must be one of: 

`IGMP_QUERY_DISABLED`
     IGMP Query on the network interface is disabled. 
`IGMP_QUERY_V2`
     IGMP Query V2 on the network interface is enabled. 
`--internal-ipv6-address`=`INTERNAL_IPV6_ADDRESS`
     Assigns the given internal IPv6 address or range to an instance. The address must be the first IP address in the range or a /96 IP address range. This option can only be used on a dual stack instance network interface. 
`--internal-ipv6-prefix-length`=`INTERNAL_IPV6_PREFIX_LENGTH`
     Optional field that indicates the prefix length of the internal IPv6 address range, should be used together with `--internal-ipv6-address=fd20::`. Only /96 IP address range is supported and the default value is 96. If not set, then either the prefix length from `--internal-ipv6-address=fd20::/96` will be used or the default value of 96 will be assigned. 
`--ipv6-address`=`IPV6_ADDRESS`
     Assigns the given external IPv6 address to an instance. The address must be the first IP in the range. This option is applicable only to dual-stack instances with stack-type=IPV4_ONLY. 
`--ipv6-aliases`=`IPV6_ALIASES`
     The IPv6 alias ranges to allocate for this interface. If there are multiple IPv6 alias ranges, they are separated by semicolons. 

For example: 
    
    
    --ipv6-aliases="2001:db8:abcd::/80;r1=/96"

`--ipv6-network-tier`=`IPV6_NETWORK_TIER`
     Specifies the IPv6 network tier that will be used to configure the instance network interface IPv6 access config. `IPV6_NETWORK_TIER` must be one of: 

`PREMIUM`
     High quality, Google-grade network tier. 
`STANDARD`
     Standard quality network tier. 
`--ipv6-prefix-length`=`IPV6_PREFIX_LENGTH`
     The prefix length of the external IPv6 address range. This flag should be used together with `--ipv6-address`. Currently only `/96` is supported and the default value is `96`. 
`--[no-]nat64-eligible`
     If specified, indicates that this network interface is eligible for NAT64. Use `--nat64-eligible` to enable and `--no-nat64-eligible` to disable. 
`--network`=`NETWORK`
     Specifies the network this network interface belongs to. 
`--network-interface`=`NETWORK_INTERFACE`; default="nic0"
     The name of the network interface to update. 
`--private-network-ip`=`PRIVATE_NETWORK_IP`
     Assign the given IP address to the interface. Can be specified only together with --network and/or --subnetwork to choose the IP address in the new subnetwork. If unspecified, then the previous IP address will be allocated in the new subnetwork. If the previous IP address is not available in the new subnetwork, then another available IP address will be allocated automatically from the new subnetwork CIDR range. 
`--security-policy`=`SECURITY_POLICY`
     The security policy that will be set for this instance network interface. To remove the policy from this instance network interface set the policy to an empty string. 
`--security-policy-region`=`SECURITY_POLICY_REGION`
     Region of the security policy to operate on. Overrides the default `compute/region` property value for this command invocation. 
`--stack-type`=`STACK_TYPE`
     The stack type for the network interface. Determines if IPv6 is enabled on the network interface. `STACK_TYPE` must be one of: 

`IPV4_IPV6`
     The network interface can have both IPv4 and IPv6 addresses. 
`IPV4_ONLY`
     The network interface will be assigned IPv4 addresses. 
`IPV6_ONLY`
     The network interface will be assigned IPv6 addresses. 
`--subnetwork`=`SUBNETWORK`
     Specifies the subnetwork this network interface belongs to. 
`--zone`=`ZONE`
     Zone of the instance to operate on. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

To avoid prompting when this flag is omitted, the user can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute instances network-interfaces update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/update)
    
    
    [gcloud beta compute instances network-interfaces update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/network-interfaces/update)
    
    
    [gcloud preview compute instances network-interfaces update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/network-interfaces/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
