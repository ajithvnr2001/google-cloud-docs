---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/virtual-machines/
title: Manage virtual machines on Distributed Cloud connected racks \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:13:02.404379+00:00
---

# Manage virtual machines on Distributed Cloud connected racks  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/virtual-machines/

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
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/overview)



Send feedback 

#  Manage virtual machines on Distributed Cloud connected racks Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage virtual machines on Google Distributed Cloud connected racks running [VM Runtime on Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/enable-disable). You must be familiar with VM Runtime on GDC before completing the steps on this page. For a list of supported guest operating systems, see [Verified guest operating systems for VM Runtime on GDC](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/guest-os).

**Note:** Virtual machine workloads are only supported on legacy Distributed Cloud connected rack hardware ("Config 1" and "Config 2") and on [Distributed Cloud connected servers](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/vm-servers). Virtual machine workloads are not supported on the refreshed Distributed Cloud connected rack hardware.

To learn how virtual machines serve as an essential component of the Distributed Cloud connected platform, see [Extending GKE Enterprise to manage on-premises edge VMs](https://cloud.google.com/blog/topics/anthos/extending-anthos-to-manage-on-premises-edge-vms-now-generally-available).

Distributed Cloud connected clusters support virtual machine webhooks. This allows Distributed Cloud connected to validate user requests made to the local Kubernetes API server. Rejected requests generate detailed information on the reason for rejection.

## Enable VM Runtime on GDC support on Distributed Cloud connected

By default, VM Runtime on GDC virtual machine support is disabled on Distributed Cloud connected. To enable it, complete the steps in this section. The instructions in this section assume that you have a fully functioning Distributed Cloud connected cluster.

  1. Modify the `VMRuntime` custom resource with the following contents and apply it to your cluster:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VMRuntime
         metadata:
           name: vmruntime
         spec:
           # Enable Anthos VM Runtime support
           enabled: true
           # vmImageFormat defaults to "raw" if not set
           vmImageFormat: "raw"
           # Set node grace period to 55 seconds;
           haPolicy:
             defaultRecoveryStrategy: Reschedule
             nodeHeartbeatInterval: 15s
             nodeMonitorGracePeriod: 55s

Do not change the value of the `vmImageFormat` parameter. Distributed Cloud connected does not support any other virtual disk formats.

This process typically takes several minutes to complete. 

Do not change the value of the `vmImageFormat` parameter. Distributed Cloud connected does not support any other virtual disk formats.

This process typically takes several minutes to complete.

  2. Use the following command to verify that the `VMRuntime` custom resource has been applied to your cluster:
         
         kubectl get vmruntime -o yaml

The command returns output similar to the following example:
         
         - apiVersion: vm.cluster.gke.io/v1
            kind: VMRuntime
            metadata:
              name: vmruntime
              ...
            spec:
              enabled: true
              vmImageFormat: raw
            status:
              ...
            ready: true
              ...
         

  3. Use the following command to verify that VM Runtime on GDC virtual machine support has been enabled on your cluster:
         
         kubectl get pods -n vm-system

The command returns output showing the VM Runtime on GDC subsystem Pods running on your cluster, similar to the following example:
         
         NAME                                                READY   STATUS         RESTARTS        AGE
         cdi-apiserver-6c76c6cf7b-n68wn                      1/1     Running        0               132m
         cdi-deployment-f78fd599-vj7tv                       1/1     Running        0               132m
         cdi-operator-65c4df9647-fcb9d                       1/1     Running        0               134m
         cdi-uploadproxy-7765ffb694-6j7bf                    1/1     Running        0               132m
         macvtap-fjfjr                                       1/1     Running        0               134m
         virt-api-77dd99dbbb-bs2fb                           1/1     Running        0               132m
         virt-api-77dd99dbbb-pqc27                           1/1     Running        0               132m
         virt-controller-5b44dbbbd7-hc222                    1/1     Running        0               132m
         virt-controller-5b44dbbbd7-p8xkk                    1/1     Running        0               132m
         virt-handler-n76fs                                  1/1     Running        0               132m
         virt-operator-86565697d9-fpxqh                      2/2     Running        0               134m
         virt-operator-86565697d9-jnbt7                      2/2     Running        0               134m
         vm-controller-controller-manager-7844d5fb7b-72d8m   2/2     Running        0               134m
         vmruntime-controller-manager-845649c847-m78r9       2/2     Running        0               175m
         




### Install the `virtctl` management tool

You need the [`virtctl`](https://kubevirt.io/user-guide/operations/virtctl_client_tool/) client tool to manage virtual machines on your Distributed Cloud connected cluster. To install the tool, complete the following steps:

  1. Install the `virtctl` client tool as a `kubectl` plugin:
         
         export VERSION=v0.59.0-anthos1.28-gke.8
         gcloud storage cp gs://anthos-baremetal-release/virtctl/${VERSION}/linux-amd64/virtctl /usr/local/bin/virtctl
         cd /usr/local/bin
         sudo ln -s virtctl kubectl-virt
         sudo chmod a+x virtctl
         cd -

  2. Verify that the `virt` plugin is installed:
         
         kubectl plugin list

If the plugin has been successfully installed, the command's output lists `kubectl-virt` as one of the plugins.




## Provision a virtual machine on Distributed Cloud connected

This section provides configuration examples that illustrate how to provision a Linux virtual machine and a Windows virtual machine on a Distributed Cloud connected cluster with the Symcloud Storage abstraction layer.

Note that you cannot create a virtual machine on a Distributed Cloud connected cluster directly by using the `kubectl virt` command because Distributed Cloud connected does not provide file system storage to virtual machines.

Before completing the steps in this section, you must first complete the steps in [Configure Distributed Cloud connected for Symcloud Storage](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/storage). If you later disable Symcloud Storage on the cluster, virtual machines configured to use Symcloud Storage will fail.

### Provision a Linux virtual machine on Distributed Cloud connected

The following example illustrates how to provision a Linux virtual machine with Symcloud Storage running Ubuntu Server 22.04. The installation source is the Ubuntu Server 22.04 ISO disc image.

  1. Create a `VirtualMachineDisk` resource with the following contents for the Ubuntu Server installation disc image, and then apply it to your cluster:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineDisk
         metadata:
           name: ubuntu-iso-disk
         spec:
           size: 20Gi
           storageClassName: robin
           diskType: cdrom
           source:
             http:
               url: https://releases.ubuntu.com/jammy/ubuntu-22.04.3-live-server-amd64.iso

  2. Create a `VirtualMachineDisk` resource with the following contents for the virtual machine's virtual hard disk, and then apply it to your cluster:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineDisk
         metadata:
           name: "ubuntu-main-disk"
         spec:
           size: 200Gi
           storageClassName: robin

  3. Create a `VirtualMachineType` resource with the following contents that specifies the virtual machine's configuration, and then apply it to your cluster:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineType
         metadata:
           name: small-2-20
         spec:
           cpu:
             vcpus: 2
           memory:
             capacity: 20Gi

  4. Create a `VirtualMachine` resource with the following contents that instantiates and starts the virtual machine on the cluster, and then apply it to your cluster:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           labels:
             kubevirt.io/vm: ubu-vm
           name: ubu-vm #  Propagate the virtual machine name to the VMI
         spec:
           osType: Linux
           compute:
             virtualMachineTypeName: small-2-20
           interfaces:
             - name: eth0
               networkName: my-network
               default: true
           disks:
             - virtualMachineDiskName: ubuntu-main-disk
               boot: true
             - virtualMachineDiskName: ubuntu-iso-disk

You must also configure the following features on your cluster:

     * [Passwordless SSH access to the virtual machine](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/connect-vms#configure_passwordless_ssh_access_to_vms)
     * [Configure VM startup routines](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/vm-startup-config)
  5. Install Ubuntu Server on the virtual machine:

     1. Wait for the `importer` Pod to download the Ubuntu Server installation disc image.
     2. Check the status of the virtual machine:
            
            kubectl get gvm VM_NAME

Replace `VM_NAME` with the name of the virtual machine—`ubu-vm` in this example.

     3. Log on to the virtual machine using either SSH or Remote Desktop.

     4. Complete the Ubuntu Linux installation steps.

  6. Clean up:

     1. Stop the virtual machine:
            
            kubectl virt stop VM_NAME

Replace `VM_NAME` with the name of the virtual machine—`ubu-vm` in this example.

     2. Edit the virtual machine's YAML file to remove the reference to the installation disc image:
            
            kubectl edit gvm VM_NAME

Replace `VM_NAME` with the name of the virtual machine—`ubu-vm` in this example.

     3. Start the virtual machine:
            
            kubectl virt start VM_NAME

Replace `VM_NAME` with the name of the virtual machine—`ubu-vm` in this example.

     4. Delete the `VirtualMachineDisk` resource for the installation disc image:
            
            kubectl delete virtualmachinedisk ubuntu-iso-disk




### Provision a Windows virtual machine on Distributed Cloud connected

The following example illustrates how to provision a Windows virtual machine with Symcloud Storage. The steps are similar to provisioning a Linux virtual machine, with the addition of the `virtio` driver disk image, which is required for installing Windows.

  1. Obtain a licensed copy of Windows and its installation media image.

  2. Create a `VirtualMachineDisk` resource with the following contents for the Windows installation disc image, and then apply it to your cluster:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineDisk
         metadata:
           name: windows-iso-disk
           namespace: default
         spec:
           size: 5Gi
           storageClassName: robin
           diskType: cdrom
           source:
             http:
               url: WINDOWS_ISO_URL

Replace `NAT_GATEWAY` with the full URL to the target Windows installation ISO disc image.

  3. Create a `VirtualMachineDisk` resource with the following contents for the `virtio` driver, and then apply it to your cluster:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineDisk
         metadata:
           name: windows-virtio-driver
           namespace: default
         spec:
           size: 1Gi
           storageClassName: robin
           diskType: cdrom
           source:
             http:
               url: https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/virtio-win.iso

  4. Create a `VirtualMachineDisk` resource with the following contents for the virtual machine's virtual hard disk, and then apply it to your cluster:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineDisk
         metadata:
           name: windows-main-disk
           namespace: default
         spec:
           size: 15Gi
           storageClassName: robin

  5. Create a `VirtualMachineType` resource with the following contents that specifies the virtual machine's configuration, and then apply it to your cluster:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineType
         metadata:
           name: small-2-20
         spec:
           cpu:
             vcpus: 2
           memory:
             capacity: 20Gi

  6. Create a `VirtualMachine` resource with the following contents that instantiates and starts the virtual machine on the cluster, and then apply it to your cluster:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           labels:
             kubevirt.io/vm: win-vm
           name: win-vm #  Propagate the virtual machine name to the VMI
         spec:
           osType: Windows
           compute:
             virtualMachineTypeName: my-vmt
           interfaces:
             - name: eth0
               networkName: my-network
               default: true
           disks:
             - virtualMachineDiskName: windows-main-disk
               boot: true
             - virtualMachineDiskName: windows-iso-disk
             - virtualMachineDiskName: win-virtio-driver

You must also configure the following features on your cluster:

     * [Passwordless SSH access to the virtual machine](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/connect-vms#configure_passwordless_ssh_access_to_vms)
     * [Configure VM startup routines](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/vm-startup-config)
  7. Install Windows on the virtual machine:

     1. Wait for the `importer` Pod to download the Windows installation disc image.
     2. Check the status of the virtual machine:
            
            kubectl get gvm VM_NAME

Replace `VM_NAME` with the name of the virtual machine—`win-vm` in this example.

     3. Complete the Windows installation by following the steps in [Connect to Windows VM and complete OS install](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/windows-vm#connect_to_windows_vm_and_complete_os_install).

  8. Clean up:

     1. Stop the virtual machine:
            
            kubectl virt stop VM_NAME

Replace `VM_NAME` with the name of the virtual machine—`win-vm` in this example.

     2. Complete the steps in [Detach the ISO image and drivers disk](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/windows-vm#detach_the_iso_image_and_drivers_disk).




## Manage virtual machines running on Distributed Cloud connected

For instructions about managing virtual machines running on Distributed Cloud connected, see the following VM Runtime on GDC documentation: 

  * [Connect to VMs](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/connect-vms)
  * [List and view VMs](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/list-view-vms)
  * [Manage power state](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/manage-power-state)
  * [Edit a VM](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/edit-vm)
  * [Delete a VM](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/delete)
  * [View VM console logs](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/view-console-logs)



To manage virtual machines running on Distributed Cloud connected, you must first [Configure `kubectl` connectivity](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/kubectl).

## Disable VM Runtime on GDC on Distributed Cloud connected

Follow the steps in this section to disable VM Runtime on GDC on Distributed Cloud connected. Before you can disable VM Runtime on GDC on Distributed Cloud connected, you must stop and delete all the virtual machines on your Distributed Cloud connected cluster as described in [Delete a VM](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/vm-runtime/delete).

To disable VM Runtime on GDC on Distributed Cloud connected, modify the `VMRuntime` custom resource by setting the `enabled` spec parameter to `false` as follows, and then apply it to your cluster:
    
    
    apiVersion: vm.cluster.gke.io/v1
    kind: VMRuntime
    metadata:
      name: vmruntime
    spec:
      # Disable Anthos VM Runtime
      enabled: false
      # vmImageFormat defaults to "raw" if not set
      vmImageFormat: "raw"

## View `AppArmor` sandboxing audit logs

Distributed Cloud connected automatically sandboxes virtual machine workloads with `AppArmor` policies in `audit-mode`. A policy violation emits an audit log entry. For example:
    
    
    {
      "jsonPayload": {
        "_SOURCE_REALTIME_TIMESTAMP": "1734596844149104",
        "SYSLOG_TIMESTAMP": "Dec 19 08:27:24 ",
        "MESSAGE": "type=AVC msg=audit(1734596844.148:27742): apparmor=\"ALLOWED\" operation=\"open\" profile=\"virt-launcher-audit\" name=\"/etc/libvirt/virtlogd.conf\" pid=182406 comm=\"virtlogd\" requested_mask=\"r\" denied_mask=\"r\" fsuid=0 ouid=0 FSUID=\"root\" OUID=\"root\"",
        "PRIORITY": "6",
        ...
        "SYSLOG_RAW": "<14>Dec 19 08:27:24 audisp-syslog: type=AVC msg=audit(1734596844.148:27742): apparmor=\"ALLOWED\" operation=\"open\" profile=\"virt-launcher-audit\" name=\"/etc/libvirt/virtlogd.conf\" pid=182406 comm=\"virtlogd\" requested_mask=\"r\" denied_mask=\"r\" fsuid=0 ouid=0 FSUID=\"root\" OUID=\"root\"\n",
        "SYSLOG_IDENTIFIER": "audisp-syslog",
        "_GID": "0",
      },
      "timestamp": "2024-12-19T08:27:24.149109Z",
      "labels": {
        "gke.googleapis.com/log_type": "system"
      },
      "receiveTimestamp": "2024-12-19T08:27:24.721842807Z"
      ...
      ...
    

## What's next

  * [Manage virtual machines on Distributed Cloud connected servers](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/vm-servers)
  * [Deploy workloads on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/deploy)
  * [Manage GPU workloads](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/gpu)
  * [Manage zones](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/zones)
  * [Manage machines](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/machines)
  * [Manage clusters](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/clusters)
  * [Manage node pools](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/nodepools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
