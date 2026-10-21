---
url: https://docs.cloud.google.com/compute/docs/images/install-guest-environment/
title: Install the guest environment \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:59:36.463891+00:00
---

# Install the guest environment  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/install-guest-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Install the guest environment Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This page explains how to manually install the guest environment on virtual machine (VM) instances. The guest environment is a collection of scripts, daemons, and binaries that instances require to run on Compute Engine. For more information, see [Guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment).

In most cases, if you use Google-provided public OS images, the guest environment is automatically included. For a full list of OS images that automatically include the guest environment, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#user-space-features).

If the guest environment is not installed or is outdated, install or update it. To identify these scenarios, see When to install or update the guest environment.

## Before you begin

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




## When to install or update the guest environment

In most cases, you don't need to manually install or update the guest environment. Review the following sections to see when you might need to manually install or update.

### Check installation requirements

Before you install the guest environment, use the Validate the guest environment procedure to check if the guest environment runs on your instance. If the guest environment is available on your instance but is outdated, update the guest environment.

You might need to install the guest environment in the following situations:

  * Your required Google-provided OS image does not have the guest environment installed.

  * You [import](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) a custom image or a virtual disk to Compute Engine and choose to prevent automatic installation of the guest environment.

When you import virtual disks or custom images, you can let Compute Engine install the guest environment for you. However, if you choose not to install the guest environment during the import process, then you must manually install the guest environment.

  * You [migrate VMs to Compute Engine using Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines/docs).




To install the guest environment, see Installation methods.

### Check update requirements

You might need to update the guest environment in the following situations:

  * You have instances that use OS images earlier than `v20141218`.

  * You use an OS image that does not have the [guest environment optimizations for Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/optimizing-local-ssd-performance#use-guest-env-optimizations).




To update the guest environment, see Update the guest environment.

## Installation methods

You can install the guest environment in multiple ways. Choose one of the following options:

  * **Import tool**. The import tool is the recommended option. However, the import tool installs the guest environment and also performs other configuration updates on the image, such as configuring networks, configuring the bootloader, and installing Google Cloud CLI. For instructions, see [Make an image bootable](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks#making_an_image_bootable).

The import tool supports a wide variety of operating systems and versions. For more information, see [operating system details page](https://docs.cloud.google.com/compute/docs/images/os-details#import).

  * **Manual installation**. Choose one of the following:

    * Connect to your instance using SSH or RDP and install the guest environment in-place
    * Clone your boot disk and install the guest environment using a startup script



## Supported operating systems

You can install or update the guest environment on VMs that use OS image versions in the general availability (GA) lifecycle or [extended support lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#extended-support).

To review a list of OS image versions and their lifecycle stage on Compute Engine, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#general-info).

## Limitations

You can't manually install or use the import tool to install guest environments for Fedora CoreOS and Container-optimized (COS) operating systems. For COS, Google recommends using the [Google-provided public images](https://docs.cloud.google.com/compute/docs/images/os-details#user-space-features), which include the guest environment as a core component.

## Install the guest environment

To manually install the guest environment, select one of the following methods, depending on your ability to connect to the instance:

  * If you can connect to the instance by using SSH or RDP, install the guest environment in-place.
  * If you can't connect to the instance, install the guest environment by cloning its boot disk and using a startup script.



### Install the guest environment in-place

Use this method to install the guest environment if you can connect to the target instance using SSH. If you can't connect to the instance to install the guest environment, you can instead install the guest environment by cloning its boot disk and using a startup script.

This procedure is useful for imported images if you can connect using SSH password-based authentication. You can also use it to reinstall the guest environment if you have at least one user account with a functional key-based SSH.

###  CentOS/RHEL/Rocky 

Complete the steps for your CentOS/RHEL/Rocky version.

###  Version 10 and later 

  1. Verify that your operating system version is supported.
  2. Determine your CentOS/RHEL/Rocky version. Then, create the source repository file, `/etc/yum.repos.d/google-cloud.repo`:
         
         eval $(grep VERSION_ID /etc/os-release)
         sudo tee /etc/yum.repos.d/google-cloud.repo << EOM
         [google-compute-engine]
         name=Google Compute Engine
         baseurl=https://packages.cloud.google.com/yum/repos/google-compute-engine-el${VERSION_ID%%.*}-x86_64-stable
         enabled=1
         gpgcheck=1
         repo_gpgcheck=0
         gpgkey=https://packages.cloud.google.com/yum/doc/rpm-package-key-v${VERSION_ID%%.*}.gpg
         EOM
         

  3. Update package lists:
         
         sudo yum makecache
         sudo yum updateinfo
         

  4. Install the guest environment packages:
         
         sudo yum install -y google-compute-engine google-osconfig-agent
         

  5. [Restart the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance). Then, inspect its console log to ensure the guest environment loads as it starts back up.

  6. Connect to the instance using SSH to verify. For detailed instructions, see [connect to the instance using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).




###  Version 9 or earlier 

  1. Verify that your operating system version is supported.
  2. Determine your CentOS/RHEL/Rocky version. Then, create the source repository file, `/etc/yum.repos.d/google-cloud.repo`:
         
         eval $(grep VERSION_ID /etc/os-release)
         sudo tee /etc/yum.repos.d/google-cloud.repo << EOM
         [google-compute-engine]
         name=Google Compute Engine
         baseurl=https://packages.cloud.google.com/yum/repos/google-compute-engine-el${VERSION_ID%%.*}-x86_64-stable
         enabled=1
         gpgcheck=1
         repo_gpgcheck=0
         gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
                https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
         EOM
         

  3. Update package lists:
         
         sudo yum makecache
         sudo yum updateinfo
         

  4. Install the guest environment packages:
         
         sudo yum install -y google-compute-engine google-osconfig-agent
         

  5. [Restart the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance). Then, inspect its console log to ensure the guest environment loads as it starts back up.

  6. Connect to the instance using SSH to verify. For detailed instructions, see [connect to the instance using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).




###  Debian 

Complete the steps for your Debian version.

###  Debian 13 and later 

  1. Verify that your operating system version is supported.
  2. Install the public repository GPG key to `/etc/apt/keyrings`:
         
         sudo curl https://packages.cloud.google.com/apt/doc/apt-key.gpg -o /etc/apt/keyrings/google-keyring.gpg
         

  3. Determine the Debian distro name. Then, create the source list file, `/etc/apt/sources.list.d/google-cloud.list`:
         
         eval $(grep VERSION_CODENAME /etc/os-release)
         sudo tee /etc/apt/sources.list.d/google-cloud.list << EOM
         deb [signed-by=/etc/apt/keyrings/google-keyring.gpg] http://packages.cloud.google.com/apt google-compute-engine-${VERSION_CODENAME}-stable main
         EOM
         

  4. Update package lists:
         
         sudo apt update
         

  5. Install the guest environment packages:
         
         sudo apt install -y gce-configs-trixie google-compute-engine google-osconfig-agent
         

  6. [Restart the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance). Then, inspect its console log to ensure the guest environment loads as it starts back up.

  7. Connect to the instance using SSH to verify. For detailed instructions, see [connect to the instance using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).




###  Debian 12 and earlier 

  1. Verify that your operating system version is supported.
  2. Install the public repository GPG key to `/etc/apt/keyrings`:
         
         sudo curl https://packages.cloud.google.com/apt/doc/apt-key.gpg -o /etc/apt/keyrings/google-keyring.gpg
         

  3. Determine the Debian distro name. Then, create the source list file, `/etc/apt/sources.list.d/google-cloud.list`:
         
         eval $(grep VERSION_CODENAME /etc/os-release)
         sudo tee /etc/apt/sources.list.d/google-cloud.list << EOM
         deb [signed-by=/etc/apt/keyrings/google-keyring.gpg] http://packages.cloud.google.com/apt google-compute-engine-${VERSION_CODENAME}-stable main
         deb [signed-by=/etc/apt/keyrings/google-keyring.gpg] http://packages.cloud.google.com/apt google-cloud-packages-archive-keyring-${VERSION_CODENAME}-stable main
         EOM
         

  4. Update package lists:
         
         sudo apt update
         

  5. Install the guest environment packages:
         
         sudo apt install -y google-cloud-packages-archive-keyring
         sudo apt install -y google-compute-engine google-osconfig-agent
         

  6. [Restart the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance). Then, inspect its console log to ensure the guest environment loads as it starts back up.

  7. Connect to the instance using SSH to verify. For detailed instructions, see [connect to the instance using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).




###  Ubuntu 

  1. Verify that your operating system version is supported.

  2. Enable the Universe repository. Canonical publishes packages for its guest environment to the [Universe repository](https://help.ubuntu.com/community/Repositories/Ubuntu).
         
         sudo apt-add-repository universe

  3. Update package lists:
         
         sudo apt update

  4. Install the guest environment packages:
         
         sudo apt install -y google-compute-engine google-osconfig-agent
         

  5. [Restart the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance). Then, inspect its console log to ensure the guest environment loads as it starts back up.

  6. Connect to the instance using SSH to verify. For detailed instructions, see [connect to the instance using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).




###  SLES 

  1. Verify that your operating system version is supported.

  2. Activate the [Public Cloud Module](https://documentation.suse.com/suma/4.3/en/suse-manager/installation-and-upgrade/pubcloud-setup.html#_activate_the_public_cloud_module)
         
         product=$(sudo SUSEConnect --list-extensions | grep -o "sle-module-public-cloud.*")
         [[ -n "$product" ]] && sudo SUSEConnect -p "$product"
         

  3. Update package lists:
         
         sudo zypper refresh

  4. Install the guest environment packages:
         
         sudo zypper install -y google-guest-{agent,configs,oslogin} \
         google-osconfig-agent
         sudo systemctl enable /usr/lib/systemd/system/google-*
         

  5. [Restart the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance). Then, inspect its console log to ensure the guest environment loads as it starts back up.

  6. Connect to the instance using SSH to verify. For detailed instructions, see [connect to the instance using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).




###  Windows 

Before you begin, verify that your operating system version is supported.

To install the [Windows guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment#windows), run the following commands in an elevated PowerShell version 3.0 or higher prompt. The `Invoke-WebRequest` command requires PowerShell version 3.0 or higher.

  1. Download and install `GooGet`.
         
         [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;
         Invoke-WebRequest https://github.com/google/googet/releases/download/v2.18.3/googet.exe -OutFile $env:temp\googet.exe;
         & "$env:temp\googet.exe" -root C:\ProgramData\GooGet -noconfirm install -sources `
         https://packages.cloud.google.com/yuck/repos/google-compute-engine-stable googet;
         Remove-Item "$env:temp\googet.exe"
         

During installation, `GooGet` adds content to the system environment. After installation completes, launch a new PowerShell console. Alternatively, provide the full path to the `googet.exe` file (C:\ProgramData\GooGet\googet.exe).

  2. Open a new console and add the `google-compute-engine-stable` repository.
         
         googet addrepo google-compute-engine-stable https://packages.cloud.google.com/yuck/repos/google-compute-engine-stable

  3. Install the core Windows guest environment packages.
         
         googet -noconfirm install google-compute-engine-windows `
         google-compute-engine-sysprep google-compute-engine-metadata-scripts `
         google-compute-engine-vss google-osconfig-agent
         

  4. Install the optional Windows guest environment package.
         
         googet -noconfirm install google-compute-engine-auto-updater

**Using the`googet` command.**

To view available packages, run the `googet available` command.

To view installed packages, run the `googet installed` command.

To update to the latest package version, run the `googet update` command.

To view additional commands, run `googet help`.




### Clone boot disk and use startup script

**Important:** In this procedure, the term **startup script** refers to using an `rc.local` script. This term doesn't refer to a startup script that is specified in the instance metadata. Instance metadata startup scripts depend on the guest environment, so you can't use them to install the guest environment.

If you can't connect to an instance to manually install the guest environment, install the guest environment using this procedure, which includes the following steps that you can complete in the Google Cloud console or Cloud Shell.

This method applies only to Linux distributions. For Windows, use one of the other two installation methods.

Use the [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell) to run this procedure. To run this procedure if you are not using Cloud Shell, install the [`jq` command-line JSON processor](https://stedolan.github.io/jq/). This processor filters gcloud CLI output. Cloud Shell has `jq` pre-installed.

###  CentOS/RHEL/Rocky 

Complete the steps for your CentOS/RHEL/Rocky version.

###  Version 10 and later 

  1. Verify that your operating system version is supported.

  2. [Create a new instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) to serve as the rescue instance. Name this instance **rescue**. This rescue instance does not need to run the same Linux OS as the problematic instance. This example uses Debian 9 on the rescue instance.

  3. Stop the problematic instance and create a copy of its boot disk.

     1. Set a variable name for the problematic instance. This variable simplifies referencing the instance in later steps.
            
            export PROB_INSTANCE_NAME=VM_NAME

Replace VM_NAME with the name of the problematic instance.

     2. Stop the problematic instance.
            
            gcloud compute instances stop "$PROB_INSTANCE_NAME"

     3. Get the name of the boot disk for the problem instance.
            
            export PROB_INSTANCE_DISK="$(gcloud compute instances describe \
            "$PROB_INSTANCE_NAME" --format='json' |  jq -r \
            '.disks[] | select(.boot == true) | .source')"
            

     4. Create a snapshot of the boot disk.
            
            export DISK_SNAPSHOT="${PROB_INSTANCE_NAME}-snapshot"
            
            gcloud compute disks snapshot "$PROB_INSTANCE_DISK" \
               --snapshot-names "$DISK_SNAPSHOT"
            

     5. Create a new disk from the snapshot.
            
            export NEW_DISK="${PROB_INSTANCE_NAME}-new-disk"
            
            gcloud compute disks create "$NEW_DISK" \
               --source-snapshot="$DISK_SNAPSHOT"
            

     6. Delete the snapshot.
            
            gcloud compute snapshots delete "$DISK_SNAPSHOT"

  4. Attach the new disk to the rescue instance and mount the root volume for the rescue instance. Since this procedure attaches only one additional disk, the device identifier of the new disk is `/dev/sdb`. CentOS/RHEL/Rocky Linux uses the first volume on a disk as the root volume by default; therefore, the volume identifier should be `/dev/sdb1`. For custom configurations, use `lsblk` to determine the volume identifier.
         
         gcloud compute instances attach-disk rescue --disk "$NEW_DISK"

  5. [Connect to the rescue instance using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
         
         gcloud compute ssh rescue

  6. Run the following steps on the rescue instance.

     1. Mount the root volume of the new disk.
            
            export NEW_DISK_MOUNT_POINT="/tmp/sdb-root-vol"
            DEV="/dev/sdb1"
            sudo mkdir "$NEW_DISK_MOUNT_POINT"
            sudo mount -o nouuid "$DEV" "$NEW_DISK_MOUNT_POINT"
            

     2. Create the `rc.local` script.
            
            cat <<'EOF' >/tmp/rc.local
            #!/bin/bash
            echo "== Installing Google guest environment for CentOS/RHEL/Rocky Linux =="
            sleep 30 # Wait for network.
            echo "Determining CentOS/RHEL/Rocky Linux version..."
            eval $(grep VERSION_ID /etc/os-release)
            if [[ -z $VERSION_ID ]]; then
              echo "ERROR: Could not determine version of CentOS/RHEL/Rocky Linux."
              exit 1
            fi
            echo "Updating repo file..."
            tee "/etc/yum.repos.d/google-cloud.repo" << EOM
            [google-compute-engine]
            name=Google Compute Engine
            baseurl=https://packages.cloud.google.com/yum/repos/google-compute-engine-el${VERSION_ID%%.*}-x86_64-stable
            enabled=1
            gpgcheck=1
            repo_gpgcheck=0
            gpgkey=https://packages.cloud.google.com/yum/doc/rpm-package-key-v${VERSION_ID%%.*}.gpg
            EOM
            echo "Running yum makecache..."
            yum makecache
            echo "Running yum updateinfo..."
            yum updateinfo
            echo "Running yum install google-compute-engine..."
            yum install -y google-compute-engine
            rpm -q google-compute-engine
            if [[ $? -ne 0 ]]; then
              echo "ERROR: Failed to install ${pkg}."
            fi
            echo "Removing this rc.local script."
            rm /etc/rc.d/rc.local
            # Move back any previous rc.local:
            if [[ -f "/etc/moved-rc.local" ]]; then
              echo "Restoring a previous rc.local script."
              mv "/etc/moved-rc.local" "/etc/rc.d/rc.local"
            fi
            echo "Restarting the instance..."
            reboot
            EOF
            

     3. Back up the existing `rc.local` file, move the temporary `rc.local` script into place on the mounted disk, then set its permission to be executable on boot. The temporary script replaces the original script when it finishes booting. To do this, run the following command:
            
            if [ -f "$NEW_DISK_MOUNT_POINT/etc/rc.d/rc.local" ]; then
              sudo mv "$NEW_DISK_MOUNT_POINT/etc/rc.d/rc.local" \
              "$NEW_DISK_MOUNT_POINT/etc/moved-rc.local"
            fi
            sudo mv /tmp/rc.local "$NEW_DISK_MOUNT_POINT/etc/rc.d/rc.local"
            sudo chmod 0755 "$NEW_DISK_MOUNT_POINT/etc/rc.d/rc.local"
            sudo chown root:root "$NEW_DISK_MOUNT_POINT/etc/rc.d/rc.local"
            

     4. Un-mount the root volume of the new disk.
            
            sudo umount "$NEW_DISK_MOUNT_POINT" && sudo rmdir \
            "$NEW_DISK_MOUNT_POINT"

     5. Exit the SSH session to the rescue instance.

  7. Detach the new disk from the rescue instance.
         
         gcloud compute instances detach-disk rescue --disk "$NEW_DISK"

  8. [Create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) to serve as the replacement. When you create the replacement instance, specify the new disk as the boot disk. You can create the replacement instance using the Google Cloud console:

     1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Click the problematic instance, then click **Create similar**.

     3. Specify a name for the replacement instance. In the **Boot disk** section, click **Change** , then click **Existing Disks**. Select the new disk.

     4. Click **Create**. The replacement instance automatically starts after it is created.

As the replacement instance boots up, the temporary `rc.local` script runs and installs the guest environment. To watch the progress of this script, inspect the console logs for lines emitted by the temporary `rc.local` script. To view logs, run the following command:
    
    gcloud compute instances get-serial-port-output REPLACEMENT_VM_NAME

Replace REPLACEMENT_VM_NAME with the name you assigned the replacement instance.

The replacement instance automatically reboots when the temporary `rc.local` script finishes. During the second reboot, you can inspect the console log to make sure the guest environment loads.

  9. Verify that you can [connect to the instance using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

After you verify that the replacement instance is functional, you can [stop](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) or [delete](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) the problematic instance.




###  Version 9 or earlier 

  1. Verify that your operating system version is supported.

  2. [Create a new instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) to serve as the rescue instance. Name this instance **rescue**. This rescue instance does not need to run the same Linux OS as the problematic instance. This example uses Debian 9 on the rescue instance.

  3. Stop the problematic instance and create a copy of its boot disk.

     1. Set a variable name for the problematic instance. This variable simplifies referencing the instance in later steps.
            
            export PROB_INSTANCE_NAME=VM_NAME

Replace VM_NAME with the name of the problematic instance.

     2. Stop the problematic instance.
            
            gcloud compute instances stop "$PROB_INSTANCE_NAME"

     3. Get the name of the boot disk for the problem instance.
            
            export PROB_INSTANCE_DISK="$(gcloud compute instances describe \
            "$PROB_INSTANCE_NAME" --format='json' |  jq -r \
            '.disks[] | select(.boot == true) | .source')"
            

     4. Create a snapshot of the boot disk.
            
            export DISK_SNAPSHOT="${PROB_INSTANCE_NAME}-snapshot"
            
            gcloud compute disks snapshot "$PROB_INSTANCE_DISK" \
               --snapshot-names "$DISK_SNAPSHOT"
            

     5. Create a new disk from the snapshot.
            
            export NEW_DISK="${PROB_INSTANCE_NAME}-new-disk"
            
            gcloud compute disks create "$NEW_DISK" \
               --source-snapshot="$DISK_SNAPSHOT"
            

     6. Delete the snapshot:
            
            gcloud compute snapshots delete "$DISK_SNAPSHOT"

  4. Attach the new disk to the rescue instance and mount the root volume for the rescue instance. Since this procedure attaches only one additional disk, the device identifier of the new disk is `/dev/sdb`. CentOS/RHEL/Rocky Linux uses the first volume on a disk as the root volume by default; therefore, the volume identifier should be `/dev/sdb1`. For custom configurations, use `lsblk` to determine the volume identifier.
         
         gcloud compute instances attach-disk rescue --disk "$NEW_DISK"

  5. [Connect to the rescue instance using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
         
         gcloud compute ssh rescue

  6. Run the following steps on the rescue instance.

     1. Mount the root volume of the new disk.
            
            export NEW_DISK_MOUNT_POINT="/tmp/sdb-root-vol"
            DEV="/dev/sdb1"
            sudo mkdir "$NEW_DISK_MOUNT_POINT"
            sudo mount -o nouuid "$DEV" "$NEW_DISK_MOUNT_POINT"
            

     2. Create the `rc.local` script.
            
            cat <<'EOF' >/tmp/rc.local
            #!/bin/bash
            echo "== Installing Google guest environment for CentOS/RHEL/Rocky Linux =="
            sleep 30 # Wait for network.
            echo "Determining CentOS/RHEL/Rocky Linux version..."
            eval $(grep VERSION_ID /etc/os-release)
            if [[ -z $VERSION_ID ]]; then
              echo "ERROR: Could not determine version of CentOS/RHEL/Rocky Linux."
              exit 1
            fi
            echo "Updating repo file..."
            tee "/etc/yum.repos.d/google-cloud.repo" << EOM
            [google-compute-engine]
            name=Google Compute Engine
            baseurl=https://packages.cloud.google.com/yum/repos/google-compute-engine-el${VERSION_ID%%.*}-x86_64-stable
            enabled=1
            gpgcheck=1
            repo_gpgcheck=0
            gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
            https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
            EOM
            echo "Running yum makecache..."
            yum makecache
            echo "Running yum updateinfo..."
            yum updateinfo
            echo "Running yum install google-compute-engine..."
            yum install -y google-compute-engine
            rpm -q google-compute-engine
            if [[ $? -ne 0 ]]; then
              echo "ERROR: Failed to install ${pkg}."
            fi
            echo "Removing this rc.local script."
            rm /etc/rc.d/rc.local
            # Move back any previous rc.local:
            if [[ -f "/etc/moved-rc.local" ]]; then
              echo "Restoring a previous rc.local script."
              mv "/etc/moved-rc.local" "/etc/rc.d/rc.local"
            fi
            echo "Restarting the instance..."
            reboot
            EOF
            

     3. Back up the existing `rc.local` file, move the temporary `rc.local` script into place on the mounted disk, then set its permission to be executable on boot. The temporary script replaces the original script when it finishes booting. To do this, run the following command:
            
            if [ -f "$NEW_DISK_MOUNT_POINT/etc/rc.d/rc.local" ]; then
              sudo mv "$NEW_DISK_MOUNT_POINT/etc/rc.d/rc.local" \
              "$NEW_DISK_MOUNT_POINT/etc/moved-rc.local"
            fi
            sudo mv /tmp/rc.local "$NEW_DISK_MOUNT_POINT/etc/rc.d/rc.local"
            sudo chmod 0755 "$NEW_DISK_MOUNT_POINT/etc/rc.d/rc.local"
            sudo chown root:root "$NEW_DISK_MOUNT_POINT/etc/rc.d/rc.local"
            

     4. Un-mount the root volume of the new disk.
            
            sudo umount "$NEW_DISK_MOUNT_POINT" && sudo rmdir \
            "$NEW_DISK_MOUNT_POINT"

     5. Exit the SSH session to the rescue instance.

  7. Detach the new disk from the rescue instance.
         
         gcloud compute instances detach-disk rescue --disk "$NEW_DISK"

  8. [Create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) to serve as the replacement. When you create the replacement instance, specify the new disk as the boot disk. You can create the replacement instance using the Google Cloud console:

     1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Click the problematic instance, then click **Create similar**.

     3. Specify a name for the replacement instance. In the **Boot disk** section, click **Change** , then click **Existing Disks**. Select the new disk.

     4. Click **Create**. The replacement instance automatically starts after it is created.

As the replacement instance boots up, the temporary `rc.local` script runs and installs the guest environment. To watch the progress of this script, inspect the console logs for lines emitted by the temporary `rc.local` script. To view logs, run the following command:
    
    gcloud compute instances get-serial-port-output REPLACEMENT_VM_NAME

Replace REPLACEMENT_VM_NAME with the name you assigned the replacement instance.

The replacement instance automatically reboots when the temporary `rc.local` script finishes. During the second reboot, you can inspect the console log to make sure the guest environment loads.

  9. Verify that you can [connect to the instance using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

After you verify that the replacement instance is functional, you can [stop](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) or [delete](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) the problematic instance.




###  Debian 

  1. Verify that your operating system version is supported

  2. [Create a new instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) to serve as the rescue instance. Name this instance **rescue**. This rescue instance does not need to run the same Linux OS as the problematic instance. This example uses Debian 9 on the rescue instance.

  3. Stop the problematic instance and create a copy of its boot disk.

     1. Set a variable name for the problematic instance. This variable simplifies referencing the instance in later steps.
            
            export PROB_INSTANCE_NAME=VM_NAME

Replace VM_NAME with the name of the problematic instance.

     2. Stop the problematic instance.
            
            gcloud compute instances stop "$PROB_INSTANCE_NAME"

     3. Get the name of the boot disk for the problem instance.
            
            export PROB_INSTANCE_DISK="$(gcloud compute instances describe \
            "$PROB_INSTANCE_NAME" --format='json' |  jq -r \
            '.disks[] | select(.boot == true) | .source')"
            

     4. Create a snapshot of the boot disk.
            
            export DISK_SNAPSHOT="${PROB_INSTANCE_NAME}-snapshot"
            
            gcloud compute disks snapshot "$PROB_INSTANCE_DISK" \
               --snapshot-names "$DISK_SNAPSHOT"
            

     5. Create a new disk from the snapshot.
            
            export NEW_DISK="${PROB_INSTANCE_NAME}-new-disk"
            
            gcloud compute disks create "$NEW_DISK" \
               --source-snapshot="$DISK_SNAPSHOT"
            

     6. Delete the snapshot:
            
            gcloud compute snapshots delete "$DISK_SNAPSHOT"

  4. Attach the new disk to the rescue instance and mount the root volume for the rescue instance. Since this procedure attaches only one additional disk, the device identifier of the new disk is `/dev/sdb`. Debian uses the first volume on a disk as the root volume by default; therefore, the volume identifier should be `/dev/sdb1`. For custom configurations, use `lsblk` to determine the volume identifier.
         
         gcloud compute instances attach-disk rescue --disk "$NEW_DISK"

  5. [Connect to the rescue instance using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
         
         gcloud compute ssh rescue

  6. Run the following steps on the rescue instance.

     1. Mount the root volume of the new disk.
            
            export NEW_DISK_MOUNT_POINT="/tmp/sdb-root-vol"
            DEV="/dev/sdb1"
            sudo mkdir "$NEW_DISK_MOUNT_POINT"
            sudo mount "$DEV" "$NEW_DISK_MOUNT_POINT"
            

     2. Create the `rc.local` script.
            
            cat <<'EOF' >/tmp/rc.local
            #!/bin/bash
            echo "== Installing Google guest environment for Debian =="
            export DEBIAN_FRONTEND=noninteractive
            sleep 30 # Wait for network.
            echo "Determining Debian version..."
            eval $(grep VERSION_CODENAME /etc/os-release)
            if [[ -z $VERSION_CODENAME ]]; then
             echo "ERROR: Could not determine Debian version."
             exit 1
            fi
            echo "Adding GPG key for Google cloud repo."
            curl https://packages.cloud.google.com/apt/doc/apt-key.gpg -o /etc/apt/keyrings/google-keyring.gpg
            echo "Updating repo file..."
            tee "/etc/apt/sources.list.d/google-cloud.list" << EOM
            deb [signed-by=/etc/apt/keyrings/google-keyring.gpg] http://packages.cloud.google.com/apt google-compute-engine-${VERSION_CODENAME}-stable main
            deb [signed-by=/etc/apt/keyrings/google-keyring.gpg] http://packages.cloud.google.com/apt google-cloud-packages-archive-keyring-${VERSION_CODENAME}-stable main
            EOM
            echo "Running apt update..."
            apt update
            echo "Installing packages..."
            for pkg in google-cloud-packages-archive-keyring google-compute-engine; do
             echo "Running apt install ${pkg}..."
             apt install -y ${pkg}
             if [[ $? -ne 0 ]]; then
                echo "ERROR: Failed to install ${pkg}."
             fi
            done
            echo "Removing this rc.local script."
            rm /etc/rc.local
            # Move back any previous rc.local:
            if [[ -f "/etc/moved-rc.local" ]]; then
             echo "Restoring a previous rc.local script."
             mv "/etc/moved-rc.local" "/etc/rc.local"
            fi
            echo "Restarting the instance..."
            reboot
            EOF
            

     3. Back up the existing `rc.local` file, move the temporary `rc.local` script into place on the mounted disk, then set its permission to be executable on boot. The temporary script replaces the original script when it finishes booting. To do this, run the following command:
            
            if [[ -f "$NEW_DISK_MOUNT_POINT/etc/rc.local" ]]; then
               sudo mv "$NEW_DISK_MOUNT_POINT/etc/rc.local" \
               "$NEW_DISK_MOUNT_POINT/etc/moved-rc.local"
            fi
            sudo mv /tmp/rc.local "$NEW_DISK_MOUNT_POINT/etc/rc.local"
            sudo chmod 0755 "$NEW_DISK_MOUNT_POINT/etc/rc.local"
            sudo chown root:root "$NEW_DISK_MOUNT_POINT/etc/rc.local"
            

     4. Un-mount the root volume of the new disk.
            
            sudo umount "$NEW_DISK_MOUNT_POINT" && sudo rmdir "$NEW_DISK_MOUNT_POINT"

     5. Exit the SSH session to the rescue instance.

  7. Detach the new disk from the rescue instance.
         
         gcloud compute instances detach-disk rescue --disk "$NEW_DISK"

  8. [Create a new instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) to serve as the replacement. When you create the replacement instance, specify the new disk as the boot disk. You can create the replacement instance using the Google Cloud console:

     1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Click the problematic instance, then click **Create similar**.

     3. Specify a name for the replacement instance. In the **Boot disk** section, click **Change** , then click **Existing Disks**. Select the new disk.

     4. Click **Create**. The replacement instance automatically starts after it is created.

As the replacement instance boots up, the temporary `rc.local` script runs and installs the guest environment. To watch the progress of this script, inspect the console logs for lines emitted by the temporary `rc.local` script. To view logs, run the following command:
    
    gcloud compute instances get-serial-port-output REPLACEMENT_VM_NAME

Replace REPLACEMENT_VM_NAME with the name you assigned the replacement instance.

The replacement instance automatically reboots when the temporary `rc.local` script finishes. During the second reboot, you can inspect the console log to make sure the guest environment loads.

  9. Verify that you can [connect to the instance using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

After you verify that the replacement instance is functional, you can [stop](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) or [delete](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) the problematic instance.




###  Ubuntu 

  1. Verify that your operating system version is supported

  2. [Create a new instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) to serve as the rescue instance. Name this instance **rescue**. This rescue instance does not need to run the same Linux OS as the problematic instance. This example uses Debian 9 on the rescue instance.

  3. Stop the problematic instance and create a copy of its boot disk.

     1. Set a variable name for the problematic instance. This variable simplifies referencing the instance in later steps.
            
            export PROB_INSTANCE_NAME=VM_NAME

Replace VM_NAME with the name of the problematic instance.

     2. Stop the problematic instance.
            
            gcloud compute instances stop "$PROB_INSTANCE_NAME"

     3. Get the name of the boot disk for the problem instance.
            
            export PROB_INSTANCE_DISK="$(gcloud compute instances describe \
            "$PROB_INSTANCE_NAME" --format='json' |  jq -r \
            '.disks[] | select(.boot == true) | .source')"
            

     4. Create a snapshot of the boot disk.
            
            export DISK_SNAPSHOT="${PROB_INSTANCE_NAME}-snapshot"
            
            gcloud compute disks snapshot "$PROB_INSTANCE_DISK" \
               --snapshot-names "$DISK_SNAPSHOT"
            

     5. Create a new disk from the snapshot.
            
            export NEW_DISK="${PROB_INSTANCE_NAME}-new-disk"
            
            gcloud compute disks create "$NEW_DISK" \
               --source-snapshot="$DISK_SNAPSHOT"
            

     6. Delete the snapshot:
            
            gcloud compute snapshots delete "$DISK_SNAPSHOT"

  4. Attach the new disk to the rescue instance and mount the root volume for the rescue instance. Since this procedure attaches only one additional disk, the device identifier of the new disk is `/dev/sdb`. Ubuntu labels its root volume 1 by default; therefore, the volume identifier should be`*/dev/sdb`*. For custom configurations, use `lsblk` to determine the volume identifier.
         
         gcloud compute instances attach-disk rescue --disk "$NEW_DISK"

  5. [Connect to the rescue instance using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
         
         gcloud compute ssh rescue

  6. Run the following steps on the rescue instance.

     1. Mount the root volume of the new disk.
            
            export NEW_DISK_MOUNT_POINT="/tmp/sdb-root-vol"
            DEV="/dev/sdb1"
            sudo mkdir "$NEW_DISK_MOUNT_POINT"
            sudo mount "$DEV" "$NEW_DISK_MOUNT_POINT"
            

     2. Create the `rc.local` script.
            
            cat <<'EOF' >/tmp/rc.local
            #!/bin/bash
            echo "== Installing a Linux guest environment for Ubuntu =="
            sleep 30 # Wait for network.
            echo "Running apt update..."
            apt update
            echo "Installing packages..."
            echo "Running apt install google-compute-engine..."
            apt install -y google-compute-engine
            if [[ $? -ne 0 ]]; then
             echo "ERROR: Failed to install ${pkg}."
            fi
            echo "Removing this rc.local script."
            rm /etc/rc.local
            # Move back any previous rc.local:
            if [[ -f "/etc/moved-rc.local" ]]; then
             echo "Restoring a previous rc.local script."
             mv "/etc/moved-rc.local" "/etc/rc.local"
            fi
            echo "Restarting the instance..."
            reboot
            EOF
            

     3. Back up the existing `rc.local` file, move the temporary `rc.local` script into place on the mounted disk, then set its permission to be executable on boot. The temporary script replaces the original script when it finishes booting. To do this, run the following command:
            
            if [[ -f "$NEW_DISK_MOUNT_POINT/etc/rc.local" ]]; then
               sudo mv "$NEW_DISK_MOUNT_POINT/etc/rc.local" \
               "$NEW_DISK_MOUNT_POINT/etc/moved-rc.local"
            fi
            sudo mv /tmp/rc.local "$NEW_DISK_MOUNT_POINT/etc/rc.local"
            sudo chmod 0755 "$NEW_DISK_MOUNT_POINT/etc/rc.local"
            sudo chown root:root "$NEW_DISK_MOUNT_POINT/etc/rc.local"
            

     4. Un-mount the root volume of the new disk.
            
            sudo umount "$NEW_DISK_MOUNT_POINT" && sudo rmdir "$NEW_DISK_MOUNT_POINT"

     5. Exit the SSH session to the rescue instance.

  7. Detach the new disk from the rescue instance.
         
         gcloud compute instances detach-disk rescue --disk "$NEW_DISK"

  8. [Create a new instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) to serve as the replacement. When you create the replacement instance, specify the new disk as the boot disk. You can create the replacement instance using the Google Cloud console:

     1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Click the problematic instance, then click **Create similar**.

     3. Specify a name for the replacement instance. In the **Boot disk** section, click **Change** , then click **Existing Disks**. Select the new disk.

     4. Click **Create**. The replacement instance automatically starts after it is created.

As the replacement instance boots up, the temporary `rc.local` script runs and installs the guest environment. To watch the progress of this script, inspect the console logs for lines emitted by the temporary `rc.local` script. To view logs, run the following command:
    
    gcloud compute instances get-serial-port-output REPLACEMENT_VM_NAME

Replace REPLACEMENT_VM_NAME with the name you assigned the replacement instance.

The replacement instance automatically reboots when the temporary `rc.local` script finishes. During the second reboot, you can inspect the console log to make sure the guest environment loads.

  9. Verify that you can [connect to the instance using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

After you verify that the replacement instance is functional, you can [stop](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) or [delete](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) the problematic instance.




## Update the guest environment

If you receive a message that the guest environment is outdated, update the packages for your operating system as follows:

###  CentOS/RHEL/Rocky

To update CentOS, RHEL and Rocky Linux operating systems, run the following commands:
    
    
    sudo yum makecache
    sudo yum install google-compute-engine google-compute-engine-oslogin \
    google-guest-agent google-osconfig-agent
    

###  Debian 

To update Debian operating systems, run the following commands:
    
    
    sudo apt update
    sudo apt install google-compute-engine google-compute-engine-oslogin \
    google-guest-agent google-osconfig-agent
    

###  Ubuntu 

To update Ubuntu operating systems, run the following commands:
    
    
    sudo apt update
    sudo apt install google-compute-engine google-compute-engine-oslogin \
    google-guest-agent google-osconfig-agent
    

###  SLES 

To update SLES operating systems, run the following commands:
    
    
    sudo zypper refresh
    sudo zypper install google-guest-{agent,configs,oslogin} \
    google-osconfig-agent
    

###  Windows 

To update Windows operating systems, run the following command:
    
    
    googet update

## Validate the guest environment

You can check if a guest environment is installed by inspecting system logs that are emitted to the console while an instance boots up, or by listing the installed packages while connected to the instance.

### View expected console logs for the guest environment

This table summarizes expected output for console logs emitted by instances with working guest environments as they start up.

Operating system | Service management | Expected output  
---|---|---  
CentOS/RHEL/Rocky Linux  
Debian  
Ubuntu  
SLES  
Container-Optimized OS 89 and newer | systemd | 
    
    
    google_guest_agent: GCE Agent Started (version YYYYMMDD.NN)
    google_metadata_script_runner: Starting startup scripts (version YYYYMMDD.NN)
    OSConfigAgent Info: OSConfig Agent (version YYYYMMDD.NN)
      
  
Container-Optimized OS 85 and older | systemd | 
    
    
    Started Google Compute Engine Accounts Daemon
    Started Google Compute Engine Network Daemon
    Started Google Compute Engine Clock Skew Daemon
    Started Google Compute Engine Instance Setup
    Started Google Compute Engine Startup Scripts
    Started Google Compute Engine Shutdown Scripts  
  
Windows |  | 
    
    
    GCEGuestAgent: GCE Agent Started (version YYYYMMDD.NN)
    GCEMetadataScripts: Starting startup scripts (version YYYYMMDD.NN)
    OSConfigAgent Info: OSConfig Agent (version YYYYMMDD.NN)
      
  
To view console logs for an instance, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     1. Select the instance you need to examine.
     2. [Restart](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance) or [reset the instance](https://docs.cloud.google.com/compute/docs/instances/reset-instance).
     3. Under **Logs** , click **Serial port 1 (console)**.
     4. Search for the expected output in the table that precedes these steps.



###  gcloud 

  1. [Restart](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance) or [reset the instance](https://docs.cloud.google.com/compute/docs/instances/reset-instance).
  2. Use the `gcloud compute instances get-serial-port-output` sub-command to connect using the Google Cloud CLI. For example:
         
         gcloud compute instances get-serial-port-output VM_NAME

Replace VM_NAME with the name of the instance you need to examine.

  3. Search for the expected output in the table that precedes these steps.




### View loaded services by operating system version

This section summarizes the services that should be loaded on instances with working guest environments. You must run the command to list services after connecting to the instance. Therefore, you can perform this check only if you have access to the instance.

###  CentOS/RHEL/Rocky 

To view loaded services for CentOS, RHEL, and Rocky Linux distributions, run the following command:
    
    
    sudo systemctl list-unit-files | grep google | grep enabled

The output resembles the following:
    
    
    google-disk-expand.service             enabled
    google-guest-agent.service             enabled
    google-osconfig-agent.service          enabled
    google-shutdown-scripts.service        enabled
    google-startup-scripts.service         enabled
    google-oslogin-cache.timer             enabled

###  Debian 

To view loaded services for Debian distributions, run the following command:
    
    
    sudo systemctl list-unit-files | grep google | grep enabled

The output resembles the following:
    
    
    google-disk-expand.service             enabled
    google-guest-agent.service             enabled
    google-osconfig-agent.service          enabled
    google-shutdown-scripts.service        enabled
    google-startup-scripts.service         enabled
    google-oslogin-cache.timer             enabled

###  Ubuntu 

To view loaded services for Ubuntu distributions, run the following command:
    
    
    sudo systemctl list-unit-files | grep google | grep enabled

The output resembles the following:
    
    
    google-guest-agent.service             enabled
    google-osconfig-agent.service          enabled
    google-shutdown-scripts.service        enabled
    google-startup-scripts.service         enabled
    google-oslogin-cache.timer             enabled

###  Container-Optimized OS 

To view loaded services for Container-Optimized OS distributions, run the following command:
    
    
    sudo systemctl list-unit-files | grep google

The output resembles the following:
    
    
    var-lib-google.mount                   disabled
    google-guest-agent.service             disabled
    google-osconfig-agent.service          disabled
    google-osconfig-init.service           disabled
    google-oslogin-cache.service           static
    google-shutdown-scripts.service        disabled
    google-startup-scripts.service         disabled
    var-lib-google-remount.service         static
    google-oslogin-cache.timer             disabled 

###  SLES 12+ 

To view loaded services for SLES 12+ distributions, run the following command:
    
    
    sudo systemctl list-unit-files | grep google | grep enabled

The output resembles the following:
    
    
    google-guest-agent.service              enabled
    google-osconfig-agent.service           enabled
    google-shutdown-scripts.service         enabled
    google-startup-scripts.service          enabled
    google-oslogin-cache.timer              enabled 

###  Windows 

To view loaded services for Windows distributions, run the following command:
    
    
    Get-Service GCEAgent Get-ScheduledTask GCEStartup

The output resembles the following:
    
    
    Running    GCEAgent   GCEAgent    GCEStartup Ready

### View installed packages by operating system version

This section summarizes the packages that should be installed on instances with working guest environments. You must run the command to list installed packages after connecting to the instance. Therefore, you can perform this check only if you have access to the instance.

**Note:** CoreOS and Container-Optimized OS don't have package managers. Instead, inspect instance console logs or loaded services to determine the guest environment's status.

For more information about these packages, see [Guest environment components](https://docs.cloud.google.com/compute/docs/images/guest-environment#guest-environment-components).

###  CentOS/RHEL/Rocky 

To view installed packages and package versions for CentOS, RHEL, and Rocky Linux distributions, run one of the following commands:

  * To view installed packages, run the following command:
        
        rpm -qa --queryformat '%{NAME}\n' | grep -iE 'google|gce'

The output resembles the following. The list of packages can vary. It might also include components such as `google-cloud-cli-anthoscli`. RHEL images can have version-specific packages, for example, `google-rhui-client-rhel8`, or SAP-specific variants.
        
        google-osconfig-agent
        google-compute-engine-oslogin
        google-guest-agent
        gce-disk-expand
        google-compute-engine
        google-cloud-cli
        google-cloud-ops-agent
        

  * To view package versions, run the following command:
        
        rpm -qa --queryformat '%{NAME}-%{VERSION}\n' | grep -iE 'google|gce'

The output resembles the following. The list of packages can vary. It might also include components such as `google-cloud-cli-anthoscli`. RHEL images can have version-specific packages, for example, `google-rhui-client-rhel8`, or SAP-specific variants.
        
        google-osconfig-agent-20251028.00
        google-compute-engine-oslogin-20250821.00
        google-guest-agent-20251205.00
        gce-disk-expand-20250820.00
        google-compute-engine-20250821.00
        google-cloud-cli-551.0.0
        google-cloud-ops-agent-2.63.0-1
        




###  Debian 

To view installed packages for Debian distributions, run the following command:
    
    
    apt list --installed | grep -i google

The output resembles the following.
    
    
    gce-disk-expand
    google-cloud-packages-archive-keyring
    google-cloud-sdk
    google-compute-engine-oslogin
    google-compute-engine
    google-guest-agent
    google-osconfig-agent

###  SUSE (SLES) 

To view installed packages and package versions for SUSE (SLES) distributions, run one of the following commands:

  * To view installed packages, run the following command:
        
        rpm -qa --queryformat '%{NAME}\n' | grep -iE 'google|gce'

The output resembles the following:
        
        google-guest-configs
        google-osconfig-agent
        google-guest-oslogin
        google-guest-agent

  * To view package versions, run the following command:
        
        rpm -qa --queryformat '%{NAME}-%{VERSION}\n' | grep -iE 'google|gce'

The output resembles the following:
        
        google-guest-configs-20260112.00
        google-osconfig-agent-20251028.00
        google-compute-engine-oslogin-20250821.00
        google-guest-agent-20251205.00




###  Ubuntu 

To view installed packages and package versions for Ubuntu distributions, run the following command:
    
    
    apt list --installed | grep -i google

The output resembles the following:
    
    
    google-compute-engine-oslogin
    google-compute-engine
    google-guest-agent
    google-osconfig-agent

###  Windows 

To view installed packages and package versions for Windows distributions, run the following command:
    
    
    googet installed

The output resembles the following:
    
    
    certgen
    googet
    google-compute-engine-auto-updater
    google-compute-engine-driver-gga
    google-compute-engine-driver-netkvm
    google-compute-engine-driver-pvpanic
    google-compute-engine-driver-vioscsi
    google-compute-engine-metadata-scripts
    google-compute-engine-powershell
    google-compute-engine-sysprep
    google-compute-engine-vss
    google-compute-engine-windows
    google-osconfig-agent
    

## What's next

  * Read the [troubleshooting tips](https://docs.cloud.google.com/compute/docs/troubleshooting).
  * Learn more about applying [metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata).
  * Learn about [SSH keys](https://docs.cloud.google.com/compute/docs/instances/adding-removing-ssh-keys).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
