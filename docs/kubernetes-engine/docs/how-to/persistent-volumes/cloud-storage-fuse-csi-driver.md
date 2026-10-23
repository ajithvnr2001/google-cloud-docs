---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver/
title: Quickstart: Access Cloud Storage buckets with the FUSE CSI driver \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:11.353514+00:00
---

# Quickstart: Access Cloud Storage buckets with the FUSE CSI driver  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quickstart: Access Cloud Storage buckets with the FUSE CSI driver

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

In this quickstart guide, you learn how to access Cloud Storage buckets from within a Google Kubernetes Engine (GKE) application as if they were local file systems. This quickstart provides a sample Kubernetes manifest to create a Pod that mounts the bucket, and shows you how to interact with the bucket's contents using the Pod's file system.

This page is for Developers, Storage specialists, and anyone else who wants to provision and manage cloud resources, and deploy workloads. To learn more about common roles, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with [Kubernetes](https://kubernetes.io/) and [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver).

This quickstart uses the GKE Autopilot mode. If you want to use the Standard mode, see [Set up the Cloud Storage FUSE CSI driver for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#standard).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the GKE and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,storage.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the GKE and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,storage.googleapis.com)

  8. Make sure that you have the following role or roles on the project: Kubernetes Engine Admin, Storage Admin, Service Account User 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 



## Create a GKE Autopilot cluster

  1. In the Google Cloud console, go to the **Create an Autopilot cluster** page. 

[Go to Create an Autopilot cluster](https://console.cloud.google.com/kubernetes/auto/add)

  2. Under **Cluster basics** , do the following:

     1. In the **Name** field, enter a name for the cluster.

     2. Keep the default values for the rest of the settings.

  3. To create the cluster, click **Create**.




## Create a Cloud Storage bucket

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box **Create**.

  3. On the **Create a bucket** page, in the **Get started** section, do the following:

     1. Enter a globally unique name for your bucket that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).

     2. Keep the default values for the rest of the settings.

  4. To create the bucket, click **Create**.




## Upload objects to your Cloud Storage bucket

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you just created.

  3. In the **Objects** tab for the bucket, do either of the following:

     * Drag files from your desktop or file manager to the main pane in the Google Cloud console.

     * Click the **Upload Files** button. In the dialog that appears, select the files that you want to upload, and click **Open**.

**Note:** If you're using the Chrome browser, folder uploads are also supported.



## Configure access to your Cloud Storage bucket

To make sure your Cloud Storage bucket is accessible by your GKE cluster, follow the steps in [Configure access to Cloud Storage buckets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#authentication).

## Set up Cloud Shell

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

A [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. It can take a few seconds for the session to initialize.

## Deploy a Pod to access your Cloud Storage bucket by using FUSE

**Note:** To optimize your configuration, see [Optimize Cloud Storage Cloud Storage FUSE CSI driver for GKE performance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf).

  1. Set the default project where you want to deploy the Pod:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with your project ID.

  2. Create and apply the Pod manifest with the following content:
         
         cat << EOF | kubectl apply -f -
         apiVersion: v1
         kind: Pod
         metadata:
           name: gcsfuse-test
           namespace: default
           annotations:
             gke-gcsfuse/volumes: "true"
         spec:
           terminationGracePeriodSeconds: 60
           containers:
           - image: busybox
             name: busybox
             command: ["sleep"]
             args: ["infinity"]
             volumeMounts:
             - name: gcsfuse-test
               mountPath: /data
               readOnly: true
           serviceAccountName: default
           volumes:
           - name: gcsfuse-test
             csi:
               driver: gcsfuse.csi.storage.gke.io
               volumeAttributes:
                 bucketName: BUCKET_NAME
                 mountOptions: "implicit-dirs"
         EOF
         

     * Replace `BUCKET_NAME` with your Cloud Storage bucket name.
     * If you're using a different namespace or a service account, replace the `namespace` and `serviceAccountName` fields accordingly.

The content of this manifest starts a Pod called `gcsfuse-test` that mounts the bucket on its `/data` path.

  3. Verify that the Pod is running:
         
         kubectl get pod gcsfuse-test
         

The output is similar to the following:
         
         NAME           READY   STATUS    RESTARTS   AGE
         gcsfuse-test   2/2     Running   0          12s
         

The Cloud Storage FUSE CSI driver [attaches a sidecar container](https://kubernetes.io/blog/2023/08/25/native-sidecar-containers/) in your Pod to manage interactions with Cloud Storage.

If the Pod isn't running, you can fetch the event logs to help you diagnose the issue by running the `kubectl describe pod gcsfuse-test` command. For more information, see [Troubleshooting](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/docs/troubleshooting.md#pod-event-warnings) on GitHub.

  4. After the Pod is running, you can explore its file system:
         
         kubectl exec -it gcsfuse-test -- find /data
         

**Success:** You've successfully accessed your Cloud Storage bucket as a local file system!



## Clean up

To avoid incurring charges to your Google Cloud account for the resources that you used in this tutorial, delete the Pod:
    
    
    kubectl delete pod gcsfuse-test
    

## What's next

  * [Learn how the Cloud Storage FUSE CSI driver for GKE works](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver).
  * [Learn more about the capabilities of Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview).
  * [Troubleshoot Cloud Storage FUSE ](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/docs/troubleshooting.md).
  * [Automatically optimize performance with Cloud Storage FUSE profiles](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gcsfuse-profiles).
  * [Manually optimize Cloud Storage FUSE for performance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
