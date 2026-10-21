---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/survivability/
title: Survivability mode \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:23:59.511587+00:00
---

# Survivability mode  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/survivability/

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
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)



Send feedback 

#  Survivability mode Stay organized with collections  Save and categorize content based on your preferences. 

Distributed Cloud connected clusters use a local control plane deployed on your Distributed Cloud connected hardware. When the connection to Google Cloud is lost, your clusters enter survivability mode and your workloads continue to run for up to 7 days. If a workload goes down while the cluster is in survivability mode, local image caching ensures that workload comes back up when the connection Google Cloud is restored.

A cluster can enter survivability mode due to a hardware or software fault outside of Google's control, or due to a fault in the Distributed Cloud connected hardware or software.

Examples of faults beyond Google's control:

  * Internet connectivity failure at the deployment site.
  * Firewall or network misconfiguration or hardware fault at the deployment site.
  * Boundary proxy instance serving the cluster is taken down or misconfigured.



If your Distributed Cloud connected cluster operates in survivability mode for 7 days or fewer due to a hardware or software failure beyond Google's control, Google Support works with you to restore it to normal operation up to the 7-day mark. Past the 7-day mark, further support is not guaranteed.

Examples of faults in the Distributed Cloud connected hardware or software:

  * A faulty Distributed Cloud connected software update.
  * A failure in the Distributed Cloud connected machine or networking hardware.
  * An undiagnosed fault in the Distributed Cloud connected software.



If your Distributed Cloud connected cluster enters survivability mode due to a fault in Distributed Cloud connected software or hardware, Google Support works with you until the cluster is restored to normal operation.

## What happens when a cluster enters survivability mode

When a Distributed Cloud connected cluster enters survivability mode, the following happens:

  * Google notifies you through email that the affected cluster has entered survivability mode. The email is sent to the technical category of essential contacts specified in the corresponding Google Cloud project.
  * If you need assistance in restoring your cluster to normal operation, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/getting-support).



## Cluster operation in survivability mode

When in survivability mode, a Distributed Cloud connected cluster operates as follows:

  * When the connection to Google Cloud is lost, Distributed Cloud connected continually attempts to reconnect to Google Cloud until the connection is re-established.
  * Control over workloads through the Google Cloud CLI, the `kubectl` CLI, and the Distributed Cloud Edge Container API is disabled. You can, however, generate offline credentials to access your clusters over an alternative internet connection as described in [Obtain credentials for a cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/clusters#credentials).
  * Distributed Cloud software updates, SLOs, and hardware repair are unavailable.
  * Limited logs and metrics are synchronized with Google Cloud after the connection to Google Cloud is re-established: 
    * System metrics are limited to 6 GB or 22 hours, whichever limit is reached first.
    * Workload logs are limited to 4 hours.
    * Workload metrics are limited to 1 GB.
    * Audit logs are limited to 10 GB.
  * By default, if a node reboots while the cluster is disconnected from Google Cloud, it cannot rejoin its cluster until the connection to Google Cloud is re-established because its authentication key cannot be refreshed. You have the option to specify an offline reboot window during which a node can rejoin a cluster after rebooting while the cluster is running in survivability mode. For more information, see [Create a cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/clusters#create).



## What to do when a cluster exits survivability mode

When a Distributed Cloud connected cluster exits survivability mode, check the following:

  * **Distributed Cloud connected software version.** You might need to update the affected cluster to the latest version of Distributed Cloud connected software unless you deliberately pinned the cluster to a specific software version. For more information, see [Upgrade the software version of a cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/clusters#software-upgrade).
  * **Fleet management certificates.** You might need to refresh your expired fleet management LOAS certificates. To address this, contact [Google Support](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/getting-support).



## Check the connection state of a cluster

You can check the state of your Distributed Cloud cluster's to Google Cloud by completing the steps in [Get information about a cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/clusters#get-cluster-info). The command returns the value for the `connectionState` field. This field can have one of the following values:

  * **`CONNECTED`** : The cluster is connected to and fully synchronized with Google Cloud.
  * **`DISCONNECTED`** : The cluster is not connected to Google Cloud.
  * **`CONNECTED_AND_SYNCING`** : The cluster has reconnected to Google Cloud and is synchronizing offline data with Google Cloud. Do not disconnect this cluster from Google Cloud until synchronization has completed.



## What's next

  * [How Distributed Cloud connected works](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/how-it-works)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
