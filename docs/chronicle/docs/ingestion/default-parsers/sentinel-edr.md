---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinel-edr/
title: Collect SentinelOne EDR logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:02:07.209893+00:00
---

# Collect SentinelOne EDR logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sentinel-edr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect SentinelOne EDR logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to export SentinelOne logs to Google Cloud Storage using SentinelOne Cloud Funnel. Since SentinelOne doesn't offer a built-in integration to directly export logs to Google Cloud Storage, Cloud Funnel acts as an intermediary service to push logs to the Cloud Storage.

## Before you begin

Ensure you have the following prerequisites:

  * Google SecOps instance
  * Privileged access to the Google Cloud platform
  * Privileged access to SentinelOne



## Configure Permissions for Cloud Funnel to Access Cloud Storage

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to **IAM & Admin**.
  3. In the **IAM** page, add a **new IAM role** for the **Cloud Funnel service account** : 
     * Assign **Storage Object Creator** permissions.
     * Optional: assign **Storage Object Viewer** if you need Cloud Funnel to read objects from the bucket.
  4. Grant these permissions to the **Cloud Funnel service account**.



## Create a Cloud Storage Bucket

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to **Storage > Browser**.
  3. Click **Create bucket**.
  4. Provide the following configurations: 
     * **Bucket Name** : Choose a unique name for your bucket (for example, **sentinelone-logs**).
     * **Storage Location** : Select the region where the bucket will reside (for example, **US-West1**).
     * **Storage Class** : Choose a **Standard** storage class.
  5. Click **Create**.



## Configure Cloud Funnel in SentinelOne

  1. In the SentinelOne Console, go to **Settings**.
  2. Locate the **Cloud Funnel** option (under **Integrations**).
  3. If it's not already enabled, click **Enable Cloud Funnel**.
  4. Once enabled, you're prompted to configure the **Destination** settings. 
     * **Destination Selection** : Choose **Google Cloud Storage** as the destination for exporting logs.
     * **Google Cloud Storage** : Provide the Google Cloud Storage credentials.
     * **Log Export Frequency** : set the **frequency** for exporting logs (for example, hourly or daily).



## How to configure Cloud Funnel Log Export

  1. In the **Cloud Funnel Configuration** section of the SentinelOne Console, set the following: 
     * **Log Export Frequency** : Choose how often logs should be exported (for example. every hour or every day).
     * **Log Format** : Choose the **JSON** format.
     * **Bucket Name** : Enter the name of the **Google Cloud Storage bucket** you created earlier (for example, **sentinelone-logs**).
     * Optional: **Log Path Prefix** : Specify a **prefix** to organize logs within the bucket (for example, `sentinelone-logs/`).
  2. Once the settings are configured, click **Save** to apply the changes.



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds > Add New Feed**
  * **Content Hub > Content Packs > Get Started**



## How to set up the SentinelOne EDR feed

  1. Click the **SentinelOne** pack.
  2. Locate the **SentinelOne EDR** feed.
  3. Specify the values for the following fields: 
     * **Source type** : Google Cloud Storage V2.
     * **Storage bucket URI** : The Google Cloud Storage bucket source URI.
     * **Source deletion option** : Whether to delete files or directories after transferring. Select the **Delete transferred files** option in **Source deletion option**.
     * **Maximum File Age** : Include files modified within the last number of days. Default is 180 days. 
     * **Chronicle Service Account** : Copy the Service Account. You'll need it to add permissions in the bucket for this Service Account to let Google SecOps read or delete data in the bucket.



**Advanced options**

  * **Feed Name** : A prepopulated value that identifies the feed.
  * **Asset Namespace** : Namespace associated with the feed.
  * **Ingestion Labels** : Labels applied to all events from this feed.


  1. Click **Create feed**.

**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`event.contentHash.sha256` | `target.process.file.sha256` | The SHA-256 hash of the target process's file, extracted from the `event.contentHash.sha256` field in the raw log.  
`event.decodedContent` | `target.labels` | The decoded content of a script, extracted from the `event.decodedContent` field in the raw log. It is added as a label with the key `Decoded Content` to the target object.  
`event.destinationAddress.address` | `target.ip` | The IP address of the destination, extracted from the `event.destinationAddress.address` field in the raw log.  
`event.destinationAddress.port` | `target.port` | The port of the destination, extracted from the `event.destinationAddress.port` field in the raw log.  
`event.method` | `network.http.method` | The HTTP method of the event, extracted from the `event.method` field in the raw log.  
`event.newValueData` | `target.registry.registry_value_data` | The new value data of the registry value, extracted from the `event.newValueData` field in the raw log.  
`event.process.commandLine` | `target.process.command_line` | The command line of the process, extracted from the `event.process.commandLine` field in the raw log.  
`event.process.executable.hashes.md5` | `target.process.file.md5` | The MD5 hash of the process's executable, extracted from the `event.process.executable.hashes.md5` field in the raw log.  
`event.process.executable.hashes.sha1` | `target.process.file.sha1` | The SHA-1 hash of the process's executable, extracted from the `event.process.executable.hashes.sha1` field in the raw log.  
`event.process.executable.hashes.sha256` | `target.process.file.sha256` | The SHA-256 hash of the process's executable, extracted from the `event.process.executable.hashes.sha256` field in the raw log.  
`event.process.executable.path` | `target.process.file.full_path` | The full path of the process's executable, extracted from the `event.process.executable.path` field in the raw log.  
`event.process.executable.sizeBytes` | `target.process.file.size` | The size of the process's executable, extracted from the `event.process.executable.sizeBytes` field in the raw log.  
`event.process.fullPid.pid` | `target.process.pid` | The PID of the process, extracted from the `event.process.fullPid.pid` field in the raw log.  
`event.query` | `network.dns.questions.name` | The DNS query, extracted from the `event.query` field in the raw log.  
`event.regKey.path` | `target.registry.registry_key` | The path of the registry key, extracted from the `event.regKey.path` field in the raw log.  
`event.regValue.key.value` | `target.registry.registry_name`, `target.registry.registry_value_name` | The name of the registry value, extracted from the `event.regValue.key.value` field in the raw log.  
`event.regValue.path` | `target.registry.registry_key` | The path of the registry value, extracted from the `event.regValue.path` field in the raw log.  
`event.results` | `network.dns.answers.data` | The DNS answers, extracted from the `event.results` field in the raw log. The data is split into individual answers using the "`;`" separator.  
`event.source.commandLine` | `principal.process.command_line` | The command line of the source process, extracted from the `event.source.commandLine` field in the raw log.  
`event.source.executable.hashes.md5` | `principal.process.file.md5` | The MD5 hash of the source process's executable, extracted from the `event.source.executable.hashes.md5` field in the raw log.  
`event.source.executable.hashes.sha1` | `principal.process.file.sha1` | The SHA-1 hash of the source process's executable, extracted from the `event.source.executable.hashes.sha1` field in the raw log.  
`event.source.executable.hashes.sha256` | `principal.process.file.sha256` | The SHA-256 hash of the source process's executable, extracted from the `event.source.executable.hashes.sha256` field in the raw log.  
`event.source.executable.path` | `principal.process.file.full_path` | The full path of the source process's executable, extracted from the `event.source.executable.path` field in the raw log.  
`event.source.executable.signature.signed.identity` | `principal.resource.attribute.labels` | The signed identity of the source process's executable, extracted from the `event.source.executable.signature.signed.identity` field in the raw log. It is added as a label with the key `Source Signature Signed Identity` to the principal resource attribute labels.  
`event.source.executable.sizeBytes` | `principal.process.file.size` | The size of the source process's executable, extracted from the `event.source.executable.sizeBytes` field in the raw log.  
`event.source.fullPid.pid` | `principal.process.pid` | The PID of the source process, extracted from the `event.source.fullPid.pid` field in the raw log.  
`event.source.parent.commandLine` | `principal.process.parent_process.command_line` | The command line of the source parent process, extracted from the `event.source.parent.commandLine` field in the raw log.  
`event.source.parent.executable.hashes.md5` | `principal.process.parent_process.file.md5` | The MD5 hash of the source parent process's executable, extracted from the `event.source.parent.executable.hashes.md5` field in the raw log.  
`event.source.parent.executable.hashes.sha1` | `principal.process.parent_process.file.sha1` | The SHA-1 hash of the source parent process's executable, extracted from the `event.source.parent.executable.hashes.sha1` field in the raw log.  
`event.source.parent.executable.hashes.sha256` | `principal.process.parent_process.file.sha256` | The SHA-256 hash of the source parent process's executable, extracted from the `event.source.parent.executable.hashes.sha256` field in the raw log.  
`event.source.parent.executable.signature.signed.identity` | `principal.resource.attribute.labels` | The signed identity of the source parent process's executable, extracted from the `event.source.parent.executable.signature.signed.identity` field in the raw log. It is added as a label with the key `Source Parent Signature Signed Identity` to the principal resource attribute labels.  
`event.source.parent.fullPid.pid` | `principal.process.parent_process.pid` | The PID of the source parent process, extracted from the `event.source.parent.fullPid.pid` field in the raw log.  
`event.source.user.name` | `principal.user.userid` | The username of the source process's user, extracted from the `event.source.user.name` field in the raw log.  
`event.source.user.sid` | `principal.user.windows_sid` | The Windows SID of the source process's user, extracted from the `event.source.user.sid` field in the raw log.  
`event.sourceAddress.address` | `principal.ip` | The IP address of the source, extracted from the `event.sourceAddress.address` field in the raw log.  
`event.sourceAddress.port` | `principal.port` | The port of the source, extracted from the `event.sourceAddress.port` field in the raw log.  
`event.target.executable.hashes.md5` | `target.process.file.md5` | The MD5 hash of the target process's executable, extracted from the `event.target.executable.hashes.md5` field in the raw log.  
`event.target.executable.hashes.sha1` | `target.process.file.sha1` | The SHA-1 hash of the target process's executable, extracted from the `event.target.executable.hashes.sha1` field in the raw log.  
`event.target.executable.hashes.sha256` | `target.process.file.sha256` | The SHA-256 hash of the target process's executable, extracted from the `event.target.executable.hashes.sha256` field in the raw log.  
`event.target.executable.path` | `target.process.file.full_path` | The full path of the target process's executable, extracted from the `event.target.executable.path` field in the raw log.  
`event.target.executable.signature.signed.identity` | `target.resource.attribute.labels` | The signed identity of the target process's executable, extracted from the `event.target.executable.signature.signed.identity` field in the raw log. It is added as a label with the key `Target Signature Signed Identity` to the target resource attribute labels.  
`event.target.executable.sizeBytes` | `target.process.file.size` | The size of the target process's executable, extracted from the `event.target.executable.sizeBytes` field in the raw log.  
`event.target.fullPid.pid` | `target.process.pid` | The PID of the target process, extracted from the `event.target.fullPid.pid` field in the raw log.  
`event.targetFile.path` | `target.file.full_path` | The full path of the target file, extracted from the `event.targetFile.path` field in the raw log.  
`event.targetFile.signature.signed.identity` | `target.resource.attribute.labels` | The signed identity of the target file, extracted from the `event.targetFile.signature.signed.identity` field in the raw log. It is added as a label with the key `Target File Signature Signed Identity` to the target resource attribute labels.  
`event.trueContext.key.value` |  | Not mapped to the UDM.  
`event.type` | `metadata.description` | The type of the event, extracted from the `event.type` field in the raw log.  
`event.url` | `target.url` | The URL of the event, extracted from the `event.url` field in the raw log.  
`meta.agentVersion` | `metadata.product_version`, `metadata.product_version` | The version of the agent, extracted from the `meta.agentVersion` field in the raw log.  
`meta.computerName` | `principal.hostname`, `target.hostname` | The hostname of the computer, extracted from the `meta.computerName` field in the raw log.  
`meta.osFamily` | `principal.asset.platform_software.platform`, `target.asset.platform_software.platform` | The operating system family of the computer, extracted from the `meta.osFamily` field in the raw log. It is mapped to `LINUX` for `linux` and `WINDOWS` for `windows`.  
`meta.osRevision` | `principal.asset.platform_software.platform_version`, `target.asset.platform_software.platform_version` | The operating system revision of the computer, extracted from the `meta.osRevision` field in the raw log.  
`meta.traceId` | `metadata.product_log_id` | The trace ID of the event, extracted from the `meta.traceId` field in the raw log.  
`meta.uuid` | `principal.asset.product_object_id`, `target.asset.product_object_id` | The UUID of the computer, extracted from the `meta.uuid` field in the raw log.  
`metadata_event_type` | `metadata.event_type` | The type of the event, set by the parser logic based on the `event.type` field.  
`metadata_product_name` | `metadata.product_name` | The name of the product, set to `Singularity XDR` by the parser logic.  
`metadata_vendor_name` | `metadata.vendor_name` | The name of the vendor, set to `SentinelOne` by the parser logic.  
`network_application_protocol` | `network.application_protocol` | The application protocol of the network connection, set to `DNS` for DNS events by the parser logic.  
`network_dns_questions.name` | `network.dns.questions.name` | The name of the DNS question, extracted from the `event.query` field in the raw log.  
`network_direction` | `network.direction` | The direction of the network connection, set to `OUTBOUND` for outgoing connections and `INBOUND` for incoming connections by the parser logic.  
`network_http_method` | `network.http.method` | The HTTP method of the event, extracted from the `event.method` field in the raw log.  
`principal.process.command_line` | `target.process.command_line` | The command line of the principal process, extracted from the `principal.process.command_line` field and mapped to the target process command line.  
`principal.process.file.full_path` | `target.process.file.full_path` | The full path of the principal process's file, extracted from the `principal.process.file.full_path` field and mapped to the target process file full path.  
`principal.process.file.md5` | `target.process.file.md5` | The MD5 hash of the principal process's file, extracted from the `principal.process.file.md5` field and mapped to the target process file MD5.  
`principal.process.file.sha1` | `target.process.file.sha1` | The SHA-1 hash of the principal process's file, extracted from the `principal.process.file.sha1` field and mapped to the target process file SHA-1.  
`principal.process.file.sha256` | `target.process.file.sha256` | The SHA-256 hash of the principal process's file, extracted from the `principal.process.file.sha256` field and mapped to the target process file SHA-256.  
`principal.process.file.size` | `target.process.file.size` | The size of the principal process's file, extracted from the `principal.process.file.size` field and mapped to the target process file size.  
`principal.process.pid` | `target.process.pid` | The PID of the principal process, extracted from the `principal.process.pid` field and mapped to the target process PID.  
`principal.user.userid` | `target.user.userid` | The user ID of the principal, extracted from the `principal.user.userid` field and mapped to the target user ID.  
`principal.user.windows_sid` | `target.user.windows_sid` | The Windows SID of the principal, extracted from the `principal.user.windows_sid` field and mapped to the target user Windows SID.  
`metadata.event_type` | `REGISTRY_CREATION` | Mapped from changelog  
`agentDetectionInfo.agentOsName` | `target.platform_version` | Mapped from changelog  
`agentDetectionInfo.agentLastLoggedInUserName` | `target.user.userid` | Mapped from changelog  
`prin_user` | `principal.user.userid` | Mapped from changelog  
`suser` | `principal.user.userid` | Mapped from changelog  
`accountId` | `target.user.userid` | Mapped from changelog  
`MessageSourceAddress` | `principal.ip` | Mapped from changelog  
`machine_host` | `principal.hostname` | Mapped from changelog  
`event.dns.response` | `network.dns.answers.data` | Mapped from changelog  
`osName` | `src.platform` | Mapped from changelog  
`site.id:account.id:agent.uuid:tgt.process.uid` | `target.process.product_specific_process_id` | Mapped from changelog  
`site.id:account.id:agent.uuid:src.process.uid` | `principal.process.product_specific_process_id` | Mapped from changelog  
`site.id:account.id:agent.uuid:src.process.parent.uid` | `principal.process.parent_process.product_specific_process_id` | Mapped from changelog  
`tgt.process.user` | `target.user.userid` | Mapped from changelog  
`metadata.event_type` | `NETWORK_HTTP` | Mapped from changelog  
`indicator.category` | `security_result.category_details` | Mapped from changelog  
`module.path` | `target.process.file.full_path` | Mapped from changelog  
`module.sha1` | `target.process.file.sha1` | Mapped from changelog  
`metadata.event_type` | `PROCESS_MODULE_LOAD` | Mapped from changelog  
`registry.keyPath` | `target.registry.registry_key` | Mapped from changelog  
`registry.value` | `target.registry.registry_value_data` | Mapped from changelog  
`event.network.protocolName` | `network.application_protocol` | Mapped from changelog  
`principal.platform", "principal.asset.platform_software.platform` | `LINUX` | Mapped from changelog  
`event.login.userName` | `target.user.userid` | Mapped from changelog  
`osSrc.process.parent.publisher` | `principal.resource.attribute.labels` | Mapped from changelog  
`src.process.rUserName/src.process.eUserName/src.process.lUserName` | `principal.user.user_display_name` | Mapped from changelog  
`tgt.file.location", "registry.valueFullSize", "registry.valueType` | `target.resource.attribute.labels` | Mapped from changelog  
`indicator.description` | `security_result.summary` | Mapped from changelog  
`metadata.event_type` | `SCAN_NETWORK` | Mapped from changelog  
`metadata.event_type` | `SCAN_UNCATEGORIZED` | Mapped from changelog  
`site.name:site.id` | `principal.namespace` | Mapped from changelog  
`event.network.direction` | `network.direction` | Mapped from changelog  
`meta.event.name` | `metadata.description` | Mapped from changelog  
`task.name` | `target.resource.name` | Mapped from changelog  
`agent.uuid` | `principal.asset.product_object_id` | Mapped from changelog  
`src.process.publisher` | `principal.resource.attribute.labels` | Mapped from changelog  
`src.process.cmdline` | `target.process.command_line` | Mapped from changelog  
`mgmt.osRevision` | `principal.asset.platform_software.platform_version` | Mapped from changelog  
`event.dns.response` | `network.dns.answers` | Mapped from changelog  
`event.id` | `target.registry.registry_value_name` | Mapped from changelog  
`event.type` | `metadata.product_event_type` | Mapped from changelog  
`event.targetFile.signature.signed.identity", "event.target.executable.signature.signed.identity", "event.target.parent.executable.signature.signed.identity` | `target.resource.attribute.labels` | Mapped from changelog  
`mgmt.url` | `metadata.url_back_to_product` | Mapped from changelog  
`site.name` | `principal.location.name` | Mapped from changelog  
`src.process.rUserUid` | `principal.user.userid` | Mapped from changelog  
`src.process.eUserId` | `principal.user.userid` | Mapped from changelog  
`src.process.lUserId` | `principal.user.userid` | Mapped from changelog  
`src.process.parent.rUserUid` | `metadata.ingestion_labels` | Mapped from changelog  
`src.process.parent.eUserId` | `metadata.ingestion_labels` | Mapped from changelog  
`src.process.parent.lUserId` | `metadata.ingestion_labels` | Mapped from changelog  
`tgt.process.rUserUid` | `target.user.userid` | Mapped from changelog  
`tgt.process.eUserId` | `target.user.userid` | Mapped from changelog  
`tgt.process.lUserId` | `target.user.userid` | Mapped from changelog  
`metadata.event_type` | `PROCESS_LAUNCH` | Mapped from changelog  
`metadata.event_type` | `PROCESS_OPEN` | Mapped from changelog  
`metadata.event_type` | `FILE_UNCATEGORIZED` | Mapped from changelog  
`metadata.event_type` | `NETWORK_CONNECTION` | Mapped from changelog  
`metadata.event_type` | `NETWORK_UNCATEGORIZED` | Mapped from changelog  
`metadata.event_type` | `FILE_MODIfICATION` | Mapped from changelog  
`metadata.event_type` | `FILE_CREATION` | Mapped from changelog  
`metadata.event_type` | `FILE_DELETION` | Mapped from changelog  
`metadata.event_type` | `USER_LOGIN` | Mapped from changelog  
`metadata.event_type` | `USER_LOGOUT` | Mapped from changelog  
`metadata.event_type` | `STATUS_UNCATEGORIZED` | Mapped from changelog  
`metadata.event_type` | `NETWORK_DNS` | Mapped from changelog  
`metadata.event_type` | `SCHEDULED_TASK_CREATION` | Mapped from changelog  
`metadata.event_type` | `SCHEDULED_TASK_MODIfICATION` | Mapped from changelog  
`metadata.event_type` | `SCHEDULED_TASK_UNCATEGORIZED` | Mapped from changelog  
`metadata.event_type` | `SCHEDULED_TASK_DELETION` | Mapped from changelog  
`metadata.event_type` | `REGISTRY_MODIfICATION` | Mapped from changelog  
`metadata.event_type` | `REGISTRY_DELETION` | Mapped from changelog  
`metadata.event_type` | `REGISTRY_UNCATEGORIZED` | Mapped from changelog  
`metadata.event_type` | `PROCESS_UNCATEGORIZED` | Mapped from changelog  
`account.id` | `metadata.product_deployment_id` | Mapped from changelog  
`agent.uuid` | `principal.asset.asset_id` | Mapped from changelog  
`dst.ip.address` | `target.ip` | Mapped from changelog  
`src.ip.address` | `principal.ip` | Mapped from changelog  
`src.process.parent.image.sha1` | `principal.process.parent_process.file.sha1` | Mapped from changelog  
`src.process.parent.image.sha256` | `principal.process.parent_process.file.sha256` | Mapped from changelog  
`src.process.parent.image.path` | `principal.process.parent_process.file.full_path` | Mapped from changelog  
`src.process.parent.cmdline` | `principal.process.parent_process.command_line` | Mapped from changelog  
`src.process.parent.image.md5` | `principal.process.parent_process.file.md5` | Mapped from changelog  
`src.process.parent.pid` | `principal.process.parent_process.pid` | Mapped from changelog  
`src.process.image.sha1` | `principal.process.file.sha1` | Mapped from changelog  
`src.process.image.md5` | `principal.process.file.md5` | Mapped from changelog  
`src.process.pid` | `principal.process.pid` | Mapped from changelog  
`src.process.cmdline` | `principal.process.command_line` | Mapped from changelog  
`src.process.image.path` | `principal.process.file.full_path` | Mapped from changelog  
`src.process.image.sha256` | `principal.process.file.sha256` | Mapped from changelog  
`src.process.user` | `principal.user.user_display_name` | Mapped from changelog  
`src.process.uid` | `principal.user.userid` | Mapped from changelog  
`src.process.storyline.id` | `principal.process.product_specific_process_id` | Mapped from changelog  
`src.process.parent.storyline.id` | `principal.process.parent_process.product_specific_process_id` | Mapped from changelog  
`mgmt.url` | `target.url` | Mapped from changelog  
`site.id` | `principal.namespace` | Mapped from changelog  
`src.port.number` | `principal.port` | Mapped from changelog  
`dst.port.number` | `target.port` | Mapped from changelog  
`event_data.id` | `metadata.product_log_id` | Mapped from changelog  
`threatClassification` | `security_result.category_details` | Mapped from changelog  
`threatConfidenceLevel" and "threatMitigationStatus` | `security_result.detection_fields` | Mapped from changelog  
`Location` | `principal.location.name` | Mapped from changelog  
`data.filePath` | `principal.process.parent_process.file.full_path` | Mapped from changelog  
`principal_userid` | `principal.user.userid` | Mapped from changelog  
`principal_domain` | `principal.administrative_domain` | Mapped from changelog  
`threatInfo.threatId` | `security_result.threat_id` | Mapped from changelog  
`threatInfo.identifiedAt` | `metadata.event_timestamp` | Mapped from changelog  
`threatInfo.threatId` | `metadata.product_log_id` | Mapped from changelog  
`security_result.alert_state` | `ALERTING` | Mapped from changelog  
`threatInfo.maliciousProcessArguments` | `security_result.description` | Mapped from changelog  
`threatInfo.threatName` | `security_result.threat_name` | Mapped from changelog  
`threatInfo.classification` | `security_result.category_details` | Mapped from changelog  
`security_result.category` | `SOFTWARE_MALICIOUS` | Mapped from changelog  
`security_result.action` | `ALLOW` | Mapped from changelog  
`threatInfo.mitigationStatus` | `security_result.action_details` | Mapped from changelog  
`threatInfo.classification threatInfo.classificationSource threatInfo.analystVerdictDescription threatInfo.threatName` | `security_result.summary` | Mapped from changelog  
`threatInfo.createdAt` | `metadata.collected_timestamp` | Mapped from changelog  
`agentRealtimeInfo.accountId` | `metadata.product_deployment_id` | Mapped from changelog  
`agentRealtimeInfo.agentVersion` | `metadata.product_version` | Mapped from changelog  
`indicator.category` | `detection_fields.key` | Mapped from changelog  
`detectionEngines.key` | `detection_fields.key` | Mapped from changelog  
`event.targetFile.hashes.md5` | `target.process.file.md5` | Mapped from changelog  
`event.targetFile.hashes.sha1` | `target.process.file.sha1` | Mapped from changelog  
`event.targetFile.hashes.sha256` | `target.process.file.sha256` | Mapped from changelog  
`event.file.path` | `target.file.full_path` | Mapped from changelog  
`event.file.hashes.md5` | `target.process.file.md5` | Mapped from changelog  
`event.file.hashes.sha1` | `target.process.file.sha1` | Mapped from changelog  
`event.file.hashes.sha256` | `target.process.file.sha256` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinel-edr-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
