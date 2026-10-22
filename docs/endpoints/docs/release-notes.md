---
url: https://docs.cloud.google.com/endpoints/docs/release-notes/
title: Cloud Endpoints release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:09.635768+00:00
---

# Cloud Endpoints release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Resources ](https://docs.cloud.google.com/endpoints/docs/release-notes)



Send feedback 

#  Cloud Endpoints release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud Endpoints in 2023 and later. We recommend that users periodically check this list for any new announcements, or subscribe to this page using a feed reader to get notifications of updates. 

See also:

  * [2022 and prior Release notes](https://docs.cloud.google.com/endpoints/docs/endpoints-release-notes)
  * [Known issues](https://docs.cloud.google.com/endpoints/docs/known-issues)

rss_feed Subscribe: 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/endpoints-release-notes.xml) directly. 

## November 12, 2025

Feature

**Cloud Endpoints now supports OpenAPI version 3.0.**

With this release, Cloud Endpoints now supports OpenAPI version 3.0, including all patch versions (3.0.x).

Key Benefits:

  * Simplified Deployment: Directly upload and deploy OpenAPI version 3.0.x specifications without prior conversion to 2.0.
  * Enhanced Compatibility: Seamlessly integrate your OpenAPI version 3.0.x definitions with Cloud Endpoints.



For more detail, see [OpenAPI overview](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-overview).

## February 21, 2025

Announcement

**Version 1.0.17 of the[endpoints-management-java Java library](https://github.com/cloudendpoints/endpoints-management-java/releases/tag/v1.0.17) is available.**

This release contains no change in binaries.

Fixed

Bug ID | Description  
---|---  
**387351751** | **Fixed`Checkstyle` violations in the `ServiceConfigSupplierTest` the of source code.**  
  
## December 19, 2024

Announcement

**Version 1.0.15 of the[endpoints-management-java Java library](https://github.com/cloudendpoints/endpoints-management-java/releases/tag/v1.0.15) is available.**

This release fixes an issue where new fields in the [Google Service Configuration](https://docs.cloud.google.com/service-infrastructure/docs/glossary#config) causes the Endpoints Frameworks Java library to fail when parsing the service configuration. Errors similar the following will appear when using _new_ service configurations created after December 5th, 2024:
    
    
    ServiceConfigException: Failed to parse the HTTP response as service configuration
    

We recommend that you upgrade to the `1.0.15` version to avoid these errors. This includes updating any references to the following dependencies:

  * `com.google.endpoints:endpoints-management-control-appengine-all`
  * `com.google.endpoints:endpoints-management-control-appengine`
  * `com.google.endpoints:endpoints-framework-auth`
  * `com.google.endpoints:endpoints-management-config`
  * `com.google.endpoints:endpoints-management-api-client`
  * `com.google.endpoints:endpoints-management-control`
  * `com.google.endpoints:endpoints-management-control-all`



When possible, we recommend that you use the `endpoints-management-control-appengine-all` version of the library to ensure that all dependencies are properly included. However, if you have a specific dependency on `endpoints-management-control-appengine` and cannot use the `endpoints-management-control-appengine-all` version, or you are upgrading from version `1.0.11` or older, you must add the following additional dependencies to your project:

  * `com.google.apis:google-api-services-servicemanagement` version `v1-rev14-1.22.0`
  * `com.google.protobuf:protobuf-java-util` version `3.9.1`



## March 21, 2023

Deprecated

As of March 21, 2023, the Cloud Endpoints Portal is no longer available. API traffic managed by Cloud Endpoints is not affected by this change. For more information, see [Cloud Endpoints Portal deprecation](https://docs.cloud.google.com/endpoints/docs/deprecations/endpoints-portal-deprecation).

## March 15, 2023

Announcement

The shutdown of the Cloud Endpoints Portal is approaching. On or after March 21, 2023, the Cloud Endpoints Portal will no longer be available. API traffic managed by Cloud Endpoints is not affected by this change. For more information, see [Cloud Endpoints Portal deprecation](https://docs.cloud.google.com/endpoints/docs/deprecations/endpoints-portal-deprecation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
