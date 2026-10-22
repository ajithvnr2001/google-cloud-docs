---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/vm-servers/
title: Manage virtual machines on Distributed Cloud connected servers \u00a0|\u00a0 Google Distributed Cloud connected, version 1.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:37.319084+00:00
---

# Manage virtual machines on Distributed Cloud connected servers  |  Google Distributed Cloud connected, version 1.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/vm-servers/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/overview)



Send feedback 

#  Manage virtual machines on Distributed Cloud connected servers Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage virtual machines on Google Distributed Cloud connected servers running [VM Runtime on Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/enable-disable). You must be familiar with VM Runtime on GDC before completing the steps on this page. For a list of supported guest operating systems, see [Verified guest operating systems for VM Runtime on GDC](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/guest-os).

To learn how virtual machines serve as an essential component of the Distributed Cloud connected platform, see [Extending GKE Enterprise to manage on-premises edge VMs](https://cloud.google.com/blog/topics/anthos/extending-anthos-to-manage-on-premises-edge-vms-now-generally-available).

Distributed Cloud connected clusters support virtual machine webhooks. This allows Distributed Cloud connected to validate user requests made to the local Kubernetes API server. Rejected requests generate detailed information on the reason for rejection.

## Configure Symcloud Storage

Google Distributed Cloud connected servers use [Rakuten Symcloud Storage](https://symphony.rakuten.com/insight/datasheet/symcloud-storage), as their storage solution. Symcloud Storage is a third-party solution that acts as a local storage abstraction layer on each Distributed Cloud connected node and makes its local storage available to workloads running on other Distributed Cloud connected nodes.

Symcloud Storage is deployed from Google Cloud Marketplace and is subject to the terms stated therein. Google provides limited support for using Symcloud Storage with Distributed Cloud connected and might engage the third-party provider for assistance. Software updates for Symcloud Storage are included in the Distributed Cloud connected software updates.

Configure your Google Distributed Cloud connected cluster as follows to enable Symcloud Storage for virtual machines:

  1. Create the `robinio` namespace with the following command:
         
         kubectl create ns robinio
         

  2. Obtain the Symcloud Storage license file and apply it to the cluster with the following command:
         
         kubectl apply LICENSE_FILE
         

  3. Verify that Symcloud Storage is up and running with the following command:
         
         kubectl apply LICENSE_FILE
         

The command returns output similar to the following:
         
         Name:         robin
          Namespace:
          Labels:       app.kubernetes.io/instance=robin
                        app.kubernetes.io/managed-by=robin.io
                        app.kubernetes.io/name=robin
          Annotations:  <none>
          API Version:  manage.robin.io/v1
          Kind:         RobinCluster
          Metadata:
            …
          Spec:
            …
          Status:
            …
            Phase:             Ready
            …
         

  4. Create the `robin-block-immediate` storage class by applying the following configuration to the cluster:
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: robin-block-immediate
         parameters:
           faultdomain: host
           replication: "3"
           blocksize:   "512"
         provisioner: robin
         reclaimPolicy: Delete
         volumeBindingMode: Immediate
         allowVolumeExpansion: true
         

  5. Create the `robin-snapshotclass` volume snapshot class by applying the following configuration to the cluster:
         
         apiVersion: snapshot.storage.k8s.io/v1
         kind: VolumeSnapshotClass
         metadata:
           name: robin-snapshotclass
           labels:
             app.kubernetes.io/instance: robin
             app.kubernetes.io/managed-by: robin.io
             app.kubernetes.io/name: robin
           annotations:
             snapshot.storage.kubernetes.io/is-default-class: "true"
         driver: robin
         deletionPolicy: Delete
         




## Enable VM Runtime on GDC support on Distributed Cloud connected

By default, VM Runtime on GDC virtual machine support is enabled on Distributed Cloud connected. If you need to manually enable it, complete the steps in this section. The instructions in this section assume that you have a fully functioning Distributed Cloud connected cluster. To disable VM Runtime on GDC virtual machine support on your cluster, undo the changes described in this section.

To enable the VM Runtime on GDC virtual machine subsystem, complete the following steps:

  1. Modify the `VMRuntime` custom resource with the following contents and apply it to your cluster:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VMRuntime
         metadata:
           annotations:
             baremetal.cluster.gke.io/vmrumtime-force-disable: "false"
             vm.cluster.gke.io/enable-vm-backup: "true"
         spec:
           enabled: true
           storage:
             defaultStorageClass: robin-block-immediate
         haPolicy:
           defaultRecoveryStrategy: Reschedule
           nodeHeartbeatInterval: 15s
           nodeMonitorGracePeriod: 55s

This process typically takes several minutes to complete.

  2. Use the following command to verify that the `VMRuntime` custom resource has been applied to your cluster:
         
         kubectl get vmruntime
         

The command returns output similar to the following example:
         
         NAME        AGE   ENABLED   READY   PREFLIGHTCHECK
         vmruntime   5m   true      true    true
         

  3. Modify the `storageprofile` for the `robin-block-immediate` storage class with the following contents and apply it to your cluster:
         
         apiVersion: cdi.kubevirt.io/v1beta1
         kind: StorageProfile
         metadata:
           name: robin-block-immediate
         spec:
           claimPropertySets:
             accessModes:
               ReadWriteMany
           volumeMode: Block




### Install the `virtctl` management tool

You need the [`virtctl`](https://kubevirt.io/user-guide/operations/virtctl_client_tool/) client tool to manage virtual machines on your Distributed Cloud connected cluster. To install the tool, complete the following steps:

  1. Install the `virtctl` client tool as a `kubectl` plugin:
         
         export VERSION=v0.59.0-anthos1.28-gke.8
         gcloud storage cp gs://anthos-baremetal-release/virtctl/${VERSION}/linux-amd64/virtctl/usr/local/bin/virtctl
         cd /usr/local/bin
         sudo ln -s virtctl kubectl-virt
         sudo chmod a+x virtctl
         cd -

  2. Verify that the `virt` plugin is installed:
         
         kubectl plugin list

If the plugin has been successfully installed, the command's output lists `kubectl-virt` as one of the plugins.




## Create a Cloud Storage bucket for virtual machine images

Complete the steps in this section to create a Cloud Storage bucket for your virtual machine images. If you already have an established image repository, skip this section.

  1. Complete the steps in [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets) to create a bucket.

  2. Configure a service account and a key to for accessing the bucket with the following commands:
         
         export PROJECT_ID=$(gcloud config get-value project)
         gcloud iam service-accounts create image-access
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:image-access@${PROJECT_ID}.iam.gserviceaccount.com" \
           --role="roles/storage.objectViewer" \
         gcloud iam service-accounts keys create ./image-access-gcr.json \
           --iam-account="image-access@${PROJECT_ID}.iam.gserviceaccount.com"

  3. Create a secret in the cluster for accessing the bucket. If your bucket is public, skip this step. This secret must exist in the same namespace as your virtual machine disks. You must create a secret in each affected namespace.
         
         kubectl create secret generic gcs-image-sa --from-file=creds-gcp.json=./image-access-gcr.json -n NAMESPACE

Replace `CLUSTER_ID` with the name of the target namespace.

  4. Store your images in the bucket.




## Create a virtual machine disk from a virtual machine image

Complete the steps in this section to create a virtual machine disk from a virtual machine image.

### Create a disk from an image stored in Cloud Storage

Create a virtual machine disk from a virtual machine stored in your Cloud Storage bucket by applying the following configuration to your cluster:
    
    
     apiVersion: vm.cluster.gke.io/v1
     kind: VirtualMachineDisk
     metadata:
       name: DISK_NAME
       namespace: NAMESPACE
     spec:
       source:
         gcs:
           url: gs://{PROJECT_ID}-vm-images/IMAGE_FILE
           secretRef: gcs-image-sa
       size: DISK_SIZE
       storageClassName: robin-block-immediate

Replace the following:

  * `DISK_NAME`: the name of this virtual machine disk.
  * `NAMESPACE`: the target namespace.
  * `IMAGE_FILE`: the name of virtual machine image file.
  * `DISK_SIZE`: the desired disk size. This must be larger than the `virtual-size` value of the virtual machine image file. You can find this value with the command `qemu-img info DISK_SIZE`.



If you don't specify a `storageClassName` value, the default value specified in the `VMRuntime` resource is used.

### Create a disk from an existing disk image

Create a virtual machine disk from an existing virtual machine disk or image file on your cluster as follows.

  1. Create the target disk by applying the following configuration to your cluster:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineDisk
         metadata:
           name: IMAGE_DISK_NAME
           namespace: NAMESPACE
         spec:
           source:
             virtualMachineDisk:
               name: EXISTING_DISK_NAME
           size: DISK_SIZE
           storageClassName: robin-block-immediate

Replace the following:

     * `IMAGE_DISK_NAME`: the name of this virtual machine disk.
     * `NAMESPACE`: the target namespace.
     * `EXISTING_DISK_NAME`: the name of the existing virtual machine disk.
     * `DISK_SIZE`: the desired disk size. This must be equal to or larger than the size of the existing disk or image file.

You can obtain the size of your existing disk or image file using the `qemu-img` tool as follows:
    
    qemu-img info EXISTING_DISK_NAME

If you don't specify a `storageClassName` value, the default value specified in the `VMRuntime` resource is used.

  2. Create a new disk from your existing image file by applying the following configuration to your cluster:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineDisk
         metadata:
           name: DISK_NAME
           namespace: NAMESPACE
         spec:
           source:
             virtualMachineDisk:
               name: IMAGE_DISK_NAME
           size: DISK_SIZE
           storageClassName: robin-block-immediate

Replace the following:

     * `IMAGE_DISK_NAME`: the name of the virtual machine disk you created in the previous step.
     * `NAMESPACE`: the target namespace.
     * `DISK_SIZE`: the desired disk size. Must be equal to the size of the virtual machine disk you created in the previous step.
  3. Resize the target disk to the desired size using the following command:
         
         kubectl edit gdisk DISK_NAME -n NAMESPACE

Replace the following:

     * `DISK_NAME`: the name of the virtual machine disk you created in the previous step.
     * `NAMESPACE`: the target namespace.
  4. Modify the `spec.size` value in the configuration of the disk and apply it to your cluster.




### Create an empty disk

Create an empty virtual machine disk by applying the following configuration to your cluster:
    
    
     apiVersion: vm.cluster.gke.io/v1
     kind: VirtualMachineDisk
     metadata:
       name: DISK_NAME
       namespace: NAMESPACE
     spec:
       size: DISK_SIZE
       storageClassName: robin-block-immediate

Replace the following:

  * `DISK_NAME`: the name of this virtual machine disk.
  * `NAMESPACE`: the target namespace.
  * `DISK_SIZE`: the desired disk size in gibibytes. This must be larger than the `virtual-size` value of the virtual machine image file. You can find this value with the command `qemu-img info DISK_SIZE`.



If you don't specify a `storageClassName` value, the default value specified in the `VMRuntime` resource is used.

## Configure virtual networking

Follow the steps in [Networking](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/networking) to configure the virtual networking for your virtual machines.

## Create a virtual machine

Complete the steps in this section to create a virtual machine on your Distributed Cloud connected server deployment. The instructions in this section are examples meant to illustrate configurations for different scenarios. For detailed information on configuring virtual machines, see [Create a VM with specific CPU and memory resources using VM Runtime on GDC](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/compute-configurations).

### Create a virtual machine from a bootable disk image

To create a virtual machine from a bootable disk image, apply the following configuration to your cluster:
    
    
     kind: VirtualMachine
     metadata:
       name: my-virtual-machine
       namespace: my-vm-namespace
     spec:
       osType: Linux/Windows
       guestEnvironment: {} // comment out this line to enable guest environment for access management
       autoRestartOnConfigurationChange: true 
       compute:
         cpu:
           vcpus: 6
         memory:
           capacity: 8Gi
       interfaces:
          - name: eth0
            networkName: network-410
            ipAddresses:
            - 10.223.237.10/25
       disks:
         - virtualMachineDiskName: my-boot-disk
           boot: true
         - virtualMachineDiskName: my-data-disk

Replace the following:

  * `DISK_NAME`: the name of this virtual machine disk.
  * `NAMESPACE`: the target namespace.



### Create a virtual machine from an ISO optical disc image

To create a virtual machine from an ISO optical disc image, complete the steps in [Create a Windows VM from ISO image in Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/windows-vm).

### Create a virtual machine with GPU support

Complete the steps described on this page to create a virtual machine configured to meet your business requirements, then complete the steps in [Configure a virtual machine to use GPU resources](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/gpu#gpu-vm).

## Access a virtual machine

Complete the steps in this section to access a virtual machine running on your Distributed Cloud connected server deployment.

### Obtain access credentials

Complete the steps in this section to obtain the credentials necessary to access your virtual machine using the Linux guest environment feature.

  1. Enable the Linux guest environment for the target virtual machine by applying the following configuration to your cluster:
         
         kind: VirtualMachine
         metadata:
          name: my-virtual-machine
          namespace: my-vm-namespace
         spec:
          osType: Linux
          guestEnvironment: {}
          autoRestartOnConfigurationChange: true 

  2. Generate an `id_rsa.pub` file containing an SSH key pair with the following command:
         
         ssh-keygen -t rsa

  3. Create a `VirtualMachineAccessRequest` resource by applying the following configuration to your cluster:
         
         apiVersion: vm.cluster.gke.io/v1alpha1
         kind: VirtualMachineAccessRequest
         metadata:
          name: RESOURCE_NAME
          namespace: NAMESPACE
         spec:
           vm: VM_NAME
           user: USER_NAME
           ssh:
             key: RSA_KEY
             ttl: 2h




Replace the following:

  * `RESOURCE_NAME`: a descriptive name for this virtual machine access request resource.
  * `NAMESPACE`: the target namespace.
  * `VM_NAME`: the name of the target virtual machine.
  * `USER_NAME`: the name of the user to whom access is being granted.
  * `RSA_KEY`: the contents of the `id_rsa.pub` file you generated in the previous step.


  1. Check the status of the access request with the following command:
         
         kubectl get vmar
         

When the command returns a `Configured` status, proceed to the next step.

  2. Access the virtual machine with SSH or Remote Desktop:

     * If the virtual machine is connected to your local network, you can access it directly.
     * If the virtual machine is connected to the Pod network, you must create a load balancer service to access the required ports.



## Start, restart, or stop a virtual machine

Use the following commands to start, restart, or stop a virtual machine:

  * **Start a virtual machine:** `kubectl virt start vm``VM_NAME``-n``NAMESPACE`
  * **Restart a virtual machine:** `kubectl virt restart vm``VM_NAME``-n``NAMESPACE`
  * **Stop a virtual machine:** `kubectl virt stop vm``VM_NAME``-n``NAMESPACE`



Replace the following:

  * `VM_NAME`: the name of the target virtual machine.
  * `NAMESPACE`: the target namespace.



## What's next

  * [Manage virtual machines on Distributed Cloud connected racks](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/virtual-machines)
  * [Deploy workloads on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/deploy)
  * [Manage GPU workloads](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/gpu)
  * [Manage zones](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/zones)
  * [Manage machines](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/machines)
  * [Manage clusters](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/clusters)
  * [Manage node pools](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs/nodepools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
