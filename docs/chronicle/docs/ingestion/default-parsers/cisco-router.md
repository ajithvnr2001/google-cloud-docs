---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-router/
title: Collect Cisco Router logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:38:03.896260+00:00
---

# Collect Cisco Router logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-router/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Router logs

**Parser Version:** 24.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Router logs to Google Security Operations using the Bindplane agent.

Cisco routers generate syslog messages for network events, ACL matches, authentication, and system operations. The parser extracts fields using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Cisco router
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Cisco router CLI



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

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/cisco_router:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: CISCO_ROUTER
            raw_log_field: body
        
        service:
          pipelines:
            logs/cisco_router_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/cisco_router
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/cisco_router:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CISCO_ROUTER
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           ```bash
           sudo systemctl status observiq-otel-collector
           ```
           

    2. Check logs for errors:
           
           ```bash
           sudo journalctl -u observiq-otel-collector -f
           ```
           




## Configure syslog on a Cisco Router

  1. Sign in to the Cisco Router.
  2. Escalate privileges:
         
         enable
         

  3. Switch to configuration mode:
         
         conf t
         

  4. Configure syslog:
         
         logging host <BINDPLANE_IP> transport <tcp/udp> port <PORT>
         logging source-interface <INTERFACE>
         

     * Replace `<BINDPLANE_IP>` with the Bindplane agent IP address.
     * Replace `<tcp/udp>` with the configured listening protocol (for example, `udp`).
     * Replace `<INTERFACE>` with the Cisco interface ID (for example, `Ethernet1/1`).
  5. Set the priority level:
         
         logging trap Informational
         logging console Informational
         logging severity Informational
         

  6. Set the syslog facility:
         
         logging facility local6
         

  7. Enable timestamps:
         
         service timestamps log datetime
         

  8. Save and exit.

  9. Save the configuration to survive restart:
         
         copy running-config startup-config
         




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`client_ip` | target.ip, target.asset.ip | The value is taken from the `client_ip` field extracted by the grok parser.  
`client_mac` | target.mac | The value is taken from the `client_mac` field extracted by the grok parser.  
`dst_ip` | target.ip, target.asset.ip | The value is taken from the `dst_ip` field extracted by the grok parser.  
`dst_port` | target.port | The value is taken from the `dst_port` field extracted by the grok parser and converted to an integer.  
`duration` | - | This field is not mapped to the UDM.  
`host_ip` | target.ip, target.asset.ip | The value is taken from the `host_ip` field extracted by the grok parser.  
`local_proxy` | intermediary.ip | The value is taken from the `local_proxy` field extracted by the grok parser.  
`message_data` | metadata.description | The value is taken from the `message_data` field extracted by the grok parser.  
`protocol` | network.ip_protocol | The value is taken from the `protocol` field extracted by the grok parser and converted to uppercase.  
`received_bytes` | network.received_bytes | The value is taken from the `received_bytes` field extracted by the grok parser and converted to an unsigned integer.  
`referral_url` | network.http.referral_url | The value is taken from the `referral_url` field extracted by the grok parser.  
`remote_proxy` | intermediary.ip | The value is taken from the `remote_proxy` field extracted by the grok parser.  
`send_bytes` | network.sent_bytes | The value is taken from the `send_bytes` field extracted by the grok parser and converted to an unsigned integer.  
`sent_bytes` | network.sent_bytes | The value is taken from the `sent_bytes` field extracted by the grok parser and converted to an unsigned integer.  
`server_host` | target.hostname, target.asset.hostname | The value is taken from the `server_host` field extracted by the grok parser.  
`server_ip` | target.ip, target.asset.ip | The value is taken from the `server_ip` field extracted by the grok parser.  
`src_ip` | principal.ip, principal.asset.ip | The value is taken from the `src_ip` field extracted by the grok parser.  
`src_port` | principal.port | The value is taken from the `src_port` field extracted by the grok parser and converted to an integer.  
`user_ip` | target.ip, target.asset.ip | The value is taken from the `user_ip` field extracted by the grok parser.  
`user_mail` | principal.user.userid, principal.user.email_addresses | The value is taken from the `user_mail` field extracted by the grok parser.  
`username` | target.user.userid | The value is taken from the `username` field extracted by the grok parser.  
- | metadata.event_timestamp | The value is taken from the `create_time` field.  
- | metadata.event_type | The value is set to `GENERIC_EVENT` by default, and changed to specific event types based on the parsed log message.  
- | metadata.log_type | The value is set to `CISCO_ROUTER`.  
- | metadata.product_event_type | The value is taken from the `message_type` field, which is generated by combining the `facility`, `priority`, and `mnemonics` fields.  
- | metadata.product_name | The value is set to `Router`.  
- | metadata.vendor_name | The value is set to `Cisco`.  
- | network.application_protocol | The value is set to `HTTP` or `HTTPS` if the `protocol` field is `http` or `https`, respectively.  
- | extensions.auth.type | The value is set to `AUTHTYPE_UNSPECIFIED` by default, and changed to specific authentication types based on the parsed log message.  
- | security_result.action | The value is set to `ALLOW` for successful logins and `BLOCK` for failed logins.  
- | security_result.category | The value is set to `NETWORK_SUSPICIOUS` for events with IP options and `AUTH_VIOLATION` for failed logins.  
- | security_result.description | The value is set to specific messages for different events.  
- | security_result.severity | The value is set to `LOW` for successful logins, `MEDIUM` for failed logins, and `INFORMATIONAL` for other events.  
- | security_result.severity_details | The value is taken from the `fail_reason` field for failed logins, and set to `Informational message` for events with IP options.  
- | security_result.summary | The value is set to specific messages for different events.  
`SN` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`P` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`C` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`target_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`target_ip` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`target_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`dst_user` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`packet_count` | `event.idm.read_only_udm.additional` | Mapped from changelog  
`status` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`src_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`user_name_` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`sc_description` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`packets` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`tar_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`tar_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`tar_ip` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`proto` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`src_ip_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`src_ip_msg` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`src_ip_msg_data` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`intermediary_host` | `intermediary.hostname` | Mapped from changelog  
`srcip` | `principal.ip` | Mapped from changelog  
`inter_hostname` | `intermediary.ip` | Mapped from changelog  
`MessageSourceAddress` | `principal.ip` | Mapped from changelog  
`SourceModuleName" and "SourceModuleType` | `principal.resource.attribute.labels` | Mapped from changelog  
`resourcename` | `principal.resource.name` | Mapped from changelog  
`app_protocol` | `network.application.protocol` | Mapped from changelog  
`app` | `target.application` | Mapped from changelog  
`source_port` | `principal.port` | Mapped from changelog  
`source_ip` | `principal.ip` | Mapped from changelog  
`device_ip` | `target.ip` | Mapped from changelog  
`intermediary_ip` | `intermediary.ip` | Mapped from changelog  
`sec_action` | `security_result.action` | Mapped from changelog  
`sec_summary` | `security_result.summary` | Mapped from changelog  
`facility` | `principal.resource.type` | Mapped from changelog  
`sc_summary` | `metadata.description` | Mapped from changelog  
`sr_action` | `security_result.action` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-router-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
