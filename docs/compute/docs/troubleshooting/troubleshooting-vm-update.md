---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-update/
title: Troubleshoot VM updates \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:07.506811+00:00
---

# Troubleshoot VM updates  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot VM updates Stay organized with collections  Save and categorize content based on your preferences. 

This document provides solutions to common issues you might encounter when updating a Compute Engine VM instance. For general instructions on how to update a VM, see [Update instance properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties).

## Best practices

To avoid common issues when updating a VM, follow these best practices:

  * Use the `update-from-file` workflow: Export the instance configuration to a file, modify the file, and then use the `gcloud compute instances update-from-file` command to apply the changes. This approach helps prevent errors from manual commands.

  * Use the `most-disruptive-allowed-action` flag: This flag prevents accidental restarts. Set it to `NO_EFFECT` to test your changes, `REFRESH` for non-disruptive updates, and `RESTART` only when you are sure a restart is acceptable.




## Common issues

This section lists errors you might encounter when updating a VM and provides guidance on how to resolve them.

### Metadata fingerprint mismatch

This error occurs when you try to update a VM instance, but the VM's metadata was updated by another process since you last refreshed the page or fetched the instance data.

**Error message** :
    
    
    Supplied fingerprint does not match current metadata fingerprint
    

**Resolution** :

The instance fingerprint property in your request must match the current fingerprint of the instance to prevent simultaneous update requests from overwriting each other. Try the following:

  * Refresh the page: If you're using the Google Cloud console, refresh the VM instance **Details** page before making your changes.

  * Use the `--no-etag-cache` Google Cloud CLI flag: If you're using the Google Cloud CLI, use the `--no-etag-cache` flag with your `gcloud compute instances update` command.

  * Retry after a few minutes: As a last resort, try stopping the VM, waiting a few minutes, and then attempt to make the change again.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
