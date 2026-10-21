---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/virtual-machines/
title: Manage virtual machines \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:31:20.216046+00:00
---

# Manage virtual machines  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/virtual-machines/

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
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/overview)



Send feedback 

#  Manage virtual machines Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage virtual machines on your Google Distributed Cloud connected deployment running [VM Runtime on Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.12.0/vm-runtime/enable-disable). You must be familiar with VM Runtime on GDC before completing the steps on this page. For a list of supported guest operating systems, see [Verified guest operating systems for VM Runtime on GDC](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.12.0/vm-runtime/guest-os).

To learn how virtual machines serve as an essential component of the Distributed Cloud connected platform, see [Extending GKE Enterprise to manage on-premises edge VMs](https://cloud.google.com/blog/topics/anthos/extending-anthos-to-manage-on-premises-edge-vms-now-generally-available).

Distributed Cloud connected clusters support virtual machine webhooks. This allows Distributed Cloud connected to validate user requests made to the local Kubernetes API server. Rejected requests generate detailed information on the reason for rejection.

## Configure Symcloud Storage

Google Distributed Cloud connected uses [Rakuten Symcloud Storage](https://symphony.rakuten.com/insight/datasheet/symcloud-storage), as their storage solution. Symcloud Storage is a third-party solution that acts as a local storage abstraction layer on each Distributed Cloud connected node and makes its local storage available to workloads running on other Distributed Cloud connected nodes.

Symcloud Storage is deployed from Google Cloud Marketplace and is subject to the terms stated therein. Google provides limited support for using Symcloud Storage with Distributed Cloud connected and might engage the third-party provider for assistance. Software updates for Symcloud Storage are included in the Distributed Cloud connected software updates.

Configure your Google Distributed Cloud connected cluster as follows to enable Symcloud Storage for virtual machines. For more information, see [Install Symcloud Storage on a Distributed Cloud connected node](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/storage#install).

  1. Create the `robin-admin` namespace with the following command:
         
         kubectl create ns robin-admin
         

  2. Obtain the Symcloud Storage license file and apply it to the cluster with the following command:
         
         kubectl apply LICENSE_FILE
         

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
         
         export VERSION=GDC_SO_VERSION
         gcloud storage cp gs://anthos-baremetal-release/virtctl/${VERSION}/linux-amd64/virtctl ./virtctl
         sudo mv ./virtctl /usr/local/bin/virtctl
         cd /usr/local/bin
         sudo ln -s virtctl kubectl-virt
         sudo chmod a+x virtctl
         cd -

Replace `GDC_SO_VERSION` with the target version of Distributed Cloud software-only.

  2. Verify that the `virt` plugin is installed:
         
         kubectl plugin list

If the plugin has been successfully installed, the command's output lists `kubectl-virt` as one of the plugins.




## Create a Cloud Storage bucket for VM images

Complete the steps in this section to create a Cloud Storage bucket for your virtual machine images. The bucket uses Workload Identity Federation to bind a Kubernetes service account to the corresponding Google Cloud service account to access the bucket; in other words, the Kubernetes service account impersonates the Google Cloud service account. If you already have an established image repository, skip this section.

To reduce the risk of identity sameness in a multi-cluster fleet, follow the guidelines in [Best practices for fleet Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/best-practices-workload-identity) when completing the steps in this section.

  1. Complete the steps in [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets) to create a bucket.

  2. Create a Google Cloud service account for accessing the bucket:
         
         export GSA_PROJECT_ID=GSA_PROJECT_ID
         export GSA_NAME=GSA_NAME
         gcloud iam service-accounts create ${GSA_NAME}

Replace the following:

     * `GSA_NAME`: a meaningful name for this Google Cloud service account.
     * `GSA_PROJECT_ID`: the ID of the Google Cloud project that hosts the target Google Cloud service account.
  3. Grant the Google Cloud service account permissions to access the bucket:
         
         export BUCKET_PROJECT_ID=BUCKET_PROJECT_ID
         export GSA_NAME=GSA_NAME
         gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PROJECT_ID}-vm-images \
            --member="serviceAccount:${GSA_NAME}@${GSA_PROJECT_ID}.iam.gserviceaccount.com" \
            --role="roles/storage.objectViewer" \
            --project=${BUCKET_PROJECT_ID}

Replace the following:

     * `GSA_NAME`: the name of the target Google Cloud service account.
     * `BUCKET_PROJECT_ID`: the ID of the Google Cloud project that hosts the bucket.
     * `GSA_PROJECT_ID`: the ID of the Google Cloud project that hosts the target Google Cloud service account.
  4. Create a Kubernetes service account in the target virtual machine's namespace to bind to your Google Cloud service account:
         
         export GSA_PROJECT_ID=GSA_PROJECT_ID
         export VM_NAMESPACE=NAMESPACE
         export KSA_NAME=KSA_NAME
         export GSA_EMAIL=${GSA_NAME}@${GSA_PROJECT_ID}.iam.gserviceaccount.com
         kubectl create serviceaccount ${KSA_NAME} -n ${VM_NAMESPACE}
         kubectl annotate serviceaccount ${KSA_NAME} gsaEmail=${GSA_EMAIL} -n ${VM_NAMESPACE}

Replace the following:

     * `GSA_PROJECT_ID`: the ID of the Google Cloud project that hosts the target Google Cloud service account.
     * `NAMESPACE`: the target virtual machine's namespace.
     * `KSA_NAME`: a meaningful name for this Kubernetes service account.
     * `GSA_NAME`: the name of the corresponding Google Cloud service account.
  5. Find the name of your cluster's [workload identity pool](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools) and identity provider:
         
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
  6. Bind the Kubernetes service account to the Google Cloud service account to set up the impersonation:
         
         export GSA_PROJECT_ID=GSA_PROJECT_ID
         export GSA_NAME=GSA_NAME
         export KSA_NAME=KSA_NAME
         export VM_NAMESPACE=NAMESPACE
         export WI_POOL=WORKLOAD_IDENTITY_POOL
         gcloud iam service-accounts add-iam-policy-binding ${GSA_NAME}@${GSA_PROJECT_ID}.iam.gserviceaccount.com \
            --project=${GSA_PROJECT_ID} \
            --role=roles/iam.workloadIdentityUser \
            --member="serviceAccount:${WI_POOL}[${VM_NAMESPACE}/${KSA_NAME}]"
            --condition="IAM_CONDITION"
            --condition-from-file="IAM_CONDITION_FILE"

Replace the following:

     * `GSA_PROJECT_ID`: the ID of the Google Cloud project that hosts the target Google Cloud service account.
     * `GSA_NAME`: the name of the corresponding Google Cloud service account.
     * `KSA_NAME`: the name of the target Kubernetes service account.
     * `NAMESPACE`: the target virtual machine's namespace.
     * `WORKLOAD_IDENTITY_POOL`: the name of your cluster's [workload identity pool](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools).
     * `IAM_CONDITION`: optional; specifies the IAM conditions to use limit access to specific clusters within the fleet. If omitted or set to `None`, no IAM conditions apply.
     * `IAM_CONDITION_FILE`: optional; specifies the file containing the IAM conditions to use limit access to specific clusters within the fleet. If omitted, no IAM conditions apply unless the `--condition` flag is specified and set to a value other than `None`.
  7. Store your images in the bucket.




You also have the option to use the legacy method using a secret generated from your Google service account's active key. For more information, see [Create a Cloud Storage bucket for virtual machine images](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/vm-servers#create_a_bucket_for_virtual_machine_images).

### Restrict access to the bucket with IAM conditions

[IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) let you specify which clusters in the fleet can access the bucket. If no IAM conditions are specified, all clusters in the fleet with the same Kubernetes service account in the same namespace can access the bucket, posing an identity sameness risk. If you don't specify IAM conditions, you can also fall back to the legacy access mechanism that uses a secret generated from a Google service account's active key. The following is an example of how to set up and apply IAM conditions for limiting access to your bucket:

  1. Create the IAM condition file:
         
         cat <<EOF > iam_condition.yaml
         > expression: request.auth.claims.google.providerId == '$IDENTITY_PROVIDER'
         title: allow_only_this_cluster
         > EOF

  2. Apply the IAM conditions file when binding the GSA to the KSA. Run the following command in your GSA Google Cloud project:
         
         gcloud iam service-accounts add-iam-policy-binding "${GSA_NAME}@${GSA_PROJECT_ID}.iam.gserviceaccount.com" \
           --project="${GSA_PROJECT_ID}" \
           --role=roles/iam.workloadIdentityUser \
           --member="serviceAccount:${WI_POOL}[${VM_NAMESPACE}/${KSA_NAME}]" \
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
           serviceAccount: KSA_NAME
       size: DISK_SIZE
       storageClassName: robin-block-immediate

Replace the following:

  * `DISK_NAME`: the name of this virtual machine disk.
  * `NAMESPACE`: the target virtual machine's namespace.
  * `IMAGE_FILE_PATH`: the full path and name of virtual machine image file. Right-click the image in Google Cloud console and select **Copy gsutil URI** to get this path.
  * `KSA_NAME`: the Kubernetes service account for downloading virtual machine images that you created earlier.
  * `DISK_SIZE`: the target disk size. This must be larger than the `virtual-size` value of the virtual machine image file. You can find this value with the command `qemu-img info DISK_SIZE`.



If you don't specify a `storageClassName` value, the default value specified in the `VMRuntime` resource is used.

### Create a disk from an image stored on a third-party service

You also have the option to use `http`, `https`, `S3` or an image registry to store your virtual machine images. If your storage service requires credentials for access, convert those credentials into a secret and specify that secret using the `secretRef` field. For example:
    
    
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

Follow the steps in [Networking](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/networking) to configure the virtual networking for your virtual machines.

## Create a virtual machine

Complete the steps in this section to create a virtual machine on your Distributed Cloud connected server deployment. The instructions in this section are examples meant to illustrate configurations for different scenarios. For detailed information on configuring virtual machines, see [Create a VM with specific CPU and memory resources using VM Runtime on GDC](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.12.0/vm-runtime/compute-configurations).

### Create a virtual machine using Google Cloud console

To create a virtual machine using Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/distributed-cloud/edgezones/clusters?project=_)

  2. Select the target Google Cloud project.

  3. (Optional) If you have not already done so, log into the target cluster:

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

  10. In the **Advanced options** section, use the **Auto-restart on update** checkbox to specify whether to restart this virtual machine after the  
Distributed Cloud connected software on the target cluster has been updated.

  11. In the **Firmware** section, do the following:

     1. Select the target firmware type in the **Bootloader type** field. If you select UEFI firmware, you have the option to enable secure boot using the **Secure boot** checkbox.

     2. Specify a serial number for this virtual machine in the **Serial** field.

     3. Specify a Universally Unique Identifier (UUID) for this virtual machine in the **UUID** field.

  12. In the **Cloud-init** section, do the following:

     * Specify a network data secret value in the **Network data secret** field.

     * Specify a user data secret value in the **User data secret** field.

  13. Click **CREATE VM** to create the virtual machine.




### Create a virtual machine from a YAML file

To create a virtual machine from a YAML configuration file, do the following:

  1. In the Google Cloud console, go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/distributed-cloud/edgezones/clusters?project=_)

  2. Select the target Google Cloud project.

  3. (Optional) If you have not already done so, log into the target cluster:

     1. In the left-hand navigation pane, click **Clusters**.

     2. In the **Anthos Managed Clusters** list, click the target cluster. 

     3. In the information pane on the right-hand side, click **LOG IN**.

     4. In the pop-up dialog that appears, select your preferred authentication method, input your credentials, and click **LOG IN**.

  4. Go to the **Virtual Machines** page. 

[Go to Virtual Machines](https://console.cloud.google.com/distributed-cloud/edgezones/vm-management/vms?project=_)

  5. Click **CREATE WITH YAML**.

  6. In the **Select cluster** field, select the target cluster for the virtual machine.

  7. Paste the virtual machine configuration in YAML format into the YAML field.

  8. Click **CREATE**.




### Create a virtual machine from a bootable disk image

To create a virtual machine from a bootable disk image, apply the following configuration to your cluster:
    
    
    kind: VirtualMachine
    metadata:
      name: my-virtual-machine
      namespace: NAMESPACE
    spec:
      osType: Linux/Windows
      guestEnvironment: {} // comment out this line to enable guest environment for access management
      priorityClassName: PRIORITY_CLASS
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
        - virtualMachineDiskName: DISK_NAME
          boot: true
        - virtualMachineDiskName: DISK_NAME

Replace the following:

  * `NAMESPACE`: the target namespace.
  * `PRIORITY_CLASS`: the priority class for this virtual machine. A priority class is a range of priority values; use `kubectl get priorityclass` to get a list of the supported priority classes. We recommend assigning a priority class that corresponds to a priority value between `5,001,000` and `1,000,000,000`. Higher priority values reduce the chance of virtual machine eviction when the system's overloaded. If omitted, the virtual machine gets the default lowest priority value.
  * `DISK_NAME`: the names of this virtual machine's disks.



### Create a virtual machine from an ISO optical disc image

To create a virtual machine from an ISO optical disc image, complete the steps in [Create a Windows VM from ISO image in Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.12.0/vm-runtime/windows-vm).

### Create a virtual machine with GPU support

Complete the steps described on this page to create a virtual machine configured to meet your business requirements, then complete the steps in [Configure a virtual machine to use GPU resources](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/gpu#gpu-vm).

## Access a virtual machine

Complete the steps in this section to access a virtual machine running on your Distributed Cloud connected server deployment.

### Obtain access credentials

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



### Start or stop a virtual machine using Google Cloud console

  1. In the Google Cloud console, go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/distributed-cloud/edgezones/clusters?project=_)

  2. Select the target Google Cloud project.

  3. (Optional) If you have not already done so, log into the target cluster:

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

  3. (Optional) If you have not already done so, log into the target cluster:

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

  3. (Optional) If you have not already done so, log into the target cluster:

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

  * [Deploy workloads on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/deploy)
  * [Manage GPU workloads](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/gpu)
  * [Manage zones](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/zones)
  * [Manage machines](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/machines)
  * [Manage clusters](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/clusters)
  * [Manage node pools](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/nodepools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
