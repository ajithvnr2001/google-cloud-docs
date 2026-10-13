---
url: https://docs.cloud.google.com/static/python/docs/reference/firestore/latest/google.cloud.firestore_bundle.bundle
title: Module bundle (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:30.522140+00:00
---

# Module bundle (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/static/python/docs/reference/firestore/latest/google.cloud.firestore_bundle.bundle

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module bundle (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 

Classes for representing bundles for the Google Cloud Firestore API.

## Classes 

### [FirestoreBundle](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_bundle.bundle.FirestoreBundle)
    
    
    FirestoreBundle(name: str)

A group of serialized documents and queries, suitable for longterm storage or query resumption.

If any queries are added to this bundle, all associated documents will be loaded and stored in memory for serialization.

Usage:
    
    
    from google.cloud.firestore import [Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client.html), _helpers
    from google.cloud.firestore_bundle import FirestoreBundle
    
    db = Client()
    bundle = FirestoreBundle('my-bundle')
    bundle.[add_named_query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_bundle.bundle.FirestoreBundle.html#google_cloud_firestore_bundle_bundle_FirestoreBundle_add_named_query)('all-users', db.[collection](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client.html#google_cloud_firestore_v1_client_Client_collection)('users')._query())
    bundle.[add_named_query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_bundle.bundle.FirestoreBundle.html#google_cloud_firestore_bundle_bundle_FirestoreBundle_add_named_query)(
        'top-ten-hamburgers',
        db.[collection](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client.html#google_cloud_firestore_v1_client_Client_collection)('hamburgers').limit(limit=10),
    )
    serialized: str = bundle.[build](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_bundle.bundle.FirestoreBundle.html#google_cloud_firestore_bundle_bundle_FirestoreBundle_build)()
    
    # Store somewhere like a Google Cloud Storage bucket for retrieval by
    # a client SDK.
    

**Parameter**  
---  
**Name** | **Description**  
`name` |  `str`   
The Id of the bundle.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
