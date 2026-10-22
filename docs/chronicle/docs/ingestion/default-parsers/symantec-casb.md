---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-casb/
title: Collect Symantec CloudSOC CASB logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:42.264762+00:00
---

# Collect Symantec CloudSOC CASB logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-casb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Symantec CloudSOC CASB logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Symantec CloudSOC CASB logs to Google Security Operations using the Bindplane agent.

Symantec CloudSOC is a cloud access security broker (CASB) that generates syslog messages for cloud application activity, DLP policy violations, threat detections, content inspection results, and user access events. The parser extracts fields from JSON-formatted and syslog-formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Symantec CloudSOC host
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Symantec CloudSOC host



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
          chronicle/symantec_casb:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: SYMANTEC_CASB
            raw_log_field: body
        
        service:
          pipelines:
            logs/symantec_casb_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/symantec_casb
        




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
          chronicle/symantec_casb:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: SYMANTEC_CASB
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
             




## Configure syslog in Symantec CloudSOC CASB

  1. Sign in to your **Symantec CloudSOC** host.
  2. Run the following command to identify which logger the system uses:
         
         ls -d /etc/*syslog*
         

  3. Go to the corresponding section, according to the response:

     * **syslog.conf** : Legacy Syslog.
     * **syslog-ng.conf** : Syslog-ng.



### Legacy syslog configuration

  1. Open the `syslogd` file, typically located in `/etc/default` directory:
         
         vi /etc/default/syslogd
         

  2. Make sure `SYSLOGD` value contains the `-r` flag:
         
         SYSLOGD="-r"
         

  3. Save the file and exit the editor.

  4. Open `services` file, typically located in the `/etc` directory:
         
         vi /etc/services
         

  5. Edit the port value for syslog service:
         
         syslog          514/udp
         

  6. Save the file and exit the editor.

  7. Open the `syslog.conf` file, typically located in the `/etc` directory:
         
         vi /etc/syslog.conf
         

  8. Update the configuration to forward all logs to the Bindplane agent:
         
         *.* @<BINDPLANE_IP>
         

     * Replace `<BINDPLANE_IP>` with the Bindplane agent IP address.
  9. Open the `hosts` file, typically located in the `/etc` directory:
         
         vi /etc/hosts
         

  10. Create a local DNS entry for the Bindplane agent:
         
         <BINDPLANE_IP>    bindplane_agent_host
         

  11. Save the file and exit the editor.

  12. Restart the syslog daemon service.




### Syslog-ng configuration

  1. Open the `syslog-ng.conf` file, typically located in the `/etc` directory:
         
         vi /etc/syslog-ng.conf
         

  2. Add the following code to the end of the file:
         
         destination d_bindplane { udp("<BINDPLANE_IP>" port(514)); };
         log { source(s_src); destination(d_bindplane); };
         

     * Replace `<BINDPLANE_IP>` with the Bindplane agent IP address.
  3. Open the `hosts` file, typically located in the `/etc` directory:
         
         vi /etc/hosts
         

  4. Create a local DNS entry for the Bindplane agent:
         
         <BINDPLANE_IP>    bindplane_agent_host
         

  5. Save the file and exit the editor.

  6. Restart the syslog-ng daemon service.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`_domain` | `target.hostname` | The value of the `_domain` field  
`_domain` | `target.asset.hostname` | The value of the `_domain` field  
`_id` | `metadata.product_log_id` | The value of the `_id` field  
`actions_taken` | `security_result.detection_fields[].value` | The value of the `actions_taken` field. Key is dynamically generated as `Action_` \+ index.  
`activity_type` | `metadata.product_event_type` | The value of the `activity_type` field if `product_data.activity_type` is empty, or the value of `product_data.activity_type` if it's not empty.  
`collector_device_ip` | `principal.ip` | The value of the `collector_device_ip` field, if not `Unknown IP`.  
`collector_device_ip` | `principal.asset.ip` | The value of the `collector_device_ip` field, if not `Unknown IP`.  
`collector_device_name` | `principal.hostname` | The value of the `collector_device_name` field.  
`collector_device_name` | `principal.asset.hostname` | The value of the `collector_device_name` field.  
`content_checks.dlp.raw_response.contentdetails[].contentBlockId` | `security_result.detection_fields[].value` | The value of `content_checks.dlp.raw_response.contentdetails[].contentBlockId`. Key is dynamically generated as `contentBlockId_` \+ index.  
`content_checks.dlp.raw_response.contentdetails[].topLevelFileType` | `security_result.detection_fields[].value` | The value of `content_checks.dlp.raw_response.contentdetails[].topLevelFileType`. Key is dynamically generated as `topLevelFileType_` \+ index.  
`content_checks.dlp.raw_response.requestid` | `security_result.detection_fields[].value` | The value of `content_checks.dlp.raw_response.requestid`. Key is `Request ID`.  
`content_checks.dlp.raw_response.responseaction` | `security_result.detection_fields[].value` | The value of `content_checks.dlp.raw_response.responseaction`. Key is `Response Action`.  
`content_checks.dlp.raw_response.violation[].name` | `security_result.detection_fields[].value` | The value of `content_checks.dlp.raw_response.violation[].name`. Key is dynamically generated as `Violation_Policy_Name_` \+ index.  
`content_checks.dlp.raw_response.violation[].policyId` | `security_result.detection_fields[].value` | The value of `content_checks.dlp.raw_response.violation[].policyId`. Key is dynamically generated as `Violation_Policy_ID_` \+ index.  
`content_checks.dlp.updated_timestamp` | `additional.fields[].value.string_value` | The value of `content_checks.dlp.updated_timestamp`. Key is `Updated TimeStamp`.  
`content_checks.filename` | `target.file.full_path` | The value of `content_checks.filename`.  
`content_checks.mimetype` | `target.file.mime_type` | The value of `content_checks.mimetype`.  
`content_checks.risktype_list[]` | `security_result.detection_fields[].value` | The value of `content_checks.risktype_list[]`. Key is dynamically generated as `RiskType_` \+ index.  
`content_checks.vba_macros.expressions[].values[].key` | `security_result.detection_fields[].key` | The value of `content_checks.vba_macros.expressions[].values[].key` concatenated with indexes.  
`content_checks.vba_macros.expressions[].values[].value` | `security_result.detection_fields[].value` | The value of `content_checks.vba_macros.expressions[].values[].value`.  
`content_checks.vk_content_iq_violations[]` | `security_result.detection_fields[].value` | The value of `content_checks.vk_content_iq_violations[]`. Key is dynamically generated as `content_violation_` \+ index.  
`content_checks.vk_dlp_policy_violations[]` | `security_result.detection_fields[].value` | The value of `content_checks.vk_dlp_policy_violations[]`. Key is dynamically generated as `dlp_policy_violation_` \+ index.  
`content_checks.vk_encryption` | `security_result.detection_fields[].value` | The value of `content_checks.vk_encryption`. Key is `vk_encryption`.  
`content_checks.vk_glba` | `security_result.detection_fields[].value` | The value of `content_checks.vk_glba`. Key is `vk_glba`.  
`content_checks.vk_hipaa` | `security_result.detection_fields[].value` | The value of `content_checks.vk_hipaa`. Key is `vk_hipaa`.  
`content_checks.vk_pci` | `security_result.detection_fields[].value` | The value of `content_checks.vk_pci`. Key is `vk_pci`.  
`content_checks.vk_pii` | `security_result.detection_fields[].value` | The value of `content_checks.vk_pii`. Key is `vk_pii`.  
`content_checks.vk_source_code` | `security_result.detection_fields[].value` | The value of `content_checks.vk_source_code`. Key is `vk_source_code`.  
`content_checks.vk_vba_macros` | `security_result.detection_fields[].value` | The value of `content_checks.vk_vba_macros`. Key is `vk_vba_macros`.  
`content_checks.vk_virus` | `security_result.detection_fields[].value` | The value of `content_checks.vk_virus`. Key is `vk_virus`.  
`content_checks.violations` | `security_result.detection_fields[].value` | The value of `content_checks.violations`. Key is `violations`.  
`created_timestamp` | `additional.fields[].value.string_value` | The value of `created_timestamp`. Key is `Created TimeStamp`.  
`date` | `metadata.event_timestamp.seconds` | Epoch seconds extracted from the `date` field.  
`device_ip` | `target.ip` | The value of the `device_ip` field, if not `Unknown IP`.  
`device_ip` | `target.asset.ip` | The value of the `device_ip` field, if not `Unknown IP`.  
`file_size` | `target.file.size` | The value of `file_size` or `product_data.file_size` if the former is empty. Converted to unsigned integer.  
`file_url` | `target.file.full_path` | The value of `product_data.file_url`.  
`group_name` | `target.group.group_display_name` | The display name extracted from the `group_name` field.  
`hosts[]` | `principal.ip` | The values of the `hosts` field, split by comma.  
`inserted_timestamp` | `additional.fields[].value.string_value` | The value of `inserted_timestamp`. Key is `Inserted TimeStamp`.  
`instance` | `principal.hostname` | The first value of the `instance` field if it's an array, or the value of the `instance` field if it's a string.  
`instance` | `principal.asset.hostname` | The first value of the `instance` field if it's an array, or the value of the `instance` field if it's a string.  
`ioi_code` | `security_result.summary` | The value of the `ioi_code` field.  
`_latency` | `security_result.detection_fields[].value` | The value of the `_latency` field. Key is `Latency`.  
`locations` | `security_result.detection_fields[].value` | The value of the `locations` field. Key is `Locations`.  
`log_name` | `intermediary.asset.asset_id` | The log ID extracted from the `log_name` field, prefixed with `logid:`.  
`mailbox_owner` | `target.user.userid` | The value of `product_data.mailbox owner`.  
`metadata.log_type` | `metadata.log_type` | Hardcoded to `SYMANTEC_CASB`.  
`metadata.product_name` | `metadata.product_name` | Hardcoded to `SYMANTEC_CASB`.  
`metadata.vendor_name` | `metadata.vendor_name` | Hardcoded to `SYMANTEC`.  
`msg` | `metadata.description` | The value of the `msg` field or the `message` field if `msg` is not present.  
`name` | `security_result.detection_fields[].value` | The value of the `name` field. Key is `Name`.  
`object_name` | `security_result.detection_fields[].value` | The value of the `object_name` field. Key is `Object Name`.  
`object_type` | `target.resource.name` | The value of the `object_type` field.  
`org_unit` | `security_result.detection_fields[].value` | The value of the `org_unit` field. Key is `org_unit ID`.  
`policy_action` | `security_result.action_details` | The value of the `policy_action` field.  
`policy_type` | `security_result.detection_fields[].value` | The value of the `policy_type` field. Key is `policy_type`.  
`policy_violated` | `security_result.detection_fields[].value` | The value of the `policy_violated` field. Key is `policy_violated`.  
`product_data._domain` | `target.hostname` | The value of `product_data._domain`.  
`product_data._domain` | `target.asset.hostname` | The value of `product_data._domain`.  
`product_data.activity_type` | `metadata.product_event_type` | The value of `product_data.activity_type`.  
`product_data.file url` | `target.file.full_path` | The value of `product_data.file url`.  
`product_data.file_size` | `target.file.size` | The value of `product_data.file_size`.  
`product_data.group` | `target.group.group_display_name` | The value of `product_data.group`.  
`product_data.location` | `principal.location.country_or_region` | The value of `product_data.location`.  
`product_data.logon error` | `security_result.summary` | The value of `product_data.logon error`.  
`product_data.mailbox owner` | `target.user.userid` | The value of `product_data.mailbox owner`.  
`product_data.name` | `target.file.full_path` | The value of `product_data.name`.  
`product_data.object_name` | `target.file.full_path` | The value of `product_data.object_name`.  
`product_data.originatingserver` `product_data.service` | `target.application` | The value of `product_data.service`.  
`product_data.site url` | `target.url` | The value of `product_data.site url`.  
`product_data.target` | `target.user.userid` | The value of `product_data.target`.  
`product_data.useragent` | `network.http.user_agent` | The value of `product_data.useragent`.  
`product_name` | `intermediary.application` | The value of the `product_name` field.  
`product_uid` | `metadata.product_name` | The value of the `product_uid` field.  
`responsible_logs` | `additional.fields[].value.string_value` | The value of the `responsible_logs` field. Key is `responsible_logs`.  
`resource_id` | `target.resource.product_object_id` | The value of the `resource_id` field.  
`risks` | `security_result.detection_fields[].value` | The value of the `risks` field. Key is `Risks`.  
`security_result.action` | `security_result.action` | Derived from `product_data.logon error`. Set to `BLOCK` if `product_data.logon error` is `BlockedByConditionalAccess`.  
`security_result.severity` | `security_result.severity` | The uppercase value of the `severity` field, if it's one of the supported severity levels.  
`security_result.severity_details` | `security_result.severity_details` | The value of the `severity` field, if it's not one of the supported severity levels.  
`security_result.summary` | `security_result.summary` | The value of the `ioi_code` field or `product_data.logon error` if `ioi_code` is not present.  
`service` | `target.application` | The value of the `service` field if `product_data.service` is empty.  
`site_url` | `target.url` | The value of `product_data.site url`.  
`source` | `principal.resource.attribute.labels[].value` | The value of the `source` field. Key is `Source`.  
`sub_feature` | `additional.fields[].value.string_value` | The value of the `sub_feature` field. Key is `Sub Feature`.  
`target.application` | `target.application` | Derived based on `product_data.activity_type` and presence of principal and target.  
`target.resource.name` | `target.resource.name` | Derived based on `product_data.activity_type` and presence of principal and target.  
`threat_score` | `security_result.detection_fields[].value` | The value of the `threat_score` field. Key is `Threat Score`.  
`transaction_id` | `security_result.detection_fields[].value` | The value of the `transaction_id` field. Key is `Transaction ID`.  
`updated_timestamp` | `additional.fields[].value.string_value` | The value of `updated_timestamp` or `content_checks.dlp.updated_timestamp` if the former is empty. Key is `Updated TimeStamp`.  
`user` | `principal.user.userid` | The value of the `user` field.  
`user_email` | `target.user.userid` | The value of the `user_email` field.  
`user_mail` | `target.user.userid` | The value of the `user_mail` field extracted from the `msg` field.  
`user_name` | `principal.user.user_display_name` | The value of the `user_name` field.  
`user_uid` | `principal.user.userid` or `target.user.userid` | The value of the `user_uid` field. Mapped to `principal.user.userid` if `product_data.activity_type` is not `InvalidLogin` or `Login`, otherwise mapped to `target.user.userid`.  
`uuid` | `intermediary.asset.product_object_id` | The value of the `uuid` field.  
`version` | `metadata.product_version` | The value of the `version` field.  
`user", "user_mail", and "user_uid` | `principal.user.email_addresses` | Mapped from changelog  
`user_email", "mailbox_owner", "product_data.target", and "user_uid` | `target.user.email_addresses` | Mapped from changelog  
`__event_timestamp` | `metadata.event_timestamp` | Mapped from changelog  
`_elastic_timestamp", "created_timestamp", "inserted_timestamp", "updated_timestamp", "responsible_logs" and "sub_feature` | `additional.fields` | Mapped from changelog  
`threat_score", "locations", "transaction_id", "content_checks.dlp.raw_response.requestid", "content_checks.dlp.raw_response.responseaction", "org_unit", "policy_type", "content_checks.vk_pci", "content_checks.vk_vba_macros", "content_checks.vk_glba", "content_checks.vk_source_code", "content_checks.vk_pii", "content_checks.vk_virus", "content_checks.vk_hipaa", "content_checks.violations", "object_name", "multi_user", "risks", "name", "_latency", "content_checks.dlp.raw_response.warning", "content_checks.dlp.raw_response.violation", "content_checks.dlp.raw_response.contentdetails", "content_checks.vk_dlp_policy_violations", "content_checks.risktype_list", "content_checks.vk_content_iq_violations", "actions_taken", "__detect_source", "multi_facility", "content_checks.vba_macros.expressions" and "policy_violated` | `security_result.detection_fields` | Mapped from changelog  
`resource_id` | `target.resource.id` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-casb-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
