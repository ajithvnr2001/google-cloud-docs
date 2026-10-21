---
url: https://docs.cloud.google.com/netapp/volumes/docs/monitor/monitor-volume-usage/
title: Monitor volume usage \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:36.872485+00:00
---

# Monitor volume usage  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/monitor/monitor-volume-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Monitor volume usage Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to monitor volume usage to prevent out-of-space errors and maintain application stability.

## About volume usage

Volumes are containers for user data and snapshot data and limit their growth to the capacity of the volume.

An application or user that writes more data than allocated into the volume receives an _out-of-space_ error, which can cause application problems. We recommend that you monitor consumption to avoid out-of-space errors.

A common approach is to increase the volume capacity as soon as a certain usage threshold, typically 80%, is reached.

## Considerations

Review the following considerations about volume usage:

  * You could encounter a lack of free space despite deleting your data and could potentially delete snapshots that reference data you need. For more information, see [Snapshots and snapshot-based data management](https://docs.cloud.google.com/netapp/volumes/docs/discover/product-overview#snapshots_and_snapshot-based_data_management).

  * Instead of deleting snapshots manually to free up space, we recommend that you increase volume capacity to avoid out-of-space conditions.

  * Inodes are limited resources in a volume and are consumed for every file or directory you create. Although running out of inodes is less common, we recommend that you monitor them in an environment where millions of files are expected in a volume.




## Methods for monitoring volume usage

You can monitor volume usage using the methods in the following sections:

### Cloud Monitoring-based usage monitoring

You can calculate volume usage from the following volume metrics:

  * **Volume space** : `netapp.googleapis.com/volume/bytes_used / netapp.googleapis.com/volume/allocated_bytes * 100`

  * **Volume inodes** : `netapp.googleapis.com/volume/inode_used / netapp.googleapis.com/volume/inode_limit * 100`




Use the volume name and location as a metric label to match metrics that belong together.

You can use Cloud Monitoring alerting to match the result against a threshold like 80% to trigger [alert notifications](https://docs.cloud.google.com/monitoring/alerts).

The following example shows [Prometheus Query Language (PromQL)](https://docs.cloud.google.com/monitoring/promql) code to monitor volume usage:
    
    
       netapp_googleapis_com:volume_bytes_used / netapp_googleapis_com:volume_allocated_bytes
     

You can extend this code for use in a [metric-threshold alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).
    
    
       (netapp_googleapis_com:volume_bytes_used /
       netapp_googleapis_com:volume_allocated_bytes) > 0.8
     

Note that the metrics are updated every five minutes. The changes occurring on a smaller time scale are not reflected in Cloud Monitoring.

### Client-side usage monitoring

You can check the used and available capacity of a volume by using the client operating system features to query the network mapped drive properties:

  * **Windows clients** : Use the `dir` command at the command prompt, or use the `Drive` > `Properties` command in File Explorer.

  * **Linux clients** : Use the `df` command for space and `df -i` for inode monitoring.




### Administrative usage monitoring

You can view the usage and provisioned space for volumes on the **Volumes page** in the Google Cloud console:

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. The **Used** column shows usage percentage and GiB used.




You can use Google Cloud CLI to get the volumes capacity and usage:
    
    
       gcloud netapp volumes list --format="table(name, capacityGib, usedGib)"
      

Inode metrics aren't available using this approach.

## What's next

Read about [Cloud Logging](https://docs.cloud.google.com/netapp/volumes/docs/monitor/cloud-logging).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
