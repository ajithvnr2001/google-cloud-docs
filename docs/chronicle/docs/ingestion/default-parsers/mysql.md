---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mysql/
title: Collect MySQL logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:32.681479+00:00
---

# Collect MySQL logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect MySQL logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest MySQL logs to Google Security Operations using the Bindplane agent.

MySQL is a relational database management system that generates syslog messages for authentication events, query execution, database operations, and audit trail entries. The parser extracts fields from syslog-formatted audit logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the MySQL server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * SSH access to the MySQL host with root or sudo privileges



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
            chronicle/mysql:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: MYSQL
                raw_log_field: body
        
        service:
            pipelines:
                logs/mysql_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/mysql
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
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
             




## Configure syslog in MySQL

  1. Sign in to the **MySQL** host using SSH.
  2. Connect to the MySQL database:
         
         mysql -u root -p
         

  3. Verify the `server_audit.so` audit plugin:
         
         show variables like 'plugin_dir';
         

  4. If the plugin is not found, install it:
         
         install plugin server_audit soname 'server_audit.so';
         

  5. Confirm the plugin is **Installed** and **Enabled** :
         
         show plugins;
         

  6. Edit the file `/etc/my.cnf` and enable the following audit settings:
         
         server_audit_events='CONNECT,QUERY,TABLE'
         server_audit_file_path=server_audit.log
         server_audit_logging=ON
         server_audit_output_type=SYSLOG
         server_audit_syslog_facility=LOG_LOCAL6
         

  7. Verify the audit variables:
         
         show global variables like "server_audit%";
         

  8. Verify auditing is enabled:
         
         Show global status like 'server_audit%';
         

  9. Edit the file `/etc/rsyslog.conf` to enable forwarding via UDP:
         
         *.* @@<bindplane-agent-ip>:<bindplane-agent-port>
         

     * Replace `<bindplane-agent-ip>` and `<bindplane-agent-port>` with your Bindplane agent configuration.
  10. Restart the MySQL service:
         
         /etc/init.d/mysqld restart
         




## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
action | read_only_udm.metadata.event_type | If the value is `Created` then FILE_CREATION, if the value is `Deleted` then FILE_DELETION, otherwise no change.  
database | read_only_udm.target.resource.parent |   
db_hostname | read_only_udm.target.hostname |   
db_user | read_only_udm.target.user.userid |   
description | read_only_udm.security_result.description |   
error_details |  | This is a temporary variable, ignore it  
error_level | read_only_udm.security_result.severity | If the value is `error` then ERROR, if the value is `warning` then MEDIUM, if the value is `note` then INFORMATIONAL, otherwise no change.  
error_message | read_only_udm.security_result.summary |   
file_path | read_only_udm.target.file.full_path |   
file_size | read_only_udm.target.file.size |   
hostname | read_only_udm.principal.hostname |   
inner_message | read_only_udm.security_result.description |   
summary | read_only_udm.metadata.product_event_type |   
table | read_only_udm.target.resource.name |   
table_not_found |  | This is a temporary variable, ignore it  
timestamp | read_only_udm.metadata.event_timestamp |   
| read_only_udm.extensions.auth.type | Static value - `MACHINE`  
| read_only_udm.metadata.event_type | Static value - `USER_LOGIN`, `GENERIC_EVENT`, `STATUS_UPDATE`, `FILE_CREATION`, `FILE_DELETION`  
| read_only_udm.metadata.log_type | Static value - `MYSQL`  
| read_only_udm.metadata.product_name | Static value - `MySQL`  
| read_only_udm.metadata.vendor_name | Static value - `Oracle Corporation`  
| read_only_udm.security_result.action | Static value - `BLOCK`  
| read_only_udm.target.resource.resource_type | Static value - `DATABASE`, `TABLE`  
`properties.event_time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`properties.ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`properties.user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`properties.error_code` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`properties.event_subclass` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`properties.is_aad_auth` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`category` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`ServerType` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`target_app` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`properties.start_time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`ts` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`time` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`properties.server_id` | `event.idm.read_only_udm.target.asset.asset_id` | Mapped from changelog  
`properties.thread_id` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`user_id` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`p_host` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`p_host` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`properties.db` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`resourceId` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`operationName` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`location` | `event.idm.read_only_udm.target.location.name` | Mapped from changelog  
`properties.host` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`properties.last_insert_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`properties.insert_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`properties.sql_text` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`properties.rows_examined` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`properties.rows_sent` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`properties.lock_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`properties.query_time` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`properties.replication_set_role` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`properties.event_class` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`csv_principal_hostname` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`csv_hostname` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`csv_principal_hostname` | `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`ts` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`csv_query_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`csv_mysql` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`account_host` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`login_proxy` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`login_os` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`arg` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`startup_data_server_id` | `event.idm.read_only_udm.principal.resource.product_object_id` | Mapped from changelog  
`startup_data_os_version` | `event.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`startup_data_mysql_version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`arg` | `event.idm.read_only_udm.principal.process.command_line` | Mapped from changelog  
`csv_mysql_sql_query` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`login.proxy` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`connection_data.connection_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`connection_data.status` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`login.os` | `event.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`account.host` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`connection_data.db` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`mysql_description` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`mysql_errno` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`mysql_version` | `event.idm.read_only_udm.metadata.product_version` | Mapped from changelog  
`process_path` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`mysql_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`status` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`error_level` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`mysql_thread_id` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`mysql_socket` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`log_level` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`mysql_timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`event_date` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`event_time` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`csv_timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`mysql_action` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`log_category` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`csv_mysql_action` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`csv_mysql_connection_type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`event_message` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`resolution_error` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`component` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`mysql_hostname` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`csv_hostname_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`mysql_username` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`csv_username` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`csv_target_hostname` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`csv_database_name` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`mysql_sql_query` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`csv_connection_id` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`mysql_message_id` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`target_mysql_hostname` | `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`csv_mysql_connection_type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`login.ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`login.ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`login.user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`account.user` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`inter_host` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`target_host` | `event.idm.read_only_udm.target.hostname` | Mapped from changelog  
`target_host` | `event.idm.read_only_udm.target.asset.hostname` | Mapped from changelog  
`target_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`target_ip` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`connection_id` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`general_data.command` | `event.idm.read_only_udm.target.process.command_line` | Mapped from changelog  
`general_data.query` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`connection_data.connection_type` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`general_data.sql_command` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`event_data` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`general_data.status` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`class` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Status` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`sql_query` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`value` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`num` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`ns` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`itemid` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`value_min` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`value_avg` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`value_max` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`query_id` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`clock` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`path` | `principal.file.full_path` | Mapped from changelog  
`logtype` | `metadata.product_event_type` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mysql-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
