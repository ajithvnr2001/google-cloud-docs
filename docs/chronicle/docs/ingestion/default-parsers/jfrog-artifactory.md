---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jfrog-artifactory/
title: Collect JFrog Artifactory logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:39.182052+00:00
---

# Collect JFrog Artifactory logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jfrog-artifactory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect JFrog Artifactory logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest JFrog Artifactory logs to Google Security Operations using the Bindplane agent.

JFrog Artifactory is a universal artifact repository manager that generates syslog messages for repository access events, authentication, configuration changes, and artifact operations. The parser extracts fields from syslog and JSON-formatted logs using grok patterns and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the JFrog Artifactory server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * SSH access to the JFrog Artifactory instance



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



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
            chronicle/jfrog_artifactory:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: JFROG_ARTIFACTORY
                raw_log_field: body
        
        service:
            pipelines:
                logs/jfrog_artifactory_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/jfrog_artifactory
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
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
             




## Configure JFrog Artifactory syslog

  1. Connect to the **JFrog Artifactory** instance.
  2. Edit the file `$JFROG_HOME/artifactory/var/etc/artifactory/logback.xml`:
         
         vi $JFROG_HOME/artifactory/var/etc/artifactory/logback.xml
         

  3. Add the following syslog appender to the file:
         
         <appender name="SYSLOG" class="ch.qos.logback.classic.net.SyslogAppender">
             <syslogHost><BINDPLANE_IP></syslogHost>
             <facility>SYSLOG</facility>
             <suffixPattern>[%thread] %logger %msg</suffixPattern>
         </appender>
         

     * Replace `<BINDPLANE_IP>` with the actual Bindplane agent IP address.
  4. Add the syslog appender reference to the root logger:
         
         <root>
             <level value="debug"/>
             <appender-ref ref="CONSOLE"/>
             <appender-ref ref="FILE"/>
             <appender-ref ref="SYSLOG"/>
         </root>
         

  5. Save the file by pressing `ESC` and typing `:wq`.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
**action** | `read_only_udm.metadata.product_event_type` | The value of **action** from the raw log is converted to lowercase and mapped.  
**datetime** | `read_only_udm.metadata.event_timestamp` | The raw log's **datetime** field is parsed and converted to a timestamp.  
**hostname** | `read_only_udm.principal.hostname` | Directly mapped from the raw log's **hostname** field.  
**id** | `read_only_udm.metadata.product_log_id` | Directly mapped from the raw log's **id** field (from JSON payload).  
**ip** | `read_only_udm.principal.ip` | Directly mapped from the raw log's **ip** field. Hardcoded to "USER_RESOURCE_ACCESS". Hardcoded to "JFROG_ARTIFACTORY". Hardcoded to "Artifactory". Hardcoded to "JFROG".  
**owner** | `read_only_udm.principal.user.userid` | Mapped if **username** is not present in the raw log (from JSON payload).  
**repo_name** | `read_only_udm.target.resource.name` | Directly mapped from the raw log's **repo_name** field.  
**repo_type** | `read_only_udm.target.resource.resource_subtype` | Directly mapped from the raw log's **repo_type** field.  
**scope** | `read_only_udm.target.resource.name` | Directly mapped from the raw log's **scope** field (from JSON payload).  
**scope** | `read_only_udm.target.resource.resource_subtype` | Hardcoded to "scope" if **scope** is present in the raw log.  
**sequenceId** | `read_only_udm.metadata.product_log_id` | Quotes are removed from the **sequenceId** field and then mapped.  
**subject** | `read_only_udm.about.labels.key` | Hardcoded to "subject" if **subject** is present in the raw log.  
**subject** | `read_only_udm.about.labels.value` | Directly mapped from the raw log's **subject** field (from JSON payload).  
**type** | `read_only_udm.metadata.product_event_type` | Directly mapped from the raw log's **type** field (from JSON payload).  
**user** | `read_only_udm.principal.user.userid` | Directly mapped from the raw log's **user** field.  
**username** | `read_only_udm.principal.user.userid` | Directly mapped from the raw log's **username** field (from JSON payload).  
`data.repository_key", "data.release_bundle_name", "data.release_bundle_version", "data.property_key", "data.property_values", "data.platforms.architecture", and "data.platforms.os` | `additional.fields` | Mapped from changelog  
`data.repo_key" ,"subscription_key","source","image_name", "data.platforms` | `additional.fields` | Mapped from changelog  
`domain` | `principal.administrative_domain` | Mapped from changelog  
`data.path` | `target.file.full_path` | Mapped from changelog  
`data.name` | `target.user.user_display_name` | Mapped from changelog  
`data.size` | `target.file.size` | Mapped from changelog  
`SHA256` | `target.process.file.sha256` | Mapped from changelog  
`target_ip` | `target.ip` | Mapped from changelog  
`desc` | `metadata.description` | Mapped from changelog  
`method` | `network.http.method` | Mapped from changelog  
`url` | `target.url` | Mapped from changelog  
`prin_url` | `principal.url` | Mapped from changelog  
`response_code` | `network.http.response_code` | Mapped from changelog  
`RequestMethod` | `network.http.method` | Mapped from changelog  
`RequestPath` | `target.url` | Mapped from changelog  
`DownstreamContentSize" and "DownstreamStatus` | `Additional.Fields` | Mapped from changelog  
`ServiceAddr` | `principal.hostname` | Mapped from changelog  
`ClientAddr` | `target.ip` | Mapped from changelog  
`user_agent` | `network.http.user_agent` | Mapped from changelog  
`level` | `security_result.severity` | Mapped from changelog  
`msg` | `security_result.description` | Mapped from changelog  
`protocol` | `network.application_protocol` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jfrog-artifactory-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
