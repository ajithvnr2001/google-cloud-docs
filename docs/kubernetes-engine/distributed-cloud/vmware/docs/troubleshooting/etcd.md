---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/etcd/
title: Troubleshoot etcd \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:40.533699+00:00
---

# Troubleshoot etcd  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/etcd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Troubleshoot etcd Stay organized with collections  Save and categorize content based on your preferences. 

This pages shows you how to resolve issues with etcd for Google Distributed Cloud.

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



## etcd data disk is full

The following error occurs when the etcd data disk is full, and might be observed in a few different ways:

  * The etcd logs might show timeout errors for writing requests:
        
        rafthttp: failed to save KV snapshot (write /var/etcd/data/member/snap/tmp720030520: no space left on device)
        

You might also see timeout errors for connections to peers:
        
        rafthttp: health check for peer [peer-id] could not connect: dial tcp [peer-ip]:2380: i/o timeout
        etcd server doesn't start:
        

  * The serial port logs might indicate that etcd can't start due to lack of space:
        
        failed on file /dev/stdout (No space left on device)
        




To determine the size of your etcd instance, use one of the following methods:

###  SSH 

  1. Connect to one of the master nodes using SSH and run the following command:
         
         ETCDCTL_API=3 etcdctl --write-out=table endpoint status
         

The `DB_SIZE` column indicates the size used, as shown in the following condensed example output:
         
         +------------------+------------------+---------+---------+
         |    ENDPOINT      |        ID        | VERSION | DB SIZE |
         +------------------+------------------+---------+---------+
         | 10.240.0.17:2379 | 4917a7ab173fabe7 |  3.5.0  |   45 kB |
         | 10.240.0.18:2379 | 59796ba9cd1bcd72 |  3.5.0  |   45 kB |
         | 10.240.0.19:2379 | 94df724b66343e6c |  3.5.0  |   45 kB |
         +------------------+------------------+---------+---------+
         




###  Console 

  1. In the console, go to the Cloud Monitoring page.

[Go to the Cloud Monitoring page](https://console.cloud.google.com/monitoring/)

  2. Select **Metrics explorer**.

  3. Select the `metric etcd_mvcc_db_total_size_in_bytes` metric.




To resolve this issue, resize the data disk for etcd using the appropriate procedure for your storage provider and operating system. Add enough additional space to account for future etcd growth.

  1. After the disk is resized, check if there's still a warning on disk space:
         
         ETCDCTL_API=3 etcdctl alarm list
         

  2. If the last column reports `NOSPACE`, disarm the alarm as follows:
         
         ETCDCTL_API=3 etcdctl alarm disarm
         




## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
