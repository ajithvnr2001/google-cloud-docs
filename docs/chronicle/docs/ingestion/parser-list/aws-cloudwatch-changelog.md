---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-cloudwatch-changelog/
title: Change log for AWS_CLOUDWATCH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:57:27.544516+00:00
---

# Change log for AWS_CLOUDWATCH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-cloudwatch-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_CLOUDWATCH

Date | Changes  
---|---  
2026-08-10 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `operationType` and `type` raw log fields with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `resourcePath` and `resourceType` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2026-07-15 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `owner` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `record_messageType` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `logevent.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `logevent.extractedFields.version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `logevent.extractedFields.interface_id` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `logevent.extractedFields.srcaddr` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `logevent.extractedFields.srcport` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `logevent.extractedFields.dstaddr` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `logevent.extractedFields.dstport` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `logevent.extractedFields.packets` raw log field with `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `logevent.extractedFields.bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `logevent.extractedFields.protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `logevent.extractedFields.action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field when `act` is equal to `ACCEPT`.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `logevent.extractedFields.action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `logevent.extractedFields.start`, `logevent.extractedFields.end` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `logevent.extractedFields.log_status`, `logevent.message` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `logevent.timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `logevent.extractedFields.account_id` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.   
2026-06-04 |  Enhancement:  
\- Added support to parse `XML` format logs.  
\- `event.idm.read_only_udm.metadata.product_deployment_id`: Newly mapped `provider_guid` raw log field with `event.idm.read_only_udm.metadata.product_deployment_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `EventRecordID`, `logevent.id` raw log fields with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `EventID`, `messageType` raw log fields with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `Level` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `ProcessId`, `prin_processid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `Computer` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `Computer` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `param2` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `xml_message` raw log fields with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `Level1` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `ThreadId` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `xml_namespace`, `provider_name`, `event_source_name`, `qualifiers`, `Task`, `Opcode`, `Keywords`, `ActivityID`, `Channel`, `param1`, `Culture`, `Provider1`, `Keyword` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `SystemTime`, `logevent.timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Added a grok pattern on `logevent.message` to parse the raw log fields.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `datetime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `prin_app` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `desc1` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.   
2026-05-29 |  Enhancement:  
\- Added support for new pattern of JSON format logs.  
\- Modified a grok pattern on `message` to parse the raw log fields.   
2026-05-22 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `logEvents.message.requestId`, `logEvents.message.extendedRequestId`, `logevent.message.caller` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `logEvents.message.ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `logEvents.message.user` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `logEvents.message.requestTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `logEvents.message.httpMethod` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `logEvents.message.resourcePath` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `logEvents.message.status` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped extracted `protocol` field from `logEvents.message.protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped extracted `protocol_version` field from `logEvents.message.protocol` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `logEvents.message.responseLength` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.   
2026-03-27 |  Enhancement  
\- Added a new grok pattern for the raw log field `message_temp` to extract `report_request_id`, `duration`, `memory_size`, `max_memory_used`, and `Billed_Duration`.  
\- Added a Grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `duration` from `event.idm.read_only_udm.additional.fields` UDM field because, it is a duplicate UDM mapping.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_target_user` is true, updated the value of `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.  
\- `event.idm.read_only_udm.principal.asset_id`: Newly mapped `aws_account` raw log field with `event.idm.read_only_udm.principal.asset_id` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `phoneNumber_country` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `aws_log_stream`, `aws_message_type`, `lambda_request_id`, `phoneNumber_countryCallingCode`, `phoneNumber_countryCallingCodeSource`, `max_memory_used`, `gridInquiryId`, `phoneCode`, `dateOfBirth`, `gender`, `countryOfBirth`, `nationality`, `nationalities`, `postalCode`, `street`, `block`, `building`, `floor`, `unit`, `addressLine`, `expirationDate`, `annualIncome_max`, `annualIncome_min`, `savings_max`, `savings_min`, `customerAgreement`, `orderHandling`, `privacyPolicy`, `riskDisclosure`, `employmentStatus`, `typeOfBusiness`, `createdAt`, `updatedAt`, `industryLabel`, `industryCode`, `occupationCode`, `occupationLabel`, `primary`, `expiredAt`, `signedAt`, `selectedTaxResidency`, `type`, `diplomaOrHigher`, `qualifiedFinancePro`, `workedPast10Years`, `workedPast3Years`, `none`, `dataConfirmed`, `isDeactivated`, `kycStatus`, `pepCheckStatus`, `cfd`, `Billed_Duration`, `countryCode`, `additional` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp_iso` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `log_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `lambda_level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `source_region`, `awsRegion` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `functionName` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `functionVersion`, `environment`, `authProvider`, `dataProvider`, `igApplicationId`, `igClientId`, `ibkrUserId`, `sourceOfFunds` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.user.phone_numbers`: Newly mapped `phoneNumber_nationalNumber` raw log field with `event.idm.read_only_udm.target.user.phone_numbers` UDM field.  
\- `event.idm.read_only_udm.principal.user.phone_numbers`: Newly mapped `phoneNumber_number`, `phoneNumber` raw log field with `event.idm.read_only_udm.principal.user.phone_numbers` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `externalUserId`, `report_request_id` raw log fields with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `memory_size` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `http_verb` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `referral_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `resp_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `userId`, `source_account` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.last_name`: Newly mapped `lastName` raw log field with `event.idm.read_only_udm.principal.user.last_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.first_name`: Newly mapped `firstName` raw log field with `event.idm.read_only_udm.principal.user.first_name` UDM field.  
\- `event.idm.read_only_udm.principal.location.city`: Newly mapped `city` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- `event.idm.read_only_udm.principal.user.employee_id`: Newly mapped `nric` raw log field with `event.idm.read_only_udm.principal.user.employee_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `principalName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.   
2026-03-10 |  Enhancement  
\- `event.idm.read_only_udm.network.direction`: If `Direction` is `Up`, set the value of `event.idm.read_only_udm.network.direction` to `OUTBOUND`.  
\- `event.idm.read_only_udm.network.direction`: If `Direction` is `Down`, set the value of `event.idm.read_only_udm.network.direction` to `INBOUND`.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `Protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `Cat` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `Hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip`: Newly mapped `IP` and `LocalIp` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `Path` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.md5`: Newly mapped `Hash` raw log field with `event.idm.read_only_udm.principal.process.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `Pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `LocalPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.port`:  
\- If `LocalPort` is not empty, set the value of `LocalPort` to `event.idm.read_only_udm.target.port`.  
\- Else, If `Port` is not empty, set the value of `Port` to `event.idm.read_only_udm.target.port`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ValidSig`, `Company`, `ImageType`, `MWName`, `DriveType`, `Times`, `SocketOpFlags`, `ALProtocolExpected`, `ALProtocolDetected`, `CipherType`, `ConnectionState`, `ProxyConnection`, `ContentEncoding`, `Broken`, `ExeType`, `Prevalence`, `PrevLastDay` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a condition to also check if principal machine data is present before mapping the `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`.  
\- `event.idm.read_only_udm.network.direction`: Removed mapping of `event.idm.read_only_udm.network.direction` when `event.idm.read_only_udm.metadata.event_type` is `STATUS_UPDATE`, as network direction can only be set for network-related events.   
2026-02-26 |  Enhancement  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `logevent.message.firewall_name` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `logevent.message.firewall_name` raw log field with `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `logevent.message.availability_zone` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `logevent.message.event.src_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `logevent.message.event.src_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `logevent.message.event.src_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `logevent.message.event.dest_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `logevent.message.event.dest_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `logevent.message.event.dest_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped with conditional logic.  
\- If `logevent.message.event.proto` is TCP, Set the value of `event.idm.read_only_udm.network.ip_protocol` to `TCP`.  
\- If `logevent.message.event.proto` is UDP, Set the value of `event.idm.read_only_udm.network.ip_protocol` to `UDP`.  
\- If `logevent.message.event.proto` is ICMP, Set the value of `event.idm.read_only_udm.network.ip_protocol` to `ICMP`.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `logevent.message.event.alert.action`, `logevent.message.event.verdict.action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `logevent.message.event.alert.signature`, `logevent.message.event.icmp_type`, `logevent.message.event.icmp_code`, `logevent.message.event.app_proto`, `logevent.message.event.alert.signature_id`, `logevent.message.event.alert.rev` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `logevent.message.event.alert.severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped with conditional logic.  
\- If `logevent.message.event.alert.severity` is 1, 2, or 3, Set the value of `event.idm.read_only_udm.security_result.severity` to `LOW`.  
\- If `logevent.message.event.alert.severity` is 4, 5, or 6, Set the value of `event.idm.read_only_udm.security_result.severity` to `MEDIUM`.  
\- If `logevent.message.event.alert.severity` is 7, 8, or 9, Set the value of `event.idm.read_only_udm.security_result.severity` to `HIGH`.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `logevent.message.event.flow_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `logevent.message.event.direction` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped logevent.message.event.alert.signature (key: Signature), logevent.message.event.icmp_type (key: Icmp_Type), logevent.message.event.icmp_code (key: Icmp_Code), logevent.message.event.app_proto (key: App_Proto), logevent.message.event.alert.signature_id (key: Signature_ID), logevent.message.event.alert.rev (key: Rev), logevent.message.event.pkt_src (key: Pkt_Src) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `logevent.message.event.timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped if `logevent.message.event.direction` raw log field value is `to_server`, Set the value of `event.idm.read_only_udm.network.direction` to `INBOUND`.  
\- Added a gsub which parses the dropped logs as a result, the following UDM fields are now being mapped correctly:  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.principal.asset.asset_id`  
\- `event.idm.read_only_udm.principal.user.userid`  
\- `event.idm.read_only_udm.security_result.description`  
\- `event.idm.read_only_udm.security_result.detection_fields.key`  
\- `event.idm.read_only_udm.security_result.detection_fields.value`  
\- `event.idm.read_only_udm.metadata.collected_timestamp.nanos`  
\- `event.idm.read_only_udm.metadata.collected_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.event_timestamp.nanos`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_version`  
\- `event.idm.read_only_udm.principal.asset_id`  
\- `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cvss_base_score`  
\- `event.idm.read_only_udm.security_result.about.asset.vulnerabilities.cvss_version`  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels.key`  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels.value`  
\- `event.idm.read_only_udm.security_result.about.resource.name`  
\- `event.idm.read_only_udm.security_result.rule_name`  
\- `event.idm.read_only_udm.security_result.severity_details`  
\- `event.idm.read_only_udm.target.location.country_or_region`  
2026-02-21 |  Enhancement  
-`event.idm.read_only_udm.additional.fields`: Newly mapped aws_log_group (key: aws_log_group), sampling_rate (key: sampling_rate), securityEvent (key: securityEvent), request-uuid (key: request-uuid), customer_id (key: customer_id), allocations (key: allocations), db (key: db), format (key: format), impersonated_user_id (key: impersonated_user_id), duration (key: duration), view (key: view), active-cuser-id (key: active-cuser-id), active-ps-dcid (key: active-ps-dcid), school_id (key: school_id), security_event (key: security_event), hosted-environment (key: hosted-environment), is-impersonating (key: is-impersonating), is-powerschool-employee (key: is-powerschool-employee), organization-client (key: organization-client), origin-cuser-id (key: origin-cuser-id), origin-ps-dcid (key: origin-ps-dcid), and product (key: product) raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
-`event.idm.read_only_udm.metadata.product_log_id`: Newly mapped aws_account_id raw log field with event.idm.read_only_udm.metadata.product_log_id UDM field.  
-`event.idm.read_only_udm.network.http.method`: Newly mapped `method` raw log field with event.idm.read_only_udm.network.http.method UDM field.  
-`event.idm.read_only_udm.network.http.response_code`: Newly mapped `status` raw log field with event.idm.read_only_udm.network.http.response_code UDM field.  
-`event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `host-instance` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname UDM fields`.  
-`event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `origin-role` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
-`event.idm.read_only_udm.security_result.description`: Newly mapped `action_detail` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
-`event.idm.read_only_udm.security_result.summary`: Newly mapped `service` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
-`event.idm.read_only_udm.target.application`: Newly mapped application raw log field with `event.idm.read_only_udm.target.application` UDM field.  
-`event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped host raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
-`event.idm.read_only_udm.target.url`: Newly mapped `url-requested` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
-`event.idm.read_only_udm.target.user.attribute.roles`: Newly mapped `active-role` raw log field with `event.idm.read_only_udm.target.user.attribute.roles` UDM field.  
-`Added support for a key-value log format using the kv filter plugin.  
-`event.idm.read_only_udm.metadata.product_event_type`:  
If `event-type` has a value, Set the value of `event.idm.read_only_udm.metadata.product_event_type` to the value of `event-type`.  
If `event-type` is empty and `controller` has a value, Set the value of `event.idm.read_only_udm.metadata.product_event_type` to the value of `controller`.  
-`event.idm.read_only_udm.network.http.referral_url`: If `action` contains http, Set the value of `event.idm.read_only_udm.network.http.referral_url` to the value of `action`.  
-`event.idm.read_only_udm.network.session_id`:  
If `user-session-id` has a value, Set the value to the value of `user-session-id`.  
If `session_id` has a value, updated the value to the value of `session_id`.  
-`event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
-`event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `http-request-origin-ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
-`event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
-`event.idm.read_only_udm.principal.user.userid`:  
If `logged_in_user_id` has a value, Set the value to `logged_in_user_id`.  
If `active-user-profile-id` has a value, updated the value to `active-user-profile-id`.  
If `user_id` has a value, updated the value to `user_id`.  
If `origin-user-profile-id` has a value, updated the value to `origin-user-profile-id`.  
-`event.idm.read_only_udm.security_result.action_details`: If `action` is not empty and does not contain http, Set the value of `event.idm.read_only_udm.security_result.action_details` to the value of `action`.  
-`event.idm.read_only_udm.security_result.severity`: If `level` contains WARN, updated the value of `event.idm.read_only_udm.security_result.severity` to MEDIUM.  
-`event.idm.read_only_udm.target.file.full_path`: If `file` is empty and path has a value, updated the value of `event.idm.read_only_udm.target.file.full_path` to the value of `path`.  
\- The above changes additionally is allowing the following UDM fields are now being parsed correctly:  
`event.idm.read_only_udm.metadata.event_timestamp.nanos`.  
`event.idm.read_only_udm.metadata.event_timestamp.seconds`.  
`event.idm.read_only_udm.metadata.event_type`.  
`event.idm.read_only_udm.metadata.log_type`.   
2026-02-18 |  Enhancement  
\- Newly added grok pattern for the `log` raw log field to parse the logs in the correct manner.  
\- Newly added kv filter for the `inner_kv` data field to fetch the raw log fields and map those fields to the respective UDM fields.  
\- Added on_error for the `severity` raw log field to parse the logs in the correct manner.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `realmId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `realmName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field  
\- `event.idm.read_only_udm.target.application`: Newly mapped `clientId` raw log field with `event.idm.read_only_udm.target.application` UDM field  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `userId` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `sessionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field  
\- `event.idm.read_only_udm.target.url`: Newly mapped `redirect_uri` raw log field with `event.idm.read_only_udm.target.url` UDM field  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `ipAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM field  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ipAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time_value_log` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `auth_type` (key: `Authentication_Type`), `thread_id` (key: `Thread_ID`), `response_type` (key: `Response_Type`), `consent` (key: `Consent`), `code_id` (key: `Code_ID`), `response_mode` (key: `Response_Mode`), `authSessionParentId` (key: `Auth_Session_Parent_ID`), `authSessionTabId` (key: `Auth_Session_Tab_ID`), `_p` (key: `raw_p_value`), `key_event` (key: `Key_Event`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `auth_method` (key: `Auth_Method`) raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` is `true`, `has_target_user` is `true`, and `type` contains `LOGIN`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` and `event.idm.read_only_udm.extensions.auth.type` to `AUTHTYPE_UNSPECIFIED`.   
2026-02-06 |  Enhancement  
\- Added support for parsing LEEF format syslogs.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `product_version` raw log field to `event.idm.read_only_udm.metadata.product_version`.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `event_id` raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `devTime` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `usrName` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `domain` raw log field to `event.idm.read_only_udm.principal.administrative_domain`.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `src` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src` raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `HostName` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `HostName` raw log field to `event.idm.read_only_udm.principal.asset.hostname`.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `MUID` raw log field to `event.idm.read_only_udm.principal.asset.asset_id`.  
\- `event.idm.read_only_udm.target.process.parent_process.file.md5`: Newly mapped `ParentHash` raw log field to `event.idm.read_only_udm.target.process.parent_process.file.md5`.  
\- `event.idm.read_only_udm.target.process.parent_process.file.full_path`: Newly mapped `ParentPath` raw log field to `event.idm.read_only_udm.target.process.parent_process.file.full_path`.  
\- `event.idm.read_only_udm.target.process.parent_process.pid`: Newly mapped `ParentPid` raw log field to `event.idm.read_only_udm.target.process.parent_process.pid`.  
\- `event.idm.read_only_udm.target.process.file.md5`: Newly mapped `ChildHash` raw log field to `event.idm.read_only_udm.target.process.file.md5`.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `ChildPath` raw log field to `event.idm.read_only_udm.target.process.file.full_path`.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `ChildPid` raw log field to `event.idm.read_only_udm.target.process.pid`.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `msg_id` raw log field to `event.idm.read_only_udm.metadata.product_log_id`.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `hostname` raw log field to `event.idm.read_only_udm.intermediary.hostname`.  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `appname` raw log field to `event.idm.read_only_udm.intermediary.application`.  
\- `event.idm.read_only_udm.intermediary.process.pid`: Newly mapped `proc_id` raw log field to `event.idm.read_only_udm.intermediary.process.pid`.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `sev` raw log field to `event.idm.read_only_udm.security_result.severity`.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `Action` raw log field to `event.idm.read_only_udm.security_result.action`.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Newly mapped `ParentCompany` raw log field to `event.idm.read_only_udm.security_result.about.resource.attribute.labels`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `log_type`, `organization`, `leef_version`, `facility`, `priority`, `version`, `LocalDateTime`, `PandaTimeStatus`, `ParentDriveType`, `ParentValidSig`, `ParentBroken`, `ParentImageType`, `ParentCat`, `ChildValidSig`, `ChildBroken`, `ChildImageType`, `ChildCat`, `OCS_Exec`, `ServiceLevel`, `WinningTech`, `DetId`, `TelemetryType`, `devTimeFormat`, `ParentExeType`, `ParentPrevalence`, `ParentPrevLastDay`, `ParentMWName`, `ChildDriveType`, `ChildCompany`, `ChildExeType`, `ChildPrevalence`, `ChildPrevLastDay`, `ChildMWName`, `OCS_Name`, `OCS_Version`, `Params`, `ToastResult`, `TTPS`, `IOAIds` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `devTime` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `sev` raw log field to `event.idm.read_only_udm.security_result.severity` with conditional logic.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `event.idm.read_only_udm.security_result.action` to `ALLOW` if `Action` is `Allow`.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `event.idm.read_only_udm.metadata.event_type` to `PROCESS_TERMINATION` when `event_id` is `endprocess` and both principal and target process information are present.  
\- Implemented KV filter to parse tab-delimited key-value pairs.   
2026-02-05 |  Enhancement  
\- event.idm.read_only_udm.principal.asset_id: Newly mapped `finding.AwsAccountId` raw log field with `event.idm.read_only_udm.principal.asset_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `finding.UpdatedAt`, `finding.Title`, `finding.FirstObservedAt`, `vulnerabilityvalue.Version`, `vulnerabilityvalue.Remediation`, `vulnerabilityvalue.Release`, `vulnerabilityvalue.PackageManager`, `vulnerabilityvalue.Name`, `vulnerabilityvalue.FixedInVersion`, `vulnerabilityvalue.Epoch`, `vulnerabilityvalue.Architecture`, `finding.SchemaVersion`, `vulnerability.RelatedVulnerabilities`, `vulnerability.ReferenceUrls`, `vulnerability.EpssScore`, `finding.AwsAccountName`, `finding.CompanyName`, `finding.GeneratorId`, `finding.ProductName`, `finding.RecordState`, `resource.Details.AwsEc2Instance.ImageId`, `resource.Details.AwsEc2Instance.SubnetId`, `resource.Details.AwsEc2Instance.Type`, `finding.ProductFields.aws/inspector/FindingStatus`, `finding.ProductFields.aws/inspector/inspectorScore`, `finding.ProductFields.aws/inspector/instanceId`, `finding.ProductFields.aws/inspector/resources/1/resourceDetails/awsEc2InstanceDetails/platform`, `resource.Tags.Application`, `resource.Tags.BuildBy`, `resource.Tags.Environment`, `resource.Tags.FacultyName`, `resource.Tags.Lifecycle`, `resource.Tags.Support`, and `resource.Tags.ams:rt:ams-managed` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `finding.CreatedAt` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `finding.Description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `finding.FindingProviderFields.Severity.Label` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `finding.FindingProviderFields.Severity.Normalized` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `finding.FindingProviderFields.Types` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vulnerability.LastKnownExploitAt`, `vulnerability.ExploitAvailable`, `vulnerability.FixAvailable`, `finding.LastObservedAt`, `finding.ProcessedAt`, and `finding.ProductArn` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.location.country_or_region: Newly mapped `finding.Region` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `finding.Remediation.Recommendation.Text` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `resource.Details.AwsEc2Instance.IpV4Addresses` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.attribute.creation_time: Newly mapped `resource.Details.AwsEc2Instance.LaunchedAt` raw log field with `event.idm.read_only_udm.target.asset.attribute.creation_time` UDM field.  
\- event.idm.read_only_udm.target.asset.attribute.cloud.vpc.id: Newly mapped `resource.Details.AwsEc2Instance.VpcId` raw log field with `event.idm.read_only_udm.target.asset.attribute.cloud.vpc.id` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `finding.ProductFields.aws/inspector/ProductVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.security_result.about.asset.vulnerabilities: Newly mapped `vulnerability.Cvss` raw log field with `event.idm.read_only_udm.security_result.about.asset.vulnerabilities` UDM field.   
2025-12-24 |  Enhancement  
\- Added a check for the `json_message_failed` flag. If true, the event will be dropped with the tag `TAG_MALFORMED_MESSAGE`.   
2025-11-07 |  Enhancement  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `logevent.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `logevent.timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `record.owner` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.location.name: Newly mapped `logevent.message.availability_zone`, `msgs.availability_zone` raw log fields with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `logevent.message.event_data.dest_ip`, `msgs.event.dest_ip` raw log fields with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `logevent.message.event_data.dest_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `logevent.message.event_data.dest_port`, `msgs.event.dest_port` raw log fields with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `logevent.message.event_data.flow_id`, `msgs.event.flow_id` raw log fields with event.idm.read_only_udm.network.session_id UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `logevent.message.event_data.src_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `logevent.message.event_data.src_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `logevent.message.firewall_name`, `msgs.firewall_name` raw log fields with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `logevent.message.event_data.alert.rev`, `logevent.message.event_data.alert.signature`, `logevent.message.event_data.alert.signature_id`, `logevent.message.event_data.pkt_src`, `msgs.event.alert.rev`, `msgs.event.alert.signature`, `msgs.event.alert.signature_id`, `msgs.event.pkt_src` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `record.messageType` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.about.resource.name: Newly mapped `record.logGroup` raw log field with `event.idm.read_only_udm.security_result.about.resource.name` UDM field.  
\- event.idm.read_only_udm.security_result.about.resource.attribute.labels: Newly mapped `record.logStream`, `record.subscriptionFilters` raw log fields with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `logevent.message.event_data.alert.action`, `logevent.message.event_data.verdict.action`, `msgs.event.alert.action`, `msgs.event.verdict.action` raw log fields with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `logevent.message.event_data.alert.severity`, `msgs.event.alert.severity` raw log fields with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.network.direction: Newly mapped `logevent.message.event_data.direction`, `msgs.event.direction` raw log fields with `event.idm.read_only_udm.network.direction` UDM field.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `logevent.message.event_data.proto`, `msgs.event.proto` raw log fields with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- event.idm.read_only_udm.security_result.description: When `logevent.message` contains JSON, it is now parsed for mapping to UDM fields, instead of being mapped to `security_result.description`.  
\- event.idm.read_only_udm.metadata.event_type: If has_principal and has_target are true, updated to NETWORK_CONNECTION  
\- event.idm.read_only_udm.metadata.event_type: If has_principal is true, updated to STATUS_UPDATE  
\- event.idm.read_only_udm.metadata.event_type: If has_user is true, updated to USER_UNCATEGORIZED   
2025-05-29 |  Enhancement  
\- `event.idm.read_only_udm.target.user.product_object_id` : Newly mapped `accountID` raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `file` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels` : Newly mapped `func`, `pointsToLaunchpadArn`, `result`, `logGroup.Arn`, `logGroup.DataProtectionStatus`, `logGroup.InheritedProperties`, `logGroup.KmsKeyId`, `logGroup.LogGroupClass`, `logGroup.MetricFilterCount`, `logGroup.RetentionInDays`,and `logGroup.StoredBytes` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.severity` : Newly mapped `level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id` : Newly mapped `logGroupArn` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name` : Newly mapped `logGroupName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `lpclagg`, `lpcltype` rawlog fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.description` : Newly mapped `msg` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id` : Newly mapped `requestID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.application` : Newly mapped `service` raw log filed with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp` : Newly mapped `time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-04-11 |  Enhancement  
\- `JSON`: Added support for `JSON` format.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `logevent.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `owner` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.about.resource.name`: Newly mapped `logGroup` raw log field with `event.idm.read_only_udm.security_result.about.resource.name` UDM field.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Newly mapped `logStream` raw log field with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `logevent.message` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `act_det` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `tar_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `tar_host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `tar_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `resp_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `rec_bytes` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `meth` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `event.idm.read_only_udm.network.http.user_agent` as `NETWORK_CONNECTION` when `src_ip` and `tar_ip` raw log fields are not null.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped event.idm.read_only_udm.metadata.event_type UDM field as USER_UNCATEGORIZED when owner raw log field is not null.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `event.idm.read_only_udm.metadata.event_type` UDM field as `GENERIC_EVENT` when `src_ip` , `tar_ip` and `tar_port` raw log fields are null.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Newly mapped `subscriptionFilter` raw log field with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.   
2025-03-05 |  Enhancement  
\- Mapped `log_processed_control_data_sampling_interval`, `log_processed_cpus_per_sock_avg`, `log_processed_cpus_per_sock_max`, `log_processed_cpus_per_sock_min`, `flow_aggregation_result` fields, `flows_after`, `flows_before`, `level`, `message`, `sock_add_result` fields, `sock_cache_len`, `sock_delta_result` fields, `sock_eviction_result` fields, `sock_nat_result` fields, `container_hash`, `container_image` to `additional.fields`.  
\- Mapped `kubernetes_host_details` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `prin_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `kubernetes_pod_id` to `principal.product_object_id`.  
\- Mapped `kubernetes_pod_name` to `principal.namespace` if `has_namespace` is `false` else mapped to `additional.fields`.  
\- Mapped `log_processed_level` to `sec_result.severity`.   
2025-02-22 |  Enhancement  
\- Added support to parse unparsed logs.   
2025-02-04 |  Enhancement  
\- Added support to parse unparsed logs.   
2024-11-12 |  Enhancement  
\- Added support to parse unparsed logs.   
2024-10-18 |  Enhancement  
\- Added support to parse unparsed logs.   
2024-08-29 |  Enhancement  
\- Added support to parse unparsed logs.  
\- Mapped `connectionTesterClassName` to `principal.hostname`.  
\- Mapped `identityToken` to `principal.user.userid`.  
\- Mapped `jdbcUrl` to `target.url`.  
\- Mapped `driverClass` to `target.application`.  
\- Mapped `uid` to `metadata.product_log_id`.  
\- Mapped `summary` to `security_result.summary`.  
\- Mapped `script` to `security_result.description`.   
2024-02-12 |  Enhancement  
\- Mapped timestamp to UNIX_MS.   
2023-09-02 |  Enhancement  
\- Added a `kv block` to parse key-value format logs.  
\- Mapped `SourceIP` to `principal.ip`.  
\- Mapped `prin_host` to `principal.hostname`.  
\- Mapped `User` to `principal.user.userid`.  
\- Mapped `Ciphers` to `network.tls.client.supported_ciphers`.  
\- Mapped `executionId` to `principal.process.pid`.  
\- Mapped `transferDetails.sessionId` to `network.session_id`.  
\- Mapped `transferDetails.username` to `principal.user.user_display_name`.  
\- Mapped `transferDetails.serverId`, `workflowId`, `details.input.initialFileLocation.etag`, `details.input.initialFileLocation.backingStore`, `details.input.initialFileLocation.bucket`, `details.input.initialFileLocation.key`,  
`Mode`, `Kex` to `additional.fields`.  
\- Mapped `BytesIn` to `network.received_bytes`.  
\- Mapped `Role` to `target.resource.product_object_id`.   
2023-08-18 |  Enhancement  
\- Added a Grok pattern to parse the unparsed raw logs.   
2023-07-07 |  Enhancement  
\- Added support for `logEvents`-related JSON logs.   
2022-12-17 |  Enhancement:  
\- Mapped `CloudType` to `target.resource.attribute.cloud.environment`.  
\- Mapped `AlertId` to `metadata.product_log_id`.  
\- Mapped `ResourceType` to `target.resource.resource_subtype`.  
\- Mapped `ResourceRegion` to `target.location.country_or_region`.  
\- Mapped `Recommendation` to `security_result.detection_fields`.  
\- Mapped `PolicyName`,`detail.additionalEventData.configRuleName` to `security_result.rule_name`.  
\- Mapped `detail-type` to `metadata.product_event_type`.  
\- Mapped `region`,`detail.awsRegion` to `principal.location.name`.  
\- Mapped `detail.eventSource` to `target.application`.  
\- Mapped `detail.requestID` to `target.resource.attribute.labels`.  
\- Mapped `detail.userAgent` to `network.http.user_agent`.  
\- Mapped `detail.eventVersion` to `metadata.product_version`.  
\- Mapped `detail.userIdentity.accountId` to `metadata.product_deployment_id`.  
\- Mapped `detail.userIdentity.accessKeyId` to `target.user.userid`.  
\- Mapped `detail.userIdentity.type` to `principal.resource.type`.  
\- Mapped `detail.userIdentity.principalId` to `principal.user.product_object_id`.  
\- Mapped `detail.user.arn` to `target.user.userid`.  
\- Mapped `detail.user.sessionContext.sessionIssuer.userName` to `target.user.user_display_name`.  
\- Mapped `detail.user.mfaAuthenticated` to `principal.user.attribute.labels`.  
\- Mapped `detail.recipientAccountId` to `target.resource.attribute.labels`.  
\- Mapped `detail.managementEvent`, `detail.eventType`, `detail.readOnly`, `detail.eventName`, `detail.additionalEventData.notificationJobType`, `detail.additionalEventData.managedRuleIdentifier`, `duration`, `billed_duration`, `memory_used` to `additional.fields`.  
\- Mapped `detail.eventCategory` to `security_result.category_details`.  
\- Mapped `detail.eventID` to `metadata.product_log_id`.  
\- Mapped `detail.additionalEventData.configRuleArn` to `security_result.rule_id`.  
\- Mapped `level` to `security_result.severity`.  
\- Mapped `src_port` to `principal.port`.  
\- Mapped `request_id` to `target.resource.attribute.labels`.  
\- Mapped `url` to `target.url`.   
2022-09-03 |  Enhancement  
\- Added grok to parse newly ingested logs.  
\- Mapped `package` to `event.idm.read_only_udm.principal.process.command_line`.  
\- Mapped `session_id` to `event.idm.read_only_udm.network.session_id`.  
\- Mapped `network_dir` to `event.idm.read_only_udm.network.direction`.  
\- Mapped `port` to `event.idm.read_only_udm.target.port`.  
\- Remapped `digestPublicKeyFingerprint` from `additional.fields` to `event.idm.read_only_udm.target.file.sha1`.  
\- Added other log levels like `AUDIT`, `TRACE`, `DEBUG`, `NOTICE`, `ERROR` for severity mapping.  
\- Duplicated the value in `target.ip` to `principal.ip` to set event_type as `STATUS_UPDATE` thereby reducing generic percentage.  
\- Added conditions for `event_type` `USER_UNCATEGORIZED`, `NETWORK_HTTP`, `NETWORK_CONNECTION`, `STATUS_UPADTE` to reduce generic percentage.   
2022-08-11 |  Bug Fix - Remapped `digestS3Bucket` to `principal.resource.name`.  
Remapped `kubernetes.pod_name` to `additional.fields`.   
2022-05-27 |  Enhancement - Modified the value stored in metadata.product_name to `AWS CloudWatch` and metadata.vendor_name to `AMAZON`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
