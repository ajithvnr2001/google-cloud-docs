---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instance-Liveness-LivenessState/
title: App Engine Admin V1 API - Module Google::Cloud::AppEngine::V1::Instance::Liveness::LivenessState (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:27.683648+00:00
---

# App Engine Admin V1 API - Module Google::Cloud::AppEngine::V1::Instance::Liveness::LivenessState (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instance-Liveness-LivenessState/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Module Google::Cloud::AppEngine::V1::Instance::Liveness::LivenessState (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API module Google::Cloud::AppEngine::V1::Instance::Liveness::LivenessState.

Liveness health check status for Flex instances.

## Constants 

### LIVENESS_STATE_UNSPECIFIED

**value:** 0  
There is no liveness health check for the instance. Only applicable for instances in App Engine standard environment.

### UNKNOWN

**value:** 1  
The health checking system is aware of the instance but its health is not known at the moment.

### HEALTHY

**value:** 2  
The instance is reachable i.e. a connection to the application health checking endpoint can be established, and conforms to the requirements defined by the health check.

### UNHEALTHY

**value:** 3  
The instance is reachable, but does not conform to the requirements defined by the health check.

### DRAINING

**value:** 4  
The instance is being drained. The existing connections to the instance have time to complete, but the new ones are being refused.

### TIMEOUT

**value:** 5  
The instance is unreachable i.e. a connection to the application health checking endpoint cannot be established, or the server does not respond within the specified timeout.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
