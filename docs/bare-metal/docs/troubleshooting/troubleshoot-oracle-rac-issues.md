---
url: https://docs.cloud.google.com/bare-metal/docs/troubleshooting/troubleshoot-oracle-rac-issues/
title: Troubleshoot Oracle RAC issues \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:32.925868+00:00
---

# Troubleshoot Oracle RAC issues  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/troubleshooting/troubleshoot-oracle-rac-issues/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot Oracle RAC issues

This page provides troubleshooting tips for issues related to Oracle RAC on Bare Metal Solution.

Check if your question or problem has already been addressed on the [Known issues and limitations](https://docs.cloud.google.com/bare-metal/docs/known-issues) page.

### SSH verification fails with OpenSSH error

SSH verification might fail with the following OpenSSH error:
    
    
    OpenSSH_6.7: ERROR [INS-06003] Failed to setup passwordless SSH connectivity During Grid Infrastructure Install
    

To resolve this issue, do the following:

  1. In the `/etc/ssh/sshd_config` file, add the following line:
         
         KexAlgorithms curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha1,diffie-hellman-group1-sha1
         

  2. Restart the `sshd` service to apply the changes.
         
         /etc/init.d/sshd restart
         




## SCP file copy taking too long

The SCP file copy with rekey operation might take too long to complete due to a Bare Metal Solution SSH daemon configuration issue.

To resolve this issue, do the following:

  1. On your Bare Metal Solution server, open the `sshd_config` file in edit mode.
         
         vi /etc/ssh/sshd_config
         

  2. In the `sshd_config` file, add following line. If the line already exists in the file, modify it as follows:
         
         ClientAliveInterval 420
         

  3. Restart the `sshd` service to apply the changes.
         
         /etc/init.d/sshd restart
         




## CRS `root.sh` or OCSSD fails with `No Network HB` error

CRS `root.sh` script fails with the following error if the node pings the IP address 169.254.169.254:
    
    
    has a disk HB, but no network HB
    

The IP address 169.254.169.254 is the Google Cloud metadata service which registers the instance in Google Cloud. If you block this IP address, the Google Cloud VM can't boot up. This in turn can interrupt the HAIP communication route causing the Bare Metal Solution RAC servers to experience HAIP communication issues.

To resolve this issue, you need to block the IP address or disable HAIP. The following example shows how to block IP address with `route` commands. The changes made by `route` statement are not persistent. Therefore, you need to modify the system startup scripts.

To resolve this issue, do the following:

  1. On all the nodes, run the following command before rerunning the `root.sh` script.
         
         /sbin/route add -host 169.254.169.254 reject
         

  2. Make the `rc` script executable.
         
         chmod +x /etc/rc.d/rc.local
         

  3. In the `/etc/rc.d/rc.local` file, add the following lines:
         
         /sbin/route add -host 169.254.169.254 reject
         
         Enable rc-local service
         systemctl status rc-local.service
         systemctl enable rc-local.service
         systemctl start rc-local.service
         




## Reboot process not responding

If your server is running Red Hat Linux, OVM, or SUSE Linux, and there are many LUNs attached to it, the reboot process might stop responding.

To resolve this issue, increase the default watchdog timeout value:

  1. Under `/etc/systemd`, create a folder named `system.conf.d`.

  2. In the folder, create a `*.conf` file. For example, `/etc/systemd/system.conf.d/kernel-reboot-workaround.conf`.

  3. In the `*.conf` file, add the following code:
         
         [Manager]
         
         RuntimeWatchdogSec=5min
         
         ShutdownWatchdogSec=5min
         




An alternative workaround is as follows:

  1. Open the `grub.cfg` file in edit mode.
         
         vi /etc/default/grub
         

  2. Remove the `quiet` parameter from the settings.

  3. Add the following after the parameter `GRUB_CMDLINE_LINUX`:
         
         acpi_no_watchdog DefaultTimeoutStartSec=900s DefaultTimeoutStopSec=900s
         

  4. Rebuild the `grub.cfg` file.
         
         grub2-mkconfig -o /boot/efi/EFI/redhat/grub.cfg
         




## Oracle Grid infrastructure 12c fails with `Rejecting connection` error

Oracle Grid infrastructure 12c installation might fail with the following error:
    
    
    Rejecting connection from node 2 as MultiNode RAC is not supported or certified in this Configuration.
    

This error occurs because the IP address 169.254.169.254 is forwarded to the local metadata service of a Compute Engine VM, making it look like the Bare Metal Solution host is a Compute Engine VM. Such a configuration might also leak the Compute Engine VM's private service account keys.

To resolve this issue, consider the security implications of your NAT configuration and limit external network access as much as possible. Do the following:

  * Block the access to the metadata service on your cloud VM:
        
        firewall-cmd --direct --add-rule ipv4 filter FORWARD 0 -d 169.254.169.254 -j REJECT --reject-with icmp-host-unreachable
        
        firewall-cmd --permanent --direct --add-rule ipv4 filter FORWARD 0 -d 169.254.169.254 -j REJECT --reject-with icmp-host-unreachable
        

  * Block access to the metadata service on the Bare Metal Solution host:
        
        firewall-cmd --direct --add-rule ipv4 filter OUTPUT 0 -d 169.254.169.254 -j REJECT --reject-with icmp-host-unreachable
        
        firewall-cmd --permanent --direct --add-rule ipv4 filter OUTPUT 0 -d 169.254.169.254 -j REJECT --reject-with icmp-host-unr
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
