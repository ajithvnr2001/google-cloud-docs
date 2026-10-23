---
url: https://docs.cloud.google.com/sap/docs/upgrade-suse-scale-up-to-angi/
title: Upgrade SAPHanaSR to SAPHanaSR-angi in a scale-up HA cluster on SLES \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:46.886280+00:00
---

# Upgrade SAPHanaSR to SAPHanaSR-angi in a scale-up HA cluster on SLES  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/upgrade-suse-scale-up-to-angi/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Upgrade SAPHanaSR to SAPHanaSR-angi in a scale-up HA cluster on SLES Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to upgrade the `SAPHanaSR` resource agent to the `SAPHanaSR` Advanced Next Generation Interface (`SAPHanaSR-angi`) resource agent in a SLES based scale-up high-availability (HA) cluster running on Google Cloud. 

`SAPHanaSR-angi` is the successor of `SAPHanaSR`. Also, from SLES for SAP 15 SP6, Google Cloud recommends that you use `SAPHanaSR-angi`. For information about this resource agent, including its benefits, see the SUSE page [What is `SAPHanaSR-angi`?](https://www.suse.com/c/what-is-saphanasr-angi/).

To illustrate the upgrade procedure, this guide assumes an SAP HANA scale-up HA system running on SLES for SAP 15 SP4, with SID `ABC`. This upgrade procedure is derived from the SUSE blog [How to upgrade to `SAPHanaSR-angi`](https://www.suse.com/c/how-to-upgrade-to-saphanasr-angi/).

**Important:** The `SAPHanaSR-angi` resource agent is a SUSE product. For any assistance for using this product, or for any additional information, you need to reach out to SUSE. For more information, see Get support.

## Before you begin

Before you upgrade from `SAPHanaSR` to `SAPHanaSR-angi` in a SLES based SAP HANA scale-up HA cluster, make sure that you're using the latest patch of one of the following OS versions: SLES 15 SP4 or later.

If you're using an earlier OS version, then you first need to update to the latest patch of one of these OS versions. Only the latest patch of these OS versions contain the `SAPHanaSR-upgrade-to-angi-demo` script provided by SUSE for this upgrade. The script is available in the `/usr/share/SAPHanaSR/samples` directory.

## Upgrade to the `SAPHanaSR-angi` resource agent in a scale-up cluster

To upgrade to the `SAPHanaSR-angi` resource agent in a SLES based SAP HANA scale-up HA cluster, complete the following steps:

  1. Prepare the instances for upgrade.
  2. Remove resource configurations from the cluster.
  3. Add resource configurations to the cluster.
  4. Verify the details of the HANA cluster attributes.



### Prepare the instances for upgrade

  1. On the primary instance of your SAP HANA HA system, install the `ClusterTools2` Linux package:
         
         zypper -y install ClusterTools2

#### Verify the package installation

Verify the installation of the `ClusterTools2` package:
         
         zypper info ClusterTools2

The output is similar to the following:
         
         Information for package ClusterTools2:
          --------------------------------------
          Repository     : SLE-Module-SAP-Applications15-SP4-Updates
          Name           : ClusterTools2
          Version        : 3.1.3-150100.8.12.1
          Arch           : noarch
          Vendor         : SUSE LLC <https://www.suse.com/>
          Support Level  : Level 3
          Installed Size : 340.1 KiB
          Installed      : Yes
          Status         : up-to-date
          Source package : ClusterTools2-3.1.3-150100.8.12.1.src
          Upstream URL   : http://www.suse.com
          Summary        : Tools for cluster management
          Description    :
              ClusterTools2 provides tools for setting up and managing a corosync/
              pacemaker cluster.
              There are some other commandline tools to make life easier.
              Starting with version 3.0.0 is support for SUSE Linux Enterprise Server 12.

  2. Copy the SUSE provided `SAPHanaSR-upgrade-to-angi-demo` demo script to `/root/bin`. This script performs the backup of configuration files and generates the commands required for the upgrade.

To copy the demo script to `/root/bin`:
         
         cp -p /usr/share/SAPHanaSR/samples/SAPHanaSR-upgrade-to-angi-demo /root/bin/
         cd /root/bin
         ls -lrt

The output is similar to the following example:
         
         ...
         -r--r--r-- 1 root root   157 Nov  8 14:45 global.ini_susTkOver
         -r--r--r-- 1 root root   133 Nov  8 14:45 global.ini_susHanaSR
         -r--r--r-- 1 root root   157 Nov  8 14:45 global.ini_susCostOpt
         -r--r--r-- 1 root root   175 Nov  8 14:45 global.ini_susChkSrv
         -r-xr-xr-x 1 root root 22473 Nov  8 14:45 **SAPHanaSR-upgrade-to-angi-demo**
         drwxr-xr-x 3 root root    26 Nov  9 07:50 crm_cfg

  3. On the secondary instance of your SAP HANA HA system, repeat steps 1-2.

  4. From either instance of your HA system, run the demo script:
         
         ./SAPHanaSR-upgrade-to-angi-demo --upgrade > upgrade-to-angi.txt

  5. Validate that the backup files are present:
         
         ls -l

The output is similar to the following example:
         
         /root/SAPHanaSR-upgrade-to-angi-demo.1736397409/*
         -rw-r--r-- 1 root   root     443 Dec 10 20:09 /root/SAPHanaSR-upgrade-to-angi-demo.1736397409/**20-saphana.sudo**
         -rwxr-xr-x 1 root   root   22461 May 14  2024 /root/SAPHanaSR-upgrade-to-angi-demo.1736397409/**SAPHanaSR-upgrade-to-angi-demo**
         -rw-r--r-- 1 root   root   28137 Jan  9 04:36 /root/SAPHanaSR-upgrade-to-angi-demo.1736397409/**cib.xml**
         -rw-r--r-- 1 root   root    3467 Jan  9 04:36 /root/SAPHanaSR-upgrade-to-angi-demo.1736397409/**crm_configure.txt**
         -rw-r--r-- 1 abcadm sapsys   929 Dec 10 20:09 /root/SAPHanaSR-upgrade-to-angi-demo.1736397409/**global.ini**




### Remove resource configurations from the cluster

  1. From either instance of your HA system, put the `SAPHana` and the `SAPHanaTopology` cluster resources in maintenance mode:
         
         cs_wait_for_idle -s 3 >/dev/null
         crm resource maintenance msl_SAPHana_ABC_HDB00 on
         cs_wait_for_idle -s 3 >/dev/null
         crm resource maintenance cln_SAPHanaTopology_ABC_HDB00 on
         cs_wait_for_idle -s 3 >/dev/null
         echo "property cib-bootstrap-options: stop-orphan-resources=false" | crm configure load update -

#### Verify the status of the cluster resources

To verify that the `SAPHana` and `SAPHanaTopology` resources:
         
         crm status

The output must show that the said resources are `unmanaged`:
         
         Cluster Summary:
          ...
          Full List of Resources:
            *  STONITH-sles-sp4-angi-vm1   (stonith:fence_gce):     Started sles-sp4-angi-vm2
            *  STONITH-sles-sp4-angi-vm2   (stonith:fence_gce):     Started sles-sp4-angi-vm1
            *  Resource Group: g-primary:
              *    rsc_vip_int-primary       (ocf::heartbeat:IPaddr2):        Started sles-sp4-angi-vm1
              *    rsc_vip_hc-primary        (ocf::heartbeat:anything):       Started sles-sp4-angi-vm1
            *  Clone Set: cln_SAPHanaTopology_ABC_HDB00 [rsc_SAPHanaTopology_ABC_HDB00] (unmanaged):
              *    rsc_SAPHanaTopology_ABC_HDB00     (ocf::suse:SAPHanaTopology):     Started sles-sp4-angi-vm1 **(unmanaged)**
              *    rsc_SAPHanaTopology_ABC_HDB00     (ocf::suse:SAPHanaTopology):     Started sles-sp4-angi-vm2 **(unmanaged)**
            *  Clone Set: msl_SAPHana_ABC_HDB00 [rsc_SAPHana_ABC_HDB00] (promotable, **unmanaged**):
              *    rsc_SAPHana_ABC_HDB00     (ocf::suse:SAPHana):     Master sles-sp4-angi-vm1 **(unmanaged)**
              *    rsc_SAPHana_ABC_HDB00     (ocf::suse:SAPHana):     Slave sles-sp4-angi-vm2 **(unmanaged)**

  2. On the primary instance of your HA system, remove the existing HA/DR provider hook configuration:
         
         grep "^\[ha_dr_provider_" /hana/shared/ABC/global/hdb/custom/config/global.ini
         su - abcadm -c "/usr/sbin/SAPHanaSR-manageProvider --sid=ABC --show --provider=SAPHanaSR" > /run/SAPHanaSR-upgrade-to-angi-demo.12915.global.ini.SAPHanaSR
         su - abcadm -c "/usr/sbin/SAPHanaSR-manageProvider --sid=ABC --reconfigure --remove /run/SAPHanaSR-upgrade-to-angi-demo.12915.global.ini.SAPHanaSR"
         rm /run/SAPHanaSR-upgrade-to-angi-demo.12915.global.ini.SAPHanaSR
         rm /run/SAPHanaSR-upgrade-to-angi-demo.12915.global.ini.suschksrv
         su - abcadm -c "hdbnsutil -reloadHADRProviders"
         grep "^\[ha_dr_provider_" /hana/shared/ABC/global/hdb/custom/config/global.ini
         cp /etc/sudoers.d/20-saphana /run/SAPHanaSR-upgrade-to-angi-demo.12915.sudoers.classic
         grep -v "abcadm.*ALL..NOPASSWD.*crm_attribute.*abc" /run/SAPHanaSR-upgrade-to-angi-demo.12915.sudoers.classic > /etc/sudoers.d/20-saphana
         cp /etc/sudoers.d/20-saphana /run/SAPHanaSR-upgrade-to-angi-demo.12915.sudoers.classic
         grep -v "abcadm.*ALL..NOPASSWD.*SAPHanaSR-hookHelper.*sid=ABC" /run/SAPHanaSR-upgrade-to-angi-demo.12915.sudoers.classic > /etc/sudoers.d/20-saphana
         rm /run/SAPHanaSR-upgrade-to-angi-demo.12915.sudoers.classic

  3. On the secondary instance of your HA system, repeat the preceding step to remove the existing HA/DR provider hook configuration.

  4. From either instance of your HA system, remove the configuration of the `SAPHana` resource agent:
         
         cibadmin --delete --xpath "//rsc_colocation[@id='col_saphana_ip_ABC_HDB00']"
         cibadmin --delete --xpath "//rsc_order[@id='ord_SAPHana_ABC_HDB00']"
         cibadmin --delete --xpath "//master[@id='msl_SAPHana_ABC_HDB00']"
         cs_wait_for_idle -s 3 >/dev/null
         crm resource refresh rsc_SAPHana_ABC_HDB00

#### Verify the status of the `SAPHana` resource agent

To verify that the `SAPHana` resource agent configuration is removed:
         
         crm status

The output must show that the said resource is `unmanaged`:
         
         Cluster Summary:
          ...
          Full List of Resources:
            * STONITH-sles-sp4-angi-vm1   (stonith:fence_gce):     Started sles-sp4-angi-vm2
            * STONITH-sles-sp4-angi-vm2   (stonith:fence_gce):     Started sles-sp4-angi-vm1
            * Resource Group: g-primary:
              * rsc_vip_int-primary       (ocf::heartbeat:IPaddr2):        Started sles-sp4-angi-vm1
              * rsc_vip_hc-primary        (ocf::heartbeat:anything):       Started sles-sp4-angi-vm1
            * Clone Set: cln_SAPHanaTopology_ABC_HDB00 [rsc_SAPHanaTopology_ABC_HDB00] **(unmanaged)** :
              * rsc_SAPHanaTopology_ABC_HDB00     (ocf::suse:SAPHanaTopology):     Started sles-sp4-angi-vm1 (unmanaged)
              * rsc_SAPHanaTopology_ABC_HDB00     (ocf::suse:SAPHanaTopology):     Started sles-sp4-angi-vm2 (unmanaged)

  5. From either instance of your HA system, remove the configuration of the `SAPHanaTopology` resource agent:
         
         cs_wait_for_idle -s 3 >/dev/null
         cibadmin --delete --xpath "//rsc_order[@id='ord_SAPHana_ABC_HDB00']"
         cibadmin --delete --xpath "//clone[@id='cln_SAPHanaTopology_ABC_HDB00']"
         cs_wait_for_idle -s 3 >/dev/null
         crm resource refresh rsc_SAPHanaTopology_ABC_HDB00

#### Verify the status of the `SAPHanaTopology` resource agent

To verify that the `SAPHanaTopology` resource agent configuration is removed:
         
         crm status

The output is similar to the following:
         
         Cluster Summary:
          * Stack: corosync
          * Current DC: sles-sp4-angi-vm1 (version 2.1.2+20211124.ada5c3b36-150400.4.20.1-2.1.2+20211124.ada5c3b36) - partition with quorum
          * Last updated: Wed Jan 29 03:30:36 2025
          * Last change:  Wed Jan 29 03:30:32 2025 by hacluster via crmd on sles-sp4-angi-vm1
          * 2 nodes configured
          * 4 resource instances configured
         
          Node List:
            * Online: [ sles-sp4-angi-vm1 sles-sp4-angi-vm2 ]
         
          Full List of Resources:
            * STONITH-sles-sp4-angi-vm1   (stonith:fence_gce):     Started sles-sp4-angi-vm2
            * STONITH-sles-sp4-angi-vm2   (stonith:fence_gce):     Started sles-sp4-angi-vm1
            * Resource Group: g-primary:
              * rsc_vip_int-primary       (ocf::heartbeat:IPaddr2):        Started sles-sp4-angi-vm1
              * rsc_vip_hc-primary        (ocf::heartbeat:anything):       Started sles-sp4-angi-vm1

  6. On the primary instance of your HA system, remove the other cluster properties:
         
         cs_wait_for_idle -s 3 >/dev/null
         crm_attribute --delete --type crm_config --name hana_abc_site_srHook_sles-sp4-angi-vm2
         crm_attribute --delete --type crm_config --name hana_abc_site_srHook_sles-sp4-angi-vm1
         cs_wait_for_idle -s 3 >/dev/null
         crm_attribute --node sles-sp4-angi-vm1 --name hana_abc_op_mode --delete
         crm_attribute --node sles-sp4-angi-vm1 --name lpa_abc_lpt --delete
         crm_attribute --node sles-sp4-angi-vm1 --name hana_abc_srmode --delete
         crm_attribute --node sles-sp4-angi-vm1 --name hana_abc_vhost --delete
         crm_attribute --node sles-sp4-angi-vm1 --name hana_abc_remoteHost --delete
         crm_attribute --node sles-sp4-angi-vm1 --name hana_abc_site --delete
         crm_attribute --node sles-sp4-angi-vm1 --name hana_abc_sync_state --lifetime reboot --delete
         crm_attribute --node sles-sp4-angi-vm1 --name master-rsc_SAPHana_ABC_HDB00 --lifetime reboot --delete
         crm_attribute --node sles-sp4-angi-vm2 --name lpa_abc_lpt --delete
         crm_attribute --node sles-sp4-angi-vm2 --name hana_abc_op_mode --delete
         crm_attribute --node sles-sp4-angi-vm2 --name hana_abc_vhost --delete
         crm_attribute --node sles-sp4-angi-vm2 --name hana_abc_site --delete
         crm_attribute --node sles-sp4-angi-vm2 --name hana_abc_srmode --delete
         crm_attribute --node sles-sp4-angi-vm2 --name hana_abc_remoteHost --delete
         crm_attribute --node sles-sp4-angi-vm2 --name hana_abc_sync_state --lifetime reboot --delete
         crm_attribute --node sles-sp4-angi-vm2 --name master-rsc_SAPHana_ABC_HDB00 --lifetime reboot --delete

  7. On the primary instance of your HA system, remove the `SAPHanaSR` package:
         
         cs_wait_for_idle -s 3 >/dev/null
         crm cluster run "rpm -e --nodeps 'SAPHanaSR'"

#### Verify the status of the cluster

To check the status of your HA cluster:
         
         crm status

The output is similar to the following example:
         
         Cluster Summary:
          ...
          Node List:
            * Online: [ sles-sp4-angi-vm1 sles-sp4-angi-vm2 ]
         
          Full List of Resources:
            * STONITH-sles-sp4-angi-vm1   (stonith:fence_gce):     Started sles-sp4-angi-vm2
            * STONITH-sles-sp4-angi-vm2   (stonith:fence_gce):     Started sles-sp4-angi-vm1
            * Resource Group: g-primary:
              * rsc_vip_int-primary       (ocf::heartbeat:IPaddr2):        Started sles-sp4-angi-vm1
              * rsc_vip_hc-primary        (ocf::heartbeat:anything):       Started sles-sp4-angi-vm1

  8. On the primary instance of your HA system, remove the `SAPHanaSR-doc` package:
         
         zypper remove SAPHanaSR-doc

  9. On the secondary instance of your HA system, remove the `SAPHanaSR-doc` package.




### Add resource configurations to the cluster

  1. From either instance of your HA system, install the `SAPHanaSR-angi` resource package manager:
         
         cs_wait_for_idle -s 3 >/dev/null
         crm cluster run "zypper --non-interactive in -l -f -y 'SAPHanaSR-angi'"
         crm cluster run "rpm -q 'SAPHanaSR-angi' --queryformat %{NAME}"
         hash -r

  2. On the primary instance of your HA system, add the HA/DR provider hook configuration:
         
         su - abcadm -c "/usr/bin/SAPHanaSR-manageProvider --sid=ABC --reconfigure --add /usr/share/SAPHanaSR-angi/samples/global.ini_susHanaSR"
         su - abcadm -c "/usr/bin/SAPHanaSR-manageProvider --sid=ABC --reconfigure --add /usr/share/SAPHanaSR-angi/samples/global.ini_susTkOver"
         su - abcadm -c "/usr/bin/SAPHanaSR-manageProvider --sid=ABC --reconfigure --add /usr/share/SAPHanaSR-angi/samples/global.ini_susChkSrv"
         su - abcadm -c "hdbnsutil -reloadHADRProviders"
         grep -A2 "^\[ha_dr_provider_" /hana/shared/ABC/global/hdb/custom/config/global.ini
         su - abcadm -c "/usr/bin/SAPHanaSR-manageProvider --sid=ABC --show --provider=SAPHanaSR"
         su - abcadm -c "/usr/bin/SAPHanaSR-manageProvider --sid=ABC --show --provider=suschksrv"
         echo "abcadm ALL=(ALL) NOPASSWD: /usr/bin/SAPHanaSR-hookHelper --sid=ABC *" >> /etc/sudoers.d/20-saphana
         echo "abcadm ALL=(ALL) NOPASSWD: /usr/sbin/crm_attribute -n hana_abc_*" >> /etc/sudoers.d/20-saphana
         sudo -l -U abcadm | grep -e crm_attribute -e SAPHanaSR-hookHelper

  3. On the secondary instance of your HA system, repeat the preceding step to add the HA/DR provider hook configuration.

  4. From either instance of your HA system, add the `SAPHanaTopology` resource agent configuration:
         
         cs_wait_for_idle -s 3 >/dev/null
         echo "
         #
         primitive rsc_SAPHanaTop_ABC_HDB00 ocf:suse:SAPHanaTopology op start interval=0 timeout=600 op stop interval=0 timeout=600 op monitor interval=50 timeout=600 params SID=ABC InstanceNumber=00
         #
         clone cln_SAPHanaTopology_ABC_HDB00 rsc_SAPHanaTop_ABC_HDB00 meta clone-node-max=1 interleave=true
         #
         " | crm configure load update -
         crm configure show cln_SAPHanaTopology_ABC_HDB00

#### Verify the status of the cluster

To check the status of your HA cluster:
         
         crm status

The output is similar to the following example:
         
         Cluster Summary:
          ...
            * Clone Set: cln_SAPHanaTopology_ABC_HDB00 [rsc_SAPHanaTop_ABC_HDB00]:
                 * Started: [ sles-sp4-angi-vm1 sles-sp4-angi-vm2 ]
         

  5. From either instance of your HA system, add `SAPHanaCon` as an unmanaged cluster resource:
         
         cs_wait_for_idle -s 3 >/dev/null
         echo "
         #
         primitive rsc_SAPHanaCon_ABC_HDB00 ocf:suse:SAPHanaController op start interval=0 timeout=3600 op stop interval=0 timeout=3600 op promote interval=0 timeout=900 op demote interval=0 timeout=320 op monitor interval=60 role=Promoted timeout=700 op monitor interval=61 role=Unpromoted timeout=700 params SID=ABC InstanceNumber=00 PREFER_SITE_TAKEOVER=true DUPLICATE_PRIMARY_TIMEOUT=7200 AUTOMATED_REGISTER=true meta maintenance=true
         #
         clone mst_SAPHanaCon_ABC_HDB00 rsc_SAPHanaCon_ABC_HDB00 meta clone-node-max=1 promotable=true interleave=true maintenance=true
         #
         order ord_SAPHanaTop_first Optional: cln_SAPHanaTopology_ABC_HDB00 mst_SAPHanaCon_ABC_HDB00
         #
         colocation col_SAPHanaCon_ip_ABC_HDB00 2000: g-primary:Started mst_SAPHanaCon_ABC_HDB00:Promoted
         #
         " | crm configure load update -
         crm configure show mst_SAPHanaCon_ABC_HDB00

#### Verify the status of the cluster

To check the status of your HA cluster:
         
         crm status

The output is similar to the following example:
         
         Cluster Summary:
         ...
          * Clone Set: cln_SAPHanaTopology_ABC_HDB00 [rsc_SAPHanaTop_ABC_HDB00]:
            * Started: [ sles-sp4-angi-vm1 sles-sp4-angi-vm2 ]
          * Clone Set: mst_SAPHanaCon_ABC_HDB00 [rsc_SAPHanaCon_ABC_HDB00] (promotable, **unmanaged**):
            * rsc_SAPHanaCon_ABC_HDB00  (ocf::suse:SAPHanaController):   Slave sles-sp4-angi-vm1 **(unmanaged)**
            * rsc_SAPHanaCon_ABC_HDB00  (ocf::suse:SAPHanaController):   Slave sles-sp4-angi-vm2 **(unmanaged)**

  6. From either instance of your HA system, add the HANA file system cluster resource:
         
         cs_wait_for_idle -s 3 >/dev/null
         echo "
         #
         primitive rsc_SAPHanaFil_ABC_HDB00 ocf:suse:SAPHanaFilesystem op start interval=0 timeout=10 op stop interval=0 timeout=20 on-fail=fence op monitor interval=120 timeout=120 params SID=ABC InstansceNumber=00
         #
         clone cln_SAPHanaFil_ABC_HDB00 rsc_SAPHanaFil_ABC_HDB00 meta clone-node-max=1 interleave=true
         #
         " | crm configure load update -
         crm configure show cln_SAPHanaFil_ABC_HDB00
         #
         clone cln_SAPHanaFil_ABC_HDB00 rsc_SAPHanaFil_ABC_HDB00 \
                meta clone-node-max=1 interleave=true

#### Verify the status of the cluster

To check the status of your HA cluster:
         
         crm status

The output is similar to the following example:
         
         Cluster Summary:
          ...
            * Clone Set: cln_SAPHanaTopology_ABC_HDB00 [rsc_SAPHanaTop_ABC_HDB00]:
              * Started: [ sles-sp4-angi-vm1 sles-sp4-angi-vm2 ]
            * Clone Set: mst_SAPHanaCon_ABC_HDB00 [rsc_SAPHanaCon_ABC_HDB00] (promotable, unmanaged):
              * rsc_SAPHanaCon_ABC_HDB00  (ocf::suse:SAPHanaController):   Slave sles-sp4-angi-vm1 (unmanaged)
              * rsc_SAPHanaCon_ABC_HDB00  (ocf::suse:SAPHanaController):   Slave sles-sp4-angi-vm2 (unmanaged)
            * Clone Set: cln_SAPHanaFil_ABC_HDB00 [rsc_SAPHanaFil_ABC_HDB00]:
              * Started: [ sles-sp4-angi-vm1 sles-sp4-angi-vm2 ]

  7. From either instance of your HA system, remove the HA cluster from maintenance mode:
         
         cs_wait_for_idle -s 3 >/dev/null
         crm resource refresh cln_SAPHanaTopology_ABC_HDB00
         cs_wait_for_idle -s 3 >/dev/null
         crm resource maintenance cln_SAPHanaTopology_ABC_HDB00 off
         cs_wait_for_idle -s 3 >/dev/null
         crm resource refresh mst_SAPHanaCon_ABC_HDB00
         cs_wait_for_idle -s 3 >/dev/null
         crm resource maintenance mst_SAPHanaCon_ABC_HDB00 off
         cs_wait_for_idle -s 3 >/dev/null
         crm resource refresh cln_SAPHanaFil_ABC_HDB00
         cs_wait_for_idle -s 3 >/dev/null
         crm resource maintenance cln_SAPHanaFil_ABC_HDB00 off
         cs_wait_for_idle -s 3 >/dev/null
         echo "property cib-bootstrap-options: stop-orphan-resources=true" | crm configure load update -

  8. Check the status of your HA cluster:
         
         cs_wait_for_idle -s 3 >/dev/null
         crm_mon -1r --include=failcounts,fencing-pending;echo;SAPHanaSR-showAttr;cs_clusterstate -i|grep -v "#"

The output is similar to the following example:
         
         Cluster Summary:
          * Stack: corosync
          * Current DC: sles-sp4-angi-vm1 (version 2.1.2+20211124.ada5c3b36-150400.4.20.1-2.1.2+20211124.ada5c3b36) - partition with quorum
          * Last updated: Wed Jan 29 05:21:05 2025
          * Last change:  Wed Jan 29 05:21:05 2025 by root via crm_attribute on sles-sp4-angi-vm1
          * 2 nodes configured
          * 10 resource instances configured
         
         Node List:
          * Online: [ sles-sp4-angi-vm1 sles-sp4-angi-vm2 ]
         
         Full List of Resources:
          * STONITH-sles-sp4-angi-vm1   (stonith:fence_gce):     Started sles-sp4-angi-vm2
          * STONITH-sles-sp4-angi-vm2   (stonith:fence_gce):     Started sles-sp4-angi-vm1
          * Resource Group: g-primary:
            * rsc_vip_int-primary       (ocf::heartbeat:IPaddr2):        Started sles-sp4-angi-vm1
            * rsc_vip_hc-primary        (ocf::heartbeat:anything):       Started sles-sp4-angi-vm1
          * Clone Set: cln_SAPHanaTopology_ABC_HDB00 [rsc_SAPHanaTop_ABC_HDB00]:
            * Started: [ sles-sp4-angi-vm1 sles-sp4-angi-vm2 ]
          * Clone Set: mst_SAPHanaCon_ABC_HDB00 [rsc_SAPHanaCon_ABC_HDB00] (promotable):
            * Masters: [ sles-sp4-angi-vm1 ]
            * Slaves: [ sles-sp4-angi-vm2 ]
          * Clone Set: cln_SAPHanaFil_ABC_HDB00 [rsc_SAPHanaFil_ABC_HDB00]:
            * Started: [ sles-sp4-angi-vm1 sles-sp4-angi-vm2 ]
         
         Migration Summary:
         
         Global cib-update dcid prim              sec               sid topology
         ------------------------------------------------------------------------
         global 0.68471.0  1    sles-sp4-angi-vm1 sles-sp4-angi-vm2 ABC ScaleUp
         
         Resource                      maintenance promotable
         -----------------------------------------------------
         mst_SAPHanaCon_ABC_HDB00      false       true
         cln_SAPHanaTopology_ABC_HDB00 false
         
         Site              lpt        lss mns               opMode    srHook srMode  srPoll srr
         ---------------------------------------------------------------------------------------
         sles-sp4-angi-vm1 1738128065 4   sles-sp4-angi-vm1 logreplay PRIM   syncmem PRIM   P
         sles-sp4-angi-vm2 30         4   sles-sp4-angi-vm2 logreplay        syncmem SOK    S
         
         Host              clone_state roles                        score site              srah version     vhost
         ----------------------------------------------------------------------------------------------------------------------
         sles-sp4-angi-vm1 PROMOTED    master1:master:worker:master 150   sles-sp4-angi-vm1 -    2.00.073.00 sles-sp4-angi-vm1
         sles-sp4-angi-vm2 DEMOTED     master1:master:worker:master 100   sles-sp4-angi-vm2 -    2.00.073.00 sles-sp4-angi-vm2




### Verify the details of the HANA cluster attributes

  * From either instance of your HA cluster, view the details of the HANA cluster attributes:
        
        SAPHanaSR-showAttr

The output is similar to the following example:
        
        Global cib-update dcid prim              sec               sid topology
        ------------------------------------------------------------------------
        global 0.98409.1  1    sles-sp4-angi-vm2 sles-sp4-angi-vm1 ABC ScaleUp
        
        Resource                      maintenance promotable
        -----------------------------------------------------
        mst_SAPHanaCon_ABC_HDB00      false       true
        cln_SAPHanaTopology_ABC_HDB00 false
        
        Site              lpt        lss mns               opMode    srHook srMode  srPoll srr
        ---------------------------------------------------------------------------------------
        sles-sp4-angi-vm1 30         4   sles-sp4-angi-vm1 logreplay SOK    syncmem SOK    S
        sles-sp4-angi-vm2 1742448908 4   sles-sp4-angi-vm2 logreplay PRIM   syncmem PRIM   P
        
        Host              clone_state roles                        score site              srah version     vhost
        ----------------------------------------------------------------------------------------------------------------------
        sles-sp4-angi-vm1 DEMOTED     master1:master:worker:master 100   sles-sp4-angi-vm1 -    2.00.073.00 sles-sp4-angi-vm1
        sles-sp4-angi-vm2 PROMOTED    master1:master:worker:master 150   sles-sp4-angi-vm2 -    2.00.073.00 sles-sp4-angi-vm2




## Get support

If you've purchased a PAYG license from Compute Engine for a SLES for SAP OS image, then you can get assistance from Cloud Customer Care to reach out to SUSE. For more information, see [How is support offered for Pay-As-You-Go (PAYG) SLES licenses on Compute Engine?](https://docs.cloud.google.com/compute/docs/images/premium/sles-faq#how_is_support_offered_for_pay-as-you-go_payg_sles_licenses_on)

For information about how to get support from Google Cloud, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
