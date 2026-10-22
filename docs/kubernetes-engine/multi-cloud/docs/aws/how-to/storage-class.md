---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-class/
title: Use StorageClasses with your workloads \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:37.644301+00:00
---

# Use StorageClasses with your workloads  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-class/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Use StorageClasses with your workloads Stay organized with collections  Save and categorize content based on your preferences. 

GKE on AWS automatically deploys the Container Storage Interface (CSI) [Amazon Elastic Block Store (EBS)](https://github.com/kubernetes-sigs/aws-ebs-csi-driver) and [Amazon Elastic File Store (EFS)](https://github.com/kubernetes-sigs/aws-efs-csi-driver).

The EBS CSI Driver and EFS CSI Driver versions are tied to an GKE on AWS Kubernetes version. The driver version is typically the latest available when a GKE version is released. When the cluster is upgraded, the drivers update automatically.

## Use the default StorageClass

Creating a PersistentVolumeClaim without the field `spec.storageClassName` provisions a [General Purpose SSD volumes (gp2) volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#EBSVolumeTypes_gp2) using the default GKE on AWS EBS CSI Driver StorageClass.

The following YAML creates a PersistentVolumeClaim (PVC) named `mypvc` with a size of 30 gibibytes.
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: mypvc
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 30Gi
    

## Use a different preinstalled StorageClass

The GKE on AWS EBS CSI Driver also includes the `premium-rwo` StorageClass, which provisions higher-throughput [Provisioned IOPS SSD volumes (`io1`) volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#EBSVolumeTypes_piops).

You can use it by specifying it in the `spec.storageClassName` of the PVC.
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: mypvc
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 30Gi
      storageClassName: premium-rwo
    

## Use a custom StorageClass

If neither the default nor the `premium-rwo` StorageClass meets your needs, you can create additional StorageClasses for EBS volumes or use Container Storage Interface (CSI) Drivers.

  1. Choose if you are using an EBS volume or another CSI driver.

### EBS Volume

This tab describes how to create your own custom StorageClass that specifies an EBS volume type, file system type, and other parameters. You can find additional StorageClass parameters on the [GKE on AWS EBS CSI Driver GitHub page](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/docs/parameters.md).

To configure a custom StorageClass, copy the following YAML manifest into a file named `my-custom-class.yaml`.
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: CLASS_NAME
         provisioner: ebs.csi.aws.com
         allowVolumeExpansion: true
         volumeBindingMode: WaitForFirstConsumer
         

Replace `CLASS_NAME` with the name of your new StorageClass.

For example, the following YAML creates a new StorageClass that provisions [Throughput Optimized HDD](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#EBSVolumeTypes_st1) EBS volumes formatted with the [XFS](https://en.wikipedia.org/wiki/XFS) file system.
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: my-custom-class
         provisioner: ebs.csi.aws.com
         allowVolumeExpansion: true
         volumeBindingMode: WaitForFirstConsumer
         parameters:
           csi.storage.k8s.io/fsType: xfs
           type: st1
         

### Custom EFS StorageClass

This tab describes how to create a custom StorageClass for the EFS CSI Driver provisioner. See [Use an EFS resource](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-efs) for a list of the prerequisites for this StorageClass. The [EFS CSI Driver page](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/README.md#storage-class-parameters-for-dynamic-provisioning) lists additional StorageClass parameters beyond those in following manifest.

Copy the following YAML manifest into a file named `my-custom-class.yaml`.
         
         kind: StorageClass
         apiVersion: storage.k8s.io/v1
         metadata:
           name: <var>EFS_STORAGE_CLASS_NAME</var>
         provisioner: efs.csi.aws.com
         mountOptions:
           - tls
         parameters:
           provisioningMode: efs-ap
           fileSystemId: EFS_ID
           directoryPerms: "700"
         

Replace:

     * EFS_STORAGE_CLASS_NAME with the name of the `StorageClass`.
     * EFS_ID with your EFS file system ID - for example, fs-12345678a.

### CSI Driver

**Note:** This is an example. Check your CSI driver's documentation for required parameters.

You can specify a different CSI driver in the `provisioner` field.

To create a StorageClass with another CSI driver, you can use the example YAML below.
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: CLASS_NAME
    provisioner: CSI_DRIVER_NAME
    allowVolumeExpansion: true
    volumeBindingMode: WaitForFirstConsumer
    parameters:
      ...
    

Replace the following:

     * `CSI_DRIVER_NAME` with the name of the CSI driver—for example,`csi.example.com`
     * `CLASS_NAME` with the name of the StorageClass—for example, `my-custom-class`

Configure the sub-fields under `parameters` according to your CSI driver.

  2. Apply the YAML to your cluster.
         
         kubectl apply -f my-custom-class.yaml
         




### Create a PersistentVolumeClaim with a custom StorageClass

  1. Once a custom StorageClass is created, you can specify it in a PVC. The example below creates a PVC named `my-pvc` that references the StorageClass `my-custom-class`.
         
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: my-pvc
         spec:
           accessModes:
             - ReadWriteOnce
           resources:
             requests:
               storage: 30Gi
           storageClassName: my-custom-class
         




## Set the default StorageClass

GKE on AWS uses a default StorageClass called `standard-rwo` that provisions [gp2 EBS volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#EBSVolumeTypes_gp2). You can change the default to another StorageClass.

To change the default StorageClass:

  1. Update the `is-default-class` annotation for the `standard-rwo` StorageClass with `kubectl patch`.
         
         kubectl patch storageclass standard-rwo -p \
         '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
         

  2. Create a new StorageClass that has the annotation `storageclass.kubernetes.io/is-default-class: true`.

The following example StorageClass uses the `ebs.csi.aws.com` driver. To install another storage driver, see [Install additional CSI drivers](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-drivers).

Copy the following YAML into a file named `my-custom-class.yaml`.
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: CLASS_NAME
           annotations:
             storageclass.kubernetes.io/is-default-class: true
         provisioner: ebs.csi.aws.com
         allowVolumeExpansion: true
         volumeBindingMode: WaitForFirstConsumer
         parameters:
           type: EBS_VOLUME_TYPE
         

Replace the following:

     * `EBS_VOLUME_TYPE`: the AWS [EBS volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) that the StorageClass creates.
     * `CLASS_NAME` with the name of your new StorageClass

For example, the following YAML creates a new default StorageClass that provisions [General Purpose SSD volumes (gp3)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#gp3-ebs-volume-type).
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: my-custom-default-class
      annotations:
        storageclass.kubernetes.io/is-default-class: "true"
    provisioner: ebs.csi.aws.com
    allowVolumeExpansion: true
    volumeBindingMode: WaitForFirstConsumer
    parameters:
      type: gp3
    

  3. Apply the new custom class to your cluster.
         
         kubectl apply -f my-custom-class.yaml
         




After applying this manifest, GKE on AWS uses the `my-custom-default-class` StorageClass for new storage requests.

## Reference the StorageClass in a StatefulSet

To use your new StorageClass, you must reference it in a StatefulSet's `volumeClaimTemplates`.

When you reference a StorageClass in a StatefulSet's `volumeClaimTemplates` specification, Kubernetes provides stable storage using PersistentVolumes (PVs). Kubernetes calls the provisioner defined in the StorageClass to create a new storage volume. After the volume is provisioned, Kubernetes automatically creates a PV.

The following StatefulSet references the `my-custom-class` StorageClass and provisions a 1 gibibyte volume:
    
    
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: web
    spec:
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - name: nginx
            image: registry.k8s.io/nginx-slim:0.8
            volumeMounts:
            - name: www
              mountPath: /usr/share/nginx/html
      volumeClaimTemplates: # This is the specification in which you reference the StorageClass
      - metadata:
          name: www
        spec:
          accessModes: [ "ReadWriteOnce" ]
          resources:
            requests:
              storage: 1Gi
          storageClassName: my-custom-class # This field references the existing StorageClass
    

## What's next

  * Learn about [Persistent volumes and dynamic provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) in GKE.

  * [Install additional CSI drivers](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-drivers) on your GKE on AWS.

  * Deploy your first workload with the [Quickstart](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/quickstart). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
