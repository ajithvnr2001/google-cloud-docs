---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-Event-DetailedState/
title: Service Health V1 API - Module Google::Cloud::ServiceHealth::V1::Event::DetailedState (v2.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:55.648970+00:00
---

# Service Health V1 API - Module Google::Cloud::ServiceHealth::V1::Event::DetailedState (v2.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-Event-DetailedState/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Service Health V1 API - Module Google::Cloud::ServiceHealth::V1::Event::DetailedState (v2.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.5.1 (latest)  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.1  1.1.0  1.0.2  0.2.0  0.1.2 

Reference documentation and code samples for the Service Health V1 API module Google::Cloud::ServiceHealth::V1::Event::DetailedState.

The detailed state of the incident. This enum lists all possible detailed states of an incident.

## Constants 

### DETAILED_STATE_UNSPECIFIED

**value:** 0  
Unspecified detail state.

### EMERGING

**value:** 1  
Google engineers are actively investigating the event to determine the impact.

### CONFIRMED

**value:** 2  
The incident is confirmed and impacting at least one Google Cloud product. Ongoing status updates will be provided until it is resolved.

### RESOLVED

**value:** 3  
The incident is no longer affecting any Google Cloud product, and there will be no further updates.

### MERGED

**value:** 4  
The incident was merged into a parent incident. All further updates will be published to the parent only. The `parent_event` field contains the name of the parent.

### AUTO_CLOSED

**value:** 9  
The incident was automatically closed because of the following reasons:

  * The impact of the incident could not be confirmed.
  * The incident was intermittent or resolved itself.



The incident does not have a resolution because no action or investigation happened. If it is intermittent, the incident may reopen.

### FALSE_POSITIVE

**value:** 10  
Upon investigation, Google engineers concluded that the incident is not affecting a Google Cloud product. This state can change if the incident is reviewed again.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
