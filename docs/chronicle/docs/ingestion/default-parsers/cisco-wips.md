---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wips/
title: Collect Cisco Wireless Intrusion Prevention System (WIPS) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:33.410375+00:00
---

# Collect Cisco Wireless Intrusion Prevention System (WIPS) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-wips/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Wireless Intrusion Prevention System (WIPS) logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Wireless Intrusion Prevention System (WIPS) logs to Google Security Operations using the Bindplane agent.

The parser extracts key-value pairs from the syslog messages, then maps those values to Unified Data Model (UDM) fields. It determines the appropriate event type based on the presence of principal, target, and user information, and categorizes security events based on `eventType` and other fields.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Cisco Access Point (AP) or Wireless LAN Controller (WLC)
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to Cisco Access Point (AP) or Wireless LAN Controller (WLC)



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

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
          chronicle/cisco_wips:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: CISCO_WIPS
            raw_log_field: body
        
        service:
          pipelines:
            logs/cisco_wips_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/cisco_wips
        




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
          chronicle/cisco_wips:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CISCO_WIPS
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
             




## Configure Adaptive Wireless Intrusion Prevention System (aWIPS) on Cisco Catalyst

  1. Sign in to Cisco Catalyst using SSH.
  2. Enter global config to enable aWIPS under the AP profile:
         
         configure terminal
         ap profile <profile-name>
         awips
         

  3. Configure syslog throttle interval for 60 seconds:
         
         awips-syslog throttle period 60
         




## Configure syslog using Cisco AP profiles

  1. In AP-join profile (via CLI):
         
         configure terminal
         ap profile <profile-name>
         syslog host <BINDPLANE_IP>
         syslog level informational
         syslog facility local0
         end
         

  2. Replace `<BINDPLANE_IP>` with the Bindplane agent IP address.




## Configure syslog on Cisco WLC (GUI)

  1. Sign in to the **WLC** web UI.
  2. Go to **Management > Logs > Config**.
  3. Enter the Bindplane agent IP address in the **Syslog Server IP Address** field.
  4. Click **Add**.
  5. Provide the following configuration details: 
     * **Syslog Severity** : Select **Informational**.
     * **Syslog Facility** : Select **Local Use 0**.
  6. Click **Apply**.
  7. Click **Save Configuration**.



## Configure syslog on Access Points using WLC (CLI)

  1. Global AP syslog host:
         
         config ap syslog host global <BINDPLANE_IP>
         

  2. Configure the specific AP syslog host:
         
         config ap syslog host specific <AP-name> <BINDPLANE_IP>
         

  3. Set the AP syslog severity:
         
         config ap logging syslog level informational
         

  4. Set the facility for AP messages:
         
         config logging syslog facility local0
         

  5. Replace `<BINDPLANE_IP>` with the Bindplane agent IP address.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`applicationCategoryData` | `security_result.summary` | Directly mapped.  
`applicationSpecificAlarmID` | `target.resource.attribute.labels.applicationSpecificAlarmID` | Converted to a label on the target resource.  
`attackerMacAddr` | `target.mac` | Directly mapped.  
`authEntityId` | `principal.resource.attribute.labels.authEntityId` | Converted to a label on the principal resource.  
`category` | `security_result.category_details` | Directly mapped.  
`detectingApCount` | `target.resource.attribute.labels.detectingApCount` | Converted to a label on the target resource.  
`description` | `metadata.description` | Directly mapped.  
`displayName` | `principal.user.userid` | Extracted using regular expression `host/(?P<user_id>[\\w-]+)` from `displayName` if the pattern matches.  
`eventType` | `metadata.product_event_type` | Directly mapped.  
`instanceId` | `principal.resource.attribute.labels.instanceId` | Converted to a label on the principal resource.  
`instanceUuid` | `metadata.product_log_id` | Directly mapped.  
`instanceVersion` | `principal.resource.attribute.labels.instanceVersion` | Converted to a label on the principal resource.  
`macInfo` | `target.resource.attribute.labels.macInfo` | Converted to a label on the target resource.  
`notificationDeliveryMechanism` | `target.resource.attribute.labels.notificationDeliveryMechanism`, `network.ip_protocol` | Converted to a label on the target resource. If the value contains "snmp" (case-insensitive), `network.ip_protocol` is set to "UDP".  
`previousSeverity` | `target.resource.attribute.labels.previousSeverity` | Converted to a label on the target resource. Set to "AUTHTYPE_UNSPECIFIED" if `eventType` is "USER_AUTHENTICATION_FAILURE" and `user_id` is not empty. Copied from the log's `timestamp`. Determined by parser logic based on several conditions:   
"USER_LOGIN" if `eventType` is "USER_AUTHENTICATION_FAILURE" and `user_id` is not empty.   
"NETWORK_CONNECTION" if both `is_target_present` and `is_principal_present` are true.   
"STATUS_UPDATE" if `is_principal_present` is true.   
"USER_UNCATEGORIZED" if `user_id` is not empty.   
"GENERIC_EVENT" otherwise. Hardcoded to "CISCO_WIPS". Hardcoded to "Wireless Intrusion Prevention System (WIPS)". Hardcoded to "Cisco". Set to "UDP" if `notificationDeliveryMechanism` contains "snmp" (case-insensitive). Mapped from either `reportingEntityAddress` or `source` if they are not IPs. Mapped from either `reportingEntityAddress` or `source` if they are IPs. Extracted using regular expression from `source` if it is a MAC address. Converted to a label on the principal resource. Converted to a label on the principal resource.  
`reportingEntityAddress` | `principal.ip`, `principal.hostname` | If it's an IP address, mapped to `principal.ip`. Otherwise, mapped to `principal.hostname`.  
`severity` | `security_result.severity` | Mapped based on these conditions:   
"CRITICAL" if `severity` is "0", "1", "CRITICAL", or "VERY-HIGH".   
"HIGH" if `severity` is "2", "3", "4", or "HIGH".   
"MEDIUM" if `severity` is "5" or "MEDIUM".   
"LOW" if `severity` is "6", "7", or "LOW".  
`sigAlertDescription` | `security_result.description` | Directly mapped.  
`signatureName` | `target.resource.attribute.labels.signatureName` | Converted to a label on the target resource.  
`source` | `principal.hostname`, `principal.ip`, `principal.mac` | If it's an IP address, mapped to `principal.ip`. If it's a MAC address, mapped to `principal.mac`. Otherwise, mapped to `principal.hostname`.  
`srcObjectClassId` | `principal.resource.attribute.labels.srcObjectClassId` | Converted to a label on the principal resource.  
`srcObjectId` | `principal.resource.attribute.labels.srcObjectId` | Converted to a label on the principal resource.  
`subclassName` | `security_result.rule_name` | Directly mapped. Set to "BLOCK" if `applicationSpecificAlarmID` contains "BlockList" (case-insensitive) or if `eventType` is one of "SIGNATURE_ATTACK", "MALICIOUS_ROGUE_AP_DETECTED", or "USER_AUTHENTICATION_FAILURE". Determined by parser logic based on `eventType`:   
"NETWORK_MALICIOUS" if `eventType` is "MALICIOUS_ROGUE_AP_DETECTED".   
"NETWORK_SUSPICIOUS" if `eventType` is "SIGNATURE_ATTACK".   
"AUTH_VIOLATION" if `eventType` is "USER_AUTHENTICATION_FAILURE".  
`timestamp` | `metadata.event_timestamp` | The `seconds` and `nanos` fields are directly mapped.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-wips-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
