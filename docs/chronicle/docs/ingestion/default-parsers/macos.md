---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/macos/
title: Collect macOS System Logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:53:38.990272+00:00
---

# Collect macOS System Logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/macos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect macOS System Logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can ingest macOS system logs to Google Security Operations using Bindplane. macOS uses the Apple Unified Logging system to capture system-level events including authentication, process execution, kernel activity, and application behavior. These logs can be forwarded via syslog to a remote collector for centralized security monitoring and analysis.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Administrative access to the macOS endpoints that will forward logs.
  * macOS 10.12 (Sierra) or later with Unified Logging support.



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Collection Agent**.
  3. Download the **Ingestion Authentication File**. 
     * Save the file securely on the system where Bindplane will be installed.



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

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: <PLACEHOLDER_CUSTOMER_ID>
             endpoint: malachiteingestion-pa.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'MACOS'
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
  * Replace `<PLACEHOLDER_CUSTOMER_ID>` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the authentication file was saved in the **Get Google SecOps ingestion authentication file** section.



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
         




## Configure macOS syslog forwarding

macOS uses the Unified Logging system. To forward logs to the Bindplane agent via syslog, configure the built-in `syslogd` service on each macOS endpoint.

### Option 1: Configure syslog forwarding using syslog.conf

  1. Open **Terminal** on the macOS endpoint.
  2. Edit the syslog configuration file:
         
         sudo nano /etc/syslog.conf
         

  3. Add the following line at the end of the file to forward all logs via UDP to the Bindplane agent:
         
         *.*     @<BINDPLANE_IP_ADDRESS>:514
         

     * Replace `<BINDPLANE_IP_ADDRESS>` with the IP address of the Bindplane agent host (for example, `192.168.1.100`).
**Note:** Use `@` for UDP forwarding. Use `@@` for TCP forwarding.
  4. Save the file and exit.

  5. Restart the syslog daemon:
         
         sudo launchctl unload /System/Library/LaunchDaemons/com.apple.syslogd.plist
         sudo launchctl load /System/Library/LaunchDaemons/com.apple.syslogd.plist
         




### Option 2: Configure syslog forwarding using asl.conf

  1. Open **Terminal** on the macOS endpoint.
  2. Edit the ASL configuration file:
         
         sudo nano /etc/asl.conf
         

  3. Add the following line to forward logs to the remote syslog server:
         
         ? [= Sender kernel] forward <BINDPLANE_IP_ADDRESS>:514
         ? [<= Level notice] forward <BINDPLANE_IP_ADDRESS>:514
         

     * Replace `<BINDPLANE_IP_ADDRESS>` with the IP address of the Bindplane agent host.
  4. Save the file and exit.

  5. Restart the syslog daemon:
         
         sudo launchctl unload /System/Library/LaunchDaemons/com.apple.syslogd.plist
         sudo launchctl load /System/Library/LaunchDaemons/com.apple.syslogd.plist
         




### Verify log forwarding

  1. On the macOS endpoint, generate a test log message:
         
         logger -p user.notice "Test syslog message for Bindplane"
         

  2. On the Bindplane agent host, check the agent logs for incoming messages:
         
         sudo journalctl -u observiq-otel-collector -f
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`activityIdentifier_label` | `additional.fields` | Merged  
`backtrace_label` | `additional.fields` | Merged  
`bootUUID_label` | `additional.fields` | Merged  
`category_label` | `additional.fields` | Merged  
`chronicle_log_type_label` | `additional.fields` | Merged  
`formatString_label` | `additional.fields` | Merged  
`log_type_label` | `additional.fields` | Merged  
`machTimestamp_label` | `additional.fields` | Merged  
`messageType_label` | `additional.fields` | Merged  
`parentActivityIdentifier_label` | `additional.fields` | Merged  
`processImageUUID_label` | `additional.fields` | Merged  
`senderImageUUID_label` | `additional.fields` | Merged  
`senderProgramCounter_label` | `additional.fields` | Merged  
`subprocess_label` | `additional.fields` | Merged  
`subsystem_label` | `additional.fields` | Merged  
`threadID_label` | `additional.fields` | Merged  
`traceID_label` | `additional.fields` | Merged  
`intermediary_host` | `intermediary.hostname` | Directly mapped  
`attributes.message` | `metadata.description` | Directly mapped  
`description` | `metadata.description` | Directly mapped  
`eventMessage` | `metadata.description` | Directly mapped  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`attributes.process` | `metadata.product_event_type` | Directly mapped  
`eventType` | `metadata.product_event_type` | Directly mapped  
`attributes.host` | `principal.asset.hostname` | Directly mapped  
`hostname` | `principal.asset.hostname` | Directly mapped  
`source` | `principal.asset.hostname` | Directly mapped  
`senderImagePath` | `principal.file.full_path` | Directly mapped  
`attributes.host` | `principal.hostname` | Directly mapped  
`hostname` | `principal.hostname` | Directly mapped  
`source` | `principal.hostname` | Directly mapped  
`command_line` | `principal.process.command_line` | Directly mapped  
`processImagePath` | `principal.process.file.full_path` | Directly mapped  
`attributes.pid` | `principal.process.pid` | Directly mapped  
`processID` | `principal.process.pid` | Directly mapped  
`process_id` | `principal.process.pid` | Directly mapped  
`userID` | `principal.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `USER_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `MacOS`  
N/A | `metadata.vendor_name` | Constant: `Apple`  
N/A | `principal.platform` | Constant: `MAC`  
`eventMessage` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`eventType` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`senderImagePath` | `event.idm.read_only_udm.principal.file.full_path` | Mapped from changelog  
`processImagePath` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`userID` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`activityIdentifier` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`bootUUID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`category` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`formatString` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`machTimestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`messageType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`parentActivityIdentifier` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`processImageUUID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`senderImageUUID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`senderProgramCounter` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`subsystem` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`threadID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`traceID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`backtrace.frames` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`processID` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`source` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/macos-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
