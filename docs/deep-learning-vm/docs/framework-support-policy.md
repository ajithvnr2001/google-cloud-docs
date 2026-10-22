---
url: https://docs.cloud.google.com/deep-learning-vm/docs/framework-support-policy/
title: Deep Learning VM framework support policy \u00a0|\u00a0 Deep Learning VM Images \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:47.932217+00:00
---

# Deep Learning VM framework support policy  |  Deep Learning VM Images  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-vm/docs/framework-support-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Deep Learning VM Images ](https://docs.cloud.google.com/deep-learning-vm/docs)
  * [ Resources ](https://docs.cloud.google.com/deep-learning-vm/docs/release-notes)



Send feedback 

#  Deep Learning VM framework support policy Stay organized with collections  Save and categorize content based on your preferences. 

Deep Learning VM Images provides containers and virtual machine images to simplify the configuration of your machine learning (ML) workloads. These images contain the operating system, the ML frameworks, drivers, and other libraries. We publish new versions of images regularly to include new patches, security updates, and features. Each image provided by Deep Learning VM provides support for a specific minor version of an ML framework.

This allows you time to update and test your code when moving from one framework version to another. You should always test your jobs and models thoroughly when switching to a new framework version, regardless of whether it's a major or minor update.

The Deep Learning VM release notes are a comprehensive log of all the changes, updates, and new features that are rolled out. They are essential for anyone using these images to stay informed about the latest developments and to manage their machine learning environments effectively. Subscribe to the [Deep Learning VM release notes](https://docs.cloud.google.com/deep-learning-vm/docs/release-notes) page for announcements about deprecations and new version releases for your images and frameworks.

See also the [list of supported framework versions](https://docs.cloud.google.com/deep-learning-vm/docs/images#supported-frameworks).

## Shared responsibility

Securing your workloads on Deep Learning VM is a shared responsibility. While Deep Learning VM regularly publishes new versions of images to address security vulnerabilities, you are responsible for tasks such as the following:

  * Manually upgrading to the latest version.

  * Ensuring that you properly configured your services to use the latest version.




For more information, see [Shared responsibility](https://docs.cloud.google.com/deep-learning-vm/docs/shared-responsibility).

## Support policy for framework versions

During the supported period for an ML framework version, we will publish new image versions regularly. The updates may include the following:

  * Patch updates for supported frameworks. For example, if we support TensorFlow 2.7, and TensorFlow releases 2.7.1 to address bugs, we will release a new image version.

  * Security updates for supported frameworks.

  * Non-breaking updates to other packages and software installed on the image.

  * Updates to dependencies that have reached end-of-support. For example, if an image has Python 3.7 installed and it reaches the end-of-support date, we will release a new image version. If the change in dependency may be a breaking change, we will update [List of all available versions](https://docs.cloud.google.com/deep-learning-vm/docs/images#supported-frameworks) to indicate the change in the dependency.




Once published, an image version is immutable and does not change. You should always use the latest image version, as earlier versions may have security vulnerabilities or other critical bugs.

### Support policy schedule

Deep Learning VM supports images for a specific window of time. It is a common practice in the industry since components, including some open source components, have to be managed to ensure security and performance. For Deep Learning VM, the support policy revolves around two key dates:

  * **End-of-patch and support date:** After this date, Deep Learning VM will no longer publish new image versions for that specific framework version. This means no more patch updates, security fixes, or non-breaking updates. Existing resources that have been deployed to Deep Learning VM will continue to function, but it's recommended to plan your migration to a newer, supported framework version.

To receive troubleshooting support from Deep Learning VM, you may be asked to upgrade to a framework version that is within the supported time period.

  * **End-of-availability date:** After this date, you can no longer use images for this framework version. Services may block the creation of new resources using these images, and the images will no longer be available for download.




### Image deprecation

When images reach the **End-of-patch and support date** , they are deprecated. Deprecation means that these images are removed from public visibility and it's encouraged to use supported images to help ensure security and performance. However, if you must use a deprecated image, see [Use an image after deprecation](https://docs.cloud.google.com/deep-learning-vm/docs/images#use-image-after-deprecation).

## What's next

  * Review the [list of supported framework versions](https://docs.cloud.google.com/deep-learning-vm/docs/images#supported-frameworks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
