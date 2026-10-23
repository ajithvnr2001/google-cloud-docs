---
url: https://docs.cloud.google.com/spanner-omni/true-time-external-consistency/
title: TrueTime and external consistency \u00a0|\u00a0 Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:05.616282+00:00
---

# TrueTime and external consistency  |  Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/true-time-external-consistency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  TrueTime and external consistency Stay organized with collections  Save and categorize content based on your preferences. 

Spanner Omni achieves external consistency in self-managed environments by implementing a software-based version of the TrueTime API. This system relies on a cluster-based architecture to provide authoritative timestamps, ensuring that transactions reflect a strict serial order across your infrastructure.

To maintain accurate and consistent timestamps and serializability, configure a primary time server and host-based clients that calculate time intervals based on network latency and clock drift. Monitor your deployment's performance through specific metrics and verify that your underlying hardware meets the required specifications for clock rate error and timestamp synchronization.

## Spanner Omni and TrueTime

To provide the same external consistency as the managed version of Spanner, Spanner Omni uses a software-based implementation of Google's TrueTime API. In the managed Spanner environment, TrueTime achieves narrow uncertainty intervals by using multiple time servers synchronized with physical GPS receivers and atomic clocks. Because Spanner Omni runs on self-managed infrastructure and can't rely on this physical hardware, it instead achieves consistency using a cluster-based architecture.

With this implementation, all transactions execute in a serial order. If a transaction finishes before another begins, the second transaction reflects the effects of the first. Spanner Omni relies on the following causal sequencing: if a call to `t1 = TrueTime::Now()` completes before a call to `t2 = TrueTime::Now()` begins (even on different machines), then `t2.latest` is later than `t1.earliest`. By assigning commit timestamps from these intervals, Spanner Omni ensures that if transaction `t1` commits before transaction `t2` starts, key timestamps reflect that `t1` occurred before `t2`.

For more information about how the managed version of Spanner uses TrueTime, see [TrueTime and external consistency](https://docs.cloud.google.com/spanner/docs/true-time-external-consistency) in the Spanner documentation.

### TrueTime architecture

The cluster-based architecture uses two core components to provide TrueTime across your deployment:

  * **Time server** : The cluster designates one database server as the primary time server. The server is the authoritative single source of truth for the entire Spanner Omni deployment, providing time from its local, high-precision clock. To ensure high availability, if the primary server stops responding, the cluster dynamically promotes another database server to assume this role. The time server is bundled within the Spanner Omni binary, requiring no separate infrastructure or external dependencies.

  * **Time client** : A background daemon runs on each host machine in the deployment. It periodically queries the primary time server to retrieve current time parameters and publishes them to the processes running on the machine.




TrueTime calculates time intervals based on bounded clock drift and the network round-trip time (RTT) between the Spanner Omni database servers and the primary time server. All host machines in the deployment must have local clocks that operate within a known bound on their rate error.

### Uncertainty (epsilon) and latency impact

TrueTime represents time as an interval, `[earliest, latest]`, rather than a single value. TrueTime calculates the size of this uncertainty interval based on two factors:

  * **Network round-trip time (RTT)** : The latency during synchronization between the time client and the primary time server. Time clients located in the same data center as the primary time server experience significantly lower uncertainty than clients in remote data centers.

  * **Clock drift** : The natural drift of the physical clocks on the client and server machines between synchronizations.




High uncertainty can increase transaction commit wait times. However, because Paxos replication also requires network communication, TrueTime uncertainty doesn't increase transaction commit latency as long as the uncertainty is smaller than the Paxos round-trip latency.

For more details, see [Spanner under the hood: Understanding strict serializability and external consistency](https://cloud.google.com/blog/products/databases/strict-serializability-and-external-consistency-in-spanner).

## Hardware requirements

For software-based TrueTime to function correctly, the underlying hardware must meet the following requirements:

  * **Timestamp counter** : You must use a hardware timestamp counter. On Linux x86 architectures, this counter is the Time Stamp Counter (TSC).
  * **Bounded clock rate error** : Local clocks must operate within a known and bounded rate error from their nominal frequency. You can monitor violations of the clock rate error using the `sla_tester_violation_count` metric. For more information, see TrueTime observability.



## Limitations

TrueTime isn't supported during live migrations of [virtual machines](https://docs.cloud.google.com/compute/docs/instances/live-migration-process) (VMs) or containers that are running Spanner Omni. Exceptions exist for specific, qualified machine types and Amazon Machine Images (AMIs) on platforms such as Amazon Web Services (AWS). For more information, see [Spanner Omni system requirements](https://docs.cloud.google.com/spanner-omni/system-requirements).

## Observability

You can use the [TrueTime dashboard](https://docs.cloud.google.com/spanner-omni/grafana-dashboards#truetime) in Grafana to monitor the following metrics. Use these metrics to ensure software-based TrueTime is operating within your expected parameters:

Metric | Description | Recommended action  
---|---|---  
`true_time_is_available` | Checks if the TrueTime API is available. | Configure alerts for any unavailability. If TrueTime is unavailable, Spanner Omni is also likely unavailable. The unavailability can be transient or persistent, and requires investigation.  
`sla_tester_violation_count` | Indicates potential clock behavior issues or hardware requirement violations. | Investigate to identify the cause of the violations. Possible causes might be live migrations, VM suspensions, or the TSC operating outside its expected bound clock rate.  
`true_time_interval_uncertainty` | Tracks the epsilon of the TrueTime interval. | Monitor this metric to minimize transaction latency. High uncertainty increases commit wait times, which can increase overall transaction latency.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
