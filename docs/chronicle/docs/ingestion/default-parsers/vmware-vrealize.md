---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vrealize/
title: Collect VMware Aria Suite (formerly VMware vRealize Suite) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:43.323786+00:00
---

# Collect VMware Aria Suite (formerly VMware vRealize Suite) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vrealize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect VMware Aria Suite (formerly VMware vRealize Suite) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide explains how to ingest VMware Aria Suite (formerly known as VMware vRealize Suite) logs to Google Security Operations using Bindplane.

VMware Aria Suite (formerly VMware vRealize Suite, now available as part of VMware Cloud Foundation and vSphere Foundation) is a cloud management platform that provides operations management, automation, log analytics, and network visibility for hybrid and multi-cloud environments. The parser extracts fields from syslog messages using grok patterns based on the `msg_type` field, maps them to the Unified Data Model (UDM), and enriches the data with network information, user details, and resource attributes.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the VMware Aria Suite environment
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to VMware Aria Operations (or VMware Aria Suite)



## Get Google SecOps credentials for the Bindplane agent

To authenticate the Bindplane agent to Google SecOps, choose one of the following methods:

  * **New deployments** : Use the Chronicle API (Option 1).
  * **Legacy deployments** : Continue using the ingestion authentication file (Option 2) until the Ingestion API is discontinued on July 20, 2027.



### Option 1: Create a service account for the Chronicle API (recommended)

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/) and select the Google Cloud project that is linked to your Google SecOps instance.
  2. Go to **IAM & Admin > Service Accounts**.
  3. Click **Create service account**.
  4. Provide the following configuration details: 
     * **Service account name** : Enter a name for the account (for example, `bindplane-ingest`).
     * **Service account description** : Enter a description (for example, `Bindplane agent log ingestion`).
  5. Click **Create and continue**.
  6. In the **Grant this service account access to project** section, click **Select a role** and select **Chronicle Editor**.
  7. Click **Continue** , and then click **Done**.
  8. Click the service account you created, and then go to the **Keys** tab.
  9. Click **Add key > Create new key**.
  10. Select **JSON** and click **Create**. The key file is downloaded to your computer.
  11. Save the key file as `ingestion-auth.json` in the Bindplane collector directory (`/opt/observiq-otel-collector/ingestion-auth.json` on Linux or `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json` on Windows), or update `creds_file_path` in `config.yaml` to match the path where you save it.
  12. Go to **IAM & Admin > Settings** and copy the **Project number**. You'll need it for the exporter configuration.

**Note:** The JSON key is a credential. Restrict access to the file on the Bindplane host and rotate the key according to your organization's policy.

### Option 2: Download the ingestion authentication file (legacy)

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This file authenticates the agent to the legacy Ingestion API (`malachiteingestion-pa.googleapis.com`), which Google has scheduled for end of life on July 20, 2027. Plan to move to Option 1 before that date.

## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** The customer ID is required for configuring the Bindplane agent exporter.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         




The service should show as **active (running)**.

### Additional installation resources

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/vmware_vrealize:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: VMWARE_VREALIZE
            raw_log_field: body
        
        service:
          pipelines:
            logs/vmware_vrealize_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/vmware_vrealize
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on:

      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1):

      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console

    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

    * `endpoint`: Keep set to `chronicle.googleapis.com`.




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/vmware_vrealize:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: VMWARE_VREALIZE
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux:

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows:

  1. Choose one of the following options:

     * Command Prompt or PowerShell as administrator:
    
    net stop observiq-otel-collector && net start observiq-otel-collector
    

     * Services console:

       1. Press `Win+R`, type `services.msc`, and press Enter.
       2. Locate **observIQ OpenTelemetry Collector**.
       3. Right-click and select **Restart**.
  2. Verify the service is running:
         
         sc query observiq-otel-collector
         

  3. Check logs for errors:
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         




## Configure syslog forwarding in VMware Aria Operations

  1. Sign in to the **VMware Aria Operations** web UI.
  2. Go to **Administration > Management > Outbound Settings**.
  3. Click **Add**.
  4. In the **Plugin Type** dropdown, select **Syslog**.
  5. Provide the following configuration details:

     * **Instance Name** : Enter a unique name to identify the syslog destination (for example, `Chronicle-Bindplane`).
     * **Node** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514`.
     * **Protocol** : Select **UDP**.
  6. Click **Test** to verify the connection to the Bindplane agent.

  7. Click **Save** to apply the outbound syslog settings.

**Note:** Ensure that VMware Aria Operations is configured to send logs in UTC timezone to avoid timestamp parsing issues.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`actorDomain` | `principal.hostname` | The value of actorDomain from the raw log is mapped to the UDM field.  
`actorId` | `principal.resource.attribute.labels.key` | The string "actorId" is assigned to the key.  
`actorId` | `principal.resource.attribute.labels.value` | The value of actorId from the raw log is assigned to the value.  
`actorId` | `additional.fields.key` | The string "actorId" is assigned to the key.  
`actorId` | `additional.fields.value.string_value` | The value of actorId from the raw log is assigned to the value.  
`actorUserName` | `principal.user.userid` | The value of actorUserName from the raw log is mapped to the UDM field.  
`actorUuid` | `principal.resource.attribute.labels.key` | The string "actorUuid" is assigned to the key.  
`actorUuid` | `principal.resource.attribute.labels.value` | The value of actorUuid from the raw log is assigned to the value.  
`actorUuid` | `additional.fields.key` | The string "actorUuid" is assigned to the key.  
`actorUuid` | `additional.fields.value.string_value` | The value of actorUuid from the raw log is assigned to the value.  
`all_request_headers.sec-ch-ua-platform` | `principal.platform` | The value is derived from all_request_headers.sec-ch-ua-platform. If it contains "win" or "windows" (case-insensitive), the value is "WINDOWS". If it contains "Mac" (case-insensitive), the value is "MAC". If it contains "lin" or "linux" (case-insensitive), the value is "LINUX".  
`all_request_headers.X-Requested-With` | `network.application_protocol` | If the value contains "http" (case-insensitive), the value is set to "HTTP".  
`automation_tag` | `metadata.product_event_type` | The value of automation_tag from the raw log is mapped to the UDM field.  
`client_ip` | `principal.ip` | The value of client_ip from the raw log is mapped to the UDM field.  
`client_src_port` | `principal.port` | The value of client_src_port from the raw log is mapped to the UDM field.  
`comp` | `about.resource.attribute.labels.key` | The string "Component" is assigned to the key.  
`comp` | `about.resource.attribute.labels.value` | The value of comp from the raw log is assigned to the value.  
`compression` | `additional.fields.key` | The string "compression" is assigned to the key.  
`compression` | `additional.fields.value.string_value` | The value of compression from the raw log is assigned to the value.  
`data` | `about.resource.attribute.labels.key` | Logic depends on msg_type. If msg_type is "Vpxa", "Hostd", or "VSANMGMTSVC", the data field is parsed using key-value pairs, and specific keys (like opID, sub) are mapped to about.resource.attribute.labels. If msg_type is "SWITCHING", "FABRIC", "MONITORING", "SYSTEM", "ROUTING", "LOAD", "nsx", "nestdb", "cfgAgent", "NSX", or "NSXV", the data field is parsed for keys like comp, subcomp, s2comp, which are then mapped to about.resource.attribute.labels.  
`data` | `about.resource.attribute.labels.value` | See logic for about.resource.attribute.labels.key.  
`data` | `security_result.description` | If msg_type is "Vpxa", "Hostd", or "VSANMGMTSVC", and after parsing data for key-value pairs, if a msg field exists, its value is assigned to security_result.description.  
`description` | `security_result.description` | If the description field exists in the raw log, its value is mapped to the UDM field.  
`deviceId` | `principal.resource.attribute.labels.key` | The string "deviceType" is assigned to the key.  
`deviceId` | `principal.resource.attribute.labels.value` | The value of values.deviceType from the raw log is assigned to the value.  
`deviceId` | `additional.fields.key` | The string "deviceType" is assigned to the key.  
`deviceId` | `additional.fields.value.string_value` | The value of values.deviceType from the raw log is assigned to the value.  
`direction` | `network.direction` | If the value is "OUT", it's mapped to "OUTBOUND". If it's "IN", it's mapped to "INBOUND".  
`dst_ip` | `target.ip` | The value of dst_ip from the raw log is mapped to the UDM field.  
`dst_port` | `target.port` | The value of dst_port from the raw log is mapped to the UDM field.  
`event_source` | `principal.url` | The value of event_source from the raw log is mapped to the UDM field.  
`headers_received_from_server.Access-Control-Allow-Origin` | `target.resource.attribute.labels.key` | The string "headers_received_from_server.Access-Control-Allow-Origin" is assigned to the key.  
`headers_received_from_server.Access-Control-Allow-Origin` | `target.resource.attribute.labels.value` | The value of headers_received_from_server.Access-Control-Allow-Origin from the raw log is assigned to the value.  
`headers_received_from_server.Content-Security-Policy` | `principal.resource.attribute.labels.key` | The string "headers_received_from_server.Content-Security-Policy" is assigned to the key.  
`headers_received_from_server.Content-Security-Policy` | `principal.resource.attribute.labels.value` | The value of headers_received_from_server.Content-Security-Policy from the raw log is assigned to the value.  
`headers_received_from_server.Cookie` | `target.resource.attribute.labels.key` | The string "headers_received_from_server.Cookie" is assigned to the key.  
`headers_received_from_server.Cookie` | `target.resource.attribute.labels.value` | The value of headers_sent_to_server.Cookie from the raw log is assigned to the value.  
`headers_received_from_server.set-cookie` | `target.resource.attribute.labels.key` | The string "headers_received_from_server.set-cookie" is assigned to the key.  
`headers_received_from_server.set-cookie` | `target.resource.attribute.labels.value` | The value of headers_received_from_server.set-cookie from the raw log is assigned to the value.  
`headers_sent_to_server.sec-ch-ua` | `principal.resource.attribute.labels.key` | The string "headers_sent_to_server.sec-ch-ua" is assigned to the key.  
`headers_sent_to_server.sec-ch-ua` | `principal.resource.attribute.labels.value` | The value of headers_sent_to_server.sec-ch-ua from the raw log is assigned to the value.  
`headers_sent_to_server.X-CSRF-TOKEN` | `principal.resource.attribute.labels.key` | The string "headers_sent_to_server.X-CSRF-TOKEN" is assigned to the key.  
`headers_sent_to_server.X-CSRF-TOKEN` | `principal.resource.attribute.labels.value` | The value of headers_sent_to_server.X-CSRF-TOKEN from the raw log is assigned to the value.  
`hostname` | `principal.hostname` | The value of hostname from the raw log is mapped to the UDM field.  
`hostname` | `intermediary.hostname` | The value of hostname from the raw log is mapped to the UDM field.  
`host` | `principal.hostname` | The value of host from the raw log is mapped to the UDM field.  
`isLocal` | `additional.fields.key` | The string "isLocal" is assigned to the key.  
`isLocal` | `additional.fields.value.string_value` | The value of isLocal from the raw log is assigned to the value.  
`json_data` | `Various fields within principal, target, additional, and security_result` | The json_data field from the raw log is parsed as JSON, and the extracted fields are mapped to various UDM fields based on their names and the parser's logic. This includes fields like uuid, tenantId, actorId, actorUserName, actorDomain, sourceIp, objectName, objectType, objectId, values.resourceType, values.success, and others.  
`kv_data` | `Various fields` | The kv_data field is parsed as key-value pairs, and the extracted fields are mapped to various UDM fields based on their names and the parser's logic.  
`level` | `security_result.severity` | If the value is "info" (case-insensitive), it's mapped to "INFORMATIONAL".  
`log_id` | `metadata.product_log_id` | The value of log_id from the raw log is mapped to the UDM field.  
`message` | `Various fields` | The message field is the main source of data and is parsed extensively using grok patterns to extract various fields like ts, hostname, msg_type, sub_msg, and others. These extracted fields are then used to populate different UDM fields based on the parser's logic.  
`method` | `network.http.method` | The value of method from the raw log is mapped to the UDM field.  
`msg` | `security_result.description` | If msg_type is "Vpxa", "Hostd", "VSANMGMTSVC", "SWITCHING", "FABRIC", "ROUTING", "LOAD-BALANCER", "nsx", "nestdb", "cfgAgent", "NSX", "NSXV", or "Rhttpproxy", and after any relevant grok parsing, if the msg field exists, its value is assigned to security_result.description. There are special cases within this logic for specific message content like "keepalive connection".  
`msg_type` | `metadata.product_event_type` | If msg_type is "FIREWALL_PKTLOG" or "FIREWALL-PKTLOG", its value is mapped to the UDM field.  
`objectName` | `target.resource.attribute.labels.key` | The string "objectName" is assigned to the key.  
`objectName` | `target.resource.attribute.labels.value` | The value of objectName from the raw log is assigned to the value.  
`objectName` | `additional.fields.key` | The string "objectName" is assigned to the key.  
`objectName` | `additional.fields.value.string_value` | The value of objectName from the raw log is assigned to the value.  
`objectId` | `target.resource.attribute.labels.key` | The string "objectId" is assigned to the key.  
`objectId` | `target.resource.attribute.labels.value` | The value of objectId from the raw log is assigned to the value.  
`objectId` | `additional.fields.key` | The string "objectId" is assigned to the key.  
`objectId` | `additional.fields.value.string_value` | The value of objectId from the raw log is assigned to the value.  
`objectType` | `target.resource.attribute.labels.key` | The string "objectType" is assigned to the key.  
`objectType` | `target.resource.attribute.labels.value` | The value of objectType from the raw log is assigned to the value.  
`objectType` | `additional.fields.key` | The string "objectType" is assigned to the key.  
`objectType` | `additional.fields.value.string_value` | The value of objectType from the raw log is assigned to the value.  
`objectType` | `security_result.description` | If objectType is "LAUNCH" and success is not "true", the description is "application launch attempt was successful". If objectType is "LAUNCH_ERROR" and success is not "true", the description is "User launched an application with an invalid request".  
`opID` | `about.resource.attribute.labels.key` | The string "opId" is assigned to the key.  
`opID` | `about.resource.attribute.labels.value` | The value of opID from the raw log is assigned to the value.  
`pool` | `additional.fields.key` | The string "pool" is assigned to the key.  
`pool` | `additional.fields.value.string_value` | The value of pool from the raw log is assigned to the value.  
`pool_name` | `additional.fields.key` | The string "pool_name" is assigned to the key.  
`pool_name` | `additional.fields.value.string_value` | The value of pool_name from the raw log is assigned to the value.  
`protocol` | `network.ip_protocol` | The value of protocol from the raw log is converted to uppercase and mapped to the UDM field. If the value is "PROTO", it is not mapped.  
`protocol` | `additional.fields.key` | If the value of protocol is "PROTO", the string "ip_protocol" is assigned to the key.  
`protocol` | `additional.fields.value.string_value` | If the value of protocol is "PROTO", the value of protocol from the raw log is assigned to the value.  
`query_data` | `network.dns.questions.name` | The query_data field is parsed to extract the question_name, which is then mapped to the UDM field.  
`query_data` | `network.dns.questions.type` | The query_data field is parsed to extract the query_type, which is then mapped to the UDM field using a lookup included from "dns_record_type.include".  
`query_data` | `network.dns.questions.class` | The query_data field is parsed to extract the dns_class, which is then mapped to the UDM field using a lookup included from "dns_query_class_mapping.include".  
`referer` | `principal.url` | The value of referer from the raw log is mapped to the UDM field.  
`request_content_type` | `additional.fields.key` | The string "request_content_type" is assigned to the key.  
`request_content_type` | `additional.fields.value.string_value` | The value of request_content_type from the raw log is assigned to the value.  
`request_state` | `additional.fields.key` | The string "request_state" is assigned to the key.  
`request_state` | `additional.fields.value.string_value` | The value of request_state from the raw log is assigned to the value.  
`response_code` | `network.http.response_code` | The value of response_code or server_response_code from the raw log is mapped to the UDM field.  
`response_content_type` | `additional.fields.key` | The string "request_content_type" is assigned to the key.  
`response_content_type` | `additional.fields.value.string_value` | The value of response_content_type from the raw log is assigned to the value.  
`rule_id` | `security_result.rule_id` | The value of rule_id from the raw log is mapped to the UDM field.  
`s2comp` | `about.resource.attribute.labels.key` | The string "S2-Component" is assigned to the key.  
`s2comp` | `about.resource.attribute.labels.value` | The value of s2comp from the raw log is assigned to the value.  
`server_ip` | `target.ip` | The value of server_ip from the raw log is mapped to the UDM field.  
`server_name` | `target.hostname` | The value of server_name from the raw log is mapped to the UDM field.  
`server_response_code` | `network.http.response_code` | See logic for response_code.  
`server_src_port` | `target.port` | The value of server_src_port from the raw log is mapped to the UDM field.  
`service_engine` | `additional.fields.key` | The string "service_engine" is assigned to the key.  
`service_engine` | `additional.fields.value.string_value` | The value of service_engine from the raw log is assigned to the value.  
`sourceIp` | `principal.ip` | The value of sourceIp from the raw log is mapped to the UDM field.  
`ssl_cipher` | `network.tls.cipher` | The value of ssl_cipher from the raw log is mapped to the UDM field.  
`ssl_session_id` | `network.session_id` | The value of ssl_session_id from the raw log is mapped to the UDM field.  
`ssl_version` | `network.tls.version_protocol` | The value of ssl_version from the raw log is mapped to the UDM field.  
`sub` | `about.resource.attribute.labels.key` | The string "Sub Component" is assigned to the key.  
`sub` | `about.resource.attribute.labels.value` | The value of sub from the raw log is assigned to the value.  
`subClusterUuid` | `additional.fields.key` | The string "subClusterUuid" is assigned to the key.  
`subClusterUuid` | `additional.fields.value.string_value` | The value of subClusterUuid from the raw log is assigned to the value.  
`sub_msg` | `Various fields within principal, target, network, security_result, and about` | The sub_msg field is parsed differently based on the msg_type. It can be parsed as JSON, using grok patterns, or using key-value pairs. The extracted fields are then mapped to various UDM fields based on their names and the parser's logic. This includes fields like ip_type, action, rule_id, direction, protocol, tcp_flag, src_ip, src_port, dst_ip, dst_port, data, msg, and others.  
`subcomp` | `about.resource.attribute.labels.key` | The string "Sub Component" is assigned to the key.  
`subcomp` | `about.resource.attribute.labels.value` | The value of subcomp from the raw log is assigned to the value.  
`tenantId` | `principal.resource.attribute.labels.key` | The string "tenantId" is assigned to the key.  
`tenantId` | `principal.resource.attribute.labels.value` | The value of tenantId from the raw log is assigned to the value.  
`tenantId` | `additional.fields.key` | The string "tenantId" is assigned to the key.  
`tenantId` | `additional.fields.value.string_value` | The value of tenantId from the raw log is assigned to the value.  
`ts` | `metadata.event_timestamp` | The value of ts from the raw log is parsed as a timestamp and mapped to the UDM field.  
`ts` | `timestamp` | The value of ts from the raw log is parsed as a timestamp and mapped to the UDM field.  
`updateType` | `additional.fields.key` | The string "updateType" is assigned to the key.  
`updateType` | `additional.fields.value.string_value` | The value of updateType from the raw log is assigned to the value.  
`uri_path` | `network.http.referral_url` | The value of uri_path from the raw log is mapped to the UDM field.  
`user_agent` | `network.http.user_agent` | The value of user_agent from the raw log is mapped to the UDM field.  
`user_agent` | `network.http.parsed_user_agent` | The value of user_agent from the raw log is parsed as a user agent string and mapped to the UDM field.  
`USER` | `principal.user.user_display_name` | The value of USER from the raw log is mapped to the UDM field.  
`values.actorExternalId` | `principal.resource.attribute.labels.key` | The string "actorExternalId" is assigned to the key.  
`values.actorExternalId` | `principal.resource.attribute.labels.value` | The value of values.actorExternalId from the raw log is assigned to the value.  
`values.actorExternalId` | `additional.fields.key` | The string "actorExternalId" is assigned to the key.  
`values.actorExternalId` | `additional.fields.value.string_value` | The value of values.actorExternalId from the raw log is assigned to the value.  
`values.deviceType` | `principal.resource.attribute.labels.key` | The string "deviceType" is assigned to the key.  
`values.deviceType` | `principal.resource.attribute.labels.value` | The value of values.deviceType from the raw log is assigned to the value.  
`values.deviceType` | `additional.fields.key` | The string "deviceType" is assigned to the key.  
`values.deviceType` | `additional.fields.value.string_value` | The value of values.deviceType from the raw log is assigned to the value.  
`values.resourceType` | `principal.resource.resource_subtype` | The value of values.resourceType from the raw log is mapped to the UDM field. The principal.resource.type is set to "VIRTUAL_MACHINE".  
`values.success` | `security_result.action` | If the value is "true" (case-insensitive), it's mapped to "ALLOW". If it's "false" (case-insensitive), it's mapped to "BLOCK".  
`virtualservice` | `additional.fields.key` | The string "virtualservice" is assigned to the key.  
`virtualservice` | `additional.fields.value.string_value" | The value of virtualservice from the raw log is assigned to the value.  
`vmw_vr_ops_appname` | `about.resource.attribute.labels.key` | The string "Ops AppName" is assigned to the key.  
`vmw_vr_ops_appname` | `about.resource.attribute.labels.value` | The value of vmw_vr_ops_appname from the raw log is assigned to the value.  
`vmw_vr_ops_clustername` | `about.resource.attribute.labels.key` | The string "Ops ClusterName" is assigned to the key.  
`vmw_vr_ops_clustername` | `about.resource.attribute.labels.value` | The value of vmw_vr_ops_clustername from the raw log is assigned to the value.  
`vmw_vr_ops_logtype` | `about.resource.attribute.labels.key` | The string "Ops Logtype" is assigned to the key.  
`vmw_vr_ops_logtype" | `about.resource.attribute.labels.value` | The value of vmw_vr_ops_logtype from the raw log is assigned to the value.  
`vmw_vr_ops_nodename` | `about.resource.attribute.labels.key` | The string "Ops NodeName" is assigned to the key.  
`vmw_vr_ops_nodename` | `about.resource.attribute.labels.value` | The value of vmw_vr_ops_nodename from the raw log is assigned to the value.  
`vs_name` | `additional.fields.key` | The string "vs_name" is assigned to the key.  
`vs_name` | `additional.fields.value.string_value` | The value of vs_name from the raw log is assigned to the value.  
`etag` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`request_length` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`server_response_length` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`server_conn_src_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`vs_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`persistent_session_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`client_rtt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`server_response_time_first_byte` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`server_response_time_last_byte` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`response_length` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`response_time_first_byte` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`response_time_last_byte` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`compression_percentage` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`client_insights` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`request_headers` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`server_ssl_session_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`server_connection_reused` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`response_headers` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`request_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`servers_tried` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`jwt_log` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`max_ingress_latency_fe` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`conn_est_time_fe` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`max_ingress_latency_be` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`conn_est_time_be` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`isLocal", "updateType", "subClusterUuid", "valueLength` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-vrealize-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
