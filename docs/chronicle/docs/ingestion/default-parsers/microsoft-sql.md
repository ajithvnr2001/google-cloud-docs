---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-sql/
title: Collect Microsoft SQL Server logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:29.569523+00:00
---

# Collect Microsoft SQL Server logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft SQL Server logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Microsoft SQL Server logs to Google Security Operations using Bindplane. The parser handles both structured (JSON, key-value pairs) and semi-structured (syslog) Microsoft SQL Server logs. It extracts fields, normalizes timestamps, handles different log formats based on `SourceModuleType` and `Message` content (including audit, login, and database events), and maps them to the UDM. It also performs specific parsing logic for audit records, login attempts, and database operations, enriching the data with additional context and severity information.collects SQL Server Audit and Error logs from Windows Event Log using a syslog forwarder (NXLog) and sends them to the BindPlane agent for delivery to Google SecOps.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows Server 2016 or later host running Microsoft SQL Server
  * Administrative access to install and configure BindPlane Agent and NXLog
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements



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



## Install Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Additional installation resources

For additional installation options, consult the [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file: 
     * Locate the `config.yaml` file. Typically, it's in the `C:\Program Files\observIQ\bindplane-agent` directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
             udplog:
               # Replace the port and IP address as required
               listen_address: "0.0.0.0:1514"
         
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
               customer_id: <YOUR_CUSTOMER_ID>
               endpoint: chronicle.googleapis.com
               # Add optional ingestion labels for better organization
               log_type: 'MICROSOFT_SQL'
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

**Note:** Ensure Windows Firewall allows inbound UDP traffic on port 1514. If you change the port, update both the BindPlane receiver configuration and the NXLog output port to match.

### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: <YOUR_CUSTOMER_ID>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'MICROSOFT_SQL'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
        
        net stop BindPlaneAgent && net start BindPlaneAgent
        




## Enable SQL Server Audit in Windows Event Log

You can enable SQL Server Audit using either the SQL Server Management Studio (SSMS) GUI or T-SQL commands. Choose the option that best suits your environment.

### Option 1: Enable SQL Server Audit via SSMS GUI

#### Create Server Audit in SQL Server Management Studio UI

  1. Open **SQL Server Management Studio (SSMS)** and connect to your SQL Server instance.
  2. In **Object Explorer** , expand your server instance.
  3. Expand the **Security** folder.
  4. Right-click on **Audits** and select **New Audit**.
  5. In the **Create Audit** dialog, provide the following configuration details: 
     * **Audit name** : Enter `ChronicleAudit`.
     * **Queue delay (in milliseconds)** : Enter `1000`.
     * **On audit log failure** : Select **Continue**.
     * **Audit destination** : Select **Application Log**.
  6. Click **OK** to create the audit.
  7. In **Object Explorer** , right-click on the newly created **ChronicleAudit** and select **Enable Audit**.



#### Create Server Audit Specification via SSMS GUI

  1. In **Object Explorer** , expand **Security**.
  2. Right-click on **Server Audit Specifications** and select **New Server Audit Specification**.
  3. In the **Create Server Audit Specification** dialog, provide the following configuration details: 
     * **Name** : Enter `ChronicleAuditSpec`.
     * **Audit** : Select **ChronicleAudit** from the menu.
  4. In the **Audit Action Type** section, click **Add** and select the following audit action groups (add each one individually by clicking **Add** after selecting each): 
     * **FAILED_LOGIN_GROUP**
     * **SUCCESSFUL_LOGIN_GROUP**
     * **LOGOUT_GROUP**
     * **SERVER_ROLE_MEMBER_CHANGE_GROUP**
     * **DATABASE_OBJECT_CHANGE_GROUP**
     * **DATABASE_PRINCIPAL_CHANGE_GROUP**
     * **SCHEMA_OBJECT_CHANGE_GROUP**
     * **DATABASE_PERMISSION_CHANGE_GROUP**
  5. Click **OK** to create the audit specification.
  6. In **Object Explorer** , right-click on the newly created **ChronicleAuditSpec** and select **Enable Server Audit Specification**.



#### Verify Audit Configuration

  1. In **Object Explorer** , expand **Security > Audits**.
  2. Right-click on **ChronicleAudit** and select **Properties**.
  3. Verify that the **Status** shows as **Started** or **Enabled**.
  4. Expand **Security > Server Audit Specifications**.
  5. Right-click on **ChronicleAuditSpec** and select **Properties**.
  6. Verify that all eight audit action groups are listed and the specification is enabled.



### Option 2: Enable SQL Server Audit using T-SQL

  1. Open **SQL Server Management Studio (SSMS)** and connect to your SQL Server instance.
  2. Execute the following T-SQL commands to create a server audit that writes to the Windows Application Log:
         
         USE master;
         GO
         
         CREATE SERVER AUDIT ChronicleAudit
         TO APPLICATION_LOG
         WITH (QUEUE_DELAY = 1000, ON_FAILURE = CONTINUE);
         GO
         
         ALTER SERVER AUDIT ChronicleAudit WITH (STATE = ON);
         GO
         

  3. Create an audit specification to capture relevant security events:
         
         CREATE SERVER AUDIT SPECIFICATION ChronicleAuditSpec
         FOR SERVER AUDIT ChronicleAudit
         ADD (FAILED_LOGIN_GROUP),
         ADD (SUCCESSFUL_LOGIN_GROUP),
         ADD (LOGOUT_GROUP),
         ADD (SERVER_ROLE_MEMBER_CHANGE_GROUP),
         ADD (DATABASE_OBJECT_CHANGE_GROUP),
         ADD (DATABASE_PRINCIPAL_CHANGE_GROUP),
         ADD (SCHEMA_OBJECT_CHANGE_GROUP),
         ADD (DATABASE_PERMISSION_CHANGE_GROUP);
         GO
         
         ALTER SERVER AUDIT SPECIFICATION ChronicleAuditSpec WITH (STATE = ON);
         GO
         




This configuration ensures authentication events, permission changes, and object modifications are logged to the Windows Event Log.

## Install and configure NXLog to forward events to Bindplane

  1. Download **NXLog Community Edition** from [nxlog.co/downloads](https://nxlog.co/downloads).
  2. Run the installer and complete the installation wizard.
  3. Open the NXLog configuration file located at:
         
         C:\Program Files\nxlog\conf\nxlog.conf
         

  4. Replace the contents with the following configuration:
         
         define ROOT C:\Program Files\nxlog
         Moduledir %ROOT%\modules
         CacheDir %ROOT%\data
         Pidfile %ROOT%\data\nxlog.pid
         SpoolDir %ROOT%\data
         LogFile %ROOT%\data\nxlog.log
         
         <Extension _json>
            Module      xm_json
         </Extension>
         
         <Input in_eventlog>
            Module      im_msvistalog
            Query       <QueryList>\
                           <Query Id="0">\
                                 <Select Path="Application">*[System[Provider[@Name='MSSQLSERVER']]]</Select>\
                           </Query>\
                        </QueryList>
         </Input>
         
         <Output out_syslog>
            Module      om_udp
            Host        127.0.0.1
            Port        1514
            Exec        to_json();
         </Output>
         
         <Route r1>
            Path        in_eventlog => out_syslog
         </Route>
         

     * Replace the **Host** current value `127.0.0.1` with the Bindplane agent IP address.
     * Ensure the **Port** value matches the Bindplane `udplog` receiver port configured earlier.
  5. Save the file and restart the NXLog service:
         
         net stop nxlog && net start nxlog
         




## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`AccountName` | `principal.user.userid` | Used for `principal.user.userid` if present in logs like Starting up database or Log was backed up.  
`AgentDevice` | `additional.fields` | Added as a key-value pair to `additional.fields` with key "AgentDevice".  
`AgentLogFile` | `additional.fields` | Added as a key-value pair to `additional.fields` with key "AgentLogFile".  
`agent.hostname` | `observer.asset.hostname` | Maps to observer hostname.  
`agent.id` | `observer.asset_id` | Concatenated with `agent.type` to form `observer.asset_id`.  
`agent.type` | `observer.asset_id` | Concatenated with `agent.id` to form `observer.asset_id`.  
`agent.version` | `observer.platform_version` | Maps to observer platform version.  
`ApplicationName` | `principal.application` | Maps to principal application.  
`application_name` | `target.application` | Maps to target application.  
`client_address` | `principal.ip` | Used for principal IP if different from host and not local or named pipe.  
`client_ip` | `principal.ip` | Maps to principal IP.  
`computer_name` | `about.hostname` | Maps to about hostname.  
`correlationId` | `security_result.detection_fields` | Added as a key-value pair to `security_result.detection_fields` with key "correlationId".  
`Date` | `metadata.event_timestamp` | Combined with `Time` to create the event timestamp.  
`database_name` | `target.resource_ancestors.name` | Used for target resource ancestor name if present in audit logs.  
`durationMs` | `network.session_duration.seconds` | Converted from milliseconds to seconds and mapped.  
`ecs.version` | `metadata.product_version` | Maps to product version.  
`error` | `security_result.detection_fields` | Added as a key-value pair to `security_result.detection_fields` with key "error".  
`err_msg` | `security_result.description` | Maps to security result description.  
`EventID` | `metadata.product_event_type` | Used to construct product event type if other fields are not available, prefixed with "EventID: ".  
`event.action` | `Source` | Used as a source if present.  
`event.code` | `metadata.product_event_type` | Combined with `event.provider` to form `metadata.product_event_type`.  
`event.provider` | `metadata.product_event_type` | Combined with `event.code` to form `metadata.product_event_type`.  
`EventReceivedTime` | `metadata.ingested_timestamp` | Parsed and used as ingested timestamp.  
`event_time` | `metadata.event_timestamp` | Parsed and used as event timestamp.  
`file_name` | `principal.process.file.full_path` | Maps to principal process file full path.  
`file_path` | `target.file.full_path` | Used for target file full path if found in backup logs.  
`first_lsn` | `target.resource.attribute.labels` | Added as a key-value pair to `target.resource.attribute.labels` with key "First LSN".  
`host` | `principal.hostname`, `observer.hostname` | Used for principal or observer hostname if not an IP. Also used for target hostname or IP depending on whether it's an IP or not.  
`host.ip` | `principal.ip` | Merged into principal IP.  
`host.name` | `host` | Used as host if present.  
`Hostname` | `principal.hostname`, `target.hostname` | Used for principal or target hostname if present.  
`hostinfo.architecture` | `principal.asset.hardware.cpu_platform` | Maps to principal asset hardware cpu platform.  
`hostinfo.os.build` | `additional.fields` | Added as a key-value pair to `additional.fields` with key "os_build".  
`hostinfo.os.kernel` | `principal.platform_patch_level` | Maps to principal platform patch level.  
`hostinfo.os.name` | `additional.fields` | Added as a key-value pair to `additional.fields` with key "os_name".  
`hostinfo.os.platform` | `principal.platform` | Uppercased and mapped to principal platform.  
`hostinfo.os.version` | `principal.platform_version` | Maps to principal platform version.  
`last_lsn` | `target.resource.attribute.labels` | Added as a key-value pair to `target.resource.attribute.labels` with key "Last LSN".  
`level` | `security_result.severity` | If "Informational", sets `security_result.severity` to "INFORMATIONAL".  
`log.level` | `security_result.severity_details` | Maps to security result severity details.  
`LoginName` | `principal.user.userid` | Used for principal user ID if present in KV logs.  
`login_result` | `security_result.action` | Determines security result action (ALLOW or BLOCK).  
`logon_user` | `principal.user.userid` | Used for principal user ID if present in login logs.  
`logstash.process.host` | `intermediary.hostname` | Maps to intermediary hostname.  
`Message` | `metadata.description`, `security_result.description` | Used for event description or security result description depending on the log type.  
`msg` | `metadata.description` | Used for event description if present.  
`ObjectName` | `target.resource.name` | Maps to target resource name.  
`object_name` | `target.resource.name` | Used for target resource name if present in audit logs.  
`ObjectType` | `target.resource.type` | Maps to target resource type.  
`operationId` | `security_result.detection_fields` | Added as a key-value pair to `security_result.detection_fields` with key "operationId".  
`operationName` | `metadata.product_event_type` | Maps to product event type.  
`operationVersion` | `additional.fields` | Added as a key-value pair to `additional.fields` with key "operationVersion".  
`ProcessInfo` | `additional.fields` | Added as a key-value pair to `additional.fields` with key "ProcessInfo".  
`properties.apiVersion` | `metadata.product_version` | Maps to product version.  
`properties.appId` | `target.resource.product_object_id` | Maps to target resource product object ID.  
`properties.clientAuthMethod` | `extensions.auth.auth_details` | Used to determine authentication details.  
`properties.clientRequestId` | `additional.fields` | Added as a key-value pair to `additional.fields` with key "clientRequestId".  
`properties.durationMs` | `network.session_duration.seconds` | Converted to seconds and mapped.  
`properties.identityProvider` | `security_result.detection_fields` | Added as a key-value pair to `security_result.detection_fields` with key "identityProvider".  
`properties.ipAddress` | `principal.ip`, `principal.asset.ip` | Parsed for IP and merged into principal IP and principal asset IP.  
`properties.location` | `principal.location.name` | Maps to principal location name.  
`properties.operationId` | `security_result.detection_fields` | Added as a key-value pair to `security_result.detection_fields` with key "operationId".  
`properties.requestId` | `metadata.product_log_id` | Maps to product log ID.  
`properties.requestMethod` | `network.http.method` | Maps to network HTTP method.  
`properties.requestUri` | `target.url` | Maps to target URL.  
`properties.responseSizeBytes` | `network.received_bytes` | Converted to unsigned integer and mapped.  
`properties.responseStatusCode` | `network.http.response_code` | Converted to integer and mapped.  
`properties.roles` | `additional.fields` | Added as a key-value pair to `additional.fields` with key "roles".  
`properties.servicePrincipalId` | `principal.user.userid` | Used for principal user ID if `properties.userId` is not present.  
`properties.signInActivityId` | `network.session_id` | Maps to network session ID.  
`properties.tenantId` | `metadata.product_deployment_id` | Maps to product deployment ID.  
`properties.tokenIssuedAt` | `additional.fields` | Added as a key-value pair to `additional.fields` with key "tokenIssuedAt".  
`properties.userAgent` | `network.http.user_agent` | Maps to network HTTP user agent.  
`properties.userId` | `principal.user.userid` | Used for principal user ID if present.  
`properties.wids` | `security_result.detection_fields` | Added as a key-value pair to `security_result.detection_fields` with key "wids".  
`reason` | `security_result.summary` | Used for security result summary in login events.  
`resourceId` | `target.resource.attribute.labels` | Added as a key-value pair to `target.resource.attribute.labels` with key "Resource ID".  
`schema_name` | `target.resource_ancestors.resource_subtype` | Used for target resource ancestor subtype if present in audit logs.  
`security_result.description` | `metadata.description` | Used for event description if not an audit event.  
`security_result.severity` | `security_result.severity` | Maps directly if present. Set to "LOW" for KV logs, "INFORMATIONAL" for certain error messages, and derived from `level` or `Severity` fields.  
`security_result.severity_details` | `security_result.severity_details` | Maps directly if present.  
`security_result.summary` | `security_result.summary` | Maps directly if present. Set to "Connection made using Windows authentication" or specific reasons from login events, or "SQL Server Audit Record" for audit events.  
`security_result_action` | `security_result.action` | Merged into `security_result.action`. Set to "ALLOW" for most events, and derived from `login_result` for login events.  
`server_instance_name` | `target.hostname` | Used for target hostname if present in audit logs.  
`server_principal_name` | `principal.user.userid` | Used for principal user ID if present in audit logs.  
`server_principal_sid` | `principal.asset_id` | Used to construct principal asset ID, prefixed with "server SID:".  
`session_id` | `network.session_id` | Used for network session ID if present in audit logs.  
`sev` | `security_result.severity` | Used to determine security result severity.  
`Severity` | `security_result.severity` | Used to determine security result severity.  
`Source` | `additional.fields` | Added as a key-value pair to `additional.fields` with key "Source".  
`source` | `principal.resource.attribute.labels` | Added as a key-value pair to `principal.resource.attribute.labels` with key "source".  
`SourceModuleType` | `observer.application` | Maps to observer application.  
`SourceModuleName` | `additional.fields` | Added as a key-value pair to `additional.fields` with key "SourceModuleName".  
`source_module_name` | `observer.labels` | Added as a key-value pair to `observer.labels` with key "SourceModuleName".  
`source_module_type` | `observer.application` | Maps to observer application.  
`SPID` | `network.session_id` | Maps to network session ID.  
`statement` | `target.process.command_line` | Used for target process command line if present in audit logs.  
`TextData` | `security_result.description`, `metadata.description` | Used for security result description if not a login event, or event description if it is.  
`time` | `metadata.event_timestamp` | Parsed and used as event timestamp.  
`Time` | `metadata.event_timestamp` | Combined with `Date` to create the event timestamp.  
`transaction_id` | `target.resource.attribute.labels` | Added as a key-value pair to `target.resource.attribute.labels` with key "transaction_id".  
`UserID` | `principal.user.windows_sid` | Used for principal user Windows SID if present and in the correct format.  
`user_id` | `principal.user.userid` | Used for principal user ID if present.  
`metadata.log_type` | `metadata.log_type` | Hardcoded to "MICROSOFT_SQL".  
`metadata.vendor_name` | `metadata.vendor_name` | Hardcoded to "Microsoft".  
`metadata.product_name` | `metadata.product_name` | Hardcoded to "SQL Server".  
`metadata.event_type` | `metadata.event_type` | Set to various values depending on the log content, including "USER_LOGIN", "USER_LOGOUT", "STATUS_STARTUP", "STATUS_SHUTDOWN", "NETWORK_HTTP", "GENERIC_EVENT", and "STATUS_UNCATEGORIZED" as a default.  
`extensions.auth.type` | `extensions.auth.type` | Set to "MACHINE" for login and logout events.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-sql-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
