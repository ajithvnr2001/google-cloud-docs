---
url: https://docs.cloud.google.com/architecture/chrome-desktop-remote-on-compute-engine/
title: Set up Chrome Remote Desktop for Linux on Compute Engine \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:49.081057+00:00
---

# Set up Chrome Remote Desktop for Linux on Compute Engine  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/chrome-desktop-remote-on-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Set up Chrome Remote Desktop for Linux on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-12 UTC

This tutorial shows you how to set up the [Chrome Remote Desktop](https://support.google.com/chrome/answer/1649523) service on a Debian Linux virtual machine (VM) instance on Compute Engine. For separate instructions for Windows VMs, see [Windows virtual machines](https://docs.cloud.google.com/architecture/chrome-desktop-remote-windows-compute-engine). Chrome Remote Desktop lets you remotely access applications with a graphical user interface from a local computer or mobile device.

When following this tutorial, the default firewall rules allow Chrome Remote Desktop connections; you don't need to configure any additional firewall rules. SSH access is required only for the initial setup.

The VM does need access to the internet (either with an external IP address or through [Cloud NAT](https://docs.cloud.google.com/nat)), and you use your Google Account for authentication and authorization.

**Note:** This solution is not suitable for graphically intensive applications, including playing videos, because those typically require hardware graphics acceleration as well as a network that has high bandwidth and low latency. If you want to run graphically intense applications remotely, see the [Creating a virtual GPU-accelerated Linux workstation](https://docs.cloud.google.com/solutions/creating-a-virtual-gpu-accelerated-linux-workstation) tutorial for an alternative solution.

This tutorial assumes that you are familiar with the Linux command line and with installing Debian packages.

For information about other options for creating virtual workstations, see [Creating a virtual workstation](https://docs.cloud.google.com/solutions/creating-a-virtual-workstation).

## Objectives

  * Create a [headless](https://wikipedia.org/wiki/Headless_computer) Compute Engine VM instance to run Chrome Remote Desktop on.
  * Install and configure the Chrome Remote Desktop service on the VM instance.
  * Set up an X Window System desktop environment in the VM instance.
  * Connect from your local computer to the desktop environment on the VM instance.



## Costs

This tutorial uses billable components of Google Cloud, including:

  * Compute Engine



Use the [Pricing Calculator](https://cloud.google.com/products/calculator/#id=01bf79df-c7d0-4c3a-afd6-cbb4754d938f) to generate a cost estimate based on your projected usage.

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



## Create a Compute Engine instance

For the purposes of this tutorial, the default machine type with a Debian Linux boot disk is used. If you are using this for your own environment, you may want to adjust the machine type, name, [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones), boot disk size, or other settings.

  1. In the Google Cloud console, go to the **VM Instances** page.

[Go to VM Instances](https://console.cloud.google.com/compute/instances/)

  2. Click **Create**.

  3. Set the instance name to `crdhost`.

  4. Click **Create**.

It takes a few moments to create your instance.

  5. After the instance has been created, connect to your new instance by clicking **SSH** in the instance list:

![Creating an SSH connection to the VM instance.](https://docs.cloud.google.com/static/architecture/images/chrome-desktop-remote-on-compute-engine-crdhost-ssh.png)




## Install Chrome Remote Desktop on the VM instance

  1. In the SSH window for your VM instance, add the Debian Linux Chrome Remote Desktop repository to your `apt` package list, and install the `chrome-remote-desktop` package.
         
         curl https://dl.google.com/linux/linux_signing_key.pub \
             | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/chrome-remote-desktop.gpg
         echo "deb [arch=amd64] https://dl.google.com/linux/chrome-remote-desktop/deb stable main" \
             | sudo tee /etc/apt/sources.list.d/chrome-remote-desktop.list
         sudo apt-get update
         sudo DEBIAN_FRONTEND=noninteractive \
             apt-get install --assume-yes chrome-remote-desktop
         

The `DEBIAN_FRONTEND=noninteractive` parameter suppresses a prompt to configure a layout for a keyboard that would be directly connected to the VM instance.




## Install an X Windows System desktop environment

You need to install an X Window System desktop environment and window manager for Chrome Remote Desktop to use. Common options are:

  * [Xfce](https://www.xfce.org/)
  * [Cinnamon](https://www.linuxmint.com/)
  * [Gnome](https://www.gnome.org/)
  * [Gnome-Classic](https://help.gnome.org/users/gnome-help/stable/gnome-classic.html.en)
  * [KDE Plasma](https://kde.org/)



You can use other desktop environments, but Chrome Remote Desktop does not support 3D graphics acceleration. If you do choose a desktop environment that uses 3D graphics acceleration, you need to disable that feature, or the remote desktop service won't start.

For remote connections over slower networks we recommended Xfce because it has minimal graphical elements and few animations.

### Xfce

  1. In the SSH window connected to your VM instance, install the Xfce desktop environment and basic desktop components:
         
         sudo DEBIAN_FRONTEND=noninteractive \
             apt install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver
         

[XScreenSaver](https://www.jwz.org/xscreensaver/) is required because the Xfce default screen locker (Light Locker) doesn't work with Chrome Remote Desktop (Light Locker displays a blank screen that cannot be unlocked).

**Note:** You might see a `Permission Denied` error for the `update-initramfs` process during installation. This is normal, and you can ignore the error.
  2. Configure Chrome Remote Desktop to use Xfce by default:
         
         sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > /etc/chrome-remote-desktop-session'
         

  3. Because there is no display connected to your instance, disable the display manager service on your instance:
         
         sudo systemctl disable lightdm.service
         

  4. Optional: Install the full suite of Linux desktop applications along with the Xfce desktop environment:
         
         sudo apt install --assume-yes task-xfce-desktop
         

  5. Optional: Install the Chrome browser on your instance:
         
         curl -L -o google-chrome-stable_current_amd64.deb \
         https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
         sudo apt install --assume-yes --fix-broken ./google-chrome-stable_current_amd64.deb
         




### Cinnamon

  1. In the SSH window connected to your VM instance, install the Cinnamon desktop environment and basic desktop components:
         
         sudo DEBIAN_FRONTEND=noninteractive \
             apt install --assume-yes cinnamon-core desktop-base dbus-x11
         

**Note:** You might see a `Permission Denied` error for the `update-initramfs` process during the installation process. This is normal and you can ignore the error.
  2. Set your Chrome Remote Desktop session to use Cinnamon in 2D mode (which does not use 3D graphics acceleration) by default:
         
         sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/cinnamon-session-cinnamon2d" > /etc/chrome-remote-desktop-session'
         

  3. Optional: Install the full suite of Linux desktop applications along with the Cinnamon desktop environment:
         
         sudo apt install --assume-yes task-cinnamon-desktop
         

  4. Optional: Install the Chrome browser on your instance:
         
         curl -L -o google-chrome-stable_current_amd64.deb \
         https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
         sudo apt install --assume-yes --fix-broken ./google-chrome-stable_current_amd64.deb
         




### Gnome

  1. In the SSH window connected to your VM instance, install the full Gnome desktop environment:
         
         sudo DEBIAN_FRONTEND=noninteractive \
             apt install --assume-yes  task-gnome-desktop
         

**Note:** You might see a `Permission Denied` error for the `update-initramfs` process during the installation process. This is normal and you can ignore the error.
  2. Set your Chrome Remote Desktop session to use Gnome
         
         sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/gnome-session" > /etc/chrome-remote-desktop-session'
         

  3. Disable the Gnome display manager service on your instance, because it conflicts with the Chrome Remote Desktop service.
         
         sudo systemctl disable gdm3.service
         sudo reboot
         

This command reboots the VM.

  4. Reconnect through SSH before continuing.

  5. Optional: Install the Chrome browser on your instance:
         
         curl -L -o google-chrome-stable_current_amd64.deb \
         https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
         sudo apt install --assume-yes --fix-broken ./google-chrome-stable_current_amd64.deb
         




### Gnome-Classic

  1. In the SSH window connected to your VM instance, install the full Gnome desktop environment:
         
         sudo DEBIAN_FRONTEND=noninteractive \
             apt install --assume-yes  task-gnome-desktop
         

The `DEBIAN_FRONTEND=noninteractive` parameter suppresses a prompt to configure a layout for a keyboard that would be directly connected to the VM instance.

**Note:** You might see a `Permission Denied` error for the `update-initramfs` process during the installation process. This is normal and you can ignore the error.
  2. Set your Chrome Remote Desktop session to use the Gnome-Classic desktop:
         
         sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/gnome-session-classic" > /etc/chrome-remote-desktop-session'
         

  3. Disable the Gnome display manager service on your instance, because it conflicts with the Chrome Remote Desktop service.
         
         sudo systemctl disable gdm3.service
         sudo reboot
         

This command reboots the VM.

  4. Reconnect through SSH before continuing.

  5. Optional: Install the Chrome browser on your instance:
         
         curl -L -o google-chrome-stable_current_amd64.deb \
         https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
         sudo apt install --assume-yes --fix-broken ./google-chrome-stable_current_amd64.deb
         




### KDE Plasma

  1. In the SSH window connected to your VM instance, install the full KDE Plasma desktop environment:
         
         sudo DEBIAN_FRONTEND=noninteractive \
             apt install --assume-yes  task-kde-desktop
         

The `DEBIAN_FRONTEND=noninteractive` parameter suppresses a prompt to configure a layout for a keyboard that would be directly connected to the VM instance.

**Note:** You might see a `Permission Denied` error for the `update-initramfs` process during the installation process. This is normal and you can ignore the error.
  2. Set your Chrome Remote Desktop session to use KDE Plasma
         
         sudo bash -c 'echo "exec /etc/X11/Xsession /usr/bin/startplasma-x11" > /etc/chrome-remote-desktop-session'
         

  3. Optional: Install the Chrome browser on your instance:
         
         curl -L -o google-chrome-stable_current_amd64.deb \
         https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
         sudo apt install --assume-yes --fix-broken ./google-chrome-stable_current_amd64.deb
         




## Configure and start the Chrome Remote Desktop service

To start the remote desktop server, you need to have an authorization key for the Google Account that you want to use to connect to it:

  1. In the Google Cloud console, go to the **VM Instances** page:

[Go to the VM Instances page](https://console.cloud.google.com/compute/instances/)

  2. Connect to your instance by clicking the **SSH** button.

  3. On your local computer, using the Chrome browser, go to the Chrome Remote Desktop command line setup page:

<https://remotedesktop.google.com/headless>

  4. If you're not already signed in, sign in with a Google Account. This is the account that will be used for authorizing remote access.

  5. On the **Set up another computer** page, click **Begin**.

  6. Click **Authorize**.

You need to allow Chrome Remote Desktop to access your account. If you approve, the page displays a command line for Debian Linux that looks like the following:
         
         DISPLAY= /opt/google/chrome-remote-desktop/start-host \
             --code="4/xxxxxxxxxxxxxxxxxxxxxxxx" \
             --redirect-url="https://remotedesktop.google.com/_/oauthredirect" \
             --name=$(hostname)
         

You use this command to set up and start the Chrome Remote Desktop service on your VM instance, linking it with your Google Account using the authorization code.

**Note:** The authorization code in the command line is valid for only a few minutes, and you can use it only once.
  7. Copy the command to the SSH window that's connected to your instance, and then run the command.

  8. When you're prompted, enter a 6-digit PIN. This number will be used for additional authorization when you connect later.

You might see errors like `No net_fetcher` or `Failed to read`. You can ignore these errors.

  9. Verify that the service is running using the following command.
         
         sudo systemctl status chrome-remote-desktop@$USER
         

If the service is running, you see output that includes the state `active`:
         
         chrome-remote-desktop.service - LSB: Chrome Remote Desktop service
             Loaded: loaded (/lib/systemd/system/chrome-remote-desktop@USER.service; enabled; vendor preset: enabled)
             Active: **active (running)** since DATE_TIME; ELAPSED_TIME
         




## Connect to the VM instance

You can connect to the VM instance using the Chrome Remote Desktop web application.

  1. On your local computer, go to the [Chrome Remote Desktop](https://remotedesktop.google.com) website.

  2. Click **Access my computer.**

  3. If you're not already signed in to Google, sign in with the same Google Account that you used to set up the Chrome Remote Desktop service.

You see your new VM instance `crdhost` in the **Remote Devices** list.

  4. Click the name of the remote desktop instance.

  5. When you're prompted, enter the PIN that you created earlier, and then click the arrow button to connect.

You are now connected to the desktop environment on your remote Compute Engine instance.

  6. If you are prompted, always allow the Remote Desktop application to read your clipboard and let you copy and paste between local and remote applications.

  7. If you installed the Xfce desktop, the first time you connect, you are prompted to set up the desktop panels. Click **Use Default Config** to get the standard taskbar at the top and the quick launch panel at the bottom.




![xfce desktop showing the taskbar and quick launch panel.](https://docs.cloud.google.com/static/architecture/images/chrome-desktop-remote-on-compute-engine-xfce-desktop.png)

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

### Disable animations and effects in Cinnamon

The Cinnamon desktop uses several graphical features and animations, such as semi-transparent windows and menus that fade in and out. Because these animations take more time to render over a remote connection, it can make the user interface feel slow.

To disable these effects:

  1. In the Cinnamon desktop, select **Menu** > **Preferences** > **Effects**.

![Setting desktop preferences in Cinnamon.](https://docs.cloud.google.com/static/architecture/images/chrome-desktop-remote-on-compute-engine-cinnamon-desktop-menu-preferences-effects.png)

  2. Disable each of the effects:

![Disabling animation effects in Cinnamon.](https://docs.cloud.google.com/static/architecture/images/chrome-desktop-remote-on-compute-engine-cinnamon-effects.png)




### Set a user password

The user account created by Compute Engine doesn't have a password. However, several desktop environments require one for unlocking screensavers and authorizing administrative actions. It is therefore important to set a password for your user:

  1. Connect to the instance using SSH, as you did when you first set up the instance.
  2. Create a password for the user:
         
         sudo passwd $(whoami)
         




### Disable screensavers and lock screens

Because you're accessing your desktop from a remote computer, it's normally not necessary to use a screensaver or screen locker, so you can disable these.

### Xfce

  1. In the **Applications** menu, select **Settings** > **Screensaver**.
  2. Set **Mode** to **Disable Screen Saver**.



### Cinnamon

  1. In the desktop, select **Menu** > **Preferences** > **Screensaver**.
  2. In the **Settings** tab, set **Delay** to **Never** and disable the following two Lock settings to lock the screen automatically.



### Gnome

  1. In the desktop, click **Activities** and type `Settings`.
  2. Select the **Settings** application.
  3. In the **Settings** application, select **Privacy** > **Screen Lock**.
  4. Disable **Automatic Screen Lock** and close the dialog.
  5. Select **Devices** > **Keyboard**.
  6. In the list of keyboard shortcuts, go to the **System** section, and then click **Lock Screen**.
  7. Press the `Backspace` key to disable the shortcut, and then click **Set**.
  8. Select **Power** and set **Blank Screen** to **Never**.



### Gnome-Classic

  1. In the desktop, select **Applications** > **System Tools** > **Settings**.
  2. In the **Settings** application, select **Privacy** > **Screen Lock**.
  3. Disable **Automatic Screen Lock** and close the dialog.
  4. Select **Devices** > **Keyboard**.
  5. In the list of keyboard shortcuts, go to the **System** section and click **Lock Screen**.
  6. Press the `Backspace` key to disable the shortcut, and then click **Set**.
  7. Select **Power** and set **Blank Screen** to **Never**.



### KDE Plasma

  1. In the desktop, click the KDE menu button, and then type `Screen Locking`.
  2. Select the **Screen Locking** application.
  3. In the **Configure Screen Locking** application, disable **Lock Screen Automatically after** and click the backspace button to clear the keyboard shortcut.
  4. Click **OK**.



### Increase the desktop resolution

If you have an ultra high-resolution monitor, you might find that the default maximum remote desktop size of 1600 x 1200 is too small. If so, you can increase it to the resolution of your monitor.

  1. Use SSH to connect to the instance.
  2. Set the `CHROME_REMOTE_DESKTOP_DEFAULT_DESKTOP_SIZES` environment variable to include the resolution of your monitor:
         
         echo "export CHROME_REMOTE_DESKTOP_DEFAULT_DESKTOP_SIZES=1600x1200,3840x2560" \
             >> ~/.profile
         

  3. Restart the service:
         
         sudo systemctl restart chrome-remote-desktop@$USER
         




### Enable advanced video codec:

The AV1 codec with High Quality color gives improved picture quality and allows better encoding of pure color information (such as text):

  1. Open the **Session Options** panel using the button _chevron_left_ that appears when you move the mouse to the side of the window.
  2. In the **Video Codec** field, select **AV1**
  3. Ensure that **High-quality color** field is enabled.



### Choose a different desktop environment

In the preceding section, you set a default desktop environment in the global `/etc/chrome-remote-desktop-session` configuration file. You can also choose a different desktop environment (if it's installed) by specifying it in the `.chrome-remote-desktop-session` configuration file in your home directory:

### Xfce
    
    
    echo "exec /etc/X11/Xsession /usr/bin/xfce4-session" > ~/.chrome-remote-desktop-session
    

### Cinnamon
    
    
    echo "exec /etc/X11/Xsession /usr/bin/cinnamon-session-cinnamon2d" > ~/.chrome-remote-desktop-session
    

### Gnome
    
    
    echo "exec /etc/X11/Xsession /usr/bin/gnome-session" > ~/.chrome-remote-desktop-session
    

### Gnome-Classic
    
    
    echo "exec /etc/X11/Xsession /usr/bin/gnome-session-classic" > ~/.chrome-remote-desktop-session
    

### KDE Plasma
    
    
    echo "exec /etc/X11/Xsession /usr/bin/startplasma-x11" > ~/.chrome-remote-desktop-session
    

After you make this change, restart the service so the change takes effect:
    
    
    sudo systemctl restart chrome-remote-desktop@$USER
    

As mentioned before, Chrome Remote Desktop does not support 3D graphics acceleration. Therefore, for any desktop environments that uses these features, you need disable 3D graphics, or the session won't start.

## Automate the installation process

When you need to set up multiple machines with Chrome Remote Desktop, the manual installation steps can become repetitive. You can use a [custom startup script](https://docs.cloud.google.com/compute/docs/startupscript) to automate this process, using the following procedure.

For the purposes of this tutorial, the default machine type with a Debian Linux boot disk is used. If you are using this for your own environment, you may want to adjust the machine type, name, region, boot disk size, or other settings.

  1. In the Google Cloud console, go to the **VM Instances** page:

[Go to the VM Instances page](https://console.cloud.google.com/compute/instances/)

  2. Click **Create Instance**.

  3. Set the instance name to `crdhost-autoinstall`.

  4. Scroll to, and expand the **Advanced Options** section.

  5. Expand the **Management** section.

  6. Copy the following shell script and paste it into the **Automation/Startup Script** field:
         
         #!/bin/bash -x
         #
         # Startup script to install Chrome remote desktop and a desktop environment.
         #
         # See environmental variables at then end of the script for configuration
         #
         
         function install_desktop_env {
           PACKAGES="desktop-base xscreensaver dbus-x11"
         
           if [[ "$INSTALL_XFCE" != "yes" && "$INSTALL_CINNAMON" != "yes" ]] ; then
             # neither XFCE nor cinnamon specified; install both
             INSTALL_XFCE=yes
             INSTALL_CINNAMON=yes
           fi
         
           if [[ "$INSTALL_XFCE" = "yes" ]] ; then
             PACKAGES="$PACKAGES xfce4"
             echo "exec xfce4-session" > /etc/chrome-remote-desktop-session
             [[ "$INSTALL_FULL_DESKTOP" = "yes" ]] && \
               PACKAGES="$PACKAGES task-xfce-desktop"
           fi
         
           if [[ "$INSTALL_CINNAMON" = "yes" ]] ; then
             PACKAGES="$PACKAGES cinnamon-core"
             echo "exec cinnamon-session-cinnamon2d" > /etc/chrome-remote-desktop-session
             [[ "$INSTALL_FULL_DESKTOP" = "yes" ]] && \
               PACKAGES="$PACKAGES task-cinnamon-desktop"
           fi
         
           DEBIAN_FRONTEND=noninteractive \
             apt-get install --assume-yes $PACKAGES $EXTRA_PACKAGES
         
           systemctl disable lightdm.service
         }
         
         function download_and_install { # args URL FILENAME
           if [[ -e "$2" ]] ; then
              echo "cannot download $1 to $2 - file exists"
              return 1;
           fi
           curl -L -o "$2" "$1" && \
             apt-get install --assume-yes --fix-broken "$2" && \
             rm "$2"
         }
         
         function is_installed {  # args PACKAGE_NAME
           dpkg-query --list "$1" | grep -q "^ii" 2>/dev/null
           return $?
         }
         
         # Configure the following environmental variables as required:
         INSTALL_XFCE=yes
         INSTALL_CINNAMON=yes
         INSTALL_CHROME=yes
         INSTALL_FULL_DESKTOP=yes
         
         # Any additional packages that should be installed on startup can be added here
         EXTRA_PACKAGES="less bzip2 zip unzip tasksel wget"
         
         apt-get update
         
         if ! is_installed chrome-remote-desktop; then
             if [[ ! -e /etc/apt/sources.list.d/chrome-remote-desktop.list ]]; then
                 echo "deb [arch=amd64] https://dl.google.com/linux/chrome-remote-desktop/deb stable main" \
                     | tee -a /etc/apt/sources.list.d/chrome-remote-desktop.list
             fi
             apt-get update
             DEBIAN_FRONTEND=noninteractive \
                 apt-get install --assume-yes chrome-remote-desktop
         fi
         
         install_desktop_env
         
         [[ "$INSTALL_CHROME" = "yes" ]] && ! is_installed google-chrome-stable && \
           download_and_install \
             https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
             /tmp/google-chrome-stable_current_amd64.deb
         
         echo "Chrome remote desktop installation completed"
         

This script performs the following tasks each time the machine is rebooted:

     * If the remote desktop package is not installed: 
       * Adds the Chrome Remote Desktop Debian package repository
       * Installs the Chrome Remote Desktop package and dependencies.
     * Installs the Xfce or Cinnamon desktop environments (depending on the script settings).
     * If the full desktop environment option is enabled, installs the necessary packages.
     * If the Google Chrome browser option is enabled and is not installed: 
       * Downloads Google Chrome package.
       * Installs Google Chrome and its dependent packages.
**Note:** You can choose which packages to install by using the variables defined near the end of the script.
  7. Click **Create**.

It takes a few moments to create your instance, and on first run with all the options enabled, the script can take up to 10 minutes to complete the installation.

  8. To monitor progress, connect to the VM instance using SSH, and in the terminal of the instance, run the following command:
         
         sudo journalctl -o cat -f _SYSTEMD_UNIT=google-startup-scripts.service
         

This command shows the output from the startup script. When the script has finished, you see the following:
         
         INFO startup-script: Chrome remote desktop installation completed
         INFO startup-script: Return code 0.
         INFO Finished running startup scripts.
         




This script only installs the required packages; you still need to configure the Remote Desktop Service for your user, as described previously.

There are various ways to specify a startup script when creating a new VM instance:

  * Pasting it into the Google Cloud console (as shown earlier).
  * Storing it as a file on a local machine, and using the `--metadata-from-file` flag when you create the instance using the Google Cloud CLI.
  * Storing it in a Cloud Storage bucket and specifying the URL to the object—either in the console or in the gcloud CLI.



For more information on the alternative methods of how to configure the startup script, see [Running Startup scripts](https://docs.cloud.google.com/compute/docs/startupscript) in the Compute Engine documentation.

## Troubleshooting

This section provides troubleshooting advice for this guide.

### Check the status of the Chrome Remote Desktop service

If at any point the Chrome Remote Desktop service is not responding, you can check its status by using SSH to connect to the instance and running the following command:
    
    
    sudo systemctl status chrome-remote-desktop@$USER
    

If the service is running, you see output that includes the state `active`:
    
    
    chrome-remote-desktop.service - LSB: Chrome Remote Desktop service
        Loaded: loaded (/lib/systemd/system/chrome-remote-desktop@USER.service; enabled; vendor preset: enabled)
        Active: **active (running)** since DATE_TIME; ELAPSED_TIME
    

To restart the service, use the following command in the SSH window:
    
    
    sudo systemctl restart chrome-remote-desktop@$USER
    

### Get log and error information

Chrome Remote Desktop writes log information to the system journal:
    
    
    journalctl SYSLOG_IDENTIFIER=chrome-remote-desktop     # All logs
    journalctl SYSLOG_IDENTIFIER=chrome-remote-desktop -e  # Most recent logs
    journalctl SYSLOG_IDENTIFIER=chrome-remote-desktop -b  # Logs since reboot
    

You can check these log files for error messages.

### Re-enable the service

If you have mistakenly disabled connections to the remote instance in the client app, you can reconfigure the service and re-enable it by following the instructions in Configure and start the Chrome Remote Desktop service.

### Check the global and user-specific session configuration files.

Check the contents of the global `/etc/chrome-remote-desktop-session` configuration file and the user-specific `~/.chrome-remote-desktop-session` configuration file and confirm that the specified desktop environments are installed.

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

  * Learn how to set up [Chrome Remote Desktop on a Windows virtual machines](https://docs.cloud.google.com/architecture/chrome-desktop-remote-windows-compute-engine).
  * Learn about other options for [creating a virtual workstation](https://docs.cloud.google.com/solutions/creating-a-virtual-workstation).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-12 UTC."],[],[]] 
