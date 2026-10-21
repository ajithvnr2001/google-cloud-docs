---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp/
title: Troubleshooting RDP \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:36:37.425635+00:00
---

# Troubleshooting RDP  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting RDP Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

In some situations, you might not be able to connect to your Compute Engine Windows virtual machine (VM) instance with RDP. This might be due to configuration errors, network errors, or the boot process might not have completed.

This document describes a number of tips and approaches to troubleshoot and resolve common RDP issues.

## Ensure the VM is online and ready

After the VM has finished booting, which may take a few minutes, confirm its state using one of the following methods:

###  Serial port 1 

Serial port 1 is used to log system and application activity. View its output to determine that your VM has finished booting and if services have started correctly.

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM you want to view logs for. The VM instance details page opens.

  3. Under **logs** , select **Serial port 1**.

  4. Review serial port 1 output and look for output similar to the following:
         
         BdsDxe: loading Boot0003 "Windows Boot Manager" from HD(2,GPT,DD3FB000-7000-4000-8000-3977378A7000,0x0000,0x00000)/\EFI\Microsoft\Boot\bootmgfw.efi
         BdsDxe: starting Boot0003 "Windows Boot Manager" from HD(2,GPT,DD3FB000-7000-4000-8000-3977378A7000,0x0000,0x00000)/\EFI\Microsoft\Boot\bootmgfw.efi
         
         UEFI: Attempting to start image.
         Description: Windows Boot Manager
         FilePath: HD(2,GPT,DD3FB000-7000-4000-8000-3977378A7000,0x0000,0x00000)/\EFI\Microsoft\Boot\bootmgfw.efi
         OptionNumber: 3.
         
         2021/04/13 10:50:22 GCEGuestAgent: GCE Agent Started (version 20210128.00)
         2021-04-13T10:50:23.4621Z OSConfigAgent Info: OSConfig Agent (version 20210217.00.0+win@1) started.
         2021/04/13 10:50:42 GCEMetadataScripts: Starting startup scripts (version 20200129.00).
         2021/04/13 10:50:42 GCEMetadataScripts: No startup scripts to run.
         




Output containing `GCEGuestAgent` or `GCEMetadataScripts` confirms that Windows has started successfully. Try reconnecting to your VM using RDP.

###  Serial port 2 

Serial port 2 provides an interactive connection to the VM and also shows the output of the [Special Administration Console (SAC)](https://technet.microsoft.com/en-us/library/cc787940). You can use serial console 2 to determine if system services have started successfully.

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM you want to view logs for. The VM instance details page opens.

  3. Under **logs** , expand **More** , then click **Serial port 2 (console)**.

  4. Review the serial port 2 output and look for output similar to the following:
         
         BdsDxe: loading Boot0003 "Windows Boot Manager" from HD(2,GPT,DD3FB000-7000-4000-8000-3977378A7000,0x0000,0x00000)/\EFI\Microsoft\Boot\bootmgfw.efi
         BdsDxe: starting Boot0003 "Windows Boot Manager" from HD(2,GPT,DD3FB000-7000-4000-8000-3977378A7000,0x0000,0x00000)/\EFI\Microsoft\Boot\bootmgfw.efi
         
         UEFI: Attempting to start image.
         Description: Windows Boot Manager
         FilePath: HD(2,GPT,DD3FB000-7000-4000-8000-3977378A7000,0x0000,0x00000)/\EFI\Microsoft\Boot\bootmgfw.efi
         OptionNumber: 3.
         
         <machine-info>
         <name>WINDOWS</name>
         <guid>b7ab5000-4000-e000-e000-bc5a738da000</guid>
         <processor-architecture>AMD64</processor-architecture>
         <os-version>10.0</os-version>
         <os-build-number>17763</os-build-number>
         <os-product>Windows Server 2019 Datacenter</os-product>
         <os-service-pack>None</os-service-pack>
         </machine-info>
         Computer is booting, SAC started and initialized.
         Use the "ch -?" command for information about using channels.
         EVENT: The CMD command is now available.
         SAC>
         




Output containing `SAC started and initialized` or `CMD command is now available` confirms that Windows has started successfully. Try reconnecting to your VM using RDP.

###  VM Screenshot 

VM screenshots provide a visual representation of a VM's state, similar to a computer monitor.

  1. Before you can capture a screenshot of your VM, you must enable the VM's virtual display. If you haven't already enabled the virtual display, see [Enabling virtual displays](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display).

  2. Capture a screenshot. For more information, see [Capturing a screenshot from a VM](https://docs.cloud.google.com/compute/docs/troubleshooting/capturing-vm-screenshots#capturing_a_screenshot_from_a_vm).

  3. Review the screenshot to see that the instance is ready.




Compare your screenshot to the following to determine the current state:

  * A [Windows login screen](https://docs.cloud.google.com/compute/docs/troubleshooting/capturing-vm-screenshots#login-screen) confirms the OS has started successfully, you can now attempt to connect using RDP.
  * The [Windows Update progress screen](https://docs.cloud.google.com/compute/docs/troubleshooting/capturing-vm-screenshots#windows-updates) indicates the VM is not yet ready, allow more time it to complete the updates.
  * A [services loading screen](https://docs.cloud.google.com/compute/docs/troubleshooting/capturing-vm-screenshots#loading-services) indicates the VM is not yet ready, allow more time for the VM to start necessary services.
  * A [UEFI loading screen](https://docs.cloud.google.com/compute/docs/troubleshooting/capturing-vm-screenshots#uefi-loading) may indicate a missing boot file or record or corrupt boot sector/manager.
  * A [Windows blue screen error](https://docs.cloud.google.com/compute/docs/troubleshooting/capturing-vm-screenshots#windows-bsod) may be temporary or require further troubleshooting.



**Note:** Avoid forcing the VM to restart if it's loading or updating. Force restarting can disrupt the progress, add additional recovery time, or potentially corrupt your operating system.

If Windows has not started successfully after a few minutes, review the [Troubleshooting Windows](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows) guide.

## Check connectivity between your workstation and the VM instance

If you run into issues when you connect your Windows VM, it's a good practice to identify whether the problem is with the workstation that you are using to connect, or the VM that you are connecting to. Check connectivity between your workstation and the VM by running the following command from your Linux, macOS, or Windows workstation:
    
    
    curl -v telnet://DESTINATION_IP_ADDRESS:PORT
    

Replace the following:

  * `DESTINATION_IP_ADDRESS`: the IP address of your Windows VM
  * `PORT`: the port configured for connecting through RDP on your Windows VM



You can also use [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests) for further verification of connectivity between the VM instance and other Google Cloud products and services. Additionally, it might also be useful to set up a bastion host on the same subnetwork for isolating RDP connectivity issues on the VM instance.

## Check connectivity to the metadata server

Connectivity to the metadata server (`169.254.169.254` or `fd20:ce::254`) is essential for a healthy Windows instance. If the instance loses access to the metadata server, applications might fail to obtain credentials, and you might not be able to connect to the instance using RDP.

Messages in the Serial Port 1 console logs might provide clues about network or service failures during boot. For example, look for errors indicating that the instance can't connect to the metadata server (`169.254.169.254` or `fd20:ce::254`).

If the instance checks pass but you still can't reach the metadata server, follow the steps in [Troubleshoot metadata server access issues](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-metadata-server) to test and resolve the connection.

## Use the RDP troubleshooting script

Windows VM instances provided by Google include a diagnostic script that automates many of the checks in this document.

  1. [Connect to a Windows VM's SAC](https://docs.cloud.google.com/compute/docs/instances/connecting-to-sac).
  2. Open PowerShell by typing `powershell`.
  3. Run the following command to start the diagnostic:
         
         powershell -file "C:\Program Files\Google\Compute Engine\diagnostics\rdp_status.ps1" | more
         

  4. Review the output for any "FAIL" results and apply the suggested solutions.




## Check your Windows instance password

Each Compute Engine Windows instance must have a local password set if it is not already on a domain or custom image. Confirm you have the correct password set by connecting to the VM through the `Google Cloud CLI` command-line tool or Google Cloud console. For more information, see [Connect to a Windows VM's SAC](https://docs.cloud.google.com/compute/docs/instances/connecting-to-sac).

If you have problems connecting, try creating or resetting the password. For more information, see [Manage accounts and credentials on Windows VMs](https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials).

## Check if you're using Windows Server Core

When connecting using RDP, if you receive a Command Prompt window on a blank background this likely indicates you are using [Windows Server Core](https://learn.microsoft.com/en-us/windows-server/administration/server-core/what-is-server-core). To confirm that you are run the following command:
    
    
    reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion" /v InstallationType
    

`Server Core` in your output confirms that you are using Windows Core edition.
    
    
    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion
        InstallationType    REG_SZ    Server Core
    

If you require a graphical user interface for your workload, look at how to [create a Windows Server instance](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#start_instance), which contains Desktop Experience, instead of a Windows Server Core instance. Alternatively, you can review the Microsoft documentation for [managing Windows Core server](https://learn.microsoft.com/en-us/windows-server/administration/server-core/server-core-manage).

## Check your VPC firewall rules

Compute Engine automatically provisions new projects with a firewall rule that allows RDP traffic. If you have an existing project, or have modified the configurations, the default firewall rule that permits RDP might not exist. Confirm that a rule allows RDP traffic to connect to the network that your affected instance is on.

To check if the [**default-allow-rdp**](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) firewall rule exists on your project, check the [Firewall rules page](https://console.cloud.google.com/networking/firewalls), or run the following gcloud CLI command:
    
    
    gcloud compute firewall-rules list
    

To create a new rule if one does not exist, create a rule with the following command:
    
    
    gcloud compute firewall-rules create allow-rdp --allow tcp:3389
    

**Note:** The default port number for Windows RDP is 3389, however you can reconfigure this number. If you do, change the port number after `tcp:` in the "create rule" command to match.

## Verify the external IP address

Ensure that you're connecting to the correct external IP address for the instance. View the IP for the instance from the [VM instance page](https://console.cloud.google.com/compute/instances) or by using the following gcloud CLI command:
    
    
    gcloud compute instances list
    

## Use of Windows Remote Desktop Services (RDS)

If you have Windows Remote Desktop Services (formerly known as Terminal Services) installed on your instance, then the conditions of the Client Access Licenses (CALs) are enforced. With these CALs, RDP connections will fail under any of the following conditions:

  * You have used all your available licenses
  * Your license is installed, but not configured or activated correctly
  * Your RDS trial period of 180 days has expired



Symptoms that you may not have enough valid licenses include messages such as:

  * This remote session was disconnected because there are no Remote Desktop License Servers available to provide a license.
  * The remote session was disconnected because of an error related to licensing in terminal server.
  * The remote session was disconnected because there are no Remote Desktop client access licenses available for this computer.



If your RDP connections fail, you can use the administrator switch to connect to the instance for administrative purposes. This can be done on a Windows machine by using the built-in Remote Desktop Connection client.

**Note:** Using the administrator switch on a VM that has exhausted the available connection licences, can forcibly disconnect a user from the VM.
    
    
    %SystemRoot%\System32\mstsc.exe /admin
    

Two concurrent remote desktop sessions for administration are included with the on-demand Windows Server and SQL Server image.

To resolve issues with RDP connections, purchase new RDS licenses for your instance. For more details about CALs, review the [Microsoft documentation](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-client-access-license). Alternatively, if Remote Desktop Services are not required, uninstall the service and use regular RDP connections.

## Validate OS level configuration and resources

If the guest environment and configurations for the instance are correct, the operating system on the instance might be misconfigured. Additionally, without adequate resources it's possible that an RDP connection might fail to be established. To validate OS level configuration, [connect to the Windows SAC](https://docs.cloud.google.com/compute/docs/instances/connecting-to-sac):

  * Ensure the VM has adequate resources
  * Check the OS configuration



### Ensure the VM has adequate resources

Verify the CPU, memory, disk usage, and available disk space are not reaching their limits. This data can be inspected by viewing the [observability metrics](https://docs.cloud.google.com/compute/docs/instances/observe-monitor-vms) in the Google Cloud console. Some metrics are available only for VMs that have the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) installed. Alternatively, if the Ops Agent is not installed, use the following commands when connected to [SAC](https://docs.cloud.google.com/compute/docs/instances/connecting-to-sac):

CPU usage, memory usage, disk usage and disk capacity

  * CPU usage: 
        
        typeperf "\Processor(_Total)\% Processor Time" -sc 5

  * Memory usage: 
        
        typeperf "\Memory\% Committed Bytes In Use" -sc 5

  * Disk Usage: 
        
        typeperf "\LogicalDisk(*)\% Idle Time" -sc 5

  * Disk Capacity: 
        
        fsutil volume diskfree C:




The following are the recommended resource usages for an RDP connection, however these are just estimates, and might vary between instances.

  * CPU: <80%
  * Memory: <80%
  * Disk space: >20%
  * Disk idle: >50%



If any of the suggested estimates are reaching their limits, you can modify that resource for the VM instance. To edit VM properties, see how to [edit the machine type of a VM instance](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance) and [increase the size of a persistent disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk).

### Check the OS configuration

[Connect to the VM's SAC](https://docs.cloud.google.com/compute/docs/instances/connecting-to-sac) and run the following commands to ensure that the instance is accepting connections:

  1. Check to see that the ethernet adapter is enabled:

     * **Command:**
           
           netsh interface show interface

     * **Pass:** Admin state is set to _Enabled_ on Interface Name labeled _Ethernet_
     * **Fail:** Admin state is set to _Disabled_ on Interface Name labeled _Ethernet_
     * **Solution:** Enable the ethernet adapter: 
           
           netsh interface set interface Ethernet admin=enabled

  2. Check to see that the instance has a valid IP configuration:

     * **Command:**
           
           ipconfig /all

     * **Pass:** Ethernet Adapter _Ethernet_ will show an IPv4 Address of the subnet the instance is assigned to.
     * **Fail:** No IPv4 address, or an address that doesn't match what is shown in Google Cloud console.
     * **Solution:** Proceed to the next step.
**Note:** If an address is assigned and not "(Preferred)" this means that the IP address was assigned as static on the guest OS level. This should be set to DHCP to allow the metadata server to assign the correct IP address.
  3. Check to see that DHCP is enabled on the instance:

     * **Command:**
           
           netsh interface ipv4 show addresses

     * **Pass:** Output under _Ethernet_ contains _DHCP Enabled: Yes_.
     * **Fail:** Output under _Ethernet_ contains _DHCP Enabled: No_.
     * **Solution:** Enable DHCP on the ethernet adapter: 
           
           netsh interface ipv4 set address Ethernet dhcp

**Note:** Virtual network adapters on Google Cloud VM instances are set to "Ethernet" by default, but can be changed or have a number appended in the case of multi-nic instances. In these cases, substitute the interface name appropriately.
  4. Check to see that the 'Remote Desktop Service' is running:

     * **Command:**
           
           net start | find "Remote Desktop Services"

     * **Pass:** Remote Desktop Service
     * **Fail:** (Remote Desktop Service missing from output)
     * **Solution:** Start the Remote Desktop Services: 
           
           net start "Remote Desktop Services"

  5. Check that Remote Connections are enabled:

     * **Command** : 
           
           reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections

     * **Pass** : fDenyTSConnections REG_DWORD 0x0
     * **Fail** : fDenyTSConnections REG_DWORD 0x1
     * **Solution** : Enable remote desktop connections in the registry: 
           
           reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /f /v fDenyTSConnections /t REG_DWORD /d 0

  6. Ensure that the Windows firewall has Remote Desktop Connections enabled:

     * **Command** : 
           
           netsh advfirewall firewall show rule name="Remote Desktop - User Mode (TCP-In)"

     * **Pass** : Enabled:Yes, Direction: In, Profiles: Public, Grouping: Remote Desktop, LocalIP: Any, RemoteIP: Any, Protocol:TCP, LocalPort: 3389, RemotePort: Any, Edge traversal: No, Action: Allow

**Note:** This is the default configuration, so your requirements might be different.
     * **Fail** : (unexpected results, such as enabled = No)

     * **Solution** : Enable the default "Remote Desktop" firewall rule within Windows Firewall: 
           
           netsh advfirewall firewall set rule group="remote desktop" new enable=Yes

  7. Check to see what port number is configured for RDP connections on the remote instance:

     * **Command** : 
           
           reg query "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber

     * **Pass** : PortNumber REG_DWORD [PORT NUMBER]
     * **Fail** : (unexpected port number)
     * **Solution** : Configure the port number in the registry required for RDP: 
           
           reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /f /v PortNumber /t REG_DWORD /d [PORT NUMBER]

**Note:** Number is in hexadecimal, 0xd3d = 3389 (default port is 3389).
  8. Verify that another application is not trying to use the same port:

     * **Command** : 
           
           netstat -ano | find "3389"

     * **Pass** : Look for an entry for the assigned RDP port with a status of _Listening_. The matching service can be found using the process identifier (PID) by using the following command: 
           
           tasklist /svc | find ""

where PID is the identifier from the previous command. The output should only have _Termservice_ being returned.
     * **Fail** : Anything but the _Termservice_ is using the assigned port.
     * **Solution** : Configure the application or service to use another port number.
  9. Ensure that connected user account has permissions for remote connections:

     * **Command** : 
           
           net localgroup "Remote Desktop Users"

     * **Pass** : (target local or domain username in resulting list)
     * **Fail** : (target local or domain username missing)
     * **Solution** : Add the "Remote Desktop Users" rule to a user in the domain: 
           
           net localgroup "Remote Desktop Users" /add [DOMAIN\USERNAME]

The domain is required only for user accounts on a system joined to a different domain. For local accounts, specify only the username.

  10. Verify the client or server security negotiation is set to its [default value](https://learn.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/microsoft-windows-terminalservices-rdp-winstationextensions-securitylayer):

     * **Command** : 
           
           reg query "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v SecurityLayer

     * **Pass** : SecurityLayer REG_DWORD 0x1
     * **Fail** : SecurityLayer REG_DWORD 0x0 (or 0x2)
     * **Solution** : Set the security negotiation value in the registry: 
           
           reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v SecurityLayer /t REG_DWORD /d 1 /f

  11. In situations where your instance is connected to an Active Directory domain, but the connection couldn't be established, you might receive the following error when trying to access your instance:
         
         The remote computer that you are trying to connect to requires Network Level Authentication (NLA), but your Windows domain controller cannot be contacted to perform NLA.
         

Verify Network Level Authentication (NLA) is set to its [default value](https://learn.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/microsoft-windows-terminalservices-rdp-winstationextensions-userauthentication):

     * **Command** : 
           
           reg query "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication

     * **Pass** : UserAuthentication REG_DWORD 0x0
     * **Fail** : UserAuthentication REG_DWORD 0x1
     * **Solution** : Set the Network Level Authentication value in the registry: 
           
           reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /t REG_DWORD /d 0 /f

  12. Verify that your MTU size is no greater than the MTU of the network:

     * **Command** : 
           
           netsh interface ipv4 show subinterfaces

     * **Pass** : When the number after the MTU matches the MTU of the VPC network.
     * **Fail** : When the number after MTU is larger than the MTU of the VPC network.
     * **Solution** : Set the MTU of the interface to the MTU of the VPC network: 
           
           netsh interface ipv4 set subinterface Ethernet mtu=MTU_OF_VPC_NETWORK

**Note:** VPC networks have a default [maximum transmission unit (MTU)](https://www.wikipedia.org/wiki/Maximum_transmission_unit) of `1460` bytes. However, the network MTU can be set to the standard Ethernet MTU of `1500` bytes, up to `8896` bytes for jumbo frames, or as low as `1300`. For more information about network MTUs, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu). 

For more information about MTU size incompatibilities, see our [packet fragmentation](https://docs.cloud.google.com/compute/docs/troubleshooting/general-tips#packetfragmentation) documentation.

  13. If you try to connect to the VM by using RDP and the VM displays the keyboard layout screen, you need to select a language by connecting to Windows SAC. To select a language, complete the following steps:

     1. [Connect to the SAC](https://docs.cloud.google.com/compute/docs/instances/connecting-to-sac).
     2. Open Powershell by typing `powershell`.
     3. Get the correct language string.
            
            Get-WinUserLanguageList

     4. Set the layout. Replace `LANGUAGE_TAG` with the language layout you want (for example, `en-US`).
            
            Set-WinUserLanguageList -LanguageList LANGUAGE_TAG -force

     5. Reboot your instance.
            
            shutdown -r -t 0

  14. For RDP errors on the logon screen mentioning `you need the right to sign in through Remote Desktop Services` or `you must be granted the Allow log on through Terminal Services right`, the Remote Desktop Users or Administrators group was removed from Local Computer Policy setting found in [Allow log on through Remote Desktop Services](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/allow-log-on-through-remote-desktop-services) or _SeRemoteInteractiveLogonRight_.

**Note:** If you encounter this issue, contact Google Cloud Support.
  15. Verify there are no missing permissions blocking certificates authentication:

     * **Command** : 
           
           icacls.exe "C:\ProgramData\Microsoft\Crypto\RSA\MachineKeys"

     * **Pass** : Output resembles _Everyone:(R,W) BUILTIN\Administrators:(F)_
     * **Fail** : Output doesn't match _Everyone:(R,W) BUILTIN\Administrators:(F)_
**Note:** If you encounter this issue, contact Google Cloud Support.
  16. Ensure that your antivirus or endpoint protection client settings allow for the configured port number and services.

**Note:** This process will vary between products, and might not have a command line solution.
  17. **CredSSP encryption oracle remediation error** : If you receive an error mentioning "CredSSP encryption oracle remediation", make sure that both your workstation and the VM instance have the latest Windows updates installed.

  18. **Internal error code 0x4** : If your connection fails with "Error Code: 0x4", make sure that TLS 1.2 is enabled on the server. You can check the registry at `HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client`.

  19. **Error code 0x108** : If you receive "Error code: 0x108 (The two computers couldn't connect in the amount of time allotted)", check the [observability metrics](https://docs.cloud.google.com/compute/docs/instances/observe-monitor-vms) for high CPU or memory utilization. If resources are exhausted, consider [changing the machine type](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance).




## Verify session timeout limits

If you're able to establish an RDP connection but you are disconnected after some time with a message mentioning that your _Timer Expired_ verify the following values are as expected:

Registry Path: `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services`

Registry Keys:

  * `MaxDisconnectionTime`
  * `MaxIdleTime`
  * `MaxConnectionTime`
  * `MaxDisconnectionTime`
  * `RemoteAppLogoffTimeLimit`



These values are set in milliseconds. If these keys are missing from your registry then there are no session limits on your VM instance. If these keys are present in your registry but their values are set to `0`, then your session never expires.

## Troubleshoot Windows startup

If the previous troubleshooting steps have not resolved your RDP connection issue, your Windows instance may not be booting or running correctly. In this case, review our guide for [troubleshooting Windows](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows).

## What's next

  * Learn more about [troubleshooting the Windows operating system](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows).

  * Learn how to [collect diagnostic information from a VM](https://docs.cloud.google.com/compute/docs/instances/collecting-diagnostic-information).

  * Learn about [troubleshooting using the serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console).

  * Learn how to [capture screenshots from VMs](https://docs.cloud.google.com/compute/docs/troubleshooting/capturing-vm-screenshots).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
