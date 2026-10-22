---
url: https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies/
title: Address groups for firewall policies \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:29.500945+00:00
---

# Address groups for firewall policies  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Address groups for firewall policies Stay organized with collections  Save and categorize content based on your preferences. 

An _address group_ contains multiple IP addresses, IP address ranges in CIDR format, or both. Each address group can be used by multiple resources, such as rules in Cloud NGFW firewall policies or rules in Cloud Armor security policies.

Updates to an address group are automatically propagated to the resources that reference the address group. For example, you can create an address group containing a set of trusted IP addresses. To change the set of trusted IP addresses, you update the address group. Your updates to the address group are reflected in each associated resource automatically.

## Specifications

Address group resources have the following characteristics:

  * Each address group is uniquely identified by a URL with the following elements: 
    * **Container type:** Determines the address group type—`organization` or `project`.
    * **Container ID:** ID of the organization or the project.
    * **Location:** Specifies if the address group is a `global` or regional resource (such as `europe-west`).
    * **Name:** The address group name with the following format: 
      * A string 1-63 characters long
      * Includes only alphanumeric characters
      * Must not start with a number
  * You can construct a unique URL identifier for an address group in the following format:
        
        <containerType>/<containerId>/locations/<location>/addressGroups/<address-group-name>
        

For example, a `global` address group `example-address-group` in project `myproject`has the following unique 4-tuple identifier:
        
        projects/myproject/locations/global/addressGroups/example-address-group
        

  * Each address group has an associated type that can be either IPv4 or IPv6, but not both. The address group type cannot be changed later.

  * Each IP address or IP range in an address group is referred to as an _item_. The number of items that you can add to an address group depends on the address group's capacity. You can define the item capacity during address group creation. This capacity cannot be changed later. The maximum capacity that you can configure for an address group varies depending on the product with which you use the address group.

  * You must specify the capacity and type when you create an address group. In addition, when you use Cloud Armor, you must set the `purpose` field to `CLOUD_ARMOR`.

  * When you create an address group with a purpose that is _not_ `CLOUD_ARMOR`, the address group has a maximum capacity of 1,000 IP addresses.




## Types of address groups

Address groups are classified based on their scope. The scope identifies the level at which the address group is applicable in the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). Address groups are categorized into the following types:

  * Project-scoped address groups
  * Organization-scoped address groups



An address group can be either project-scoped or organization-scoped, but not both.

### Project-scoped address groups

Use project-scoped address groups when you want to define your own list of IP addresses to be used within a project or a network to block or allow a list of changing IP addresses. For example, if you want to define your own threat intelligence list and add it to a rule, create an address group with the required IP addresses.

The container type for project-scoped address groups is always set to `project`. For more information about how to create and modify project-scoped address groups, see [Use project-scoped address groups](https://docs.cloud.google.com/firewall/docs/use-address-groups-firewall-policies#project-scoped-address-group). 

### Organization-scoped address groups

Use organization-scoped address groups when you want to define a central list of IP addresses that can be used in high-level rules to provide consistent control for the entire organization and reduce the overhead for individual network and project owners to maintain common lists, such as trusted services and internal IP addresses. 

The container type for organization-scoped address groups is always set to `organization`. For more information about how to create and modify organization-scoped address groups, see [Use organization-scoped address groups](https://docs.cloud.google.com/firewall/docs/use-address-groups-firewall-policies#organization-scoped-address-group). 

## IAM roles

To create and manage an address group, you need the Compute Network Admin role (`roles/compute.networkAdmin`). You can also define a custom role with an equivalent set of permissions.

The following table provides a list of Identity and Access Management (IAM) permissions required to perform a set of tasks on address groups.

Task | IAM role name | IAM permissions  
---|---|---  
Create and manage address groups | Compute Network Admin (`roles/compute.networkAdmin`) | 
    
    
    networksecurity.addressGroups.*
      
  
Discover and view address groups | Compute Network User (`roles/compute.networkUser`) | 
    
    
    networksecurity.addressGroups.list
    networksecurity.addressGroups.get
    networksecurity.addressGroups.use
      
  
For more information about which roles include specific IAM permissions, see the [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/permissions-reference).

## How address groups work with firewall policies

Address groups simplify the configuration and maintenance of firewall policies. You can share the IP addresses across firewall policies and define more complex, consistent, and robust firewall policies for your network with reduced maintenance overhead. Consider the following additional specifications when you use address groups with firewall policies:

  * The capacity of an address group gets added to the total attribute count of the firewall policy where the address group is used. Make sure that you set the capacity to an appropriate value based on your use case.

  * If an address group added to the firewall policy rule does not exist, the address group filter is removed from the rule. For information about how source address groups work with other source filters in the ingress rules, see [Sources for ingress rules in hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-ingress-src) and [Sources for ingress rules in network firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#nfp-ingress-src). For information about how destination address groups work with other destination filters in the egress rules, see [Destinations for egress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-egress-dest).

  * Organization-scoped address groups can be used in [hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#rule_tasks), [global network firewall policies](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#add_rules), and [regional network firewall policies](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#rule_tasks). Project-scoped address groups can only be used in [global network firewall policies](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#add_rules) and [regional network firewall policies](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#rule_tasks).

  * For both project-scoped and organization-scoped address groups, the location of the address group must match with the location of the firewall policy.




## What's next

  * [Create address groups for firewall policies](https://docs.cloud.google.com/firewall/docs/create-address-groups-firewall-policies)
  * [Manage address groups for firewall policies](https://docs.cloud.google.com/firewall/docs/use-address-groups-firewall-policies)
  * [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details)
  * [Google Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview)
  * [Fully qualified domain name objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
