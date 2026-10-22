---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cybereason-edr/
title: Collect LevelBlue Cybereason EDR (formerly Cybereason EDR) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:48.359096+00:00
---

# Collect LevelBlue Cybereason EDR (formerly Cybereason EDR) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cybereason-edr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect LevelBlue Cybereason EDR (formerly Cybereason EDR) logs

**Parser Version:** 8.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest LevelBlue Cybereason EDR (formerly known as Cybereason EDR) logs to Google Security Operations using Bindplane.

LevelBlue Cybereason EDR (Endpoint Detection and Response) is a cybersecurity platform that detects and responds to advanced threats across endpoints. It identifies Malops (Malicious Operations) — correlated attack chains that tie together suspicious activities into complete attack narratives — and provides security analysts with visibility into threat progression, affected machines, compromised users, and network connections.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Cybereason Detection Server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Access to Cybereason management console with System Admin role
  * Cybereason platform version 20.1 or later



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
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         




The service should show as **active (running)**.

### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/cybereason:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id'
            endpoint: chronicle.googleapis.com
            log_type: CYBEREASON_EDR
            raw_log_field: body
        
        service:
          pipelines:
            logs/cybereason_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/cybereason
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0:514` to listen on all interfaces on port 514 (requires root on Linux)
      * `0.0.0.0:1514` to listen on an unprivileged port (recommended for Linux non-root)
    * Receiver type options: 
      * `tcplog` for TCP syslog (required for Cybereason syslog forwarding)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Google SecOps customer ID
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/cybereason:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CYBEREASON_EDR
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
         




## Configure Cybereason EDR syslog forwarding

Cybereason sends MalOp and User Audit events in CEF (Common Event Format) via syslog. Syslog forwarding configuration requires a request to Cybereason Technical Support.

### Request syslog forwarding from Cybereason Technical Support

  1. Sign in to the **Cybereason management console**.
  2. Contact **Cybereason Technical Support** through the Cybereason support portal.
  3. Submit a syslog forwarding configuration request with the following information: 
     * **Syslog server IP address** : The IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Syslog server port** : The port matching the Bindplane agent `listen_address` (for example, `514`).
     * **Protocol** : TCP (unencrypted TCP syslog).
     * **Log types** : Request forwarding of the following log types: 
       * **MalOp syslog** : Security alerts and Malicious Operations events
       * **User Audit syslog** : User activity and administrative actions
  4. Wait for Cybereason Technical Support to confirm the syslog forwarding configuration.

**Note:** Cybereason syslog forwarding is not a self-service configuration. You must submit a request to Cybereason Technical Support to enable and configure syslog forwarding to your SIEM collector.



### Configure firewall rules

Ensure the following firewall rules are in place:

Direction | Protocol | Port | Source | Destination  
---|---|---|---|---  
Outbound | TCP | 514 | Cybereason Detection Server | Bindplane agent host  
**Note:** The default syslog port is 514. Adjust the port number to match your Bindplane agent configuration.

### Alternative: Cybereason CEF Forwarder

If Cybereason Technical Support is unable to configure direct syslog forwarding, you can use the Cybereason CEF Forwarder tool:

  1. Download the Cybereason CEF Forwarder Docker image from Cybereason Technical Support.
  2. Create or edit the configuration file at `cybereason-forwarders/config/config.json`.
  3. Configure the following settings:
         
         {
             "host": "<BINDPLANE_AGENT_IP>",
             "port": 514
         }
         

  4. Replace `<BINDPLANE_AGENT_IP>` with the IP address of the Bindplane agent host.

  5. Build and run the Docker container:
         
         docker build -t cybereason-cef-forwarder .
         docker run -d --name cybereason-forwarder cybereason-cef-forwarder
         

**Note:** The Cybereason CEF Forwarder is a Docker-based tool that queries the Cybereason API and forwards events in CEF format to a syslog server. Contact Cybereason Technical Support for access to the Docker image and configuration documentation.



### Syslog event types

Cybereason generates CEF syslog messages for the following event categories:

Event Category | Description  
---|---  
**MalOp created** | New Malicious Operation detected  
**MalOp updated** | Existing MalOp status or details changed  
**MalOp closed** | MalOp resolved or closed by analyst  
**Malware detected** | Malware identified on an endpoint  
**Suspicious process** | Suspicious process activity detected  
**Network connection** | Suspicious network connection identified  
**User login** | User authentication events  
**Machine isolation** | Endpoint isolated from or reconnected to the network  
**Policy changes** | Security policy modifications  
  
### Verify syslog forwarding

  1. After Cybereason Technical Support confirms the syslog configuration, perform a test action in the Cybereason console (for example, view a MalOp or isolate a test machine).
  2. Check the Bindplane agent logs for incoming syslog messages: 
     * **Linux** : `sudo journalctl -u observiq-otel-collector -f`
     * **Windows** : `type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"`
  3. Verify that CEF-formatted messages appear in the logs, for example:
         
         CEF:0|Cybereason|Cybereason|2.0|MalOp|MalOp Created|8|cs1=MALOP_ID_HERE dvchost=server01.company.com suser=admin@company.com
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
detectionName_label | additional.fields | Mapped as key-value pair  
sensorId_label | additional.fields | Mapped as key-value pair  
status | metadata.description | If value is not empty  
log_description | metadata.description | Fallback if status is empty  
(CEF format) | metadata.event_type | Set to GENERIC_EVENT for CEF logs  
event_type | metadata.event_type | Set to PROCESS_OPEN if value is "PROCESS_OPEN", NETWORK_CONNECTION if value is "NETWORK_CONNECTION", SCAN_HOST if value is "MALWARE"  
has_principal, has_target | metadata.event_type | Set to SCAN_FILE if both has_principal and has_target are true  
has_principal | metadata.event_type | Set to STATUS_UPDATE if only has_principal is true  
has_user | metadata.event_type | Set to USER_UNCATEGORIZED if has_user is true in Malop context  
(default) | metadata.event_type | Set to GENERIC_EVENT otherwise  
LogType | metadata.product_event_type | If value is not empty  
malop_data.simpleValues.elementDisplayName.values.0 | metadata.product_event_type | Fallback if LogType is empty  
type | metadata.product_event_type | Fallback  
prod_event, prod_event2 | metadata.product_event_type | Concatenated as prod_event - prod_event2  
malop_process.guidString | metadata.product_log_id | For PROCESS_OPEN event type  
malop_connection.guidString | metadata.product_log_id | For NETWORK_CONNECTION event type  
guid | metadata.product_log_id | For MALWARE or Malop event types  
(static) | metadata.product_version | Set to "2.0" initially  
Sensor.version | metadata.product_version | Overwrites "2.0" if present  
malop_url | metadata.url_back_to_product | Directly mapped  
(static) | metadata.vendor_name | Set to "Cybereason"  
direction | network.direction | Directly mapped  
malop_connection.simpleValues.transportProtocol.values.0 | network.ip_protocol | Directly mapped  
malop_connection.simpleValues.receivedBytesCount.values.0 | network.received_bytes | Converted to unsigned integer  
malop_connection.simpleValues.transmittedBytesCount.values.0 | network.sent_bytes | Converted to unsigned integer  
Sensor.fqdn | principal.administrative_domain | Directly mapped  
malop_process.elementValues.ownerMachine.elementValues.0.guid | principal.asset.asset_id | Prefixed with "Cybereason:"  
malop_data.elementValues.affectedMachines.elementValues.0.guid | principal.asset.asset_id | Prefixed with "Cybereason:", fallback  
malop_process.elementValues.ownerMachine.elementValues.0.name | principal.asset.hostname | Directly mapped  
malop_data.elementValues.affectedMachines.elementValues.0.name | principal.asset.hostname | Fallback  
machineName | principal.asset.hostname | Fallback  
host | principal.asset.hostname | Fallback  
dvchost | principal.asset.hostname | Fallback  
Sensor.fqdn | principal.asset.hostname | Fallback  
client.ip | principal.asset.ip | Directly mapped  
Sensor.externalIpAddress | principal.asset.ip | Fallback  
malop_process.elementValues.ownerMachine.elementValues.0.name | principal.hostname | Directly mapped  
malop_data.elementValues.affectedMachines.elementValues.0.name | principal.hostname | Fallback  
machineName | principal.hostname | Fallback  
host | principal.hostname | Fallback  
dvchost | principal.hostname | Fallback  
Sensor.fqdn | principal.hostname | Fallback  
client.ip | principal.ip | Directly mapped  
Sensor.externalIpAddress | principal.ip | Fallback  
Sensor.internalIpAddress | principal.nat_ip | Directly mapped  
Sensor.privateServerIp | principal.nat_ip | Fallback  
Sensor.osType | principal.platform | Set to WINDOWS if value is "WINDOWS", LINUX if "LINUX", MAC if "MAC"  
Sensor.osVersionType | principal.platform_version | Directly mapped  
malop_connection.simpleValues.localPort.values.0 | principal.port | Converted to integer  
malop_process.simpleValues.commandLine.values.0 | principal.process.command_line | Directly mapped  
malwareDataModel.filePath | principal.process.command_line | Fallback  
malop_process.simpleValues.calculatedName.values.0 | principal.process.file.full_path | Directly mapped  
name | principal.process.file.full_path | Fallback  
malop_process.elementValues.parentProcess.elementValues.0.guid | principal.process.parent_process.product_specific_process_id | Prefixed with "Cybereason:"  
malop_process.elementValues.self.elementValues.0.guid | principal.process.pid | Directly mapped  
malop_process.elementValues.self.elementValues.0.guid | principal.process.product_specific_process_id | Prefixed with "Cybereason:"  
malop_connection.elementValues.ownerProcess.elementValues.0.guid | principal.process.product_specific_process_id | Prefixed with "Cybereason:", fallback  
companyName | principal.user.company_name | Directly mapped  
malop_process.elementValues.calculatedUser.elementValues.0.name | principal.user.user_display_name | Directly mapped  
malop_data.elementValues.affectedUsers.elementValues.0.name | principal.user.user_display_name | Fallback  
malop_connection.elementValues.ownerProcess.user.elementValues.0.name | principal.user.user_display_name | Fallback  
malop_process.elementValues.calculatedUser.elementValues.0.guid | principal.user.userid | Directly mapped  
malop_data.elementValues.affectedUsers.elementValues.0.guid | principal.user.userid | Fallback  
malop_connection.elementValues.ownerProcess.user.elementValues.0.guid | principal.user.userid | Fallback  
security_result_action | security_result.action | Set to ALLOW, BLOCK, or QUARANTINE based on status  
is_alert | security_result.alert_state | Set to ALERTING if value is True  
sr_category | security_result.category | Set to SOFTWARE_MALICIOUS or NETWORK_MALICIOUS  
query_details | security_result.detection_fields | Mapped as key-value pair  
affected_machine_count | security_result.detection_fields | Mapped as key-value pair  
link_to_malop | security_result.detection_fields | Mapped as key-value pair  
context_label | security_result.detection_fields | Mapped as key-value pair  
old_state_label | security_result.detection_fields | Mapped as key-value pair  
new_state_label | security_result.detection_fields | Mapped as key-value pair  
investigation_label | security_result.detection_fields | Mapped as key-value pair  
event_id_label | security_result.detection_fields | Mapped as key-value pair  
malop_activity_type_label | security_result.detection_fields | Mapped as key-value pair  
malop_suspect_label | security_result.detection_fields | Mapped as key-value pair  
malop_key_suspicion_label | security_result.detection_fields | Mapped as key-value pair  
device_custom_date_label | security_result.detection_fields | Mapped as key-value pair  
device_custom_date2_label | security_result.detection_fields | Mapped as key-value pair  
device_custom_date3_label | security_result.detection_fields | Mapped as key-value pair  
guid_label | security_result.detection_fields | Mapped as key-value pair  
displayName_label | security_result.detection_fields | Mapped as key-value pair  
pylumId_label | security_result.detection_fields | Mapped as key-value pair  
connected_label | security_result.detection_fields | Mapped as key-value pair  
isolated_label | security_result.detection_fields | Mapped as key-value pair  
osType_label | security_result.detection_fields | Mapped as key-value pair  
admin_label | security_result.detection_fields | Mapped as key-value pair  
domainUser_label | security_result.detection_fields | Mapped as key-value pair  
localSystem_label | security_result.detection_fields | Mapped as key-value pair  
description | security_result.description | Concatenated with decision_feature, malop_status, privileges, passwordAgeDays, elementType, status, score, detectionValue, detectionValueType, detectionEngine  
decision_feature | security_result.description | Concatenated into description  
malop_status | security_result.description | Concatenated into description  
privileges | security_result.description | Concatenated into description  
passwordAgeDays | security_result.description | Concatenated into description  
elementType | security_result.description | Concatenated into description  
status | security_result.description | Concatenated into description  
score | security_result.description | Concatenated into description  
detectionValue | security_result.description | Concatenated into description  
detectionValueType | security_result.description | Concatenated into description  
detectionEngine | security_result.description | Concatenated into description  
malop_data.malopPriority | security_result.priority | Directly mapped  
malop_severity | security_result.severity | Directly mapped  
security_severity | security_result.severity | Set to CRITICAL if value > 8, HIGH if > 6, MEDIUM if > 4, LOW if > 1  
severity | security_result.severity | Set to INFORMATIONAL if "Info", ERROR if "Error" or "High", MEDIUM if "Warning" or "Medium", CRITICAL if "Critical", LOW if "Low", UNKNOWN otherwise  
description | security_result.summary | Directly mapped  
type | security_result.summary | Fallback  
malopId | security_result.threat_id | Directly mapped  
malop_data.simpleValues.detectionType.values.0 | security_result.threat_name | Directly mapped  
virusName | security_result.threat_name | Fallback  
status | security_result.threat_status | Set to ACTIVE if value is "Active", otherwise FALSE_POSITIVE  
malop_url | security_result.url_back_to_product | Directly mapped  
machineName | target.asset.hostname | Directly mapped  
affectedMachine | target.asset.hostname | Fallback  
dvchost | target.asset.hostname | Fallback  
Sensor.serverName | target.asset.hostname | Fallback  
server.ip | target.asset.ip | Directly mapped  
Sensor.serverIp | target.asset.ip | Fallback  
malop_process.simpleValues.calculatedName.values.0 | target.file.full_path | Directly mapped  
malop_connection.elementValues.ownerProcess.elementValues.0.name | target.file.full_path | Fallback  
name | target.file.full_path | Fallback  
malwareDataModel_filePath | target.file.full_path | Fallback  
malop_process.simpleValues.imageFile.md5String.values.0 | target.file.md5 | Directly mapped  
name | target.file.names | Directly mapped  
machineName | target.hostname | Directly mapped  
affectedMachine | target.hostname | Fallback  
dvchost | target.hostname | Fallback  
Sensor.serverName | target.hostname | Fallback  
server.ip | target.ip | Directly mapped  
Sensor.serverIp | target.ip | Fallback  
malop_connection.simpleValues.remoteAddressCountryName.values.0 | target.location.country_or_region | Directly mapped  
Sensor.privateServerIp | target.nat_ip | Directly mapped  
malop_connection.simpleValues.remotePort.values.0 | target.port | Converted to integer  
malop_process.simpleValues.calculatedName.values.0 | target.process.file.full_path | Directly mapped  
malop_process.elementValues.self.elementValues.0.guid | target.process.pid | Directly mapped  
malop_url | target.url | Directly mapped  
(static) | metadata.product_name | Set to "Cybereason"  
`iocs` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`mitreSubTechniques` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`decisionStatuses` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`groups` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`labels` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`LogType` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`Sensor.guid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`status` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`Sensor.fqdn` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.serviceStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.avDbVersion` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.documentProtectionMode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.antiMalwareStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.documentProtectionStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.amStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.outdated` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.collectionStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.collectiveUuid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.privateServerIp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.privateServerIp` | `event.idm.read_only_udm.target.nat_ip` | Mapped from changelog  
`Sensor.status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.siteId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.isolated` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.exitReason` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.lastUpgradeResult` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.quickScanStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.policyName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.groupId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.groupName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.groupStickinessLabel` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.fullScanStatus` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Sensor.siteName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`machine.pylumId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`needsAttention` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`id.malwareType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`referenceGuid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`referenceElementType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`schedulerScan` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`malwareDataModel` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`iconBase64` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`cs3Label", "cs4Label", "cs5Label", "deviceCustomDate1Label", "deviceCustomDate2Label" and "deviceCustomDate3Label` | `security_result.detection_fields` | Mapped from changelog  
`malop_data.simpleValues.malopActivityTypes.values.0", "malop_data.isMalicious` | `security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cybereason-edr-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
