---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jfrog-artifactory/
title: Collect JFrog Artifactory logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:04.279465+00:00
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
          chronicle/jfrog_artifactory:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
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
          chronicle/jfrog_artifactory:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: JFROG_ARTIFACTORY
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
