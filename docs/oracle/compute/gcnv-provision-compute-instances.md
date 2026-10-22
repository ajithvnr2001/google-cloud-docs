---
url: https://docs.cloud.google.com/oracle/compute/gcnv-provision-compute-instances/
title: Provision Compute Engine instances \u00a0|\u00a0 Oracle on Google Cloud Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:52.372105+00:00
---

# Provision Compute Engine instances  |  Oracle on Google Cloud Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/compute/gcnv-provision-compute-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Oracle on Google Cloud Compute ](https://docs.cloud.google.com/oracle/compute)
  * [ Guides ](https://docs.cloud.google.com/oracle/compute/overview)



Send feedback 

#  Provision Compute Engine instances Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to provision Compute Engine instances for Oracle Database deployment using Google Cloud NetApp Volumes.

To provision Compute Engine instances to host Oracle Database, complete the following tasks:

  1. Create the Compute Engine instances.
  2. Configure VPC firewall.
  3. Configure hostname, DNS, and `/etc/hosts`.
  4. Prepare the operating system on DB hosts only.
  5. Capture the IQN of each database host.



## Create the Compute Engine instances

Create the following three Compute Engine instances in different zones of the same region (zonal failure isolation).

VM | Zone | Machine type | Boot disk | Network | Purpose  
---|---|---|---|---|---  
`oracdb1` | `us-west1-a` | n4-highmem-8 (sample) or c4-standard-* | OL 10, 50 GB Hyperdisk Balanced (OS only) | `oracle-vpc` or `oracle-subnet`, gVNIC | Primary database  
`oracdb2` | `us-west1-b` | Same as primary | OL 10, 50 GB Hyperdisk Balanced (OS only) | Same | Standby database  
`oradg-obs` | `us-west1-c` | e2-medium | OL 10, 20 GB Hyperdisk Balanced | Same | Fast-Start Failover Observer (Instant Client only)  
  
For more information, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

While creating the instances, consider the following:

  * Network tier: Select **Premium** when latency or egress (>~200 GiB/month) matters and **Standard** for lower TCO in dev/test.
  * Security: Enable **Secure Boot** , **vTPM** , and **Integrity monitoring** on all three instances.
  * Storage: the boot disk holds only the operating system. `/u01`, Grid/DB homes, staging, and all ASM data use NetApp Volumes iSCSI volumes.

**Note:** Don't attach a separate Compute Engine data disk for `/u01`.



## Configure VPC firewall

Configure VPC firewall to allowlist TCP port 1521 between all three instances for Oracle Net redo transport and Observer connectivity. Missing rules break Oracle Data Guard replication.

  1. [Create VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls#creating_firewall_rules) with the following specifications:

     * Name: `allow-oracle-net-dbhosts`
     * Network: `oracle-vpc`
     * Direction of traffic: `Ingress`
     * Action on match: `Allow`
     * Sources: three `/32` IPs, TCP 1521.

You can mirror egress if required.

  2. To validate connectivity from each instance, run the following commands from each Compute Engine instance toward each peer IP:
         
         sudo dnf install -y nmap-ncat
         for tgt in <oracdb1-ip> <oracdb2-ip> <oradg-obs-ip>; do
           nc -zv -w 5 "$tgt" 22
           nc -zv -w 5 "$tgt" 1521
         done

Port | Expected output | Meaning  
---|---|---  
22 | Connected | SSH path works  
1521 | Connection refused | Firewall open; Grid listener starts in Step 6.1.5 (static DG entries in Step 8.3)  
Either | Timeout | Fix firewall or routing  



## Configure hostname, DNS, and `/etc/hosts`

On all three Compute Engine instances, configure the hostname and DNS resolution so that the forward and reverse name resolution works for Oracle Net, the Broker, and the Observer.

  1. Set the hostname and add `/etc/hosts` entries on all three instances.

Substitute the Compute Engine instance internal IP addresses and run the following commands. You can retrieve the internal IP addresses from the Google Cloud console by going to the **Compute Engine** > **VM instances** list, and then looking at **Internal IP** column.
         
         # Run on each VM, substituting the local short name (oracdb1, oracdb2, oradg-obs)
         sudo hostnamectl set-hostname HOSTNAME.example.internal
         
         # Run on every instance
         sudo tee -a /etc/hosts >/dev/null <<EOF
         # Oracle Data Guard peers + FSFO Observer
         <oracdb1-ip>    oracdb1.example.internal    oracdb1
         <oracdb2-ip>    oracdb2.example.internal    oracdb2
         <oradg-obs-ip>  oradg-obs.example.internal  oradg-obs
         EOF

  2. Validate name resolution from each instance.
         
         ping -c 1 oracdb1 && ping -c 1 oracdb2 && ping -c 1 oradg-obs




## Prepare the operating system on DB hosts only

Prepare the OS on `oracdb1` and `oracdb2` for Oracle Database 26ai by installing the preinstall package, creating users and groups, installing iSCSI and multipath packages, and configuring the iSCSI initiator.

  1. Outbound HTTPS to `yum.oracle.com` (Cloud NAT or internal mirror on private subnets).

  2. Install the Oracle Preinstall package on both `oracdb1` and `oracdb2`.
         
         sudo dnf install -y oracle-ai-database-preinstall-26ai \
           || sudo dnf install -y oracle-database-preinstall-26ai \
           || sudo dnf install -y oracle-database-preinstall-23ai

  3. Create the grid user, ASM groups, and add the `oracle` user to the ASM groups.
         
         sudo groupadd -g 54327 asmadmin; sudo groupadd -g 54328 asmdba; sudo groupadd -g 54329 asmoper
         sudo useradd -u 54322 -g oinstall -G dba,oper,asmadmin,asmdba,asmoper grid
         sudo passwd -l grid; sudo passwd -l oracle
         sudo usermod -a -G asmdba,asmadmin oracle

  4. Install iSCSI, multipath, and JDK packages.
         
         sudo dnf install -y iscsi-initiator-utils device-mapper-multipath sg3_utils java-21-openjdk-headless libxcrypt-compat

  5. Verify THP and time synchronization.
         
         cat /sys/kernel/mm/transparent_hugepage/enabled   # expect [never]
         timedatectl; chronyc tracking

  6. Configure SELinux, firewall, and iSCSI initiator settings, and then reboot.

**Note:** Security posture (OL 10): The following commands set SELinux to permissive and disable `firewalld`. This is a minimal lab posture only. For hardened SELinux and firewall configuration, consult your organization's security baseline.
         
         sudo setenforce 0
         sudo sed -i 's/^SELINUX=.*/SELINUX=permissive/' /etc/selinux/config
         sudo systemctl disable --now firewalld
         
         sudo cp -n /etc/iscsi/iscsid.conf /etc/iscsi/iscsid.conf.orig
         sudo sed -i '/^[#[:space:]]*node\.session\.timeo\.replacement_timeout/d' /etc/iscsi/iscsid.conf
         echo "node.session.timeo.replacement_timeout = 120" | sudo tee -a /etc/iscsi/iscsid.conf
         sudo systemctl enable --now iscsid
         
         sudo reboot




## Capture the IQN of each database host

After the reboot, capture the iSCSI initiator name (IQN) of each database host. You need these IQNs later to create the NetApp Volumes host groups.

  1. Copy the IQN from `oracdb1` and note it somewhere safe.
         
         sudo cat /etc/iscsi/initiatorname.iscsi
         # InitiatorName=iqn.1994-05.com.redhat:abc123def456

  2. Repeat the previous step for `oracdb2`, and note its IQN.




Use one host group per host so that a single host's reboot or IQN regeneration cannot affect another host's NetApp Volumes iSCSI volume visibility.

Cloned instances: If both hosts share the same IQN, regenerate on `oracdb2`:

  1. Stop `iscsi`
  2. Clear `/var/lib/iscsi/nodes/*`
  3. New `InitiatorName` in `/etc/iscsi/initiatorname.iscsi`
  4. Restart `iscsi`



## What's next

  * [Provision NetApp Volumes iSCSI volumes](https://docs.cloud.google.com/oracle/compute/gcnv-provision-gcnv-volumes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
