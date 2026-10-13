---
url: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.InterceptEndpointGroupAssociation
title: Class InterceptEndpointGroupAssociation (0.13.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:19.683945+00:00
---

# Class InterceptEndpointGroupAssociation (0.13.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.InterceptEndpointGroupAssociation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class InterceptEndpointGroupAssociation (0.13.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.4 (latest)  0.13.3  0.12.0  0.11.0  0.10.0  0.9.21  0.8.0  0.7.2  0.6.1  0.5.0  0.4.2  0.3.2  0.2.0  0.1.5 
    
    
    InterceptEndpointGroupAssociation(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

An endpoint group association represents a link between a network and an endpoint group in the organization.

Creating an association creates the networking infrastructure linking the network to the endpoint group, but does not enable intercept by itself. To enable intercept, the user must also create a network firewall policy containing intercept rules and associate it with the network.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Immutable. Identifier. The resource name of this endpoint group association, for example: `projects/123456789/locations/global/interceptEndpointGroupAssociations/my-eg-association`. See https://google.aip.dev/122 for more details.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when the resource was created. See https://google.aip.dev/148#timestamps.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The timestamp when the resource was most recently updated. See https://google.aip.dev/148#timestamps.   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels are key/value pairs that help to organize and filter resources.   
`intercept_endpoint_group` |  `str`   
Required. Immutable. The endpoint group that this association is connected to, for example: `projects/123456789/locations/global/interceptEndpointGroups/my-eg`. See https://google.aip.dev/124.   
`network` |  `str`   
Required. Immutable. The VPC network that is associated. for example: `projects/123456789/global/networks/my-network`. See https://google.aip.dev/124.   
`locations_details` |  `MutableSequence[[google.cloud.network_security_v1.types.InterceptEndpointGroupAssociation.LocationDetails](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.InterceptEndpointGroupAssociation.LocationDetails)]`   
Output only. The list of locations where the association is present. This information is retrieved from the linked endpoint group, and not configured as part of the association itself.   
`state` |  `[google.cloud.network_security_v1.types.InterceptEndpointGroupAssociation.State](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.InterceptEndpointGroupAssociation.State)`   
Output only. Current state of the endpoint group association.   
`reconciling` |  `bool`   
Output only. The current state of the resource does not match the user's intended state, and the system is working to reconcile them. This part of the normal operation (e.g. adding a new location to the target deployment group). See https://google.aip.dev/128.   
`locations` |  `MutableSequence[[google.cloud.network_security_v1.types.InterceptLocation](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.InterceptLocation)]`   
Output only. The list of locations where the association is configured. This information is retrieved from the linked endpoint group.   
`network_cookie` |  `int`   
Output only. Identifier used by the data-path. See the NSI GENEVE format for more details: https://docs.cloud.google.com/network-security-integration/docs/understand-geneve#network_id   
  
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
  
### LocationDetails
    
    
    LocationDetails(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Contains details about the state of an association in a specific cloud location.

### State
    
    
    State(value)

The state of the association.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
