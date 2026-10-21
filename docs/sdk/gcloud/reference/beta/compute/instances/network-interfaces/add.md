---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/network-interfaces/add/
title: gcloud beta compute instances network-interfaces add \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:59:55.830621+00:00
---

# gcloud beta compute instances network-interfaces add  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/network-interfaces/add/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute instances network-interfaces add Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute instances network-interfaces add - add a Dynamic Network Interface to a Compute Engine instance 
SYNOPSIS
    

`gcloud beta compute instances network-interfaces add` `INSTANCE_NAME` [`--aliases`=`ALIASES`] [`--external-ipv6-address`=`EXTERNAL_IPV6_ADDRESS`] [`--external-ipv6-prefix-length`=`EXTERNAL_IPV6_PREFIX_LENGTH`] [`--igmp-query`=`IGMP_QUERY`] [`--internal-ipv6-address`=`INTERNAL_IPV6_ADDRESS`] [`--internal-ipv6-prefix-length`=`INTERNAL_IPV6_PREFIX_LENGTH`] [`--ipv6-aliases`=`IPV6_ALIASES`] [`--ipv6-network-tier`=`IPV6_NETWORK_TIER`] [`--network`=`NETWORK`] [`--network-attachment`=`NETWORK_ATTACHMENT`] [`--network-tier`=`NETWORK_TIER`] [`--parent-nic-name`=`PARENT_NIC_NAME`] [`--private-network-ip`=`PRIVATE_NETWORK_IP`] [`--service-class-id`=`SERVICE_CLASS_ID`] [`--stack-type`=`STACK_TYPE`] [`--subnetwork`=`SUBNETWORK`] [`--vlan`=`VLAN`] [`--zone`=`ZONE`] [`--address`=`ADDRESS` | `--no-address`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute instances network-interfaces add` adds a Dynamic Network Interface to a Compute Engine instance. 
EXAMPLES
     To add a Dynamic Network Interface to a Compute Engine instance, run:
    
    
    gcloud beta compute instances network-interfaces add instance-name --parent-nic-name=nic1 --vlan=2 --network=network-1 --subnetwork=subnetwork-1

POSITIONAL ARGUMENTS
    

`INSTANCE_NAME`
     Name of the instance to operate on. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
FLAGS
    

`--aliases`=`ALIASES`
     The IP alias ranges to allocate for this interface. If there are multiple IP alias ranges, they are separated by semicolons. 

For example: 
    
    
    --aliases="10.128.1.0/24;range1:/32"

Each IP alias range consists of a range name and an IP range separated by a colon, or just the IP range. The range name is the name of the range within the network interface's subnet from which to allocate an IP alias range. If unspecified, it defaults to the primary IP range of the subnet. The IP range can be a CIDR range (e.g. `192.168.100.0/24`), a single IP address (e.g. `192.168.100.1`), or a netmask in CIDR format (e.g. `/24`). If the IP range is specified by CIDR range or single IP address, it must belong to the CIDR range specified by the range name on the subnet. If the IP range is specified by netmask, the IP allocator will pick an available range with the specified netmask and allocate it to this network interface. 

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
`--ipv6-aliases`=`IPV6_ALIASES`
     The IPv6 alias ranges to allocate for this interface. If there are multiple IPv6 alias ranges, they are separated by semicolons. 

For example: 
    
    
    --ipv6-aliases="2001:db8:1234::/80;range1=/96"

Each IPv6 alias range consists of an optional range name and an IPv6 range separated by an equal sign, or just the IPv6 range. The range name is the name of the range within the network interface's subnet from which to allocate an IPv6 alias range. If unspecified, it defaults to the primary IPv6 range of the subnet. The IPv6 range can be a CIDR range (e.g. `2001:db8:abcd::/80`) or a prefix length (e.g. `/96`). 

`--ipv6-network-tier`=`IPV6_NETWORK_TIER`
     Specifies the IPv6 network tier that will be used to configure the instance network interface IPv6 access config. `IPV6_NETWORK_TIER` must be one of: 

`PREMIUM`
     High quality, Google-grade network tier. 
`STANDARD`
     Standard quality network tier. 
`--network`=`NETWORK`
     Specifies the network this network interface belongs to. 
`--network-attachment`=`NETWORK_ATTACHMENT`
     The network attachment URL this network interface should connect to. 
`--network-tier`=`NETWORK_TIER`
     Specifies the network tier that will be used to configure the instance network interface. ``NETWORK_TIER`` must be one of: `PREMIUM`, `STANDARD`, `FIXED_STANDARD`. The default value is `PREMIUM`. `NETWORK_TIER` must be one of: 

`FIXED_STANDARD`
     Public internet quality with fixed bandwidth. 
`PREMIUM`
     High quality, Google-grade network tier. 
`STANDARD`
     Public internet quality. 
`--parent-nic-name`=`PARENT_NIC_NAME`
     Name of the parent network interface of a dynamic network interface. 
`--private-network-ip`=`PRIVATE_NETWORK_IP`
     Specifies the RFC1918 IP to assign to the network interface. The IP should be in the subnet IP range. 
`--service-class-id`=`SERVICE_CLASS_ID`
     The regional Service Class ID for the producer service associated with this network interface. Can only be used with network_attachment. It is not possible to use on its own; however, network_attachment can be used without service_class_id. 
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
`--vlan`=`VLAN`
     VLAN tag of a dynamic network interface, must be an integer in the range from 2 to 255 inclusively. 
`--zone`=`ZONE`
     Zone of the instance to operate on. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

To avoid prompting when this flag is omitted, the user can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

At most one of these can be specified: 

`--address`=`ADDRESS`
     Assigns the given external address to the network interface. The address might be an IP address or the name or URI of an address resource. Specifying an empty string will assign an ephemeral IP. Mutually exclusive with no-address. If neither key is present the network interface will get an ephemeral IP. 
`--no-address`
     If specified the network interface will have no external IP. Mutually exclusive with address. If neither key is present the network interfaces will get an ephemeral IP. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute instances network-interfaces add](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/add)
    
    
    [gcloud alpha compute instances network-interfaces add](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/add)
    
    
    [gcloud preview compute instances network-interfaces add](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/network-interfaces/add)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
