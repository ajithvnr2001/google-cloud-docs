---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-dra/
title: Collect Imperva Data Risk Analytics (DRA) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:38.903218+00:00
---

# Collect Imperva Data Risk Analytics (DRA) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/imperva-dra/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Imperva Data Risk Analytics (DRA) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Imperva DRA logs to Google Security Operations using the Bindplane agent.

The parser extracts fields from Imperva Data Risk Analytics syslog formatted logs. It uses grok and/or kv to parse the log message and then maps these values to the Unified Data Model (UDM). It also sets default metadata values for the event source and type. Imperva DRA helps uncover suspicious data activity and prioritize critical incidents among billions of audit events.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Imperva DRA management console



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
  2. Go to **SIEM Settings** > **Profile**.
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

For additional installation options, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

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
             customer_id: <CUSTOMER_ID>
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'IMPERVA_DRA'
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
     * Replace `<CUSTOMER_ID>` with the actual Customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: <CUSTOMER_ID>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'IMPERVA_DRA'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Syslog forwarding on Imperva DRA

  1. Sign in to the **Imperva DRA Management Console**.
  2. Go to **Configuration** > **SIEM Integration**.
  3. In the **Syslog Server** section, provide the following configuration details:

     * **Server IP** : Enter the Bindplane agent IP address.
     * **Port** : Enter the Bindplane agent port number (default 514).
     * **Protocol** : Select **UDP** or **TCP** , depending on your Bindplane agent configuration.
     * **Facility** : Select appropriate syslog facility (for example, **LOCAL0**).
  4. Click **Send Test Syslog Message** to verify connectivity.

  5. In the **Events to be sent** section, configure:

     * **Event Classes** : Select **Breach Detection** and/or **Risk Reduction** based on requirements.
     * **Notification Types** : Choose incident open/close/reopen actions and their severity levels.
     * **Message Format** : Select **JSON** for structured data format or **Raw** for basic syslog format.
  6. Configure **Severity Threshold** to determine which severity levels should be forwarded.

  7. Save the configuration.

**Note:** It is recommended not to send "Issues" notifications to SIEM systems due to their dynamic nature. Use only incident notifications for consistent SIEM integration.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`category_label` | `additional.fields` | Merged  
`clusterMemberNames_label` | `additional.fields` | Merged  
`clusterNames_label` | `additional.fields` | Merged  
`clusterNames_list` | `additional.fields` | Merged  
`dbName_list` | `additional.fields` | Merged  
`dbUser_list` | `additional.fields` | Merged  
`destHostname_list` | `additional.fields` | Merged  
`dstips_label` | `additional.fields` | Merged  
`fileExtension_list` | `additional.fields` | Merged  
`folder_list` | `additional.fields` | Merged  
`numOfAccessedObjects_label` | `additional.fields` | Merged  
`severity` | `additional.fields` | Mapped: `(?i)test-severity` → `severity_label`  
`severity_label` | `additional.fields` | Merged  
`sourceApps_list` | `additional.fields` | Merged  
`srcApp_list` | `additional.fields` | Merged  
`srcHostname_list` | `additional.fields` | Merged  
`srcUser_list` | `additional.fields` | Merged  
`suspiciousCommand_list` | `additional.fields` | Merged  
`tableName_list` | `additional.fields` | Merged  
`userAction_label` | `additional.fields` | Merged  
`hostname` | `intermediary.hostname` | Directly mapped  
`msg` | `metadata.description` | Directly mapped  
`event_timestamp` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss`  
`firstIncidentTime` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`lastIncidentTime` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`securityEventTimestamp` | `metadata.event_timestamp` | Parsed as `UNIX`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `RESOURCE_CREATION`, `true` → `USER_UNCATEGORIZED`, `true` → `NETWORK_CONNE...  
`type` | `metadata.product_event_type` | Directly mapped  
`data.id` | `metadata.product_log_id` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`sapp` | `principal.application` | Directly mapped  
`sourceApps` | `principal.application` | Directly mapped  
`srcApp` | `principal.application` | Directly mapped  
`shost` | `principal.asset.hostname` | Directly mapped  
`srcHosts` | `principal.asset.hostname` | Directly mapped  
`pri_ip` | `principal.asset.ip` | Merged  
`src` | `principal.asset.ip` | Merged  
`srcIp` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`src_ips` | `principal.asset.ip` | Merged  
`shost` | `principal.hostname` | Directly mapped  
`srcHosts` | `principal.hostname` | Directly mapped  
`pri_ip` | `principal.ip` | Merged  
`src` | `principal.ip` | Merged  
`srcIp` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`src_ips` | `principal.ip` | Merged  
`editUser` | `principal.user.userid` | Directly mapped  
`srcUser` | `principal.user.userid` | Directly mapped  
`srcUsers` | `principal.user.userid` | Directly mapped  
`suser` | `principal.user.userid` | Directly mapped  
`server_sec_res` | `security_result` | Merged  
`user_sec_res` | `security_result` | Merged  
`actionType` | `security_result.action_details` | Directly mapped  
`data.ruleComment` | `security_result.description` | Directly mapped  
`msg` | `security_result.description` | Directly mapped  
`act_label` | `security_result.detection_fields` | Merged  
`action_label` | `security_result.detection_fields` | Merged  
`cat_label` | `security_result.detection_fields` | Merged  
`dateEdited_label` | `security_result.detection_fields` | Merged  
`firstIncidentTime_label` | `security_result.detection_fields` | Merged  
`incidents_label` | `security_result.detection_fields` | Merged  
`lastIncidentTime_label` | `security_result.detection_fields` | Merged  
`num_of_Incidents_label` | `security_result.detection_fields` | Merged  
`data.ruleName` | `security_result.rule_name` | Directly mapped  
`severity` | `security_result.severity` | Mapped values (5 total, e.g. `(?i)Low` → `LOW`, `(?i)Medium` → `MEDIUM`, `(?i)High` → `HIGH`)  
`severityScore` | `security_result.severity_details` | Renamed/mapped  
`srcHost` | `src.asset.hostname` | Directly mapped  
`srcHost` | `src.asset.ip` | Mapped: `^(?:[0-9]{1,3}[.]){3}[0-9]{1,3}$` → `srcHost`  
`srcHost` | `src.hostname` | Directly mapped  
`srcHost` | `src.ip` | Mapped: `^(?:[0-9]{1,3}[.]){3}[0-9]{1,3}$` → `srcHost`  
`dhost` | `target.asset.hostname` | Directly mapped  
`dstHost` | `target.asset.hostname` | Directly mapped  
`dstHosts` | `target.asset.hostname` | Directly mapped  
`dest_ip` | `target.asset.ip` | Merged  
`dst` | `target.asset.ip` | Mapped: `^(?:[0-9]{1,3}[.]){3}[0-9]{1,3}$` → `dst`  
`dst_ip` | `target.asset.ip` | Merged  
`dst_ips` | `target.asset.ip` | Merged  
`tar_ip` | `target.asset.ip` | Merged  
`dhost` | `target.hostname` | Directly mapped  
`dstHost` | `target.hostname` | Directly mapped  
`dstHosts` | `target.hostname` | Directly mapped  
`dest_ip` | `target.ip` | Merged  
`dst` | `target.ip` | Mapped: `^(?:[0-9]{1,3}[.]){3}[0-9]{1,3}$` → `dst`  
`dst_ip` | `target.ip` | Merged  
`dst_ips` | `target.ip` | Merged  
`tar_ip` | `target.ip` | Merged  
`clusterName` | `target.resource.name` | Directly mapped  
`dest` | `target.resource.name` | Directly mapped  
`destination` | `target.resource.name` | Directly mapped  
`server.dbName` | `target.resource.name` | Directly mapped  
`destinationType` | `target.resource.resource_subtype` | Directly mapped  
`dstType` | `target.resource.resource_subtype` | Directly mapped  
`server.dbType` | `target.resource.resource_subtype` | Directly mapped  
`accessedTables` | `target.resource.type` | Directly mapped  
`url` | `target.url` | Directly mapped  
`acct` | `target.user.userid` | Directly mapped  
`destinationAccount` | `target.user.userid` | Directly mapped  
`server.dbUser` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `RESOURCE_CREATION`  
N/A | `metadata.product_name` | Constant: `Data Risk Analytics`  
N/A | `metadata.vendor_name` | Constant: `IMPERVA`  
N/A | `security_result.severity` | Constant: `LOW`  
`client_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`source_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`action_id` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`client_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`destination_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`destination_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`distinguished_name_device_id` | `event.idm.read_only_udm.principal.asset.asset_id` | Mapped from changelog  
`distinguished_name` | `event.idm.read_only_udm.principal.user.group_identifiers` | Mapped from changelog  
`distinguished_name_ou` | `event.idm.read_only_udm.principal.user.group_identifiers` | Mapped from changelog  
`distinguished_name_user` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`rule_name` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`packet_size` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`collective_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`collective_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`connection_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`entitlement_token_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`json_wrapper.appname` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`json_wrapper.facility` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`start` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`json_wrapper.priority` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`rule_subnet` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`srcHosts` | `event.idm.read_only_udm.src.ip` | Mapped from changelog  
`srcHosts` | `event.idm.read_only_udm.src.asset.ip` | Mapped from changelog  
`srcHosts` | `event.idm.read_only_udm.src.hostname` | Mapped from changelog  
`srcHosts` | `event.idm.read_only_udm.src.asset.hostname` | Mapped from changelog  
`dstHosts` | `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`srcUsers` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`srcIps` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`srcIps` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`srcHosts` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`srcHosts` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`sourceApps` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`dstIps` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`dstIps` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`dstHosts` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`destinationAccount` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`destination` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`destinationType` | `event.idm.read_only_udm.target.resource.resource_subtype` | Mapped from changelog  
`accessedTables` | `event.idm.read_only_udm.target.resource.type` | Mapped from changelog  
`securityEventTimestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`actionType` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`numOfAccessedObjects` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`userAction` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`clusterNames` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-dra-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
