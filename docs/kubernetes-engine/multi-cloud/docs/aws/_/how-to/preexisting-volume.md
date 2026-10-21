---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws//how-to/preexisting-volume/
title: Importing a preexisting EBS volume \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:41:29.996400+00:00
---

# Importing a preexisting EBS volume  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws//how-to/preexisting-volume/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Importing a preexisting EBS volume Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

If you already have an AWS [Elastic Block Store (EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) volume to import into GKE on AWS, you can create a [PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) (PV) object and reserve it for a specific PersistentVolumeClaim (PVC).

This page explains how to create a PV by using an existing EBS volume populated with data, and how to use the PV in a Pod. This page is for Operators and Storage specialists who want to configure and manage storage. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

Before completing these steps, you must you must:

  * [Create a GKE on AWS cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster) and configure access to it with `kubectl`.
  * [Connect and authenticate to your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/connect-and-authenticate-to-your-cluster)



### Using encrypted EBS volumes

If your EBS volume is encrypted with the AWS Key Management Service (KMS), you need to grant the GKE on AWS control plane AWS IAM role access to your KMS key.

To grant the control plane role access to your key:

  1. Find the name of your cluster's [control plane role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_the_control_plane_role).

  2. Choose the AWS KMS key used to encrypt your EBS volume, and add the control plane role as a key user by following the instructions in [Allow key users to use the KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#key-policy-default-allow-users).




## Creating a PersistentVolume for a pre-existing EBS volume

You can import an existing EBS volume by specifying a new PV and adding it to your cluster.

  1. Copy the following YAML into a file named `existing-volume.yaml`:
         
         apiVersion: v1
         kind: PersistentVolume
         metadata:
           name: VOLUME_NAME
           annotations:
             pv.kubernetes.io/provisioned-by: ebs.csi.aws.com
         spec:
           capacity:
             storage: VOLUME_CAPACITY
           accessModes:
             - ReadWriteOnce
           persistentVolumeReclaimPolicy: Retain
           storageClassName: STORAGE_CLASS_NAME
           claimRef:
             name: my-pvc
             namespace: default
           csi:
             driver: ebs.csi.aws.com
             volumeHandle: EBS_VOLUME_ID
             fsType: FILE_SYSTEM_TYPE
           nodeAffinity:
             required:
               nodeSelectorTerms:
               - matchExpressions:
                 - key: topology.ebs.csi.aws.com/zone
                   operator: In
                   values:
                   - ZONE
         
         
         Replace the following:
         

     * `VOLUME_NAME`: The name for your volume.
     * `VOLUME_CAPACITY`: size of the volume— for example, `30G`. For more information on specifying volume capacity in Kubernetes, see the [Meaning of memory](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/#meaning-of-memory).
     * `STORAGE_CLASS_NAME`: the name of the StorageClass that provisions the volume— for example, `standard-rwo`.

**Note:** A StorageClass is required to reference other attributes like `allowVolumeExpansion`, even if a volume is not dynamically provisioned.
     * `EBS_VOLUME_ID`: Your EBS [volume id](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-volumes.html#examples). For example, `vol-05786ec9ec9526b67`.

     * `FS_TYPE`: The [file system](https://github.com/kubernetes-sigs/aws-ebs-csi-driver#createvolume-parameters) of the volume— for example, `ext4`.

     * `ZONE`: The AWS Availability Zone that hosts the EBS volume— for example, `us-east-1c`.

  2. Apply the YAML to your cluster
         
         kubectl apply -f existing-volume.yaml
         

  3. Confirm the creation of your PV
         
         kubectl describe pv volume-name
         

The output of this command contains the status of the PV.




## Using the volume with a PersistentVolumeClaim and Pod

After you have imported your volume, you can create a PVC and a Pod that attaches the PVC.

  1. The YAML below creates a PVC and attaches it to a Pod running the Nginx web server. Copy it into a file named `nginx.yaml`:
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: my-pvc
         spec:
           storageClassName: STORAGE_CLASS_NAME
           volumeName: VOLUME_NAME
           accessModes:
             - ReadWriteOnce
           resources:
             requests:
               storage: VOLUME_CAPACITY
         ---
         
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
                  name: data
           volumes:
            - name: data
              persistentVolumeClaim:
                claimName: PVC_NAME
         

Replace the following:

     * `STORAGE_CLASS`: The name of the StorageClass from the PersistentVolume you created previously— for example, `standard-rwo`.
     * `VOLUME_NAME`
     * `VOLUME_CAPACITY`
     * `PVC_NAME`: Name of the PVC— for example, `my-pvc`.
  2. Apply the YAML to your cluster
         
         kubectl apply -f nginx.yaml
         

  3. Check the status of your Nginx instance with `kubectl describe`. The output should have a `STATUS` of `Running`.
         
         kubectl describe pod web-server
         




## What's next

  * Use additional [storage drivers](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-drivers) with GKE on AWS.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
