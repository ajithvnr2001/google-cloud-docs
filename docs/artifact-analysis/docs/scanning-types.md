---
url: https://docs.cloud.google.com/artifact-analysis/docs/scanning-types/
title: Types of scanning \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:05.996809+00:00
---

# Types of scanning  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/scanning-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)



Send feedback 

#  Types of scanning Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Analysis provides two features for scanning your containers: on-demand scanning and automatic scanning. This document introduces the benefits of each. Artifact Analysis also provides metadata management. To learn more about how you can use scanning and metadata storage together to secure your CI/CD pipeline from end to end, see the [Artifact Analysis overview](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis).

On-demand and automatic scanning can identify vulnerabilities and malicious packages in your [operating system](https://docs.cloud.google.com/artifact-analysis/docs/os-overview), and language packages ([Java](https://docs.cloud.google.com/artifact-analysis/docs/java-overview), and [Go](https://docs.cloud.google.com/artifact-analysis/docs/go-overview)). However, automatic language package scanning is only available for Artifact Registry.

For a list of supported scanning types for each registry product, view the [comparison chart](https://docs.cloud.google.com/artifact-registry/docs/transition/setup-repo#analysis).

See [pricing](https://cloud.google.com/artifact-analysis/pricing) to learn more about the costs associated with scanning container images.

## On-demand scanning

On-demand scanning lets you scan container images locally on your computer or in your registry, using the gcloud CLI. This gives you the flexibility to customize your CI/CD pipeline, depending on when you need to access the vulnerability results.

## Automatic scanning

Artifact Analysis performs vulnerability and malicious package scans on your artifacts in Artifact Registry. Artifact Analysis also monitors the vulnerability and malicious package information to keep it up to date. This process comprises two main tasks: on-push scanning and continuous analysis.

### On-push scanning

Artifact Analysis scans new images when they're uploaded to Artifact Registry. This scan extracts information about the packages in the container, including both system and application language packages, and identifies any malicious software. The images are scanned only once, based on the image's digest. This means that adding or modifying tags won't trigger new scans, only changing the contents of the image will.

Artifact Analysis only detects packages publicly monitored for security vulnerabilities.

When the scan of an image is completed, the resulting **scan result** shows the collection of vulnerability and malicious package occurrences for that image.

**Important:** When you enable the Artifact Analysis API, Artifact Analysis automatically begins scanning each new image as they are pushed to Artifact Registry repositories in your project. However, scanning is disabled by default for packages pushed to Artifact Registry repositories. To enable scanning in a repository, see [Control scanning settings for an individual repository](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning#disable-repo).

### Continuous analysis

Artifact Analysis creates occurrences for vulnerabilities and malicious packages found when you upload the image. After the initial scan, it continuously monitors the metadata for scanned images in Artifact Registry for new risks.

Artifact Analysis receives new and updated vulnerability information from vulnerability sources multiple times each day. When new vulnerability data arrives, Artifact Analysis updates the metadata of the scanned images to keep it up-to-date. Artifact Analysis updates existing vulnerability occurrences, creates new vulnerability occurrences for new notes, and deletes vulnerability occurrences that are no longer valid.

Artifact Analysis continues to scan images and packages as long as they have been pulled within the last 30 days. After 30 days, metadata for scanned images and packages will no longer be updated, and the results will be stale.

Artifact Analysis archives metadata that has been stale for more than 90 days. This archived metadata can be evaluated only by using the API. You can re-scan an image with stale or archived metadata by pulling that image. Refreshing metadata can take up to 24 hours. Packages with stale or archived metadata can't be rescanned.

### Vulnerability sources

Artifact Analysis obtains vulnerability data from various upstream providers to identify security risks in your container images. This data includes vulnerability data for [operating system packages](https://docs.cloud.google.com/artifact-analysis/docs/os-overview) and [language packages](https://docs.cloud.google.com/artifact-analysis/docs/os-overview).

Artifact Analysis also obtains data for malicious packages from the [OpenSSF Malicious Packages Repository](https://github.com/ossf/malicious-packages). Malicious packages are reported as **CRITICAL** severity findings.

For a complete list of vulnerability and malicious package sources, see [Vulnerability sources](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview#sources).

### Architectures

Artifact Analysis can scan images on any Linux-based architecture.

You can also use vulnerability scanning with manifest lists. A [manifest list](https://docs.docker.com/registry/spec/manifest-v2-2/#manifest-list) is a list of pointers to manifests for several platforms. They allow a single image to work with multiple architectures or variations of an operating system.

If your manifest list contains a Linux amd64 image, Artifact Analysis will scan that image. Otherwise, Artifact Analysis selects a different image from the list.

## What's next

  * [Work with OS packages](https://docs.cloud.google.com/artifact-analysis/docs/os-overview).
  * [Work with Go packages](https://docs.cloud.google.com/artifact-analysis/docs/go-overview).
  * [Work with Java packages](https://docs.cloud.google.com/artifact-analysis/docs/java-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
