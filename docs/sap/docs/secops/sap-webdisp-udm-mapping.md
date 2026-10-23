---
url: https://docs.cloud.google.com/sap/docs/secops/sap-webdisp-udm-mapping/
title: SAP Web Dispatcher UDM mapping \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:32.835207+00:00
---

# SAP Web Dispatcher UDM mapping  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/secops/sap-webdisp-udm-mapping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  SAP Web Dispatcher UDM mapping Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The `SAP_WEBDISP` parser logs HTTP and HTTPS traffic passing through the SAP Web Dispatcher, providing visibility into external access to SAP web services and applications.

For information about Google SecOps for SAP, see [Secure SAP applications with Google SecOps](https://docs.cloud.google.com/sap/docs/secops/overview).

## Field mapping reference

The following tables describe the mapping between SAP Web Dispatcher log fields and Google SecOps UDM fields.

### Log format 1

Log field | UDM mapping | Logic  
---|---|---  
`_time` | `event.idm.read_only_udm.metadata.event_timestamp` | Primary Unix timestamp indicating when the event occurred.  
`host` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | Hostname of the system where the SAP Web Dispatcher is running.  
`source` | `event.idm.read_only_udm.target.file.full_path` | The full path of the source log file.  
`clz_dir` | `event.idm.read_only_udm.additional.fields["clz_dir"]` | Directory context for log categorization.  
`clz_subdir` | `event.idm.read_only_udm.additional.fields["clz_subdir"]` | Sub-directory context for log categorization.  
`clzfilename` | `event.idm.read_only_udm.additional.fields["clz_filename"]` | Filename of the log being processed.  
`_raw[thread_id]` | `event.idm.read_only_udm.principal.process.pid` | The process thread ID extracted from the internal _raw message.  
`_raw[log_timestamp]` | `event.idm.read_only_udm.metadata.collected_timestamp` | The SAP-formatted timestamp extracted from the _raw payload.  
  
### Log format 2

Log field | UDM mapping | Logic  
---|---|---  
`_time` | `event.idm.read_only_udm.metadata.event_timestamp` | Primary Unix timestamp indicating when the event occurred.  
`host` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | Hostname of the system where the SAP Web Dispatcher is running.  
`source` | `event.idm.read_only_udm.target.file.full_path` | The full path of the source log file.  
`clz_dir` | `event.idm.read_only_udm.additional.fields["clz_dir"]` | Directory context for log categorization.  
`clz_subdir` | `event.idm.read_only_udm.additional.fields["clz_subdir"]` | Sub-directory context for log categorization.  
`clzfilename` | `event.idm.read_only_udm.additional.fields["clz_filename"]` | Filename of the log being processed.  
`_raw[severity]` | `event.idm.read_only_udm.security_result.severity` | Indicates the severity (e.g., ERROR).  
`_raw[sap_component]` | `event.idm.read_only_udm.target.resource.attribute.labels["sap_component"]` | The SAP component (e.g., ICR) where the error occurred.  
`_raw[system_id]` | `event.idm.read_only_udm.target.resource.attribute.labels["system_id"]` | The SAP System ID (SID) of the target backend.  
`_raw[target_url]` | `event.idm.read_only_udm.target.url` | The URL for which access was requested/denied.  
`_raw[response_code]` | `event.idm.read_only_udm.network.http.response_code` | HTTP Status code returned (e.g., 403).  
`_raw[file]` | `event.idm.read_only_udm.security_result.detection_fields["file"]` | Source code file reporting the error.  
`_raw[line]` | `event.idm.read_only_udm.security_result.detection_fields["line"]` | Line number in the source code file.  
  
### Log format 3

Log field | UDM mapping | Logic  
---|---|---  
`_time` | `event.idm.read_only_udm.metadata.event_timestamp` | Primary Unix timestamp indicating when the event occurred.  
`host` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | Hostname of the system where the SAP Web Dispatcher is running.  
`source` | `event.idm.read_only_udm.target.file.full_path` | The full path of the source log file.  
`clz_dir` | `event.idm.read_only_udm.additional.fields["clz_dir"]` | Directory context for log categorization.  
`clz_subdir` | `event.idm.read_only_udm.additional.fields["clz_subdir"]` | Sub-directory context for log categorization.  
`clzfilename` | `event.idm.read_only_udm.additional.fields["clz_filename"]` | Filename of the log being processed.  
`_raw[msg_start]` | `event.idm.read_only_udm.security_result.detection_fields["msg_start"]` | Descriptive start of the error message.  
`_raw[transaction_id]` | `event.idm.read_only_udm.security_result.detection_fields["transaction_id"]` | The SAP transaction ID (e.g., SICF) related to the event.  
`_raw[sap_code]` | `event.idm.read_only_udm.additional.fields["sap_code"]` | SAP Note or specific SAP internal code.  
`_raw[system_id]` | `event.idm.read_only_udm.target.resource.attribute.labels["system_id"]` | Identifies the ABAP backend system.  
`_raw[target_url]` | `event.idm.read_only_udm.target.url` | The URL being checked in the backend.  
  
### Log format 4

Log field | UDM mapping | Logic  
---|---|---  
`thread_id` | `event.idm.read_only_udm.principal.process.pid` | Thread ID of the SAP ICM process that generated the log entry.  
`message` | `event.idm.read_only_udm.metadata.description` | Contains the raw log message.  
  
### Log format 5

Log field | UDM mapping | Logic  
---|---|---  
`message` | `event.idm.read_only_udm.metadata.description` | Contains the raw log message.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
