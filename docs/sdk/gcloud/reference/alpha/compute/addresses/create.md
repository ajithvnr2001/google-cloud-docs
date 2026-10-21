---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/create/
title: gcloud alpha compute addresses create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:19.075540+00:00
---

# gcloud alpha compute addresses create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute addresses create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute addresses create - reserve IP addresses 
SYNOPSIS
    

`gcloud alpha compute addresses create` [`NAME` …] [`--description`=`DESCRIPTION`] [`--endpoint-type`=`ENDPOINT_TYPE`] [`--network`=`NETWORK`] [`--network-tier`=`NETWORK_TIER`] [`--prefix-length`=`PREFIX_LENGTH`] [`--purpose`=`PURPOSE`] [`--subnet`=`SUBNET`] [`--addresses`=`ADDRESS`,[`ADDRESS`,…] | `--ip-version`=`IP_VERSION`] [`--global` | `--region`=`REGION`] [`--internal-range`=`INTERNAL_RANGE` | `--ip-collection`=`IP_COLLECTION`] [`--network-attachment`=`NETWORK_ATTACHMENT` : `--service-class-id`=`SERVICE_CLASS_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute addresses create` is used to reserve one or more IP addresses. Once an IP address is reserved, it will be associated with the project until it is released using 'gcloud compute addresses delete'. Ephemeral IP addresses that are in use by resources in the project can be reserved using the '--addresses' flag. 
EXAMPLES
     To reserve three IP addresses in the 'us-central1' region, run: 
    
    
    gcloud alpha compute addresses create address-1 address-2 address-3 --region=us-central1

To reserve ephemeral IP addresses '162.222.181.198' and '23.251.146.189' which are being used by virtual machine instances in the 'us-central1' region, run: 
    
    
    gcloud alpha compute addresses create --addresses=162.222.181.198,23.251.146.189 --region=us-central1

In the above invocation, the two addresses will be assigned random names. 

To reserve an IP address named subnet-address-1 from the subnet 'default' in the 'us-central1' region, run: 
    
    
    gcloud alpha compute addresses create subnet-address-1 --region=us-central1 --subnet=default

To reserve an IP address that can be used by multiple internal load balancers from the subnet 'default' in the 'us-central1' region, run: 
    
    
    gcloud alpha compute addresses create shared-address-1 --region=us-central1 --subnet=default --purpose=SHARED_LOADBALANCER_VIP

To reserve an IP range '10.110.0.0/16' from the network 'default' for 'VPC_PEERING', run: 
    
    
    gcloud alpha compute addresses create ip-range-1 --global --addresses=10.110.0.0 --prefix-length=16 --purpose=VPC_PEERING --network=default

To reserve any IP range with prefix length '16' from the network 'default' for 'VPC_PEERING', run: 
    
    
    gcloud alpha compute addresses create ip-range-1 --global --prefix-length=16 --purpose=VPC_PEERING --network=default

To reserve an address from network 'default' for PRIVATE_SERVICE_CONNECT, run: 
    
    
    gcloud alpha compute addresses create psc-address-1 --global --addresses=10.110.0.10 --purpose=PRIVATE_SERVICE_CONNECT --network=default

To reserve an external IPv4 address for global passthrough Network Load Balancer in availability group 0, run: 
    
    
    gcloud alpha compute addresses create gnlb-ipv4-address-0 --global --ip-version=IPV4 --purpose=PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0

To reserve an external IPv6 address for global passthrough Network Load Balancer in availability group 0, run: 
    
    
    gcloud alpha compute addresses create gnlb-ipv6-address-0 --global --ip-version=IPV6 --purpose=PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0

POSITIONAL ARGUMENTS
    

[`NAME` …]
     Names of the addresses to create. 
FLAGS
    

`--description`=`DESCRIPTION`
     An optional textual description for the addresses. 
`--endpoint-type`=`ENDPOINT_TYPE`
     The endpoint type of the external IPv6 address to be reserved. `ENDPOINT_TYPE` must be one of: `VM`, `NETLB`. 
`--network`=`NETWORK`
     If specified, the network resource in which the address(es) should be reserved. 

This is only available for global internal address, which represents an internal IP range reservation from within the network. 

`--network-tier`=`NETWORK_TIER`
     The network tier to assign to the reserved IP addresses. ``NETWORK_TIER`` must be one of: `PREMIUM`, `STANDARD`. The default value is `PREMIUM`. 

While regional external addresses (`--region` specified, `--subnet` omitted) can use either `PREMIUM` or `STANDARD`, global external addresses (`--global` specified, `--subnet` omitted) can only use `PREMIUM`. Internal addresses can only use `PREMIUM`. 

`--prefix-length`=`PREFIX_LENGTH`
     The prefix length of the IP range. If the address is an IPv4 address, it must be a value between 8 and 30 inclusive. If the address is an IPv6 address, the only allowed value is 96. If not present, it means the address field is a single IP address. 

This field is not applicable to external IPv4 addresses or global IPv6 addresses. 

`--purpose`=`PURPOSE`
     The purpose of the address resource. VPC_PEERING, SHARED_LOADBALANCER_VIP, GCE_ENDPOINT, IPSEC_INTERCONNECT, and PRIVATE_SERVICE_CONNECT are only applicable to internal addresses. PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0 and PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP1 are only applicable to global external addresses. `PURPOSE` must be one of: `VPC_PEERING`, `SHARED_LOADBALANCER_VIP`, `GCE_ENDPOINT`, `IPSEC_INTERCONNECT`, `PRIVATE_SERVICE_CONNECT`, `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0`, `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP1`. 
`--subnet`=`SUBNET`
     If specified, the subnet name in which the address(es) should be reserved. The subnet must be in the same region as the address. 

The address will represent an internal IP reservation from within the subnet. If \--address is specified, it must be within the subnet's IP range. 

May not be specified with --global. 

At most one of these can be specified: 

`--addresses`=`ADDRESS`,[`ADDRESS`,…]
     Ephemeral IP addresses to promote to reserved status. Only addresses that are being used by resources in the project can be promoted. When providing this flag, a parallel list of names for the addresses can be provided. For example, 
    
    
    gcloud alpha compute addresses create ADDRESS-1 ADDRESS-2        --addresses 162.222.181.197,162.222.181.198             --region us-central1

will result in 162.222.181.197 being reserved as 'ADDRESS-1' and 162.222.181.198 as 'ADDRESS-2'. If no names are given, server-generated names will be assigned to the IP addresses. 

`--ip-version`=`IP_VERSION`
     Version of the IP address to be allocated and reserved. The default is IPV4. 

IP version can only be specified for global addresses that are generated automatically (i.e., along with the `--global` flag, given `--addresses` is not specified) and if the `--network-tier` is `PREMIUM`. 

`IP_VERSION` must be one of: `IPV4`, `IPV6`. 

At most one of these can be specified: 

`--global`
     If set, the addresses are global. 
`--region`=`REGION`
     Region of the addresses to create. Overrides the default `compute/region` property value for this command invocation. 
At most one of these can be specified: 

`--internal-range`=`INTERNAL_RANGE`
     If specified, the internal range from which to allocate the global internal IP address. 
`--ip-collection`=`IP_COLLECTION`
     If specified, the public delegated prefix (PDP) from which to allocate the BYOIP IP address. If an IPv4 PDP is used, the PDP must support enhanced IPv4 allocations. If an IPv6 PDP is used, the PDP must be in EXTERNAL_IPV6_FORWARDING_RULE_CREATION mode. If not specified, the address will be allocated from the Google-owned IP pool. 
Flags for reserving an address with a network attachment. 
`--network-attachment`=`NETWORK_ATTACHMENT`
     Regional network attachment resource in which the address(es) should be reserved. 

This is used to reserve an internal IP address for a PSC interface. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--service-class-id`=`SERVICE_CLASS_ID`
     Regional Service Class ID of the producer service associated with the address. 

This is used in conjunction with `--network-attachment` to authorize address reservation based on the service class. Can only be specified if `--network-attachment` is also specified. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute addresses create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create)
    
    
    [gcloud beta compute addresses create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/addresses/create)
    
    
    [gcloud preview compute addresses create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/addresses/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
