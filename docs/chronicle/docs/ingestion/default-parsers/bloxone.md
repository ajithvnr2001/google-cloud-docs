---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bloxone/
title: Collect BloxOne Threat Defense logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:05.361389+00:00
---

# Collect BloxOne Threat Defense logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bloxone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect BloxOne Threat Defense logs

**Parser Version:** 8.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest BloxOne Threat Defense logs to Google Security Operations using the Bindplane agent.

Infoblox BloxOne Threat Defense is a cloud-managed DNS security service that generates syslog messages in CEF format for DNS queries, threat intelligence events, and policy actions. The parser normalizes fields and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Infoblox BloxOne platform
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Infoblox Portal



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
          chronicle/bloxone:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: BLOXONE
            raw_log_field: body
        
        service:
          pipelines:
            logs/bloxone_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/bloxone
        




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
          chronicle/bloxone:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: BLOXONE
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
             




## Configure syslog in Infoblox BloxOne

  1. Sign in to the **Infoblox Portal**.
  2. Go to **Configure > Administration > Data Connector**.
  3. Select the **Destination Configuration** tab.
  4. Click **Create > Syslog**.
  5. Provide the following configuration details: 
     * **Name** : Provide a descriptive name (for example, Google SecOps collector).
     * **Description** : Provide a brief description.
     * **State** : Select **Enable**.
     * **Tags** : Click **Add** and specify the following to associate a key with the destination: 
       * **KEY** : Enter a descriptive name for the key.
       * **VALUE** : Enter your value for the key.
     * **Format** : Select **CEF**.
     * **Protocol** : Select **UDP** or **TCP** (depending on your Bindplane agent configuration).
     * **FQDN/IP** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port (default is `514` for **UDP**).
  6. Click **Save & Close**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`additional_list.key` |  | This field is used in a loop to iterate over the `additional_list` array and extract data based on the value of the `key` field. It is not directly mapped to the UDM.  
`additional_list.value` | `principal.location.region_latitude`, `principal.location.region_longitude`, `target.location.region_latitude`, `target.location.region_longitude` | This field is used in conjunction with `additional_list.key` to extract specific values from the `additional_list` array. The logic for extracting and mapping the value depends on the corresponding `key`. For example:   
\- If `additional_list.key` is `intel:source:ip:geoIP:location`, extract latitude and longitude values using grok and map them to `principal.location.region_latitude` and `principal.location.region_longitude`, respectively.   
\- If `additional_list.key` is `intel:destination:ip:geoIP:location`, extract latitude and longitude values using grok and map them to `target.location.region_latitude` and `target.location.region_longitude`, respectively.  
`additional_string.key` |  | Similar to `additional_list.key`, this field is used in a loop to iterate over the `additional_string` array and extract data based on the `key` value. It is not directly mapped to the UDM.  
`additional_string.value` | `additional.fields.value.string_value`, `principal.location.country_or_region`, `target.location.country_or_region`, `src.ip`, `src.port`, `src.hostname`, `network.ip_protocol` | Used with `additional_string.key` to extract values from the `additional_string` array. The logic for mapping the value depends on the corresponding `key`. For example:   
\- If `additional_string.key` is `intel:source:ip:ip2asn:start_ip`, `intel:source:ip:ip2asn:finish_ip`, `intel:destination:ip:ip2asn:start_ip`, or `intel:destination:ip:ip2asn:finish_ip`, map the value to `additional.fields.value.string_value` with the corresponding key.   
\- If `additional_string.key` is `intel:source:ip:geoIP:country`, map the value to `principal.location.country_or_region`.   
\- If `additional_string.key` is `intel:destination:ip:geoIP:country`, map the value to `target.location.country_or_region`.   
\- If `additional_string.key` is `log:source:ip`, map the value to `src.ip`.   
\- If `additional_string.key` is `log:source:port`, map the value to `src.port` after converting it to an integer.   
\- If `additional_string.key` is `log:source:hostname`, map the value to `src.hostname`.   
\- If `additional_string.key` is `log:cdh:input:protocol`, map the value to `network.ip_protocol` after converting it to uppercase.  
`app_category` | `security_result.category_details` | Directly mapped.  
`confidence` | `security_result.confidence` | Mapped based on the following logic:  
\- If `confidence` is `LOW`, map to `LOW_CONFIDENCE`.  
\- If `confidence` is `MEDIUM`, map to `MEDIUM_CONFIDENCE`.  
\- If `confidence` is `HIGH`, map to `HIGH_CONFIDENCE`.  
`country` | `principal.location.name` | Directly mapped, but only if `raw.infobloxb1region` is empty.  
`device` | `principal.ip`, `principal.asset.ip` | Directly mapped, but only if `raw.dvc` is empty.  
`dhcp_fingerprint` | `security_result.detection_fields.value` | Directly mapped with the key `dhcp_fingerprint`.  
`dns_view` | `security_result.detection_fields.value` | Directly mapped with the key `dns_view`.  
`endpoint_groups` | `security_result.detection_fields.value` | Directly mapped with the key `endpoint_groups`.  
`event_time` | `metadata.event_timestamp.seconds` | Parsed as an ISO8601 timestamp and the seconds value is extracted. Used only if the `timestamp` field is empty.  
`feed_name` | `principal.resource.name` | `feed_name` is mapped to `principal.resource.name`.  
`feed_type` | `principal.resource.attribute.labels.value` | Directly mapped with the key `feed_type`.  
`mac_address` | `principal.mac` | Directly mapped after converting to lowercase.  
`network` | `principal.hostname`, `principal.asset.hostname` | Directly mapped, but only if both `raw.dvchost` and `raw.dvc` are empty.  
`os_version` | `principal.platform_version` | Directly mapped.  
`policy_action` | `security_result.action_details`, `security_result.action` | `policy_action` is directly mapped to `security_result.action_details`.  
`security_result.action` is derived based on the following logic:  
\- If `policy_action` is `Redirect` or `Log`, map to `ALLOW`.  
\- If `policy_action` is `BLOCK`, map to `BLOCK`.  
`policy_name` | `security_result.detection_fields.value` | Directly mapped with the key `policy_name`.  
`qname` | `network.dns.questions.name` | Directly mapped.  
`qtype` | `network.dns.questions.type` | Mapped based on the following logic:  
\- If `qtype` is `A`, map to 1 (converted to unsigned integer).  
\- If `qtype` is `PTR`, map to 12 (converted to unsigned integer).  
`raw.act` | `security_result.action_details` | Directly mapped.  
`raw.app` | `network.application_protocol` | Directly mapped after converting to uppercase.  
`raw.deviceeventclassid` | `metadata.product_event_type` | Concatenated with `raw.name` (separated by `-`) and mapped to `metadata.product_event_type`.  
`raw.devicevendor` | `metadata.vendor_name` | Directly mapped.  
`raw.deviceproduct` | `metadata.product_name` | Directly mapped.  
`raw.deviceversion` | `metadata.product_version` | Directly mapped.  
`raw.deviceseverity` | `security_result.severity_details`, `security_result.severity` | `raw.deviceseverity` is directly mapped to `security_result.severity_details`.  
`security_result.severity` is derived based on the following logic:  
\- If `raw.deviceseverity` is in [`0`, `1`, `2`, `3`], map to `LOW`.  
\- If `raw.deviceseverity` is in [`4`, `5`, `6`], map to `MEDIUM`.  
\- If `raw.deviceseverity` is in [`7`, `8`], map to `HIGH`.  
\- If `raw.deviceseverity` is in [`9`, `10`], map to `CRITICAL`.  
`raw.dvc` | `principal.ip`, `principal.asset.ip` | Directly mapped.  
`raw.dvchost` | `principal.hostname`, `principal.asset.hostname` | Directly mapped, but only if it's not equal to `raw.dvc`.  
`raw.infobloxb1connectiontype` | `additional.fields.value.string_value` | Directly mapped with the key `infobloxb1connectiontype`.  
`raw.infobloxb1ophname` | `observer.hostname`, `observer.asset.hostname` | Directly mapped.  
`raw.infobloxb1ophipaddress` | `observer.ip` | Directly mapped.  
`raw.infobloxb1policyname` | `security_result.detection_fields.value` | Directly mapped with the key `infobloxb1policyname`.  
`raw.infobloxdnsqclass` | `dns_question.class`, `dns_answer.class` | Used to derive `dns_question.class` and `dns_answer.class` based on a lookup table defined in the `dns_query_class_mapping.include` file.  
`raw.infobloxdnsqtype` | `dns_question.type`, `dns_answer.type` | Used to derive `dns_question.type` and `dns_answer.type` based on a lookup table defined in the `dns_record_type.include` file.  
`raw.infobloxdnsrcode` | `network.dns.response_code` | Used to derive `network.dns.response_code` based on a lookup table defined in the `dns_response_code.include` file.  
`raw.infobloxpolicyid` | `security_result.detection_fields.value` | Directly mapped with the key `infobloxpolicyid`.  
`raw.msg` | `metadata.description` | `raw.msg` is directly mapped to `metadata.description` after removing leading and trailing quotes.  
`raw.name` | `metadata.product_event_type` | Concatenated with `raw.deviceeventclassid` (separated by `-`) and mapped to `metadata.product_event_type`.  
`rcode` | `security_result.detection_fields.value`, `network.dns.response_code` | `rcode` is directly mapped to `security_result.detection_fields.value` with the key `rcode`.  
If `rcode` is `NXDOMAIN`, `network.dns.response_code` is set to 3 (converted to unsigned integer).  
`rdata` | `network.dns.answers.data` | Directly mapped.  
`rip` | `target.ip`, `target.asset.ip` | Directly mapped.  
`severity` | `security_result.severity` | Mapped based on the following logic:  
\- If `severity` is `INFO` (case-insensitive), map to `INFORMATIONAL`.  
\- If `severity` is `HIGH`, map to `HIGH`.  
`tclass` | `security_result.detection_fields.value` | Directly mapped with the key `tclass`.  
`threat_indicator` | `security_result.detection_fields.value` | Directly mapped with the key `threat_indicator`.  
`timestamp` | `metadata.event_timestamp.seconds` | Parsed as an ISO8601 timestamp and the seconds value is extracted.  
`user` | `principal.user.user_display_name` | Directly mapped.  
`user_groups` | `security_result.detection_fields.value` | Directly mapped with the key `user_groups`.  
N/A | `principal.resource.resource_subtype` | Set to `Feed` if `feed_name` is not empty.  
N/A | `metadata.log_type` | Set to `BLOXONE`.  
N/A | `additional.fields.key` | Set to `infobloxancount`, `infobloxarcount`, `infobloxb1connectiontype`, `infobloxnscount`, `intel:destination:ip:ip2asn:finish_ip`, `intel:destination:ip:ip2asn:start_ip`, `intel:source:ip:ip2asn:finish_ip`, or `intel:source:ip:ip2asn:start_ip` based on the corresponding `raw` fields.  
N/A | `metadata.event_type` | Set to `STATUS_UPDATE` if `has_principal` is `true`, otherwise set to `GENERIC_EVENT`.  
N/A | `network.dns.questions.type` | Set to 1 for `A` records and 12 for `PTR` records, converted to unsigned integer.  
N/A | `network.dns.answers.name`, `network.dns.answers.type`, `network.dns.answers.class` | Extracted from `raw.msg` by parsing the DNS response string.  
N/A | `intermediary.hostname`, `intermediary.ip`, `intermediary.asset.ip` | Extracted from `raw.msg` by parsing the DNS response string.  
`intermediaryhost` | `intermediary.hostname` | Mapped from changelog  
`app_name` | `principal.application` | Mapped from changelog  
`endpoint_groups", "user_groups", "dns_view", "dhcp_fingerprint", "policy_name", "tclass", "tproperty", "threat_indicator", "category", and "rcode` | `security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bloxone-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
