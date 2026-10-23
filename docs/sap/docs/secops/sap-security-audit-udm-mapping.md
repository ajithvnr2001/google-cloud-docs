---
url: https://docs.cloud.google.com/sap/docs/secops/sap-security-audit-udm-mapping/
title: SAP Security Audit UDM mapping \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:33.291327+00:00
---

# SAP Security Audit UDM mapping  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/secops/sap-security-audit-udm-mapping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  SAP Security Audit UDM mapping Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The `SAP_SECURITY_AUDIT` parser records security-critical events at the SAP application level, such as user logins, failed logon attempts, transaction executions, and report starts.

For information about Google SecOps for SAP, see [Secure SAP applications with Google SecOps](https://docs.cloud.google.com/sap/docs/secops/overview).

## Field mapping reference

The following table describes the mapping between SAP Security Audit log fields and Google SecOps UDM fields.

Log field | UDM mapping | Logic  
---|---|---  
`sid / SID` | `event.idm.read_only_udm.target.application` | Identifies the specific SAP system.  
`instance / INSTANCE` | `event.idm.read_only_udm.target.resource.name` | Name of the SAP instance process or server.  
`salDate / SAL_DATE` | `event.idm.read_only_udm.metadata.event_timestamp` | Date of the event, combined with time field to create event_timestamp.  
`salTime / SAL_TIME` | `event.idm.read_only_udm.metadata.event_timestamp` | Time of the event, combined with date field to create event_timestamp.  
`slguser / SLGUSER` | `event.idm.read_only_udm.principal.user.userid` | User ID associated with the audit event.  
`useralias / USERALIAS` | `event.idm.read_only_udm.principal.user.userid` | User alias, used as principal user ID if slguser/SLGUSER is not available.  
`class / CLASS` | `event.idm.read_only_udm.principal.user.group_identifiers` | User classification or group (e.g., 'SUPER').  
`txsubclsid / TXSUBCLSID` | `event.idm.read_only_udm.security_result.summary` | Text description of audit event type; 'Dialog logon' indicates a USER_LOGIN event.  
`severityS / SEVERITY_S` | `event.idm.read_only_udm.security_result.severity` | Severity rating character (L, M, H), converted to LOW, MEDIUM, or HIGH in UDM.  
`txseverity / TXSEVERITY` | `event.idm.read_only_udm.security_result.severity_details` | Text description of the event severity (e.g., 'Medium').  
`salData / SAL_DATA` | `event.idm.read_only_udm.metadata.description` | Payload or detailed message of the audit event.  
`taskno / TASKNO` | `event.idm.read_only_udm.principal.process.pid` | Task number or process identifier for the event.  
`slgrepna / SLGREPNA` | `event.idm.read_only_udm.principal.process.file.names` | Name of the SAP program or report that generated the event.  
`epp / EPP` | `event.idm.read_only_udm.principal.user.product_object_id` | Passport ID or unique identifier for the entry point.  
`slgltrm2 / SLGLTRM2` | `event.idm.read_only_udm.principal.ip` or `event.idm.read_only_udm.principal.hostname` | Terminal name or IP address; parsed to differentiate IP from hostname.  
`termIpv6 / TERM_IPV6` | `event.idm.read_only_udm.principal.ip` | IPv6 address if available and different from slgltrm2.  
`subid / SUBID` | `event.idm.read_only_udm.target.resource.attribute.labels` | Sub-identifier within an audit area (e.g., '1' for AU area).  
`counter / COUNTER` | `event.idm.read_only_udm.additional.fields` | Sequence counter for events.  
`slgtc / SLGTC` | `event.idm.read_only_udm.security_result.detection_fields` | SAP transaction code (T-code) executed.  
`subclasid / SUBCLASID` | `event.idm.read_only_udm.security_result.detection_fields` | Numeric identifier for the audit event subclass.  
`severity / SEVERITY` | `event.idm.read_only_udm.additional.fields` | Numeric representation of event severity.  
`msg / MSG` | `event.idm.read_only_udm.additional.fields` | Message identifier (e.g., 'AU1').  
`fileNo / FILE_NO` | `event.idm.read_only_udm.additional.fields` | Associated file number for the audit log.  
`tasktype / TASKTYPE` | `event.idm.read_only_udm.additional.fields` | Type of task that generated the log (e.g., 'Df', 'Da', 'B1').  
`slgdattim / SLGDATTIM` | `event.idm.read_only_udm.additional.fields` | Raw timestamp string from SAP (YYYYMMDDHHMMSS).  
`logTstmp / LOG_TSTMP` | `event.idm.read_only_udm.additional.fields` | High-precision timestamp from the logging system.  
`param1 / PARAM1` | `event.idm.read_only_udm.additional.fields` | Generic parameter 1 associated with the event message.  
`param2 / PARAM2` | `event.idm.read_only_udm.additional.fields` | Generic parameter 2 associated with the event message.  
`param3 / PARAM3` | `event.idm.read_only_udm.additional.fields` | Generic parameter 3 associated with the event message.  
`area / AREA` | `event.idm.read_only_udm.additional.fields` | Functional area of the audit event (e.g., 'AU' for Audit).  
`slgmand / SLGMAND` | `event.idm.read_only_udm.target.resource.attribute.labels` | SAP Client number (Mandant).  
`smtpAddr / SMTP_ADDR` | `event.idm.read_only_udm.additional.fields` | Email address associated with the user.  
`xString / X_STRING` | `event.idm.read_only_udm.additional.fields` | Additional data string, often hexadecimal.  
`paramx / PARAMX` | `event.idm.read_only_udm.additional.fields` | Extended parameter field.  
`src / SRC` | `event.idm.read_only_udm.additional.fields` | Source information field.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
