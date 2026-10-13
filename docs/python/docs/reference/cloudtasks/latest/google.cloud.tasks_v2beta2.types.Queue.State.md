---
url: https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Queue.State
title: Class State (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:40.527222+00:00
---

# Class State (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Queue.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class State (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.3  2.18.0  2.17.1  2.16.5  2.15.1  2.14.2  2.13.2  2.12.1  2.11.0  2.10.4  2.9.1  2.8.1  2.7.2  2.6.0  2.5.3  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.5.2  1.4.0  1.3.0  1.2.1 
    
    
    State(value)

State of the queue.
    
    
        If the queue was created using Cloud Tasks and the queue has
        had no activity (method calls or task dispatches) for 30
        days, the queue may take a few minutes to re-activate. Some
        method calls may return
        `NOT_FOUND][google.rpc.Code.NOT_FOUND]` and tasks may not be
        dispatched for a few minutes until the queue has been
        re-activated.
    PAUSED (2):
        Tasks are paused by the user. If the queue is paused then
        Cloud Tasks will stop delivering tasks from it, but more
        tasks can still be added to it by the user. When a pull
        queue is paused, all
        <xref uid="google.cloud.tasks.v2beta2.CloudTasks.LeaseTasks">LeaseTasks</xref>
        calls will return a
        `FAILED_PRECONDITION][google.rpc.Code.FAILED_PRECONDITION]`.
    DISABLED (3):
        The queue is disabled.
    
        A queue becomes `DISABLED` when
        `queue.yaml <https://cloud.google.com/appengine/docs/python/config/queueref>`__
        or
        `queue.xml <https://cloud.google.com/appengine/docs/standard/java/config/queueref>`__
        is uploaded which does not contain the queue. You cannot
        directly disable a queue.
    
        When a queue is disabled, tasks can still be added to a
        queue but the tasks are not dispatched and
        <xref uid="google.cloud.tasks.v2beta2.CloudTasks.LeaseTasks">LeaseTasks</xref>
        calls return a `FAILED_PRECONDITION` error.
    
        To permanently delete this queue and all of its tasks, call
        <xref uid="google.cloud.tasks.v2beta2.CloudTasks.DeleteQueue">DeleteQueue</xref>.
    

## Enums  
  
---  
**Name** | **Description**  
`STATE_UNSPECIFIED` | Unspecified state.  
`RUNNING` | The queue is running. Tasks can be dispatched.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
