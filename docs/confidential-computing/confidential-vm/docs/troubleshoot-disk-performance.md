---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-disk-performance/
title: Disk performance \u00a0|\u00a0 Confidential VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:28.329740+00:00
---

# Disk performance  |  Confidential VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-disk-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  Disk performance Stay organized with collections  Save and categorize content based on your preferences. 

If you encounter slow disk performance, particularly with large file operations (greater than 1 GB), on your Confidential VM instance with a GPU, add `idle=poll` in `GRUB_CMDLINE_LINUX_DEFAULT` to the `/etc/default/grub.d/50-cloudimg-settings.cfg` file on your VM. Run the `sudo update-grub` command to update the GRUB configuration, and then reboot.

For more information, see [Troubleshooting disk performance in Google Cloud instances](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-performance#storage_performance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
