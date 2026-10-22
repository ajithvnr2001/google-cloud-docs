---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortiddos/
title: Collect Fortinet FortiDDoS logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:26.227561+00:00
---

# Collect Fortinet FortiDDoS logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortiddos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Fortinet FortiDDoS logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide explains how you can ingest Fortinet FortiDDoS logs to Google Security Operations using Bindplane agent.

Fortinet FortiDDoS is a DDoS attack mitigation appliance that protects networks and applications from distributed denial of service attacks. FortiDDoS provides real-time attack detection, automated mitigation, and detailed reporting for both network and application layer attacks.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance.
  * Windows Server 2016 or later, or Linux host with systemd.
  * Network connectivity between Bindplane agent and Fortinet FortiDDoS appliance.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the FortiDDoS web interface with Read-Write permission for Log & Report settings.



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



## Install Bindplane agent

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

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

**Linux:**
    
    
    sudo nano /opt/observiq-otel-collector/config.yaml
    

**Windows:**
    
    
    notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
    

### Edit the configuration file

Replace the entire contents of `config.yaml` with the following configuration:
    
    
    receivers:
      udplog:
        listen_address: "0.0.0.0:514"
    
    exporters:
      chronicle/fortiddos:
        protocol: https
        # Region of your instance, for example us, europe, asia-southeast1
        location: <LOCATION>
        # Project number of the Google Cloud project linked to the instance
        project: '<PROJECT_NUMBER>'
        compression: gzip
        creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
        customer_id: 'your-customer-id-here'
        endpoint: chronicle.googleapis.com
        log_type: FORTINET_FORTIDDOS
        raw_log_field: body
        ingestion_labels:
          env: production
    
    service:
      pipelines:
        logs/fortiddos_to_chronicle:
          receivers:
            - udplog
          exporters:
            - chronicle/fortiddos
    

### Configuration parameters

Replace the following placeholders:

**Receiver configuration:**

  * `listen_address`: IP address and port to listen on. Use `0.0.0.0:514` to listen on all interfaces on port 514.



**Exporter configuration:**

  * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
    * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
    * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
  * `customer_id`: Customer ID from the previous step.
  * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
  * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * `endpoint`: Keep set to `chronicle.googleapis.com`.
  * `log_type`: Must be `FORTINET_FORTIDDOS`.
  * `ingestion_labels`: Optional labels in YAML format.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/fortiddos:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id-here'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: FORTINET_FORTIDDOS
            raw_log_field: body
            ingestion_labels:
              env: production
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
  * **Windows** : Click **File > Save**



## Restart Bindplane agent to apply the changes

  * Linux
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    2. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * Windows

Choose one of the following options: 

    * Using Command Prompt or PowerShell as administrator:
          
          net stop observiq-otel-collector && net start observiq-otel-collector
          

    * Using Services console:

      1. Press `Win+R`, type `services.msc`, and press **Enter**.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.

      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure FortiDDoS Event Log remote logging

FortiDDoS supports two types of remote syslog logging: Event Logs for system events and Attack Logs for DDoS attack events. Configure both to send comprehensive logs to Google SecOps.

  1. Sign in to the **FortiDDoS** web interface.
  2. Go to **Log & Report > Log Configuration > Event Log Remote**.
  3. Click **Add** to create a new remote log server configuration.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Chronicle-Event-Logs`).
     * **Address** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Minimum Log Level** : Select the minimum severity level to forward (for example, **Information** or **Notification**).
     * **Facility** : Select a syslog facility (for example, **local0**).
  5. Click **Save** to save the configuration.



## Configure FortiDDoS Attack Log remote logging

Attack log remote logging is configured per Service Protection Profile (SPP). You must configure attack log forwarding for each SPP that you want to monitor.

  1. Sign in to the **FortiDDoS** web interface.
  2. Go to **Log & Report > Log Configuration > Attack Log Remote**.
  3. Click **Add** to create a new remote log server configuration.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Chronicle-Attack-Logs`).
     * **SPP** : Select the Service Protection Profile to configure.
     * **Address** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Interval** : Select the reporting interval (for example, **1 minute** or **5 minutes**).
  5. Click **Save** to save the configuration.
  6. Repeat steps 3 through 5 for each SPP that you want to monitor.

**Note:** FortiDDoS allows up to two remote syslog servers per SPP. All SPPs can send to the same syslog server, but each SPP must be configured individually.



## Verify syslog forwarding

After configuring remote logging, verify that logs are being sent to the Bindplane agent:

  1. On the Bindplane agent host, monitor incoming syslog traffic:

**Linux:**
         
         sudo tcpdump -i any -n port 514
         

**Windows:**

Use a network monitoring tool or check the Bindplane agent logs.

  2. On the FortiDDoS appliance, generate test log messages:

**Event log test:**

     * Make a configuration change in the FortiDDoS web interface to generate an event log.

**Attack log test:**

     * Wait for the configured reporting interval (1 or 5 minutes). FortiDDoS reports at regular intervals and takes an additional 2 minutes to aggregate reporting. For example, logs reported for the 5-minute mark will show on the syslog server at the 7-minute mark.
  3. Verify logs appear in Google SecOps console within 5 to 10 minutes.

**Note:** FortiDDoS uses UDP syslog, which is a fire-and-forget protocol. The appliance is unaware if the syslog server is present or accepting logs. Ensure the Bindplane agent is running and listening before configuring FortiDDoS to send logs.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
additional | additional | Value copied directly  
| additional.fields.additional_label.key | Set to "type"  
type | additional.fields.additional_label.value.string_value | Value copied directly  
| additional.fields.src_label.key | Set to "device_id"  
devid | additional.fields.src_label.value.string_value | Value copied directly  
log_id | security_result.detection_fields.log_id_label.value | Value copied directly  
| security_result.detection_fields.log_id_label.key | Set to "log_id"  
metadata | metadata | Value copied directly  
desc_Data | metadata.description | Value copied directly  
sip,dip,user | metadata.event_type | Set to "NETWORK_CONNECTION" if sip and dip not empty, else "USER_UNCATEGORIZED" if user not empty, else "STATUS_UPDATE" if sip not empty, else "GENERIC_EVENT"  
network | network | Value copied directly  
principal | principal | Value copied directly  
sip | principal.asset.ip | Value copied directly  
sip | principal.ip | Value copied directly  
date,time,tz | principal.labels.date_label.value | Concatenated from date, time, tz with spaces  
| principal.labels.date_label.key | Set to "date"  
dir | principal.labels.direction_label.value | Value copied directly  
| principal.labels.direction_label.key | Set to "direction"  
dport | principal.port | Converted to integer  
user | principal.user.userid | Value copied directly  
security_result | security_result | Value copied directly  
direction | security_result.detection_fields.direction_label.value | Value copied directly  
| security_result.detection_fields.direction_label.key | Set to "direction"  
dropcount | security_result.detection_fields.dropcount_label.value | Value copied directly  
| security_result.detection_fields.dropcount_label.key | Set to "dropcount"  
evecode | security_result.detection_fields.evecode_label.value | Value copied directly  
| security_result.detection_fields.evecode_label.key | Set to "evecode"  
evesubcode | security_result.detection_fields.evesubcode_label.value | Value copied directly  
| security_result.detection_fields.evesubcode_label.key | Set to "evesubcode"  
facility | security_result.detection_fields.facility_label.value | Value copied directly  
| security_result.detection_fields.facility_label.key | Set to "facility"  
level | security_result.detection_fields.level_label.value | Value copied directly  
| security_result.detection_fields.level_label.key | Set to "level"  
msg_id | security_result.detection_fields.msg_id_label.value | Value copied directly  
| security_result.detection_fields.msg_id_label.key | Set to "msg_id"  
spp_name | security_result.detection_fields.spp_name_label.value | Value copied directly  
| security_result.detection_fields.spp_name_label.key | Set to "spp_name"  
spp | security_result.detection_fields.spp_label.value | Value copied directly  
| security_result.detection_fields.spp_label.key | Set to "spp"  
sppoperatingmode | security_result.detection_fields.sppoperatingmode_label.value | Value copied directly  
| security_result.detection_fields.sppoperatingmode_label.key | Set to "sppoperatingmode"  
subnet_name | security_result.detection_fields.subnet_name_label.value | Value copied directly  
| security_result.detection_fields.subnet_name_label.key | Set to "subnet_name"  
subnetid | security_result.detection_fields.subnetid_label.value | Value copied directly  
| security_result.detection_fields.subnetid_label.key | Set to "subnetid"  
subtype | security_result.detection_fields.subtype_label.value | Value copied directly  
| security_result.detection_fields.subtype_label.key | Set to "subtype"  
target | target | Value copied directly  
dip | target.asset.ip | Value copied directly  
dip | target.ip | Value copied directly  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortiddos-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
