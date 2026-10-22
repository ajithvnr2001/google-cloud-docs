---
url: https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-log-examples/
title: Firewall policy rules logging examples \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:46.658998+00:00
---

# Firewall policy rules logging examples  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-log-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Firewall policy rules logging examples Stay organized with collections  Save and categorize content based on your preferences. 

Firewall policy rules generate log entries when they apply to traffic. While a packet flow can generate multiple log entries, firewall policy rule generates at most one log entry per connection from a virtual machine (VM) instance.

The following examples show how firewall policy rules logging works, including behaviors that differ from legacy Virtual Private Cloud (VPC) firewall rules, such as repeat logging for denied connections and session-based logging for advanced inspection.

## Egress deny example

In this example, traffic flows between two VM instances in the `example-net` VPC network in the `example-proj` project.

  * VM1 in zone `us-west1-a` with IP address `10.10.0.99` in the `west-subnet` (`us-west1` region).
  * VM2 in zone `us-east1-b` with IP address `10.20.0.99` in the `east-subnet` (`us-east1` region).
  * Rule A: An egress deny firewall rule has a target of all instances in the network, a destination of `10.20.0.99` (VM2), and applies to TCP port `80`. Logging is enabled for this rule.
  * Rule B: An ingress allow firewall rule has a target of all instances in the network, a source of `10.10.0.99` (VM1), and applies to TCP port `80`. Logging is also enabled for this rule.



To create the firewall policy rule, see [Firewall policy rule tasks](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#rule_tasks).

In a scenario where VM1 attempts to connect to VM2 on TCP port `80`, the following happens:

  * The firewall generates a log entry for rule A from VM1's perspective for the failed connection attempt.

  * Because rule A is a `DENY` rule, the firewall logs each packet corresponding to the unique 5-tuple as a failed connection attempt. If the firewall continues to receive packets for this connection, it repeats the same log entry every 5 seconds.

  * Because rule A blocks the traffic at the source, the firewall doesn't consider rule B. Therefore, it generates no log entry for rule B from VM2's perspective.




VM1 reports the following firewall log record:

Field | Values  
---|---  
`connection` | src_ip=10.10.0.99  
src_port=[EPHEMERAL_PORT]  
dest_ip=10.20.0.99  
dest_port=80  
protocol=6  
`disposition` | DENIED  
`rule_details` | reference = "network:example-net/firewallPolicy:12345"  
priority = 10  
action = DENY  
destination_range = 10.20.0.99/32  
ip_port_info = tcp:80  
direction = egress  
`instance` | project_id="example-proj"  
instance_name=VM1  
region=us-west1  
zone=us-west1-a  
  
## Egress allow, ingress allow example

In this example, traffic flows between VM instances in the `example-net` VPC network in the `example-proj` project.

  * VM1 in zone `us-west1-a` with IP address `10.10.0.99` in the `west-subnet` (`us-west1` region).
  * VM2 in zone `us-east1-b` with IP address `10.20.0.99` in the `east-subnet` (`us-east1` region).
  * Rule A: A global network firewall policy egress allow rule has a destination of `10.20.0.99` (VM2), and applies to TCP port `80`. Logging is enabled for this rule.
  * Rule B: A global network firewall policy ingress allow rule has a source of `10.10.0.99` (VM1), and applies to TCP port `80`. Logging is enabled for this rule.



To create the firewall policy rule, see [Firewall policy rule tasks](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#rule_tasks).

In a scenario where VM1 attempts to connect to VM2 on TCP port `80`, the following happens:

  * The firewall generates a log entry for rule A from VM1's perspective while VM1 connects to `10.20.0.99`. Because it is an `ALLOW` rule, the connection is logged only once and isn't repeated.
  * The firewall generates a log entry for rule B from VM2's perspective while VM2 allows incoming connections from `10.10.0.99`.



VM1 reports the following firewall log record:

Field | Values  
---|---  
`connection` | src_ip=10.10.0.99  
src_port=[EPHEMERAL_PORT]  
dest_ip=10.20.0.99  
dest_port=80  
protocol=6  
`disposition` | ALLOWED  
`rule_details` | reference = "network:example-net/firewallPolicy:12345"  
priority = 10  
action = ALLOW  
destination_range = 10.20.0.99/32  
ip_port_info = tcp:80  
direction = egress  
  
VM2 reports the following firewall log record:

Field | Values  
---|---  
`connection` | src_ip=10.10.0.99  
src_port=[EPHEMERAL_PORT]  
dest_ip=10.20.0.99  
dest_port=80  
protocol=6  
`disposition` | ALLOWED  
`rule_details` | reference = "network:example-net/firewallPolicy:67890"  
priority = 10  
action = ALLOW  
source_range = 10.10.0.99/32  
ip_port_info = tcp:80  
direction = ingress  
  
## Internet ingress example

In this example, traffic flows from an external resource to a VM instance within the `example-net` VPC network. The network is in the `example-proj` project.

  * The system on the internet has IP address `203.0.113.114`.
  * VM1 in zone `us-west1-a` has IP address `10.10.0.99` in the `west-subnet` (`us-west1` region).
  * Rule C: An ingress allow firewall policy rule has a source of any IP address (`0.0.0.0/0`), and applies to TCP port `80`. Logging is enabled for this rule.
  * Rule D: An egress deny firewall policy rule has a destination of any IP address (`0.0.0.0/0`), and applies to all protocols. Logging is enabled for this rule.



To create the firewall policy rule, see [Firewall policy rule tasks](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#rule_tasks).

In a scenario where the system with IP address `203.0.113.114` attempts to connect to VM1 on TCP port `80`, the following happens:

  * VM1 generates a log entry for rule C as it accepts traffic from `203.0.113.114`.
  * Cloud Next Generation Firewall (Cloud NGFW) policy rules are stateful, which means that if an incoming (ingress) firewall rule allows traffic to a VM instance, the outgoing (egress) return traffic is automatically permitted. In this case, rule C allows ingress traffic, so VM1 can send reply traffic to `203.0.113.114` despite rule D.
  * Connection tracking allows reply traffic and doesn't cause any logging, regardless of egress firewall rules. Therefore, the firewall doesn't consider rule D and generates no egress log entry.



VM1 reports the following firewall log record:

Field | Values  
---|---  
`connection` | src_ip=203.0.113.114  
src_port=[EPHEMERAL_PORT]  
dest_ip=10.10.0.99  
dest_port=80  
protocol=6  
`disposition` | ALLOWED  
`rule_details` | reference = "network:example-net/firewallPolicy:12345"  
priority = 10  
action = ALLOW  
source_range = 0.0.0.0/0  
ip_port_info = tcp:80  
direction = ingress  
`remote_location` | continent  
country  
region  
city  
  
## Advanced inspection example

In this example, Cloud NGFW firewall policy uses the `apply_security_profile_group` action to intercept traffic for deep packet inspection.

  * The system on the internet has IP address `203.0.113.114`.
  * VM1 in zone `us-west1-a` with IP address `10.10.0.99` in the `west-subnet` (`us-west1` region).
  * Rule E: An egress firewall policy rule with the action set to `apply_security_profile_group`. Logging is enabled for this rule.



To create the firewall policy rule for advanced inspection, see [Security profile overview](https://docs.cloud.google.com/firewall/docs/about-security-profiles).

Suppose VM1 sends traffic that matches rule E. The following happens:

  * The `apply_security_profile_group` action uses session-based logging, which differs from the connection-based logs produced by standard `allow` or `deny` rules.

  * Cloud NGFW generates a single firewall rule log entry for the initial session that matches the rule, confirming that the traffic was successfully intercepted and redirected to the firewall endpoint. Cloud NGFW generates this high-level log even if multiple connections are identified as part of the same session.




VM1 reports the following firewall log record:

Field | Values  
---|---  
`connection` | src_ip=10.10.0.99  
src_port=[EPHEMERAL_PORT]  
dest_ip=203.0.113.114  
dest_port=80  
protocol=6  
`disposition` | INTERCEPTED  
`rule_details` | reference = "network:example-net/firewallPolicy:12345"  
priority = 10  
action = APPLY_SECURITY_PROFILE_GROUP  
apply_security_profile_fallback_action = UNSPECIFIED  
destination_range = 0.0.0.0/0  
direction = egress  
**Note:** When the firewall intercepts a connection with the `apply_security_profile_group` action, it records `disposition` as `INTERCEPTED`. Firewall then sets the `apply_security_profile_fallback_action` field to `UNSPECIFIED`.

## What's next

  * [Use firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/using-firewall-rules-logging)
  * [Firewall Insights](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/overview)
  * [Logging overview](https://docs.cloud.google.com/logging/docs/overview)
  * [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
