---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bigswitch-bcf/
title: Collect Big Switch BigCloudFabric logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:14.371008+00:00
---

# Collect Big Switch BigCloudFabric logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bigswitch-bcf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Big Switch BigCloudFabric logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Big Switch BigCloudFabric logs to Google Security Operations using Bindplane agent.

Arista Networks Big Cloud Fabric (BCF), now known as Converged Cloud Fabric (CCF), is a software-defined networking (SDN) solution that provides automated data center fabric management through a centralized controller. The BCF/CCF controller manages leaf-spine network architectures, providing centralized configuration, monitoring, and troubleshooting capabilities for enterprise data center networks. This product was originally developed by Big Switch Networks before being acquired by Arista Networks.

**Note:** Big Switch Networks Big Cloud Fabric (BCF) is a retired product. Arista Networks now offers Converged Cloud Fabric (CCF) as the successor product. This document applies to both BCF and CCF controllers.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and BCF/CCF Controller
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the BCF/CCF Controller via GUI or CLI
  * BCF/CCF Controller version 2.5 or later (for syslog support)



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

**Note:** The `customer ID` is required for configuring the Bindplane agent exporter.



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

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * Linux:
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * Windows:
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  1. Replace the entire contents of `config.yaml` with the following configuration:
         
         receivers:
           udplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/bigswitch_bcf:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
             customer_id: 'YOUR_CUSTOMER_ID'
             endpoint: chronicle.googleapis.com
             log_type: BIGSWITCH_BCF
             raw_log_field: body
             ingestion_labels:
               env: production
               source: bcf_controller
         
         service:
           pipelines:
             logs/bcf_to_chronicle:
               receivers:
                 - udplog
               exporters:
                 - chronicle/bigswitch_bcf
         

  2. Replace the following placeholders:

     * Receiver configuration:

       * The receiver is configured to listen on UDP port 514 for syslog messages from the BCF/CCF Controller
       * To use a different port, change `514` to your desired port number (for example, `1514` for unprivileged Linux installations)
     * Exporter configuration:

       * `creds_file_path`: Full path to the service account JSON key file (Option 1):

         * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
         * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
       * `YOUR_CUSTOMER_ID`: Replace with your `Customer ID`. For details, see Get Google SecOps customer ID.

       * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

       * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

       * `endpoint`: Keep set to `chronicle.googleapis.com`.

       * `log_type`: Set to `BIGSWITCH_BCF` (do not change)

       * `ingestion_labels`: Optional labels for categorizing logs (customize as needed)




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/bigswitch_bcf:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: BIGSWITCH_BCF
            raw_log_field: body
            ingestion_labels:
              env: production
              source: bcf_controller
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
  * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux:

    1. Run the following command:
           
           sudo systemctl restart observiq-otel-collector
           

    2. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    3. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * To restart the Bindplane agent in Windows:

    1. Choose one of the following options:

       * Command Prompt or PowerShell as administrator:
             
             net stop observiq-otel-collector && net start observiq-otel-collector
             

       * Services console:

         1. Press `Win+R`, type `services.msc`, and press Enter.
         2. Locate **observIQ OpenTelemetry Collector**.
         3. Right-click and select **Restart**.
    2. Verify the service is running:
           
           sc query observiq-otel-collector
           

    3. Check logs for errors:
           
           type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
           




## Configure Big Switch BigCloudFabric syslog forwarding

Configure the BCF/CCF Controller to forward syslog messages to the Bindplane agent using either the GUI or CLI method.

### Method 1: Configure syslog using the GUI

  1. Sign in to the BCF/CCF Controller web interface using your administrator credentials.
  2. Go to **Maintenance > Logging**.
  3. Click the **Remote Logging** tab.
  4. Click **Add** to create a new remote syslog server configuration.
  5. Provide the following configuration details: 
     * **Server** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (or the port configured in the Bindplane agent config.yaml).
     * **Protocol** : Select **UDP**.
  6. Click **Save** or **Apply** to save the configuration.
  7. Verify the configuration appears in the Remote Logging list.



### Method 2: Configure syslog using the CLI

  1. Connect to the BCF/CCF Controller via SSH using your administrator credentials.
  2. Enter enable mode:
         
         controller-1> enable
         

  3. Enter configuration mode:
         
         controller-1# configure
         

  4. Configure the remote syslog server:
         
         controller-1(config)# logging remote 192.168.1.100
         

Replace `192.168.1.100` with the IP address of the Bindplane agent host.

  5. Exit configuration mode:
         
         controller-1(config)# exit
         

  6. Verify the syslog configuration:
         
         controller-1# show logging
         

The output should display the configured remote syslog server IP address.




### Verify log forwarding

  1. Generate test log events on the BCF/CCF Controller by performing configuration changes or viewing system status.
  2. Check the Bindplane agent logs to verify syslog messages are being received:

     * Linux:
           
           sudo journalctl -u observiq-otel-collector -f
           

     * Windows:
           
           type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
           

  3. Sign in to the Google SecOps console and verify logs are appearing in the **Search** interface with the ingestion label `BIGSWITCH_BCF`.

**Note:** It may take several minutes for logs to appear in Google SecOps after initial configuration.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
description | metadata.description | Value copied directly, with leading and trailing spaces removed  
target_host, time, product_event_type, description, application | metadata.event_type | Set to STATUS_HEARTBEAT if target_host and time not empty; SERVICE_STOP if product_event_type == PORT_DOWN; SERVICE_START if description matches "._Running job._ " or product_event_type == PORT_UP or application == snmpd-execstart; STATUS_SHUTDOWN if description matches "._status down._ "; SERVICE_DELETION if product_event_type == Removing Endpoint; SERVICE_CREATION if product_event_type == Adding Endpoint; SERVICE_MODIFICATION if product_event_type == Moving Endpoint or description matches "._change instances._ "; NETWORK_CONNECTION if target_host not empty; else GENERIC_EVENT  
product_event_type | metadata.product_event_type | Value copied directly  
application_protocol | network.application_protocol | Set to "UNKNOWN_APPLICATION_PROTOCOL" if application_protocol == "lldpa"  
host | principal.hostname | Value copied directly  
ip | principal.ip | Value copied directly  
process_id | principal.process.pid | Value copied directly  
USER | principal.user.userid | Value copied directly  
log_level | security_result | Object with severity set to INFORMATIONAL if INFO, MEDIUM if WARN, HIGH if ERROR; action set to ALLOW if INFO or WARN, BLOCK if ERROR  
application | target.application | Value copied directly  
target_host | target.hostname | Value copied directly  
port | target.port | Converted to integer  
COMMAND | target.process.command_line | Value copied directly  
product_specific_id | target.process.product_specific_process_id | Prefixed with "Bigswitch:"  
kv_1, kv2, kv3 | target.user.group_identifiers | Merged from kv_1 if not empty, kv2 if not empty, kv3 if not empty  
| metadata.product_name | Set to "Big Cloud Fabric"  
| metadata.vendor_name | Set to "Big Switch"  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
