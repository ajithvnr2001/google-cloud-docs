---
url: https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update/
title: Automatic updates \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:49.999889+00:00
---

# Automatic updates  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Automatic updates Stay organized with collections  Save and categorize content based on your preferences. 

Container-Optimized OS images have the built-in capability to automatically upgrade to a newer version when released. This capability, when enabled, allows user instances to stay up-to-date with respect to security fixes and bug fixes.

When Container-Optimized OS is used as part of a managed service (for example, Google Kubernetes Engine, Cloud SQL, etc.), the managed service takes care of updating the Container-Optimized OS instance for the users. So, automatic updates are disabled on those by default.

Users running production workloads that are sensitive to kernel upgrades and require controlled qualification and rollout should also disable automatic updates. For more information, see the Disabling automatic updates section.

**Note:** In-place updates are not supported on Container-Optimized OS VMs with Unified Extensible Firmware Interface (UEFI) Secure Boot enabled. UEFI Secure Boot is not enabled on Container-Optimized OS VMs by default. To learn more about UEFI Secure Boot, see the [Shielded VM documentation](https://docs.cloud.google.com/security/shielded-cloud/shielded-vm#secure-boot).**Note:** In-place updates are not supported on Container-Optimized OS Arm-based images.

## Enable or disable automatic updates

In milestone 117 and later, the automatic updates feature is disabled by default on all Container-Optimized OS images. In milestones earlier than 117, the feature is enabled by default. You can enable or disable automatic updates by setting the `cos-update-strategy` metadata on new instances, existing instances, or on all instances in a project, as described in the following sections.

### Configure auto-updates on a new instance

Create a new instance with automatic updates enabled:
    
    
    gcloud compute instances create INSTANCE_NAME \
       --metadata cos-update-strategy=update_enabled
    

Create a new instance with automatic updates disabled:
    
    
    gcloud compute instances create INSTANCE_NAME \
       --metadata cos-update-strategy=update_disabled
    

### Configure auto-updates on an existing instance

Enable automatic updates for an existing instance:
    
    
    gcloud compute instances add-metadata INSTANCE_NAME \
       --metadata cos-update-strategy=update_enabled
    

Disable automatic updates for an existing instance:
    
    
    gcloud compute instances add-metadata INSTANCE_NAME \
       --metadata cos-update-strategy=update_disabled
    

### Configure auto-updates on all instances in a project

Starting from [milestone 97](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m97), you can enable or disable auto-updates for all instances in a project using metadata flags in project metadata.

Enable updates for all instances in a project:
    
    
    gcloud compute project-info add-metadata \
       --metadata cos-update-strategy=update_enabled
    

Disable updates for all instances in a project:
    
    
    gcloud compute project-info add-metadata \
       --metadata cos-update-strategy=update_disabled
    

**Note:** Metadata flags defined at the instance level take precedence over metadata flags defined at project level.

## Automatic update design

Container-Optimized OS uses an active-passive root partition scheme. The OS image is updated in its entirety, including the kernel, as opposed to package-by-package updates like on traditional Linux distributions. The image ships with the automatic updates feature enabled; this means that a default Container-Optimized OS instance always downloads the latest OS version and installs it on the passive partition soon after it's released.

If you are using an image from [LTS milestone](https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning#lts_milestones) or cos-stable image family, then you will get an update of the latest OS version from the same milestone. On cos-dev and cos-beta image family, the update will be the latest OS version from the corresponding image family.

**Note:** The update does not take effect until the instance is rebooted, and the auto-updater does not force reboot when an update is installed. After an updated version has been installed, the instance must be rebooted before it can update to a newer version.

### Changes to automatic update behavior

The Container-Optimized OS team is actively working on improving our backend infrastructure that makes automatic updates possible. As part of these changes, we are rotating the keys used to sign and validate the update payloads. However, images released before the key rotation cannot be automatically updated to images released after the rotation. The affected list of images are as followings:

  * These images cannot be updated to latest versions:

    * On Milestone 77: images prior to cos-77-12371-1000-0
    * On Milestone 81: images prior to cos-81-12871-1000-0
    * On Milestone 85: images prior to cos-85-13310-1000-0
    * On Milestone 86: images prior to cos-dev-86-15053-0-0
  * These images will no longer receive any updates:

    * All milestones before 77, including any previously deprecated milestones.



Users running standalone Container-Optimized OS with any of the affected versions, and having the auto-update feature enabled, will not see their instances being updated to newer versions. In these cases, users should manually choose newer OS versions by recreating their VM instances with the newer image. Automatic updates will continue to work on all supported milestones for new releases.

**Note:** Users using Container-Optimized OS as part of a managed service (for example, Google Kubernetes Engine, Cloud SQL, etc.) are not affected.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
