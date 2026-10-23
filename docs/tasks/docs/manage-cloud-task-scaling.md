---
url: https://docs.cloud.google.com/tasks/docs/manage-cloud-task-scaling/
title: Manage scaling risks \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:46.924643+00:00
---

# Manage scaling risks  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/manage-cloud-task-scaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Manage scaling risks Stay organized with collections  Save and categorize content based on your preferences. 

Google's infrastructure is designed to operate elastically at high-scale: most layers can adapt to increased traffic demands up to massive scale. A core design pattern that makes this possible is adaptive layers—infrastructure components that dynamically re-allocate load based on traffic patterns. This adaptation, however, takes time. Because Cloud Tasks enables very high volumes of traffic to be dispatched, it exposes production risks in situations where traffic can climb faster than the infrastructure can adapt.

## Overview

This document provides guidelines on the best practices for maintaining high Cloud Tasks performance in high-traffic queues. A **high-TPS queue** is a queue that has 500 created or dispatched tasks per second (**TPS**) or more. A **high-TPS queue group** is a contiguous set of queues, for example [_queue0001_ , _queue0002_ , …, _queue0099_], that have at least 2000 tasks created or dispatched in total. The historical TPS of a queue or group of queues are viewable using the [Cloud Monitoring metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-cloudtasks), `api/request_count` for `CreateTask` operations and `queue/task_attempt_count` for task attempts. High-traffic queues and queue groups are prone to two different broad classes of failures:

  * Queue overload
  * Target overload



**Queue overload** occurs when task creation and dispatch to an individual queue or queue group increases faster than the queue infrastructure is able to adapt. Similarly, **target overload** occurs when the rate at which tasks are being dispatched causes traffic spikes in the downstream target infrastructure. In both cases, we recommend following a **500/50/5 pattern** : when scaling beyond 500 TPS, increase traffic by no more than 50% every 5 minutes. This document reviews different scenarios that can introduce scaling risks and gives examples of how to apply this pattern.

**Caution:** We don't recommend a queue with more than 1000 TPS (creates plus dispatches) as it will produce higher delivery latency than normal.

## Queue overload

Queues or queue groups can become overloaded any time traffic increases suddenly. As a result, these queues can experience:

  * Increased task creation latency
  * Increased task creation error rate
  * Reduced dispatch rate



To defend against this, we recommend establishing controls in any situation where the create or dispatch rate of a queue or queue group can spike suddenly. We recommend a maximum of 500 operations per second to a cold queue or queue group, then increasing traffic by 50% every 5 minutes. In theory, you can grow to 740K operations per second after 90 minutes using this ramp up schedule. There are a number of circumstances in which this can occur.

For example:

  * Launching new features that make heavy use of Cloud Tasks
  * Moving traffic between queues
  * Rebalancing traffic across more or fewer queues
  * Running batch jobs that inject large numbers of tasks



In these cases and others, follow the 500/50/5 pattern.

### Initial queue ramp-up

The 500/50/5 pattern applies to queues that are already operating at a steady state. The initial ramp-up for a cold queue is an independent process designed to safely reach that initial steady state.

When a queue is new or has been idle, it doesn't immediately dispatch tasks at its configured [`maxDispatchesPerSecond`](https://docs.cloud.google.com/tasks/docs/reference/rpc/google.cloud.tasks.v2#ratelimits) rate. To protect your system from sudden traffic spikes, Cloud Tasks gradually ramps up the dispatch rate.

If you have a sustained rate of task creation, the system will eventually scale up to your configured dispatch rate. However, if your traffic is spiky, with bursts of tasks separated by more than a week of inactivity, you might notice this ramp-up behavior in particular. This is expected behavior and ensures stability.

### Using App Engine traffic splitting

If the tasks are created by an App Engine app, you can take advantage of App Engine traffic splitting ([Standard](https://docs.cloud.google.com/appengine/docs/standard/java/splitting-traffic)/[Flex](https://docs.cloud.google.com/appengine/docs/flexible/java/splitting-traffic)) to smooth traffic increases. By splitting traffic between versions ([Standard](https://docs.cloud.google.com/appengine/docs/admin-api/deploying-apps)/[Flex](https://docs.cloud.google.com/appengine/docs/flexible/java/testing-and-deploying-your-app)), requests that need to be rate-managed can be spun up over time to protect queue health. As an example, consider the case of spinning up traffic to a newly expanded queue group: Let [_queue0000_ , _queue0199_] be a sequence of high-TPS queues that receive 100,000 TPS creations in total at peak.

Let [_queue0200_ , _queue0399_] be a sequence of new queues. After all traffic has been shifted, the number of queues in the sequence has doubled and the new queue range receives 50% of the sequence's total traffic.

When deploying the version that increases the number of queues, gradually ramp up traffic to the new version, and thus the new queues, using traffic splitting:

  * Start shifting 1% of the traffic to the new release. For example 50% of 1% of 100,000 TPS yields 500 TPS to the set of new queues.
  * Every 5 minutes, increase by 50% the traffic that is sent to the new release, as detailed in the following table:

Minutes since start of the deployment | % of total traffic shifted to the new version | % of total traffic to the new queues | % of total traffic to the old queues  
---|---|---|---  
0 | 1.0 | 0.5 | 99.5  
5 | 1.5 | 0.75 | 99.25  
10 | 2.3 | 1.15 | 98.85  
15 | 3.4 | 1.7 | 98.3  
20 | 5.1 | 2.55 | 97.45  
25 | 7.6 | 3.8 | 96.2  
30 | 11.4 | 5.7 | 94.3  
35 | 17.1 | 8.55 | 91.45  
40 | 25.6 | 12.8 | 87.2  
45 | 38.4 | 19.2 | 80.8  
50 | 57.7 | 28.85 | 71.15  
55 | 86.5 | 43.25 | 56.75  
60 | 100 | 50 | 50  
  
### Release-driven traffic spikes

When launching a release that significantly increases traffic to a queue or queue group, gradual rollout is, again, an important mechanism for smoothing the increases. Gradually roll out your instances such that the initial launch does not exceed 500 total operations to the new queues, increasing by no more than 50% every 5 minutes.

### New High-TPS queues or queue groups

Newly created queues are especially vulnerable. Groups of queues, for example [_queue0000_ , _queue0001_ , …, _queue0199_], are just as sensitive as single queues during the initial rollout stages. For these queues, gradual rollout is an important strategy. Launch new or updated services, which create high-TPS queues or queue groups, in stages such that initial load is below 500 TPS and increases of 50% or less are staged 5 minutes or more apart.

### Newly expanded queue groups

When increasing the total capacity of a queue group, for example expanding [_queue0000_ -_queue0199_ to _queue0000_ -_queue0399_], follow the 500/50/5 pattern. It is important to note that, for rollout procedures, new queue groups behave no differently than individual queues. Apply the 500/50/5 pattern to the new group as a whole, not just to individual queues within the group. For these queues group expansions, gradual rollout is again an important strategy. If the source of your traffic is App Engine, you can use traffic splitting (see Release-Driven Traffic Spikes). When migrating your service to add tasks to the increased number of queues, gradually roll out your instances such that the initial launch does not exceed 500 total operations to the new queues, increasing by no more than 50% every 5 minutes.

### Emergency queue group expansion

On occasion, you might want to expand an existing queue group, for example because tasks are expected to be added to the queue group faster than the group can dispatch them. If the names of the new queues are spread out evenly among your existing queue names when sorted lexicographically, then traffic can be sent immediately to those queues as long as there are no more than 50% new interleaved queues and the traffic to each queue is less than 500 TPS. This method is an alternative to using traffic splitting and gradual rollout as described in the previous sections.

This type of interleaved naming can be achieved by appending a suffix to queues ending in even numbers. For example, if you have 200 existing queues [_queue0000_ -_queue0199_] and want to create 100 new queues, choose [_queue0000a_ , _queue0002a_ , _queue0004a_ , …, _queue0198a_] as the new queue names, instead of [_queue0200_ -_queue0299_].

If you need a further increase, you can still interleave up to 50% more queues every 5 minutes.

### Large-scale/batch task enqueues

When a large number of tasks, for example millions or billions, need to be added, a double-injection pattern can be useful. Instead of creating tasks from a single job, use an injector queue. Each task added to the injector queue fans out and adds 100 tasks to the relevant queue or queue group. The injector queue can be sped up over time, for example start at 5 TPS, then increase by 50% every 5 minutes.

### Named Tasks

When you create a new task, Cloud Tasks assigns the task a unique name by default. You can assign your own name to a task by using the _name_ parameter. However, this introduces significant performance overhead, resulting in increased latencies and potentially increased error rates associated with named tasks. These costs can be magnified significantly if tasks are named sequentially, such as with timestamps. So, if you assign your own names, we recommend using a well-distributed prefix for task names, such as a hash of the contents. [See documentation](https://docs.cloud.google.com/tasks/docs/reference/rpc/google.cloud.tasks.v2#google.cloud.tasks.v2.Task.FIELDS.string.google.cloud.tasks.v2.Task.name) for more details on naming a task.

## Target overload

Cloud Tasks can overload other services that you are using, such as App Engine, Datastore, and your network usage, if dispatches from a queue increase dramatically in a short period of time. If a backlog of tasks has accumulated, then unpausing those queues can potentially overload these services. The recommended defense is the same 500/50/5 pattern suggested for queue overload: if a queue dispatches more than 500 TPS, increase traffic triggered by a queue by no more than 50% every 5 minutes. To monitor your traffic increases proactively, use [Cloud Monitoring metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-cloudtasks). You can use Cloud Monitoring alerts to detect potentially dangerous situations.

### Unpausing or resuming high-TPS queues

When a queue or series of queues is unpaused or re-enabled, queues resume dispatches. If the queue has many tasks, the newly-enabled queue's dispatch rate could increase dramatically from 0 TPS to the full capacity of the queue. To ramp up, stagger queue resumes or control the queue dispatch rates using Cloud Tasks's [`maxDispatchesPerSecond`](https://docs.cloud.google.com/tasks/docs/reference/rpc/google.cloud.tasks.v2#ratelimits).

### Bulk scheduled tasks

Large numbers of tasks, which are scheduled to dispatch at the same time, can also introduce a risk of target overloading. If you need to start a large number of tasks at once, consider using queue rate controls to increase the dispatch rate gradually or explicitly spinning up target capacity in advance.

### Increased fan-out

When updating services that are executed through Cloud Tasks, increasing the number of remote calls can create production risks. For example, say the tasks in a high-TPS queue call the handler `/task-foo`. A new release could significantly increase the cost of calling `/task-foo` if, for example, that new release adds several expensive Datastore calls to the handler. The net result of such a release would be a massive increase in Datastore traffic that is immediately related to changes in user traffic. Use gradual rollout or traffic splitting to manage ramp up.

## Retries

Your code can retry on failure when making Cloud Tasks API calls. However, when a significant proportion of requests are failing with server-side errors, a high rate of retries can overload your queues even more and cause them to recover more slowly. Thus, we recommend capping the amount outgoing traffic if your client detects that a significant proportion of requests are failing with server-side errors, for example using the Adaptive Throttling algorithm described in the _Handling Overload_ chapter of the [Site Reliability Engineering book](https://landing.google.com/sre/book.html). Google's gRPC client libraries implement a [variation of this algorithm](https://github.com/grpc/proposal/blob/master/A6-client-retries.md#throttling-retry-attempts-and-hedged-rpcs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
