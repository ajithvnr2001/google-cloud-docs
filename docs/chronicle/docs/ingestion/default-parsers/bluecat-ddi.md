---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecat-ddi/
title: Collect BlueCat DDI logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:33.916985+00:00
---

# Collect BlueCat DDI logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bluecat-ddi/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect BlueCat DDI logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest BlueCat DDI logs to Google Security Operations using Bindplane. BlueCat DDI is an integrated DNS, DHCP, and IP Address Management (IPAM) solution that provides centralized management and automation of core network services. It helps organizations manage DNS zones, DHCP scopes, and IP address allocations across complex enterprise environments.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the BlueCat Address Manager administration console.



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

For additional installation options, consult the [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it is in the `/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/bluecat_ddi:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             customer_id: '<customer_id>'
             endpoint: chronicle.googleapis.com
             log_type: BLUECAT_DDI
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/bluecat_ddi:
               receivers:
                 - udplog
               exporters:
                 - chronicle/bluecat_ddi
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace `<customer_id>` with the actual customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the path where the service account key file (Option 1) was saved in the Get Google SecOps credentials for the Bindplane agent section.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/bluecat_ddi:
            compression: gzip
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: BLUECAT_DDI
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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
         




## Configure BlueCat DDI syslog forwarding

### Configure syslog on BlueCat Address Manager

  1. Sign in to the **BlueCat Address Manager** web interface.
  2. From the **configuration** drop-down menu, select a configuration.
  3. Select the **Servers** tab.
  4. Under **Servers** , click the name of the BDDS (BlueCat DNS/DHCP Server) that you want to configure.
  5. Click the **Syslog** tab.
  6. Under **Syslog** , click **New**.
  7. Provide the following configuration details: 
     * **Server Address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (or your configured Bindplane agent port).
     * **Transport** : Select **UDP**.
  8. Click **Add** to save the syslog redirection entry.
  9. Click **Deploy** to push the updated configuration to the BDDS appliance.



### Configure syslog on BlueCat DNS/DHCP Server (BDDS) via CLI

If you prefer to configure syslog forwarding directly on the BDDS appliance instead of through Address Manager:

  1. Connect to the BDDS appliance via SSH.
  2. Sign in with administrative credentials.
  3. Edit the syslog-ng configuration file:
         
         sudo vi /etc/syslog-ng/syslog-ng.conf
         

  4. Add the following destination and log statements:
         
         destination d_bindplane {
             udp("<BINDPLANE_IP>" port(514));
         };
         
         log {
             source(s_local);
             destination(d_bindplane);
         };
         

  5. Replace `<BINDPLANE_IP>` with the IP address of the Bindplane agent host.

  6. Save the file and restart the syslog-ng service:
         
         sudo systemctl restart syslog-ng
         

  7. Verify that logs are being forwarded by checking the Bindplane agent logs.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`auth_mechanism` | `extensions.auth.mechanism` | Merged  
`log_type` | `extensions.auth.mechanism` | Mapped: `systemd` → `auth_mechanism`  
`log_type` | `extensions.auth.type` | Mapped: `CRON` → `AUTHTYPE_UNSPECIFIED`, `audit` → `AUTHTYPE_UNSPECIFIED`  
`log_type` | `intermediary` | Mapped: `named` → `intermediary`  
`relay_ip` | `intermediary.ip` | Merged  
`description` | `metadata.description` | Renamed/mapped  
`inner_message` | `metadata.description` | Directly mapped  
`kv.cat` | `metadata.description` | Directly mapped  
`msg` | `metadata.description` | Directly mapped  
`ts` | `metadata.event_timestamp` | Parsed as `MMM d HH:mm:ss`  
`ts_date` | `metadata.event_timestamp` | Parsed as `MMM d HH:mm:ss`  
`ts_timestamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`  
`log_type` | `metadata.event_type` | Mapped values (15 total, e.g. `named` → `USER_UNCATEGORIZED`, `named` → `NETWORK_DNS`, `dhcp...  
`message` | `metadata.event_type` | Mapped: `session closed` → `USER_LOGOUT`  
`operation_type` | `metadata.event_type` | Mapped: `view` → `USER_UNCATEGORIZED`  
`csv.event_id` | `metadata.product_event_type` | Directly mapped  
`log_type` | `network.application_protocol` | Mapped: `named` → `DNS`, `dhcpd` → `DHCP`  
`client_mac` | `network.dhcp.chaddr` | Directly mapped  
`client_ip` | `network.dhcp.ciaddr` | Directly mapped  
`src_ip` | `network.dhcp.ciaddr` | Directly mapped  
`relay_ip` | `network.dhcp.giaddr` | Directly mapped  
`log_type` | `network.dhcp.opcode` | Mapped: `dhcpd` → `BOOTREQUEST`, `dhcpd` → `BOOTREPLY`  
`message_type` | `network.dhcp.opcode` | Mapped values (7 total, e.g. `DHCPDISCOVER` → `BOOTREQUEST`, `"DHCPREQUEST", "BOOTREQUEST"` ...  
`src_ip` | `network.dhcp.siaddr` | Directly mapped  
`server_host` | `network.dhcp.sname` | Renamed/mapped  
`log_type` | `network.dhcp.type` | Mapped values (7 total, e.g. `dhcpd` → `DISCOVER`, `dhcpd` → `REQUEST`, `dhcpd` → `OFFER`)  
`message_type` | `network.dhcp.type` | Mapped values (7 total, e.g. `DHCPDISCOVER` → `DISCOVER`, `"DHCPREQUEST", "BOOTREQUEST"` → `...  
`src_ip` | `network.dhcp.yiaddr` | Directly mapped  
`log_type` | `network.dns.answers` | Mapped: `named` → `response`  
`response` | `network.dns.answers` | Merged  
`log_type` | `network.dns.questions` | Mapped: `named` → `query`  
`query` | `network.dns.questions` | Merged  
`question` | `network.dns.questions` | Merged  
`ses` | `network.session_id` | Directly mapped  
`hostname` | `principal.hostname` | Directly mapped  
`server_host` | `principal.hostname` | Directly mapped  
`kv.src` | `principal.ip` | Merged  
`log_type` | `principal.ip` | Mapped: `named` → `src_ip`, `dhcpd` → `src_ip`, `syslog-ng` → `src_ip`  
`src_ip` | `principal.ip` | Merged  
`client_mac` | `principal.mac` | Merged  
`log_type` | `principal.mac` | Mapped: `dhcpd` → `client_mac`  
`message_type` | `principal.mac` | Mapped: `DHCPDISCOVER` → `client_mac`, `"DHCPREQUEST", "BOOTREQUEST"` → `client_mac`, `DHCPR...  
`src_port` | `principal.port` | Renamed/mapped  
`acct` | `principal.user.userid` | Directly mapped  
`src_user` | `principal.user.userid` | Directly mapped  
`application` | `target.application` | Directly mapped  
`terminal` | `target.application` | Directly mapped  
`file_path` | `target.file.full_path` | Directly mapped  
`server_host` | `target.hostname` | Directly mapped  
`target_host` | `target.hostname` | Directly mapped  
`log_type` | `target.ip` | Mapped: `named` → `target_ip`, `dhcpd` → `target_ip`, `syslog-ng` → `target_ip`  
`server_ip` | `target.ip` | Merged  
`target_ip` | `target.ip` | Merged  
`client_mac` | `target.mac` | Merged  
`log_type` | `target.mac` | Mapped: `dhcpd` → `client_mac`  
`message_type` | `target.mac` | Mapped: `"DHCPOFFER", "BOOTREPLY"` → `client_mac`, `DHCPACK` → `client_mac`, `DHCPNAK` → `cl...  
`tgt_port` | `target.port` | Renamed/mapped  
`cmd` | `target.process.command_line` | Directly mapped  
`exe` | `target.process.command_line` | Directly mapped  
`file_path` | `target.process.file.full_path` | Directly mapped  
`pid` | `target.process.pid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `USER_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `Bluecat DDI`  
N/A | `metadata.vendor_name` | Constant: `Bluecat Networks`  
N/A | `network.application_protocol` | Constant: `DNS`  
N/A | `network.dhcp.opcode` | Constant: `BOOTREQUEST`  
N/A | `network.dhcp.type` | Constant: `DISCOVER`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bluecat-ddi-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
