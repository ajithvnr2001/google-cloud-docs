---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vsftpd/
title: Collect vsftpd logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:54.154489+00:00
---

# Collect vsftpd logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vsftpd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect vsftpd logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest vsftpd logs to Google Security Operations using the Bindplane agent.

vsftpd (Very Secure FTP Daemon) is an FTP server that generates syslog messages for FTP connections, file transfers, authentication events, and session activity.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the vsftpd server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Root or sudo access to the vsftpd server



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
          chronicle/vsftpd:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: VSFTPD
            raw_log_field: body
        
        service:
          pipelines:
            logs/vsftpd_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/vsftpd
        




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
          chronicle/vsftpd:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: VSFTPD
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
             




## Configure syslog forwarding for vsftpd

  1. Edit the vsftpd configuration file:
         
         sudo nano /etc/vsftpd.conf
         

  2. Set the following parameters:
         
         syslog_enable=YES
         log_ftp_protocol=YES
         

  3. Configure rsyslog to forward vsftpd logs. Edit `/etc/rsyslog.conf` or create a new file `/etc/rsyslog.d/vsftpd.conf`:
         
         sudo nano /etc/rsyslog.d/vsftpd.conf
         

  4. Add the following forwarding rule (replace `<bindplane-ip>` with your Bindplane agent IP address):
         
         if $programname == 'vsftpd' then @<bindplane-ip>:514
         

  5. Restart vsftpd and rsyslog to apply the changes:
         
         sudo systemctl restart vsftpd
         sudo systemctl restart rsyslog
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`certificate` | `security_result.detection_fields.key`: "cert"  
`security_result.detection_fields.value`: value of `certificate` | The value of the `certificate` field is mapped to a `security_result.detection_fields` object with the key "cert".  
`cipher` | `network.tls.cipher` | The value of the `cipher` field is directly mapped.  
`client_ip` | `principal.ip` | The value of the `client_ip` field is directly mapped.  
`date` | `metadata.event_timestamp` | Used with `month`, `year`, and `time` to construct the `metadata.event_timestamp`. The format is derived from the `timestamp` field in the raw log, parsed, and converted to a timestamp object.  
`day` | `metadata.event_timestamp` | Used with `month`, `year`, and `time` to construct the `metadata.event_timestamp`.  
`desc` | `metadata.description` | The value of the `desc` field (extracted from the `type` field) is directly mapped. This applies to "MKDIR", "RMDIR", and "DELETE" operations.  
`description` | `network.ftp.command`  
`security_result.description`  
`target.file.full_path` | If `type` is "FTP command", the value is mapped to `network.ftp.command`. If `type` is "DEBUG" and doesn't match specific SSL patterns, it's mapped to `security_result.description`. If `type` starts with "OK" and is not "OK LOGIN", and the log describes a file operation (MKDIR, RMDIR, DELETE), it's mapped to `target.file.full_path`.  
`file_name` | `target.file.full_path` | The value of the `file_name` field is directly mapped.  
`file_size` | `network.received_bytes`  
`network.sent_bytes` | If `type` is "OK DOWNLOAD" or "FAIL DOWNLOAD", the value is converted to an unsigned integer and mapped to `network.received_bytes`. If `type` is "OK UPLOAD" or "FAIL UPLOAD", the value is converted to an unsigned integer and mapped to `network.sent_bytes`. Set to "USER_LOGIN" if `type` is "OK LOGIN". Set to "FILE_UNCATEGORIZED" if `type` is related to file operations ("OK UPLOAD", "OK DOWNLOAD", "FAIL DOWNLOAD", "OK MKDIR", "OK RMDIR", "OK DELETE", "FAIL UPLOAD"). Set to "STATUS_UPDATE" for all other `type` values. Always set to "VSFTPD". Always set to "VSFTPD". Always set to "VSFTPD".  
`month` | `metadata.event_timestamp` | Used with `day`, `year`, and `time` to construct the `metadata.event_timestamp`.  
`pid` | `principal.process.pid` | The value of the `pid` field is directly mapped.  
`response_code` | `network.http.response_code` | The value of the `response_code` field is converted to an integer and mapped.  
`reused_status` | `security_result.detection_fields.key`: "reused status"  
`security_result.detection_fields.value`: value of `reused_status` | The value of the `reused_status` field is mapped to a `security_result.detection_fields` object with the key "reused status".  
`speed` | `additional.fields.key`: "download_speed" or "upload_speed"  
`additional.fields.value.string_value`: value of `speed` | If `type` is "OK DOWNLOAD" or "FAIL DOWNLOAD", the value is mapped to `additional.fields` with the key "download_speed". If `type` is "OK UPLOAD" or "FAIL UPLOAD", the value is mapped to `additional.fields` with the key "upload_speed".  
`ssl_shutdown_state` | `security_result.detection_fields.key`: "SSL Shutdown State"  
`security_result.detection_fields.value`: value of `ssl_shutdown_state` | The value of the `ssl_shutdown_state` field is mapped to a `security_result.detection_fields` object with the key "SSL Shutdown State".  
`ssl_version` | `network.tls.version` | The value of the `ssl_version` field is directly mapped.  
`time` | `metadata.event_timestamp` | Used with `day`, `month`, and `year` to construct the `metadata.event_timestamp`.  
`type` | `metadata.description`  
`security_result.action_details` | The value of the `type` field is mapped to `metadata.description` except when it's "OK LOGIN". It is also mapped to `security_result.action_details` when it indicates an allow or block action (starts with "OK" or "FAIL").  
`userid` | `principal.user.userid`  
`target.user.userid` | If `type` is "OK LOGIN", the value is mapped to `target.user.userid`. Otherwise, it's mapped to `principal.user.userid`.  
`year` | `metadata.event_timestamp` | Used with `day`, `month`, and `time` to construct the `metadata.event_timestamp`. Set to "NETWORK" if `type` is "OK LOGIN". Set to "MACHINE" if `type` is "OK LOGIN". Set to "ALLOW" if `type` starts with "OK". Set to "BLOCK" if `type` starts with "FAIL".  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vsftpd-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
