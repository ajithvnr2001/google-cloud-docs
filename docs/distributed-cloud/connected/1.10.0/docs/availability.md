---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/availability/
title: Availability best practices \u00a0|\u00a0 Google Distributed Cloud connected, version 1.10.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:27:23.030445+00:00
---

# Availability best practices  |  Google Distributed Cloud connected, version 1.10.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/availability/

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
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/overview)



Send feedback 

#  Availability best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page describes best practices for ensuring high availability for your Google Distributed Cloud connected installation. Distributed Cloud connected does not offer a service level agreement (SLA) and only provides the service level objective (SLO) described on this page.

## Choose and implement the level of availability

You must choose the level of availability for your Distributed Cloud connected workloads that best suits your business requirements. For example, a self-checkout application at a retail store has a much lower availability risk than an edge RAN deployment of a mobile network carrier.

Target availability is directly proportional to the Distributed Cloud spare resource capacity that you reserve for emergencies. The following table describes this relationship. These estimates do not include the downtime scheduled with a maintenance window.

The Distributed Cloud connected software consumes some resources on each physical machine. The amount varies depending on the specific configuration of your Distributed Cloud connected deployment. Google recommends that you benchmark your Distributed Cloud connected deployment to measure this amount and account for it when planning your workload distribution.

GDC connected form factor | Capacity in use | Reserved capacity | Target availability  
---|---|---|---  
**GDC connected rack**  
(single 6-machine cluster) | 83.33% | 16.67% | 99.9%  
**GDC connected rack**  
(single 6-machine cluster) | 100% | 0% | 93.5%  
**GDC connected server**  
(single 3-machine cluster) | 66.6% | 33.3% | 99.9%  
  
You might experience a sudden loss of capacity due to hardware failure or a node that requires a restart. To prepare for this, you must architect your workloads with resource quotas in mind so that you always have available capacity on each Distributed Cloud connected node that meets your chosen level of availability.

For example, to achieve 99.9% target availability on a Distributed Cloud connected rack deployment, you must configure your workloads so that one of the six physical machines in each Distributed Cloud connected cluster is available as a backup.

## Geographically diversify your Distributed Cloud zones

To minimize the impact of potential [management plane faults](https://docs.cloud.google.com/docs/geography-and-regions#service_dependencies), we strongly recommend that you distribute your Distributed Cloud zones across several neighboring regions.

## Use survivability mode

Distributed Cloud clusters use a local control plane that runs on your Distributed Cloud connected hardware. Your workloads continue to run when the connection to Google Cloud is lost. For more information, see [Distributed Cloud connected survivability mode](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/survivability).

## Understand software updates and maintenance windows

Google regularly updates the Distributed Cloud connected software. These software updates are mandatory and you cannot opt out of them. Distributed Cloud connected lets you specify individual maintenance windows for each of your Distributed Cloud connected clusters. 

To mitigate potential transient disruptions to your workloads, maintenance windows let you control when automatic upgrades of control planes and nodes can occur. Maintenance windows are useful for the following types of scenarios, among others:

  * **Off-peak hours:** You want to minimize the chance of downtime by scheduling automatic upgrades during off-peak hours when traffic is reduced.
  * **On-call:** You want to ensure that upgrades happen during working hours so that someone can monitor the upgrades and manage any unanticipated issues.
  * **Multi-cluster upgrades:** You want to roll out upgrades across multiple clusters in different regions one at a time at specified intervals.



Distributed Cloud connected supports the following types of maintenance windows:

  * **Maintenance window.** Specifies a time window during which Google can perform maintenance and software upgrades on your Distributed Cloud connected cluster.
  * **Maintenance exclusion window.** Specifies a time window during which Google cannot perform maintenance or software upgrades on your Distributed Cloud connected cluster. To configure a maintenance exclusion window, you must first configure a maintenance window. A maintenance exclusion window takes precedence over the cluster's maintenance window.

**Warning:** A Distributed Cloud connected cluster does not have a default maintenance window. This means that a software update can potentially bring down a critical workload. To ensure high availability, we strongly recommend that you configure staggered maintenance windows and configure maintenance exclusion windows for your clusters.

In addition to automatic upgrades, Google might occasionally need to perform other maintenance tasks. In those cases, it honors a cluster's maintenance window when possible.

If a software upgrade or maintenance task does not finish before the end of a maintenance window, Distributed Cloud connected pauses the upgrade or task and resumes it during the next scheduled maintenance window. If a software upgrade fails, Distributed Cloud connected halts the upgrade; in such cases you must contact [Google Support](https://cloud.google.com/distributed-cloud/connected/1.10.0/docs/getting-support) to repair your software installation.

Distributed Cloud connected reserves the right to roll out unplanned emergency upgrades outside of maintenance windows. Additionally, mandatory upgrades from deprecated or outdated software might automatically occur outside of maintenance windows.

You can also [manually upgrade your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) at any time. Manually-initiated upgrades begin immediately and ignore any maintenance windows.

To learn how to set up a maintenance window for a new or existing cluster, see Configure a maintenance window.

### Software update staggering

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To reduce workload downtime, Distributed Cloud connected software updates are staggered. In other words, Google upgrades worker nodes in each Distributed Cloud connected cluster in stages. All worker nodes in a software upgrade stage go down simultaneously.

The number of nodes in a software upgrade stage is determined as follows:

  * **Deployments of up to 3 racks:** Each stage is the total number of machines across all racks divided by 6 and rounded up to the next integer.
  * **Deployments of 4 or more racks:** Each stage is the total number of machines across all racks in the deployment divided by the number of racks in the deployment.



You also have the option to set your own software upgrade stage size. In other words, you can specify the number of nodes that can go down for a software upgrade simultaneously in a Distributed Cloud connected cluster. For instructions, see [Manage node downtime during software upgrades](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/clusters#stage-size).

### Restrictions

Maintenance windows have the following restrictions:

  * **One maintenance window per cluster.** You can only configure a single maintenance window per cluster. Configuring a new maintenance window overwrites the previous one.

  * **Time zones for maintenance windows.** When configuring and viewing maintenance windows, times are shown differently depending on the tool that you are using, as detailed in the following sections.




#### When configuring maintenance windows

When you use the more generic `--maintenance-window` flag to configure a maintenance window, you cannot specify a time zone. When you use the Google Cloud CLI or the API, UTC is used to display times. The Google Cloud console uses the local time zone to display times.

When you use more granular flags, such as `--maintenance-window-start`, you can specify the time zone as part of the value. If you omit the time zone, your local time zone is used. Times are always stored in UTC.

#### When viewing maintenance windows

When you view information about your cluster, timestamps for maintenance windows can be shown in UTC or in your local time zone, depending on how you are viewing the information:

  * When you use the Google Cloud console to view information about your cluster, times are always displayed in your local time zone.
  * When you use the gcloud CLI to view information about your cluster, times are always shown in UTC.



In both cases, the `RRULE` is always in UTC. That means that if specifying, for example, days of the week, then those days are in UTC.

## Configure cluster maintenance windows

Distributed Cloud connected lets you specify a maintenance window for each of your Distributed Cloud connected clusters. This window tells Google to only update the Distributed Cloud software during the time and at the frequency that you specify.

The following rules govern Distributed Cloud connected cluster maintenance windows:

  * If you specify a maintenance window for a Distributed Cloud connected cluster, Google updates your Distributed Cloud connected software 48 hours after the update has been announced through the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/release-notes). On the release notes page, you can subscribe to the Distributed Cloud connected release notes RSS feed to stay informed about software updates as they are released.
  * The minimum length of a maintenance window is five hours. You can specify a longer window based on the complexity of your Distributed Cloud connected installation and your business requirements.
  * The minimum frequency of software updates is once per week. You can specify either weekly or daily maintenance windows. You can include and exclude specific days.
  * You can change the maintenance window schedule for a cluster at any time, except when a maintenance window has already been scheduled or when a maintenance window is in progress.
  * If the software update does not complete within the specified time window, it pauses and then resumes during the next scheduled maintenance window.



For detailed instructions, see [Configure a maintenance window for a cluster](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/clusters#maintenance).

## Repair of failed hardware

When Google detects a failure of the Distributed Cloud connected hardware, we do one of the following:

  * For Google-owned Distributed Cloud hardware, Google attempts to schedule a site visit within three business days. For a Google-authorized technician to perform the necessary diagnosis and repairs, you must grant them access to the Distributed Cloud connected hardware.

  * For customer-owned Distributed Cloud hardware, Google notifies you and the Google-certified SI of the problem. You must work with the SI who delivered your Distributed Cloud connected hardware to schedule a technician visit and perform the necessary diagnosis and repairs.




If a failure of Distributed Cloud connected hardware occurs, one of the following scenarios applies depending on whether your Distributed Cloud connected hardware uses Self-Encrypting Disk (SED) storage:

  * **Distributed Cloud connected racks** store data on non-SED drives. When Google or a Google-certified SI performs on-site repairs, all disk drives are removed from the affected Distributed Cloud connected machine before servicing begins and are placed in your custody for the duration of the repair.

  * **Distributed Cloud connected servers** store data on SED drives. When a machine fails, Google or a Google-certified SI replaces the entire machine. Before the machine is removed from your premises, Google ensures that your data has been securely wiped from all of its drives.


**Warning:** Neither Google nor the Google-certified SI cannot recover the data that you choose to store on Distributed Cloud connected hardware in the event of a hardware failure. You are responsible for maintaining functioning redundant backups of all the data that you choose to store on Distributed Cloud connected hardware.

### Other points of failure

You are responsible for maintaining the following aspects of your Distributed Cloud installation that are outside of Google's control and can affect the availability of Distributed Cloud connected:

  * Any and all data that you choose to store on Distributed Cloud connected hardware. This includes functioning redundant backups and the export of your data before returning your Distributed Cloud connected hardware to Google.
  * [Electrical power supply](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/order#power).
  * [Ambient temperature, humidity, and cooling](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/order#cooling).
  * [Physical hardware security](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/security#physical).
  * [Local network security](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/security#network).
  * Local network and internet connectivity. Distributed Cloud connected must reconnect to Google Cloud every 7 days to refresh security tokens, encryption keys, and synchronize logging and management data.



## What's next

  * [Configure Network Function operator resources](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/network-function)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
