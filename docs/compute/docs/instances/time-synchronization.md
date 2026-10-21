---
url: https://docs.cloud.google.com/compute/docs/instances/time-synchronization/
title: Configure time synchronization \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:50:45.568884+00:00
---

# Configure time synchronization  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/time-synchronization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure time synchronization Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Many software systems that depend on careful sequencing of events rely on a stable, consistent system clock. System logs written by most services include a timestamp, which helps debug issues that occur between various components of your system.

By default, Compute Engine instances are preconfigured to use network time protocol (NTP), which helps keep system clocks in sync with each other. By properly configuring NTP on your virtual machine (VM), you can optimize your VM's time synchronization to account for leap seconds as they occur.

If ensuring accurate time synchronization and monitoring the accuracy of your time synchronization are important goals, then instead of using NTP, you can sync your VM's clock with its host server's clock by using `chrony` and `ptp_kvm`. This configuration is designed to achieve accuracy within 1 ms for supported setups.

## Configure network time protocol (NTP) on a VM

Compute Engine instances are preconfigured to use network time protocol (NTP), which helps keep system clocks in sync with each other, and includes the following:

  * Higher accuracy than third-party NTP servers.
  * Handling for _leap seconds_ , one-second adjustments made to UTC time to account for changes in the Earth's rotation. Leap seconds don't happen at routine intervals, because the Earth's rotation speed varies irregularly in response to climatic and geological events.



For steps to configure NTP for a VM, see [Configure NTP for a VM](https://docs.cloud.google.com/compute/docs/instances/time-synchronization/configure-ntp).

## Configure accurate time

For accuracy designed to be within 1 ms with supported setups, you can configure your VM to sync its clock with its host server's clock. For details, see [Configure accurate time for Compute Engine VMs](https://docs.cloud.google.com/compute/docs/instances/time-synchronization/configure-time-sync).

## What's next

  * Learn more about [PCI Data Security Standard compliance](https://docs.cloud.google.com/architecture/pci-dss-compliance-in-gcp).
  * Review the [Google Public NTP FAQ](https://developers.google.com/time/faq).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
