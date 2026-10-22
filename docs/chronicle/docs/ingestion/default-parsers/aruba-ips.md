---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-ips/
title: Collect Aruba IPS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:56.535776+00:00
---

# Collect Aruba IPS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aruba-ips/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Aruba IPS logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Aruba IPS logs to Google Security Operations using the Bindplane agent. The parser extracts events, notifications, rogue APs, and WIDS AP information from JSON formatted logs. It transforms the raw log data into UDM by mapping fields, handling various event types (user login/logout, network events, security events), and enriching the data with contextual information like channel, SSID, BSSID, and severity. The parser also performs timestamp normalization and error handling for malformed JSON.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Aruba device management console or CLI



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

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
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
             customer_id: YOUR_CUSTOMER_ID_HERE
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'ARUBA_IPS'
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
     * Replace `YOUR_CUSTOMER_ID_HERE` with the actual Customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.
     * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
     * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: YOUR_CUSTOMER_ID_HERE
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'ARUBA_IPS'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Syslog forwarding on Aruba devices

Choose the configuration method based on your Aruba device type:

### Option A: Aruba Controllers (AOS-8)

#### Using WebUI (Recommended for CEF format)

  1. Sign in to the **Aruba Controller** web interface.
  2. In the **Managed Network** node hierarchy, go to **Configuration > System > Logging > Syslog Servers**.
  3. To add a logging server, click **+** in the **Syslog Servers** section.
  4. Provide the following configuration details: 
     * **Server IP Address** : Enter the Bindplane agent IP address.
     * **Port** : Enter `514` (or the port configured in Bindplane).
     * **Protocol** : Select **UDP** or **TCP** , depending on your Bindplane agent configuration.
  5. Click **Apply**.
  6. To select the types of messages you want to log, select **Logging Levels**.
  7. Select the category or subcategory to be logged.
  8. To select the severity level for the category or subcategory, select the level from the **Logging Level** drop-down list.
  9. Select the logging format **CEF** or **BSD-standard** from the **Format** drop-down list. 
     * The ArcSight **CEF** (Common Event Format) is recommended for structured logging.
  10. Click **Submit**.
  11. Click **Pending Changes**.
  12. In the **Pending Changes** window, select the check-box and click **Deploy changes**.



### Option B: Aruba Instant AP

#### Using WebUI

  1. Sign in to the **Aruba Instant** web interface.
  2. In the Instant main window, click the **System** link.
  3. Click **Show advanced options** to display the advanced options.
  4. Click the **Monitoring** tab. 
     * The Monitoring tab details are displayed.
  5. In the **Syslog server** text box which is in the **Servers** section, enter the IP address of the Bindplane agent.
  6. In the **Syslog Facility Levels** section, select the required values to configure syslog facility levels. 
     * **Syslog Level** : Detailed log about syslog levels.
     * **AP-Debug** : Detailed log about the Instant AP device.
     * **Network** : Log about change of network, for example, when a new Instant AP is added to a network.
     * **Security** : Log about network security, for example, when a client connects using wrong password.
     * **System** : Log about configuration and system status.
     * **User** : Important logs about client.
     * **User-Debug** : Detailed log about client.
     * **Wireless** : Log about radio.
  7. Click **OK** to save the configuration.



#### Using CLI

  1. Sign in to the **Aruba Instant AP CLI**.
  2. Enter configuration mode:
         
         configure terminal
         

  3. Configure syslog server and level:
         
         syslog-server <BINDPLANE_IP_ADDRESS>
         syslog-level warnings
         

     * Replace `<BINDPLANE_IP_ADDRESS>` with the IP address of your Bindplane agent host.
     * Adjust severity level as needed.



### Option C: Aruba AOS-S (Switches)

  1. Sign in to the **Aruba AOS-S switch CLI**.
  2. Enter configuration mode:
         
         configure
         

  3. Configure syslog server:
         
         logging <BINDPLANE_IP_ADDRESS>
         logging severity warnings
         

     * Replace `<BINDPLANE_IP_ADDRESS>` with the IP address of your Bindplane agent host.
     * Adjust severity level as needed.
  4. Save the configuration:
         
         write memory
         




### Option D: Aruba Central (On-Premises)

  1. Sign in to the **Aruba Central** web interface.
  2. Go to **System > System Administration > Notifications > Syslog Server**.
  3. Click **Add** or **Enable**.
  4. Provide the following configuration details: 
     * **Host** : Enter the Bindplane agent IP address.
     * **Port** : Enter `514` (or the port configured in Bindplane).
     * **Protocol** : Select **UDP** or **TCP** , depending on your Bindplane agent configuration.
     * **Facility** : Select **Local7** or as required.
     * **Severity** : Select the minimum log level (for example, **Warning** or **Info**).
  5. Click **Save**.



## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`notifications.created_timestamp` | `metadata.event_timestamp.seconds` | The raw log field `notifications.created_timestamp` is converted to seconds and mapped. The nanoseconds are lost in the conversion.  
`notifications.customer_id` | `metadata.product_log_id` | Direct mapping.  
`notifications.device_id` | `principal.resource.product_object_id` | Direct mapping.  
`notifications.group_name` | `principal.group.group_display_name` | Direct mapping.  
`notifications.id` | `metadata.product_log_id` | Direct mapping.  
`notifications.timestamp` | `metadata.event_timestamp.seconds` | The raw log field `notifications.timestamp` is converted to seconds and mapped.  
`rogue_aps.acknowledged` | `security_result.detection_fields.value` where `security_result.detection_fields.key` is "acknowledged" | Converted to string and mapped.  
`rogue_aps.containment_status` | `metadata.description` | Direct mapping.  
`rogue_aps.cust_id` | `metadata.product_log_id` | Direct mapping.  
`rogue_aps.encryption` | `security_result.detection_fields.value` where `security_result.detection_fields.key` is "encryption" | Direct mapping.  
`rogue_aps.first_det_device` | `principal.resource.product_object_id` | Direct mapping.  
`rogue_aps.first_det_device_name` | `principal.hostname` | Direct mapping.  
`rogue_aps.first_seen` | `principal.domain.first_seen_time.seconds` | Parsed as a date and the seconds since epoch are mapped.  
`rogue_aps.group_name` | `principal.group.group_display_name` | Direct mapping.  
`rogue_aps.id` | `principal.mac` | Lowercased and mapped.  
`rogue_aps.labels` | `security_result.detection_fields.value` where `security_result.detection_fields.key` is "labels" | Direct mapping.  
`rogue_aps.last_det_device` | `security_result.about.user.product_object_id` | Direct mapping.  
`rogue_aps.last_det_device_name` | `target.hostname` | Direct mapping.  
`rogue_aps.last_seen` | `principal.domain.last_seen_time.seconds` | Parsed as a date and the seconds since epoch are mapped. Also used as the event timestamp if present.  
`rogue_aps.mac_vendor` | `target.administrative_domain` | Direct mapping.  
`rogue_aps.name` | `target.user.userid` | Direct mapping.  
`rogue_aps.overriden` | `security_result.detection_fields.value` where `security_result.detection_fields.key` is "overriden" | Converted to string and mapped.  
`rogue_aps.signal` | `security_result.detection_fields.value` where `security_result.detection_fields.key` is "signal" | Converted to string and mapped.  
`rogue_aps.ssid` | `security_result.detection_fields.value` where `security_result.detection_fields.key` is "ssid" | Direct mapping.  
`site` | `principal.location.name` | Direct mapping.  
`wids_aps_info_list.attack_type` | `metadata.description` | Direct mapping.  
`wids_aps_info_list.detected_ap` | `principal.hostname` | Direct mapping.  
`wids_aps_info_list.description` | `security_result.description` | Direct mapping. Also used to extract several fields using grok.  
`wids_aps_info_list.event_time` | `metadata.event_timestamp.seconds` | Converted to string and used as the event timestamp if present.  
`wids_aps_info_list.event_type` | `metadata.product_event_type` | Direct mapping.  
`wids_aps_info_list.macaddr` | `principal.mac` | Lowercased and mapped.  
`wids_aps_info_list.radio_band` | `security_result.detection_fields.value` where `security_result.detection_fields.key` is "radio_band" | Direct mapping.  
`wids_aps_info_list.virtual_controller` | `target.hostname` | Direct mapping. Set to `true` if `notifications.severity` is "Emergency", "Alert", or "Critical". Set to `true` if `notifications.severity` is "Emergency", "Alert", or "Critical". Determined by the `events.event_type` or `notifications.type` fields, or set to `GENERIC_EVENT` as a default. Several mappings are derived from the logic: `STATUS_STARTUP`, `STATUS_SHUTDOWN`, `STATUS_UPDATE`, `USER_LOGIN`, `USER_LOGOUT`. Always set to "ARUBA_IPS". Always set to "ARUBA_IPS". Always set to "ARUBA". Set to "DHCP" if `events.event_type` is "Client DHCP Acknowledged" or "Client DHCP Timeout". Set to "BOOTREPLY" if `events.event_type` is "Client DHCP Acknowledged" or "Client DHCP Timeout". Extracted from `events.description` using grok if `events.event_type` is "Client DHCP Acknowledged". Set to "ACK" if `events.event_type` is "Client DHCP Acknowledged" and `events.description` contains an IP address. Otherwise, set to "WIN_EXPIRED". Set to "ACCESS POINT" if `events.event_type` starts with "Radio", "WLAN", "AP", or is "Security". Set to "DEVICE" if `events.event_type` starts with "Radio", "WLAN", "AP", or is "Security". Mapped from `events.client_mac` for most client events, or `rogue_aps.last_det_device` for rogue AP events. Set to "AUTH_VIOLATION" for specific `events.event_type` values or if `notifications.description` contains "DoS Attack" or "disconnect attack". Set for specific `events.event_type` values. Several key-value pairs are added based on extracted fields like `bssid`, `channel`, `previous_channel`, `ssid`, `previous bssid`, `acknowledged`, `overriden`, `encryption`, `signal`, `labels`, `radio_band`. Mapped from `wids_aps_info_list.description` for wids events. Determined by `notifications.severity` or `wids_aps_info_list.level`. Set to "level: %{wids_aps_info_list.level}" for wids events. Set for specific `events.event_type` values. Mapped from `rogue_aps.mac_vendor` for rogue AP events. Mapped from `rogue_aps.last_det_device_name` for rogue AP events or `wids_aps_info_list.virtual_controller` for wids events. Extracted from `events.description` using grok if `events.event_type` is "Security". Mapped from `notifications.client_mac` for notification events, `events.client_mac` for client events, `target_mac` extracted from `wids_aps_info_list.description` for wids events, or `rogue_aps.id` for rogue AP events. Set to "CLIENT" for most client events. Set to "DEVICE" for most client events. Set to "ACTIVE" if `events.event_type` is "Security". Mapped from `rogue_aps.name` for rogue AP events.  
`events.bssid` | `security_result.detection_fields.value` where `security_result.detection_fields.key` is "bssid" | Direct mapping.  
`events.client_mac` | `target.mac` | Direct mapping. Also used to populate `security_result.about.user.product_object_id` for client events and `target.ip` for "Security" events.  
`events.description` | `metadata.description` | Direct mapping for AP and Radio events. Used to extract several fields using grok for other event types.  
`events.device_mac` | `principal.mac` | Direct mapping.  
`events.device_serial` | `principal.resource.product_object_id` | Direct mapping.  
`events.events_details.2.channel` | `security_result.detection_fields.value` where `security_result.detection_fields.key` is "channel" | Direct mapping.  
`events.group_name` | `principal.group.group_display_name` | Direct mapping.  
`events.hostname` | `principal.hostname` | Direct mapping.  
`events.timestamp` | `metadata.event_timestamp.seconds` | Converted to string, milliseconds are removed, and then mapped. Also used as the event timestamp if present.  
`timestamp` | `metadata.event_timestamp` | Used as event timestamp if other timestamp fields are not present. Set to "ACTIVE" for most client events and "Security" events. Set to "AUTHTYPE_UNSPECIFIED" if `events.event_type` is "Client 802.1x Radius Reject". Extracted from `events.description` using grok if `events.event_type` is "Security".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-ips-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
