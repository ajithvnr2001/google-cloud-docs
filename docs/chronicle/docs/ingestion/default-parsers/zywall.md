---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zywall/
title: Collect ZyXEL ZyWALL logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:48:40.590543+00:00
---

# Collect ZyXEL ZyWALL logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zywall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect ZyXEL ZyWALL logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest ZyXEL ZyWALL logs to Google Security Operations using the Bindplane agent.

ZyXEL ZyWALL is a UTM/firewall appliance that generates firewall, VPN, IDP, content filter, and system event logs. It provides unified threat management for on-premise network environments.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the ZyXEL ZyWALL appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the ZyXEL ZyWALL appliance



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
            chronicle/zywall:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: ZYWALL
                raw_log_field: body
        
        service:
            pipelines:
                logs/zywall_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/zywall
        




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
             




## Configure ZyXEL ZyWALL syslog forwarding

  1. Sign in to the **ZyWALL** web management interface by navigating to the appliance IP address in a web browser.
  2. Go to **Configuration > Log & Report > Log Settings**.
  3. In the **Remote Server** section, select an available profile (for example, **Remote Server 1**) and click **Edit**.
  4. Configure the following settings: 
     * Check **Active** to enable the remote syslog profile.
     * **Log Format** : Select **VRPT/Syslog**.
     * **Server Address** : Enter the IP address of the Bindplane agent host.
     * **Server Port** : Enter `514`.
     * **Log Facility** : Select **Local0** or your preferred facility.
  5. In the **Active Log** section, select the log categories you want to forward: 
     * **System**
     * **Firewall**
     * **VPN**
     * **IDP** (Intrusion Detection and Prevention)
     * **Content Filter**
     * **Anti-Virus**
     * **Anti-Spam**
  6. Click **OK** to save the configuration.
  7. Verify that the syslog server is receiving logs from the ZyWALL appliance.

**Note:** The ZyWALL supports up to four remote server profiles (Remote Server 1 through 4), allowing you to forward logs to multiple syslog destinations simultaneously.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
devID, class, dir | additional.fields | Additional fields not covered by the standard UDM schema  
inter_host | intermediary.hostname | Hostname of the intermediary device  
msg | metadata.description | Description of the event  
| metadata.event_type | Type of the event  
protoID | network.ip_protocol | IP protocol used in the network event  
src_ip | principal.asset.ip | IP address of the asset associated with the principal  
src_ip | principal.ip | IP address of the principal  
ob_mac | principal.mac | MAC address of the principal  
src_port | principal.port | Port number used by the principal  
cat | security_result.category_details | Category details of the security result  
rule_name | security_result.rule_name | Name of the rule that triggered the security result  
note | security_result.summary | Summary of the security result  
dst_ip | target.asset.ip | IP address of the asset associated with the target  
dst_ip | target.ip | IP address of the target  
dst_port | target.port | Port number used by the target  
| metadata.product_name | Name of the product that generated the event  
| metadata.vendor_name | Name of the vendor of the product  
`action` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`app` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cef_event_class_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cef_spec_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`proto` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cef_name` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`cef_device_version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`ob` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`cef_severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`ZYlevel` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`dvchost` | `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`dvchost` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zywall-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
