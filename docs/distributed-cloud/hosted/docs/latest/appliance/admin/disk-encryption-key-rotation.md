---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/disk-encryption-key-rotation/
title: Rotate disk encryption keys \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:43.115507+00:00
---

# Rotate disk encryption keys  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/disk-encryption-key-rotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Rotate disk encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped appliance uses the Linux Unified Key Setup (LUKS) to encrypt data on disks when external HSM is not provided. A RAID5 array is created on top of the 4 data drives, and a single LUKS device is created on top of the RAID5 array. The LUKS KEK is randomly generated and can be rotated.

This document describes the steps to rotate the LUKS KEK that must be performed for:

  * regularly scheduled KEK rotation.
  * KEK exposure.

**Note:** Rotate the exposed KEK as soon as possible.

## Before you begin

Complete the following steps:

  1. Verify that you meet the [laptop prerequisites](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/laptop).
  2. Ensure that you can sign in to the three nodes as root user.



## Rotate KEK

The Google Distributed Cloud (GDC) air-gapped appliance system utilizes a two-node NetApp ONTAP Select (OTS) cluster deployed on nodes bm01 and bm02 (typically without GPUs). Each node possesses 4 dedicated data drives configured as a RAID5 array for enhanced redundancy. A single LUKS encrypted device is layered on top of each RAID5 array to ensure data security.

The LUKS encryption KEK is stored on the boot disk located in `/etc/luks`. Rotating the LUKS KEK necessitates rotating the LUKS encryption on both nodes to maintain security across the cluster. To perform a regular KEK rotation or if the KEK is exposed, repeat the following steps on both bm01 and bm02:

  1. Sign in to the node as root user.

  2. Make sure the RAID device exists, and get the `RAID_DEVICE` full path.
         
         ll /dev/md
         

  3. Make sure the old LUKS key file exists, and get the `OLD_KEY` full path.
         
         ll /etc/luks
         

  4. Add the old KEK to key slot 1, so that both key slot 0 and 1 have the same KEK.
         
         cryptsetup luksAddKey RAID_DEVICE OLD_KEY --key-slot 1 --key-file OLD_KEY
         

Replace `RAID_DEVICE` and `OLD_KEY` with the paths from the previous steps.

  5. Remove the old KEK from key slot 0.
         
         cryptsetup luksKillSlot RAID_DEVICE 0 --key-file OLD_KEY
         

  6. Generate a new KEK, and store it in the new key file `NEW_KEY`.
         
         dd if=/dev/urandom of=NEW_KEY bs=512 count=1
         chmod u=r,go-rwx NEW_KEY
         

Replace `NEW_KEY` with the full path to the new key file.

  7. Add the new KEK to key slot 0.
         
         cryptsetup luksAddKey RAID_DEVICE NEW_KEY --key-slot 0 --key-file OLD_KEY
         

  8. Set persistent config to open or close the LUKS device on machine boot or shutdown.
         
         DEVICE_UUID=$(cryptsetup luksUUID RAID_DEVICE)
         echo "luksrd5 UUID=${DEVICE_UUID} NEW_KEY luks,discard" > /etc/crypttab
         

  9. Remove the old KEK from key slot 1.
         
         cryptsetup luksKillSlot RAID_DEVICE 1 --key-file NEW_KEY
         

  10. Verify the new KEK is working.
         
         cryptsetup luksDump --dump-master-key RAID_DEVICE --key-file NEW_KEY
         

  11. Verify the old KEK is not working anymore.
         
         cryptsetup luksDump --dump-master-key RAID_DEVICE --key-file OLD_KEY
         

  12. Remove the old KEK.
         
         rm OLD_KEY
         




If a node is rebooted before the rotation completes, the LUKS device can still be opened after boot. You can resume the steps after the node is back.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
