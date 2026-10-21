---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-io-operation-timeouts/
title: I/O operation timeouts \u00a0|\u00a0 Confidential VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:41.414727+00:00
---

# I/O operation timeouts  |  Confidential VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-io-operation-timeouts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  I/O operation timeouts Stay organized with collections  Save and categorize content based on your preferences. 

If you're encountering I/O timeout errors on your Confidential VM instance, latency might be exceeding the default timeout parameter for I/O operations submitted to NVMe devices.

To increase the timeout parameter, add the following lines to the `/lib/udev/rules.d/65-gce-disk-naming.rules` file on your VM, and then reboot:
    
    
    KERNEL=="nvme*n*", ENV{DEVTYPE}=="disk", ATTRS{model}=="nvme_card-pd",
    ATTR{queue/io_timeout}="4294967295"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
