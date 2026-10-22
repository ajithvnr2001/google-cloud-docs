---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/juniper-junos/
title: Collect Juniper Junos logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:54.080251+00:00
---

# Collect Juniper Junos logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/juniper-junos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Juniper Junos logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Juniper Junos logs to Google Security Operations using Bindplane.

Juniper Junos OS is the operating system that powers Juniper Networks routers, switches, and security devices. It provides a unified platform for network infrastructure management, routing, switching, and security functions with comprehensive logging of system events, security events, and network traffic. The parser extracts fields from Juniper Junos syslog and key-value formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Juniper device running Junos OS



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
            log_type: 'JUNIPER_JUNOS'
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

  * Replace the following placeholders:

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
      * `log_type`: Log type exactly as it appears in Chronicle (`JUNIPER_JUNOS`)



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: 'JUNIPER_JUNOS'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    2. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * To restart the Bindplane agent in Windows, choose one of the following options: 

    * Command Prompt or PowerShell as administrator:
          
          net stop observiq-otel-collector && net start observiq-otel-collector
          

    * Services console:

      1. Press `Win+R`, type `services.msc`, and press **Enter**.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.

      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure Syslog forwarding on Juniper Junos

  1. Connect to the **Juniper** device via SSH or console.
  2. Enter configuration mode:
         
         configure
         

  3. Configure the syslog host with the following commands:
         
         set system syslog host BINDPLANE_IP any info
         set system syslog host BINDPLANE_IP port 514
         set system syslog host BINDPLANE_IP facility-override local7
         set system syslog host BINDPLANE_IP log-prefix JUNOS
         

     * Replace `BINDPLANE_IP` with the IP address of the Bindplane agent host.
  4. Configure additional log sources (optional but recommended):
         
         set system syslog host BINDPLANE_IP authorization info
         set system syslog host BINDPLANE_IP daemon info
         set system syslog host BINDPLANE_IP kernel info
         set system syslog host BINDPLANE_IP firewall any
         set system syslog host BINDPLANE_IP interactive-commands info
         

  5. Configure structured syslog data (optional for enhanced parsing):
         
         set system syslog host BINDPLANE_IP structured-data
         

  6. Commit the configuration:
         
         commit and-quit
         

  7. Verify the syslog configuration:
         
         show system syslog host BINDPLANE_IP
         

  8. Verify syslog messages are being sent by checking the Bindplane agent logs.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
DPT | target.port | The destination port of the network connection, converted to an integer.  
DST | target.ip | The destination IP address of the network connection.  
FLAG | additional.fields{}.key: "FLAG", additional.fields{}.value.string_value: Value of FLAG | The TCP flag associated with the network connection.  
ID | additional.fields{}.key: "ID", additional.fields{}.value.string_value: Value of ID | The IP identification field.  
IN | additional.fields{}.key: "IN", additional.fields{}.value.string_value: Value of IN | The incoming network interface.  
LEN | additional.fields{}.key: "LEN", additional.fields{}.value.string_value: Value of LEN | The length of the IP packet.  
MAC | principal.mac | The MAC address extracted from the MAC field.  
OUT | additional.fields{}.key: "OUT", additional.fields{}.value.string_value: Value of OUT | The outgoing network interface.  
PREC | additional.fields{}.key: "PREC", additional.fields{}.value.string_value: Value of PREC | The Precedence field in the IP header.  
PROTO | network.ip_protocol | The IP protocol used in the network connection.  
RES | additional.fields{}.key: "RES", additional.fields{}.value.string_value: Value of RES | Reserved field in the TCP header.  
SPT | principal.port | The source port of the network connection, converted to an integer.  
SRC | principal.ip | The source IP address of the network connection.  
TOS | additional.fields{}.key: "TOS", additional.fields{}.value.string_value: Value of TOS | The Type of Service field in the IP header.  
TTL | network.dns.additional.ttl | Time To Live value, converted to an unsigned integer.  
URGP | additional.fields{}.key: "URGP", additional.fields{}.value.string_value: Value of URGP | Urgent pointer field in the TCP header.  
WINDOW | additional.fields{}.key: "WINDOW_SIZE", additional.fields{}.value.string_value: Value of WINDOW | The TCP window size.  
action | security_result.action | The action taken by the firewall, extracted from the CEF message.  
agt | observer.ip | The IP address of the agent.  
amac | target.mac | The MAC address of the target, converted to lowercase and with hyphens replaced by colons.  
app | target.application | The application involved in the event.  
artz | observer.zone | The observer time zone.  
atz | target.location.country_or_region | The target time zone.  
categoryBehavior | additional.fields{}.key: "Category Behavior", additional.fields{}.value.string_value: Value of categoryBehavior with slashes removed | The category behavior.  
categoryDeviceGroup | additional.fields{}.key: "Category Device Group", additional.fields{}.value.string_value: Value of categoryDeviceGroup with slashes removed | The category device group.  
categoryObject | additional.fields{}.key: "Category Object", additional.fields{}.value.string_value: Value of categoryObject with slashes removed | The category object.  
categoryOutcome | additional.fields{}.key: "Category Outcome", additional.fields{}.value.string_value: Value of categoryOutcome with slashes removed | The category outcome.  
categorySignificance | additional.fields{}.key: "category Significance", additional.fields{}.value.string_value: Value of categorySignificance | The category significance.  
command | target.process.command_line | The command executed.  
cs1Label | additional.fields{}.key: cs1Label, additional.fields{}.value.string_value: Value of corresponding CEF field | Custom string field 1 label and value from the CEF message.  
cs2Label | additional.fields{}.key: cs2Label, additional.fields{}.value.string_value: Value of corresponding CEF field | Custom string field 2 label and value from the CEF message.  
cs3Label | additional.fields{}.key: cs3Label, additional.fields{}.value.string_value: Value of corresponding CEF field | Custom string field 3 label and value from the CEF message.  
cs4Label | additional.fields{}.key: cs4Label, additional.fields{}.value.string_value: Value of corresponding CEF field | Custom string field 4 label and value from the CEF message.  
cs5Label | additional.fields{}.key: cs5Label, additional.fields{}.value.string_value: Value of corresponding CEF field | Custom string field 5 label and value from the CEF message.  
cs6Label | additional.fields{}.key: cs6Label, additional.fields{}.value.string_value: Value of corresponding CEF field | Custom string field 6 label and value from the CEF message.  
dhost | target.hostname | Destination hostname.  
deviceCustomString1 | additional.fields{}.key: cs1Label, additional.fields{}.value.string_value: Value of deviceCustomString1 | Device custom string 1.  
deviceCustomString2 | additional.fields{}.key: cs2Label, additional.fields{}.value.string_value: Value of deviceCustomString2 | Device custom string 2.  
deviceCustomString3 | additional.fields{}.key: cs3Label, additional.fields{}.value.string_value: Value of deviceCustomString3 | Device custom string 3.  
deviceCustomString4 | additional.fields{}.key: cs4Label, additional.fields{}.value.string_value: Value of deviceCustomString4 | Device custom string 4.  
deviceCustomString5 | additional.fields{}.key: cs5Label, additional.fields{}.value.string_value: Value of deviceCustomString5 | Device custom string 5.  
deviceCustomString6 | additional.fields{}.key: cs6Label, additional.fields{}.value.string_value: Value of deviceCustomString6 | Device custom string 6.  
deviceDirection | network.direction | The direction of the network traffic.  
deviceEventClassId | additional.fields{}.key: "eventId", additional.fields{}.value.string_value: Value of deviceEventClassId | The device event class ID.  
deviceFacility | observer.product.subproduct | The device facility.  
deviceProcessName | about.process.command_line | The device process name.  
deviceSeverity | security_result.severity | The device severity.  
deviceTimeZone | observer.zone | The device time zone.  
deviceVendor | metadata.vendor_name | The device vendor.  
deviceVersion | metadata.product_version | The device version.  
dpt | target.port | The destination port.  
dst | target.ip | The destination IP address.  
duser | target.user.user_display_name | The destination user.  
eventId | additional.fields{}.key: "eventId", additional.fields{}.value.string_value: Value of eventId | Event ID.  
event_time | metadata.event_timestamp | The time the event occurred, parsed from the message.  
firewall_action | security_result.action_details | The firewall action taken.  
host | principal.hostname, intermediary.hostname | The hostname of the device generating the log. Used for both principal and intermediary in different cases.  
msg | security_result.summary | The message associated with the event, used as a summary for the security result.  
name | metadata.product_event_type | The name of the event.  
process_name | additional.fields{}.key: "process_name", additional.fields{}.value.string_value: Value of process_name | The name of the process.  
p_id | target.process.pid | The process ID, converted to a string.  
sha256 | principal.process.file.sha256 | The SHA256 hash of a file, extracted from the SSH2 key information.  
shost | principal.hostname | Source hostname.  
source_address | principal.ip | The source IP address.  
source_port | principal.port | The source port, converted to an integer.  
src | principal.ip | The source IP address.  
src_ip | principal.ip | The source IP address.  
src_port | principal.port | The source port, converted to an integer.  
ssh2 | security_result.detection_fields{}.key: "ssh2", security_result.detection_fields{}.value: Value of ssh2 | SSH2 key information.  
subtype | metadata.product_event_type | The subtype of the event.  
task_summary | security_result.description | The task summary, used as the description for the security result.  
timestamp | metadata.event_timestamp | The timestamp of the event.  
user | target.user.userid | The user associated with the event.  
username | principal.user.userid | The username associated with the event.  
user_name | principal.user.userid | The username.  
| metadata.vendor_name | Hardcoded to "Juniper Firewall". Hardcoded to "Juniper Firewall". Hardcoded to "JUNIPER_JUNOS". Determined by parser logic based on log content. Defaults to "STATUS_UPDATE" if not a CEF message and no other specific event type is identified. Set to "NETWORK_HTTP" for CEF messages. If no desc field is present, this field is populated with the message_description extracted from the raw log message.  
`protocol-name` | `network.ip_protocol` | Mapped from changelog  
`application_name` | `target.application` | Mapped from changelog  
`desc` | `sec_result.summary` | Mapped from changelog  
`mac-address` | `principal.mac` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-junos-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
