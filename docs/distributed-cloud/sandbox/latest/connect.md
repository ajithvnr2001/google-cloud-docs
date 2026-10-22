---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/connect/
title: Connect to your instance \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:10.982680+00:00
---

# Connect to your instance  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Connect to your instance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes methods for accessing the Google Distributed Cloud (GDC) Sandbox (GDC Sandbox) environment.

Your GDC Sandbox instance is a simulation of a Google Distributed Cloud air-gapped environment, hosted on Google Cloud. Like a real Google Distributed Cloud air-gapped environment, the services and virtual machines running in your GDC Sandbox instance are not connected directly to the internet. To interact with your instance, you must connect through your **GDC Sandbox gateway:** a virtual machine (VM) that has access to the internet as well as the services and VMs running in your GDC Sandbox instance.

The gateway is a Linux virtual machine, complete with GUI support, that takes the place of a machine on a private network with access to a real Google Distributed Cloud air-gapped environment. You can use it to:

  * Access the web-based management interface, the _GDC console_ , of your Google Distributed Cloud air-gapped environment
  * Manage and use your instance using browser-based or command line tools
  * Download software and resources from the internet to deploy workloads to the instance



The gateway is not meant to be a development machine; it is not provisioned with the required resources, and is non-persistent.

This page describes three options for accessing the web management interface of your instance.

  1. Use a remote desktop (RDP) client on your local Windows, macOS, or Linux machine to access the gateway GUI environment.
  2. Use a tool called **sshuttle** to create a secure VPN-like tunnel from your machine to the gateway, enabling you to use your own web browser and other locally installed tools to directly access resources in your instance.
  3. Create a Compute Engine VM, and use that as a client machine to connect to the gateway GUI environment, using one of the other two methods in this list.



The gateway VM comes pre-installed with a fixed set of user accounts, called **gateway accounts** , that you and your fellow users of your instance can use when connecting to the gateway. There are 25 of these accounts, with a fixed set of usernames, from `sandboxuser1` through `sandboxuser25`. These usernames cannot be changed, and new users cannot be created in the gateway VM. The main use of these accounts is for establishing a Remote Desktop connection to the gateway, and maintaining a separate desktop and shell environment for different users logged into the VM. There is no explicit connection between gateway accounts and the Google Cloud user accounts with access to the GDC Sandbox instance; nor is there an explicit connection between these accounts and the user accounts inside the GDC Sandbox environment itself, which will be covered later. If multiple users will be using your instance, we suggest creating a tracking spreadsheet, assigning each of your users to a gateway account.

If you access the environment through a remote desktop, choose an OS and the supported remote desktop client from the following options:

**OS name** | **OS version** | **Supported remote desktop client**  
---|---|---  
Windows | 11 | 

  * Microsoft Remote Desktop


  * IAP Desktop

  
Ubuntu  | 22.04 | Remmina, version 1.4.32  
Debian | 10 Rodete | Remmina, version 1.4.32  
macOS | Any version with Microsoft Remote Desktop support | Microsoft Remote Desktop, latest version  
  
## Before you begin

To begin the process of connecting to your instance, you will need the connection information included in your GDC Sandbox offer email, as described in [Get access](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/get-access). If you are not the primary administrator specified in that email, you must be added to the [Google Group used for access control](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/get-access#add-users).

Before you access the GDC Sandbox environment, ensure you complete the following based on your access method:

  * **Remote desktop access from your local machine** :

    1. [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
    2. [Initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize).
    3. [Authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate) using the same email that you used to register for GDC Sandbox.
    4. Set up the remote desktop client based on your OS: 
       * **Ubuntu 22.04** and **Debian 10 Rodete** : see [How to install Remmina](https://remmina.org/how-to-install-remmina/).
       * **Windows 11** : follow [Get started with the Remote Desktop app for Windows](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/windows).
       * **macOS** : follow [Get started with the macOS client](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac).
  * **Access through an`sshuttle` tunnel**:

**sshuttle** is a tool that lets you tunnel network traffic through an SSH connection, providing a VPN-like connection from your local machine to services running in your GDC Sandbox instance.

    1. [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
    2. [Initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize).
    3. [Authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate) using the same email that you used to register for GDC Sandbox.
    4. Install `sshuttle` based on your OS. See [How to install sshuttle](https://github.com/sshuttle/sshuttle?tab=readme-ov-file#obtaining-sshuttle)
  * **Access through a Compute Engine VM** :

**Important:** To access your environment through a Compute Engine connected VM, you must have a Google Cloud account.
    1. Start and set up [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).
    2. [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
    3. [Initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize).
    4. [Authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate) using the same email that you used to register for GDC Sandbox.



## Access the environment

To access your GDC Sandbox environment, complete the following sections based on your access method:

###  Linux 

  1. Ensure you've installed Remmina:
         
         sudo apt-get install remmina
         

**Chromebook users** : If you are using a Linux development environment, you must also install `freerdp2-x11`:
         
         sudo apt-get install freerdp2-x11
         

  2. Start the tunnel to your GDC Sandbox instance:
         
         gcloud compute start-iap-tunnel GDC_SANDBOX_INSTANCE_NAME 3389 --project=PROJECT_NAME \
         --zone=ZONE --local-host-port=localhost:PORT_NUMBER
         

Replace the following:

     * `GDC_SANDBOX_INSTANCE_NAME`: the name of your GDC Sandbox instance. You receive this name from the GDC Sandbox team.
     * `PORT_NUMBER`: a port number you define. For example, `8888`.
     * `PROJECT_NAME`: the name of your project.
     * `ZONE`: the zone in which your environment is. You receive the name of this zone from the GDC Sandbox team.
  3. From your local environment, open Remmina.

  4. click _add_box_ **New Connection Profile** in the upper left corner to begin the creation of a new profile.

  5. In the **Server** field, enter your URL in the format `localhost:PORT_NUMBER`.

  6. In the **Username** field, enter the name of one of the gateway accounts described in the introduction to this page. These follow the pattern from `sandboxuser1` through `sandboxuser20`.

  7. In the **Password** field, repeat the value you entered in the **Username** field. The `sandboxuser` gateway accounts are created with initial passwords that match their usernames.

  8. Navigate to the **Resolution** field and select **use client resolution**.

  9. Click **Save and Connect**.




You are now connected to a virtual desktop, running on your gateway. Perform the following steps inside the gateway environment:

  1. If this is your first time connecting to your gateway, change your password to a new password: 
     1. Open a terminal window.
     2. Type `passwd` and press **Enter**.
     3. Enter your current password if prompted.
     4. Enter your new password and confirm it by retyping it.
     5. The terminal window displays `Password updated successfully`.
  2. Download and extract the trust certificates

     1. Open a terminal window.
     2. Run command to download the trust bundle and split the certificates in the bundle.
            
            echo -n | curl https://console.org-1.zone1.google.gdch.test/.well-known/certificate-authority > trust_bundle.crt
                awk 'BEGIN {c=0;} /BEGIN CERT/{c++} { print > "cert." c ".crt"}' < trust_bundle.crt
            

     3. This command will create 4 certificate files, with names from `cert.0.crt` to `cert.3.crt`.

  3. Open the Chrome browser inside your gateway.

  4. Install the certificates into the Chrome browser (one time setup):

     1. Go to **Chrome > Settings > Privacy and security > Security**.
     2. Go to **Manage certificates**.
     3. Switch to the **Installed By You** tab.
     4. For each of the certificate files downloaded in the previous step, repeat the following steps: 
        1. click **Import** beside **Trusted Certificates**
        2. Locate the certificate and click **Select**.
     5. The certificates should now be added to the trust store.
  5. In the address bar, enter the URL `https://console.org-1.zone1.google.gdch.test` to access the GDC console for your GDC Sandbox instance.




###  Windows 

  1. Open a PowerShell window.
  2. Start the tunnel to your GDC Sandbox instance:
         
         gcloud compute start-iap-tunnel GDC_SANDBOX_INSTANCE_NAME 3389 --project=PROJECT_NAME \
         --zone=ZONE --local-host-port=localhost:PORT_NUMBER
         

Replace the following:

     * `GDC_SANDBOX_INSTANCE_NAME`: the name of your GDC Sandbox instance. You receive this name from the GDC Sandbox team.
     * `PORT_NUMBER`: a port number you define. For example, `8888`.
     * `PROJECT_NAME`: the name of your project.
     * `ZONE`: the zone in which your environment is. You receive the name of this zone from the GDC Sandbox team.
  3. From your local environment, open Microsoft Remote Desktop.

  4. In the **Computer** input field, enter the URL in the format `localhost:PORT_NUMBER`.

  5. Click **Connect**. If successful, a login dialog appears.

  6. In the **Username** field, enter the name of one of the gateway accounts described in the introduction to this page. These follow the pattern from `sandboxuser1` through `sandboxuser20`.

  7. In the **Password** field, repeat the value you entered in the **Username** field. The `sandboxuser` gateway accounts are created with initial passwords that match their usernames.

  8. Click **OK**.




You are now connected to a virtual desktop, running on your gateway. Perform the following steps inside the gateway environment:

  1. If this is your first time connecting to your gateway, change your password to a new password: 
     1. Open a terminal window.
     2. Type `passwd` and press **Enter**.
     3. Enter your current password if prompted.
     4. Enter your new password and confirm it by retyping it.
     5. The terminal window displays `Password updated successfully`.
  2. Download and extract the trust certificates

     1. Open a terminal window.
     2. Run command to download the trust bundle and split the certificates in the bundle.
    
    echo -n | curl https://console.org-1.zone1.google.gdch.test/.well-known/certificate-authority > trust_bundle.crt
        awk 'BEGIN {c=0;} /BEGIN CERT/{c++} { print > "cert." c ".crt"}' < trust_bundle.crt
    

     1. This command will create 4 certificate files, with names from `cert.0.crt` to `cert.3.crt`.
  3. Open the Chrome browser inside your gateway.

  4. Install the certificates into the Chrome browser (one time setup):

     1. Go to **Chrome > Settings > Privacy and security > Security**.
     2. Go to **Manage certificates**.
     3. Switch to the **Installed By You** tab.
     4. For each of the certificate files downloaded in the previous step, repeat the following, 
        1. click **Import** beside **Trusted Certificates**
        2. Locate the certificate and click **Select**.
     5. The certificates should now be added to the trust store.
  5. In the address bar, enter the URL `https://console.org-1.zone1.google.gdch.test` to access the GDC console for your GDC Sandbox instance.




###  macOS 

  1. Open a terminal window.
  2. Start the tunnel to your GDC Sandbox instance:
         
         gcloud compute start-iap-tunnel GDC_SANDBOX_INSTANCE_NAME 3389 --project=PROJECT_NAME \
         --zone=ZONE --local-host-port=localhost:PORT_NUMBER
         

Replace the following:

     * `GDC_SANDBOX_INSTANCE_NAME`: the name of your GDC Sandbox instance. You receive this name from the GDC Sandbox team.
     * `PORT_NUMBER`: a port number you define. For example, `8888`.
     * `PROJECT_NAME`: the name of your project.
     * `ZONE`: the zone in which your environment is. You receive the name of this zone from the GDC Sandbox team.
  3. Open Microsoft Remote Desktop.

  4. Click **Add PC**.

  5. In the **PC name** input field, enter a URL in the format `localhost:PORT_NUMBER`.

  6. Click **Add**. If successful, a login dialog appears.

  7. In the **Username** field, enter the name of one of the gateway accounts described in the introduction to this page. These follow the pattern from `sandboxuser1` through `sandboxuser20`.

  8. In the **Password** field, repeat the value you entered in the **Username** field. The `sandboxuser` gateway accounts are created with initial passwords that match their usernames.

  9. Click **OK**.




You are now connected to a virtual desktop, running on your gateway. Perform the following steps inside the gateway environment:

  1. If this is your first time connecting to your gateway, change your password to a new password: 
     1. Open a terminal window.
     2. Type `passwd` and press **Enter**.
     3. Enter your current password if prompted.
     4. Enter your new password and confirm it by retyping it.
     5. The terminal window displays `Password updated successfully`.
  2. Download and extract the trust certificates

     1. Open a terminal window.
     2. Run command to download the trust bundle and split the certificates in the bundle.
    
    echo -n | curl https://console.org-1.zone1.google.gdch.test/.well-known/certificate-authority > trust_bundle.crt
        awk 'BEGIN {c=0;} /BEGIN CERT/{c++} { print > "cert." c ".crt"}' < trust_bundle.crt
    

     1. This command will create 4 certificate files, with names from `cert.0.crt` to `cert.3.crt`.
  3. Open the Chrome browser inside your gateway.

  4. Install the certificates into the Chrome browser (one time setup):

     1. Go to **Chrome > Settings > Privacy and security > Security**.
     2. Go to **Manage certificates**.
     3. Switch to the **Installed By You** tab.
     4. For each of the certificate files downloaded in the previous step, repeat the following, 
        1. click **Import** beside **Trusted Certificates**
        2. Locate the certificate and click **Select**.
     5. The certificates should now be added to the trust store.
  5. In the address bar, enter the URL `https://console.org-1.zone1.google.gdch.test` to access the GDC console for your GDC Sandbox instance.




###  sshuttle 

To complete this process, you will need some values provided to you by the GDC Sandbox team when you signed up for the service:

  * `GDC_SANDBOX_INSTANCE_NAME`: the name of your GDC Sandbox instance.
  * `PROJECT_NAME`: the project hosting your instance.
  * `ZONE`: the zone containing your instance.



Perform the following steps to connect to your instance using `sshuttle`.

  1. Install the certificate (one time setup):

To use `sshuttle`, you must install a certificate. You only need to perform this once, on each machine you use to access the service.

     1. Download the certificate bundle and split it into four certificates with names from `cert.0.crt` to `cert.3.crt`.
    
    echo -n | curl https://console.org-1.zone1.google.gdch.test/.well-known/certificate-authority > trust_bundle.crt
    awk 'BEGIN {c=0;} /BEGIN CERT/{c++} { print > "cert." c ".crt"}' < trust_bundle.crt
    

  2. Add the CA certificate to the Linux Trust Store:

     1. Set a variable to hold the path of the CA certificate bundle (`trust_bundle.crt`) you downloaded:
            
            export CERT_PATH=LOCAL_FILE_PATH
            

     2. Add a line break if it does not exist for the certificate file and copy it to the `ca-certificates` directory:
            
            sed -i '$a\' ${CERT_PATH}
            sudo cp ${CERT_PATH} /usr/local/share/ca-certificates
            

     3. Add the certificate to the trust store:
            
            sudo update-ca-certificates
            

  3. Add the CA certificate to the gateway Chrome Trust Store:

     1. Go to **Chrome > Settings > Privacy and security > Security**.
     2. Go to **Manage certificates**.
     3. Switch to the **Installed By You** tab.
     4. For each of the certificate files downloaded in the previous step, repeat the following, 
        1. Click **Import** beside **Trusted Certificates**
        2. Locate the certificate and click **Select**.
     5. The certificates should now be added to the trust store.
  4. Open a terminal and run the command to start the tunnel to the GDC Sandbox instance:
         
         sshuttle -r GDC_SANDBOX_INSTANCE_NAME --no-latency-control \
         --ssh-cmd 'gcloud compute ssh --project PROJECT_NAME --zone ZONE --tunnel-through-iap' \
         10.200.0.0/16 --dns
         

Replace the following with the values provided to you by the GDC Sandbox team:

     * `GDC_SANDBOX_INSTANCE_NAME`: the name of your GDC Sandbox instance.
     * `PROJECT_NAME`: the name of your project.
     * `ZONE`: the zone containing your GDC Sandbox environment. You receive the name of this zone from the GDC Sandbox team.

While this command is running, all network requests to `10.200.0.0/16` from your local machine are routed to your GDC Sandbox instance, through a secure tunnel.

  5. Open the Chrome browser.

  6. In the address bar, enter the URL `https://console.org-1.zone1.google.gdch.test` to access the GDC console for your GDC Sandbox instance. While `sshuttle` is running, this URL will be directed through the gateway to your GDC Sandbox environment.

  7. You can proceed with the sign-in instructions in the next section. When you are finished working with your instance, enter `Ctrl+C` in the terminal where the `sshuttle` command is running, to terminate the `sshuttle` process.




###  Compute Engine VM 

To access the GDC Sandbox environment in a Compute Engine VM, you create the VM with a startup script and use the Chrome Remote Desktop. To create the VM and access the environment, do the following:

  1. Open a Cloud Shell terminal.
  2. View a list of available images:
         
         gcloud compute images list
         

Note the Debian-10 image and the project name where the image resides.

  3. Create a text file. For example, `startup-script.txt`.

  4. In the file, add in the following startup script:
         
         sudo apt-get upgrade
         curl https://dl.google.com/linux/linux_signing_key.pub \
             | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/chrome-remote-desktop.gpg
         echo "deb [arch=amd64] https://dl.google.com/linux/chrome-remote-desktop/deb stable main" \
             | sudo tee /etc/apt/sources.list.d/chrome-remote-desktop.list
         sudo apt-get update
         sudo DEBIAN_FRONTEND=noninteractive \
             apt-get install --assume-yes chrome-remote-desktop
         sudo DEBIAN_FRONTEND=noninteractive \
             apt install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver
         sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session'
         sudo systemctl disable lightdm.service
         sudo apt install --assume-yes task-xfce-desktop
         curl -L -o google-chrome-stable_current_amd64.deb \
         https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
         sudo apt install --assume-yes --fix-broken ./google-chrome-stable_current_amd64.deb
         sudo apt install --assume-yes remmina
         

  5. Create a Compute Engine VM:
         
         gcloud compute instances create VM_NAME \
         --image-project=PROJECT_NAME \
         --image-family=debian-10 \
         --metadata=startup-script-from-file=SCRIPT_FILENAME
         

Replace the following:

     * `VM_NAME`: the name you give to the VM. For example, test-vm.
     * `PROJECT_NAME`: the name of the project that contains the image.
     * `SCRIPT_FILENAME`: the name of the file that contains the startup script. For example, `startup-script.txt`.
  6. Install Chrome Remote Desktop by following [Install Chrome Remote Desktop on the VM instance](https://docs.cloud.google.com/architecture/chrome-desktop-remote-on-compute-engine#install_chrome_remote_desktop_on_the_vm_instance).

  7. Activate Chrome Remote Desktop by following [Connect to the VM instance](https://docs.cloud.google.com/architecture/chrome-desktop-remote-on-compute-engine#connect_to_the_vm_instance).




After you have connected to your Compute Engine VM, you can choose either of the following options to connect to your instance:

  * follow the instructions on the **Linux** tab to connect to your gateway desktop GUI using Remmina, or
  * follow the instructions on the **sshuttle** tab to create a tunnel from your Compute Engine VM to your gateway, and use the browser and terminal in your VM to connect to your GDC Sandbox instance.



## Sign in to the GDC console

  1. After you visit `https://console.org-1.zone1.google.gdch.test/`, A **Sign in** page for the GDC console appears.
  2. Click **Continue with fake-oidc-provider**. A **Fake OIDC Provider** page appears.
  3. In the **Select a user** list, click **Platform Admin**.

**Note:** The Cluster Admin and Infrastructure Operator roles are not used in GDC Sandbox and don't work. Later pages will describe how to add additional users.
  4. Click **Submit**.




You are now signed into the GDC console. Follow the steps in [Create a project](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/create-project) to set up the administrator account and your first project.

## Tips

If you encounter any browser issues, close the browser window, reopen a new browser page and enter `https://console.org-1.zone1.google.gdch.test/` into the address bar.

### Add the sign-in page as the home page in your browser (optional)

For convenience, you can configure the GDC console as the home address in your browser. This is especially useful if you are using a remote desktop to access the GUI running on the gateway.

  1. In the address bar, enter `https://console.org-1.zone1.google.gdch.test/`. A **Sign in** page appears.

  2. To add this page to your browser home button, select **Browser**.

  3. In the Chrome menu, select more_vert **Customize and control Google Chrome** .

  4. Select **username** > **Customize Your Chrome**.

  5. In the navigation menu, select **Appearance**.

  6. Click the **Show home button** toggle to **On** and enter the `https://console.org-1.zone1.google.gdch.test/` URL.

  7. In the navigation menu, select **On startup**.

  8. Select **Open a specific page or set of pages** and enter the Site URL of `https://console.org-1.zone1.google.gdch.test/`. Click **Add**.




The GDC Sandbox user interface opens every time you open your browser or click the Home button.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
