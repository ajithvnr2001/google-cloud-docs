---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ipswitch-moveit-transfer/
title: Collect Progress MOVEit Transfer logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:41:12.911986+00:00
---

# Collect Progress MOVEit Transfer logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ipswitch-moveit-transfer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Progress MOVEit Transfer logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Progress MOVEit Transfer logs into Google Security Operations using Bindplane.

Progress MOVEit Transfer is a managed file transfer (MFT) solution that provides secure, encrypted file transfers using protocols such as HTTPS, FTPS, and SFTP. It offers tamper-evident audit logging, role-based access controls, and compliance support for regulations including HIPAA, PCI DSS, and GDPR. MOVEit Transfer records all file transfer activity, user authentication events, and administrative actions in its audit database.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Progress MOVEit Transfer server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * SysAdmin-level access to the Progress MOVEit Transfer web administration console
  * UDP port 514 (or your chosen syslog port) open from the MOVEit Transfer server to the Bindplane agent host



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

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/moveit_transfer:
                compression: gzip
                creds_file_path: '<CREDS_FILE_PATH>'
                customer_id: '<CUSTOMER_ID>'
                endpoint: <REGION_ENDPOINT>
                log_type: IPSWITCH_MOVEIT_TRANSFER
                raw_log_field: body
                ingestion_labels:
                    log_source: moveit_transfer
        
        service:
            pipelines:
                logs/moveit_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/moveit_transfer
        




### Configuration parameters

Replace the following placeholders.

**Exporter configuration:**

  * `<CREDS_FILE_PATH>`: Full path to ingestion authentication file: 
    * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
    * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
  * `<CUSTOMER_ID>`: Google SecOps customer ID copied earlier
  * `<REGION_ENDPOINT>`: Regional endpoint URL:

    * **US** : `malachiteingestion-pa.googleapis.com`
    * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
    * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
    * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
  * **Example configuration**
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/moveit_transfer:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: IPSWITCH_MOVEIT_TRANSFER
                raw_log_field: body
                ingestion_labels:
                    log_source: moveit_transfer
        
        service:
            pipelines:
                logs/moveit_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/moveit_transfer
        




### Save the configuration file

After editing, save the file: * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X` * **Windows** : Click **File > Save**

## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux, do the following:

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows, do the following:

  1. Choose one of the following options:

     * Command Prompt or PowerShell as administrator:
           
           net stop observiq-otel-collector && net start observiq-otel-collector
           

     * Services console:

       1. Press `Win+R`, type `services.msc`, and press Enter.
       2. Locate **observIQ OpenTelemetry Collector**.
       3. Right-click and select **Restart**.
       4. Verify the service is running:
              
              sc query observiq-otel-collector
              

       5. Check logs for errors:
              
              type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
              




## Configure Progress MOVEit Transfer syslog forwarding

To configure MOVEit Transfer to forward audit log entries to the Bindplane agent via syslog:

  1. Sign in to the **MOVEit Transfer** web administration console as a user with **SysAdmin** permissions.
  2. Go to **SETTINGS > System > Auditing > Syslog**. The **Configure Syslog Settings** page displays.
  3. In the **Syslog Logging** section, select **Enabled**. When enabled, each audit log entry is sent to the specified syslog host as well as to the MOVEit Transfer audit database.
  4. In the **Syslog Host** field, enter the IP address or hostname of the Bindplane agent host (for example, `192.168.1.100`).
  5. In the **Syslog Port** field, enter `514`. If this field is left blank, it reverts to the default port `514`.

**Note:** MOVEit Transfer uses the BSD Syslog implementation based on UDP. Ensure the port matches the `listen_address` port configured in the Bindplane agent `config.yaml`.
  6. In the **Syslog Facility** dropdown, select the facility under which MOVEit Transfer syslog messages will appear on the remote syslog host. The default value is **FTP**. The following standard syslog facilities are available:

     * KERN
     * USER
     * MAIL
     * DAEMON
     * AUTH
     * SYSLOG
     * LPR
     * NEWS
     * UUCP
     * CRON
     * AUTHPRIV
     * FTP (default)
     * LOCAL0 through LOCAL7
  7. Click **Change Logging Settings** to save the configuration.

  8. Click **Send Test Syslog Message** to send a test message to the specified Bindplane agent host. Because the BSD Syslog implementation is based on UDP, manually verify that the test message arrived by checking the Bindplane agent logs.

  9. Verify the test message was received by the Bindplane agent:

     * **Linux:**
           
           sudo journalctl -u observiq-otel-collector -f
           

     * **Windows:**
           
           type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
           




### Firewall requirements

Ensure the following firewall rule is in place to allow syslog traffic from MOVEit Transfer to the Bindplane agent:

Direction | Protocol | Source | Destination | Port  
---|---|---|---|---  
Outbound from MOVEit Transfer | UDP | MOVEit Transfer server IP | Bindplane agent host IP | 514  
  
## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
column1 | metadata.collected_timestamp | Converted using date match patterns: d/M/yyyy H:mm:ss A, M/d/yyyy H:mm:ss A, MM/dd/yyyy HH:mm:ss A  
column1 | metadata.event_timestamp | Converted using date match patterns: d/M/yyyy H:mm:ss A, M/d/yyyy H:mm:ss A, MM/dd/yyyy HH:mm:ss A  
column2 | security_result.action_details | Value copied directly  
column3 | target.hostname, target.asset.hostname | Value copied directly from column3  
column4 | principal.ip, principal.asset.ip | Extracted from column4 using grok pattern for IP  
column6 | target.file.full_path | Concatenated from folderPath and fileName if both present, else from fileName alone  
column7 | target.file.full_path |   
column15 | target.file.full_path |   
column7 | target.user.email_addresses | Merged if column2 == file_sentemail  
column10 | metadata.description | Value copied directly  
column11 | metadata.product_event_type | Value copied directly if not None  
column12 | target.ip, target.asset.ip | Extracted from column12 using grok pattern for IP  
column16 | target.file.full_path | Concatenated from folderPath and fileName if both present, else from fileName alone  
column23 | target.file.full_path |   
column19 | target.user.user_display_name | Value copied directly if column2 == file_sentemail and column8 == sender, else for target user  
event_received_time | metadata.collected_timestamp | Converted using date match patterns: UNIX_MS, dd/MM/yyyy HH:mm:ss, yyyy-MM-dd HH:mm:ss, MM/dd/yyyy HH:mm:ss A, yyyy/MM/dd HH:mm:ss, RFC 3339, yyyy-MM-ddTHH:mm:ss  
timestamp | metadata.event_timestamp | Converted using date match patterns: MMM d HH:mm:ss, MMM dd HH:mm:ss, ISO8601, yyyy-MM-dd HH:mm:ss, yyyy-MM-dd HH:mm:ss Z, MM/dd/yyyy HH:mm:ss A, yy-MM-dd HH:mm:ss, RFC 3339, yyyy-MM-ddTHH:mm:ss  
prin_ip | principal.ip, principal.asset.ip | Value copied directly  
AgentVersion | metadata.product_version | Value copied directly  
principal_host | principal.hostname, principal.asset.hostname | Value copied directly  
Username | principal.user.userid | Value copied directly  
company_name | principal.user.company_name | Value copied directly  
ID | target.process.pid | Value copied directly  
InstID | metadata.product_log_id | Value copied directly  
FileID | target.resource.attribute.labels | Merged as additional_id_2 with key FileID and value from FileID  
FolderID | target.resource.attribute.labels | Merged as additional_id_3 with key FolderID and value from FolderID  
FolderPath | target.file.full_path | Concatenated from FolderPath and FileName if both present, else from FolderPath  
FileName | target.file.full_path |   
FileName | target.resource.attribute.labels | Merged as filename with key FileName and value from FileName  
host | principal.hostname, principal.asset.hostname | Value copied directly  
log_level | security_result.severity | Set to INFORMATIONAL if INFO or DEBUG, ERROR if ERROR  
source_module_name | observer.resource.attribute.labels | Merged as source_module_label with key source_module_name and value from source_module_name  
source_module_type | observer.application | Value copied directly  
log_msg | metadata.description | Value from log_msg if http_method != GET and file_path empty, else log_desc, else description, else Message  
log_desc | metadata.description |   
description | metadata.description |   
Message | metadata.description |   
port | principal.port | Value copied directly, converted to integer  
tgtport | target.port | Value copied directly, converted to integer  
package | principal.process.command_line | Value copied directly  
srcip | principal.ip, principal.asset.ip | Value copied directly  
username | principal.user.userid | Value copied directly  
version | metadata.product_version | Value copied directly  
http_method | network.http.method | Value copied directly  
action | security_result.action_details | Value copied directly  
summary | security_result.summary | Value copied directly  
security_result | security_result | Merged directly  
tgtip | target.ip, target.asset.ip | Value copied directly  
application_proto | network.application_protocol | Uppercased and copied directly  
url | network.http.referral_url | Value copied directly  
status_code | network.http.response_code | Value copied directly, converted to integer  
file_path | principal.process.file.full_path | Value copied directly  
file_size | principal.process.file.size | Converted to uinteger if not 0  
process_id | principal.process.pid | Value copied directly  
session_id | network.session_id | Value copied directly  
task_id | additional.fields | Merged as additional_field with key TASK_ID and string_value from task_id  
AgentBrand | metadata.product_event_type | Value copied directly  
Parm1 | additional.fields | Merged as additional_field_3 with key Parm1 and string_value from Parm1  
Parm2 | additional.fields | Merged as additional_field_4 with key Parm2 and string_value from Parm2  
Error | additional.fields | Merged as additional_field_5 with key Error and string_value from Error  
XFerSize | target.resource.attribute.labels | Merged as additional_field_1 with key XFerSize and value from XFerSize  
FolderPath | metadata.event_type | Set to FILE_DELETION if FolderPath and action_performed matches Delete File, NETWORK_HTTP if tgtip or host and application_proto == HTTP, USER_LOGIN if Username or username, STATUS_UPDATE if tgtip or host or principal_host or IPAddress, else GENERIC_EVENT  
tgtip | metadata.event_type |   
host | metadata.event_type |   
principal_host | metadata.event_type |   
IPAddress | metadata.event_type |   
Username | metadata.event_type |   
username | metadata.event_type |   
tgtip | metadata.event_type | Set to USER_LOGIN if column2 == sec_signon and tgtip or tar_host, USER_LOGOUT if sec_signoff and tgtip or tar_host, FILE_UNCATEGORIZED if folder_add, FILE_CREATION if file_upload or download and tgtip and is_tgt_file_present, FILE_DELETION if file_delete and srcip and is_tgt_file_present, FILE_MODIFICATION if file_rename, FILE_UNCATEGORIZED if file_dlhashchk, EMAIL_TRANSACTION if file_sentemail and useremail, STATUS_UPDATE if srcip, else GENERIC_EVENT  
tar_host | metadata.event_type |   
srcip | metadata.event_type |   
is_tgt_file_present | metadata.event_type |   
column2 | metadata.event_type |   
useremail | metadata.event_type |   
security_result | metadata.event_type |   
extensions.auth.type | extensions.auth.type | Set to MACHINE for login/logout events  
metadata.vendor_name | metadata.vendor_name | Set to "IPS"  
metadata.product_name | metadata.product_name | Set to "IPSWITCH MOVEIT TRANSFER"  
`target_application` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`product_event` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`dstip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`AdminTrust` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Permission` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`log_status` | `event.idm.read_only_udm.security_result.action.details` | Mapped from changelog  
`srcip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`EventReceivedTime` | `event.timestamp` | Mapped from changelog  
`SourceModuleName` | `observer.resource.attribute.labels` | Mapped from changelog  
`SourceModuleType` | `observer.application` | Mapped from changelog  
`SourceName` | `metadata.product_event_type` | Mapped from changelog  
`Severity` | `security_result.` | Mapped from changelog  
`Hostname` | `principal.hostname` | Mapped from changelog  
`Channel` | `security_result.about.resource.attribute.labels` | Mapped from changelog  
`AgentVersion` | `metadata.version` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ipswitch-moveit-transfer-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
