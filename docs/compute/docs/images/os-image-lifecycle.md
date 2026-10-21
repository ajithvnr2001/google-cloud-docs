---
url: https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle/
title: Operating systems lifecycle \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:43.403047+00:00
---

# Operating systems lifecycle  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Operating systems lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes the lifecycle stages of public operating system (OS) images on Compute Engine. Use this information to understand how OS versions transition from general availability (GA) through end of support (EOS) or end of life (EOL) to help you design upgrade plans for your workloads.

The following sections outline the lifecycle stages of an OS version on Compute Engine.

## Mainstream support or general availability (GA)

In this stage the following processes take place:

  1. With the introduction of a new OS version, the OS image provider creates a new OS image and assigns a name by using the naming convention for that OS distribution. For example, `debian-13-trixie-v20260827`.
  2. The image provider then creates a new image family. For example, `debian-13.`

_Image families_ help you manage OS images in your project by grouping related images together, so that you can roll forward and roll back between specific OS image versions. For more information, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

All calls to the image family references this recently created OS image. For example, if you specify an image family during VM creation by using the `--image-family` flag with the appropriate `--image-project`, then the latest version of the image is used.

  3. Occasionally, the image provider applies critical security or bug fixes, that are sent by the OS provider, to the OS image. In these updates, new features might be introduced. When an update is sent, the following takes place:

     * The current OS image is updated and a new name is generated. For example, the `debian-13-trixie-v20260827` with the updates becomes `debian-13-trixie-v20260902.`
     * The `debian-13` image family now points to the new `debian-13-trixie-v20260902` OS image.
     * The previous OS image (`debian-13-trixie-v20260827`) is marked `deprecated`.



## Deprecated or End of Support (EOS)

At some point, each OS version reaches the deprecation phase. For OS version deprecation dates, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).

Deprecated OS versions can either be in an extended supported or end of lifecycle phase.

In this stage, OS providers stop providing image updates and the OS images are marked deprecated. You might still be able to use these OS images, but you are responsible for acquiring updates, which are subject to availability from the OS distribution, vendor, or open source community.

When an OS version reaches EOS, the following takes place:

  * The latest image in the image family is either deleted or marked deprecated.
  * You can no longer use the image family. However, you can still use some or all of the OS images by referencing them directly with the exception of Windows where all OS images are deleted at EOS.

To create a VM from a deprecated image, you must use the Google Cloud CLI or REST. When specifying the image, you must use the `--image` flag because image families don't point to deprecated images. For more information about creating VMs, see [Create a VM instance from a public image](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#publicimage).

  * When an OS version reaches or goes past the extended lifecycle stage, Google doesn't guarantee feature compatibility with new machine families or CPU platforms, to these deprecated versions.

All VMs that use OS images that belong to this EOS OS version continue to work on Compute Engine and are still eligible for [Google Cloud support](https://docs.cloud.google.com/compute/docs/images/support-maintenance-policy#support-scope) beyond their EOS date. However, if any issues with the VM is identified to be associated with the deprecated OS version, Google might not be able to resolve the issue as OS provider support is no longer available.




Deprecated OS versions can either be in an extended supported phase or end of lifecycle.

### Extended support

For some operating systems, when they reach the deprecation phase, OS distributors provide a maintenance, extended or long-term paid package that can be applied to your OS:

  * For Red Hat Enterprise Linux (RHEL) OS: Maintenance support, Extended life phase, Extended Lifecycle support ELS (Add-On), or Extended Update Support (EUS)
  * For Rocky Linux: Long Term Support can be [purchased from CIQ](https://ciq.com/products/rocky-linux/)
  * For SUSE Linux Enterprise Server (SLES) OS: Long Term Service Pack Support, Extended Service Pack Overlap Support (ESPOS)
  * For Ubuntu Pro OS: Extended Security Maintenance (ESM)
  * For Windows OS: Extended Security Updates



For more details on these extended lifecycle packages, see the documentation for the OS provider.

### End of lifecycle (EOL)

For operating systems that have reached the end of the extended support period, or operating systems that don't support an extended support period, the following takes place:

  * The latest image in the image family is marked deprecated, or is deleted from Google Cloud.

  * The guest environment software provided by Google won't be updated for EOL OS versions, and repositories are no longer updated or maintained.

  * For existing VMs that use EOL OS versions, the following takes place:

    * The VM can't download or install software packages or updates from the OS vendor and security updates are no longer available. This occurs because content from the OS vendor might no longer be available from the existing channels as the configured software repository infrastructure from the OS vendor might be turned down or archived.
    * The VM continues to run but continued compatibility is not guaranteed. Active support might not be available from the OS vendor or Google. Google can provide options for migration or upgrades to newer OS versions.



## OS image naming convention, update schedule, and deprecation policy

The following table outlines the naming convention for OS images and image families, the update schedule, and the applicable EOS policy.

### Definitions

The following notations are used in the table:

  * `V` is the numeric version for the OS. For example `RHEL-7` where `7` is the numeric version
  * `R` is the release string sometimes referred to as the development codename for the OS. For example, `debian-13-trixie-v20260827` where `trixie` is the release string. _Release strings only apply to Debian and Ubuntu OS images_.
  * `N` is the numeric build number. _Build numbers only apply to Container-Optimized OS and Fedora CoreOS_.
  * `YYYYMMDD` is the Year/Month/Day that identifies the date that the OS image was built or published. For some OS, the date is preceded by a lowercase `v`. For example, `vYYYYMMDD`.

OS | Image family | OS image | Update schedule | Deprecation policy  
---|---|---|---|---  
CentOS Stream | 

  * centos-stream-V
  * centos-stream-V-arm64

| 

  * centos-stream-V-vYYYYMMDD
  * centos-stream-V-arm64-vYYYYMMDD

| Monthly | OS images are marked deprecated but are still available for use.  
Container-Optimized OS | 

  * cos-V-lts
  * cos-arm64-V

| 

  * cos-V-N
  * cos-arm64-V-N

| Monthly | OS images are marked deprecated but are still available for use.  
Debian | 

  * debian-V
  * debian-V-arm64

| 

  * debian-V-R-vYYYYMMDD
  * debian-V-R-arm64-vYYYYMMDD

| Monthly | OS images are marked deprecated but are still available for use.  
Fedora CoreOS | 

  * fedora-coreos-R
  * fedora-coreos-R-arm64

| 

  * fedora-coreos-V-YYYYMMDD-N-gcp-x86-64
  * fedora-coreos-V-YYYYMMDD-N-gcp-aarch64

| Critical bug or security issues | OS images are deleted on the EOS date.  
RHEL | 

  * rhel-V
  * rhel-V-arm64

| 

  * rhel-V-vYYYYMMDD
  * rhel-V-arm64-vYYYYMMDD

| Monthly | OS images are marked deprecated but are still available for use.  
RHEL BYOS | 

  * rhel-V-byos
  * rhel-V-byos-arm64
  * rhel-V-sap-byos

| 

  * rhel-V-byos-vYYYYMMDD
  * rhel-V-byos-arm64-vYYYYMMDD
  * rhel-V-sap-byos-vYYYYMMDD

| Monthly | OS images are marked deprecated but are still available for use.  
RHEL for SAP | 

  * rhel-V-sap-ha

| 

  * rhel-V-sap-vYYYYMMDD

| Monthly | OS images are marked deprecated but are still available for use.  
Rocky Linux | 

  * rocky-linux-V
  * rocky-linux-V-arm64
  * rocky-linux-V-optimized-gcp
  * rocky-linux-V-optimized-gcp-arm64

| 

  * rocky-linux-V-vYYYMMDD
  * rocky-linux-arm64-V-vYYYMMDD
  * rocky-linux-V-optimized-gcp-vYYYYMMDD
  * rocky-linux-V-optimized-gcp-arm64-vYYYYMMDD

| Monthly | OS images are marked deprecated but are still available for use.  
SQL Server on Windows Server | 

  * sql-R-V-win-V

| 

  * sql-V-R-windows-V-dc-vYYYYMMDD

| Monthly | OS images are deleted on the EOS date.  
SLES | 

  * sles-V
  * sles-V-arm64

| 

  * sles-V-vYYYYMMDD-x86-64
  * sles-V-vYYYYMMDD-arm64

| Quarterly | OS images are marked deprecated but are still available for use.  
SLES for SAP | 

  * sles-V-sap
  * sles-V-sap-hardened

| 

  * sles-V-sap-vYYYYMMDD-x86-64
  * sles-V-sap-hardened-vYYYYMMDD-x86-64

| Quarterly | OS images are marked deprecated but are still available for use.  
SLES for SAP BYOS | 

  * sles-V-byos
  * sles-V-byos-arm64
  * sles-V-sap-byos

| 

  * sles-V-byos-vYYYYMMDD-x86-64
  * sles-V-byos-vYYYYMMDD-arm64
  * sles-V-sap-byos-vYYYYMMDD-x86-64

| Quarterly | OS images are marked deprecated but are still available for use.  
Ubuntu LTS | 

  * ubuntu-V-lts
  * ubuntu-V-lts-arm64
  * ubuntu-minimal-V-lts
  * ubuntu-minimal-V-lts-arm64

| 

  * ubuntu-V-R-vYYYYMMDD
  * ubuntu-V-R-arm64-vYYYYMMDD
  * ubuntu-minimal-V-R-vYYYYMMDD
  * ubuntu-minimal-V-R-arm64-vYYYYMMDD

| Critical bug or security issues | OS images are marked deprecated but are still available for use.  
Ubuntu Pro | 

  * ubuntu-pro-V-lts
  * ubuntu-pro-V-lts-arm64
  * ubuntu-pro-fips-V-lts

| 

  * ubuntu-pro-V-R-vYYYYMMDD
  * ubuntu-pro-V-R-arm64-vYYYYMMDD
  * ubuntu-pro-fips-V-R-vYYYYMMDD

| Critical bug or security issues | OS images are marked deprecated but are still available for use.  
Windows Server | 

  * windows-V
  * windows-V-core

| 

  * windows-server-V-dc-vYYYYMMDD
  * windows-server-V-dc-core-vYYYYMMDD

| Monthly | OS images are deleted on the EOS date.  
  
## What's next

  * Learn more about [OS upgrade best practices](https://docs.cloud.google.com/compute/docs/images/os-upgrade-best-practices).
  * Learn more about the [operating systems](https://docs.cloud.google.com/compute/docs/images/os-details) that are available on Compute Engine.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
