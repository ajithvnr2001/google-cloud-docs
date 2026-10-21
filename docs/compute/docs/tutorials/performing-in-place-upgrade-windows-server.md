---
url: https://docs.cloud.google.com/compute/docs/tutorials/performing-in-place-upgrade-windows-server/
title: Performing an in-place upgrade of Windows\u00a0Server \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:04.921520+00:00
---

# Performing an in-place upgrade of Windows Server  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tutorials/performing-in-place-upgrade-windows-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Performing an in-place upgrade of Windows Server Stay organized with collections  Save and categorize content based on your preferences. 

If you have virtual machine (VM) instances running earlier versions of Windows Server, you can upgrade them to later versions of Windows Server:

Upgrade from | Upgrade to  
---|---  
Windows Server 2008 R2 (Desktop Experience) | Windows Server 2012 R2 (Desktop Experience)  
Windows Server 2012 R2 (Core) | Windows Server 2016 (Core)  
Windows Server 2012 R2 (Desktop Experience) | Windows Server 2016 (Desktop Experience)  
Windows Server 2016 (Core) | Windows Server 2019 (Core)   
Windows Server 2016 (Desktop Experience) | Windows Server 2019 (Desktop Experience)   
Windows Server 2019 (Core) | Windows Server 2022 (Core)   
Windows Server 2019 (Desktop Experience) | Windows Server 2022 (Desktop Experience)   
Windows Server 2022 (Core) | Windows Server 2025 (Core)   
Windows Server 2022 (Desktop Experience) | Windows Server 2025 (Desktop Experience)   
  
Upgrades are subject to the following constraints:

  * Microsoft has [ended support for Windows Server 2012 R2](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-server-2012-r2-end-of-support) and [Windows Server 2008 R2](https://support.microsoft.com/en-us/help/4456235/end-of-support-for-windows-server-2008-and-windows-server-2008-r2). If you perform an in-place upgrade of either of these versions and encounter problems related to the Windows Setup process (`setup.exe`), Google might only be able to provide limited assistance.

  * If you plan to upgrade Windows Server 2008 R2 to a version later than Windows Server 2012 R2, you must first perform an upgrade to Windows Server 2012 R2, and then perform a second upgrade to Windows Server 2016 or later.

  * You must upgrade incrementally, one version at a time, because multiple version in-place upgrades are not supported.


**Important:** This guide only describes how to perform an in-place upgrade from Datacenter editions of Windows Server to Datacenter editions of Windows Server.

## Objectives

This guide describes how to perform an in-place upgrade of Windows Server by:

  1. Planning the in-place upgrade
  2. Performing the in-place upgrade
  3. Troubleshooting the in-place upgrade
  4. Cleaning up after the in-place upgrade



## Costs

There is no charge for performing an in-place upgrade of Windows Server. You are only charged for the resources consumed during the upgrade, including:

  * [Compute Engine](https://docs.cloud.google.com/compute)



Use the [pricing calculator](https://cloud.google.com/products/calculator/#id=beb5326f-90c3-4842-9c3f-%0Aa3761b40fbe3) to generate a cost estimate based on your projected usage.

## Before you begin

The guide assumes that you have basic knowledge of:

  * [Compute Engine](https://docs.cloud.google.com/compute)
  * [Performing unattended Windows Server installations by using Windows Setup](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/automate-windows-setup).



## Plan the in-place upgrade

Performing an in-place upgrade of a virtual machine (VM) instance that is running an earlier version of Windows Server can be a pragmatic way to modernize your infrastructure and to mitigate the risks of approaching the end of the support lifecycle of Windows Server versions.

### Alternatives to consider

Before you decide to use an in-place upgrade to migrate to a newer version of Windows Server, be aware of the following limitations:

  * **Downtime:** Depending on the configuration and software installed, the upgrade might take an hour or longer. During the upgrade, access to the VM instance is limited because:

    * Workloads running on the VM instance are unavailable to users
    * Remote Desktop Protocol (RDP) is not available
    * There are limited ways to check the upgrade progress and the time remaining in the upgrade
  * **Risk:** Depending on the configurations of your existing instances and the installed software:

    * The upgrade can fail
    * Some configuration options can be overridden
    * Incompatibilities can cause your workload to malfunction on the upgraded instance



Depending on the workload running on your Windows Server instance, you can reduce downtime and risk by pursuing different approaches.

Workload | Approach  
---|---  
Your VM instance is running a workload that supports replication, such as: 

  * Active Directory Domain Services
  * DNS
  * SQL Server

| Consider setting up a new VM instance that is running a more recent version of Windows Server, and then use replication to shift the workload from your existing VM instance to the new VM instance.   
You have a VM instance that is running a multitude of workloads  | Consider migrating these workloads to separate VM instances so that each VM instance runs only a single workload. Even if you can't migrate all workloads, reducing the number of workloads running on a single VM instance can help reduce risks during an in-place upgrade.   
  
### Product keys

A Windows Server product key is valid for only a specific version; when you perform an upgrade to a later version of Windows Server, you must supply a new product key. There are two primary scenarios:

  * **You are upgrading a VM instance that is based on a[public operating system image](https://docs.cloud.google.com/compute/docs/images#windows_server) provided by Google:** In this scenario, you must use the predefined [KMS client setup keys](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys#earlier-versions-of-windows-server) for the version of Windows Server that you are upgrading to. The upgrade does not incur additional charges.

  * **You are upgrading a VM instance for which you brought an existing license:** In [BYOL](https://docs.cloud.google.com/compute/docs/instances/windows/bring-your-own-license), you need to acquire a product key from your license vendor to perform the upgrade. [Check the Microsoft documentation](https://docs.microsoft.com/en-us/windows-server/get-started/installation-and-upgrade#upgrading-to-windows-server-2012) to determine which edition you can upgrade to and whether you are eligible for license conversion.




### Installation media

To perform the upgrade, you need an installation media. There are two primary scenarios:

  * **You are upgrading a VM instance that is based on a[public operating system image](https://docs.cloud.google.com/compute/docs/images#windows_server) provided by Google:** In this scenario, you can use the volume license installation media provided by Google. The steps to access this installation media are provided below.

  * **You are upgrading a VM instance that is based on an imported disk or image:** In this scenario, you cannot use the installation media provided by Google. Instead, you have to use an installation media that matches the type of media that you used to install Windows Server on the imported disk or image.

**Important:** If you use a custom install media to upgrade to Windows Server 2012 R2, make sure to [disable animations](https://mskb.pkisolutions.com/kb/2955372) before using it to perform an upgrade. Disabling animations is critical to prevent the `MSOOBE` process from causing the upgrade to stop responding indefinitely.



### Other prerequisites

Before you begin your upgrade, review the Microsoft documentation about prerequisites and potential limitations for the version of Windows Server you are planning to upgrade to:

### 2012 R2

  * Verify that your VM instance meets the [system requirements for Windows Server 2012](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj134246\(v%3Dws.11\)#system-requirements) and has [sufficient free disk space](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj134246\(v%3Dws.11\)#disk-space-requirements).

  * Review [recommendations for upgrading server roles](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ff972408\(v=ws.10\)#upgrading-server-roles), [known issues](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ff972310\(v=ws.10\)), and the [upgrade process](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ff972309\(v=ws.10\)) for Windows Server 2012 R2.

  * Review the [recommendations for planning an in-place upgrade](https://www.microsoft.com/upgradecenter/scenario/WS2008R2-on-prem-to-WS2012).

  * Verify that you aren't affected by [features removed or deprecated](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn303411\(v=ws.11\)) in Windows Server 2012 R2.

  * Verify that all your custom or third-party software is compatible with Windows Server 2012 R2.




### Year 2016

  * Verify that your VM instance meets the [system requirements for Windows Server 2016](https://docs.microsoft.com/en-us/windows-server/get-started/system-requirements) and has [sufficient free disk space](https://docs.microsoft.com/en-us/windows-server/get-started/system-requirements#storage-controller-and-disk-space-requirements).

  * Review the [server role upgrade and migration matrix for Windows Server 2016](https://docs.microsoft.com/en-us/windows-server/get-started/server-role-upgradeability-table) and [application compatibility table](https://docs.microsoft.com/en-us/windows-server/get-started/server-application-compatibility)

  * Verify that you aren't affected by [features removed or planned for replacement](https://docs.microsoft.com/en-us/windows-server/get-started/deprecated-features) in Windows Server 2016.

  * Verify that all your custom or third-party software is compatible with Windows Server 2016.




### Year 2019

  * Verify that your VM instance meets the [system requirements for Windows Server 2019](https://docs.microsoft.com/en-us/windows-server/get-started-19/sys-reqs-19) and has [sufficient free disk space](https://docs.microsoft.com/en-us/windows-server/get-started-19/sys-reqs-19#storage-controller-and-disk-space-requirements).

  * Review the [Windows Server 2019 and Microsoft Server application compatibility](https://docs.microsoft.com/en-us/windows-server/get-started-19/app-compat-19) list.

  * Verify that you aren't affected by [features removed or planned for replacement](https://docs.microsoft.com/en-us/windows-server/get-started-19/removed-features-19) in Windows Server 2019.

  * Verify that all your custom or third-party software is compatible with Windows Server 2019.




###  Year 2022

  * Verify that your VM instance meets the [system requirements for Windows Server 2022](https://docs.microsoft.com/en-us/windows-server/get-started/hardware-requirements) and has [sufficient free disk space](https://docs.microsoft.com/en-us/windows-server/get-started/hardware-requirements#storage-controller-and-disk-space-requirements).

  * Review the [Windows Server 2022 and Microsoft Server application compatibility](https://docs.microsoft.com/en-us/windows-server/get-started/application-compatibility-windows-server-2022) list.

  * Verify that you aren't affected by [features removed or planned for replacement](https://docs.microsoft.com/en-us/windows-server/get-started/removed-deprecated-features-windows-server-2022) in Windows Server 2022.

  * Verify that all your custom or third-party software is compatible with Windows Server 2022.




### Year 2025

  * Verify that your VM instance meets the [system requirements for Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/hardware-requirements?tabs=cpu&pivots=windows-server-2025) and has [sufficient free disk space](https://learn.microsoft.com/en-us/windows-server/get-started/hardware-requirements?tabs=storage&pivots=windows-server-2025#storage-requirements).

  * Review the [Windows Server 2025 and Microsoft Server application compatibility](https://learn.microsoft.com/en-us/windows-server/get-started/application-compatibility?pivots=windows-server-2025) list.

  * Verify that you aren't affected by [features removed or planned for replacement](https://learn.microsoft.com/en-us/windows-server/get-started/removed-deprecated-features-windows-server?tabs=ws25) in Windows Server 2025.

  * Verify that all your custom or third-party software is compatible with Windows Server 2025.




## Perform the in-place upgrade

The following sections guide you through the process of upgrading your VM instance.

### Create a snapshot

Before you start the upgrade, we recommend that you [create a snapshot of your VM instance](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#creating_snapshots), so that you can revert to a safe state in case anything goes wrong:

  * Create a [regular snapshot](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot#create_the_snapshot) for the boot disk of your VM instance.

  * If the VM instance has additional data disks attached, create snapshots for the data disks by using [the Volume Shadow Copy Service (VSS)](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot#create-snapshot).




### Prepare your Windows Server configuration

Verify the configuration of your Windows Server VM instance:

  1. [Connect to your VM instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#windows_gui) with an RDP client.

  2. Verify that Windows Server is up to date [by using Windows Update](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc731322\(v=ws.11\)#downloading-and-installing-updates).

  3. Disable or uninstall antivirus, antispyware, and other agents that can interfere with the upgrade or are incompatible with the Windows Server version that you're upgrading to.




### Attach the install media

Before you can perform the upgrade, attach the necessary installation media to the VM instance. The right media to use depends on your scenario:

  * **You are upgrading a VM instance that is based on a public operating system image provided by Google:** In this scenario, you only need to attach the volume license installation media provided by Google. This media contains both the necessary scripts to run the upgrade and the files for the new version of Windows Server.
  * **You are upgrading a VM instance that is based on an imported disk or image:** In this scenario, you also need to attach the volume license installation media provided by Google so that you can access the necessary scripts.

Additionally, you have to attach a custom installation media that matches the type of media that you used to install Windows Server on the imported disk or image.




To attach the volume license installation media provided by Google, follow these steps:

  1. In the Google Cloud console, open [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell) by clicking the **Activate Cloud Shell** ![Activate Cloud Shell.](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg) button.

[Go to the Google Cloud console](https://console.cloud.google.com/)

  2. Set the default project ID. Replace `PROJECT_ID` with the name of your Compute Engine project:
         
         gcloud config set project PROJECT_ID
         

  3. Create a disk based on the installation media. Replace `ZONE` with the name of the zone where the VM is located:
         
         gcloud compute disks create win-installers --image-family=windows-install-media --image-project=compute-image-tools --zone=ZONE
         

This command adds a disk named `win-installers` to your project. This disk is not attached to any VM instance.

  4. Attach the disk to your VM by using read-only (`ro`) mode, so that you can attach the disk to multiple VMs if necessary:
         
         gcloud compute instances attach-disk VM_NAME --disk=win-installers --mode=ro --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of the VM instance to upgrade
     * `ZONE`: the name of the zone where the VM is located

You can use the same disk for multiple and parallel VM upgrades within the same zone, but if you want to upgrade a VM in a different zone, you must create another disk in that zone.




If you are upgrading a VM that is based on an imported disk or image, attach the custom installation media as an additional disk:

  1. Follow the steps in [Creating an image from an ISO file](https://docs.cloud.google.com/compute/docs/images/creating-an-image-from-an-iso-file) to create a disk from the ISO image that you want to use as custom installation media.

  2. Attach the disk to your VM, by using read-only (`ro`) mode so that you can attach the disk to multiple VMs if necessary:
         
         gcloud compute instances attach-disk VM_NAME --disk=CUSTOM_MEDIA_DISK --mode=ro --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of the VM to upgrade
     * `CUSTOM_MEDIA_DISK`: the name of the disk containing your custom installation media
     * `ZONE`: the name of the zone where the VM is located



### Start the upgrade

By default, Windows Setup prompts you for input at various points during an upgrade. Because you can't connect to the VM by using RDP during the upgrade and therefore can't provide any input, run the upgrade in [unattended mode](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/automate-windows-setup).

  1. Connect to your VM with an RDP client. For more information, see [Connecting to instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  2. Open an elevated command prompt:

     * If you use Server Core, an elevated command prompt should open automatically after login.
     * If you use Windows Server with full Desktop Experience, right-click the **Start** button and select **Command Prompt (Admin)**.
  3. Change the working directory to the installation media. The correct working directory depends on the Windows Server version that you are upgrading to:

###  2012 R2
         
         cd /d d:\*2012*
         

###  Year 2016
         
         cd /d d:\*2016*
         

###  Year 2019
         
         cd /d d:\*2019*
         

###  Year 2022 
         
         cd /d d:\*2022*
         

###  Year 2025 
         
         cd /d d:\*2025*
         

**Important:** Adjust the drive letter if Windows assigned a different letter than `D:` to the disk containing the volume license installation media provided by Google.
  4. Start the Windows upgrade. The required steps to start the upgrade depend on the Windows Server version that you are upgrading to and whether your VM is based on a public operating system image or on an imported disk or image:

###  2012 R2 

Run `upgrade.ps1` to start the Windows upgrade. The script completes the following steps:

     * Install the latest [Google driver packages](https://github.com/GoogleCloudPlatform/compute-windows-drivers), which are critical for the Windows Server upgrade to succeed.
     * Apply Windows settings that are required for [Compute Engine](https://docs.cloud.google.com/compute/docs/images#windows_server).
     * Enable access to the [Emergency Management Services (EMS) console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows#connectems) during the upgrade.
     * Launch Windows Setup (`setup.exe`) from the install media to perform an upgrade in unattended mode.
     * Selects the correct edition of Windows Server 2012 R2 to install.
     * Provides the Generic Volume License Key (GVLK) for the new version of Windows Server.
    
    powershell -ExecutionPolicy Bypass -File upgrade.ps1
    

###  2012 R2 (BYOL) 

Run `upgrade.ps1` to start the Windows upgrade. The script completes the following steps:

     * Install the latest [Google driver packages](https://github.com/GoogleCloudPlatform/compute-windows-drivers), which are critical for the Windows Server upgrade to succeed.
     * Apply Windows settings that are required for [Compute Engine](https://docs.cloud.google.com/compute/docs/images#windows_server).
     * Enable access to the [Emergency Management Services (EMS) console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows#connectems) during the upgrade.
     * Launch Windows Setup (`setup.exe`) from the install media to perform an upgrade in unattended mode.
     * Selects the correct edition of Windows Server 2012 R2 to install.
     * Provides the user provided license key for the new version of Windows Server.
    
    powershell -ExecutionPolicy Bypass -File upgrade.ps1 -SetupExePath SETUP_PATH -ProductKey PRODUCT_KEY
    

Replace the following:

     * ` SETUP_PATH`: the path to `setup.exe` on your custom installation media
     * `PRODUCT_KEY`: a valid product key for Windows Server 2016.

The `-ProductKey` parameter is only required if you are upgrading a VM instance for which you brought an existing license (BYOL)

###  2016 or later 

Run `upgrade.ps1` to start the Windows upgrade. The script completes the following steps:

     * Install the latest [Google driver packages](https://github.com/GoogleCloudPlatform/compute-windows-drivers), which are critical for the Windows Server upgrade to succeed.
     * Apply Windows settings that are required for [Compute Engine](https://docs.cloud.google.com/compute/docs/images#windows_server).
     * Enable access to the [Emergency Management Services (EMS) console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows#connectems) during the upgrade.
     * Launch Windows Setup (`setup.exe`) from the install media to perform an upgrade in silent mode.
     * Provide a product key for the new version of Windows Server.
    
    powershell -ExecutionPolicy Bypass -File upgrade.ps1
    

In some cases, Windows Setup might show a **Select Image** screen. If you see this screen, select the configuration that matches your current configuration:

     * If you use Server Core, select **Datacenter**.
     * If you use Windows Server with full desktop experience, select **Datacenter (Desktop Experience)**.

     * Click **Next** to begin the upgrade.

It might take several minutes for the setup to initialize.

###  2016 or later (imported) 

Run `upgrade.ps1` to start the Windows upgrade. The script completes the following steps:

     * Install the latest [Google driver packages](https://github.com/GoogleCloudPlatform/compute-windows-drivers), which are critical for the Windows Server upgrade to succeed.
     * Apply Windows settings that are required for [Compute Engine](https://docs.cloud.google.com/compute/docs/images#windows_server).
     * Enable access to the [Emergency Management Services (EMS) console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows#connectems) during the upgrade.
     * Launch Windows Setup (`setup.exe`) from the install media to perform an upgrade in silent mode.
    
    powershell -ExecutionPolicy Bypass -File upgrade.ps1 -SetupExePath SETUP-PATH -ProductKey PRODUCT-KEY
    

Replace the following:

     * ` SETUP_PATH`: the path to `setup.exe` on your custom installation media
     * `PRODUCT_KEY`: a valid product key for the version of Windows Server that is being upgraded to. For example, if upgrading from Windows Server 2016 Datacenter to Windows Server 2019 Datacenter, provide a valid Windows Server 2019 Datacenter key.

The `-ProductKey` parameter is only required if you are upgrading a VM instance for which you brought an existing license (BYOL).

In some cases, Windows Setup might show a **Select Image** screen. If you see this screen, select the configuration that matches your current configuration:

     * If you use Server Core, select **Windows Server Datacenter**.
     * If you use Windows Server with full desktop experience, select **Windows Server Datacenter (Desktop Experience)**.

     * Click **Next** to begin the upgrade.

It might take several minutes for the setup to initialize.

The upgrade process might issue the following warning. If so, you can ignore it:
    
    [package name] or a newer version is already installed on the system
    

The system can become temporarily unresponsive while installing the `netkvm` driver. If this happens, don't close the RDP connection or stop the VM instance unless the system is unresponsive for more than 5 minutes. If you do lose RDP connectivity, wait approximately 5 minutes before you reconnect to the VM instance.

The Setup Wizard might require you to restart the system first. In this case, restart the VM instance and run Windows Setup again, using the same command.

After about 5 minutes, the machine reboots, and RDP disconnects.




### Observe the upgrade process

Depending on the machine type of your VM instance and your Windows Server configuration, the upgrade might take between 10 and 60 minutes to complete. During that time, you can observe the status through the [serial port output](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output):

  1. In Cloud Shell, observe the boot process by running the following command:
         
         gcloud compute instances tail-serial-port-output VM_NAME --zone=ZONE
         

Replace the following:

     * `VM_NAME`: name of your VM instance
     * `ZONE`: name of the zone where the VM instance is located
  2. Wait until the machine has rebooted four times. Depending on the configuration of your VM instance, it might take 30 minutes or more for these reboots to occur. You can recognize a reboot by output that looks similar to this:
         
         SeaBIOS (version 1.8.2-20190620_103534-google)
         Total RAM Size = 0x00000001e0000000 = 7680 MiB
         CPUs found: 2     Max CPUs supported: 2
         

  3. After the fourth reboot, wait until the output `GCEMetadataScripts: Finished running startup scripts` or `No startup scripts to run` appears.




### Perform post-upgrade steps

You can now connect to the VM instance to verify that the upgrade has been successfully completed.

  1. Connect to the VM instance by using an RDP client. For more information, see [Connecting to instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  2. Sign in using a user account with local administrator privileges.

  3. Open an elevated command prompt:

     * If you use Server Core, an elevated command prompt should open automatically after login.
     * If you use Windows Server with full desktop experience, right-click the **Start** button and select **Command Prompt (Admin)**.
  4. Run the following command to query the version of Windows Server:

###  Windows Server Core
         
         ver
         

###  Windows Server with Desktop Experience 
         
         winver
         

Verify that the version matches the expected version of Windows Server.

  5. Change the working directory to the installation media. The correct working directory depends on the Windows Server version that you are upgrading to:

###  2012 R2
         
         cd /d d:\*2012*
         

###  Year 2016
         
         cd /d d:\*2016*
         

###  Year 2019
         
         cd /d d:\*2019*
         

###  Year 2022
         
         cd /d d:\*2022*
         

###  Year 2025
         
         cd /d d:\*2025*
         

**Important:** Adjust the drive letter if Windows assigned a different letter than `D:` to the disk containing the volume license installation media provided by Google.
  6. Run `upgrade.ps1` again to re-apply specific Compute Engine settings that might have been lost during the upgrade:
         
         powershell -ExecutionPolicy Bypass -File upgrade.ps1
         

  7. Restart the VM instance to ensure all changes take effect. It might take 1 to 2 minutes for the reboot to complete before you can connect to the VM instance again.




### Detach the installation disk

You can now detach the installation disk from the VM instance:

  * In Cloud Shell, detach the installation disk from your VM instance, replacing `VM_NAME` with the name of your VM instance:
        
        gcloud compute instances detach-disk VM_NAME --disk=win-installers
        




### Install updates and restore access

After the upgrade is complete, run Windows Update to download and install any security updates. To install the security updates, follow these steps: 

  1. Connect to the machine by using an RDP client. For more information, see [Connecting to instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  2. Use Windows Update to [install the latest Windows updates](https://support.microsoft.com/en-us/help/12373/windows-update-faq). You might have to restart the VM instance multiple times during this process.

  3. Re-enable any agents, antivirus, or antimalware software that you disabled before the upgrade.




## Troubleshoot the in-place upgrade

While running Windows Setup, you can't connect to the VM instance with RDP. If you suspect that the upgrade failed or is not progressing, use the following approaches, in order, to diagnose the situation:

### Check the serial port output

To check the progress of the upgrade process, view the [serial port output](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output) of the VM instance:

  * Serial port 1 captures the boot status
  * Serial port 3 captures the log output of Windows Setup



During the upgrade, you should observe four reboots. If you don't observe any progress for more than 30 minutes after the first reboot, it is likely that the upgrade failed.

### Check CPU and I/O metrics

Running a Windows Server upgrade is a CPU and disk I/O intensive operation. By checking the CPU and I/O metrics, you can get an indication for whether the setup is progressing.

View the CPU and I/O metrics in the Google Cloud console:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the instance that you're upgrading.

  3. Click the **Monitoring** tab.




### Connect to the Emergency Management Services console

Both during and after running Windows Setup, you can connect to the [Emergency Management Services (EMS) console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows#connectems). Using the EMS console, check the [Windows Setup log files](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/deployment-troubleshooting-and-log-files#windows-%0Asetup-scenario) and the [event log](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-eventlog?view=powershell-5.1) for indications that the upgrade is still progressing or for information about any errors that might have occurred.

### Connect remotely by using WinRM

If connecting by using RDP or EMS fails, you can try using WinRM to establish a remote PowerShell session:

  1. Connect to a different Windows Server instance in the same VPC.

  2. Open PowerShell.

  3. Establish a remote PowerShell session, replacing `VM_NAME` with the name of the instance to upgrade:
         
         Enter-PSSession -ComputerName VM_NAME -UseSSL -SessionOption (New-PsSessionOption -SkipCACheck) -Credential (Get-Credential)
         

  4. When prompted for credentials, enter the username and password of an administrative user account.

  5. Use the remote PowerShell session to check the [Windows Setup log files](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/deployment-troubleshooting-and-log-files#windows-setup-scenario) and the [event log](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-eventlog?view=powershell-5.1).




### Analyze log files offline

If you can't connect to the instance by using Windows Remote Management (WinRM), you can cancel the upgrade and analyze the log files from a different VM instance. To do this, follow these steps:

  1. [Stop the VM instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance).

This can take several minutes if Windows Server is unresponsive.

  2. [Detach the boot disk](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#detach_disk) from the instance.

  3. Create a new, temporary Windows Server instance, and attach the boot disk of the original instance as an additional disk.

  4. Use the temporary Windows Server instance to analyze the [setup log and event log files](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-setup-log-files-and-event-logs) of the instance that you were trying to upgrade.

  5. After you have completed the analysis, detach the disk from the temporary instance and [reattach it as a boot disk](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#attach_disk) to the original VM instance.




### Troubleshoot RDP

For information about troubleshooting RDP, see [Troubleshooting RDP](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp).

### Troubleshoot your Windows Server instances

For information about troubleshooting your Windows Server instances, see [Tips and troubleshooting for Windows instances](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows).

## Clean up

To avoid incurring further costs after you have completed this process, delete the installation disk.

### Delete the installation disk

You can create an installation disk based on the Google-provided image at any time. If you don't plan to upgrade more VM instances in the same zone, delete the installation disk:

  * In Cloud Shell, delete the `win-installers` disk that you created earlier:
        
        gcloud compute disks delete win-installers
        




## What's next

  * Learn how to [bring existing licenses to Compute Engine](https://docs.cloud.google.com/compute/docs/instances/windows/bring-your-own-license).

  * Learn how to [connect to Windows instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  * Learn about [sole-tenant nodes on Compute Engine](https://docs.cloud.google.com/compute/docs/nodes).

  * Work through more [Windows tutorials](https://docs.cloud.google.com/compute/docs/tutorials#windows).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
