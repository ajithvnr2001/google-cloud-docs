---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortimail/
title: Collect Fortinet FortiMail logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:42.898442+00:00
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

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/fortinet_fortimail:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
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
          chronicle/fortinet_fortimail:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: FORTINET_FORTIMAIL
            raw_log_field: body
        


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

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
