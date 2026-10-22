---
url: https://docs.cloud.google.com/code/docs/shell/manage-vms/
title: Manage VMs in Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:08.670663+00:00
---

# Manage VMs in Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/manage-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Manage VMs in Cloud Code for Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

With Cloud Code's Compute Engine integration, you can view the Compute Engine VMs running your applications, establish connections to your VMs using SSH, view application logs, and upload files to a VM.

This document shows you how to access Compute Engine with Cloud Code in your IDE and manage your VM instances.

## View VMs

To view VMs in your Google Cloud project and the VM instance details in the Google Cloud console, follow these steps:

  1. Launch the [Cloud Shell Editor](https://shell.cloud.google.com).

  2. Sign into Cloud Code if you haven't already, and select your Google Cloud project.

  3. To view VM instances in your Google Cloud project, in the activity bar of your IDE, click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Compute Engine** explorer.

  4. To view the VM instance details in the Google Cloud console, right-click the VM instance and select **Open in Cloud Console**.




## Connect to a VM

To connect to the VM instance in your IDE with Cloud Code using the built-in IDE terminal and SSH, follow these steps:

  1. To connect to a VM instance, in the **Compute Engine** explorer, hold the pointer over the VM instance and click terminal **Open SSH** or right-click the VM instance and select **Open SSH**.

A terminal appears, displaying information about the remote instance.

  2. If the connection to the VM instance fails:

     * For Windows and Linux users, see [Troubleshooting SSH errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors) for common errors that you might run into when connecting to a VM using SSH, ways to resolve errors, and methods for diagnosing failed SSH connections.

     * For macOS users, after pressing any key to clear the error message in the terminal, an error message dialog appears. To view information in the terminal about the issue and potential resolutions, click **Troubleshoot**. Or, to view the [Troubleshooting SSH errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors) documentation, click **Learn more**.




## View application logs on a VM

To view the application logs of a VM instance, follow these steps:

  1. To view the application logs of a VM instance in Cloud Code, right-click the VM instance and select **View Logs**.

The Logs Viewer window appears in your IDE, allowing you to filter by log type, time, severity, and instance.

  2. To view logs in real time, turn on the **Streaming** toggle.

  3. To view the logging page for a particular VM instance in the Google Cloud console, click open_in_new **Open in browser**.




## Upload a file to a VM

To copy application files from your local IDE to your remote VM instance, follow these steps:

**Note:** Cloud Code only supports [transferring files to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/transfer-files). For additional options for Windows machines, see [Transfer files to Windows VMs](https://docs.cloud.google.com/compute/docs/instances/transfer-files-windows).

  1. To upload a file to a VM, in the Cloud Code **Compute Engine** explorer, hold the pointer over the VM instance and click cloud_upload **Upload File via SCP** , or right-click the VM instance and select **Upload File via SCP**.

  2. Navigate to the file that you want to upload and click **Upload**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
