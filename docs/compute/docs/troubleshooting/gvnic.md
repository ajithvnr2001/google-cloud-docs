---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/gvnic/
title: Troubleshooting network drivers for Compute Engine instances \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:57.638885+00:00
---

# Troubleshooting network drivers for Compute Engine instances  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/gvnic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting network drivers for Compute Engine instances Stay organized with collections  Save and categorize content based on your preferences. 

Here are some tips to help troubleshoot network drivers for [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) and [Infrastructure Data Plane Function (IDPF)](https://docs.cloud.google.com/compute/docs/networking/using-idpf). 

## Common errors for the gVNIC driver

The following issue occurs when the image used to create the VM instance isn't tagged to use gVNIC.
    
    
    ERROR: (gcloud.compute.instances.create) Could not fetch resource:
     - Invalid value for field 'resource.networkInterfaces[0].nicType': 'GVNIC'.
    NetworkInterface NicType can only be set to GVNIC on instances with
    GVNIC GuestOsFeature.

To resolve this issue, ensure that you are using an image that is tagged to use gVNIC. For more information, see [Create a custom image](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#create-custom-image).

### VM instance didn't boot

  * **Cause:** gVNIC is not enabled on the image.

  * **Diagnosis:** Check that the image has `gVNIC` enabled. To verify, run the following command:
        
        gcloud compute images describe IMAGE_NAME

Replace `IMAGE_NAME` with the name of your image. For instructions on how to find the image name, see [View the source image of a VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-image).

The output of the command should show `GVNIC` under `guestOsFeatures`.

You can also check if the VM instance was created with the `nic-type` set to `gVNIC`. To do this run the following command:
        
        gcloud compute instances describe VM_NAME

Replace `VM_NAME` with the name of your VM instance.

  * **Resolution:** Ensure that you are using a [supported image](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#os-support) or that you have properly [set up the gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup) on your custom image.




### VM instance booted but is not reachable over the network

  * **Cause:** gVNIC was not successfully installed and loaded.

  * **Diagnosis:** To check if the driver was installed and loaded, complete the following steps:

###  Linux 

    1. Check that the driver is installed.
           
           modinfo gve

The output should resemble the following:
           
           filename:       /lib/modules/4.15.0-1036-gcp/updates/dkms/gve.ko
           version:        1.1.0
           license:        Dual MIT/GPL
           description:    gVNIC Driver
           author:         Google, XXX.
           srcversion:     5FEFB9DD945EB2DEC94EE09
           alias:          pci:v00001AE0d00000042sv*sd*bc*sc*i*
           depends:
           retpoline:      Y
           name:           gve
           vermagic:       4.15.0-1036-gcp SMP mod_unload
           

    2. Check that the driver is loaded.
           
           lsmod | grep gve

The output should resemble the following:
           
           gve                    49152  0

###  Windows 

    1. Connect to instance through [SAC](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#windows_cli).
    2. Login with your username and password.
    3. From the command prompt, run the following command:
           
           dism /online /get-drivers | findstr gvnic

    4. Review the result.

       * If the driver is installed, you should see the text `Original File Name : gvnic.inf` in the output.
       * If the driver is not installed, no message is returned.

**Note:** You can also review the [interactive serial console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console) when debugging issues with your connection.
  * **Resolution:** If gVNIC is not available, ensure that you are using a [supported image](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#os-support) or that you have properly [set up gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup) on your custom image.




### Poor networking throughput for Windows Server 2022 and Windows 11 VMs

You might experience poor networking throughput when using [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) with Windows Server 2022 and Windows 11 VM instances that use gVNIC driver GooGet package version `1.0.0@44` or earlier.

To resolve this issue, update the gVNIC driver GooGet package to version `1.0.0@45` or later by doing the following:

  1. Check which driver version is installed on your VM instance by running the following command from an administrator Command Prompt or Powershell session:
         
         googet installed
         

The output looks similar to the following:
         
         Installed packages:
           ...
           google-compute-engine-driver-gvnic.x86_64 VERSION_NUMBER
           ...
         

  2. If the `google-compute-engine-driver-gvnic.x86_64` driver version is `1.0.0@44` or earlier, update the driver from the [GooGet package repository](https://github.com/google/googet) by running the following command from an administrator Command Prompt or Powershell session:
         
         googet install google-compute-engine-driver-gvnic
         




## Common errors for the IDPF driver

The following issue occurs when the image used to create a bare metal instance isn't tagged to use IDPF.
    
    
    ERROR: (gcloud.compute.instances.create) Could not fetch resource:
     - Invalid value for field 'resource.machineType': ...
    NetworkInterface NicType can only be set to IDPF on instances with
    IDPF GuestOsFeature.

To resolve this issue, ensure that you are using an image that supports and is tagged to use IDPF. For more information, see [Create a custom OS image that supports IDPF](https://docs.cloud.google.com/compute/docs/networking/using-idpf#create-custom-image).

### Bare metal instance didn't boot

  * **Cause:** IDPF isn't enabled on the image.

  * **Diagnosis:** Check that the image has `IDPF` enabled. To verify, run the following command:
        
        gcloud compute images describe IMAGE_NAME

Replace `IMAGE_NAME` with the name of the image used by the compute instance. For instructions on how to find the image name, see [View the source image of a VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-image).

The output of the command should show `IDPF` under `guestOsFeatures`.
        
        ...
        guestOsFeatures:
        ...
            - type: IDPF
            - type: SEV_CAPABLE
            - type: VIRTIO_SCSI_MULTIQUEUE
            - type: SEV_LIVE_MIGRATABLE
        ...
        

You can also check if the bare metal instance was created with the `nic-type` set to `IDPF` by using the following command:
        
        gcloud compute instances describe INSTANCE_NAME
        

Replace `INSTANCE_NAME` with the name of your compute instance.

Look for the `networkInterfaces` section of the output:
        
        ...
        name: instance-20260319-221828
        networkInterfaces:
          - accessConfigs:
            - kind: compute#accessConfig
              networkTier: PREMIUM
              type: ONE_TO_ONE_NAT
          name: nic0
          network: https://www.googleapis.com/compute/v1/projects/my-project/global/networks/default
          networkIP: 203.0.113.8
          nicType: IDPF
          stackType: IPV4_ONLY
          subnetwork: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/subnetworks/default
        

  * **Resolution:** Ensure that you are using a [supported image](https://docs.cloud.google.com/compute/docs/networking/using-idpf#os-support) or that you have configured the IDPF driver in your custom image.




### Bare metal instance booted but is not reachable over the network

  * **Cause:** IDPF was not successfully installed and loaded.

  * **Diagnosis:** To check if the driver was installed and loaded, see [Verify that IDPF is enabled](https://docs.cloud.google.com/compute/docs/networking/using-idpf#verify-idpf).

  * **Resolution:** If IDPF is not available, ensure that you are using a public image that supports IDPF, or that you have properly configured the IDPF driver in your custom image.




## MTU value set in VPC not being used by compute instance

After following the instructions to [change the MTU value](https://docs.cloud.google.com/vpc/docs/change-mtu-vpc-network), the MTU configuration on the instance isn't using the same MTU value. For example, you might run the `/sbin/ifconfig | grep mtu` command on your instance to check the MTU setting. You have restarted the instance, but the instance configuration isn't updated.

**Cause:** The network driver version is not recent enough to support the MTU feature.

**Resolution:**

  1. If your instance uses a public image, review the **Networking features** tab for your OS version on the [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#network-features) page. Make sure it shows that Jumbo Frames are completely supported.
  2. If the public image doesn't fully support Jumbo Frames, or if you are using a custom OS image, then the installed version of the network driver is too old, and doesn't support the higher MTU values.

     * **GVNIC** : Update the gVNIC driver for your compute instance by following the instructions in [Use on non-supported operating systems](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup).
     * **IDPF** : Update the IDPF driver for your compute instance by following the instructions in [Use on non-supported operating systems](https://docs.cloud.google.com/compute/docs/networking/using-idpf#manual-idpf-setup).
  3. After updating the network driver, restart the instance and recheck the MTU configuration.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
