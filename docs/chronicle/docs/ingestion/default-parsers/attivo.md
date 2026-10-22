---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/attivo/
title: Collect SentinelOne Attivo (formerly Attivo Networks) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:08.190227+00:00
---

# Collect SentinelOne Attivo (formerly Attivo Networks) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/attivo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect SentinelOne Attivo (formerly Attivo Networks) logs

**Parser Version:** 9.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest SentinelOne Attivo (formerly known as Attivo Networks) logs to Google Security Operations using Bindplane.

SentinelOne Attivo is a deception technology platform that detects in-network threats, lateral movement, and credential-based attacks. It deploys decoys and lures across the environment to detect attackers who have bypassed perimeter defenses. Attivo forwards detection events and alerts via syslog.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the SentinelOne Attivo BOTsink management console.



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

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           tcplog:
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
             customer_id: <your_customer_id>
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'ATTIVO'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/chronicle_w_labels
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace `<your_customer_id>` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: <your_customer_id>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'ATTIVO'
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
         




## Configure SentinelOne Attivo syslog forwarding

### Create a CEF syslog profile

  1. Sign in to the **Attivo BOTsink** management console.
  2. Go to **Administration > Management > Syslog**.
  3. Click **Add** to create a new syslog profile.
  4. Enter a descriptive name for the profile (for example, `SecOps-CEF`).
  5. Set **Event Forwarding** to **Enabled**.
  6. Select **CEF** as the **Message Format**.
  7. Configure the severity mapping for events: 
     * **Very High** : Select **Emergency**.
     * **High** : Select **Critical**.
     * **Medium** : Select **Alert**.
     * **Low** : Select **Warning**.
     * **Very Low** : Select **Informational**.
  8. Click **Save** to save the syslog profile.



### Add a syslog server connection

  1. In the syslog profile you created, click **Add New Connection**.
  2. Provide the following connection details: 
     * **Server Name** : Enter a descriptive name for the connection (for example, `Bindplane-Agent`).
     * **Profile Name** : Select the CEF syslog profile created in the previous section.
     * **IP Address** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (or your configured Bindplane agent port).
     * **Protocol** : Select **TCP**.
  3. Click **Test Connection** to verify that BOTsink can reach the Bindplane agent.
  4. Click **Save**.



### Verify syslog delivery

  1. After configuring syslog forwarding, trigger a test alert or wait for a detection event.
  2. On the Bindplane agent host, verify that logs are being received:
         
         sudo journalctl -u observiq-otel-collector -f
         




For more information, see the [SentinelOne Attivo documentation](https://www.sentinelone.com/resources/).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`src` | `principal.ip` | Value taken from `src` field.  
`dst` | `target.ip` | Value taken from `dst` field.  
`spt` | `principal.port` | Value taken from `spt` and converted to integer.  
`dpt` | `target.port` | Value taken from `dpt` and converted to integer.  
`shost` | `principal.hostname` | Value taken from `shost` field.  
`dhost` | `target.hostname` | Value taken from `dhost` field.  
`suser` | `principal.user.userid` | Value taken from `suser` field.  
`duser` | `target.user.userid` | Value taken from `duser` field.  
`msg` | `metadata.description` | Value taken from `msg` field.  
`cat` | `security_result.category_details` | Value taken from `cat` (CEF category) field.  
`act` | `security_result.action_details` | Value taken from `act` (action) field.  
`severity` | `security_result.severity` | Mapped from CEF severity: 1-3 -> LOW, 4-6 -> MEDIUM, 7-8 -> HIGH, 9-10 -> CRITICAL.  
`deviceEventClassId` | `metadata.product_event_type` | Value taken from `deviceEventClassId` field.  
`name` | `security_result.summary` | Value taken from CEF `name` field (event name).  
`deviceVendor` | `metadata.vendor_name` | Value taken from `deviceVendor` field. Typically set to "Attivo Networks".  
`deviceProduct` | `metadata.product_name` | Value taken from `deviceProduct` field. Typically set to "BOTsink".  
`deviceVersion` | `metadata.product_version` | Value taken from `deviceVersion` field.  
| `metadata.event_type` | Set to "GENERIC_EVENT" by default. Set to "NETWORK_CONNECTION" if source and destination IPs are present. Set to "STATUS_UPDATE" if only principal information is available.  
| `metadata.log_type` | Set to "ATTIVO".  
`VLANID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Forwarder_IP` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`VTSummaryResult` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`WebRootReputation` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Forwarder` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Target_IP_Ports` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`TargetIP_List` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Dest_UserName` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`Attacker_IP_Domain` | `event.idm.read_only_udm.principal.administrative_domain` | Mapped from changelog  
`attacker_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`detail_target_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`target_host` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`target_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`target_os` | `event.idm.read_only_udm.target.platform_version` | Mapped from changelog  
`description` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`detail_source_ip` | `event.idm.read_only_udm.observer.ip` | Mapped from changelog  
`phase` | `event.idm.read_only_udm.security_result.category_details` | Mapped from changelog  
`Attacker_HostName` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`Attacker_MAC` | `event.idm.read_only_udm.principal.mac` | Mapped from changelog  
`Attacker_UserNames` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`Source_Device_Name` | `event.idm.read_only_udm.observer.hostname` | Mapped from changelog  
`Attivo_AlertID` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`MITRE_Technique_Name` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`MITRE_Tactic_Name` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`Target_Ports` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`Target_IP_Domain` | `event.idm.read_only_udm.target.administrative_domain` | Mapped from changelog  
`Alert.subject` | `metadata.description` | Mapped from changelog  
`Alert.body` | `metadata.description` | Mapped from changelog  
`Alert.app` | `principal.application` | Mapped from changelog  
`Alert.dest_ip` | `target.ip` | Mapped from changelog  
`Alert.dest_host` | `target.hostname` | Mapped from changelog  
`Alert.src_hostname` | `principal.hostname` | Mapped from changelog  
`Alert.src_ip_domain` | `principal.domain.name` | Mapped from changelog  
`Alert.dest_ip_domain` | `target.domain.name` | Mapped from changelog  
`Alert.id` | `metadata.product_log_id` | Mapped from changelog  
`Alert.des_os` | `target.asset.platform_software.platform_version` | Mapped from changelog  
`Alert.src_ip` | `principal.ip` | Mapped from changelog  
`Alert.src_mac` | `prinicipal.mac` | Mapped from changelog  
`Alert.bootsink_ip` | `intermediary.ip` | Mapped from changelog  
`Alert.forwarder" and "Alert.service` | `additional.fields` | Mapped from changelog  
`techinque_id` | `security_result.attack_details.tactics.id` | Mapped from changelog  
`techinque_name` | `security_result.attack_details.tactics.name` | Mapped from changelog  
`Alert.severity` | `security_result.severity` | Mapped from changelog  
`Alert.src_category` | `security_result.threat_name` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/attivo-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
