---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup-prerequisites/
title: Insert the YubiKeys into the device \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:38.619835+00:00
---

# Insert the YubiKeys into the device  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup-prerequisites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Insert the YubiKeys into the device Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to verify and insert the YubiKeys into Google Distributed Cloud (GDC) air-gapped appliance.

**Important:** To access the URLs on this page, you must connect to the internet. The URLs are provided for use when you have such access.

## Before you begin

[Verify cabling](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/check-cables)

## Verify YubiKeys are present

Each GDC air-gapped appliance is shipped with YubiKeys in the original packaging. If the YubiKeys arrive opened (or in damaged packaging), open a support case immediately.

## Insert the YubiKeys

To authenticate blades and decrypt local storage during startup, you must insert a dedicated YubiKey into each server prior to booting.

Complete the following steps to install and handle the YubiKeys:

  1. **Unpack each YubiKey and insert it into a server USB port.**
     * Make sure the **gold contact pins faces upward**.
     * Insert one YubiKey per server across all three servers. If a YubiKey is missing at startup, the operating system fails to boot and displays a console error.
  2. **Start the bootstrap process.** During bootstrapping, the system binds each YubiKey to its specific blade. After binding, keys are node-specific and can't be used interchangeably.
  3. **(Optional) Remove the YubiKeys after the appliance finishes booting:** removing a YubiKey after boot won't disrupt active appliance operations.
  4. **Reinsert the corresponding YubiKey into its original node before the next reboot.** Each blade requires its specific bound YubiKey to decrypt and boot successfully.

**Warning:** Store all YubiKeys in a secure location and remove them whenever the appliance is not in operation. Because YubiKeys can decrypt local drives at any stage of the GDC air-gapped appliance lifecycle, leaving them unattended in an inactive device creates a security vulnerability.

For detailed hardware specifications, see the YubiKey 5 Nano FIPS product overview: <https://www.yubico.com/product/yubikey-5-nano-fips/>

## What's next

[Connect the laptop to the switch](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/connect-the-device)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
