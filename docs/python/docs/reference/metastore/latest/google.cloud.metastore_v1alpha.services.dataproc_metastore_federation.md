---
url: https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1alpha.services.dataproc_metastore_federation
title: Package dataproc_metastore_federation (1.24.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:26.667671+00:00
---

# Package dataproc_metastore_federation (1.24.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1alpha.services.dataproc_metastore_federation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package dataproc_metastore_federation (1.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.24.0 (latest)  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.3  1.17.0  1.16.1  1.15.5  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.3  1.5.1  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.3.3  0.2.2  0.1.0 

API documentation for `metastore_v1alpha.services.dataproc_metastore_federation` package.

## Classes 

### [DataprocMetastoreFederationAsyncClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1alpha.services.dataproc_metastore_federation.DataprocMetastoreFederationAsyncClient)

Configures and manages metastore federation services. Dataproc Metastore Federation Service allows federating a collection of backend metastores like BigQuery, Dataplex Lakes, and other Dataproc Metastores. The Federation Service exposes a gRPC URL through which metadata from the backend metastores are served at query time.

The Dataproc Metastore Federation API defines the following resource model:

  * The service works with a collection of Google Cloud projects.
  * Each project has a collection of available locations.
  * Each location has a collection of federations.
  * Dataproc Metastore Federations are resources with names of the form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.



### [DataprocMetastoreFederationClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1alpha.services.dataproc_metastore_federation.DataprocMetastoreFederationClient)

Configures and manages metastore federation services. Dataproc Metastore Federation Service allows federating a collection of backend metastores like BigQuery, Dataplex Lakes, and other Dataproc Metastores. The Federation Service exposes a gRPC URL through which metadata from the backend metastores are served at query time.

The Dataproc Metastore Federation API defines the following resource model:

  * The service works with a collection of Google Cloud projects.
  * Each project has a collection of available locations.
  * Each location has a collection of federations.
  * Dataproc Metastore Federations are resources with names of the form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.



## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1alpha.services.dataproc_metastore_federation.pagers)

API documentation for `metastore_v1alpha.services.dataproc_metastore_federation.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
