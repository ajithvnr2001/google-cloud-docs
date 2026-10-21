---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-compute-context-changelog/
title: Change log for GCP_COMPUTE_CONTEXT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:55:04.285748+00:00
---

# Change log for GCP_COMPUTE_CONTEXT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-compute-context-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_COMPUTE_CONTEXT

Date | Changes  
---|---  
2026-05-21 |  Enhancement:  
\- `event.idm.entity.entity.asset.attribute.labels`: Newly mapped `networkInterface.networkIP` with key as `networkInterface.name - ip` raw log fields with `event.idm.entity.entity.asset.attribute.labels` UDM field.   
2026-04-28 |  Enhancement:  
\- `event.idm.entity.entity.asset.attribute.labels`: Newly mapped `fingerprint`, `name`, `network`, `subnetwork`, `stackType`, `name`, `natIP`, `networkTier`, and `type` from the raw log fields with `event.idm.entity.entity.asset.attribute.labels` UDM field.   
2024-01-27 |  Bug-Fix:  
\- Segregated the mappings of `name`, `resource.data.id`, `resource.data.name`, `region`, `resource.data.selfLink`, `project_id`, `asset_network_id` and `{region}-%{zone_suffix}` into separate mutate blocks.   
2024-01-05 |  Enhancement:  
\- Removed the mapping of `event.idm.entity.entity.namespace`.  
\- Added support to parse all the `networkIP` from `resource.data.networkInterfaces`.   
2022-07-29 |  \- Added conditional check for `resource.data.lastStartTimestamp` and mapped to `entity.asset.last_boot_time`.  
\- Added conditional check for `resource.data.networkInterfaces.0.networkIP` and mapped to `entity.asset.ip`.   
2022-04-04 |  Updating vendor name   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
