---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent/
title: Install the Backup and DR agent on a Linux host for appliance-managed backups \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:14.855402+00:00
---

# Install the Backup and DR agent on a Linux host for appliance-managed backups  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Install the Backup and DR agent on a Linux host for appliance-managed backups Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page describes how to install the Backup and DR agent for appliance-managed storage on a Linux host and perform other operations such as how to regenerate a secret key, check the Backup and DR agent status, and restart the Backup and DR agent.

## How it works

The Backup and DR agent for Linux runs as a daemon process under username root. It listens on TCP port 5106 for communication from the backup/recovery appliance. The agent writes to a log file in the installation directory `/var/act/log/UDSAgent.log` and posts significant events to the `/var/log/messages` repository.

After installing the agent, you need to initialize trusted communications between the backup/recovery appliance and the Backup and DR agent. This only needs to be done once. The secret key needs to be added within two hours of being generated. If the secret key expires, you need to generate a new key.

Sometimes you may need to regenerate a secret key. For example, if a host remains offline for an extended period, its certificate status may change to "Uninitialized". If this occurs, you must generate a new key to re-establish a valid certificate and resume normal operation.

## Install the agent on a Linux host

**Note:** You must have at least 1 GB of free space in the /opt directory for UDSAgent to install or upgrade on Linux hosts.

Use the following instructions to install the agent on a Linux host:

  1. Download the agent installer file, see [Obtain the right Backup and DR agent for your host](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/about-connector#right-connector).

  2. Upload the installer file to your Linux server.

  3. To install the agent, choose one of the following:

     * For Linux 32-bit installation, run the following command.
           
           rpm -ivh connector-Linux_x86-version.rpm
           

     * For Linux 64-bit installation, run the following command.
           
           rpm -ivh connector-Linux-version.rpm
           

     * For Linux Ubuntu installation, run the following command.
           
           dpkg -i connector-linux_ubuntu_amd64-version.deb
           

The agent always installs at `/opt/act`. When the installation is complete, a secret key displays.

  4. Save the secret key in a notepad or in a text editor, you need to add this in Backup and DR agent section, see [Add Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-linux-hosts).




### Regenerate the secret key

The secret key that is generated in the Install the agent on a Linux host section is valid only for two hours. You need to add it to the appliance management console within this timeframe or generate a new one.

Use the following instructions to generate a new key and add it to the management console.

  1. On the Linux host, sign in as a root user and run either of the commands in the directory:

     * To reset the secret key after confirmation the action, run the following command:
           
           /opt/act/bin/udsagent secret --reset
           

     * To reset the secret immediately without confirmation, run the following command:
           
           /opt/act/bin/udsagent secret --reset --restart
           

  2. Save the secret key in a notepad or in editor. This secret key is valid for two hours.




### Add a secret key

If you want to update the secret key or didn't add the secret key the first time, you can add in the [Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-linux-hosts) using the following instructions.

  1. In the appliance management console, select **Manage** and then select **Hosts**.

  2. Right-click the Linux host and choose **Edit**.

  3. Go to **Backup and DR agent Settings** section and find the **Secret** field.

  4. Paste the secret key that you saved earlier in the **Secret** field and click **Save**. Ensure the **Certificate** status changes to **Valid**. If you get a partial success message, use the instructions to [Validate backup/recovery appliance to Backup and DR agent connectivity](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-network-settings#validate).




### Check Backup and DR agent status

After the agent is installed, you can verify its status on the Linux hosts using the following command.
    
    
    systemctl status udsagent
    

The output looks similar to the following:
    
    
    [root@postgres ~]# systemctl status udsagent
    ● udsagent.service - Google Cloud Backup and DR service
       Loaded: loaded (/usr/lib/systemd/system/udsagent.service; enabled; vendor preset: disabled)
       Active: active (running) since Wed 2025-11-09 22:13:45 UTC; 17min ago
       Process: 1056 ExecStart=/opt/act/initscripts/udsagent.init start (code=exited, status=0/SUCCESS)
       Main PID: 1128 (udsagent)
            CGroup: /system.slice/udsagent.service
                ├─1128 /opt/act/bin/udsagent start
                └─1132 /opt/act/bin/udsagent start
    
        Nov 09 22:13:44 postgres systemd[1]: Starting Google Cloud Backup and DR…
        Nov 09 22:13:45 postgres udsagent.init[1056]: Starting /opt/act/bin/udsagent as a daemon. It may take a few minutes for the service to start completely.
    

### Restart the Backup and DR agent on a Linux host

To restart the Backup and DR agent on a Linux host, execute the following command on the host.
    
    
    systemctl restart udsagent
    

## Configure multipathing for the agent

Before installing the agent, configure multipathing as follows:

  1. Add the following changes to /etc/multipath.conf on the host:
         
         blacklist {
               device {
               vendor "ACTIFIO|SCST_FIO|SCST_BIO"
               product "ActifioSky|LUN0"
               }
          }
         

  2. Restart multipathd:
         
         systemctl status multipathd
         




## Disable multipath from the agent config
    
    
     ```none
     /act/config/connector.conf
    
     DisableMultipathCheck = true
     ```
    

### Uninstall the Backup and DR agent from a Linux host using the command line

Use the following instructions to uninstall the Backup and DR agent from a Linux host:

### CentOS/RHEL/SLES

  1. Sign in as a root user and stop the Backup and DR agent by running the following command:
         
         systemctl stop udsagent
         

For older Linux versions you may need to use the following command:
         
         /etc/init.d/udsagent stop
         

  2. Check the installed Linux Backup and DR agent RPM name with the following command:
         
         yum list installed | grep udsagent
         

You can also use the following command to check the RPM name:
         
         rpm -qa udsagent
         

The output looks similar to the following:
         
         udsagent-11.0.15-8756.x86_64
         

  3. Uninstall the package using the name you obtained from the query. For example:
         
         yum remove udsagent
         

You can also use the following command to uninstall the package:
         
         rpm -e udsagent
         




### Ubuntu

  1. Sign in as a root user and stop the Backup and DR agent by running the following command:
         
         systemctl stop udsagent
         

  2. Uninstall the agent using the following command:
         
         dpkg --remove udsagent
         




## What's next

  * To install Backup and DR agent on a Windows host, see [Backup and DR agent on Windows hosts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/windows-agent)

  * To configure iSCSI connectivity on a Linux host, see [iSCSI connectivity on a Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-linux-hosts#iSCSI)

  * To configure NFS connectivity on a Linux host, see [NFS connectivity on a Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-linux-hosts#NFS)

  * To upgrade Backup and DR agent, see [Maintain Backup and DR agents on hosts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-agent)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
