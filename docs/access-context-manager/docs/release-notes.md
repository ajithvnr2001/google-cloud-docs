---
url: https://docs.cloud.google.com/access-context-manager/docs/release-notes/
title: Access Context Manager release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:55:18.204451+00:00
---

# Access Context Manager release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/access-context-manager/docs/resources)



Send feedback 

#  Access Context Manager release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Access Context Manager. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/access-context-manager-release-notes.xml) directly. 

## September 21, 2026

Feature

Access Context Manager supports extended session length for Workforce Identity Federation. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages) for Looker (Google Cloud core) customers. For more information, see [Configure extended session length for Workforce Identity Federation](https://docs.cloud.google.com/access-context-manager/docs/extended-session-length-for-workforce-identity-federation).

## June 17, 2026

Feature

The Common Expression Language (CEL) function, `originatesFromProjects()`, can be used in [custom access levels](https://docs.cloud.google.com/access-context-manager/docs/custom-access-level-spec). The feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## March 21, 2025

Feature

Access Context Manager now supports custom organization policies. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). For more information, see [Create custom constraints for Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/custom-constraints).

## October 03, 2024

Feature

**Generally available** : App allowlist support for context-aware access

You can now create an access binding with a map of applications to access levels to apply access levels to specific applications, avoiding unintended effects on other applications. For more information, see [Create an access binding with a map of applications to access levels](https://docs.cloud.google.com/beyondcorp-enterprise/docs/securing-console-and-apis#create_an_access_binding_with_a_map_of_applications_to_access_levels).

## June 28, 2024

Feature

[Generally available](https://cloud.google.com/products/#product-launch-stages): You can now use an internal IP address when specifying an IP address range in basic access levels.

For more information, see [Creating a basic access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level).

## February 17, 2023

Feature

The ability to [add individual VPC networks](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-perimeters-management) to a perimeter is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Previously, all VPC networks in a host project were added to a perimeter. You can now do the following:

  * Add individual VPC networks as members of a perimeter.
  * Create an ingress rule to authorize individual VPC networks to access a perimeter.



## June 30, 2022

Feature

Support to add individual VPC networks to a perimeter is now available in [Preview](https://cloud.google.com/products/#product-launch-stages).

Previously, the entire VPC host project was added to a perimeter. VPC Service Controls now supports the following enhancements:

  * You can now add individual VPC networks as members of a perimeter.
  * You can create an ingress rule to authorize individual VPC networks to access a perimeter.



## March 31, 2022

Feature

General availability of scoped policies for VPC Service Controls.

To delegate administration of VPC Service Controls perimeters and access levels to folder-level and project-level administrators, you can use [scoped policies](https://docs.cloud.google.com/access-context-manager/docs/scoped-policies). You can create access policies that are scoped to specific folders or projects.

## April 22, 2021

Feature

General Availability release of [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) for VPC Service Controls.

## October 22, 2020

Feature

Access levels now support checking the [Storage encryption](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#storage-encryption) (`allowedEncryptionStatuses`), [Require admin approval](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#require-admin-approval) (`requireAdminApproval`) and [Require corp owned device](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#require-corp-owned-device) (`requireCorpOwned`) attributes of requests originating from [mobile devices](https://docs.cloud.google.com/access-context-manager/docs/use-mobile-devices).

## June 30, 2020

Feature

General availability of dry run mode for service perimeters.

This release introduces dry run configurations for your service perimeters, allowing you to test changes to perimeters before enforcing the changes. For more information, read about [dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode).

## June 11, 2020

Feature

General availability of the Access Context Manager Bulk API.

Use the Access Context Manager Bulk API to replace all of your organization's access levels in one operation. For more information, see [Making bulk changes to access levels](https://docs.cloud.google.com/access-context-manager/docs/bulk-operations).

## June 01, 2020

Feature

General availability of custom access levels.

[Custom access levels](https://docs.cloud.google.com/access-context-manager/docs/custom-access-levels) provide a way to use Common Expression Language to craft custom conditions. [Create custom access levels](https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level) using the `gcloud` command line tool, the Access Context Manager API, and in the Google Cloud Console using the Advanced Mode for configuring access levels.

## April 03, 2020

Feature

Beta release of the Access Context Manager Bulk API.

The Access Context Manager Bulk API can be used for operations such as replacing all of your organization's access levels. For more information, see [Making bulk changes to access levels](https://docs.cloud.google.com/access-context-manager/docs/bulk-operations).

## February 25, 2020

Feature

Access Context Manager support for mobile devices has entered Beta. You can now [create access levels that target iOS and Android devices](https://docs.cloud.google.com/access-context-manager/docs/use-mobile-devices).

Currently, the **[OS policy](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#os-policy)** and **[Require screen lock](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#require-screen-lock)** device attributes are supported for use with iOS and Android devices.

To take advantage of the new feature, your organization must use Google Workspace [basic mobile device management](https://support.google.com/a/answer/7400753).

## January 06, 2020

Deprecated

The Access Context Manager v1beta API is being deprecated in July 2020.

## October 07, 2019

Change

Access Context Manager's v1alpha API is re-enabled.

The v1alpha API no longer uses `AccessZone`. `AccessZone` has been replaced with `ServicePerimeter`.

To use the v1alpha API, you must be whitelisted.

## August 05, 2019

Change

Error handling in Access Context Manager API v1alpha: 

  * Attempting to call any v1alpha API method will start returning errors as of 08/12/2019.



Deprecated

Access Context Manager API v1alpha is being deprecated in Q3 2019.

## March 19, 2019

Feature

The following access level attributes are now available:

  * Regions
  * For Device policy: 
    * Require admin approval
    * Require corp owned device
    * Require verified Chrome OS



## March 08, 2019

Feature

General availability of Access Context Manager.

## June 01, 2018

Feature

Access Context Manager Closed Beta launch.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
