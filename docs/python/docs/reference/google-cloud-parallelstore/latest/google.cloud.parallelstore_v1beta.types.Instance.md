---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.Instance
title: Class Instance (0.6.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:35.860241+00:00
---

# Class Instance (0.6.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.Instance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Instance (0.6.2) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    Instance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A Parallelstore instance.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The resource name of the instance, in the format `projects/{project}/locations/{location}/instances/{instance_id}`.   
`description` |  `str`   
Optional. The description of the instance. 2048 characters or less.   
`state` |  `[google.cloud.parallelstore_v1beta.types.Instance.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.Instance.State)`   
Output only. The instance state.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the instance was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the instance was updated.   
`labels` |  `MutableMapping[str, str]`   
Optional. Cloud Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer's organizational needs and deployment strategies. See https://cloud.google.com/resource-manager/docs/labels-overview for details.   
`capacity_gib` |  `int`   
Required. Immutable. The instance's storage capacity in Gibibytes (GiB). Allowed values are between 12000 and 100000, in multiples of 4000; e.g., 12000, 16000, 20000, ...   
`daos_version` |  `str`   
Output only. Deprecated: The version of DAOS software running in the instance.   
`access_points` |  `MutableSequence[str]`   
Output only. A list of IPv4 addresses used for client side configuration.   
`network` |  `str`   
Optional. Immutable. The name of the Compute Engine `VPC network   
`reserved_ip_range` |  `str`   
Optional. Immutable. The ID of the IP address range being used by the instance's VPC network. See `Configure a VPC network   
`effective_reserved_ip_range` |  `str`   
Output only. Immutable. The ID of the IP address range being used by the instance's VPC network. This field is populated by the service and contains the value currently used by the service.   
`file_stripe_level` |  `[google.cloud.parallelstore_v1beta.types.FileStripeLevel](https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.FileStripeLevel)`   
Optional. Immutable. Stripe level for files. Allowed values are: \- `FILE_STRIPE_LEVEL_MIN`: offers the best performance for small size files. \- `FILE_STRIPE_LEVEL_BALANCED`: balances performance for workloads involving a mix of small and large files. \- `FILE_STRIPE_LEVEL_MAX`: higher throughput performance for larger files.   
`directory_stripe_level` |  `[google.cloud.parallelstore_v1beta.types.DirectoryStripeLevel](https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.DirectoryStripeLevel)`   
Optional. Immutable. Stripe level for directories. Allowed values are: \- `DIRECTORY_STRIPE_LEVEL_MIN`: recommended when directories contain a small number of files. \- `DIRECTORY_STRIPE_LEVEL_BALANCED`: balances performance for workloads involving a mix of small and large directories. \- `DIRECTORY_STRIPE_LEVEL_MAX`: recommended for directories with a large number of files.   
`deployment_type` |  `[google.cloud.parallelstore_v1beta.types.DeploymentType](https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.DeploymentType)`   
Optional. Immutable. The deployment type of the instance. Allowed values are: \- `SCRATCH`: the instance is a scratch instance. \- `PERSISTENT`: the instance is a persistent instance.   
  
## Classes 

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### State
    
    
    State(value)

The possible states of a Parallelstore instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
