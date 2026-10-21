---
url: https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning/
title: Versioning scheme \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:10:12.029980+00:00
---

# Versioning scheme  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Versioning scheme Stay organized with collections  Save and categorize content based on your preferences. 

## Milestones and Build Numbers

Major versions of Container-Optimized OS images are identified using what we call **milestones**. Container-Optimized OS milestones are monotonically increasing integers. Each new milestone indicates the start of a new development cycle (a branch in our code) and may introduce new features and other major changes.

Over the lifetime of a Container-Optimized OS milestone, we may release several updates containing bug fixes, security fixes and other changes. These incremental releases on a milestone can be identified using the **build number**.

The milestone and build number of the Container-Optimized OS you are using can be identified by inspecting the `/etc/os-release` file. In this file, the value of the `VERSION_ID` (for example, `VERSION_ID=81`) represents the milestone and the value of the `BUILD_ID` field (for example, `BUILD_ID=12871.1160.0`) represents the build number. The milestone and build number are also present as part of the Container-Optimized OS image name. For example, image `cos-81-12871-1160-0` has milestone `81` and build number `12871-1160-0`.

## Long Term Supported (LTS) milestones

Milestones that are intended for production use and supported for longer duration are labelled as LTS (for Long Term Supported). On Compute Engine, we use the [image families](https://docs.cloud.google.com/compute/docs/images#image_families) feature to label and identify our LTS releases.

The following table provides a summary of Container-Optimized OS releases available on Compute Engine: 

### Active Milestones

OS version | Image project | x86 image family | Arm image family | Built by | End of support | Release notes  
---|---|---|---|---|---|---  
COS 138 DEV | `cos-cloud` | `cos-dev` | `cos-arm64-dev` | Google | To Be Defined | [dev](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/dev)  
COS 133 LTS | `cos-cloud` | `cos-133-lts` | `cos-arm64-133-lts` | Google | Nov 2028 | [milestone 133](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m133)  
COS 129 LTS | `cos-cloud` | `cos-129-lts` | `cos-arm64-129-lts` | Google | July 2028 | [milestone 129](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m129)  
COS 125 LTS | `cos-cloud` | `cos-125-lts` | `cos-arm64-125-lts` | Google | Feb 2028 | [milestone 125](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m125)  
COS 121 LTS | `cos-cloud` | `cos-121-lts` | `cos-arm64-121-lts` | Google | March 2027 | [milestone 121](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121)  
  
### Deprecated Milestones

OS version | Image project | x86 image family | Arm image family | Built by | Deprecation date | Release notes  
---|---|---|---|---|---|---  
COS 117 LTS | `cos-cloud` | `cos-117-lts` | `cos-arm64-117-lts` | Google | Sept 2026 | [milestone 117](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117)  
COS 113 LTS | `cos-cloud` | `cos-113-lts` | `cos-arm64-113-lts` | Google | March 2026 | [milestone 113](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m113)  
COS 109 LTS | `cos-cloud` | `cos-109-lts` | `cos-arm64-109-lts` | Google | Sept 2025 | [milestone 109](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m109)  
COS 105 LTS | `cos-cloud` | `cos-105-lts` | `cos-arm64-105-lts` | Google | March 2025 | [milestone 105](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m105)  
COS 101 LTS | `cos-cloud` | `cos-101-lts` | `N/A` | Google | Oct 2024 | [milestone 101](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m101)  
COS 97 LTS | `cos-cloud` | `cos-97-lts` | `N/A` | Google | April 2024 | [milestone 97](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m97)  
COS 93 LTS | `cos-cloud` | `cos-93-lts` | `N/A` | Google | October 2023 | [milestone 93](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m93)  
COS 89 LTS | `cos-cloud` | `cos-89-lts` | `N/A` | Google | March 2023 | [milestone 89](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m89)  
COS 85 LTS | `cos-cloud` | `cos-85-lts` | `N/A` | Google | September 2022 | [milestone 85](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m85)  
COS 81 LTS | `cos-cloud` | `cos-81-lts` | `N/A` | Google | September 20211 | [milestone 81](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m81)  
COS 77 LTS | `cos-cloud` | `cos-77-lts` | `N/A` | Google | April 20211 | [milestone 77](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m77)  
COS 73 LTS | `cos-cloud` | `cos-73-lts` | `N/A` | Google | June 2020 | [milestone 73](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m73)  
COS 69 LTS | `cos-cloud` | `cos-69-lts` | `N/A` | Google | December 2019 | [milestone 69](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m69)  
  
### Development Release Notes

For release notes related to the milestone under development, see the [Development Release Notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/dev) page. 

For release notes related to cos-dev before M93, see the [Legacy Release Notes](https://docs.cloud.google.com/container-optimized-os/docs/legacy-release-notes) page. 

There may be multiple active LTS milestones at any time. For example, the following command shows currently active LTS image families:
    
    
    gcloud compute images list --no-standard-images --project=cos-cloud | grep lts
    cos-101-17162-40-16               cos-cloud  cos-101-lts                    READY
    cos-89-16108-766-3                cos-cloud  cos-89-lts                     READY
    cos-93-16623-295-5                cos-cloud  cos-93-lts                     READY
    cos-97-16919-189-3                cos-cloud  cos-97-lts                     READY
    cos-arm64-101-17162-40-16         cos-cloud  cos-arm64-101-lts              READY
    

## Lifecycle of an LTS milestone

A new Container-Optimized OS LTS milestone is introduced approximately every 4 months on its own image family named `cos-[MILESTONE]-lts` (x86) and `cos-arm64-[MILESTONE]-lts` (Arm). Before being labeled as LTS, the milestone undergoes approximately 4 months of feature development and 2 months of extensive testing and stabilization.

The lifecycle of a Container-Optimized OS LTS milestone looks as follows:

Stage | Duration | Description  
---|---|---  
Development | 4 months | Active development during which the milestone receives major package upgrades, new features.   
Released monthly or as needed on `cos-dev` and `cos-arm64-dev` families.   
Stabilization | 2 months | Features are frozen and the focus is on expanded testing, bug fixing and stabilizing the release.  
Released as needed on `cos-beta` and `cos-arm64-beta` families.   
Production | 26 months | Active maintenance of milestone by addressing production issues and security fixes with priority.  
Released as needed on `cos-[MILESTONE]-lts` and `cos-arm64-[MILESTONE]-lts` families.   
Deprecation | N/A | All images on the milestone are marked deprecated and the `cos-[MILESTONE]-lts` and `cos-arm64-[MILESTONE]-lts` are removed. Users may still refer to the deprecated images, but will not receive any bug fixes or security updates.   
  
Once promoted to the LTS family, the LTS milestone provides the following benefits:

  * A support duration of 26 months
  * Security fixes for the entire support duration
  * Fixes for any production issues
  * A dedicated [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes#lts_image_families) page listing every change going into the image.



**For all of your production deployments, we recommend that you use an image from one of the LTS families.**

After the LTS support duration is over for a LTS milestone, the corresponding image family will no longer receive any security or bug fixes. In addition, the corresponding `cos-[MILESTONE]-lts` and `cos-arm64-[MILESTONE]-lts` image families will be marked as deprecated.

**Warning:** Any [image family API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/getFromFamily) references to the deprecated image family will return errors and break any workflows depending on it. You should not use this API to create production instances.

Please refer to the [Support Policy](https://docs.cloud.google.com/container-optimized-os/docs/resources/support-policy) to learn more about support commitments for these families.

### LTS Refresh releases

On-demand releases are made on LTS milestones in response to high priority bug and security fixes. Every three months, a release is made that includes medium and low priority bug and security fixes. We call these releases "LTS Refresh" releases. These releases are made less frequently to help users manage update risks.

The release notes page for the milestone will indicate which releases are LTS Refresh releases. Users should take extra care when rolling out these releases, because medium and low priority bug and security fixes might introduce regressions.

## Choosing the right Container-Optimized OS version

On Compute Engine, the image families for Container-Optimized OS can guide you in selecting the correct image for your intended purpose. We strongly recommend that you set up tiered testing alongside your production environment utilizing the convenience offered by the image family api.

**Warning:** We recommend using the [Image Family API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/getFromFamily) only for testing to automatically pick the latest images released on the image families. We do not recommend using it for creating production instances. You should always refer to a specific image you have qualified for use in production. This prevents any potential disruption due to the image being updated and rolled out to your production environment without being qualified first.x86 image family | Arm image family | Description | Suggested use  
---|---|---|---  
`cos-[MILESTONE]-lts` | `cos-arm64-[MILESTONE]-lts` | This family follows releases for a particular production-ready milestone. Images on this family receive only security and stability fixes. | Suitable for running all production workloads. Start with the highest milestone to maximize support duration.  
`cos-stable` | `cos-arm64-stable` | This family follows our _latest_ production-ready milestone. Images on this family receive all security and stability fixes. Every 4 months, the latest LTS milestone containing new features is also released on this family. | Create one-off instances that you plan to configure and maintain manually.  
`cos-beta` | `cos-arm64-beta` | This family follows our _next_ major release in stabilization phase. | Use for continuous testing to validate new features and OS upgrades.  
`cos-dev` | `cos-arm64-dev` | This family follows our latest in-development release. Images on this family receive major changes and potentially unstable features. | Use for experimentation and one-off testing.  
  
A tiered testing setup like this should help to minimize issues when rolling out newer major versions of Container-Optimized OS images to your production environment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


