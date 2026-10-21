---
url: https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details/
title: Firewall policy rule components \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:23.833660+00:00
---

# Firewall policy rule components  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Firewall policy rule components Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the components of a firewall policy rule that you configure in a [hierarchical](https://docs.cloud.google.com/firewall/docs/using-firewall-policies), [global](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies), or [regional](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies) [firewall policy](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) that applies to a [regular Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/firewall/docs/network-profiles#network-profiles). These components include direction, source, destination, and Layer 4 characteristics such as protocol and destination port (if the protocol uses ports).

Firewall policy rules in Google Cloud let you control traffic to enhance security and operational efficiency. When you create a firewall policy rule, you specify the components that define what the rule does. Each firewall policy rule applies to either incoming (ingress) or outgoing (egress) connections, but not both.

For specialized, high-performance network profiles such as Remote Direct Memory Access (RDMA) over Converged Ethernet (RoCE), firewall policy rule capabilities and configurations differ from regular networks. For details about firewall rules for RDMA network profiles, see [Cloud NGFW for RoCE VPC networks](https://docs.cloud.google.com/firewall/docs/firewall-for-roce).

This document is intended for network administrators and security engineers who configure and manage firewall policy rules.

## Priority

Each rule in a firewall policy must have a unique priority.

Consider the following guidelines when assigning a priority to a firewall policy rule:

  * The priority is an integer from `0` to `2,147,483,547`, inclusive.
  * In a firewall policy, every rule must have a unique priority number. Firewall policy rules don't have names.
  * Priority number `0` is the highest priority and `2,147,483,547` is the lowest. Priority decreases as the number increases. In a firewall policy, if a packet matches multiple rules, only the matching rule with the highest priority is enforced.



Consider the following example where two firewall policy rules in a global network firewall policy associated with your VPC network exist:

  * An ingress rule from sources `0.0.0.0/0` (any IPv4 address) applicable to all targets, all protocols, and all destination ports, having a `deny` action and a priority of `1000`.

  * An ingress rule from sources `0.0.0.0/0` (any IPv4 address) applicable to specific targets with the secure tag `tagKeys/123/tagValues/456` (tag key [shortName](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating_tag) `role` and tag value `webserver`), for traffic on TCP 80, with an `allow` action.




The priority of the second rule determines whether TCP traffic to port 80 is allowed for the `webserver` targets:

  * If the priority of the second rule is set to a number _greater than_ `1000`, it has a _lower_ priority, so the first rule denying all traffic applies.

  * If the priority of the second rule is set to a number _less than_ `1000`, it has a _higher_ priority. A packet arriving for the `webserver` on TCP 80 matches the second rule first. The traffic is allowed and the firewall stops looking at any other rules. The first rule is never checked for this specific packet.




The previous example demonstrates how you can use priorities to create selective `allow` rules and global `deny` rules to implement a security best practice of least privilege.

## Action on match

A rule in a firewall policy can have one of the following actions:

Action parameter | Description  
---|---  
`allow` |  Allows packets for a new connection. Stops evaluating rules in the firewall policy that contains the matching rule. Doesn't evaluate any other firewall rules. Regardless of the direction of the rule, if the packet protocol and firewall policy type support connection tracking, an allow rule creates a firewall connection tracking table entry that permits both ingress and egress packets.  
`deny` |  Disallows packets for a new connection. Stops evaluating rules in the firewall policy that contains the matching rule. Doesn't evaluate any other firewall rules. Cloud NGFW always checks for a firewall connection tracking table entry before it evaluates firewall rules. Consequently, if an allow rule created a connection tracking table entry, that connection tracking table entry takes precedence.  
`apply_security_profile_group` |  Intercepts packets for a new connection, sending them to a [firewall endpoint](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints) or [ intercept endpoint group](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-groups-overview). Stops evaluating rules in the firewall policy that contains the matching rule. Doesn't evaluate any other firewall rules. Regardless of the direction of the rule, if the packet protocol and firewall policy type support connection tracking, a rule with the `apply_security_profile_group` action creates a firewall connection tracking table entry so that both ingress and egress packets are intercepted by the firewall endpoint or intercept endpoint group. You can't use the `apply_security_profile_group` action in regional network firewall policies or regional system firewall policies. The `apply_security_profile_group` action has some special requirements depending on the rule's target type. For more information, see Targets.  
`goto_next` |  Stops evaluating other rules in the firewall policy, and evaluates rules in the next step of the [ firewall policy and rule evaluation order](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order).  The next step of the firewall policy and rule evaluation order might be evaluation of rules in another firewall policy or the implied firewall rules.  
  
## Enforcement

You can choose whether a firewall policy rule is _enforced_ by setting its state to enabled or disabled. You set the enforcement state when you create a rule or when you update a rule.

If you don't set an enforcement state when you create a new firewall rule, the firewall rule is automatically enabled.

## Protocols and ports

Similar to VPC firewall rules, you must specify one or more protocol and port constraints when you create a rule. When specifying TCP or UDP in a rule, you can specify the protocol, the protocol and a destination port, or the protocol and a destination port range; you cannot specify only a port or port range. Also, you can only specify destination ports. Rules based on source ports aren't supported.

You can use the following protocol names in firewall rules: `tcp`, `udp`, `icmp` (for IPv4 ICMP), `esp`, `ah`, `sctp`, and `ipip`. For all other protocols, use the [IANA protocol numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).

Many protocols use the same name and number in both IPv4 and IPv6, but some protocols, such as ICMP, don't. To specify IPv4 ICMP, use `icmp` or protocol number `1`. To specify IPv6 ICMP, use protocol number `58`.

Firewall rules don't support specifying ICMP types and codes, just the protocol.

The IPv6 Hop-by-Hop protocol isn't supported in firewall rules.

If you don't specify protocol and port parameters, the rule applies to all protocols and destination ports.

## Logging

Logging for firewall policy rules works the same as for VPC [VPC firewall rules logging](https://docs.cloud.google.com/firewall/docs/using-firewall-rules-logging) except for the following:

  * The reference field includes the firewall policy ID and a number indicating the level of the resource to which the policy is attached. For example, `0` means that the policy is applied to an organization, and `1` means that the policy is applied to a top-level folder under the organization.

  * Logs for firewall policy rules include a `target_resource` field that identifies the VPC networks to which the rule applies.



  * Logging can only be enabled for `allow`,`deny`, and `apply_security_profile_group` rules; logging cannot be enabled for `goto_next` rules.

  * When you enable logging for a rule that uses the `apply_security_profile_group` action, Cloud NGFW generates a single log entry when it intercepts a traffic session and redirects the traffic to the firewall endpoint for deep packet inspection. This log entry confirms that the firewall rule matched the traffic and successfully redirected it to the firewall endpoint. For more information, see [Firewall policy rules logging overview](https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-logging-overview#limitations).

  * The firewall endpoint performs deep packet inspection, such as intrusion detection and prevention service and URL filtering service, and generates its own set of logs. These logs provide detailed information about the connections within the intercepted session, listing any detected threats or URL filtering actions. These deep packet inspection logs can generate multiple log entries per session.




## Target, source, destination

Target, source, and destination parameters work together to determine the scope of a firewall rule.

  * Target parameters: identify the resources that the firewall rule applies to.

  * Source and destination parameters: define the traffic criteria. You can specify both for ingress and egress rules. Valid options for source and destination parameters depend on the target parameters and the direction of the firewall rule.




### Targets

The _target type_ parameter and one or more _target_ parameters define the targets of a firewall rule. These targets of a firewall rule are the resources that the firewall rule protects.

  * If the target type is omitted or is set to `INSTANCES`, the firewall rule applies to the network interfaces of Compute Engine instances, including Google Kubernetes Engine (GKE) nodes and App Engine flexible environment instances. Both ingress and egress rules are supported.

To specify which VM network interfaces the firewall rule applies to, use target parameters:

    * If you omit all target parameters, the firewall rule applies to the broadest instance targets.

    * For target parameter and target parameter combination details, see Specific targets and Specific target combinations.

  * If you set the target type to `INTERNAL_MANAGED_LB`, the firewall rule applies to the managed Envoy proxies that handle traffic for internal Application Load Balancers and internal proxy Network Load Balancers. Only ingress rules are supported.

    * If you omit the _target forwarding rules_ parameter, the firewall rule applies to the broadest load balancer targets.

    * To restrict the firewall rule to a single load balancer, use the target forwarding rules parameter. For more information, see Specific targets.

You can delete a forwarding rule that is defined as a target forwarding rule without removing the firewall policy rule itself. Target forwarding rules are bound to the firewall policy rule by their ID, not by name. If you delete a forwarding rule and create a new forwarding rule with the same name, the firewall policy rule doesn't automatically rebind to the new forwarding rule. To reapply the firewall policy rule, you must update the rule to reference the new forwarding rule.

    * To use the `apply_security_profile_group` action in a global network firewall policy with the target type set to `INTERNAL_MANAGED_LB`, specify only one cross-region internal Application Load Balancer forwarding rule. To specify the target forwarding rule, use the `target-forwarding-rules` parameter.

    * You can't use secure tags, network tags, or backend service account attributes to identify load balancer targets.




#### Broadest instance targets

The broadest instance targets depend on the firewall policy type:

  * **Broadest instance targets for a rule in a hierarchical firewall policy** : all VM network interfaces in a subnet in any region of any VPC network that's located in a project under the Resource Manager node (folder or organization) associated with the hierarchical firewall policy.

  * **Broadest instance targets for a rule in a global network firewall policy** : all VM network interfaces in a subnet in any region of the VPC network that's associated with the global network firewall policy.

  * **Broadest instance targets for a rule in regional network firewall policy** : all VM network interfaces in a subnet within the region and VPC network that are associated with the regional network firewall policy.




#### Broadest load balancer targets

The broadest load balancer targets depend on the following firewall policy types:

  * **Broadest load balancer targets for a rule in a global network firewall policy** : all forwarding rules for internal Application Load Balancers and internal proxy Network Load Balancers in a subnet in any region of the VPC network that is associated with the global network firewall policy.

  * **Broadest load balancer targets for a rule in a regional network firewall policy** : all forwarding rules for internal Application Load Balancers and internal proxy Network Load Balancers in a subnet within the region and VPC network that is associated with the regional network firewall policy.




#### Specific targets

The following table lists the target parameters, the firewall policies that support rules with each parameter, and the supported rule target types. If you don't specify a target parameter, the rule uses either the broadest instance targets or broadest load balancer targets, based on the rule's target type. The checkmark indicates that the parameter is supported, and the symbol indicates that the parameter isn't supported.

Target parameter | Firewall policy support | Rule target type support  
---|---|---  
Hierarchical | Global network | Regional network | `INSTANCES` | `INTERNAL_MANAGED_LB`  
**Target VPC network resources** A list of one or more VPC networks specified by using the `target-resources` parameter. This list narrows the broadest instance targets to the VM network interfaces that are in at least one of the specified VPC networks. |  |  |  |  |   
**Target service accounts** A list of one or more service accounts specified by using the `target-service-accounts` parameter. This list narrows the broadest instance targets to the VM network interfaces that belong to VM instances associated with at least one of the specified service accounts. |  |  |  |  |   
**Target secure tag values from a tag key with network purpose data** A rule that uses the `target-secure-tags` parameter containing a list of one or more tag values from a tag key whose `purpose-data` specifies a single VPC network. This list narrows the broadest instance targets to the VM network interfaces that each meet _both_ of the following criteria:

  * The interface is in the VPC network that matches the `purpose-data` of the tag key.
  * The interface belongs to a VM that's bound to the tag value.

For more information, see [Secure tags for firewalls](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview). |  |  |  |  |   
**Target secure tag values from a tag key with organization purpose data** A rule that uses the `target-secure-tags` parameter containing a list of one or more tag values from a tag key whose `purpose-data` is `organization=auto`. This list narrows the broadest instance targets to the VM network interfaces that each meet _both_ of the following criteria:

  * The interface is in any VPC network of the organization.
  * The interface belongs to a VM that's bound to the tag value.

For more information, see [Secure tags for firewalls](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview). |  |  |  |  |   
**Target forwarding rules** A single forwarding rule for an internal Application Load Balancer or internal proxy Network Load Balancer specified in the target forwarding rules format. This parameter narrows the broadest load balancer targets to a specific internal Application Load Balancer or internal proxy Network Load Balancer. |  |  |  |  |   
  
#### Specific target combinations

Rules that support the `target-resources` parameter can combine it with another target parameter to create a target parameter combination. The following table lists supported target parameter combinations, the firewall policies that support rules with each parameter, and the supported rule target types. If you don't specify a target parameter, the rule uses either the broadest instance targets or broadest load balancer targets, based on the rule's target type.

The checkmark indicates that the parameter is supported, and the symbol indicates that the parameter isn't supported.

Target parameter combination | Firewall policy support | Rule target type support  
---|---|---  
Hierarchical | Global network | Regional network | `INSTANCES` | `INTERNAL_MANAGED_LB`  
**Combination of target VPC network resources and target service accounts** A rule that uses both the `target-resources` and `target-service-accounts` parameters. This combination narrows the broadest instance targets to VM network interfaces that each meet _both_ of the following criteria:

  * The interface is in at least one of the VPC networks specified in `target-resources`.
  * The interface belongs to a VM instance that's associated with at least one of the specified service accounts.

|  |  |  |  |   
**Combination of target VPC network resources and target secure tag values** A rule that uses both the `target-resources` and `target-secure-tags` parameters. Tag values must come from a tag key whose `purpose-data` is `organization=auto`. This combination narrows the broadest instance targets to VM network interfaces that each meet _both_ of the following criteria:

  * The interface is in at least one of the VPC networks specified in `target-resources`.
  * The interface belongs to a VM that's bound to the tag value.

|  |  |  |  |   
  
#### Target forwarding rules format

When you set the target type for a firewall rule to `INTERNAL_MANAGED_LB`, the `target-forwarding-rules` parameter accepts values in the following formats:

  * For regional internal Application Load Balancers and regional internal proxy Network Load Balancers:

    * `https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/forwardingRules/FORWARDING_RULE_NAME`
    * `projects/PROJECT_ID/regions/REGION/forwardingRules/FORWARDING_RULE_NAME`
  * For cross-region internal Application Load Balancers and cross-region internal proxy Network Load Balancers:

    * `https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/forwardingRules/FORWARDING_RULE_NAME`
    * `projects/PROJECT_ID/global/forwardingRules/FORWARDING_RULE_NAME`

**Note:** In a regional network firewall policy, a firewall rule that uses the `target-forwarding-rules` parameter must reference a supported forwarding rule in the same region as the firewall policy.

#### Targets and IP addresses for ingress rules

When a firewall rule target type is either omitted or set to `INSTANCES`, the rule applies to packets that are routed to network interfaces of target VMs.

  * If the ingress firewall rule _includes_ a destination IP address range, the packet's destination must fit within one of the explicitly defined destination IP address ranges.

  * If the ingress firewall rule does _not_ include a destination IP address range, the packet's destination must match one of the following IP addresses of each target VM:

    * The primary internal IPv4 address assigned to the instance's NIC.

    * Any configured [alias IP address ranges](https://docs.cloud.google.com/vpc/docs/alias-ip) on the instance's NIC.

    * The external IPv4 address that's associated with the instance's NIC.

    * If IPv6 is configured on the subnet, any of the IPv6 addresses assigned to the NIC.

    * An internal or external IP address associated with a forwarding rule used for pass-through load balancing, where the instance is a backend for an internal passthrough Network Load Balancer or an external passthrough Network Load Balancer.

    * An internal or external IP address associated with a forwarding rule used for protocol forwarding, where the instance is referenced by a target instance.

    * An IP address within the destination range of a custom static route that uses the instance (`next-hop-instance` or `next-hop-address`) as a next hop VM.

    * An IP address within the destination range of a custom static route that uses an internal passthrough Network Load Balancer (`next-hop-ilb`) as a next hop if the VM is a backend for that load balancer.




When you set the target type of a firewall policy rule to `INTERNAL_MANAGED_LB`, you must leave the destination parameter of the rule unset. The firewall policy rule applies to packets whose destination IP addresses match the forwarding rule IP addresses of the targeted internal Application Load Balancers and internal proxy Network Load Balancers.

#### Targets and IP addresses for egress rules

When a firewall rule target type is either omitted or set to `INSTANCES`, the rule applies to packets that are emitted by network interfaces of target VMs.

  * If the target VM has [IP forwarding](https://docs.cloud.google.com/vpc/docs/using-routes#canipforward) disabled (default), the VM can only emit packets with the following sources:

    * The primary internal IPv4 address of an instance's NIC.

    * Any configured alias IP address range on an instance's NIC.

    * If IPv6 is configured on the subnet, any of the IPv6 addresses assigned to the NIC.

    * An internal or external IP address associated with a forwarding rule, for pass-through load balancing or protocol forwarding. This is valid if the instance is a backend for an internal passthrough Network Load Balancer, an external passthrough Network Load Balancer, or is referenced by a target instance.

If the egress firewall rule _includes_ source IP address ranges, the target VMs are still limited to the source IP addresses mentioned previously, but a source parameter can be used to refine the sources. Use of a source parameter without enabling IP forwarding _never_ expands the set of possible packet source addresses.

If the egress firewall rule does _not_ include a source IP address range, all the source IP addresses mentioned previously are permitted.

  * If the target VM has IP forwarding enabled, the VM can emit packets with arbitrary source addresses. You can use the source parameter to more precisely define the set of allowed packet sources.




### Sources

Source parameter values depend on the direction of the firewall rule.

#### Sources for ingress rules

This table lists the source parameters for ingress rules, the firewall policies that support each parameter, and the rule target types that are compatible with each parameter. You must specify at least one source parameter. The checkmark indicates that the parameter is supported, and the symbol indicates that the parameter isn't supported.

Ingress rule source parameter | Firewall policy support | Rule target type support  
---|---|---  
Hierarchical | Global network | Regional network | `INSTANCES` | `INTERNAL_MANAGED_LB`  
**Source IP address ranges** A list consisting of IPv4 addresses in CIDR format or IPv6 addresses in CIDR format. The list is stored within the firewall policy rule itself. |  |  |  |  |   
**Source address groups** Reusable collections of IPv4 addresses in CIDR format or IPv6 addresses in CIDR format. The firewall rule references the collection. For more information, see [Address groups for firewall policies](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies). |  |  |  |  |   
**Source domain names** A list of one or more source domain names. For more information, including how domain names are converted to IP addresses, see [FQDN objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview). |  |  |  |  |   
**Source secure tag values from a tag key with network purpose data** A list of one or more tag values from a tag key whose purpose data specifies a single VPC network. For more information, see [Secure tags for firewalls](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview) and How source secure tags imply packet sources. |  |  |  |  |   
**Source secure tag values from a tag key with organization purpose data** A list of one or more tag values from a tag key whose purpose data is `organization=auto`. For more information, see [Secure tags for firewalls](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview) and How source secure tags imply packet sources. |  |  |  |  |   
**Source geolocations** A list of one or more source geographic locations specified as two-letter country or region codes. For more information, see [Geolocation objects](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview) |  |  |  |  |   
**Source Google Threat Intelligence lists** A list of one or more predefined Google Threat Intelligence list names. For more information, see [Google Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview). |  |  |  |  |   
**Source network context** A constraint that defines a security boundary. Valid values depend on the target type of the rule. For more information, see [Network contexts](https://docs.cloud.google.com/firewall/docs/understand-network-contexts). |  |  |  |  |   
  
##### Ingress rule source combinations

In a single ingress rule, you can use two or more source parameters to produce a source combination. Cloud NGFW enforces the following constraints on source combinations of each ingress rule:

  * Source IP address ranges must contain either IPv4 or IPv6 CIDRs, not a combination of both.
  * A source address group that contains IPv4 CIDRs cannot be used with a source address group that contains IPv6 CIDRs.
  * A source IP address range that contains IPv4 CIDRs cannot be used with a source address group that contains IPv6 CIDRs.
  * A source IP address range that contains IPv6 CIDRs cannot be used with a source address group that contains IPv4 CIDRs.
  * The internet network context cannot be used with the source secure tags.
  * Non-internet context, VPC networks context, and inter-VPC context cannot be used with source Google Threat Intelligence lists or source geolocations.



Cloud NGFW applies the following logic to match the packets to an ingress rule that uses a source combination:

  * If the source combination does _not_ include a source network context, packets match the ingress rule if they match at least one source parameter in the source combination.

  * If the source combination includes a source network context, packets match the ingress rule if they match the source network context _and_ at least one of the other source parameters in the source combination.




#### How source secure tags imply packet sources

An ingress firewall rule can use source secure tag values when its target type is omitted or set to `INSTANCES`. Secure tag values identify network interfaces, not packet characteristics like IP addresses.

Packets sent from a network interface of a VM instance match an ingress rule that uses a source secure tag value according to the following rules:

  * If the ingress rule is in a regional network policy, the VM instance must be located in a zone of the same region as the regional network firewall policy. Otherwise, the VM instance can be located in any zone.

  * The VM instance must be associated with the same secure tag value that is used as a source secure tag in an ingress firewall rule.

  * The secure tag value associated with the VM instance and used by the ingress firewall rule must come from a tag key whose `purpose-data` attribute identifies at least one VPC network that contains a network interface of the VM instance:

    * If the tag key's purpose data specifies a single VPC network, ingress firewall rules that use the source secure tag value apply to the network interfaces of the VM instance that are in that VPC network.

    * If the tag key's purpose data specifies the organization, ingress firewall rules that use the source secure tag value apply to the network interfaces of the VM instance that are in any VPC network of the organization.

  * The identified VM network interface must meet one of the following criteria:

    * The VM network interface is in the same VPC network as the VPC network to which the firewall policy applies.
    * The VM network interface is in a VPC network that's connected, using VPC Network Peering, to the VPC network to which the firewall policy applies.

    * The VPC network that's used by the VM network interface and the VPC network to which the firewall policy applies are both VPC spokes on the same Network Connectivity Center hub.




For more information about secure tags for firewalls, see [Specifications](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview#specifications).

#### Sources for egress rules

You can use the following sources for egress rules in both hierarchical firewall policies and network firewall policies:

  * **Default—implied by target** : if you omit the source parameter from an egress rule, packet sources are defined implicitly as described in Targets and IP addresses for egress rules.

  * **Source IPv4 address ranges** : a list of IPv4 addresses in CIDR format.

  * **Source IPv6 address ranges** : a list of IPv6 addresses in CIDR format.




Follow these guidelines to add source IP address ranges for egress rules:

  * If a VM network interface is assigned an external IPv4 addresses, or if it doesn't have an external IPv4 address but uses a Cloud NAT gateway, egress firewall evaluation occurs before Google Cloud changes the outbound packet's source from an internal IPv4 address to an external IPv4 address. To apply an egress firewall rule, you must either omit the **Source** parameter or include the VM network interface's internal IPv4 address in the **Source** parameter.

  * If you have a source IP address range and destination parameters in the egress rule, then the destination parameters are resolved into the same IP version as the source IP version.


For example, in an egress rule, you have an IPv4 address range in the source parameter and an [FQDN object](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview) in the destination parameter. If the FQDN resolves into both IPv4 and IPv6 addresses, only the resolved IPv4 address is used during rule enforcement. 

### Destinations

Destination parameter values depend on the direction of the firewall rule.

#### Destinations for ingress rules

You can use the following destinations for ingress firewall rules in both hierarchical and network firewall policies:

  * **Default—implied by target** : if you omit the destination parameter from an ingress rule, packet destinations are defined implicitly as described in Targets and IP addresses for ingress rules.

  * **Destination IPv4 address ranges** : a list of IPv4 addresses in CIDR format.

  * **Destination IPv6 address ranges** : a list of IPv6 addresses in CIDR format.




Follow these guidelines to add destination IP address ranges for ingress rules:

  * If a VM network interface is assigned an external IPv4 addresses, or if it doesn't have an external IPv4 address but uses a Cloud NAT gateway, ingress firewall evaluation occurs after Google Cloud changes the inbound packet's destination from an external IPv4 address to an internal IPv4 address. To apply an ingress firewall rule, you must either omit the **Destination** parameter or include the VM network interface's internal IPv4 address in the **Destination** parameter.

  * If you have both source and destination parameters defined in an ingress rule, then the source parameters are resolved into the same IP version as the destination IP version. To learn more about how to define a source for ingress rules, see Sources for ingress rules in hierarchical firewall policies and Sources for ingress rules in network firewall policies.

For example, in an ingress rule, you have an IPv6 address range in the destination parameter and a geolocation country code in the source parameter. During rule enforcement, only the mapped IPv6 address is used for the specified source country code.




#### Destinations for egress rules

This table lists the destination parameters for egress rules, the firewall policies that support each parameter, and the rule target types that are compatible with each parameter. You must specify at least one destination parameter. The checkmark indicates that the parameter is supported, and the symbol indicates that the parameter isn't supported.

Egress rule destination parameter | Firewall policy support | Rule target type support  
---|---|---  
Hierarchical | Global network | Regional network | `INSTANCES` | `INTERNAL_MANAGED_LB`  
**Destination IP address ranges** A list consisting of IPv4 addresses in CIDR format or IPv6 addresses in CIDR format. The list is stored within the firewall policy rule itself. |  |  |  |  |   
**Destination address groups** Reusable collections of IPv4 addresses in CIDR format or IPv6 addresses in CIDR format. The firewall policy rule references the collection. For more information, see [Address groups for firewall policies](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies). |  |  |  |  |   
**Destination domain names** A list of one or more destination domain names. For more information, including how domain names are converted to IP addresses, see [FQDN objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview). |  |  |  |  |   
**Destination geolocations** A list of one or more source geographic locations specified as two-letter country or region codes. For more information, see [Geolocation objects](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview). |  |  |  |  |   
**Destination Google Threat Intelligence lists** A list of one or more predefined Google Threat Intelligence list names. For more information, see [Google Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview). |  |  |  |  |   
**Destination network context** A constraint that defines a security boundary. |  |  |  |  |   
  
##### Egress rule destination combinations

In a single egress rule, you can use two or more destination parameters to produce a destination combination. Cloud NGFW enforces the following constraints on destination combinations of each egress rule:

  * Destination IP address ranges must contain either IPv4 or IPv6 CIDRs, not a combination of both.
  * You can't use a destination address group that contains IPv4 CIDRs with a destination address group that contains IPv6 CIDRs.
  * You can't use a destination IP address range that contains IPv4 CIDRs with a destination address group that contains IPv6 CIDRs.
  * You can't use a destination IP address range that contains IPv6 CIDRs with a destination address group that contains IPv4 CIDRs.
  * You can't use destination Google Threat Intelligence lists or destination geolocations with destination non-internet network context.



Cloud NGFW applies the following logic to match the packets to an egress rule that uses a destination combination:

  * If the destination combination does _not_ include a destination network context, packets match the egress rule if they match at least one destination parameter in the destination combination.

  * If the destination combination includes a destination network context, packets match the egress rule if they match the destination network context _and_ at least one of the other destination parameters in the destination combination.




## What's next

  * [Google Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview)


  * [Fully qualified domain name objects overview](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview)


  * [Address groups for firewall policies](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
