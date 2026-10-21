---
url: https://docs.cloud.google.com/armor/docs/address-groups-overview/
title: Address groups overview \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:18.965316+00:00
---

# Address groups overview  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/address-groups-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Address groups overview Stay organized with collections  Save and categorize content based on your preferences. 

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

The container type for project-scoped address groups is always set to `project`. For more information about how to create and modify project-scoped address groups, see [Use project-scoped address groups](https://docs.cloud.google.com/armor/docs/address-groups-using#project-scoped-address-group). 

### Organization-scoped address groups

Use organization-scoped address groups when you want to define a central list of IP addresses that can be used in high-level rules to provide consistent control for the entire organization and reduce the overhead for individual network and project owners to maintain common lists, such as trusted services and internal IP addresses. 

The container type for organization-scoped address groups is always set to `organization`. For more information about how to create and modify organization-scoped address groups, see [Use organization-scoped address groups](https://docs.cloud.google.com/armor/docs/address-groups-using#organization-scoped-address-group). 

## How address groups work with security policies

Address groups simplify the configuration and maintenance of security policies because you can share each list of IP addresses across many security policies. Consider the following additional specifications when you use address groups with security policies:

  * Address groups are only available for globally scoped [backend security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#backend-policies).
  * Organization-scoped address groups are available for both service-level security policies and hierarchical security policies.
  * The capacity of an address group is added to the total attribute count of the security policy where the address group is used. Make sure that you set the capacity to an appropriate value based on your use case.
  * To use address groups, your project must be enrolled in [Google Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview). If you downgrade to standard billing, you can't create new address groups or modify existing address groups. You also can't create rules that reference an existing address group, and your security policies that reference address groups are frozen. This means that they are still active, but that you can't modify them until you delete all of the rules that reference an address group.



We recommend that you view the [quotas](https://docs.cloud.google.com/armor/quotas#address-group-quotas) and [limits](https://docs.cloud.google.com/armor/quotas#address-group-limits) for address groups.

In addition to configuring organization-scoped address groups for your backend security policies, you can configure organization-scoped address groups for your hierarchical security policies. You can't use project-scoped address groups in any security policies outside of the project in which they exist, but you can share organization-scoped address groups with security policies across your entire organization; this makes organization-scoped address groups with security policies especially helpful when you use them with hierarchical security policies. For more information about hierarchical security policies, see the [Hierarchical security policies overview](https://docs.cloud.google.com/armor/docs/hierarchical-policies-overview).

### Examples

The following examples demonstrate how you might use address groups to help you configure security policies:

  * Imagine that you have a network configuration in which you have three backend services, each of which has one security policy. In addition, you have a list of IP addresses that you know are malicious. When you create a `deny` rule in each security policy, you can create one address group and use it with all three security policies instead of adding the list of IP addresses to each security policy. Then, whenever you create a new security policy, you can use the address group again to make new rules.
  * Imagine that you have an organization with many projects that are grouped into folders, and you have three lists of IP addresses that each need access to only some of these folders. You can create three organization-scoped address groups, one for each list of IP addresses, and then create three hierarchical security policies. You can give each hierarchical security policy an `allow` rule that matches on one of the three address groups, then associate the hierarchical security policy with each folder that the allowed IP address group needs to access.



## What's next

  * [Configure address groups](https://docs.cloud.google.com/armor/docs/address-groups-using).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
