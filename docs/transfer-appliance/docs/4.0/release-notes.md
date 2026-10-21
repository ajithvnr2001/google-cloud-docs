---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/release-notes/
title: Transfer Appliance version 4.0 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:39:11.158387+00:00
---

# Transfer Appliance version 4.0 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Resources ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/resources)



Send feedback 

#  Transfer Appliance version 4.0 release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Transfer Appliance. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/transferappliance-4.0-release-notes.xml) directly. 

## December 18, 2023

Feature

Transfer Appliance has introduced GA support for the data export appliance in the US. This enables you to place orders for exporting data from your Cloud Storage bucket to the appliance, which will then be shipped to you. See the [documentation](https://cloud.google.com/transfer-appliance/docs/4.0/data-export) for full details.

## October 31, 2023

Feature

Transfer Appliance now has alpha-level support in the gcloud CLI (gcloud alpha transfer appliances) allowing you to view in-progress transfer results, work with draft orders, clone existing orders, and more. See the [reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/transfer/appliances) for full details.

## October 09, 2023

Feature

'ta mount' and 'ta unmount' are command line tools offering the user the ability to mount their own NFS or CIFS shares onto the appliance. 

Learn more about [how to mount to an appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/transfer-data#ta-mount).

## September 27, 2023

Feature

New Appliance setup experience is released. Users can use the Google Cloud console to fully [set up permissions](https://cloud.google.com/transfer-appliance/docs/4.0/procedure-guide#project-setup-and-key-download) for the appliance and [receive the credentials](https://cloud.google.com/transfer-appliance/docs/4.0/procedure-guide#receive-appliance).

## March 08, 2023

Feature

`ta check` is a command line tool to detect and help fix configuration issues with [Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/diagnostics) and [Edge Appliance](https://docs.cloud.google.com/distributed-cloud/edge-appliance/docs/diagnostics).

## November 10, 2022

Feature

Users can now use SMB to transfer data by [enabling SMB file share](https://docs.cloud.google.com/transfer-appliance/docs/4.0/transfer-data#use_smb_to_transfer_data).

## September 14, 2022

Feature

Users can now review data that successfully transferred and failed to transfer in log files that auto-generate after a transfer is completed. Learn more about data verification log files [here](https://docs.cloud.google.com/transfer-appliance/docs/4.0/access-data).

## September 09, 2022

Feature

Remote Wipe is an optional step in the appliance return process that allows customers to erase data on their appliance before returning it to Google. 

Learn more about [how to wipe an appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/return-appliance).

## September 02, 2022

Feature

The lock/unlock feature allows you to securely move an appliance between data centers while ensuring that the data is encrypted and not accessible when the appliance comes in contact with third-party shipping services or people outside of your organization. 

Learn more about the guide [here](https://docs.cloud.google.com/transfer-appliance/docs/4.0/lock-unlock-userguide).

## August 17, 2022

Announcement

Edge Appliance is now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)).

Edge Appliance is a Google Cloud-managed, secure, high-performance appliance for edge locations. It provides local storage, ML inference, data transformation, and export.

[Learn more](https://docs.cloud.google.com/transfer-appliance/docs/edge/overview) or [request Edge Appliance now](https://docs.cloud.google.com/transfer-appliance/docs/edge/request).

## August 12, 2022

Feature

You can now place your Transfer Appliance into suspend mode before moving it to a new location. Suspend mode removes access to data on the device and suspends any transfers.

Learn more from the [Suspend](https://docs.cloud.google.com/transfer-appliance/docs/4.0/shutdown-appliance#suspend) section of the documentation.

## July 12, 2022

Feature

Transfer Appliance is now available in an additional size. The TA7 appliance offers up to 7TB of storage in a smaller form factor than our other appliances. It offers both online and offline transfer modes.

Learn more about the TA7 on the [Specifications](https://docs.cloud.google.com/transfer-appliance/docs/4.0/specifications) page, or [order an appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/order-appliance) from the Cloud console.

## June 29, 2022

Feature

Transfer Appliance now supports monitoring of the amount of data stored on your appliance, and whether online transfer is enabled, through Cloud Monitoring. See [Monitor Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/monitor-appliance) for details.

## June 16, 2022

Feature

You can now order Transfer Appliance from the Cloud console, as well as view, track, and manage your orders and appliances. For more info, see the [Order Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/order-appliance) page.

## June 02, 2021

Feature

Transfer Appliance offers the [Transfer Appliance Cloud Setup Application](https://docs.cloud.google.com/transfer-appliance/docs/4.0/permissions-application). The application prompts for several settings, and uses the information you provide to configure your Google Cloud permissions, preferred Cloud Storage bucket, and Cloud KMS key for your transfer.

## March 30, 2021

Change

Transfer Appliance version 4.0 is now available to order in Singapore.

Change

Transfer Appliance version 2.2 is deprecated and replaced by [Transfer Appliance version 4.0](https://docs.cloud.google.com/transfer-appliance/docs/4.0).

## November 04, 2020

Change

Transfer Appliance version 4.0 is released.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
