---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/monitor-volume-performance-usage/
title: Monitor volume performance and usage \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:30.122858+00:00
---

# Monitor volume performance and usage  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/monitor-volume-performance-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Monitor volume performance and usage Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to monitor volume performance and usage.

The volume details page now includes an observability tab, available in Preview. This feature provides an in-context view of your volume's performance and usage metrics, without the need to navigate to Cloud Monitoring.

The observability tab provides the following information:

  * **Volume capacity usage** : monitor how close your volume is to being full. If you reach 100%, you can't write any more data. Add more capacity to avoid out-of-space errors.

  * **Volume inode usage** : track the number of files and folders you can create. At 100%, you can't add additional files or folders. If you run out of inodes, consider [adding volume capacity](https://docs.cloud.google.com/netapp/volumes/docs/quotas#inode_limits).

  * **Volume throughput usage** : monitor how much of your provisioned performance the volume consumes. For Standard, Premium, and Extreme volumes, the volume size defines the maximum throughput. For the Flex Unified and Flex File volumes, the pool defines the maximum throughput, which is shared among its volumes.

  * **Volume throughput** : view the data transfer rate for your volume.

  * **Volume IOPS** : view the I/O operations per second.

  * **Volume latency** : view the response time for volume operations.

  * **Auto-tiering volume used space** : compare data stored in the hot and cold tiers over time to identify trends, such as data cooling off or moving back to the hot tier.

  * **Volume IO activity** : analyze the types of IOPS: reads, writes, and metadata operations your volume is handling.

**Note:** The charts in Cloud Monitoring display metrics that update every five minutes. You can't see transient spikes that take less than five minutes.



To access the observability tab, do the following:

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Click the volume you want to monitor.

  4. Click the **Observability** tab on the volume details page.




## What's next

[Manage volume clones](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume-clones).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
