---
url: https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client
title: Module publisher_client (1.13.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:38.584627+00:00
---

# Module publisher_client (1.13.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module publisher_client (1.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.13.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 1.12.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.12.0/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 1.11.1 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.11.1/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 1.10.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.10.0/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 1.9.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.9.0/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 1.8.3 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.8.3/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 1.7.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.7.0/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 1.6.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.6.0/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 1.5.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.5.0/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 1.4.3 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.4.3/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 1.3.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.3.0/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 1.2.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.2.0/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 1.1.4 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.1.4/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 1.0.2 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.0.2/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 0.6.1 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.6.1/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 0.5.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.5.0/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 0.4.1 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.4.1/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 0.3.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.3.0/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 0.2.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.2.0/google.cloud.pubsublite.cloudpubsub.publisher_client)
  * [ 0.1.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.1.0/google.cloud.pubsublite.cloudpubsub.publisher_client)



API documentation for `pubsublite.cloudpubsub.publisher_client` module.

## Classes 

### [AsyncPublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.AsyncPublisherClient)
    
    
    AsyncPublisherClient(
        *,
        per_partition_batching_settings: typing.Optional[
            google.cloud.pubsub_v1.types.BatchSettings
        ] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: str = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        enable_idempotence: bool = False
    )

An AsyncPublisherClient publishes messages similar to Google Pub/Sub, but must be used in an async context. Any publish failures are unlikely to succeed if retried.

Must be used in an `async with` block or have **aenter**() awaited before use.

### [PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient)
    
    
    PublisherClient(
        *,
        per_partition_batching_settings: typing.Optional[
            google.cloud.pubsub_v1.types.BatchSettings
        ] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: str = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        enable_idempotence: bool = False
    )

A PublisherClient publishes messages similar to Google Pub/Sub. Any publish failures are unlikely to succeed if retried.

Must be used in a `with` block or have **enter**() called before use.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
