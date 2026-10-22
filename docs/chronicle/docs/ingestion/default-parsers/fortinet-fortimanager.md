---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortimanager/
title: Collect Fortinet FortiManager logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:27.497534+00:00
---

# Collect Fortinet FortiManager logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortimanager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fortinet FortiManager logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Fortinet FortiManager logs to Google Security Operations using Bindplane.

Fortinet FortiManager is a centralized network management platform that provides unified management, best practices compliance, and workflow automation for Fortinet security and networking devices. FortiManager enables administrators to centrally manage configurations, policies, firmware updates, and security services across thousands of FortiGate firewalls and other Fortinet devices in the Security Fabric.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows Server 2016 or later, or a Linux host with systemd.
  * Network connectivity between the Bindplane agent and Fortinet FortiManager.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Fortinet FortiManager management console with permissions to modify System Settings.
  * FortiManager version 5.0.7 or later.



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

**Note:** The customer ID is required for configuring the Bindplane agent exporter.

## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         

The service should show as **RUNNING**.




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         

The service should show as **active (running)**.




### Additional installation resources

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:** `bash sudo nano /opt/observiq-otel-collector/config.yaml`
  * **Windows:** `cmd notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"`



### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/fortimanager:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id-here'
            endpoint: chronicle.googleapis.com
            log_type: FORTINET_FORTIMANAGER
            raw_log_field: body
            ingestion_labels:
              env: production
              source: fortimanager
        
        service:
          pipelines:
            logs/fortimanager_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/fortimanager
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on. Use `0.0.0.0:514` to listen on all interfaces on port **514**. If port **514** requires root privileges on Linux, use `0.0.0.0:1514` and configure FortiManager to send to port **1514**.
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1). 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Your Customer ID (for example, `a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6`).
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `log_type`: Must be exactly `FORTINET_FORTIMANAGER`.
    * `ingestion_labels`: Optional labels for filtering and organization.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/fortimanager:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id-here'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: FORTINET_FORTIMANAGER
            raw_log_field: body
            ingestion_labels:
              env: production
              source: fortimanager
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`.
  * **Windows** : Click **File** > **Save**.



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
         




## Configure Fortinet FortiManager syslog forwarding

FortiManager syslog configuration is a two-step process: first, define the syslog server in the GUI, then enable local log forwarding via CLI.

### Step 1: Add syslog server in FortiManager GUI

  1. Sign in to the **Fortinet FortiManager** web interface.
  2. Go to **System Settings** > **Advanced** > **Syslog Server**.
  3. Click **Create New** in the toolbar.
  4. Configure the following settings: 
     * **Name** : Enter a descriptive name (for example, `Chronicle-Bindplane`).
     * **IP address (or FQDN)** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Syslog Server Port** : Enter `514` (or `1514` if using a non-privileged port).
     * **Reliable Connection** : Leave disabled for UDP (default), or enable for TCP.
     * **Secure Connection** : Leave disabled unless you have configured TLS certificates.
  5. Click **OK** to save the syslog server configuration.



### Step 2: Enable local log forwarding via CLI

  1. Connect to the FortiManager CLI via SSH or console.
  2. Run the following commands (For FortiManager 5.0.7 and later):
         
         config system locallog syslogd setting
                 set syslog-name Chronicle-Bindplane
                 set severity information
                 set status enable
         end
         




**Configuration parameters:**

  * `syslog-name`: Must match the **Name** you configured in the GUI.
  * `severity`: Set to `information` to capture all local logs. Options include: `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, `debug`.
  * `status`: Set to `enable` to start forwarding logs.


  1. Verify the configuration: `config system locallog syslogd setting show end`

  2. Verify logs are being sent:

     * **Linux:** `sudo tcpdump -i any port 514 -A`
     * **Windows:** Use Wireshark to capture traffic on port **514**.



### Notes on FortiManager syslog behavior

  * FortiManager sends its **own local event logs** (system, configuration changes, administrative actions), not logs from managed FortiGate devices.
  * By default, **Reliable Connection** is disabled (UDP port 514). If enabled, logs use TCP port 514.
  * Syslog messages use a Fortinet-specific format. The Google SecOps `FORTINET_FORTIMANAGER` parser is designed for this format.
  * Ensure system time is synchronized with **NTP** and configured to **UTC**. (Go to **Dashboard** > **System Information** widget to edit).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`type`, `subtype`, `pri`, `operation`, `performed_on`, `lograte`, `msgrate`, `logratelimit`, `logratepeak`, `action`, `cpuusage`, `memusage`, `diskusage`, `disk2usage`, `userfrom` | `about.resource.attribute.labels` | Labels associated with the resource.  
`clearpass-spt`, `allow-routing`, `color`, `comment`, `fabric-object`, `name`, `node-ip-only`, `obj-type`, `sdn-addr-type`, `sub-type`, `adom`, `pkgname`, `_signal-lte-rsrq`, `_signal-lte-rssi`, `performed_on_dev`, `changetype` | `additional.fields` | Additional fields for extended data.  
`cache_ttl_label` | `network.dns.answers` | DNS answers mapping.  
`changes` | `metadata.description` | Detailed description of the event.  
`event_type` | `metadata.event_type` | The category/type of event.  
`log_id` | `metadata.product_log_id` | Product-specific identifier.  
`session_id` | `network.session_id` | Session identifier.  
`adminprof` | `principal.administrative_domain` | Administrative domain of the principal.  
`devname` | `principal.hostname` | Hostname of the principal.  
`src_ip` | `principal.ip` | IP address of the principal.  
`device_id` | `principal.resource.product_object_id` | Resource product ID.  
`uuid` | `principal.user.userid` | User ID of the principal.  
`action_details` | `security_result.action` | The security action taken.  
`wildcard`, `subnet`, `end-ip`, `start-ip` | `security_result.detection_fields` | Fields used for security detection.  
`msg` | `security_result.summary` | Summary of the security event.  
`target_ip`, `tar_ip`, `remote_ip` | `target.ip` | Target entity IP address.  
`tar_port`, `remote_port` | `target.port` | Target entity port.  
`user` | `target.user.userid` | User ID of the target.  
N/A | `metadata.vendor_name` | Set to **Fortinet**.  
N/A | `metadata.product_name` | Set to **FortiManager**.  
`vd` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`unauthuser` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`unauthusersource` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`level` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`trandisp` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`policyid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`sentpkt` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`rcvdpkt` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`sentdelta` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`rcvddelta` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`durationdelta` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`sentpktdelta` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`rcvdpktdelta` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`crscore` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`poluuid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`policytype` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`policyname` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`craction` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`crlevel` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`subtype` | `event.idm.read_only_udm.target.resource.resource_subtype` | Mapped from changelog  
`logid` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`devid` | `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
`srcip` | `event.idm.read_only_udm.src.ip` | Mapped from changelog  
`srcip` | `event.idm.read_only_udm.src.asset.ip` | Mapped from changelog  
`src` | `event.idm.read_only_udm.src.ip` | Mapped from changelog  
`src` | `event.idm.read_only_udm.src.asset.ip` | Mapped from changelog  
`srcname` | `event.idm.read_only_udm.src.hostname` | Mapped from changelog  
`srcname` | `event.idm.read_only_udm.src.asset.hostname` | Mapped from changelog  
`srcport` | `event.idm.read_only_udm.src.port` | Mapped from changelog  
`dst` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`dst` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`dstport` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`dstintf` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`dstintfrole` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`srccountry` | `event.idm.read_only_udm.principal.location.country_or_region` | Mapped from changelog  
`dstcountry` | `event.idm.read_only_udm.target.location.country_or_region` | Mapped from changelog  
`sessionid` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`app_protocol_output` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`proto` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`view` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`CAT` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`product_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`product_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vendor_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`qtype` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`action` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`action` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`duration` | `event.idm.read_only_udm.network.session_duration.seconds` | Mapped from changelog  
`appcat` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`srchwversion` | `event.idm.read_only_udm.src.platform_version` | Mapped from changelog  
`mastersrcmac` | `event.idm.read_only_udm.principal.mac` | Mapped from changelog  
`mastersrcmac` | `event.idm.read_only_udm.principal.asset.mac` | Mapped from changelog  
`r_value` | `event.idm.read_only_udm.intermediary.resource.id` | Mapped from changelog  
`resource_name` | `event.idm.read_only_udm.intermediary.resource.name` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`ip` | `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`process_id` | `event.idm.read_only_udm.intermediary.resource.attribute.labels` | Mapped from changelog  
`process` | `event.idm.read_only_udm.intermediary.process.command_line` | Mapped from changelog  
`app` | `event.idm.read_only_udm.intermediary.application` | Mapped from changelog  
`srcserver` | `event.idm.read_only_udm.src.resource.attribute.labels` | Mapped from changelog  
`srcintfrole` | `event.idm.read_only_udm.src.resource.attribute.labels` | Mapped from changelog  
`srcswversion` | `event.idm.read_only_udm.src.resource.attribute.labels` | Mapped from changelog  
`srchwvendor` | `event.idm.read_only_udm.src.resource.attribute.labels` | Mapped from changelog  
`srcfamily` | `event.idm.read_only_udm.src.resource.attribute.labels` | Mapped from changelog  
`spt` | `event.idm.read_only_udm.src.resource.attribute.labels` | Mapped from changelog  
`srcintf` | `event.idm.read_only_udm.src.resource.attribute.labels` | Mapped from changelog  
`srcmac` | `event.idm.read_only_udm.src.mac` | Mapped from changelog  
`srcmac` | `event.idm.read_only_udm.src.asset.mac` | Mapped from changelog  
`service` | `event.idm.read_only_udm.principal.resource.name` | Mapped from changelog  
`sentbyte` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`rcvdbyte` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`devtype` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`osname` | `event.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`adom` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`pkgname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`_signal-lte-rsrq` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`_signal-lte-rssi` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`performed_on` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`changes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortimanager-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
