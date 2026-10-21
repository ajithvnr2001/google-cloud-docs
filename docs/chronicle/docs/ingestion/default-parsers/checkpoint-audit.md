---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-audit/
title: Collect Check Point Audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:10.195194+00:00
---

# Collect Check Point Audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Check Point Audit logs

**Parser Version:** 20.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Check Point Audit logs to Google Security Operations using the Bindplane agent.

Check Point management servers generate audit logs for administrator activity, configuration changes, login/logout events, and policy operations. The parser extracts key-value pairs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Check Point management server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Check Point Management Console



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**
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

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
            chronicle/checkpoint_audit:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: CHECKPOINT_AUDIT
                raw_log_field: body
        
        service:
            pipelines:
                logs/checkpoint_audit_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/checkpoint_audit
        




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
             




## Configure syslog in Check Point

  1. Sign in to the **Checkpoint Management Console**.
  2. Go to **Logs and Monitoring > Log Export**.
  3. Click **Add**.
  4. Choose **Syslog** as the **export type**.
  5. Provide the following configuration details: 
     * **Name** : Enter a name for your configuration (for example, `Google SecOps Export`).
     * **Destination** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number.
     * **Log Export** : Select **Audit Logs** or **All**.
     * **Syslog Format** : Select **RFC 3164** or **RFC 5424**.
  6. Click **Save**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
act | read_only_udm.security_result.action | Value from `act` field in the raw log.  
additional_info | read_only_udm.security_result.description | Value from `additional_info` field in the raw log.  
administrator | read_only_udm.target.user.user_display_name | Value from `administrator` field in the raw log.  
comment | read_only_udm.additional.fields.value.string_value | Value from `comment` field in the raw log. The key is hardcoded as `comment`.  
deviceDirection | read_only_udm.network.direction | If `deviceDirection`=1 then OUTBOUND else INBOUND.  
ifname | read_only_udm.additional.fields.value.string_value | Value from `ifname` field in the raw log. The key is hardcoded as `ifname`.  
loguid | read_only_udm.metadata.product_log_id | Value from `loguid` field in the raw log.  
log_sys_message | read_only_udm.metadata.description | Value from `log_sys_message` field in the raw log.  
msg | read_only_udm.metadata.description | Value from `msg` field in the raw log.  
operation | read_only_udm.security_result.action_details | Value from `operation` field in the raw log.  
origin | read_only_udm.intermediary.ip | Value from `origin` field in the raw log.  
originsicname | read_only_udm.additional.fields.value.string_value | Value from `originsicname` field in the raw log. The key is hardcoded as `originsicname`.  
outcome | read_only_udm.security_result.outcomes.value | Value from `outcome` field in the raw log. The key is hardcoded as `outcome`.  
product | read_only_udm.metadata.product_name | Value from `product` field in the raw log.  
rt | read_only_udm.metadata.event_timestamp.seconds | Value from `rt` field in the raw log, converted to seconds.  
sendtotrackerasadvancedauditlog | read_only_udm.additional.fields.value.string_value | Value from `sendtotrackerasadvancedauditlog` field in the raw log. The key is hardcoded as `sendtotrackerasadvancedauditlog`.  
sequencenum | read_only_udm.additional.fields.value.string_value | Value from `sequencenum` field in the raw log. The key is hardcoded as `sequencenum`.  
session_uid | read_only_udm.additional.fields.value.string_value | Value from `session_uid` field in the raw log. The key is hardcoded as `session_uid`.  
sntdom | read_only_udm.principal.administrative_domain | Value from `sntdom` field in the raw log.  
src | read_only_udm.principal.ip | Value from `src` field in the raw log.  
subject | read_only_udm.security_result.summary | Value from `subject` field in the raw log.  
update_service | read_only_udm.additional.fields.value.string_value | Value from `update_service` field in the raw log. The key is hardcoded as `update_service`.  
version | read_only_udm.additional.fields.value.string_value | Value from `version` field in the raw log. The key is hardcoded as `version`.  
N/A | read_only_udm.metadata.event_type | If `host` field exists in the raw log, then `STATUS_UPDATE`. If `operation` field equals to `Log Out` then `USER_LOGOUT`. If `operation` field equals to `Log In` then `USER_LOGIN`. Otherwise `GENERIC_EVENT`.  
N/A | read_only_udm.metadata.vendor_name | Hardcoded value: `Check Point`.  
N/A | read_only_udm.metadata.product_version | Hardcoded value: `Check Point`.  
N/A | read_only_udm.metadata.product_event_type | Hardcoded value: `[Log] - Log`.  
N/A | read_only_udm.metadata.log_type | Hardcoded value: `CHECKPOINT_FIREWALL`.  
N/A | read_only_udm.principal.hostname | Value from `host` field in the raw log.  
N/A | read_only_udm.principal.asset.hostname | Value from `host` field in the raw log.  
N/A | read_only_udm.extensions.auth.type | If `operation` field equals to `Log Out` or `Log In` then `AUTHTYPE_UNSPECIFIED`.  
N/A | read_only_udm.extensions.auth.mechanism | If `operation` field equals to `Log Out` or `Log In` then `MECHANISM_UNSPECIFIED`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-audit-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
