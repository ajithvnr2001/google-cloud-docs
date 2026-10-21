---
url: https://docs.cloud.google.com/feeds/confidential-space-release-notes.xml
title: Confidential Space - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:50:30.686490+00:00
---

# Confidential Space - Release notes

> Source: https://docs.cloud.google.com/feeds/confidential-space-release-notes.xml

tag:google.com,2016:confidential-space-release-notesConfidential Space - Release notesGoogle Cloud Platform2026-10-05T00:00:00-07:00October 05, 2026tag:google.com,2016:confidential-space-release-notes#October_05_20262026-10-05T00:00:00-07:00Announcement 

A new Confidential Space image (260900) is available.

]]> September 15, 2026tag:google.com,2016:confidential-space-release-notes#September_15_20262026-09-15T00:00:00-07:00Announcement 

A new Confidential Space image (260800) is available. Support for Confidential Space on H100 GPU (`a3-highgpu-1g` machine family) with Intel Trust Authority (ITA) attestation is [generally available](https://cloud.google.com/products#product-launch-stages).

]]> August 10, 2026tag:google.com,2016:confidential-space-release-notes#August_10_20262026-08-10T00:00:00-07:00Announcement 

A new Confidential Space image (260701) is available.

]]> June 24, 2026tag:google.com,2016:confidential-space-release-notes#June_24_20262026-06-24T00:00:00-07:00Announcement 

Confidential Space image 260600 is available. This image provides support for graceful shutdown of container workloads on power button events.

]]> May 20, 2026tag:google.com,2016:confidential-space-release-notes#May_20_20262026-05-20T00:00:00-07:00Announcement 

Confidential Space image 260500 is available. This image introduces support for [Intel Trust Authority (ITA)](https://docs.trustauthority.intel.com/main/articles/articles/ita/introduction.html) as an independent attestation verifier service for your workloads. This lets you verify the identity, the hardware state, and the software state of the Confidential Space environment directly using Intel's attestation service.

]]> May 04, 2026tag:google.com,2016:confidential-space-release-notes#May_04_20262026-05-04T00:00:00-07:00Issue 

When running a Confidential Space workload with an NVIDIA H100 GPU attached, you might see the following error message:
    
    
    failed to get launchspec, make sure you're running inside
    a GCE VM: GPU Driver installation is not supported.
    

This is a known issue with the Confidential Space image. To work around the issue, restart the Confidential VM.

]]> April 29, 2026tag:google.com,2016:confidential-space-release-notes#April_29_20262026-04-29T00:00:00-07:00Announcement 

A Confidential Space image (260400) is available. Support for Confidential Space on H100 GPU (a3-highgpu-1g machine family) is [generally available](https://cloud.google.com/products#product-launch-stages).

]]> March 24, 2026tag:google.com,2016:confidential-space-release-notes#March_24_20262026-03-24T00:00:00-07:00Announcement 

A new Confidential Space image (260300) is available.

]]> February 20, 2026tag:google.com,2016:confidential-space-release-notes#February_20_20262026-02-20T00:00:00-08:00Announcement 

A new Confidential Space image (260200) is available.

]]> January 20, 2026tag:google.com,2016:confidential-space-release-notes#January_20_20262026-01-20T00:00:00-08:00Announcement 

A new Confidential Space image (260100) is available.

]]> December 16, 2025tag:google.com,2016:confidential-space-release-notes#December_16_20252025-12-16T00:00:00-08:00Announcement 

A new Confidential Space image (251200) is available.

]]> October 03, 2025tag:google.com,2016:confidential-space-release-notes#October_03_20252025-10-03T00:00:00-07:00Announcement 

New Confidential Space images (251000 and 251001) are available.

]]> September 02, 2025tag:google.com,2016:confidential-space-release-notes#September_02_20252025-09-02T00:00:00-07:00Announcement 

A new Confidential Space image (250800) is available.

]]> March 31, 2025tag:google.com,2016:confidential-space-release-notes#March_31_20252025-03-31T00:00:00-07:00Feature 

Confidential Space now allows adding specific Linux capabilities, including CAP_SYS_ADMIN, and provides a namespaced read or write cgroup.

### Feature

Support for Confidential Space on Intel CPUs (C3 machine family) with Intel TDX is now [generally available](https://cloud.google.com/products#product-launch-stages).

### Announcement

New Confidential Space images (250300 and 250301) are now available.

]]> March 28, 2025tag:google.com,2016:confidential-space-release-notes#March_28_20252025-03-28T00:00:00-07:00Feature 

AWS token support for Confidential Space is now [generally available](https://cloud.google.com/products#product-launch-stages).

You can now integrate Confidential Space with AWS resources. For more information, see [Integrate AWS resources](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/connect-external-resources#integrate-aws).

]]> February 05, 2025tag:google.com,2016:confidential-space-release-notes#February_05_20252025-02-05T00:00:00-08:00Change 

Update go-sev-guest to v.0.12.1.

### Announcement

A new Confidential Space image (250101) is now available.

### Change

Update the verifier API version to include a new principal tag token type.

]]> January 14, 2025tag:google.com,2016:confidential-space-release-notes#January_14_20252025-01-14T00:00:00-08:00Fixed 

Added retry logic when pulling the workload image and calling the Confidential Computing API.

### Change

Changed the default OOM score for the workload container.

### Announcement

A new Confidential Space image (250100) is now available.

### Change

Updated default TPM Dictionary Lockout parameters. This change should significantly reduce the chance for users to get into the TPM lockout state.

### Feature

Improved the logging and monitoring experience. Added CPU metric monitoring to the image.

]]> October 21, 2024tag:google.com,2016:confidential-space-release-notes#October_21_20242024-10-21T00:00:00-07:00Feature 

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

]]> July 01, 2024tag:google.com,2016:confidential-space-release-notes#July_01_20242024-07-01T00:00:00-07:00Feature 

A new Confidential Space image (240700) is now available. This image provides the following fixes:

  * Fixed a bug that caused attestation token refreshing to fail.

]]> May 30, 2024tag:google.com,2016:confidential-space-release-notes#May_30_20242024-05-30T00:00:00-07:00Feature 

A new Confidential Space image (240500) is now available. This image provides the following fixes:

  * Fixed an issue where default service account credentials would expire after 1 hour, causing `Failed to fetch signatures from the target repo` errors.
  * Fixed a concurrent TPM access issue.

]]> May 01, 2024tag:google.com,2016:confidential-space-release-notes#May_01_20242024-05-01T00:00:00-07:00Feature 

A new Confidential Space image (240402) is now available. This image provides support for automatically resizing the boot disk stateful partition. See [disk and memory limits](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads#disk-memory-limits) for more information.

]]> February 28, 2024tag:google.com,2016:confidential-space-release-notes#February_28_20242024-02-28T00:00:00-08:00Feature 

Data collaborators can now [check if memory monitoring is enabled](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/reference/attestation-assertions?tab=vm-assertions#instance_memory_monitoring_enabled) on a Confidential VM running a Confidential Space workload.

### Announcement

A new Confidential Space image (240200) is now available. This image provides support for data collaborators to add memory monitoring as part of their attestation assertions.

]]> December 18, 2023tag:google.com,2016:confidential-space-release-notes#December_18_20232023-12-18T00:00:00-08:00Feature 

A workload operator can now [enable memory monitoring](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/deploy-workloads#tee-monitoring-memory-enable) on the Confidential VM running the workload. This must be [permitted by the workload author](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads#monitoring-memory-allow).

### Announcement

A new Confidential Space image (231201) is now available. This image provides support for Confidential VM memory monitoring.

]]> December 05, 2023tag:google.com,2016:confidential-space-release-notes#December_05_20232023-12-05T00:00:00-08:00Announcement 

A new Confidential Space image (231200) is now available. This image provides support for [custom attestation tokens](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/connect-external-resources).

### Feature

You can now use [custom attestation tokens](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/connect-external-resources) to authenticate a workload to relying parties outside of Google Cloud. External relying parties can use authentication to help establish trust and exchange sensitive data securely.

]]> November 22, 2023tag:google.com,2016:confidential-space-release-notes#November_22_20232023-11-22T00:00:00-08:00Feature 

You can now [use the Split-Trust Encryption Tool (STET) with Confidential Space](https://docs.cloud.google.com/confidential-computing/docs/split-trust-encryption-tool).

]]> November 20, 2023tag:google.com,2016:confidential-space-release-notes#November_20_20232023-11-20T00:00:00-08:00Announcement 

Support for VPC Service Controls is released to [General Availability](https://cloud.google.com/products#product-launch-stages).

You can now protect Confidential Space using VPC Service Controls perimeters. For more information, see [VPC Service Controls supported products](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_confidential_space).

]]> November 08, 2023tag:google.com,2016:confidential-space-release-notes#November_08_20232023-11-08T00:00:00-08:00Feature 

Support for VPC Service Controls is released to [Preview](https://cloud.google.com/products#product-launch-stages).

You can now protect Confidential Space using VPC Service Controls perimeters. For more information, see [VPC Service Controls supported products](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_confidential_space).

]]> November 03, 2023tag:google.com,2016:confidential-space-release-notes#November_03_20232023-11-03T00:00:00-07:00Change 

A new Confidential Space image (231001) is now available. This image provides support for signing container images.

]]> October 04, 2023tag:google.com,2016:confidential-space-release-notes#October_04_20232023-10-04T00:00:00-07:00Announcement 

A new Confidential Space image (230901) is now available. This image provides improved logging capabilities and increases the file descriptor limits.

]]> June 30, 2023tag:google.com,2016:confidential-space-release-notes#June_30_20232023-06-30T00:00:00-07:00Announcement 

A new Confidential Space image (230600) is now available. This image provides support for opening ports for inbound network traffic to your workload.

]]>
