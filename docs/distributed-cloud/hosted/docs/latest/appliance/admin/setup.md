---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup/
title: Configure the appliance and install software \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:39.160259+00:00
---

# Configure the appliance and install software  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Configure the appliance and install software Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up and configure Google Distributed Cloud (GDC) air-gapped appliance at the customer site.

On first boot, the drives are unlocked without human intervention. The configuration takes about four to six hours to complete.

**Warning:** You must complete the final [cleanup steps](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup#execute-cleanup) without interruption. Restarting or powering off before completing the configuration causes a system error that requires a full re-bootstrap.**Important:** To access the URLs on this page, you must connect to the internet. The URLs are provided for use when you have such access.

## Before you begin

  1. [Create input configuration file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/create-input-ciq).
  2. If you plan to use an external NTP server or HSM, connect the appliance to the hardware before you run the install.



## Configure the appliance

Verify all fields of the input configuration file are accurate. Once the file is copied to the server blade in the following steps, the final configuration begins automatically and cannot easily be stopped.

  1. Transfer the input configuration file to the path `/var/lib/assets/ciq_configure_input.yaml` on the server blade assigned the `198.18.0.6` IP address.
         
         scp configuration-input.yaml applianceusr@198.18.0.6:/var/lib/assets/ciq_configure_input.yaml
         

  2. The configuration starts automatically and saves output in the `/var/log/gdch-install.txt` file.

  3. Monitor progress with one of the following:

     * Monitor the `/var/log/gdch-install.txt` file with the following:
           
           ssh applianceusr@198.18.0.6 'tail -f /var/log/gdch-install.txt'
           

The installation is complete when the log outputs the following line, indicating the cleanup phase has finished:
           
           <<< Completed phase: cleanup
           

     * Alternatively, you can look for the status of the installation service, with the following:
           
           ssh applianceusr@198.18.0.6 'systemctl status gdch-app-install'
           

The output indicates the status of the installation. In particular, the `Active` field indicates if the install is ongoing, failed, or inactive. When the line indicates that the install process is inactive and has a status of `0/SUCCESS`, the installation is complete.




## Back up the credentials

Retrieve the device emergency credentials and store them in a secure location

  1. Create a backup archive of the access credentials by running the following, enter the `applianceusr` password when prompted:
         
         ssh applianceusr@198.18.0.6 'sudo -S /var/lib/release/gdcloud appliance install --phase=postinstall'
         

  2. Copy the credential backup to the bootstrapper by running the following, enter the `applianceusr` password when prompted:
         
         ssh applianceusr@198.18.0.6 'sudo -S setfacl -m u:applianceusr:rwx /var/lib/assets/credentials.tar.gz'
         scp applianceusr@198.18.0.6:/var/lib/assets/credentials.tar.gz .
         

  3. Verify the contents of this archive include, the cellcfg backup, identity provider credentials, switch credentials, and SSH keys for the server blade assigned to the `198.18.0.6` IP address.

  4. Store the archive on a separate, secure medium (such as a USB drive) for emergency access.




## Delete appliance user and stop appliance install services

After the backup of emergency credentials is completed, run the following command on the server blade assigned the `198.18.0.6` IP address to delete the default appliance user account and stop install services. In order to use the server blade assigned the `198.18.0.6` IP address in the future, you can use [emergency credentials](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup#back_up_emergency_credentials).

  1. Execute the following to remove the default user access and secure the device
         
         ssh applianceusr@198.18.0.6 'sudo -S /usr/local/bin/cleanup_appliance_user.sh'
         




## Manage YubiKeys

Each YubiKey is bound to a blade during the bootstrap process and cannot be used with another blade. The keys cannot be used interchangeably.

**Warning:** Store all YubiKeys in a secure location and remove them whenever the appliance is not in operation. Because YubiKeys can decrypt local drives at any stage of the GDC air-gapped appliance lifecycle, leaving them unattended in an inactive device creates a security vulnerability.

The YubiKey only needs to be inserted during the boot process. If you remove the YubiKey after the boot process, it doesn't affect the operation of the appliance. If you remove the YubiKey, it must be reinserted in the same node before the next boot.

## What's next

  * [Configure external NTP](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/configure-ntp)
  * [Configure external HSM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/configure-hsm-network-connection)
  * [Set up IO tools to access runbooks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/iotool-setup)
  * [Configure alert notifications](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/smtp-alerts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
