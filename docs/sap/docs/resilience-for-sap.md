---
url: https://docs.cloud.google.com/sap/docs/resilience-for-sap/
title: Resilience for SAP deployments on Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:46.771850+00:00
---

# Resilience for SAP deployments on Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/resilience-for-sap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Resilience for SAP deployments on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document describes design considerations that help you run resilient and reliable SAP systems on Google Cloud. 

Infrastructure and software can fail. The causes and scope of such failures require SAP system deployments to follow certain principles in order to take best advantage of the Google Cloud infrastructure. Combining infrastructure options with resilient SAP software deployment architectures ensures data integrity and protection against data loss or system unavailability.

## Resilience and reliability options

You can deploy resilient and robust systems by utilizing capabilities in both infrastructure and application layers to either absorb failures, or allow recovery from failures. To ensure resilience and reliability for SAP system deployments on Google Cloud, we recommend that you consider the following options:

  * **Platform resilience:** Google Cloud services and products are designed with resilience in mind and have built-in redundancy to attain our published [Service Level Agreements](https://cloud.google.com/compute/sla). When you deploy your SAP systems in accordance with Google Cloud [guidelines](https://docs.cloud.google.com/sap/docs/checklist-sap-overview) and [best practices](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems), the underlying platform mechanisms increase the resilience of your SAP system. This lets you continue with your business operations in case of a failure or disaster.
  * **High availability (HA):** By using infrastructure and software configurations that support HA, you can enable automated system recovery with minimal disruption. This usage also ensures that minimal intervention is required from you in case failures occur in parts of the underlying infrastructure or application software. HA is intended to protect your system against single-component failure or degradation by providing redundancy for your system components.
  * **Disaster Recovery (DR):** DR enables recovery of business operations in case of failure caused by a [disaster](https://cloud.google.com/learn/what-is-disaster-recovery). DR involves moving the services and applications to a physically isolated, secondary location from where operations can continue. DR systems extend beyond a single component or service failure to mitigate less frequent but more impactful events. This can include regional events such as natural disasters, power grid loss, and localized events such as fires or human error. DR provisions include the following: 
    * **Data replication:** You can use either software or storage level replication to ensure that your data is transferred to a secondary location with minimal potential data loss.
    * **Backups:** You can recover a system or database by using backups that are stored separately from your primary data storage. This can include using snapshots or backups uploaded in Cloud Storage, provided the snapshots or backups are stored in a [region](https://docs.cloud.google.com/compute/docs/regions-zones) other than where the system is deployed.



Because these options are complementary, you can combine aspects of each option to increase resilience within your SAP deployments. The options you select affect the recovery time objective (RTO) and recovery point objective (RPO) of your deployment. Therefore, you also need to evaluate the cost of these options against their impact on system resilience and business continuity. We recommend that you carefully consider all the available options and implement them to suit your disaster recovery objectives.

The following section describes an example SAP deployment and the impact that you can expect from different HA and DR configurations on its resilience and reliability.

## Example scenarios

Consider a scale-up SAP S/4HANA deployment on Google Cloud. The following table presents example HA and DR configurations that can be applied to this deployment and their expected impact on system resilience and reliability dimensions such as availability, RTO, and RPO.

HA or DR configuration | Resilience or reliability dimension | Expectation  
---|---|---  
**An HA configuration.** Consider the following: 

  * `us-central1` is the primary region.
  * X4 instances are deployed in two different zones, such as `us-central1-a` and `us-central1-b`.

| Availability | 

  * 99.99% or higher for the entire system.
  * 99.9% or higher for each individual instance.

  
**A DR configuration that uses async SAP HANA system replication to a fully memory resident DR system.** Consider the following: 

  * `us-central1` is the primary location.
  * `us-east4` is the DR location, and it runs an X4 instance that's the same size as the primary location.
  * Data is pre-loaded in the X4 instance running SAP HANA on the DR location.
  * In the DR location, application servers are either provisioned or you have purchased reservations for them. Note 1

| Recovery time | A few hours, which might include the time required for DNS propagation to client systems.  
Recovery point | Minutes, with respect to the last asynchronous replication.  
**A DR configuration that uses backups with pre-provisioned infrastructure** Note 1. Consider a system that uses [ Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) based backup and recovery.  | Recovery time | Time to recover database from the backup Note 2.  
Recovery point | To the last point in time in the SAP HANA log backup or snapshot.  
**A DR configuration that uses backups without pre-provisioned infrastructure** Note 3. Consider a system that uses [ Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) based backup and recovery.  | Recovery time | Several days to provision the infrastructure Note 4 and recover data from backup Note 3.   
Recovery point | To the last point in time in the SAP HANA log backup or snapshot.  
  
Table notes: 

  1. You can deploy your DR solution without pre-provisioning the required infrastructure by reserving the required resources in advance. This is a way to ensure the availability of the required resources when you need to activate your DR solution due to a disaster on the primary location. For more information, see [Choose a reservation type](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).



* The execution time of a recovery operation depends greatly on the backup solution used and the size of the backup files. To determine exact time expectations for your database size and change rates, you need to evaluate the speed of recovery for the backup solution you use, such as [Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) or [ disk snapshot](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery).

* Deploying a DR solution without pre-provisioning or reserving the required resources can lead to situations where the required resources aren't available. This can increase the recovery time of your deployment, which in turn impacts your business operations.

* For machine types such as X4, which are not available on demand and need to be ordered, several weeks of lead time might be required without a prior capacity reservation.

Consider the information presented in the preceding table as supplementary to any existing designs and disaster recovery plans that you derive from industry guidelines. For additional information, see the following resources:

  * [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide)
  * [Designing resilient systems](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems)



## Recommendations for resilient deployments

The following sections provide an overview of HA and DR configurations that we recommend for deploying resilient and reliable SAP workloads on Google Cloud.

While we strongly recommend that you implement these recommendations for SAP workloads that host business-critical production operations, you can also implement them for non-production SAP systems where a prolonged outage can have a detrimental impact on your business operations.

For information about the recommendations, see the following sections:

  * High availability recommendations
  * Disaster recovery recommendations
  * Other recommendations



### High availability recommendations

  * **Use at least two different zones** within the same region for deploying instances.
  * **Remove single points of failure.** You can achieve this by adding additional resources that provide resilience and redundancy to the faulty services or application components in case of failure.
  * **Use regional services** that have built-in redundancy. For example, use Filestore Regional (formerly Enterprise) for hosting shared files, and load balancers provided by Cloud Load Balancing.
  * **Use automation for failover.** Automation limits the need for manual intervention in case of a failure and reduces the impact on business operations. For example, you can use a Linux cluster manager such as [Pacemaker](https://clusterlabs.org/pacemaker/).
  * **Use redundant network paths.** Ensure that you have redundant connectivity into your primary region. Depending on your connectivity requirements, various options are available. For more information, see [Google Cloud connectivity](https://cloud.google.com/hybrid-connectivity).

To achieve 99.99% availability for your connections to Google Cloud regions, we recommend that you configure multiple connections. For more information, see [Establish 99.99% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability).

  * **Enable live migration and auto-restart policies on Compute Engine resources** :

    * To keep compute instances online during Google-initiated maintenance events, you can use live migration by setting the `onHostMaintenance` property with the `MIGRATE` (**Default**) option. For compute instances that don't support live migration, set the `automaticRestart` property to `true` (**Default**). This lets Google restart any instance that becomes unresponsive. For more information, see [About host events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview).
    * For compute instances that don't support live migration or planned maintenance, advanced maintenance controls are available. For more information, see [Enable advanced maintenance control for sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-advanced-maintenance-control).
  * **Before your go-live, test failover in your environment.**

    * To ensure that your HA configuration is set up correctly and functions as expected, make sure to test failure scenarios that trigger the termination of one or more components. For more information, see [Testing your HA cluster on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide#testing_your_ha_cluster_on).
    * To evaluate your HA configuration, you can use Workload Manager. For more information, see [About Workload Manager evaluation](https://docs.cloud.google.com/workload-manager/docs/about-evaluations). For information about the evaluations that Workload Manager supports for SAP workloads, see [Workload Manager best practices for SAP](https://docs.cloud.google.com/workload-manager/docs/reference/best-practices).



### Disaster recovery recommendations

  * **Host the DR solution in a location other than the primary location.** To avoid your DR solution from being impacted by the same event as your primary system, make sure that the two are hosted in different locations.

Ideally, your DR location must be a different [region](https://docs.cloud.google.com/compute/docs/regions-zones). However, if using a second region isn't a good option because of data residency or sovereignty concerns, then contact [Google Cloud Sales](https://cloud.google.com/contact) to discuss other available options.

The following diagram shows the high-level architecture for an SAP HANA deployment on Google Cloud with the following HA and DR provisions:

    * To achieve HA, the primary system has two nodes that are deployed in different zones within the same region.
    * To enable resilience, the primary and DR systems are hosted in different regions, with asynchronous replication.

![High-level architecture diagram for SAP HANA on Google Cloud with
high availability and disaster recovery.](https://docs.cloud.google.com/static/sap/docs/images/hana-ha-dr.svg)

  * **Ensure adequate capacity in the DR location.**

    * Decide whether your DR system needs to run at the same capacity as the primary system or at a diminished capacity. For databases such as SAP HANA, your DR location must have enough resources to productively operate your SAP workload.
    * Further, check in advance that the required resources are available in your DR location. To ensure resource availability, you can either provision them at the DR location or purchase reservations in advance. Purchasing reservations helps you avoid scenarios where after a failure, resources aren't available due to them being allocated to other Google Cloud customers. This is particularly important for larger compute instance types such as M2 or X4. For information about reservations, see [Choose a reservation type](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).

To achieve greater cost efficiency, the infrastructure in your DR location can be used for non-production workloads, and switched over to serve your production workload during a DR event. However, this comes at the cost of an increased recovery time.

  * **Validate connectivity to your DR location.** As with the redundant network paths to your primary location, consider adding additional fall-back options such as Cloud VPN.

  * **Identify signals that can be used to identify a disaster.** These signals help in making the decision about when to trigger your DR solution. The following are examples of some such signals:

    * Information about the health of Google Cloud services from [Google Cloud service health](https://status.cloud.google.com/).
    * Complete loss of instance availability as reported by Cloud Monitoring, as configured for your Google Cloud projects.
    * Communication from Google Cloud Customer Care or the representative of your Google Cloud account, that advises on outages and potential resolution times.
    * Logical corruptions to your database that are determined by the users or administrators of your SAP system, which cannot be solved by HA mechanisms.
  * **Test your DR solution regularly.** Ensure that your solution works in case of a disaster. This can affect your day-to-day operations. If your operations allow, then consider operating symmetrically over your primary and secondary locations, and rotate operations between them every 3 to 6 months.

  * **Use replication to achieve the best recovery point.** Replication gives a near-real-time version of your primary site on your DR site. The following replication options are available, depending on how your SAP workload is designed:

    * Database level replication by leveraging mechanisms such as [SAP HANA system replication](https://help.sap.com/docs/SAP_HANA_PLATFORM/4e9b18c116aa42fc84c7dbfd02111aba/afac7100bc6d47729ae8eae32da5fdec.html), which replicates at a logical level between the primary and the DR site.
    * Storage level replication by leveraging mechanisms such as [PD Async Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about), which replicates at a block storage level. Depending on the storage option used by your SAP workload, the available storage level replication options differ.

Make sure to monitor the replication by using an appropriate tool, such as SAP HANA Cockpit. This helps in verifying that your SAP workload has been fully replicated before your DR solution gets triggered in case of a DR event.

  * **Use data backups to provide point-in-time recoverability.**

    * To create redundancy, use multiple storage locations to store your backups. For example: 
      * While creating a backup by using the Backint feature of Google Cloud's Agent for SAP, use a dual-region or multi-region bucket location. For more information, see [Creating Cloud Storage buckets](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#creating_storage_bucket).
      * While creating a backup by using the [disk snapshot](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery) feature of the agent, use multi-region or dual-region Cloud Storage. For information about Cloud Storage bucket locations, see [Bucket locations](https://docs.cloud.google.com/storage/docs/locations).
    * Use incremental or differential backups, which can include storing snapshots on Google Cloud.
    * Monitor your backups to ensure that they are being correctly created in accordance with your backup strategy. For a complete data protection solution, consider using Google Cloud's [Backup and DR Service](https://cloud.google.com/backup-disaster-recovery).
    * Periodically test your backups to ensure that they are recoverable in case of a disaster and review how long it takes to recover your system or database. It is advisable to test recovery once every backup cycle, which usually spans 28 days.
    * Safeguard your backups as you would your primary system, for example, by using storage retention settings and encryption keys.



### Other recommendations

  * Evaluate the cost of the HA and DR configurations against the impact that they have on the following aspects of your business: 
    * Potential downtime in operations and business transactions.
    * Potential data loss resulting in the loss of sales, customer, or vendor confidence, or compliance failures.
  * All businesses have unique considerations. If your particular situation requires a more customized solution, then don't hesitate to contact [Google Cloud Sales](https://cloud.google.com/contact).



## What's next

  * [SAP HANA high-availability planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide)
  * [SAP HANA disaster recovery planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-dr-planning-guide)
  * [High-availability planning guide for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-ha-planning-guide)
  * [Disaster recovery planning guide for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-dr-on-gcp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
