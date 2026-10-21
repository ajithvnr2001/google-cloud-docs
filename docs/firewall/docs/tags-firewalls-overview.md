---
url: https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview/
title: Secure tags for firewalls \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:26.691811+00:00
---

# Secure tags for firewalls  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Secure tags for firewalls Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Next Generation Firewall (Cloud NGFW) rules use tags to specify sources and targets. This flexible approach avoids dependence on IP addresses.

## Types of tags

To filter network traffic in firewall rules, Cloud NGFW supports two types of tags:

  * Identity and Access Management (IAM)-governed [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview), also referred to as _secure tags_ , are created and managed in Resource Manager as tag keys and tag values. Secure tag values can be used to specify sources for ingress rules and targets for ingress or egress rules in a hierarchical firewall policy, global network firewall policy, or regional network firewall policy.

  * _Network tags_ are character strings without access controls that can be added to virtual machine (VM) instances or [instance templates](https://docs.cloud.google.com/compute/docs/instance-templates). Network tags can be used to specify sources for ingress Virtual Private Cloud (VPC) firewall rules and targets for ingress or egress VPC firewall rules. Network tags can't be used by rules in a hierarchical firewall policy, global network firewall policy, or regional network firewall policy. For more information about network tags, see [Add network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags).




For more information, see Comparison of secure tags and network tags.

Additionally, you can attach Resource Manager tags directly to Cloud NGFW resources to govern them with services like Identity and Access Management (IAM) and Organization Policy Service. These tags are used exclusively for resource governance; firewall rules don't evaluate them to filter network traffic. For more information about creating and managing tags on firewall resources, see [Create and manage tags for firewall resources](https://docs.cloud.google.com/firewall/docs/tags).

The following section of this page describes secure tags in firewall policies.

## Specifications

Secure tags have the following specifications:

  * **Parent resource** : the parent resource is the resource where the secure tag key is defined. Tag keys can be created in a parent [project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) or an [organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). For more information about creating tag keys, see [Create and manage secure tags](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls).

  * **Purpose and purpose data** : to use a secure tag key with Cloud NGFW, you must set the `purpose` attribute of the tag key to `GCE_FIREWALL`, and you must specify the `purpose-data` attribute:

    * You can set the `purpose-data` attribute of the tag key to `network`, followed by a single VPC network specification.

      * For tag keys with a parent project, if you set the `purpose-data` attribute of the tag key to `network`, the specified VPC network must be located in the same project as the tag key.

      * For tag keys with a parent organization, if you set the `purpose-data` attribute of the tag key to `network`, the specified VPC network must be located in the same organization as the tag key.

    * You can set the `purpose-data` attribute of the tag key to `organization=auto`. This identifies all VPC networks in the organization.

Neither the `purpose` nor the `purpose-data` attribute can be changed after you create a tag key. For more information about how to format the network specification in the `purpose-data` attribute of a tag key, see [Purpose](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys#purpose) in the Resource Manager API documentation.

  * **Structure and format** : a secure tag key can reference up to 1,000 unique tag values. IAM principals with the Tag Administrator role (`roles/resourcemanager.tagAdmin`) create tag keys and tag values for each tag key. For more information about secure tag limits, see [Limits](https://docs.cloud.google.com/firewall/docs/quotas#limits).

  * **Moving projects between organizations** : you can move a project from one organization to another. Before you move a project, detach any tag keys that have a `purpose-data` attribute specifying an organization used in your project from the original organization. If you don't detach the secure tags first, you receive an error message during the move.

  * **Access control** : IAM policies determine which IAM principals can manage and use secure tags:

    * IAM principals with the Tag Administrator role (`roles/resourcemanager.tagAdmin`) can create tag keys and manage their tag values:

      * IAM principals granted the Tag Administrator role (`roles/resourcemanager.tagAdmin`) in the IAM policy of the organization can create tag keys with the organization as their parent.

      * IAM principals granted the Tag Administrator role (`roles/resourcemanager.tagAdmin`) in the IAM policy of the organization, a folder, or a project, can create tag keys with a project as their parent.

    * IAM principals with the Tag User role (`roles/resourcemanager.tagUser`) can bind tag values to VM instances or use tag values in firewall rules of a hierarchical firewall policy, global network firewall policy, or regional network firewall policy.

      * IAM principals granted the Tag User role (`roles/resourcemanager.tagUser`) in the IAM policy of the organization can use tag values from tag keys that have the organization as their parent.

      * IAM principals granted the Tag User role (`roles/resourcemanager.tagUser`) in the IAM policy of the organization, a folder, or a project, can use tag values from tag keys with a project as their parent.

    * IAM principals who are developers, database administrators, or operational teams can be granted the Tag User role (`roles/resourcemanager.tagUser`), and other appropriate roles, without needing to be granted the Compute Security Admin role (`roles/compute.securityAdmin`). This way, operational teams can control which firewall rules apply to the network interfaces of the VM instances they manage without being able to modify those firewall rules.

For more information about the required permissions, see IAM roles.

  * **Firewall rule support** : rules in hierarchical firewall policies, global network firewall policies, and regional network firewall policies support tag keys as source secure tags or target secure tags. VPC firewall rules don't support secure tags. For more information, see Comparison of secure tags and network tags.

  * **VM binding and applicable firewall rules** : when you bind a secure tag value to a VM instance, applicable firewall rules that use the tag value include VM network interfaces as sources or targets:

    * If the secure tag value bound to the instance is from a tag key whose `purpose-data` attribute specifies a single VPC network:

      * Ingress firewall rules that use that tag value as a source secure tag have sources that include the network interfaces of the VM that are in the specified VPC network.

      * Ingress and egress firewall rules that use that tag value as a target secure tag have targets that include the network interfaces of the VM that are in the specified VPC network.

    * If the secure tag value bound to the instance is from a tag key whose `purpose-data` attribute specifies an organization:

      * Ingress firewall rules that use that tag value as a source secure tag have sources that include the network interfaces of the VM that are in any VPC network of the organization.

      * Ingress and egress firewall rules that use that tag value as a target secure tag have targets that include the network interfaces of the VM that are in any VPC network of the organization.

  * **How applicable firewall rules identify packets** : Cloud NGFW maps source secure tags and target secure tags to network interfaces, not IP addresses:

    * When a source secure tag of an ingress firewall rule includes a VM network interface as a source, Google Cloud matches whatever packets are sent from that network interface.

    * When a target secure tag of an ingress firewall rule includes a VM network interface as a target, Google Cloud matches whatever packets are received by that network interface.

    * When a target secure tag of an egress firewall rule includes a VM network interface as a target, Google Cloud matches whatever packets are sent from that network interface.

  * **Number of tag values per instance** : you can bind each tag value to an unlimited number of VM instances. The number of tag values that each instance supports is variable. Google Cloud enforces a limit of 10 tag values that _apply_ to each network interface of a VM. Google Cloud prevents you from binding additional tag values to a VM instance if more than 10 tag values apply to one or more of its network interfaces. For more information, see Bind secure tags.

  * **Network peering and NCC support** : you can use secure tags to identify VM network interfaces in peered networks. This includes networks connected through VPC Network Peering and VPC spokes on a Network Connectivity Center hub. This feature helps consumers of published services using [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access). For example, you can use ingress firewall rules with source secure tags to control traffic from service producer VMs to your VMs.

  * **Secure tags with Google Kubernetes Engine (GKE)** : you can bind secure tags to GKE clusters and node pools for use in network firewall policies. For more information, see [Create and manage secure tags](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls).




## Bind secure tags

To use secure tags with Cloud NGFW, you must bind a tag value to a VM instance. Each secure tag key supports multiple tag values; however, for each tag key, you can only bind one of its tag values to an instance. For more information about IAM permissions and how to bind secure tags, see [Bind secure tags](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls#bind-tags).

The examples in this section show how bound tag values apply to VM network interfaces. Consider the example `instance1` VM instance with two network interfaces:

  * `nic0` is connected to the `network1` VPC network
  * `nic1` is connected to the `network2` VPC network



Both of the VPC networks are in the same organization.

[ ![VM instance with two network interfaces, each
      connected to a different VPC network.](https://docs.cloud.google.com/static/firewall/images/secure-tags/binding_securetags.svg)](https://docs.cloud.google.com/static/firewall/images/secure-tags/binding_securetags.svg) **Figure 1.** VM instance with two network interfaces, each connected to a different VPC network (click to enlarge).

The `purpose-data` attribute of the corresponding tag key determines the relationship between bound tag values and VM network interfaces.

### Tag keys whose `purpose-data` attribute specifies a VPC network

Suppose you create two tag keys with the following `purpose-data` attributes and tag values:

  * `tag_key1` has a `purpose-data` attribute that specifies the `network1` VPC network and two tag values `tag_value1` and `tag_value2`.

  * `tag_key2` has a `purpose-data` attribute that specifies the `network2` VPC network and one tag value `tag_value3`.


[ ![The `purpose-data` attribute of each tag key
      specifies a single VPC network.](https://docs.cloud.google.com/static/firewall/images/secure-tags/define_networktag.svg)](https://docs.cloud.google.com/static/firewall/images/secure-tags/define_networktag.svg) **Figure 2.** The `purpose-data` attribute of each tag key specifies a single VPC network (click to enlarge).

When you bind secure tag values `tag_value1` and `tag_value3` to `instance1`:

  * `tag_value1` applies to the `nic0` network interface because its parent `tag_key1` has a `purpose-data` attribute that specifies the `network1` VPC network, and the `nic0` network interface is in `network1`.

  * `tag_value3` applies to the `nic1` network interface because its parent `tag_key2` has a `purpose-data` attribute that specifies the `network2` VPC network, and the `nic1` network interface is in `network2`.




The following diagram shows binding tag values from tag keys whose `purpose-data` attribute specifies a single VPC network.

[ ![Bound tag values from tag keys whose `purpose-data`
         attribute specifies a single VPC network.](https://docs.cloud.google.com/static/firewall/images/secure-tags/networktag.svg)](https://docs.cloud.google.com/static/firewall/images/secure-tags/networktag.svg) **Figure 3.** Bound tag values from tag keys whose `purpose-data` attribute specifies a single VPC network (click to enlarge).

### Tag keys whose `purpose-data` attribute specifies the organization

Suppose you create two tag keys with the following `purpose-data` attributes and tag values:

  * `tag_key3` has a `purpose-data` attribute that specifies the parent organization and has two tag values `tag_value4` and `tag_value5`.

  * `tag_key4` has a `purpose-data` attribute that specifies the parent organization and has one tag value `tag_value6`.


[ ![The `purpose-data` attribute of each tag key
      specifies the parent organization.](https://docs.cloud.google.com/static/firewall/images/secure-tags/define_orgtag_auto.svg)](https://docs.cloud.google.com/static/firewall/images/secure-tags/define_orgtag_auto.svg) **Figure 4.** The `purpose-data` attribute of each tag key specifies the parent organization (click to enlarge).

When you bind the tag value `tag_value4` to `instance1`:

  * `tag_value4` applies to the `nic0` network interface because its parent `tag_key3`has a `purpose-data` attribute that specifies the parent organization containing the `network1` VPC network, and the `nic0` network interface is in `network1`.

  * `tag_value4` also applies to the `nic1` network interface because its parent `tag_key3` includes a `purpose-data` attribute that specifies the parent organization that contains the `network2` VPC network. The `nic1` network interface is in `network2`.




The following diagram shows binding tag values from tag keys whose `purpose-data` attribute specifies the parent organization.

[ ![Bound tag values from tag keys whose `purpose-data` attribute
    specifies the parent organization.](https://docs.cloud.google.com/static/firewall/images/secure-tags/orgtag.svg)](https://docs.cloud.google.com/static/firewall/images/secure-tags/orgtag.svg) **Figure 5.** Bound tag values from tag keys whose `purpose-data` attribute specifies the parent organization (click to enlarge).

## Configure secure tags

The following workflow provides a high-level sequence of steps required to configure secure tags in firewall policies.

  1. You can create secure tags at the organization or project level. To create a tag at the organization level, you must first be granted IAM permission by the organization administrator. For more information, see [Grant permissions to secure tags](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls#grant-tag-roles).

  2. To create a secure tag, you must first create a tag key. This tag key describes the tag you are creating. For more information, see [Create the secure tag keys and values](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls#create-tags).

  3. After you create a secure tag key, you must add the relevant secure tag values to it. For more information, see [Create the secure tag keys and values](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls#create-tags). To give users specific access to manage secure tag keys and attach tag values to resources, use the Google Cloud console. For more information, see [Manage access to tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#managing_access).

  4. After you create a secure tag, you can use it in either a network firewall policy or a hierarchical firewall policy. For more information, see [Create a hierarchical firewall policy](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls#hierarchical-firewall-policy) and [Create a network firewall policy](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls#network-firewall-policy).

  5. To allow the selected traffic between the VMs with the source tag keys and target tag keys, create a firewall policy rule (network or hierarchical) with the specific source tag values and target tag values. For more information, see [Create a firewall policy rule with secure tags](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls#rules-with-tags).

  6. After a tag key is created and appropriate access is granted to both the tag key and the resource, a tag value can be bound to a VM instance. For more information, see [Bind secure tags](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls#bind-tags).




## Comparison of secure tags and network tags

The following table summarizes the differences between secure tags and network tags. The checkmark indicates that the attribute is supported, and the symbol indicates that the attribute isn't supported.

Attribute | Secure tag with `purpose-data` attribute specifying a VPC network | Secure tag with `purpose-data` attribute specifying the organization | Network tag  
---|---|---|---  
Parent resource | Project or organization | Project or organization | Project  
Structure and format | Tag key with up to 1,000 values | Tag key with up to 1,000 values | Simple string  
Access control | Using IAM | Using IAM | No access control  
Applicable network interfaces | 

  * Ingress firewall rule with source secure tag value: sources include VM network interfaces in the VPC network specified by the `purpose-data` attribute of the tag key.
  * Ingress or egress firewall rule with target secure tag value: targets include VM network interfaces in the VPC network specified by the `purpose-data` attribute of the tag key.

| 

  * Ingress firewall rule with source secure tag value: sources include VM network interfaces in any VPC network of the parent organization.
  * Ingress or egress firewall rule with target secure tag value: targets include VM network interfaces in any VPC network of the parent organization.

| 

  * Ingress firewall rule with source network tag: sources include VM network interfaces in any VPC network used by the VM if that network has VPC firewall rules using the source network tag.
  * Ingress or egress firewall rule with target network tag: targets include VM network interfaces in any VPC network used by the VM if that network has VPC firewall rules using the target network tag.

  
Supported by rules in hierarchical firewall policies |  |  |   
Supported by rules in global and regional network firewall policies |  |  |   
Supported by VPC firewall rules |  |  |   
Ingress firewall rules can include sources in VPC networks connected using VPC Network Peering | 1 | 1 |   
Ingress firewall rules can include sources in other VPC spokes on the NCC hub | 1 | 1 |   
  
1A source secure tag value can identify network interfaces in another VPC network when both of the following are true: 

  * The tag key `purpose-data` attribute specifies the other VPC network (or parent organization containing the other VPC network)
  * The other VPC network and the VPC network that uses the firewall policy are connected using VPC Network Peering or are both VPC spokes on the same NCC hub.



## IAM roles

For more information about the IAM roles and permissions that you need to create and manage secure tags, see [Manage tags on resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).

## What's next

  * To grant permissions to secure tags and create secure tag key-value pairs, see [Create and manage secure tags](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls).
  * To use secure tags in network peering, see [Use secure tags across peered networks](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls#use-tags-across-peered-networks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
