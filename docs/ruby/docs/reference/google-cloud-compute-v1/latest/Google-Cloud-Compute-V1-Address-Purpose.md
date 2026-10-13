---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Address-Purpose/
title: Google Cloud Compute V1 API - Module Google::Cloud::Compute::V1::Address::Purpose (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:24:15.521311+00:00
---

# Google Cloud Compute V1 API - Module Google::Cloud::Compute::V1::Address::Purpose (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Address-Purpose/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Module Google::Cloud::Compute::V1::Address::Purpose (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API module Google::Cloud::Compute::V1::Address::Purpose.

The purpose of this resource, which can be one of the following values:
    
    
     - GCE_ENDPOINT for addresses that are used by VM
     instances, alias IP ranges, load balancers, and similar resources.
     - DNS_RESOLVER for a DNS resolver address in a subnetwork
       for a Cloud DNS  inbound
       forwarder IP addresses (regional internal IP address in a subnet of
       a VPC network)
     - VPC_PEERING for global internal IP addresses used for
    
          private services access allocated ranges.
     - NAT_AUTO for the regional external IP addresses used by
          Cloud NAT when allocating addresses using
    
          automatic NAT IP address allocation.
     - IPSEC_INTERCONNECT for addresses created from a private
     IP range that are reserved for a VLAN attachment in an
     *HA VPN over Cloud Interconnect* configuration. These addresses
     are regional resources.
     - `SHARED_LOADBALANCER_VIP` for an internal IP address that is assigned
     to multiple internal forwarding rules.
     - `PRIVATE_SERVICE_CONNECT` for a private network address that is
     used to configure Private Service Connect. Only global internal addresses
     can use this purpose.
     - `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0` for addresses
     that can only be assigned to global external Passthrough Network Load
     Balancer forwarding rules, as an Availability Group 0 address.
     - `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP1` for addresses that
     can only be assigned to global external Passthrough Network Load Balancer
     forwarding rules, as an Availability Group 1 address.
    

## Constants 

### UNDEFINED_PURPOSE

**value:** 0  
A value indicating that the enum field is not set.

### DNS_RESOLVER

**value:** 476_114_556  
DNS resolver address in the subnetwork.

### GCE_ENDPOINT

**value:** 230_515_243  
VM internal/alias IP, Internal LB service IP, etc.

### IPSEC_INTERCONNECT

**value:** 340_437_251  
A regional internal IP address range reserved for the VLAN attachment that is used in HA VPN over Cloud Interconnect. This regional internal IP address range must not overlap with any IP address range of subnet/route in the VPC network and its peering networks. After the VLAN attachment is created with the reserved IP address range, when creating a new VPN gateway, its interface IP address is allocated from the associated VLAN attachment's IP address range.

### NAT_AUTO

**value:** 163_666_477  
External IP automatically reserved for Cloud NAT.

### PRIVATE_SERVICE_CONNECT

**value:** 48_134_724  
A private network IP address that can be used to configure Private Service Connect. This purpose can be specified only forGLOBAL addresses of Type INTERNAL

### SERVERLESS

**value:** 270_492_508  
A regional internal IP address range reserved for Serverless.

### SHARED_LOADBALANCER_VIP

**value:** 294_447_572  
A private network IP address that can be shared by multiple Internal Load Balancer forwarding rules.

### VPC_PEERING

**value:** 400_800_170  
IP range for peer networks.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
