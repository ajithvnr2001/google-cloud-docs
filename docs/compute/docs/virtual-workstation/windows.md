---
url: https://docs.cloud.google.com/compute/docs/virtual-workstation/windows/
title: Create a virtual Windows workstation \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:09.944404+00:00
---

# Create a virtual Windows workstation  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/virtual-workstation/windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a virtual Windows workstation Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to create a virtual Windows workstation running Windows Server 2022 with a [virtual display](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display). A virtual display device is useful when applications on your virtual machine (VM) instances require a display device, but don't require the full power or cost of a [GPU](https://docs.cloud.google.com/compute/docs/gpus).

For information about other types of virtual workstations, including Linux, see [About creating a virtual workstation](https://docs.cloud.google.com/compute/docs/virtual-workstation).

**Note:** This solution is not suitable for graphically intensive applications that require hardware graphics acceleration. For information about the types of virtual workstations that you can create on Google Cloud, see [Creating a virtual workstation](https://docs.cloud.google.com/compute/docs/virtual-workstation).

After you create the virtual workstation, you learn how to remotely access it using [HP Anyware](https://anyware.hp.com/) (formerly Teradici CAS), using [PC-over-IP (PCoIP®)](https://h20195.www2.hp.com/v2/GetDocument.aspx?docname=4AA8-3293ENW) technology, a remote desktop protocol widely used in the media and entertainment, game development, architecture, and engineering industries. PCoIP offers features essential to these types of workloads, such as color accuracy, support for multiple monitors, lossless display, and tablet pressure sensitivity.

This tutorial assumes you are familiar with Microsoft Windows and the PowerShell command line.

## Objectives

  * Create a Compute Engine VM. This VM serves as the foundation for a virtual workstation.
  * Install HP Anyware software on the virtual workstation.
  * Connect to the virtual workstation using a PCoIP software client.

**Note:** This tutorial does not include advanced security features such as fine-grained SSH key management, certificate issuance, or multi-factor authentication (MFA). A full deployment requires a [connection broker](https://wikipedia.org/wiki/Connection_broker) and [domain controller](https://wikipedia.org/wiki/Domain_controller_\(Windows\)), which help enable a stronger security profile for connecting to virtual workstations.

## Costs

This tutorial uses the following billable components of Google Cloud:

  * [Compute Engine](https://cloud.google.com/products/compute/pricing)



You can use the [pricing calculator](https://cloud.google.com/products/calculator/estimate-preview/CiQ1Njk1MDAzYi1jMjk3LTQ5YTUtODYyMC04ODU4NzliMTVmMzQQAQ==) to generate a cost estimate based on your projected usage.

The resources that make up the virtual workstation and the factors that affect cost in this tutorial are:

  * 4 vCPUs, 16 GB RAM [E2 standard machine type](https://docs.cloud.google.com/compute/vm-instance-pricing#general-purpose_machine_type_family)
  * [Windows licensing](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages)
  * 50-GB SSD [balanced boot disk](https://docs.cloud.google.com/compute/disks-image-pricing#persistentdisk)
  * [Internet outbound data transfer costs](https://docs.cloud.google.com/vpc/network-pricing#internet_egress)



Internet data transfer represents data that streams from your virtual workstation to your local display client and is billed at [internet outbound data transfer costs](https://docs.cloud.google.com/vpc/network-pricing#internet_egress). Variables that affect data transfer during a PCoIP session are bandwidth, screen resolution, number of display monitors, applications used, and the type of activity on each monitor. The HP Anyware [Session Planning Guide](https://www.teradici.com/web-help/pcoip_session_planning/current/) can help you understand different workload requirements.

**Note:** Costs differ depending on region and connection method. These estimated costs are based on connection over the public internet, with resources located in the `us-central1` region (Iowa).

## Before you begin

This tutorial uses the Google Cloud CLI, which you can run from a [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell) instance launched from the [](https://console.cloud.google.com/)[Google Cloud console](https://console.cloud.google.com/). If you want to use gcloud CLI on your local workstation, install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs). The tutorial shows you how to run commands in Cloud Shell; if you use the gcloud CLI on your workstation, adjust the instructions accordingly.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)




In addition, make sure you have the following:

  * A [Google Chrome](https://www.google.com/chrome/) browser to access the Google Cloud console.
  * The latest [PCoIP Client software](https://anyware.hp.com/find/product/hp-anyware) for Windows, Mac, or Linux to access the virtual workstation.
  * An account on [help.teradici.com](https://help.teradici.com/) to download the HP Anyware software. Account registration is free.
  * An HP Anyware software license. You can [request a trial license](https://reinvent.hp.com/Anyware-Demo), or contact your HP representative and ask for a trial registration code to use for this virtual workstation.



## Architecture

The following diagram shows the components that are used in this tutorial to deploy a single virtual workstation. Optional components shown in the diagram include different ways to connect to your virtual workstation, shared storage, an additional VM for serving third-party licenses, and additional infrastructure representing a render or compute farm.

![Architecture of the virtual workstation infrastructure.](https://docs.cloud.google.com/static/compute/docs/virtual-workstation/img/architecture.svg)

## Choose a region

An important factor when you deploy a virtual workstation is the latency between your location and the VM you create. The lower the latency, the better the experience. Therefore, you want to place your VM in a region and zone that's geographically closest to you.

## Create the virtual workstation

In Cloud Shell, create the Compute Engine virtual workstation instance:
    
    
    gcloud compute instances create VM_NAME \
        --zone=ZONE \
        --machine-type=e2-standard-4 \
        --enable-display-device \
        --image-project=windows-cloud \
        --image-family=windows-2022 \
        --boot-disk-size=50 \
        --boot-disk-type=pd-balanced \
        --network=default
    

Replace the following:

  * `VM_NAME`: a name for your VM instance.
  * `ZONE`: the zone that's geographically closest to you. An important factor when you deploy a virtual workstation is the latency between your location and the VM you create. The lower the latency, the better the experience. For information about the geographical location of zones, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).



After the virtual workstation is created, the VM status is displayed. The output looks similar to the following:
    
    
    NAME: test-workstation
    ZONE: us-west1-b
    MACHINE_TYPE: e2-standard-4
    PREEMPTIBLE:
    INTERNAL_IP: 10.138.XX.XXX
    EXTERNAL_IP: XX.XXX.XXX.XXX
    STATUS: RUNNING
    

Note the external IP address, you need it later in the tutorial.

## Create a Windows password

You use RDP to access the Windows virtual workstation in order to install the HP Anyware Standard Agent host software. To sign in with RDP, you need to create a Windows password for your user.

  1. In Cloud Shell, run the following command:
         
         gcloud compute reset-windows-password VM_NAME

Replace `VM_NAME` with the name of the VM to change the password for.

  2. Review the information in the confirmation prompt:
         
         This command creates an account and sets an initial password for the
         user [username] if the account does not already exist.
         If the account already exists, resetting the password can cause the
         LOSS OF ENCRYPTED DATA secured with the current password, including
         files and stored passwords.
         
         For more information, see:
         https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials#console
         
         Would you like to set or reset the password for [username] (Y/n)?
         

  3. After confirming the previous prompt, review the confirmation of new credentials, which appears as follows:
         
         Resetting and retrieving password for [username] on [instance-name]
         Updated [https://www.googleapis.com/compute/v1/projects/project-name/zones/zone/instances/instance-name].
         ip_address: ip-address
         password:   password
         username:   username
         

  4. You can now [connect to the VM instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) by using the new credentials.


**Note:** You can't retrieve this auto-generated password after you close the Cloud Shell window. If necessary, you can repeat this step to generate a new Windows password. It's a good practice to [set a custom password](https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials#change_your_password) after you've signed in to the virtual workstation. If you have difficulty connecting using RDP, see the [Troubleshooting RDP](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp) page.

## Sign in to your virtual workstation

After you create the virtual workstation, sign into the machine so you can configure it.

  1. On your local workstation, use your RDP client to connect to your virtual workstation using its external IP address.
  2. When you're prompted to enter your credentials, enter the username and password you generated earlier.
  3. If you see a certificate warning, ignore it and click **Continue**.



The virtual workstation desktop appears. Close the Windows Server Manager after it finishes launching.

## Install Google Chrome

The next step is to install Chrome on the VM instance.

  1. In your RDP session, click the **Start** button on the Windows taskbar, type `Windows PowerShell`.
  2. Right-click on Windows PowerShell and select **Run as administrator**.
  3. At the PowerShell prompt, enable HTTPS requests:
         
         [Net.ServicePointManager]::SecurityProtocol = "tls12, tls11, tls"
         

  4. Download and run the Chrome installer:
         
         $installer = "$env:TEMP\chrome_installer.exe";
         Write-Host 'Downloading Chrome.'
         Invoke-WebRequest `
         'https://dl.google.com/chrome/install/latest/chrome_installer.exe' `
           -OutFile $installer
         Write-Host 'Installing Chrome.'
         & $installer /silent /install | Out-Default
         Remove-Item $installer
         

  5. When the command has completed, close PowerShell.




## Install HP Anyware software

HP Anyware software provides an agent that runs on your virtual workstation, delivering the desktop to your hardware or software client.

  1. On the Windows instance, open Google Chrome and go to the [PCoIP Hosts section](https://anyware.hp.com/find/product/hp-anyware) on the HP Anyware support page.
  2. Download **Standard Agent for Windows**.
  3. If not already logged in, click **Log in to download**.
  4. Click **Downloads and scripts**.
  5. Complete the agent installation process and choose the option to run the downloaded Standard Agent executable. Follow the prompts to install the Standard Agent in the default location.



## Register the Anyware Standard Agent

When the installation process is complete, you're prompted for a registration code.

  1. In the **License Registration** window, enter the registration code you received during the trial sign-up process.

**Note:** The registration code provided to you by HP Teradici is in the form `ABCDEFGHIJKL@0123-4567-89AB-CDEF`.
  2. After you've entered the registration code, reboot the Windows instance.




## Create a firewall rule

The PCoIP client communicates with your virtual workstation using several ports. You must set firewall rules that allow traffic to your virtual workstation.

  * In Cloud Shell (not on the virtual workstation), create a firewall rule that opens the required ports:
        
        gcloud compute firewall-rules create allow-pcoip \
            --action=ALLOW \
            --rules=tcp:443,tcp:4172,udp:4172 \
            --source-ranges=0.0.0.0/0
        

**Note:** This firewall rule allows traffic from anywhere on the internet to access your VM instance. Always follow [best practices for firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls#best_practices_for_firewall_rules) to restrict traffic to your instance.



## Sign in to your virtual workstation using the PCoIP client

  1. On your local computer, go to the **PCoIP Clients** section on the [HP Anyware support page](https://anyware.hp.com/find/product/hp-anyware), and then download, install, and launch the PCoIP Software Client application for your operating system.

  2. In the **Host Address or Registration Code** field, enter the external IP address of your virtual workstation. If you want, you can enter a name for the connection.

**Note:** By default, PCoIP traffic is encrypted using AES-256. However, HP Anyware Software uses a self-signed certificate that's issued by Teradici. This might trigger a verification warning when you connect. You can remove this warning by creating and installing your own [custom security certificates](https://anyware.hp.com/generic/unassigned/documentation/administrators-guide/security-guide/creating-custom-certificates). Or, you can suppress the warning by changing the [client security mode](https://www.teradici.com/web-help/pcoip_client/mac/current/security/software_client_security_modes/) for your client OS. For the purposes of this tutorial, you can ignore this warning by clicking **Connect Insecurely** in the dialog.
  3. When you are connected, authenticate by entering the username and password that you created earlier for the virtual workstation.

In a few seconds, your Windows desktop appears.




## Activate audio on your virtual workstation

To activate audio on your virtual workstation, enable the _Teradici Virtual Audio Driver_ as the default playback device.

  1. On the Windows VM, click the Start button on the Windows taskbar and type `mmsys.cpl` to open the Sound control panel and initialize the Teradici Virtual Audio Driver.

  2. Click **Yes**. Windows verifies that the audio driver is working.




## Test your virtual workstation

After you've deployed your virtual workstation, you can test performance and interactivity using a number of tools:

  * Use [Google Chrome](https://www.google.com/chrome/) to browse your favorite sites or play [YouTube](https://www.youtube.com/) videos.
  * Install the Teradici [Session Statistics Viewer](https://anyware.hp.com/knowledge/pcoip-session-statistics-viewer) to examine bandwidth usage, latency, and other desktop streaming metrics.
  * Learn more about configuring the [Teradici Standard Agent for Windows](https://www.teradici.com/web-help/pcoip_agent/standard_agent/windows/current/admin-guide/configuring/configuring/).
  * Install applications and test their behavior and performance.



You can also learn more about [PCoIP performance optimization](https://www.teradici.com/web-help/pcoip_session_planning/current/optimization/performance-optimization/) based on your workload.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Stop your virtual workstation

Stopped virtual workstations incur [costs for persistent disk](https://docs.cloud.google.com/persistent-disk) usage, but they can be restarted at any time. To stop your virtual workstation, run the following command:
    
    
    gcloud compute instances stop VM_NAME

### Delete all the components

  1. [Delete the virtual workstation](https://docs.cloud.google.com/compute/docs/instances/stopping-or-deleting-an-instance#delete_an_instance).
  2. [Delete the firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#deleting_firewall_rules).



### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn how to [create a virtual Linux workstation](https://docs.cloud.google.com/compute/docs/virtual-workstation/linux).
  * Learn more about [HP Anyware software](https://www.hp.com/us-en/services/workforce-solutions/workforce-computing/digital-workspaces.html).
  * Learn more about how [PCoIP](https://h20195.www2.hp.com/v2/GetDocument.aspx?docname=4AA8-3293ENW) differs from other remote desktop software.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
