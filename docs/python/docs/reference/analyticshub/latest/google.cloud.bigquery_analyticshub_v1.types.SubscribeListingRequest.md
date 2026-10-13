---
url: https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_analyticshub_v1.types.SubscribeListingRequest
title: Class SubscribeListingRequest (0.6.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:15:33.860089+00:00
---

# Class SubscribeListingRequest (0.6.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_analyticshub_v1.types.SubscribeListingRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SubscribeListingRequest (0.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.9.0  0.8.0  0.7.0  0.6.0  0.5.20  0.4.20  0.3.2  0.2.1  0.1.1 
    
    
    SubscribeListingRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message for subscribing to a listing.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`destination_dataset` |  `[google.cloud.bigquery_analyticshub_v1.types.DestinationDataset](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_analyticshub_v1.types.DestinationDataset)`   
Input only. BigQuery destination dataset to create for the subscriber. This field is a member of `oneof`_ `destination`.   
`destination_pubsub_subscription` |  `[google.cloud.bigquery_analyticshub_v1.types.DestinationPubSubSubscription](https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_analyticshub_v1.types.DestinationPubSubSubscription)`   
Input only. Destination Pub/Sub subscription to create for the subscriber. This field is a member of `oneof`_ `destination`.   
`name` |  `str`   
Required. Resource name of the listing that you want to subscribe to. e.g. `projects/myproject/locations/us/dataExchanges/123/listings/456`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
