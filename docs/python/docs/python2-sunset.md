---
url: https://docs.cloud.google.com/python/docs/python2-sunset/
title: Python 2 support on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:33.639134+00:00
---

# Python 2 support on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/python2-sunset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Guides ](https://docs.cloud.google.com/python/docs/setup)



Send feedback 

#  Python 2 support on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

The Python community announced that it will [sunset Python 2](https://www.python.org/doc/sunset-python-2/) on January 1, 2020, and are encouraging all developers to upgrade to Python 3 as soon as they can. In recognition that customers may need more time to migrate from Python 2 to Python 3, **Google Cloud customers will be able to run Python 2 apps and use existing Python 2[client libraries](https://github.com/googleapis/google-cloud-python#google-cloud-python-client) after January 1, 2020.**

Managed compute services, such as App Engine, will continue to provide a Python 2 runtime beyond January 1, 2020. Python 2 client libraries will continue to be available for download, but future major releases will only target Python 3.

This page provides a summary of Python 2 and 3 support across Google Cloud and will provide resources to help you migrate to Python 3. We will keep this page updated with the latest resources and information.

## Python 2 support status

### Google Cloud Python Client Libraries

New major versions of [Python client libraries](https://github.com/googleapis/google-cloud-python#google-cloud-python-client) released after January 1, 2020 will not support Python 2.7. Previous major versions will remain available for download, allowing access to existing service endpoints, and will support users currently developing for Python 2.7.

If a vulnerability is detected in an old library version or in a library dependency of an old library version there is no plan to release a patch.

### App Engine Python 2.7 Runtime

We are committed to providing long term support for the App Engine Python 2.7 runtime, continuing our more than decade-long history of supporting your apps as you move to the future at your own pace.

To support the Python 2.7 runtime for the long term, we will make the following changes over time:

  * Return the runtimes to their unforked, open-source states as much as possible. We had to heavily restrict and modify some of the runtimes to securely run your apps in our data centers. By making changes to how we operate the runtimes in our data centers, we can provide a secure and scalable environment for these runtimes over the long term.

  * Add full build systems that support package repositories, native component builds, and asset repositories.




For more information on the long term support of the App Engine Python 2.7 runtime, see the [App Engine long term support plan](https://docs.cloud.google.com/appengine/docs/standard/long-term-support)) More migration information is available for [migrating to the Python 3 standard runtime](https://docs.cloud.google.com/appengine/docs/standard/python/migrate-to-python3).

### Google Cloud CLI

[Google Cloud CLI version 274.0.0](https://docs.cloud.google.com/sdk/docs/release-notes#27400_2019-12-17) introduces support for Python 3. Older versions of the gcloud CLI will remain [available for download](https://docs.cloud.google.com/sdk/docs/downloads-versioned-archives), but we recommend using version 274.0.0 or newer and migrating to Python 3 as soon as possible.

For instructions on how to configure the gcloud CLI to use Python 3, see [Using Python 3](https://cloud.google.com/sdk/gcloud/reference/topic/startup).

Some Python tools other than the gcloud CLI that are shipped in the Google Cloud CLI still require a Python 2.7 interpreter. For details, run: [`gcloud topic startup`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/startup).

### Deployment Manager templates

We expect that most Deployment Manager templates will continue to work with Python 3. If you use additional Python code with your templates, such as helper scripts or template modules, make sure that they are compatible with Python 3.

For information on what to expect during the transition from Python 2.7 to 3.x, see the [Deployment Manager documentation](https://docs.cloud.google.com/deployment-manager/docs/migrate-to-python3).

### Dataflow

As of October 7, 2020, Dataflow [no longer supports Python 2 pipelines](https://docs.cloud.google.com/dataflow/docs/support/using-unsupported-sdks). Due to both the industry shift and the discontinuation of Python 2 support in Apache Beam, Dataflow cannot guarantee long-term functional support or maintenance of the Python 2 offering.

You can run existing Python batch and streaming pipelines on Python 3 using the most recent Apache Beam SDK. We recommend checking that your pipeline code is compatible with Python 3 by following the [Porting Python 2 Code to Python 3 documentation](https://docs.python.org/3/howto/pyporting.html).

For known issues related to the Apache Beam Python 3 migration, refer to the FAQ on the [BEAM-1251](https://issues.apache.org/jira/browse/BEAM-1251) tracker. For more information on the support status of Apache Beam 2.x SDKs, see the [SDK version support status page](https://docs.cloud.google.com/dataflow/docs/support/sdk-version-support-status#apache-beam-2x-sdks).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
