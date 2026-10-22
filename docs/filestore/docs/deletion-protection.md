---
url: https://docs.cloud.google.com/filestore/docs/deletion-protection/
title: Prevent deletion of an instance \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:15.587583+00:00
---

# Prevent deletion of an instance  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/deletion-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Prevent deletion of an instance Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to help prevent the accidental deletion of existing or new Filestore instances.

## Overview

You can set the deletion protection option when you create an instance or update this option on an existing instance. In both cases, deletion is prevented at the instance level.

### Plan for deletion

If you are planning to delete an instance, complete the following steps:

  * Confirm that it is safe to delete the instance.
  * Confirm that deletion protection is deactivated. If necessary, edit the instance to deactivate deletion protection.



### Limitations

Deletion protection doesn't prevent the following operations:

  * Editing an instance
  * Deleting a backup
  * Reverting a snapshot
  * Deleting a file



## Set deletion protection on a new instance

This section shows you how to set the deletion protection option when creating a new instance. By default, the feature is deactivated.

If deletion protection is enabled, an attempt to delete the instance fails.

###  Google Cloud console 

  1. In the Google Cloud console, go to the Filestore **Instances** page.



[Go to the Filestore **Instances** page](https://console.cloud.google.com/filestore/instances)

  1. Click **Create Instance**.
  2. Follow the instructions noted in [Create an instance](https://docs.cloud.google.com/filestore/docs/creating-instances#google-cloud-console). Before clicking **Create** , add the following specifications: 
     1. In the **Tags** section, expand the **Advanced options** section.
     2. In the **Deletion protection** section, select the **Enable deletion protection** checkbox. We recommend stating the reason for enabling deletion protection to provide more context.
  3. Click **Create**.



###  gcloud 

  1. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs).

If you already have the gcloud CLI installed, update it:
         
         gcloud components update
         

  2. Run the [`gcloud filestore instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/filestore/instances/create) command to create a Filestore instance. Follow the instructions noted in [Create an instance](https://docs.cloud.google.com/filestore/docs/creating-instances#gcloud). Before you press `Enter`, add the following options:
         
         --deletion-protection \
         --deletion-protection-reason=PROTECTION_REASON
         

Where:

     * `--deletion-protection` is the flag used to enable deletion protection when creating the instance.
     * `--deletion-protection-reason` is the flag used to add a description of the justification for the instance's deletion protection setting you chose. PROTECTION_REASON is the description text you want to use. For example, "All genomics data must adhere to current organization policies." For more information, see [Deletion protection](https://docs.cloud.google.com/filestore/docs/deletion-protection).



###  REST API 

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [Filestore API](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/create). Follow the instructions noted in [Create an instance](https://docs.cloud.google.com/filestore/docs/creating-instances#api-create), adding the following options before running the command:
         
         "deletionProtectionEnabled",
             "deletionProtectionReason":"PROTECTION_REASON"
         

Where:

     * `deletionProtectionEnabled` is the flag used to enable deletion protection when creating the instance.
     * `deletionProtectionReason` is the flag used to add a description of the justification for the instance's deletion protection setting you chose. PROTECTION_REASON is the description text you want to use. For example, "All genomics data must adhere to current organization policies." For more information, see [Deletion protection](https://docs.cloud.google.com/filestore/docs/deletion-protection).



## Set or remove deletion protection on an existing instance

This section shows you how to edit the deletion protection option on an instance. By default, the feature is deactivated.

If you enable the option, a subsequent attempt to delete the instance fails.

###  Google Cloud console 

To edit Filestore instances using the Google Cloud console, navigate to the **Edit instance** page, where you can edit the instance description, manage IP-based access control rules, and scale the file share performance:

  1. In the Google Cloud console, go to the Filestore **Instances** page.

[Go to the Filestore Instances page](https://console.cloud.google.com/filestore/instances)

  2. Click the instance ID of the instance you want to edit.

  3. On the **Instance details** page, click **Edit** to go to the **Edit instance** page.

  4. In the **Deletion protection** section, select the **Enable deletion protection** checkbox. We recommend stating the reason for enabling deletion protection to provide more context.

  5. Click **Save**.




###  gcloud 

To enable deletion protection when you update an instance, use the [`gcloud filestore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/update) command similar to the following:
    
    
      gcloud filestore instances update INSTANCE_NAME \
          --deletion-protection \
          --deletion-protection-reason=PROTECTION_REASON
    

Where:

  * `INSTANCE_NAME` is the name of the instance you want to edit. For example, `my-genomics-instance`.
  * `PROTECTION_REASON` is the description text you want to use. For example, "All genomics data must adhere to current organization policies." For more information, see [Deletion protection](https://docs.cloud.google.com/filestore/docs/deletion-protection).



To deactivate deletion protection when you update an instance, use a command similar to the following:
    
    
      gcloud filestore instances update INSTANCE_NAME \
          --no-deletion-protection
    

Where:

  * `INSTANCE_NAME` is the name of the instance you want to edit. For example, `my-genomics-instance`.



Once deactivated, the `deletion-protection-reason` field is cleared.

###  REST API 

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [Filestore API](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/patch).

To set deletion protection on an instance, specify `true` in the `deletionProtectionEnabled` field. To remove it, specify `false` in the field. Use an operation call similar to the following:
         
         curl --request PATCH \
             'https://file.googleapis.com/v1/projects/PROJECT/locations/LOCATION/instances?instanceId=NAME?updateMask=deletionProtectionEnabled,deletionProtectionReason' \
             --header "Authorization: Bearer $(gcloud auth print-access-token)" \
             --header 'Accept: application/json' \
             --header 'Content-Type: application/json' \
             --data '{"tier":"TIER","networks":[{"network":"NETWORK"}],"fileShares":[{"capacityGb":CAPACITY,"name":"SHARE_NAME"}], "deletionProtectionEnabled": true, "deletionProtectionReason": "PROTECTION_REASON"}' \
             --compressed
         

Where:

     * `deletionProtectionEnabled` is the flag used to enable deletion protection. For example, `true` or `false`.
     * `deletionProtectionReason` is the flag used to add a description of the justification for the instance's deletion protection setting you chose. Only present when the feature is enabled. PROTECTION_REASON is the description text you want to use. For example, "All genomics data must adhere to current organization policies." For more information, see [Deletion protection](https://docs.cloud.google.com/filestore/docs/deletion-protection).



## What's next

  * [Create a new instance](https://docs.cloud.google.com/filestore/docs/creating-instances).
  * [What is a snapshot?](https://docs.cloud.google.com/filestore/docs/snapshots)
  * [What is a backup?](https://docs.cloud.google.com/filestore/docs/backups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
