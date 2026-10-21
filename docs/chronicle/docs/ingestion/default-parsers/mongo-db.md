---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mongo-db/
title: Collect MongoDB logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:41.551357+00:00
---

# Collect MongoDB logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mongo-db/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect MongoDB logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest MongoDB logs to Google Security Operations using Bindplane.

MongoDB is a NoSQL document database that generates audit logs for CRUD operations, authentication events, database commands, and replica set operations. MongoDB writes structured JSON log files locally, which the Bindplane agent can collect directly from the file system.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the MongoDB server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the MongoDB server (root or database administrator role)
  * MongoDB Enterprise or MongoDB Community Edition with [audit logging](https://www.mongodb.com/docs/manual/core/auditing/) enabled



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

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest logs and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          filelog:
            include:
              - /var/log/mongodb/auditLog.json
            start_at: beginning
        
        exporters:
          chronicle/mongodb:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: MONGO_DB
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/mongodb_to_chronicle:
              receivers:
                - filelog
              exporters:
                - chronicle/mongodb
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `filelog`: The receiver type for collecting log files from disk
    * `include`: List of file paths to monitor: 
      * **Linux** : `/var/log/mongodb/auditLog.json` (default MongoDB audit log path)
      * **Windows** : `C:\data\log\auditLog.json` or your configured audit log path
    * `start_at`: Set to `beginning` to read existing logs or `end` to only read new entries
  * **Exporter configuration:**

    * `mongodb`: Descriptive name for the exporter
    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<customer_id>`: Customer ID from the previous step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `MONGO_DB`: Log type exactly as it appears in Chronicle
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`)
  * **Pipeline configuration:**

    * `mongodb_to_chronicle`: Descriptive name for the pipeline



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/mongodb:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: MONGO_DB
            raw_log_field: body
            ingestion_labels:
              env: production
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux: 

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows:

  1. Choose one of the following options:

     * Command Prompt or PowerShell as administrator:
    
    net stop observiq-otel-collector && net start observiq-otel-collector
    

     * Services console: 
       1. Press `Win+R`, type `services.msc`, and press Enter.
       2. Locate **observIQ OpenTelemetry Collector**.
       3. Right-click and select **Restart**.
  2. Verify the service is running:
         
         sc query observiq-otel-collector
         

  3. Check logs for errors:
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         




## Configure MongoDB to generate audit logs

  1. Sign in to the **MongoDB** server with administrator or root privileges.
  2. Open the MongoDB configuration file (`mongod.conf`). Default locations: 
     * **Linux** : `/etc/mongod.conf`
     * **Windows** : `C:\Program Files\MongoDB\Server\<version>\bin\mongod.cfg`
  3. Verify that audit logging is enabled. In the `mongod.conf` file, confirm the following settings:

     * `auditLog.destination` is set to `file`.
     * `auditLog.format` is set to `JSON`.
     * Note the `auditLog.path` (for example, `/var/log/mongodb/auditLog.json`).

     * If audit logging is not enabled, add the following to `mongod.conf`:
    
    auditLog:
      destination: file
      format: JSON
      path: /var/log/mongodb/auditLog.json
    

  4. Restart the MongoDB service to apply the configuration:

     * **Linux** :
           
           sudo systemctl restart mongod
           

     * **Windows** :
           
           net stop MongoDB && net start MongoDB
           

  5. Verify that the audit log file is being written at the configured path (for example, `/var/log/mongodb/auditLog.json`).

  6. Ensure the Bindplane agent `include` path in `config.yaml` matches the `auditLog.path` configured in `mongod.conf`.

**Note:** MongoDB Enterprise is required for the audit logging feature. MongoDB Community Edition does not include built-in audit logging. Make sure the audit log path is readable by the Bindplane agent service account.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
ctx, connectionId, connectionCount, attr.protocol, attr.storage.data.bytesRead, attr.storage.data.timeReadingMicros, attr.command.$readPreference.mode, attr.queryHash, param_old, cluster_node, param.indexName, temp_db_value | additional.fields | Merged from various fields based on conditions  
db_mechanism, param.mechanism | extensions.auth.auth_details | Value from db_mechanism if not empty, else param.mechanism  
| extensions.auth.mechanism | Set to "MECHANISM_OTHER"  
| extensions.auth.type | Set to "AUTHTYPE_UNSPECIFIED"  
lb_hostname, src_hostname | intermediary.hostname | Value from lb_hostname if not empty, else src_hostname  
lb_port, src_port | intermediary.port | Value from lb_port if not empty, else src_port (converted to integer)  
msg | metadata.description | Value copied directly  
| metadata.event_type | Set based on msg_atype, category, param_passwordChanged, param_command, remote_ip conditions  
msg_atype, category | metadata.product_event_type | Value from msg_atype if not empty, else category  
id, type, traceId | metadata.product_log_id | Value from id if not empty, else uuid.$binary if type == "04", else traceId  
| metadata.product_name | Set to "MongoDB Enterprise"  
| metadata.vendor_name | Set to "MongoDB"  
application_name | principal.application | Value copied directly  
accessLog.hostname | principal.asset.hostname | Value copied directly  
remote_ip | principal.asset.ip | Value copied directly  
software_label | principal.asset.software | Merged from software_label  
accessLog.hostname | principal.hostname | Value copied directly  
remote_ip | principal.ip | Value copied directly  
os_type | principal.platform | Set to WINDOWS if matches Windows; MAC if matches osx or mac; LINUX if matches Linux  
os_name, param.clientMetadata.os.name | principal.platform_patch_level | Value from os_name if not empty, else param.clientMetadata.os.name  
os_version, param.clientMetadata.os.version | principal.platform_version | Value from os_version if not empty, else param.clientMetadata.os.version  
remote_port | principal.port | Converted to integer  
principal_userid | principal.user.userid | Value copied directly  
sr_action | security_result.action | Value copied directly  
param.reason, param.indexBuildState | security_result.description | Value from param.reason if msg_atype == "logout"; from param.indexBuildState if msg_atype in ["createIndex", "dropIndex"]  
severity, level | security_result.severity | Set to INFORMATIONAL if severity in ["i", "I"] or level in ["INFO", "DEBUG"]; ERROR if severity in ["e", "E"] or level == "ERROR"; MEDIUM if severity in ["w", "W", "f", "F"]  
msg_result, attr.error, attr.planSummary, reason, attr.msg_data | security_result.summary | Set based on msg_result, attr.error, attr.planSummary, reason, attr.msg_data conditions  
db_value | target.administrative_domain | Value copied directly  
application_name | target.application | Value copied directly  
local_ip | target.asset.ip | Value copied directly  
host_group | target.group.group_display_name | Value copied directly  
local_ip | target.ip | Value copied directly  
local_port | target.port | Converted to integer  
old_name_label, cluster_node_label, mode_label, query_hash_label, bytes_read_label, time_reading_micro_label, environment_label, area_label | target.resource.attribute.labels | Merged from various label fields  
param_ns, db_value, param_new, param.args.find | target.resource.name | Set based on msg_atype and param_command conditions  
| target.resource.resource_subtype | Set to "MongoDB Database" for database/user events; "MongoDB Collection" for collection events; "MongoDB Index" for index events  
| target.resource.resource_type | Set to "DATABASE" for database/user events; "TABLE" for collection/index events  
db_user, param.user | target.user.userid | Value from db_user if not empty, else param.user  
`service.name` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`host.name` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`host.name` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`mongodb.group.id` | `event.idm.read_only_udm.principal.group.product_object_id` | Mapped from changelog  
`mongodb.cluster.name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`mongodb.customer.cluster.name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`ts.date` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`uuid.binary` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`users.1.user` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`remote.ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`remote.port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`local.ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`local.port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`roles.role` | `event.idm.read_only_udm.principal.user.attribute.roles` | Mapped from changelog  
`param.args.client.application.name` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`param.args.client.os.type` | `event.idm.read_only_udm.principal.asset.platform_software.platform` | Mapped from changelog  
`param.args.client.os.version` | `event.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`param.args.client.os.architecture` | `event.idm.read_only_udm.principal.asset.hardware` | Mapped from changelog  
`atype` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`param.command` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`param.ns` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`result` | `event.idm.read_only_udm.security_result.action` | Mapped from changelog  
`mongodb.log.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.db` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`uuid.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.clientOperationKey.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.clientOperationKey.binary` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.aggregate` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.mayBypassWriteBlocking` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.configTime.timestamp.t` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.topologyTime.timestamp.t` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.audit` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.cursor.batchSize.numberLong` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.includeQueryStatsMetrics` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.fromMongos` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.readConcern.provenance` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.readConcern.level` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.writeConcern.provenance` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.writeConcern.level` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.client.platform` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.client.driver.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.client.driver.version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.client.os.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.clusterTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.lsid.id.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.lsid.uid.binary` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.users.1.db` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.client.mongos.version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.writeConcern.w` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.writeConcern.wtimeout` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.lsid.uid.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.pipeline.1.match.managedClusterType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.pipeline.2.group.n.sum.const` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.pipeline.2.group._id.const` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.client.mongos.client.port` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`param.args.audit.impersonatedRoles` | `event.idm.read_only_udm.principal.user.attribute.roles` | Mapped from changelog  
`param.args.audit.impersonatedUser` | `event.idm.read_only_udm.principal.user.attribute.labels` | Mapped from changelog  
`param.args.client.mongos.client` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`param.args.client.mongos.host` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`param.args.client.mongos.host` | `event.idm.read_only_udm.intermediary.port` | Mapped from changelog  
`accessLog.authResult` | `additional.fields` | Mapped from changelog  
`accessLog.authSource` | `additional.fields` | Mapped from changelog  
`accessLog.failureReason` | `additional.fields` | Mapped from changelog  
`accessLog.groupId` | `target.resource.product_object_id` | Mapped from changelog  
`accessLog.ipAddress` | `intermediary.ip` | Mapped from changelog  
`accessLog.logLine.t.$date` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.s` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.c` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.id` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.ctx` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.msg` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.attr.client` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.attr.isSpeculative` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.attr.isClusterMember` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.attr.mechanism` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.attr.user` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.attr.db` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.attr.result` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.attr.metrics.conversation_duration.micros` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.attr.metrics.conversation_duration.summary.step` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.attr.metrics.conversation_duration.summary.step_total` | `additional.fields` | Mapped from changelog  
`accessLog.logLine.attr.metrics.conversation_duration.summary.duration_micros` | `additional.fields` | Mapped from changelog  
`accessLog.username` | `target.user.user_display_name` | Mapped from changelog  
`accessLog.timestamp` | `additional.fields` | Mapped from changelog  
`roles.db` | `principal.user.attribute.roles` | Mapped from changelog  
`roles.db` | `target.user.attribute.roles` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mongo-db-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
