---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arbor-sightline/
title: Collect Netscout Arbor Sightline logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:42.703116+00:00
---

# Collect Netscout Arbor Sightline logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/arbor-sightline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Netscout Arbor Sightline logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Netscout Arbor Sightline logs into Google Security Operations using Bindplane agent.

Netscout Arbor Sightline (formerly Peakflow SP) is a DDoS detection and network visibility platform that provides robust capabilities from network-wide capacity planning to identifying and managing the mitigation of DDoS and other threats to the network. Sightline collects and analyzes flow data, BGP routing information, and SNMP data to detect anomalies, generate alerts, and coordinate mitigation responses.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Netscout Arbor Sightline appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Netscout Arbor Sightline web interface
  * Administrative access to the Netscout Arbor Sightline command-line interface (CLI) for system alert configuration



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

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * Linux:
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * Windows:
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  1. Replace the entire contents of `config.yaml` with the following configuration:
         
         receivers:
           udplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/arbor_sightline:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '<CREDS_FILE_PATH>'
             customer_id: '<CUSTOMER_ID>'
             endpoint: chronicle.googleapis.com
             log_type: ARBOR_SIGHTLINE
             raw_log_field: body
             ingestion_labels:
               env: production
         
         service:
           pipelines:
             logs/arbor_to_chronicle:
               receivers:
                 - udplog
               exporters:
                 - chronicle/arbor_sightline
         

  2. Replace the following placeholders:

     * Receiver configuration:

       * The receiver is configured to listen on UDP port 514 on all interfaces (`0.0.0.0:514`)
       * If you need to use a different port (for example, `1514` for non-root Linux installations), modify the `listen_address` value
       * If you prefer TCP syslog, replace `udplog` with `tcplog` in both the receivers section and the pipeline
     * Exporter configuration:

       * `<CREDS_FILE_PATH>`: Full path to the service account JSON key file (Option 1):

         * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
         * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
       * `<CUSTOMER_ID>`: Customer ID from the previous step

       * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

       * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

       * `endpoint`: Keep set to `chronicle.googleapis.com`.

       * `log_type`: Set to `ARBOR_SIGHTLINE` (exact match required)

       * `ingestion_labels`: Optional labels in YAML format (modify as needed for your environment)




### Example configuration
    
    
    receivers:
      udplog:
        listen_address: "0.0.0.0:514"
    
    exporters:
      chronicle/arbor_sightline:
        protocol: https
        # Region of your instance, for example us, europe, asia-southeast1
        location: <LOCATION>
        # Project number of the Google Cloud project linked to the instance
        project: '<PROJECT_NUMBER>'
        compression: gzip
        creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
        customer_id: 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
        endpoint: chronicle.googleapis.com
        log_type: ARBOR_SIGHTLINE
        raw_log_field: body
        ingestion_labels:
          env: production
          source: sightline
    
    service:
      pipelines:
        logs/arbor_to_chronicle:
          receivers:
            - udplog
          exporters:
            - chronicle/arbor_sightline
    

### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/arbor_sightline:
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ARBOR_SIGHTLINE
            raw_log_field: body
            ingestion_labels:
              env: production
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
  * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux:

    1. Run the following command:
           
           sudo systemctl restart observiq-otel-collector
           

    2. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    3. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * To restart the Bindplane agent in Windows:

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
           




## Configure Netscout Arbor Sightline syslog forwarding

To send logs to Google SecOps, you must configure Netscout Arbor Sightline to forward syslog events to the Bindplane agent. This involves creating a notification group, configuring global notification settings, and setting up alert notification rules.

### Create a notification group

  1. Sign in to the **Netscout Arbor Sightline** web interface as an administrator.
  2. Go to **Administration > Notification > Groups**.
  3. Click **Add Notification Group**.
  4. Provide the following configuration details: 
     * **Destinations** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (or the port configured in the Bindplane agent, such as `1514`).
     * **Facility** : Select a syslog facility (for example, `local0` or `user`).
     * **Severity** : Select `info`. The informational severity collects all event messages at the informational event level and higher severity.
  5. Click **Save**.
  6. Click **Configuration Commit** to apply the configuration changes.

**Note:** The notification group defines where syslog messages are sent. You can create multiple notification groups for different destinations.



### Configure global notification settings

Global notifications in Netscout Arbor Sightline provide system notifications that are not associated with specific alert rules.

  1. In the Netscout Arbor Sightline web interface, go to **Administration > Notification > Global Settings**.
  2. In the **Default Notification Group** field, select the notification group you created for Google SecOps.
  3. Click **Save**.
  4. Click **Configuration Commit** to apply the configuration changes.



### Enable system alert notifications

System alerts require additional configuration via the command-line interface (CLI).

  1. Sign in to the **Netscout Arbor Sightline** command-line interface as an administrator.
  2. List the current system alert configuration:
         
         services sp alerts system_errors show
         

  3. To list available system alert field names that can be configured, run:
         
         services sp alerts system_errors ?
         

  4. Enable notifications for system alerts. For each alert type you want to enable, run:
         
         services sp alerts system_errors <alert_name> notifications enable
         

Replace `<alert_name>` with the specific system alert field name (for example, `disk_full`, `flow_collector_down`, `license_expiring`).

  5. Commit the configuration changes:
         
         config write
         

**Note:** System alerts include critical events such as disk space issues, service failures, and license warnings. Enable notifications for alerts relevant to your monitoring requirements.



### Configure alert notification rules

Alert notification rules determine which alerts trigger syslog notifications to Google SecOps.

  1. In the Netscout Arbor Sightline web interface, go to **Administration > Notification > Rules**.
  2. Choose one of the following options: 
     * Click an existing rule to edit it.
     * Click **Add Rule** to create a new notification rule.
  3. Configure the following values: 
     * **Name** : Enter a descriptive name for the rule (for example, `Chronicle-DDoS-Alerts`).
     * **Resource** : Enter a CIDR address or select a managed object from the list of Sightline resources. To apply the rule to all resources, leave this field empty or select **All**.
     * **Importance** : Select the minimum importance level for alerts (for example, `Low`, `Medium`, `High`, or `Critical`). Alerts at or above this level will trigger notifications.
     * **Notification Group** : Select the notification group you created for Google SecOps.
  4. Repeat these steps to configure additional rules as needed for different resources or importance levels.
  5. Click **Save**.
  6. Click **Configuration Commit** to apply the configuration changes.

**Note:** Alert notification rules can be scoped to specific managed objects (customer networks, peer networks) and importance levels. Create multiple rules to fine-tune which alerts are sent to Google SecOps.



### Test syslog connectivity

After configuring the notification group and rules, verify that syslog messages are being sent to the Bindplane agent.

  1. In the Netscout Arbor Sightline CLI, test the syslog connection:
         
         services sp notification test syslog group <notification_group_name>
         

Replace `<notification_group_name>` with the name of the notification group you created.

  2. The command should return:
         
         Server returned: Success
         

  3. Check the Bindplane agent logs to verify that test messages are being received:

**Linux:**
         
         sudo journalctl -u observiq-otel-collector -f
         

**Windows:**
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         

  4. In the Google SecOps console, go to **Search** and verify that Netscout Arbor Sightline logs are appearing with the ingestion label `ARBOR_SIGHTLINE`.

**Note:** It may take several minutes for logs to appear in Google SecOps after initial configuration. If no logs appear, verify network connectivity between Sightline, the Bindplane agent, and Google SecOps.



## Event types forwarded to Google SecOps

  * Netscout Arbor Sightline forwards the following event categories via syslog:

    * **Denial of Service (DoS) events** : DDoS attack detection alerts, including volumetric attacks, protocol attacks, and application-layer attacks
    * **Authentication events** : User login successes and failures, authentication attempts
    * **Exploit events** : Detected exploit attempts and suspicious traffic patterns
    * **Suspicious activity events** : Anomalous traffic behavior and potential security threats
    * **System events** : Appliance health, service status, configuration changes, and operational alerts
    * **Mitigation events** : Mitigation start, stop, and status updates for DDoS attacks
**Note:** The specific events forwarded depend on your notification rules configuration. Adjust the importance levels and resource scopes in your notification rules to control which events are sent to Google SecOps.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
msg1 | additional.fields | Merged with labels from each field if not empty, using specific keys like "message_description" for msg1, "config_version" for config_version, etc.  
config_version | additional.fields |   
prin_user | additional.fields |   
old_bgp_attributes | additional.fields |   
new_bgp_attributes | additional.fields |   
reason | additional.fields |   
sample_rate | additional.fields |   
proto | additional.fields |   
flows | additional.fields |   
identifier | additional.fields |   
expected_bps | additional.fields |   
actual_bps | additional.fields |   
server | additional.fields |   
status | additional.fields |   
percent | additional.fields |   
rate | additional.fields |   
rateunit | additional.fields |   
flags | additional.fields |   
router | additional.fields |   
interface | additional.fields |   
ip_ver | additional.fields |   
protocol_id | additional.fields |   
router_name | additional.fields |   
interface_id | additional.fields |   
interface_name | additional.fields |   
priority | additional.fields |   
log_level | additional.fields |   
pool | additional.fields |   
thread_id | additional.fields |   
timeout | additional.fields |   
attempts | additional.fields |   
vulns | extensions.vulns.vulnerabilities | Merged if vulns not empty  
desc | metadata.description | Set to "%{desc}: %{desc2}" if both desc and desc2 not empty, else desc; overwritten by message_desc if not empty  
desc2 | metadata.description |   
message_desc | metadata.description |   
event_time | metadata.event_timestamp | Converted using date filter with format MMM dd HH:mm:ss or MMM d HH:mm:ss, timezone Europe/London  
desc2 | metadata.event_type | Set to "SCAN_PROCESS" if desc2 matches "(DNS Amplification  
message | metadata.event_type |   
src_ip | metadata.event_type |   
has_target_ip | metadata.event_type |   
has_network_protocol | metadata.event_type |   
host_name | metadata.event_type |   
message | metadata.product_event_type | Set to "Host Detection" if message matches "Host Detection"; "TMS Mitigation started" if message matches " started"; "TMS Mitigation stopped" if message matches " stopped"  
metadata.product_name | metadata.product_name | Set to "ARBOR_SIGHTLINE"  
metadata.vendor_name | metadata.vendor_name | Set to "NETSCOUT"  
direction | network.direction | Set to "INBOUND" if direction "incoming"  
proto | network.ip_protocol | Set to "TCP" if proto "6"; else set to uppercase network_protocol if matches "(?i)(TCP  
network_protocol | network.ip_protocol |   
bytes | network.sent_bytes | Value copied directly, converted to uinteger  
packets | network.sent_packets | Value copied directly, converted to integer  
duration | network.session_duration.seconds | Value copied directly if not empty and not "0", converted to integer  
host_name | principal.hostname | Value copied directly  
src_ip | principal.ip | Merged from src_ip and nameserver_ip  
nameserver_ip | principal.ip |   
namespace | principal.namespace | Value copied directly  
filename | principal.process.file.full_path | Value copied directly  
alert_id | principal.process.pid | Value copied directly  
prin_url | principal.url | Value copied directly  
prin_user | principal.user.userid | Value copied directly  
impact | security_result.detection_fields | Merged with keys "Impact" from impact, "Importance" from importance, "Signature" from signature, "Leader" from leader, "parent_managed_object" from parent_managed_object, "Alert ID" from alert_id  
importance | security_result.detection_fields |   
signature | security_result.detection_fields |   
leader | security_result.detection_fields |   
parent_managed_object | security_result.detection_fields |   
alert_id | security_result.detection_fields |   
severity | security_result.severity | Set to "INFORMATIONAL" if severity in ["10","9"]; "LOW" if in ["8","7"]; "MEDIUM" if "6"; "HIGH" if in ["5","4"]; "CRITICAL" if in ["3","2","1"]  
desc2 | security_result.threat_status | Set to "ACTIVE" if desc matches "Host Detection alert" and message "start" and not "stop"; "CLEARED" if desc matches "Host Detection alert" and message "stop"  
message | security_result.threat_status |   
intem_host | target.group.product_object_id | Value copied directly  
dst_ip | target.ip | Value copied directly  
dst_port | target.port | Value copied directly, converted to integer  
file_path | target.process.file.full_path | Value copied directly  
stop_time | vulns.vulnerabilities.scan_end_time | Converted using date filter with format yyyy-MM-dd HH:mm:ss  
start_time | vulns.vulnerabilities.scan_start_time | Converted using date filter with format yyyy-MM-dd HH:mm:ss or yyyy-MM-dd  
`msg1` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`prin_user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`config_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`old_bgp_attributes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`new_bgp_attributes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`reason` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sample_rate` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`proto` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`proto` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`bytes` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`packets` | `event.idm.read_only_udm.network.sent_packets` | Mapped from changelog  
`flows` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`identifier` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`expected_bps` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`actual_bps` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`server` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`percent` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rate` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rateunit` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`flags` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`router` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`interface` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ip_ver` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`protocol_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`router_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`interface_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`interface_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`network_protocol` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`prin_url` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`src_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`dst_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`dst_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`Active/Cleared` | `security_result.threat_status` | Mapped from changelog  
`alert_id","parent_managed_object` | `security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arbor-sightline-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
