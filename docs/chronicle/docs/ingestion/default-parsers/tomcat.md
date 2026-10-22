---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tomcat/
title: Collect Apache Tomcat logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:20.700391+00:00
---

# Collect Apache Tomcat logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tomcat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Apache Tomcat logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Apache Tomcat logs to Google Security Operations using the Bindplane agent.

Apache Tomcat is a web application server that generates JSON access logs for HTTP requests, authentication events, and server activity. The parser extracts fields from JSON-formatted and syslog-formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Bindplane agent installed on the Tomcat server (to read local log files)
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Tomcat server



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



## Install the Bindplane agent on the Tomcat server to collect log files

Install the Bindplane agent on the Tomcat server itself, since it needs to read local log files.

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

## Configure the Bindplane agent to ingest Tomcat logs and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          filelog/tomcat:
            include:
              - /path/to/tomcat/logs/access-log.*.json
            start_at: beginning
        
        exporters:
          chronicle/tomcat:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: TOMCAT
            raw_log_field: body
        
        service:
          pipelines:
            logs/tomcat_to_chronicle:
              receivers:
                - filelog/tomcat
              exporters:
                - chronicle/tomcat
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `include`: Path to Tomcat JSON access log files. Adjust to match your Tomcat log directory and file pattern.
    * `start_at`: Set to `beginning` to read existing logs, or `end` to read only new entries.
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
          chronicle/tomcat:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: TOMCAT
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
             




## Configure JSON access logs in Tomcat

  1. Open the Tomcat configuration file at `$CATALINA_BASE/conf/server.xml`.
  2. Locate the `<Host>` tag and add the following inside:
         
         <Valve className="org.apache.catalina.valves.JsonAccessLogValve"
                directory="logs"
                prefix="access-log"
                suffix=".json"
                rotatable="true"
                maxDays="7"/>
         

  3. Restart Tomcat to apply changes:
         
         cd /path/to/tomcat
         bin/catalina.sh stop
         bin/catalina.sh start
         

  4. A new JSON log file will appear daily (for example, `logs/access-log.2025-07-02.json`).




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`@timestamp` | `metadata.event_timestamp` | The value of `@timestamp` from the raw log is directly mapped to this UDM field. It represents the time the event occurred.  
`agent.ephemeral_id` | `additional.fields[ephemeral_id].value.string_value` | The ephemeral ID from the agent is added as a key-value pair in the `additional` fields.  
`agent.hostname` | `observer.hostname` | The agent's hostname is used as the observer hostname.  
`agent.id` | `observer.asset_id` | The agent ID is combined with the agent type to create the observer asset ID (e.g., `filebeat: <agent_id>`).  
`agent.type` | `observer.application` | The agent type is used as the observer application.  
`agent.version` | `observer.platform_version` | The agent version is used as the observer platform version.  
`host.hostname` | `principal.hostname` | The host's hostname is used as the principal hostname.  
`host.id` | `principal.asset.asset_id` | The host ID is prepended with `Host Id:` to create the principal asset ID.  
`host.ip` | `principal.ip`, `observer.ip` | The host's IP address is used for both the principal and observer IP. If multiple IPs are present, they are merged into an array.  
`host.mac` | `principal.mac` | The host's MAC address is used as the principal MAC address. If multiple MACs are present, they are merged into an array.  
`host.os.family` | `principal.platform` | If the host OS family is `rhel` or `redhat`, the principal platform is set to `LINUX`.  
`host.os.kernel` | `principal.platform_patch_level` | The host OS kernel version is used as the principal platform patch level.  
`host.os.name` | `additional.fields[os_name].value.string_value` | The host OS name is added as a key-value pair in the `additional` fields.  
`host.os.version` | `principal.platform_version` | The host OS version is used as the principal platform version.  
`log.file.path` | `principal.process.file.full_path` | The log path is used as the principal process file's full path.  
`log_level` | `security_result.severity`, `security_result.severity_details`, `security_result.action` | The log level is used to determine the security result severity, severity details, and action. DEBUG, INFO, and AUDIT map to INFORMATIONAL severity and ALLOW action. ERROR maps to ERROR severity and BLOCK action. WARNING and WARN map to MEDIUM severity and BLOCK action. The raw log_level value is also mapped to severity_details.  
`logstash.irm_environment` | `additional.fields[irm_environment].value.string_value` | The Iron Mountain environment from Logstash is added as a key-value pair in the `additional` fields.  
`logstash.irm_region` | `additional.fields[irm_region].value.string_value` | The Iron Mountain region from Logstash is added as a key-value pair in the `additional` fields.  
`logstash.irm_site` | `additional.fields[irm_site].value.string_value` | The Iron Mountain site from Logstash is added as a key-value pair in the `additional` fields.  
`logstash.process.host` | `intermediary.hostname` | The Logstash processing host is used as the intermediary hostname.  
`logstash.process.timestamp` | `metadata.collected_timestamp` | The Logstash processing timestamp is used as the collected timestamp.  
`logstash.xyz_environment` | `additional.fields[xyz_environment].value.string_value` | The xyz environment from Logstash is added as a key-value pair in the `additional` fields.  
`logstash.xyz_region` | `additional.fields[xyz_region].value.string_value` | The xyz region from Logstash is added as a key-value pair in the `additional` fields.  
`logstash.xyz_site` | `additional.fields[xyz_site].value.string_value` | The xyz site from Logstash is added as a key-value pair in the `additional` fields.  
`message` | `metadata.description` | The message field is parsed as JSON and its `event_message` field is used as the metadata description. The intermediary application is hardcoded to `logstash`. The metadata event type is hardcoded to `USER_UNCATEGORIZED`. The metadata log type is set to `TOMCAT` from the raw log's batch.type or batch.log_type. The metadata product name is hardcoded to `Tomcat`. The metadata vendor name is hardcoded to `Tomcat`.  
`user` | `principal.user.userid` | The user field from the raw log is used as the principal user ID.  
`product_event` | `metadata.product_event_type` | Mapped from changelog  
`summary` | `security_result.summary` | Mapped from changelog  
`query` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tomcat-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
