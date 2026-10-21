---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-asset-changelog/
title: Change log for TANIUM_ASSET \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:49:17.174747+00:00
---

# Change log for TANIUM_ASSET  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-asset-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TANIUM_ASSET

Date | Changes  
---|---  
2025-01-08 |  Enhancement:  
\- Added an on error for `computer_id` and `prod_id` to avoid parsing errors.  
\- Added an on conditional check before mapping `comp_serial_num` to `_asset_entity.asset.product_object_id`.  
\- Mapped `comp_serial_num` to `_asset_entity.asset.product_object_id`.   
2024-02-27 |  Enhancement:  
\- Added a `gsub` function to maintain the JSON format.  
\- Mapped `application_name`, `count`, `application_vendor`, `BIOS_Release_Date`, `BIOS_Vendor`, and `BIOS_Current_Language` to `metadata.source_labels`.  
\- Mapped `application_version` and `BIOS_Version` to `metadata.product_version`.  
\- Mapped `os` to `entity.asset.platform_software.platform`.  
\- Mapped `computer_id` to `entity.asset.asset_id`.  
\- Mapped `serial` to `hardware.serial_number`.  
\- Mapped `comp_serial_num` to `hardware.serial_number`.  
\- Mapped `manufacturer` to `hardware.manufacturer`.   
2022-09-26 |  Bug-fix - Removed the gsub to correctly fetch the value of `Last Logged In User` mapped to `event.idm.entity.entity.relations.user.userid`.  
Enhancement - Added support for new SYSLOG+KV log format.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
