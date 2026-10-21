---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/stix/
title: Collect STIX Threat Intelligence logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:39.158870+00:00
---

# Collect STIX Threat Intelligence logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/stix/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect STIX Threat Intelligence logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest STIX Threat Intelligence logs to Google Security Operations using the Bindplane agent.

STIX (Structured Threat Information Expression) is a standardized language and format for sharing indicators of compromise (IOCs) and threat intelligence data between organizations. STIX data is typically received as JSON or XML files from TAXII servers or threat intelligence platforms. The Bindplane agent collects STIX data files directly from the local file system.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * A TAXII client or threat intelligence platform that saves STIX-formatted files (JSON or XML) to a local directory



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

## Configure the Bindplane agent to ingest logs and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          filelog:
            include:
              - /var/log/stix/*.json
            start_at: beginning
        
        exporters:
          chronicle/stix:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: STIX
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/stix_to_chronicle:
              receivers:
                - filelog
              exporters:
                - chronicle/stix
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths to monitor. Set this to the directory where STIX files are saved: 
      * **Linux** : `/var/log/stix/*.json`
      * **Windows** : `C:\Logs\stix\*.json`
    * `start_at`: Set to `beginning` to read existing logs or `end` to only read new entries
  * **Exporter configuration:**

    * `stix`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `STIX`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `stix_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/stix:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: STIX
            raw_log_field: body
            ingestion_labels:
              env: production
        


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
             




## Configure STIX data file collection

STIX is a data format, not a product. STIX threat intelligence data is typically received as JSON or XML files from TAXII clients, threat intelligence platforms, or manual downloads. You need to ensure these files are placed in a directory that the Bindplane agent monitors.

### Linux

  1. Create a directory to store STIX data files:
         
         sudo mkdir -p /var/log/stix
         

  2. Configure your TAXII client or threat intelligence platform to save STIX files to `/var/log/stix/`.

  3. Ensure the Bindplane agent service account has read access to the directory:
         
         sudo chmod 755 /var/log/stix
         




### Windows

  1. Create a directory to store STIX data files:
         
         mkdir C:\Logs\stix
         

  2. Configure your TAXII client or threat intelligence platform to save STIX files to `C:\Logs\stix`.

  3. Update the Bindplane agent `include` path in `config.yaml` to match:
         
         include:
           - C:\Logs\stix\*.json
         

**Note:** STIX data can be in JSON (STIX 2.x) or XML (STIX 1.x) format. Adjust the `include` glob pattern to match your file format (for example, `*.json`, `*.xml`, or both using multiple `include` entries). The Bindplane agent service account must have read access to the data directory.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
| entity.administrative_domain | Set to "TEST"  
assetid_value | entity.asset.asset_id | Value from assetid_value if not empty  
condition_label, related_indicators_relationship_label, related_indicators_scope, indicator_types_label, valid_start_time_label, controlled_structure_label, marking_structure_label | entity.asset.attribute.labels | Merged from various labels  
name | entity.file.full_path | Value copied directly  
val, hash.simple_hash_value, MD5_val, hash_value | entity.file.md5 | Value from val if matches md5 regex, else hash.simple_hash_value if type MD5, else MD5_val, else hash_value  
value | entity.file.names | Value copied directly  
val, hash.simple_hash_value, sha1_val, hash_value | entity.file.sha1 | Value from val if matches sha1 regex, else hash.simple_hash_value if type SHA1, else sha1_val, else hash_value  
val, hash.simple_hash_value, sha256val, sha_value, sha_value | entity.file.sha256 | Value from val if matches sha256 regex, else hash.simple_hash_value if type SHA256, else sha256val, else sha_value  
observable.object.properties.value, dom, value, host, name, external_references.0.source_name | entity.hostname | Value from observable.object.properties.value if type FQDN, else dom from grok, else value if type domain-name, else host, else name if main_observable_type domain/hostname, else external_references.0.source_name  
ip_val, ipval, ip, source_ip, value, src_ip | entity.ip | Value from ip_val if grok matched, else ipval if category ipv4-addr, else ip from pattern grok, else source_ip, else value if type ipv4, else src_ip from grok  
source_port, src_port | entity.port | Value from source_port or src_port  
indicator_label, extension_value1, extension_value2, extension_value3, extension_value4, revoked_value, spec_version_value, object_marking_ref_value, label_value | entity.resource.attribute.labels | Merged from various labels  
observable.object.properties.value, url_val, value, observable_properties_value | entity.url | Value from observable.object.properties.value if type URL, else url_val from grok, else value if type url, else observable_properties_value if not empty  
email_val, mail, value | entity.user.email_addresses | Value from email_val if grok matched, else mail from grok, else value if type email-addr  
timestamp | metadata.collected_timestamp | Converted using date match ISO8601/RFC 3339  
title, description | metadata.description | Value from title or description  
entity_type | metadata.entity_type | Value copied directly  
timestamp, valid_until | metadata.interval.end_time | Converted from timestamp or valid_until using date match ISO8601/RFC 3339  
timestamp, valid_from, created | metadata.interval.start_time | Converted from timestamp, valid_from, created, or timestamp using date match ISO8601/RFC 3339  
id | metadata.product_entity_id | Value copied directly  
version | metadata.product_version | Value copied directly  
threat_detail | metadata.threat | Merged from threat_detail  
threat_detail_category | threat.category | Value copied directly  
confidence_value, confidence, x_stix_confidence, x_ctix_confidence_score | threat.confidence_details | Value from confidence_value, else confidence if no_value, else x_stix_confidence, else x_ctix_confidence_score  
value, confidence, x_ctix_confidence_score | threat.confidence_score | Value from value if name Confidence Score, else confidence, else x_ctix_confidence_score, converted to float  
property_label, sha512_value, observable_id, observable_object_id, keyword_label | threat.detection_fields | Merged from various labels  
description | threat.description | Value copied directly  
value, extensions.extension-definition--ea279b3e-5c71-4632-ac08-831c66a786ba.score | threat.risk_score | Value from value if name Risk, else extensions score, converted to float  
| metadata.product_name | Set to "STIX"  
| metadata.vendor_name | Set to "STIX"  
`dom` | `event.idm.entity.entity.hostname` | Mapped from changelog  
`name` | `event.idm.entity.entity.url` | Mapped from changelog  
`valid_from` | `event.idm.entity.entity.resource.attribute.labels` | Mapped from changelog  
`valid_until` | `event.idm.entity.entity.resource.attribute.labels` | Mapped from changelog  
`pattern_version` | `event.idm.entity.entity.resource.attribute.labels` | Mapped from changelog  
`observable.object.properties.value.condition` | `event.idm.entity.entity.asset.attribute.labels` | Mapped from changelog  
`handling.controlled_structure` | `event.idm.entity.entity.asset.attribute.labels` | Mapped from changelog  
`handling.marking_structures.color` | `event.idm.entity.entity.asset.attribute.labels` | Mapped from changelog  
`related_indicators.related_indicators` | `event.idm.entity.entity.asset.attribute.labels` | Mapped from changelog  
`related_indicators.scope` | `event.idm.entity.entity.asset.attribute.labels` | Mapped from changelog  
`indicator_types` | `event.idm.entity.entity.asset.attribute.labels` | Mapped from changelog  
`valid_time_positions` | `event.idm.entity.entity.asset.attribute.labels` | Mapped from changelog  
`observable.object.properties.custom_properties` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`observable.object.properties.value` | `event.ioc.domain_and_ports.domain` | Mapped from changelog  
`mitre-extension-definition.extension_type` | `entity.resource.attribute.labels.value` | Mapped from changelog  
`sco-extension-definition.extension_type` | `entity.resource.attribute.labels.value` | Mapped from changelog  
`x_ctix_confidence_score` | `threat_detail.confidence_score` | Mapped from changelog  
`modified` | `timestamp` | Mapped from changelog  
`valid_from` | `entity_event.metadata.interval.start_time` | Mapped from changelog  
`confidence` | `threat_detail.confidence_score` | Mapped from changelog  
`name` | `entity.entity.file.full_path` | Mapped from changelog  
`description` | `threat_detail.description` | Mapped from changelog  
`external_references.0.source_name` | `entity_event.entity.hostname` | Mapped from changelog  
`entity_type` | `IP_ADDRESS` | Mapped from changelog  
`entity_type` | `USER` | Mapped from changelog  
`entity_type` | `FILE` | Mapped from changelog  
`entity_type` | `DOMAIN_NAME` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/stix-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
