---
url: https://docs.cloud.google.com/profiler/docs/concepts-profiling/
title: Profiling concepts \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:26:51.671191+00:00
---

# Profiling concepts  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/concepts-profiling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Guides ](https://docs.cloud.google.com/profiler/docs/measure-app-performance)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Profiling concepts

Profiling is a form of dynamic code analysis. You capture characteristics of the application _as it runs_ , and then you use this information to identify how to make your application faster and more efficient.

Historically, profiling was performed only during application development. This approach relied on the ability to develop load tests and benchmarks that could accurately predict a production environment.

_Continuous profiling_ refers to profiling the application while it executes in a production environment. This approach alleviates the need to develop accurate predictive load tests and benchmarks for the production environment. Research on continuous profiling has shown it is accurate and cost effective*.

Cloud Profiler is a continuous profiling tool that is designed for applications running on Google Cloud:

  * It's a statistical, or sampling, profiler that has low overhead and is suitable for production environments.

  * It supports common languages and collects multiple profile types. See Types of profiling available for an overview.




Configuring a Google Cloud application to generate profile data is a simple, one time process: link or run your service with a profiling agent included. After your application is deployed, the _profiling agent_ runs periodically to gather performance data and then sends that data to your Google Cloud project. For details about this process, see Profile collection.

After you have collected profile data for your application, you can analyze the data by using the Profiler interface. Analyzing profile data is typically an iterative process that relies on your knowledge of the application design and its programming language.

*See the following [Google-Wide Profiling: A Continuous Profiling Infrastructure for Data Centers](https://research.google/pubs/pub36575/) and [Continuous Profiling: Where Have All the Cycles Gone?](https://dl.acm.org/doi/10.1145/265924.265925). 

## Types of profiling available

The following table summarizes the supported profile types:

Profile type | Go | Java | Node.js | Python  
---|---|---|---|---  
CPU time | Y| Y | | Y  
Heap | Y| Y | Y|   
Allocated heap | Y|  | |   
Contention | Y|  | |   
Threads | Y|  | |   
Wall time | | Y | Y| Y  
  
The remainder of this section provides more detail about each of these profile types.

### Time measurements

  * **CPU time** is the time the CPU spends executing a block of code.

The CPU time for a function tells you how long the CPU was busy executing instructions. It doesn't include the time the CPU was waiting or processing instructions for something else.

  * **Wall-clock time** (also called _wall time_) is the time it takes to run a block of code.

The wall-clock time for a function measures the time elapsed between entering and exiting a function. Wall-clock time includes all wait time, including that for locks and thread synchronization. The wall time for a block of code can never be less than the CPU time.

**Note:** When the number of samples is low, the wall time can appear to be less than the CPU time in a sampling profile such as Cloud Profiler.



If the wall-clock time is longer than the CPU time, then that indicates the code spends time waiting. When the difference is substantial, your application might have a resource bottleneck.

If the CPU time is similar to the wall time, then that indicates the code is CPU intensive; almost all the time it takes to run is spent by the CPU. Long-running CPU-intensive blocks of code might be candidates for optimization.

### Heap (memory) usage

  * **Heap usage** (also called _heap_) is the amount of memory allocated in the program's heap at the instant the profile is collected. Unlike other profile types where data is collected over an interval, this profile type collects the heap usage at a single point in time.

  * **Heap allocation** (also called _allocated heap_) is the total amount of memory that was allocated in the program's heap during the interval in which the profile was collected. This value includes any memory that was allocated and has been freed and is no longer in use. As an example, consider a job that repeats the following sequence: allocates 1 MiB, waits 500 msec, frees 1 MiB, waits 500 msec. In the 10 seconds in which the allocated heap profile is collected, there are 10 allocations and 10 frees. This profile would show 10 MiB allocated heap, as the frees aren't considered. The average rate of allocation is 10 MiB/10 seconds or 1 MiB per second.




Profiling heap usage helps you find potential inefficiencies and memory leaks in your programs. Profiling heap allocations helps you know which allocations are causing the most work for the garbage collector.

### Threading information

Applications that create threads can suffer from blocked threads and from thread leaks:

  * Blocked threads are threads that are created but are waiting for a lock. These threads are not currently running, and they might never run. However, a blocked thread might eventually run.
  * Thread leaks occur when the number of created threads keeps increasing.



Blocked threads are one cause of leaked threads.

At the frame level, the **Thread** profile displays the average number of threads that include that frame. This profile type collects thread usage at a single point in time.

### Contention

In a multi-threaded program, the time spent waiting to serialize access to a shared resource can be significant. Understanding contention behavior can guide the design of the code and provide information for performance tuning.

## Profile collection

The role of the profiler agent is to capture profile data from your application and to transmit this data to the Profiler backend using the Profiler API. Each profile is for a single instance of an application and it includes four fields that uniquely identify its deployment:

  * Google Cloud project
  * Application name
  * Application zone
  * Application version



When an agent is ready to capture a profile, it issues a Profiler API command to the Profiler backend. The backend receives this request and, in the simplest scenario, immediately replies to the agent. The reply specifies the type of profile to capture. In response, the agent captures the profile and transmits it to the backend. Lastly, the Profiler backend associates the profile with your Google Cloud project. You can then view and analyze it by using the Profiler interface.

The actual handshake sequence is more complex than described in the previous paragraph. For example, when the Profiler receives a request from an agent, the backend checks its database to determine if it has received previous requests from the agent. If not, the backend adds the agent information to its database. A new deployment is created if the agent deployment fields don't match the settings of any other recorded agent.

Each minute, on average, and for each deployment and each profile type, the backend selects an agent and instructs it to capture a profile. For example, if the agents for a deployment support Heap and Wall time profiling, on average, two profiles are captured each minute:

  * For all profile types except heap usage and threads, a single profile represents data collected for 10 seconds.

  * Heap usage and thread profiles are collected instantaneously.




After the agent notifies the Profiler backend that it's ready to capture data, the agent idles until the backend replies with the type of profile to capture. If you have 10 instances of an application running in the same deployment, then you create 10 profiling agents. However, most of the time these agents are idle. Over a 10-minute period, you can expect 10 profiles; each agent receives one reply for each profile type, on average. There is some randomization involved, so the actual number might vary.

The Profiler backend uses Profiler API quotas and the profile deployment fields to limit the profiles ingested. For information on viewing and managing your Profiler quotas, see [Quotas and limits](https://docs.cloud.google.com/profiler/quotas).

## Analyzing data

After Profiler has collected data, you can view and analyze this data using the Profiler interface.

In the Google Cloud console, go to the **Profiler** page: 

[Go to **Profiler**](https://console.cloud.google.com/profiler)

You can also find this page by using the search bar.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
