---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/backups/
title: Backups \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:11:24.777585+00:00
---

# Backups  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Backups Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee is redundant and provides live services within each region as a first layer of redundancy.

Data is backed up once per day at a minimum. Some services and data repositories are backed up multiple times per day.

All data backed up by Google is encrypted using Google-owned and Google-managed encryption keys.

The following table describes the backup for each type of data. 

Data | Backup Notes  
---|---  
Control plane data | 

  * Backed up and replicated across multiple regions, which may include the US.
  * The following data is stored in [Google Cloud Storage](https://docs.cloud.google.com/storage) but there is no separate backup outside of what Storage provides: 
    * API proxies
    * Shared flows
    * Keystores
    * Resource files
Google recommends that you maintain regular backups for control plane data. Backups for API proxies and shared flows can be created by [downloading](https://cloud.google.com/apigee/docs/api-platform/fundamentals/download-api-proxies#download) them, keystores certificates can be retrieved through [Apigee APIs](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keystores.aliases/getCertificate), and resource files can be retrieved using the UI or Apigee API as documented in [Managing resources](https://cloud.google.com/apigee/docs/api-platform/develop/resource-files). 
  * Kept under the same security as our production customer services, with restricted access using tools equal to or identical to those used in securing Apigee Cloud platform.

  
Analytics | 

  * Apigee stores backup data for EU analytics regions in the EU region.
  * Apigee stores backup data for North and South America analytics regions in the US.
  * Apigee stores backup data for the following analytics regions in multi-regional Asia:
    * `asia-east1`
    * `asia-south1`
    * `asia-northeast1`
    * `australia-southeast1`
For more information, see [Google Cloud Regions](https://docs.cloud.google.com/compute/docs/regions-zones).

  
Runtime data | 

  * Apigee stores data in the same region as the runtime instance. For more information, see [Google Cloud Regions](https://docs.cloud.google.com/compute/docs/regions-zones).
  * If you have Apigee provisioned in more than one region, then Apigee stores the backup data in each of those regions.

**Note:** Runtime plane backup is applicable to Apigee organizations only.  
Developer Portal (Integrated Portal only) | 

  * Backed up and replicated across multiple regions.
  * Apigee stores backup data in the US multi-region.

For more information, see [Quick start: Build your portal in real time](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/quick-start).  
  
Google tests the process of restoring from backup data as part of our operational excellence. This testing occurs quarterly and the results are included in the audit reports that we share (such as the SOC).

Google recommends that you have a full software development lifecycle (SDLC) plan for your Apigee projects. In addition to backup and restoration plans, this also includes plans for versioning, change management, and authorization.

**Note** : Apigee does not support restoration of individual organization data caused by accidental deletion by the customer.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
