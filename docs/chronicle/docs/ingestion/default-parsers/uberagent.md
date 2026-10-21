---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/uberagent/
title: Collect uberAgent logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:47:12.425336+00:00
---

# Collect uberAgent logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/uberagent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect uberAgent logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest uberAgent logs to Google Security Operations using the Bindplane agent.

uberAgent is an endpoint security analytics and user experience monitoring platform for Windows and macOS. It collects telemetry data including process events, logon events, network connections, and application usage on monitored endpoints.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the uberAgent endpoints
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the uberAgent management console or the endpoints where uberAgent is installed



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

## Configure Bindplane agent to ingest logs and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            filelog:
                include:
                    - 'C:\uberAgent\logs\*.log'
                    - 'C:\uberAgent\logs\*.csv'
                start_at: beginning
                poll_interval: 5s
        
        exporters:
            chronicle/uberagent:
                compression: gzip
                creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: UBERAGENT
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/uberagent_to_chronicle:
                    receivers:
                        - filelog
                    exporters:
                        - chronicle/uberagent
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `include`: Paths to uberAgent log files: 
      * **Windows (local)** : `C:\uberAgent\logs\*.log` and `C:\uberAgent\logs\*.csv`
      * **Windows (file share)** : `\\SERVER\Share\uberagent-logs\*.log`
      * Adjust the path based on your uberAgent file output configuration
    * `start_at`: Set to `beginning` to read existing logs, or `end` to read only new entries
    * `poll_interval`: How often to check for new log data (default: `5s`)
  * **Exporter configuration:**

    * `uberagent`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `UBERAGENT`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `uberagent_to_chronicle`: Descriptive name for the pipeline



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
             




## Configure uberAgent file output

uberAgent supports multiple output backends. To export data as files for collection by the Bindplane agent:

  1. Open the uberAgent configuration file (`uberAgent.conf`) on the endpoint or via Group Policy.
  2. Configure a file-based output receiver:
         
         [Receiver]
         Name = FileOutput
         Type = File
         Path = C:\uberAgent\logs\
         

**Note:** Replace `C:\uberAgent\logs\` with the desired output path. For centralized collection, use a network file share path such as`\SERVER\Share\uberagent-logs`. uberAgent outputs data in CSV format by default.
  3. Configure the metrics and sourcetypes to export:

     * **Process** : Process start/stop events, resource usage.
     * **Logon** : User logon/logoff events.
     * **Network** : Network connection events.
     * **Application** : Application usage and errors.
  4. Save the configuration and restart the uberAgent service.

  5. Verify that log files are being created in the configured output directory.

  6. Ensure the Bindplane agent has read permissions on the log directory and files.

**Note:** For detailed configuration options, see the [uberAgent documentation](https://uberagent.com/docs/).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
SessionRpLatencyMs2, SessionHRes, SessionVRes, SessionColorDepth, SessionClientPlatform, SessionClientVersion, SessionClientOsLanguage, SessionPublishedName, SessionPublishedAppsCtx, SessionAppStateCtx, SessionEncryptionCtx, SessionClientTypeCtx, SessionBrokerDnsVmw, SessionBrokerUrlVmw, SessionBrokerTunneledVmw, SessionBrokerTunnelUrlVmw, SessionBrokerRemoteIpVmw, SessionBrokerUserVmw, SessionBrokerDomainVmw, SessionClientTimezoneVmw, SessionClientIdVmw, SessionTypeVmw, SessionBrokerType, SessionFgAppId, SessionFgAppVersion, SessionFgProcessName, SessionFgProcessId, SessionFgBrowserType, SessionFgBrowserActiveTabHost, SessionFgWindowTitle, SessionClientHwIdCtx2, SessionRoundTripTimeMs, SessionFps, SessionTransportProtocols, SessionProcessCount, SessionIOMB, SessionCPUTimeMs, SessionConnectionState, SessionUser, SessionIOCount, SessionNetKBPS, SessionWorkingSetMB, SessionCPUUsagePercent, SessionIOPS, SessionClientName, SessionIOLatencyMs, PowerSupportsS3, IsBatteryPresent, PowerSupportsS1, PowerSupportsS2, PowerSupportsS5, CPUMaxMhz, BaseboardSerial, CtxMachineCatalogName, AdDomainDns, HwHypervisorVendor, OsBuild, HwBiosVersion, PowerSupportsS4, HwIsVirtualMachine, IsUpsPresent, PowerSupportsConnectedStandby, OsInstallDate, Sourcetype, uberagent_index_name, data_stream.namespace, data_stream.dataset, data_stream.type, data_stream.subset, CPUCoresLogical, AdOu, AdDomainNetBios, logstash_pipeline, AdSite, CtxFarmName, CPUSockets, OsSpName, OsName, OsType, OsUpdateBuildRevision, ComputerNameCanonical, ComputerNameDn, CtxDeliveryGroupName, tags, user_agent.original | additional.fields | Merged as key-value pairs from the listed fields  
| metadata.event_type | Set to STATUS_UPDATE if has_principal true and has_target false, NETWORK_CONNECTION if both true, GENERIC_EVENT otherwise  
SessionGUID | metadata.product_log_id | Value copied directly  
user_agent.original | network.http.parsed_user_agent | Converted to parsed user agent  
user_agent.original | network.http.user_agent | Value copied directly  
SessionTransportProtocols | network.ip_protocol | Set to UDP if matches (?i)udp, TCP if (?i)tcp  
SessionID | network.session_id | Value copied directly  
SessionClientUserDomain | principal.administrative_domain | Value copied directly  
CPUCoresPhysical, RAMSizeGB, CPUName, HwManufacturer, OsArchitecture, BIOSSerial, HwModel | principal.asset.hardware | Merged into hardware object  
SessionClientDomain, host | principal.asset.hostname | Value from SessionClientDomain if not empty, else host  
prin_ip, SessionClientIp, system_ip | principal.asset.ip | Value from prin_ip if not empty, else SessionClientIp, else system_ip  
SessionClientDomain, host | principal.hostname | Value from SessionClientDomain if not empty, else host  
prin_ip, SessionClientIp, system_ip | principal.ip | Value from prin_ip if not empty, else SessionClientIp, else system_ip  
SessionClientMac | principal.mac | Value from SessionClientMac, with - replaced by :, lowercased  
SessionClientPlatform | principal.platform | Set to WINDOWS if matches (?i)windows  
SessionClientVersion | principal.platform_version | Set to value if matches (?i)windows  
SessionUser, SessionClientUser | principal.user.user_display_name | Value from SessionUser if not empty, else SessionClientUser  
SessionBrokerRemoteIpVmw | target.ip | Value copied directly  
SessionBrokerUserVmw | target.user.user_display_name | Value copied directly  
SessionClientIdVmw | target.user.userid | Value copied directly  
| metadata.product_name | Set to "UBERAGENT"  
| metadata.vendor_name | Set to "UBERAGENT"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/uberagent-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
