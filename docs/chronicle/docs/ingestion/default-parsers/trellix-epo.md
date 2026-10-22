---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-epo/
title: Collect Trellix EPO logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:55.546074+00:00
---

# Collect Trellix EPO logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trellix-epo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trellix EPO logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Trellix ePO logs to Google Security Operations using the Bindplane agent.

Trellix ePO (formerly McAfee ePolicy Orchestrator) is a centralized security management platform that provides unified policy enforcement, real-time visibility, and automated compliance across endpoint security products. It allows administrators to manage security policies, deploy agents, monitor threats, and generate reports from a single web-based console.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Trellix ePO console with administrator privileges



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

### Windows Installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux Installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional Installation Resources

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane Agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           tcplog:
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
             customer_id: YOUR_CUSTOMER_ID_HERE
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'MCAFEE_EPO'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/chronicle_w_labels
         

     * Replace the port and IP address as required in your infrastructure.
     * Replace `YOUR_CUSTOMER_ID_HERE` with the actual Customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.
     * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
     * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: YOUR_CUSTOMER_ID_HERE
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'MCAFEE_EPO'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart Bindplane Agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Trellix ePO syslog forwarding

  1. Sign in to the **Trellix ePO** console with administrator credentials.
  2. Go to **Menu > Configuration > Registered Servers**.
  3. Click **New Server**.
  4. In the **Server type** drop-down list, select **Syslog**.
  5. In the **Name** field, enter a descriptive name (for example, `Chronicle-Bindplane`).
  6. Click **Next**.
  7. In the **Syslog Server** field, enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
  8. In the **Port** field, enter `514` (or the port configured in Bindplane).
  9. In the **Protocol** drop-down list, select **TCP**.
  10. In the **Event format** drop-down list, select **Common Event Format (CEF)**.
  11. Click **Test Connection** to verify connectivity to the Bindplane agent.
  12. Click **Save**.
  13. Go to **Menu > Automation > Automatic Responses**.
  14. Click **New Response** to create a new automatic response rule.
  15. In the **Name** field, enter a descriptive name (for example, `Syslog-Chronicle`).
  16. In the **Event Group** drop-down list, select the event groups to forward: 
     * **ePO Notification Events**
     * **Threat Events**
     * **Client Events**
  17. Click **Next**.
  18. In the **Filter** tab, configure any event filters as needed (or leave defaults to forward all events).
  19. Click **Next**.
  20. In the **Actions** section, select **Send Syslog**.
  21. In the **Syslog Server** drop-down list, select the registered syslog server (`Chronicle-Bindplane`).
  22. Click **Next**.
  23. Review the configuration and click **Save**.

**Note:** For more information, see the [Trellix ePO product documentation](https://docs.trellix.com/bundle/epolicy-orchestrator-on-prem-5.10.0-product-guide/page/GUID-5C5332B3-837A-4DDA-BE5C-1513A230E474.html).



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`about_token` | `about` | Merged  
`additional_token` | `additional` | Renamed/mapped  
`ActionID_label` | `additional.fields` | Merged  
`BadLinkRatingID_label` | `additional.fields` | Merged  
`ContentID_label` | `additional.fields` | Merged  
`DownloadRatingID_label` | `additional.fields` | Merged  
`Error_label` | `additional.fields` | Merged  
`ExploitRatingID_label` | `additional.fields` | Merged  
`InitiatorID_label` | `additional.fields` | Merged  
`InitiatorType_label` | `additional.fields` | Merged  
`ListID_label` | `additional.fields` | Merged  
`Locale_label` | `additional.fields` | Merged  
`PhishingRatingID_label` | `additional.fields` | Merged  
`PopupRatingID_label` | `additional.fields` | Merged  
`ProductID_label` | `additional.fields` | Merged  
`RatingID_label` | `additional.fields` | Merged  
`ReasonID_label` | `additional.fields` | Merged  
`SiteName_label` | `additional.fields` | Merged  
`SourceProcessSigned_label` | `additional.fields` | Merged  
`SourceProcessSigner_label` | `additional.fields` | Merged  
`SpamRatingID_label` | `additional.fields` | Merged  
`TargetDriveType_label` | `additional.fields` | Merged  
`_field` | `additional.fields` | Merged  
`analyzer_engine_version_label` | `additional.fields` | Merged  
`analyzer_ipv4_label` | `additional.fields` | Merged  
`analyzer_label` | `additional.fields` | Merged  
`analyzer_name_label` | `additional.fields` | Merged  
`analyzerengineversion_label` | `additional.fields` | Merged  
`bps_id_label` | `additional.fields` | Merged  
`client_labels_` | `additional.fields` | Merged  
`description_value_label` | `additional.fields` | Merged  
`detected_utc_label` | `additional.fields` | Merged  
`eventType_label` | `additional.fields` | Merged  
`event_version_label` | `additional.fields` | Merged  
`extradatnames_label` | `additional.fields` | Merged  
`machine_agent_version_label` | `additional.fields` | Merged  
`opg_data_label` | `additional.fields` | Merged  
`product_family_label` | `additional.fields` | Merged  
`product_name_label` | `additional.fields` | Merged  
`server_list_labels` | `additional.fields` | Merged  
`source_ipv4_label` | `additional.fields` | Merged  
`sphotfix_label` | `additional.fields` | Merged  
`target_protocol_label` | `additional.fields` | Merged  
`targetprotocol_label` | `additional.fields` | Merged  
`tenant_guid_label` | `additional.fields` | Merged  
`tenant_id_label` | `additional.fields` | Merged  
`tenant_node_path_label` | `additional.fields` | Merged  
`threat_action_taken_label` | `additional.fields` | Merged  
`time_s_zone_label` | `additional.fields` | Merged  
`timezone_bias_label` | `additional.fields` | Merged  
`type_label` | `additional.fields` | Merged  
`user_info_label` | `additional.fields` | Merged  
`verbuild_label` | `additional.fields` | Merged  
`vermin_label` | `additional.fields` | Merged  
`vermjr_label` | `additional.fields` | Merged  
`verrev_label` | `additional.fields` | Merged  
`workflowid_label` | `additional.fields` | Merged  
`intermediary` | `intermediary` | Merged  
`intermediary1` | `intermediary` | Merged  
`Analyzer` | `intermediary.application` | Directly mapped  
`analyzer` | `intermediary.application` | Directly mapped  
`AnalyzerHostName` | `intermediary.asset.hostname` | Directly mapped  
`AnalyzerMAC` | `intermediary.asset.mac` | Merged  
`AnalyzerHostName` | `intermediary.hostname` | Directly mapped  
`analyzerhostname` | `intermediary.hostname` | Directly mapped  
`analyzeripv4` | `intermediary.ip` | Merged  
`AnalyzerMAC` | `intermediary.mac` | Merged  
`analyzermac` | `intermediary.mac` | Merged  
`Name` | `metadata.description` | Directly mapped  
`event_description` | `metadata.description` | Directly mapped  
`eventname` | `metadata.description` | Directly mapped  
`scantype` | `metadata.description` | Directly mapped  
`tvdeventid` | `metadata.description` | Directly mapped  
`event_type` | `metadata.event_type` | Directly mapped  
`TenantId` | `metadata.product_deployment_id` | Directly mapped  
`EventID` | `metadata.product_event_type` | Directly mapped  
`Type` | `metadata.product_event_type` | Directly mapped  
`eventType` | `metadata.product_event_type` | Directly mapped  
`prod_event_type` | `metadata.product_event_type` | Directly mapped  
`product_event_type` | `metadata.product_event_type` | Renamed/mapped  
`tvdeventid` | `metadata.product_event_type` | Directly mapped  
`AutoID` | `metadata.product_log_id` | Directly mapped  
`AutoId` | `metadata.product_log_id` | Directly mapped  
`alertId` | `metadata.product_log_id` | Directly mapped  
`autoid` | `metadata.product_log_id` | Directly mapped  
`product_log_id` | `metadata.product_log_id` | Renamed/mapped  
`analyzername` | `metadata.product_name` | Directly mapped  
`product_name` | `metadata.product_name` | Directly mapped  
`AnalyzerVersion` | `metadata.product_version` | Directly mapped  
`analyzerversion` | `metadata.product_version` | Directly mapped  
`product_version` | `metadata.product_version` | Directly mapped  
`productversion` | `metadata.product_version` | Directly mapped  
`app_protocol` | `network.application_protocol` | Directly mapped  
`target_protocol` | `network.ip_protocol` | Directly mapped  
`sys_ip` | `observer.ip` | Merged  
`analyzer_name` | `observer.namespace` | Directly mapped  
`principal_token` | `principal` | Renamed/mapped  
`source_user_domain` | `principal.administrative_domain` | Directly mapped  
`application_name` | `principal.application` | Directly mapped  
`host` | `principal.application` | Directly mapped  
`process_name` | `principal.application` | Directly mapped  
`source_process_name` | `principal.application` | Directly mapped  
`agentguid` | `principal.asset.asset_id` | Directly mapped  
`token_new` | `principal.asset.attribute.labels` | Merged  
`SiteName` | `principal.asset.hostname` | Directly mapped  
`SourceHostName` | `principal.asset.hostname` | Directly mapped  
`host` | `principal.asset.hostname` | Directly mapped  
`principal_hostname` | `principal.asset.hostname` | Directly mapped  
`source` | `principal.asset.hostname` | Directly mapped  
`machine_ip_address` | `principal.asset.ip` | Merged  
`sourceIP` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`SourceMAC` | `principal.asset.mac` | Merged  
`machine_raw_mac_address` | `principal.asset.mac` | Merged  
`AutoGUID` | `principal.asset.product_object_id` | Directly mapped  
`autoguid` | `principal.asset.product_object_id` | Directly mapped  
`SiteName` | `principal.hostname` | Directly mapped  
`SourceHostName` | `principal.hostname` | Directly mapped  
`TargetHostName` | `principal.hostname` | Directly mapped  
`analyzer_host_name` | `principal.hostname` | Directly mapped  
`host` | `principal.hostname` | Directly mapped  
`machine_name` | `principal.hostname` | Directly mapped  
`prin_host` | `principal.hostname` | Directly mapped  
`principal_asset_hostname` | `principal.hostname` | Directly mapped  
`principal_machine_name` | `principal.hostname` | Directly mapped  
`source_host_name` | `principal.hostname` | Directly mapped  
`sourcehostname` | `principal.hostname` | Directly mapped  
`machine_ip_address` | `principal.ip` | Merged  
`normalized_ip_address` | `principal.ip` | Merged  
`prin_ip` | `principal.ip` | Merged  
`sourceIP` | `principal.ip` | Merged  
`source_ip` | `principal.ip` | Merged  
`sourceipv4` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`srcip` | `principal.ip` | Merged  
`SourceMAC` | `principal.mac` | Merged  
`machine_raw_mac_address` | `principal.mac` | Merged  
`normalized_mac_address` | `principal.mac` | Merged  
`sourcemac` | `principal.mac` | Merged  
`source_port` | `principal.port` | Directly mapped  
`cmd_line` | `principal.process.command_line` | Directly mapped  
`eventCommandLine` | `principal.process.command_line` | Directly mapped  
`source_process_cmd` | `principal.process.command_line` | Directly mapped  
`SourceFilePath` | `principal.process.file.full_path` | Directly mapped  
`SourceProcessName` | `principal.process.file.full_path` | Directly mapped  
`eventProgramName` | `principal.process.file.full_path` | Directly mapped  
`process_name` | `principal.process.file.full_path` | Directly mapped  
`prog_name` | `principal.process.file.full_path` | Directly mapped  
`sourceprocessname` | `principal.process.file.full_path` | Directly mapped  
`SourceProcessHash` | `principal.process.file.md5` | Directly mapped  
`Source_FileSize` | `principal.process.file.size` | Directly mapped  
`parent_process_name` | `principal.process.parent_process.file.full_path` | Directly mapped  
`source_parent_process_id` | `principal.process.parent_process.pid` | Directly mapped  
`process_id` | `principal.process.pid` | Directly mapped  
`source_process_id` | `principal.process.pid` | Directly mapped  
`source_device_sn` | `principal.resource.id` | Directly mapped  
`source_product_name` | `principal.resource.name` | Directly mapped  
`SourceURL` | `principal.url` | Directly mapped  
`sourceurl` | `principal.url` | Directly mapped  
`subject` | `principal.user.group_identifiers` | Merged  
`machine_user_name` | `principal.user.user_display_name` | Directly mapped  
`source_user_name` | `principal.user.user_display_name` | Directly mapped  
`username` | `principal.user.user_display_name` | Directly mapped  
`SourceUserName` | `principal.user.userid` | Directly mapped  
`clientId` | `principal.user.userid` | Directly mapped  
`eventProgramUser` | `principal.user.userid` | Directly mapped  
`sourceusername` | `principal.user.userid` | Directly mapped  
`sec_res` | `security_result` | Merged  
`security_result` | `security_result` | Merged  
`security_result_token` | `security_result` | Merged  
`virus_type_label` | `security_result.about.resource.attribute.labels` | Merged  
`action` | `security_result.action` | Merged  
`security_action` | `security_result.action` | Merged  
`action_taken` | `security_result.action_details` | Directly mapped  
`security_action_details` | `security_result.action_details` | Directly mapped  
`threat_action_taken` | `security_result.action_details` | Directly mapped  
`category` | `security_result.category` | Merged  
`security_category` | `security_result.category` | Merged  
`ThreatCategory` | `security_result.category_details` | Merged  
`category_details` | `security_result.category_details` | Merged  
`security_category_details` | `security_result.category_details` | Merged  
`threatcategory` | `security_result.category_details` | Merged  
`Data` | `security_result.description` | Directly mapped  
`natural_lang_description` | `security_result.description` | Directly mapped  
`security_description` | `security_result.description` | Directly mapped  
`Access_Requested_label` | `security_result.detection_fields` | Merged  
`Analyzer_ContentVersion_label` | `security_result.detection_fields` | Merged  
`_field` | `security_result.detection_fields` | Merged  
`analyzer_dat_version_label` | `security_result.detection_fields` | Merged  
`analyzer_detection_method_label` | `security_result.detection_fields` | Merged  
`analyzerdatversion_label` | `security_result.detection_fields` | Merged  
`analyzerdetectionmethod_label` | `security_result.detection_fields` | Merged  
`command_executed_label` | `security_result.detection_fields` | Merged  
`label_agent_guid` | `security_result.detection_fields` | Merged  
`label_task_name` | `security_result.detection_fields` | Merged  
`labels0` | `security_result.detection_fields` | Merged  
`return_code_label` | `security_result.detection_fields` | Merged  
`seq_no_label` | `security_result.detection_fields` | Merged  
`server_id_label` | `security_result.detection_fields` | Merged  
`task_id_label` | `security_result.detection_fields` | Merged  
`task_name_label` | `security_result.detection_fields` | Merged  
`threat_event_id_label` | `security_result.detection_fields` | Merged  
`threat_handled_label` | `security_result.detection_fields` | Merged  
`threat_type_label` | `security_result.detection_fields` | Merged  
`threateventid_label` | `security_result.detection_fields` | Merged  
`threathandled_label` | `security_result.detection_fields` | Merged  
`threattype_label` | `security_result.detection_fields` | Merged  
`total_chunks_label` | `security_result.detection_fields` | Merged  
`transaction_id_label` | `security_result.detection_fields` | Merged  
`TVDEventID` | `security_result.rule_id` | Directly mapped  
`event_id` | `security_result.rule_id` | Directly mapped  
`policy_name` | `security_result.rule_name` | Directly mapped  
`rule_name` | `security_result.rule_name` | Directly mapped  
`TVDSeverity` | `security_result.severity_details` | Directly mapped  
`ThreatSeverity` | `security_result.severity_details` | Directly mapped  
`threat_severity` | `security_result.severity_details` | Directly mapped  
`threatseverity` | `security_result.severity_details` | Directly mapped  
`ThreatActionTaken` | `security_result.summary` | Directly mapped  
`ThreatType` | `security_result.summary` | Directly mapped  
`detection_message` | `security_result.summary` | Directly mapped  
`security_result.severity` | `security_result.summary` | Directly mapped  
`security_summary` | `security_result.summary` | Directly mapped  
`threat_type` | `security_result.threat_id` | Directly mapped  
`ThreatName` | `security_result.threat_name` | Directly mapped  
`threat_name` | `security_result.threat_name` | Directly mapped  
`threatname` | `security_result.threat_name` | Directly mapped  
`src_token` | `src` | Renamed/mapped  
`src_domain` | `src.administrative_domain` | Directly mapped  
`source_ip` | `src.ip` | Merged  
`source_port` | `src.port` | Directly mapped  
`src_user` | `src.user.userid` | Directly mapped  
`target_token` | `target` | Renamed/mapped  
`ProductCode` | `target.application` | Directly mapped  
`tar_app` | `target.application` | Directly mapped  
`serverid` | `target.asset.asset_id` | Directly mapped  
`token_new` | `target.asset.attribute.labels` | Merged  
`HostName` | `target.asset.hostname` | Directly mapped  
`TargetHostName` | `target.asset.hostname` | Directly mapped  
`target_hostname` | `target.asset.hostname` | Directly mapped  
`targetIP` | `target.asset.ip` | Merged  
`TargetMAC` | `target.asset.mac` | Merged  
`AgentGUID` | `target.asset_id` | Directly mapped  
`TargetFileName` | `target.file.full_path` | Directly mapped  
`target_file_name` | `target.file.full_path` | Directly mapped  
`targetfilename` | `target.file.full_path` | Directly mapped  
`target_file_size` | `target.file.size` | Renamed/mapped  
`HostName` | `target.hostname` | Directly mapped  
`TargetHostName` | `target.hostname` | Directly mapped  
`machine_name` | `target.hostname` | Directly mapped  
`target_asset_hostname` | `target.hostname` | Directly mapped  
`target_host_name` | `target.hostname` | Directly mapped  
`targethostname` | `target.hostname` | Directly mapped  
`dstip` | `target.ip` | Merged  
`normalized_ip_address` | `target.ip` | Merged  
`targetIP` | `target.ip` | Merged  
`target_ip` | `target.ip` | Merged  
`target_ipv4` | `target.ip` | Directly mapped  
`targetipv4_val` | `target.ip` | Merged  
`TargetMAC` | `target.mac` | Merged  
`normalized_mac_address` | `target.mac` | Merged  
`targetmac` | `target.mac` | Merged  
`TenantId` | `target.namespace` | Directly mapped  
`tenantid` | `target.namespace` | Directly mapped  
`TargetPort` | `target.port` | Directly mapped  
`target_port` | `target.port` | Directly mapped  
`targetport` | `target.port` | Directly mapped  
`TargetProcessName` | `target.process.file.full_path` | Directly mapped  
`eventObject` | `target.process.file.full_path` | Directly mapped  
`file_name` | `target.process.file.full_path` | Directly mapped  
`process_name` | `target.process.file.full_path` | Directly mapped  
`target_file_name` | `target.process.file.full_path` | Directly mapped  
`target_name` | `target.process.file.full_path` | Directly mapped  
`targetprocessname` | `target.process.file.full_path` | Directly mapped  
`value_data` | `target.process.file.full_path` | Directly mapped  
`hash` | `target.process.file.md5` | Directly mapped  
`md5` | `target.process.file.md5` | Directly mapped  
`target_hash` | `target.process.file.md5` | Directly mapped  
`sha1` | `target.process.file.sha1` | Directly mapped  
`target_sha` | `target.process.file.sha1` | Directly mapped  
`sha256` | `target.process.file.sha256` | Directly mapped  
`file_size` | `target.process.file.size` | Directly mapped  
`target_parent_file_name` | `target.process.parent_process.file.full_path` | Directly mapped  
`LogonSessionID` | `target.process.pid` | Directly mapped  
`tar_pid` | `target.process.pid` | Directly mapped  
`key_name` | `target.registry.registry_key` | Directly mapped  
`ThreatName` | `target.resource.name` | Directly mapped  
`source_url` | `target.url` | Directly mapped  
`nodeid_label` | `target.user.attribute.labels` | Merged  
`version_label` | `target.user.attribute.labels` | Merged  
`targetuseremail` | `target.user.email_addresses` | Merged  
`machine_user_name` | `target.user.user_display_name` | Directly mapped  
`target_user_name` | `target.user.user_display_name` | Directly mapped  
`value` | `target.user.user_display_name` | Directly mapped  
`TargetUserName` | `target.user.userid` | Directly mapped  
`UserName` | `target.user.userid` | Directly mapped  
`UserSID` | `target.user.windows_sid` | Directly mapped  
N/A | `about` | Constant: `about_token`  
N/A | `additional.fields` | Constant: `eventType_label`  
N/A | `intermediary` | Constant: `intermediary1`  
N/A | `intermediary.asset.mac` | Constant: `AnalyzerMAC`  
N/A | `intermediary.ip` | Constant: `analyzeripv4`  
N/A | `intermediary.mac` | Constant: `AnalyzerMAC`  
N/A | `metadata.description` | Constant: `No raw event available`  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `McAfee EPO`  
N/A | `metadata.vendor_name` | Constant: `McAfee`  
N/A | `observer.ip` | Constant: `sys_ip`  
N/A | `principal.asset.attribute.labels` | Constant: `token_new`  
N/A | `principal.asset.ip` | Constant: `src_ip`  
N/A | `principal.asset.mac` | Constant: `SourceMAC`  
N/A | `principal.ip` | Constant: `src_ip`  
N/A | `principal.mac` | Constant: `SourceMAC`  
N/A | `principal.platform` | Constant: `WINDOWS`  
N/A | `principal.process.file.size` | Constant: `uinteger`  
N/A | `principal.user.group_identifiers` | Constant: `subject`  
N/A | `security_result` | Constant: `sec_res`  
N/A | `security_result.about.resource.attribute.labels` | Constant: `virus_type_label`  
N/A | `security_result.action` | Constant: `action`  
N/A | `security_result.category` | Constant: `category`  
N/A | `security_result.category_details` | Constant: `ThreatCategory`  
N/A | `security_result.detection_fields` | Constant: `threat_event_id_label`  
N/A | `security_result.severity` | Constant: `HIGH`  
N/A | `src.ip` | Constant: `source_ip`  
N/A | `target.asset.attribute.labels` | Constant: `token_new`  
N/A | `target.asset.ip` | Constant: `targetIP`  
N/A | `target.asset.mac` | Constant: `TargetMAC`  
N/A | `target.ip` | Constant: `targetIP`  
N/A | `target.mac` | Constant: `TargetMAC`  
N/A | `target.process.file.size` | Constant: `uinteger`  
N/A | `target.user.attribute.labels` | Constant: `version_label`  
N/A | `target.user.email_addresses` | Constant: `targetuseremail`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
