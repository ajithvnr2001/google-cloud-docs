---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/import-migrate/
title: Troubleshooting licenses \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:16.135411+00:00
---

# Troubleshooting licenses  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/import-migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting licenses Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document shows you how to resolve issues related to importing and migrating virtual machine (VM) instances to Compute Engine that have a misapplied license.

For example, learn how to resolve issues with a VM that has an on-demand license instead of a bring your own license (BYOL). For information about the different types of licenses, see [About licenses](https://docs.cloud.google.com/compute/docs/licenses/about).

## Mitigate incorrect license imports or migrations

If you tried to import or migrate a VM into Compute Engine with a BYOL or BYOS license, but the VM's [license string](https://docs.cloud.google.com/compute/docs/images/os-details#license-strings) is not appended with `byol` or `byos`, then your license was not successfully imported or migrated with the VM.

To resolve this issue, do one of the following depending on how you imported or migrated the VM:

  * If you imported the VM using the [`gcloud compute instances import` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/import) or the Cloud Build API, import the VM again, and specify the [`--os` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/import#--os) with the `byol` version of the OS.

  * If you imported the VM using the [`gcloud beta compute machine-images import` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/machine-images/import), import the VM again, and specify the [`--byol` flag](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/machine-images/import#--byol).

  * If you imported the VM using the [`gcloud beta compute images import` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/images/import), import the VM again, and specify the [`--byol` flag](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/images/import#--byol).

  * If you migrated the VM using Migrate to Virtual Machines, contact Cloud Customer Care to help you resolve the issue. For more information, see [Getting support with Cloud Customer Care](https://docs.cloud.google.com/support/docs).




## What's next

  * [Learn how to view and append license strings](https://docs.cloud.google.com/compute/docs/licenses/view-append)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
