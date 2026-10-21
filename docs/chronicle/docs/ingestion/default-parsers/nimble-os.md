---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nimble-os/
title: Collect HPE Nimble Storage OS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:31:44.369793+00:00
---

# Collect HPE Nimble Storage OS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nimble-os/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect HPE Nimble Storage OS logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest HPE Nimble Storage OS logs to Google Security Operations using Bindplane.

HPE Nimble Storage OS is a storage array operating system that generates system, hardware, and replication logs. The platform monitors storage operations and provides detailed event logging for capacity management, array health, and data protection activities. HPE Nimble Storage arrays support native syslog forwarding of system events to external collectors.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and HPE Nimble Storage array
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the HPE Nimble Storage array with administrator permissions



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
        
        sudo systemctl status observiq-otel-collector
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/nimble_os:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: NIMBLE_OS
                raw_log_field: body
                ingestion_labels:
                    env: production
        
        service:
            pipelines:
                logs/nimble_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/nimble_os
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `nimble_os`: Descriptive name for the exporter
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list
    * `NIMBLE_OS`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `nimble_to_chronicle`: Descriptive name for the pipeline



### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux: 

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows:

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
         




## Configure HPE Nimble Storage OS syslog forwarding

HPE Nimble Storage arrays support forwarding system, hardware, and replication event logs to an external syslog server. You can configure syslog forwarding using the CLI or the management GUI.

### Configure syslog using the CLI

  1. Connect to the HPE Nimble Storage array via SSH with administrator credentials:
         
         ssh admin@<nimble_array_ip>
         

  2. Enable syslog and specify the Bindplane agent as the syslog server:
         
         group --edit --syslog_server <bindplane_agent_ip>
         

  3. (Optional) Specify a custom syslog port (default is `514`):
         
         group --edit --syslog_port <port_number>
         

  4. Verify the syslog configuration:
         
         group --info | grep -i syslog
         

The output should show `Syslogd enabled: Yes`, along with the configured server address and port.

**Note:** Ensure that firewall rules allow UDP traffic on the syslog port (typically `514`) from the Nimble array to the Bindplane agent host.



### Configure syslog using the management GUI

  1. Sign in to the HPE Nimble Storage management interface.
  2. Go to **Administration > Syslog**.
  3. Click **Enable Syslog Server**.
  4. In the **Server** field, enter the IP address of the Bindplane agent host.
  5. In the **Port** field, enter the port matching the Bindplane agent receiver configuration (default `514`).
  6. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
| extensions.auth.mechanism | Authentication mechanism  
| extensions.auth.type | Authentication type  
data_message | metadata.description | Event description  
type | metadata.event_type | Event type  
type | metadata.product_event_type | Product event type  
id | metadata.product_log_id | Product log ID  
version | metadata.product_version | Product version  
group | principal.group.group_display_name | Group display name  
logsource | principal.hostname | Principal hostname  
client_ip | principal.ip | Principal IP address  
array | principal.resource.name | Resource name  
| principal.resource.resource_subtype | Resource subtype  
| principal.resource.resource_type | Resource type  
status | security_result.action | Security action  
error | security_result.description | Security result description  
| security_result.summary | Security result summary  
filename,target | target.file.full_path | File full path  
object_id | target.resource.id | Resource ID  
object,target,filename,partner,volname | target.resource.name | Resource name  
| target.resource.resource_subtype | Resource subtype  
| target.resource.resource_type | Resource type  
| target.user.user_display_name | User display name  
username | target.user.userid | User ID  
| metadata.product_name | Product name  
| metadata.vendor_name | Vendor name  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nimble-os-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
