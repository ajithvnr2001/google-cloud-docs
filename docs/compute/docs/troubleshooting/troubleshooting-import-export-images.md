---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-import-export-images/
title: Troubleshooting image import and export \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:30.823963+00:00
---

# Troubleshooting image import and export  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-import-export-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting image import and export Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes the common issues that you might encounter when you import images to Compute Engine and when you export images to Cloud Storage. 

## Diagnose image import and export issues

Diagnose the cause of image import or export issues by reviewing the Cloud Build logs and the serial port output of the temporary VMs (or worker VMs).

### Review Cloud Build logs

The image import tool uses the Cloud Build API to import and export images. Review the Cloud Build logs to get the status of the running process.

To view Cloud Build logs, do one of the following:

  * If you import or export images by using Google Cloud console, view logs on the **Images** page in the Google Cloud console, in the **Image import history** or **Image export history** tab. Click the Cloud Build ID to view the logs.

[Go to Images](https://console.cloud.google.com/compute/images)

  * If you import or export images by using Google Cloud CLI, you can view the Cloud Build log location at the standard output after running the process.




### Review serial port output

Reviewing the serial port output of the worker VMs that are created during the image import or export process might be useful to troubleshoot issues with system-level entities. For more information about these logs, see [Viewing serial port output](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output).

## Common errors

The following are examples of common errors you might encounter when you import or export images.

### ExportFailed error when exporting images larger than 2 TB

The maximum size for images in `vmdk`, `vpc`, and `vhd` formats is limited to 2 TB. Therefore, when you export images larger than 2 TB in these formats, you might see an error message similar to the following in the log:

**Error message** :
    
    
    [image -export]: 2022 - 01 - 27T16: 08: 24Z Error running workflow: step
    "image-export-export-disk" run error: step "wait-for-inst-image-export-export-disk"
    run error: WaitForInstancesSignal FailureMatch found for
    "WORKER_VM_NAME--SUFFIX":
    "ExportFailed: Failed to export disk source to DESTINATION_URI"

**Resolution** :

To resolve this issue, specify the image format as `vdi`, `vhdx`, or `qcow2` and set the `--timeout` value as `24h` when you run the [`gcloud compute images export` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/export).

If the issue persists, contact [Google Cloud Support](https://docs.cloud.google.com/support) for assistance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
