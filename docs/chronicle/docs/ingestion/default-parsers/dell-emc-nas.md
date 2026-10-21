---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-nas/
title: Collect Dell EMC Isilon NAS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:43:40.402966+00:00
---

# Collect Dell EMC Isilon NAS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dell-emc-nas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Dell EMC Isilon NAS logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Dell EMC Isilon NAS logs to Google Security Operations using the Bindplane agent.

Dell EMC Isilon (now Dell PowerScale) is a scale-out NAS platform that generates syslog messages for file access auditing, protocol events, and system operations. The parser extracts fields and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Dell EMC Isilon system
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Dell EMC Isilon (CLI)



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
            chronicle/dell_emc_nas:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: DELL_EMC_NAS
                raw_log_field: body
        
        service:
            pipelines:
                logs/dell_emc_nas_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/dell_emc_nas
        




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
             




## Configure syslog for OneFS version 7.x

  1. Sign in to the **Dell Isilon** using CLI.
  2. Enable auditing using the following commands (replace `zone_name` with actual zone name):
         
         isi audit settings modify --protocol-auditing-enabled yes --audited-zones <zone_names>
         isi zone zones modify <zone_name> --audit-success create,delete,read,rename,set_security,write
         isi zone zones modify <zone_name> --audit-failure create,delete,read,rename,set_security,write
         isi zone zones modify <zone_name> --syslog-audit-events create,delete,read,rename,set_security,write
         

  3. Enable syslog forwarding using the following command:
         
         isi zone zones modify <zone_name> --syslog-forwarding-enabled=yes
         

  4. Connect to an Isilon node using an SSH client.

  5. Open the `syslog.conf` file using `vi`, which is located in the `/etc/mcp/templates` directory:
         
         vi syslog.conf
         

  6. Locate the `!audit_protocol` line and add the following line (replace `<bindplane-ip>` with the actual Bindplane agent IP address):
         
         *.* @<bindplane-ip>
         

  7. Save the `syslog.conf` file:
         
         :wq
         




## Configure syslog for OneFS versions 8.0 and 8.1

  1. Sign in to the **Dell Isilon** using CLI.
  2. Enable auditing using the following commands (replace `zone_name` with actual zone name):
         
         isi audit settings global modify --protocol-auditing-enabled yes --audited-zones <zone_names>
         isi audit settings modify --zone <zone_name> --audit-success create,delete,read,rename,set_security,write
         isi audit settings modify --zone <zone_name> --audit-failure create,delete,read,rename,set_security,write
         isi audit settings modify --zone <zone_name> --syslog-audit-events create,delete,read,rename,set_security,write
         

  3. Enable syslog forwarding using the following command:
         
         isi audit settings modify --syslog-forwarding-enabled=yes --zone=<zone_name>
         

  4. Connect to an Isilon node using an SSH client.

  5. Open the `syslog.conf` file using `vi`, which is located in the `/etc/mcp/templates` directory:
         
         vi syslog.conf
         

  6. Locate the `!audit_protocol` line and add the following line (replace `<bindplane-ip>` with the actual Bindplane agent IP address):
         
         *.* @<bindplane-ip>
         

  7. Save the `syslog.conf` file:
         
         :wq
         




## Configure syslog for OneFS versions 8.2 to 9.4

  1. Enable auditing using the following commands (replace `<bindplane-ip>` with Bindplane agent IP address and `zone_name` with actual zone name):
         
         isi audit settings global modify --protocol-auditing-enabled yes --audited-zones <zone_name> --protocol-syslog-servers <bindplane-ip>
         isi audit settings modify --zone <zone_name> --audit-success create,delete,read,rename,set_security,write
         isi audit settings modify --zone <zone_name> --audit-failure create,delete,read,rename,set_security,write
         isi audit settings modify --zone <zone_name> --syslog-audit-events create,delete,read,rename,set_security,write
         

  2. Enable syslog forwarding using the following command:
         
         isi audit settings modify --syslog-forwarding-enabled yes --zone <zone_name>
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
COMMAND | target.process.command_line | The raw log field `COMMAND` is mapped to this UDM field.  
PWD | target.file.full_path | The raw log field `PWD` is mapped to this UDM field when `message` doesn't contain `command not allowed`.  
USER | principal.user.userid | The raw log field `USER` is mapped to this UDM field.  
action_done |  | Temporary variable used for parsing logic.  
application | target.application | The raw log field `application` is mapped to this UDM field.  
data |  | This field is not mapped to the UDM.  
description | metadata.description | The raw log field `description` is mapped to this UDM field. Additionally, `command not allowed` is mapped to this field when `message` contains `command not allowed`.  
file_name | target.file.full_path | The raw log field `file_name` is mapped to this UDM field after removing any `  
intermediary_ip | intermediary.ip | The raw log field `intermediary_ip` is mapped to this UDM field.  
kv_data |  | Temporary variable used for parsing logic.  
method |  | Temporary variable used for parsing logic.  
pid | target.process.pid | The raw log field `pid` is mapped to this UDM field when it's not empty or `-`.  
resource_type | target.resource.type | The raw log field `resource_type` is mapped to this UDM field.  
src_host | principal.hostname | The raw log field `src_host` is mapped to this UDM field.  
src_ip | principal.ip | The raw log field `src_ip` is mapped to this UDM field. It can also be extracted from the `description` field using a Grok pattern.  
status |  | Temporary variable used for parsing logic.  
ts | metadata.event_timestamp.seconds | The raw log field `ts` is parsed and its seconds value is mapped to this UDM field.  
user | principal.user.userid | The raw log field `user` is mapped to this UDM field if `USER` is empty.  
wsid | principal.user.windows_sid | The raw log field `wsid` is mapped to this UDM field after removing any characters after `  
N/A | metadata.event_type | This UDM field is derived from the parser logic based on the values of `action_done`, `method`, and `PWD`. It can be one of the following: `PROCESS_UNCATEGORIZED`, `PROCESS_OPEN`, `FILE_CREATION`, `FILE_OPEN`, `FILE_DELETION`, `FILE_MODIFICATION`, `FILE_UNCATEGORIZED`, or `STATUS_SHUTDOWN` (default).  
N/A | security_result.action | This UDM field is derived from the parser logic based on the value of `status`. It can be either `ALLOW` or `BLOCK`.  
N/A | security_result.summary | This UDM field is derived from the parser logic and populated with the value of `action_done`.  
N/A | security_result.description | This UDM field is derived from the parser logic by concatenating the values of `method` and `status` with a `-` separator.  
N/A | metadata.vendor_name | This UDM field is hardcoded to `DELL`.  
N/A | metadata.product_name | This UDM field is hardcoded to `DELL_EMC_NAS`.  
N/A | metadata.log_type | This UDM field is hardcoded to `DELL_EMC_NAS`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-emc-nas-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
