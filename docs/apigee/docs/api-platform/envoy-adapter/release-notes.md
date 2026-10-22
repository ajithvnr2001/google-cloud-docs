---
url: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/release-notes/
title: Apigee Adapter for Envoy release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:27.709856+00:00
---

# Apigee Adapter for Envoy release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Apigee Adapter for Envoy release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Apigee Adapter for Envoy in 2022 and later. We recommend that users periodically check this list for any new announcements, or subscribe to this page using a feed reader to get notifications of updates. What is a feed reader?

### What is a feed reader?

Really simple syndication (RSS) feed readers aggregate content from websites that you specify.

Feed reader notifications can be email-, browser-, desktop-, or mobile-based. Some readers are free, or have free versions, and some require a subscription.

A few examples:

  * [Feedly](https://feedly.com)
  * [Feedreader](https://feedreader.com)
  * [Feeder](https://feeder.co/)



More information on RSS:

  * [RSS](https://en.wikipedia.org/wiki/RSS)
  * [ Comparison of feed aggregators](https://en.wikipedia.org/wiki/Comparison_of_feed_aggregators)



Close

See also:

  * [2021 and prior Release notes](https://docs.cloud.google.com/apigee/docs/release/notes/100-envoy-adapter-release-notes)
  * [Known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues)

rss_feed Subscribe: 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/apigee-envoy-adapter-release-notes.xml) directly. 

## July 07, 2023

v2.1.1

Announcement

### v2.1.1

On June 7, 2023, we released version 2.1.1 of Apigee Adapter for Envoy.

v2.1.1

Fixed

An issue was fixed where quotas were being improperly duplicated between operations instead of being shared at the Product level.

## June 05, 2023

v2.1.0

Announcement

### v2.1.0

On June 5, 2023, we released version 2.1.0 of Apigee Adapter for Envoy.

v2.1.0

Fixed

The `application_id` claim was added to the `/verifyApiKey` response.

## March 09, 2023

v2.0.7

Announcement

### v2.0.7

On March 9, 2023, we released version 2.0.7 of Apigee Adapter for Envoy.

**Note:** If you are **upgrading** an existing Apigee Adapter for Envoy, you **must** add the `--force-proxy-install` flag to the provision command. This flag forces the Apigee proxy to be replaced with the latest proxy. See [Apigee hybrid example](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/latest/example-hybrid).

v2.0.7

Fixed

  * An issue was fixed where an invalid api key could create spurious log entries and analytics records.
  * A deprecated version check was removed in a proxy that caused issues in newer versions of Apigee.



v2.0.7

Feature

JWTs can now add a claim named `customattributes` that will pass the value on to the target in a header called `x-apigee-customattributes` (if `append_metadata_headers` is configured to be true).

## October 18, 2022

v2.0.6

Announcement

### v2.0.6

On October 18, 2022, we released version 2.0.6 of Apigee Adapter for Envoy.

v2.0.6

Change

Security release to address a Denial of Service (DoS) vulnerability in a dependency library. See [CVE-2022-28948](https://www.cve.org/CVERecord?id=CVE-2022-28948).

## March 03, 2022

v2.0.5

Announcement

### Envoy adapter v2.0.5

On March 3, 2022 we released a new version of Apigee Adapter for Envoy v2.0.5.

v2.0.5

Security

Security release to address a Denial of Service (DoS) risk in the prometheus library. See [CVE-2022-21698](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21698).

## December 03, 2021

v2.0.4

Announcement

### v2.0.4

On December 3, 2021 we released an updated version of the Apigee Adapter for Envoy v2.0.4 software.

**Note:** If you are upgrading an existing Apigee Adapter for Envoy, you must add the `--force-proxy-install` flag to the provision command. This flag forces the Apigee proxy to be replaced with the latest proxy. See [Apigee hybrid example](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/latest/example-hybrid).

▶ Click to see the list of supported platforms.

We publish binaries for MacOS, Linux, and Windows, and in this version, we support the following platforms:

  * Apigee hybrid version 1.4.x, 1.5.x, 1.6.x
  * Apigee X
  * Apigee Edge for Public Cloud
  * Apigee Edge for Private Cloud
  * Istio versions 1.10, 1.11, 1.12
  * Envoy versions 1.17, 1.18, 1.19, 1.20




v2.0.4

Feature

**The list of supported Envoy and Istio versions for the CLI samples command has been updated.** These versions are now supported for samples:

  * Envoy versions 1.18 to 1.20
  * Istio versions 1.10 to 1.12



v2.0.4

Fixed

Bug ID | Description  
---|---  
**360** | A nil-check was added for the PEM block private key loading to avoid panic.  
**104** | Remote service authorization errors are now logged at the Debug level. An exception to this categorization is made for token fetching errors for API keys. In that case, errors are logged at the Error level so that they are visible even if Debug log level for apigee-remote-service-envoy is disabled. See also [Setting remote service log levels](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/troubleshooting#settingremoteserviceloglevels).  
  
## September 21, 2021

v2.0.3

Fixed

Bug ID | Description  
---|---  
**N/A** | **An analytics logging issue with direct responses was fixed.** The issue only occurred under certain circumstances. For example: a) For requests not requiring authn/z check, no authContext was generated and dynamic metadata was nil causing the access log entry to be ignored. b) The denied response used RPC code instead of HTTP code, causing records to be shown in the Apigee UI as success.  
  
v2.0.3

Announcement

### v2.0.3

On September 21, 2021 we released an updated version of the Apigee Adapter for Envoy v2.0.3 software.

**Note:** If you are upgrading an existing Apigee Adapter for Envoy, you must add the `--force-proxy-install` flag to the provision command. This flag forces the Apigee proxy to be replaced with the latest proxy. See [Apigee hybrid example](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/latest/example-hybrid).

▶ Click to see the list of supported platforms.

We publish binaries for MacOS, Linux, and Windows, and in this version, we support the following platforms:

  * Apigee hybrid version 1.4.x, 1.5.x, 1.6.x
  * Apigee X
  * Apigee Edge for Public Cloud
  * Apigee Edge for Private Cloud
  * Istio versions 1.10, 1.11, 1.12
  * Envoy versions 1.17, 1.18, 1.19




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
