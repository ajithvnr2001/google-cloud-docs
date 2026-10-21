---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-afm/
title: Collect F5 AFM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:49:48.205568+00:00
---

# Collect F5 AFM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-afm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect F5 AFM logs

**Parser Version:** 23.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest F5 Advanced Firewall Management (AFM) logs to Google Security Operations using the Bindplane agent.

F5 BIG-IP AFM is a network firewall module that generates syslog messages for firewall rule actions (accept, drop, reject), IP intelligence events, and TCP errors. The parser extracts fields from CSV-formatted or syslog-formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the F5 BIG-IP appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to F5 BIG-IP and F5 Advanced Firewall Management



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

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

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            tcplog:
                listen_address: "0.0.0.0:5145"
        
        exporters:
            chronicle/f5_afm:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: F5_AFM
                raw_log_field: body
        
        service:
            pipelines:
                logs/f5_afm_to_chronicle:
                    receivers:
                        - tcplog
                    exporters:
                        - chronicle/f5_afm
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `5145` is used for F5 AFM high-speed logging (adjust to match your F5 configuration)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



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
             




## Enable F5 BIG-IP Advanced Firewall Manager

  1. Sign in to the **BIG-IP appliance** management console.
  2. Go to **System > License**.
  3. Verify that the **Advanced Firewall Manager** is **licensed** and **enabled**.
  4. To enable the **Advanced Firewall Manager** , go to **System > Resource > Provisioning**.
  5. Select the checkbox from the **Provisioning column** and select **Nominal** from the list.
  6. Click **Submit**.



## Configure Logging Pool in F5 AFM

  1. Go to **Local Traffic > Pools**.
  2. Click **Create**.
  3. Provide the following configuration details: 
     * **Name** : Enter a name for the logging pool (for example, **logging_pool**).
     * **Health Monitor** : In the **Available** list, select **TCP** and click **< <**.
  4. In the **Resource** tab, select the **Logging Pool** you created earlier from the **Node Name** list.
  5. In the **Address** field, enter the Bindplane agent IP address.
  6. In the **Service Port** field, enter `5145` or other port as you defined in the Bindplane agent.
  7. Click **Add**.
  8. Click **Finish**.



## Configure the formatted log destination in F5 AFM

  1. Go to **System > Logs > Configuration > Log Destinations**.
  2. Click **Create**.
  3. Provide the following configuration details: 
     * **Name** : Enter a name for the logging format destination (for example, `Logging_Format_Destination`).
     * **Description** : Enter a description.
     * **Type** : Select **Remote Syslog**.
     * **Syslog Format** : Select **Syslog**.
     * **High-Speed Log Destination** : Select your high-speed logging destination (for example, `Logging_HSL_Destination`).
  4. Click **Finished**.



## Configure Log Publisher in F5 AFM

  1. Go to **System > Logs > Configuration > Log Publishers**.
  2. Click **Create**.
  3. Provide the following configuration details: 
     * **Name** : Enter a name for the publisher (for example, `Log_Publisher`).
     * **Description** : Enter a description.
     * **Destinations** : Select the **log destination name** that you created in the **Configure Logging Pool in F5 AFM** step and click **< <** to add items to the **Selected** list.



## Configure Logging Profile in F5 AFM

  1. Go to **Security > Event Logs > Logging Profile**.
  2. Click **Create**.
  3. Provide the following configuration details: 
     * **Name** : Enter a name for the log profile (for example, **Logging_Profile**).
     * **Network Firewall** : Select the **Enabled** checkbox.
     * **Publisher** : Select the **log publisher** that you configured earlier (for example, `Log_Publisher`).
     * **Log Rule Matches** : Select the **Accept, Drop, and Reject** checkboxes.
     * **Log IP Errors** : Select the **Enabled** checkbox.
     * **Log TCP Errors** : Select the **Enabled** checkbox.
     * **Log TCP Events** : Select the **Enabled** checkbox.
     * **Storage Format** : Select **Field-List**.
     * **Delimiter** : Enter `,` (comma) as the delimiter for events.
     * **Storage Options** : Select **all of the options** in the **Available Items** list and click **< <**.
     * In the **IP Intelligence** tab, select the **log publisher** that you configured (for example, `Log_Publisher`).
  4. Click **Finished**.



## Configure Virtual Server Profile Association in F5 AFM

  1. Go to **Local Traffic > Virtual Servers**.
  2. Select the **virtual server** to modify.
  3. Go to the **Security tab > Policies**.
  4. From the **Log Profile** list, select **Enabled**.
  5. From the **Profile** field, select **Logging_Profile** and click **< <**.
  6. Click **Update**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
acl_policy_name | security_result.detection_fields.acl_policy_name | Value of column22 if the log format is SYSLOG, else value of column13  
acl_policy_type | security_result.detection_fields.acl_policy_type | Value of column21 if the log format is SYSLOG, else value of column18  
acl_rule_name | security_result.rule_name | Value of column23 if the log format is SYSLOG, else value of column11  
acl_rule_uuid | security_result.rule_id | Value of acl_rule_uuid field from the grok pattern  
action | security_result.action | If value of column25 is `Drop`, `Reject` or `Block` then BLOCK, else if value of column25 is `Accept`, `Accept decisively`, `Established` or `Allow` then ALLOW  
attackID | security_result.detection_fields.attackID | Value of column12 if the log format is CSV with no src_ip  
bigip_hostname | intermediary.hostname | Value of column2 if the log format is SYSLOG, else value of column3  
bigip_ip | intermediary.ip | Value of column2 if the log format is SYSLOG, else value of column1  
context_name | additional.fields.context_name.string_value | Value of column4 if the log format is SYSLOG, else value of column10 if there is src_ip, else value of column5  
context_type | additional.fields.context_type.string_value | Value of column3 if the log format is SYSLOG, else value of column4 if there is src_ip, else value of column4  
dest_fqdn | additional.fields.dest_fqdn.string_value | Value of column7 if the log format is SYSLOG, else value of column13  
dest_geo | additional.fields.dest_geo.string_value | Value of column14  
dest_ip | target.asset.ip, target.ip | Value of column8 if the log format is SYSLOG, else value of column6 if there is src_ip, else value of column6  
dest_port | target.port | Value of column10 if the log format is SYSLOG, else value of column8 if there is src_ip, else value of column8  
drop_reason | security_result.summary | Value of column26 if the log format is SYSLOG, else value of column19  
eventId | additional.fields.eventId.string_value | Value captured in the grok pattern  
flow_id | additional.fields.flow_id.string_value | Value of column29 if the log format is SYSLOG, else value of column17  
loglevel | security_result.severity | If value of loglevel field from the grok pattern is `warning`,`debug` or `notice` then MEDIUM, else if value is `info` or `informational` then INFORMATIONAL, else if value is `err` or `error` then HIGH, else if value is `alert`, `crit` or `emer` then CRITICAL  
packetsReceived | network.received_packets | Value of column15 if the log format is CSV with no src_ip  
process | target.application | Value of process field from the grok pattern  
protocol_number_src | network.ip_protocol | Value of column12 if the log format is SYSLOG, else value extracted from the ip_protocol_out variable  
route_domain | additional.fields.route_domain.string_value | Value of column13 if the log format is SYSLOG, else value of column9  
source_fqdn | additional.fields.source_fqdn.string_value | Value of column5 if the log format is SYSLOG, else value of column7  
src_geo | additional.fields.src_geo.string_value | Value of column8  
src_ip | principal.asset.ip, principal.ip | Value of column6 if the log format is SYSLOG, else value of column9 if the log format is CSV with no src_ip, else value of column5  
src_port | principal.port | Value of column9 if the log format is SYSLOG, else value of column7 if the log format is CSV with no src_ip, else value of column7  
ts | metadata.event_timestamp | Value of ts field from the grok pattern  
vlan | additional.fields.vlan.string_value | Value of column11 if the log format is SYSLOG, else value of column21  
| metadata.event_type | If src_ip and dest_ip exist then NETWORK_CONNECTION, else if only src_ip exists then STATUS_UPDATE, else GENERIC_EVENT  
| metadata.log_type | F5_AFM  
| metadata.product_name | Advanced Firewall Management  
| metadata.vendor_name | F5  
`partition` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`level` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tty` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`attempts` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`start` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`end` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`prin_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`internal_tag` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`src_zone` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`dest_zone` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`translated_dest_ip` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`translated_dest_port` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`translated_source_ip` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`translated_source_port` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`syslog_reporter_host` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sa_translation_pool` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sa_translation_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`translated_route_domain` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`send_to_vs` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`src_zone` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`dest_zone` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`acl_policy_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`acl_policy_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`chronicle_log_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`chronicle_namespace` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`flow_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`vlan` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`route_domain` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`partition_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`source_ipint_categories` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`src_geo` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`source_fqdn` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`dest_ipint_categories` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`dst_geo` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`dest_fqdn` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`acl_rule_name` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`acl_rule_id` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`action` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`bigip_mgmt_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`context_name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`context_type` | `event.idm.read_only_udm.target.resource.type` | Mapped from changelog  
`date_time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`dest_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`net.peer.ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`dest_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`net.peer.port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`device_version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`drop_reason` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`ip_protocol` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`source_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`net.host.ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`source_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`net.host.port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`errdefs_msg_name` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`errdefs_msgno` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`source_user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`source_user_group` | `event.idm.read_only_udm.principal.user.group_identifiers` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`dvchost` | `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`dvc` | `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`c6a2` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`F5SrcZone` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`F5SrcFqdn` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`F5SrcUser` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`c6a3` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`F5DstZone` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`F5DstVlan` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`F5DstFqdn` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`F5SendToVs` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`F5SrcIpiCategories` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`F5DstIpiCategories` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`module` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cpu` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cmd_line` | `event.idm.read_only_udm.target.process.command_line` | Mapped from changelog  
`msg_data` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`pid` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`folder_path` | `event.idm.read_only_udm.principal.file.full_path` | Mapped from changelog  
`status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cmd_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`target_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`desc` | `metadata.description` | Mapped from changelog  
`prin_port` | `principal.port` | Mapped from changelog  
`target_port` | `target.port` | Mapped from changelog  
`ts2` | `metadata.event_timestamp` | Mapped from changelog  
`tls_ver` | `network.tls.version` | Mapped from changelog  
`cipher` | `network.tls.cipher` | Mapped from changelog  
`prod_event_type` | `metadata.product_event_type` | Mapped from changelog  
`path` | `target.url` | Mapped from changelog  
`response_size` | `network.sent_bytes` | Mapped from changelog  
`received_size` | `network.received_bytes` | Mapped from changelog  
`usr` | `principal.user.userid` | Mapped from changelog  
`schema_version` | `target.resource.attribute.labels` | Mapped from changelog  
`severity_info` | `security_result.severity_details` | Mapped from changelog  
`target_pid` | `target.process.pid` | Mapped from changelog  
`additional1` | `additional.fields` | Mapped from changelog  
`dvc` | `intermediary.hostname` | Mapped from changelog  
`metadata.event_type` | `USER_UNCATEGORIZED` | Mapped from changelog  
`prin_ip` | `principal.ip` | Mapped from changelog  
`F5FlowID` | `additional.fields` | Mapped from changelog  
`F5TranslatedVlan` | `additional.fields` | Mapped from changelog  
`F5SrcTranslationType` | `additional.fields` | Mapped from changelog  
`F5SrcTranslationPool` | `additional.fields` | Mapped from changelog  
`F5SrcGeo` | `additional.fields` | Mapped from changelog  
`F5DstGeo` | `additional.fields` | Mapped from changelog  
`F5RouteDomain` | `additional.fields` | Mapped from changelog  
`Column12` | `security_result.detection_fields` | Mapped from changelog  
`Column14` | `security_result.action` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-afm-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
