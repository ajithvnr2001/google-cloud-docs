---
url: https://docs.cloud.google.com/spectrum-access-system/docs/release-notes/
title: Spectrum Access System release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:49:10.850892+00:00
---

# Spectrum Access System release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Resources ](https://docs.cloud.google.com/spectrum-access-system/docs/resources)



Send feedback 

#  Spectrum Access System release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to Spectrum Access System. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/spectrum-access-system-release-notes.xml) directly. 

## January 09, 2023

Announcement

Google SAS no longer enforces Part 90 of the Grandfathered Wireless Protection Zone (GWPZ) regulations. This change opens more spectrum for [CBRS](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbrs) usage in the 3650-3700 MHz range, particularly in Texas and Louisiana.

  * CBSDs that were located within GWPZs can now use the upper 50 MHz of the range.
  * CBSDs within 40km of GWPZs now have [EIRP](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#eirp) restrictions removed when requesting grants (if no other incumbent limitations are present).



In order to take advantage of the potentially higher EIRP, CBSDs must perform a [spectrum Inquiry](https://docs.cloud.google.com/spectrum-access-system/docs/overview#cbrs-spec-avail) to check available EIRP or otherwise request new grants. For more information on how to perform a Spectrum Inquiry, see [Best Practices](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/operator-tips). This feature is Generally Available (GA).

## November 10, 2022

Feature

The [CBSDs](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsd) can now operate in the 3650–3700 MHz portion of the [CBRS](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbrs) band in the 150 km area around fixed-satellite service (FSS) receive-only earth stations. The 150 km area around each FSS for 3650-3700 MHz that was considered an exclusion zone is now a protection zone. For more information on how to access the CBRS heatmaps, see [CBRS heatmaps](https://docs.cloud.google.com/spectrum-access-system/docs/cbrs-availability#cbrs-heatmaps).

This feature is Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)).

## April 07, 2022

Feature

You can now [analyze the state of your network](https://docs.cloud.google.com/spectrum-access-system/docs/portal#analyze-status) and apply filters to show only the devices that you want. You can also register and operate devices in the [National Radio Quiet Zone (NRQZ)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#nrqz) through the SAS Portal. For more information, see [Operate CBSDs in the NRQZ](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#cbsd-nrqz).

This feature is Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)).

## March 23, 2022

Feature

The advanced [CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsd) search is Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)). This is available in both Map and Table view. For more information, see [Review CBSD configurations](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/review-configuration).

## January 13, 2022

Feature

The new map control in the SAS Portal is Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)). You can now rotate and tilt maps in the SAS Portal.

## June 09, 2021

Feature

You can now create deployments within your organizations. For more information, see [Manage CBSD configuration](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/manage-configurations).

This feature is Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)).

## May 06, 2021

Change

The deregistration of a device directly from the CBSD configuration and viewing the CBSD history in the SAS Portal is Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Deregister a CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/manage-configurations#cbsd-deregister).

## April 12, 2021

Feature

You can now find PAL Protected Areas (PPA)s and Priority Access License (PAL)s in the SAS Portal. For more information, see [Use PALs in the SAS Portal](https://docs.cloud.google.com/spectrum-access-system/docs/use-pals). 

This feature is Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)).

## March 04, 2021

Feature

You can now move a device to a new location or separate a single device from a multi-sector site. The Customer Premise Equipment (CPE)s and base stations are now highlighted in the map view to help you easily find all CBSDs in the same sector and optimize base stations and CPE connectivity. For more information, see [Channels for a CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/channels).

This feature is Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)).

## February 10, 2021

Change

The [channel planning](https://docs.cloud.google.com/spectrum-access-system/docs/channel-plan), new Dynamic Protection Area (DPA) neighborhood overlays, and [locked user management settings](https://docs.cloud.google.com/spectrum-access-system/docs/users-sasportal) are now improved. For more information, see [CBRS spectrum availability](https://docs.cloud.google.com/spectrum-access-system/docs/cbrs-availability).

## November 04, 2020

Feature

You can now update a field in a current [CBSD configuration](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsdconfig) or sign CBSDs in bulk. This feature is Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Import CBSD configurations](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/manage-configurations#import).

## October 14, 2020

Announcement

All Admins now receive an email when a [CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsd) grant is suspended. Also you will get notified by an email when you're added to the SAS Portal or if you change roles. For more information, see [Review your CBSD configurations in the SAS Portal](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/review-configuration).

## June 02, 2020

Feature

You can now find available spectrum for your deployments in the new [SAS Portal](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#sas-portal). This feature is Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [CBRS spectrum availability](https://docs.cloud.google.com/spectrum-access-system/docs/cbrs-availability) and [Troubleshoot grants in the SAS Portal](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting#grant-issue).

## May 06, 2020

Change

The heartbeat interval is changed from 200 seconds to 60 seconds. [SAS](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#sas) now processes single batch requests with up to 120 CBSDs. For more information, see [Resend (106) response code](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/errors-grant-suspension#106-response-code).

## April 10, 2020

Announcement

Starting April 20, 2020, the `userId` field in the **[DeviceConfig](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.devices#deviceconfig)** is required when you call a SAS Portal API method. This change doesn't affect your existing [CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsd) configurations in the SAS Portal.

## March 25, 2020

Feature

The high-resolution [CBRS](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbrs) heatmaps and importing [CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsd) configurations are Generally Available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [CBRS spectrum availability](https://docs.cloud.google.com/spectrum-access-system/docs/cbrs-availability) and [Import CBSD configurations](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/manage-configurations#import).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
