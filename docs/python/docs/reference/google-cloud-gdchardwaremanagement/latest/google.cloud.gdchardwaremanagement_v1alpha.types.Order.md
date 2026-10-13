---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order
title: Class Order (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:49.350369+00:00
---

# Class Order (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Order (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.3.0  0.2.0  0.1.13 
    
    
    Order(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An order for GDC hardware.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. Name of this order. Format: `projects/{project}/locations/{location}/orders/{order}`  
`display_name` |  `str`   
Optional. Display name of this order.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when this order was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when this order was last updated.   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels associated with this order as key value pairs. For more information about labels, see `Create and manage labels   
`state` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.Order.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order.State)`   
Output only. State of this order. On order creation, state will be set to DRAFT.   
`organization_contact` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.OrganizationContact](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.OrganizationContact)`   
Required. Customer contact information.   
`target_workloads` |  `MutableSequence[str]`   
Optional. Customer specified workloads of interest targeted by this order. This must contain <= 20="" elements="" and="" the="" length="" of="" each="" element="" must="" be=""><= 50="" characters.="">  
`customer_motivation` |  `str`   
Required. Information about the customer's motivation for this order. The length of this field must be <= 1000="" characters.="">  
`fulfillment_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Deprecated: Please use customer_requested_installation_date instead.   
`customer_requested_installation_date` |  `google.type.date_pb2.Date`   
Optional. Customer requested installation date for this order.   
`region_code` |  `str`   
Required. `Unicode CLDR `__ region code where this order will be deployed. For a list of valid CLDR region codes, see the `Language Subtag Registry   
`order_form_uri` |  `str`   
Output only. Link to the order form.   
`type_` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.Order.Type](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order.Type)`   
Output only. Type of this Order.   
`submit_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when the order was submitted. Is auto-populated to the current time when an order is submitted.   
`billing_id` |  `str`   
Output only. The Google Cloud Billing ID to be charged for this order.   
`existing_hardware` |  `MutableSequence[[google.cloud.gdchardwaremanagement_v1alpha.types.HardwareLocation](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.HardwareLocation)]`   
Optional. Existing hardware to be removed as part of this order. Note: any hardware removed will be recycled unless otherwise agreed.   
`deployment_type` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.Order.DeploymentType](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Order.DeploymentType)`   
Output only. The deployment type of this order.   
`actual_installation_date` |  `google.type.date_pb2.Date`   
Output only. Actual installation date for this order.   
`estimated_installation_date` |  `google.type.date_pb2.Date`   
Output only. Estimated installation date for this order.   
`estimated_delivery_date` |  `google.type.date_pb2.Date`   
Output only. Estimated delivery date for this order.   
`migration` |  `bool`   
Optional. Whether this order is a migration from customer's existing infrastructure.   
`accepted_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the order was moved to ACCEPTED state.   
`requested_date_change` |  `google.type.date_pb2.Date`   
Output only. The date to which the customer or Google wants to set the scheduled installation date.   
`vendor_notes` |  `str`   
Output only. Notes for this order, provided by the vendor.   
`vendor_contact` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.OrganizationContact](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.OrganizationContact)`   
Output only. Contact information of the SI assigned to this order.   
  
## Classes 

### DeploymentType
    
    
    DeploymentType(value)

Valid types of a deployment.

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

Valid states of an order.

### Type
    
    
    Type(value)

Valid types of an Order.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
