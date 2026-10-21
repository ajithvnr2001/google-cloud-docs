---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/intel-ema/
title: Collect Intel Endpoint Management Assistant (Intel EMA) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:10:05.298781+00:00
---

# Collect Intel Endpoint Management Assistant (Intel EMA) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/intel-ema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Intel Endpoint Management Assistant (Intel EMA) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Intel Endpoint Management Assistant (Intel EMA) logs into Google Security Operations using Bindplane.

Intel Endpoint Management Assistant (Intel EMA) is a software application that provides remote management of Intel vPro platform-based devices in the cloud, both inside and outside the firewall. Intel EMA enables IT administrators to remotely configure and manage Intel Active Management Technology (Intel AMT) endpoints, perform out-of-band and in-band operations, and monitor endpoint activity through audit event logging.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Intel EMA server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrator access to the Intel EMA server with permissions to modify the NLog configuration file
  * Intel EMA server version 1.10 or later installed and operational



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
            chronicle/intel_ema:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: 'YOUR_CUSTOMER_ID'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: INTEL_EMA
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/intel_ema_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/intel_ema
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: Set to `0.0.0.0:514` to listen on all interfaces on UDP port 514. You may use a different port such as `1514` if running as non-root on Linux.
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Replace `YOUR_CUSTOMER_ID` with your customer ID from the previous step.
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `log_type`: Set to `INTEL_EMA` exactly as shown.
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`).



### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
  * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux, do the following:

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows, do the following:

  1. Choose one of the following options:

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
              




## Configure Intel EMA syslog forwarding

Intel EMA uses the NLog logging framework. To forward logs via syslog to the Bindplane agent, you must add a syslog network target to the Intel EMA NLog configuration file.

### Install the NLog Syslog target extension

  1. Sign in to the Intel EMA server as a local administrator.
  2. Open **PowerShell** as an administrator.
  3. Navigate to the Intel EMA web application directory:
         
         cd C:\inetpub\wwwroot
         

  4. Install the **NLog.Targets.Syslog** NuGet package by copying the `NLog.Targets.Syslog.dll` file into the Intel EMA web application directory (`C:\inetpub\wwwroot`).

**Note:** You can download the `NLog.Targets.Syslog` package from the [NuGet Gallery](https://www.nuget.org/packages/NLog.Targets.Syslog). Extract the DLL from the package and place it in the same directory as the `NLog.dll` and `NLog.config` files.



### Edit the NLog configuration file

  1. Open the NLog configuration file in a text editor:
         
         notepad C:\inetpub\wwwroot\NLog.config
         

  2. Add the syslog extension inside the `<extensions>` section. If the `<extensions>` section does not exist, create it within the `<nlog>` element:
         
         <extensions>
             <add assembly="NLog.Targets.Syslog" />
         </extensions>
         

  3. Add a syslog target inside the `<targets>` section:
         
         <target name="syslog" xsi:type="Syslog">
             <sl:messageSend>
                 <protocol>UDP</protocol>
                 <udp>
                     <server>BINDPLANE_AGENT_IP</server>
                     <port>514</port>
                 </udp>
             </sl:messageSend>
         </target>
         

     * Replace `BINDPLANE_AGENT_IP` with the IP address of the host running the Bindplane agent (for example, `192.168.1.100`).
     * Replace `514` with the port configured in the Bindplane agent if you are using a non-standard port.
     * Set the **protocol** to `UDP` or `TCP` to match the Bindplane agent receiver configuration.
  4. Add a logging rule inside the `<rules>` section to route all log messages to the syslog target:
         
         <logger name="*" minlevel="Info" writeTo="syslog" />
         

**Note:** Set `minlevel` to `Info` to capture informational, warning, error, and critical events. Set to `Debug` for more verbose logging, or `Warn` for fewer messages.
  5. Save and close the file.




### Example NLog.config with syslog target

  * The following shows an example of the relevant sections added to the NLog.config file:
        
        <?xml version="1.0" encoding="utf-8"?>
        <nlog xmlns="http://www.nlog-project.org/schemas/NLog.xsd"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xmlns:sl="http://www.nlog-project.org/schemas/NLog.Targets.Syslog.xsd">
            <extensions>
                <add assembly="NLog.Targets.Syslog" />
            </extensions>
            <targets>
                <!-- Existing file targets remain here -->
                <target name="syslog" xsi:type="Syslog">
                    <sl:messageSend>
                        <protocol>UDP</protocol>
                        <udp>
                            <server>192.168.1.100</server>
                            <port>514</port>
                        </udp>
                    </sl:messageSend>
                </target>
            </targets>
            <rules>
                <!-- Existing rules remain here -->
                <logger name="*" minlevel="Info" writeTo="syslog" />
            </rules>
        </nlog>
        




### Restart IIS to apply the changes

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Restart IIS to reload the NLog configuration:
         
         iisreset
         

  3. Verify that the Intel EMA web application is running by navigating to the Intel EMA Platform Manager in a web browser.




### Verify syslog forwarding

  1. Perform an action in the Intel EMA console (for example, sign in, view endpoints, or modify a configuration) to generate audit events.
  2. Check the Bindplane agent logs to confirm that syslog messages are being received from the Intel EMA server.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
server_type | additional.fields | Merged labels with keys server_type, server_type_id, Endpoint_count  
server_type_id | additional.fields |   
Endpoint_count | additional.fields |   
Time | metadata.event_timestamp | Parsed using date filter with formats yyyy-MM-dd HH:mm:ss.SSSS, ISO8601, RFC 3339  
metadata.event_type | metadata.event_type | Set to "GENERIC_EVENT"  
version_id | metadata.product_version | Value copied directly  
EndpointId | security_result.detection_fields | Merged label with key EndpointId  
severity | security_result.severity | Mapped to CRITICAL if CRITICAL, ERROR if ERROR, HIGH if ALERT or EMERGENCY, INFORMATIONAL if INFO or NOTICE, LOW if DEBUG, MEDIUM if WARNING, else UNKNOWN_SEVERITY  
Culture | target.resource.attribute.labels | Merged labels with keys culture, public_key_token, process_name  
Publickeytoken | target.resource.attribute.labels |   
process_name | target.resource.attribute.labels |   
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/intel-ema-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
