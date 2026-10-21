---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortiauthenticator/
title: Collect Fortinet FortiAuthenticator logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:13:36.966699+00:00
---

# Collect Fortinet FortiAuthenticator logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortiauthenticator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fortinet FortiAuthenticator logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Fortinet FortiAuthenticator logs to Google Security Operations using the Bindplane agent.

Fortinet FortiAuthenticator is a centralized authentication management appliance that generates syslog messages for user authentication, RADIUS/LDAP events, certificate operations, and system activity. The parser extracts fields from syslog-formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Fortinet FortiAuthenticator
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Fortinet FortiAuthenticator



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
            chronicle/fortinet_fortiauthenticator:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: FORTINET_FORTIAUTHENTICATOR
                raw_log_field: body
        
        service:
            pipelines:
                logs/fortinet_fortiauthenticator_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/fortinet_fortiauthenticator
        




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
             




## Configure a syslog server in FortiAuthenticator

  1. Sign in to the **FortiAuthenticator** web UI.
  2. Select **Logging > Log config > Syslog servers**.
  3. In the **Syslog servers** list, select **Create new**.
  4. Specify the following configuration details: 
     * **Name** : Enter a unique name for the syslog server; for example, `Google SecOps`.
     * **Server name/IP** : Enter the IP address of your Bindplane agent.
     * **Port** : Enter the Bindplane agent port number; for example, `514`.
     * **Level** : Select **Information**.
     * **Facility** : Select a facility.
  5. Select **OK** to add the syslog server.



## Configure remote syslog in FortiAuthenticator

  1. After adding the syslog server, select **Logging > Log config > Log settings**.
  2. In the **Remote syslog** session, click to enable **Send logs to remote syslog servers**.
  3. Select the server name created previously and move it to the **Chosen syslog server** list.
  4. Click **OK**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`action_label` | `additional.fields` | Merged  
`category_label` | `additional.fields` | Merged  
`has_user_login` | `extensions.auth.type` | Mapped: `true` → `MACHINE`  
`has_user_logout` | `extensions.auth.type` | Mapped: `true` → `MACHINE`  
`date_time` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss Z`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`, `true` → `STATUS_UPDATE`  
`has_target_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`has_user_login` | `metadata.event_type` | Mapped: `true` → `USER_LOGIN`  
`has_user_logout` | `metadata.event_type` | Mapped: `true` → `USER_LOGOUT`  
`logid` | `metadata.product_log_id` | Directly mapped  
`devid` | `principal.asset.asset_id` | Directly mapped  
`devname` | `principal.asset.hostname` | Directly mapped  
`prin_ip` | `principal.asset.ip` | Merged  
`user_ip` | `principal.asset.ip` | Merged  
`devname` | `principal.hostname` | Directly mapped  
`prin_ip` | `principal.ip` | Merged  
`user_ip` | `principal.ip` | Merged  
`nas_ip` | `principal.nat_ip` | Merged  
`prin_user` | `principal.user.userid` | Directly mapped  
`subtype` | `security_result.about.resource.resource_subtype` | Directly mapped  
`sec_action` | `security_result.action` | Merged  
`status` | `security_result.action_details` | Directly mapped  
`logdesc` | `security_result.description` | Directly mapped  
`subcategory` | `security_result.description` | Directly mapped  
`index_label` | `security_result.detection_fields` | Merged  
`nas_label` | `security_result.detection_fields` | Merged  
`type_label` | `security_result.detection_fields` | Merged  
`userip_label` | `security_result.detection_fields` | Merged  
`typeid` | `security_result.rule_id` | Directly mapped  
`level` | `security_result.severity` | Mapped: `warning` → `HIGH`, `notice` → `MEDIUM`, `"information", "info"` → `LOW`, `error` ...  
`vd` | `target.user.user_display_name` | Directly mapped  
`user` | `target.user.userid` | Directly mapped  
`vd` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `MACHINE`  
N/A | `metadata.event_type` | Constant: `USER_LOGIN`  
N/A | `metadata.product_name` | Constant: `FortiAuthenticator`  
N/A | `metadata.vendor_name` | Constant: `Fortinet`  
N/A | `security_result.severity` | Constant: `HIGH`  
`prin_hostname` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortiauthenticator-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
