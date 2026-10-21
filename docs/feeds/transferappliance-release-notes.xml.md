---
url: https://docs.cloud.google.com/feeds/transferappliance-release-notes.xml
title: Transfer Appliance - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:26:25.548133+00:00
---

# Transfer Appliance - Release notes

> Source: https://docs.cloud.google.com/feeds/transferappliance-release-notes.xml

tag:google.com,2016:transferappliance-release-notesTransfer Appliance - Release notesGoogle Cloud Platform2023-12-18T00:00:00-08:00December 18, 2023tag:google.com,2016:transferappliance-release-notes#December_18_20232023-12-18T00:00:00-08:004.0 

### Feature

Transfer Appliance has introduced GA support for the data export appliance in the US. This enables you to place orders for exporting data from your Cloud Storage bucket to the appliance, which will then be shipped to you. See the [documentation](https://cloud.google.com/transfer-appliance/docs/4.0/data-export) for full details.

]]> October 31, 2023tag:google.com,2016:transferappliance-release-notes#October_31_20232023-10-31T00:00:00-07:004.0 

### Feature

Transfer Appliance now has alpha-level support in the gcloud CLI (gcloud alpha transfer appliances) allowing you to view in-progress transfer results, work with draft orders, clone existing orders, and more. See the [reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/transfer/appliances) for full details.

]]> October 09, 2023tag:google.com,2016:transferappliance-release-notes#October_09_20232023-10-09T00:00:00-07:004.0 

### Feature

'ta mount' and 'ta unmount' are command line tools offering the user the ability to mount their own NFS or CIFS shares onto the appliance. 

Learn more about [how to mount to an appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/transfer-data#ta-mount).

]]> September 27, 2023tag:google.com,2016:transferappliance-release-notes#September_27_20232023-09-27T00:00:00-07:004.0 

### Feature

New Appliance setup experience is released. Users can use the Google Cloud console to fully [set up permissions](https://cloud.google.com/transfer-appliance/docs/4.0/procedure-guide#project-setup-and-key-download) for the appliance and [receive the credentials](https://cloud.google.com/transfer-appliance/docs/4.0/procedure-guide#receive-appliance).

]]> March 08, 2023tag:google.com,2016:transferappliance-release-notes#March_08_20232023-03-08T00:00:00-08:004.0 

### Feature

`ta check` is a command line tool to detect and help fix configuration issues with [Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/diagnostics) and [Edge Appliance](https://docs.cloud.google.com/distributed-cloud/edge-appliance/docs/diagnostics).

]]> November 10, 2022tag:google.com,2016:transferappliance-release-notes#November_10_20222022-11-10T00:00:00-08:004.0 

### Feature

Users can now use SMB to transfer data by [enabling SMB file share](https://docs.cloud.google.com/transfer-appliance/docs/4.0/transfer-data#use_smb_to_transfer_data).

]]> September 14, 2022tag:google.com,2016:transferappliance-release-notes#September_14_20222022-09-14T00:00:00-07:004.0 

### Feature

Users can now review data that successfully transferred and failed to transfer in log files that auto-generate after a transfer is completed. Learn more about data verification log files [here](https://docs.cloud.google.com/transfer-appliance/docs/4.0/access-data).

]]> September 09, 2022tag:google.com,2016:transferappliance-release-notes#September_09_20222022-09-09T00:00:00-07:004.0 

### Feature

Remote Wipe is an optional step in the appliance return process that allows customers to erase data on their appliance before returning it to Google. 

Learn more about [how to wipe an appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/return-appliance).

]]> September 02, 2022tag:google.com,2016:transferappliance-release-notes#September_02_20222022-09-02T00:00:00-07:004.0 

### Feature

The lock/unlock feature allows you to securely move an appliance between data centers while ensuring that the data is encrypted and not accessible when the appliance comes in contact with third-party shipping services or people outside of your organization. 

Learn more about the guide [here](https://docs.cloud.google.com/transfer-appliance/docs/4.0/lock-unlock-userguide).

]]> August 17, 2022tag:google.com,2016:transferappliance-release-notes#August_17_20222022-08-17T00:00:00-07:004.0 

### Announcement

Edge Appliance is now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)).

Edge Appliance is a Google Cloud-managed, secure, high-performance appliance for edge locations. It provides local storage, ML inference, data transformation, and export.

[Learn more](https://docs.cloud.google.com/transfer-appliance/docs/edge/overview) or [request Edge Appliance now](https://docs.cloud.google.com/transfer-appliance/docs/edge/request).

]]> August 12, 2022tag:google.com,2016:transferappliance-release-notes#August_12_20222022-08-12T00:00:00-07:004.0 

### Feature

You can now place your Transfer Appliance into suspend mode before moving it to a new location. Suspend mode removes access to data on the device and suspends any transfers.

Learn more from the [Suspend](https://docs.cloud.google.com/transfer-appliance/docs/4.0/shutdown-appliance#suspend) section of the documentation.

]]> July 12, 2022tag:google.com,2016:transferappliance-release-notes#July_12_20222022-07-12T00:00:00-07:004.0 

### Feature

Transfer Appliance is now available in an additional size. The TA7 appliance offers up to 7TB of storage in a smaller form factor than our other appliances. It offers both online and offline transfer modes.

Learn more about the TA7 on the [Specifications](https://docs.cloud.google.com/transfer-appliance/docs/4.0/specifications) page, or [order an appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/order-appliance) from the Cloud console.

]]> June 29, 2022tag:google.com,2016:transferappliance-release-notes#June_29_20222022-06-29T00:00:00-07:004.0 

### Feature

Transfer Appliance now supports monitoring of the amount of data stored on your appliance, and whether online transfer is enabled, through Cloud Monitoring. See [Monitor Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/monitor-appliance) for details.

]]> June 16, 2022tag:google.com,2016:transferappliance-release-notes#June_16_20222022-06-16T00:00:00-07:004.0 

### Feature

You can now order Transfer Appliance from the Cloud console, as well as view, track, and manage your orders and appliances. For more info, see the [Order Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs/4.0/order-appliance) page.

]]> June 02, 2021tag:google.com,2016:transferappliance-release-notes#June_02_20212021-06-02T00:00:00-07:004.0 

### Feature

Transfer Appliance offers the [Transfer Appliance Cloud Setup Application](https://docs.cloud.google.com/transfer-appliance/docs/4.0/permissions-application). The application prompts for several settings, and uses the information you provide to configure your Google Cloud permissions, preferred Cloud Storage bucket, and Cloud KMS key for your transfer.

]]> March 30, 2021tag:google.com,2016:transferappliance-release-notes#March_30_20212021-03-30T00:00:00-07:004.0 

### Change

Transfer Appliance version 2.2 is deprecated and replaced by [Transfer Appliance version 4.0](https://docs.cloud.google.com/transfer-appliance/docs/4.0/index).

### Change

Transfer Appliance version 4.0 is now available to order in Singapore.

**2.2**

### Deprecated

Transfer Appliance version 2.2 is deprecated, and replaced by [Transfer Appliance version 4.0](https://docs.cloud.google.com/transfer-appliance/docs/4.0/index).

]]> November 04, 2020tag:google.com,2016:transferappliance-release-notes#November_04_20202020-11-04T00:00:00-08:004.0 

### Change

Transfer Appliance version 4.0 is released.

]]> April 11, 2019tag:google.com,2016:transferappliance-release-notes#April_11_20192019-04-11T00:00:00-07:002.0 & 2.2 

### Feature

Transfer Appliance documentation provides instructions for [using NFS to capture data from HDFS](https://docs.cloud.google.com/transfer-appliance/docs/2.0/capturing-data-hdfs-nfs-share).

]]> June 26, 2018tag:google.com,2016:transferappliance-release-notes#June_26_20182018-06-26T00:00:00-07:002.0 

### Feature

Disk status indicators are now accessible from the Settings menu in Transfer Appliance Web User Interface.

### Feature

While performing an [NFS capture](https://docs.cloud.google.com/transfer-appliance/docs/2.0/capturing-data-appliance), Transfer Appliance allows you to navigate to and select specific folders.

### Feature

The target path is now configurable while you're [rehydrating uploaded data](https://docs.cloud.google.com/transfer-appliance/docs/2.0/rehydrating-data#rehydrate-data).

### Feature

Transfer Appliance Capture Utility provides the option to [skip symbolic links to files](https://docs.cloud.google.com/transfer-appliance/docs/2.0/capturing-data-windows#skip-links).

### Feature

Users no longer need to manually create the staging bucket when [preparing to ship Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs/2.0/shipping-appliance) to the Google upload facility.

### Feature

[Rehydration job time to completion](https://docs.cloud.google.com/transfer-appliance/docs/2.0/monitoring-rehydration-jobs) is now displayed in the **Pending Jobs** list.

### Feature

[NFS share export](https://docs.cloud.google.com/transfer-appliance/docs/2.0/exporting-nfs-share) is now a supported data capture method.

### Change

Transfer Appliance Console User Interface now provides most features through **Data Capture** and **Settings** menus.

### Feature

Transfer Appliance allows [cancellation of data capture jobs](https://docs.cloud.google.com/transfer-appliance/docs/2.0/canceling-jobs).

### Feature

[Rehydrator job status](https://docs.cloud.google.com/transfer-appliance/docs/2.0/monitoring-rehydration-jobs) now displays rehydration job start and end time.

### Feature

[Serial data captures using multiple appliances](https://docs.cloud.google.com/transfer-appliance/docs/2.0/performing-serial-captures) is now supported, allowing you to continue data captures even if your data size exceeds the capacity of a single Transfer Appliance.

### Feature

To avoid early deletion charges, the Rehydrator uses [regional or multi-regional](https://docs.cloud.google.com/storage/docs/bucket-locations#key-concepts) storage class locations as appropriate when building component objects to rehydrate files greater than 100GB.

### Feature

[Network usage monitoring](https://docs.cloud.google.com/transfer-appliance/docs/2.0/monitoring-capture-jobs#monitor-network-usage) is now available through the Transfer Appliance Web User Interface.

### Change

[Password for SMTP configuration](https://docs.cloud.google.com/transfer-appliance/docs/2.0/preparing-to-unpack#get-smtp-info) is now optional, enabling email alerts to be sent via both authenticated and unauthenticated SMTP servers.

### Feature

Password for [Rehydrator SMTP configuration](https://docs.cloud.google.com/transfer-appliance/docs/2.0/launching-rehydrator) is now optional.

### Change

New communications protocol removes the need for connections from Transfer Appliance to workstations running the Capture Utility. See [Firewall port requirements](https://docs.cloud.google.com/transfer-appliance/docs/2.0/preparing-data-transfer#firewall-port-requirements).

### Feature

Transfer Appliance now allows you to perform a [factory reset](https://docs.cloud.google.com/transfer-appliance/docs/2.0/shipping-appliance#prepare-for-shipping) after you prepare an appliance for shipment to the Google upload facility.

### Feature

Transfer Appliance software now performs a [data integrity check](https://docs.cloud.google.com/transfer-appliance/docs/2.0/rehydrating-data#verify-rehydrated-data) at every stage of the data migration.

**2.0 & 2.2**

### Feature

Transfer Appliance Capture Utility now [preserves file metadata by default](https://docs.cloud.google.com/transfer-appliance/docs/2.0/capturing-data-windows#capture-metadata).

]]>
