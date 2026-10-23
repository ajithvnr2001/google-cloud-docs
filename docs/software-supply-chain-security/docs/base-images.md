---
url: https://docs.cloud.google.com/software-supply-chain-security/docs/base-images/
title: Base images \u00a0|\u00a0 Software supply chain security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:03.502148+00:00
---

# Base images  |  Software supply chain security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/software-supply-chain-security/docs/base-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Software supply chain security ](https://docs.cloud.google.com/software-supply-chain-security/docs)
  * [ Guides ](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)



Send feedback 

#  Base images Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of Google-provided base container images.

## What are base images?

A base image is the starting point for most container-based development workflows. Developers start with a base image and layer on top of it the necessary libraries, binaries, and configuration files used to run their application.

Many base images are basic or minimal Linux distributions: Debian, Ubuntu, Red Hat Enterprise Linux (RHEL), Rocky Linux, or Alpine. Developers can consume these images directly from Docker Hub or other sources. There are official providers along with a wide variety of other downstream repackagers that layer software to meet customer needs.

Google maintains base images for building its own applications. These images are built from the same source that Docker Hub uses. Therefore, they match the images you would get from Docker Hub.

The advantage of using Google-maintained images is that they are stored on Google Cloud, so you can pull these images directly from your environment without having to traverse networks.

Google updates these images whenever a new version of an official image is released. For more information on image versions, see the GitHub repository of [official images](https://github.com/docker-library/official-images).

## Google-provided base images

Google-provided [base images](https://console.cloud.google.com/marketplace/browse?filter=solution-type:container&filter=category:os) are available for the following OS distributions:

OS | Repository path | Google Cloud Marketplace listing  
---|---|---  
Debian 11 "Bullseye" | `marketplace.gcr.io/google/debian11` | [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/details/google/debian11)  
Debian 12 "Bookworm" | `marketplace.gcr.io/google/debian12` | [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/details/google/debian12)  
Rocky Linux 8 | `marketplace.gcr.io/google/rockylinux8` | [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/details/google/rockylinux8)  
Rocky Linux 9 | `marketplace.gcr.io/google/rockylinux9` | [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/details/google/rockylinux9)  
Ubuntu 22.04 | `marketplace.gcr.io/google/ubuntu2204` | [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/details/google/ubuntu2204)  
Ubuntu 24.04 | `marketplace.gcr.io/google/ubuntu2404` | [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/details/google/ubuntu2404)  
  
## Changes to Google-provided base images

The following base image changes took effect on November 3, 2023:

  * Updated Debian 11 images no longer have OpenSSL pre-installed.
  * The updated Ubuntu 20.04 image no longer has curl, Python, systemd, or sudo pre-installed.
  * Google no longer provides base images for the following Linux distributions: CentOS 7, CentOS 8, Ubuntu 18.04, and Debian 9 "Stretch".



## Licensing

For information about the license that applies to the base images, refer to the distribution's documentation.

## Alternative options

If base images aren't for you, you can use **Cached images** , which are frequently requested Docker Hub images stored on `mirror.gcr.io`. If you configure your Docker daemon to use cached images, your client always checks for a cached copy of a Docker Hub image before attempting to pull it directly from Docker Hub.

Learn more about [pulling cached images](https://docs.cloud.google.com/artifact-registry/docs/pull-cached-dockerhub-images).

For more ways to protect your software supply chain, including image validation, see [Software supply chain security](https://docs.cloud.google.com/software-supply-chain-security/docs/overview).

## What's next

  * Learn about [dependency management](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
