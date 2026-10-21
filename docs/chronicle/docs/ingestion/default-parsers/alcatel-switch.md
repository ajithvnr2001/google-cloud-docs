---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/alcatel-switch/
title: Collect Alcatel switch logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:03:43.019763+00:00
---

# Collect Alcatel switch logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/alcatel-switch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Alcatel switch logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Alcatel switch logs to Google Security Operations using Bindplane agent.

Alcatel-Lucent Enterprise OmniSwitch is a family of stackable LAN switches that provide network access, security policy enforcement, and unified wired/wireless management. The switches generate syslog messages covering authentication events, interface state changes, VLAN operations, and CLI commands.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Alcatel switch
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged credentials to the Alcatel switch (administrator access)



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
            chronicle/alcatel_switch:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: ALCATEL_SWITCH
                raw_log_field: body
        
        service:
            pipelines:
                logs/alcatel_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/alcatel_switch
        




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
             




## Configure syslog export on the Alcatel switch

  1. Connect to the switch using SSH or a console cable.
  2. Sign in with **administrator** credentials.
  3. Enter **global configuration** mode:
         
         enable
         configure terminal
         

  4. Set the Bindplane (syslog) server IP address:
         
         swlog output socket <BINDPLANE_IP>
         

     * Replace `<BINDPLANE_IP>` with the Bindplane agent IP address.
**Note:** By default, the switch uses **UDP** port `514` for syslog communication.
  5. Enable logging to the syslog server:
         
         swlog remote enable
         

  6. Configure the logging level:
         
         swlog console level info
         

  7. Enable command logging:
         
         command-log enable
         

  8. Save the changes to the startup configuration:
         
         write memory
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`1.1.1.1` | `principal.ipprincipal.asset.ip` | Extracted from the log message.  
`1.1.1.2` | `target.iptarget.asset.ip` | Extracted from the log message.  
`1.1.2.7` | `target.iptarget.asset.ip` | Extracted from the log message.  
`1035` | `target.port` | Extracted from the log message.  
`2266` | `additional.fields.value.string_value` | Extracted from the log message and mapped as `vlan`.  
`3036` | `principal.port` | Extracted from the log message.  
`59300` | `target.port` | Extracted from the log message.  
`60588` | `target.port` | Extracted from the log message.  
`997` | `principal.resource.attribute.labels.value` | Extracted from the log message and mapped as `limit`.  
`A6450-L2-K4B-01` | `principal.application` | Extracted from the log message.  
`A6450-L2-X1B-02-01` | `principal.application` | Extracted from the log message.  
`A6450-L2-X2A-01-01` | `principal.application` | Extracted from the log message.  
`A6450-L2-X4B-02-01` | `principal.application` | Extracted from the log message.  
`A6900-L3-LTX0A` | `principal.application` | Extracted from the log message.  
`Accepted keyboard-interactive/pam` | `security_result.summary` | Part of the extracted `sec_summary` field.  
`b8:53:ac:6e:c9:bc` | `principal.mac` | Extracted from the log message.  
`BRIDGE(10)` | `additional.fields.value.string_value` | Extracted from the log message and mapped as `id_protocol`.  
`CLI log,` | `security_result.summary` | Part of the extracted `sec_summary` field.  
`cmd: show configuration snapshot all,` | `security_result.detection_fields.value` | Extracted from the log message and mapped as `cmd`.  
`Connection reset by 1.1.2.7 port 60505` | `security_result.summary` | Extracted from the log message.  
`Dec 7 14:28:40` | `metadata.event_timestamp.secondsmetadata.event_timestamp.nanos` | Parsed from the `ts` field.  
`Dec 8 04:21:22` | `metadata.event_timestamp.secondsmetadata.event_timestamp.nanos` | Parsed from the `ts` field.  
`Dec 9 20:08:29` | `metadata.event_timestamp.secondsmetadata.event_timestamp.nanos` | Parsed from the `ts` field.  
`Dec 9 20:51:34` | `metadata.event_timestamp.secondsmetadata.event_timestamp.nanos` | Parsed from the `ts` field.  
`Dec 11 10:18:30` | `metadata.event_timestamp.secondsmetadata.event_timestamp.nanos` | Parsed from the `ts` field.  
`Dec 17 02:14:22` | `metadata.event_timestamp.secondsmetadata.event_timestamp.nanos` | Parsed from the `ts` field.  
`Dec 19 10:27:33` | `metadata.event_timestamp.secondsmetadata.event_timestamp.nanos` | Parsed from the `ts` field.  
`Did not receive identification string from 1.1.2.7 port 60588` | `security_result.summary` | Extracted from the log message.  
`esmSetRateLimit: Txing` | `additional.fields.value.string_value` | Extracted from the log message and mapped as `esm_set_rate_limit`.  
`Feb 15 16:29:29` | `metadata.event_timestamp.secondsmetadata.event_timestamp.nanos` | Parsed from the `ts` field.  
`Feb 16 11:08:45` | `metadata.event_timestamp.secondsmetadata.event_timestamp.nanos` | Parsed from the `ts` field.  
`Feb 16 11:08:49` | `metadata.event_timestamp.secondsmetadata.event_timestamp.nanos` | Parsed from the `ts` field.  
`flashManager FlashMgr Main info(5) flashMgrValidateImage_exec: valid` | `security_result.summary` | Extracted from the log message.  
`for ncmadmin from 1.1.1.2 port 59300 ssh2` | `security_result.summary` | Part of the extracted `sec_summary` field.  
`from port 3036 to port 1035` | `security_result.summary` | Part of the extracted `sec_summary` field.  
`IVDELCSW03` | `principal.hostnameprincipal.asset.hostname` | Extracted from the log message when `principal_ip` is not an IP address.  
`IP-HELPER(22)` | `additional.fields.value.string_value` | Extracted from the log message and mapped as `id_protocol`.  
`Jan 16 02:14:13` | `metadata.event_timestamp.secondsmetadata.event_timestamp.nanos` | Parsed from the `ts` field.  
`LLDP(42)` | `additional.fields.value.string_value` | Extracted from the log message and mapped as `id_protocol`.  
`limit=997,` | `principal.resource.attribute.labels.value` | Extracted from the log message and mapped as `limit`.  
`limitType=1` | `principal.resource.attribute.labels.value` | Extracted from the log message and mapped as `limitType`.  
`lldpProcessLocationIdTLV: Error, LLDP-MED Civic Address LCI len 39 invalid, tlvL` | `security_result.summary` | Extracted from the log message.  
`Mac Movement for MacAddr: a0:29:19:c0:55:18` | `security_result.summary` | Extracted from the log message.  
`MacAddr: a0:29:19:c0:55:18` | `principal.mac` | Extracted from the log message.  
`ncmadmin` | `principal.user.userid` | Extracted from the log message.  
`OS6360` | `principal.hostnameprincipal.asset.hostname` | Extracted from the log message when `principal_ip` is not an IP address.  
`result: SUCCESS` | `security_result.detection_fields.value` | Extracted from the log message and mapped as `result`.  
`SES CMD info(5)` | `security_result.summary` | Part of the extracted `sec_summaryfield`.  
`STACK-MANAGER` | `principal.application` | Extracted from the log message.  
`Stack Port A MAC Frames TX/RX Enabled` | `security_result.summary` | Extracted from the log message.  
`STP(11)` | `additional.fields.value.string_value` | Extracted from the log message and mapped as `id_protocol`.  
`SWCONSOLE-L2-K0A-01` | `target.hostnametarget.asset.hostname` | Extracted from the log message.  
`trafficType=2,` | `principal.resource.attribute.labels.value` | Extracted from the log message and mapped as `traffic` Type.  
`user: ncmadmin` | `security_result.summary` | Part of the extracted `sec_summary` field.  
`zslot=0,` | `principal.resource.attribute.labels.value` | Extracted from the log message and mapped as `zslot`.  
`-` | `additional.fields.key` | Hardcoded value: `id_protocol`  
`-` | `additional.fields.key` | Hardcoded value: `esm_set_rate_limit`  
`-` | `additional.fields.key` | Hardcoded value: `vlan`  
`-` | `metadata.event_type` | Set to `GENERIC_EVENT` if no other type is matched.  
`-` | `metadata.product_name` | Hardcoded value: `Alcatel Switch`  
`-` | `metadata.vendor_name` | Hardcoded value: `ALCATEL SWITCH`  
`-` | `network.application_protocol` | Set to `SSH` when `id_protocol` matches `ssh` (case-insensitive).  
`-` | `principal.resource.attribute.labels.key` | Hardcoded value: `limit`  
`-` | `principal.resource.attribute.labels.key` | Hardcoded value: `trafficType`  
`-` | `principal.resource.attribute.labels.key` | Hardcoded value: `limitType`  
`-` | `principal.resource.attribute.labels.key` | Hardcoded value: `zslot`  
`-` | `security_result.detection_fields.key` | Hardcoded value: `cmd`  
`-` | `security_result.detection_fields.key` | Hardcoded value: `result`  
`-` | `security_result.severity` | Set to `INFORMATIONAL` when `prod_severity` matches `info` (case-insensitive).  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/alcatel-switch-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
