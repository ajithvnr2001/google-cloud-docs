---
url: https://docs.cloud.google.com/firewall/docs/vpc-log-format/
title: VPC firewall rules logging format \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:30.880261+00:00
---

# VPC firewall rules logging format  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/vpc-log-format/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  VPC firewall rules logging format Stay organized with collections  Save and categorize content based on your preferences. 

VPC firewall rules logging records network traffic information to help you query, analyze, and troubleshoot rule matches on your Google Cloud Virtual Private Cloud (VPC) network. This document describes the log format and field structure for VPC firewall rules logging.

Cloud Logging structures firewall log records by using base and metadata fields, which you use to identify network misconfigurations and optimize rule performance. Log records appear in the JSON payload field of a Logging [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

This document is intended for network administrators, security engineers, and operations analysts who query, review, and analyze network firewall logs.

## Supported log fields

The following table describes the log fields supported for VPC firewall rules.

Field name | Field type: base or optional metadata | Description  
---|---|---  
`connection` | Base | IpConnection  
5-Tuple describing the source and destination IP address, source and destination port, and IP protocol of this connection.  
`disposition` | Base | Indicates whether the connection was `ALLOWED` or `DENIED`.  
`rule_details` | Base | RuleDetails  
VPC firewall rule details. For VPC firewall rules, the format is `network:{network name}/firewall:{firewall_name}`.  
`instance` | Metadata | InstanceDetails  
VM instance details. In a Shared VPC configuration, `project_id` corresponds to that of the service project.  
`load_balancer_details` | Metadata | LoadBalancingDetails  
Details of the internal Application Load Balancer or internal proxy Network Load Balancer to which the firewall rule applies. When the target of a firewall rule is one of these load balancers, the `instance` field is omitted.  
`vpc` | Metadata | VpcDetails  
VPC network details. In a Shared VPC configuration, `project_id` corresponds to that of the host project.  
`remote_instance` | Metadata | InstanceDetails  
If the remote endpoint of the connection was a VM located in the Compute Engine, this field is populated with VM instance details.  
`remote_vpc` | Metadata | VpcDetails  
If the remote endpoint of the connection was a VM that is located in a VPC network, this field is populated with the network details.  
`remote_location` | Metadata | GeographicDetails  
If the remote endpoint of the connection was external to the VPC network, this field is populated with available location metadata.  
  
## IpConnection

Field | Type | Description  
---|---|---  
`src_ip` | string | The source IP address. If the source is a Compute Engine VM, `src_ip` is either the primary internal IP address or an address in an alias IP range of the VM's network interface. The external IP address is not shown. Logging shows the IP address of the VM as the VM sees it on the packet header, the same as if you ran `tcpdump` on the VM.  
`src_port` | integer | The source port.  
`dest_ip` | string | The destination IP address. If the destination is a Google Cloud VM, `dest_ip` is either the primary internal IP address or an address in an alias IP range of the VM's network interface. The external IP address is not shown even if it was used in making the connection.  
`dest_port` | integer | The destination port.  
`protocol` | integer | [IP protocol](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) of the connection.  
  
## RuleDetails

Field | Type | Description  
---|---|---  
`reference` | string | A unique identifier string referring to a resource-named firewall rule bound to a single VPC network. The format for VPC firewall rule is:  
`network:{network name}/firewall:{VPC firewall rule name}`.  
`priority` | integer | The priority for the VPC firewall rule.  
`action` | string | Action applied to the connection. Supported values are `ALLOW` or `DENY`.  
`direction` | string | The direction that the VPC firewall rule applies to. It can be `INGRESS` or `EGRESS`  
`source_range[ ]` | string | List of source ranges that theVPC firewall rule applies to.  
`destination_range[ ]` | string | List of destination ranges that the VPC firewall rule applies to.  
`ip_port_info[ ]` | string | List of IP protocols and applicable port ranges for rules.  
`source_tag[ ]` | string | Lists of source network tags the VPC firewall rule applies to.  
`target_tag[ ]` | string | Lists of target network tags the VPC firewall rule applies to.  
`source_service_account[ ]` | string | List of all the source service accounts that the VPC firewall rule applies to.  
`target_service_account[ ]` | string | List of all the target service accounts that the VPC firewall rule applies to.  
  
## IpPortDetails

Field | Type | Description  
---|---|---  
`ip_protocol` | string | IP protocol that the VPC firewall rule applies to. Can be set to `ALL` if the rule applies to all IP protocols.  
`port_range[ ]` | string | List of applicable port ranges for VPC firewall rules. For example, `8080-9090`.  
  
## InstanceDetails

Field | Type | Description  
---|---|---  
`project_id` | string | ID of the project containing the VM.  
`vm_name` | string | Instance name of the VM.  
`region` | string | Region of the VM.  
`zone` | string | Zone of the VM.  
  
## LoadBalancingDetails

Field | Type | Description  
---|---|---  
`forwarding_rule_project_id` | string | Google Cloud project ID that contains the forwarding rule. Sent when the load balancer is the target instead of a VM.  
`type` | string | Load balancer type: `APPLICATION_LOAD_BALANCER` indicates an internal Application Load Balancer. `PROXY_NETWORK_LOAD_BALANCER` indicates an internal proxy Network Load Balancer. Sent when the load balancer is the target instead of a VM.  
`scheme` | string | Load balancer scheme, `INTERNAL_MANAGED`. Sent when the load balancer is the target instead of a VM.  
`url_map_name` | string | Name of the URL map. Only populated if the `type` is `APPLICATION_LOAD_BALANCER`. Sent when the load balancer is the target instead of a VM.  
`forwarding_rule_name` | string | Name of the forwarding rule. Sent when the load balancer is the target instead of a VM.  
  
## VpcDetails

Field | Type | Description  
---|---|---  
`project_id` | string | ID of the project containing the network.  
`vpc_name` | string | Network on which the VM is operating.  
`subnetwork_name` | string | Subnet on which the VM is operating.  
  
## GeographicDetails

Field | Type | Description  
---|---|---  
`continent` | string | Name of the continent. Its applicable if the remote endpoint of the connection is external to the VPC.  
`country` | string | Name of the country. Its applicable if the remote endpoint of the connection is external to the VPC.  
`region` | string | Name of the region. Its applicable if the remote endpoint of the connection is external to the VPC.  
`city` | string | Name of the city. It's applicable if the remote endpoint of the connection is external to the VPC.  
  
## What's next

  * [Firewall policy rules logging format](https://docs.cloud.google.com/firewall/docs/firewall-policy-log-format).
  * [ VPC firewall rules logging overview](https://docs.cloud.google.com/firewall/docs/vpc-firewall-rules-logging-overview).
  * [Manage VPC firewall rules logging](https://docs.cloud.google.com/firewall/docs/manage-vpc-firewall-rules-logging).
  * [Cloud Logging](https://docs.cloud.google.com/logging/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
