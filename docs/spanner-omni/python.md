---
url: https://docs.cloud.google.com/spanner-omni/python/
title: Use the Python client library to connect to Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:34.384457+00:00
---

# Use the Python client library to connect to Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/python/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Use the Python client library to connect to Spanner Omni Stay organized with collections  Save and categorize content based on your preferences. 

The Python client library for Spanner works with Spanner Omni in the same way it works with Spanner. This document shows you how to establish secure connections to Spanner Omni by configuring the Python client library. You establish these connections by setting client options when you create a client.

The Python client library supports plain text, TLS, TLS with credentials, and mTLS connections.

For more information, see [Get started with Spanner in Python](https://docs.cloud.google.com/spanner/docs/getting-started/python) in the Spanner documentation.

## Before you begin

To use the Python client library with Spanner Omni, use the [Python client library](https://docs.cloud.google.com/python/docs/reference/spanner/latest) version 3.72.0 or later.

To install the Spanner Omni Python package, run the following command:
    
    
    pip install google-cloud-spanner>=3.72.0
    

## Configure the `Client` object

When configuring the [`Client`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client) object, specify the Spanner Omni endpoint in `client_options` and specify `instance_type=InstanceType.OMNI`.

The following examples show how to configure the `Client` object for each supported security configuration:

###  Plain text 

To establish a plain-text connection, specify `instance_type=InstanceType.OMNI` and `use_plain_text=True`:
    
    
    from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
    from google.cloud.spanner_v1 import [InstanceType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance.InstanceType.html)
    
    spanner_client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)(
        client_options={"api_endpoint": "ENDPOINT"},
        instance_type=[InstanceType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance.InstanceType.html).OMNI,
        use_plain_text=True,
    )
    

Replace the following:

  * `ENDPOINT`: the endpoint of your Spanner Omni instance.



###  TLS 

To establish a TLS connection, specify the path to your CA certificate using `ca_certificate`:
    
    
    from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
    from google.cloud.spanner_v1 import [InstanceType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance.InstanceType.html)
    
    spanner_client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)(
        client_options={"api_endpoint": "ENDPOINT"},
        instance_type=[InstanceType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance.InstanceType.html).OMNI,
        ca_certificate="PATH_TO_CA_CERT",
    )
    

Replace the following:

  * `ENDPOINT`: the endpoint of your Spanner Omni instance.

  * `PATH_TO_CA_CERT`: the path to your CA certificate file.




###  TLS with credentials 

To establish a TLS connection with username and password authentication, specify the `username` and `password` parameters alongside the CA certificate:
    
    
    from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
    from google.cloud.spanner_v1 import [InstanceType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance.InstanceType.html)
    
    spanner_client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)(
        client_options={"api_endpoint": "ENDPOINT"},
        instance_type=[InstanceType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance.InstanceType.html).OMNI,
        ca_certificate="PATH_TO_CA_CERT",
        username="USERNAME",
        password="PASSWORD",
    )
    

Replace the following:

  * `ENDPOINT`: the endpoint of your Spanner Omni instance.

  * `PATH_TO_CA_CERT`: the path to your CA certificate file.

  * `USERNAME`: the username for your Spanner Omni user.

  * `PASSWORD`: the password for your Spanner Omni user.




###  mTLS 

To establish a mutual TLS (mTLS) connection, specify the CA certificate, client certificate, and private client key:
    
    
    from google.cloud import [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html)
    from google.cloud.spanner_v1 import [InstanceType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance.InstanceType.html)
    
    spanner_client = [spanner](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.html).[Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client.html)(
        client_options={"api_endpoint": "ENDPOINT"},
        instance_type=[InstanceType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance.InstanceType.html).OMNI,
        ca_certificate="PATH_TO_CA_CERT",
        client_certificate="PATH_TO_CLIENT_CERT",
        client_key="PATH_TO_CLIENT_KEY",
    )
    

Replace the following:

  * `ENDPOINT`: the endpoint of your Spanner Omni instance.

  * `PATH_TO_CA_CERT`: the path to your CA certificate file.

  * `PATH_TO_CLIENT_CERT`: the path to your client certificate file.

  * `PATH_TO_CLIENT_KEY`: the path to your client private key file.




## Get a database

After you configure the `Client` object, you can get a database. Because Spanner Omni does not use Google Cloud project or instance IDs, specify `default` for the instance ID when you create an `Instance`:
    
    
    instance = spanner_client.instance("default")
    database = instance.database("DATABASE_ID")
    

Replace the following:

  * `DATABASE_ID`: the ID of your Spanner Omni database.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
