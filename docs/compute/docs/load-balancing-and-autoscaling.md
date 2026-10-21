---
url: https://docs.cloud.google.com/compute/docs/load-balancing-and-autoscaling/
title: Load balancing and scaling \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:12.717302+00:00
---

# Load balancing and scaling  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/load-balancing-and-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Load balancing and scaling Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud offers load balancing and autoscaling for [groups of instances](https://docs.cloud.google.com/compute/docs/instance-groups).

## Load balancing

Google Cloud offers server-side load balancing so you can distribute incoming traffic across multiple virtual machine (VM) instances. Load balancing provides the following benefits: 

  * Scale your app
  * Support heavy traffic
  * Detect and automatically remove unhealthy VM instances using [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts). Instances that become healthy again are automatically re-added.
  * Route traffic to the closest virtual machine



Google Cloud load balancing uses forwarding rule resources to match certain types of traffic and forward it to a load balancer. For example, a forwarding rule can match TCP traffic destined to port 80 on IP address `192.0.2.1`, then forward it to a load balancer, which then directs it to healthy VM instances.

Google Cloud load balancing is a managed service, which means its components are redundant and highly available. If a load balancing component fails, it is restarted or replaced automatically and immediately.

Google Cloud offers several different types of load balancing that differ in capabilities, usage scenarios, and how you configure them. See [Google Cloud load balancing documentation](https://docs.cloud.google.com/load-balancing/docs) for descriptions.

## Autoscaling

Compute Engine offers autoscaling to automatically add or remove VM instances from a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) based on increases or decreases in load. Autoscaling lets your apps gracefully handle increases in traffic, and it reduces cost when the need for resources is lower. You can autoscale a MIG based on its CPU utilization, Cloud Monitoring metrics, schedules, or load balancing serving capacity.

When you set up an autoscaler to scale based on load balancing serving capacity, the autoscaler watches the serving capacity of an instance group and scales when the VM instances are over or under capacity. The serving capacity of an instance can be defined in the load balancer's [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) and can be based on either utilization or requests per second. For more information, see [Scaling based on load balancing serving capacity](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-load-balancing).

To learn more about autoscaling, see [Autoscaling groups of instances](https://docs.cloud.google.com/compute/docs/autoscaler).

## What's next

  * Learn more about [instance groups](https://docs.cloud.google.com/compute/docs/instance-groups).
  * Learn how to [autoscale managed instance groups](https://docs.cloud.google.com/compute/docs/autoscaler) based on: 
    * [CPU utilization](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cpu)
    * [Load balancing serving capacity](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-load-balancing)
    * [Monitoring metrics](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-stackdriver-monitoring-metrics)
    * [Schedules](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules)
  * Learn how to [choose a load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer) and 
    * How to [set up an external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https)
    * How to [set up an external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
