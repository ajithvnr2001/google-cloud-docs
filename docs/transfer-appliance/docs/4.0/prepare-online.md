---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-online/
title: Prepare for online transfer \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:08.078469+00:00
---

# Prepare for online transfer  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-online/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)



Send feedback 

#  Prepare for online transfer Stay organized with collections  Save and categorize content based on your preferences. 

Online transfer requires setup for the first time you use it. Subsequent transfers after initial setup don't require these steps.

## Enable the APIs

To complete first-time setup for online transfer, a Google Cloud administrator must do the following:

  1. Enable the Google Storage Transfer API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=storagetransfer)

     1. Confirm the project you are enabling the API for, then click **Next**.

     2. Click **Enable**.

  2. Enable the Pub/Sub API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=pubsub)

     1. Confirm the project you are enabling the API for, then click **Next**.

     2. Click **Enable**.




## Configure the Storage Transfer Service service agent

In the email titled _Google Transfer Appliance Prepare Destination Bucket_ , a service agent is specified for you. It looks similar to the following example:
    
    
    project-IDENTIFIER@storage-transfer-service.gserviceaccount.com
    

Grant the following role to the Storage Transfer Service service agent [on your project](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#granting-console):

  * **`Pub/Sub Editor`**



Grant the following role to the Storage Transfer Service service agent [for the destination bucket](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add):

  * **`Storage Admin`**



## Create and configure a user-managed service account

  1. [Create a user-managed service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your project.

  2. Grant the following roles to the user-managed service account [on your project](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#granting-console):

     * **`Pub/Sub Editor`**
     * **`Storage Transfer Admin`**
     * **`Monitoring Metric Writer`** if you'll enable [Cloud Monitoring](https://docs.cloud.google.com/transfer-appliance/docs/4.0/monitor-appliance).
  3. Grant the following role to the user-managed service account [for the destination bucket](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add):

     * **`Storage Admin`**



Once the service account is configured, prepare a service account key:

  1. [Create a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#iam-service-account-keys-create-console) for the user-managed service account. The key is downloaded when you create it, and you cannot download it again.

  2. Rename the key to `key.json`, and save it to a safe location.

  3. Once you've received your appliance, upload `key.json` to the `/tmp` directory on the appliance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
