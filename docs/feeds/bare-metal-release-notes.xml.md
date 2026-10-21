---
url: https://docs.cloud.google.com/feeds/bare-metal-release-notes.xml
title: Bare Metal Solution - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:35:29.628475+00:00
---

# Bare Metal Solution - Release notes

> Source: https://docs.cloud.google.com/feeds/bare-metal-release-notes.xml

tag:google.com,2016:bare-metal-release-notesBare Metal Solution - Release notesGoogle Cloud Platform2026-06-19T00:00:00-07:00June 19, 2026tag:google.com,2016:bare-metal-release-notes#June_19_20262026-06-19T00:00:00-07:00Feature 

Bare Metal Solution supports using Privileged Access Manager to provide temporary elevated access to a user to perform the critical evict operation that permanently deletes a storage resource. For more information, see [Evict a LUN or storage volume](https://docs.cloud.google.com/bare-metal/docs/bms-delete-storage-volume-resources#evict-storage-volume).

]]> December 29, 2025tag:google.com,2016:bare-metal-release-notes#December_29_20252025-12-29T00:00:00-08:00Deprecated 

Support for OS image `SLES12SP5SAP` on Bare Metal Solution is now deprecated. For information, see [Available OS images](https://docs.cloud.google.com/bare-metal/docs/bms-planning#available_os_images).

]]> April 08, 2025tag:google.com,2016:bare-metal-release-notes#April_08_20252025-04-08T00:00:00-07:00Change 

The command to connect to the interactive serial console of a server is changing on May 1, 2025. 

Old command:
    
    
    ssh -i SSH_KEY_ID -p 9600 PROJECT_ID.REGION.SERVER_NAME.USERNAME.bms=true@ssh-serialport.googleapis.com
    

New command: 
    
    
    ssh -i SSH_KEY_ID -p 9600 PROJECT_ID.REGION.SERVER_NAME.USERNAME.bms=true@\REGION\-ssh-serialport.googleapis.com
    

We recommend that you update your configurations by April 30, 2025 to avoid any disruptions. For instructions, see [Configure serial console](https://docs.cloud.google.com/bare-metal/docs/configure-serial-console).

]]> July 01, 2024tag:google.com,2016:bare-metal-release-notes#July_01_20242024-07-01T00:00:00-07:00Announcement 

Performance SSD storage is now available in all [Bare Metal Solution regions](https://docs.cloud.google.com/bare-metal/docs/bms-planning#regional_availability).

]]> June 10, 2024tag:google.com,2016:bare-metal-release-notes#June_10_20242024-06-10T00:00:00-07:00Deprecated 

Support for `BIOS_PUR043.37.14.021` (`TS24.02`) and `BIOS_PUR043.37.16.023` (`TS24.05`) firmware on Bare Metal Solution is now deprecated. For information, see [Available firmware](https://docs.cloud.google.com/bare-metal/docs/bms-planning#available_firmware_versions).

]]> May 28, 2024tag:google.com,2016:bare-metal-release-notes#May_28_20242024-05-28T00:00:00-07:00Feature 

You can now [order Bare Metal Solution storage and Partner Interconnect resources](https://docs.cloud.google.com/bare-metal/docs/order-bms-resources) on a 1 month commitment term. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

]]> May 21, 2024tag:google.com,2016:bare-metal-release-notes#May_21_20242024-05-21T00:00:00-07:00Feature 

You can now order Performance SSD storage for your Bare Metal Solution. For more information and availability in your region, see [Performance SSD storage](https://docs.cloud.google.com/bare-metal/docs/bms-planning#performance_ssd_storage). This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). To learn how to order Performance SSD storage, see [Order Bare Metal Solution resources](https://docs.cloud.google.com/bare-metal/docs/order-bms-resources).

]]> May 14, 2024tag:google.com,2016:bare-metal-release-notes#May_14_20242024-05-14T00:00:00-07:00Announcement 

You can now view information about upcoming maintenance events for Bare Metal Solution on [Upcoming maintenance events](https://docs.cloud.google.com/bare-metal/docs/upcoming-maintenance-events) page.

]]> May 02, 2024tag:google.com,2016:bare-metal-release-notes#May_02_20242024-05-02T00:00:00-07:00Feature 

You can now [set up Ops Agent on your Bare Metal Solution server](https://docs.cloud.google.com/bare-metal/docs/view-infrastructure-metrics) to view Bare Metal Solution metrics. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

### Feature

Bare Metal Solution now supports Oracle Linux 9. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Operating systems](https://docs.cloud.google.com/bare-metal/docs/bms-planning#operating_systems) and [Change the OS for a server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#change-os-for-server).

]]> March 20, 2024tag:google.com,2016:bare-metal-release-notes#March_20_20242024-03-20T00:00:00-07:00Feature 

You can now [create and manage VRFs](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#manage_vrfs) for the networks in your Bare Metal Solution environment. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

]]> February 12, 2024tag:google.com,2016:bare-metal-release-notes#February_12_20242024-02-12T00:00:00-08:00Feature 

You can now select the pod for your Bare Metal Solution resources through the [Google Cloud console intake form](https://docs.cloud.google.com/bare-metal/docs/bms-deploy#use_the_console_intake_form_to_enter_your_selections). This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

]]> February 06, 2024tag:google.com,2016:bare-metal-release-notes#February_06_20242024-02-06T00:00:00-08:00Feature 

You can now [view the details of the OS of your Bare Metal Solution server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#view-os-details). This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

]]> December 09, 2023tag:google.com,2016:bare-metal-release-notes#December_09_20232023-12-09T00:00:00-08:00Feature 

You can now set up [encryption keys](https://docs.cloud.google.com/bare-metal/docs/bms-encryption-keys) and [SSH keys](https://docs.cloud.google.com/bare-metal/docs/bms-ssh-keys) for your Bare Metal Solution server while provisioning or reimaging it. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

]]> October 02, 2023tag:google.com,2016:bare-metal-release-notes#October_02_20232023-10-02T00:00:00-07:00Feature 

You can now use Bare Metal Solution's self-service functionality to order your resources after executing a one-time Order Form. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Order Bare Metal Solution resources](https://docs.cloud.google.com/bare-metal/docs/order-bms-resources).

]]> September 22, 2023tag:google.com,2016:bare-metal-release-notes#September_22_20232023-09-22T00:00:00-07:00Feature 

You can now view the pod for your Bare Metal Solution [servers](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#view-servers), [networks](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#view-networks-in-your-bare-metal-solution-environment), [volumes](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#view-storage-in-your-bare-metal-solution-environment), and [NFS Shares](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#view-nfs-file-storage-in-your-bare-metal-solution-environment). This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

]]> September 14, 2023tag:google.com,2016:bare-metal-release-notes#September_14_20232023-09-14T00:00:00-07:00Feature 

You can now [view the status of your server activity](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#view-servers) in the Google Cloud console. it informs you if there's an issue with your Bare Metal Solution infrastructure. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

### Feature

[Observability for storage volumes](https://docs.cloud.google.com/bare-metal/docs/view-infrastructure-metrics#view_storage_volume_and_lun_metrics) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

]]> August 30, 2023tag:google.com,2016:bare-metal-release-notes#August_30_20232023-08-30T00:00:00-07:00Feature 

You can now view and respond to [maintenance events](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance-process) through Google Cloud console. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Manage maintenance events](https://docs.cloud.google.com/bare-metal/docs/manage-maintenance-events).

]]> July 14, 2023tag:google.com,2016:bare-metal-release-notes#July_14_20232023-07-14T00:00:00-07:00Change 

To create a client network, the [Google Cloud console intake form](https://docs.cloud.google.com/bare-metal/docs/bms-deploy#use_the_console_intake_form_to_enter_your_selections) now accepts VLAN attachment names and project number instead of pairing keys if your VLAN attachments are in a different project.

]]> June 20, 2023tag:google.com,2016:bare-metal-release-notes#June_20_20232023-06-20T00:00:00-07:00Feature 

You can now rename your Bare Metal Solution resources, including [servers](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#rename-server), [networks](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#rename-network), [storage volumes](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#rename-storage-volume), and [NFS shares](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#rename-nfs-volume). This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

### Feature

You can now [view storage volume and LUN metrics](https://docs.cloud.google.com/bare-metal/docs/view-infrastructure-metrics#view_storage_volume_and_lun_metrics) in the Google Cloud console. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

]]> April 11, 2023tag:google.com,2016:bare-metal-release-notes#April_11_20232023-04-11T00:00:00-07:00Feature 

You can now skip the cooling-off period while deleting a LUN or a storage volume. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Delete LUNs from a storage volume](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#delete-luns-from-storage-volume) and [Delete a storage volume](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#delete-storage-volume).

]]> March 31, 2023tag:google.com,2016:bare-metal-release-notes#March_31_20232023-03-31T00:00:00-07:00Feature 

You can now [view Bare Metal Solution infrastructure metrics](https://docs.cloud.google.com/bare-metal/docs/view-infrastructure-metrics) in the Google Cloud console. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

]]> March 23, 2023tag:google.com,2016:bare-metal-release-notes#March_23_20232023-03-23T00:00:00-07:00Announcement 

You can now provision multiple storage volumes to attach to the existing servers in a single configuration request through [Google Cloud console intake form](https://docs.cloud.google.com/bare-metal/docs/bms-deploy#use_the_console_intake_form_to_enter_your_selections).

]]> March 17, 2023tag:google.com,2016:bare-metal-release-notes#March_17_20232023-03-17T00:00:00-07:00Feature 

You can now use the [interactive serial console](https://docs.cloud.google.com/bare-metal/docs/troubleshooting/configure-serial-console) to access your Bare Metal Solution servers. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

]]> December 15, 2022tag:google.com,2016:bare-metal-release-notes#December_15_20222022-12-15T00:00:00-08:00Announcement 

Enhancements to Bare Metal Solution resource management for SAP HANA–For Bare Metal Solution environments running SAP HANA, you can now use the Google Cloud console, gcloud CLI, and API to view and manage your Bare Metal Solution servers, storage, and networks.

For more information, see [Maintaining your Bare Metal Solution environment](https://docs.cloud.google.com/sap/docs/sap-hana-on-bms-deployment#maintain_bms_environment) in the **SAP HANA on Bare Metal Solution deployment guide**.

]]> December 09, 2022tag:google.com,2016:bare-metal-release-notes#December_09_20222022-12-09T00:00:00-08:00Feature 

Operating systems updates for Bare Metal Solution servers–The following OS is now supported on general-purpose servers:

  * Red Hat Enterprise Linux (RHEL) 8.4



Other formatting revisions have been added to the [Bare Metal Solution operating systems page](https://docs.cloud.google.com/bare-metal/docs/bms-planning#linux) and the [SAP HANA on Bare Metal Solution operating systems page](https://docs.cloud.google.com/sap/docs/sap-hana-on-bms-planning#hana-cert-table-oss) to make them easier to use.

]]> November 11, 2022tag:google.com,2016:bare-metal-release-notes#November_11_20222022-11-11T00:00:00-08:00Feature 

New firmware version for Bare Metal Solution servers--The following is the latest firmware version available:

  * TS54



For more information about the features of TS54 firmware, see [Firmware](https://docs.cloud.google.com/bare-metal/docs/bms-planning#firmware).

]]> November 09, 2022tag:google.com,2016:bare-metal-release-notes#November_09_20222022-11-09T00:00:00-08:00Feature 

Enhancements to Bare Metal Solution resource management–Adds the following self-service functionality:

  * [Manage networks](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#manage_networks)–You can create, attach, detach, and delete networks. You can also add, update, and delete VLAN attachments.
  * [Manage boot volume snapshots](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#manage_boot_volume_snapshots)–You can create, delete, and restore boot volume snapshots. 
  * [Manage NFS file storage](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#manage_nfs_file_storage)–You can create, update, and delete NFS storage volumes.
  * Advanced networking–You can [add connections to multiple networks on a single server](https://docs.cloud.google.com/bare-metal/docs/bms-deploy#use_the_console_intake_form_to_enter_your_selections). You can now [view advanced networking information](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#view-advanced-networking-info) through the Google Cloud console too. 
  * Labels–You can organize your Bare Metal Solution resources by using labels. You can add labels to [servers](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#organize-servers-using-labels), [networks](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#organize-networks-using-labels), [storage volumes](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#organize-storage-volume-using-labels), and [NFS file storage](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#organize-nfsShares-using-labels). 
  * [Manage the power state of servers](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#restart_a_bare_metal_solution_server)–You can turn power on and off for your server and restart your server. You can also [check the status of a server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#check_the_status_of_a_server).

]]> August 22, 2022tag:google.com,2016:bare-metal-release-notes#August_22_20222022-08-22T00:00:00-07:00Feature 

New operating systems for Bare Metal Solution servers--The following OSes are now supported:

  * Red Hat Enterprise Linux (RHEL) 8.5
  * Oracle Linux 8.5



### Deprecated

The following operating systems are no longer supported on Bare Metal Solution servers:

  * Oracle Linux 8.4
  * RHEL for SAP Solutions 7.6
  * RHEL for SAP Solutions 7.7

]]> July 29, 2022tag:google.com,2016:bare-metal-release-notes#July_29_20222022-07-29T00:00:00-07:00Feature 

Enhancements to [Bare Metal Solution resource management](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#manage_resources_in_your_environment)–Adds the following functionality:

  * [Change the operating system for a Bare Metal Solution server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#change-os-for-server)
  * [Enable hyperthreading on a Bare Metal Solution server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#enable-hyperthreading-on-server)
  * [View advanced networking information](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#view-advanced-networking-info)
  * [Implement IP address management](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#implement-ip-address-management)
  * [Provision storage volume resources](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#provision-storage-volume-in-your-bare-metal-solution-environment)
  * [Remove storage volume resources](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#remove_storage_volume_resources_in_a_environment)



### Change

API for long-running operations:

The API for [long-running operations](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#view_the_status_of_a_long-running_operation) has changed from v1 to v2.

]]> June 15, 2022tag:google.com,2016:bare-metal-release-notes#June_15_20222022-06-15T00:00:00-07:00Feature 

[Advanced networking capabilities for Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs/bms-planning#choose_standard_networking_or_explore_advanced_networking_options)–Enables you to use the following features:

  * Add multiple VLANs on the same bonded server interface.
  * Configure multiple VLAN attachments over a Partner Interconnect connection to your Bare Metal Solution environment.
  * Connect the Bare Metal Solution environment to more than one Virtual Private Cloud (VPC) in your Google Cloud project.
  * Use network templates to enable a flexible network design of your choice, such as active/active and active/backup, to meet your needs for high availability, redundancy, and load balancing.

]]>
