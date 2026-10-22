---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-efs/
title: Provision a Persistent Volume with EFS \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:57.821918+00:00
---

# Provision a Persistent Volume with EFS  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-efs/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Provision a Persistent Volume with EFS Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up an EFS-based PersistentVolume for use in GKE on AWS using the [EFS CSI Driver](https://github.com/kubernetes-sigs/aws-efs-csi-driver). The [Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) (EFS) is the underlying AWS mechanism that provides network filesystems to your cluster. An EFS-based PersistentVolume is a cluster resource that makes storage available to your workloads through an EFS access point, and ensures that the storage persists even when no workloads are connected to it.

This page is for Operators and Storage specialists who want to configure and manage storage. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

GKE on AWS supports both static and dynamic provisioning of PersistentVolumes. Dynamic provisioning uses a slightly different setup but needs less administrative effort afterwards.

## Before you begin

To perform the steps on this page, first complete the following:

  * Familiarize yourself with how Kubernetes and GKE on AWS handle workload storage. To learn about these topics, see [Using persistent storage in your GKE on AWS workloads](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/storage#using_persistent_storage_in_your_workloads) and [Creating Amazon EFS resources](https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs.html).
  * Upgrade to Kubernetes version 1.25 or later to use dynamic provisioning of PersistentVolumes using EFS. If you are using Kubernetes version 1.24, [contact support](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/getting-support) for access to this feature.



## Static provisioning overview

Creating an Elastic File System (EFS) and making it available to workloads in your cluster through static provisioning has four steps:

  * Create your EFS resource
  * Configure your network
  * Create a mount target
  * Create a `PersistentVolume`



The final step is by the workload: to request persistent storage by issuing a `PersistentVolumeClaim`.

## Dynamic provisioning overview

Creating an EFS resource and making it available through dynamic provisioning also has four steps:

  * Create your EFS resource
  * Configure your network
  * Create a mount target
  * Create a `StorageClass`



Creating the `StorageClass` is a one-time operation. Once a storage class with given characteristics is defined, the workload can issue a PersistentVolumeClaim, or request for persistent storage. All PersistentVolumeClaims for storage with those characteristics can request the same `StorageClass`.

### Common steps

Whether you're using static or dynamic provisioning in your cluster, you must begin with the setup steps listed here, then continue with the static or dynamic provisioning steps as appropriate. Once you've created your EFS and made it accessible, the workload must take the final steps to access it. The steps to do so are described in [Use EFS storage](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-efs).

### Create an AWS EFS Resource

An EFS resource is required whether you're using static or dynamic provisioning. If your cluster uses both, you can create separate EFS resources for them or use the same one for both. See [Creating Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs) to read more about creating an EFS resource.

You can also re-use an existing EFS, in which case you can skip this section and proceed to [Create mount targets](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-efs#create_mount_targets).

  1. Get the AWS region where your cluster runs.
         
         gcloud container aws clusters describe CLUSTER_NAME \
           --location=LOCATION \
           --format="value(awsRegion)"
         

Replace the following:

     * CLUSTER_NAME: the name of the AWS cluster.
     * LOCATION: the Google Cloud location of the AWS cluster
  2. Create an EFS resource system in the same AWS region with the following command.
         
         aws efs create-file-system \
           --region AWS_REGION \
           --performance-mode generalPurpose \
           --query 'FileSystemId' \
           --output text
         

Replace the following:

     * AWS_REGION: the AWS region where the cluster runs



The output includes the file system's ID. Save this value. You'll need it later.

### Create mount targets

The CSI driver for EFS accesses file systems through EFS mount targets. A mount target is a private IP address that uses AWS security groups to control access to the underlying EFS.

If the node pools in your cluster are running on different subnets, you must create a separate mount target on each node pool subnet.

In this example, the access to each mount target is protected by a single security group that includes both the mount targets and the node pool machines. Depending on your VPC configuration and security requirements, you might choose to split this configuration into two or more security groups— for example, one for mount targets and another for node pool worker nodes.

  1. Create a dedicated security group to control access to the EFS

Obtain the ID of the AWS VPC where the cluster runs.
         
         gcloud container aws clusters describe CLUSTER_NAME \
           --location=LOCATION \
           --format="value(networking.vpcId)"
         

Replace the following:

     * CLUSTER_NAME
     * LOCATION

The output includes the ID of your VPC. Save this value. You'll need it later.

  2. Create a security group to control access to your EFS mount target.
         
         aws ec2 create-security-group \
           --group-name gke-efs-security-group \
           --description "EFS security group" \
           --vpc-id VPC_ID \
           --output text
         

Replace VPC_ID with the ID of the AWS VPC where the cluster runs.

The output includes the ID of the new security group. Save this value. You'll need it later.

  3. By default, AWS creates security groups with a default rule that allows all outbound traffic. Remove the default outbound rule.
         
         aws ec2 revoke-security-group-egress \
           --group-id SECURITY_GROUP_ID
           --ip-permissions '[{"IpProtocol":"-1","FromPort":-1,"ToPort":-1,"IpRanges":[{"CidrIp":"0.0.0.0/0"}]}]'
         

Replace SECURITY_GROUP_ID with the ID of the AWS security group.

  4. Authorize inbound and outbound traffic for EFS (port 2049).
         
         aws ec2 authorize-security-group-ingress \
             --group-id SECURITY_GROUP_ID \
             --protocol tcp \
             --port 2049 \
             --source-group SECURITY_GROUP_ID
         
         
         aws ec2 authorize-security-group-egress \
             --group-id SECURITY_GROUP_ID \
             --protocol tcp \
             --port 2049 \
             --source-group SECURITY_GROUP_ID
         

  5. Create an EFS mount target on each node pool subnet.

List subnets associated with all node pools.
         
         gcloud container aws node-pools list \
           --cluster=CLUSTER_NAME \
           --location=LOCATION \
           --format="value(subnetId)"
         

Replace the following:

     * CLUSTER_NAME
     * LOCATION

The output is a list of subnet IDs. Save this value. You'll need it later.

  6. For each subnet, create an associated EFS mount target with the security group applied.
         
         aws efs create-mount-target \
             --file-system-id EFS_ID \
             --subnet-id SUBNET_ID \
             --security-groups SECURITY_GROUP_ID
         

Replace the following:

     * EFS_ID: the ID of your EFS resource.
     * SUBNET_ID: the ID of the node pool's subnet.
     * SECURITY_GROUP_ID
  7. Add the EFS security group to all cluster node pools.

Get the list all your node pools.
         
         gcloud container aws node-pools list \
           --cluster=CLUSTER_NAME \
           --location=LOCATION
         

Replace the following:

     * CLUSTER_NAME
     * LOCATION

The output includes the names of your cluster's node pools. Save this value. You'll need it later.

  8. Update each node pool to include the new EFS security group.
         
         gcloud container aws node-pools update NODE_POOL_NAME \
           --cluster=CLUSTER_NAME \
           --location=LOCATION  \
           --security-group-ids=SECURITY_GROUP_IDS
         

Replace the following:

     * NODE_POOL_NAME: the name of the node pool.
     * CLUSTER_NAME: the name of your cluster.
     * LOCATION
     * SECURITY_GROUP_IDS the list of security group IDs for worker nodes.



## Create a PersistentVolume (static) or StorageClass (dynamic)

If you're using static provisioning, the next step is to create a PersistentVolume. If you're using dynamic provisioning, the EFS driver does this for you; instead, you define a StorageClass for workloads to specify in their PersistentVolumeClaim. Choose the tab matching your chosen provisioning method.

### Static provisioning

If you're using static provisioning, the next step is to create a PersistentVolume that mounts an EFS share.

  1. Choose the appropriate tab depending on whether you're connecting directly to the EFS share or via an access point.

### Connect directly

Copy the following YAML manifest into a file named `efs-volume.yaml`. The manifest references the EFS storage class you created previously.
         
         apiVersion: v1
         kind: PersistentVolume
         metadata:
           name: VOLUME_NAME
         spec:
           capacity:
             # Note: storage capacity is not used by the EFS CSI driver.
             # It is required by the PersistentVolume spec.
             storage: 5Gi
           volumeMode: Filesystem
           accessModes:
             - ReadWriteMany
           persistentVolumeReclaimPolicy: Retain
           storageClassName: "" # storageClassName is not required, see note in the following section.
           claimRef:
             name: CLAIM_NAME
             namespace: default
           csi:
             driver: efs.csi.aws.com
             volumeHandle: EFS_ID
         

Replace the following:

     * VOLUME_NAME with a name for the persistent volume.
     * CLAIM_NAME with the name you want to use for the PersistentVolumeClaim.
     * EFS_ID with your EFS resource ID. For example, `fs-12345678a`.

### Access point

To create an access point based volume, you need to manually provision it. See [Working with EFS access points](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html) for more information.

Copy the following YAML manifest into a file named `efs-volume.yaml`. The manifest references the EFS storage class you created previously.
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: VOLUME_NAME
    spec:
      capacity:
        # Note: storage capacity is not used by the EFS CSI driver.
        # It is required by the PersistentVolume spec.
        storage: 5Gi
      volumeMode: Filesystem
      accessModes:
        - ReadWriteMany
      persistentVolumeReclaimPolicy: Retain
      # Set storageClassName to empty string for static provisioning. See [Use an EFS resource](/kubernetes-engine/multi-cloud/docs/aws/how-to/use-efs)
      storageClassName: ""
      claimRef:
        name: CLAIM_NAME
        namespace: default
      csi:
        driver: efs.csi.aws.com
        volumeHandle: EFS_ID::ACCESS_POINT_ID
    

Replace the following:

     * VOLUME_NAME with a name for the persistent volume.
     * CLAIM_NAME with the name you want to use for the PersistentVolumeClaim.
     * EFS_ID with your EFS resource ID. For example, `fs-12345678a`.
     * ACCESS_POINT_ID with your access point's ID. For example, `fsap-1234567890abcde`.

**Note:** You must use the same `storageClassName` value for your PersistentVolume and PersistentVolumeClaim resources.
  2. Apply the YAML to your cluster.
         
         kubectl apply -f efs-volume.yaml
         

The output confirms the PersistentVolume's creation.
         
         persistentvolume/VOLUME_NAME created
         
         




### Dynamic provisioning

This section describes how to create a StorageClass that references the EFS resource you created earlier. Once this is done, developers can access the EFS resource by following the steps described in [Use an EFS resource](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-efs).

  1. Create a StorageClass that references the EFS resource ID.

Copy the following yaml fragment to a new file named `efs-storage-class.yaml`. To learn more about how to adjust the characteristics of the StorageClass described by this file, see the documentation on [EFS StorageClass parameters](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/README.md#storage-class-parameters-for-dynamic-provisioning).
         
         kind: StorageClass
         apiVersion: storage.k8s.io/v1
         metadata:
           name: EFS_STORAGE_CLASS_NAME
         provisioner: efs.csi.aws.com
         mountOptions:
           - tls
         parameters:
           provisioningMode: efs-ap
           fileSystemId: EFS_ID
           directoryPerms: "700"
         
         

Replace:

     * EFS_STORAGE_CLASS_NAME with the name you've chosen for the StorageClass.
     * EFS_ID with your EFS resource ID - for example, fs-12345678a.
  2. Apply the YAML to your cluster.
         
         kubectl apply -f efs-storage-class.yaml
         

If successful, this command's output will contain a line similar to the following:

`storageclass/EFS_STORAGE_CLASS_NAME created`




## Clean up

**Note:** When you release a `PersistentVolume`, the CSI Driver doesn't delete the data in the EFS resource. You must manually delete this data yourself.

To remove the resources you created in the previous sections, run the following commands:

  1. Use `kubectl` to remove the EFS claim resource from your cluster:
         
         kubectl delete -f efs-claim.yaml
         

  2. If using static provisioning, use `kubectl` to remove the associated resources from your cluster:
         
         kubectl delete -f efs-volume.yaml
         

  3. If using dynamic provisioning, use `kubectl` to remove the associated resources from your cluster:
         
         kubectl delete -f efs-storage-class.yaml
         

  4. Find the ID of your mount target:
         
         aws efs describe-mount-targets \
         --file-system-id EFS_ID \
         --profile adminuser \
         --region AWS_REGION
         

Replace the following:

     * EFS_ID: the ID of your EFS resource
     * AWS_REGION: the AWS region where the cluster runs

The output includes the mount target id. Save this value. You'll need it later.

  5. Delete your EFS mount target:
         
         aws efs delete-mount-target \
         --mount-target-id MOUNT_TARGET_ID \
         --profile adminuser \
         --region AWS_REGION
         

Replace the following:

     * MOUNT_TARGET_ID: the ID of your EFS mount target
     * AWS_REGION: the AWS region of your mount target
  6. Delete any security groups you created.

  7. Delete the file system by using the delete-file-system CLI command. You can get a list of your file systems by using the describe-file-systems CLI command. The file system ID is in the response.
         
         aws efs delete-file-system \
           --file-system-id EFS_ID \
           --profile adminuser \
           --region AWS_REGION
         

Replace the following:

     * EFS_ID
     * AWS_REGION



## What's next

  * Learn how to [use a `PersistentVolumeClaim`](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-efs) from a workload to access an EFS volume
  * Learn about additional ways to use EFS volumes in the [`aws-efs-csi-driver` examples](https://github.com/kubernetes-sigs/aws-efs-csi-driver).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
