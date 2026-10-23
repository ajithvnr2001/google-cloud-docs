---
url: https://docs.cloud.google.com/firewall/docs/url-filtering-logs/
title: URL filtering logs \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:51.292994+00:00
---

# URL filtering logs  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/url-filtering-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  URL filtering logs Stay organized with collections  Save and categorize content based on your preferences. 

The URL filtering service logs let you audit, verify, and analyze the URL-based traffic filtering in your network.

When Cloud Next Generation Firewall performs URL-based filtering on traffic with Layer 7 inspection enabled, it generates a log entry for each connection with details about the connection. Cloud NGFW generates a log entry when the firewall rule with Layer 7 inspection is activated, regardless of whether Cloud Logging is enabled or disabled.

To view and examine the URL filtering logs, in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), search for the log `networksecurity.googleapis.com/firewall_url_filter`.

This page describes the format and structure of the URL filtering logs that Cloud NGFW generates for each connection when it allows or denies traffic.

## URL filtering log format

Cloud NGFW creates a log record entry in [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) for each connection that undergoes URL filtering to monitor traffic to or from a virtual machine (VM) instance in a specific zone. Log records are included in the JSON payload field of a [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry).

Some log fields are in a multiple-field format, with more than one piece of data in a given field. For example, the `connection` field is of the `Connection` format, which contains the server IP address and port, the client IP address and port, and the protocol number in a single field.

The following table describes the format of the URL filtering log fields.

Field  | Type  | Description   
---|---|---  
`connection` | `Connection` | A 5-tuple that describes the connection parameters associated with the traffic that is either allowed or denied based on domain and server name indication (SNI) information.   
`interceptInstance` | `InterceptInstance` | The details of the VM instance where the traffic is either allowed or denied based on domain and SNI information.   
`detectionTime` | `string` | The time (UTC) when the firewall endpoint detects a match for the domain and SNI information.   
`uriMatched` | `string` | The domain against which firewall endpoint detected a match.   
`interceptVpc` | `VpcDetails` | The details of the Virtual Private Cloud (VPC) network associated with the VM instance where the traffic is either allowed or denied based on domain and SNI information.   
`ruleIndex` | `integer` | The index or the order number of the URL filter against which firewall endpoint detected a match.   
`direction` | `string` | The direction of the traffic (either `CLIENT_TO_SERVER` or `SERVER_TO_CLIENT`) for which firewall endpoint detected a match.   
`securityProfileGroupDetails` | `SecurityProfileGroupDetails` | The details of the security profile group applied to the intercepted traffic.   
`denyType` | `string` | The type of information that the firewall endpoint uses to deny a traffic. 

  * `SNI`: the firewall endpoint denied traffic because of a match detected against an SNI.
  * `HOST`: the firewall endpoint denied traffic because of a match detected against the domain information present in the host header field.
  * `URI`: the firewall endpoint denied traffic because of a match detected against a URI.

  
`action` | `string` | The action, either `allow` or `deny`, performed on the traffic that is filtered based on the domain and SNI information. The security profile defines this action. To learn more about the configured action, see [URL filtering security profile](https://docs.cloud.google.com/firewall/docs/about-security-profiles#url-filtering-profile).   
`applicationLayerDetails` | `ApplicationLayerDetails` | The details related to application layer processing.   
`sessionLayerDetails` | `SessionLayerDetails` | The details related to session layer processing.   
  
### `Connection` field format

The following table describes the format of the `Connection` field.

Field  | Type  | Description   
---|---|---  
`clientIp` | `string` | The client IP address. If the client is a Compute Engine VM, `clientIp` is either the primary internal IP address or an address in an alias IP range of the VM's network interface. The external IP address is not shown. The logs show the IP address of the VM instance as observed on the IP header, similar to the TCP dump on the VM instance.   
`clientPort` | `integer` | The client port number.   
`serverIp` | `string` | The server IP address. If the server is a Compute Engine VM, `serverIp` is either the primary internal IP address or an address in an alias IP range of the VM's network interface. The external IP address is not shown even if it is used in making the connection.   
`serverPort` | `integer` | The server port number.   
`protocol` | `string` | The [IP protocol](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) of the connection.   
  
### `InterceptInstance` field format

The following table describes the format of the `InterceptInstance` field.

Field  | Type  | Description   
---|---|---  
`zone` | `string` | The name of zone where VM instance associated with the intercepted traffic is located.   
`vm` | `string` | The name of the VM instance associated with the intercepted traffic.   
`projectId` | `string` | The name of the Google Cloud project associated with the intercepted traffic.   
  
### `VpcDetails` field format

The following table describes the format of the `VpcDetails` field.

Field  | Type  | Description   
---|---|---  
`vpc` | `string` | The name of the VPC network associated with the intercepted traffic.   
`projectId` | `string` | The name of the Google Cloud project associated with the VPC network.   
  
### `SecurityProfileGroupDetails` field format

The following table describes the format of the `SecurityProfileGroupDetails` field.

Field  | Type  | Description   
---|---|---  
`securityProfileGroupId` | `string` | The security profile group name that is applied to the traffic.   
`organizationId` | `string` | The organization ID that the VM instance belongs to.   
  
### `ApplicationLayerDetails` field format

The following table describes the format of the `ApplicationLayerDetails` field.

Field  | Type  | Description   
---|---|---  
`protocol` | `string` | The protocol version that the firewall endpoint uses at the application layer. 

  * `HTTP0`: indicates HTTP version less than 1. The firewall endpoint reads the domain information from the first host header field.
  * `HTTP1`: indicates HTTP version 1._x_. The firewall endpoint reads the domain information from the first host header field.
  * `HTTP2`: indicates HTTP version 2._x_. Because the host header field is optional for this protocol version, the firewall endpoint reads the domain information from either the authority pseudo-header or header blocks of header, continuation, or push_promise frame types.

  
`uri` | `string` | The domain and subdomain information that the firewall endpoint reads from the traffic.   
  
### `SessionLayerDetails` field format

The following table describes the format of the `SessionLayerDetails` field.

Field  | Type  | Description   
---|---|---  
`sni` | `string` | The Server Name Indication (SNI) that the firewall endpoint reads from the traffic.   
`protocolVersion` | `string` | The protocol version that the firewall endpoint uses at the session layer. 

  * `TLS1_0`: indicates TLS version 1.0.
  * `TLS1_1`: indicates TLS version 1.1.
  * `TLS1_2`: indicates TLS version 1.2.
  * `TLS1_3`: indicates TLS version 1.3.

  
  
## URL filtering log correlation with a firewall log

When traffic is evaluated by a firewall rule, Cloud NGFW logs a [firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-logging-overview) entry. This entry includes fields such as the source IP address, the destination IP address, and the time of traffic inspection. To view these firewall rule logs, see [View logs](https://docs.cloud.google.com/firewall/docs/using-firewall-rules-logging#viewing_logs).

If a firewall policy rule with Layer 7 inspection has logging enabled, Cloud NGFW first logs the VPC firewall rules logging entry for the evaluated traffic. Then, it sends the traffic to the firewall endpoint for Layer 7 inspection.

The firewall endpoint analyzes the traffic using its domain and SNI, and creates a separate URL filtering log for the connection. This URL filtering log includes fields such as the domain name, the source of the traffic, and the destination of the traffic.

To view the URL filtering logs, in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), search for the log `networksecurity.googleapis.com/firewall_url_filter`.

You can compare the fields in the [firewall policy rules log](https://docs.cloud.google.com/firewall/docs/firewall-policy-log-format) and URL filtering log to identify the connection that triggered URL filtering and take appropriate action to resolve it.

For example, you have a firewall policy rule configured with the following settings:

  * Source IP address: `192.0.2.0`
  * Source port: `47644`
  * Destination IP address: `192.0.2.1`
  * Destination port: `80`
  * Logging: `Enabled`



To view the URL filtering logs associated with this rule, navigate to the **Logs Explorer** page. In the **Query** pane, paste the following query into the query editor field.
    
    
      resource.type="networksecurity.googleapis.com/FirewallEndpoint"
      jsonPayload.source_ip_address="192.0.2.0"
      jsonPayload.source_port="47644"
      jsonPayload.destination_ip_address="192.0.2.1"
      jsonPayload.destination_port="80"
      

The **Query results** section displays the following URL filtering log:
    
    
        {
          "insertId": "akxp8uf5f0fuv",
          "jsonPayload": {
          "connection": {
          "serverPort": 80,
          "clientPort": 47644,
          "protocol": "TCP",
          "clientIp": "192.0.2.0",
          "serverIp": "192.0.2.1"
        },
          "interceptInstance": {
          "zone": "us-central1-c",
          "vm": "aied-test-dont-delete",
          "projectId": "project_001"
        },
          "detectionTime": "2025-06-02T19:09:27.802711668Z",
          "uriMatched": "",
          "interceptVpc": {
          "projectId": "project_001",
          "vpc": "default"
        },
          "ruleIndex": 0,
          "direction": "CLIENT_TO_SERVER",
          "@type": "type.googleapis.com/google.cloud.networksecurity.logging.v1.URLFilterLog",
          "securityProfileGroupDetails": {
          "securityProfileGroupId": "project_001/spg/my-spg-id",
          "organizationId": "organization_001"
        },
          "denyType": "HOST",
          "action": "DENY",
          "applicationLayerDetails": {
          "protocol": "HTTP1",
          "uri": "server.fwp.com"
        },
          "sessionLayerDetails": {
          "sni": "",
          "protocolVersion": "PROTOCOL_VERSION_UNSPECIFIED"
        }
      },
        "resource": {
        "type": "networksecurity.googleapis.com/FirewallEndpoint",
        "labels": {
          "location": "us-central1-c",
          "resource_container": "organizations/organization_001",
          "id": "pg-ni-latencyayzl8peq"
        }
      },
      "timestamp": "2025-06-02T19:09:35.452299517Z",
      "logName": "projects/project_001/logs/networksecurity.googleapis.com%2Ffirewall_url_filter",
      "receiveTimestamp": "2025-06-02T19:09:35.452299517Z"
    }
       

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
          project_id: "project_001"
          subnetwork_name: "fwplus-us-central1-subnet"
          vpc_name: "fwplus-vpc"
          }
          }
          logName: "projects/project_001/logs/compute.googleapis.com%2Ffirewall",
          receiveTimestamp: "2023-11-28T19:08:46.749244092Z"
          resource: {2}
          timestamp: "2023-11-28T19:08:40.207465099Z"
        }
       

With both the URL filtering log and firewall log queries you can view the correlation between them. The following table maps the firewall log fields to the corresponding URL filtering log fields.

Firewall log field  | URL filtering log field  | Description   
---|---|---  
`src_ip` | `clientIp` | The source IP address in the firewall log is correlated with the client IP address in the URL filtering log to identify the origin of the filtered traffic  
`src_port` | `clientPort` | The source port in the firewall log is correlated with the client port in the URL filtering log to identify the source port used by the filtered traffic  
`dest_ip` | `serverIp` | The destination IP address in the firewall log is correlated with the server IP address in the URL filtering log to pinpoint the target of the filtered traffic  
`dest_port` | `serverPort` | The destination port in the firewall log is correlated with the server port in the URL filtering log to identify the destination port used by the filtered traffic  
  
## What's next

  * [URL filtering service overview](https://docs.cloud.google.com/firewall/docs/about-url-filtering)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
