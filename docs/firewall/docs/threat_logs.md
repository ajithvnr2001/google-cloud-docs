---
url: https://docs.cloud.google.com/firewall/docs/threat_logs/
title: Threat logs \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:31.804614+00:00
---

# Threat logs  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/threat_logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Threat logs Stay organized with collections  Save and categorize content based on your preferences. 

Threat logs let you audit, verify, and analyze the threats detected in your network.

When Cloud Next Generation Firewall (Cloud NGFW) detects a threat on the traffic being monitored for Layer 7 inspection, it generates a log entry in the originating project with the details of the threat. To view and examine the threat logs, in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), search for the log `networksecurity.googleapis.com/firewall_threat`. You can also view these threat logs on the [**Threats** page](https://docs.cloud.google.com/firewall/docs/view-threats).

This page explains the format and structure of the threat logs that are generated when a threat is detected.

## Threat log format

Cloud NGFW creates a log record entry in [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) for each threat detected on the monitored traffic to or from a virtual machine (VM) instance in a specific zone. Log records are included in the JSON payload field of a [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

Some log fields are in a multiple-field format, with more than one piece of data in a given field. For example, the `connection` field is of the `Connection` format, which contains the server IP address and port, the client IP address and port, and the protocol number in a single field.

The following table describes the format of the threat log fields.

Field  | Type  | Description   
---|---|---  
`connection` | `Connection` | A 5-tuple that describes the connection parameters associated with the traffic where the threat is detected.   
`action` | `string` | The action performed on the packet where the threat is detected. This action can either be the [default action](https://docs.cloud.google.com/firewall/docs/about-threats#default-threat-signatures) or the [override action](https://docs.cloud.google.com/firewall/docs/about-security-profiles#threat-prevention-profile) specified in the security profile. **Note** : When a threat is detected with the `DENY` override action, the `action` field displays `DROP` as the packet is dropped, and an alert is generated.   
`threatDetails` | `ThreatDetails` | The details of the threat detected.   
`securityProfileGroupDetails` | `SecurityProfileGroupDetails` | The details of the security profile group applied to the intercepted traffic.   
`interceptVpc` | `VpcDetails` | The details of the Virtual Private Cloud (VPC) network associated with the VM instance or the load balancer where the threat is detected. For both VM instances and load balancer forwarding rules, the project that owns the VPC network serves as the logging project.  
`interceptInstance` | `InterceptInstance` | The details of the VM instance where the threat is detected.   
`interceptLoadBalancer` | [`LoadBalancingDetails`](https://docs.cloud.google.com/firewall/docs/firewall-policy-log-format#loadbalancingdetails) | The details of the load balancer where the threat is detected and the firewall rule is applied.   
  
### `Connection` field format

The following table describes the format of the `Connection` field.

Field  | Type  | Description   
---|---|---  
`clientIp` | `string` | The client IP address. If the client is a Compute Engine VM, `clientIp` is either the primary internal IP address or an address in an alias IP range of the VM's network interface. The external IP address is not shown. The logs show the IP address of the VM instance as observed on the packet header, similar to the TCP dump on the VM instance.   
`clientPort` | `integer` | The client port number.   
`serverIp` | `string` | The server IP address. If the server is a Compute Engine VM, `serverIp` is either the primary internal IP address or an address in an alias IP range of the VM's network interface. The external IP address is not shown even if it is used in making the connection.   
`serverPort` | `integer` | The server port number.   
`protocol` | `string` | The [IP protocol](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) of the connection.   
  
### `ThreatDetails` field format

The following table describes the format of the `ThreatDetails` field.

Field  | Type  | Description   
---|---|---  
`id` | `string` | The unique Palo Alto Networks threat identifier.   
`threat` | `string` | The name of the threat detected.   
`description` | `string` | A detailed description of the threat detected.   
`direction` | `string` | The direction of the traffic. For example, `client_to_server` or `server_to_client`.   
`application` | `string` | The application associated with the threat detected.   
`severity` | `string` | The severity associated with the threat detected. For more information, see [Threat severity levels](https://docs.cloud.google.com/firewall/docs/about-threats#threat-severity-level).   
`detectionTime` | `string` | The time when the threat is detected.   
`category` | `string` | The subtype of the threat detected. For example, `CODE_EXECUTION`.   
`uriOrFilename` | `string` | The URI or filename of the relevant threat (if applicable).   
`type` | `string` | The type of the threat detected. For example, `SPYWARE`.   
`repeatCount` | `integer` | The number of sessions with the same client IP address, server IP address, and threat type seen within five seconds.   
`cves` | `string` | A list of [Common Vulnerabilities and Exposure (CVEs)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) associated with the threat. For example, `CVE-2021-44228-Apache Log4j remote code execution vulnerability`.   
  
### `SecurityProfileGroupDetails` field format

The following table describes the format of the `SecurityProfileGroupDetails` field.

Field  | Type  | Description   
---|---|---  
`securityProfileGroupId` | `string` | The security profile group name that is applied to the traffic.   
`organizationId` | `integer` | The organization ID that the VM instance belongs to.   
  
### `VpcDetails` field format

The following table describes the format of the `VpcDetails` field.

Field  | Type  | Description   
---|---|---  
`vpc` | `string` | The name of the VPC network associated with the intercepted traffic.   
`projectId` | `string` | The name of the Google Cloud project associated with the VPC network.   
  
### `InterceptInstance` field format

The following table describes the format of the `InterceptInstance` field.

Field  | Type  | Description   
---|---|---  
`projectId` | `string` | The name of the Google Cloud project associated with the intercepted traffic.   
`vm` | `string` | The name of the VM instance associated with the intercepted traffic.   
  
## Threat log correlation with a firewall log

When a packet matches a firewall rule with logging enabled, Cloud NGFW logs a [firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-logging-overview) entry. This entry includes fields such as the source IP address, the destination IP address, and the time of packet inspection. To view these firewall rule logs, see [View logs](https://docs.cloud.google.com/firewall/docs/manage-firewall-policy-rules-logging#viewing_logs).

If you have a firewall policy rule for Layer 7 inspection with logging enabled, Cloud NGFW first logs the VPC firewall rules logging entry for the matched packet. Then, it sends the packet to the firewall endpoint for Layer 7 inspection. The firewall endpoint analyzes the traffic and generates specific threat or [URL filtering logs](https://docs.cloud.google.com/firewall/docs/url-filtering-logs). If a threat is detected, a separate threat log is created. This threat log include fields such as the type of threat, the source of the threat, and the destination of the threat. To view threat logs, see [View threats](https://docs.cloud.google.com/firewall/docs/view-threats#view-threats).

**Note:** The firewall rule logs appear once at the start of a session, whereas inspection logs record specific connections or threats detected during the session.

You can compare the fields in the [firewall policy rule log](https://docs.cloud.google.com/firewall/docs/firewall-policy-log-format) and threat log to identify the packet that triggered the threat and take appropriate action to resolve it.

For example, you have a firewall policy rule configured with the following settings:

  * Source IP address: `192.0.2.0`
  * Source port: `47644`
  * Destination IP address: `192.0.2.1`
  * Destination port: `80`
  * Logging: `Enabled`



To view the threat logs associated with this rule, navigate to the **Logs Explorer** page. In the **Query** pane, paste the following query into the query editor field.
    
    
        resource.type="networksecurity.googleapis.com/FirewallEndpoint"
        jsonPayload.source_ip_address="192.0.2.0"
        jsonPayload.source_port="47644"
        jsonPayload.destination_ip_address="192.0.2.1"
        jsonPayload.destination_port="80"
       

The **Query results** section displays the following threat log:
    
    
        {
          insertId: "0ac7f359-263f-4428-8ded-ac655d8a09db"
          jsonPayload: {
          action: "reset-server"
          alert_severity: "HIGH"
          alert_time: "2023-11-28T19:07:15Z"
          category: "info-leak"
          ▸ cves: [6]
          }
          destination_ip_address: "192.0.2.1"
          destination_port: "80"
          details:
          "This signature detects Microsoft Windows win.ini access attempts. A successful attack could allow an
          attacker to access sensitive information and conduct further attacks."
          direction: "CLIENT_TO_SERVER"
          ip_protocol: "tcp"
          name: "Microsoft Windows win.ini Access Attempt Detected"
          network: "projects/XXXX/global/networks/fwplus-vpc.
          repeat_count: "1"
          security_profile_group:
          "organizations/XXXX/locations/global/securityprofileGroups/XXXX-fwplus-spg"
          source_ip_address: "192.0.2.0"
          source_port: "47644"
          threat_id: "30851"
          type: "vulnerability"
          uri_or_filename:
          logName: "projects/XXXX/logs/networksecurity.googleapis.com%2Ffirewall_threat"
          receiveTimestamp: "2023-11-28T19:08:49.841883684Z"
          ▸ resource: {2}
        }
        timestamp: "2023-11-28T19:08:47.560012184Z"
       

Similarly, to view the firewall logs associated with this rule, navigate to the **Logs Explorer** page. In the **Query** pane, paste the following query into the query editor field.
    
    
        jsonPayload.rule_details.action="APPLY_SECURITY_PROFILE_GROUP"
        jsonPayload.connection.src_ip="192.0.2.0"
        jsonPayload.connection.src_port="47644"
        jsonPayload.connection.dest_ip="192.0.2.1"
        jsonPayload.connection.dest_port="80"
       

The **Query results** section displays the following firewall log:
    
    
        {
          insertId: "qn82vdg109q3r9"
          jsonPayload: {
          connection: {
          }
          dest_ip: "192.0.2.1"
          dest_port: 80
          protocol: 6
          src_ip: "192.0.2.0"
          src_port: 47644
          disposition: "INTERCEPTED"
          ►instance: {4}
          ▸ remote_instance: {4}
          ▸ remote_vpc: {3}
          rule_details: {
          action: "APPLY_SECURITY_PROFILE_GROUP"
          apply_security_profile_fallback_action: "UNSPECIFIED"
          direction: "INGRESS"
          ▸ ip_port_info: [1]
          ▼
          priority: 6000
          reference: "network: fwplus-vpc/firewallPolicy: fwplus-fwpolicy"
          source_range: [
          1
          0: "192.0.2.0/24"
          target_secure_tag: [
          0: "tagValues/281479199099651"
          ]
          }
          vpc: {
          project_id:XXXX
          subnetwork_name: "fwplus-us-central1-subnet"
          vpc_name: "fwplus-vpc"
          }
          }
          logName: "projects/XXXX/logs/compute.googleapis.com%2Ffirewall",
          receiveTimestamp: "2023-11-28T19:08:46.749244092Z"
          resource: {2}
          timestamp: "2023-11-28T19:08:40.207465099Z"
        }
       

With both the threat log and firewall log queries you can view the correlation between them. The following table maps the firewall log fields to the corresponding threat log fields.

Firewall log field  | Threat log field  | Description   
---|---|---  
`src_ip` | `source_ip_address` | The source IP address in the firewall log is correlated with the source IP address in the threat log to identify the origin of the potential threat  
`src_port` | `source_port` | The source port in the firewall log is correlated with the source port in the threat log to identify the source port used in the potential threat  
`dest_ip` | `destination_ip_address` | The destination IP address in the firewall log is correlated with the destination IP address in the threat log to pinpoint the target of the potential threat  
`dest_port` | `destination_port` | The destination port in the firewall log is correlated with the destination port in the threat log to identify the destination port used in the potential threat  
  
## What's next

  * [View threats](https://docs.cloud.google.com/firewall/docs/view-threats)
  * [Threat signatures overview](https://docs.cloud.google.com/firewall/docs/about-threats)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
