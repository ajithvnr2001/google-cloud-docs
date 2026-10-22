---
url: https://docs.cloud.google.com/docs/buildpacks/support-policy/
title: Google Cloud's buildpacks support policy \u00a0|\u00a0 Buildpacks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:42:31.353799+00:00
---

# Google Cloud's buildpacks support policy  |  Buildpacks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/buildpacks/support-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Buildpacks ](https://docs.cloud.google.com/docs/buildpacks)
  * [ Resources ](https://docs.cloud.google.com/docs/buildpacks/release-notes)



Send feedback 

#  Google Cloud's buildpacks support policy Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud's buildpacks use open source components that are maintained by their respective communities. Google Cloud's buildpacks publishes [builders](https://docs.cloud.google.com/docs/buildpacks/builders) that contain necessary components to build and run an application or function. Each builder is tied to a specific operating system (OS) distribution and has their own set of supported components and language runtimes.

Google provides support for builders during [General availability (GA)](https://cloud.google.com/products#product-launch-stages). New builders will generally follow Ubuntu LTS releases and are announced in the Google Cloud's buildpacks [release notes](https://docs.cloud.google.com/docs/buildpacks/release-notes).

During the GA support period:

  * Builder components (OS packages, libraries, language runtimes, etc.) are regularly updated with security and bug fixes.
  * To maintain stability, Google Cloud's buildpacks avoid implementing breaking features or changes into the builder. Breaking changes are announced in advance in the Google Cloud's buildpacks [release notes](https://docs.cloud.google.com/docs/buildpacks/release-notes).



When a builder's OS distribution is no longer actively maintained, for example the End of Support for Ubuntu, the Google Cloud's buildpacks builder might be deprecated and, eventually get sunset.

This involves three aspects: a publication of the deprecation date, a deprecation period, and a sunset date. The dates posted in the Support schedule section indicate the start of the deprecation period and the sunset date.

During the deprecation period, you can generally continue to create new applications and update existing applications using the builder. You should use this time to migrate apps or functions that use the deprecated builder to a recent builder.

The builder image will continue to be available in the registry but include an additional `<builder-version>-sunset` tag, for example `v1-sunset`. Container images that were built using the sunset builder will continue to exist in the registry, be deployable from wherever it is stored, and continue to run as normal.

Google might change any builder's support schedule or lifecycle in accordance with the terms of your agreement for the use of Google Cloud services

## Support schedule

The following list includes the supported Google Cloud's buildpacks builders, as well as the builders that have been deprecated and sunset.

Tag | Location | Operating system | Deprecation | Sunset  
---|---|---|---|---  
`google-24` | `[gcr.io/buildpacks/builder:google-24](https://gcr.io/buildpacks/builder:google-24)`,`latest` | Ubuntu 24 | April 2029 | April 2030  
`google-22` | `[gcr.io/buildpacks/builder:google-22](https://gcr.io/buildpacks/builder:google-22)` | Ubuntu 22 | April 2027 | April 2028  
`v1` | `[gcr.io/buildpacks/builder:v1](https://gcr.io/buildpacks/builder:v1)` | Ubuntu 18 | December 2024 | April 2025  
  
The `latest` tag always points to `google-24`.

Key dates might be delayed based on the stability and availability of key components. Revisit this page to stay up to date.

## Languages & Builders

Every builder provided by Google Cloud's buildpacks support different operating system packages and language runtime versions. For details, see the list of [supported languages for each builder](https://docs.cloud.google.com/docs/buildpacks/builders).

Language runtimes have their own support and maintenance schedules provided by their respective communities. This is notable in two ways:

  * Language versions that are available by supported builders might not be supported by their community. We encourage you to update to a newer and actively supported language version as soon as possible.
  * A builder's underlying OS might be out of support but your preferred language version is still actively maintained. In this case, we encourage you to update to a recent builder version with an actively maintained OS community.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
