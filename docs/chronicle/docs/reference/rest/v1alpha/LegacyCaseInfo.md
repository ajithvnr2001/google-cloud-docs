---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo/
title: LegacyCaseInfo \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:01.457702+00:00
---

# LegacyCaseInfo  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  LegacyCaseInfo Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * LegacyCaseSecurityEvent
    * JSON representation
  * LegacyCasePropertyValue
    * JSON representation
  * CaseType
  * CasePriority
  * LegacyCaseInfoAttachment
    * JSON representation
  * LoadDataTypeEnumQueue
  * IngestionSourceType



CaseInfo represents the case information model.

JSON representation  
---  
      
    
    {
      "creatorUserId": string,
      "events": [
        {
          object ([LegacyCaseSecurityEvent](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#LegacyCaseSecurityEvent))
        }
      ],
      "environment": string,
      "sourceSystemName": string,
      "ticketId": string,
      "description": string,
      "displayId": string,
      "reason": string,
      "name": string,
      "deviceVendor": string,
      "deviceProduct": string,
      "startTime": string,
      "endTime": string,
      "ruleGenerator": string,
      "sourceGroupingIdentifier": string,
      "playbookTriggerKeywords": [
        string
      ],
      "extensions": [
        {
          object ([LegacyCasePropertyValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#LegacyCasePropertyValue))
        }
      ],
      "attachments": [
        {
          object ([LegacyCaseInfoAttachment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#LegacyCaseInfoAttachment))
        }
      ],
      "sourceSystemUrl": string,
      "sourceRuleIdentifier": string,
      "siemAlertId": string,
      "updatedFields": [
        {
          object ([LegacyCasePropertyValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#LegacyCasePropertyValue))
        }
      ],
      "alertMetadata": {
        string: value,
        ...
      },
      "dataAccessScope": string,
      "type": enum ([CaseType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#CaseType)),
      "priority": enum ([CasePriority](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#CasePriority)),
      "isTrimmed": boolean,
      "dataType": enum ([LoadDataTypeEnumQueue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#LoadDataTypeEnumQueue)),
      "sourceType": enum ([IngestionSourceType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#IngestionSourceType)),
      "alertUpdateSupported": boolean
    }  
  
Fields  
---  
`creatorUserId` |  `string` Optional. CreatorUserId identifies the user who creates this case - only relevant for cases of type Request.  
`events[]` |  `object (`[LegacyCaseSecurityEvent](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#LegacyCaseSecurityEvent)`)` Required. Events is a list of the events that make up this case.  
`environment` |  `string` Optional. Environment is the case environment.  
`sourceSystemName` |  `string` Optional. SourceSystemName is the name of the source system - based on the connector.  
`ticketId` |  `string` Optional. TicketId is the external case id received from the external product - based on the connector.  
`description` |  `string` Optional. Description is the case description.  
`displayId` |  `string` Optional. DisplayId is the external case display id received from the external product - based on the connector.  
`reason` |  `string` Optional. Reason is the case reason.  
`name` |  `string` Optional. Name is the case name.  
`deviceVendor` |  `string` Optional. DeviceVendor is the case product vendor - based on the connector.  
`deviceProduct` |  `string` Optional. DeviceProduct is the case product vendor - based on the connector.  
`startTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. StartTime is the case starting time in unix format as milliseconds - based on the connector. Represents DateTime StartTime as unix time  
`endTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. EndTime is the case ending time in unix format as milliseconds - based on the connector. Represents DateTime EndTime as unix time  
`ruleGenerator` |  `string` Optional. RuleGenerator is the rule that generates this case - based on the connector.  
`sourceGroupingIdentifier` |  `string` Optional. SourceGroupingIdentifier is the source grouping identifier will be used to group alert into one case - depends on alert grouping configuration - based on the connector.  
`playbookTriggerKeywords[]` |  `string` Optional. PlaybookTriggerKeywords is the playbook trigger keywords - used for 'Alert Trigger Value' playbook trigger type.  
`extensions[]` |  `object (`[LegacyCasePropertyValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#LegacyCasePropertyValue)`)` Optional. Extensions is an obsolete field.  
`attachments[]` |  `object (`[LegacyCaseInfoAttachment](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#LegacyCaseInfoAttachment)`)` Optional. Attachments is the case attachments - based on the connector.  
`sourceSystemUrl` |  `string` Optional. SourceSystemUrl is the configured source url - defined in the connector that ingested this alert.  
`sourceRuleIdentifier` |  `string` Optional. SourceRuleIdentifier is the configured source rule url - defined in the connector that ingested this alert.  
`siemAlertId` |  `string` Optional. SiemAlertId is the Chronicle SIEM alert identifier.  
`updatedFields[]` |  `object (`[LegacyCasePropertyValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#LegacyCasePropertyValue)`)` Optional. UpdatedFields is the alert Updated Fields.  
`alertMetadata` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Optional. AlertMetadata is the additional alert metadata as key-value pairs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`dataAccessScope` |  `string` Optional. DataAccessScope is the Chronicle SIEM resource name of the DataAccessScope of this alert.  
`type` |  `enum (`[CaseType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#CaseType)`)` Optional. Type is the case type.  
`priority` |  `enum (`[CasePriority](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#CasePriority)`)` Optional. Priority is the case priority.  
`isTrimmed` |  `boolean` Optional. IsTrimmed is a flag that indicates whether the case got trimmed or not.  
`dataType` |  `enum (`[LoadDataTypeEnumQueue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#LoadDataTypeEnumQueue)`)` Optional. DataType is the case data type.  
`sourceType` |  `enum (`[IngestionSourceType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#IngestionSourceType)`)` Optional. SourceType is the case source type.  
`alertUpdateSupported` |  `boolean` Optional. AlertUpdateSupported indicates if the alert source system support alert updates.  
  
## LegacyCaseSecurityEvent

SecurityEvent represents a security event.

JSON representation  
---  
      
    
    {
      "environment": string,
      "sourceSystemName": string,
      "extensions": [
        {
          object ([LegacyCasePropertyValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#LegacyCasePropertyValue))
        }
      ],
      "parentEventId": string,
      "sourceMacAddress": string,
      "destinationMacAddress": string,
      "name": string,
      "message": string,
      "type": string,
      "severity": string,
      "eventId": string,
      "managerReceiptTime": string,
      "startTime": string,
      "ruleGenerator": string,
      "endTime": string,
      "deviceHostName": string,
      "deviceAddress": string,
      "destinationDnsDomain": string,
      "destinationNtDomain": string,
      "sourceDnsDomain": string,
      "sourceNtDomain": string,
      "deviceEventClassId": string,
      "transportProtocol": string,
      "applicationProtocol": string,
      "destinationPort": string,
      "categoryOutcome": string,
      "deviceEventCategory": string,
      "deviceVendor": string,
      "deviceProduct": string,
      "deviceSeverity": string,
      "fileType": string,
      "baseEventIds": [
        string
      ],
      "cefVersion": string,
      "deviceVersion": string,
      "signatureId": string,
      "description": string,
      "receiptTime": string,
      "rawDataFields": {
        string: string,
        ...
      },
      "destinationUrl": string,
      "creditCard": string,
      "phoneNumber": string,
      "cve": string,
      "threatActor": string,
      "threatCampaign": string,
      "process": string,
      "parentProcess": string,
      "parentHash": string,
      "childProcess": string,
      "ipset": string,
      "cluster": string,
      "application": string,
      "database": string,
      "pod": string,
      "container": string,
      "service": string,
      "genericEntity": string,
      "sourceProcessName": string,
      "fileName": string,
      "fileHash": string,
      "deployment": string,
      "emailSubject": string,
      "threatSignature": string,
      "usb": string,
      "childHash": string,
      "sourceHostName": string,
      "sourceAddress": string,
      "destinationHostName": string,
      "destinationAddress": string,
      "destinationUserName": string,
      "sourceUserName": string,
      "sourceUserId": string,
      "destinationProcessName": string,
      "sourceDomain": string,
      "destinationDomain": string,
      "fields": {
        string: value,
        ...
      },
      "isCorrelation": boolean
    }  
  
Fields  
---  
`environment` |  `string` Required. Environment is the event environment.  
`sourceSystemName` |  `string` Optional. SourceSystemName is the name of the source system.  
`extensions[]` |  `object (`[LegacyCasePropertyValue](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/LegacyCaseInfo#LegacyCasePropertyValue)`)` Optional. Extensions is a list of key-value pairs for event extensions.  
`parentEventId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. ParentEventId is the ID of the parent event.  
`sourceMacAddress` |  `string` Optional. SourceMacAddress is the source MAC address.  
`destinationMacAddress` |  `string` Optional. DestinationMacAddress is the destination MAC address.  
`name` |  `string` Optional. Name is the name of the event.  
`message` |  `string` Optional. Message is the event message.  
`type` |  `string` Optional. Type is the event type.  
`severity` |  `string` Optional. Severity is the event severity.  
`eventId` |  `string` Optional. EventId is the event identifier.  
`managerReceiptTime` |  `string` Optional. ManagerReceiptTime is the manager receipt time.  
`startTime` |  `string` Optional. StartTime is the event start time.  
`ruleGenerator` |  `string` Optional. RuleGenerator is the rule that generated the event.  
`endTime` |  `string` Optional. EndTime is the event end time.  
`deviceHostName` |  `string` Optional. DeviceHostName is the device host name.  
`deviceAddress` |  `string` Optional. DeviceAddress is the device address.  
`destinationDnsDomain` |  `string` Optional. DestinationDnsDomain is the destination DNS domain.  
`destinationNtDomain` |  `string` Optional. DestinationNtDomain is the destination NT domain.  
`sourceDnsDomain` |  `string` Optional. SourceDnsDomain is the source DNS domain.  
`sourceNtDomain` |  `string` Optional. SourceNtDomain is the source NT domain.  
`deviceEventClassId` |  `string` Optional. DeviceEventClassId is the device event class ID.  
`transportProtocol` |  `string` Optional. TransportProtocol is the transport protocol.  
`applicationProtocol` |  `string` Optional. ApplicationProtocol is the application protocol.  
`destinationPort` |  `string` Optional. DestinationPort is the destination port.  
`categoryOutcome` |  `string` Optional. CategoryOutcome is the category outcome.  
`deviceEventCategory` |  `string` Optional. DeviceEventCategory is the device event category.  
`deviceVendor` |  `string` Optional. DeviceVendor is the device vendor.  
`deviceProduct` |  `string` Optional. DeviceProduct is the device product.  
`deviceSeverity` |  `string` Optional. DeviceSeverity is the device severity.  
`fileType` |  `string` Optional. FileType is the file type.  
`baseEventIds[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. BaseEventIds is a list of base event IDs.  
`cefVersion` |  `string` Optional. CefVersion is the CEF version.  
`deviceVersion` |  `string` Optional. DeviceVersion is the device version.  
`signatureId` |  `string` Optional. SignatureId is the signature ID.  
`description` |  `string` Optional. Description is the event description.  
`receiptTime` |  `string` Optional. ReceiptTime is the receipt time.  
`rawDataFields` |  `map (key: string, value: string)` Optional. RawDataFields is a map of raw data fields.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`destinationUrl` |  `string` Optional. DestinationURL is the destination URL.  
`creditCard` |  `string` Optional. CreditCard is the credit card information.  
`phoneNumber` |  `string` Optional. PhoneNumber is the phone number.  
`cve` |  `string` Optional. CVE is the CVE identifier.  
`threatActor` |  `string` Optional. ThreatActor is the threat actor.  
`threatCampaign` |  `string` Optional. ThreatCampaign is the threat campaign.  
`process` |  `string` Optional. Process is the process name.  
`parentProcess` |  `string` Optional. ParentProcess is the parent process name.  
`parentHash` |  `string` Optional. ParentHash is the parent hash.  
`childProcess` |  `string` Optional. ChildProcess is the child process name.  
`ipset` |  `string` Optional. IPSET is the IP set.  
`cluster` |  `string` Optional. Cluster is the cluster name.  
`application` |  `string` Optional. Application is the application name.  
`database` |  `string` Optional. Database is the database name.  
`pod` |  `string` Optional. Pod is the pod name.  
`container` |  `string` Optional. Container is the container name.  
`service` |  `string` Optional. Service is the service name.  
`genericEntity` |  `string` Optional. GenericEntity is a generic entity.  
`sourceProcessName` |  `string` Optional. SourceProcessName is the source process name.  
`fileName` |  `string` Optional. FileName is the file name.  
`fileHash` |  `string` Optional. FileHash is the file hash.  
`deployment` |  `string` Optional. Deployment is the deployment name.  
`emailSubject` |  `string` Optional. EmailSubject is the email subject.  
`threatSignature` |  `string` Optional. ThreatSignature is the threat signature.  
`usb` |  `string` Optional. USB is the USB information.  
`childHash` |  `string` Optional. ChildHash is the child hash.  
`sourceHostName` |  `string` Optional. SourceHostName is the source host name.  
`sourceAddress` |  `string` Optional. SourceAddress is the source address.  
`destinationHostName` |  `string` Optional. DestinationHostName is the destination host name.  
`destinationAddress` |  `string` Optional. DestinationAddress is the destination address.  
`destinationUserName` |  `string` Optional. DestinationUserName is the destination user name.  
`sourceUserName` |  `string` Optional. SourceUserName is the source user name.  
`sourceUserId` |  `string` Optional. SourceUserID is the source user ID.  
`destinationProcessName` |  `string` Optional. DestinationProcessName is the destination process name.  
`sourceDomain` |  `string` Optional. SourceDomain is the source domain.  
`destinationDomain` |  `string` Optional. DestinationDomain is the destination domain.  
`fields` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Optional. Fields is a map of fields.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`isCorrelation` |  `boolean` Optional. IsCorrelation indicates if the event is a correlation.  
  
## LegacyCasePropertyValue

PropertyValue represents a key-value pair.

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` Required. Key is the property key.  
`value` |  `string` Required. Value is the property value.  
  
## CaseType

LINT.IfChange(CaseType) CaseType represents the type of a case.

Enums  
---  
`EXTERNAL` | External case type.  
`TEST` | Test case type.  
`REQUEST` | Request case type.  
  
## CasePriority

CasePriority represents the priority of a case. LINT.IfChange(CasePriority)

Enums  
---  
`UNCHANGED` | Unchanged case priority.  
`LOW` | Low case priority.  
`MEDIUM` | Medium case priority.  
`HIGH` | High case priority.  
`CRITICAL` | Critical case priority.  
`INFORMATIVE` | Informative case priority.  
  
## LegacyCaseInfoAttachment

CaseInfoAttachment represents the case attachment model.

JSON representation  
---  
      
    
    {
      "base64Blob": string,
      "type": string,
      "name": string,
      "description": string,
      "isImportant": boolean
    }  
  
Fields  
---  
`base64Blob` |  `string` Required. Base64Blob is the base64 representation of the attachment.  
`type` |  `string` Optional. Type is the type of the attachment.  
`name` |  `string` Optional. Name is the name of the attachment.  
`description` |  `string` Optional. Description is the description of the attachment.  
`isImportant` |  `boolean` Optional. IsImportant indicates if the attachment is important.  
  
## LoadDataTypeEnumQueue

LoadDataTypeEnumQueue represents the type of data to load.

Enums  
---  
`EVENTS` | Events data type.  
`CASES` | Cases data type.  
`CONNECTOR_LOG` | Connector log data type.  
`CONNECTOR_OVERFLOW` | Connector overflow data type.  
  
## IngestionSourceType

IngestionSourceType represents the source type of an ingestion.

Enums  
---  
`CONNECTOR` | Connector ingestion source type.  
`WEBHOOK` | Webhook ingestion source type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-10 UTC."],[],[]] 
