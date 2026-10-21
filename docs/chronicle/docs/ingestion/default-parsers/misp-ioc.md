---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/misp-ioc/
title: Collect MISP IOC logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:05:49.061295+00:00
---

# Collect MISP IOC logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/misp-ioc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect MISP IOC logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest MISP (Malware Information Sharing Platform) IOC logs to Google Security Operations using Bindplane. The parser processes the data in both CSV and JSON formats. It extracts IOC attributes like IP addresses, domains, hashes, and URLs, mapping them to a unified data model (UDM) along with threat details like severity, confidence, and descriptions. The parser handles both single and multiple IOC entries within the input data, normalizing them into a consistent UDM output. 

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to your MISP server



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
  3. Copy and save the **Customer ID** from the **Organization details** section.



## Get MISP API credentials

  1. Sign in to your MISP web interface as an Administrator.
  2. Go to **Administration > List Auth Keys**.
  3. Click **Add authentication key**.
  4. Provide the following configuration details: 
     * **User** : Select the user account associated with the key.
     * Optional: **Allowed IPs** : Specify allowed IP addresses for the key.
     * **Expiration** : Leave empty for no expiration or set as needed.
  5. Click **Submit**.
  6. Copy and save the API key in a secure location.
  7. Click **I have noted down my key**.



## Configure MISP data export

  1. Install PyMISP on your MISP server:
         
         pip3 install pymisp
         

  2. Create the export directory:
         
         sudo mkdir -p /opt/misp/scripts
         sudo mkdir -p /opt/misp/ioc_export
         

  3. Create the credentials file `/opt/misp/scripts/keys.py`:
         
         misp_url = 'https://<MISP_SERVER_URL>'
         misp_key = '<MISP_API_KEY>'
         misp_verifycert = True
         misp_client_cert = ''
         

     * Replace `<MISP_SERVER_URL>` with your MISP server URL.
     * Replace `<MISP_API_KEY>` with the API key from the prerequisites.
  4. Create the export script `/opt/misp/scripts/misp_export.py`:
         
         #!/usr/bin/env python3
         # -*- coding: utf-8 -*-
         import argparse
         from pymisp import ExpandedPyMISP
         from keys import misp_url, misp_key, misp_verifycert
         
         if __name__ == '__main__':
             parser = argparse.ArgumentParser(description='Export MISP IOCs to CSV format.')
             parser.add_argument("--controller", default='attributes',
                                 help="Controller to use for search (events, objects, attributes)")
             parser.add_argument("--event_id",
                                 help="Event ID to fetch. Without it, fetches recent data.")
             parser.add_argument("--attributes", nargs='*',
                                 help="Requested attributes for CSV export")
             parser.add_argument("--misp_types", nargs='+',
                                 help="MISP types to fetch (ip-src, hostname, domain, etc.)")
             parser.add_argument("--context", action='store_true',
                                 help="Add event level context (tags, metadata)")
             parser.add_argument("--outfile", required=True,
                                 help="Output file to write the CSV data")
             parser.add_argument("--last", required=True,
                                 help="Time period: days (d), hours (h), minutes (m) - e.g., 1d, 12h, 30m")
         
             args = parser.parse_args()
         
             api = ExpandedPyMISP(misp_url, misp_key, misp_verifycert, debug=False)
         
             response = api.search(
                 controller=args.controller,
                 return_format='csv',
                 type_attribute=args.misp_types,
                 publish_timestamp=args.last,
                 include_context=args.context,
                 requested_attributes=args.attributes or None
             )
         
             with open(args.outfile, 'w') as response_file:
                 response_file.write(response)
         

  5. Make the script executable:
         
         sudo chmod +x /opt/misp/scripts/misp_export.py
         




## Schedule MISP data exports

  1. Create scheduled exports using crontab:
         
         sudo crontab -e
         

  2. Add the following cron entries:
         
         # Export different IOC types daily with context
         0 0 * * * python3 /opt/misp/scripts/misp_export.py --outfile /opt/misp/ioc_export/domains.csv --misp_types domain --last 1d --context --attributes uuid event_id category type value comment to_ids date attribute_tag event_info
         0 1 * * * python3 /opt/misp/scripts/misp_export.py --outfile /opt/misp/ioc_export/ip-src.csv --misp_types ip-src --last 1d --context --attributes uuid event_id category type value comment to_ids date attribute_tag event_info
         0 2 * * * python3 /opt/misp/scripts/misp_export.py --outfile /opt/misp/ioc_export/ip-dst.csv --misp_types ip-dst --last 1d --context --attributes uuid event_id category type value comment to_ids date attribute_tag event_info
         0 3 * * * python3 /opt/misp/scripts/misp_export.py --outfile /opt/misp/ioc_export/urls.csv --misp_types url --last 1d --context --attributes uuid event_id category type value comment to_ids date attribute_tag event_info
         0 4 * * * python3 /opt/misp/scripts/misp_export.py --outfile /opt/misp/ioc_export/sha256.csv --misp_types sha256 --last 1d --context --attributes uuid event_id category type value comment to_ids date attribute_tag event_info
         0 5 * * * python3 /opt/misp/scripts/misp_export.py --outfile /opt/misp/ioc_export/filenames.csv --misp_types filename --last 1d --context --attributes uuid event_id category type value comment to_ids date attribute_tag event_info
         0 6 * * * python3 /opt/misp/scripts/misp_export.py --outfile /opt/misp/ioc_export/registries.csv --misp_types regkey --last 1d --context --attributes uuid event_id category type value comment to_ids date attribute_tag event_info
         0 7 * * * python3 /opt/misp/scripts/misp_export.py --outfile /opt/misp/ioc_export/mutexes.csv --misp_types mutex --last 1d --context --attributes uuid event_id category type value comment to_ids date attribute_tag event_info
         

  3. Optionally, schedule a pull of feeds from MISP:
         
         23 0 * * * curl --insecure --header "Authorization: <MISP_API_KEY>" --header "Accept: application/json" --header "Content-Type: application/json" https://<MISP_SERVER_URL>/feeds/fetchFromAllFeeds
         




## Install the Bindplane agent

Install the Bindplane agent on your Linux operating system according to the following instructions.

### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-otel-collector/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

  * For additional installation options, consult the [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest MISP logs and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux.
     * Open the file using a text editor (for example, `nano`, `vi`).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           filelog:
             include:
               - "/opt/misp/ioc_export/*.csv"
         
         exporters:
           chronicle/chronicle_w_labels:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: <customer_id>
             endpoint: chronicle.googleapis.com
             # Set the log_type to ensure the correct parser is applied
             log_type: 'MISP_IOC'
             raw_log_field: body
             # You can optionally add other custom ingestion labels here if needed
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - filelog
               exporters:
                 - chronicle/chronicle_w_labels
         

     * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
     * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
     * Replace `<customer_id>` with the actual customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: <customer_id>
            endpoint: malachiteingestion-pa.googleapis.com
            # Set the log_type to ensure the correct parser is applied
            log_type: 'MISP_IOC'
            raw_log_field: body
            # You can optionally add other custom ingestion labels here if needed
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Linux** , run the following command:
        
        sudo systemctl restart observiq-otel-collector
        




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
Attribute.category | entity.metadata.threat.category_details | Direct mapping from the `category` field in the `Attribute` object.  
Attribute.comment | entity.metadata.threat.summary | Direct mapping from the `comment` field in the `Attribute` object.  
Attribute.deleted | entity.metadata.threat.detection_fields.value | Direct mapping from the `deleted` field in the `Attribute` object. The key is set to `Attribute deleted`.  
Attribute.event_id | entity.metadata.threat.detection_fields.value | Direct mapping from the `event_id` field in the `Attribute` object. The key is set to `Attribute event_id`.  
Attribute.first_seen | entity.metadata.threat.detection_fields.value | Direct mapping from the `first_seen` field in the `Attribute` object. The key is set to `Attribute first_seen`.  
Attribute.id | entity.metadata.threat.detection_fields.value | Direct mapping from the `id` field in the `Attribute` object. The key is set to `Attribute id` or `Attribute id $$` depending on the format of the raw log.  
Attribute.timestamp | entity.metadata.threat.detection_fields.value | Direct mapping from the `timestamp` field in the `Attribute` object. The key is set to `Attribute timestamp`.  
Attribute.to_ids | entity.metadata.threat.detection_fields.value | Direct mapping from the `to_ids` field in the `Attribute` object. The key is set to `Attribute to_ids`.  
Attribute.type | entity.metadata.threat.category_details | Direct mapping from the `type` field in the `Attribute` object.  
Attribute.type | log_type | Used to determine the type of IOC and map it to the appropriate UDM fields.  
Attribute.uuid | entity.metadata.product_entity_id | Direct mapping from the `uuid` field in the `Attribute` object.  
Attribute.value | entity.entity.file.full_path | Mapped if the `Attribute.type` is `filename`.  
Attribute.value | entity.entity.file.md5 | Mapped if the `Attribute.type` is `md5`.  
Attribute.value | entity.entity.file.sha1 | Mapped if the `Attribute.type` is `sha1`.  
Attribute.value | entity.entity.file.sha256 | Mapped if the `Attribute.type` is `sha256`.  
Attribute.value | entity.entity.hostname | Mapped if the `Attribute.type` is `domain`.  
Attribute.value | entity.entity.ip | Mapped if the `Attribute.type` is `ip-dst`, `ip-dst|port`, or `ip-src`. The value is extracted using a grok pattern.  
Attribute.value | entity.entity.resource.name | Mapped if the `Attribute.type` is `mutex`.  
Attribute.value | entity.entity.registry.registry_key | Mapped if the `Attribute.type` is `regkey`.  
Attribute.value | entity.entity.url | Mapped if the `Attribute.type` is `uri` or `URL`.  
column1 | entity.metadata.product_entity_id | Direct mapping from the first column in the CSV data.  
column14 | event_info | Used to append additional information to the `threat_sr.description` field.  
column16 | event_source_org | Direct mapping from the 16th column in the CSV data.  
column18 | threat_level | Direct mapping from the 18th column in the CSV data.  
column21 | description | Direct mapping from the 21st column in the CSV data.  
column3 | misp_category | Direct mapping from the third column in the CSV data.  
column4 | type | Direct mapping from the fourth column in the CSV data.  
column5 | value | Direct mapping from the fifth column in the CSV data.  
column6 | comment | Direct mapping from the sixth column in the CSV data.  
column8 | ts1 | Direct mapping from the eighth column in the CSV data.  
description | ioc.description | The value is generated by combining the `description` field with the `event_info` field, separated by `- additional info:`.  
description | entity.metadata.threat.description | Direct mapping from the `description` field.  
event_creator_email | entity.entity.labels.value | Direct mapping from the `event_creator_email` field. The key is set to `event_creator_email`.  
event_source_org | ioc.feed_name | Direct mapping from the `event_source_org` field.  
event_source_org | entity.metadata.threat.threat_feed_name | Direct mapping from the `event_source_org` field.  
Feed.publish | entity.metadata.threat.detection_fields.value | Direct mapping from the `publish` field in the `Feed` object. The key is set to `Feed publish`.  
first_seen | ioc.active_timerange.start | Direct mapping from the `first_seen` field. The value is parsed as a date.  
first_seen | entity.metadata.interval.start_time | Direct mapping from the `first_seen` field. The value is parsed as a date.  
info | entity.metadata.description | Direct mapping from the `info` field.  
last_seen | ioc.active_timerange.end | Direct mapping from the `last_seen` field. The value is parsed as a date.  
log.category | ioc.categorization | Direct mapping from the `category` field in the `log` object.  
log.category | entity.metadata.threat.category_details | Direct mapping from the `category` field in the `log` object.  
log.comment | entity.entity.file.full_path | Mapped if the `log.type` is `filename` and the `comment` field is not `Artifacts dropped`.  
log.comment | entity.metadata.threat.detection_fields.value | Direct mapping from the `comment` field in the `log` object. The key is set to `Attribute comment`.  
log.comment | entity.metadata.threat.summary | Direct mapping from the `comment` field in the `log` object.  
log.deleted | entity.metadata.threat.detection_fields.value | Direct mapping from the `deleted` field in the `log` object. The key is set to `Attribute deleted`.  
log.event_id | entity.metadata.threat.detection_fields.value | Direct mapping from the `event_id` field in the `log` object. The key is set to `Attribute event_id`.  
log.first_seen | entity.metadata.threat.detection_fields.value | Direct mapping from the `first_seen` field in the `log` object. The key is set to `Attribute first_seen`.  
log.id | entity.metadata.threat.detection_fields.value | Direct mapping from the `id` field in the `log` object. The key is set to `Attribute id`.  
log.timestamp | entity.metadata.threat.detection_fields.value | Direct mapping from the `timestamp` field in the `log` object. The key is set to `Attribute timestamp`.  
log.to_ids | entity.metadata.threat.detection_fields.value | Direct mapping from the `to_ids` field in the `log` object. The key is set to `Attribute to_ids`.  
log.type | ioc.categorization | Direct mapping from the `type` field in the `log` object.  
log.type | log_type | Used to determine the type of IOC and map it to the appropriate UDM fields.  
log.uuid | entity.metadata.product_entity_id | Direct mapping from the `uuid` field in the `log` object.  
log.value | entity.entity.file.full_path | Mapped if the `log.type` is `filename`.  
log.value | entity.entity.file.md5 | Mapped if the `log.type` is `md5`.  
log.value | entity.entity.file.sha1 | Mapped if the `log.type` is `sha1`.  
log.value | entity.entity.file.sha256 | Mapped if the `log.type` is `sha256`.  
log.value | entity.entity.hostname | Mapped if the `log.type` is `domain`.  
log.value | entity.entity.ip | Mapped if the `log.type` is `ip-dst`, `ip-dst|port`, or `ip-src`. The value is extracted using a grok pattern.  
log.value | entity.entity.resource.name | Mapped if the `log.type` is `mutex`.  
log.value | entity.entity.registry.registry_key | Mapped if the `log.type` is `regkey`.  
log.value | entity.entity.url | Mapped if the `log.type` is `uri` or `url`.  
log.value | ioc.domain_and_ports.domain | Mapped if the `log.type` is `domain`.  
log.value | entity.entity.user.email_addresses | Mapped if the `log.type` is `threat-actor`.  
misp_category | entity.metadata.threat.category_details | Direct mapping from the `misp_category` field.  
Org.name | entity.metadata.threat.detection_fields.value | Direct mapping from the `name` field in the `Org` object. The key is set to `Org name`.  
published | entity.metadata.threat.detection_fields.value | Direct mapping from the `published` field. The key is set to `published`.  
Tag.colour | entity.metadata.threat.detection_fields.value | Direct mapping from the `colour` field in the `Tag` object. The key is set to `tag colour`.  
Tag.exportable | entity.metadata.threat.detection_fields.value | Direct mapping from the `exportable` field in the `Tag` object. The key is set to `tag exportable`.  
Tag.hide_tag | entity.metadata.threat.detection_fields.value | Direct mapping from the `hide_tag` field in the `Tag` object. The key is set to `tag hide_tag`.  
Tag.id | entity.metadata.threat.detection_fields.value | Direct mapping from the `id` field in the `Tag` object. The key is set to `tag id`.  
Tag.is_custom_galaxy | entity.metadata.threat.detection_fields.value | Direct mapping from the `is_custom_galaxy` field in the `Tag` object. The key is set to `tag is_custom_galaxy`.  
Tag.is_galaxy | entity.metadata.threat.detection_fields.value | Direct mapping from the `is_galaxy` field in the `Tag` object. The key is set to `tag is_galaxy`.  
Tag.isinherited | entity.metadata.threat.detection_fields.value | Direct mapping from the `isinherited` field in the `Tag` object. The key is set to `tag isinherited`.  
Tag.name | entity.metadata.threat.detection_fields.value | Direct mapping from the `name` field in the `Tag` object. The key is set to `tag name`.  
Tag.numerical_value | entity.metadata.threat.detection_fields.value | Direct mapping from the `numerical_value` field in the `Tag` object. The key is set to `tag numerical_value`.  
Tag.user_id | entity.metadata.threat.detection_fields.value | Direct mapping from the `user_id` field in the `Tag` object. The key is set to `tag user_id`.  
threat_level | ioc.raw_severity | Direct mapping from the `threat_level` field.  
threat_level | entity.metadata.threat.severity_details | Direct mapping from the `threat_level` field.  
threat_level_id | entity.entity.labels.value | Direct mapping from the `threat_level_id` field. The key is set to `threat_level_id`.  
ts1 | ioc.active_timerange.start | Direct mapping from the `ts1` field. The value is parsed as a date.  
ts1 | entity.metadata.interval.start_time | Direct mapping from the `ts1` field. The value is parsed as a date.  
| entity.entity.file.full_path | Mapped if the `type` is `filename`.  
| entity.entity.file.md5 | Mapped if the `type` is `md5`.  
| entity.entity.file.sha1 | Mapped if the `type` is `sha1`.  
| entity.entity.file.sha256 | Mapped if the `type` is `sha256`.  
| entity.entity.hostname | Mapped if the `type` is `domain`.  
| entity.entity.ip | Mapped if the `type` is `ip-dst`, `ip-dst|port`, or `ip-src`. The value is extracted using a grok pattern.  
| entity.entity.port | Mapped if the `port` field is not empty. The value is converted to an integer.  
| entity.entity.resource.name | Mapped if the `type` is `mutex`.  
| entity.entity.resource.resource_subtype | Mapped if the `type` is `regkey`. The value is set to `regkey`.  
| entity.entity.resource.resource_type | Mapped if the `type` is `mutex` or `regkey`. The value is set to `MUTEX` or `STORAGE_OBJECT` respectively.  
| entity.entity.registry.registry_key | Mapped if the `type` is `regkey`.  
| entity.entity.url | Mapped if the `type` is `uri` or `url`.  
| entity.metadata.collected_timestamp | The value is set to the timestamp of the raw log entry.  
| entity.metadata.description | The value is set to the `type` field if the raw log is in CSV format. Otherwise, it's set to the `info` field.  
| entity.metadata.entity_type | The value is determined based on the `type` or `log_type` field. It can be `DOMAIN_NAME`, `FILE`, `IP_ADDRESS`, `MUTEX`, `RESOURCE`, or `URL`.  
| entity.metadata.interval.end_time | The value is set to a default value of 253402300799 seconds.  
| entity.metadata.interval.start_time | The value is set to the `first_seen` field if it's not empty. Otherwise, it's set to a default value of 1 second or the timestamp of the raw log entry.  
| entity.metadata.product_name | The value is set to `MISP`.  
| entity.metadata.threat.confidence | The value is set to `UNKNOWN_CONFIDENCE` if the `confidence` field is empty or `f`. Otherwise, it's set to `HIGH_CONFIDENCE`, `MEDIUM_CONFIDENCE`, or `LOW_CONFIDENCE` based on the value of the `confidence` field.  
| entity.metadata.threat.confidence_details | Direct mapping from the `confidence` field.  
| entity.metadata.threat.detection_fields | The value is a list of key-value pairs extracted from various fields in the raw log.  
| entity.metadata.vendor_name | The value is set to `MISP`.  
| ioc.active_timerange.end | The value is set to the `last_seen` field if it's not empty.  
| ioc.active_timerange.start | The value is set to the `ts1` or `first_seen` field if they are not empty. Otherwise, it's set to a default value of 1 second.  
| ioc.categorization | The value is set to `misp_category IOCs` if the raw log is in CSV format. Otherwise, it's set to the `category` field in the `Attribute` or `log` object.  
| ioc.confidence_score | Direct mapping from the `confidence` field.  
| ioc.description | The value is generated by combining the `description` field with the `event_info` field, separated by `- additional info:`.  
| ioc.domain_and_ports.domain | Mapped if the `type` or `log_type` is `domain`.  
| ioc.feed_name | The value is set to `MISP` if the `event_source_org` field is empty. Otherwise, it's set to the `event_source_org` field.  
| ioc.ip_and_ports.ip_address | Mapped if the `ip` field is not empty. The value is converted to an IP address.  
| ioc.ip_and_ports.ports | Mapped if the `port` field is not empty. The value is converted to an unsigned integer.  
| ioc.raw_severity | Direct mapping from the `threat_level` field.  
| timestamp | The value is set to the timestamp of the raw log entry.  
`column9` | `event.idm.read_only_udm.entity.labels` | Mapped from changelog  
`column11` | `event.idm.read_only_udm.entity.labels` | Mapped from changelog  
`column12` | `event.idm.read_only_udm.entity.labels` | Mapped from changelog  
`column13` | `event.idm.read_only_udm.entity.labels` | Mapped from changelog  
`"name"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"comment"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Attribute.last_seen"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"first_seen"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Org.id"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Org.uuid"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Org.local"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Orgc.id"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Orgc.uuid"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Orgc.local"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Attribute.distribution"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Attribute.interval_start"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Attribute.interval_end"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Attribute.sharing_group_id"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Attribute.disable_correlation"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Attribute.object_id"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Attribute.object_relation"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"log.id"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"log.event_id"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"log.distribution"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"interval_start"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"interval_end"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"template_uuid"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"meta-category"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"log.sharing_group_id"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"log.disable_correlation"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"log.object_id"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"log.object_relation"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Tag"` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`"Attribute.value"` | `event.idm.entity.entity.hostname` | Mapped from changelog  
`"Orgc.name"` | `event.idm.entity.entity.hostname` | Mapped from changelog  
`log.uuid` | `event.idm.entity.metadata.product_entity_id` | Mapped from changelog  
`Event.info` | `event.idm.entity.metadata.description` | Mapped from changelog  
`entity_first_seen` | `event.idm.entity.metadata.interval.start_time` | Mapped from changelog  
`log.category` | `event.idm.entity.metadata.threat.category_details` | Mapped from changelog  
`log.comment` | `event.idm.entity.metadata.threat.summary` | Mapped from changelog  
`Event.threat_level_id` | `event.idm.entity.entity.labels` | Mapped from changelog  
`event_creator_email` | `event.idm.entity.entity.labels` | Mapped from changelog  
`log.comment` | `event.idm.entity.entity.file.full_path` | Mapped from changelog  
`log.value` | `event.idm.entity.entity.file.full_path` | Mapped from changelog  
`file_name` | `event.idm.entity.entity.file.full_path` | Mapped from changelog  
`log.value` | `event.idm.entity.entity.file.sha256` | Mapped from changelog  
`file_sha256` | `event.idm.entity.entity.file.sha256` | Mapped from changelog  
`log.value` | `event.idm.entity.entity.file.sha1` | Mapped from changelog  
`log.value` | `event.idm.entity.entity.file.md5` | Mapped from changelog  
`log.value` | `event.idm.entity.entity.hostname` | Mapped from changelog  
`ip` | `event.idm.entity.entity.ip` | Mapped from changelog  
`port` | `event.idm.entity.entity.port` | Mapped from changelog  
`log.value` | `event.idm.entity.entity.resource.name` | Mapped from changelog  
`log.value` | `event.idm.entity.entity.registry.registry_key` | Mapped from changelog  
`log.value` | `event.idm.entity.entity.user.email_addresses` | Mapped from changelog  
`log.uuid` | `event.idm.entity.entity.user.user_display_name` | Mapped from changelog  
`log.value` | `event.idm.entity.entity.url` | Mapped from changelog  
`log.id` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`log.event_id` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`log.to_ids` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`log.timestamp` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`log.comment` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`log.deleted` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`log.first_seen` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`Org.name` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`Feed.publish` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`published` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`Event.Tag` | `event.idm.entity.metadata.threat.detection_fields` | Mapped from changelog  
`timestamp` | `event.idm.entity.metadata.entity_timestamp` | Mapped from changelog  
`indicator` | `event.idm.entity.entity.file.sha1` | Mapped from changelog  
`indicator` | `event.idm.entity.entity.file.md5` | Mapped from changelog  
`indicator` | `event.idm.entity.entity.file.sha256` | Mapped from changelog  
`indicator` | `event.idm.entity.entity.hostname` | Mapped from changelog  
`indicator` | `event.idm.entity.entity.ip` | Mapped from changelog  
`indicator` | `event.idm.entity.entity.url` | Mapped from changelog  
`confidence` | `event.idm.entity.metadata.threat.confidence_score` | Mapped from changelog  
`stix_package_title` | `event.idm.entity.metadata.threat.summary` | Mapped from changelog  
`type` | `event.idm.entity.metadata.threat.category_details` | Mapped from changelog  
`confidence` | `threat_.confidence_details` | Mapped from changelog  
`published", "Feed.publish", "Org.name", "Attribute.id", "Attribute.event_id", "Attribute.to_ids", "Attribute.timestamp", "Attribute.comment", "Attribute.deleted", "Attribute.first_seen", all "tag.names` | `threat.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/misp-ioc-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
