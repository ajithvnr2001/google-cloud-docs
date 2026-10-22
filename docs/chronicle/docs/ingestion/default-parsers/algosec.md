---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/algosec/
title: Collect AlgoSec Security Management logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:45.172016+00:00
---

# Collect AlgoSec Security Management logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/algosec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AlgoSec Security Management logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest AlgoSec Security Management logs to Google Security Operations using the Bindplane agent.

AlgoSec Security Management Suite (ASMS) provides network security policy management across firewalls, SDN, and cloud platforms. It includes Firewall Analyzer for risk and compliance analysis, FireFlow for change management automation, and AppViz for application connectivity visibility.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the AlgoSec appliances
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to AlgoSec Firewall Analyzer, FireFlow, and AppViz



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
          chronicle/algosec:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: ALGOSEC
            raw_log_field: body
        
        service:
          pipelines:
            logs/algosec_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/algosec
        




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
          chronicle/algosec:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ALGOSEC
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
             




## Configure syslog for Firewall Analyzer

  1. Sign in to the **AFA** appliance using SSH.
  2. Go to the **syslog-ng** configuration directory:
         
         cd /etc/syslog-ng
         

  3. Backup the existing configuration:
         
         cp syslog-ng.conf syslog-ng.conf.orig
         

  4. Edit the syslog-ng configuration file:
         
         vi syslog-ng.conf
         

  5. Add the following lines to define the remote syslog server:
         
         destination d_remote { udp("<BINDPLANE_IP>" port(514)); };
         log { source(s_sys); destination(d_remote); };
         

     * Replace `<BINDPLANE_IP>` with the IP address of the Bindplane agent.
  6. Save and exit the editor.

  7. Restart the syslog-ng service to apply changes:
         
         service syslog-ng restart
         

  8. Optional: Verify the Syslog configuration:

     1. Go to **Administration > Syslog Server Settings**.
     2. Click **Test Connectivity**.



## Configure syslog for FireFlow

  1. Sign in to the **FireFlow** machine as **root**.
  2. Open the `/etc/syslog.conf` file for editing:
         
         vi /etc/syslog.conf
         

  3. Add the following line to the file:
         
         local0.*@<BINDPLANE_IP>
         

     * Replace `<BINDPLANE_IP>` with the IP address of the Bindplane agent server.



## Configure Syslog for AppViz

  1. Sign in to the **AppViz** appliance via SSH.
  2. Go to the **syslog-ng** configuration directory:
         
         cd /etc/syslog-ng
         

  3. Back up the existing configuration:
         
         cp syslog-ng.conf syslog-ng.conf.orig
         

  4. Edit the syslog-ng configuration file:
         
         vi syslog-ng.conf
         

  5. Add the following to define the remote syslog server:
         
         destination d_remote { udp("<BINDPLANE_IP>" port(514)); };
         log { source(s_sys); destination(d_remote); };
         

     * Replace `<BINDPLANE_IP>` with the IP address of the Bindplane agent.
  6. Save and exit the editor.

  7. Restart the syslog-ng service to apply changes:
         
         service syslog-ng restart
         

  8. Verify the syslog configuration:

     1. In the AppViz interface, go to **Administration > Syslog Server Settings**.
     2. Click **Test Connectivity**.



## Configure syslog for login and logout events

  1. Sign in to the **ASMS appliance** via SSH.
  2. Go to the **syslog-ng** configuration directory:
         
         cd /etc/syslog-ng
         

  3. Backup the existing configuration:
         
         cp syslog-ng.conf syslog-ng.conf.orig
         

  4. Edit the syslog-ng configuration file:
         
         vi syslog-ng.conf
         

  5. Add the following to define the remote syslog server:
         
         destination d_remote { udp("<BINDPLANE_IP>" port(514)); };
         log { source(s_sys); destination(d_remote); };
         

     * Replace `<BINDPLANE_IP>` with the IP address of the Bindplane agent.
  6. Save and exit the editor.

  7. Restart the syslog-ng service to apply changes:
         
         service syslog-ng restart
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`by_user` | `principal.user.user_display_name` | The value of the `by_user` field from the raw log is assigned to this UDM field.  
`collection_time` | `metadata.event_timestamp` | The seconds and nanos fields are combined to create a timestamp.  
`comm` | `target.process.command_line` | The value of the `comm` field extracted from the `desc` field using grok is assigned to this UDM field.  
`datetime` | `metadata.event_timestamp` | The date and time are extracted from the raw log and used to populate the event timestamp.  
`desc` | `metadata.description` | The value of the `desc` field from the raw log is assigned to this UDM field when no other description is available.  
`dest_ip` | `target.ip` | The value of the `dest_ip` field from the raw log is assigned to this UDM field.  
`dest_port` | `target.port` | The value of the `dest_port` field from the raw log is assigned to this UDM field.  
`details` | `security_result.summary` | The value of the `details` field from the raw log is assigned to this UDM field.  
`device` | `principal.asset.hostname` | The value of the `device` field from the raw log is assigned to this UDM field.  
`dst_ip` | `target.ip` | The value of the `dst_ip` field from the raw log is assigned to this UDM field.  
`dst_port` | `target.port` | The value of the `dst_port` field from the raw log is assigned to this UDM field.  
`event_id` | `metadata.product_event_type` | The value of the `event_id` field from the raw log is assigned to this UDM field. It is also used in parser logic to determine the `metadata.event_type` and other fields.  
`event_name` | `metadata.product_event_type` | The value of the `event_name` field from the raw log is assigned to this UDM field.  
`firewall` | `target.hostname` | The value of the `firewall` field from the raw log is assigned to this UDM field.  
`host` | `principal.hostname` | The value of the `host` field from the raw log is assigned to this UDM field.  
`host_type` | `principal.asset.category` | The value of the `host_type` field from the raw log is assigned to this UDM field.  
`iporhost` | `principal.ip/principal.hostname/target.ip/target.hostname/observer.ip/observer.hostname` | If the value is an IP address, it's mapped to `principal.ip,target.ip,` or `observer.ip` depending on the log source and event type. If it's a hostname, it's mapped to `principal.hostname,target.hostname,` or `observer.hostname`.  
`IP` | `principal.ip` | The value of the `IP` field from the raw log is assigned to this UDM field.  
`kv_data` | `security_result.summary` | The value of the `kv_data` field from the raw log is assigned to this UDM field.  
`log_type` | `metadata.log_type` | Hardcoded to `ALGOSEC`.  
`metric` | `security_result.action_details` | The value of the `metric` field from the raw log is assigned to this UDM field.  
`msg` | `security_result.summary/security_result.description` | The value of the `msg` field from the raw log is used to populate either the summary or description of the security result, depending on the context. It is also used to `extractrisk_level,risk_count,risk_code,` and `risk_title` fields.  
`pid` | `target.process.pid` | The value of the `pid` field extracted from the `desc` field using grok is assigned to this UDM field.  
`product` | `metadata.product_name` | The value of the `product` field from the raw log is assigned to this UDM field.  
`report` | `security_result.description` | The value of the `report` field from the raw log is included in the description of the security result.  
`report_data.Device IP` | `target.ip` | The value of the `Device IP` field from the parsed JSON data is assigned to this UDM field.  
`report_data.Highest Risk Level` | `security_result.description` | The value of the `Highest Risk Level` field from the parsed JSON data is included in the description of the security result. It is also used to determine the severity of the security result.  
`report_data.Security Rating Score` | `security_result.description` | The value of the `Security Rating Score` field from the parsed JSON data is included in the description of the security result.  
`Requestor.Email` | `principal.user.email_addresses` | The value of the `Email` field within the `Request` object from the parsed JSON data is assigned to this UDM field.  
`Requestor.Name` | `principal.user.user_display_name` | The value of the `Name` field within the `Requestor` object from the parsed JSON data is assigned to this UDM field.  
`RequestType` | `target.resource.attribute.labels` | The value of the `RequestType` field from the raw log is added as a label to the target resource.  
`risk_title` | `security_result.summary` | The value of the `risk_title` field from the raw log is assigned to this UDM field.  
`src_ip` | `principal.ip` | The value of the `src_ip` field from the raw log is assigned to this UDM field.  
`src_port` | `principal.port` | The value of the `src_port` field from the raw log is assigned to this UDM field.  
`status` | `security_result.description/security_result.action_details` | The value of the `status` field from the raw log is included in the description of the security result or action details, depending on the context. It is also used to determine the severity of the security result.  
`target_app` | `target.application` | The value of the `target_app` field from the raw log is assigned to this UDM field.  
`TemplateName` | `metadata.description` | The value of the `TemplateName` field from the raw log is assigned to this UDM field.  
`url` | `security_result.url_back_to_product` | The value of the `url` field from the raw log is assigned to this UDM field.  
`user` | `principal.user.userid` | The value of the `user` field from the raw log is assigned to this UDM field.  
`vendor` | `metadata.vendor_name` | The value of the `vendor` field from the raw log is assigned to this UDM field.  
`version` | `metadata.product_version` | The value of the `version` field from the raw log is assigned to this UDM field.  
`WorkFlow` | `target.resource.attribute.labels` | The value of the `WorkFlow` field from the raw log is added as a label to the target resource.  
`(Parser Logic)` | `extensions.auth.type` | Hardcoded to `MACHINE`.  
`(Parser Logic)` | `security_result.action` | Determined based on the `event_id` and other fields. Typically set to `ALLOW or BLOCK`.  
`(Parser Logic)` | `security_result.category` | Hardcoded to `POLICY_VIOLATION` for Firewall Analyzer events.  
`(Parser Logic)` | `security_result.description` | Constructed based on other fields, providing context and details about the event.  
`(Parser Logic)` | `security_result.severity` | Determined based on the `event_id,msg,` and other fields. Typically set to `LOW,MEDIUM,` or `HIGH.  
`(Parser Logic)` | `metadata.event_type` | Determined based on the `event_id` and other fields. Examples include `USER_LOGIN,USER_LOGOUT,USER_RESOURCE_ACCESS,GENERIC_EVENT,STATUS_UNCATEGORIZED,SCAN_HOST,NETWORK_CONNECTION,` and `STATUS_UPDATE`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/algosec-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
