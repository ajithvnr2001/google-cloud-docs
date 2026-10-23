---
url: https://docs.cloud.google.com/oracle/compute/gcnv-provision-gcnv-volumes/
title: Provision NetApp Volumes iSCSI volumes \u00a0|\u00a0 Oracle on Google Cloud Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:53.260910+00:00
---

# Provision NetApp Volumes iSCSI volumes  |  Oracle on Google Cloud Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/compute/gcnv-provision-gcnv-volumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Oracle on Google Cloud Compute ](https://docs.cloud.google.com/oracle/compute)
  * [ Guides ](https://docs.cloud.google.com/oracle/compute/overview)



Send feedback 

#  Provision NetApp Volumes iSCSI volumes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to provision NetApp Volumes iSCSI volumes for Oracle Database 26ai high availability.

To provision volumes, complete the following tasks:

  1. Create storage pools.
  2. Create host groups.
  3. Create NetApp Volumes iSCSI volumes.
  4. Configure iSCSI and multipath.
  5. Partition ASM devices.
  6. Format and mount `/u01` file system.



## Create storage pools

Create two Flex Unified storage pools, one in each database zone, to provide iSCSI volumes for the primary and standby hosts. Each database host uses volumes from its local zone's pool.

  1. Create two pools as per the following specifications:

Pool name | Zone | DB host | Service level | Type | Private services access  
---|---|---|---|---|---  
`oracle-pool-a` | `us-west1-a` | `oracdb1` (primary) | Flex | Unified | connected to `oracle-vpc`  
`oracle-pool-b` | `us-west1-b` | `oracdb2` (standby) | Flex | Unified | connected to `oracle-vpc`  
  
For capacity, sized for workload. Use custom provisioned throughput/IOPS when redo, backup, or restore exceeds default headroom (up to 5120 MiB/s or 160K IOPS per pool, per product limits).

For instructions, see [Create a storage pool](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/create-storage-pool).

  2. Before proceeding further, wait for both pools to reach `READY` status. Scale pool sizes to your database footprint (Step 5.3 sizes are examples).




Default-mode (this guide): Flex Unified pools use default mode (`--mode=default`). Create pools and iSCSI volumes with Google Cloud console or `gcloud netapp`.

## Create host groups

Create one host group per database host so each instance only sees its own volumes. The primary and standby must not share NetApp Volumes iSCSI volumes to maintain independent storage.

  1. Create a host group for `oracdb1` with the following specifications:

     * Name: `oracdb1-hg`
     * Region: `us-west1`
     * Type: **iSCSI initiator**
     * OS type: **Linux**
     * Hosts: paste the IQN from `oracdb1` (the value of /etc/iscsi/initiatorname.iscsi). This is the IQN that you captured in [Step: Capture the IQN of each database host](https://docs.cloud.google.com/oracle/compute/gcnv-provision-compute-instances#capture-IQN).
     * Description: "Oracle primary host oracdb1"
  2. Repeat for `oracdb2` with name `oracdb2-hg` with the IQN of `oracdb2`.




For instructions, see [Create a host group](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/host-groups/create-host-group).

**Note:** The Observer host requires no NetApp Volumes resources.

## Create NetApp Volumes iSCSI volumes

Create five NetApp Volumes iSCSI volumes for each database host — one for `/u01` and four for ASM backing devices. Each host's volumes must be created in its local zone's storage pool with its corresponding host group.

  1. Create the five volumes for `oracdb1` in `oracle-pool-a` with host group `oracdb1-hg`, and as per the following specifications: 

NetApp Volumes iSCSI volume | Size | Use | Multipath alias  
---|---|---|---  
ora_<host>_u01 | 100 GiB | /u01 GCNV iSCSI volume — Grid/Oracle homes, staging | /dev/mapper/ora_<host>_u01  
ora_<host>_data_01 | 50 GiB | ASM +DATA | /dev/mapper/ora_<host>_data_01  
ora_<host>_data_02 | 50 GiB | ASM +DATA (striped) | /dev/mapper/ora_<host>_data_02  
ora_<host>_arch_01 | 100 GiB | ASM +RECO | /dev/mapper/ora_<host>_arch_01  
ora_<host>_fra_01 | 100 GiB | ASM +FRA | /dev/mapper/ora_<host>_fra_01  
**Note:** The name of the volumes must only contain letters, numbers, and underscores. Hyphens are not allowed.

Minimal layout (validation only): two LUNs per host (`*_data`, `*_reco`) with `arch_01p1`→`+RECO` and `arch_01p2`→`+FRA` is acceptable for lab. Production uses five volumes.

  2. Create five volumes for `oracdb2` in `oracle-pool-b` with host group `oracdb2-hg` using the same specifications as that of the `oracdb1` volumes in the previous step.




For instructions, see [Create volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume#create_a_volume).

Record the following information for each pool:

  * iSCSI portal IPs: ISCSI_PORTAL_1, ISCSI_PORTAL_2 (primary pool portals on `oracdb1` and standby pool portals on `oracdb2` might differ).
  * Volume serial from the Google Cloud console. You need this in the next step.



## Configure iSCSI and multipath

Configure iSCSI and `device-mapper-multipath` on each database host to access the NetApp Volumes through both storage portal IPs.

Perform the following steps on `oracdb1` using the primary pool portal IPs. Then, repeat the steps on `oracdb2` using the standby pool's portal IPs.

If host egress is restricted, allow TCP port 3260 from each database host to its NetApp Volumes iSCSI portal IPs, in addition to the inter-VM TCP port 1521 from [Step: Configure VPC firewall](https://docs.cloud.google.com/oracle/compute/gcnv-provision-compute-instances#configure-vpc-firewall).

  1. Discover targets, sign in, and persist node startup.
         
         sudo iscsiadm --mode discovery --op update --type sendtargets --portal <ISCSI_PORTAL_1>
         sudo iscsiadm --mode discovery --op update --type sendtargets --portal <ISCSI_PORTAL_2>
         sudo iscsiadm --mode node --op update --name node.startup --value automatic
         sudo iscsiadm --mode node -l all
         sudo systemctl enable --now iscsid iscsi multipathd
         sudo iscsiadm --mode session         # expect 10 sessions (5 GCNV iSCSI volumes × 2 portals)
         sudo lsblk -o NAME,SIZE,WWN,VENDOR,MODEL

  2. After reboot, recheck before starting Oracle.
         
         sudo iscsiadm --mode session
         sudo multipath -ll

  3. Configure `device-mapper-multipath`.
         
         sudo tee /etc/multipath.conf >/dev/null <<'EOF'
         defaults {
             find_multipaths    yes
             user_friendly_names yes
         }
         blacklist {
             devnode "^(ram|raw|loop|fd|md|dm-|sr|scd|st)[0-9]*"
             devnode "^hd[a-z]"
             devnode "^cciss.*"
         }
         EOF
         
         sudo systemctl enable --now multipathd
         sudo multipath -ll

  4. Add host-discovered WWID aliases to `/etc/multipath.conf`. The `multipath.conf` doesn't expand shell variables. Discover WWIDs:
         
         sudo multipath -ll
         for dev in /dev/sd*; do
           [ -b "$dev" ] || continue
           printf '%s: ' "$dev"
           sudo /usr/lib/udev/scsi_id --whitelisted --device="$dev" 2>/dev/null || true
           echo
         done

  5. Append concrete aliases for that host to `/etc/multipath.conf`, and then `sudo systemctl restart multipathd`.

On `oracdb1`, append:
         
         multipaths {
             multipath { wwid       alias ora_oracdb1_u01     }
             multipath { wwid   alias ora_oracdb1_data_01 }
             multipath { wwid   alias ora_oracdb1_data_02 }
             multipath { wwid   alias ora_oracdb1_arch_01 }
             multipath { wwid    alias ora_oracdb1_fra_01  }
         }
         

  6. On `oracdb2`, use the same pattern with `ora_oracdb2_*` aliases, then:
         
         sudo systemctl restart multipathd
         ls -l /dev/mapper/ora_$(hostname -s)_*




## Partition ASM devices

Partition the four ASM backing devices (excluding `u01`) with one GPT partition each for ASM consumption. Then, configure `udev` rules for grid ownership.

Run the following steps on each database host:

  1. Partition the four ASM backing devices with GPT and verify the partitions.
         
         HOST=$(hostname -s)        # oracdb1 on the primary, oracdb2 on the standby
         for dev in /dev/mapper/ora_${HOST}_data_01 \
                     /dev/mapper/ora_${HOST}_data_02 \
                     /dev/mapper/ora_${HOST}_arch_01 \
                     /dev/mapper/ora_${HOST}_fra_01; do
           sudo parted -s "$dev" mklabel gpt
           sudo parted -s "$dev" mkpart primary 0% 100%
         done
         sudo partprobe
         sudo systemctl reload multipathd
         ls /dev/mapper/ora_${HOST}_*p1     # expect 4 partitions

  2. Configure `udev` rules to assign grid ownership and trigger the changes.
         
         HOST=$(hostname -s)
         sudo tee /etc/udev/rules.d/99-oracle-asm.rules >/dev/null <<'EOF'
         KERNEL=="dm-*", ENV{DM_UUID}=="part?-mpath-*", ENV{DM_NAME}=="ora_oracdb*_*p?", \
             OWNER="grid", GROUP="asmadmin", MODE="0660"
         EOF
         sudo udevadm control --reload-rules
         for part in /dev/mapper/ora_${HOST}_*p1; do
           dm=$(readlink -f "$part" | xargs basename)
           sudo udevadm trigger --action=change --name-match="/dev/${dm}"
         done
         sudo udevadm settle
         ls -lL /dev/mapper/ora_${HOST}_*p1    # grid:asmadmin 0660




## Format and mount `/u01` file system

Format the `ora_&lt;host&gt;_u01` iSCSI volume with XFS and mount it persistently using UUID in `/etc/fstab`. The `/u01` file system holds Grid home, Oracle home, and staging files.

  1. Format the multipath device with XFS and capture its UUID.
         
         HOST=$(hostname -s)
         U01_DEV=/dev/mapper/ora_${HOST}_u01
         ls -l "$U01_DEV"
         sudo mkfs.xfs -f "$U01_DEV"
         U01_UUID=$(sudo blkid -s UUID -o value "$U01_DEV")

  2. Add the UUID-based mount entry to `/etc/fstab` and mount the file system.
         
         sudo mkdir -p /u01
         echo "UUID=${U01_UUID} /u01 xfs defaults,_netdev,nofail,x-systemd.requires=iscsi.service,x-systemd.requires=multipathd.service,x-systemd.after=iscsi.service,x-systemd.after=multipathd.service 0 0" | sudo tee -a /etc/fstab
         sudo mount -a

  3. Create the directory structure with proper ownership for Grid and Oracle software.
         
         sudo mkdir -p /u01/app/oraInventory /u01/app/26ai/grid /u01/app/grid /u01/app/oracle/product/26ai/db_1 /u01/stage
         sudo chown -R grid:oinstall /u01/app/oraInventory /u01/app/26ai /u01/app/grid
         sudo chown -R oracle:oinstall /u01/app/oracle /u01/stage
         sudo chmod -R 775 /u01/app /u01/stage

  4. Reboot once and confirm `/u01` mounts before [Installing Oracle software](https://docs.cloud.google.com/oracle/compute/gcnv-install-oracle-software).




## What's next

  * [Install Oracle software](https://docs.cloud.google.com/oracle/compute/gcnv-install-oracle-software).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
