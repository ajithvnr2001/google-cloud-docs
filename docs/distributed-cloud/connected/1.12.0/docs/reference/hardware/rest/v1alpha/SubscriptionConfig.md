---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/SubscriptionConfig/
title: SubscriptionConfig \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:24.032489+00:00
---

# SubscriptionConfig  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/SubscriptionConfig/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/apis)



Send feedback 

#  SubscriptionConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SubscriptionState



A message to store a subscription configuration.

JSON representation  
---  
      
    
    {
      "subscriptionId": string,
      "billingId": string,
      "state": enum ([SubscriptionState](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/SubscriptionConfig#SubscriptionState)),
      "startTime": string
    }  
  
Fields  
---  
`subscriptionId` |  `string` Output only. The unique identifier of the subscription.  
`billingId` |  `string` Output only. The Google Cloud Billing ID that the subscription is created under.  
`state` |  `enum (`[SubscriptionState](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs/reference/hardware/rest/v1alpha/SubscriptionConfig#SubscriptionState)`)` Output only. The current state of the subscription.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of the subscription.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## SubscriptionState

Enum to represent the state of the subscription.

Enums  
---  
`SUBSCRIPTION_STATE_UNSPECIFIED` | State is unspecified.  
`ACTIVE` | Active state means that the subscription has been created successfully and billing is happening.  
`INACTIVE` | Inactive means that the subscription has been created successfully, but billing has not started yet.  
`ERROR` | The subscription is in an erroneous state.  
`FAILED_TO_RETRIEVE` | The subscription state failed to be retrieved. This may be a transient issue. The user should retry the request.  
`COMPLETED` | The subscription has been completed, because it has reached the end date.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-07 UTC."],[],[]] 
