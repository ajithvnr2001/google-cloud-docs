---
url: https://docs.cloud.google.com/compute/docs/disks/design-considerations-for-resilient-workloads-with-regional-persistent-disks/
title: Design considerations for resilient workloads with regional disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:24:07.810776+00:00
---

# Design considerations for resilient workloads with regional disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/design-considerations-for-resilient-workloads-with-regional-persistent-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Design considerations for resilient workloads with regional disks Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2020-09-23 UTC

This document explains the behaviors and interactions between a stateful application, a health-check agent, and an application-specific regional control plane that is used to monitor and orchestrate a zonal failover by deploying [regional, synchronously replicated disks](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk).

This document is intended for application developers as a follow-up to [Build HA services using regional disks](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk), expanding on the design and architecture described in the section [Building HA database services using regional disks](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk#building_ha_database_services_using_regional_persistent_disks). We recommend that you read that document first, especially the sections about [design considerations](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk#design_considerations) and [cost comparison, performance, and resilience](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk#compare_cost_performance_and_resiliency).

A _stateless_ application increases resilience by having at least one secondary Compute Engine instance running in a different zone. When the primary instance fails, the application continues to run on the secondary instance. A _stateful_ application can persist its application state to a _zonal disk_ , or a disk that is available in only a single zone, to recover its state from an instance restart. To be resilient, a stateful application must also persist the application state to a secondary instance.

Figure 1 illustrates a typical two-node stateful application that is replicated across two zones. The application in each zone has a zonal disk to capture the application state, and a networking connection between the instances to synchronize application state changes between the nodes.

![A load balancer is used to replicate an application state to a primary and a secondary instance, which are in different zones.](https://docs.cloud.google.com/static/compute/images/disks/design-considerations-with-app-replication-between-disks-2.svg)

**Figure 1.** Two node stateful application without regional disks

## Adding a regional disk

Another way to synchronize a stateful application's application state is to add a [regional disk](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk#zonal_replication). When an application writes its application state to a regional disk, Google Cloud automatically synchronizes the block storage with another zone.

Figure 2 shows the architecture of a stateful database application.

![A regional disk is attached to two VM instances across two zones.](https://docs.cloud.google.com/static/compute/images/disks/design-considerations-with-regional-disks.svg)

**Figure 2.** Stateful database application

As figure 2 shows, there are still two application compute instances—a primary instance and a secondary instance—deployed in two zones. Along with using a regional disk for application state storage, there's now an extra entity, the application-specific regional control plane. The application-specific regional control plane decides which instance has the regional disk attached and which instance is the current primary instance. This architecture is an active-passive configuration because only the primary instance can commit an application state to the regional disk.

### Compute instances and the stateful application

Figure 2 illustrates a hot, active-passive database application. The following configurations are also possible:

  * If your recovery time objective (RTO) can afford the additional latency of starting a secondary instance, you can save on Compute Engine costs by running only the active instance. In a failover, the application-specific regional control plane starts the secondary instance and attaches the regional disk to that instance.
  * Batch or stream processing workloads that checkpoint their progress to the regional disk. In a failover, the application resumes processing from that last checkpoint.



## Managing Compute Engine instance startups

Because only a single compute instance can have a regional disk attached at one time, you need to start up the instances and attach the regional disk systematically. One best practice is to separate the compute instance and the application startup from the attachment of the regional disk. The instance's startup scripts shouldn't initiate the regional disk attachment. Instead, the startup scripts should start the health check agent and wait for the regional disk to be attached.

At startup, the compute instance needs to perform the following sequential steps:

  1. Start the health check agent.
  2. Wait for the regional disk to be attached.
  3. After the regional disk is attached, mount the file system.
  4. After the file system is mounted, start the application.



These steps cover the system startup, but there is also a failover. During a failover, the regional disk is force-attached to the secondary instance. The regional disk is also forcibly removed from the primary instance, and I/O operations to the file system fail. At this point, you need to shut down or restart the compute instance.

## Running the health check agent and health checks

As described in the preceding section, the compute instance waits for the regional disk to be attached before starting the application. The application-specific regional control plane attaches the regional disk, but only to a compute instance that's waiting for the disk to be attached. When a disk is attached, the application-specific control plane monitors the application's health and initiates a failover if the application becomes unhealthy.

Each compute instance has one of the following states:

  * Down
  * Starting
  * Waiting for a disk
  * Application running



The health check agent reports the current state of the instance. Instead of reporting these two states through a single health check, you can run two binary health checks. If the compute instance is ready to have the regional disk attached, or if the regional disk is attached and writable, then the instance health check reports a healthy status. If the application is running and is able to write the application state to the regional disk, the application health check reports a healthy status.

Using two binary health checks has several advantages:

  * You can use the Compute Engine [managed health check service](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts), which polls the health check agent and also resolves transient errors through threshold counts.
  * A [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) can monitor the instance health check and [autoheal](https://docs.cloud.google.com/compute/docs/instance-groups#autohealing) an unhealthy compute instance.
  * The load balancer can monitor the application health check and route traffic to the active application instance.



You can prevent the system from reacting to a transient failure by decreasing the health check reporting frequency, or by increasing the threshold of the repeated signals that are required to transition from one level to another. Both approaches delay the system from reacting to an outage and increase the time to recovery. By testing and measuring these parameters, you can adjust health check parameters to balance system recovery time.

## Understanding the application-specific regional control plane

The final piece in the architecture is the application-specific regional control plane, which is responsible for the following two functions:

  * Managing the lifecycle of the primary and secondary compute instances.
  * Deciding if a failover is required, by monitoring the status of the application health check.



If a failover is needed, the application-specific regional control plane orchestrates the failover with the following steps:

  1. Checks that a secondary instance is running and is waiting for the regional disk to be attached.
  2. Forces the attachment of the regional disk to the secondary instance.
  3. Monitors and restarts the failed primary instance. When the primary instance is restarted, the control plane initiates a failback as needed.



The application-specific regional control plane itself must be highly available across the two zones where the application is running. In on-premises data centers, high availability (HA) is often achieved by deploying additional servers to build a quorum, decide which compute instance is the primary instance, and orchestrate failover. This approach often uses HA monitoring tools such as [Heartbeat](https://wikipedia.org/wiki/Linux-HA), [Pacemaker](https://clusterlabs.org/pacemaker/), or [Keepalived](http://www.keepalived.org/).

Although you can use the application-specific regional control plane anywhere in the cloud, Google Cloud offers the following managed and regionally available services that simplify the implementation of this approach:

  * Google Cloud serverless products such as [App Engine](https://docs.cloud.google.com/appengine), [Cloud Run](https://docs.cloud.google.com/run), and [Cloud Run functions](https://docs.cloud.google.com/functions), which are easy to manage and deploy.
  * [Managed health checks](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) that offload the monitoring of the compute instances that run the application.
  * [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups) that manage the lifecycle of the compute instances.



Figure 3 illustrates the use of Cloud Run functions for the application-specific regional control plane, along with a [stateful managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs) and managed health checks.

![An application-specific regional control plane manages the primary and secondary VMs.](https://docs.cloud.google.com/static/compute/images/disks/design-considerations-with-regional-control-plane.svg)

**Figure 3.** Application-specific regional control plane

Figure 3 shows two compute instances of the application, primary and secondary. Each instance runs in a separate zone and is managed by a stateful regional MIG. A regional disk is available across the same two zones. Two managed health check services are running. One managed health check service monitors instance health status and is used by the stateful MIG. The other health check service monitors application health status and is used by the load balancer's target pool.

An application-specific regional control plane interacts with the target pool application health status and with the stateful regional MIG in order to monitor application status and to initiate attaching the regional disk to the current healthy compute instance.

## What's next

  * Read [Provisioning regional disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/regional-pd) in the Google Kubernetes Engine documentation.
  * To learn how you can adapt on-premises HA tools for use in Google Cloud, see [Patterns for using floating IP addresses](https://docs.cloud.google.com/architecture/patterns-for-floating-ip-addresses-in-compute-engine).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2020-09-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2020-09-23 UTC."],[],[]] 
