---
url: https://docs.cloud.google.com/migration-center/docs/migration-risks/
title: Evaluate and mitigate migration risks \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:43.154695+00:00
---

# Evaluate and mitigate migration risks  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/migration-risks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Evaluate and mitigate migration risks Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to handle migration risks by creating a migration risk assessment.

## Migration risk assessment

In large transformation programs, organizations confront a number of factors that might pose varying degrees of risks during and after the cloud migration. It is therefore essential that you continuously collect data to identify these risks, and undertake mitigation. This creates the need for a migration risk assessment workstream as a part of your program governance for cloud transformation.

Usually, initial high-level discovery and assessment efforts produce directional recommendations on migration strategy and planning. As soon as you start your migration wave planning, it is critical that you run the discovery and assessment effort continuously. Continuous discovery produces additional workload-specific data points and allows you to refine the scope and priorities of the migration waves.

## Typical migration risks

The following table presents typically encountered migration risks, and how their mitigation helps refine the migration wave planning.

**Risks** | **Description** | **Possible mitigation strategies**  
---|---|---  
**Technical blockers** | Factors that prevent the migration of specific workloads. For example, stored procedures can block database migration to PaaS. | Incorporate a blocker mitigation workstream to eliminate blockers before the migration.  
  
Alternatively, move the migration plan for these workloads to later waves.  
**Regulatory requirements and constraints** | Requirements for data protection and privacy, including data localization. | Refine the foundational architecture to incorporate improvements, such as restricted landing zones and regional replication strategies.   
  
Use separate migration waves for workloads with regulatory constraints and non regulated workloads.  
**Performance and availability requirements** | Typically, applications with a high degree of mission criticality and a geographically widespread user base have stringent requirements for response time and maximum acceptable latency. | Before you start the migration wave, validate right-sizing for performance and availability.  
**Interconnect between migrated and non-migrated workloads** | Upstream and downstream connectivity between migrated and non-migrated workloads can impact SLAs and BLAs. | Optimize the sizing of interconnect, and readjust the migration waves.  
**Security requirements** | Security requirements for specific workloads, such as data, application, and network. | Continuously refine the foundational architecture to address security needs. This might also require you to adjust the migration waves.  
  
## What's next

  * Learn how to [plan your migration waves](https://docs.cloud.google.com/migration-center/docs/plan-migration-waves).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
