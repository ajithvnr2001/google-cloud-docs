---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/armis-activities-changelog/
title: Change log for ARMIS_ACTIVITIES \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:55:00.283672+00:00
---

# Change log for ARMIS_ACTIVITIES  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/armis-activities-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ARMIS_ACTIVITIES

Date | Changes  
---|---  
2026-08-30 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `site.location`, `site.name`, `decisionData.srcDeviceId`, `decisionData.hmiDeviceId`, `decisionData.queryType`, `decisionData.protocol`, `decisionData.deviceId`, `decisionData.host`, `sourceEndpoint.businessImpact`, `sourceEndpoint.sites`, `sourceEndpoint.boundaries`, `destinationEndpoint.dataSources`, `destinationEndpoint.businessImpact`, `destinationEndpoint.boundaries` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.asset.product_object_id`: Newly mapped `decisionData.smbData.smbServerDeviceId`, `decisionData.plcDeviceId`, `decisionData.targetDeviceId` raw log fields with `event.idm.read_only_udm.target.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `sourceEndpoint.id` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.observer.asset.product_object_id`: Newly mapped `decisionData.sensorId` raw log field with `event.idm.read_only_udm.observer.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `decisionData.serverDeviceId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `decisionData.otProtocol` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `decisionData.errorType` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `decisionData.method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `decisionData.userAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `decisionData.result` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.intermediary.port`: Newly mapped `decisionData.port` raw log field with `event.idm.read_only_udm.intermediary.port` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `destinationEndpoint.name` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.asset.attribute.labels`: Newly mapped `decisionData.vlan`, `destinationEndpoint.riskLevel`, `destinationEndpoint.id` raw log fields with `event.idm.read_only_udm.target.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `decisionData.clientDeviceId` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `site.name` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.principal.asset.location.name`: Newly mapped `site.location` raw log field with `event.idm.read_only_udm.principal.asset.location.name` UDM field.  
\- `event.idm.read_only_udm.network.tls.client.supported_ciphers`: Newly mapped `decisionData.clientOfferedSuites` raw log field with `event.idm.read_only_udm.network.tls.client.supported_ciphers` UDM field.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `decisionData.selectedSuite` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.read_only_udm.network.tls.established`: Newly mapped `decisionData.sslConnectionStatus` raw log field with `event.idm.read_only_udm.network.tls.established` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `decisionData.version` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.network.dns.answers`: Newly mapped `decisionData.answerIps` raw log field with `event.idm.read_only_udm.network.dns.answers` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `decisionData.requestedDialects`, `decisionData.selectedSuiteSecurityLevel` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `sourceEndpoint.name` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `sourceEndpoint.ip`, `decisionData.srcIp` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `sourceEndpoint.macAddress`, `decisionData.srcMac` raw log fields with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.security_result.risk_score`: Newly mapped `sourceEndpoint.riskLevel` raw log field with `event.idm.read_only_udm.security_result.risk_score` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `destinationEndpoint.name` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `destinationEndpoint.name` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields when `destinationEndpoint.name` is an IP address.  
\- `event.idm.read_only_udm.target.asset_id`: Newly mapped `destinationEndpoint.id` raw log field with `event.idm.read_only_udm.target.asset_id` UDM field.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Newly mapped `destinationEndpoint.id` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `destinationEndpoint.ip`, `decisionData.serverIp` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac`: Newly mapped `destinationEndpoint.macAddress`, `decisionData.nicIdentifier` raw log fields with `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.about.ip`: Newly mapped `decisionData.ip` raw log field with `event.idm.read_only_udm.about.ip` UDM field.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `destinationEndpoint.sites` raw log field with `event.idm.read_only_udm.target.location.name` UDM field.   
2025-10-23 |  Enhancement:  
\- Added support for an optional Syslog header before the JSON payload.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `source_user` raw log field to `event.idm.read_only_udm.principal.user.user_display_name`.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field from syslog header to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `intermediary_hostname` raw log field to `event.idm.read_only_udm.intermediary.hostname`.  
\- `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `intermediary_hostname` raw log field to `event.idm.read_only_udm.intermediary.asset.hostname`.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `id` raw log field to `event.idm.read_only_udm.security_result.rule_id`.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` and `policy.actions.actionType` raw log fields to `event.idm.read_only_udm.security_result.severity`.  
\- `event.idm.read_only_udm.security_result.risk_score`: Newly mapped `riskLevel` raw log field to `event.idm.read_only_udm.security_result.risk_score`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `status` and `activities.decision_data.risk_factor_type` raw log fields to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `policy.description` raw log field to `event.idm.read_only_udm.security_result.description`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `classification`,`policy.labels`, `policy.rules.and`, `policy.actions.actionParams.title`, `policy.actions.actionParams.alertDescription`, `policy.actions.actionParams.alertClassificationId`, `policy.actions.actionParams.endpoint`, `policy.actions.actionParams.timeBack`, `policy.actions.actionParams.emailRecipients`, `sources.sensor.name`, `sources.sensor.type`, `sources.boundaries`, `sources.dataSources`, `policy.isActive`, `policy.isBoundary`, `policy.isEditable`, `policy.creationTime`, `policy.modificationTime`, `policy.owner`, `activities.type`, `activities.decision_data.client_offered_suites`, `activities.decision_data.selected_suite`, `activities.decision_data.src_device_id`, `activities.decision_data.risk_factor_id`, `activities.decision_data.risk_factor_category`, `activities.decision_data.risk_factor_description`, `activities.decision_data.risk_factor_score`, `activities.decision_data.connection`, `activities.decision_data.category`, and `activities.decision_data.client_device_id` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `policy.actions.actionType` raw log field to `event.idm.read_only_udm.security_result.severity_details`.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `sources.category` raw log field to `event.idm.read_only_udm.security_result.category_details`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `sources.id` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `sources.ip`, `sources.ipv6`, and `activities.decision_data.src_ip` raw log fields to `event.idm.read_only_udm.principal.ip`.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `sources.ip`, `sources.ipv6`, and `activities.decision_data.src_ip` raw log fields to `event.idm.read_only_udm.principal.asset.ip`.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `sources.name` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `sources.name` raw log field to `event.idm.read_only_udm.principal.asset.hostname`.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `sources.site.name` raw log field to `event.idm.read_only_udm.principal.location.name`.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `sources.site.location` raw log field to `event.idm.read_only_udm.principal.location.country_or_region`.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `sources.type` and `sources.model` raw log fields to `event.idm.read_only_udm.principal.user.attribute.labels`.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `sources.identifier` raw log field to `event.idm.read_only_udm.principal.mac`.  
\- `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `sources.identifier` raw log field to `event.idm.read_only_udm.principal.asset.mac`.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `sources.identifier` raw log field to `event.idm.read_only_udm.principal.asset.product_object_id` when it's not a valid MAC address.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `activities.UUID` raw log field to `event.idm.read_only_udm.metadata.product_log_id`.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `activities.decision_data.version` raw log field to `event.idm.read_only_udm.network.tls.version`.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `activities.decision_data.host` raw log field to `event.idm.read_only_udm.target.ip`.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `activities.decision_data.host` raw log field to `event.idm.read_only_udm.target.asset.ip`.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `activities.decision_data.host` raw log field to `event.idm.read_only_udm.target.hostname`.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `activities.decision_data.host` raw log field to `event.idm.read_only_udm.target.asset.hostname`.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `activities.decision_data.port` raw log field to `event.idm.read_only_udm.target.port`.  
\- `event.idm.read_only_udm.security_result.confidence`: Newly mapped `activities.decision_data.confidence` raw log field to `event.idm.read_only_udm.security_result.confidence`.  
\- `event.idm.read_only_udm.security_result.confidence_details`: Newly mapped `activities.decision_data.confidence` raw log field to `event.idm.read_only_udm.security_result.confidence_details`.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `activities.decision_data.protocol` raw log field to `event.idm.read_only_udm.network.application_protocol`.  
\- `event.idm.read_only_udm.network.dns.questions.name`: Newly mapped `activities.decision_data.host` and `activities.decision_data.query_type` raw log fields to `event.idm.read_only_udm.network.dns.questions.name` for DNS_QUERY events.  
\- `event.idm.read_only_udm.network.dns.answers.data`: Newly mapped `activities.decision_data.answer_ips` raw log field to `event.idm.read_only_udm.network.dns.answers.data` for DNS_QUERY events.  
\- Modified grok patterns to handle the optional Syslog header and extract the JSON data.  
\- The `metadata.event_type` is now dynamically set to `NETWORK_CONNECTION`, `USER_UNCATEGORIZED`, `STATUS_UPDATE`, or `GENERIC_EVENT` based on the presence of principal, target, and user information, replacing the previous hardcoded value.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
