---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/digitalguardian-edr-changelog/
title: Change log for DIGITALGUARDIAN_EDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:07.172041+00:00
---

# Change log for DIGITALGUARDIAN_EDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/digitalguardian-edr-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for DIGITALGUARDIAN_EDR

Date | Changes  
---|---  
2025-11-13 |  Enhancement  
\- event.idm.read_only_udm.target.resource.attribute.labels : Newly mapped `Destination_File_Encryption` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Alert_ID` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Computer_Type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Operation` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `Printer_Jobname` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `Was_Destination_Classified` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.src.resource.attribute.labels: Newly mapped `Was_Source_Classified` raw log field with `event.idm.read_only_udm.src.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.src.resource.attribute.labels: Newly mapped `Source_File_Encryption` raw log field with `event.idm.read_only_udm.src.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.src.resource.attribute.labels: Newly mapped `Source_Device_ID` raw log field with `event.idm.read_only_udm.src.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `Destination_Device_ID` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `Detail_Event_ID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.src.resource.name: Newly mapped `Source_Device_Friendly_Name` raw log field with `event.idm.read_only_udm.src.resource.name` UDM field.  
\- event.idm.read_only_udm.src.resource.resource_subtype: Newly mapped `Source_Device_Product_Name` raw log field with `event.idm.read_only_udm.src.resource.resource_subtype` UDM field.  
\- event.idm.read_only_udm.src.resource.attribute.labels: Newly mapped `Source_Device_Serial_Number` raw log field with `event.idm.read_only_udm.src.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `File_Size_MB` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `Detail_File_Size_MB` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `Event_ID` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Block_Code` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Policy` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Agent_Local_Date` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Agent_Local_Time` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Agent_UTC_Time` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2022-12-07 |  Enhancement  
\- Mapped `Source_File` to `src.file.names`.  
\- Mapped `Source_File_Extension` to `src.file.mime_type`.  
\- Mapped `Destination_File` to `target.file.names`.  
\- Mapped `Destination_File_Extension` to `target.file.mime_type`.  
\- Mapped `Source_Drive_Type` to `security_result.detection_fields`.  
\- Mapped `Destination_Drive_Type` to `security_result.detection_fields`.  
\- Mapped `Application` to `target.application`.  
\- Mapped `Was_Removable` to `security_result.detection_fields`.  
\- Mapped `Was_Source_Removable` to `security_result.detection_fields`.  
\- Mapped `Severity` to `security_result.severity`.  
\- Added conditional null checks for the following udm fields: `metadata.product_version`, `principal.user.userid`, `principal.administrative_domain`, `principal.hostname`, `target.hostname`, `target.url`, `security_result.rule_name`.   
2022-06-28 |  Enhancement  
\- Mapped `Bytes_Written` to `network.sent_bytes`.  
\- Mapped `Product_Version` to `metadata.product_version`.  
\- Mapped `Process_SHA256_Hash` to `target.process.file.sha256`.  
\- Mapped `MD5_Checksum` to `target.process.file.md5`.  
\- Mapped `File_Extension` to `additional.fields`.  
\- Mapped `Protocol` to `network.ip_protocol`.  
\- Mapped `Command_Line1` to `principal.process.command_line`.  
\- Mapped `Network_Direction` to `network.direction`.  
\- Mapped `Local_Port` to `principal.port`.  
\- Mapped `Remote_Port` to `target.port`.  
\- Mapped `IP_Address` to `principal.ip`.  
\- Mapped `Dll_SHA1_Hash` to `target.process.file.sha1`.  
\- Dropped the logs having invalid GROK format or due to kv parsing failure.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
