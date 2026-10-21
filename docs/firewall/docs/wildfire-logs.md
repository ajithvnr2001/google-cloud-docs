---
url: https://docs.cloud.google.com/firewall/docs/wildfire-logs/
title: Advanced malware sandbox logs \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:31.919768+00:00
---

# Advanced malware sandbox logs  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/wildfire-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Advanced malware sandbox logs Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When Cloud Next Generation Firewall Enterprise detects and submits a file to Advanced malware sandbox (WildFire) for analysis, it generates detailed logs that help you audit and analyze malware detection and prevention. These logs provide visibility into network-based threats and sandboxing results.

This page describes the format and structure of the Advanced malware sandbox submission logs.

## Types of Advanced malware sandbox logs

Advanced malware sandbox introduces two main categories of logs:

  * **Submission logs** : generated when an unknown file is evaluated by Advanced malware sandbox. These contain two subtypes:

    * **`wildfire`** : indicates a file was extracted and submitted to the Advanced malware sandbox cloud for asynchronous deep sandboxing.
    * **`inline-wildfire`** : indicates a file was evaluated in real-time by the Advanced malware sandbox inline cloud analysis engine before reaching the network.
  * **Threat logs** : generated when the firewall detects and actively blocks a known or dynamically identified threat inline. These add two new subtypes of threat logs:

    * **`WILDFIRE_VIRUS`** : indicates a virus detected by the Advanced malware sandbox cloud service based on a known signature match.
    * **`ML_VIRUS`** : indicates a virus detected dynamically by the firewall's on-box Advanced malware sandbox inline machine learning (ML) engine.



## View logs

To view and analyze the Advanced malware sandbox logs, see [View all firewall logs](https://docs.cloud.google.com/firewall/docs/manage-firewall-policy-rules-logging#all_firewall_logs).

You can use the following queries in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) query editor field:

  * To view submission logs, enter `type.googleapis.com/google.cloud.networksecurity.logging.v1.WildfireSubmissionLog`.

  * To view threat logs, enter the following query:
        
        type.googleapis.com/google.cloud.networksecurity.logging.v1.ThreatLog
        jsonPayload.threatDetails.type="WILDFIRE_VIRUS" OR jsonPayload.threatDetails.type="ML_VIRUS"
        




## Advanced malware sandbox log format

Cloud Next Generation Firewall Enterprise creates a log entry in Cloud Logging for each file submitted to Advanced malware sandbox. The log records are included in the JSON payload field of a [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) object.

The following table describes the format of the Advanced malware sandbox submission log fields:

Field | Type | Description  
---|---|---  
`connection` | `Connection` | A 5-tuple that describes the connection parameters associated with the traffic.  
`action` | `string` | The action performed on the connection where the file is submitted to Advanced malware sandbox. For example, `allow`, `deny`.  
`wildfireDetails` | `WildFireDetails` | The details of the Advanced malware sandbox file submission and analysis results.  
`securityProfileGroupDetails` | `SecurityProfileGroupDetails` | The details of the security profile group applied to the intercepted traffic.  
`interceptVpc` | `VpcDetails` | The details of the Virtual Private Cloud (VPC) network associated with the intercepted traffic.  
`interceptInstance` | `InterceptInstance` | The details of the virtual machine (VM) instance where the traffic was intercepted.  
  
### `Connection` field format

The following table describes the format of the `Connection` field:

Field | Type | Description  
---|---|---  
`clientIp` | `string` | The client IP address. If the client is a Compute Engine VM instance, `clientIp` is either the primary internal IP address or an address in an alias IP range of the network interface for the VM. The external IP address is omitted. The logs show the IP address of the VM instance as observed on the IP header, similar to the TCP dump on the VM instance.  
`clientPort` | `integer` | The client port number.  
`serverIp` | `string` | The server IP address. If the server is a Compute Engine VM instance, `serverIp` is either the primary internal IP address or an address in an alias IP range of the network interface for the VM. The external IP address is omitted, even if it is used to make the connection.  
`serverPort` | `integer` | The server port number.  
`protocol` | `string` | The [IP protocol](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) of the connection.  
  
### `WildFireDetails` field format

The following table describes the format of the `wildfireDetails` field:

Field | Type | Description  
---|---|---  
`verdict` | `string` | The Advanced malware sandbox verdict on the file. For example, malicious.  
`detectionTime` | `string` | The time the malware was detected.  
`direction` | `string` | The direction of the file transmission. For example, `CLIENT_TO_SERVER`.  
`fileName` | `string` | The name of the file.  
`fileType` | `string` | The type of the file. For example, Linux, PE.  
`hash` | `string` | The Secure Hash Algorithm 256-bit (SHA-256) hash of the file.  
`severity` | `string` | The severity associated with the detected malware. For more information, see [Threat severity levels](https://cloud.google.com/firewall/docs/about-threats#threat-severity-level).  
`repeatCount` | `integer` | The number of sessions with the same client IP address, server IP address, client port, server port, protocol, and domain seen within five seconds.  
`reportUrl` | `string` | A URL to download the Advanced malware sandbox report. This URL generally points to `networksecurity.usercontent.google.com` and contains the organization or project, location, firewall endpoint, and report information.  
`sampleUrl` | `string` | A URL to download the malware sample. This URL generally points to `networksecurity.usercontent.google.com` and contains the organization or project, location, firewall endpoint, and sample information.  
`subtype` | `string` | The subtype of Advanced malware sandbox. For example, wildfire, inline-wildfire.  
**Note:** When using the `reportUrl` or `sampleUrl` from a Advanced malware sandbox submission log from a project-level endpoint, you must replace the project ID with the project number.

### `SecurityProfileGroupDetails` field format

The following table describes the format of the `SecurityProfileGroupDetails` field:

Field | Type | Description  
---|---|---  
`securityProfileGroupId` | `string` | The security profile group name that is applied to the traffic.  
`organizationId` | `string` | The organization ID that the VM instance belongs to.  
  
### `VpcDetails` field format

The following table describes the format of the `VpcDetails` field:

Field | Type | Description  
---|---|---  
`vpc` | `string` | The name of the VPC network associated with the intercepted traffic  
`projectId` | `string` | The name of the Google Cloud project associated with the VPC network.  
  
### `InterceptInstance` field format

The following table describes the format of the `InterceptInstance` field:

Field | Type | Description  
---|---|---  
`zone` | `string` | The name of the zone where the VM instance is located.  
`vm` | `string` | The name of the VM instance associated with the intercepted traffic.  
`projectId` | `string` | The name of the Google Cloud project associated with the VPC network.  
  
## Advanced malware sandbox log correlation with firewall logs

When traffic is evaluated by a firewall rule, Cloud NGFW records a [firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-logging-overview) entry. For more information, see Advanced malware sandbox log format. To view these firewall rule logs, see [View logs](https://docs.cloud.google.com/firewall/docs/using-firewall-rules-logging#viewing_logs).

When firewall policy rule with Layer 7 inspection has logging enabled, Cloud NGFW first records a VPC firewall rules logging entry for the evaluated traffic. Then, it sends the traffic to the firewall endpoint for Layer 7 inspection. For more information, see [Enable or disable firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/manage-firewall-policy-rules-logging#enable-and-disable-firewall-policy-rules-logging)

The firewall endpoint analyzes the traffic for files to submit to Advanced malware sandbox, and creates a separate Advanced malware sandbox submission log for the connection. This Advanced malware sandbox submission log includes fields such as the filename, the file hash, the source of the traffic, and the destination of the traffic.

To view the Advanced malware sandbox submission logs, in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), search for the log `networksecurity.googleapis.com%2Ffirewall_wildfire`.

You can compare the fields in the [firewall policy rules log](https://docs.cloud.google.com/firewall/docs/firewall-policy-log-format) and the Advanced malware sandbox log format to identify the connection that triggered Advanced malware sandbox file submission and take appropriate action to resolve it.

For example, you have a firewall policy rule configured with the following settings:

  * Source IP address: `192.0.2.0`
  * Source port: `47644`
  * Destination IP address: `192.0.2.1`
  * Destination port: `80`
  * Logging: `Enabled`



To view the Advanced malware sandbox submission logs associated with this rule, navigate to the **Logs Explorer** page. In the **Query** pane, paste the following query into the query editor field.
    
    
      resource.type="networksecurity.googleapis.com/FirewallEndpoint"
      jsonPayload.connection.clientIp="192.0.2.0"
      jsonPayload.connection.clientPort="47644"
      jsonPayload.connection.serverIp="192.0.2.1"
      jsonPayload.connection.serverPort="80"
      

The **Query results** section displays the following Advanced malware sandbox submission log:
    
    
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
          "interceptVpc": {
          "projectId": "project_001",
          "vpc": "default"
        },
          "@type": "type.googleapis.com/google.cloud.networksecurity.logging.v1.WildfireSubmissionLog",
          "securityProfileGroupDetails": {
          "securityProfileGroupId": "project_001/spg/my-spg-id",
          "organizationId": "organization_001"
        },
          "action": "DENY",
          "wildfireDetails": {
            "detectionTime": "2026-04-19T21:18:50Z",
            "direction": "SERVER_TO_CLIENT",
            "fileName": "sheet.exe",
            "fileType": "PE",
            "hash": "02521f0bb91b4c74d1590b85254f26f0d258cd780393010593ae6daaa5993753",
            "repeatCount": 1,
            "reportUrl": "https://networksecurity.usercontent.google.com/projects/12345/locations/us-west2-a/firewallEndpoints/prober-wfmixed-fwp-ep-us-w2-a/wildfireReports/C08DD6908D91EAB335FA89675E499631557B3126ADFF9C83A1856D4404D2F4A2",
            "sampleUrl": "https://networksecurity.usercontent.google.com/projects/12345/locations/us-west2-a/firewallEndpoints/prober-wfmixed-fwp-ep-us-w2-a/wildfireSamples/C08DD6908D91EAB335FA89675E499631557B3126ADFF9C83A1856D4404D2F4A2",
            "severity": "INFORMATIONAL",
            "subtype": "WILDFIRE",
            "verdict": "MALICIOUS"
          },
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
      "logName": "projects/project_001/logs/networksecurity.googleapis.com%2Ffirewall_wildfire",
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
       

By using both the Advanced malware sandbox submission log and firewall log queries, you can see the correlation between them. The following table maps the firewall log fields to the corresponding Advanced malware sandbox submission log fields:

Firewall log field  | Advanced malware sandbox submission log field  | Description   
---|---|---  
`src_ip` | `clientIp` | The source IP address in the firewall log is correlated with the client IP address in the Advanced malware sandbox submission log to identify the origin of the evaluated traffic.  
`src_port` | `clientPort` | The source port in the firewall log is correlated with the client port in the Advanced malware sandbox submission log to identify the source port used by the evaluated traffic.  
`dest_ip` | `serverIp` | The destination IP address in the firewall log is correlated with the server IP address in the Advanced malware sandbox submission log to pinpoint the target of the evaluated traffic.  
`dest_port` | `serverPort` | The destination port in the firewall log is correlated with the server port in the Advanced malware sandbox submission log to identify the destination port used by the evaluated traffic.  
  
## What's next

  * [Advanced malware sandbox overview](https://docs.cloud.google.com/firewall/docs/about-wildfire)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
