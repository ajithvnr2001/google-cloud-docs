---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-securesphere/
title: Collect Imperva SecureSphere Management logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:42.078084+00:00
---

# Collect Imperva SecureSphere Management logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-securesphere/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Imperva SecureSphere Management logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Imperva SecureSphere Management logs to Google Security Operations using the Bindplane agent.

Imperva SecureSphere is a web application firewall, database security, and file security platform that generates CEF-formatted syslog messages for security events, system events, and policy violations. The parser extracts fields from CEF messages using grok and key-value parsing and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Imperva SecureSphere Management server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Imperva SecureSphere Management Console



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
          chronicle/imperva_securesphere:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: IMPERVA_SECURESPHERE
            raw_log_field: body
        
        service:
          pipelines:
            logs/imperva_securesphere_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/imperva_securesphere
        




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
          chronicle/imperva_securesphere:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: IMPERVA_SECURESPHERE
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
             




## Configure syslog forwarding on Imperva SecureSphere Management

  1. Sign in to the **Imperva SecureSphere Management Console**.
  2. Go to **Configuration > Action Sets**.
  3. Click **Add** to create a new Action Set.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps Syslog`).



### Configure security event action

  * Click **Add Action** and configure:

    * **Action Type** : Select **Syslog**.
    * **Host** : Enter the Bindplane agent IP address.
    * **Port** : Enter the Bindplane agent port number (default `514`).
    * **Protocol** : Select **UDP** or **TCP**.
    * **Syslog Log Level** : Select **DEBUG**.
    * **Syslog Facility** : Select **LOCAL0**.
    * **Message Format** : Select **Gateway Log - Security Event - System Log (syslog) using CEF standard**.



### Configure system event action

  * Click **Add Action** and configure:

    * **Action Type** : Select **System Log**.
    * **Host** : Enter the Bindplane agent IP address.
    * **Port** : Enter the Bindplane agent port number.
    * **Protocol** : Select **UDP** or **TCP**.
    * **Message Format** : Select **Log System Event to System Log (syslog) using CEF standard**.



### Apply action sets to policies

  1. Go to **Policies > Security Policies**.
  2. For each relevant policy, configure **Followed Actions** to use your Action Set.
  3. Go to **Policies > System Events Policies**.
  4. Configure system event policies to use the Action Set for comprehensive monitoring.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`action` | `security_result.action_details` | The value of the `action` field is assigned to the `security_result.action_details` field.  
`application-name` | `target.application` | The value of the `application-name` field is assigned to the `target.application` field.  
`cat` | `security_result.category_details` | The value of the `cat` field is assigned to the `security_result.category_details` field.  
`class` | `security_result.detection_fields.value` | The value of the `class` field is assigned to the `value` field within `security_result.detection_fields`. The corresponding `key` is "class".  
`collection_time.seconds` | `metadata.event_timestamp.seconds` | The value of `collection_time.seconds` from the raw log is used as the seconds value for the `metadata.event_timestamp`.  
`create-time` | `metadata.event_timestamp.seconds` | The value of `create-time` is parsed and its seconds value is used as the seconds value for the `metadata.event_timestamp`.  
`cs1` | `security_result.rule_name` | The value of the `cs1` field is assigned to the `security_result.rule_name` field.  
`cs10` | `target.resource.attribute.labels.value` | The value of the `cs10` field is assigned to the `value` field within `target.resource.attribute.labels`.  
`cs10Label` | `target.resource.attribute.labels.key` | The value of the `cs10Label` field is assigned to the `key` field within `target.resource.attribute.labels`.  
`cs11` | `principal.application` | The value of the `cs11` field is assigned to the `principal.application` field.  
`cs12` | `security_result.description` | The value of the `cs12` field, after removing curly braces and dollar signs, is assigned to the `security_result.description` field.  
`cs14` | `target.resource.attribute.labels.value` | The value of the `cs14` field is assigned to the `value` field within `target.resource.attribute.labels`.  
`cs14Label` | `target.resource.attribute.labels.key` | The value of the `cs14Label` field is assigned to the `key` field within `target.resource.attribute.labels`.  
`cs15` | `security_result.summary` | The value of the `cs15` field is assigned to the `security_result.summary` field.  
`cs16` | `principal.process.command_line` | The value of the `cs16` field is assigned to the `principal.process.command_line` field.  
`cs17` | `target.resource.resource_subtype` | The value of the `cs17` field is assigned to the `target.resource.resource_subtype` field.  
`cs2` | `principal.group.group_display_name` | The value of the `cs2` field is assigned to the `principal.group.group_display_name` field.  
`cs3` | `principal.hostname`, `principal.asset.hostname` | The value of the `cs3` field is assigned to both the `principal.hostname` and `principal.asset.hostname` fields.  
`cs4` | `target.application` | The value of the `cs4` field is assigned to the `target.application` field, unless the value is "ProcessWitness".  
`cs5` | `metadata.description` | The value of the `cs5` field is assigned to the `metadata.description` field.  
`cs6` | `target.resource_ancestors.name` | The value of the `cs6` field is assigned to the `target.resource_ancestors.name` field.  
`cs7` | `target.resource_ancestors.resource_subtype` | The value of the `cs7` field is assigned to the `target.resource_ancestors.resource_subtype` field.  
`cs8` | `target.resource.name`, `target.resource.resource_type` | The value of the `cs8` field is assigned to the `target.resource.name` field, and the `target.resource.resource_type` is set to "DATABASE".  
`cs9` | `principal.user.userid` | The value of the `cs9` field is assigned to the `principal.user.userid` field.  
`description` | `security_result.description` | The value of the `description` field is assigned to the `security_result.description` field.  
`dest-ip` | `target.ip`, `target.asset.ip` | The IP address extracted from the `dest-ip` field is assigned to both the `target.ip` and `target.asset.ip` fields.  
`dest-port` | `target.port` | The value of the `dest-port` field, converted to an integer, is assigned to the `target.port` field.  
`deviceExternalId` | `intermediary.hostname` | The value of the `deviceExternalId` field is assigned to the `intermediary.hostname` field.  
`dpt` | `target.port` | The value of the `dpt` field, converted to an integer, is assigned to the `target.port` field.  
`dst` | `target.ip`, `target.asset.ip` | The value of the `dst` field is assigned to both the `target.ip` and `target.asset.ip` fields.  
`duser` | `target.user.userid` | The value of the `duser` field is assigned to the `target.user.userid` field.  
`eventId` | `metadata.product_log_id` | The value of the `eventId` field is assigned to the `metadata.product_log_id` field.  
`gateway-name` | `security_result.detection_fields.value` | The value of the `gateway-name` field is assigned to the `value` field within `security_result.detection_fields`. The corresponding `key` is "gateway-name".  
`http.request.method` | `network.http.method` | The value of the `http.request.method` field is assigned to the `network.http.method` field.  
`http.request.user-agent` | `network.http.user_agent` | The value of the `http.request.user_agent` field is assigned to the `network.http.user_agent` field.  
`http.response.code` | `network.http.response_code` | The value of the `http.response.code` field, converted to an integer, is assigned to the `network.http.response_code` field.  
`http.session-id` | `network.session_id` | The value of the `http.session-id` field is assigned to the `network.session_id` field.  
`http.user-name` | `principal.user.userid` | The value of the `http.user-name` field, with surrounding quotes removed, is assigned to the `principal.user.userid` field.  
`log_type` | `metadata.log_type` | The value of the `log_type` field from the raw log is assigned to the `metadata.log_type` field.  
`mx-ip` | `intermediary.ip` | The value of the `mx-ip` field is assigned to the `intermediary.ip` field.  
`MxIP` | `intermediary.ip` | The value of the `MxIP` field is assigned to the `intermediary.ip` field.  
`OSUser` | `principal.user.userid` | The value of the `OSUser` field is assigned to the `principal.user.userid` field.  
`policy-name` | `security_result.detection_fields.value` | The value of the `policy-name` field is assigned to the `value` field within `security_result.detection_fields`. The corresponding `key` is "policy-name".  
`pquery` | `target.resource.name`, `target.process.command_line` | If `pquery` is not empty and contains the word "from", the table name is extracted and assigned to `target.resource.name`, `target.resource.resource_type` is set to "TABLE", and the entire `pquery` value is assigned to `target.process.command_line`. Otherwise, the entire `pquery` value is assigned to `target.resource.name`.  
`pro` | `security_result.description` | The value of the `pro` field is assigned to the `security_result.description` field.  
`product` | `metadata.product_name` | The value of the `product` field is assigned to the `metadata.product_name` field.  
`product_type` | `metadata.product_event_type` | The value of the `product_type` field is assigned to the `metadata.product_event_type` field.  
`protocol` | `network.ip_protocol` | If the value of the `protocol` field is "TCP" or "UDP", it is assigned to the `network.ip_protocol` field.  
`proto` | `network.ip_protocol` | The value of the `proto` field is assigned to the `network.ip_protocol` field.  
`reason` | `security_result.rule_name` | The value of the `reason` field is assigned to the `security_result.rule_name` field.  
`rt` | `metadata.event_timestamp.seconds` | The value of `rt` is parsed and its seconds value is used as the seconds value for the `metadata.event_timestamp`.  
`server-group-name` | `target.resource.attribute.labels.value` | The value of the `server-group-name` field is assigned to the `value` field within `target.resource.attribute.labels`. The corresponding `key` is "server-group-name".  
`server-group-simulation-mode` | `target.resource.attribute.labels.value` | The value of the `server-group-simulation-mode` field is assigned to the `value` field within `target.resource.attribute.labels`. The corresponding `key` is "server-group-simulation-mode".  
`service-name` | `target.resource.attribute.labels.value` | The value of the `service-name` field is assigned to the `value` field within `target.resource.attribute.labels`. The corresponding `key` is "service-name".  
`ServiceName` | `target.application` | If `ApplicationName` is not empty and `ServiceName` is empty, the value of `ApplicationName` is assigned to `ServiceName`. The value of `ServiceName` is then assigned to `target.application`.  
`severity` | `security_result.severity`, `security_result.severity_details` | The value of the `severity` field is converted to uppercase. If it's one of "LOW", "MEDIUM", "HIGH", "CRITICAL", it's assigned to `security_result.severity`. If it's "INFORMATIVE" or "INFO", `security_result.severity` is set to "INFORMATIONAL". The original value is also assigned to `security_result.severity_details`.  
`severity_data` | `security_result.severity` | The value of the `severity_data` field is converted to uppercase. If it's one of "HIGH", "LOW", "MEDIUM", "CRITICAL", "ERROR", "INFORMATIONAL", it's assigned to `security_result.severity`.  
`source-ip` | `principal.ip`, `principal.asset.ip` | The value of the `source-ip` field is assigned to both the `principal.ip` and `principal.asset.ip` fields.  
`source-port` | `principal.port` | The value of the `source-port` field, converted to an integer, is assigned to the `principal.port` field.  
`spt` | `principal.port` | The value of the `spt` field, converted to an integer, is assigned to the `principal.port` field.  
`src` | `principal.ip`, `principal.asset.ip` | The value of the `src` field is assigned to both the `principal.ip` and `principal.asset.ip` fields.  
`srcapp` | `principal.application` | The value of the `srcapp` field is assigned to the `principal.application` field.  
`srchost` | `principal.hostname`, `principal.asset.hostname` | The value of the `srchost` field is assigned to both the `principal.hostname` and `principal.asset.hostname` fields.  
`vendor` | `metadata.vendor_name` | The value of the `vendor` field is assigned to the `metadata.vendor_name` field.  
`version` | `metadata.product_version` | The value of the `version` field is assigned to the `metadata.product_version` field.  
`violation-id` | `security_result.detection_fields.value` | The value of the `violation-id` field is assigned to the `value` field within `security_result.detection_fields`. The corresponding `key` is "violation-id".  
`violation-type` | `security_result.detection_fields.value` | The value of the `violation-type` field is assigned to the `value` field within `security_result.detection_fields`. The corresponding `key` is "violation-type".  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`externalId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`deviceCustomDate1` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`flexString1` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`flexString2` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`flexString2Label` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`requestContext` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`flexNumber1` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cn2` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cn1` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`ad.host` | `event.idm.read_only_udm.observer.hostname` | Mapped from changelog  
`requestMethod` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`request` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`msg` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`flexNumber2` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`flexString2` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`cs6` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`name` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`cs2` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs3` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs4` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`suser` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`login_user` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`princ_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`cs1` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`cs5` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`device_vendor` | `event.idm.read_only_udm.metadata.vendor_name` | Mapped from changelog  
`device_product` | `event.idm.read_only_udm.metadata.product_name` | Mapped from changelog  
`cs9` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs9Label` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs17` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`cs2Label` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`additional_json_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cs5` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`cs4` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`cs6` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`cs7` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`cs11` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`cs10` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`cs15` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`cs9` | `event.idm.read_only_udm.security_result.threat_id` | Mapped from changelog  
`cs12` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`inter_host` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`cs13` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`cs13` | `metadata.product_log_id` | Mapped from changelog  
`cs1Label` | `security_result.detection_fields` | Mapped from changelog  
`cs2Label` | `security_result.detection_fields` | Mapped from changelog  
`cs3Label` | `security_result.detection_fields` | Mapped from changelog  
`cs5Label` | `security_result.detection_fields` | Mapped from changelog  
`cs10Label` | `additional.fields` | Mapped from changelog  
`cs12Label` | `additional.fields` | Mapped from changelog  
`cs13Label` | `additional.fields` | Mapped from changelog  
`cs14Label` | `additional.fields` | Mapped from changelog  
`cs16Label` | `additional.fields` | Mapped from changelog  
`cs17Label` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-securesphere-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
