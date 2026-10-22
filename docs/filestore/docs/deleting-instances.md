---
url: https://docs.cloud.google.com/filestore/docs/deleting-instances/
title: Delete instances \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:00.139207+00:00
---

# Delete instances  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/deleting-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Delete instances Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to delete a Filestore instance.

## Delete an instance

**Caution:** Deleting a Filestore instance deletes all data on that instance. Once an instance is deleted, the data stored in the instance is not recoverable.

Before deleting a Filestore instance, unmount it from client VMs first. Not doing so causes file operations to stop responding.

###  Google Cloud console 

  1. In the Google Cloud console, go to the Filestore Instances page.

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

  2. Click the Filestore instance ID to open the instance details page.

  3. Click **Delete** _delete_.

  4. When prompted, type the instance ID.

  5. Click **Delete**.




###  gcloud 

#### Before you begin

To use the gcloud CLI, you must either [install the gcloud CLI](https://docs.cloud.google.com/sdk/downloads) or use the Cloud Shell that's built into the Google Cloud console:

[Go to the Google Cloud console](https://console.cloud.google.com/)

You can delete a Filestore instance by running the [`instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/delete) command:
    
    
      gcloud filestore instances delete instance-id \
      --project="project-id" \
      --zone=zone
      --force
    

where:

  * instance-id is the instance ID of the Filestore instance you want to delete.
  * project-id is the project ID of the Google Cloud project that contains the Filestore instance. You can skip this flag if the Filestore instance is in the `gcloud` default project. You can set the default project by running the [`config set project`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) command:
        
        gcloud config set project project-id
        

  * zone is the zone where the Filestore instance resides. Run the `gcloud filestore zones list` command to get a list of supported zones. You can skip this flag if the Filestore instance is in the `gcloud` default zone. You can set the default zone by running the [`config set filestore/zone`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) command:
        
        gcloud config set filestore/zone zone
        

  * `--force` Optional. Use this flag with the command to delete the Filestore instance and any associated snapshots.




### REST API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [Filestore API](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/delete):
         
         curl -s \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           --header "Content-Type: application/json" \
           --request DELETE "https://file.googleapis.com/v1/projects/PROJECT/locations/LOCATION/instances/INSTANCE_NAME"

Where:

     * `PROJECT` is the name of the project where your instance is located. For example, `my-genomics-project`.
     * `LOCATION` is the location where your instance resides. For example, `us-west1-a`.
     * `INSTANCE_NAME` is the name of the instance you want to delete. For example, `my-genomics-instance`.



[Zonal with a higher capacity range (previously high scale SSD)](https://docs.cloud.google.com/filestore/docs/service-tiers#high_scale_ssd_tier) tier instances can take up to 10 minutes to delete, depending on the instance size.

The Filestore quota is released when instance deletion completes but you are not be billed for the instance during this time.

### Delete instances that have snapshots

If you want to delete a zonal, regional, or enterprise instance that contains snapshots, you must complete either of the following tasks:

  * Delete the instance's snapshots before deleting the instance.
  * Include the `--force` flag in the `gcloud filestore instances delete` command.



The Google Cloud console allows for the deletion of instances containing snapshots and automatically deletes the snapshots.

## What's next

  * [Create a different instance](https://docs.cloud.google.com/filestore/docs/creating-instances).
  * [What is a snapshot?](https://docs.cloud.google.com/filestore/docs/snapshots)
  * [What is a backup?](https://docs.cloud.google.com/filestore/docs/backups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
