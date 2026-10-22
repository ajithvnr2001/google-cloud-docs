---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-dhcp/
title: Collect Sophos DHCP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:49.117947+00:00
---

# Collect Sophos DHCP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sophos-dhcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Sophos DHCP logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Sophos DHCP logs to Google Security Operations using Bindplane.

**Note:** Sophos UTM (which includes DHCP logging) reaches **End of Life on June 30, 2026**. Sophos Firewall (SFOS) also supports DHCP syslog via **Configure** > **System services** > **Log settings**.

The parser extracts fields from Sophos DHCP syslog formatted logs using grok and/or kv. It maps these values to the Unified Data Model (UDM) and sets default metadata values for the event source and type.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * Network connectivity: If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Sophos Firewall/UTM administrator UI.



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
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: <customer_id>
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'SOPHOS_DHCP'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - udplog
               exporters:
                 - chronicle/chronicle_w_labels
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace `<customer_id>` with your actual **Customer ID**.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: <customer_id>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'SOPHOS_DHCP'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in Linux, run the following command:
         
         /opt/observiq-otel-collector/config.yaml
         

  2. To restart the Bindplane agent in Windows, you can either use the **Services** console or enter the following command:
         
         net stop BindPlaneAgent && net start BindPlaneAgent
         




## Configure Syslog forwarding on Sophos DHCP

  1. Sign in to the **Sophos Firewall/UTM** admin UI with administrator privileges.
  2. Navigate to the syslog settings: 
     * **Sophos Firewall:** **System services** > **Log settings**.
     * **Sophos UTM:** **Logging & Reporting** > **Log Settings** > **Remote Syslog Server**.
  3. Click **Add** under **Syslog servers** and provide the following details: 
     * **Name** : A descriptive name (e.g., `GoogleSecOps-BindPlane`).
     * **IP address/Domain** : The IP address of the Bindplane Agent host.
     * **Port** : The Bindplane Agent port (e.g., `514`).
     * **Facility** : **DAEMON**.
     * **Severity level** : **Information** (adjust per your internal policy).
     * **Format** : **Device standard format** (key=value) to align with **SYSLOG + KV**.
  4. Click **Save/Apply** to start forwarding DHCP-related logs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`msg` | `metadata.description` | Directly mapped  
`sub` | `metadata.description` | Directly mapped  
`log_date` | `metadata.event_timestamp` | Parsed as `yyyy:MM:dd-HH:mm:ss`  
`log_date_inner` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss`  
`event_type` | `metadata.event_type` | Directly mapped  
`msg` | `metadata.event_type` | Mapped: `call=new` → `GENERIC_EVENT`  
`process_type` | `metadata.event_type` | Mapped: `"confd","ulogd"` → `GENERIC_EVENT`, `dhcpd` → `GENERIC_EVENT`, `dhcpd` → `NETWORK_D...  
`id` | `metadata.product_event_type` | Directly mapped  
`process_type` | `metadata.product_event_type` | Directly mapped  
`msg` | `metadata.product_name` | Mapped: `call=new` → `SOPHOS_DHCP`  
`process_type` | `metadata.product_name` | Mapped: `"confd","ulogd"` → `SOPHOS_DHCP`  
`msg` | `metadata.vendor_name` | Mapped: `call=new` → `SOPHOS`  
`process_type` | `metadata.vendor_name` | Mapped: `"confd","ulogd"` → `SOPHOS`  
`process_type` | `network.application_protocol` | Mapped: `dhcpd` → `DHCP`  
`src_mac` | `network.dhcp.chaddr` | Directly mapped  
`src_ip` | `network.dhcp.ciaddr` | Directly mapped  
`src_host` | `network.dhcp.client_hostname` | Directly mapped  
`dhcp_type` | `network.dhcp.opcode` | Mapped: `DHCPREQUEST` → `BOOTREQUEST`, `DHCPACK` → `BOOTREPLY`, `DHCPOFFER` → `BOOTREPLY`, `...  
`process_type` | `network.dhcp.opcode` | Mapped: `dhcpd` → `BOOTREQUEST`, `dhcpd` → `BOOTREPLY`  
`dhcp_type` | `network.dhcp.type` | Mapped: `DHCPREQUEST` → `REQUEST`, `DHCPACK` → `ACK`, `DHCPOFFER` → `OFFER`, `DHCPNAK` → `NAK`  
`process_type` | `network.dhcp.type` | Mapped: `dhcpd` → `REQUEST`, `dhcpd` → `ACK`, `dhcpd` → `OFFER`, `dhcpd` → `NAK`  
`src_ip` | `network.dhcp.yiaddr` | Directly mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`src_host` | `observer.hostname` | Directly mapped  
`dhcp_type` | `observer.ip` | Mapped: `DHCPREQUEST` → `src_ip`  
`process_type` | `observer.ip` | Mapped: `dhcpd` → `src_ip`  
`src_ip` | `observer.ip` | Merged  
`client` | `principal.hostname` | Directly mapped  
`src_host` | `principal.hostname` | Directly mapped  
`dhcp_type` | `principal.ip` | Mapped: `DHCPREQUEST` → `src_ip`, `DHCPNAK` → `src_ip`  
`ip` | `principal.ip` | Merged  
`msg` | `principal.ip` | Mapped: `call=new` → `srcip`  
`oldattr_address` | `principal.ip` | Merged  
`process_type` | `principal.ip` | Mapped: `"confd","ulogd"` → `srcip`, `"confd","ulogd"` → `oldattr_address`, `"confd","ulogd"...  
`src_ip` | `principal.ip` | Merged  
`srcip` | `principal.ip` | Merged  
`dhcp_type` | `principal.mac` | Mapped: `DHCPREQUEST` → `src_mac`, `DHCPNAK` → `src_mac`  
`process_type` | `principal.mac` | Mapped: `"confd","ulogd"` → `srcmac`, `dhcpd` → `src_mac`  
`src_mac` | `principal.mac` | Merged  
`srcmac` | `principal.mac` | Merged  
`srcport` | `principal.port` | Directly mapped  
`pid` | `principal.process.pid` | Directly mapped  
`objname` | `principal.resource.name` | Directly mapped  
`user` | `principal.user.userid` | Directly mapped  
`msg` | `security_result` | Mapped: `call=new` → `sec_result`  
`process_type` | `security_result` | Mapped: `"confd","ulogd"` → `sec_result`, `"confd","ulogd"` → `security_result`  
`sec_result` | `security_result` | Merged  
`initf_label` | `security_result.about.labels` | Merged  
`outitf_label` | `security_result.about.labels` | Merged  
`process_type` | `security_result.about.labels` | Mapped: `"confd","ulogd"` → `initf_label`, `"confd","ulogd"` → `outitf_label`, `"confd","ulo...  
`sid_label` | `security_result.about.labels` | Merged  
`tcpflags_label` | `security_result.about.labels` | Merged  
`action` | `security_result.action_details` | Directly mapped  
`action` | `security_result.category` | Mapped: `portscan` → `category`  
`category` | `security_result.category` | Merged  
`process_type` | `security_result.category` | Mapped: `"confd","ulogd"` → `category`  
`info` | `security_result.description` | Directly mapped  
`name` | `security_result.description` | Directly mapped  
`fwrule` | `security_result.rule_id` | Directly mapped  
`process_type` | `security_result.severity` | Mapped: `"confd","ulogd"` → `INFORMATIONAL`, `"confd","ulogd"` → `MEDIUM`  
`severity` | `security_result.severity` | Mapped: `"info","debug"` → `INFORMATIONAL`, `warn` → `MEDIUM`  
`call` | `security_result.summary` | Directly mapped  
`attr_address` | `target.ip` | Merged  
`dstip` | `target.ip` | Merged  
`ip` | `target.ip` | Merged  
`process_type` | `target.ip` | Mapped: `"confd","ulogd"` → `dstip`, `"confd","ulogd"` → `attr_address`, `"confd","ulogd"` →...  
`dstmac` | `target.mac` | Merged  
`process_type` | `target.mac` | Mapped: `"confd","ulogd"` → `dstmac`  
`dstport` | `target.port` | Directly mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `SOPHOS_DHCP`  
N/A | `metadata.vendor_name` | Constant: `SOPHOS`  
N/A | `network.application_protocol` | Constant: `DHCP`  
N/A | `network.dhcp.opcode` | Constant: `BOOTREQUEST`  
N/A | `network.dhcp.type` | Constant: `REQUEST`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
