---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/troubleshoot/etcd/
title: Troubleshoot etcd for GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:37.049681+00:00
---

# Troubleshoot etcd for GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/troubleshoot/etcd/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot etcd for GKE on Azure

This pages shows you how to resolve issues with etcd for GKE on Azure.

If you need additional assistance, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/getting-support). 

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

If you need additional assistance, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/getting-support). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
