---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-nss-feeds/
title: Collect Zscaler NSS Feeds for Alerts logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:21:10.499191+00:00
---

# Collect Zscaler NSS Feeds for Alerts logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-nss-feeds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Zscaler NSS Feeds for Alerts logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Zscaler NSS Feeds for Alerts logs to Google Security Operations using the Bindplane agent.

Zscaler Nanolog Streaming Service (NSS) delivers cloud security alert logs for web, firewall, and DLP events. NSS streams logs from the Zscaler cloud to a designated destination using either Cloud NSS (cloud-native) or NSS VM (on-premises virtual appliance).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Zscaler NSS output
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Zscaler Internet Access (ZIA) admin portal
  * A configured Zscaler NSS server or NSS for Cloud with permissions to stream logs



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
            tcplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/zscaler_nss:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: ZSCALER_NSS_FEEDS
                raw_log_field: body
        
        service:
            pipelines:
                logs/zscaler_nss_to_chronicle:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/zscaler_nss
        




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
             




## Configure Zscaler NSS syslog forwarding

Zscaler NSS streams logs from the Zscaler cloud to a designated destination. Choose the option that matches your environment.

### Option 1: Configure Cloud NSS Feeds (recommended)

**Note:** Cloud NSS is disabled by default in ZIA. If you do not see the **Cloud NSS Feeds** option in your ZIA environment, create a support request with Zscaler support to enable it.

  1. Sign in to the **Zscaler Internet Access (ZIA)** admin portal.
  2. Go to **Administration > Nanolog Streaming Service > Cloud NSS Feeds**.
  3. Click **Add Cloud NSS Feed**.
  4. Configure the following parameters: 
     * **Feed Name** : Enter a descriptive name (for example, `NSS-Alerts-to-Chronicle`).
     * **NSS Type** : Select the log type: **NSS for Alerts**.
     * **SIEM Type** : Select **Other** for generic syslog-based ingestion.
     * **Status** : Select **Enabled**.
     * **API URL** : Enter the IP address and port of the Bindplane agent host (for example, `http://BINDPLANE_AGENT_IP:514`).
     * **Feed Output Type** : Select **JSON** (recommended for Chronicle ingestion).
     * **Timezone** : Select **GMT** (default).
  5. (Optional) Configure **Feed Output Filters** to include only specific log fields or to filter logs by criteria such as department, location, or action.
  6. Click **Save**.
  7. Click **Activate** to activate the pending configuration changes.

**Note:** Each Cloud NSS feed can stream one log type. Create separate feeds for each log type you want to ingest (for example, one feed for Web logs and another for Alerts).



### Option 2: Deploy and configure NSS VM (on-premises)

  1. Download the NSS VM image from the Zscaler admin portal: 
     1. Go to **Administration > Nanolog Streaming Service > NSS Servers**.
     2. Download the NSS OVA (for VMware) or VHD (for Hyper-V/Azure) image.
  2. Deploy the NSS VM in your hypervisor (VMware vSphere, Hyper-V, or Azure): 
     1. Import the downloaded image and configure the VM with the recommended resources (consult the [NSS Deployment Guides](https://help.zscaler.com/zia/documentation-knowledgebase/analytics/nss/nss-deployment-guides) for your platform).
     2. Configure network settings so the NSS VM can make outbound TLS connections to the Zscaler cloud.
  3. Register the NSS VM in the ZIA admin portal: 
     1. Go to **Administration > Nanolog Streaming Service > NSS Servers**.
     2. Verify that the NSS VM appears and its **State** column shows **Healthy**.
  4. Configure NSS feeds: 
     1. Go to **Administration > Nanolog Streaming Service > NSS Feeds**.
     2. Click **Add NSS Feed**.
     3. Configure the following parameters: 
        * **Feed Name** : Enter a descriptive name (for example, `NSS-Alerts-Feed`).
        * **NSS Server** : Select the deployed NSS VM.
        * **NSS Type** : Select the log type: **NSS for Alerts**.
        * **SIEM IP Address** : Enter the IP address of the Bindplane agent host.
        * **SIEM TCP Port** : Enter `514` (or the port configured in the Bindplane agent).
        * **Feed Output Type** : Select **JSON** (recommended).
     4. (Optional) Configure **Feed Filters** to limit which log entries are streamed.
     5. Click **Save**.
  5. Click **Activate** to activate the pending configuration changes.

**Note:** Each NSS VM supports up to 8 data feeds. The NSS VM connects to the Zscaler Nanolog cluster over an outbound TLS connection, decodes the compressed logs, and forwards them to the Bindplane agent over TCP.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
additional | additional | Additional information for the event  
meta.slt.node, meta.slt.pipeline, meta.customer, meta.source.type | additional.fields | Additional metadata fields not covered by other UDM fields  
| metadata.event_type | Type of event  
network | network | Network information for the event  
principal | principal | Principal entity involved in the event  
meta.source.host | principal.asset.hostname | Hostname of the asset associated with the principal  
meta.source.host | principal.hostname | Hostname of the principal  
meta.source.port | principal.port | Port number  
security_result | security_result | Security result information  
target | target | Target entity involved in the event  
meta.proxy.host | target.asset.hostname | Hostname of the asset associated with the target  
meta.proxy.host | target.hostname | Hostname of the target  
meta.proxy.port | target.port | Port number  
| metadata.product_name | Name of the product  
| metadata.vendor_name | Name of the vendor  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-nss-feeds-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
