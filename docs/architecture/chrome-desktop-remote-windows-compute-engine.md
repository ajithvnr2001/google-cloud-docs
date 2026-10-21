---
url: https://docs.cloud.google.com/architecture/chrome-desktop-remote-windows-compute-engine/
title: Set up Chrome Remote Desktop for Windows on Compute Engine \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:45.724433+00:00
---

# Set up Chrome Remote Desktop for Windows on Compute Engine  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/chrome-desktop-remote-windows-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Set up Chrome Remote Desktop for Windows on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-12 UTC

This tutorial shows you how to set up the [Chrome Remote Desktop](https://support.google.com/chrome/answer/1649523) service on a Microsoft Windows virtual machine (VM) instance on Compute Engine. For separate instructions for Linux VMs, see [Linux virtual machines](https://docs.cloud.google.com/architecture/chrome-desktop-remote-on-compute-engine). Chrome Remote Desktop lets you remotely access applications with a graphical user interface from a local computer or mobile device.

When following this tutorial, the default firewall rules allow Chrome Remote Desktop connections; you don't need to configure any additional firewall rules.

The VM does need access to the internet (either with an external IP address or through [Cloud NAT](https://docs.cloud.google.com/nat)), and you use your Google Account for authentication and authorization.

Two methods of setting up Chrome Remote Desktop are described:

  * An interactive method using Windows Remote Desktop Protocol (RDP).

This method requires that the VM be directly accessible from your local machine using an RDP client, which may not be possible in all situations.

  * A non-interactive method using a [startup script](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows) to install and configure Chrome Remote Desktop while the VM is being created.

This method should be used if you have firewalls preventing direct access to the VM, or if you don't have access to an RDP client—for example, on Chrome OS.


**Note:** This solution is not suitable for graphically intensive applications, including playing videos, because those typically require hardware graphics acceleration as well as a network that has high bandwidth and low latency. If you want to run graphically intense applications remotely, see the [Creating a virtual GPU-accelerated Windows workstation](https://docs.cloud.google.com/solutions/creating-a-virtual-gpu-accelerated-windows-workstation) tutorial for an alternative solution.

This tutorial assumes that you are familiar with Microsoft Windows and the PowerShell command line.

For information about other options for creating virtual workstations, see [Creating a virtual workstation](https://docs.cloud.google.com/solutions/creating-a-virtual-workstation).

## Objectives

  * Create a Windows Compute Engine VM instance to run Chrome Remote Desktop on.
  * Install and configure the Chrome Remote Desktop service on the VM instance.
  * Connect from your local computer to the desktop environment on the VM instance.



## Costs

This tutorial uses billable components of Google Cloud, including:

  * Compute Engine



Use the [Pricing Calculator](https://cloud.google.com/products/calculator/#id=6bfdb97f-013e-480a-b02a-a9192be6ce09) to generate a cost estimate based on your projected usage.

## Before you begin

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

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

  8. Make sure that you have the following role or roles on the project: roles/compute.admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 
  9. You use the [Google Chrome](https://www.google.com/chrome/) browser on your local machine.
  10. If you're using the interactive method, your local machine needs to have an RDP client and be able to make a direct RDP connection to the remote VM instance.



## Interactive installation using RDP

To install Chrome Remote Desktop interactively, you need to be able to connect to the remote VM using an RDP client. In this tutorial, you create the VM in the [default VPC with default firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#more_rules_default_vpc), which exposes the RDP port 3339 to the internet.

If this is not possible in your environment, use the non-interactive method that's described later in this document.

### Create a Compute Engine instance

For the purposes of this tutorial, the default machine type is used. If you are using this for your own environment, you may want to adjust the machine type, name, [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones), boot disk size, or other settings.

###  Console 

  1. In the Google Cloud console, go to the **VM Instances** page:



[Go to VM Instances](https://console.cloud.google.com/compute/instances/)

  1. Click **Create**.

  2. Set the instance name to `crdhost`.

  3. Enable the **Enable display device** checkbox because Chrome Remote Desktop requires a display device on Windows VMs.

  4. Under **Boot disk** , click **Change** to open the **Boot disk** panel.

  5. From the **Operating system** list, select **Windows Server**.

  6. From the **Version** list, select **Windows Server 2022 Datacenter**.

  7. Click **Select** to close the panel.

  8. Click **Create**.




###  Cloud Shell 

  1. Open Cloud Shell.

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Set your preferred zone:
         
         ZONE=us-central1-b
         REGION=us-central1
         gcloud config set compute/zone "${ZONE}"
         

  3. Create a Compute Engine instance by using the app image for Windows Server 2022 Datacenter:
         
         gcloud compute instances create crdhost \
             --machine-type=e2-medium \
             --scopes=cloud-platform \
             --enable-display-device \
             --image-family=windows-2022 \
             --image-project=windows-cloud \
             --boot-disk-size=50GB \
             --boot-disk-device-name=crdhost
         

This command creates a Windows Server 2022 virtual machine that has an attached display device (required for Chrome Remote Desktop on Windows VMs) a 50GB boot disk, and grants the instance full access to Google Cloud APIs.

Ignore the disk performance warning because you don't need high performance for this tutorial.




### Connect to the VM instance by using RDP

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Make sure a green check mark _check_ is displayed next to the name of your `crdhost` instance, indicating that the instance is ready.

  3. Click the instance name `crdhost` to open the **VM instance details** page.

  4. Under **Remote access** , click **Set Windows password** , and then click **Set** to create your account on the remote machine.

This step generates a password for you. Make a note of the password or copy it to a secure temporary file.

  5. To connect to the remote instance, click the arrow _arrow_drop_down_ next to the **RDP** button, and then select **Download the RDP file**. You can open the RDP file by using your preferred RDP client.

  6. When your RDP client prompts for a password, enter the password that you generated earlier.

  7. When you're prompted whether you want your computer discoverable by other PCs and devices on the network, click **No**.

  8. Close the **Server Manager Dashboard** if it is open.




### Install the Chrome Remote Desktop service

The next step is to install Google Chrome and the Chrome Remote Desktop service on the VM instance.

  1. In your RDP session, click **Start** on the Windows taskbar, type `PowerShell`, and then select the Windows PowerShell app.

  2. At the PowerShell prompt, download and run the Chrome Remote Desktop Host installer.
         
         $installer = "$env:TEMP\chromeremotedesktophost.msi"
           $uri = 'https://dl.google.com/edgedl/chrome-remote-desktop/chromeremotedesktophost.msi'
           (New-Object Net.WebClient).DownloadFile($uri,"$installer")
           Start-Process $installer -Wait
           Remove-Item $installer
         

  3. When you're prompted, confirm that you want the installer to make changes.




### Set up the Chrome Remote Desktop service

You now generate a Windows command that starts the Chrome Remote Desktop service and links it to your Google Account.

  1. On your local computer, using the Chrome browser, go to the [Chrome Remote Desktop command line setup page](https://remotedesktop.google.com/headless).

  2. If you're not already signed in, sign in with a Google Account. This is the account that will be used for authorizing remote access.

  3. On the **Set up another computer** page, click **Begin** , then **Next**.

  4. Click **Authorize**.

You need to allow Chrome Remote Desktop to access your account. If you approve, the page displays several command lines, one of which is for **Windows (Powershell)** that looks like the following:
         
         & "${Env:PROGRAMFILES(X86)}\Google\Chrome Remote Desktop\CurrentVersion\remoting_start_host.exe" `
         --code="4/ENCODED_AUTHENTICATION_TOKEN" `
         --redirect-url="https://remotedesktop.google.com/_/oauthredirect" `
         --name=$Env:COMPUTERNAME
         

  5. Click **Copy** _content_copy_ to copy the command line to your clipboard.

  6. In your RDP session, at the Powershell prompt, paste the command line you just copied and press `Enter`.

  7. When you're prompted, confirm that you want the application to make changes.

  8. When you're prompted, enter a 6-digit PIN. This number will be used for additional authorization when you connect later.

After the command completes, your remote desktop service has started.

  9. Close the Powershell window.

  10. Close the RDP session.




You can now connect to the VM using Chrome Remote Desktop.

## Non-interactive installation

In this approach, you configure the VM instance to have a [startup script](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/windows) that runs when the VM is created.

With this approach, the VM does not need to be directly accessible _from_ the internet, although it still needs access _to_ the internet.

### Authorize the Chrome Remote Desktop service

You now generate a Windows command that you use later in the specialize script. As part of this procedure, you provide authorization information that's included in the command.

  1. On your local computer, using the Chrome browser, go to the [Chrome Remote Desktop command line setup page](https://remotedesktop.google.com/headless).

  2. If you're not already signed in, sign in with a Google Account. This is the account that will be used for authorizing remote access.

  3. Click **Begin** , and then click **Next**.

  4. Click **Authorize**.

  5. Allow Chrome Remote Desktop to access your account.

The page now contains several command lines, one of which is for **Windows (Cmd)** that looks like the following:
         
         "%PROGRAMFILES(X86)%\Google\Chrome Remote Desktop\CurrentVersion\remoting_start_host.exe"
         --code="4/ENCODED_AUTHENTICATION_TOKEN"
         --redirect-url="https://remotedesktop.google.com/_/oauthredirect"
         --name=%COMPUTERNAME%
         

The `--code` flag contains a unique short-lived OAuth token.

The authorization code in the command line is valid for only a few minutes, and you can use it only once.

Keep this page open.




### Copy the startup command to Cloud Shell

The next step is to create a file in your Cloud Shell instance that contains the startup command that you just generated.

  1. Open Cloud Shell.

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Create a file for the startup command:
         
         cat  > crd-auth-command.txt
         

  3. Go to the page that has the Chrome Remote Desktop startup command and copy the **Windows (Cmd)** command line.

  4. In Cloud Shell paste the command to add it to the file.

  5. Press `Enter` to end the line, and then press `Control-D` to close the file.




### Create the startup script

  * Copy the following code block and paste it into Cloud Shell.
        
        cat << "EOF" > crd-sysprep-script.ps1
        <#
            .SYNOPSIS
            GCESysprep specialize script for unattended Chrome Remote Desktop installation.
        #>
        $ErrorActionPreference = 'stop'
        
        function Get-Metadata([String]$metadataName) {
          try {
            $value = (Invoke-RestMethod `
                -Headers @{'Metadata-Flavor' = 'Google'} `
                -Uri "http://metadata.google.internal/computeMetadata/v1/instance/attributes/$metadataName")
          }
          catch {
            # Report but ignore REST errors.
            Write-Host $_
          }
          if ($value -eq $null -or $value.Length -eq 0) {
            throw "Metadata value for ""$metadataName"" not specified. Skipping Chrome Remote Desktop service installation."
          }
          return $value
        }
        
        # Get config from metadata
        #
        $crdCommand = Get-Metadata('crd-command')
        $crdPin = Get-Metadata('crd-pin')
        $crdName = Get-Metadata('crd-name')
        
        if ($crdPin -isNot [Int32] -or $crdPin -gt 999999 -or $crdPin -lt 0) {
          throw "Metadata ""crd-pin""=""$crdPin"" is not a 6 digit number. Skipping Chrome Remote Desktop service installation."
        }
        # Prefix $crdPin with zeros if required.
        $crdPin = $crdPin.ToString("000000");
        
        # Extract the authentication code and redirect URL arguments from the
        # remote dekstop startup command line.
        #
        $crdCommandArgs = $crdCommand.Split(' ')
        $codeArg = $crdCommandArgs | Select-String -Pattern '--code="[^"]+"'
        $redirectArg = $crdCommandArgs | Select-String -Pattern '--redirect-url="[^"]+"'
        
        if (-not $codeArg) {
          throw 'Cannot get --code= parameter from crd-command. Skipping Chrome Remote Desktop service installation.'
        }
        if (-not $redirectArg) {
          throw 'Cannot get --redirect-url= parameter from crd-command. Skipping Chrome Remote Desktop service installation.'
        }
        
        Write-Host 'Downloading Chrome Remote Desktop.'
        $installer = "$env:TEMP\chromeremotedesktophost.msi"
        $uri = 'https://dl.google.com/edgedl/chrome-remote-desktop/chromeremotedesktophost.msi'
        (New-Object Net.WebClient).DownloadFile($uri,"$installer")
        Write-Host 'Installing Chrome Remote Desktop.'
        & msiexec.exe /I $installer /qn /quiet | Out-Default
        Remove-Item $installer
        
        Write-Host 'Starting Chrome Remote Desktop service.'
        & "${env:ProgramFiles(x86)}\Google\Chrome Remote Desktop\CurrentVersion\remoting_start_host.exe" `
            $codeArg $redirectArg --name="$crdName" -pin="$crdPin" | Out-Default
        
        Write-Host 'Downloading Chrome.'
        $installer = "$env:TEMP\chrome_installer.exe"
        $uri = 'https://dl.google.com/chrome/install/latest/chrome_installer.exe'
        (New-Object Net.WebClient).DownloadFile($uri,"$installer")
        Write-Host 'Installing Chrome.'
        & $installer /silent /install | Out-Default
        Remove-Item $installer
        
        EOF
        

This code block is a PowerShell script that runs when the VM is created. It performs the following actions:

    * Downloads and installs the Chrome Remote Desktop host service.
    * Retrieves the following metadata parameters: 
      * `crd-command` \- the Windows authentication and startup command.
      * `crd-pin` \- the 6-digit PIN used for additional authentication.
      * `crd-name` \- the name for this instance.
    * Configures and starts the Chrome Remote Desktop host service.
    * Downloads and installs the Chrome browser.



### Create a new Windows virtual machine

You now create a new Windows VM using the files you created earlier to configure and set up Chrome Remote Desktop.

For the purposes of this tutorial, the `e2-medium` machine type is used. If you are using this for your own environment, you may want to adjust the machine type, name, region, boot disk size, or other settings.

  1. In Cloud Shell, set your preferred zone:
         
         ZONE=us-central1-b
         REGION=us-central1
         gcloud config set compute/zone "${ZONE}"
         

  2. Set a 6-digit PIN for additional authentication to Chrome Remote Desktop:
         
         CRD_PIN=your-pin
         

Replace your-pin with a 6-digit number.

  3. Set a name for this VM instance:
         
         INSTANCE_NAME=crdhost
         

  4. Create the instance:
         
         gcloud compute instances create ${INSTANCE_NAME} \
             --machine-type=e2-medium \
             --scopes=cloud-platform \
             --enable-display-device \
             --image-family=windows-2022 \
             --image-project=windows-cloud \
             --boot-disk-size=50GB \
             --boot-disk-device-name=${INSTANCE_NAME} \
             --metadata=crd-pin=${CRD_PIN},crd-name=${INSTANCE_NAME} \
             --metadata-from-file=crd-command=crd-auth-command.txt,sysprep-specialize-script-ps1=crd-sysprep-script.ps1
         

This command creates a Windows Server 2022 virtual machine in the default VPC that has an attached display device (required for Chrome Remote Desktop on Windows VMs), a 50GB boot disk, and grants the instance full access to Google Cloud APIs.

The metadata values specify the specialize script, Windows startup command line, and the parameters required to start the Chrome Remote Desktop service.




### Monitor the VM startup

You can verify that the startup script is successful by checking the messages logged to the VM's serial port while it is being created.

  1. In Cloud Shell, display the messages logged during VM startup:
         
         gcloud compute instances tail-serial-port-output ${INSTANCE_NAME}
         

If the Chrome Remote Desktop configuration is successful, you see the following log lines:
         
         Found sysprep-specialize-script-ps1 in metadata.
         sysprep-specialize-script-ps1: Downloading Chrome Remote Desktop.
         sysprep-specialize-script-ps1: Installing Chrome Remote Desktop.
         sysprep-specialize-script-ps1: Downloading Chrome.
         sysprep-specialize-script-ps1: Installing Chrome.
         sysprep-specialize-script-ps1: Starting Chrome Remote Desktop service.
         Finished running specialize scripts.
         

You might also see the following line: 
         
         sysprep-specialize-script-ps1: ... Failed to read 'C:\ProgramData\Google\Chrome Remote Desktop\host_unprivileged.json'.: The system cannot find the path specified. (0x3)
         

This is normal and can be ignored.

If starting the Chrome Remote Desktop service fails, you see an error message indicating the problem, for example:
         
         sysprep-specialize-script-ps1: Couldn't start host: OAuth error.
         

This error indicates that the OAuth token from the Chrome Remote Desktop authentication page is no longer valid, either because it has already been used, or because it has expired.

To correct this error, either connect using RDP and perform an interactive setup as described previously, or delete the VM and retry the setup process.

When you see the following message in the serial port monitor, the VM is ready.
         
         GCEInstanceSetup: ------------------------------------------------------------
         GCEInstanceSetup: Instance setup finished. crdhost is ready to use.
         GCEInstanceSetup: ------------------------------------------------------------
         

  2. Press `Control-C` to stop displaying the startup messages.




### Create a Windows user account

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click the instance name `crdhost` to open the **VM instance details** page.

  3. Under **Remote access** , click **Set Windows password** , and then click **Set** to create your account on the remote machine.

This step generates a password for you. Make a note of the username and password or copy it to a secure temporary file.




## Connect to the VM instance with Chrome Remote Desktop

You can connect to the VM instance using the Chrome Remote Desktop web application.

  1. On your local computer, go to the [Chrome Remote Desktop](https://remotedesktop.google.com/access) website.

  2. Click **Access my computer.**

  3. If you're not already signed in to Google, sign in with the same Google Account that you used to set up the Chrome Remote Desktop service.

You see your new VM instance `crdhost` in the **Remote Devices** list.

  4. Click the name of the remote desktop instance.

  5. When you're prompted, enter the PIN that you created earlier, and then click the arrow _arrow_forward_ button to connect.

You are now connected to the Windows login screen on your remote Compute Engine instance.

  6. If you are prompted, always allow the Remote Desktop application to read your clipboard and let you copy and paste between local and remote applications.

  7. Press any key, and enter the password for the Windows user that you generated earlier. Note that the default remote keyboard has a US-English layout, so the characters entered may not match the characters on your local keyboard. You also cannot copy and paste the password.




You are now connected and logged in to the remote Windows desktop.

## Improve the remote desktop experience

This section provides instructions for changing settings in order to improve the remote desktop experience.

### Install the Remote Desktop Chrome app

The Remote Desktop Chrome app gives a separate windowed experience and allows keyboard shortcuts that would normally be intercepted by Chrome to be used on the remote system.

If this app is not installed, do the following:

  1. Open the **Session Options** panel using the button _chevron_left_ that appears when you move the mouse to the side of the window.
  2. In the **Install App** section, click **Begin**.
  3. Click **Install**.



The remote desktop session reopens in its own application window.

You can move any remote desktop sessions from a Chrome tab to the app window by clicking the **Open With** _open_in_new_ icon in the address bar.

### Improve the screen resolution

The default remote desktop resolution can modified to better suit your local computers desktop resolution.

  1. Right-click the remote desktop's background and select **Display Settings**.
  2. In the **Resolution** drop-down list, select a different screen resolution.
  3. Confirm the new screen resolution in the dialog.



### Re-enable the service

If you have mistakenly disabled connections to the remote instance in the client app, you can reconfigure the service and re-enable it by following the instructions in Set up the Chrome Remote Desktop Service.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the Compute Engine instance

As an alternative to deleting the entire project, you can delete the VM instance you created for this tutorial:

  1. In the Google Cloud console, go to the [VM Instances](https://console.cloud.google.com/compute/instances) page:

[Go to the VM Instances page](https://console.cloud.google.com/compute/instances)

  2. Select the checkbox next to the instance name you created earlier (`crdhost`).

  3. Click the **Delete** button at the top of the page:

![Deleting the VM instance.](https://docs.cloud.google.com/static/architecture/images/chrome-desktop-remote-on-compute-engine-delete-crdhost-vm.png)

It takes a few moments to delete your instance.




### Deauthorize Chrome Remote Desktop for the instance

If you no longer want to connect to the VM instance, you can disable it and remove the instance from the **Remote Devices** list.

  1. On your local computer, go to the [Chrome Remote Desktop Remote Device list](https://remotedesktop.google.com/access) website.
  2. Click delete next to the instance name `crdhost`.
  3. Click **OK** to confirm that the remote device connection should be disabled.



## What's next

  * Learn how to set up [Chrome Remote Desktop on a Linux virtual machines](https://docs.cloud.google.com/architecture/chrome-desktop-remote-on-compute-engine).
  * Learn about other options for [creating a virtual workstation](https://docs.cloud.google.com/solutions/creating-a-virtual-workstation).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-12 UTC."],[],[]] 
