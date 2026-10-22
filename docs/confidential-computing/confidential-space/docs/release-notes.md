---
url: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/release-notes/
title: Confidential Space release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:28:03.882529+00:00
---

# Confidential Space release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Confidential Space ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs)
  * [ Resources ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/get-support)



Send feedback 

#  Confidential Space release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Confidential Space. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/confidential-space-release-notes.xml) directly. 

## October 19, 2026

Announcement

A new Confidential Space image (261000) is available.

## October 05, 2026

Announcement

A new Confidential Space image (260900) is available.

## September 15, 2026

Announcement

A new Confidential Space image (260800) is available. Support for Confidential Space on H100 GPU (`a3-highgpu-1g` machine family) with Intel Trust Authority (ITA) attestation is [generally available](https://cloud.google.com/products#product-launch-stages).

## August 10, 2026

Announcement

A new Confidential Space image (260701) is available.

## June 24, 2026

Announcement

Confidential Space image 260600 is available. This image provides support for graceful shutdown of container workloads on power button events.

## May 20, 2026

Announcement

Confidential Space image 260500 is available. This image introduces support for [Intel Trust Authority (ITA)](https://docs.trustauthority.intel.com/main/articles/articles/ita/introduction.html) as an independent attestation verifier service for your workloads. This lets you verify the identity, the hardware state, and the software state of the Confidential Space environment directly using Intel's attestation service.

## May 04, 2026

Issue

When running a Confidential Space workload with an NVIDIA H100 GPU attached, you might see the following error message:
    
    
    failed to get launchspec, make sure you're running inside
    a GCE VM: GPU Driver installation is not supported.
    

This is a known issue with the Confidential Space image. To work around the issue, restart the Confidential VM.

## April 29, 2026

Announcement

A Confidential Space image (260400) is available. Support for Confidential Space on H100 GPU (a3-highgpu-1g machine family) is [generally available](https://cloud.google.com/products#product-launch-stages).

## March 24, 2026

Announcement

A new Confidential Space image (260300) is available.

## February 20, 2026

Announcement

A new Confidential Space image (260200) is available.

## January 20, 2026

Announcement

A new Confidential Space image (260100) is available.

## December 16, 2025

Announcement

A new Confidential Space image (251200) is available.

## October 03, 2025

Announcement

New Confidential Space images (251000 and 251001) are available.

## September 02, 2025

Announcement

A new Confidential Space image (250800) is available.

## March 31, 2025

Feature

Confidential Space now allows adding specific Linux capabilities, including CAP_SYS_ADMIN, and provides a namespaced read or write cgroup.

Feature

Support for Confidential Space on Intel CPUs (C3 machine family) with Intel TDX is now [generally available](https://cloud.google.com/products#product-launch-stages).

Announcement

New Confidential Space images (250300 and 250301) are now available.

## March 28, 2025

Feature

AWS token support for Confidential Space is now [generally available](https://cloud.google.com/products#product-launch-stages).

You can now integrate Confidential Space with AWS resources. For more information, see [Integrate AWS resources](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/connect-external-resources#integrate-aws).

## February 05, 2025

Change

Update go-sev-guest to v.0.12.1.

Announcement

A new Confidential Space image (250101) is now available.

Change

Update the verifier API version to include a new principal tag token type.

## January 14, 2025

Fixed

Added retry logic when pulling the workload image and calling the Confidential Computing API.

Change

Changed the default OOM score for the workload container.

Announcement

A new Confidential Space image (250100) is now available.

Change

Updated default TPM Dictionary Lockout parameters. This change should significantly reduce the chance for users to get into the TPM lockout state.

Feature

Improved the logging and monitoring experience. Added CPU metric monitoring to the image.

## October 21, 2024

Feature

A new Confidential Space image (241000) is now available. This image version adds IPv6 ingress traffic support.

The following Confidential Space images were also previously released:

  * September 2, 2024 (240900): 
    * Added `tmpfs` mount support for Confidential Space workloads
    * Added configurable `/dev/shm` size for Confidential Space workloads
    * Added retry capability to the container signature fetch.
    * Minor bug fixes.
  * August 5, 2024 (240800): 
    * Moved to COS-113 as the base image.
    * Patched OpenSSH vulnerability CVE-2024-6387 in the debug image.



## July 01, 2024

Feature

A new Confidential Space image (240700) is now available. This image provides the following fixes:

  * Fixed a bug that caused attestation token refreshing to fail.



## May 30, 2024

Feature

A new Confidential Space image (240500) is now available. This image provides the following fixes:

  * Fixed an issue where default service account credentials would expire after 1 hour, causing `Failed to fetch signatures from the target repo` errors.
  * Fixed a concurrent TPM access issue.



## May 01, 2024

Feature

A new Confidential Space image (240402) is now available. This image provides support for automatically resizing the boot disk stateful partition. See [disk and memory limits](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads#disk-memory-limits) for more information.

## February 28, 2024

Feature

Data collaborators can now [check if memory monitoring is enabled](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/reference/attestation-assertions?tab=vm-assertions#instance_memory_monitoring_enabled) on a Confidential VM running a Confidential Space workload.

Announcement

A new Confidential Space image (240200) is now available. This image provides support for data collaborators to add memory monitoring as part of their attestation assertions.

## December 18, 2023

Feature

A workload operator can now [enable memory monitoring](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/deploy-workloads#tee-monitoring-memory-enable) on the Confidential VM running the workload. This must be [permitted by the workload author](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads#monitoring-memory-allow).

Announcement

A new Confidential Space image (231201) is now available. This image provides support for Confidential VM memory monitoring.

## December 05, 2023

Announcement

A new Confidential Space image (231200) is now available. This image provides support for [custom attestation tokens](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/connect-external-resources).

Feature

You can now use [custom attestation tokens](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/connect-external-resources) to authenticate a workload to relying parties outside of Google Cloud. External relying parties can use authentication to help establish trust and exchange sensitive data securely.

## November 22, 2023

Feature

You can now [use the Split-Trust Encryption Tool (STET) with Confidential Space](https://docs.cloud.google.com/confidential-computing/docs/split-trust-encryption-tool).

## November 20, 2023

Announcement

Support for VPC Service Controls is released to [General Availability](https://cloud.google.com/products#product-launch-stages).

You can now protect Confidential Space using VPC Service Controls perimeters. For more information, see [VPC Service Controls supported products](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_confidential_space).

## November 08, 2023

Feature

Support for VPC Service Controls is released to [Preview](https://cloud.google.com/products#product-launch-stages).

You can now protect Confidential Space using VPC Service Controls perimeters. For more information, see [VPC Service Controls supported products](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_confidential_space).

## November 03, 2023

Change

A new Confidential Space image (231001) is now available. This image provides support for signing container images.

## October 04, 2023

Announcement

A new Confidential Space image (230901) is now available. This image provides improved logging capabilities and increases the file descriptor limits.

## June 30, 2023

Announcement

A new Confidential Space image (230600) is now available. This image provides support for opening ports for inbound network traffic to your workload.

## June 09, 2023

Feature

[Ports can now be opened](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads#inbound-ports) for ingress network traffic when using Confidential Space image version 230600 and above.

## March 28, 2023

Announcement

[Confidential Space](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview) is now **generally available**.

Confidential Space is designed to let parties share sensitive data with a mutually agreed upon workload, while they retain confidentiality and ownership of that data. Such data might include personally identifiable information (PII), protected health information (PHI), intellectual property, cryptographic secrets, and more. Confidential Space helps create isolation so that data is only visible to the workload and the original owners of the data.

## March 27, 2023

Feature

The `assertion.submods.confidential_space.support_attributes` assertion can be used to verify the support status of the Confidential Space image being used. It can be used, for example, to ensure that the workload is running on the latest version of the Confidential Space image.

Change

The `assertion.swversion` [attestation assertion](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/reference/attestation-assertions?tab=image-assertions#swversion) now verifies the Confidential Space image version number the workload is being run on, with the result returned as a list. Previously the assertion was used to determine whether the workload was running on a production or debug Confidential Space image, and the result was returned as an integer. You now determine if a production or debug image is being used with the `assertion.dbgstat` assertion.

## February 28, 2023

Announcement

A new Confidential Space image (2302-0) is now available. This image provides support for the following features and fixes:

  * Attestation is now run in the same location as your workload.
  * The launcher and workload return codes are now recorded in logs.
  * A bug that prevented Docker from pulling images has been fixed.



## February 27, 2023

Breaking

The service account attached to a Confidential Space workload VM now requires the `confidentialcomputing.workloadUser` role to generate an attestation token. If you receive a permission denied message for `confidentialcomputing.locations.list` on your existing workload, add the role to the VM service account.

## December 02, 2022

Feature

**Preview** : [Confidential Space](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview) is designed to let parties share sensitive data with a mutually agreed upon workload, while they retain confidentiality and ownership of that data. Such data might include personally identifiable information (PII), protected health information (PHI), intellectual property, cryptographic secrets, and more. Confidential Space helps create isolation so that data is only visible to the workload and the original owners of the data.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
