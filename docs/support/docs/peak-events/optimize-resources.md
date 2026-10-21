---
url: https://docs.cloud.google.com/support/docs/peak-events/optimize-resources/
title: Optimize your cloud resources \u00a0|\u00a0 Cloud Customer Care \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:33.312935+00:00
---

# Optimize your cloud resources  |  Cloud Customer Care  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/support/docs/peak-events/optimize-resources/

When creating a case, **Live chat** is your quickest connection to a support representative. For more information, see [Create a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Customer Care ](https://docs.cloud.google.com/support/docs)
  * [ Guides ](https://docs.cloud.google.com/support/docs/overview)



Send feedback 

#  Optimize your cloud resources Stay organized with collections  Save and categorize content based on your preferences. 

Before your peak capacity event occurs, manage and optimize the resources that are used by your Google Cloud workloads. This involves right-sizing resources based on actual usage and demand, using autoscaling for dynamic resource allocation, and reviewing architecture and security recommendations. Both [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) and [Recommender](https://docs.cloud.google.com/recommender) (Active Assist) can help you to identify opportunities to optimize your cloud resources. By using these tools, you can gain insights into resource usage and make informed decisions prior to your event.

## Review Google Cloud best practices

Many peak capacity event issues can be avoided by following the recommended best practices for the Google Cloud product that you are using. The following are examples of some best practice guides:

General  | 

  * [Google Cloud security best practices center](https://cloud.google.com/security/best-practices)
  * [Patterns for scalable and resilient apps](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps)

  
---|---  
BigQuery  | 

  * [Optimize query computation](https://docs.cloud.google.com/bigquery/docs/best-practices-performance-compute)

  
Cloud Storage  | 

  * [Best practices for Cloud Storage](https://docs.cloud.google.com/storage/docs/best-practices)

  
Compute Engine  | 

  * [Best practices for the Compute Engine API](https://docs.cloud.google.com/compute/docs/api/best-practices)
  * [Choose a Compute Engine deployment strategy for your workload](https://docs.cloud.google.com/compute/docs/choose-compute-deployment-option)
  * [Designing resilient systems](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems)

  
Dataflow  | 

  * [Dataflow pipeline best practices](https://docs.cloud.google.com/dataflow/docs/guides/pipeline-best-practices)
  * [Best practices for highly parallel workflows](https://docs.cloud.google.com/dataflow/docs/hpc-ep/hpc-best-practices)

  
Managed Service for Apache Spark  | 

  * [Managed Service for Apache Spark best practices for production](https://docs.cloud.google.com/dataproc/docs/guides/dataproc-best-practices)

  
Google Kubernetes Engine  | 

  * [Best practices for GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking)
  * [Best practices for running batch workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/batch-platform-on-gke)
  * [About GKE scalability](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/scalability)

  
  
## Review scalability

Autoscaling can ensure that your cloud-based applications have the resources that they need to handle varying workloads, while avoiding over provisioning and unnecessary costs. Google Cloud offers several product-specific autoscaling options, including the following:

  * [Compute Engine managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) are groups of VMs that are managed and scaled as a single entity. With MIGs, you can define autoscaling policies that specify the minimum and maximum number of VMs to maintain in the group, and the conditions that trigger autoscaling.
  * [Google Kubernetes Engine (GKE) autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) dynamically adjusts your cluster resources to match your application's needs. It offers tools that can optimize resource utilization, ensure application performance, and simplify cluster management.
  * [Cloud Run](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) offers built-in autoscaling, which automatically adjusts the number of instances based on the incoming traffic.



Before your event, we recommend that you scale up manually. Although you might have autoscaling configured, due to the velocity of event traffic, autoscaling might not be able to catch up with demand. So pre-warm resources ahead of time, including the following:

  * Virtual machines
  * Caches if you want to pre-load
  * Serverless components to prevent cold starts

**Note:** Google [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing) doesn't require pre-warming. However, other cloud providers might require load balancer pre-warming. Make sure to check with those providers.

## Review Active Assist recommendations

Active Assist refers to the portfolio of tools used in Google Cloud to generate recommendations and insights to help you optimize your Google Cloud projects. For more information, see [What is Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist).

## Review your product versions

Ensure that all your cloud products and services are up-to-date with the latest stable version.

## Review alerts and dashboards

Proactively identify and address issues by evaluating the alerts and dashboards provided to you through Google Cloud Observability tools and third-party solutions.

Check your [Google Cloud Observability metrics, logs, and traces](https://docs.cloud.google.com/stackdriver/docs) to gain insights into resource utilization, performance characteristics, and the overall health of your resources. Monitor important metrics that align with system health indicators such as CPU utilization, memory usage, network traffic, disk I/O, and application response times. You should also consider business-specific metrics. By tracking these metrics, you can identify potential bottlenecks, performance issues, and resource constraints. Additionally, you can set up alerts to notify relevant teams proactively about potential issues or anomalies.

For alerts, focus on critical metrics, set appropriate thresholds to minimize alert fatigue, and ensure timely responses to significant issues. This targeted approach lets you proactively maintain workload reliability. For more information, see the [Alerting overview](https://docs.cloud.google.com/monitoring/alerts).

## What's next

  * [Conduct load testing](https://docs.cloud.google.com/support/docs/peak-events/conduct-load-testing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
