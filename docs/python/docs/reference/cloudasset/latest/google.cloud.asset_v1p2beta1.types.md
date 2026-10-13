---
url: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types
title: Package types (4.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:42.864471+00:00
---

# Package types (4.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.30.1  3.29.2  3.28.0  3.27.1  3.26.4  3.25.1  3.24.3  3.23.0  3.22.0  3.21.0  3.20.1  3.19.1  3.18.1  3.17.1  3.16.0  3.15.0  3.14.2  3.13.1  3.12.0  3.11.0  3.10.0  3.9.1  3.8.1  3.7.1  3.6.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.0  2.2.2  2.1.0  2.0.0  1.3.2  1.2.0  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 

API documentation for `asset_v1p2beta1.types` package.

## Classes 

### [Asset](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.Asset)

An asset in Google Cloud. An asset can be any resource in the Google Cloud `resource hierarchy <https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy>`**, a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. IAM policy). See`Supported asset types <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`** for more information.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchGetAssetsHistoryResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.BatchGetAssetsHistoryResponse)

Batch get assets history response.

### [ContentType](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.ContentType)

Asset content type.

### [CreateFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.CreateFeedRequest)

Create asset feed request.

### [DeleteFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.DeleteFeedRequest)

### [ExportAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.ExportAssetsResponse)

The export asset response. This message is returned by the `google.longrunning.Operations.GetOperation][google.longrunning.Operations.GetOperation]` method in the returned `google.longrunning.Operation.response][google.longrunning.Operation.response]` field.

### [Feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.Feed)

An asset feed used to export asset updates to a destinations. An asset feed filter controls what updates are exported. The asset feed must be created within a project, organization, or folder. Supported destinations are:

Cloud Pub/Sub topics.

### [FeedOutputConfig](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.FeedOutputConfig)

Output configuration for asset feed destination.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GcsDestination](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.GcsDestination)

A Cloud Storage location.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GetFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.GetFeedRequest)

Get asset feed request.

### [ListFeedsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.ListFeedsRequest)

List asset feeds request.

### [ListFeedsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.ListFeedsResponse)

### [OutputConfig](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.OutputConfig)

Output configuration for export assets destination.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PubsubDestination](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.PubsubDestination)

A Pub/Sub destination.

### [Resource](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.Resource)

A representation of a Google Cloud resource.

### [TemporalAsset](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.TemporalAsset)

An asset in Google Cloud and its temporal metadata, including the time window when it was observed and its status during that window.

### [TimeWindow](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.TimeWindow)

A time window specified by its `start_time` and `end_time`.

### [UpdateFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.UpdateFeedRequest)

Update asset feed request.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
