---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-harmony/
title: Collect Check Point Harmony logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:58.181598+00:00
---

# Collect Check Point Harmony logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-harmony/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Check Point Harmony logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Check Point Harmony Email and Collaboration (HEC) logs to Google Security Operations using Bindplane. This parser code extracts key-value pairs from Check Point Harmony syslog messages and maps them to a Unified Data Model (UDM). It first normalizes the message format, then iteratively parses and maps fields to UDM categories like `principal`, `target`, `network`, and `security_result`, enriching the data for security analysis.

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance
  * Windows 2016 or later, or a Linux host with `systemd`
  * If running behind a proxy, firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open
  * Privileged access to Check Point Harmony HEC (Infinity Portal)



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



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, consult the [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file: 
     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
             udplog:
                 # Replace the port and IP address as required
                 listen_address: "0.0.0.0:514"
         
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
                 # Add optional ingestion labels for better organization
                 log_type: 'CHECKPOINT_HARMONY'
                 raw_log_field: body
                 ingestion_labels:
         
         service:
             pipelines:
                 logs/source0__chronicle_w_labels-0:
                     receivers:
                         - udplog
                     exporters:
                         - chronicle/chronicle_w_labels
         

     * Replace the port and IP address as required in your infrastructure.
     * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
     * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
     * Replace `<customer_id>` with the actual customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the path where the service account key file (Option 1) was saved in the Get Google SecOps credentials for the Bindplane agent section.



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
                # Add optional ingestion labels for better organization
                log_type: 'CHECKPOINT_HARMONY'
                raw_log_field: body
                ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Linux** , run the following command:
        
        sudo systemctl restart bindplane-agent
        

  * To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
        
        net stop BindPlaneAgent && net start BindPlaneAgent
        




## Configure Syslog for Check Point Harmony HEC

  1. Sign in to the **Infinity Portal > Harmony Email & Collaboration** web UI.
  2. Go to **Settings > Monitoring > SIEM**.
  3. Click **Add SIEM Server**.
  4. Provide the following configuration details: 
     * Host: Enter the Bindplane agent IP address.
     * Port: Enter the Bindplane agent port number.
     * Protocol: Select **UDP**.
     * (Optional) Token: Enter an optional tag to the logs.
  5. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
action | security_result.action_details | Directly mapped.  
| security_result.action | Mapped to ALLOW, BLOCK, ALLOW_WITH_MODIFICATION, or QUARANTINE based on the value of the action field.  
additional_info | additional.fields.value.string_value | Directly mapped with key = `additional_info`.  
analyzed_on | security_result.detection_fields.value | Directly mapped with key = `analyzed_on`.  
client_name | additional.fields.value.string_value | Directly mapped with key = `client_name`.  
client_version | intermediary.platform_version | Directly mapped.  
confidence_level | security_result.detection_fields.value | Directly mapped with key = `confidence_level`.  
| security_result.confidence | Mapped to UNKNOWN_CONFIDENCE, LOW_CONFIDENCE, MEDIUM_CONFIDENCE, or HIGH_CONFIDENCE based on the value of the confidence_level field.  
description | security_result.description | Directly mapped.  
dst | target.ip | Directly mapped.  
dst_dns_name | security_result.detection_fields.value | Directly mapped with key = `dst_dns_name`.  
dst_machine_name | security_result.detection_fields.value | Directly mapped with key = `dst_machine_name`.  
| target.asset.hostname | Directly mapped.  
| target.hostname | Directly mapped.  
dst_user_dn | security_result.detection_fields.value | Directly mapped with key = `dst_user_dn`.  
dst_user_name | target.user.userid | Directly mapped.  
ep_rule_id | security_result.rule_id | Directly mapped if rule_uid is empty.  
errors | security_result.summary | Directly mapped.  
event_type | metadata.product_event_type | Directly mapped.  
file_md5 | target.process.file.md5 | Directly mapped if the value is a valid MD5 hash and not all zeros.  
| target.file.md5 | Directly mapped if the value is a valid MD5 hash and not all zeros.  
file_name | target.process.file.full_path | Directly mapped.  
file_sha1 | target.process.file.sha1 | Directly mapped if the value is a valid SHA-1 hash and not all zeros.  
| target.file.sha1 | Directly mapped if the value is a valid SHA-1 hash and not all zeros.  
file_sha256 | target.process.file.sha256 | Directly mapped if the value is a valid SHA256 hash and not all zeros.  
| target.file.sha256 | Directly mapped if the value is a valid SHA256 hash and not all zeros.  
file_size | target.file.size | Directly mapped.  
file_type | target.file.file_type | Mapped to FILE_TYPE_ZIP, FILE_TYPE_DOS_EXE, FILE_TYPE_PDF, or FILE_TYPE_XLSX based on the value of the file_type field.  
flags | additional.fields.value.string_value | Directly mapped with key = `flags`.  
fw_subproduct | additional.fields.value.string_value | Directly mapped with key = `fw_subproduct` if product is empty.  
| metadata.product_name | Directly mapped if product is empty.  
host_type | security_result.detection_fields.value | Directly mapped with key = `host_type`.  
ifdir | network.direction | Directly mapped after converting to uppercase.  
ifname | security_result.detection_fields.value | Directly mapped with key = `ifname`.  
installed_products | security_result.detection_fields.value | Directly mapped with key = `installed_products`.  
is_scanned | security_result.detection_fields.value | Directly mapped with key = `is_scanned`.  
layer_name | security_result.detection_fields.value | Directly mapped with key = `layer_name`.  
| security_result.rule_set_display_name | Directly mapped.  
layer_uuid | security_result.detection_fields.value | Directly mapped with key = `layer_uuid`.  
| security_result.rule_set | Directly mapped.  
loguid | metadata.product_log_id | Directly mapped.  
machine_guid | principal.asset.attribute.labels.value | Directly mapped with key = `machine_guid`.  
malware_action | security_result.detection_fields.value | Directly mapped with key = `malware_action`.  
malware_family | security_result.detection_fields.value | Directly mapped with key = `malware_family`.  
media_authorized | security_result.detection_fields.value | Directly mapped with key = `media_authorized`.  
media_class_id | security_result.detection_fields.value | Directly mapped with key = `media_class_id`.  
media_description | security_result.detection_fields.value | Directly mapped with key = `media_description`.  
media_encrypted | security_result.detection_fields.value | Directly mapped with key = `media_encrypted`.  
media_manufacturer | security_result.detection_fields.value | Directly mapped with key = `media_manufacturer`.  
media_type | security_result.detection_fields.value | Directly mapped with key = `media_type`.  
methods | security_result.detection_fields.value | Directly mapped with key = `methods`.  
originsicname | security_result.detection_fields.value | Directly mapped with key = `originsicname`.  
origin | intermediary.ip | Directly mapped.  
os_version | principal.asset.platform_software.platform_patch_level | Directly mapped.  
outzone | security_result.detection_fields.value | Directly mapped with key = `outzone`.  
parent_rule | security_result.detection_fields.value | Directly mapped with key = `parent_rule`.  
peer_gateway | intermediary.ip | Directly mapped.  
policy_guid | security_result.detection_fields.value | Directly mapped with key = `policy_guid`.  
policy_name | security_result.detection_fields.value | Directly mapped with key = `policy_name`.  
policy_number | security_result.detection_fields.value | Directly mapped with key = `policy_number`.  
policy_type | security_result.detection_fields.value | Directly mapped with key = `policy_type`.  
product | additional.fields.value.string_value | Directly mapped with key = `product`.  
| metadata.product_name | Directly mapped.  
product_family | additional.fields.value.string_value | Directly mapped with key = `product_family`.  
program_name | additional.fields.value.string_value | Directly mapped with key = `program_name`.  
protection_name | security_result.detection_fields.value | Directly mapped with key = `protection_name`.  
protection_type | security_result.detection_fields.value | Directly mapped with key = `protection_type`.  
reading_data_access | security_result.detection_fields.value | Directly mapped with key = `reading_data_access`.  
rule_action | security_result.detection_fields.value | Directly mapped with key = `rule_action`.  
rule_name | security_result.rule_name | Directly mapped.  
rule_uid | security_result.rule_id | Directly mapped if ep_rule_id is empty.  
s_port | principal.port | Directly mapped.  
scheme | security_result.detection_fields.value | Directly mapped with key = `scheme`.  
sequencenum | additional.fields.value.string_value | Directly mapped with key = `sequencenum`.  
service | target.port | Directly mapped.  
service_id | security_result.detection_fields.value | Directly mapped with key = `service_id`.  
session_uid | network.session_id | Directly mapped.  
src | principal.ip | Directly mapped.  
src_dns_name | security_result.detection_fields.value | Directly mapped with key = `src_dns_name`.  
src_machine_name | security_result.detection_fields.value | Directly mapped with key = `src_machine_name`.  
| principal.asset.hostname | Directly mapped.  
| principal.hostname | Directly mapped.  
src_user_dn | security_result.detection_fields.value | Directly mapped with key = `src_user_dn`.  
src_user_name | principal.user.userid | Directly mapped.  
| principal.user.email_addresses | The email address is extracted from the src_user_name field if it exists and is in the format `userid (email)`.  
te_verdict_determined_by | security_result.detection_fields.value | Directly mapped with key = `te_verdict_determined_by`.  
timestamp | metadata.event_timestamp | Directly mapped.  
trusted_domain | security_result.detection_fields.value | Directly mapped with key = `trusted_domain`.  
user | principal.user.userid | Directly mapped if src_user_name is empty.  
| principal.user.email_addresses | The email address is extracted from the user field if it exists and is in the format `userid (email)`.  
user_name | principal.user.email_addresses | Directly mapped if the value is a valid email address.  
user_sid | principal.user.windows_sid | Directly mapped.  
verdict | security_result.detection_fields.value | Directly mapped with key = `verdict`.  
version | additional.fields.value.string_value | Directly mapped with key = `version`.  
vpn_feature_name | security_result.detection_fields.value | Directly mapped with key = `vpn_feature_name`.  
web_client_type | security_result.detection_fields.value | Directly mapped with key = `web_client_type`.  
| metadata.log_type | This field is hardcoded to `CHECKPOINT_HARMONY`.  
| metadata.vendor_name | This field is hardcoded to `CHECKPOINT_HARMONY`.  
| principal.asset.platform_software.platform | Mapped to WINDOWS, MAC, or LINUX based on the value of the os_name field.  
| network.ip_protocol | Mapped to TCP, UDP, ICMP, IP6IN4, or GRE based on the value of the proto field and other fields like service and service_id.  
| security_result.severity | Mapped to LOW, MEDIUM, HIGH, or CRITICAL based on the value of the severity field.  
| metadata.event_type | This field is set to `NETWORK_CONNECTION` if both principal and target are present, `STATUS_UNCATEGORIZED` if only principal is present, and `GENERIC_EVENT` otherwise.  
`label` | `event.idm.read_only_udm.network.email.to` | Mapped from changelog  
`entityLink` | `event.idm.read_only_udm.metadata.url_back_to_product` | Mapped from changelog  
`actionType` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`eventId` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`eventCreated` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`act.createTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`act.relatedEntityId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`customerId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`saas` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`state` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`entityId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`connectivity_state` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`actions.actionType` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`senderAddress` | `event.idm.read_only_udm.network.email.from` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-harmony-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
