---
url: https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v1.types.Node.State
title: Class State (1.28.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:48.302246+00:00
---

# Class State (1.28.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v1.types.Node.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class State (1.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.28.0 (latest)  1.27.0  1.26.0  1.25.0  1.24.0  1.23.2  1.22.0  1.21.0  1.20.0  1.19.1  1.18.5  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.2  1.10.1  1.9.0  1.8.0  1.7.2  1.6.0  1.5.2  1.4.1  1.3.4  1.2.1  1.1.0  1.0.2  0.2.2  0.1.0 
    
    
    State(value)

Represents the different states of a TPU node during its lifecycle.

## Enums  
  
---  
**Name** | **Description**  
`STATE_UNSPECIFIED` | TPU node state is not known/set.  
`CREATING` | TPU node is being created.  
`READY` | TPU node has been created.  
`RESTARTING` | TPU node is restarting.  
`REIMAGING` | TPU node is undergoing reimaging.  
`DELETING` | TPU node is being deleted.  
`REPAIRING` | TPU node is being repaired and may be unusable. Details can be found in the `help_description` field.  
`STOPPED` | TPU node is stopped.  
`STOPPING` | TPU node is currently stopping.  
`STARTING` | TPU node is currently starting.  
`PREEMPTED` | TPU node has been preempted. Only applies to Preemptible TPU Nodes.  
`TERMINATED` | TPU node has been terminated due to maintenance or has reached the end of its life cycle (for preemptible nodes).  
`HIDING` | TPU node is currently hiding.  
`HIDDEN` | TPU node has been hidden.  
`UNHIDING` | TPU node is currently unhiding.  
`UNKNOWN` | TPU node has unknown state after a failed repair.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
