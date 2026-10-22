---
url: https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows/
title: Connect to Windows VMs using RDP \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:30.873299+00:00
---

# Connect to Windows VMs using RDP  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Connect to Windows VMs using RDP Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

This document describes how to connect to Windows virtual machine (VM) instances using RDP. For other ways to connect to Windows VMs, see the following guides:

  * [Connect to Windows VMs using PowerShell](https://docs.cloud.google.com/compute/docs/instances/windows/connecting-powershell)
  * [Connect to a Windows VM's SAC](https://docs.cloud.google.com/compute/docs/instances/connecting-to-sac)
  * [Connect to Windows VMs using SSH](https://docs.cloud.google.com/compute/docs/connect/windows-ssh)

**Note:** When a user connects to a VM, that user can use all of the IAM permissions granted to the service account attached to the VM. 

## Before you begin

  * Be sure the VM allows access through Remote Desktop Protocol (RDP). By default, Compute Engine creates firewall rules that allow RDP access on TCP port 3389. Verify that these firewall rules exist by visiting the [firewall rules page in the Google Cloud console](https://console.cloud.google.com/networking/firewalls) and looking for firewall rules that allow `tcp:3389` connections.
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




## Connect to Windows VMs by using RDP

Compute Engine supports multiple ways to connect to your Windows instances.

![Connecting to Windows instances.](https://docs.cloud.google.com/static/compute/images/connecting-to-windows-instances.svg)

The best way to connect to the remote desktop of a Windows instance depends on multiple factors:

  * If you are connecting from anywhere over the public internet (Connecting from > **Anywhere** in the previous illustration), it's best to enable [Identity-Aware Proxy TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) for your project. Then use IAP Desktop (on Windows) or the Google Cloud CLI in combination with an RDP client. For more information, see [Microsoft Remote Desktop clients](https://docs.microsoft.com/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients) to connect to the Windows instance. If you cannot use Identity-Aware Proxy TCP forwarding, use [Chrome Remote Desktop](https://remotedesktop.google.com/).
  * If the compute instance has a public IP address and firewall rules permit RDP access, use an RDP client. For more information, see [Microsoft Remote Desktop clients](https://docs.microsoft.com/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients) to connect to the Windows instance.
  * If the compute instance does not have a public IP and you are connecting by using [Cloud VPN or Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product), you can connect to the VM's private IP address by using an RDP client For more information, see [Microsoft Remote Desktop clients](https://docs.microsoft.com/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients).



If you have difficulty connecting using RDP, see [Troubleshooting RDP](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp). If you can't connect to a Windows instance by using Remote Desktop, see [Connect to a Windows VM's SAC](https://docs.cloud.google.com/compute/docs/instances/connecting-to-sac).

To connect to the remote desktop of a Windows instance, use one of the following procedures.

###  IAP Desktop 

[IAP Desktop](https://googlecloudplatform.github.io/iap-desktop/?utm_source=cloud.google.com) is a Windows application that lets you manage multiple Remote Desktop connections to Windows compute instances. IAP Desktop connects to compute instances by using [Identity-Aware Proxy TCP forwarding](https://docs.cloud.google.com/iap/docs/tcp-forwarding-overview) and does not require compute instances to have a public IP address.

Before you connect by using IAP Desktop, make sure that the following prerequisites are met:

  * You've configured your VPC to [allow IAP traffic to your compute instance](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#create-firewall-rule).
  * You've [downloaded and installed](https://github.com/GoogleCloudPlatform/iap-desktop/releases/latest/download/IapDesktop.msi) IAP Desktop on your local computer.



To connect to a compute instance by using IAP Desktop, do the following:

  1. In IAP Desktop, select **Profile > Add project**.

  2. Enter the ID or name of your project, and click **OK**.

  3. In the **Project Explorer** window, right-click the compute instance you want to connect to and select **Connect**.

![IAP Desktop.](https://docs.cloud.google.com/static/iap/images/iap-desktop.png)




For more information about IAP Desktop, see the [GitHub project page](https://googlecloudplatform.github.io/iap-desktop/?utm_source=cloud.google.com).

**Note:** IAP Desktop is an open-source project and not an officially supported Google product.

###  Remote Desktop Connection app 

You can use the Microsoft Remote Desktop Connection app that is part of Windows to connect to Windows instances.

Before you connect using the Microsoft Remote Desktop Connection app, make sure that one of the following prerequisites is met:

  * Your compute instance has a public IP address and your [firewall rules](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp#firewall_rules) allow TCP ingress traffic from your client's public IP address to the instance by using port 3389.
  * Your local network is connected to your VPC by using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) and your [firewall rules](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp#firewall_rules) allow TCP ingress traffic from your client's private IP address to the instance by using port 3389.



To connect with Microsoft Windows Remote Desktop, do the following:

  1. [Create a Windows account and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) if you don't have one yet.

  2. To connect over the internet, use the _external_ IP address. To connect by using Cloud VPN or Cloud Interconnect, use the _internal_ IP address.

Identify the external and internal IP addresses of your Windows instance by completing one of the following steps:

     * In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

     * By using the gcloud CLI, run `gcloud compute instances list`:
           
           gcloud compute instances list

  3. Open Microsoft Windows Remote Desktop Connection on your Windows machine. You can find the executable at `%systemroot%\system32\mstsc.exe`

![The Remote Desktop Connection dialog.](https://docs.cloud.google.com/static/compute/images/mstsc.png)

  4. In the **Computer** box, enter the IP address.

If you've configured your instance to use a different port number for RDP, add it after the IP address, for example: `1.2.3.4:3389`.

  5. Click **Connect**.

  6. Enter your username and password, and click **OK**.

If you have forgotten your password, you can [reset it](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances).




###  Chrome Remote Desktop 

[Chrome Remote Desktop](https://support.google.com/chrome/answer/1649523/) is a service that lets you remotely access another computer by using a web browser. Chrome Remote Desktop works on Windows, macOS, and Linux and does not require the compute instance to have a public IP address.

Before you connect by using Chrome Remote Desktop, make sure that the following prerequisites are met:

  * You've [created a Windows account and password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances) on the compute instance.
  * You've [installed the Chrome Remote Desktop service on the compute instance](https://docs.cloud.google.com/solutions/chrome-desktop-remote-windows-compute-engine).



To connect to a compute instance by using Chrome Remote Desktop, do the following:

  1. On your local computer, go to the [Chrome Remote Desktop](https://remotedesktop.google.com/access) website.

  2. If you're not already signed in to Google, sign in with the same Google Account that you used to set up the Chrome Remote Desktop service.

  3. Select the instance that you want to connect to.

  4. When you're prompted, enter the PIN that you created when installing the Chrome Remote Desktop service, and click the arrow_forward arrow button to connect.




###  Other 

You can connect to your Windows compute instances by using other RDP clients, such as clients developed for Android, iOS, Mac, and others. For a list of officially supported clients, see [Microsoft Remote Desktop clients](https://docs.microsoft.com/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients).

Before you connect, make sure that one of the following prerequisites is met:

  * Your compute instance has a public IP address and your [firewall rules](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp#firewall_rules) allow TCP ingress traffic from your client's public IP address to the instance by using port 3389.
  * Your local network is connected to your VPC by using [VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) and your [firewall rules](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp#firewall_rules) allow TCP ingress traffic from your client's private IP address to the instance by using port 3389.



To connect using other RDP clients, do the following:

  1. To connect over the internet, use the _external_ IP address. To connect by using Cloud VPN or Cloud Interconnect, use the _internal_ IP address.

Identify the external and internal IP addresses of your Windows instance by completing one of the following steps:

     * In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

     * By using the gcloud CLI, run `gcloud compute instances list`:
           
           gcloud compute instances list

  2. Install the supported client according to the client's installation instructions.

  3. Connect using the IP address of your instance, and authenticate with your username and password for the instance.




If you have difficulty connecting using RDP, see the [Troubleshooting RDP](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp) page. For information about RDP licensing, see the [FAQ about Microsoft licenses](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing-faq#are_remote_desktop_services_rds_client_access_licenses_cals_required_for_on-demand_vm_instances).

### Verify the RDP certificate

Verify the RDP certificate by viewing the serial port output from the initial boot of the VM or by using the appropriate PowerShell command from the SAC.

###  Serial port 

  1. During the initial boot of the Windows VM, [view the output from serial port 1](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output#viewing_serial_port_output).

  2. In the output, look for the following details:
         
         Serial port 1 (console) output for rdp-test
         ...
         ...
         2021/03/31 15:53:58 GCEInstanceSetup: RDP certificate details: Subject: CN=rdp-test, Thumbprint: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
         ...
         ...
         

**Note:** In some cases, the `Thumbprint:` field might be empty in the console output. If the field is empty, then verify the certificate by using the PowerShell method described in the **PowerShell from the SAC** tab in this section.



###  PowerShell from the SAC 

  1. Connect to the Windows SAC.

  2. Run the following PowerShell commands:
         
         # WinRM Cert
         Write-Host 'WinRM certificate details:'; Get-ChildItem 'Cert:\LocalMachine\My' | Where-Object { $_.Subject -like "CN=$env:COMPUTERNAME*" -and $_.NotAfter -gt $(Get-Date) -and $_.HasPrivateKey} |  Select-Object Subject, Thumbprint | Format-List
         # RDP Cert
         Write-Host 'RDP certificate details:'; Get-ChildItem 'Cert:\LocalMachine\Remote Desktop\' | Where-Object { $_.Subject -like "CN=$env:COMPUTERNAME*" -and $_.NotAfter -gt $(Get-Date) -and $_.HasPrivateKey} |  Select-Object Subject, Thumbprint | Format-List
         




## What's next

  * Learn how to [transfer files to Windows VMs](https://docs.cloud.google.com/compute/docs/instances/transfer-files-windows).
  * Learn how to [Connect to Linux VMs](https://docs.cloud.google.com/compute/docs/connect/standard-ssh).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
