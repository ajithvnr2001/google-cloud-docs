---
url: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Asset
title: Class Asset (4.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:21.932328+00:00
---

# Class Asset (4.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Asset

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Asset (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.30.1  3.29.2  3.28.0  3.27.1  3.26.4  3.25.1  3.24.3  3.23.0  3.22.0  3.21.0  3.20.1  3.19.1  3.18.1  3.17.1  3.16.0  3.15.0  3.14.2  3.13.1  3.12.0  3.11.0  3.10.0  3.9.1  3.8.1  3.7.1  3.6.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.0  2.2.2  2.1.0  2.0.0  1.3.2  1.2.0  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 
    
    
    Asset(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An asset in Google Cloud. An asset can be any resource in the Google Cloud `resource hierarchy <https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy>`**, a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. IAM policy), or a relationship (e.g. an INSTANCE_TO_INSTANCEGROUP relationship). See`Supported asset types <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`** for more information.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The last update timestamp of an asset. update_time is updated when create/update/delete operation is performed.   
`name` |  `str`   
The full name of the asset. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1` See `Resource names   
`asset_type` |  `str`   
The type of the asset. Example: `compute.googleapis.com/Disk` See `Supported asset types   
`resource` |  `[google.cloud.asset_v1.types.Resource](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Resource)`   
A representation of the resource.   
`iam_policy` |  `google.iam.v1.policy_pb2.Policy`   
A representation of the IAM policy set on a Google Cloud resource. There can be a maximum of one IAM policy set on any given resource. In addition, IAM policies inherit their granted access scope from any policies set on parent resources in the resource hierarchy. Therefore, the effectively policy is the union of both the policy set on this resource and each policy set on all of the resource's ancestry resource levels in the hierarchy. See `this topic   
`org_policy` |  `MutableSequence[google.cloud.orgpolicy.v1.orgpolicy_pb2.Policy]`   
A representation of an `organization policy   
`access_policy` |  `google.identity.accesscontextmanager.v1.access_policy_pb2.AccessPolicy`   
Also refer to the `access policy user guide   
`access_level` |  `google.identity.accesscontextmanager.v1.access_level_pb2.AccessLevel`   
Also refer to the `access level user guide   
`service_perimeter` |  `google.identity.accesscontextmanager.v1.service_perimeter_pb2.ServicePerimeter`   
Also refer to the `service perimeter user guide   
`os_inventory` |  `google.cloud.osconfig_v1.types.Inventory`   
A representation of runtime OS Inventory information. See `this topic   
`related_assets` |  `[google.cloud.asset_v1.types.RelatedAssets](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.RelatedAssets)`   
DEPRECATED. This field only presents for the purpose of backward-compatibility. The server will never generate responses with this field. The related assets of the asset of one relationship type. One asset only represents one type of relationship.   
`related_asset` |  `[google.cloud.asset_v1.types.RelatedAsset](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.RelatedAsset)`   
One related asset of the current asset.   
`ancestors` |  `MutableSequence[str]`   
The ancestry path of an asset in Google Cloud `resource hierarchy   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
