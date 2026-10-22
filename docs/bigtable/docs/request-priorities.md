---
url: https://docs.cloud.google.com/bigtable/docs/request-priorities/
title: Configure request priorities \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:05.694358+00:00
---

# Configure request priorities  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/request-priorities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure request priorities

To prioritize some traffic to a Bigtable table over other traffic, you can specify an app profile's _request priority_. Bigtable uses the specified request priority to determine the order in which it executes requests.

## Priority levels

All requests sent to Bigtable use an _app profile_ , which stores settings that tell your Bigtable instance how to handle incoming requests. To understand how they work, see [App profiles overview](https://docs.cloud.google.com/bigtable/docs/app-profiles).

You can specify the following request priorities in an app profile:

  * High
  * Medium
  * Low



Higher priority requests are likely to run before lower priority requests.

If you don't specify a priority, all requests are considered high priority by default.

**Note:** Bigtable's scheduling of high priority requests favors operations that take less time to complete, such as simple, single-row read requests that return small payloads on the order of kilobytes.

## Base priority level on workload type

Specify high priority for app profiles that you use for latency-sensitive, serving-path workloads.

Specify medium or low priority for app profiles that you use for workloads that you want to run without impacting the performance of high priority requests. For example, you can make batch read analytics a low priority so that traffic doesn't compete with application-serving traffic that you designate as high priority.

Specify low priority for batch jobs that use [batch write flow control](https://docs.cloud.google.com/bigtable/docs/writes#flow-control).

## Monitor CPU utilization

When you send a mix of high, medium, or low priority traffic, be sure to keep your clusters' CPU utilization below the recommended maximum values. Maintaining lower CPU utilization ensures that lower priority requests aren't [starved](https://en.wikipedia.org/wiki/Starvation_\(computer_science\)). To review the recommended maximums, see [Plan your capacity](https://docs.cloud.google.com/bigtable/docs/performance#planning-your-capacity).

## Configure request priorities

You must use the Google Cloud CLI to specify request priorities. To ensure that you have the most recent version of the gcloud CLI, run the following:
    
    
    gcloud components update
    

When you execute the gcloud CLI commands, replace the following:

  * `APP_PROFILE_ID` \- The permanent identifier for the app profile.
  * `INSTANCE_ID` \- The permanent identifier for the instance.
  * `PRIORITY_LEVEL` \- The priority level that the app profile uses. Accepted values are `PRIORITY_HIGH`, `PRIORITY_MEDIUM`, or `PRIORITY_LOW`.



### Specify a request priority when creating a new app profile

To create an app profile with a specified request priority, run the following command. For the complete list of additional positional arguments and flags that you can use with this command, see [`gcloud bigtable app-profiles create`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/create).
    
    
    gcloud bigtable app-profiles create APP_PROFILE_ID \
        --instance=INSTANCE_ID \
        --route-any \
        --priority=PRIORITY_LEVEL
    

### Add or change an app profile's request priority

To update the priority of an existing app profile, run the following command. For the complete list of additional positional arguments and flags that you can use with this command, see [`gcloud bigtable app-profiles update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/update).
    
    
    gcloud bigtable app-profiles update APP_PROFILE_ID \
        --instance=INSTANCE_ID \
        --route-any \
        --priority=PRIORITY_LEVEL
    

To stop using request priorities for a table, run the command to set the priority to `PRIORITY_HIGH` for every app profile that your applications use to send requests to the table.

## What's next

  * [See examples of replication settings](https://docs.cloud.google.com/bigtable/docs/replication-settings)
  * [Review write-request types](https://docs.cloud.google.com/bigtable/docs/writes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
