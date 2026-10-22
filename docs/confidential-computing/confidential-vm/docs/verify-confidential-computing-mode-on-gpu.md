---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/verify-confidential-computing-mode-on-gpu/
title: Verify Confidential Computing is enabled on GPUs \u00a0|\u00a0 Confidential VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:31.749726+00:00
---

# Verify Confidential Computing is enabled on GPUs  |  Confidential VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/verify-confidential-computing-mode-on-gpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  Verify Confidential Computing is enabled on GPUs Stay organized with collections  Save and categorize content based on your preferences. 

After completing [the configuration steps](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-a-confidential-vm-instance-with-gpu), verify that your GPU is correctly operating in confidential computing mode:

  1. Verify that the `nvidia-persistenced` service is running with `uvm-persistence-mode` enabled:
         
         ps aux | grep nvidia-persistenced | grep -v grep
         

The output is similar to the following:
         
         nvidia-+     729  6.2  0.0   5468  1664 ?  Ss   12:02   0:10
         /usr/bin/nvidia-persistenced \
         --user nvidia-persistenced \
         --uvm-persistence-mode \
         --verbose
         

**Caution:** Don't restart the `nvidia-persistenced` service after enabling `uvm-persistence-mode`, as this can disrupt the secure connection and require a VM reboot.
  2. Confirm that the GPU is running in confidential computing mode:
         
         sudo nvidia-smi conf-compute -f
         

The output is similar to the following:
         
         CC status: ON
         

  3. Set GPU to ready state after each reboot.
         
         sudo nvidia-smi conf-compute -srs 1
         

  4. Verify Confidential Computing ready state.
         
         sudo nvidia-smi conf-compute -grs
         

If you transition a GPU out of the ready state using `nvidia-smi conf-compute -srs 0`, reboot the VM instance to return the GPU to the ready state.

The output is similar to the following:
         
         Confidential Compute GPUs Ready state: ready
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
