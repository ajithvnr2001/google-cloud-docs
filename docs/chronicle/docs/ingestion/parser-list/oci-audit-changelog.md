---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oci-audit-changelog/
title: Change log for OCI_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:56:50.275195+00:00
---

# Change log for OCI_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oci-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OCI_AUDIT

Date | Changes  
---|---  
2026-05-19 |  Enhancement:  
\- `OracleDatabaseUnifiedAudit`: Added support for the event `OracleDatabaseUnifiedAudit` and relevant corresponding raw log fields.  
\- Added a conditional check before already existing mapping of `message` to handle `OracleDatabaseUnifiedAudit`.  
\- Added a `mutate` to remove newlines from `message`.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `data.auditEventTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `data.auditLocation`, `data.auditPolicies`, `data.auditType`, `data.databaseType`, `data.databaseUniqueName`, `data.extendedEventAttributes`, `data.isAlerted`, `data.operation`, `data.osTerminal`, `subject` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `data.clientHostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `data.clientIp` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `data.clientProgram` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `data.dbUserName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `data.eventName` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `data.targetId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `data.targetName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `data.timeCollected` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: If `data.operationStatus` is SUCCESS, updated the value of `event.idm.read_only_udm.security_result.action` to ALLOW.  
\- `event.idm.read_only_udm.security_result.action`: If `data.operationStatus` is FAILURE, updated the value of `event.idm.read_only_udm.security_result.action` to BLOCK.  
\- `event.idm.read_only_udm.principal.user.userid`: If `data.osUserName` is present and `data.dbUserName` is empty, updated the value of `event.idm.read_only_udm.principal.user.userid` to `data.osUserName`.  
\- `event.idm.read_only_udm.target.resource.resource_type`: If `data.targetClass` is DATABASE, updated the value of `event.idm.read_only_udm.target.resource.resource_type` to DATABASE.   
2026-04-15 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `additionalDetails_actorId` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `actorDisplayName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `additionalDetails_actorName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `additionalDetails_actorOcid`, `domainId`, `additionalDetails_idcsCreatedBy_value`, `additionalDetails_idcsLastModifiedBy_value`, `principalId`, `actorOcid`, `actorName`, `actorType`, `idcsCreatedBy_value`, `idcsCreatedBy_type`, `idcsCreatedBy_display`, `idcsLastModifiedBy_display`, `idcsLastModifiedBy_value`, `idcsLastModifiedBy_type`, `callerId`, `callerName`, `resourceId` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `clientIp`, `ipAddress` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `domainDisplayName` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `ecId`, `logContent_id`, `httpResponseStatus`, `ssoCompletedFactors`, `ssoMatchedSignOnPolicy`, `ssoMatchedSignOnRule`, `ssoMatchedSignOnPolicyName`, `ssoMatchedSignOnRuleName`, `consoleSessionId`, `auditEventMapValue_message`, `oracle_compartmentid` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.group.product_object_id`: Newly mapped `domainName` raw log field with `event.idm.read_only_udm.principal.group.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `eventId` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `additionalDetails_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `created_value`, `additionalDetails_meterAsOPCService`, `additionalDetails_ssoIdentityProviderType`, `additionalDetails_ssoSessionCreateTime`, `timestamp`, `logContent_dataschema`, `logContent_oracle_compartmentid`, `loggroupid`, `logContent_source`, `rId`, `schemas`, `clientName`, `reasonValue`, `actorId`, `ssoRp`, `ssoCSR`, `ssoApplicationId`, `ssoApplicationName`, `ssoApplicationType`, `ssoSessionCreateTime`, `ssoSessionExpiryTime`, `ssoAuthnLevel`, `ssoIdentityProviderType`, `ssoPolicyObligations`, `meterAsOPCService`, `quotaCount`, `id`, `checksum`, `meta_created`, `meta_lastModified`, `definedTags`, `eventGroupingId`, `freeformTags`, `authType`, `identity_credentials`, `action`, `parameters`, `path`, `headers`, `response_message`, `payload`, `current`, `previous`, `datetime`, `request_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `additionalDetails_ssoApplicationId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `additionalDetails_ssoApplicationName` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `additionalDetails_ssoApplicationType`, `additionalDetails_ssoRp`, `oracle_tenantid`, `logContent_type`, `ssoSessionId` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped `additionalDetails_ssoIdentityProvider` raw log field with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `additionalDetails_ssoMatchedSignOnPolicy` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `additionalDetails_ssoSessionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `availabilityDomain`, `compartmentId`, `compartmentName`, `principalName`, `tenantId` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `eventName` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `identity_userAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `logContent_specversion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `data_message` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `status` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `responseTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `ssoLocalIp`, `hostIp` raw log fields with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `hostName` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `clientId` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `serviceName` raw log field with `event.idm.read_only_udm.intermediary.application` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `ssoProtectedResource` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `ssoComments` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `logContent_type` is `com.oraclecloud.IdentitySignOn.InteractiveLogin` and `eventName` is `InteractiveLogin`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN`.  
\- `event.idm.read_only_udm.metadata.ingested_timestamp`: Newly mapped `ingestedtime` raw log field with `event.idm.read_only_udm.metadata.ingested_timestamp` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.mechanism`: Newly mapped `ssoIdentityProvider` raw log field with `event.idm.read_only_udm.extensions.auth.mechanism` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: Newly mapped `ssoPlatform` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- `event.idm.read_only_udm.principal.browser.browser_type`: Newly mapped `ssoBrowser` raw log field with `event.idm.read_only_udm.principal.browser.browser_type` UDM field.  
\- `event.idm.read_only_udm.security_result.last_updated_time`: Newly mapped `lastModified_value` raw log field with `event.idm.read_only_udm.security_result.last_updated_time` UDM field.   
2026-04-08 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: If event has both `principal_user` and `target_resource`, updated the value of `event.idm.read_only_udm.metadata.event_type` to USER_RESOURCE_ACCESS.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `data.identity.authType`, `data.response.responseTime`, `dataschema` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `oracle.ingestedtime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.   
2025-10-28 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `column3` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Added a Grok pattern to support mapping of Newly mapped `column2` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `column2` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `column6` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `column6` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped static value `ALLOW` with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.type`: Newly mapped static value `AUTHTYPE_UNSPECIFIED` with `event.idm.read_only_udm.extensions.auth.type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped static value `OCI_AUDIT` with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped static value `Oracle` with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `column3` is `login successful`, updated to `USER_LOGIN`.  
\- `event.idm.read_only_udm.metadata.event_type` is conditionally set to STATUS_UPDATE or GENERIC_EVENT based on the presence of principal information.  
\- The existing JSON parsing logic is now enclosed in an `else` block to handle logs that are not pipe-separated.   
2025-03-21 |  Enhancement:  
\- Mapped `data.backendAddr` to `target.ip` and `target.asset.ip`, and `target.port`.  
\- Mapped `data.clientAddr` to `principal.ip`, `principal.asset.ip`, and `principal.port`.  
\- Mapped `data.forwardedForAddr` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `data.host` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `data.backendConnectTime`, `data.backendProcessingTime`, `data.listenerName`, `data.requestProcessingTime`, `data.routingRulesEngineErrors`, `data.routingRulesMatchedRule`, `data.routingRulesRuleHits`, `oracle.loggroupid`, `oracle.logid`, `oracle.resourceid`, `source` and `data.routingRulesRuleMisses` to `additional.fields`.  
\- Mapped `data.backendStatusCode` to `network.http.response_code`.  
\- Mapped `data.receivedBytes` to `network.received_bytes`.  
\- Mapped `data.sentBytes` to `network.sent_bytes`.  
\- Mapped `data.sslCipher` to `network.tls.cipher`.  
\- Mapped `data.sslProtocol` to `network.tls.version`.  
\- Mapped `data.userAgent` to `network.http.user_agent`.   
2025-01-30 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2024-11-22 |  Enhancement:  
\- Mapped `data.request.headers.oci-original-url.0` to `principal.url`.  
\- Mapped `originalConnection.destinationIp` to `target.ip` and `target.asset.ip`.  
\- Mapped `originalConnection.destinationPort` to `target.port`.  
\- Mapped `originalConnection.sourcePort` to `principal.port`.  
\- Mapped `originalConnection.protocol` to `network.application_protocol`.   
2024-10-24 |  Enhancement:  
\- Added support to handle JSON logs.   
2024-06-14 |  Enhancement:  
\- If `has_principal_user`, `has_target_user`, or `has_target` is `true`, then set `metadata.event_type` to `USER_UNCATEGORIZED`.   
2023-09-29 |  Bug-Fix:  
\- Added a Grok pattern before mapping `data.identity.ipAddress` to UDM fields.  
\- Mapped `ip1` to `principal.ip`.  
\- Mapped `ip2` to `principal.ip`.   
2023-05-23 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
