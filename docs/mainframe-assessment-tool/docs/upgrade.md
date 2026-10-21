---
url: https://docs.cloud.google.com/mainframe-assessment-tool/docs/upgrade/
title: Upgrade Mainframe Assessment Tool \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:38:08.424379+00:00
---

# Upgrade Mainframe Assessment Tool  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-assessment-tool/docs/upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Assessment Tool ](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview)



Send feedback 

#  Upgrade Mainframe Assessment Tool Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to upgrade Mainframe Assessment Tool.

## Limitations

  * Upgrade is only supported for VM deployments (not supported for Google Kubernetes Engine deployments).

  * Upgrade is only supported sequentially. You can upgrade only to the next immediate version and can't skip intermediate versions. For example, to upgrade from version 2.1.0 to 2.3.0, you must first upgrade to 2.2.0 and then upgrade to 2.3.0.




## Before you begin

  * Use Mainframe Assessment Tool version 2.1.0 or later. Earlier versions don't support upgrades.

  * Complete all in-progress assessments before you start the upgrade.

If you upgrade while an assessment is in progress, Mainframe Assessment Tool won't resume the assessment following the upgrade and the assessment can't be restarted. You must re-upload your application to restart the assessment. However, your previously completed assessments are preserved.

  * Confirm that you have superuser privileges on the Mainframe Assessment Tool VM instance to complete the upgrade.




## Upgrade Mainframe Assessment Tool

To upgrade Mainframe Assessment Tool, follow these steps:

  1. In the Google Cloud console, click ![Activate Shell Button](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell**.

[Go to the Google Cloud console](https://console.cloud.google.com/)

  2. To connect to the Mainframe Assessment Tool VM, run the following command:
         
         gcloud compute ssh VM_NAME --tunnel-through-iap
         

Replace VM_NAME with the name of the Mainframe Assessment Tool VM.

  3. In the Mainframe Assessment Tool VM's command-line interface, to change your privileges to superuser, run the following command:
         
         sudo su
         

  4. To download the upgrade script, run the following command:
         
         gcloud storage cp "gs://mainframe-ai-release/mat/VM_IMAGE_NAME/upgrade" DESTINATION_DIRECTORY
         

Replace the following:

     * VM_IMAGE_NAME: the name of the VM image that you want to upgrade to. For example, `mainframe-assessment-2-2-0`.
     * DESTINATION_DIRECTORY: the directory in your Mainframe Assessment Tool VM where you want to download the upgrade script.
  5. To make the script executable, run the following command:
         
         chmod +x DESTINATION_DIRECTORY/upgrade
         

Replace DESTINATION_DIRECTORY with the directory in your Mainframe Assessment Tool VM

  6. To start the upgrade, run the following command:
         
         DESTINATION_DIRECTORY/upgrade VERSION us-docker.pkg.dev/migrate-modernize-public/mainframe-assessment-prod
         

Replace the following:

     * DESTINATION_DIRECTORY: the directory in your Mainframe Assessment Tool VM where you have downloaded the upgrade script.
     * VERSION: the Mainframe Assessment Tool version that you want to upgrade to. The version must be in `mainframe-assessment-x-y-z` format; example: `mainframe-assessment-2-2-0`.
  7. To confirm the upgrade, on the **Admin & Settings** page, refresh the page and check the **Version**.




## What's next

  * Learn how to [configure settings for Mainframe Assessment Tool](https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-settings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
