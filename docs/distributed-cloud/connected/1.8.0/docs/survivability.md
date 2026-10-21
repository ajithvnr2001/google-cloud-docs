---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/survivability/
title: Survivability mode \u00a0|\u00a0 Google Distributed Cloud connected, version 1.8.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:30:38.846531+00:00
---

# Survivability mode  |  Google Distributed Cloud connected, version 1.8.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/survivability/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/overview)



Send feedback 

#  Survivability mode Stay organized with collections  Save and categorize content based on your preferences. 

Distributed Cloud connected clusters use a local control plane deployed on your Distributed Cloud connected hardware. When the connection to Google Cloud is lost, such clusters enter survivability mode and your workloads continue to run for up to 7 days.

When you create a Distributed Cloud connected cluster, the following rules apply:

  * You must create Distributed Cloud connected clusters in their own Google Cloud project. Distributed Cloud connected clusters cannot coexist in the same Google Cloud project with any other type of clusters, including non-Distributed Cloud connected clusters. Mixing Distributed Cloud connected clusters with any other type of clusters in the same Google Cloud project can result in data loss.
  * If you reassign a node between Distributed Cloud connected clusters, that node is wiped clean and reset to the default configuration.
  * By default, the local control plane workloads run in high availability mode with three replicas that span across three nodes chosen automatically by Distributed Cloud. This is true unless there are fewer than three nodes in the cluster, or you specifically configure the cluster to use one node to run the local control plane workloads. You also have the option to specify the three nodes for high availability mode by using the `--control-plane-machine-filter` flag. No other node combinations are supported.
  * The nodes that run the local control plane workloads also run your application workloads.
  * The IP addresses of local control plane endpoints are accessible on your local network. You must ensure that your local network's security configuration prevents external access to those IP addresses.



When in survivability mode, a Distributed Cloud connected cluster operates as follows:

  * Control over workloads through the Google Cloud CLI, the `kubectl` CLI, and the Distributed Cloud Edge Container API is disabled. 
  * Distributed Cloud software updates, SLOs, and hardware repair are unavailable.
  * Limited logs and metrics are synchronized with Google Cloud after the connection to Google Cloud is re-established.
  * By default, if a node reboots while the cluster is disconnected from Google Cloud, it cannot rejoin its cluster until the connection to Google Cloud is re-established because its authentication key cannot be refreshed. You have the option to specify an offline reboot window during which a node can rejoin a cluster after rebooting while the cluster is running in survivability mode. For more information, see [Create a cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/clusters#create).



## Check the connection state of a cluster

You can check the state of your Distributed Cloud cluster's to Google Cloud by completing the steps in [Get information about a cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/clusters#get-cluster-info). The command returns the value for the `connectionState` field. This field can have one of the following values:

  * **`CONNECTED`** : The cluster is connected to and fully synchronized with Google Cloud.
  * **`DISCONNECTED`** : The cluster is not connected to Google Cloud.
  * **`CONNECTED_AND_SYNCING`** : The cluster has reconnected to Google Cloud and is synchronizing offline data with Google Cloud. Do not disconnect this cluster from Google Cloud until synchronization has completed.



## What's next

  * [How Distributed Cloud connected works](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/how-it-works)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
