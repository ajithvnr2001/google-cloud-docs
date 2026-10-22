---
url: https://docs.cloud.google.com/docs/buildpacks/base-images/
title: Base images \u00a0|\u00a0 Buildpacks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:17.732585+00:00
---

# Base images  |  Buildpacks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/buildpacks/base-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Buildpacks ](https://docs.cloud.google.com/docs/buildpacks)
  * [ Guides ](https://docs.cloud.google.com/docs/buildpacks/overview)



Send feedback 

#  Base images Stay organized with collections  Save and categorize content based on your preferences. 

A base image is the starting point for most container-based development workflows. Developers start with a base image and layer on top of it the necessary libraries, binaries, and configuration files used to run their application. Google Cloud's buildpacks publishes base images with multiple configurations of the available system packages and languages.

Base images are hosted in every region where Artifact Registry is available. You can customize the base image path by replacing the first portion of the URI with your region of choice:

`REGION-docker.pkg.dev/serverless-runtimes/STACK/runtimes/RUNTIME_ID`

Replace:

  * REGION with the preferred region, for example `us-central1`.
  * STACK with the preferred operating system stack, for example `google-24`.
  * RUNTIME_ID with the runtime ID used by your function, for example `python313`.



For example, buildpacks references the Node.js 24 base image using the `google-24` stack, hosted in `us-central1` with the following URL: `us-central1-docker.pkg.dev/serverless-runtimes/google-24/runtimes/nodejs24`.

For more information on the supported runtimes, see the [Runtime lifecycle](https://docs.cloud.google.com/docs/buildpacks/runtime-support#support_schedule).

## Security patches

To provide security patches, Google-provided base images depend on upstream providers, such as open source projects and operating system distributions. Upstream providers routinely identify security vulnerabilities and release patch updates to their components. Google receives those updates and includes them in a new base image version using the following process:

  1. Google creates a new image containing the patched dependencies and tags this image with `public-image-next`.
  2. Google tests the image with updated components and dependencies in staging environments.
  3. After tests are successful, Google starts updating all base images of running workloads to use the new base image.
  4. After testing and updates are complete, Google promotes the new image tag to `latest` and `public-image-current`, and deprecates the previous `latest` tag.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
