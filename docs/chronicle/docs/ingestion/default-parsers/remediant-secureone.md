---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/remediant-secureone/
title: Collect Netwrix Privilege Secure for Discovery (formerly Remediant SecureONE) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:09.705834+00:00
---

# Collect Netwrix Privilege Secure for Discovery (formerly Remediant SecureONE) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/remediant-secureone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Netwrix Privilege Secure for Discovery (formerly Remediant SecureONE) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Netwrix Privilege Secure for Discovery (formerly Remediant SecureONE) logs to Google Security Operations using the Bindplane agent.

Netwrix Privilege Secure for Discovery is an agentless privileged access management (PAM) solution that provides dynamic Just-in-Time (JIT) privileged account access. It eliminates standing privileges by providing continuous visibility into privileged accounts, effectively preventing lateral movement attacks and reducing an organization's attack surface.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Remediant SecureONE appliance (SSH access to the node running fluentd)
  * Remediant SecureONE version 2.8 or later (or the `s1_fluentd` service upgraded to fluentd version 1)



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

## Get a Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install Bindplane agent

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

For additional installation options, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
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
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'REMEDIANT_SECUREONE'
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
    * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
    * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * Replace `<customer_id>` with the actual Customer ID.
    * Update `/path/to/ingestion-authentication-file.json` to the file path where you saved the service account key file (Option 1).



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'REMEDIANT_SECUREONE'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Linux** , run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

  * To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
        
        net stop observiq-otel-collector && net start observiq-otel-collector
        




## Configure Remediant SecureONE syslog forwarding

  1. Use SSH to connect to the Remediant SecureONE node running the `fluentd` service.
  2. Back up the existing `fluentd` configuration file:
         
         sudo cp /secureone/conf/fluentd/fluent.conf /secureone/conf/fluentd/fluent.conf.$(date +%Y.%m.%d)
         

  3. Open the `fluentd` configuration file for editing:
         
         sudo vim /secureone/conf/fluentd/fluent.conf
         

  4. Edit the `match docker.**` section to add the `remote_syslog` store. Replace the entire file contents with the following configuration:
         
         #fluent.conf for fluentd version 1
         <source>
           @type forward
         </source>
         <filter docker.**>
           @type parser
           time_key key3
           format json
           key_name log
           reserve_data true
         </filter>
         <match docker.**>
           @type copy
           <store>
             @type remote_syslog
             host BINDPLANE_IP
             port 514
             protocol tcp
             packet_size 4096
             program secureone
             hostname SECUREONE_HOSTNAME
             <format>
               @type single_value
               message_key log
             </format>
           </store>
           <store>
             @type stdout_pp
             pp true
             time_color blue
             tag_color yellow
             record_colored true
           </store>
         </match>
         <match **>
           @type stdout_pp
           pp true
           time_color blue
           tag_color yellow
           record_colored true
         </match>
         

  5. Replace the following values:

     * **BINDPLANE_IP** : Enter the IP address of the Bindplane agent host (for example, `10.100.11.13`).
     * **514** : Enter the port number matching the Bindplane agent `listen_address` port.
     * **SECUREONE_HOSTNAME** : Enter the hostname of the SecureONE node (for example, `secureone-prod-01`).
  6. Save the configuration file and exit the editor.

  7. Restart the fluentd service to apply the new configuration:
         
         s1 restart fluentd
         

  8. Verify the fluentd version and running configuration:
         
         sudo docker exec -it $(sudo docker ps | grep fluentd | cut -d' ' -f1) fluent-gem list | grep fluentd
         

  9. Validate the configuration syntax:
         
         sudo docker exec -it $(sudo docker ps | grep fluentd | cut -d' ' -f1) fluentd -c /fluentd/etc/fluent.conf --dry-run
         

  10. Verify logs are being forwarded by monitoring traffic on the syslog port:
         
         sudo tcpdump -vv -i any port 514
         

**Note:** SecureONE forwards logs from all Docker services including api, worker, scanner, ldapsync, analytics_engine, internal_api, health_reporter, and expire. All services are forwarded based on the `docker.**` match stanza.**Note:** SecureONE versions prior to 2.8 use a version of fluentd that truncates logs at 1 KB. Upgrade the fluentd service to version 1 or later before configuring syslog forwarding.



For more information, see the [Netwrix Privilege Secure for Discovery documentation](https://docs.netwrix.com/docs/privilegesecurediscovery/2_22/integrations/siem/forwardlogs).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`access_tokenId_label` | `additional.fields` | Merged  
`access_tokenType_label` | `additional.fields` | Merged  
`access_type_label` | `additional.fields` | Merged  
`createdBy_label` | `additional.fields` | Merged  
`details.failover_dc_label` | `additional.fields` | Merged  
`details.initial_dc_label` | `additional.fields` | Merged  
`details.sync_end_ts_label` | `additional.fields` | Merged  
`duration_label` | `additional.fields` | Merged  
`ldapName_label` | `additional.fields` | Merged  
`manage_local_sids_label` | `additional.fields` | Merged  
`persistent_label` | `additional.fields` | Merged  
`req_query_limit_label` | `additional.fields` | Merged  
`req_query_page_label` | `additional.fields` | Merged  
`scan_label` | `additional.fields` | Merged  
`secure_label` | `additional.fields` | Merged  
`strict_secure_label` | `additional.fields` | Merged  
`sync_start_ts_label` | `additional.fields` | Merged  
`targetSystem_cn_label` | `additional.fields` | Merged  
`targetSystem_distinguishedName_label` | `additional.fields` | Merged  
`targetSystem_operatingSystem_label` | `additional.fields` | Merged  
`user_distinguishedName_label` | `additional.fields` | Merged  
`req_headers_host` | `intermediary.asset.hostname` | Directly mapped  
`req_headers_host` | `intermediary.hostname` | Directly mapped  
`json_message` | `metadata.description` | Directly mapped  
`msg` | `metadata.description` | Directly mapped  
`time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`event_type` | `metadata.event_type` | Directly mapped  
`name` | `metadata.product_event_type` | Directly mapped  
`req_id` | `metadata.product_log_id` | Directly mapped  
`req.method` | `network.http.method` | Directly mapped  
`res.statusCode` | `network.http.response_code` | Renamed/mapped  
`req_header_user_agent` | `network.http.user_agent` | Directly mapped  
`targetSystem.domain_netbios` | `principal.administrative_domain` | Directly mapped  
`user_domain_fqdn` | `principal.administrative_domain` | Directly mapped  
`source_application` | `principal.application` | Directly mapped  
`req_headers_host` | `principal.hostname` | Directly mapped  
`targetSystem.cn` | `principal.hostname` | Directly mapped  
`client_ip` | `principal.ip` | Merged  
`remote_address` | `principal.ip` | Merged  
`client_ua_os` | `principal.platform` | Mapped: `(?i)windows` → `WINDOWS`, `(?i)linux` → `LINUX`, `(?i)mac` → `MAC`  
`client_ua_platform` | `principal.platform_version` | Directly mapped  
`client_ua_version` | `principal.platform_version` | Directly mapped  
`req.remotePort` | `principal.port` | Renamed/mapped  
`script_cmd` | `principal.process.command_line` | Directly mapped  
`pid` | `principal.process.pid` | Directly mapped  
`browser_label` | `principal.resource.attribute.labels` | Merged  
`req_header_map_label` | `principal.resource.attribute.labels` | Merged  
`system` | `principal.resource.product_object_id` | Directly mapped  
`domain_netbios_label` | `principal.user.attribute.labels` | Merged  
`objectSid_label` | `principal.user.attribute.labels` | Merged  
`user_domain_label` | `principal.user.attribute.labels` | Merged  
`user_domain_netbios_label` | `principal.user.attribute.labels` | Merged  
`user_id_label` | `principal.user.attribute.labels` | Merged  
`user_objectSid_label` | `principal.user.attribute.labels` | Merged  
`authData.access.role` | `principal.user.role_name` | Directly mapped  
`user_user` | `principal.user.user_display_name` | Directly mapped  
`access.user.sAMAccountName` | `principal.user.userid` | Directly mapped  
`user_cn` | `principal.user.userid` | Directly mapped  
`user_sid` | `principal.user.windows_sid` | Directly mapped  
`disabled_label` | `security_result.detection_fields` | Merged  
`disabled_label1` | `security_result.detection_fields` | Merged  
`level_label` | `security_result.detection_fields` | Merged  
`req_id_key_label` | `security_result.detection_fields` | Merged  
`req_params_computerId_label` | `security_result.detection_fields` | Merged  
`targetSystem_id_label` | `security_result.detection_fields` | Merged  
`hostname` | `src.hostname` | Directly mapped  
`ldapName` | `target.administrative_domain` | Directly mapped  
`targetsystem` | `target.asset.hostname` | Directly mapped  
`server` | `target.hostname` | Directly mapped  
`targetsystem` | `target.hostname` | Directly mapped  
`header_map_label` | `target.resource.attribute.labels` | Merged  
`req.url` | `target.url` | Directly mapped  
`user_user` | `target.user.userid` | Directly mapped  
N/A | `metadata.product_name` | Constant: `SecureONE`  
N/A | `metadata.vendor_name` | Constant: `Remediant`  
N/A | `principal.platform` | Constant: `WINDOWS`  
`targetSystem.cn` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`req.query.page` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user.distinguishedName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`targetSystem.operatingSystem` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`req.query.limit` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`req.params.computerId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`req.id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`targetSystem._id` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`user.domain_netbios` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`user.id` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`user.objectSid` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`persistent` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`access.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`access.tokenId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`access.tokenType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`targetSystem.cn` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`targetSystem.distinguishedName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`targetSystem.policy.strict_secure` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`targetSystem.policy.secure` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`targetSystem.policy.scan` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`targetSystem.policy.manage_local_sids` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user.domain` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`access.user.domain_netbios` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`access.user.objectSid` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`user.sid` | `event.idm.read_only_udm.principal.user.windows_sid` | Mapped from changelog  
`user.user` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`failover_dc","initial_dc","ldapName","sync_end_ts" ,and "sync_start_ts` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/remediant-secureone-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
