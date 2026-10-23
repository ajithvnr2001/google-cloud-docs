---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/support/support-cluster-snapshot/
title: Share snapshots with Google Support \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:27.362241+00:00
---

# Share snapshots with Google Support  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/support/support-cluster-snapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Share snapshots with Google Support Stay organized with collections  Save and categorize content based on your preferences. 

If you have a problem with registered clusters outside Google Cloud that you can't resolve yourself, you may be asked to create a snapshot of your cluster and share it with the team. For example, these clusters could be on bare metal, VMware, or attached clusters.

This document tells you how to share this information with Google Cloud Support.

For more information about support, see:

  * [Get support for clusters on bare metal](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support)
  * [Get support for clusters on VMware](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support)



## Allow Google Cloud Support to view your uploaded cluster snapshot

For some support cases, you might need to take a snapshot of the affected cluster for the Google Cloud Support team. Instead of emailing the snapshot, you can upload the file to a Cloud Storage bucket and share access to the bucket with the team. To grant access to a storage bucket, review the required permissions specified in [Identity and Access Management permissions for `gcloud storage` commands](https://docs.cloud.google.com/storage/docs/access-control/iam-gcloud).

### Create cluster snapshot

The process for creating a snapshot depends on your cluster type:

  * **GKE on AWS (previous generation)** : Follow the instructions in [Create a snapshot](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws/previous-generation/troubleshooting#snapshots)
  * **Google Distributed Cloud deployments on VMware** : Follow the instructions in [Upload snapshots to a Cloud Storage bucket](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/diagnose#upload_snapshots_to_a_bucket) to create a cluster snapshot and upload the cluster snapshot to a Cloud Storage bucket. Note the location of the snapshot in the output.
  * **Google Distributed Cloud deployments on bare metal** : Follow the instructions in [How to create a default snapshot](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/bmctl-snapshot) to create a cluster snapshot and upload the cluster snapshot to a Cloud Storage bucket. These instructions also show you how to grant Google Cloud Support access to the bucket.
  * **Attached clusters** : Use [this script](https://github.com/GoogleCloudPlatform/anthos-samples/blob/master/troubleshooting/create_snapshot.py) as a reference to create a snapshot.



### Create a Google Cloud service account

Create a dedicated Google Cloud service account to be used by the support team. You do this by running the following command:

**Note:** With release 1.15.0 and higher of Google Distributed Cloud, the following command isn't needed. The command to create and upload a snapshot automatically provisions the service account for sharing access to your uploaded snapshot.
    
    
    gcloud services enable connectgateway.googleapis.com --project=PROJECT_ID
    gcloud beta services identity create --service=connectgateway.googleapis.com --project=PROJECT_ID

...where:

  * PROJECT_ID is the Project ID of the cluster snapshot's storage bucket.



### Share access with Google Cloud Support

Grant read-only access of the bucket's storage object to the dedicated Google Cloud service account used by the support team for your case. You do this by running the following command:

#### Google Distributed Cloud on bare metal release 1.15.0 and higher

To share access with Google Support, use the following command:
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-anthossupport.iam.gserviceaccount.com \
        --role=roles/storage.objectViewer
    

Replace BUCKET_NAME with the name of the bucket into which your snapshot was uploaded. By default, the bucket name starts with `anthos-snapshot-`.

To revoke access to your bucket:
    
    
    gcloud storage buckets remove-iam-policy-binding gs://BUCKET_NAME \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-anthossupport.iam.gserviceaccount.com \
        --role=roles/storage.objectViewer
    

#### Google Distributed Cloud on VMware release 1.15.0 and higher

As described in [Upload snapshots to a Cloud Storage bucket](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/diagnose#upload_snapshots_to_a_bucket), when you create a snapshot with the `--share-with` flag, it is automatically shared with Google Support. No additional command is needed.

#### Manually share access to an uploaded snapshot
    
    
    gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME/CLUSTER_NAME/SNAPSHOT_FILE_NAME \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-anthossupport.iam.gserviceaccount.com \
        --role=roles/storage.legacyObjectReader

...where:

  * BUCKET_NAME/CLUSTER_NAME/SNAPSHOT_FILE_NAME is the snapshot location you noted when you created the cluster snapshot.
  * PROJECT_NUMBER is your project's ID number, used to create an identifier for the support case service account. You can get this value in the Google Cloud console by visiting the [IAM and Admin settings page](https://console.cloud.google.com/iam-admin/settings).



After the support case is closed, Google will disable the service account. If you want to revoke Google's permission to access your Cloud Storage bucket, run the following command:
    
    
    gcloud storage buckets remove-iam-policy-binding gs://BUCKET_NAME/CLUSTER_NAME/SNAPSHOT_FILE_NAME \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-anthossupport.iam.gserviceaccount.com \
        --role=roles/storage.legacyObjectReader

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
