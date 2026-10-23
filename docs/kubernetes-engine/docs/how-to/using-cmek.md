---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek/
title: Use customer-managed encryption keys (CMEK) \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:03.727560+00:00
---

# Use customer-managed encryption keys (CMEK)  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Use customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes how to use Customer Managed Encryption Keys (CMEK) on Google Kubernetes Engine (GKE). If you need to control management of your keys, you can use [Cloud Key Management Service](https://docs.cloud.google.com/kms) and CMEK to protect attached Persistent Disks and [custom boot disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-boot-disks) in your GKE cluster.

## Overview

By default, Google Cloud [encrypts customer content at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption), and GKE manages encryption for you without any action on your part.

If you want to control and manage encryption key rotation yourself, you can use CMEK. These keys encrypt the data encryption keys that encrypt your data. For more information, see [Key management](https://docs.cloud.google.com/docs/security/encryption/default-encryption#key_management).

You can also encrypt secrets in your cluster using keys that you manage. For details, see [Application-layer secrets encryption](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets).

In GKE, CMEK can protect data of two types of storage disks: node boot disks and attached disks.

Node boot disks
    Node boot disks are part of your cluster's node pools. You can create a CMEK-encrypted node boot disk when you create clusters and node pools.
Attached disks
    Attached disks are PersistentVolumes used by Pods for durable storage. CMEK-encrypted attached persistent disks are available in GKE as a [dynamically provisioned PersistentVolume](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#dynamic_provisioning).

To learn more about storage disks, see [Storage options](https://docs.cloud.google.com/compute/docs/disks). Control plane disks, used for GKE control planes, cannot be protected with CMEK.

## Before you begin

  1. To do the exercises in this topic, you need two Google Cloud projects:

     * **Key project:** This is where you create an encryption key.

     * **Cluster project:** This is where you create a cluster that enables CMEK.

**Note:** You can use the same project for your key project and cluster project. But the recommended practice is to use [separate projects](https://docs.cloud.google.com/kms/docs/separation-of-duties).
  2. In your key project, ensure that you have enabled the Cloud KMS API.

[Enable Cloud KMS API](https://console.cloud.google.com/apis/library/cloudkms.googleapis.com)

  3. In your **key project** , the user who creates the key ring and key needs the following IAM permissions:

     * `cloudkms.keyRings.getIamPolicy`
     * `cloudkms.keyRings.setIamPolicy`

These permissions are granted to the predefined `roles/cloudkms.admin` [Identity and Access Management role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.admin). You can learn more about [granting permissions to manage keys](https://docs.cloud.google.com/kms/docs/iam) in the Cloud KMS documentation.

  4. In your **cluster project** , ensure that you have enabled the Cloud KMS API.

[Enable Cloud KMS API](https://console.cloud.google.com/apis/library/cloudkms.googleapis.com)

  5. Ensure that you have installed the [gcloud CLI](https://docs.cloud.google.com/sdk/downloads).

  6. Update `gcloud` to the latest version:
         
         gcloud components update
         




## Create a Cloud KMS key

Before you can protect your node boot disk or attached disk with a CMEK, you need a Cloud KMS [key ring and key](https://docs.cloud.google.com/kms/docs/object-hierarchy).

Your key ring and key have the following requirements:

  * Your key should use symmetric encryption.

  * You need to grant the GKE service account permissions to use the key.

  * Your key ring must have a location that matches the location of your GKE cluster:

    * A [zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#zonal_clusters) should use a key ring from a superset location. For example, a cluster in the `us-central1-a` zone can only use a key in the `us-central1` region.

    * A [regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters) should use a key ring from the same location. For example, a cluster in the `asia-northeast1` region should be protected with a key ring from the `asia-northeast1` region.

    * The Cloud KMS `global` region is not supported for use with GKE.




For instructions on how to create a key ring and key, see [Creating symmetric keys](https://docs.cloud.google.com/kms/docs/creating-keys).

### Grant permission to use the key

You must grant the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) IAM role on the Cloud KMS key to the [Compute Engine service agent](https://docs.cloud.google.com/iam/docs/service-agents#compute-engine-service-agent) in your cluster project. Granting this role allows GKE Persistent Disks to access and use your encryption key.

**Note:** For CMEK-protected node boot disks and CMEK-protected attached disks, this Compute Engine service agent requires the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role even if you use a custom IAM service account on your nodes.

To grant the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role to the Compute Engine service agent, select one of the following options:

### gcloud

Run the following command:
    
    
    gcloud kms keys add-iam-policy-binding KEY_NAME \
        --location LOCATION \
        --keyring RING_NAME \
        --member serviceAccount:service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com \
        --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
        --project KEY_PROJECT_ID
    

Replace the following:

  * `KEY_NAME`: the name of your key.
  * `LOCATION`: the region where you created your key ring.
  * `RING_NAME`: the name of your key ring.
  * `PROJECT_NUMBER`: your cluster's project number.
  * `KEY_PROJECT_ID`: your key project ID.



### Console

  1. In the Google Cloud console, go to the **Key management** page. 

[Go to Key management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring that contains the key.

  3. Click the name of the key that you want to modify.

  4. Click the **Permissions** tab.

  5. Click person_add **Grant access**. The **Grant access to key** pane opens.

  6. In the **New principals** field, enter the name of the Compute Engine service agent:
         
         service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com
         

Replace `PROJECT_NUMBER` with your cluster's project number.

  7. In the **Select a role** menu, select **Cloud KMS CryptoKey Encrypter/Decrypter**.

  8. Click **Save**.




## Use CMEK-protected node boot disks

In this section, you create a new cluster or node pool with a CMEK protected boot disk.

You cannot enable customer-managed encryption for node boot disks on an existing cluster, as you cannot change the boot disk type of an existing cluster or node pool. However, you can create a new node pool for your cluster with customer- managed encryption enabled, and delete the previous node pool.

You also cannot disable customer-managed encryption for node boot disks on an existing cluster or an existing node pool. However, you can create a new node pool for your cluster with customer-managed encryption disabled, and delete the previous node pool.

### Create a cluster with a CMEK-protected node boot disk

You can create a cluster with a CMEK-protected node boot disk using the gcloud CLI or the Google Cloud console.

For Standard clusters, only a standard persistent disk (`pd-standard`) or an SSD persistent disk (`pd-ssd`) can be encrypted with a CMEK key.

### gcloud

To create a cluster whose boot disk is encrypted with a CMEK key, specify a value for the `--boot-disk-kms-key` parameter in your cluster creation command.

**Create a Standard cluster**

To create a Standard cluster whose boot disk is encrypted with a CMEK key, use the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --cluster-version=latest \
        --location CONTROL_PLANE_LOCATION \
        --boot-disk-kms-key projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME \
        --project CLUSTER_PROJECT_ID \
        --disk-type DISK_TYPE
    

**Create an Autopilot cluster**

To create an Autopilot cluster whose boot disk is encrypted with a CMEK key, use the following command:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --cluster-version=latest \
        --location CONTROL_PLANE_LOCATION \
        --boot-disk-kms-key projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME \
        --project CLUSTER_PROJECT_ID
    

Replace the following:

  * `CLUSTER_NAME`: the name for your new cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional Standard and Autopilotclusters, or a zone for zonal Standard clusters.
  * `KEY_PROJECT_ID`: your key project ID.
  * `LOCATION`: the location of your key ring.
  * `RING_NAME`: the name of your key ring.
  * `KEY_NAME`: the name of your key.
  * `CLUSTER_PROJECT_ID` is your cluster project ID.
  * `DISK_TYPE`: `pd-standard` (default) or `pd-ssd`.



### Console

**Create a Standard cluster**

To create a Standard cluster whose boot disk is encrypted with a CMEK key, perform the following steps:

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. Configure your cluster as desired.
  3. From the navigation pane, under **Node Pools** , click **Nodes**.
  4. In the **Boot disk type** drop-down list, select **Standard persistent disk** or **SSD Persistent Disk**.
  5. Select the **Enable customer-managed encryption for Boot Disk** checkbox and choose the Cloud KMS encryption key you created earlier.
  6. Click **Create**.



**Create an Autopilot cluster**

To create an Autopilot cluster whose boot disk is encrypted with a CMEK key, perform the following steps:

  1. In the Google Cloud console, go to the **Create an Autopilot cluster** page. 

[Go to Create an Autopilot cluster](https://console.cloud.google.com/kubernetes/auto/add)

  2. Configure your cluster as desired.
  3. Expand the **Advanced Options** section and locate the **Security** options.
  4. Select the **Enable customer-managed encryption for Boot Disk** checkbox and choose the Cloud KMS encryption key you created earlier.
  5. Click **Create**.



### Create a new node pool with CMEK-protected node boot disks

**Note:** This section applies only to Standard clusters. Nodes and node pools in Autopilot clusters are fully-managed by Google.

To create a new node pool with CMEK enabled on an existing standard cluster, you can use the gcloud CLI or the Google Cloud console.

### gcloud

To create a node pool with customer-managed encryption for node boot disks, specify a value for the `--boot-disk-kms-key` parameter in your creation command.
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --location CONTROL_PLANE_LOCATION \
        --disk-type DISK_TYPE \
        --boot-disk-kms-key projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME \
        --project CLUSTER_PROJECT_ID \
        --cluster CLUSTER_NAME
    

Replace the following:

  * `NODE_POOL_NAME`: the name you choose for your node pool.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `DISK_TYPE`: `pd-standard` (default) or `pd-ssd`.
  * `KEY_PROJECT_ID`:your key project ID.
  * `LOCATION`: the location of your key ring.
  * `RING_NAME`: the name of your key ring.
  * `KEY_NAME`: the name of your key.
  * `CLUSTER_PROJECT_ID`: your cluster project ID.
  * `CLUSTER_NAME`: the name of the Standard cluster you created in the previous step.



### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Click **Create user-managed node pool**.

  5. From the navigation pane, click **Nodes**.

  6. In the **Machine Configuration** section, ensure **Boot disk type** is either **Standard persistent disk** or **SSD persistent disk**.

  7. Select the **Enable customer-managed encryption for boot disk** checkbox and select the Cloud KMS encryption key you created.

  8. Click **Create**.




## Use CMEK-protected Filestore instances or Persistent Disks

The following information covers how to encrypt newly created Filestore instances or Persistent Disks. You can enable CMEK on a new or existing cluster, using a new or existing Cloud KMS key.

These instructions need to be completed once per GKE cluster:

  * Create a GKE cluster, if you don't already have one available.
  * Deploy the [Filestore CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver) or [Compute Engine Persistent Disk CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gce-pd-csi-driver) to your cluster.
  * Create a Cloud KMS [key ring and key version](https://docs.cloud.google.com/kms/docs/object-hierarchy), if you don't already have one available.
  * [Grant key access permissions to the Filestore service account](https://docs.cloud.google.com/filestore/docs/cmek#grant_key_access_permission_to_the_service_account).
  * Create a [StorageClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#storageclasses) that enables disks provisioned by Kubernetes to automatically be encrypted with that Cloud KMS key. For details on how to do this, see the following section.

**Note:** For CMEK encryption of Filestore instances, your cluster must run GKE 1.21 or higher. CMEK encryption of Filestore instances is only supported for the [Enterprise and High Scale SSD (preview) tiers](https://docs.cloud.google.com/filestore/docs/cmek#supported_tiers).**Caution:** CMEK encryption on Filestore instances cannot be removed.

### Create a StorageClass referencing the Cloud KMS key

  1. Copy the content below into a YAML file named `cmek-sc.yaml`. This configuration enables dynamic provisioning of encrypted volumes.

###  Filestore instances 
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: csi-filestore-cmek
         provisioner: filestore.csi.storage.gke.io
         allowVolumeExpansion: true
         parameters:
           tier: enterprise
           instance-encryption-kms-key: projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME
         

     * The `instance-encryption-kms-key` field must be the [fully qualified resource identifier](https://docs.cloud.google.com/kms/docs/object-hierarchy#key) for the key that will be used to encrypt new Filestore instances.
     * The values in `instance-encryption-kms-key` are case sensitive (for example: `keyRings` and `cryptoKeys`). Provisioning a new volume with incorrect values results in an `invalidResourceUsage` error.
     * You cannot add the `instance-encryption-kms-key` parameter to an existing `StorageClass` object. However, you can delete the `StorageClass` object and recreate it with the same name, but a different set of parameters.

###  Persistent Disks 
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: csi-gce-pd-cmek
    provisioner: pd.csi.storage.gke.io
    volumeBindingMode: "WaitForFirstConsumer"
    allowVolumeExpansion: true
    parameters:
      type: pd-standard
      disk-encryption-kms-key: projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME
    

     * The `disk-encryption-kms-key` field must be the [fully qualified resource identifier](https://docs.cloud.google.com/kms/docs/object-hierarchy#key) for the key that will be used to encrypt new disks.
     * The values in `disk-encryption-kms-key` are case sensitive (for example: `keyRings` and `cryptoKeys`). Provisioning a new volume with incorrect values results in an `invalidResourceUsage` error.
     * You cannot add the `disk-encryption-kms-key` parameter to an existing `StorageClass` object. However, you can delete the `StorageClass` object and recreate it with the same name, but a different set of parameters. Make sure the provisioner of the existing class is `pd.csi.storage.gke.io`.

You can set the [StorageClass as the default](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/).

  2. Deploy the `StorageClass` on your GKE cluster using [`kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster#choosing_a_shell):
         
         kubectl apply -f cmek-sc.yaml
         

  3. Verify that your `StorageClass` used the Compute Engine Filestore or Persistent Disk CSI driver and includes the ID of your key:

###  Filestore instances 
         
         kubectl describe storageclass csi-filestore-cmek
         

In the output of the command, verify the following:

     * The provisioner is set as filestore.csi.storage.gke.io.
     * The ID of your key follows instance-encryption-kms-key.
    
    Name:                  csi-filestore-cmek
    IsDefaultClass:        No
    Annotations:           None
    Provisioner:           filestore.csi.storage.gke.io
    Parameters:            instance-encryption-kms-key=projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME,type=pd-standard
    AllowVolumeExpansion:  true
    MountOptions:          none
    ReclaimPolicy:         Delete
    VolumeBindingMode:     WaitForFirstConsumer
    Events:                none
    

###  Persistent Disks 
    
    kubectl describe storageclass csi-gce-pd-cmek
    

In the output of the command, verify the following:

     * The provisioner is set as `pd.csi.storage.gke.io`.
     * The ID of your key follows `disk-encryption-kms-key`.
    
    Name:                  csi-gce-pd-cmek
    IsDefaultClass:        No
    Annotations:           None
    Provisioner:           pd.csi.storage.gke.io
    Parameters:            disk-encryption-kms-key=projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME,type=pd-standard
    AllowVolumeExpansion:  unset
    MountOptions:          none
    ReclaimPolicy:         Delete
    VolumeBindingMode:     WaitForFirstConsumer
    Events:                none
    




### Create an encrypted storage volume in GKE

In this section, you dynamically provision encrypted Kubernetes storage volumes with your new `StorageClass` and Cloud KMS key.

  1. Copy the following contents into a new file named `pvc.yaml`, and make sure the value for `storageClassName` matches the name of your `StorageClass` object:

###  Filestore instances 
         
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: podpvc
         spec:
           accessModes:
             - ReadWriteMany
           storageClassName: csi-filestore-cmek
           resources:
             requests:
               storage: 1Ti
         

###  Persistent Disks 
         
         kind: PersistentVolumeClaim
         apiVersion: v1
         metadata:
           name: podpvc
         spec:
           accessModes:
             - ReadWriteOnce
           storageClassName: csi-gce-pd-cmek
           resources:
             requests:
               storage: 6Gi
         

**Note:** If you marked the new `StorageClass` as default, then you can omit the `storageClassName` field.
  2. Apply the `PersistentVolumeClaim` (PVC) on your GKE cluster:
         
         kubectl apply -f pvc.yaml
         

  3. If your `StorageClass` has the `volumeBindingMode` field set to `WaitForFirstConsumer`, you must create a Pod to use the PVC before you can verify it. Copy the following contents into a new file named `pod.yaml`, and make sure the value for `claimName` matches the name of your `PersistentVolumeClaim` object:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: web-server
         spec:
           containers:
            - name: web-server
              image: nginx
              volumeMounts:
                - mountPath: /var/lib/www/html
                  name: mypvc
           volumes:
            - name: mypvc
              persistentVolumeClaim:
                claimName: podpvc
                readOnly: false
         

  4. Apply the Pod on your GKE cluster:
         
         kubectl apply -f pod.yaml
         

  5. Get the status of your cluster's `PersistentVolumeClaim` and verify that the PVC is created and bound to a newly provisioned `PersistentVolume`.

###  Filestore instances 
         
         kubectl get pvc
         

The output is similar to the following:
         
         NAME      STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS     AGE
         podpvc    Bound     pvc-e36abf50-84f3-11e8-8538-42010a800002   1Ti        RWO            csi-filestore-cmek  9s
         

**Note:** The provisioning of PVCs using [Enterprise tier](https://docs.cloud.google.com/filestore/docs/service-tiers#enterprise_tier) Filestore instances might take 20 to 30 minutes to complete.

###  Persistent Disks 
         
         kubectl get pvc
         

The output is similar to the following:
         
         NAME      STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS     AGE
         podpvc    Bound     pvc-e36abf50-84f3-11e8-8538-42010a800002   6Gi       RWO            csi-gce-pd-cmek  9s
         




You can now use your CMEK-protected Persistent Disk with your GKE cluster.

### Remove CMEK protection

When you encrypt a Persistent Disk by using a Cloud KMS key, the encryption is permanent. You can't remove the encryption key from that specific disk, even if you delete or disable the Cloud KMS key. The only way to change the encryption key or to remove CMEK protection from a Persistent Disk is to create a new Persistent Disk based on a snapshot of the existing disk. For more information, see [Remove your Cloud KMS encryption key from a Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#remove_encryption).

CMEK encryption cannot be removed from Filestore instances.

## GKE and CMEK organization policies

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

GKE supports [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy) (Preview) that can require CMEK protection and can limit which Cloud KMS keys you can use for CMEK protection.

When `container.googleapis.com` is in the `Deny` policy list of services for the `constraints/gcp.restrictNonCmekServices` constraint, GKE refuses to create the following resources if you don't enable CMEK protection:

  * New clusters and node pools
  * New Filestore instances and Persistent Disks



When the `constraints/gcp.restrictNonCmekCryptoKeyProjects` constraint is configured in an organization policy, GKE only creates CMEK-protected resources that use an encryption key from an allowed project, folder, or organization.

## What's next

  * Learn about [protecting resources with Cloud KMS Keys](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
