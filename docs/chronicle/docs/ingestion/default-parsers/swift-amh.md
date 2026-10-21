---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/swift-amh/
title: Collect Swift Alliance Messaging Hub logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:54:22.780417+00:00
---

# Collect Swift Alliance Messaging Hub logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/swift-amh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Swift Alliance Messaging Hub logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Swift Alliance Messaging Hub (AMH) logs to Google Security Operations using Bindplane.

Swift Alliance Messaging Hub (AMH) is a financial messaging platform used for SWIFT network message routing, monitoring, and audit logging. The Bindplane agent collects AMH log files directly from the local file system.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Swift AMH server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Swift AMH server with administrator permissions



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



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

## Configure Bindplane agent to ingest logs and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            filelog:
                include:
                    - /opt/swift/amh/log/*.log
                start_at: beginning
        
        exporters:
            chronicle/swift_amh:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: SWIFT_AMH
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/swift_amh_to_chronicle:
                    receivers:
                        - filelog
                    exporters:
                        - chronicle/swift_amh
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths to monitor. Default Swift AMH log locations: 
      * **Linux** : `/opt/swift/amh/log/*.log` or `/var/log/swift/amh/*.log`
      * **Windows** : `C:\Swift\AMH\log\*.log`
    * `start_at`: Set to `beginning` to read existing logs or `end` to only read new entries
  * **Exporter configuration:**

    * `swift_amh`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `SWIFT_AMH`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `swift_amh_to_chronicle`: Descriptive name for the pipeline



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
         




## Configure Swift Alliance Messaging Hub logging

  1. Sign in to the **Swift AMH** server with administrator privileges.
  2. Navigate to the AMH log directory. Default paths include:

     * **Linux** : `/opt/swift/amh/log/` or `/var/log/swift/amh/`
     * **Windows** : `C:\Swift\AMH\log\`
**Note:** The exact log directory depends on your AMH installation configuration. Consult the SWIFT Alliance Messaging Hub Administration Guide for your version.
  3. Key log files include:

     * **Audit logs** (`audit*.log`): User login/logout events, message routing decisions, and configuration changes.
     * **Message logs** (`msg*.log`): SWIFT message processing, routing, and delivery events.
     * **System logs** (`system*.log`): Application start/stop, errors, and performance events.
  4. (Optional) To export additional log data from the AMH Web Console:

     1. Sign in to the **Swift AMH** web console.
     2. Go to **Monitoring > Event Journal**.
     3. Configure the date range and event filters.
     4. Click **Export** to download the event data.
     5. Save the exported file to the log directory monitored by the Bindplane agent.
  5. Ensure the Bindplane agent `include` paths in `config.yaml` match the actual log file locations on your Swift AMH server.

**Note:** The Bindplane agent service account must have read access to the Swift AMH log directory. If your installation uses non-default paths, update the `include` configuration accordingly.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
| about | Additional context or metadata about the event  
spanId, traceId, aal, mr | about.labels | Key-value pairs providing additional labels for the event  
| extensions.auth.type | Type of authentication used  
Intermediary | intermediary | Information about intermediary entities involved in the event  
target.data.message.Header.DateCreated | metadata.event_timestamp | Timestamp when the event occurred  
| metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
traceId | metadata.product_deployment_id | Identifier for the product deployment  
snmp_1_3_6_1_4_1_18494_2_1_5, event_number, product_event_type | metadata.product_event_type | Product-specific event type  
target.data.message.Header.MessageType.Code, snmp_1_3_6_1_4_1_18494_2_1_10, sag, product_object_id | metadata.product_log_id | Product-specific log identifier  
| metadata.product_version | Version of the product  
sessionid, session | network.session_id | Identifier for the network session  
data.creationDate | principal.asset.creation_time | Time when the asset was created  
target.data.message.Header.DateDelivered | principal.asset.last_discover_time | Last time the asset was discovered  
target.data.message.Status.CurrentStatus.StatusDate | principal.asset.system_last_update_time | Last system update time for the asset  
ldap_group | principal.group.group_display_name | Display name of the group  
hostname | principal.hostname | Hostname of the principal  
client | principal.ip | Source IP address of the connection  
target.data.message.Header.TransactionReference | principal.process.parent_pid | Parent process ID  
target.data.message.Header.MessageReference | principal.process.pid | Process ID  
amount, currency, offset, bussiness_element, pl | principal.resource.attribute.labels | Labels for resource attributes  
message_partner | principal.resource.name | Name of the resource  
pal | principal.user.attribute.labels | Labels for user attributes  
uumid | principal.user.product_object_id | Product-specific object ID for the user  
first_name last_name, user_HSM1 | principal.user.user_display_name | Display name of the user  
userid, record.User, user, record.Description | principal.user.userid | User identifier  
ac, sr | security_result | Result of security analysis or action  
operator | src.user.userid | Source user identifier  
act | sr.action | Action taken in the security result  
snmp_1_3_6_1_4_1_18494_2_1_9, description | sr.description | Description of the security result  
event_class | sr.rule_name | Name of the rule that triggered the security result  
| sr.severity | Severity level of the security result  
snmp_1_3_6_1_4_1_18494_2_1_6, event_severity, severity | sr.severity_details | Detailed severity information  
snmp_1_3_6_1_4_1_18494_2_1_8, summary | sr.summary | Summary of the security result  
| target.hostname | Destination hostname  
tip | target.ip | Destination IP address  
target.data.message.Header.TransferReference | target.process.pid | Target process ID  
target_display_name, user_HSM1 | target.user.user_display_name | Display name of the target user  
record.Description, user_cn, user_HSM1, userid | target.user.userid | Target user identifier  
| metadata.product_name | Name of the product  
| metadata.vendor_name | Vendor/company name  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/swift-amh-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
