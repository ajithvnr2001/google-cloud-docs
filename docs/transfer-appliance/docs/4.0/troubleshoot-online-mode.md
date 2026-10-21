---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/troubleshoot-online-mode/
title: Troubleshoot online mode \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:13.703273+00:00
---

# Troubleshoot online mode  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/troubleshoot-online-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  Troubleshoot online mode Stay organized with collections  Save and categorize content based on your preferences. 

This article describes how to troubleshoot and potentially resolve issues with Transfer Appliance online mode.

## Not configured for online operations

**Error:**

`This appliance has not been configured for online operations.`

**Solution:**

If you ordered an online appliance and received this error, contact Transfer Appliance Team at [data-support@google.com](mailto:data-support@google.com).

If you ordered an offline appliance, this message is expected. Offline appliances do not support online mode. If you need further assistance, contact Transfer Appliance Team.

## Credential file is missing

**Error:**

`An error occurred while running hta containers: "credential file: '/tmp/key.json is missing"`

**Solution:**

Verify that you did the following items:

  * [Prepared IAM permissions and storage](https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-permissions).
  * [Created a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) for the user-managed service account.
  * Renamed the service account key to `key.json`
  * Uploaded the service account key to `/tmp` on the appliance.



## Failed to run containers binary

**Error:**

`An error occurred while running hta containers: "Failed to run HTA containers binary \"opt/ta_containers/ta_containers\": exit status 1"`

**Solution:**

Contact Transfer Appliance Team at [data-support@google.com](mailto:data-support@google.com) for assistance.

## Failed to update Operating System

**Error:**

`Failed to update Operating System. An error occurred while updating the appliance: "failed update OS: error transferring configuration files: error setting up tmp mount for new srv partition: error setting up mount /var/tmp/update1298680145: command [mount /dev/sdc2 /var/tmp/update1298680145] failed with output: mount: /var/tmp/update1298680145: special device /dev/sdc2 does not exist.\n and error: exit status 32"`

**Solution:**

Contact Transfer Appliance Team at [data-support@google.com](mailto:data-support@google.com) for assistance.

## Update cannot be run without credentials file

**Error:**

`Update cannot be run without credentials file. Please upload credentials file onto the appliance.`

This error occurs when trying to [update software](https://docs.cloud.google.com/transfer-appliance/docs/4.0/update-software) on the Transfer Appliance.

**Solution:**

Make sure that you've completed the following steps:

  * [Prepare IAM permissions and storage](https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-permissions).

  * [Prepare for online transfer](https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-online). Specifically, ensure that you have:

    * Created a user-managed service account.
    * Granted appropriate permissions to the service account.
    * Created a service account key for the user-managed service account.
    * Renamed the key to `key.json` and uploaded it to `/tmp` on the appliance.



## Object prefix does not update to nil string

**Error:**

This error occurs when you expect the object prefix to default to the nil string when running update destination bucket but it does not.

Updating without the object prefix specified:

`ta online --bucket=myrandombucket`

Running this command does not update the object prefix to the nil string since the object prefix only updates if you specify the `--object_prefix` flag.

**Solution:**

Update with at least the object prefix specified:

`ta online --bucket=myrandombucket --object_prefix=""`

`ta online --bucket=myrandombucket --object_prefix=`

`ta online --object_prefix=""`

`ta online --object_prefix=`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
