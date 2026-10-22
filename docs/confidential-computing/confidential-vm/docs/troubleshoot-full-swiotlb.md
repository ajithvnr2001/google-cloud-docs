---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-full-swiotlb/
title: Full SWIOTLB \u00a0|\u00a0 Confidential VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:17.214139+00:00
---

# Full SWIOTLB  |  Confidential VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-full-swiotlb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  Full SWIOTLB Stay organized with collections  Save and categorize content based on your preferences. 

For disk and network input/output operations, Confidential VM uses a specific area in memory called the Software Input Output Translation Lookaside Buffer (SWIOTLB), which has a default size of 64 MB. The SWIOTLB is part of the total available RAM on the guest.

To check if a Confidential VM instance has encountered the `swiotlb buffer is full` error, connect to the instance and run the following command to query the `dmesg` logs:
    
    
    dmesg | grep 'swiotlb buffer is full'
    

To resolve this issue, increase the SWIOTLB size. Before increasing the size, ensure that the guest has enough RAM for the SWIOTLB and the operating system. Setting an excessively large SWIOTLB size can cause the VM instance to exceed memory limits, resulting in out-of-memory (OOM) errors or boot failures.

## Increase the SWIOTLB size

  1. To increase the size of the SWIOTLB, append the following line to `/etc/default/grub`:
         
         GRUB_CMDLINE_LINUX_DEFAULT=".... swiotlb=SIZE_IN_BYTES"
         

The following example shows how to increase the size of the SWIOTLB to 512 MB:
         
         GRUB_CMDLINE_LINUX_DEFAULT=".... swiotlb=262144"
         

Based on the Ubuntu version, you need to update the string in the `grub` file. For example, if you use Ubuntu 18.04, you need to update the `GRUB_CMDLINE_LINUX` string instead of the `GRUB_CMDLINE_LINUX_DEFAULT` string.

  2. Run the following command to regenerate `grub.cfg`:

### Ubuntu
         
         sudo update-grub
         

### Other distros
         
         grubcfg="/etc/grub2-efi.cfg"
         cp $grubcfg $grubcfg.bak
         grub2-mkconfig -o $grubcfg
         

  3. Reboot the VM.




For more information, see [How to increase SWIOTLB limit](https://github.com/AMDESE/AMDSEV#faq-4).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
