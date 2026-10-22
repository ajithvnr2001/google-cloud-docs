---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyber-2-ids/
title: Collect Cyber 2.0 IDS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:38.907304+00:00
---

# Collect Cyber 2.0 IDS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyber-2-ids/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cyber 2.0 IDS logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cyber 2.0 IDS logs into Google Security Operations using the Bindplane agent.

Cyber 2.0 IDSs provide enterprise-grade network security with integrated intrusion detection and prevention capabilities. The MX appliances use the Snort intrusion detection engine to monitor network traffic for malicious activity and generate IDS alerts based on threat intelligence from Cisco Talos. IDS alerts are generated in two formats: legacy `ids-alerts` and current `security_event` types, with priority levels ranging from 1 (high) to 4 (very low) based on Snort signature classifications.

## Before you begin

Make sure that you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Cyber 2.0 IDS
  * If running behind a proxy, ensure that firewall ports are open according to the Bindplane agent requirements
  * Administrative access to the Cisco Meraki Dashboard
  * Cyber 2.0 IDS with Advanced Security Edition licensing (required for IDS/IPS features)
  * Network connectivity from the Meraki MX appliance to the Bindplane agent host (UDP port 514 or custom port)



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

## Get the Google SecOps customer ID

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
         

The service status should be **RUNNING**.




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         

The service status should be **active (running)**.




### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane agent to ingest syslog and send logs to Google SecOps

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
           chronicle/meraki_ids:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '<CREDS_FILE_PATH>'
             customer_id: '<CUSTOMER_ID>'
             endpoint: chronicle.googleapis.com
             log_type: CYBER_2_IDS
             raw_log_field: body
             ingestion_labels:
               vendor: cisco_meraki
               product: mx_security_appliance
         
         service:
           pipelines:
             logs/meraki_to_chronicle:
               receivers:
                 - udplog
               exporters:
                 - chronicle/meraki_ids
         

  2. Replace the following placeholders:

     * Receiver configuration:

       * The receiver is configured to listen on all interfaces (`0.0.0.0`) on UDP port `514` (standard syslog port)
       * If port 514 is already in use or you need to run as non-root on Linux, change the port to `1514` or another available port
     * Exporter configuration:

       * `<CREDS_FILE_PATH>`: Full path to the service account JSON key file (Option 1):

         * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
         * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
       * `<CUSTOMER_ID>`: Customer ID copied from the previous step

       * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

       * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

       * `endpoint`: Keep set to `chronicle.googleapis.com`.

       * `log_type`: Set to `CYBER_2_IDS` for Cisco Meraki IDS alerts.

       * `ingestion_labels`: Optional labels to categorize logs in Google SecOps.




#### Example configuration
    
    
    receivers:
      udplog:
        listen_address: "0.0.0.0:514"
    
    exporters:
      chronicle/meraki_ids:
        protocol: https
        # Region of your instance, for example us, europe, asia-southeast1
        location: <LOCATION>
        # Project number of the Google Cloud project linked to the instance
        project: '<PROJECT_NUMBER>'
        compression: gzip
        creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
        customer_id: 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
        endpoint: chronicle.googleapis.com
        log_type: CYBER_2_IDS
        raw_log_field: body
        ingestion_labels:
          vendor: cisco_meraki
          product: mx_security_appliance
          environment: production
    
    service:
      pipelines:
        logs/meraki_to_chronicle:
          receivers:
            - udplog
          exporters:
            - chronicle/meraki_ids
    

### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/meraki_ids:
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CYBER_2_IDS
            raw_log_field: body
            ingestion_labels:
              vendor: cisco_meraki
              product: mx_security_appliance
        


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
           

    3. Check the logs for errors:
           
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
           

    3. Check the logs for errors:
           
           type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
           




## Configure Cyber 2.0 IDS syslog forwarding

  1. Sign in to the **Cisco Meraki Dashboard** at <https://dashboard.meraki.com>.
  2. Select your organization from the organization dropdown menu at the top left.
  3. Select the network containing your MX Security Appliance from the network dropdown menu.
  4. Go to **Network-wide > Configure > General**.
  5. Scroll down to the **Reporting** section.
  6. Under **Syslog servers** , click **Add a syslog server**.
  7. Configure the syslog server with the following settings: 
     * **Server IP** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (or the custom port configured in the Bindplane agent if different).
     * **Roles** : Select the following roles to forward IDS alerts: 
       * Check **IDS alerts** (for legacy `ids-alerts` format events)
       * Check **Security events** (for current `security_event` format events including IDS alerts and AMP malware detections)
  8. Click **Save changes** at the bottom of the page.
  9. Verify that IDS/IPS is enabled on your MX Security Appliance: 
     1. Go to **Security & SD-WAN > Configure > Threat protection**.
     2. Ensure **Mode** is set to **Detection** (IDS) or **Prevention** (IPS).
     3. Select a ruleset: **Connectivity** , **Balanced** , or **Security** , based on your security requirements.
     4. Click **Save changes**.
  10. Generate test traffic to verify log forwarding:

     1. Go to **Security & SD-WAN > Monitor > Security center**.
     2. Verify that IDS alerts are being generated.
     3. Check the Bindplane agent logs to confirm that events are being received and forwarded to Google SecOps.
**Note:** IDS alerts are only available with Advanced Security Edition licensing on Cyber 2.0 IDSs. Alert delivery typically occurs within 90 seconds of event detection.**Note:** The **IDS alerts** role forwards legacy format events with the `ids-alerts` event type, while the **Security events** role forwards current format events with the `security_event` event type. Both formats contain IDS alert information and are supported by the CYBER_2_IDS parser. It is recommended to enable both roles to capture all IDS-related events.**Note:** Cisco Meraki syslog uses UDP protocol by default. TCP and TLS protocols are not supported for syslog forwarding from Meraki devices.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
time1, monthnum+day+time2, time | metadata.event_timestamp | Timestamp when the event occurred  
app_version | about.resource.attribute.labels | List of key-value pairs for resource attributes  
prod_event_type | metadata.product_event_type | Product-specific event type  
Groups | principal.group.group_display_name | Display name of the group  
app_name, app_version, hostname, principal_ip, md5_value | about | Information about the event  
inter_host | intermediary.hostname | Hostname of the intermediary  
description | metadata.description | Description of the event  
Protocol | network.ip_protocol | IP protocol used in the network connection  
Direction | network.direction | Direction of the network traffic  
Source | principal.port | Port number of the principal  
Destination | target.port | Port number of the target  
SourceIP, principal_ip | principal.ip | IP address of the principal  
SourceIP, principal_ip | principal.asset.ip | IP address of the principal's asset  
DestinationIP | target.ip | IP address of the target  
DestinationIP | target.asset.ip | IP address of the target's asset  
HostName, hostname | principal.hostname | Hostname of the principal  
HostName, hostname | principal.asset.hostname | Hostname of the principal's asset  
ApplicationName | target.application | Application name of the target  
UserName | principal.user.userid | User ID of the principal  
FullPath | target.file.full_path | Full path of the file  
Status | security_result.action | Action taken by the security system  
pid | principal.process.pid | Process ID  
src_application | principal.application | Application name of the principal  
SubSeqNumber, FlowHandle, ClientZValue, MACAddress, State, IsXCast, FlowState, DLLMode | security_result.detection_fields | Detection fields from the security result  
severity | security_result.severity | Severity of the security result  
DB, NewApps, UniqueApps, Computers, Duration | additional.fields | Additional fields  
| metadata.event_type | Type of event  
| metadata.product_name | Product name  
| metadata.vendor_name | Vendor name  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyber-2-ids-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
