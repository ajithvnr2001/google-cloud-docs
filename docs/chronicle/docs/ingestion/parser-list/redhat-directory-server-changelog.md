---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/redhat-directory-server-changelog/
title: Change log for REDHAT_DIRECTORY_SERVER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:11:22.808860+00:00
---

# Change log for REDHAT_DIRECTORY_SERVER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/redhat-directory-server-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for REDHAT_DIRECTORY_SERVER

Date | Changes  
---|---  
2026-05-04 |  Enhancement  
\- `event.idm.read_only_udm.about.labels`: Removed mapping of `properties._file_inode`, `properties._file_offset`, `conn`, `op`, `err`, `tag`, `nentries`, `wtime`, `optime`, `etime`, `csn`, `cn`, `ou`, `filter`, `attrs`, `scope`, `o`, `targetop`, `msgid`, `method`, `version`, `fd`, `slot`, `name` raw log fields from `event.idm.read_only_udm.about.labels` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `properties._file_inode`, `properties._file_offset`, `conn`, `op`, `err`, `tag`, `nentries`, `wtime`, `optime`, `etime`, `csn`, `cn`, `ou`, `filter`, `attrs`, `scope`, `o`, `targetop`, `msgid`, `method`, `version`, `fd`, `slot`, `name` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field  
\- `event.idm.read_only_udm.metadata.event_type`: Updated `event.idm.read_only_udm.metadata.event_type` UDM field to `USER_UNCATEGORIZED`, `NETWORK_CONNECTION`,`USER_RESOURCE_ACCESS` and `STATUS_UPDATE` based on the necessary data present in the logs.   
2024-10-24 |  Enhancement  
\- Added a Grok pattern to parse new logs.  
\- Mapped `host` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `desc` to `metadata.description`.   
2024-10-07 |  Enhancement  
\- Added a Grok pattern to map `user` field to `principal.user.userid`.   
2024-06-25 |  Enhancement  
\- Mapped `properties.country` to `target.location.country_or_region`  
\- Mapped `properties.discipline` ,`properties.document_type` ,`properties.environment` ,`properties.hostgroup` ,`properties.platform` ,`properties.product` to `target.resource.attribute.labels`  
2022-04-11 |  Enhancement-Added mappings for new fields  
Mapped conn, op, err, tag, nentries, wtime, optime, etime, csn, properties._file_offset,filter,attrs,scope,op,o,targetop,msgid,method,version,fd,slot to about.labels.  
Mapped creationDate and recordDate fields to attribute.creation_time and metadata.collected_timestamp respectively.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
