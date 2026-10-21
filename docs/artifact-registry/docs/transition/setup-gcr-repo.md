---
url: https://docs.cloud.google.com/artifact-registry/docs/transition/setup-gcr-repo/
title: gcr.io repositories \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:45:24.211194+00:00
---

# gcr.io repositories  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/transition/setup-gcr-repo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  gcr.io repositories Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of Artifact Registry `gcr.io` repositories. `gcr.io` repositories let Container Registry users maintain their existing Google Cloud infrastructure by storing container images in Artifact Registry and supporting requests to the same `gcr.io` URLs used by Container Registry.

`gcr.io` repositories hosted on Artifact Registry are a [Generally Available](https://cloud.google.com/products#product-launch-stages) feature, and they will continue to work after the Container Registry deprecation.

To transition to `gcr.io` repositories on Artifact Registry, follow the instructions in [Migrate automatically to Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/auto-migrate-gcr-ar).

## Background information on Container Registry deprecation

Container Registry is deprecated. Effective March 18, 2025, Container Registry is shut down and writing images to Container Registry is unavailable.

`gcr.io` URLs hosted on Artifact Registry, including Google-owned images with `gcr.io` URLs, are not affected by the Container Registry shutdown.

## `gcr.io` domain support

Artifact Registry supports requests to the `gcr.io` domain in `gcr.io` repositories in multi-regional locations corresponding with Container Registry host locations.

Container Registry hostname | Artifact Registry repository location | Artifact Registry repository name  
---|---|---  
gcr.io | us | gcr.io  
asia.gcr.io | asia | asia.gcr.io  
eu.gcr.io | europe | eu.gcr.io  
us.gcr.io | us | us.gcr.io  
  
## Storage bucket configuration

When you create a repository in Artifact Registry, Artifact Registry does not create corresponding Cloud Storage buckets in your project. If you have automation for Container Registry that interacts directly with storage buckets, you must update it to make corresponding changes to the Artifact Registry repository.

For example, if you programmatically grant Cloud Storage permissions on storage buckets for Container Registry, you must update that automation to grant Artifact Registry permissions on the Artifact Registry repositories that host images for the `gcr.io` domain.

## Limitations

The following limitations apply to Artifact Registry `gcr.io` repositories:

  * When transitioning from Container Registry, you cannot map a Container Registry host to an Artifact Registry repository in a different project.

**Note:** You can still pull container images in a `gcr.io` repository from other Google Cloud projects.
  * Each Container Registry hostname maps to only one corresponding Artifact Registry `gcr.io` repository in the same multi-region.

  * Names for `gcr.io` repositories are predefined and you can't modify them.




If you need more control over the location of your repositories, you can transition to `pkg.dev` repositories in Artifact Registry. Since `pkg.dev` repositories don't have any support for the `gcr.io` domain, this transition approach requires more changes to your existing automation and workflows. See [Choose a transition option](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr#transition-options) to learn about feature differences.

## What's next

  * Use the [automatic migration tool](https://docs.cloud.google.com/artifact-registry/docs/transition/auto-migrate-gcr-ar) to transition to `gcr.io` Artifact Registry repositories.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
