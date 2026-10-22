---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-dlp/
title: Collect Symantec DLP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:28.324935+00:00
---

# Collect Symantec DLP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-dlp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Symantec DLP logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Symantec DLP logs to Google Security Operations using the Bindplane agent.

Symantec Data Loss Prevention (DLP) is a data protection solution that generates syslog messages for policy violations, data discovery incidents, endpoint monitoring events, and network monitoring alerts. The parser extracts fields from pipe-delimited and CEF-formatted syslog logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Symantec DLP server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Symantec Server administration console



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
          chronicle/symantec_dlp:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: SYMANTEC_DLP
            raw_log_field: body
        
        service:
          pipelines:
            logs/symantec_dlp_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/symantec_dlp
        




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
          chronicle/symantec_dlp:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: SYMANTEC_DLP
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
             




## Configure Symantec DLP

  1. Sign in to the **Symantec Server administration** console.
  2. Select **Manage > Policies > Response rules**.
  3. Select **Configure response rule** and enter a rule name.
  4. Provide the following details:

     * **Actions** : Select **Log to a syslog server**.
     * **Host** : Enter the Bindplane IP address.
     * **Port** : Enter the Bindplane port number.
     * **Message** : Enter the following syslog message template:
    
    |symcdlpsys|APPLICATION_NAME|$APPLICATION_NAME$|APPLICATION_USER|$APPLICATION_USER$|ATTACHMENT_FILENAME|$ATTACHMENT_FILENAME$|BLOCKED|$BLOCKED$|DATAOWNER_NAME|$DATAOWNER_NAME$|DATAOWNER_EMAIL|$DATAOWNER_EMAIL$|...
    

     * **Debugging** : Select **Level 4**.
  5. Click **Apply**.




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
act | security_result.action | If `act` is `Passed`, set to `ALLOW`. If `act` is `Modified`, set to `ALLOW_WITH_MODIFICATION`. If `act` is `Blocked`, set to `BLOCK`. Otherwise, set to `UNKNOWN_ACTION`.  
application_name | target.application | Directly mapped.  
asset_ip | principal.ip, principal.asset.ip | Directly mapped.  
asset_name | principal.hostname, principal.asset.hostname | Directly mapped.  
attachment_name | security_result.about.file.full_path | Directly mapped.  
blocked | security_result.action_details | Directly mapped.  
calling_station_id | principal.mac, principal.asset.mac | If `calling_station_id` is a MAC address, map it directly after replacing `-` with `:` and converting to lowercase.  
called_station_id | target.mac, target.asset.mac | If `called_station_id` is a MAC address, extract the MAC address part before the `:` and map it directly after replacing `-` with `:` and converting to lowercase.  
category1 | security_result.detection_fields | Create a label with key `category1` and value from `category1`.  
category2 | security_result.detection_fields | Create a label with key `category2` and value from `category2`.  
category3 | security_result.detection_fields | Create a label with key `category3` and value from `category3`.  
client_friendly_name | target.user.userid | Directly mapped.  
dataowner_mail | principal.user.email_addresses | Directly mapped if it's a valid email address.  
description | metadata.description | Directly mapped.  
dest_location | target.location.country_or_region | Directly mapped if it's not `RED`.  
deviceId | target.asset_id | Mapped as `ID:%{deviceId}`.  
device_version | metadata.product_version | Directly mapped.  
dhost | network.http.referral_url | Directly mapped.  
dlp_type | security_result.detection_fields | Create a label with key `dlp_type` and value from `dlp_type`.  
DLP_EP_Incident_ID | security_result.threat_id, security_result.detection_fields | Directly mapped to `threat_id`. Also, create a label with key `Incident ID` and value from `DLP_EP_Incident_ID`.  
domain | principal.administrative_domain | Directly mapped.  
dst | target.ip, target.asset.ip | Directly mapped if it's a valid IP address.  
endpoint_machine | target.ip, target.asset.ip | Directly mapped if it's a valid IP address.  
endpoint_user_department | target.user.department | Directly mapped.  
endpoint_user_email | target.user.email_addresses | Directly mapped.  
endpoint_user_manager | target.user.managers | Create a manager object with `user_display_name` from `endpoint_user_manager`.  
endpoint_user_name | target.user.user_display_name | Directly mapped.  
endpoint_user_title | target.user.title | Directly mapped.  
event_description | metadata.description | Directly mapped.  
event_id | metadata.product_log_id | Directly mapped.  
event_source | target.application | Directly mapped.  
event_timestamp | metadata.event_timestamp | Directly mapped.  
file_name | security_result.about.file.full_path | Directly mapped.  
filename | target.file.full_path, src.file.full_path | Directly mapped to `target.file.full_path`. If `has_principal` is true, also map to `src.file.full_path` and set `event_type` to `FILE_COPY`.  
host | src.hostname, principal.hostname, principal.asset.hostname | If `cef_data` contains `CEF`, map to all three fields. Otherwise, map to `principal.hostname` and `principal.asset.hostname`.  
incident_id | security_result.threat_id, security_result.detection_fields | Directly mapped to `threat_id`. Also, create a label with key `Incident ID` and value from `incident_id`.  
location | principal.resource.attribute.labels | Create a label with key `Location` and value from `location`.  
match_count | security_result.detection_fields | Create a label with key `Match Count` and value from `match_count`.  
monitor_name | additional.fields | Create a label with key `Monitor Name` and value from `monitor_name`.  
nas_id | target.hostname, target.asset.hostname | Directly mapped.  
occurred_on | principal.labels, additional.fields | Create a label with key `Occurred On` and value from `occurred_on` for both `principal.labels` and `additional.fields`.  
policy_name | sec_result.detection_fields | Create a label with key `policy_name` and value from `policy_name`.  
policy_rule | security_result.rule_name | Directly mapped.  
policy_severity | security_result.severity | Mapped to `severity` after converting to uppercase. If `policy_severity` is `INFO`, map it as `INFORMATIONAL`. If `policy_severity` is not one of `HIGH`, `MEDIUM`, `LOW`, or `INFORMATIONAL`, set `severity` to `UNKNOWN_SEVERITY`.  
policy_violated | security_result.summary | Directly mapped.  
Protocol | network.application_protocol, target.application, sec_result.description | If `Protocol` is not `FTP` or `Endpoint`, map it to `network.application_protocol` after parsing it using the `parse_app_protocol.include` file. If `Protocol` is `FTP`, map it to `target.application`. If `Protocol` is `Endpoint`, set `sec_result.description` to `Protocol=%{Protocol}`.  
recipient | target.user.email_addresses, about.user.email_addresses | For each email address in `recipient`, map it to both `target.user.email_addresses` and `about.user.email_addresses`.  
recipients | network.http.referral_url, target.resource.attribute.labels | Directly mapped to `network.http.referral_url`. Also, create a label with key `recipients` and value from `recipients`.  
reported_on | additional.fields | Create a label with key `Reported On` and value from `reported_on`.  
rules | security_result.detection_fields | Create a label with key `Rules` and value from `rules`.  
sender | network.email.from, target.resource.attribute.labels | If `sender` is a valid email address, map it to `network.email.from`. Also, create a label with key `sender` and value from `sender`.  
server | target.application | Directly mapped.  
Severity | security_result.severity | See `policy_severity` for mapping logic.  
src | principal.ip, principal.asset.ip | Directly mapped if it's a valid IP address.  
status | principal.labels, additional.fields | Create a label with key `Status` and value from `status` for both `principal.labels` and `additional.fields`.  
subject | target.resource.attribute.labels, network.email.subject | Create a label with key `subject` and value from `subject`. Also, map `subject` to `network.email.subject`.  
target_type | target.resource.attribute.labels | Create a label with key `Target Type` and value from `target_type`.  
timestamp | metadata.event_timestamp | Directly mapped after parsing it using the `date` filter.  
url | target.url | Directly mapped.  
user | target.user.userid | Directly mapped.  
user_id | principal.user.userid | Directly mapped.  
username | principal.user.userid | Directly mapped.  
N/A | metadata.product_name | Set to `SYMANTEC_DLP`.  
N/A | metadata.vendor_name | Set to `SYMANTEC`.  
N/A | metadata.event_type | If `event_type` is not empty, map it directly. Otherwise, if `host` is not empty and `has_principal` is true, set to `SCAN_NETWORK`. Otherwise, set to `GENERIC_EVENT`.  
N/A | metadata.product_event_type | If `policy_violated` contains `-NM-` or `data` contains `DLP NM`, set to `Network Monitor`. If `policy_violated` contains `-EP-` or `data` contains `DLP EP`, set to `Endpoint`.  
N/A | metadata.log_type | Set to `SYMANTEC_DLP`.  
`subject` | `event.idm.read_only_udm.network.email.subject` | Mapped from changelog  
`end` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`cnt` | `event.idm.read_only_udm.network.session_duration.seconds` | Mapped from changelog  
`resolution` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`dhost` | `event.idm.read_only_udm.target.user.email_addresses` | Mapped from changelog  
`ATTACHMENT_FILENAME` | `principal.file.full_path` | Mapped from changelog  
`DATAOWNER_NAME` | `principal.user.userid` | Mapped from changelog  
`ENDPOINT_USERNAME` | `principal.user.userid` | Mapped from changelog  
`reported_on" and "monitor_name` | `additional.fields` | Mapped from changelog  
`incident_id" and "DLP_EP_Incident_ID` | `security_result.detection_fields` | Mapped from changelog  
`application` | `principal.application` | Mapped from changelog  
`Occurred on` | `principal.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-dlp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
