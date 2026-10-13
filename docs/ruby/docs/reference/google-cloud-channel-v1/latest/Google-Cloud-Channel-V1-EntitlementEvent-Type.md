---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementEvent-Type/
title: Cloud Channel V1 API - Module Google::Cloud::Channel::V1::EntitlementEvent::Type (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:21.335231+00:00
---

# Cloud Channel V1 API - Module Google::Cloud::Channel::V1::EntitlementEvent::Type (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-channel-v1/latest/Google-Cloud-Channel-V1-EntitlementEvent-Type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Channel V1 API - Module Google::Cloud::Channel::V1::EntitlementEvent::Type (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.24.0  0.23.2  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.5 

Reference documentation and code samples for the Cloud Channel V1 API module Google::Cloud::Channel::V1::EntitlementEvent::Type.

Type of entitlement event.

## Constants 

### TYPE_UNSPECIFIED

**value:** 0  
Not used.

### CREATED

**value:** 1  
A new entitlement was created.

### PRICE_PLAN_SWITCHED

**value:** 3  
The offer type associated with an entitlement was changed. This is not triggered if an entitlement converts from a commit offer to a flexible offer as part of a renewal.

### COMMITMENT_CHANGED

**value:** 4  
Annual commitment for a commit plan was changed.

### RENEWED

**value:** 5  
An annual entitlement was renewed.

### SUSPENDED

**value:** 6  
Entitlement was suspended.

### ACTIVATED

**value:** 7  
Entitlement was unsuspended.

### CANCELLED

**value:** 8  
Entitlement was cancelled.

### SKU_CHANGED

**value:** 9  
Entitlement was upgraded or downgraded (e.g. from Google Workspace Business Standard to Google Workspace Business Plus).

### RENEWAL_SETTING_CHANGED

**value:** 10  
The renewal settings of an entitlement has changed.

### PAID_SERVICE_STARTED

**value:** 11  
Paid service has started on trial entitlement.

### LICENSE_ASSIGNMENT_CHANGED

**value:** 12  
License was assigned to or revoked from a user.

### LICENSE_CAP_CHANGED

**value:** 13  
License cap was changed for the entitlement.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
