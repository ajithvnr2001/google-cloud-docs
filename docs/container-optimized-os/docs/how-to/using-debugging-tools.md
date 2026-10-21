---
url: https://docs.cloud.google.com/container-optimized-os/docs/how-to/using-debugging-tools/
title: Use debugging tools \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:16:41.593375+00:00
---

# Use debugging tools  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/how-to/using-debugging-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Use debugging tools Stay organized with collections  Save and categorize content based on your preferences. 

This page explains tools that you can use to debug Container-Optimized OS.

## Run the `perf` tool on Container-Optimized OS

By default, [`perf`](https://perf.wiki.kernel.org/index.php/Main_Page) is installed on Container-Optimized OS. You can run `perf` on your `cos` instance from your shell command line.

If you have limited privilege, you might need to enable the use of the performance events system using the following command:
    
    
    echo -1 | sudo tee /proc/sys/kernel/perf_event_paranoid
    

For information on how to use perf, refer to the [`perf` manual](http://man7.org/linux/man-pages/man1/perf.1.html) and the kernel [sysctl](https://www.kernel.org/doc/Documentation/sysctl/kernel.txt) settings.

## Enable kernel crash dump collection

In the rare event of a kernel panic, enabling kernel crash dump collection can help you and Cloud Customer Care determine the root cause. To enable crash dumps, see [User Guide: Kernel Crash Dump Collection for COS](https://cos.googlesource.com/cos/overlays/board-overlays/+/refs/heads/master/project-lakitu/docs/kdump.md) in the open source documentation. This user guide explains how to collect kernel crash dumps on GKE nodes with Container-Optimized OS or Container-Optimized OS instances created from Compute Engine.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
