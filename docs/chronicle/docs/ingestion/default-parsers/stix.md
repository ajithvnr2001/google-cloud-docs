---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/stix/
title: Collect STIX Threat Intelligence logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:55:35.805866+00:00
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



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi&quot; /quiet
         

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
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                custom<er_id: '>;customer_id'
                endpoint: malachiteingestion-pa.googleapis.com
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
    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for the complete list
    * `STIX`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `stix_to_chronicle`: Descriptive name for the pipeline



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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
