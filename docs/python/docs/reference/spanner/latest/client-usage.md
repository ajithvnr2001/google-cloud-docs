---
url: https://docs.cloud.google.com/python/docs/reference/spanner/latest/client-usage/
title: Spanner Client Usage \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:48.853716+00:00
---

# Spanner Client Usage  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/spanner/latest/client-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Spanner Client Usage Stay organized with collections  Save and categorize content based on your preferences. 

3.71.0 (latest)  3.70.0  3.69.1  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.1  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.0  3.23.0  3.22.2  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.1  3.14.1  3.13.0  3.12.1  3.11.1  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.1.1  2.0.0  1.19.3  1.18.0  1.17.1  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0 

## Instantiating a Client

To use the API, the [`Client`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/client#google.cloud.spanner_v1.client.Client) class defines a high-level interface which handles authorization and creating other objects:
    
    
    from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
    client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)()
    

## Configuration

  * For an overview of authentication in `google.cloud-python`, see [Authentication](https://googleapis.dev/python/google-api-core/latest/auth.html).

  * In addition to any authentication configuration, you can also set the `GCLOUD_PROJECT` environment variable for the Google Cloud Console project you’d like to interact with. If your code is running in Google App Engine or Google Compute Engine the project will be detected automatically. (Setting this environment variable is not required, you may instead pass the `project` explicitly when constructing a [`Client`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/client#google.cloud.spanner_v1.client.Client)).

  * After configuring your environment, create a [`Client`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/client#google.cloud.spanner_v1.client.Client)



    
    
    >>> from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
    >>> client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)()
    

or pass in `credentials` and `project` explicitly
    
    
    >>> from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
    >>> client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)(project='my-project', credentials=creds)
    

## Using a Cloud Spanner Emulator

There are two ways to use the client with a Cloud Spanner emulator: programmatically or via an environment variable.

To programmatically use an emulator, you must specify the project, the endpoint of the emulator, and use anonymous credentials:
    
    
    from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
    from google.auth.credentials import AnonymousCredentials
    
    client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)(
        project='my-project',
        client_options={"api_endpoint": "0.0.0.0:9010"},
        credentials=AnonymousCredentials()
    )
    

To use an emulator via an environment variable, set the SPANNER_EMULATOR_HOST environment variable to the emulator endpoint:
    
    
    export SPANNER_EMULATOR_HOST=0.0.0.0:9010
    

## Next Step

After a [`Client`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/client#google.cloud.spanner_v1.client.Client), the next highest-level object is an [`Instance`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/instance#google.cloud.spanner_v1.instance.Instance). You’ll need one before you can interact with databases.

Next, learn about the [Instance Admin Usage](https://docs.cloud.google.com/python/docs/reference/spanner/latest/instance-usage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
