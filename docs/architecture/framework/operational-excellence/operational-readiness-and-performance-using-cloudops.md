---
url: https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops/
title: Ensure operational readiness and performance using CloudOps \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:36.349638+00:00
---

# Ensure operational readiness and performance using CloudOps  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Ensure operational readiness and performance using CloudOps Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-10-02 UTC

This principle in the operational excellence pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) helps you to ensure operational readiness and performance of your cloud workloads. It emphasizes establishing clear expectations and commitments for service performance, implementing robust monitoring and alerting, conducting performance testing, and proactively planning for capacity needs.

## Principle overview

Different organizations might interpret operational readiness differently. Operational readiness is how _your_ organization prepares to successfully operate workloads on Google Cloud. Preparing to operate a complex, multilayered cloud workload requires careful planning for both go-live and [day-2](https://discuss.google.dev/t/simplify-day-2-cloud-operations-with-google-cloud-solutions-and-architectural-design-best-practices/98008) operations. These operations are often called _CloudOps_.

## Focus areas of operational readiness

Operational readiness consists of four focus areas. Each focus area consists of a set of activities and components that are necessary to prepare to operate a complex application or environment in Google Cloud. The following table lists the components and activities of each focus area:

**Note:** The recommendations in the operational excellence pillar of the Well-Architected Framework are relevant to one or more of these operational-readiness focus areas.Focus area of operational readiness | Activities and components  
---|---  
Workforce | 

  * Defining clear roles and responsibilities for the teams that manage and operate the cloud resources.
  * Ensuring that team members have appropriate skills.
  * Developing a learning program.
  * Establishing a clear team structure.
  * Hiring the required talent.

  
Processes | 

  * Observability.
  * Managing service disruptions.
  * Cloud delivery.
  * Core cloud operations.

  
Tooling | Tools that are required to support CloudOps processes.  
Governance | 

  * Service levels and reporting.
  * Cloud financials.
  * Cloud operating model.
  * Architectural review and governance boards.
  * Cloud architecture and compliance.

  
  
## Recommendations

To ensure operational readiness and performance by using CloudOps, consider the recommendations in the following sections. Each recommendation in this document is relevant to one or more of the focus areas of operational readiness.

### Define SLOs and SLAs

A core responsibility of the cloud operations team is to define service level objectives (SLOs) and service level agreements (SLAs) for all of the critical workloads. This recommendation is relevant to the _governance_ focus area of operational readiness.

  * **Define SLOs** :

SLOs must be specific, measurable, achievable, relevant, and time-bound (SMART), and they must reflect the level of service and performance that you want.

    * **Specific** : Clearly articulates the required level of service and performance.
    * **Measurable** : Quantifiable and trackable.
    * **Achievable** : Attainable within the limits of your organization's capabilities and resources.
    * **Relevant** : Aligned with business goals and priorities.
    * **Time-bound** : Has a defined timeframe for measurement and evaluation.

For example, an SLO for a web application might be "99.9% availability" or "average response time less than 200 ms." Such SLOs clearly define the required level of service and performance for the web application, and the SLOs can be measured and tracked over time.

  * **Define SLAs** :

SLAs outline the commitments to customers regarding service availability, performance, and support, including any penalties or remedies for noncompliance. SLAs must include specific details about the services that are provided, the level of service that can be expected, the responsibilities of both the service provider and the customer, and any penalties or remedies for noncompliance. SLAs serve as a contractual agreement between the two parties, ensuring that both have a clear understanding of the expectations and obligations that are associated with the cloud service.

  * **Track SLOs** :

Use [Cloud Monitoring](https://docs.cloud.google.com/monitoring) and service level indicators (SLIs) to track SLOs. Cloud Monitoring provides comprehensive monitoring and observability capabilities that enable your organization to collect and analyze metrics that are related to the availability, performance, and latency of cloud-based applications and services. SLIs are specific metrics that you can use to measure and track SLOs over time. By utilizing these tools, you can effectively monitor and manage cloud services, and ensure that they meet the SLOs and SLAs.




Clearly defining, communicating, and tracking SLOs and SLAs for all of your critical cloud services helps to ensure reliability and performance of your deployed applications and services.

### Implement comprehensive observability

To get real-time visibility into the health and performance of your cloud environment, we recommend that you use a combination of [Google Cloud Observability tools](https://cloud.google.com/products/observability) and third-party solutions. This recommendation is relevant to the _processes_ and _tooling_ focus areas of operational readiness.

Implementing a combination of observability solutions provides you with a comprehensive observability strategy that covers various aspects of your cloud infrastructure and applications. Google Cloud Observability is a unified platform for collecting, analyzing, and visualizing metrics, logs, and traces from various Google Cloud services, applications, and external sources. By using Cloud Monitoring, you can gain insights into resource utilization, performance characteristics, and overall health of your resources.

To ensure comprehensive monitoring, monitor important metrics that align with system health indicators such as CPU utilization, memory usage, network traffic, disk I/O, and application response times. You must also consider business-specific metrics. By tracking these metrics, you can identify potential bottlenecks, performance issues, and resource constraints. Additionally, you can set up alerts to notify relevant teams proactively about potential issues or anomalies.

To enhance your monitoring capabilities further, you can integrate third-party solutions with Google Cloud Observability. These solutions can provide additional functionality, such as advanced analytics, machine learning-powered anomaly detection, and incident management capabilities. This combination of Google Cloud Observability tools and third-party solutions lets you create a robust and customizable monitoring ecosystem that's tailored to your specific needs. By using this combination approach, you can proactively identify and address issues, optimize resource utilization, and ensure the overall reliability and availability of your cloud applications and services.

### Implement performance and load testing

Performing regular performance testing helps you to ensure that your cloud-based applications and infrastructure can handle peak loads and maintain optimal performance. Load testing simulates realistic traffic patterns. Stress testing pushes the system to its limits to identify potential bottlenecks and performance limitations. This recommendation is relevant to the _processes_ and _tooling_ [focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

  * **Test performance** : Use [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing) and [load testing services](https://docs.cloud.google.com/load-balancing/docs/backend-service-load-testing) to simulate real-world traffic patterns and stress-test your applications. These tools provide valuable insights into how your system behaves under various load conditions, and can help you to identify areas that require optimization.

  * **Optimize performance** : Based on the results of performance testing, you can make decisions to optimize your cloud infrastructure and applications for optimal performance and scalability. This optimization might involve adjusting resource allocation, tuning configurations, or implementing caching mechanisms.

For example, if you find that your application is experiencing slowdowns during periods of high traffic, you might need to increase the number of virtual machines or containers that are allocated to the application. Alternatively, you might need to adjust the configuration of your web server or database to improve performance.




By regularly conducting performance testing and implementing the necessary optimizations, you can ensure that your cloud-based applications and infrastructure always run at peak performance, and deliver a seamless and responsive experience for your users. Doing so can help you to maintain a competitive advantage and build trust with your customers.

### Plan and manage capacity

To keep your cloud systems running and scaling in response to changes in demand, you need to actively plan and manage capacity for the cloud resources. This recommendation supports the _processes_ and _tooling_ [focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

  * **Consider service limits and manage resource quotas** : To plan capacity for your cloud resources, start with the hard limits (the fixed constraints) for the services that you plan to use.

    * Estimate the [quota](https://docs.cloud.google.com/docs/quotas/view-manage) requirements for compute, storage, API limits and other resources that you need. Request suitable quota adjustments before you need the resources.
    * Load metrics from [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) into [BigQuery](https://docs.cloud.google.com/bigquery/docs/loading-data), and use the metrics to identify traffic patterns and track the system load over time.
    * Forecast the demand for resources based on upcoming marketing campaigns, user signups, and feature rollouts. Also consider your current and planned SLA commitments.
  * **Design for flexibility and efficiency** : When you plan capacity for your cloud deployments, decouple application components from specific machine types. When you pin a workload to a single machine type, you can't take advantage of newer cloud hardware or changes in regional capacity.

    * For workloads that need specialized hardware, such as high-memory instances or GPUs, ensure that you can obtain resources when required. Use [future reservations](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview) to get an assurance of capacity for critical machine types up to a year ahead.
    * For batch-processing or model-training workloads that can tolerate variable start times, schedule capacity dynamically by using [Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms). These VMs use Dynamic Workload Scheduling (DWS) to queue requests and reduce compute costs.
    * Avoid reserving older machine families or resources for transient development environments.
    * Plan for resources in secondary regions so that you can fail over efficiently for disaster recovery (DR).
  * **Implement automatic scaling** : To dynamically adapt your cloud resources to real-time workload fluctuations, implement autoscaling policies. Autoscaling algorithms evaluate metrics such as CPU utilization, memory pressure, and queue depth. Based on the evaluation, resources are scaled out during peak traffic periods and scaled in during low-utilization windows, which helps to optimize the cost of your cloud resources.

    * Configure [managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility) with mixed instance templates that combine current and newer generations of machine types.
    * Ensure that your MIG configurations include both instance flexibility (specifying multiple compatible machine types) and location flexibility (spreading targets across multiple zones in a region). Depending on the current capacity requirements, your system automatically provisions the next preferred machine type from your fallback list without dropping requests or limiting compute resources.



### Continuously monitor and optimize

To manage and optimize cloud workloads, you must establish a process for continuously monitoring and analyzing performance metrics. This recommendation is relevant to the _processes_ and _tooling_ [focus areas of operational readiness](https://docs.cloud.google.com/architecture/framework/operational-excellence/operational-readiness-and-performance-using-cloudops#focus-areas-of-operational-readiness).

  * **Track and gather data** :

To establish a process for continuous monitoring and analysis, you need to track, collect, and evaluate data that's related to various aspects of your cloud environment. By using this data, you can proactively identify areas for improvement, optimize resource utilization, and ensure that your cloud infrastructure consistently meets or exceeds your performance expectations.

  * **Review logs and traces** :

Logs provide valuable insights into system events, errors, and warnings. Traces provide detailed information about the flow of requests through your application. By analyzing logs and traces, you can identify potential issues, identify the root causes of problems, and get a better understanding of how your applications behave under different conditions. Metrics like the round-trip time between services can help you to identify and understand bottlenecks that are in your workloads.

  * **Tune for performance** :

Use performance-tuning techniques to significantly optimize application response times and overall efficiency. The following are examples of techniques that you can use:

    * **Caching** : Store frequently accessed data in memory to reduce the need for repeated database queries or API calls.
    * **Database optimization** : Use techniques like indexing and query optimization to improve the performance of database operations.
    * **Code profiling** : Identify areas of your code that consume excessive resources or cause performance issues.



[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/architecture/framework/operational-excellence)

[ Next Manage incidents and problems  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/operational-excellence/manage-incidents-and-problems)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
