---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tomcat/
title: Collect Apache Tomcat logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:04:54.407531+00:00
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



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



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
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
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

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
