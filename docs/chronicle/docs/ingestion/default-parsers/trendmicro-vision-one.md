---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one/
title: Collect Trend Micro Vision One logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:53:15.382807+00:00
---

# Collect Trend Micro Vision One logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Trend Micro Vision One logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Trend Micro Vision One logs by setting up a Google Security Operations feed. The parser pushes alerts, event data, container vulnerabilities, activity data, and audit logs to AWS S3 buckets managed by Trend Micro. Google SecOps retrieves this data using data feeds approximately every 15 minutes. Unretrieved data in the S3 buckets is retained for 7 days before being purged.

You can create multiple feeds in Google SecOps and configure the data obtained using the feeds individually.

## Before you begin

  * Ensure that you have a Google SecOps instance.
  * Ensure that you have privileged access to Trend Micro Vision One.



## Configure Trend Vision One Data Export to Google SecOps

  1. In the Trend Vision One console, generate the access key and specify the data to send to Google SecOps.
  2. Go to **Workflow and Automation > Third-Party Integration**.
  3. In the **Integration** column, click **Google Security Operations**.
  4. Under **Access key** , click **Generate key** to generate the access key ID and secret access key. Save the access key ID and secret access key for later use.
  5. Under **Data transfer** , turn on the toggle next to the data you want to send to S3 buckets. Whenever a data transfer is enabled, an S3 URI is generated and the data begins to be sent to the corresponding S3 bucket. Copy and store the S3 URI for later use.
  6. For **Events** and **Activity data** , click **Edit** to modify the scope of the data.
  7. To stop sending a type of data to Google SecOps, turn off the toggle next to the data. Re-enabling the data transfer generates a new S3 URI. You need to configure a new feed in Google SecOps.



## Configure a feed in Google SecOps to ingest the Trend Micro Vision One logs

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add new**.
  3. In the **Feed name** field, enter a name for the feed; for example, `Trend Micro Vision One Workbench Logs`.
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select the Trend Vision One data you want Google SecOps to ingest as the **Log type**. Available options include: 
     * **Trend Micro Vision One**
     * **Trend Micro Vision One Activity**
     * **Trend Micro Vision One Audit**
     * **Trend Micro Vision One Container Vulnerabilities**
     * **Trend Micro Vision One Detections**
     * **Trend Micro Vision One Observed Attack Techniques**
     * **Trend Micro Vision One Workbench**
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **S3 URI** : enter the S3 URI obtained in the previous section.
     * **Source deletion options** : select **Never delete files**.
     * **Maximum File Age** : Includes files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : enter the User access key obtained in the previous section.
     * **Secret Access Key** : enter the User secret key with access to the S3 bucket obtained in the previous section.
     * **Asset namespace** : the [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : the label to be applied to the events from this feed.
  8. Click **Next**.
  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



Repeat this process to add multiple feeds for all the Trend Vision One data types you want to ingest into Google SecOps.

## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`message` | `about` | Mapped: `CEF:` → `about`  
`deviceNtDomain` | `about.administrative_domain` | Renamed/mapped  
`sslCertCommonName` | `about.artifact.last_https_certificate.issuer.common_name` | Directly mapped  
`sslCertSerialNumber` | `about.artifact.last_https_certificate.serial_number` | Directly mapped  
`sslCertFingerprint` | `about.artifact.last_https_certificate.thumbprint` | Directly mapped  
`sslCertValidUntil` | `about.artifact.last_https_certificate.validity.expiry_time` | Directly mapped  
`sslCertValidFrom` | `about.artifact.last_https_certificate.validity.issue_time` | Merged  
`deviceExternalId` | `about.asset.asset_id` | Directly mapped  
`device_product` | `about.asset.asset_id` | Directly mapped  
`device_vendor` | `about.asset.asset_id` | Directly mapped  
`fileHash` | `about.file.full_path` | Directly mapped  
`filePath` | `about.file.full_path` | Renamed/mapped  
`_hash` | `about.file.sha256` | Renamed/mapped  
`fileHash` | `about.file.sha256` | Renamed/mapped  
`fileSize` | `about.file.size` | Renamed/mapped  
`fsize` | `about.file.size` | Renamed/mapped  
`dvchost` | `about.hostname` | Renamed/mapped  
`ips` | `about.ip` | Merged  
`message` | `about.ip` | Mapped: `CEF:` → `ips`  
`dvc_mac` | `about.mac` | Mapped: `slot` → `mac_address`  
`dvcmac` | `about.mac` | Merged  
`mac_address` | `about.mac` | Merged  
`message` | `about.mac` | Mapped: `CEF:` → `mac_address`, `CEF:` → `dvcmac`  
`deviceTranslatedAddress` | `about.nat_ip` | Merged  
`message` | `about.nat_ip` | Mapped: `CEF:` → `deviceTranslatedAddress`  
`Emne` | `about.process.command_line` | Directly mapped  
`Path` | `about.process.command_line` | Directly mapped  
`Subject` | `about.process.command_line` | Directly mapped  
`deviceProcessName` | `about.process.command_line` | Renamed/mapped  
`dvcpid` | `about.process.pid` | Renamed/mapped  
`message` | `about.resource.attribute.permissions` | Mapped: `CEF:` → `permissions`  
`permissions` | `about.resource.attribute.permissions` | Merged  
`_field` | `additional.fields` | Merged  
`accountCount_label` | `additional.fields` | Merged  
`additional_cfp1` | `additional.fields` | Merged  
`additional_cfp2` | `additional.fields` | Merged  
`additional_cfp3` | `additional.fields` | Merged  
`additional_cfp4` | `additional.fields` | Merged  
`additional_cn1` | `additional.fields` | Merged  
`additional_cn2` | `additional.fields` | Merged  
`additional_cn3` | `additional.fields` | Merged  
`additional_cs1` | `additional.fields` | Merged  
`additional_cs2` | `additional.fields` | Merged  
`additional_cs3` | `additional.fields` | Merged  
`additional_cs4` | `additional.fields` | Merged  
`additional_cs5` | `additional.fields` | Merged  
`additional_cs6` | `additional.fields` | Merged  
`additional_cs7` | `additional.fields` | Merged  
`additional_devicePayloadId` | `additional.fields` | Merged  
`additional_eventId` | `additional.fields` | Merged  
`additional_eventSourceType` | `additional.fields` | Merged  
`additional_eventSubId` | `additional.fields` | Merged  
`additional_flexString1` | `additional.fields` | Merged  
`additional_fname` | `additional.fields` | Merged  
`additional_integrityLevel` | `additional.fields` | Merged  
`additional_objectFileHashId` | `additional.fields` | Merged  
`additional_objectFirstSeen` | `additional.fields` | Merged  
`additional_objectHashId` | `additional.fields` | Merged  
`additional_objectLastSeen` | `additional.fields` | Merged  
`additional_objectLaunchTime` | `additional.fields` | Merged  
`additional_objectName` | `additional.fields` | Merged  
`additional_objectRunAsLocalAccount` | `additional.fields` | Merged  
`additional_objectSigner` | `additional.fields` | Merged  
`additional_objectSignerValid` | `additional.fields` | Merged  
`additional_objectUser` | `additional.fields` | Merged  
`additional_objectUserDomain` | `additional.fields` | Merged  
`additional_osType` | `additional.fields` | Merged  
`additional_parentName` | `additional.fields` | Merged  
`additional_parentSigner` | `additional.fields` | Merged  
`additional_parentSignerValid` | `additional.fields` | Merged  
`additional_parentUser` | `additional.fields` | Merged  
`additional_parentUserDomain` | `additional.fields` | Merged  
`additional_plang` | `additional.fields` | Merged  
`additional_pplat` | `additional.fields` | Merged  
`additional_processHashId` | `additional.fields` | Merged  
`additional_processLaunchTime` | `additional.fields` | Merged  
`additional_processTrueType` | `additional.fields` | Merged  
`additional_processUser` | `additional.fields` | Merged  
`additional_processUserDomain` | `additional.fields` | Merged  
`additional_productCode` | `additional.fields` | Merged  
`additional_searchDL` | `additional.fields` | Merged  
`additional_srcFirstSeen` | `additional.fields` | Merged  
`additional_srcHashId` | `additional.fields` | Merged  
`additional_srcLastSeen` | `additional.fields` | Merged  
`additional_uuid` | `additional.fields` | Merged  
`alertProvider_label` | `additional.fields` | Merged  
`caseId_label` | `additional.fields` | Merged  
`clientIp_label` | `additional.fields` | Merged  
`cloudIdentityCount_label` | `additional.fields` | Merged  
`containerCount_label` | `additional.fields` | Merged  
`cs2` | `additional.fields` | Mapped: `arc_test` → `additional_cs2`  
`cs5_label` | `additional.fields` | Merged  
`desktopCount_label` | `additional.fields` | Merged  
`detail_channel_label` | `additional.fields` | Merged  
`detail_engineOperation_label` | `additional.fields` | Merged  
`detail_objectLaunchTime_label` | `additional.fields` | Merged  
`detectionTime_label` | `additional.fields` | Merged  
`emailAddressCount_label` | `additional.fields` | Merged  
`endpoint_ip_label` | `additional.fields` | Merged  
`endpoint_object_guid_label` | `additional.fields` | Merged  
`engVer_label` | `additional.fields` | Merged  
`entity_entityValue_label` | `additional.fields` | Merged  
`entity_guid_value_label` | `additional.fields` | Merged  
`entity_managementScopeGroupId_label` | `additional.fields` | Merged  
`entity_managementScopeInstanceId_label` | `additional.fields` | Merged  
`entity_managementScopePartitionKey_label` | `additional.fields` | Merged  
`entity_type_label` | `additional.fields` | Merged  
`eventSourceType_label` | `additional.fields` | Merged  
`eventSubName_label` | `additional.fields` | Merged  
`filePathName_label` | `additional.fields` | Merged  
`incidentId_label` | `additional.fields` | Merged  
`ingestionTime_label` | `additional.fields` | Merged  
`instance_id_label` | `additional.fields` | Merged  
`key` | `additional.fields` | Mapped: `"device_Facility", "ApexCentral_Host"` → `_field`  
`level_label` | `additional.fields` | Merged  
`logKey_label` | `additional.fields` | Merged  
`logReceivedTime_label` | `additional.fields` | Merged  
`matchedDateTime_label` | `additional.fields` | Merged  
`matched_filter_id_label` | `additional.fields` | Merged  
`message` | `additional.fields` | Mapped values (109 total, e.g., `CEF:` → `_field`, `CEF:` → `additional_eventId`, `CEF:` → `a...  
`modelId_label` | `additional.fields` | Merged  
`modelType_label` | `additional.fields` | Merged  
`model_label` | `additional.fields` | Merged  
`object_guid_label` | `additional.fields` | Merged  
`objects_label` | `additional.fields` | Merged  
`pname_additional_label` | `additional.fields` | Merged  
`process_cmd_label` | `additional.fields` | Merged  
`process_file_hash_sha1_label` | `additional.fields` | Merged  
`process_file_hash_sha256_label` | `additional.fields` | Merged  
`process_file_path_label` | `additional.fields` | Merged  
`process_file_size_label` | `additional.fields` | Merged  
`process_hash_id_label` | `additional.fields` | Merged  
`process_launch_time_label` | `additional.fields` | Merged  
`process_pid_label` | `additional.fields` | Merged  
`process_user_label` | `additional.fields` | Merged  
`provenance_data` | `additional.fields` | Merged  
`reportLink_label` | `additional.fields` | Merged  
`rtHour_label` | `additional.fields` | Merged  
`rtWeekDay_label` | `additional.fields` | Merged  
`schema_version_label` | `additional.fields` | Merged  
`senderGUID_label` | `additional.fields` | Merged  
`serverCount_label` | `additional.fields` | Merged  
`serverIp_label` | `additional.fields` | Merged  
`status_label` | `additional.fields` | Merged  
`has_user` | `extensions.auth.type` | Mapped: `true` → `AUTHTYPE_UNSPECIFIED`  
`message` | `extensions.auth.type` | Mapped: `CEF:` → `AUTHTYPE_UNSPECIFIED`  
`message` | `intermediary` | Mapped: `CEF:` → `intermediary`  
`inter_host` | `intermediary.hostname` | Directly mapped  
`Model` | `metadata.description` | Directly mapped  
`description` | `metadata.description` | Directly mapped  
`eventSubName` | `metadata.description` | Directly mapped  
`msg` | `metadata.description` | Renamed/mapped  
`Generated` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`Received` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`createdDateTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`detail.eventTime` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`detectedDateTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`detectionTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`firstSeen` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`ingestedDateTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`lastSeen` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`loggedDateTime` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`processFileModifiedTime` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`rt` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`sslCertValidFrom` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`sslCertValidUntil` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`unix_logReceivedTime` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`updatedDateTime` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`utc` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss.SSSZ`  
`event_name` | `metadata.event_type` | Mapped: `"LogSpyware","LogPredictiveMachineLearning"` → `SCAN_UNCATEGORIZED`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_LOGIN`, `true` → `USER_UNCATEGORIZED`  
`message` | `metadata.event_type` | Mapped values (8 total, e.g., `CEF:` → `SCAN_UNCATEGORIZED`, `CEF:` → `STATUS_UPDATE`, `CEF:`...  
`principal_present` | `metadata.event_type` | Mapped: `true` → `PROCESS_UNCATEGORIZED`, `true` → `NETWORK_CONNECTION`, `true` → `PROCESS_L...  
`activity` | `metadata.product_event_type` | Directly mapped  
`device_event_class_id` | `metadata.product_event_type` | Directly mapped  
`event_name` | `metadata.product_event_type` | Directly mapped  
`type` | `metadata.product_event_type` | Directly mapped  
`WorkbenchID` | `metadata.product_log_id` | Directly mapped  
`detail.uuid` | `metadata.product_log_id` | Directly mapped  
`e_ID` | `metadata.product_log_id` | Directly mapped  
`externalId` | `metadata.product_log_id` | Directly mapped  
`id` | `metadata.product_log_id` | Directly mapped  
`detail.mpname` | `metadata.product_name` | Directly mapped  
`device_product` | `metadata.product_name` | Directly mapped  
`message` | `metadata.product_name` | Mapped: `CEF:` → `Vision One`  
`detail.mpver` | `metadata.product_version` | Directly mapped  
`device_version` | `metadata.product_version` | Directly mapped  
`device_vendor` | `metadata.vendor_name` | Renamed/mapped  
`message` | `metadata.vendor_name` | Mapped: `CEF:` → `Trend Micro`  
`app_protocol_output` | `network.application_protocol` | Directly mapped  
`deviceDirection` | `network.direction` | Mapped: `0` → `INBOUND`, `1` → `OUTBOUND`  
`message` | `network.direction` | Mapped: `CEF:` → `INBOUND`, `CEF:` → `OUTBOUND`  
`object.CustomValue` | `network.email.from` | Directly mapped  
`message` | `network.email.subject` | Mapped: `CEF:` → `title`  
`title` | `network.email.subject` | Merged  
`message` | `network.email.to` | Mapped: `CEF:` → `object.CustomValue`  
`object.CustomValue` | `network.email.to` | Merged  
`objecttype` | `network.email.to` | Mapped: `email_forward` → `object.CustomValue`  
`requestMethod` | `network.http.method` | Renamed/mapped  
`Link` | `network.http.referral_url` | Directly mapped  
`requestClientApplication` | `network.http.user_agent` | Renamed/mapped  
`userAgent` | `network.http.user_agent` | Directly mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`in` | `network.received_bytes` | Renamed/mapped  
`out` | `network.sent_bytes` | Renamed/mapped  
`sessionId` | `network.session_id` | Directly mapped  
`tlsSelectedCipher` | `network.tls.cipher` | Directly mapped  
`ja3Hash` | `network.tls.client.ja3` | Directly mapped  
`ja3sHash` | `network.tls.server.ja3s` | Directly mapped  
`detail.mDeviceGUID` | `observer.asset.asset_id` | Directly mapped  
`detail.dvchost` | `observer.hostname` | Directly mapped  
`ip` | `observer.ip` | Merged  
`message` | `observer.ip` | Mapped: `CEF:` → `ip`  
`account_domain` | `principal.administrative_domain` | Directly mapped  
`sntdom` | `principal.administrative_domain` | Renamed/mapped  
`userDomain` | `principal.administrative_domain` | Directly mapped  
`userDomain.0` | `principal.administrative_domain` | Directly mapped  
`application` | `principal.application` | Renamed/mapped  
`sourceServiceName` | `principal.application` | Renamed/mapped  
`detail.endpointGuid` | `principal.asset.asset_id` | Directly mapped  
`endpoint.agentGuid` | `principal.asset.asset_id` | Directly mapped  
`mDeviceGUID` | `principal.asset.asset_id` | Directly mapped  
`entityName_label` | `principal.asset.attribute.labels` | Merged  
`message` | `principal.asset.attribute.labels` | Mapped: `CEF:` → `entityName_label`  
`endpoint.name` | `principal.asset.hostname` | Directly mapped  
`endpointHostName` | `principal.asset.hostname` | Directly mapped  
`object_hostname` | `principal.asset.hostname` | Directly mapped  
`shost` | `principal.asset.hostname` | Directly mapped  
`Appliance_IP_address` | `principal.asset.ip` | Merged  
`IP_address` | `principal.asset.ip` | Merged  
`ip` | `principal.asset.ip` | Merged  
`ip_src_value` | `principal.asset.ip` | Merged  
`message` | `principal.asset.ip` | Mapped values (7 total, e.g., `CEF:` → `IP_address`, `CEF:` → `Appliance_IP_address`, `CEF:` ...  
`object_field` | `principal.asset.ip` | Mapped: `src` → `ip_src_value`  
`shost` | `principal.asset.ip` | Merged  
`src` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`endpointGuid` | `principal.asset_id` | Directly mapped  
`object_guid` | `principal.asset_id` | Directly mapped  
`detail.fullPath` | `principal.file.full_path` | Directly mapped  
`requestMimeType` | `principal.file.mime_type` | Directly mapped  
`indicator.value` | `principal.file.sha1` | Directly mapped  
`Group_name` | `principal.group.group_display_name` | Directly mapped  
`Gruppenavn` | `principal.group.group_display_name` | Directly mapped  
`clientGroup` | `principal.group.group_display_name` | Directly mapped  
`detail.groupId` | `principal.group.product_object_id` | Directly mapped  
`Device_name` | `principal.hostname` | Directly mapped  
`Enhetsnavn` | `principal.hostname` | Directly mapped  
`endpoint.name` | `principal.hostname` | Directly mapped  
`endpointHostName` | `principal.hostname` | Directly mapped  
`object_hostname` | `principal.hostname` | Directly mapped  
`shost` | `principal.hostname` | Directly mapped  
`Appliance_IP_address` | `principal.ip` | Merged  
`IP_address` | `principal.ip` | Merged  
`ip` | `principal.ip` | Merged  
`ip_src_value` | `principal.ip` | Merged  
`message` | `principal.ip` | Mapped values (8 total, e.g., `CEF:` → `IP_address`, `CEF:` → `Appliance_IP_address`, `CEF:` ...  
`object_field` | `principal.ip` | Mapped: `src` → `ip_src_value`  
`principal_ip` | `principal.ip` | Merged  
`shost` | `principal.ip` | Merged  
`src` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`mac` | `principal.mac` | Merged  
`message` | `principal.mac` | Mapped: `CEF:` → `mac`  
`message` | `principal.nat_ip` | Mapped: `CEF:` → `sourceTranslatedAddress`  
`sourceTranslatedAddress` | `principal.nat_ip` | Merged  
`sourceTranslatedPort` | `principal.nat_port` | Renamed/mapped  
`message` | `principal.platform` | Mapped: `CEF:` → `WINDOWS`, `CEF:` → `MAC`, `CEF:` → `LINUX`  
`osName` | `principal.platform` | Mapped: `(?i)windows` → `WINDOWS`, `(?i)Mac/iOS` → `MAC`, `(?)Lin` → `LINUX`  
`osVer` | `principal.platform_version` | Directly mapped  
`platform_version` | `principal.platform_version` | Directly mapped  
`spt` | `principal.port` | Renamed/mapped  
`object.value` | `principal.process.command_line` | Directly mapped  
`processCmd` | `principal.process.command_line` | Directly mapped  
`process_cmd` | `principal.process.command_line` | Directly mapped  
`sproc` | `principal.process.command_line` | Renamed/mapped  
`detail.processName` | `principal.process.file.full_path` | Directly mapped  
`object.value` | `principal.process.file.full_path` | Directly mapped  
`processFilePath` | `principal.process.file.full_path` | Directly mapped  
`process_file_path` | `principal.process.file.full_path` | Directly mapped  
`processFileModifiedTime` | `principal.process.file.last_modification_time` | Renamed/mapped  
`detail.processFileHashMd5` | `principal.process.file.md5` | Directly mapped  
`processFileHashMd5` | `principal.process.file.md5` | Directly mapped  
`fileHash` | `principal.process.file.sha1` | Directly mapped  
`object.value` | `principal.process.file.sha1` | Directly mapped  
`processFileHashSha1` | `principal.process.file.sha1` | Directly mapped  
`process_file_hash_sha1` | `principal.process.file.sha1` | Directly mapped  
`fileHashSha256` | `principal.process.file.sha256` | Directly mapped  
`processFileHashSha256` | `principal.process.file.sha256` | Directly mapped  
`process_file_hash_sha256` | `principal.process.file.sha256` | Directly mapped  
`processFileSize` | `principal.process.file.size` | Renamed/mapped  
`parentFilePath` | `principal.process.parent_process.file.full_path` | Directly mapped  
`parentFileHashMd5` | `principal.process.parent_process.file.md5` | Directly mapped  
`parentFileHashSha1` | `principal.process.parent_process.file.sha1` | Directly mapped  
`parentFileHashSha256` | `principal.process.parent_process.file.sha256` | Directly mapped  
`parentPid` | `principal.process.parent_process.pid` | Directly mapped  
`processPid` | `principal.process.pid` | Directly mapped  
`process_pid` | `principal.process.pid` | Directly mapped  
`spid` | `principal.process.pid` | Renamed/mapped  
`message` | `principal.resource.attribute.labels` | Mapped: `CEF:` → `sourceLabel`, `CEF:` → `pname_label`, `CEF:` → `senderGUID_label`  
`pname_label` | `principal.resource.attribute.labels` | Merged  
`senderGUID_label` | `principal.resource.attribute.labels` | Merged  
`sourceLabel` | `principal.resource.attribute.labels` | Merged  
`uuid` | `principal.resource.product_object_id` | Directly mapped  
`customer_name_label` | `principal.user.attribute.labels` | Merged  
`message` | `principal.user.attribute.labels` | Mapped: `CEF:` → `customer_name_label`  
`message` | `principal.user.attribute.roles` | Mapped: `CEF:` → `principal_role`, `CEF:` → `roles`  
`principal_role` | `principal.user.attribute.roles` | Merged  
`roles` | `principal.user.attribute.roles` | Merged  
`message` | `principal.user.department` | Mapped: `CEF:` → `userDepartment`  
`userDepartment` | `principal.user.department` | Merged  
`details.identifier.email` | `principal.user.email_addresses` | Merged  
`entity.entityValue` | `principal.user.email_addresses` | Merged  
`message` | `principal.user.email_addresses` | Mapped: `CEF:` → `details.identifier.email`, `CEF:` → `entity.entityValue`, `CEF:` → `princi...  
`principalName` | `principal.user.email_addresses` | Merged  
`entity_entityValue` | `principal.user.user_display_name` | Directly mapped  
`loggedUser` | `principal.user.user_display_name` | Directly mapped  
`suser` | `principal.user.user_display_name` | Directly mapped  
`account` | `principal.user.userid` | Directly mapped  
`account_name` | `principal.user.userid` | Directly mapped  
`detail.suid` | `principal.user.userid` | Directly mapped  
`details.identifier.id` | `principal.user.userid` | Directly mapped  
`loggedUser` | `principal.user.userid` | Directly mapped  
`logonUser.0` | `principal.user.userid` | Directly mapped  
`object.CustomValue` | `principal.user.userid` | Directly mapped  
`process_user` | `principal.user.userid` | Directly mapped  
`suid` | `principal.user.userid` | Renamed/mapped  
`security_id` | `principal.user.windows_sid` | Directly mapped  
`message` | `security_result` | Mapped values (5 total, e.g., `CEF:` → `security_result`, `CEF:` → `task_sec_res`, `CEF:` → `...  
`sec` | `security_result` | Merged  
`sec_isEntity` | `security_result` | Merged  
`sec_res` | `security_result` | Merged  
`task_sec_res` | `security_result` | Merged  
`wasEntity.key` | `security_result.about.file.full_path` | Directly mapped  
`investigationResult` | `security_result.about.investigation.comments` | Merged  
`message` | `security_result.about.investigation.comments` | Mapped: `CEF:` → `investigationResult`  
`investigationStatus` | `security_result.about.investigation.status` | Mapped: `New` → `NEW`, `Closed` → `CLOSED`, `Open` → `OPEN`, `Reviewed` → `REVIEWED`  
`message` | `security_result.about.investigation.status` | Mapped values (5 total, e.g., `CEF:` → `NEW`, `CEF:` → `CLOSED`, `CEF:` → `OPEN`)  
`attr_value` | `security_result.about.process.command_line` | Directly mapped  
`_action` | `security_result.action` | Merged  
`act` | `security_result.action` | Mapped: `accept` → `_action`, `deny` → `_action`  
`action_data` | `security_result.action` | Merged  
`message` | `security_result.action` | Mapped: `CEF:` → `_action`, `CEF:` → `action_data`, `CEF:` → `security_result_action`  
`object_field` | `security_result.action` | Mapped: `actResult` → `security_result_action`  
`result` | `security_result.action` | Mapped: `Successful` → `action_data`, `Unsuccess` → `action_data`  
`security_result_action` | `security_result.action` | Merged  
`Action_Taken` | `security_result.action_details` | Directly mapped  
`act` | `security_result.action_details` | Directly mapped  
`actResult` | `security_result.action_details` | Directly mapped  
`detail.accessPermission` | `security_result.action_details` | Directly mapped  
`result` | `security_result.action_details` | Directly mapped  
`message` | `security_result.attack_details.tactics` | Mapped: `CEF:` → `tactics`, `CEF:` → `tactic`  
`tactic` | `security_result.attack_details.tactics` | Merged  
`tactics` | `security_result.attack_details.tactics` | Merged  
`message` | `security_result.attack_details.techniques` | Mapped: `CEF:` → `techniques`  
`techniques` | `security_result.attack_details.techniques` | Merged  
`act` | `security_result.category` | Mapped: `Block` → `event_category`  
`event_category` | `security_result.category` | Merged  
`message` | `security_result.category` | Mapped: `CEF:` → `event_category`  
`cat` | `security_result.category_details` | Merged  
`category` | `security_result.category_details` | Merged  
`detail.behaviorCat` | `security_result.category_details` | Merged  
`message` | `security_result.category_details` | Mapped: `CEF:` → `cat`, `CEF:` → `category`, `CEF:` → `detail.behaviorCat`  
`Scan_Type` | `security_result.description` | Directly mapped  
`Type` | `security_result.description` | Directly mapped  
`filters.0.description` | `security_result.description` | Directly mapped  
`msg_data_2` | `security_result.description` | Directly mapped  
`LogonID_label` | `security_result.detection_fields` | Merged  
`accessType_label` | `security_result.detection_fields` | Merged  
`access_right_label` | `security_result.detection_fields` | Merged  
`account_modified_name_label` | `security_result.detection_fields` | Merged  
`account_type_label` | `security_result.detection_fields` | Merged  
`activity_label` | `security_result.detection_fields` | Merged  
`attr_name` | `security_result.detection_fields` | Mapped: `sha256` → `sha256_label`, `startType` → `startType_label`, `state` → `state_label`  
`evt_type_label` | `security_result.detection_fields` | Merged  
`filepath_label` | `security_result.detection_fields` | Merged  
`highlighted_field_label` | `security_result.detection_fields` | Merged  
`highlighted_type_label` | `security_result.detection_fields` | Merged  
`indicator_label` | `security_result.detection_fields` | Merged  
`infection_channel_label` | `security_result.detection_fields` | Merged  
`matched_event_uuid_label` | `security_result.detection_fields` | Merged  
`message` | `security_result.detection_fields` | Mapped values (30 total, e.g., `CEF:` → `operation_label`, `CEF:` → `operasjon_label`, `CEF:`... )  
`mpver_label` | `security_result.detection_fields` | Merged  
`objecttype` | `security_result.detection_fields` | Mapped: `text` → `text_label`  
`operasjon_label` | `security_result.detection_fields` | Merged  
`operation_label` | `security_result.detection_fields` | Merged  
`permission_label` | `security_result.detection_fields` | Merged  
`policy_id_label` | `security_result.detection_fields` | Merged  
`sha256_label` | `security_result.detection_fields` | Merged  
`spyware_Grayware_Type_label` | `security_result.detection_fields` | Merged  
`startType_label` | `security_result.detection_fields` | Merged  
`state_label` | `security_result.detection_fields` | Merged  
`subRuleId_label` | `security_result.detection_fields` | Merged  
`subRuleName_label` | `security_result.detection_fields` | Merged  
`tag_label` | `security_result.detection_fields` | Merged  
`text_label` | `security_result.detection_fields` | Merged  
`threat_probability_label` | `security_result.detection_fields` | Merged  
`tillatelse_label` | `security_result.detection_fields` | Merged  
`was_key_label` | `security_result.detection_fields` | Merged  
`winEventId_label` | `security_result.detection_fields` | Merged  
`createdDateTime` | `security_result.first_discovered_time` | Renamed/mapped  
`firstSeen` | `security_result.first_discovered_time` | Renamed/mapped  
`lastSeen` | `security_result.last_discovered_time` | Renamed/mapped  
`updatedDateTime` | `security_result.last_updated_time` | Renamed/mapped  
`Score` | `security_result.risk_score` | Renamed/mapped  
`score` | `security_result.risk_score` | Renamed/mapped  
`detail.ruleId` | `security_result.rule_id` | Renamed/mapped  
`detail.uuid` | `security_result.rule_id` | Directly mapped  
`filters.0.unique_id` | `security_result.rule_id` | Directly mapped  
`ruleUuid` | `security_result.rule_id` | Renamed/mapped  
`detail.ruleName` | `security_result.rule_name` | Renamed/mapped  
`filters.0.id` | `security_result.rule_name` | Directly mapped  
`mwProfile` | `security_result.rule_name` | Directly mapped  
`object.CustomValue` | `security_result.rule_name` | Directly mapped  
`ruleName` | `security_result.rule_name` | Directly mapped  
`filter.type` | `security_result.rule_type` | Directly mapped  
`ruleType` | `security_result.rule_type` | Directly mapped  
`message` | `security_result.severity` | Mapped values (5 total, e.g., `CEF:` → `LOW`, `CEF:` → `MEDIUM`, `CEF:` → `HIGH`)  
`severity` | `security_result.severity` | Mapped values (6 total, e.g., `"0", "1", "2", "3", "LOW"` → `LOW`, `"4", "5", "6", "MEDIUM", ... )  
`filter.riskLevel` | `security_result.severity_details` | Directly mapped  
`Result` | `security_result.summary` | Directly mapped  
`appcategory` | `security_result.summary` | Directly mapped  
`filters.0.name` | `security_result.summary` | Directly mapped  
`reason` | `security_result.summary` | Renamed/mapped  
`Spyware` | `security_result.threat_name` | Directly mapped  
`Unknown_Threat` | `security_result.threat_name` | Directly mapped  
`Virus_Malware_Name` | `security_result.threat_name` | Directly mapped  
`object.value` | `security_result.threat_name` | Directly mapped  
`workbenchLink` | `security_result.url_back_to_product` | Renamed/mapped  
`oldFilePath` | `src.file.full_path` | Renamed/mapped  
`oldFileSize` | `src.file.size` | Renamed/mapped  
`message` | `src.resource.attribute.permissions` | Mapped: `CEF:` → `old_permissions`  
`old_permissions` | `src.resource.attribute.permissions` | Merged  
`dntdom` | `target.administrative_domain` | Renamed/mapped  
`destinationServiceName` | `target.application` | Renamed/mapped  
`detail.deviceGUID` | `target.asset.asset_id` | Directly mapped  
`dst` | `target.asset.ip` | Merged  
`ip_dst_value` | `target.asset.ip` | Merged  
`message` | `target.asset.ip` | Mapped: `CEF:` → `dst`, `CEF:` → `ip_dst_value`  
`object_field` | `target.asset.ip` | Mapped: `dst` → `ip_dst_value`  
`object.CustomValue` | `target.file.full_path` | Directly mapped  
`object.value` | `target.file.full_path` | Directly mapped  
`value` | `target.file.full_path` | Directly mapped  
`object.CustomValue` | `target.file.sha1` | Directly mapped  
`object.value` | `target.file.sha1` | Directly mapped  
`detail.objectFileSize` | `target.file.size` | Directly mapped  
`message` | `target.file.size` | Mapped: `CEF:` → `uinteger`  
`temp_dhost` | `target.hostname` | Directly mapped  
`IPv6_Address` | `target.ip` | Merged  
`dst` | `target.ip` | Merged  
`dst_ip` | `target.ip` | Merged  
`ip_dst_value` | `target.ip` | Merged  
`ipv6` | `target.ip` | Mapped: `-` → `IPv6_Address`  
`message` | `target.ip` | Mapped: `CEF:` → `dst_ip`, `CEF:` → `IPv6_Address`, `CEF:` → `dst`, `CEF:` → `ip_dst_value`  
`object_field` | `target.ip` | Mapped: `dst` → `ip_dst_value`  
`mac_address` | `target.mac` | Merged  
`message` | `target.mac` | Mapped: `CEF:` → `mac_address`  
`destination_translated_address` | `target.nat_ip` | Merged  
`message` | `target.nat_ip` | Mapped: `CEF:` → `destination_translated_address`  
`destinationTranslatedPort` | `target.nat_port` | Renamed/mapped  
`dpt` | `target.port` | Renamed/mapped  
`dproc` | `target.process.command_line` | Renamed/mapped  
`object.CustomValue` | `target.process.command_line` | Directly mapped  
`object.value` | `target.process.command_line` | Directly mapped  
`objectCmd` | `target.process.command_line` | Directly mapped  
`File_name` | `target.process.file.full_path` | Directly mapped  
`Infected_Resource` | `target.process.file.full_path` | Directly mapped  
`Object` | `target.process.file.full_path` | Directly mapped  
`Objekt` | `target.process.file.full_path` | Directly mapped  
`fileName` | `target.process.file.full_path` | Directly mapped  
`object.CustomValue` | `target.process.file.full_path` | Directly mapped  
`object.value` | `target.process.file.full_path` | Directly mapped  
`objectFilePath` | `target.process.file.full_path` | Directly mapped  
`objectFileHashMd5` | `target.process.file.md5` | Directly mapped  
`object.CustomValue` | `target.process.file.sha1` | Directly mapped  
`object.value` | `target.process.file.sha1` | Directly mapped  
`objectFileHashSha1` | `target.process.file.sha1` | Directly mapped  
`objectFileHashSha256` | `target.process.file.sha256` | Directly mapped  
`object.CustomValue` | `target.process.parent_process.command_line` | Directly mapped  
`object.CustomValue` | `target.process.parent_process.file.full_path` | Directly mapped  
`object.CustomValue` | `target.process.parent_process.file.sha1` | Directly mapped  
`object.value` | `target.process.parent_process.file.sha1` | Directly mapped  
`dpid` | `target.process.pid` | Renamed/mapped  
`objectPid` | `target.process.pid` | Directly mapped  
`command_line_label` | `target.resource.attribute.labels` | Merged  
`dacDeviceType_label` | `target.resource.attribute.labels` | Merged  
`endpointGUID_label` | `target.resource.attribute.labels` | Merged  
`file_path_label` | `target.resource.attribute.labels` | Merged  
`file_sha1_label` | `target.resource.attribute.labels` | Merged  
`message` | `target.resource.attribute.labels` | Mapped values (6 total, e.g., `CEF:` → `resource_Type_label`, `CEF:` → `dacDeviceType_label`,...  
`objecttype` | `target.resource.attribute.labels` | Mapped: `command_line` → `command_line_label`, `file_sha1` → `file_sha1_label`, `fullpath` →...  
`resource_Type_label` | `target.resource.attribute.labels` | Merged  
`request` | `target.url` | Directly mapped  
`message` | `target.user.attribute.roles` | Mapped: `CEF:` → `target_role`  
`target_role` | `target.user.attribute.roles` | Merged  
`CustomerName` | `target.user.user_display_name` | Directly mapped  
`temp_duser` | `target.user.user_display_name` | Directly mapped  
`Bruker` | `target.user.userid` | Directly mapped  
`User_value` | `target.user.userid` | Directly mapped  
`temp_duid` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `AUTHTYPE_UNSPECIFIED`  
N/A | `metadata.event_type` | Constant: `SCAN_UNCATEGORIZED`  
N/A | `metadata.product_name` | Constant: `Vision One`  
N/A | `metadata.vendor_name` | Constant: `Trend Micro`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `principal.platform` | Constant: `WINDOWS`  
N/A | `security_result.about.investigation.status` | Constant: `NEW`  
N/A | `security_result.severity` | Constant: `LOW`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
