---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/performance-testing/
title: Performance testing methodology for AlloyDB Omni on a VM \u00a0|\u00a0 AlloyDB Omni for containers: 15.7.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:39:43.939872+00:00
---

# Performance testing methodology for AlloyDB Omni on a VM  |  AlloyDB Omni for containers: 15.7.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/performance-testing/

This page documents AlloyDB Omni version **15.7.1** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/overview)



Send feedback 

#  Performance testing methodology for AlloyDB Omni on a VM Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.1keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/performance-testing)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/performance-testing)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/performance-testing)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/performance-testing)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/performance-testing)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/performance-testing)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/performance-testing)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/performance-testing)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/performance-testing)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/performance-testing)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/performance-testing)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/performance-testing)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/performance-testing)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/performance-testing)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/performance-testing)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/performance-testing)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/performance-testing)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/performance-testing)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/performance-testing)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/performance-testing)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/performance-testing)

This document describes recommendations for running performance tests on AlloyDB Omni on a VM. This document assumes that you're familiar with PostgreSQL. 

When benchmarking performance, define what you expect to learn from the test before beginning. For example:

  * What is the maximum throughput the system can achieve?
  * How long does a particular query or workload take?
  * How does the performance change as the amount of data increases?
  * How does the performance of two different systems compare?
  * How much does the Columnar Engine reduce the response time of my query performance?
  * How much load can a database handle before I should consider upgrading to a more powerful machine?



Understanding the goals of your performance study informs what benchmark you run, what environment is required, and what metrics you need to collect.

## Repeatability

To draw conclusions from performance testing, the test results must be repeatable. If your test results have a wide variation, assessing the impact of changes you made in the application or the system configuration will be difficult. Running tests multiple times or for longer periods of time to provide more data can help lower the variation amount.

Ideally, performance tests should be run on systems that are isolated from other systems. Running in an environment where external systems can affect the performance of your application can lead to drawing incorrect conclusions. Full isolation is often not possible when running in a multi-tenant, cloud environment, so you should expect to see greater variability in the results

Part of repeatability is ensuring that the test workload remains the same between runs. Some randomness in the input to a test is acceptable as long as the randomness does not cause significantly different application behavior. If randomly generated client input changes the mix of reads and writes from run to run, performance will vary significantly.

## Database size, caching, and I/O patterns

Ensure the amount of data you are testing with is representative of your application. Running tests with a small amount of data when you have hundreds of gigabytes or terabytes of data will likely not give a true representation of how your application performs. The size of the dataset also influences choices the query optimizer makes. Queries against small test tables may use table scans that give poor performance at larger scales and you won`t identify missing indexes in this configuration.

Strive to replicate the I/O patterns of your application. The ratio of reads to writes is important to the performance profile of your application.

## Benchmark Duration

In a complex system, there is a lot of state information that is maintained as the system executes: database connections are established, caches are populated, processes and threads are spawned. At the start of a performance test, the initialization of these components could take up system resources and adversely affect the measured performance if the runtime of the workload is too short.

We recommend running performance tests for at least 20 minutes to minimize the effects of warming up the system. Measure performance during a steady state after startup and long enough to ensure that all aspects of database operations are included. For example, database checkpoints are a critical feature of database systems and can have a significant impact on performance. Running a short benchmark that completes before the checkpoint interval hides this important factor in your application`s behavior.

## Methodical testing

When tuning performance, change only one variable at a time. If you change multiple variables between runs, you won't be able to isolate which variable improved performance. In fact, multiple changes can offset each other so you won't see the benefit of an appropriate change. If the database server is overutilized, try switching to a machine with more vCPUs while keeping the load constant. If the database server is underutilized, try increasing the load while keeping the CPU configuration constant.

## Network topology and latencies

The network topology of your system can affect the performance test results. Latency between zones differs. When doing performance testing, ensuring that the client and the database cluster are in the same zone minimizes the network latency and yields the best performance–especially for applications with high throughput, short transactions as the network latency can be a big component of the overall transaction response time.

When comparing the performance of two different systems, ensure the network topology is the same for both systems. Note that network latency variability cannot be completely eliminated, even within the same zone there can be differences in latency due to underlying network topologies.

When deploying your application, you might want to better understand the impact of cross zone latencies by considering a typical high volume web application. The application has a load balancer sending requests to multiple web servers deployed across multiple zones for high availability. The latencies might differ depending on which web server processes a request because of cross-zone latency differences.

The following figure shows the typical architecture of a web application using AlloyDB Omni. Client requests are handled by a load balancer, which forwards each request to one web server out of many. The web servers are all connected to AlloyDB Omni. Some servers are in a different zone from where AlloyDB Omni is running, and will encounter higher latencies when making database requests.

![Flow diagram that shows a typical web application architecture.](https://docs.cloud.google.com/static/alloydb/omni/containers/15.7.1/docs/images/webappusingAlloyDB.png)**Fig. 1:** A figure of a typical web application architecture. We would expect lower latencies when the web servers in Zone B make requests to the database because they are in the same zone as the AlloyDB Omni database. 

## Resource Monitoring

To optimize the performance of your database system, you need to monitor the resource usages of both the database system and the client systems using the database system. By monitoring both systems, you can ensure that the client systems are providing enough workload to get meaningful measurements in the database system. Monitoring the resource utilization of the system you are testing is critical. Monitoring the resource utilization of the client systems you are using to drive the workload is equally important. For example, if you want to determine the maximum number of clients your database system can support before it runs out of CPU resources, you will need sufficient client systems to generate the workload required to use up all the CPU resources in the database system. You won't be able to drive the database system hard enough if the client machines generating load don't have sufficient CPU themselves.

## Scalability testing

Scalability testing is another aspect of performance testing. Scalability refers to how performance metrics change as one characteristic of a workload varies. Some examples of scalability studies include:

  * How does an increase in the number of concurrent requests change throughput and response times?
  * How does an increase in database size change the throughput and response times?



Scalability tests consist of multiple runs of a workload where a single dimension is varied between runs and one or more metrics are collected and plotted. This type of testing informs decisions about what bottlenecks exist in the system, how much load the system can handle given a specific configuration, the maximum load a system can support, and what the behavior of the system is when the load increases beyond those levels.

## Machine size considerations

AlloyDB Omni introduces many new features to Postgres to improve the reliability and availability of the database. The monitoring necessary to do this uses resources on the machine running AlloyDB Omni. On very small machine sizes there are limited memory and CPU resources to begin with, so for benchmarking, we recommend using machine sizes of four vCPUs minimally.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
