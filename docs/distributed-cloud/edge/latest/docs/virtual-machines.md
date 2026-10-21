---
url: https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/virtual-machines/
title: Manage virtual machines \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:27:48.281951+00:00
---

# Manage virtual machines  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/virtual-machines/

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
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/overview)



Send feedback 

#  Manage virtual machines Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage virtual machines on your Google Distributed Cloud connected deployment running [VM Runtime on Google Distributed Cloud](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/vm-runtime/overview). You must be familiar with VM Runtime on GDC before completing the steps on this page. For a list of supported guest operating systems, see [Verified guest operating systems for VM Runtime on GDC](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/vm-runtime/guest-os).

To learn how virtual machines serve as an essential component of the Distributed Cloud connected platform, see [Extending GKE Enterprise to manage on-premises edge VMs](https://cloud.google.com/blog/topics/anthos/extending-anthos-to-manage-on-premises-edge-vms-now-generally-available).

Distributed Cloud connected clusters support virtual machine webhooks. This allows Distributed Cloud connected to validate user requests made to the local Kubernetes API server. Rejected requests generate detailed information on the reason for rejection.

## Configure Symcloud Storage

Google Distributed Cloud connected uses [Rakuten Symcloud Storage](https://symphony.rakuten.com/insight/datasheet/symcloud-storage), as their storage solution. Symcloud Storage is a third-party solution that acts as a local storage abstraction layer on each Distributed Cloud connected node and makes its local storage available to workloads running on other Distributed Cloud connected nodes.

Symcloud Storage is deployed from Google Cloud Marketplace and is subject to the terms stated therein. Google provides limited support for using Symcloud Storage with Distributed Cloud connected and might engage the third-party provider for assistance. Software updates for Symcloud Storage are included in the Distributed Cloud connected software updates.

Configure your Google Distributed Cloud connected cluster as follows to enable Symcloud Storage for virtual machines. For more information, see [Install Symcloud Storage on a Distributed Cloud connected node](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/storage#install).

  1. Create the `robin-admin` namespace with the following command:
         
         kubectl create ns robin-admin
         

  2. Obtain the Symcloud Storage license file and apply it to the cluster with the following command:
         
         kubectl apply -f LICENSE_FILE
         

Replace `LICENSE_FILE` with the path to the license file.

  3. Verify that Symcloud Storage is up and running with the following command:
         
         kubectl describe robincluster
         

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
         

**Caution:** The `blocksize` parameter is mandatory and must be set to the value of `512`.
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
         

  6. Modify the `storageprofile` for the `robin-block-immediate` storage class with the following contents and apply it to your cluster:
         
         apiVersion: cdi.kubevirt.io/v1beta1
         kind: StorageProfile
         metadata:
           name: robin-block-immediate
         spec:
           claimPropertySets:
            – accessModes:
              – ReadWriteMany
           volumeMode: Block




### Install the `virtctl` management tool

You need the [`virtctl`](https://kubevirt.io/user-guide/operations/virtctl_client_tool/) client tool to manage virtual machines on your Distributed Cloud connected cluster. To install the tool, complete the following steps:

  1. Install the `virtctl` client tool as a `kubectl` plugin:
         
         export VERSION=v1.3.1-anthos1.35-gke.39
         gcloud storage cp gs://anthos-baremetal-release/virtctl/${VERSION}/linux-amd64/virtctl ./virtctl
         sudo mv ./virtctl /usr/local/bin/virtctl
         cd /usr/local/bin
         sudo ln -s virtctl kubectl-virt
         sudo chmod a+x virtctl
         cd -

  2. Verify that the `virt` plugin is installed:
         
         kubectl plugin list

If the plugin has been successfully installed, the command's output lists `kubectl-virt` as one of the plugins.




## Create a Cloud Storage bucket for VM images

Complete the steps in this section to create a Cloud Storage bucket for your virtual machine images. The bucket uses Workload Identity Federation to grant a Kubernetes ServiceAccount direct access to the bucket. If you already have an established image repository, skip this section.

To reduce the risk of identity sameness in a multi-cluster fleet, follow the guidelines in [Best practices for fleet Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/best-practices-workload-identity) when completing the steps in this section.

  1. Complete the steps in [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets) to create a bucket.

  2. Create a Kubernetes ServiceAccount in the target virtual machine's namespace:
         
         export VM_NAMESPACE=NAMESPACE
         export KUBERNETES_SERVICEACCOUNT=KUBERNETES_SERVICEACCOUNT
         kubectl create serviceaccount ${KUBERNETES_SERVICEACCOUNT} -n ${VM_NAMESPACE}

Replace the following:

     * `NAMESPACE`: the target virtual machine's namespace.
     * `KUBERNETES_SERVICEACCOUNT`: a meaningful name for this Kubernetes ServiceAccount.
  3. Find the name of your cluster's [workload identity pool](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools) and identity provider:
         
         gcloud container fleet memberships describe MEMBERSHIP_ID \
             --project=FLEET_PROJECT_ID \
             --format="table(authority.identityProvider,authority.workloadIdentityPool,name)"

Replace the following:

     * `MEMBERSHIP_ID`: the cluster's fleet [membership name](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership). This is typically the name of your cluster.
     * `FLEET_PROJECT_ID`: the ID of the fleet host Google Cloud project.

The command returns output similar to the following:
    
    IDENTITY_PROVIDER: IDENTITY_PROVIDER
    WORKLOAD_IDENTITY_POOL: WORKLOAD_IDENTITY_POOL
    

In the output, take note of the following values:

     * `IDENTITY_PROVIDER`: the identity provider for this cluster.
     * `WORKLOAD_IDENTITY_POOL`: is the name of the [workload identity pool](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools) associated with your fleet. The name has the format `FLEET_PROJECT_ID.svc.id.goog`. For more information about the command in this step, see [Use fleet Workload Identity Federation in applications](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity#use_fleet_workload_identity).
  4. Grant the Storage Object Viewer role (`roles/storage.objectViewer`) on the bucket to the Kubernetes ServiceAccount:
         
         export BUCKET_PROJECT_ID=BUCKET_PROJECT_ID
         export FLEET_PROJECT_NUMBER=FLEET_PROJECT_NUMBER
         export KUBERNETES_SERVICEACCOUNT=KUBERNETES_SERVICEACCOUNT
         export VM_NAMESPACE=NAMESPACE
         export WI_POOL=WORKLOAD_IDENTITY_POOL
         gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PROJECT_ID}-vm-images \
            --member="principal://iam.googleapis.com/projects/${FLEET_PROJECT_NUMBER}/locations/global/workloadIdentityPools/${WI_POOL}/subject/ns/${VM_NAMESPACE}/sa/${KUBERNETES_SERVICEACCOUNT}" \
            --role="roles/storage.objectViewer" \
            --project=${BUCKET_PROJECT_ID} \
            --condition="IAM_CONDITION" \
            --condition-from-file="IAM_CONDITION_FILE"

Replace the following:

     * `BUCKET_PROJECT_ID`: the ID of the Google Cloud project that hosts the bucket.
     * `FLEET_PROJECT_NUMBER`: the project number of the fleet host Google Cloud project.
     * `KUBERNETES_SERVICEACCOUNT`: the name of the target Kubernetes ServiceAccount.
     * `NAMESPACE`: the target virtual machine's namespace.
     * `WORKLOAD_IDENTITY_POOL`: the name of your cluster's [workload identity pool](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools).
     * `IAM_CONDITION`: optional; specifies the IAM conditions to use limit access to specific clusters within the fleet. If omitted or set to `None`, no IAM conditions apply.
     * `IAM_CONDITION_FILE`: optional; specifies the file containing the IAM conditions to use limit access to specific clusters within the fleet. If omitted, no IAM conditions apply unless the `--condition` flag is specified and set to a value other than `None`.
  5. Store your images in the bucket.




You also have the option to use the legacy method using a secret generated from your Google service account's active key. For more information, see [Create a Cloud Storage bucket for virtual machine images](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/vm-servers#create_a_bucket_for_virtual_machine_images).

### Restrict access to the bucket with IAM conditions

[IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) let you specify which clusters in the fleet can access the bucket. If no IAM conditions are specified, all clusters in the fleet with the same Kubernetes ServiceAccount in the same namespace can access the bucket, posing an identity sameness risk. If you don't specify IAM conditions, you can also fall back to the legacy access mechanism that uses a secret generated from a Google service account's active key. The following is an example of how to set up and apply IAM conditions for limiting access to your bucket:

  1. Create the IAM condition file:
         
         cat <<EOF > iam_condition.yaml
         > expression: request.auth.claims.google.providerId == '$IDENTITY_PROVIDER'
         title: allow_only_this_cluster
         > EOF

  2. Apply the IAM conditions file when granting the Kubernetes ServiceAccount access to the bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PROJECT_ID}-vm-images \
           --project="${BUCKET_PROJECT_ID}" \
           --role="roles/storage.objectViewer" \
           --member="principal://iam.googleapis.com/projects/${FLEET_PROJECT_NUMBER}/locations/global/workloadIdentityPools/${WI_POOL}/subject/ns/${VM_NAMESPACE}/sa/${KUBERNETES_SERVICEACCOUNT}" \
           --condition-from-file=iam_condition.yaml




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
           url: gs://${BUCKET_PROJECT_ID}-vm-images/IMAGE_FILE_PATH
           serviceAccount: KUBERNETES_SERVICEACCOUNT
       size: DISK_SIZE
       storageClassName: robin-block-immediate

Replace the following:

  * `DISK_NAME`: the name of this virtual machine disk.
  * `NAMESPACE`: the target virtual machine's namespace.
  * `IMAGE_FILE_PATH`: the full path and name of virtual machine image file. Right-click the image in Google Cloud console and select **Copy gsutil URI** to get this path.
  * `KUBERNETES_SERVICEACCOUNT`: the Kubernetes ServiceAccount for downloading virtual machine images that you created earlier.
  * `DISK_SIZE`: the target disk size. This must be larger than the `virtual-size` value of the virtual machine image file. You can find this value with the command `qemu-img info DISK_SIZE`.



If you don't specify a `storageClassName` value, the default value specified in the `VMRuntime` resource is used.

### Create a disk from an image stored on a third-party service

You also have the option to use `http`, `https`, `S3` or an image registry to store your virtual machine images. If your storage service requires credentials for access, convert those credentials into a secret and specify that secret using the `secretRef` field.

For example:
    
    
    source:
        http/s3/registry:
           url:
           secretRef: "SECRET_NAME" # optional

Replace `SECRET_NAME` with the name of your secret.

For more information, see [HTTP/S3/GCS/Registry source](https://github.com/kubevirt/containerized-data-importer/blob/main/doc/datavolumes.md#https3gcsregistry-source).

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

Follow the steps in [Networking](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/networking) to configure the virtual networking for your virtual machines.

## Create a virtual machine

Complete the steps in this section to create a virtual machine on your Distributed Cloud connected server deployment. The instructions in this section are examples meant to illustrate configurations for different scenarios. For detailed information on configuring virtual machines, see [Create a VM with specific CPU and memory resources using VM Runtime on GDC](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/vm-runtime/compute-configurations).

Resource allocation for VMs is constrained by the hardware profiles of your Distributed Cloud connected deployment, such as G1 or G2 hardware. You can't size a single VM larger than the physical Distributed Cloud connected machine that it runs on.

### Create a virtual machine using Google Cloud console

To create a virtual machine using Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/distributed-cloud/edgezones/clusters?project=_)

  2. Select the target Google Cloud project.

  3. (Optional) If you have not already done so, sign in to the target cluster:

     1. In the left-hand navigation pane, click **Clusters**.

     2. In the **Anthos Managed Clusters** list, click the target cluster.

     3. In the information pane on the right-hand side, click **LOG IN**.

     4. In the pop-up dialog that appears, select your preferred authentication method, input your credentials, and click **LOG IN**.

  4. Go to the **Virtual Machines** page. 

[Go to Virtual Machines](https://console.cloud.google.com/distributed-cloud/edgezones/vm-management/vms?project=_)

  5. Click **CREATE**.

  6. In the **Basics** section, do the following:

     1. In the **Name** field, enter a meaningful name for the virtual machine.

     2. In the **Select cluster** field, select the target cluster for the virtual machine.

     3. In the **Namespace** field, select the target namespace.

     4. In the **OS Type** field, select the target operating system.

     5. (Optional) If you want to add one or more labels to this virtual machine's configuration, click **ADD LABEL**.

  7. In the **Machine Configuration** section, do one of the following:

     * If you want to specify the number of vCPUs and the amount of memory for this virtual machine, select **Custom Configuration** and enter the target values, then click **NEXT**.

     * If you want to use a predetermined number of vCPUs and amount of memory for this virtual machine, select **Standard Configuration** and select a machine configuration from the **Machine Type** drop-down list, then click **NEXT**.

  8. In the **Storage** section, do one of the following:

     * If you want to create a new virtual disk for this virtual machine, select **Add a new disk** and enter a meaningful name in the **Name** field, a size in gigabytes in the **GiB** field, and a URL in the **Image** field.

     * If you want to use an existing virtual disk for this virtual machine, select **Select an existing disk** and select the target disk image from the **Select a disk** drop-down list.

     * Specify whether you want the disk to be read-only and whether it will be automatically deleted when this virtual machine is deleted using the **Read-only** and **Auto delete** checkboxes.

     * Specify a virtual disk driver in the **Driver** drop-down list.

     * To add another disk to this virtual machine, click **ADD A DISK** in the **Additional disks** section.

     * Click **NEXT**.

  9. In the **Network** section, do the following:

     1. In the **Default network interface** subsection, specify the name of the primary network interface for this virtual machine in the **Interface name** field.

     2. Select the corresponding network type from the **Network type** drop-down list.

     3. Specify whether to allow external access to this network interface using the **Allow external access** checkbox. If you enable this option, you must enter a comma-separated list of ports to expose externally in the **Exposed ports** field.

     4. If you want to add one or more secondary network interfaces to this virtual machine, click **ADD A NETWORK INTERFACE**.

     5. Click **NEXT**.

  10. In the **Advanced options** section, use the **Auto-restart on update** checkbox to specify whether to restart this virtual machine after the Distributed Cloud connected software on the target cluster has been updated.

  11. In the **Firmware** section, do the following:

     1. Select the target firmware type in the **Bootloader type** field. If you select UEFI firmware, you have the option to enable secure boot using the **Secure boot** checkbox.

     2. Specify a serial number for this virtual machine in the **Serial** field.

     3. Specify a Universally Unique Identifier (UUID) for this virtual machine in the **UUID** field.

  12. In the **Cloud-init** section, specify a user data secret value in the **User data secret** field.

  13. Click **CREATE VM** to create the virtual machine.




### Create a virtual machine from a YAML file

To create a virtual machine from a YAML configuration file, do the following:

  1. In the Google Cloud console, go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/distributed-cloud/edgezones/clusters?project=_)

  2. Select the target Google Cloud project.

  3. (Optional) If you have not already done so, sign in to the target cluster:

     1. In the left-hand navigation pane, click **Clusters**.

     2. In the **Anthos Managed Clusters** list, click the target cluster.

     3. In the information pane on the right-hand side, click **LOG IN**.

     4. In the pop-up dialog that appears, select your preferred authentication method, input your credentials, and click **LOG IN**.

  4. Go to the **Virtual Machines** page. 

[Go to Virtual Machines](https://console.cloud.google.com/distributed-cloud/edgezones/vm-management/vms?project=_)

  5. Click **CREATE WITH YAML**.

  6. In the **Select cluster** field, select the target cluster for the virtual machine.

  7. Paste the virtual machine configuration in YAML format into the YAML field. For details about the supported YAML fields, see the Virtual machine specification reference.

  8. Click **CREATE**.




### Create a virtual machine from a bootable disk image

To create a virtual machine from a bootable disk image, apply the following configuration to your cluster. To customize this configuration, such as the CPU, memory, or network options, see the Virtual machine specification reference:
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    metadata:
      name: my-virtual-machine
      namespace: NAMESPACE
    spec:
      osType: Linux/Windows
      # guestEnvironment: {} # uncomment this line to disable guest environment
      priorityClassName: PRIORITY_CLASS
      compute:
        cpu:
          vcpus: 6
        memory:
          capacity: 8Gi
      interfaces:
        - name: eth0
          networkName: NETWORK_NAME
          ipAddresses:
            - IP_ADDRESS/PREFIX
      disks:
        - virtualMachineDiskName: DISK_NAME
          boot: true
        - virtualMachineDiskName: DISK_NAME

Replace the following:

  * `NAMESPACE`: the target namespace.
  * `PRIORITY_CLASS`: the priority class for this virtual machine. A priority class is a range of priority values. Use `kubectl get priorityclass` to see a list of supported priority classes. Higher scheduling priority reduces the chance of VM eviction when node resources are constrained. If omitted, the virtual machine gets the default lowest priority value.
  * `NETWORK_NAME`: the name of the L2 network to attach the VM interface to.
  * `DISK_NAME`: the names of this virtual machine's disks.
  * `vcpus`: the number of vCPUs to assign to the VM.
  * `capacity`: the amount of memory to assign to the VM. For example, `4Gi` or `8Gi`.
  * `ipAddresses`: optional; provides static IP assignment for the virtual machine. If the underlying L2 network supports external DHCP, you can omit `ipAddresses` to allow dynamic allocation.



### Use the `cloud-init` API to initialize VMs

The `cloud-init` API is a standard way to initialize a cloud VM. Use `cloud-init` to set up files, users, and other aspects of your VM.

To ensure compatibility, validate your `cloud-init` startup routines. Before using the configuration in production, apply the configuration to a test VM to ensure that it initializes successfully.

The following examples are generic and must be tested in your environment.

#### Automate VM configuration with `cloud-init` user data

VM Runtime on GDC supports `cloud-init` user data for Linux VMs. You can specify user data as a plain-text string, a base64-encoded string, or by referencing a Kubernetes Secret.

To ensure that your VM initializes correctly, validate all user data configurations before deploying them to a production environment.

The following example shows a `VirtualMachine` manifest that includes plain-text `cloud-init` user data to run a command when the VM boots:
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    metadata:
      name: VM_NAME
    spec:
      compute:
        cpu:
          vcpus: 2
        memory:
          capacity: 4Gi
      osType: Linux
      cloudInit:
        noCloud:
          userData: |
            #cloud-config
            runcmd:
              - echo "Hello World" > /tmp/hello.txt

Replace `VM_NAME` with the name of the virtual machine.

To create the VM with `cloud-init` data, save the manifest as `vm-cloud-init.yaml`, and apply it to your cluster by running the [`kubectl apply`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/) command:
    
    
    kubectl apply -f vm-cloud-init.yaml
    

#### Troubleshoot `cloud-init`

If you encounter issues with `cloud-init`, check the logs within the VM. You can usually find the logs in the following directories:

  * `/var/log/cloud-init.log`
  * `/var/log/cloud-init-output.log`



### Create a virtual machine from an ISO optical disc image

You can create a Windows virtual machine (VM) that boots from an ISO image using VM Runtime on GDC. This capability lets you migrate legacy Windows-based enterprise applications, specialized third-party software, or custom point-of-sale systems directly to your Distributed Cloud connected clusters.

Images used for VM disks are imported from a Distributed Cloud connected image bucket. Before creating the manifests, you must download the Windows installation ISO and the [KubeVirt `virtio` drivers ISO](https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/virtio-win.iso) and upload them to your image bucket. We recommend that you maintain a verified copy of the drivers ISO in an internal repository or prestage it in Cloud Storage to ensure reliable, repeatable virtual machine builds.

#### Create the manifests

To boot from a Windows ISO image, you need the following manifests:

  * A `VirtualMachineDisk` containing the Windows ISO.
  * A `VirtualMachineDisk` containing the KubeVirt Windows `virtio` drivers.
  * An empty `VirtualMachineDisk` to serve as the boot disk where Windows will be installed.



The following examples show the `VirtualMachineDisk` manifests for the three required disks.

In the manifests, replace the following:

  * `BUCKET_PROJECT_ID`: The project ID where your image bucket resides.
  * `KUBERNETES_SERVICEACCOUNT`: The Kubernetes ServiceAccount with permissions to read from the bucket.



The PVC `size` requested in the manifests must always be greater than or equal to the ISO's exact virtual size.

**Windows ISO disk**
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachineDisk
    metadata:
      name: windows-iso
    spec:
      size: 10Gi
      storageClassName: robin-block-immediate
      diskType: cdrom
      source:
        gcs:
          url: gs://BUCKET_PROJECT_ID-vm-images/windows.iso
          serviceAccount: KUBERNETES_SERVICEACCOUNT

**VirtIO drivers disk**
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachineDisk
    metadata:
      name: virtio-driver
    spec:
      size: 1Gi
      storageClassName: robin-block-immediate
      diskType: cdrom
      source:
        gcs:
          url: gs://BUCKET_PROJECT_ID-vm-images/virtio-win.iso
          serviceAccount: KUBERNETES_SERVICEACCOUNT

**Empty boot disk**
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachineDisk
    metadata:
      name: windows-vm-boot-dv
    spec:
      size: 40Gi
      storageClassName: robin-block-immediate

#### Create the disks

To create these disks, save the `VirtualMachineDisk` manifests, and apply them to your cluster by running the [`kubectl apply`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/) command:
    
    
    kubectl apply -f windows-iso.yaml
    kubectl apply -f virtio-driver.yaml
    kubectl apply -f windows-vm-boot-dv.yaml
    

#### Create a Windows VM

To create a Windows VM, create a manifest that defines the VM and references the disks. The VM boots from the ISO disk to start the installation.

The following example shows a `VirtualMachine` manifest:
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VirtualMachine
    metadata:
      labels:
        kubevirt.io/vm: windows-vm
      name: windows-vm
    spec:
      osType: Windows
      disks:
        - virtualMachineDiskName: windows-vm-boot-dv
          boot: true
        - virtualMachineDiskName: windows-iso
        - virtualMachineDiskName: virtio-driver
      compute:
        cpu:
          vcpus: 2
        memory:
          capacity: 4Gi
      interfaces:
        - name: eth0
          networkName: NETWORK_NAME
          default: true
          ipAddresses:
            - IP_ADDRESS/PREFIX

**Note:** The `ipAddresses` field provides static IP assignment. If the underlying L2 network supports external DHCP, you can omit `ipAddresses` to allow dynamic allocation.

To create the VM, save the manifest as `windows-vm.yaml`, and apply it to your cluster by running the [`kubectl apply`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/) command:
    
    
    kubectl apply -f windows-vm.yaml
    

#### Connect and complete installation

To connect and complete the installation, follow these steps:

  1. To connect to the VM using VNC, use the `virtctl` tool or `kubectl virt` plugin:
         
         virtctl vnc windows-vm
         

Or, if you installed `virtctl` as a `kubectl` plugin:
         
         kubectl virt vnc windows-vm
         

For more information about `virtctl`, see the [KubeVirt documentation](https://kubevirt.io/user-guide/operations/virtctl_client_tool/).

  2. Follow the instructions displayed by the Windows installer. When prompted, select **Custom install**.

  3. When prompted, load the `virtio` drivers for storage and network, browsing to the attached `virtio-driver` disk.

  4. Complete the installation.




#### Access through Remote Desktop Protocol

After you install and enable Remote Desktop Protocol (RDP) in the guest OS, you can access the VM through RDP.

Because the virtual machine is attached to an L2 network, it is directly reachable from outside the cluster using its assigned IP address (for example, `10.223.237.10`). Connect to this IP address on port 3389 using an RDP client. Ensure that the L2 internal IP address is reachable from your client machine through your corporate firewall and routing rules.

### Create a virtual machine with GPU support

Complete the steps described on this page to create a virtual machine configured to meet your business requirements, then complete the steps in [Configure a virtual machine to use GPU resources](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/gpu#gpu-vm).

### Virtual machine specification reference

The following table describes the key fields in the `VirtualMachine` specification. Use these fields when configuring a virtual machine YAML manifest to apply to your cluster using `kubectl apply`, or when using the **Create with YAML** option in the Google Cloud console.

Field | Description | Required  
---|---|---  
`apiVersion` | Must be `vm.cluster.gke.io/v1`. | Required  
`kind` | Must be `VirtualMachine`. | Required  
`metadata.name` | A unique name for the virtual machine. | Required  
`metadata.namespace` | The Kubernetes namespace where the VM runs. | Required  
`spec.osType` | The guest operating system type. Supported values: `Linux` and `Windows`. | Required  
`spec.guestEnvironment` | Configures the guest environment. If omitted, the guest environment is enabled by default. To disable, set to `{}`. | Optional  
`spec.priorityClassName` | The priority class for the VM. Higher priority reduces the chance of eviction. | Optional  
`spec.compute` | Configures the compute resources for the VM. | Required  
`spec.compute.cpu.vcpus` | Number of vCPUs to allocate. Accepted values are 1 to 96. | Required  
`spec.compute.memory.capacity` | Memory capacity, for example, `8Gi`. | Required  
`spec.interfaces` | List of network interfaces for the VM. | Required  
`spec.interfaces[].name` | Name of the interface, for example, `eth0`. | Required  
`spec.interfaces[].networkName` | Name of the subnetwork to connect to, which maps to a `Network` resource in the cluster. | Required  
`spec.interfaces[].ipAddresses` | Static IP addresses to assign to this interface. If the subnetwork does not have DHCP enabled, you must specify a static IP address. | Optional  
`spec.disks` | List of disks to attach to the VM. | Required  
`spec.disks[].virtualMachineDiskName` | Name of the `VirtualMachineDisk` resource. | Required  
`spec.disks[].boot` | Set to `true` for the boot disk. Only one disk can be marked as bootable. | Optional  
  
## Access a virtual machine

Complete the steps in this section to access a virtual machine running on your Distributed Cloud connected server deployment.

### Network requirements for direct access

To access a virtual machine directly from your local network without using a Kubernetes `LoadBalancer` service, you must configure the logical and physical networking components. Distributed Cloud connected automatically manages in-cluster network resources, but you need to configure the external network and the VM interface.

  1. **Configure subnetwork (VLAN)** : Create a subnetwork with a specific VLAN ID using the Distributed Cloud Edge Network API, using `gcloud` or the API. Distributed Cloud connected automatically syncs this configuration to your cluster. You don't need to manually create Kubernetes network resources. See [Create and manage subnetworks](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/subnetworks).

  2. **Configure your local network** : Your network administrator must configure the physical switches and routers connected to the Distributed Cloud connected servers to:

     * Allow the configured VLAN ID on the switch ports (VLAN trunking).
     * Enable routing between your local network and the subnetwork. If [Border Gateway Protocol (BGP)](https://en.wikipedia.org/wiki/Border_Gateway_Protocol), a dynamic routing protocol, is configured on your Distributed Cloud connected routers, these routes are advertised automatically after the subnetwork is created. Otherwise, you must configure static routes on your physical routers to route traffic for the subnetwork's IP range (CIDR) to the Distributed Cloud connected nodes.
  3. **Configure VM interface** : In your `VirtualMachine` YAML configuration, configure the VM to use this subnetwork by specifying the network name in the `spec.interfaces` field. For more information, see Virtual machine specification reference.




### Obtain access credentials for Linux VMs

If you don't already have credentials for accessing the virtual machine, complete the steps in this section to obtain them using the Linux guest environment feature.

  1. Enable the Linux guest environment for the target virtual machine by applying the following configuration to your cluster:
         
         kind: VirtualMachine
         metadata:
          name: my-virtual-machine
          namespace: my-vm-namespace
         spec:
          osType: Linux
          guestEnvironment: // enabled by default; disable with guestEnvironment: {}
            accessManagement:
             enable: true

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
  4. To check the status of the access request, run the [`kubectl get`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/) command:
         
         kubectl get vmar
         

When the command returns a `Configured` status, proceed to the next step.

  5. Access the virtual machine with SSH. If the virtual machine is connected to your local network, access it directly using SSH:
         
         ssh USERNAME@VM_IP_ADDRESS -i PATH_TO_KEY

Replace the following:

     * `USERNAME`: the username to sign in with, for example, the user configured in the `VirtualMachineAccessRequest` resource.
     * `VM_IP_ADDRESS`: the IP address of your virtual machine.
     * `PATH_TO_KEY`: the path to the private SSH key corresponding to the public key generated in previous steps.



### Use RDP to access a Windows VM

To access a Windows VM using Remote Desktop Protocol (RDP) from your local network, enable RDP in the guest OS, ensure that the VM is network-accessible, and set up user credentials.

#### Prerequisites

**Enable RDP in Windows** : RDP must be enabled within the Windows guest OS. If RDP is not yet enabled, use a Virtual Network Computing, or VNC, console to access the VM screen directly and enable it. The `kubectl virt vnc` command opens a graphical viewer window on your local workstation and requires a VNC viewer client, such as Remote Viewer or VNC Viewer, installed on your workstation:
    
    
    kubectl virt vnc VM_NAME -n NAMESPACE

Replace the following:

  * `VM_NAME`: the name of your Windows VM.
  * `NAMESPACE`: the namespace of the VM.



#### Connect using RDP

  1. To get the IP address of the VM, run the [`kubectl get`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/) command:
         
         kubectl get vmi VM_NAME -n NAMESPACE -o jsonpath='{.status.interfaces[*].ipAddress}'

Replace the following:

     * `VM_NAME`: the name of your Windows VM.
     * `NAMESPACE`: the namespace of the VM.

Make a note of the IP address belonging to your routed subnetwork from the output.

  2. Use a standard RDP client, such as Remote Desktop Connection on Windows or Remmina on Linux, to connect to the retrieved IP address on port `3389`.

  3. Use the username and password to sign in.




## Start, restart, or stop a virtual machine

Use the following commands to start, restart, or stop a virtual machine:

  * **Start a virtual machine:** `kubectl virt start vm``VM_NAME``-n``NAMESPACE`
  * **Restart a virtual machine:** `kubectl virt restart vm``VM_NAME``-n``NAMESPACE`
  * **Stop a virtual machine:** `kubectl virt stop vm``VM_NAME``-n``NAMESPACE`



Replace the following:

  * `VM_NAME`: the name of the target virtual machine.
  * `NAMESPACE`: the target namespace.



### Start or stop a virtual machine using Google Cloud console

  1. In the Google Cloud console, go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/distributed-cloud/edgezones/clusters?project=_)

  2. Select the target Google Cloud project.

  3. (Optional) If you have not already done so, sign in to the target cluster:

     1. In the left-hand navigation pane, click **Clusters**.

     2. In the **Anthos Managed Clusters** list, click the target cluster.

     3. In the information pane on the right-hand side, click **LOG IN**.

     4. In the dialog that appears, select your preferred authentication method, input your credentials, and click **LOG IN**.

  4. Go to the **Virtual Machines** page. 

[Go to Virtual Machines](https://console.cloud.google.com/distributed-cloud/edgezones/vm-management/vms?project=_)

  5. In the list of virtual machines, select the checkbox(es) for the target virtual machine(s).

  6. At the top of the page, click **START** or **STOP** as applicable.




## View the status of a virtual machine using Google Cloud console

  1. In the Google Cloud console, go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/distributed-cloud/edgezones/clusters?project=_)

  2. Select the target Google Cloud project.

  3. (Optional) If you have not already done so, sign in to the target cluster:

     1. In the left-hand navigation pane, click **Clusters**.

     2. In the **Anthos Managed Clusters** list, click the target cluster.

     3. In the information pane on the right-hand side, click **LOG IN**.

     4. In the pop-up dialog that appears, select your preferred authentication method, input your credentials, and click **LOG IN**.

  4. Go to the **Virtual Machines** page. 

[Go to Virtual Machines](https://console.cloud.google.com/distributed-cloud/edgezones/vm-management/vms?project=_)

  5. Click the target virtual machine.

  6. In the page that appears, click the **Details** , **Events** , and **YAML** tab to view the corresponding information about this virtual machine.




## Modify a virtual machine

To modify a virtual machine, you must delete it and re-create it with the updated configuration.

## Delete a virtual machine using Google Cloud console

  1. In the Google Cloud console, go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/distributed-cloud/edgezones/clusters?project=_)

  2. Select the target Google Cloud project.

  3. (Optional) If you have not already done so, sign in to the target cluster:

     1. In the left-hand navigation pane, click **Clusters**.

     2. In the **Anthos Managed Clusters** list, click the target cluster.

     3. In the information pane on the right-hand side, click **LOG IN**.

     4. In the dialog that appears, select your preferred authentication method, input your credentials, and click **LOG IN**.

  4. go to the **Virtual Machines** page. 

[Go to Virtual Machines](https://console.cloud.google.com/distributed-cloud/edgezones/vm-management/vms?project=_)

  5. In the list of virtual machines, select the checkbox for the target virtual machine.

  6. At the top of the page, click **DELETE**.

  7. In the confirmation dialog that appears, enter the virtual machine's name and click **DELETE**.




## What's next

  * [Deploy workloads on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/deploy)
  * [Manage GPU workloads](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/gpu)
  * [Manage zones](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/zones)
  * [Manage machines](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/machines)
  * [Manage clusters](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/clusters)
  * [Manage node pools](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/nodepools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
