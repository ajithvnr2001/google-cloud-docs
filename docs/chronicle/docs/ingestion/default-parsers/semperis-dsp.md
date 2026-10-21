---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/semperis-dsp/
title: Collect Semperis DSP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:29:43.784090+00:00
---

# Collect Semperis DSP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/semperis-dsp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Semperis DSP logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Semperis Directory Services Protector (DSP) logs to Google Security Operations using the Bindplane agent.

Semperis Directory Services Protector (DSP) is an Active Directory threat detection and response platform that monitors AD changes and attacks, providing real-time alerts and automated remediation. The parser extracts fields from DSP log entries and maps them to the Unified Data Model (UDM), capturing AD object modifications, authentication events, DNS changes, and security results.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Semperis DSP server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Semperis DSP management console with administrator permissions



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane will be installed.

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
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            tcplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/semperis_dsp:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: SEMPERIS_DSP
                raw_log_field: body
        
        service:
            pipelines:
                logs/semperis_dsp:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/semperis_dsp
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `tcplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
      * `syslog` for RFC 3164/5424 syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `<customer_id>`: Customer ID from the earlier step
    * `malachiteingestion-pa.googleapis.com`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for the complete list
    * Adjust the `creds_file_path` depending on the platform: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`



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
             




## Configure Semperis DSP syslog forwarding

  1. Sign in to the **Semperis DSP** management console.
  2. Go to **Settings > SIEM Integration**.
  3. Enable **Syslog** forwarding.
  4. Provide the following configuration details: 
     * **Host** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (must match the Bindplane receiver port).
     * **Protocol** : Select **TCP** (must match the Bindplane receiver type).
  5. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
event_type | extensions.auth.type | Set to "SSO" if ObjectModificationType == "LoginADSM"  
host | intermediary.hostname | Value copied directly  
ObjectModificationType | metadata.description | Value copied directly  
event_type | metadata.event_type | Set to RESOURCE_CREATION if ObjectModificationType == "CreateObject" and OriginatingUsers != ""; RESOURCE_WRITTEN if ObjectModificationType == "ModifyObject" and OriginatingUsers != "" and AttributeName contains "Password"; RESOURCE_WRITTEN if ObjectModificationType == "ModifyObject" and OriginatingUsers != ""; RESOURCE_DELETION if ObjectModificationType == "DeleteObject" and OriginatingUsers != ""; USER_LOGIN if ObjectModificationType == "LoginADSM" and OriginatingUsers != ""; RESOURCE_WRITTEN if ObjectModificationType == "OperationRequest" and OriginatingUsers != ""; STATUS_UPDATE if principal_present == "true"; USER_UNCATEGORIZED if principal_user_present == "true"; else GENERIC_EVENT  
| metadata.product_name | Set to "SEMPERIS_DSP"  
| metadata.vendor_name | Set to "SEMPERIS"  
StringValueFrom | network.dns.answers.data | Value copied directly after cleaning  
NameNode | network.dns.answers.name | Value copied directly  
Ttl | network.dns.answers.ttl | Value copied directly, converted to uinteger  
Type | network.dns.answers.type | Set to "1" if Type =~ "DNS_TYPE_A"; "12" if Type =~ "DNS_TYPE_PTR", converted to uinteger  
OriginatingServer | principal.asset.hostname | Value copied directly  
ip | principal.asset.ip | Value copied directly after validation and cleaning  
OriginatingServer | principal.hostname | Value copied directly  
ip | principal.ip | Value copied directly after validation and cleaning  
DistinguishedName | principal.user.group_identifiers | Value merged directly  
ForestId | principal.user.product_object_id | Value copied directly  
OriginatingUsers | principal.user.userid | Value copied directly if OperationType != "LoginADSM"  
security_action | security_result.action | Value copied directly  
RequestedAction | security_result.summary | Value copied directly if OperationResult =~ "Granted" or "Denied"  
AttributeName | target.resource.name | Value copied directly if AttributeName != "" and AttributeName != "isDeleted"  
ClassName | target.resource.resource_subtype | Value copied directly  
OriginatingUsers | target.user.userid | Value copied directly if OperationType == "LoginADSM"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/semperis-dsp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
