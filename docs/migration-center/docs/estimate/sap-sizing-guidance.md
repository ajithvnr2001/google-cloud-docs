---
url: https://docs.cloud.google.com/migration-center/docs/estimate/sap-sizing-guidance/
title: Review SAP application sizing guidance \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:04.565124+00:00
---

# Review SAP application sizing guidance  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/estimate/sap-sizing-guidance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Review SAP application sizing guidance Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance on when to select which application size in the SAP calculator depending upon your vCPU and memory requirements.

## Sizing guidance for SAP BO

In case of SAP BusinessObjects (SAP BO), as size increases from Small to X-Large, the number of instances of the machine in use increases instead of the machine size itself.

Use the following sizing guidance to select the SAP BO size that matches your requirements:

**Number of instances** | **Number of vCPUs for App, Production** | **Memory Size for App (GB), Production** | **SAP BO Size**  
---|---|---|---  
1 | 16 | 64 | Small  
2 | 16 | 64 | Medium  
4 | 16 | 64 | Large   
8 | 16 | 64 | X-Large  
  
## Sizing guidance for SAP BODS

Use the following sizing guidance to select the SAP BusinessObjects Data Services (SAP BODS) size that matches your requirements:

**Number of vCPUs for App, Production** | **Memory Size for App (GB), Production** | **BODS Size**  
---|---|---  
8 | 32 | Small  
16 | 64 | Medium  
32 | 128 | Large   
  
## Sizing guidance for SAP BW/4HANA

Use the following sizing guidance to select the SAP BW/4HANA size that matches your requirements:

**Number of vCPUs for DB, Production** | **Memory size for DB (GB), Production** | **BW/4HANA Size**  
---|---|---  
32 | 256 | X-Small  
64 | 512 | Small  
96 | 1433 | Medium  
168 | 3844 | Large   
416 | 5888 | X-Large  
  
## Sizing guidance for SAP Fiori

Use the following sizing guidance to select the SAP Fiori size that matches your requirements:

**Number of vCPUs for App, Production** | **Memory Size for App (GB), Production** | **Fiori Size**  
---|---|---  
8 | 32 | XX-Small  
8 | 32 | X-Small  
8 | 32  | Small  
16 | 64  | Medium  
16 | 64 | Large   
16 | 64 | X-Large   
  
## Sizing guidance for SAP PO

Use the following sizing guidance to select the SAP Process Orchestration (SAP PO) size that matches your requirements:

**Number of vCPUs for DB, Production** | **Memory Size for DB (GB), Production** | **PO Size**  
---|---|---  
4 | 16 | Small  
8 | 32 | Medium  
16 | 64 | Large  
  
## Sizing guidance for SAP S/4HANA

In the SAP calculator, S/4HANA is available in five different sizes. You can choose the size based on either the number of Full User Equivalent (FUE) or memory size. You must select the next tier of the application size if your memory size is higher than the FUE usage tier. 

Use the following sizing guidance to select the SAP S/4HANA size that matches your requirements:

**Usage Tier** | **Memory size for HANA DB (GB), Production and QAS** | **S/4HANA Size**  
---|---|---  
136 to 550 FUE | 256 | X-Small  
551 to 1000 FUE | 512 | Small  
1001 to 2000 FUE | 1024 | Medium  
2001 to 4000 FUE | 2048 | Large   
4001 to 6000 FUE | 3072 | X-Large  
  
## Sizing guidance for SAP NW ABAP

Use the following sizing guidance to select the SAP NetWeaver Application Server for ABAP (SAP NW ABAP) size that matches your requirements:

**Memory size HANA DB (GB), Production** | **NW ABAP Size**  
---|---  
128 | X-Small  
128 | Small  
256 | Medium  
512 | Large  
961 | X-Large  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
