---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-utm/
title: Collect Sophos UTM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:52.334950+00:00
---

# Collect Sophos UTM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-utm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Sophos UTM logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Sophos UTM logs to Google Security Operations using Bindplane.

**Note:** Sophos UTM and SG Series hardware reach End of Life on June 30, 2026. For new deployments, consider migrating to Sophos Firewall (SFOS) on XGS hardware. This guide applies to existing Sophos UTM deployments.

Sophos UTM (Unified Threat Management) is an all-in-one network security appliance that provides firewall, VPN, intrusion prevention, web filtering, email filtering, and antivirus capabilities. It offers centralized security management for enterprise networks through a single web-based management console. The parser extracts fields from Sophos UTM KV formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Sophos UTM WebAdmin interface



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

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
          chronicle/chronicle_w_labels:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: 'SOPHOS_UTM'
            raw_log_field: body
            ingestion_labels:
        
        service:
          pipelines:
            logs/source0__chronicle_w_labels-0:
              receivers:
                - udplog
              exporters:
                - chronicle/chronicle_w_labels
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: Use `udplog` for UDP syslog or `tcplog` for TCP syslog
    * `0.0.0.0`: IP address to listen on (`0.0.0.0` to listen on all interfaces)
    * `514`: Port number to listen on (standard syslog port)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1):

      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `YOUR_CUSTOMER_ID`: Customer ID from the Get customer ID section

    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

    * `endpoint`: Keep set to `chronicle.googleapis.com`.

    * `log_type`: Log type exactly as it appears in Chronicle (`SOPHOS_UTM`)




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'SOPHOS_UTM'
            raw_log_field: body
            ingestion_labels:
        


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
         




## Configure Syslog forwarding on Sophos UTM

  1. Sign in to the **Sophos UTM** WebAdmin interface.
  2. Go to **Logging & Reporting > Log Settings > Remote Syslog Server**.
  3. Click the toggle to **Enable** remote syslog.
  4. Provide the following configuration details: 
     * **Remote Syslog Server** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
  5. In the **Remote Syslog Log Selection** section, select the log types to forward:

     * **Packet Filter** : Firewall packet filter logs
     * **Web Filter** : Web filtering activity
     * **IPS** : Intrusion Prevention System events
     * **Authentication** : User authentication events
     * **Email** : Email filtering and quarantine events
     * **Network Protection** : Advanced threat protection logs
     * **WebServer Protection** : WAF logs
     * **VPN** : VPN connection events
     * **HA/Cluster** : High availability and cluster events
     * **System** : System-level events
     * **DHCP** : DHCP server logs
     * **DNS** : DNS query logs
  6. Click **Apply** to save the configuration.

  7. Verify syslog messages are being sent by checking the Bindplane agent logs.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
action | security_result.action | If action is "pass" or "accept", map to "ALLOW". If action is "drop", map to "BLOCK".  
ad_domain | target.administrative_domain | Direct mapping.  
address | target.ip, target.asset.ip | Direct mapping, used when id is "2203".  
app | target.application | Direct mapping.  
app-id | additional.fields[].key, additional.fields[].value.string_value | Renamed to app_id. If not empty, the key is set to "app-id" and the value is the app-id itself.  
application | principal.application | Direct mapping.  
aptptime | additional.fields[].key, additional.fields[].value.string_value | If not empty, the key is set to "aptptime" and the value is the aptptime itself.  
auth | extensions.auth.auth_details | Direct mapping.  
authtime | additional.fields[].key, additional.fields[].value.string_value | If not empty and not "0", the key is set to "authtime" and the value is the authtime itself.  
avscantime | additional.fields[].key, additional.fields[].value.string_value | If not empty and not "0", the key is set to "avscantime" and the value is the avscantime itself.  
category | security_result.detection_fields[].key, security_result.detection_fields[].value | If not empty, the key is set to "category" and the value is the category itself. If name contains "portscan", security_result.category is set to "NETWORK_RECON" and a detection field with key "category" and value "NETWORK_RECON" is added.  
categoryname | security_result.category_details | Direct mapping.  
connection | security_result.rule_name | Direct mapping, used when id is "2203".  
content-type data | (See other fields) | The data field contains key-value pairs that are parsed into individual fields.  
datetime | metadata.event_timestamp | Parsed and mapped as seconds since epoch.  
device | additional.fields[].key, additional.fields[].value.string_value | If not empty and not "0", the key is set to "device" and the value is the device itself.  
dnstime | additional.fields[].key, additional.fields[].value.string_value | If not empty and not "0", the key is set to "dnstime" and the value is the dnstime itself.  
dstip | target.ip, target.asset.ip | Direct mapping. Also extracted from the url field if present.  
dstmac | target.mac | Direct mapping.  
dstport | target.port | Direct mapping, converted to integer.  
error event | security_result.summary | Direct mapping, used when id is "2201", "2202", or "2203".  
exceptions | additional.fields[].key, additional.fields[].value.string_value | If not empty, the key is set to "exceptions" and the value is the exceptions itself.  
file | about.file.full_path | Direct mapping.  
filteraction | security_result.rule_name | Direct mapping.  
fullreqtime | additional.fields[].key, additional.fields[].value.string_value | If not empty, the key is set to "fullreqtime" and the value is the fullreqtime itself.  
fwrule | security_result.rule_id | Direct mapping.  
group | target.group.group_display_name | Direct mapping.  
id | metadata.product_log_id | Direct mapping.  
info | security_result.description | Direct mapping. If present, metadata.event_type is set to "NETWORK_UNCATEGORIZED".  
initf interface | security_result.about.labels[].key, security_result.about.labels[].value | If not empty, a label with key "Interface" and value interface is added to security_result.about.labels.  
ip_address | target.ip, target.asset.ip | Direct mapping.  
length line message | security_result.summary | Used when id is "0003". Also used for general grok parsing.  
method | network.http.method | Direct mapping.  
name | security_result.summary | Direct mapping.  
outitf pid | target.process.pid | Direct mapping.  
port | target.port | Direct mapping, converted to integer.  
prec profile | security_result.rule_name | Direct mapping.  
proto | network.ip_protocol | Converted to IP protocol name using a lookup table.  
reason referer | network.http.referral_url | Direct mapping.  
request | additional.fields[].key, additional.fields[].value.string_value | If not empty, the key is set to "request" and the value is the request itself.  
reputation | additional.fields[].key, additional.fields[].value.string_value | If not empty, the key is set to "reputation" and the value is the reputation itself.  
rx | network.received_bytes | Direct mapping, used when id is "2202", converted to unsigned integer.  
sandbox severity | security_result.severity | If severity is "info", map to "LOW".  
size | target.file.size | Direct mapping, converted to unsigned integer.  
srcip | principal.ip, principal.asset.ip | Direct mapping.  
srcmac | principal.mac | Direct mapping.  
srcport | principal.port | Direct mapping, converted to integer.  
statuscode | network.http.response_code | Direct mapping, converted to integer.  
sub | network.application_protocol | If sub is "http", the metadata.event_type is set to "NETWORK_HTTP" and network.application_protocol is set to "HTTP". If sub is "packetfilter", metadata.description is set to sub. Otherwise, converted to application protocol name using a lookup table. If no match is found in the lookup table, the dstport is used for the lookup.  
sys | metadata.product_event_type | Direct mapping.  
tcpflags tos ttl tx | network.sent_bytes | Direct mapping, used when id is "2202", converted to unsigned integer.  
ua | network.http.user_agent | Direct mapping.  
url | network.http.referral_url, target.hostname, target.asset.hostname | Direct mapping for network.http.referral_url. Extracted hostname for target.hostname and target.asset.hostname. Also used to extract dstip.  
user | target.user.userid | Direct mapping.  
username | target.user.userid | Direct mapping, used when id is "2201" or "2202".  
variant | Not included in final UDM, but used in description | Used in conjunction with sub to create the security_result.description when id is "2201", "2202", or "2203".  
virtual_ip | target.ip, target.asset.ip | Direct mapping, used when id is "2201" or "2202".  
metadata.event_type | metadata.event_type | Initialized to "GENERIC_EVENT". Set to specific values based on log content and parser logic.  
metadata.log_type | metadata.log_type | Hardcoded to "SOPHOS_UTM".  
metadata.product_name | metadata.product_name | Hardcoded to "SOPHOS UTM".  
metadata.vendor_name | metadata.vendor_name | Hardcoded to "SOPHOS Ltd".  
intermediary.hostname | intermediary.hostname | Extracted from the log message using grok and renamed.  
`content-type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`reason` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`referer` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`subject` | `network.email.subject` | Mapped from changelog  
`from` | `network.email.from` | Mapped from changelog  
`to` | `network.email.to` | Mapped from changelog  
`virus` | `security_result.detection_fields` | Mapped from changelog  
`filename` | `target.file.names` | Mapped from changelog  
`severity` | `security_result.severity_details` | Mapped from changelog  
`inter_host` | `intermediary.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-utm-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
