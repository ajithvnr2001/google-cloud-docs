---
url: https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1BlockingPublisherConnection/
title: Class BlockingPublisherConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:09.688709+00:00
---

# Class BlockingPublisherConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1BlockingPublisherConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class BlockingPublisherConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

A connection to the Cloud Pub/Sub service to publish events. 

This interface defines pure-virtual methods for each of the user-facing overload sets in [`BlockingPublisher`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1BlockingPublisher). That is, all of [`BlockingPublisher`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1BlockingPublisher)'s overloads will forward to the one pure-virtual method declared in this interface. This allows users to inject custom behavior (e.g., with a Google Mock object) in a [`BlockingPublisher`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1BlockingPublisher) object for use in their own tests.

To create a concrete instance that connects you to the real Cloud Pub/Sub service, see [`MakeBlockingPublisherConnection()`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/namespacegoogle_1_1cloud_1_1pubsub).

###### The *Params nested classes

Applications may define classes derived from [`PublisherConnection`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1PublisherConnection), for example, because they want to mock the class. To avoid breaking all such derived classes when we change the number or type of the arguments to the member functions we define lightweight structures to pass the arguments. 

## Functions 

### virtual Publish(PublishParams)

Defines the interface for [`BlockingPublisher::Publish()`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1BlockingPublisher#classgoogle_1_1cloud_1_1pubsub_1_1BlockingPublisher_1a37e3aae927a3fb1fa2e83f1663d621a1)

**Parameter**  
---  
**Name** | **Description**  
`p` |  `PublishParams`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< std::string >` |   
  
### virtual options()

Returns the options configured at initialization time. 

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
