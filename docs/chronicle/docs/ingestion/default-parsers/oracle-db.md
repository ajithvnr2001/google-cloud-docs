---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-db/
title: Collect Oracle DB logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:21:54.819639+00:00
---

# Collect Oracle DB logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/oracle-db/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Oracle DB logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Oracle DB logs to Google Security Operations using the Bindplane agent.

The parser extracts fields from SYSLOG messages, handling multiple formats using grok patterns and key-value parsing. It then maps these extracted fields to the Unified Data Model (UDM), enriching the data with static metadata like vendor and product names, and dynamically setting event types based on specific field values like ACTION and USERID.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Oracle Database host
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Oracle Database instance (SYSDBA or AUDIT_ADMIN role)
  * Oracle Database 19c or later with unified auditing enabled (or mixed-mode auditing on Oracle 12c–18c)



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane will be installed.

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
            chronicle/oracle_db:
                compression: gzip
                creds_file_path: '/path/to/ingestion-authentication-file.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: ORACLE_DB
                raw_log_field: body
        log_type: 'ORACLE_DB'
                ingestion_labels:
        
        service:
            pipelines:
                logs/oracle_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/oracle_db
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: The IP address and port to listen on: 
      * Replace `0.0.0.0` with a specific IP address to listen on one interface, or leave as `0.0.0.0` to listen on all interfaces (recommended)
      * Replace `514` with the port number matching the Oracle syslog forwarding configuration
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied in the **Get Google SecOps customer ID** section
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
             




## Configure Oracle Database unified auditing and syslog forwarding

### Enable unified auditing

If unified auditing is not yet enabled, relink the Oracle binaries with the `uniaud_on` option. This requires shutting down all Oracle processes running from the Oracle Home (database instance and listener).

  1. Connect to the Oracle Database host as the `oracle` operating system user.
  2. Shut down the Oracle instance and listener:
         
         sqlplus / as sysdba <<EOF
         shutdown immediate;
         exit
         EOF
         lsnrctl stop
         

  3. Relink the Oracle binaries with unified auditing enabled:
         
         cd $ORACLE_HOME/rdbms/lib
         make -f ins_rdbms.mk uniaud_on ioracle
         

  4. Start the listener and Oracle instance:
         
         lsnrctl start
         sqlplus / as sysdba <<EOF
         startup;
         exit
         EOF
         

  5. If Oracle Enterprise Manager Cloud Control is running on the same host, restart it:
         
         cd /u01/app/oracle/product/middleware/oms
         export OMS_HOME=/u01/app/oracle/product/middleware/oms
         $OMS_HOME/bin/emctl start oms
         

  6. Verify that unified auditing is enabled. Connect to the Oracle Database with SQLplus:
         
         SELECT VALUE FROM V$OPTION WHERE PARAMETER = 'Unified Auditing';
         




Verify that the command returns one row with **VALUE** equal to `TRUE`.

### Configure unified audit syslog output

Set the `UNIFIED_AUDIT_SYSTEMLOG` initialization parameter to write unified audit records to syslog. This parameter was introduced in Oracle 19c and replaces the deprecated `AUDIT_SYSLOG_LEVEL` parameter (which applies only to traditional auditing).

  1. Connect to the Oracle Database with SQLplus as SYSDBA.
  2. Set the `UNIFIED_AUDIT_SYSTEMLOG` parameter:

     * On **UNIX/Linux** systems, set the parameter to a `facility.priority` value:
    
    ALTER SYSTEM SET UNIFIED_AUDIT_SYSTEMLOG = 'LOCAL7.INFO' SCOPE=SPFILE;
    

     * On **Windows** systems, set the parameter to `TRUE` to write to the Windows Event Viewer:
    
    ALTER SYSTEM SET UNIFIED_AUDIT_SYSTEMLOG = TRUE SCOPE=SPFILE;
    

  3. Optional: To write common unified audit policy records from a CDB root container to syslog on UNIX/Linux systems, set the `UNIFIED_AUDIT_COMMON_SYSTEMLOG` parameter:
         
         ALTER SYSTEM SET UNIFIED_AUDIT_COMMON_SYSTEMLOG = TRUE SCOPE=SPFILE;
         

**Note:** `UNIFIED_AUDIT_COMMON_SYSTEMLOG` can only be set in the root container of a CDB. There is no Windows equivalent.
  4. Restart the Oracle Database instance for the parameter changes to take effect:
         
         SHUTDOWN IMMEDIATE;
         STARTUP;
         




### Configure the syslog daemon on the Oracle host

On the Oracle Database host, configure the syslog daemon to forward audit log entries to the Bindplane agent.

  1. Sign in to the Oracle Database host as `root`.
  2. Open the syslog configuration file:

     * On **RHEL/CentOS/Oracle Linux** with rsyslog:
           
           sudo vi /etc/rsyslog.conf
           

     * On older systems with syslog:
           
           sudo vi /etc/syslog.conf
           

  3. Add a forwarding rule that matches the facility and priority you configured in `UNIFIED_AUDIT_SYSTEMLOG`. For example, if you set `LOCAL7.INFO`:

     * To forward via **UDP** (matching Bindplane `udplog` receiver):
           
           local7.info @<BINDPLANE_HOST_IP>:514
           

     * To forward via **TCP** (if Bindplane uses `tcplog` receiver):
           
           local7.info @@<BINDPLANE_HOST_IP>:514
           

     * Replace `<BINDPLANE_HOST_IP>` with the IP address or hostname of the system running the Bindplane agent.

**Note:** A single `@` prefix indicates UDP forwarding. A double `@@` prefix indicates TCP forwarding. Ensure this matches the receiver type in the Bindplane `config.yaml`.
  4. Optional: To also retain a local copy of audit logs, add the following line:
         
         ```none
         local7.info /var/log/oracle_audit.log
         ```
         

  5. Save the file and restart the syslog daemon:

     * On **RHEL/CentOS/Oracle Linux** with rsyslog:
           
           sudo systemctl restart rsyslog
           

     * On older systems with syslog:
           
           sudo service syslog restart
           




### Verify audit log forwarding

  1. Generate a test audit event by performing an auditable action in the Oracle Database. For example, connect as a user and run:
         
         SELECT * FROM DBA_USERS WHERE ROWNUM = 1;
         

  2. Check the Bindplane agent logs for incoming syslog messages:
         
         sudo journalctl -u observiq-otel-collector -f
         

  3. Verify that the syslog message contains the `Oracle Unified Audit` tag with key-value pairs such as `TYPE`, `DBID`, `SESID`, `DBUSER`, `ACTION`, and `RETCODE`.

**Note:** Only a subset of unified audit record fields are written to syslog. The complete audit record is stored in the `UNIFIED_AUDIT_TRAIL` view within the database. Syslog entries are typically limited to 1024 bytes.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`ACTION` | `security_result.action_details` | The value of `ACTION` from the raw log is directly mapped to this UDM field. Additional logic is applied to determine `security_result.action` and `security_result.description` based on the value of `ACTION` (for example, `100` maps to `ALLOW` and `Success`).  
`ACTION_NAME` | `metadata.product_event_type` | Directly mapped.  
`ACTION_NUMBER` | `additional.fields[action_number].value.string_value` | Directly mapped with the key `Source Event`. Also used in combination with other fields to derive `metadata.event_type` and `metadata.product_event_type`.  
`APPLICATION_CONTEXTS` | `additional.fields[application_contexts_label].value.string_value` | Directly mapped with the key `APPLICATION_CONTEXTS`.  
`AUDIT_POLICY` | `additional.fields[audit_policy_label].value.string_value` or `additional.fields[AUDIT_POLICY_#].value.string_value` | If `AUDIT_POLICY` contains a comma, it's split into multiple labels with keys like `AUDIT_POLICY_0`, `AUDIT_POLICY_1`, etc. Otherwise, it's mapped directly with the key `AUDIT_POLICY`.  
`AUDIT_TYPE` | `additional.fields[audit_type_label].value.string_value` | Directly mapped with the key `AUDIT_TYPE`.  
`AUTHENTICATION_TYPE` | `metadata.event_type`, `extensions.auth.type` | Used to derive `metadata.event_type` as `USER_LOGIN` if `auth_type` (extracted from `AUTHENTICATION_TYPE`) is not empty and other conditions are met. `extensions.auth.type` is set to `AUTHTYPE_UNSPECIFIED`.  
`CLIENT_ADDRESS` | `principal.ip`, `principal.port`, `network.ip_protocol`, `intermediary[host].user.userid` | IP, port, and protocol are extracted using grok patterns. If a username is present in the `CLIENT_ADDRESS` field, it's mapped to `intermediary[host].user.userid`.  
`CLIENT_ID` | `target.user.userid` | Directly mapped.  
`CLIENT_PROGRAM_NAME` | `additional.fields[client_program_name_label].value.string_value` | Directly mapped with the key `CLIENT_PROGRAM_NAME`.  
`CLIENT_TERMINAL` | `additional.fields[CLIENT_TERMINAL_label].value` | Directly mapped with the key `CLIENT_TERMINAL`.  
`CLIENT_USER` | `target.user.user_display_name` | Directly mapped.  
`COMMENT$TEXT` | `additional.fields[comment_text_label].value.string_value` | Directly mapped with the key `comment_text` after replacing `+` with `:`.  
`CURRENT_USER` | `additional.fields[current_user_label].value.string_value` | Directly mapped with the key `current_user`.  
`CURUSER` | `additional.fields[current_user_label].value.string_value` | Directly mapped with the key `current_user`.  
`DATABASE_USER` | `principal.user.user_display_name` | Directly mapped if not empty or `/`.  
`DBID` | `metadata.product_log_id` | Directly mapped after removing single quotes.  
`DBNAME` | `target.resource.resource_type`, `target.resource.resource_subtype`, `target.resource.name` | Sets `resource_type` to `DATABASE`, `resource_subtype` to `Oracle Database`, and maps `DBNAME` to `name`.  
`DBPROXY_USERRNAME` | `intermediary[dbproxy].user.userid` | Directly mapped.  
`DBUSERNAME` | `target.user.user_display_name` | Directly mapped.  
`ENTRYID` | `target.resource.attribute.labels[entry_id_label].value` | Directly mapped with the key `Entry Id`.  
`EXTERNAL_USERID` | `additional.fields[external_userid_label].value.string_value` | Directly mapped with the key `EXTERNAL_USERID`.  
`LENGTH` | `additional.fields[length_label].value.string_value` | Directly mapped with the key `length`.  
`LOGOFF$DEAD` | `target.resource.attribute.labels[LOGOFFDEAD_label].value` | Directly mapped with the key `LOGOFFDEAD`.  
`LOGOFF$LREAD` | `target.resource.attribute.labels[LOGOFFLREAD_label].value` | Directly mapped with the key `LOGOFFLREAD`.  
`LOGOFF$LWRITE` | `target.resource.attribute.labels[LOGOFFLWRITE_label].value` | Directly mapped with the key `LOGOFFLWRITE`.  
`LOGOFF$PREAD` | `target.resource.attribute.labels[LOGOFFPREAD_label].value` | Directly mapped with the key `LOGOFFPREAD`.  
`NTIMESTAMP#` | `metadata.event_timestamp` | Parsed and converted to RFC 3339 or ISO8601 format.  
`OBJCREATOR` | `target.resource.attribute.labels[obj_creator_label].value` | Directly mapped with the key `OBJ Creator`.  
`OBJNAME` | `target.resource.attribute.labels[obj_name_label].value` | Directly mapped with the key `OBJ Name`.  
`OS_USERNAME` | `principal.user.user_display_name` | Directly mapped.  
`OSUSERID` | `target.user.userid` | Directly mapped.  
`PDB_GUID` | `principal.resource.product_object_id` | Directly mapped.  
`PRIV$USED` | `additional.fields[privused_label].value.string_value` | Directly mapped with the key `privused`.  
`PRIVILEGE` | `principal.user.attribute.permissions.name` | Directly mapped.  
`RETURN_CODE` | `security_result.summary` | Directly mapped. Logic is applied to derive `security_result.action` and `security_result.description`.  
`RETURNCODE` | `security_result.summary` | Directly mapped. Logic is applied to derive `security_result.action` and `security_result.description`.  
`RLS_INFO` | `additional.fields[rls_info_label].value.string_value` | Directly mapped with the key `RLS_INFO`.  
`SCHEMA` | `additional.fields[schema_label].value.string_value` | Directly mapped with the key `schema`.  
`SESSIONCPU` | `target.resource.attribute.labels[SESSIONCPU_label].value` | Directly mapped with the key `SESSIONCPU`.  
`SESSIONID` | `network.session_id` | Directly mapped.  
`SESID` | `network.session_id` | Directly mapped.  
`SQL_TEXT` | `target.process.command_line` | Directly mapped.  
`SQLTEXT` | `target.process.command_line` | Directly mapped.  
`STATEMENT` | `target.resource.attribute.labels[statement_label].value` | Directly mapped with the key `STATEMENT`.  
`STATUS` | `security_result.summary` | Directly mapped. Logic is applied to derive `security_result.action` and `security_result.description`.  
`SYSTEM_PRIVILEGE_USED` | `additional.fields[system_privilege_used_label].value.string_value` | Directly mapped with the key `SYSTEM_PRIVILEGE_USED`.  
`TARGET_USER` | `additional.fields[target_user_label].value.string_value` | Directly mapped with the key `TARGET_USER`.  
`TERMINAL` | `additional.fields[CLIENT_TERMINAL_label].value` | Directly mapped with the key `CLIENT_TERMINAL`.  
`TYPE` | `additional.fields[type_label].value.string_value` | Directly mapped with the key `type`.  
`USERHOST` | `principal.hostname`, `principal.administrative_domain` | Hostname and domain are extracted using grok patterns.  
`USERID` | `principal.user.userid` | Directly mapped.  
`device_host_name` | `target.hostname` | Directly mapped.  
`event_name` | `metadata.product_event_type` | Directly mapped after converting to uppercase.  
`file_name` | `target.file.full_path` | Directly mapped.  
`hostname` | `principal.hostname` | Directly mapped.  
`length` | `additional.fields[length_label].value.string_value` | Directly mapped with the key `length`.  
`log_source_name` | `principal.application` | Directly mapped.  
`message` | Various | Used for grok parsing to extract several fields.  
`returncode` | `RETURNCODE` | Directly mapped.  
`src_ip` | `principal.ip` | Directly mapped.  
`t_hostname` | `target.hostname` | Directly mapped.  
(Parser Logic) | `metadata.vendor_name` | Hardcoded to `Oracle`.  
(Parser Logic) | `metadata.product_name` | Hardcoded to `Oracle DB`.  
(Parser Logic) | `metadata.event_type` | Determined based on the values of `ACTION`, `ACTION_NUMBER`, `source_event`, `OSUSERID`, `USERID`, `SQLTEXT`, `AUTHENTICATION_TYPE`, `DBUSERNAME`, `device_host_name`, `database_name`. Defaults to `USER_RESOURCE_ACCESS` if no specific condition is met.  
(Parser Logic) | `metadata.product_event_type` | Determined based on the values of `ACTION`, `ACTION_NUMBER`, `source_event`, `p_event_type`, `ACTION_NAME`.  
(Parser Logic) | `metadata.log_type` | Hardcoded to `ORACLE_DB`.  
(Parser Logic) | `extensions.auth.mechanism` | Set to `USERNAME_PASSWORD` under certain conditions based on `ACTION`, `ACTION_NUMBER`, `source_event`, and `OSUSERID`.  
(Parser Logic) | `extensions.auth.type` | Set to `AUTHTYPE_UNSPECIFIED` under certain conditions based on `ACTION`, `ACTION_NUMBER`, and `AUTHENTICATION_TYPE`.  
(Parser Logic) | `security_result.description` | Derived from `RETURNCODE` or `STATUS`.  
(Parser Logic) | `security_result.action` | Derived from `RETURNCODE` or `STATUS`.  
(Parser Logic) | `target.resource.attribute.labels` | Several labels are added based on the presence and values of various log fields.  
(Parser Logic) | `additional.fields` | Several fields are added as key-value pairs based on the presence and values of various log fields.  
(Parser Logic) | `intermediary` | Created and populated based on the presence and values of `DBPROXY_USERRNAME` and `CLIENT_ADDRESS`.  
(Parser Logic) | `network.ip_protocol` | Derived from protocol extracted from `CLIENT_ADDRESS` using an include file `parse_ip_protocol.include`.  
`has_target_user` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`GRANTEE` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`EXTENDED_TIMESTAMP` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`USERNAME` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`SRC_DATABASE` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`DBID` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`OBJ_NAME` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`OS_USERNAME` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`OWNER` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`NEW_OWNER` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`NEW_NAME` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`OBJ_PRIVILEGE` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ADMIN_OPTION` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SES_ACTIONS` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`LOGOFF_TIME` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`LOGOFF_LREAD` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`LOGOFF_PREAD` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`LOGOFF_LWRITE` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`LOGOFF_DLOCK` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ECONTEXT_ID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SESSION_CPU` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`PROXY_SESSIONID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`GLOBAL_UID` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SQL_BIND` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`SQL_TEXT` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`OBJ_EDITION_NAME` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`COMMENT_TEXT` | `event.idm.read_only_udm.security_result.description` | Mapped from changelog  
`comment_principal_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`comment_principal_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`priority` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`facility` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`inter_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`inter_port` | `event.idm.read_only_udm.intermediary.port` | Mapped from changelog  
`HOST_ID` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`SYS_PRIVILEGE` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`PRIV_USED` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`OS_PROCESS` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`TRANSACTIONID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`SCN` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`INSTANCE_NUMBER` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`ENTRY_ID` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`STATEMENTID` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`intermediary_hostname` | `event.idm.read_only_udm.intermediary_hostname` | Mapped from changelog  
`org_id" and "comp_id` | `additional.fields` | Mapped from changelog  
`host_addr` | `principal.ip` | Mapped from changelog  
`host_id` | `principal.hostname` | Mapped from changelog  
`level` | `security_result.severity_details` | Mapped from changelog  
`LENGTH", "LOGOFFDEAD", "LOGOFFLREAD", "LOGOFFLWRITE", "LOGOFFPREAD", "SESSIONCPU", "CLIENT_TERMINAL` | `target.resource.attribute.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-db-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
