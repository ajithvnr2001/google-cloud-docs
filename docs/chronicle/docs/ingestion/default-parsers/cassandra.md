---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cassandra/
title: Collect Apache Cassandra logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:02.330226+00:00
---

# Collect Apache Cassandra logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cassandra/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Apache Cassandra logs

**Parser Version:** 4.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Apache Cassandra logs to Google Security Operations using the Bindplane agent.

Apache Cassandra generates logs for database operations, cluster events, and system activity. The parser extracts fields using grok patterns and JSON filters, then maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Apache Cassandra host
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative (SSH) access to the Apache Cassandra host



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
          chronicle/cassandra:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: CASSANDRA
            raw_log_field: body
        
        service:
          pipelines:
            logs/cassandra_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/cassandra
        




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
          chronicle/cassandra:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CASSANDRA
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
           
           ```bash
           sudo systemctl status observiq-otel-collector
           ```
           

    2. Check logs for errors:
           
           ```bash
           sudo journalctl -u observiq-otel-collector -f
           ```
           

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
             




## Configure syslog export in Apache Cassandra

  1. Sign in to the Apache Cassandra host using SSH.
  2. Open the configuration file `logback.xml`:

     * Apache Cassandra (most versions): `$(CASSANDRA_HOME)/conf`
     * Datastax Enterprise (package install): `/etc/dse`
     * Datastax Enterprise (tar install): `$(TARBALL_ROOT)/resources/cassandra/conf`
  3. Add the following **Appender** definition to the `logback.xml` file on Line 28:
         
         <appender name="SYSLOG" class="ch.qos.logback.classic.net.SyslogAppender">
             <syslogHost>BINDPLANE_IP</syslogHost>
             <port>BINDPLANE_PORT</port>
             <facility>LOCAL7</facility>
             <throwableExcluded>true</throwableExcluded>
             <suffixPattern>%thread:%level:%logger{36}:%msg</suffixPattern>
         </appender>
         

  4. Replace `BINDPLANE_IP` and `BINDPLANE_PORT` with the actual Bindplane agent IP address and port.

  5. Add the following code to the root logger block `<root level="INFO">` in the `logback.xml` file:

The location where this line is inserted depends on your version of Apache Cassandra:

     * Apache Cassandra 5.0.x, Line 123
     * Apache Cassandra 4.0.x and 4.1.x, Line 115
     * Apache Cassandra 3.11.x and 3.0.x, Line 92
     * Datastax Enterprise (all versions), Line 121
    
    <appender-ref ref="SYSLOG" />
    




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`agent.ephemeral_id` | `observer.labels.value` | Value of `agent.ephemeral_id` from the inner JSON message.  
`agent.hostname` | `observer.hostname` | Value of `agent.hostname` from the inner JSON message.  
`agent.id` | `observer.asset_id` | Concatenation of `filebeat:` and the value of `agent.id` from the inner JSON message.  
`agent.name` | `observer.user.userid` | Value of `agent.name` from the inner JSON message.  
`agent.type` | `observer.application` | Value of `agent.type` from the inner JSON message.  
`agent.version` | `observer.platform_version` | Value of `agent.version` from the inner JSON message.  
`cloud.availability_zone` | `principal.cloud.availability_zone` | Value of `cloud.availability_zone` from the inner JSON message.  
`cloud.instance.id` | `principal.resource.product_object_id` | Value of `cloud.instance.id` from the inner JSON message.  
`cloud.instance.name` | `principal.resource.name` | Value of `cloud.instance.name` from the inner JSON message.  
`cloud.machine.type` | `principal.resource.attribute.labels.value` | Value of `cloud.machine.type` from the inner JSON message, where the corresponding `key` is `machine_type`.  
`cloud.provider` | `principal.resource.attribute.labels.value` | Value of `cloud.provider` from the inner JSON message, where the corresponding `key` is `provider`.  
`event_metadata._id` | `metadata.product_log_id` | Value of `event_metadata._id` from the inner JSON message.  
`event_metadata.version` | `metadata.product_version` | Value of `event_metadata.version` from the inner JSON message.  
`host.architecture` | `target.asset.hardware.cpu_platform` | Value of `host.architecture` from the inner JSON message.  
`host.fqdn` | `target.administrative_domain` | Value of `host.fqdn` from the inner JSON message.  
`host.hostname` | `target.hostname` | Value of `host.hostname` from the inner JSON message.  
`host.id` | `target.asset.asset_id` | Concatenation of `Host Id:` and the value of `host.id` from the inner JSON message.  
`host.ip` | `target.asset.ip` | Array of IP addresses from `host.ip` in the inner JSON message.  
`host.mac` | `target.mac` | Array of MAC addresses from `host.mac` in the inner JSON message.  
`host.os.kernel` | `target.platform_patch_level` | Value of `host.os.kernel` from the inner JSON message.  
`host.os.platform` | `target.platform` | Set to `LINUX` if `host.os.platform` is `debian`.  
`host.os.version` | `target.platform_version` | Value of `host.os.version` from the inner JSON message.  
`hostname` | `principal.hostname` | Value of `hostname` extracted from the `message` field using grok.  
`key` | `security_result.detection_fields.value` | Value of `key` extracted from the `message` field using grok, where the corresponding `key` is `key`.  
`log.file.path` | `principal.process.file.full_path` | Value of `log.file.path` from the inner JSON message.  
`log_level` | `security_result.severity` | Mapped based on the value of `log_level`: `DEBUG`, `INFO`, `AUDIT` map to `INFORMATIONAL`; `ERROR` maps to `ERROR`; `WARNING` maps to `MEDIUM`.  
`log_level` | `security_result.severity_details` | Value of `log_level` extracted from the `message` field using grok.  
`log_type` | `metadata.log_type` | Value of `log_type` from the raw log.  
`message` | `security_result.description` | Description extracted from the `message` field using grok.  
`message` | `target.process.command_line` | Command line extracted from the `message` field using grok.  
`now` | `security_result.detection_fields.value` | Value of `now` extracted from the `message` field using grok, where the corresponding `key` is `now`. Parsed from the `event_time` field extracted from the `message` field using grok. Set to `USER_RESOURCE_ACCESS` if both `hostname` and `host.hostname` are present, otherwise set to `GENERIC_EVENT`. Set to `CASSANDRA`. Set to `CASSANDRA`. Set to `ephemeral_id`. Set to `VIRTUAL_MACHINE` if `cloud.instance.name` is present. Set to `key` and `now` for the corresponding detection fields.  
`timestamp` | `timestamp` | From the raw log's `create_time` field.  
`authenticated_var` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`authenticated_var` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`user_var` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`operation` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`operation` | `event.idm.read_only_udm.target.process.command_line` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cassandra-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
