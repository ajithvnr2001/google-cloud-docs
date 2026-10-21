---
url: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/State/
title: State \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:11:46.341519+00:00
---

# State  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/State/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Reference ](https://docs.cloud.google.com/fault-injection-testing/apis)



Send feedback 

#  State Stay organized with collections  Save and categorize content based on your preferences. 

Represents the current state of an `Experiment` or `Validation` dry run. String values are used in JSON.

Enums  
---  
`STATE_UNSPECIFIED` | The state is not known or not set.  
`PREPARING` | The system is identifying the target Google Cloud resources for the `Experiment` or `Validation` and checking necessary permissions.  
`PREPARED` | The experiment is fully set up and ready to start.  
`INJECTING` | The system is actively applying the fault to the targeted resources. Example: Slowing down responses, triggering errors.  
`INJECTED` | The fault is active on the targeted resources. The `Experiment` is now running for its planned duration.  
`REVERTING` | The `Experiment` is being stopped, and FIT is removing the fault and restoring the resources to their normal operational state.  
`COMPLETED` | The `Experiment` or `Validation` has finished, and the resources are back to their normal state. No further actions will occur.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-21 UTC."],[],[]] 
