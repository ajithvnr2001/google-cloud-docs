---
url: https://docs.cloud.google.com/container-optimized-os/docs/resources/support-policy/
title: Support policy \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:40:00.567095+00:00
---

# Support policy  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/resources/support-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Resources ](https://docs.cloud.google.com/container-optimized-os/docs/resources)



Send feedback 

#  Support policy Stay organized with collections  Save and categorize content based on your preferences. 

Container-Optimized OS is tested and qualified for running various container workloads on Google Cloud. It is actively patched with security updates (CVEs) and bug-fixes to address issues that impact Google Cloud users. Users get access to these fixes via our image releases in the `cos-cloud` project.

Container-Optimized OS image support is available for our Long Term Supported (LTS) family of images in the `cos-cloud` project. For a description of available image families, see [Versioning scheme](https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning#image_families). The following support commitment applies only to our LTS family of images.

## Support duration

Approximately three times each year, the Container-Optimized OS team releases a Long Term Supported (LTS) milestone on its `cos-[MILESTONE]-lts` and `cos-arm64-[MILESTONE]-lts` image families. Once a milestone is introduced on the LTS families, it is supported for **26 months**.

During this support window:

  * The milestone is actively patched for any critical bugs.
  * The milestone is actively scanned for security vulnerabilities, and security fixes are applied on regular basis.
  * New releases containing high priority bug and security fixes are released on-demand.
  * New releases containing medium and low priority bug and security fixes are released every 3 months.
  * To maintain stability, no new breaking features are introduced.
  * All changes in the image are documented on a dedicated [release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes#lts_image_families) page.



## Deprecation

At the end of a milestone's support window, the corresponding `cos-[MILESTONE]-lts` and `cos-arm64-[MILESTONE]-lts` families are deprecated. Specifically, we set the [DEPRECATED flag](https://docs.cloud.google.com/compute/docs/reference/latest/images/deprecate) on images in that milestone and those images stop appearing in the active list of images in the `cos-cloud` project.

**Warning:** Any [Image Family API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/getFromFamily) references to the deprecated image family will return errors and break any workflows depending on it. You should not use this API to create production instances.

Deprecated images are still accessible and usable when accessed directly by name using the [`images get` API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/get). However, any issues with those images might not be fixed or will only be fixed in newer milestones. Issues reported against deprecated images may be fixed only in newer image milestones. To continue having access to bug fixes and security patches, upgrade to one of the newer active milestones.

## Contact us

  * For technical support: Contact [Google Cloud support](https://docs.cloud.google.com/support)
  * For general questions: 
    * StackOverflow: [google-container-os](http://stackoverflow.com/questions/tagged/google-container-os) tag
    * Mailing list for Compute Engine users: [gce-discussion](https://groups.google.com/forum/#!forum/gce-discussion)
    * Mailing list for Kubernetes Users: [kubernetes-users](https://groups.google.com/forum/#!forum/kubernetes-users)
    * Visit the Google Cloud [Slack community](https://googlecloud-community.slack.com/); [use this form to sign up](https://join.slack.com/t/googlecloud-community/shared_invite/zt-3icuwfdvq-eq_58LqmOoCNc16mpZcaNA).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
