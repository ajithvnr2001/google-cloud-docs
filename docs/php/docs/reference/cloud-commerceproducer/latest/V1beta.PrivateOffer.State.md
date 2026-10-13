---
url: https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.PrivateOffer.State
title: Google Cloud Commerce Producer V1beta Client - Class State (0.2.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:15:01.328403+00:00
---

# Google Cloud Commerce Producer V1beta Client - Class State (0.2.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-commerceproducer/latest/V1beta.PrivateOffer.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Commerce Producer V1beta Client - Class State (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.2.0 (latest)  0.1.3 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Commerce Producer V1beta Client class State.

State of an offer.

Protobuf type `google.cloud.commerceproducer.v1beta.PrivateOffer.State`

## Namespace

Google \ Cloud \ CommerceProducer \ V1beta \ PrivateOffer

## Methods 

### static::name

**Parameter**  
---  
**Name** | **Description**  
`value` |  `mixed`   
  
  
### static::value

**Parameter**  
---  
**Name** | **Description**  
`name` |  `mixed`   
  
  
## Constants 

### STATE_UNSPECIFIED
    
    
    Value: 0

Default value. This value is unused.

Generated from protobuf enum `STATE_UNSPECIFIED = 0;`

### DRAFT
    
    
    Value: 1

The default state after creation when the offer can be edited.

In all other states, the contents of the offer cannot be edited.

Generated from protobuf enum `DRAFT = 1;`

### PUBLISHING
    
    
    Value: 2

The offer is publishing.

Publishing will complete when all publishing requirements are satisfied.

Generated from protobuf enum `PUBLISHING = 2;`

### PUBLISHED
    
    
    Value: 3

The offer has been published and is available to the customer to accept.

Generated from protobuf enum `PUBLISHED = 3;`

### ACCEPTED
    
    
    Value: 4

The offer has been accepted by the customer.

Generated from protobuf enum `ACCEPTED = 4;`

### CANCELLED
    
    
    Value: 5

The offer was cancelled by the provider before it was transacted.

Cancelled offers can no longer be accepted by the customer.

Generated from protobuf enum `CANCELLED = 5;`

### EXPIRED
    
    
    Value: 6

The offer expired without being accepted by the customer.

Expired offers can no longer be accepted by the customer.

Generated from protobuf enum `EXPIRED = 6;`

### ENDED
    
    
    Value: 7

The offer has ended.

Ended offers were accepted and active in the past, but have now reached the end of their term or have been terminated.

Generated from protobuf enum `ENDED = 7;`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
