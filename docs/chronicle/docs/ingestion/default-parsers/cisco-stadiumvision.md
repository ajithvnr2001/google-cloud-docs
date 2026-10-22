---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-stadiumvision/
title: Collect Cisco Vision Dynamic Signage Director (formerly StadiumVision Director) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:07.843175+00:00
---

# Collect Cisco Vision Dynamic Signage Director (formerly StadiumVision Director) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-stadiumvision/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Cisco Vision Dynamic Signage Director (formerly StadiumVision Director) logs

**Parser Version:** 1.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Cisco Vision Dynamic Signage Director (formerly known as StadiumVision Director) logs to Google Security Operations using Bindplane.

Cisco Vision Dynamic Signage Director is a digital signage and content management platform designed for stadiums, arenas, and large venues. It enables centralized control and distribution of multimedia content to digital displays, including video walls, scoreboards, and digital menu boards across venue networks.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Cisco Vision Dynamic Signage Director server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Cisco Vision Dynamic Signage Director web interface with administrator role
  * Cisco Vision Dynamic Signage Director Release 6.4 or later (syslog support was added in Release 6.4)



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

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * Locate the configuration file on your operating system as follows:

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
          chronicle/cisco_vision:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '<PLACEHOLDER_CREDS_FILE_PATH>'
            customer_id: '<PLACEHOLDER_CUSTOMER_ID>'
            endpoint: chronicle.googleapis.com
            log_type: CISCO_STADIUMVISION
            raw_log_field: body
            ingestion_labels:
              source: cisco_vision_director
        
        service:
          pipelines:
            logs/cisco_vision_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/cisco_vision
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * The receiver is configured to listen on UDP port 514 on all network interfaces (`0.0.0.0:514`)
    * Cisco Vision Director sends syslog messages using RFC 5424 format over UDP (RFC 5426 transport)
  * **Exporter configuration:**

    * `<PLACEHOLDER_CREDS_FILE_PATH>`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<PLACEHOLDER_CUSTOMER_ID>`: Your Google SecOps customer ID
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
  * Example configuration
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/cisco_vision:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
            endpoint: chronicle.googleapis.com
            log_type: CISCO_STADIUMVISION
            raw_log_field: body
            ingestion_labels:
              source: cisco_vision_director
              env: production
        
        service:
          pipelines:
            logs/cisco_vision_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/cisco_vision
        




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/cisco_vision:
            compression: gzip
            creds_file_path: '<PLACEHOLDER_CREDS_FILE_PATH>'
            customer_id: '<PLACEHOLDER_CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CISCO_STADIUMVISION
            raw_log_field: body
            ingestion_labels:
              source: cisco_vision_director
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



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
         




## Configure Cisco Vision Dynamic Signage Director syslog forwarding

### Enable syslog on Cisco Vision Director

  1. Sign in to the Cisco Vision Dynamic Signage Director web interface with administrator credentials.
  2. Go to **Configuration > System Configuration > Dynamic Signage Director Setting > Syslog Configuration**.
  3. Select **Enable Syslog** from the Configuration Properties panel.
  4. Click **Edit**. The Edit Configuration Setting dialog box appears.
  5. Select **true** from the dropdown menu.
  6. Click **Save**.

**Note:** The default value for Enable Syslog is `false`. Setting this to `true` enables Cisco Vision Director to send system log files to an external syslog server.

### Configure syslog server IP address and port

  1. In the same **Syslog Configuration** section, select **Syslog Server IP & Port**.
  2. Click **Edit**. The Edit Configuration dialog box appears.
  3. In the **Value** field, enter the IP address and port of the Bindplane agent host in the format `IP_ADDRESS:PORT`. 
     * For example: `192.168.1.100:514`
     * Replace `192.168.1.100` with the actual IP address of the Bindplane agent host
     * Use port `514` to match the Bindplane agent configuration
  4. Click **Save**.
  5. Verify the IP address and port now appear in the **Syslog Server IP & Port** field.

**Note:** Cisco Vision Director forwards system log files using RFC 5424 format (latest syslog message format) over UDP transport (RFC 5426).

### Enable DMP syslog forwarding through Director (optional)

If you want to forward Digital Media Player (DMP) system logs through Cisco Vision Director to the external syslog server:

  1. In the **Syslog Configuration** section, select **Enable DMP Syslog through Director**.
  2. Click **Edit**. The Edit Configuration Setting dialog box appears.
  3. Change the **Value** to **true**.
  4. Click **Save**.

**Note:** This setting enables DMP system log files to be forwarded to the external syslog server through Cisco Vision Director, except for DWS logs. The default value is `false`.

### Verify syslog configuration

  1. After saving the configuration, verify that logs are being sent to the Bindplane agent.
  2. Check the Bindplane agent logs for incoming syslog messages:

     * **Linux:**
    
    sudo journalctl -u observiq-otel-collector -f
    

     * **Windows:**
    
    type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
    

  3. You should see log entries indicating successful receipt and forwarding of Cisco Vision Director syslog messages.




### Additional configuration resources

For more information about Cisco Vision Dynamic Signage Director syslog configuration, see the following Cisco documentation:

  * [Cisco Vision Dynamic Signage Director Release Notes for Release 6.4](https://www.cisco.com/c/en/us/td/docs/Sports_Entertainment/cisco-vision/dynamic-signage-director/release-notes/6-4/cv-dsd-relnotes-6-4.html)
  * [Cisco Vision Dynamic Signage Director Administration Guide Release 6.4](https://www.cisco.com/c/en/us/td/docs/Sports_Entertainment/cisco-vision/dynamic-signage-director/admin-guides/6-4/cv-dsd-sys-admin-6-4/module-sys-admin-cfg-server.html)



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
intem_host | intermediary.hostname | Hostname of the intermediary device  
desc, data | metadata.description | Additional description of the event  
| metadata.event_type | Type of event represented by the log entry  
event_category | metadata.product_event_type | Product-specific event type  
| network.application_protocol | Application protocol used in the connection  
method | network.http.method | HTTP method used in the request  
response | network.http.response_code | HTTP response code  
user_agent | network.http.user_agent | User agent string from the HTTP request  
ses | network.session_id | Identifier for the network session  
application | principal.application | Application associated with the principal  
prin_ip | principal.ip | IP address associated with the principal  
pid | principal.process.pid | Process ID of the principal  
acct | principal.user.userid | User ID of the principal  
action_result | security_result.action | Action taken by the security system  
res, task | security_result.action_details | Details of the security action  
msg_data, desc | security_result.description | Description of the security result  
grantors, method_name, type, name, count, m1_rate, m5_rate, m15_rate, mean_rate, rate_unit, duration_unit | security_result.detection_fields | Additional fields related to detection  
severity | security_result.severity | Severity level of the security result  
op, act_detail | security_result.summary | Summary of the security result  
exe, ENV | target.file.full_path | Full path to the target file  
COMMAND | target.process.command_line | Command line of the target process  
path, url | target.url | URL associated with the target  
USER | target.user.userid | User ID of the target  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-stadiumvision-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
