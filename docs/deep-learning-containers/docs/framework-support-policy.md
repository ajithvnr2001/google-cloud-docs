---
url: https://docs.cloud.google.com/deep-learning-containers/docs/framework-support-policy/
title: Deep Learning Containers framework support policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:47.456736+00:00
---

# Deep Learning Containers framework support policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-containers/docs/framework-support-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Deep Learning Containers ](https://docs.cloud.google.com/deep-learning-containers/docs)
  * [ Resources ](https://docs.cloud.google.com/deep-learning-containers/docs/release-notes)



Send feedback 

#  Deep Learning Containers framework support policy Stay organized with collections  Save and categorize content based on your preferences. 

Deep Learning Containers publishes containers and virtual machine images to simplify the configuration of your machine learning (ML) workloads. These images contain the operating system, the ML frameworks, drivers, and other libraries. We publish new versions of images regularly to include new patches, security updates, and features. Each image provided by Deep Learning Containers provides support for a specific minor version of an ML framework.

This allows you time to update and test your code when moving from one framework version to another. You should always test your jobs and models thoroughly when switching to a new framework version, regardless of whether it's a major or minor update.

For all services, subscribe to the [Deep Learning Containers release notes](https://docs.cloud.google.com/deep-learning-containers/docs/release-notes) page for announcements about new version releases for your containers, images, and frameworks.

For the list of supported framework versions, see [Choose a container image](https://docs.cloud.google.com/deep-learning-containers/docs/choosing-container#deciding).

## Shared responsibility

Securing your workloads on Deep Learning Containers is a shared responsibility. While Deep Learning Containers regularly publishes new versions of images to address security vulnerabilities, you are responsible for tasks such as the following:

  * Manually upgrading to the latest version.

  * Ensuring that you properly configured your services to use the latest version.




For more information, see [Shared responsibility](https://docs.cloud.google.com/deep-learning-containers/docs/shared-responsibility).

## Support policy for framework versions

During the supported period for an ML framework version, we will publish new image versions regularly. The updates may include the following:

  * Patch updates for supported frameworks. For example, if we support TensorFlow 2.7, and TensorFlow releases 2.7.1 to address bugs, we will release a new image version.

  * Security updates for supported frameworks.

  * Non-breaking updates to other packages and software installed on the image.

  * Updates to dependencies that have reached end-of-support. For example, if an image has Python 3.7 installed and it reaches the end-of-support date, we will release a new image version. If the change in dependency may be a breaking change, we will update [Choose a container image](https://docs.cloud.google.com/deep-learning-containers/docs/choosing-container#deciding) to indicate the change in the dependency.




Once published, an image version is immutable and does not change. You should always use the latest image version, as older versions may have security vulnerabilities or other critical bugs.

### Support policy schedule

Support periods for each framework version follows this schedule:

  * **End-of-patch and support date:** After this date, Deep Learning Containers will no longer publish new image versions for that framework version. Existing resources that have been deployed to Deep Learning Containers continue to function. After this date, we recommend you plan to switch to a more recent framework version.

To receive troubleshooting support from Deep Learning Containers, you may be asked to upgrade to a framework version that is within the supported time period. 

  * **End-of-availability date:** After this date, you can no longer use images for this framework version. Services may block the creation of new resources using these images, and the images will no longer be available for download.




## What's next

  * Review the [list of supported framework versions](https://docs.cloud.google.com/deep-learning-containers/docs/choosing-container#deciding).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
