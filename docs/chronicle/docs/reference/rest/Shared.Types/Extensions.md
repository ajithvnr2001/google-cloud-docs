---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions/
title: Extensions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:54.846402+00:00
---

# Extensions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  Extensions Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Vulnerabilities
    * JSON representation
  * LinuxUtmp
    * JSON representation
  * WindowsEventLog
    * JSON representation
  * ResourceUsage
    * JSON representation
  * SystemEventDetails
    * JSON representation
  * OutlookMetadata
    * JSON representation
  * Srum
    * JSON representation
  * UserAssist
    * JSON representation



Extensions to a UDM event.

JSON representation  
---  
      
    
    {
      "auth": {
        object ([Authentication](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Authentication))
      },
      "vulns": {
        object ([Vulnerabilities](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#Vulnerabilities))
      },
      "entityRisk": {
        object ([EntityRisk](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/EntityRisk))
      },
      "linuxUtmp": {
        object ([LinuxUtmp](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#LinuxUtmp))
      },
      "windowsEventLog": {
        object ([WindowsEventLog](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#WindowsEventLog))
      },
      "resourceUsage": {
        object ([ResourceUsage](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#ResourceUsage))
      },
      "systemEventDetails": {
        object ([SystemEventDetails](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#SystemEventDetails))
      },
      "outlookMetadata": {
        object ([OutlookMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#OutlookMetadata))
      },
      "srum": {
        object ([Srum](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#Srum))
      },
      "userAssist": {
        object ([UserAssist](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#UserAssist))
      }
    }  
  
Fields  
---  
`auth` |  `object (`[Authentication](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Authentication)`)` An authentication extension.  
`vulns` |  `object (`[Vulnerabilities](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#Vulnerabilities)`)` A vulnerability extension.  
`entityRisk` |  `object (`[EntityRisk](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/EntityRisk)`)` An entity risk change extension.  
`linuxUtmp` |  `object (`[LinuxUtmp](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#LinuxUtmp)`)` A Linux Utmp extension. This captures details specific to Linux Utmp events, which record login and logout sessions on a Linux system.  
`windowsEventLog` |  `object (`[WindowsEventLog](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#WindowsEventLog)`)` A Windows Event Log extension. This captures details specific to Windows Event Log events, providing structured information from various Windows logs.  
`resourceUsage` |  `object (`[ResourceUsage](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#ResourceUsage)`)` A resource usage extension. This captures details about what entity, for example, a process or user, is using a specific resource.  
`systemEventDetails` |  `object (`[SystemEventDetails](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#SystemEventDetails)`)` A system event details extension. This captures additional details for system-level events, such as message type, sender image ID, and subsystem.  
`outlookMetadata` |  `object (`[OutlookMetadata](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#OutlookMetadata)`)` A Microsoft Outlook metadata extension. This includes metadata related to Outlook items, such as comments, templates, and security flags.  
`srum` |  `object (`[Srum](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#Srum)`)` A SRUM extension. This captures details specific to Windows System Resource Usage Monitor (SRUM) events, providing insights into application resource consumption.  
`userAssist` |  `object (`[UserAssist](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Extensions#UserAssist)`)` A UserAssist extension. This captures details specific to Windows User Assist events, which track application usage and execution.  
  
## Vulnerabilities

The Vulnerabilities extension captures details on observed/detected vulnerabilities.

JSON representation  
---  
      
    
    {
      "vulnerabilities": [
        {
          object ([Vulnerability](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Vulnerability))
        }
      ]
    }  
  
Fields  
---  
`vulnerabilities[]` |  `object (`[Vulnerability](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Vulnerability)`)` A list of vulnerabilities.  
  
## LinuxUtmp

The LinuxUtmp extension captures details specific to Linux Utmp events.

JSON representation  
---  
      
    
    {
      "recordType": enum ([RecordType](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/RecordType))
    }  
  
Fields  
---  
`recordType` |  `enum (`[RecordType](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/RecordType)`)` The activity record type.  
  
## WindowsEventLog

The WindowsEventLog extension captures details specific to Windows Event Log events.

JSON representation  
---  
      
    
    {
      "channel": enum ([Channel](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Channel)),
      "eventId": string,
      "activityId": string
    }  
  
Fields  
---  
`channel` |  `enum (`[Channel](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Channel)`)` The channel of the event.  
`eventId` |  `string` A unique identifier for a specific type of event.  
`activityId` |  `string` A GUID (Globally Unique Identifier) used to link a sequence of related events together.  
  
## ResourceUsage

The ResourceUsage extension captures details about what is using a resource.

JSON representation  
---  
      
    
    {
      "usedEntity": string,
      "usedEntityId": string
    }  
  
Fields  
---  
`usedEntity` |  `string` The name of the entity (e.g., process, user) that is using the resource.  
`usedEntityId` |  `string` A numerical identifier for the entity using the resource (e.g., PID, UID).  
  
## SystemEventDetails

Captures additional details for system-level events.

JSON representation  
---  
      
    
    {
      "messageType": string,
      "senderImageId": string,
      "subsystem": string
    }  
  
Fields  
---  
`messageType` |  `string` The specific type or category of the message.  
`senderImageId` |  `string` An identifier for the image associated with the sender of the message.  
`subsystem` |  `string` The subsystem or component that generated the event.  
  
## OutlookMetadata

Microsoft Outlook specific metadata.

JSON representation  
---  
      
    
    {
      "comment": string,
      "template": string,
      "title": string,
      "securityFlagsCount": integer
    }  
  
Fields  
---  
`comment` |  `string` A user-defined comment or note associated with the Outlook item.  
`template` |  `string` The name of the template file used to create the Outlook item.  
`title` |  `string` The title of the Outlook item.  
`securityFlagsCount` |  `integer` Count of Security-related flags for the message, such as encryption or signing status.  
  
## Srum

The Srum extension captures details specific to Windows System Resource Usage Monitor (SRUM) events.

JSON representation  
---  
      
    
    {
      "id": string,
      "backgroundBytesRead": string,
      "backgroundBytesWritten": string,
      "backgroundContextSwitches": string,
      "backgroundCycleCount": string,
      "backgroundFlushesCount": string,
      "backgroundReadOperations": string,
      "backgroundWriteOperations": string,
      "interfaceLuid": string
    }  
  
Fields  
---  
`id` |  `string` A unique identifier for the SRUM record or the application/user being monitored.  
`backgroundBytesRead` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of bytes read by the application while running in the background.  
`backgroundBytesWritten` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of bytes written by the application while running in the background.  
`backgroundContextSwitches` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of context switches performed by the application's threads while in the background.  
`backgroundCycleCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The amount of CPU cycle time consumed by the application in the background, measured in clock cycles.  
`backgroundFlushesCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of flush operations performed by the application in the background.  
`backgroundReadOperations` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of read operations performed by the application in the background.  
`backgroundWriteOperations` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of write operations performed by the application in the background.  
`interfaceLuid` |  `string` The Locally Unique Identifier (LUID) for the network interface used for data transfer.  
  
## UserAssist

The UserAssist extension captures details specific to Windows User Assist events.

JSON representation  
---  
      
    
    {
      "applicationFocusCount": string,
      "applicationFocusDuration": string,
      "executionsCount": string,
      "entryIndex": string
    }  
  
Fields  
---  
`applicationFocusCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of times the application associated with the entry gained focus.  
`applicationFocusDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The total duration the application associated with the entry was in focus.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`executionsCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of times the application associated with the entry has been executed.  
`entryIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The index or identifier of the user assist entry, unique per user.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-13 UTC."],[],[]] 
