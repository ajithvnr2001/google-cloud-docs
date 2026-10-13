---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Zone
title: Class Zone (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:54.347499+00:00
---

# Class Zone (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Zone

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Zone (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.3.0  0.2.0  0.1.13 
    
    
    Zone(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A zone holding a set of hardware.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. Name of this zone. Format: `projects/{project}/locations/{location}/zones/{zone}`  
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when this zone was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when this zone was last updated.   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels associated with this zone as key value pairs. For more information about labels, see `Create and manage labels   
`display_name` |  `str`   
Optional. Human friendly display name of this zone.   
`state` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.Zone.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Zone.State)`   
Output only. Current state for this zone.   
`contacts` |  `MutableSequence[[google.cloud.gdchardwaremanagement_v1alpha.types.Contact](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Contact)]`   
Required. The points of contact.   
`ciq_uri` |  `str`   
Output only. Link to the Customer Intake Questionnaire (CIQ) sheet for this zone.   
`network_config` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.ZoneNetworkConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.ZoneNetworkConfig)`   
Optional. Networking configuration for this zone.   
`globally_unique_id` |  `str`   
Output only. Globally unique identifier generated for this Edge Zone.   
`subscription_configs` |  `MutableSequence[[google.cloud.gdchardwaremanagement_v1alpha.types.SubscriptionConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.SubscriptionConfig)]`   
Output only. Subscription configurations for this zone.   
`provisioning_state` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.Zone.ProvisioningState](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Zone.ProvisioningState)`   
Output only. Provisioning state for configurations like MAC addresses.   
`skip_cluster_provisioning` |  `bool`   
Optional. Whether to skip the cluster provisioning step during factory turnup. If true, indicates that the Kubernetes cluster will be created after the zone's hardware is installed at the customer site.   
`cluster_intent_required` |  `bool`   
Output only. Indicates whether a valid cluster intent must be provided by the customer before accepting the order. If true, the order cannot be accepted until cluster intent is present. This is used to enforce early validation and prevent delays caused by missing configuration.   
`cluster_intent_verified` |  `bool`   
Output only. Indicates whether the provided cluster intent has been successfully verified. This flag ensures cluster intent exists before order can be accepted.   
  
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
  
### ProvisioningState
    
    
    ProvisioningState(value)

Valid provisioning states for configurations like MAC addresses.

### State
    
    
    State(value)

Valid states for a zone.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
