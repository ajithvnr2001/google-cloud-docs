---
url: https://docs.cloud.google.com/build/docs/securing-builds/cmek/
title: CMEK compliance in Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:09.439337+00:00
---

# CMEK compliance in Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/securing-builds/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  CMEK compliance in Cloud Build Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Build provides [customer-managed encryption keys (CMEK) compliance](https://docs.cloud.google.com/kms/docs/cmek#cmek_compliance) by encrypting the build-time persistent disk with an ephemeral key that is generated for each build. No configuration is required. The key is uniquely generated for each build.

Once a build starts, the key is accessible only to the build processes requiring it for the lifetime of the build. Then, the key is wiped from memory and destroyed.

The key isn't retained anywhere, isn't accessible to Google engineers or support staff, and can't be restored. The data that was protected using such a key is permanently inaccessible once the build completes.

## How does the ephemeral key encryption work?

Cloud Build supports CMEK through the use of ephemeral keys, allowing it to be fully consistent and compatible with a CMEK-enabled setup.

Cloud Build does the following to ensure build-time persistent disks are encrypted with an ephemeral key:

  1. Cloud Build mints a random 256-bit encryption key for encrypting each build-time persistent disk.

  2. Cloud Build leverages the Customer-Supplied Encryption Key (CSEK) feature of persistent disk to use this new encryption key as a persistent disk encryption key.

  3. Cloud Build destroys the ephemeral key as soon as the disk is created. The key is never logged or written to any persistent storage and is now irretrievable.

  4. When the build is completed, the persistent disk is deleted, at which point no traces of the key nor the encrypted persistent disk data remain anywhere in Google infrastructure.




## When does ephemeral key encryption not apply?

When you create or trigger a build using source mirroring (and not using GitHub triggers), your source code is stored in Cloud Storage or Cloud Source Repositories. You have full control over the code storage location, including control over its encryption.

## Build logs

Cloud Build offers [several options](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs) for storing your build logs. To be CMEK compliant, you must store your logs [only in Cloud Logging](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs#store-custom-logging) or in [your own Cloud Storage bucket](https://docs.cloud.google.com/build/docs/securing-builds/store-manage-build-logs#store-custom-storage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
