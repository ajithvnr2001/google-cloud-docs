---
url: https://docs.cloud.google.com/python/docs/reference/pubsub/latest/
title: Python Client for Cloud Pub/Sub \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:39:20.714233+00:00
---

# Python Client for Cloud Pub/Sub  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/pubsub/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Python Client for Cloud Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

2.42.0 (latest)  2.41.0  2.40.0  2.39.2  2.38.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0  2.27.3  2.26.1  2.25.2  2.23.1  2.22.0  2.21.5  2.20.3  2.19.8  2.18.4  2.17.1  2.16.1  2.15.2  2.14.1  2.13.12  2.12.1  2.11.1  2.10.0  2.9.0  2.8.0  2.7.1  2.6.1  2.5.0  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.7.2  1.6.1  1.5.0  1.4.3  1.3.1  1.2.0  1.1.0  1.0.2  0.45.0  0.44.0  0.43.0 

[![image](https://img.shields.io/badge/support-stable-gold.svg)](https://github.com/googleapis/google-cloud-python/blob/main/README.rst#stability-levels) [![image](https://img.shields.io/pypi/v/google-cloud-pubsub.svg)](https://pypi.org/project/google-cloud-pubsub/) [![image](https://img.shields.io/pypi/pyversions/google-cloud-pubsub.svg)](https://pypi.org/project/google-cloud-pubsub/)

[Cloud Pub/Sub](https://cloud.google.com/pubsub/docs): Provides reliable, many-to-many, asynchronous messaging between applications.

  * [Client Library Documentation](https://cloud.google.com/python/docs/reference/pubsub/latest/summary_overview)

  * [Product Documentation](https://cloud.google.com/pubsub/docs)




## Quick Start

In order to use this library, you first need to go through the following steps:

  1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)

  2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)

  3. [Enable the Cloud Pub/Sub.](https://cloud.google.com/pubsub/docs)

  4. [Set up Authentication.](https://googleapis.dev/python/google-api-core/latest/auth.html)




### Installation

Install this library in a virtual environment using [venv](https://docs.python.org/3/library/venv.html). [venv](https://docs.python.org/3/library/venv.html) is a tool that creates isolated Python environments. These isolated environments can have separate versions of Python packages, which allows you to isolate one project’s dependencies from the dependencies of other projects.

With [venv](https://docs.python.org/3/library/venv.html), it’s possible to install this library without needing system install permissions, and without clashing with the installed system dependencies.

### Code samples and snippets

Code samples and snippets live in the [samples/](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-pubsub/samples) folder.

#### Supported Python Versions

Our client libraries are compatible with all current [active](https://devguide.python.org/devcycle/#in-development-main-branch) and [maintenance](https://devguide.python.org/devcycle/#maintenance-branches) versions of Python.

Python >= 3.10, including 3.14

#### Unsupported Python Versions

Python <= 3.9

If you are using an [end-of-life](https://devguide.python.org/devcycle/#end-of-life-branches) version of Python, we recommend that you update as soon as possible to an actively supported version.

#### Mac/Linux
    
    
    python3 -m venv <your-env>
    source <your-env>/bin/activate
    pip install google-cloud-pubsub
    

#### Windows
    
    
    py -m venv <your-env>
    .\<your-env>\Scripts\activate
    pip install google-cloud-pubsub
    

### Example Usage

#### Publishing

To publish data to Cloud Pub/Sub you must create a topic, and then publish messages to it
    
    
    import os
    from google.cloud import pubsub_v1
    
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    topic_name = 'projects/{project_id}/topics/{topic}'.format(
        project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
        topic='MY_TOPIC_NAME',  # Set this to something appropriate.
    )
    publisher.create_topic(name=topic_name)
    future = [publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)er.[publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)(topic_name, b'My first message!', spam='eggs')
    future.result()
    

To learn more, consult the [publishing documentation](https://cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.publisher.client.Client).

#### Subscribing

To subscribe to data in Cloud Pub/Sub, you create a subscription based on the topic, and subscribe to that, passing a callback function.
    
    
    import os
    from google.cloud import pubsub_v1
    
    topic_name = 'projects/{project_id}/topics/{topic}'.format(
        project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
        topic='MY_TOPIC_NAME',  # Set this to something appropriate.
    )
    
    subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
        project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),
        sub='MY_SUBSCRIPTION_NAME',  # Set this to something appropriate.
    )
    
    def callback(message):
        print(message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data))
        message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
    with pubsub_v1.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)() as subscriber:
        subscriber.create_subscription(
            name=subscription_name, topic=topic_name)
        future = subscriber.subscribe(subscription_name, callback)
    

The future returned by the call to `subscriber.subscribe` can be used to block the current thread until a given condition obtains:
    
    
    try:
        future.result()
    except KeyboardInterrupt:
        future.cancel()
    

It is also possible to pull messages in a synchronous (blocking) fashion. To learn more about subscribing, consult the [subscriber documentation](https://cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.client.Client).

#### Authentication

It is possible to specify the authentication method to use with the Pub/Sub clients. This can be done by providing an explicit [Credentials](https://google-auth.readthedocs.io/en/latest/reference/google.auth.credentials.html#google.auth.credentials.Credentials) instance. Support for various authentication methods is available from the [google-auth](https://google-auth.readthedocs.io/en/latest/index.html) library.

For example, to use JSON Web Tokens, provide a [google.auth.jwt.Credentials](https://google-auth.readthedocs.io/en/latest/reference/google.auth.jwt.html#google.auth.jwt.Credentials) instance:
    
    
    import json
    from google.auth import jwt
    
    service_account_info = json.load(open("service-account-info.json"))
    audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"
    
    credentials = jwt.Credentials.from_service_account_info(
        service_account_info, audience=audience
    )
    
    subscriber = pubsub_v1.SubscriberClient(credentials=credentials)
    
    # The same for the publisher, except that the "audience" claim needs to be adjusted
    publisher_audience = "https://pubsub.googleapis.com/google.pubsub.v1.Publisher"
    credentials_pub = credentials.with_claims(audience=publisher_audience)
    publisher = pubsub_v1.PublisherClient(credentials=credentials_pub)
    

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

It is currently in major version one (1.y.z), which means that the public API should be considered stable.

## Contributing

Contributions to this library are always welcome and highly encouraged.

See the [CONTRIBUTING doc](https://github.com/googleapis/google-cloud-python/blob/main/CONTRIBUTING.rst) for more information on how to get started.

## Community

The best place to ask questions is via Stackoverflow: <https://stackoverflow.com/questions/tagged/google-cloud-pubsub>

## License

Apache 2.0 - See [the LICENSE](https://github.com/googleapis/google-cloud-python/blob/main/LICENSE) for more information.

### Next Steps

  * Read the [Client Library Documentation](https://cloud.google.com/python/docs/reference/pubsub/latest/summary_overview) for Cloud Pub/Sub to see other available methods on the client.

  * Read the [Cloud Pub/Sub Product documentation](https://cloud.google.com/pubsub/docs) to learn more about the product and see How-to Guides.

  * View this [README](https://github.com/googleapis/google-cloud-python/blob/main/README.rst) to see the full list of Cloud APIs that we cover.




## Logging

This library uses the standard Python `logging` functionality to log some RPC events that could be of interest for debugging and monitoring purposes. Note the following:

  1. Logs may contain sensitive information. Take care to **restrict access to the logs** if they are saved, whether it be on local storage or on Google Cloud Logging.

  2. Google may refine the occurrence, level, and content of various log messages in this library without flagging such changes as breaking. **Do not depend on immutability of the logging events**.

  3. By default, the logging events from this library are not handled. You must **explicitly configure log handling** using one of the mechanisms below.




### Simple, environment-based configuration

To enable logging for this library without any changes in your code, set the `GOOGLE_SDK_PYTHON_LOGGING_SCOPE` environment variable to a valid Google logging scope. This configures handling of logging events (at level `logging.DEBUG` or higher) from this library in a default manner, emitting the logged messages in a structured format. It does not currently allow customizing the logging levels captured nor the handlers, formatters, etc. used for any logging event.

A logging scope is a period-separated namespace that begins with `google`, identifying the Python module or package to log.

  * Valid logging scopes: `google`, `google.cloud.asset.v1`, `google.api`, `google.auth`, etc.

  * Invalid logging scopes: `foo`, `123`, etc.




**NOTE** : If the logging scope is invalid, the library does not set up any logging handlers.

#### Environment-Based Examples

  * Enabling the default handler for all Google-based loggers


    
    
    export GOOGLE_SDK_PYTHON_LOGGING_SCOPE=google
    

  * Enabling the default handler for a specific Google module (for a client library called `library_v1`):


    
    
    export GOOGLE_SDK_PYTHON_LOGGING_SCOPE=google.cloud.library_v1
    

### Advanced, code-based configuration

You can also configure a valid logging scope using Python’s standard logging mechanism.

#### Code-Based Examples

  * Configuring a handler for all Google-based loggers


    
    
    import logging
    
    from google.cloud import library_v1
    
    base_logger = logging.getLogger("google")
    base_logger.addHandler(logging.StreamHandler())
    base_logger.setLevel(logging.DEBUG)
    

  * Configuring a handler for a specific Google module (for a client library called `library_v1`):


    
    
    import logging
    
    from google.cloud import library_v1
    
    base_logger = logging.getLogger("google.cloud.library_v1")
    base_logger.addHandler(logging.StreamHandler())
    base_logger.setLevel(logging.DEBUG)
    

### Logging details

  1. Regardless of which of the mechanisms above you use to configure logging for this library, by default logging events are not propagated up to the root logger from the google-level logger. If you need the events to be propagated to the root logger, you must explicitly set `logging.getLogger("google").propagate = True` in your code.

  2. You can mix the different logging configurations above for different Google modules. For example, you may want use a code-based logging configuration for one library, but decide you need to also set up environment-based logging configuration for another library.

     1. If you attempt to use both code-based and environment-based configuration for the same module, the environment-based configuration will be ineffectual if the code -based configuration gets applied first.
  3. The Google-specific logging configurations (default handlers for environment-based configuration; not propagating logging events to the root logger) get executed the first time _any_ client library is instantiated in your application, and only if the affected loggers have not been previously configured. (This is the reason for 2.i. above.)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
