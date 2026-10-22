---
url: https://docs.cloud.google.com/firewall/docs/firewall-policy-log-format/
title: Firewall policy rules logging format \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:06.608196+00:00
---

# Firewall policy rules logging format  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/firewall-policy-log-format/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Firewall policy rules logging format Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the firewall policy rules logging structure in Cloud Logging. When a firewall rule with logging enabled applies to traffic to or from a virtual machine (VM) instance, Cloud Logging creates a log entry. Log records appear in the `JSON` payload field of a Logging [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

Firewall log records consist of base fields, which are the core fields of every log record, and an optional metadata fields. To reduce storage costs, you can exclude metadata fields.

Some log fields can contain other fields as values. For example, the `connection` field uses the `IpConnection` format, which includes the source and destination IP address and port, and the protocol, in a single field.

The following table describes the log fields supported for Cloud Next Generation Firewall (Cloud NGFW) policy rules, such as hierarchical, global, and regional, excluding legacy fields such as network tags and service accounts, which are unsupported for Cloud NGFW policies.

Field | Description | Field type: base or optional metadata  
---|---|---  
`connection` | IpConnection  
5-Tuple describing the source and destination IP address, source and destination port, and IP protocol of this connection. | Base  
`disposition` | Indicates whether the connection was `ALLOWED`, `DENIED`, or `INTERCEPTED`. | Base  
`rule_details` | RuleDetails  
Firewall policy rule details. The log format is `{folder tier index}/firewallPolicy:{firewall policy ID}` or `network:{network name}/firewallPolicy:{firewall policy ID}` based on the scope of the policy. | Base  
`instance` | InstanceDetails  
VM instance details. In a Shared VPC configuration, `project_id` corresponds to that of the service project. | Metadata  
`load_balancer_details` | LoadBalancingDetails  
Details of the internal Application Load Balancer or internal proxy Network Load Balancer to which the firewall policy rule applies. When the target of a firewall rule is one of these load balancers, the `instance` field is omitted. | Metadata  
`vpc` | VpcDetails  
VPC network details. In a Shared VPC configuration, `project_id` corresponds to that of the host project. | Metadata  
`remote_instance` | InstanceDetails  
If the remote endpoint of the connection was a VM located in the Compute Engine, this field is populated with VM instance details. | Metadata  
`remote_vpc` | VpcDetails  
If the remote endpoint of the connection was a VM that is located in a VPC network, this field is populated with the network details. | Metadata  
`remote_location` | GeographicDetails  
If the remote endpoint of the connection was external to the VPC network, this field is populated with available location metadata. | Metadata  
  
## IpConnection

Field | Type | Description  
---|---|---  
`src_ip` | string | Source IP address. If the source is a Compute Engine VM, `src_ip` is either the primary internal IP address or an address in an alias IP range of the VM's network interface. The external IP address is not shown. Logging shows the IP address of the VM as the VM sees it on the packet header, the same as if you ran `tcpdump` on the VM.  
`src_port` | integer | Source port  
`dest_ip` | string | Destination IP address. If the destination is a Google Cloud VM, `dest_ip` is either the primary internal IP address or an address in an alias IP range of the VM's network interface. The external IP address is not shown even if it was used in making the connection.  
`dest_port` | integer | The destination port.  
`protocol` | integer | [IP protocol](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) of the connection.  
  
## RuleDetails

Field | Type | Description  
---|---|---  
`reference` | string | The unique, absolute resource path to the rule that matched the network traffic. The format for firewall policy rules is: 

  * Hierarchical firewall policy: `{folder tier index}/firewallPolicy:{id}`
  * Global firewall policy: `network:{network name}/firewallPolicy:{id}`
  * Regional firewall policy: `network:{network name}/region:{region name}/firewallPolicy:{id}`

  
`priority` | integer | The priority for the firewall policy rule.  
`action` | string | The action of the firewall policy rule. Can be `ALLOW`, `DENY`, or `APPLY_SECURITY_PROFILE_GROUP`.  
`source_networks[ ]` | string | List of VPC networks when the source network context parameter is `VPC_NETWORKS`.  
`destination_networks[ ]` | string | List of VPC networks when the destination network context parameter is `VPC_NETWORKS`.  
`source_network_context` | string | The network context for the traffic that an ingress rule applies to.  
`destination_network_context` | string | The network context for the traffic that an egress rule applies to.  
`apply_security_profile_fallback_action` | string | Applicable if the action is `APPLY_SECURITY_PROFILE_GROUP`. Values are `ALLOW` or `UNSPECIFIED` Set if the connection disposition is `INTERCEPTED`.  
`direction` | string | The direction that the firewall policy rule applies to. It can be `INGRESS` or `EGRESS`.  
`source_range[ ]` | string | (Optional metadata) List of source ranges that the firewall policy rule applies to.  
`destination_range[ ]` | string | (Optional metadata) List of destination ranges that the firewall policy rule applies to.  
`ip_port_info[ ]` | string | (Optional metadata) List of IP protocols and applicable port ranges for rules.  
`target_resource[ ]` | string | (Optional metadata) Target resource strings formatted as `projects/{project ID}/global/networks/{network name}`. It is available in hierarchical firewall policies.  
`source_secure_tag[ ]` | string | (Optional metadata) List of all the source secure tags that the firewall policy rule applies to.  
`target_secure_tag[ ]` | string | (Optional metadata) List of all the target secure tags that the firewall policy rule applies to.  
`source_region_code[ ]` | string | (Optional metadata) List of all the source country codes that the firewall policy rule applies to.  
`destination_region_code[ ]` | string | (Optional metadata) List of all the destination country codes that the firewall policy rule applies to.  
`source_fqdn[ ]` | string | (Optional metadata) List of all the source domain names that the firewall policy rule applies to.  
`destination_fqdn[ ]` | string | (Optional metadata) List of all the destination domain names that the firewall policy rule applies to.  
`source_threat_intelligence[ ]` | string | (Optional metadata) List of all the source Google Threat Intelligence list names that the firewall policy rule applies to.  
`destination_threat_intelligence[ ]` | string | (Optional metadata) List of all the destination Google Threat Intelligence list names that the firewall policy rule applies to.  
`source_address_groups[ ]` | string | (Optional metadata) List of all the source address groups that the firewall policy rule applies to.  
`destination_address_groups[ ]` | string | (Optional metadata) List of all the destination address groups that the firewall policy rule applies to.  
`target_type` | string | INSTANCES or INTERNAL_MANAGED_LB  
`target_forwarding_rules` | string | List of full or partial forwarding rule URLs for internal Application Load Balancers or internal proxy Network Load Balancers to which the firewall rule applies.  
  
## IpPortDetails

Field | Type | Description  
---|---|---  
`ip_protocol` | string | IP protocol that the firewall policy rule applies to. It can't be set to `ALL` for firewall policy rules.  
`port_range[ ]` | string | List of applicable port ranges for firewall policy rules. For example, `8080-9090`.  
  
## InstanceDetails

Field | Type | Description  
---|---|---  
`project_id` | string | ID of the project containing the Compute Engine VM.  
`vm_name` | string | Instance name of the Compute Engine VM.  
`region` | string | Region of the Compute Engine VM.  
`zone` | string | Zone of the Compute Engine VM.  
  
## LoadBalancingDetails

Field | Type | Description  
---|---|---  
`forwarding_rule_project_id` | string | Google Cloud project ID that contains the forwarding rule.  
`type` | string | Load balancer type: `APPLICATION_LOAD_BALANCER` indicates an internal Application Load Balancer. `PROXY_NETWORK_LOAD_BALANCER` indicates an internal proxy Network Load Balancer.  
`scheme` | string | Load balancer scheme, `INTERNAL_MANAGED`.  
`url_map_name` | string | Name of the URL map. Only populated if the `type` is `APPLICATION_LOAD_BALANCER`.  
`forwarding_rule_name` | string | Name of the forwarding rule.  
  
## VpcDetails

Field | Type | Description  
---|---|---  
`project_id` | string | ID of the project containing the network.  
`vpc_name` | string | Network on which the VM is operating.  
`subnetwork_name` | string | Subnet on which the VM is operating.  
  
## GeographicDetails

Field | Type | Description  
---|---|---  
`continent` | string | Continent name for external endpoints.  
`country` | string | Country name for external endpoints.  
`region` | string | Region name for external endpoints.  
`city` | string | City name for external endpoints.  
  
## What's next

  * [ VPC firewall rules logging format](https://docs.cloud.google.com/firewall/docs/vpc-log-format).
  * [Firewall policy rules logging overview](https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-logging-overview).
  * [Manage firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/manage-firewall-policy-rules-logging).
  * [Cloud Logging overview](https://docs.cloud.google.com/logging/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
