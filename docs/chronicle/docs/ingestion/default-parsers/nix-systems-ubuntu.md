---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nix-systems-ubuntu/
title: Collect Nix Systems Ubuntu Server (Unix System) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:35.502602+00:00
---

# Collect Nix Systems Ubuntu Server (Unix System) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nix-systems-ubuntu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Nix Systems Ubuntu Server (Unix System) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Ubuntu Server (Unix System) logs to Google Security Operations using Bindplane. The parser ingests syslog and JSON formatted logs, initializes a wide array of Unified Data Model (UDM) fields to empty strings, performs several string substitutions on the `message` field, and then attempts to parse the message as JSON. If JSON parsing fails, it uses grok patterns to extract fields based on the `message` and `event_details.original` content, mapping the extracted fields to the UDM based on the event type and various conditional checks, handling different log formats and structures from various Unix system processes and services.

## Before you begin

Ensure that you have the following prerequisites:

  * Google SecOps instance
  * If running behind a proxy, firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open
  * Privileged access to a RHEL server



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



## Install the Bindplane agent

### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c `$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)` install_unix.sh
         




### Additional installation resources

For additional installation options, consult the [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file: 
     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux.
     * Open the file using a text editor (for example, `nano` or `vi`).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           filelog/unix:
             include:
               - /var/log/auth.log
               - /var/log/lastlog
               - /var/log/btmp
               - /var/log/wtmp
               - /var/log/faillog
               - /var/log/dpkg.log
               - /var/log/boot.log
               - /var/log/kern.log
               - /var/log/syslog
             start_at: end
             poll_interval: 5s
         
         exporters:
           chronicle/linux:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: <customer_id>
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'NIX_SYSTEM'
             override_log_type: false
             raw_log_field: body
         
         service:
           pipelines:
             logs/linux:
               receivers:
                 - filelog/linux
               exporters: [chronicle/linux]
         

  3. Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.

  4. Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

  5. Replace `<customer_id>` with the actual customer ID.

  6. Update `/path/to/ingestion-authentication-file.json` to the path where the service account key file (Option 1) was saved in the Get Google SecOps credentials for the Bindplane agent section.




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/linux:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: <customer_id>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'NIX_SYSTEM'
            override_log_type: false
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Start the Bindplane agent and apply changes

  1. Start the Bindplane agent:
         
         sudo systemctl start bindplane-agent
         

  2. Enable the observIQ otel collector Service:
         
         systemctl enable --now bindplane-agent
         

  3. Restart Bindplane agent if needed:
         
         sudo systemctl restart bindplane-agent
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`AccessControlRuleAction` | `security_result.action` | If `AccessControlRuleAction` is `Allow`, set to `ALLOW`. If `AccessControlRuleAction` is `Block`, set to `BLOCK`.  
`ACPolicy` | `security_result.rule_labels` | Key: `ACPolicy`, Value: `ACPolicy`  
`AccessControlRuleName` | `security_result.rule_name` | Direct mapping.  
`acct` | `event.idm.read_only_udm.target.user.userid` | Direct mapping after removing quotes and backslashes.  
`addr` | `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip` | Direct mapping if not empty, `?`, or `UNKNOWN`.  
`ApplicationProtocol` | `event.idm.read_only_udm.network.application_protocol` | Direct mapping.  
`auid` | `event.idm.read_only_udm.additional.fields` | Key: `auid`, Value: `auid`  
`comm` | `event.idm.read_only_udm.target.process.command_line` | Direct mapping.  
`command` | `event.idm.read_only_udm.target.process.command_line` | Direct mapping after removing leading/trailing whitespace.  
`Computer` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | Direct mapping. If empty, use `HostName`.  
`ConnectionID` | `security_result.detection_fields` | Key: `Connection ID`, Value: `ConnectionID`  
`cwd` | `event.idm.read_only_udm.target.process.file.full_path` | Direct mapping after removing quotes.  
`data` | `message` | Used in grok patterns.  
`desc` | `security_result.description` | Direct mapping.  
`description` | `event.idm.read_only_udm.metadata.description`, `security_result.description` | Direct mapping.  
`descript` | `security_result.description` | Direct mapping after removing hashes.  
`DeviceUUID` | `event.idm.read_only_udm.metadata.product_log_id` | Direct mapping.  
`DNSQuery` | `event.idm.read_only_udm.additional.fields` | Key: `DNSQuery`, Value: `DNSQuery`  
`DNSRecordType` | `event.idm.read_only_udm.additional.fields` | Key: `DNSRecordType`, Value: `DNSRecordType`  
`DNSResponseType` | `event.idm.read_only_udm.additional.fields` | Key: `DNSResponseType`, Value: `DNSResponseType`  
`DNS_TTL` | `event.idm.read_only_udm.additional.fields` | Key: `DNS_TTL`, Value: `DNS_TTL`  
`DstIP` | `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip` | Direct mapping.  
`DstPort` | `event.idm.read_only_udm.target.port` | Direct mapping, converted to integer.  
`dvc` | `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`, `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`, `event.idm.read_only_udm.intermediary.ip`, `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip`, `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname` | If valid IP, mapped to principal/target IP. If hostname, mapped to principal/target hostname. Also used for intermediary IP if valid IP.  
`EgressInterface` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Key: `EgressInterface`, Value: `EgressInterface`  
`EgressVRF` | `event.idm.read_only_udm.principal.asset.attribute.labels` | Key: `EgressVRF`, Value: `EgressVRF`  
`EgressZone` | `event.idm.read_only_udm.target.location.name` | Direct mapping.  
`eventType` | `event.idm.read_only_udm.metadata.product_event_type`, `event.idm.read_only_udm.target.application` | Direct mapping. For `SERVICE_START` and `SERVICE_STOP`, mapped to `target.application` and then cleared.  
`EventTime` | `@timestamp` | Parsed as timestamp.  
`exe` | `event.idm.read_only_udm.target.process.command_line` | Direct mapping after removing quotes and backslashes.  
`extended_description` | `event.idm.read_only_udm.metadata.description` | Direct mapping after removing hyphens and quotes.  
`Facility` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Key: `Facility`, Value: `Facility`  
`filepath` | `event.idm.read_only_udm.principal.process.file.full_path` | Direct mapping.  
`file_path` | `event.idm.read_only_udm.target.file.full_path` | Direct mapping.  
`file_path_value` | `event.idm.read_only_udm.target.file.full_path` | Direct mapping.  
`FirstPacketSecond` | `security_result.detection_fields` | Key: `FirstPacketSecond`, Value: `FirstPacketSecond`  
`from` | `event.idm.read_only_udm.network.email.from` | Direct mapping after removing angle brackets.  
`generic_ip` | `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` | Direct mapping if a valid IP and not `A256:`.  
`gid` | `event.idm.read_only_udm.target.user.group_identifiers` | Direct mapping.  
`grp` | `event.idm.read_only_udm.target.group.group_display_name` | Direct mapping after removing quotes and backslashes.  
`hashing_algo` | `security_result.summary` | Direct mapping.  
`home` | `event.idm.read_only_udm.target.file.full_path` | Direct mapping.  
`HostName` | `Computer` | Used if `Computer` is empty.  
`HostIP` | `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` | The part of `HostIP` before `%` is extracted and mapped as `validated_ip`.  
`hostname` | `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname`, `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | Direct mapping if not empty or `?`.  
`host_name` | `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname` | Direct mapping.  
`InitiatorBytes` | `event.idm.read_only_udm.network.sent_bytes` | Direct mapping, converted to unsigned integer.  
`InitiatorPackets` | `event.idm.read_only_udm.network.sent_packets` | Direct mapping, converted to integer.  
`insertId` | `event.idm.read_only_udm.metadata.product_log_id` | Direct mapping.  
`InstanceID` | `security_result.detection_fields` | Key: `Instance ID`, Value: `InstanceID`  
`int_dvc` | `event.idm.read_only_udm.intermediary.hostname` | Direct mapping.  
`ip` | `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip`, `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` | Direct mapping.  
`ip_protocol` | `event.idm.read_only_udm.network.ip_protocol` | Direct mapping.  
`laddr` | `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` | Direct mapping if not empty or `?`.  
`level` | `security_result.severity` | If `info`, set to `INFORMATIONAL`.  
`log.syslog.facility.name` | `event.idm.read_only_udm.target.application` | Direct mapping.  
`log.syslog.severity.name` | `security_result.severity` | If `Emergency`, set to `HIGH`.  
`logName` | `logname` | Direct mapping.  
`log_description` | `security_result.description` | Direct mapping.  
`log_level` | `security_result.severity` | If `error`, set to `ERROR`.  
`log_summary` | `security_result.summary` | Direct mapping.  
`logger_name` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Key: `logger_name`, Value: `logger_name`  
`log_type` | `event.idm.read_only_udm.metadata.log_type` | Hardcoded to `NIX_SYSTEM`.  
`lport` | `event.idm.read_only_udm.principal.port` | Direct mapping, converted to integer.  
`MG` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Key: `MG`, Value: `MG`  
`method` | `event.idm.read_only_udm.network.http.method` | Direct mapping, converted to uppercase.  
`msg1` | `event.idm.read_only_udm.metadata.description`, `event.idm.read_only_udm.additional.fields`, `security_result.description` | Parsed using grok patterns. If `event_type` is `GENERIC_EVENT`, mapped to `description`.  
`msg2` | `event.idm.read_only_udm.network.received_bytes`, `security_result.summary` | If contains digits, converted to unsigned integer and mapped to `received_bytes`. Otherwise, mapped to `summary`.  
`NAPPolicy` | `security_result.rule_labels` | Key: `NAPPolicy`, Value: `NAPPolicy`  
`name` | `event.idm.read_only_udm.target.process.file.full_path` | Direct mapping after removing quotes.  
`outcome` | `security_result.action` | If `Succeeded` or contains `success`, set to `ALLOW`.  
`p_id` | `event.idm.read_only_udm.target.process.pid` | Direct mapping.  
`pid` | `event.idm.read_only_udm.target.process.pid`, `event.idm.read_only_udm.principal.process.pid` | Direct mapping.  
`principal_hostname` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | Direct mapping.  
`principal_ip` | `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` | Direct mapping.  
`principal_present` | `event.idm.read_only_udm.metadata.event_type` | If `true` and `has_target` is `true`, set `event_type` to `NETWORK_UNCATEGORIZED`. If `true` or `user_present` is `true`, set `event_type` to `USER_UNCATEGORIZED`.  
`process` | `event.idm.read_only_udm.target.application`, `event.idm.read_only_udm.metadata.product_event_type` | Direct mapping. If `eventType` is empty, used as `target.application`.  
`ProcessID` | `event.idm.read_only_udm.principal.process.pid` | Direct mapping, converted to string.  
`ProcessName` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Key: `ProcessName`, Value: `ProcessName`  
`prod_eve_type` | `event.idm.read_only_udm.metadata.product_event_type` | Direct mapping.  
`product_event_type` | `event.idm.read_only_udm.metadata.product_event_type` | Direct mapping.  
`Protocol` | `event.idm.read_only_udm.network.ip_protocol` | If matches `icmp`, `udp`, or `tcp` (case-insensitive), mapped to corresponding uppercase value.  
`proto` | `event.idm.read_only_udm.network.application_protocol` | If `ssh` or `ssh2`, set to `SSH`.  
`pwd` | `event.idm.read_only_udm.target.file.full_path` | Direct mapping.  
`reason` | `security_result.summary`, `security_result.description` | Used in combination with `action` and `desc` to create `security_result.description`. Also mapped to `security_result.summary`.  
`relayHostname` | `event.idm.read_only_udm.intermediary.hostname` | Direct mapping.  
`relayIp` | `event.idm.read_only_udm.intermediary.ip` | Direct mapping.  
`res` | `security_result.summary` | Direct mapping.  
`resource.labels.instance_id` | `event.idm.read_only_udm.target.resource.product_object_id` | Direct mapping.  
`resource.labels.project_id` | `event.idm.read_only_udm.target.asset.attribute.cloud.project.id` | Direct mapping.  
`resource.labels.zone` | `event.idm.read_only_udm.target.asset.attribute.cloud.availability_zone` | Direct mapping.  
`resource.type` | `event.idm.read_only_udm.target.resource.resource_subtype` | Direct mapping.  
`response_code` | `event.idm.read_only_udm.network.http.response_code` | Direct mapping, converted to integer.  
`ResponderBytes` | `event.idm.read_only_udm.network.received_bytes` | Direct mapping, converted to unsigned integer.  
`ResponderPackets` | `event.idm.read_only_udm.network.received_packets` | Direct mapping, converted to integer.  
`rhost` | `event.idm.read_only_udm.additional.fields` | Key: `rhost`, Value: `rhost`  
`ruser` | `srcUser` | Direct mapping.  
`sec_action` | `security_result.action` | Mapped based on `action` or `eventType`.  
`sec_summary` | `security_result.summary` | Direct mapping.  
`security_action` | `security_result.action` | Direct mapping.  
`sent_bytes` | `event.idm.read_only_udm.network.sent_bytes` | Direct mapping, converted to unsigned integer.  
`ses` | `event.idm.read_only_udm.network.session_id`, `event.idm.read_only_udm.network.session_duration` | If numeric, parsed as UNIX timestamp and mapped to `session_duration`. Otherwise, mapped to `session_id`.  
`SeverityLevel` | `security_result.severity` | Mapped to different severities based on value (notice/info -> INFORMATIONAL, warn -> HIGH, error -> ERROR, other -> UNKNOWN_SEVERITY).  
`sessionId` | `event.idm.read_only_udm.network.session_id` | Direct mapping.  
`size` | `event.idm.read_only_udm.network.received_bytes` | Direct mapping, converted to unsigned integer.  
`source` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | Direct mapping after removing leading whitespace.  
`SourceSystem` | `event.idm.read_only_udm.principal.resource.attribute.labels`, `event.idm.read_only_udm.principal.platform` | Key: `SourceSystem`, Value: `SourceSystem`. Also mapped to `platform` (Linux -> LINUX, Window -> WINDOWS, Mac/iOS -> MAC).  
`SrcIP` | `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` | Direct mapping.  
`SrcPort` | `event.idm.read_only_udm.principal.port` | Direct mapping, converted to integer.  
`srcIp` | `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` | Direct mapping.  
`srcPort` | `event.idm.read_only_udm.principal.port` | Direct mapping, converted to integer.  
`srcUser` | `event.idm.read_only_udm.principal.user.userid` | Direct mapping.  
`src_user` | `event.idm.read_only_udm.principal.user.userid` | Direct mapping.  
`src_user_display_name` | `event.idm.read_only_udm.principal.user.user_display_name` | Direct mapping.  
`status` | `security_result.action` | If `Deferred`, set to `BLOCK`. If `Sent`, set to `ALLOW`.  
`summary` | `security_result.summary` | Direct mapping.  
`SyslogMessage` | `security_result.description` | Direct mapping.  
`targetEmail` | `event.idm.read_only_udm.network.email.to` | Direct mapping.  
`targetEmailfrom` | `event.idm.read_only_udm.network.email.from` | Direct mapping.  
`targetHostname` | `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname` | Direct mapping.  
`target_hostname` | `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname` | Direct mapping.  
`target_ip` | `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip` | Direct mapping.  
`target_mac` | `event.idm.read_only_udm.target.mac` | Direct mapping.  
`target_uri` | `event.idm.read_only_udm.target.url` | Direct mapping.  
`TenantId` | `event.idm.read_only_udm.principal.user.product_object_id` | Direct mapping.  
`terminal` | `event.idm.read_only_udm.additional.fields` | Key: `terminal`, Value: `terminal` if not empty or `?`.  
`TimeGenerated` | `event.idm.read_only_udm.metadata.collected_timestamp` | Parsed as timestamp.  
`timestamp` | `@timestamp` | Parsed as timestamp.  
`tls_cipher` | `event.idm.read_only_udm.network.tls.cipher` | Direct mapping.  
`Type` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Key: `Type`, Value: `Type`  
`uid` | `event.idm.read_only_udm.principal.user.userid` | If `0`, set to `root`. Otherwise, direct mapping.  
`uid_2` | `event.idm.read_only_udm.target.user.userid` | Direct mapping if `uid` is empty.  
`unit` | `event.idm.read_only_udm.target.application` | Direct mapping.  
`url` | `event.idm.read_only_udm.target.url` | Direct mapping.  
`user` | `username` | Direct mapping.  
`username` | `event.idm.read_only_udm.target.user.userid`, `event.idm.read_only_udm.principal.user.userid` | Direct mapping.  
`user_display_name` | `event.idm.read_only_udm.target.user.user_display_name` | Direct mapping.  
`user_present` | `event.idm.read_only_udm.metadata.event_type` | If `true` or `principal_present` is `true`, set `event_type` to `USER_UNCATEGORIZED`.  
`_Internal_WorkspaceResourceId` | `event.idm.read_only_udm.target.resource.attribute.labels`, `event.idm.read_only_udm.target.resource.product_object_id` | Key: `_Internal_WorkspaceResourceId`, Value: `_Internal_WorkspaceResourceId`. The subscription ID is extracted and mapped to `product_object_id`.  
`_ItemId` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Key: `_ItemId`, Value: `_ItemId`  
`_ResourceId` | `event.idm.read_only_udm.principal.resource.attribute.labels`, `event.idm.read_only_udm.principal.resource.product_object_id` | Key: `_ResourceId`, Value: `_ResourceId`. The subscription ID is extracted and mapped to `product_object_id`.  
`_timestamp` | `@timestamp` | Parsed as timestamp.  
`_timestamp_tz` | `@timestamp` | Parsed as timestamp.  
  
`event.idm.read_only_udm.metadata.event_type`: Set to `GENERIC_EVENT` initially, then overwritten based on parser logic. `event.idm.read_only_udm.metadata.product_name`: Hardcoded to `Unix System`. `event.idm.read_only_udm.extensions.auth.type`: Set to `MACHINE` for certain event types. `event.idm.read_only_udm.target.asset.attribute.cloud.environment`: Set to `GOOGLE_CLOUD_PLATFORM` for Google Cloud audit logs. `event.idm.read_only_udm.target.resource.resource_type`: Set to `VIRTUAL_MACHINE` for Google Cloud audit logs. `event.idm.read_only_udm.extensions.auth.mechanism`: Set to `USERNAME_PASSWORD` for login events. `has_target_resource`: Set to `true` if `resource.labels.instance_id` or `_Internal_WorkspaceResourceId` is present.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
