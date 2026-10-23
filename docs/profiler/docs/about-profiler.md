---
url: https://docs.cloud.google.com/profiler/docs/about-profiler/
title: Cloud Profiler overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:26.923862+00:00
---

# Cloud Profiler overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/about-profiler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Guides ](https://docs.cloud.google.com/profiler/docs/measure-app-performance)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Profiler overview

Understanding the performance of production systems is notoriously difficult. Attempting to measure performance in test environments usually fails to replicate the pressures on a production system. Microbenchmarking parts of your application is sometimes feasible, but it also typically fails to replicate the workload and behavior of a production system.

Continuous profiling of production systems is an effective way to discover where resources like CPU cycles and memory are consumed as a service operates in its working environment. But profiling adds an additional load on the production system: in order to be an acceptable way to discover patterns of resource consumption, the additional load of profiling must be small.

Cloud Profiler is a statistical, low-overhead profiler that continuously gathers CPU usage and memory-allocation information from your production applications. It attributes that information to the source code that generated it, helping you identify the parts of your application that are consuming the most resources, and otherwise illuminating your applications performance characteristics.

## Types of profiling available

Cloud Profiler supports different types of profiling based on the language in which a program is written. The following table summarizes the supported profile types by language:

Profile type | Go | Java | Node.js | Python  
---|---|---|---|---  
CPU time | Y| Y | | Y  
Heap | Y| Y | Y|   
Allocated heap | Y|  | |   
Contention | Y|  | |   
Threads | Y|  | |   
Wall time | | Y | Y| Y  
  
For complete information on the language requirements and any restrictions, see the language's how-to page. For more information about these profile types, see [Profiling concepts](https://docs.cloud.google.com/profiler/docs/concepts-profiling).

## Supported configurations

When you instrument your application to capture profile data, you include a language-specific [profiling agent](https://docs.cloud.google.com/profiler/docs/about-profiler#profiling_agent). The following table summarizes the supported environments: 

Environments | Go | Java | Node.js | Python  
---|---|---|---|---  
Compute Engine | Y| Y| Y| Y  
Google Kubernetes Engine | Y| Y| Y| Y  
App Engine flexible environment | Y| Y| Y| Y  
App Engine standard environment | Y| Y| Y| Y  
Managed Service for Apache Spark | | Y| |   
Dataflow | | Y| | Y  
Outside of Google Cloud | Y| Y| Y| Y  
  
The following table summarizes the supported operating systems: 

Operating systems | Go | Java | Node.js | Python  
---|---|---|---|---  
Linux  
`glibc` implementation of the standard C library | Y| Y | Y| Y  
Linux  
`musl` implementation of the standard C library | Y| Y (Alpha) | Y| Y (Alpha)  
  
## Performance impact

Cloud Profiler creates a single **profile** by collecting profiling data, usually for 10 seconds, every 1 minute for a single instance of the configured service in a single Compute Engine zone. If, for example, your GKE service runs 10 replicas of a pod, then, in a 10-minute period, roughly 10 profiles are created, and each pod is profiled approximately once. The profiling period is randomized, so there is variation. See [Profile collection](https://docs.cloud.google.com/profiler/docs/concepts-profiling#collection) for more information.

The overhead of the CPU and heap allocation profiling at the time of the data collection is less than 5 percent. Amortized over the execution time and across multiple replicas of a service, the overhead is commonly less than 0.5 percent, making it an affordable option for always-on profiling in production systems.

## Components

Cloud Profiler consists of the profiling agent, which collects the data, and a console interface on Google Cloud, which lets you view and analyze the data collected by the agent.

### Profiling agent

You install the agent on the virtual machines where your application runs. The agent typically comes as a library that you attach to your application when you run it. The agent collects profiling data as the app runs.

For information on running the Cloud Profiler agent, see: 

  * [Profiling Go applications](https://docs.cloud.google.com/profiler/docs/profiling-go)
  * [Profiling Java applications](https://docs.cloud.google.com/profiler/docs/profiling-java)
  * [Profiling Node.js applications](https://docs.cloud.google.com/profiler/docs/profiling-nodejs)
  * [Profiling Python applications](https://docs.cloud.google.com/profiler/docs/profiling-python)
  * [Profiling applications running outside Google Cloud](https://docs.cloud.google.com/profiler/docs/profiling-external)



### Profiler interface

After the agent has collected some profiling data, you can use the Profiler interface to see how the statistics for CPU and memory usage correlate with areas of your application.

![Cloud Profiler interface](https://docs.cloud.google.com/static/profiler/docs/images/profiler-interface.png)

The profile data is retained for 30 days, so you can analyze performance data for periods up to the last 30 days. Profiles can be downloaded for long-term storage.

## Quotas and limits

For information on viewing and managing your Profiler quotas, see [Quotas and limits](https://docs.cloud.google.com/profiler/quotas).

## Data security

Cloud Profiler is a VPC Service Controls supported service. For more information, see [VPC Service Controls documentation](https://docs.cloud.google.com/vpc-service-controls/docs).

## Analyzing data

After Profiler has collected data, you can view and analyze this data using the Profiler interface.

In the Google Cloud console, go to the **Profiler** page: 

[Go to **Profiler**](https://console.cloud.google.com/profiler)

You can also find this page by using the search bar.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
