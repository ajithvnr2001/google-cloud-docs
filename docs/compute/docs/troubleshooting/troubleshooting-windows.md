---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows/
title: Troubleshooting Windows VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:50.015846+00:00
---

# Troubleshooting Windows VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting Windows VMs Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

This document describes the methods and tools available to resolve the following Compute Engine Windows virtual machine (VM) instance boot issues:

  * You can't connect to the VM using RDP, and [troubleshooting](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp) is unsuccessful in resolving your connection.

  * The login screen has not appeared in a [VM screenshot](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp#vm-screenshot), and the VM does not appear to be making progress or performing an update.

  * You have encountered a blue screen error, frozen or erratically behaving VM under normal operation.




If you are experiencing issues connecting to Windows VMs, see [Troubleshooting RDP](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp).

To identify why a compute instance fails to boot, and to detect the cause automatically, see [Troubleshoot Windows Compute Engine instance boot issues](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows-boot-issues).

For issues related to migrating to a third generation VM, see Windows [Known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#move-windows-vm-gen3).

## Before you begin

  * Review the [Microsoft Advanced troubleshooting for Windows boot problems](https://docs.microsoft.com/en-us/windows/client-management/advanced-troubleshooting-boot-problems) for information about troubleshooting the Windows boot process.
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).




## Using the Advanced Boot Options menu

If Windows doesn't start correctly, use the Advanced Boot Options menu to access safe mode or complete an online repair of the operating system. For more information, see [Advanced startup options](https://support.microsoft.com/en-us/windows/advanced-startup-options-including-safe-mode-b90e7808-80b5-a291-d4b8-1a1af602b617).

To enter the Advanced Boot Options menu on your Windows VM, complete the following procedure:

  1. Enable a [display device](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display#virtual-display-add-remove) for the VM if you haven't already.
  2. [Connect to the VM's interactive serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#connectserialconsole).

  3. Reset the VM by using one of the following methods:

###  Console 

     1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Click the name of the VM you want to reset. The VM instance details page opens.

     3. Click the **Reset** button to reboot the VM.

###  gcloud 

Use the [`gcloud compute instances reset` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/reset) to reset the VM:
    
    gcloud compute instances reset VM_NAME --zone=ZONE --project=PROJECT_ID
    

Replace the following:

     * `PROJECT_ID`: the ID of the project that contains the VM
     * `ZONE`: the name of the zone in which the VM is located
     * `VM_NAME`: the name of the VM

###  Command Prompt 

While connected to the interactive serial console, open a Command Prompt session and run the following command. For more information about opening a Command Prompt session, see [Opening Command Prompt in Windows SAC](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#command-prompt).
    
    shutdown /r /t 0
    

The Windows Boot Manager menu opens:

![Windows Boot Manager menu](https://docs.cloud.google.com/static/compute/images/windows-boot-manager.png)

  4. Before the countdown expires, complete these steps:

     1. Ensure the interactive serial console is your active window.

     2. Press the `Esc` key on your keyboard.

     3. Press the number `8` key on your keyboard.

The Advanced Boot Options menu opens:

![Advanced Boot Options
menu](https://docs.cloud.google.com/static/compute/images/windows-advanced-boot-options.png)

  5. Use the arrow keys on your keyboard to select an option, then open it by pressing the **Enter** key.


**Note:** If you are unable to see the Windows Boot Manager and need to enter the Advanced Boot Options menu, you will need to enable the Windows Boot Manager menu.

## Enabling the Windows Boot Manager menu

You can configure the Windows Boot Manager menu to display when a Windows VM instance is being rebooted. To enable the Windows boot manager menu, do the following:

**Note:** If you need to enable the Windows Boot Menu to perform a operating system repair and are unable to login to the VM, you might need to complete an offline repair instead.

[Connect to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and open a Command Prompt with [administrative access](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj717276\(v=ws.11\)). If you cannot connect to the VM, add the subsequent steps as values to a `windows-startup-script-cmd` or `windows-startup-script-ps1` [startup script](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows#passing-directly) instead of running them directly

###  Command Prompt 

  1. To enable the Windows Boot Manager menu at startup and add a 15 second timeout, run the following commands:
         
         bcdedit /set {bootmgr} displaybootmenu yes
         
         
         bcdedit /set {bootmgr} timeout 15
         

  2. To reboot the VM and display the Windows boot manager menu in the serial console using the following command:
         
         shutdown -r -t 0
         




###  PowerShell 

  1. To enable the Windows Boot Manager menu at startup and add a 15 second timeout, run the following commands:
         
         bcdedit /set '{bootmgr}' displaybootmenu yes
         
         
         bcdedit /set '{bootmgr}' timeout 15
         

  2. To reboot the VM and display the Windows boot manager menu in the serial console using the following command:
         
         shutdown -r -t 0
         




## Completing an offline repair

If your VM doesn't start correctly and using the advanced boot menu has failed to resolve the issue, try performing an offline repair using a functional Windows VM instance for recovery with a snapshot of the troubled VM's boot disk. Using a snapshot gives you a backup copy that can be modified without changing the state of the original VM.

  1. [Create a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) of the troubled VM's boot disk.

  2. [Create a disk](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot#create-disk-from-snapshot) using that snapshot.

  3. [Create a VM with an additional non-boot disk](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-additional-non-boot-disks), using the newly created disk. Your recovery VM should meet these criteria:

     * The recovery VM must be in the same zone as the disk that was created.
     * The recovery VM should also be using a [Windows Server image](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server).
     * The [source image](https://docs.cloud.google.com/compute/docs/instances/view-vm-image) of the recovery VM's boot disk should be different to the source image of troubled VM's boot disk.
**Caution:** Ensure that the [boot disk image](https://docs.cloud.google.com/compute/docs/instances/view-vm-image) of the recovery VM differs from the boot disk that is being repaired; failure to do so may result in duplicate disk or partition GUID and unpredictable results as [confirmed by Microsoft](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-and-gpt-faq#detecting-a-duplicate-disk-or-partition-guid).
  4. You can now use Windows tools and utilities to attempt an offline repair of the additional attached disk. Refer to the following documentation for details about completing an offline repair of your VM:

     * [Scanning the volume for errors with the `chkdsk` utility](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/chkdsk)

     * [Verify the integrity of system files with `sfc`](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/sfc)

     * [Repair your Windows image with `dism`](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/repair-a-windows-image)

  5. If the offline repair has completed successfully, [update the boot disk](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#update_a_boot_disk_for_an_instance) of the troubled VM to be the newly repaired boot disk.

  6. Optional: Delete the additional resources after you no longer need them:

     * [Delete the recovery VM](https://docs.cloud.google.com/compute/docs/instances/deleting-instance)
     * Delete the original corrupted boot disk
     * [Delete the original corrupted boot disk snapshot](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots#delete_a_snapshot)



## Troubleshooting blue screen errors

The Windows operating system may experience a stop code or blue screen error, also know as a Blue Screen of Death. If a VM experiences a blue screen error, the VM stops running and needs to perform a restart before resuming normal operations.

If you believe a blue screen error may have occurred, confirm this by identifying presence of errors using one or more of the following methods:

###  Serial port 1 

**Note:** Google provided [Windows public images](https://docs.cloud.google.com/compute/docs/images) version 20191112 and later contain the `google-compute-engine-driver-pvpanic` driver which automatically sends kernel panic information to the serial port. If it is not installed on your instance, [install the driver](https://docs.cloud.google.com/compute/docs/instances/windows#gce-windows-drivers).

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM you want to view logs for. The VM instance details page opens.

  3. Under **Logs** , click **Serial port 1**.

  4. A stack trace dump similar to the following confirms a blue screen error:
         
         ntoskrnl.exe [0xFFFFF802C9606000, 0xFFFFF802C9E23000]
         netbios.sys [0xFFFFF80E98430000, 0xFFFFF80E98442000]
         volmgr.sys [0xFFFFF80E97E40000, 0xFFFFF80E97E58000]
         NTFS.sys [0xFFFFF80E98060000, 0xFFFFF80E98293000]
         crashdmp.sys [0xFFFFF80E986C0000, 0xFFFFF80E986D9000]
         pvpanic.sys [0xFFFFF80E99030000, 0xFFFFF80E9903C000]
         myfault.sys [0xFFFFF80E9A570000, 0xFFFFF80E9A578000]
         Dumping stack trace:
         0xFFFFF80E990317C7 (pvpanic.sys+0x17C7)
         0xFFFFF80E990316D3 (pvpanic.sys+0x16D3)
         0xFFFFF802C97D9681 (ntoskrnl.exe+0x1D3681)
         0xFFFFF802C97D8A1F (ntoskrnl.exe+0x1D2A1F)
         0xFFFFF802C97633F4 (ntoskrnl.exe+0x15D3F4)
         0xFFFFF802C9773329 (ntoskrnl.exe+0x16D329)
         0xFFFFF802C976F152 (ntoskrnl.exe+0x169152)
         0xFFFFF80E9A572794 (myfault.sys+0x2794)
         Current Process: notmyfault64.e
         


**Note:** Serial logs are kept as long as the instance is in the `RUNNING` [life cycle state](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle), unless you have serial logging enable. For more information, see [Viewing serial port output](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output).

###  Serial port 2 

**Note:** Google provided [Windows public images](https://docs.cloud.google.com/compute/docs/images) version 20191112 and later contain the `google-compute-engine-driver-pvpanic` driver which automatically sends kernel panic information to the serial port. If it is not installed on your instance, [install the driver](https://docs.cloud.google.com/compute/docs/instances/windows#gce-windows-drivers).

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM you want to view logs for. The VM instance details page opens.

  3. Under **Logs** , expand **More** , then click **Serial port 2 (console)**.

  4. Review the serial port of the instance, and look for this output similar to the following:
         
         !SAC>
         Your PC ran into a problem and needs to restart.
         If you call a support person, give them this info:
         UNEXPECTED_KERNEL_MODE_TRAP
         
         myfault.sys
         
         0x0000000000000008
         0xFFFFC6812AB94F70
         0xFFFFC6812E38EFF0
         0xFFFFF80E9A572794
         
         We're just collecting some error info, and then we'll restart for you.
         100% complete
         


**Note:** Serial logs are kept as long as the instance is in the `RUNNING` [life cycle state](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle), unless you have serial logging enable. For more information, see [Viewing serial port output](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output).

###  Command Prompt 

  1. [Connect to the instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and open a Command Prompt with [administrative access](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj717276\(v=ws.11\)).

  2. To display the most recent blue screen event, run the following command:
         
         wevtutil qe System "/q:*[System [(EventID=1001)]]" /rd:True /c:1 /f:Text
         

  3. Review the output, which looks similar to the following:
         
         Event[0]:
           Log Name: System
           Source: Microsoft-Windows-WER-SystemErrorReporting
           Date: 2021-04-14T08:53:52.933
           Event ID: 1001
           Task: N/A
           Level: Error
           Opcode: N/A
           Keyword: Classic
           User: N/A
           User Name: N/A
           Computer: WINDOWS
           Description:
         The computer has rebooted from a bugcheck.  The bugcheck was: 0x1000007f (0x
         0000000000000008, 0xffffc6812ab94f70, 0xffffc6812e38eff0, 0xfffff80e9a572794
         ). A dump was saved in: C:\Windows\Minidump\041421-12656-01.dmp. Report Id:
         a5710c98-a577-4b3e-a3c9-2fc0aa4e5d83.
         




For information about customizing `wetutil` queries, see [`wevtutil`](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil).

###  Disk Snapshot 

If the VM is no longer operational, or the other methods have proven unsuccessful. You can inspect the boot disk of the suspected blue screen VM with a secondary VM. Using a snapshot gives you a backup copy that can be modified without changing the state of the original VM.

  1. [Create a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) of the suspected blue screen VM's boot disk.

  2. [Create a disk](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot#create-disk-from-snapshot) using that snapshot.

  3. [Create a VM with an additional non-boot disk](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-additional-non-boot-disks) , using the newly created disk of the suspected VM. Your recovery VM should meet these criteria:

     * The recovery VM must be in the same zone as the disk that was created.
     * The recovery VM should also be using a [Windows Server image](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server).
     * The [source image](https://docs.cloud.google.com/compute/docs/instances/view-vm-image) of the recovery VM's boot disk should be different to the source image of troubled VM's boot disk.
**Caution:** Ensure that the [boot disk image](https://docs.cloud.google.com/compute/docs/instances/view-vm-image) of the recovery VM differs from the boot disk that is being repaired; failure to do so may result in duplicate disk or partition GUID and unpredictable results as [confirmed by Microsoft](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-and-gpt-faq#detecting-a-duplicate-disk-or-partition-guid).
  4. Browse the additional disk and locate for the following files:
         
         %SystemRoot%\Memory.dmp
         %SystemRoot%\Minidump\DATE-TIME-NUM.dmp
         

The date and time of the file can help you correlate if the suspected instance experienced a blue screen error. These files can also be used for analysis and diagnosis.

  5. Optional: Delete the additional resources after you no longer need them:

     * [Delete the newly created VM](https://docs.cloud.google.com/compute/docs/instances/deleting-instance)
     * [Delete the original corrupted boot disk](https://docs.cloud.google.com/compute/docs/disks/working-with-persistent-disks)
     * [Delete the original corrupted boot disk snapshot](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots#delete_a_snapshot)



After you obtain the blue screen error information and optionally obtained access to the memory dump file, follow the diagnostic steps and recommendations as provided by Microsoft:

  * [Understanding blue screen data](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/blue-screen-data)

  * [Bug check code reference](https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/bug-check-code-reference2)

  * [Advanced troubleshooting for stop code or blue screen errors](https://docs.microsoft.com/en-us/windows/client-management/troubleshoot-stop-errors)




## Licensing issues

Windows operating systems renew their licenses every seven days by connecting to the [Key Management Service (KMS)](https://technet.microsoft.com/en-us/library/ff793434.aspx) server. If you receive messages about license expiration or any other issues related to licenses on your Windows VMs, do the following:

  1. Confirm that your Windows VM's VPC network is configured to [allow communication with KMS](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#kms-server).

  2. Confirm that the Windows Firewall permits outbound connections to the KMS server:

     * IP address: `35.190.247.13`
     * Port: `1688`
     * Protocol: `TCP`

For more information about configuring Windows Advanced Firewall rules, see [Create an Outbound Port Rule](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/create-an-outbound-port-rule).

  3. Check that the connection to the KMS server is successful by running the following command in Cloud Shell:
         
         gcloud network-management connectivity-tests create test-access-to-gcp-kms \
             --source-ip-address=WINDOWS_VM_IP_ADDRESS \
             --destination-ip-address=35.190.247.13 \
             --destination-port=1688 \
             --protocol=TCP \
             --round-trip
         

As shown in the following image, you should see **Next hop: Internet gateway** listed in the **Static route** field of the [Connectivity Test](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests#viewing-tests) result card. If you see a different result, then the Windows activation will fail. ![KMS Connectivity Test result.](https://docs.cloud.google.com/static/compute/images/windows-kms-connectivity-results.png). The result should show a status of `Reachability` and a `Successful` result.

  4. Run the following commands to confirm the current state of your license, set the server IP address of the KMS and force an activation:
         
         cscript \windows\system32\slmgr.vbs /dlv
         
         
         cscript \windows\system32\slmgr.vbs /skms 35.190.247.13:1688
         
         
         cscript \windows\system32\slmgr.vbs /ato
         




## Troubleshooting Interactive Serial Console

  1. Ensure that you meet the [prerequsiste to access serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#before-you-begin).

  2. Enable [Emergency Management Services](https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/boot-parameters-to-enable-ems-redirection). If EMS is turned off, the serial console won't take any keyboard inputs but present only a blank screen with a blinking cursor.

###  Command Prompt 

     1. [Connect to the VM using RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and open `Command Prompt` as an Administrator. If you cannot RDP, add the subsequent steps as values to the [`windows-startup-script-cmd`](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows#passing-directly) startup key.

     2. Set the global EMS redirection settings to use COM2, a baud rate of 115200, and enable EMS.
            
            bcdedit /emssettings EMSPORT:2 EMSBAUDRATE:115200
            bcdedit /ems on
            

     3. Reboot the VM to apply the updated configuration. If you're using a metadata script don't add the shutdown command.
            
            shutdown -r -t 0
            

###  PowerShell 

     1. [Connect through RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and open `Powershell` as Administrator. If you cannot RDP, add the subsequent steps as values to the [`windows-startup-script-ps1`](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows#passing-directly) startup key.

     2. Set the global EMS redirection settings to use COM2, a baud rate of 115200, and enable EMS.
            
            bcdedit /emssettings EMSPORT:2 EMSBAUDRATE:115200
            bcdedit /ems on
            

     3. Reboot the VM to apply the updated configuration. If you're using a metadata script don't add the shutdown command.
            
            shutdown -r -t 0
            


**Note:** Make sure there are no Group Policy Objects (GPOs) or any scripts disabling the [Special Administration Console Helper service (Sacsvr)](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/system-services#special-administration-console-helper). If this service is disabled or not running, SAC doesn't start, which prevents you from using command prompts in the serial console.

## What's next

  * Learn how to [collect diagnostic information from a VM](https://docs.cloud.google.com/compute/docs/instances/collecting-diagnostic-information).

  * Learn how to [capture screenshots from VMs](https://docs.cloud.google.com/compute/docs/instances/capturing-vm-screenshots).

  * Learn about [licensing for Windows Server and SQL Server images](https://docs.cloud.google.com/compute/docs/instances/windows#licensing_for_windows_server_images).

  * Learn more about [interacting with the serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#enabling_interactive_access_on_the_serial_console).

  * Learn how to [Troubleshoot RDP connections](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
