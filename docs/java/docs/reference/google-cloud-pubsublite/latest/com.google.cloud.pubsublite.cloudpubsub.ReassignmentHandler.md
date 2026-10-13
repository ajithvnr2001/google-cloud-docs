---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.ReassignmentHandler
title: Interface ReassignmentHandler (1.16.5) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:17.317746+00:00
---

# Interface ReassignmentHandler (1.16.5)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.ReassignmentHandler

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReassignmentHandler (1.16.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.5 (latest)  1.16.2  1.15.21  1.14.8  1.13.8  1.12.22  1.11.2  1.10.0  1.9.4  1.8.0  1.7.1  1.6.3  1.5.5  1.4.12 
    
    
    public interface ReassignmentHandler

A ReassignmentHandler is called any time a new partition assignment is received from the server. It will be called with both the previous and new assignments as decided by the backend.

The client library will not acknowledge the assignment until handleReassignment returns. The assigning backend will not assign any of the partitions in `before` to another server unless the assignment is acknowledged, or a client takes too long to acknowledged (currently 30 seconds from the time the assignment is sent from server's point of view).

Because of the above, as long as reassignment handling is processed quickly, it can be used to abort outstanding operations on partitions which are being assigned away from this client.

## Methods 

### handleReassignment(Set<Partition> before, Set<Partition> after)
    
    
    public abstract void handleReassignment(Set<Partition> before, Set<Partition> after)

Called with the previous and new assignment delivered to this client on an assignment change. The assignment will not be acknowledged until this method returns, so it should complete quickly, or the backend will assume it is non-responsive and assign all partitions away without waiting for acknowledgement.

handleReassignment will only be called after no new messages will be delivered for the partition.

Acks or nacks on messages from partitions being assigned away will have no effect.

**Parameters**  
---  
**Name** | **Description**  
`before` | `[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[Partition](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Partition)>`  
the previous assignment  
`after` | `[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[Partition](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Partition)>`  
the new assignment  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-26 UTC."],[],[]] 
