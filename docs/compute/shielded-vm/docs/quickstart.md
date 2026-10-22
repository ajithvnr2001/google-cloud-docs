---
url: https://docs.cloud.google.com/compute/shielded-vm/docs/quickstart/
title: Quickstart: Enable Shielded VM options \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:01.565670+00:00
---

# Quickstart: Enable Shielded VM options  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/shielded-vm/docs/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Shielded VM ](https://docs.cloud.google.com/compute/shielded-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quickstart: Enable Shielded VM options

Learn how to enable Shielded VM options by using the Google Cloud console.

## Before you begin

Before you start this tutorial, complete the following steps:

  1. Create a VM instance with [an OS that supports Shielded VM features](https://docs.cloud.google.com/compute/docs/images/os-details#security-features). Learn more about [creating a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
  2. Verify that you have the following permissions on the VM.

     * `compute.instances.updateShieldedInstanceConfig`

Learn more about [managing access to Compute Engine resources](https://docs.cloud.google.com/compute/docs/access/managing-access-to-resources).




## Enable all Shielded VM options

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

  2. Click the instance name to open the **VM instance details** page.

  3. Click stop **Stop**. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.

  4. After the instance stops, click **Edit**.

  5. In the **Shielded VM** section, modify the Shielded VM options:

     * Toggle **Turn on Secure Boot** to enable Secure Boot. Learn more about [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot).
     * Toggle **Turn on vTPM** to enable the virtual trusted platform module (vTPM). Learn more about [vTPM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm).
     * Toggle **Turn on Integrity Monitoring** to enable integrity monitoring. Learn more about [integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring).
  6. Click **Save**.

  7. Click **Start** to start the instance.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

  2. In the row for the VM instance you created for this exercise, click **More Actions** , and then select **Delete**.




## What's next

  * Learn more about the [key concepts in Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm).
  * Learn more about [modifying Shielded VM options](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
