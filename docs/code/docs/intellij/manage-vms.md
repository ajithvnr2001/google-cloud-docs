---
url: https://docs.cloud.google.com/code/docs/intellij/manage-vms/
title: Manage VMs in Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:06.852261+00:00
---

# Manage VMs in Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/manage-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Manage VMs in Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

With Cloud Code's Compute Engine integration, you can view the Compute Engine VMs running your applications, establish connections to your VMs using SSH, view application logs, and upload files to a VM.

This document shows you how to access Compute Engine with Cloud Code in your IDE and manage your VM instances.

## View VMs

To view VMs in your Google Cloud project and the VM instance details in the Google Cloud console, follow these steps:

  1. Click the **Compute Engine** tab or select **View > Tool Windows > Compute Engine**.

![Compute Engine tab in IntelliJ](https://docs.cloud.google.com/static/code/docs/intellij/images/compute-engine-tab-intellij.png)

  2. If you haven't selected a Google Cloud project, click **Select a Google Cloud Project** , select a project, and then click **OK**.

  3. To view your VM instances, expand the **All VM Instances** snippet.

  4. To view the VM instance details in the Google Cloud console, right-click the VM instance and select **Open in Cloud Console**.




### Add and view favorite VMs

IntelliJ supports _favorite VM instances_ per Google Cloud project, which are retained between VM restarts. To add VMs to your favorites list and to view the list, follow these steps:

  1. In the **Compute Engine** tab, under the **All VM Instances** snippet, right-click a VM instance and select **Add to Favorites**.

  2. To view your favorites list, expand the **Favorite VM Instances** snippet.

  3. To remove a VM from your favorites list, right-click the VM and select **Remove from Favorites**.




## Connect to a VM

To connect to the VM instance in your IDE with Cloud Code using the built-in IDE terminal and SSH, follow these steps:

  1. To connect to a VM instance, right-click the VM instance and select **Open SSH connection**.

A terminal appears, displaying information about the remote instance.

  2. If the connection to the VM instance fails, an error message dialog appears. To view information in the terminal about the issue and potential resolutions, click **Troubleshoot in terminal**. Or, to view [Troubleshooting SSH errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh) documentation, click **View troubleshooting guide**.




## View application logs on a VM

To view the application logs of a VM instance in your IDE, right-click the VM instance and select **View Logs Explorer**. This takes you to the Logs Explorer in the Google Cloud console.

## Upload a file to a VM

To copy application files from your local IDE to your remote VM instance, follow these steps:

**Note:** Cloud Code only supports [transferring files to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/transfer-files). For additional options for Windows machines, see [Transfer files to Windows VMs](https://docs.cloud.google.com/compute/docs/instances/transfer-files-windows).

  1. To upload a file to a VM, select a VM instance and at the top of the **Compute Engine** pane, click cloud_upload **Upload** , or right-click the VM instance and select **Upload a file/directory**.

  2. Navigate to the file that you want to upload and click **Open**. A terminal opens with the list of files and progress of the upload.

  3. If the upload fails, the **SSH Connectivity Troubleshooting** dialog appears. Choose an option to click:

     * **View file transfer guide** : Opens [Transferring files to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/transfer-files) for more information on transferring files to Compute Engine VM instances.
     * **Troubleshoot in terminal** : Displays information in the terminal about the issue and potential resolutions.
     * **View troubleshooting guide** : Opens [Troubleshooting SSH errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh) for more information about common errors that you might run into when connecting to a VM using SSH, ways to resolve errors, and methods for diagnosing failed SSH connections.



## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
