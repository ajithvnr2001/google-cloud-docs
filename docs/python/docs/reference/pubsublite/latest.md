---
url: https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/
title: Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:39:20.326308+00:00
---

# Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.13.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/)
  * [ 1.12.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.12.0/)
  * [ 1.11.1 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.11.1/)
  * [ 1.10.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.10.0/)
  * [ 1.9.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.9.0/)
  * [ 1.8.3 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.8.3/)
  * [ 1.7.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.7.0/)
  * [ 1.6.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.6.0/)
  * [ 1.5.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.5.0/)
  * [ 1.4.3 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.4.3/)
  * [ 1.3.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.3.0/)
  * [ 1.2.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.2.0/)
  * [ 1.1.4 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.1.4/)
  * [ 1.0.2 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/1.0.2/)
  * [ 0.6.1 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.6.1/)
  * [ 0.5.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.5.0/)
  * [ 0.4.1 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.4.1/)
  * [ 0.3.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.3.0/)
  * [ 0.2.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.2.0/)
  * [ 0.1.0 ](https://docs.cloud.google.com/python/docs/reference/pubsublite/0.1.0/)



# Python Client for Pub/Sub Lite API

[![image](https://img.shields.io/badge/support-stable-gold.svg)](https://github.com/googleapis/google-cloud-python/blob/main/README.rst#stability-levels) [![image](https://img.shields.io/pypi/v/google-cloud-pubsublite.svg)](https://pypi.org/project/google-cloud-pubsublite/) [![image](https://img.shields.io/pypi/pyversions/google-cloud-pubsublite.svg)](https://pypi.org/project/google-cloud-pubsublite/)

[Pub/Sub Lite API](https://cloud.google.com/pubsub/lite): is designed to provide reliable, many-to-many, asynchronous messaging between applications. Publisher applications can send messages to a topic and other applications can subscribe to that topic to receive the messages. By decoupling senders and receivers, Google Cloud Pub/Sub allows developers to communicate between independently written applications.

Compared to Google Pub/Sub, Pub/Sub Lite provides partitioned zonal data storage with predefined capacity. Both products present a similar API, but Pub/Sub Lite has more usage caveats.

See the [Google Pub/Sub Lite docs](about:invalid#zCSafez) for more details on how to activate Pub/Sub Lite for your project, as well as guidance on how to choose between Cloud Pub/Sub and Pub/Sub Lite.

  * [Client Library Documentation](https://cloud.google.com/python/docs/reference/pubsublite/latest)

  * [Product Documentation](https://cloud.google.com/pubsub/lite)




## Quick Start

In order to use this library, you first need to go through the following steps:

  1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)

  2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)

  3. [Enable the Pub/Sub Lite API.](https://cloud.google.com/pubsub/lite)

  4. [Setup Authentication.](https://googleapis.dev/python/google-api-core/latest/auth.html)




### Installation

Install this library in a [virtualenv](https://virtualenv.pypa.io/en/latest/) using pip. [virtualenv](https://virtualenv.pypa.io/en/latest/) is a tool to create isolated Python environments. The basic problem it addresses is one of dependencies and versions, and indirectly permissions.

With [virtualenv](https://virtualenv.pypa.io/en/latest/), it’s possible to install this library without needing system install permissions, and without clashing with the installed system dependencies.

### Code samples and snippets

Code samples and snippets live in the samples/ folder.

#### Supported Python Versions

Our client libraries are compatible with all current [active](https://devguide.python.org/devcycle/#in-development-main-branch) and [maintenance](https://devguide.python.org/devcycle/#maintenance-branches) versions of Python.

Python >= 3.7

#### Unsupported Python Versions

Python <= 3.6

If you are using an [end-of-life](https://devguide.python.org/devcycle/#end-of-life-branches) version of Python, we recommend that you update as soon as possible to an actively supported version.

#### Mac/Linux
    
    
    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install google-cloud-pubsublite
    

#### Windows
    
    
    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-cloud-pubsublite
    

### Next Steps

  * Read the [Client Library Documentation](https://cloud.google.com/python/docs/reference/pubsublite/latest) for Pub/Sub Lite API to see other available methods on the client.

  * Read the [Pub/Sub Lite API Product documentation](https://cloud.google.com/pubsub/lite) to learn more about the product and see How-to Guides.

  * View this [README](https://github.com/googleapis/google-cloud-python/blob/main/README.rst) to see the full list of Cloud APIs that we cover.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
