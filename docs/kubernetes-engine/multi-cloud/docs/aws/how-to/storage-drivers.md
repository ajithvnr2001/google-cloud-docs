---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-drivers/
title: Install additional CSI drivers \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:41.682525+00:00
---

# Install additional CSI drivers  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-drivers/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Install additional CSI drivers Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to install a Container Storage Interface (CSI) storage driver on your GKE clusters.

[CSI](https://github.com/container-storage-interface/spec/blob/master/spec.md) is an open standard API that enables Kubernetes to expose arbitrary storage systems to containerized workloads. Also, CSI enables the use of modern storage features, such as and resizing and snapshots.

By default, GKE on AWS provisions [EBS volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) with the [`ebs-csi-driver`](https://github.com/kubernetes-sigs/aws-ebs-csi-driver). You can also provision [EFS volumes](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-efs) with the [`efs-csi-driver`](https://github.com/kubernetes-sigs/aws-efs-csi-driver). If you want to use another type of storage volume, you can install a CSI driver. 

After installing a CSI driver, you need to create a Kubernetes [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/). You set the CSI driver as the provisioner for the StorageClass. Then, you can [set the StorageClass as default](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-class#set_default), or configure your workloads to use the StorageClass.

## Before you begin

[Connect and authenticate to your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/connect-and-authenticate-to-your-cluster)

## Install a vendor's CSI driver

Storage vendors are responsible for providing installation instructions for their CSI drivers. See the list of [CSI drivers](https://kubernetes-csi.github.io/docs/drivers.html) in the CSI documentation.

Follow the installation instructions for your CSI driver, and then continue with the next steps on this page.

Google does not provide support or instructions for third-party drivers. Contact your storage vendor for support.

## Verify your driver installation

After you install a CSI driver, you can verify the installation by running the following commands.
    
    
    kubectl get csinodes \
        -o jsonpath='{range .items[*]} {.metadata.name}{": "} {range .spec.drivers[*]} {.name}{"\n"} {end}{end}'
    

## Use a CSI driver

To use a CSI driver, do the following:

  1. Create a custom [StorageClass](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-class#custom) which references the driver in its `provisioner` field.

  2. To provision storage, you can either:

     * Reference the StorageClass in a [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)'s `volumeClaimTemplates` specification.
     * [Set it as the cluster's default StorageClass](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-class#set_default).



## Considerations for StorageClass backed by a CSI driver

When you create a StorageClass, consider the following:

  * Check your CSI driver documentation for [driver-specific parameters](https://kubernetes.io/docs/concepts/storage/storage-classes/#the-storageclass-resource) that you provide to your StorageClass, including the provisioner name.

  * You should name the StorageClass after its properties (such as `fast` or `highly-replicated`), rather than after the name of the specific driver or appliance behind it. When you name a StorageClass after its properties, you can create StorageClasses with the same name in different clusters and environments. Then, configure your workloads to use the same StorageClass.




## What's next?

  * Create a [StorageClass](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/storage-class#custom) which references the CSI driver.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
