---
url: https://docs.cloud.google.com/filestore/docs/known-issues/
title: Known issues \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:09.477318+00:00
---

# Known issues  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

Filestore has the following known issues.

## Filestore instances and clients can't have an IP address from the `172.17.0.0/16` subnet range

Filestore instances use the `172.17.0.0/16` address range for internal components. As a result, the following limitations apply:

  * Clients with an IP address from the `172.17.0.0/16` range can't connect to Filestore instances. 

**Note:** This limitation doesn't apply when using Private Service Connect.
  * You can't create a Filestore instance with a reserved IP range that overlaps with the range `172.17.0.0/16`.




## Slow response on Windows NFS clients

On some Windows NFS clients, it can take 20+ seconds to create a folder or delete files. To improve client response, use the following procedure to create a Windows firewall rule to block network traffic to the ports used by NetBIOS and SMB, usually ports 445 and 139.

  1. Open the **Windows Firewall with Advanced Security** snap-in in the Microsoft Management Console.
  2. In the left-hand pane, click **Outbound Rules**.
  3. In the right-hand **Actions** pane, click **New Rule**.
  4. In the **New Outbound Rule Wizard** , select the **Port** radio button and then click **Next**.
  5. Select the **TCP** radio button, select the **Specific Remote ports** radio button, and then type **445, 139** in the field next to the **Specific Remote ports** radio button. Click **Next**.
  6. Select the **Block the connection** radio button and then click **Next**.
  7. Select the **Domain** , **Private** , and **Public** checkboxes, and then click **Next**.
  8. Type a name for the firewall rule, and then click **Finish**.



## No quota for a particular service tier in a particular region

If a particular region shows a default capacity quota of 0 for a particular service tier, you can't create a Filestore instance of that tier until quota is increased.

To fix this issue, [request additional quota](https://docs.cloud.google.com/filestore/docs/requesting-quota-increases).

## Copy data between Cloud Storage and Filestore

Copying data from Cloud Storage to a Filestore instance using `gcloud` can be slow. For detailed information on how to improve performance, see [Improve performance across Google Cloud resources](https://docs.cloud.google.com/filestore/docs/performance#across-resources).

You can also use [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/cloud-storage-to-cloud-storage) to move large datasets from Cloud Storage to your Filestore file shares. For more information, see [Transfer large datasets from Cloud Storage to Filestore](https://docs.cloud.google.com/filestore/docs/transfer-data-from-gcs).

For other options, see [Copy data to or from instances](https://docs.cloud.google.com/filestore/docs/copying-data).

## Mount over VPN

  * When the subnet ranges of the client and the Filestore instance overlap, attempting to mount over a VPN may cause the `mount` command to become unresponsive.

If your client is a Compute Engine VM, follow the instructions at [Migrating a VM](https://docs.cloud.google.com/compute/docs/instances/migrating-interfaces-between-networks#migrating-a-vm) and change only the **Subnetwork** field. For this field, select a subnet that does not overlap with the IP range of the Filestore instance.

  * If you don't explicitly configure the Cloud Router to advertise the IP address of the Filestore instance, attempting to mount over a VPN results in an error:

`mount.nfs: Connection timed out`

For instructions on configuring the Cloud Router to advertise the IP address of a Filestore instance, see [Advertising custom IP ranges](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip).

  * You must use an external or third-party VPN provider. For more information, see [Remote mounting](https://docs.cloud.google.com/filestore/docs/remote-mounting#establish-connection).




## Capacity errors before reaching full provisioned capacity

  * When you reach close to maximum capacity usage, you may receive a `No space left on device` error. In this case, you can [add capacity](https://docs.cloud.google.com/filestore/docs/editing-instances#scaling_capacity) to the instance.

  * Each file stored on the file share consumes one inode. If the file system runs out of inodes, you won't be able to store more files on the file share even if you haven't reached the maximum allocated capacity. If connecting to numerous smaller files, you may need to increase capacity. For more information, see [Inode usage](https://docs.cloud.google.com/filestore/docs/scale#inode-usage).




## What's next

  * [List of Filestore-specific response error codes and messages](https://docs.cloud.google.com/filestore/docs/response-errors)
  * [Operations concurrency](https://docs.cloud.google.com/filestore/docs/operations-concurrency)
  * [Troubleshoot performance-related issues](https://docs.cloud.google.com/filestore/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
