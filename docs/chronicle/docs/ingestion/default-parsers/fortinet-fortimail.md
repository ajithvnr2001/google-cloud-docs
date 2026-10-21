---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortimail/
title: Collect Fortinet FortiMail logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:46:31.920008+00:00
---

# Collect Fortinet FortiMail logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortimail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fortinet FortiMail logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Fortinet FortiMail logs to Google Security Operations using the Bindplane agent.

Fortinet FortiMail is an email security gateway that generates syslog messages for email transactions, spam filtering, virus detection, authentication events, and policy enforcement. The parser extracts key-value pairs, normalizes timestamps and IP addresses, and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Fortinet FortiMail
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Fortinet FortiMail



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

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

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

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
            chronicle/fortinet_fortimail:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: FORTINET_FORTIMAIL
                raw_log_field: body
        
        service:
            pipelines:
                logs/fortinet_fortimail_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/fortinet_fortimail
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



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

      1. Press `Win+R`, type `services.msc`, and press Enter.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.
      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure Fortinet FortiMail syslog

  1. Sign in to the FortiMail device web interface.
  2. Select **Log & Report > Log Settings > Remote**.
  3. Click **New** to create a new entry.
  4. In the dialog that appears, select **Enable** to allow logging to a remote host.
  5. Provide the following details: 
     * **Name** : Enter a unique and meaningful name.
     * **Server name/IP** : Enter the **Bindplane** IP address.
     * **Server port** : Enter the **Bindplane** UDP port number.
     * **Level** : Select **Information** as severity level.
     * **Facility** : Enter a unique facility identifier and verify that no other network devices use the same facility identifier.
     * Deselect **CSV format**.
     * **Log protocol** : Select **Syslog**.
     * **Logging policy configuration** : Enable all types of events or logs to be forwarded.
  6. Click **Create**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
authid | read_only_udm.target.user.email_addresses | If `authid` field contains `@` then map to this field  
authid | read_only_udm.target.user.userid | Map `authid` field to this field  
cipher | read_only_udm.network.tls.cipher | Map `cipher` field to this field  
client_ip | read_only_udm.principal.ip | Map `client_ip` field to this field  
client_name | read_only_udm.principal.hostname | Map `client_name` field to this field  
detail | read_only_udm.security_result.summary | Map `detail` field to this field  
device_id | read_only_udm.principal.resource.id | Map `device_id` field to this field  
devname | read_only_udm.principal.resource.name | Map `devname` field to this field  
direction | read_only_udm.network.direction | If `direction` field is equal to `out` then map value `OUTBOUND`, if `direction` field is equal to `in` then map value `INBOUND`, else map value `UNKNOWN_DIRECTION`  
disposition | read_only_udm.security_result.detection_fields.value | Map `disposition` field to this field, when key field is equal to `Disposition`  
domain | read_only_udm.principal.administrative_domain | Map `domain` field to this field  
dst_ip | read_only_udm.target.ip | Map `dst_ip` field to this field  
from | read_only_udm.network.email.from | If `from` field contains `@` then map to this field  
log_id | read_only_udm.metadata.product_log_id | Map `log_id` field to this field  
message_id | read_only_udm.network.email.mail_id | Map `message_id` field to this field  
message_length | read_only_udm.additional.fields.value.number_value | Map `message_length` field to this field, when key field is equal to `message_length`  
msg | read_only_udm.security_result.description | Map `msg` field to this field  
polid | read_only_udm.security_result.detection_fields.value | Map `polid` field to this field, when key field is equal to `Polid`  
relay | read_only_udm.intermediary.ip | Map `relay` field to this field  
resolved | read_only_udm.security_result.detection_fields.value | Map `resolved` field to this field, when key field is equal to `Resolved`  
session_id | read_only_udm.network.session_id | Map `session_id` field to this field  
src_type | read_only_udm.additional.fields.value.string_value | Map `src_type` field to this field, when key field is equal to `src_type`  
stat | read_only_udm.metadata.description | Map `stat` field to this field  
subject | read_only_udm.network.email.subject | Map `subject` field to this field  
to | read_only_udm.network.email.to | If `to` field contains `@` then map to this field  
user | read_only_udm.principal.user.userid | Map `user` field to this field  
N/A | read_only_udm.extensions.auth.mechanism | The value of this field is hardcoded in the parser code as `USERNAME_PASSWORD` when `authid` field exists  
N/A | read_only_udm.extensions.auth.type | The value of this field is hardcoded in the parser code as `AUTHTYPE_UNSPECIFIED` when `authid` field exists  
N/A | read_only_udm.metadata.event_type | The value of this field is determined by the parser logic based on a combination of available fields. If `from` field exists then the value is `EMAIL_TRANSACTION`, else if `to` field exists then the value is `EMAIL_UNCATEGORIZED`, else if both `client_ip` and `dst_ip` fields exist then the value is `NETWORK_CONNECTION`, else if `authid` field exists then the value is `USER_LOGIN`, else if `user` field exists then the value is `USER_UNCATEGORIZED`, else if `client_ip` field exists then the value is `STATUS_UPDATE`, else the value is `GENERIC_EVENT`  
N/A | read_only_udm.metadata.log_type | The value of this field is hardcoded in the parser code as `FORTINET_FORTIMAIL`  
N/A | read_only_udm.metadata.product_name | The value of this field is hardcoded in the parser code as `FORTINET_FORTIMAIL`  
N/A | read_only_udm.metadata.vendor_name | The value of this field is hardcoded in the parser code as `FORTINET`  
N/A | read_only_udm.principal.resource.resource_type | The value of this field is hardcoded in the parser code as `DEVICE`  
`type" and "subtype` | `metadata.product_event_type` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortimail-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
