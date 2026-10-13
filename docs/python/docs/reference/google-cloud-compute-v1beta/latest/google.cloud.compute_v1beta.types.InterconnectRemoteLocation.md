---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InterconnectRemoteLocation
title: Class InterconnectRemoteLocation (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:25.687289+00:00
---

# Class InterconnectRemoteLocation (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InterconnectRemoteLocation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class InterconnectRemoteLocation (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    InterconnectRemoteLocation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a Cross-Cloud Interconnect Remote Location resource. You can use this resource to find remote location details about an Interconnect attachment (VLAN).

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`address` |  `str`   
Output only. [Output Only] The postal address of the Point of Presence, each line in the address is separated by a newline character. This field is a member of `oneof`_ `_address`.   
`attachment_configuration_constraints` |  `[google.cloud.compute_v1beta.types.InterconnectAttachmentConfigurationConstraints](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InterconnectAttachmentConfigurationConstraints)`   
Output only. [Output Only] Subset of fields from InterconnectAttachment's \|configurationConstraints\| field that apply to all attachments for this remote location. This field is a member of `oneof`_ `_attachment_configuration_constraints`.   
`city` |  `str`   
Output only. [Output Only] Metropolitan area designator that indicates which city an interconnect is located. For example: "Chicago, IL", "Amsterdam, Netherlands". This field is a member of `oneof`_ `_city`.   
`constraints` |  `[google.cloud.compute_v1beta.types.InterconnectRemoteLocationConstraints](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InterconnectRemoteLocationConstraints)`   
Output only. [Output Only] Constraints on the parameters for creating Cross-Cloud Interconnect and associated InterconnectAttachments. This field is a member of `oneof`_ `_constraints`.   
`continent` |  `str`   
Output only. [Output Only] Continent for this location, which can take one of the following values: :: \- AFRICA \- ASIA_PAC \- EUROPE \- NORTH_AMERICA \- SOUTH_AMERICA Check the Continent enum for the list of possible values. This field is a member of `oneof`_ `_continent`.   
`creation_timestamp` |  `str`   
Output only. [Output Only] Creation timestamp inRFC3339 text format. This field is a member of `oneof`_ `_creation_timestamp`.   
`description` |  `str`   
Output only. [Output Only] An optional description of the resource. This field is a member of `oneof`_ `_description`.   
`facility_provider` |  `str`   
Output only. [Output Only] The name of the provider for this facility (e.g., EQUINIX). This field is a member of `oneof`_ `_facility_provider`.   
`facility_provider_facility_id` |  `str`   
Output only. [Output Only] A provider-assigned Identifier for this facility (e.g., Ashburn-DC1). This field is a member of `oneof`_ `_facility_provider_facility_id`.   
`id` |  `int`   
Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server. This field is a member of `oneof`_ `_id`.   
`kind` |  `str`   
Output only. [Output Only] Type of the resource. Alwayscompute#interconnectRemoteLocation for interconnect remote locations. This field is a member of `oneof`_ `_kind`.   
`lacp` |  `str`   
Output only. [Output Only] Link Aggregation Control Protocol (LACP) constraints, which can take one of the following values: LACP_SUPPORTED, LACP_UNSUPPORTED Check the Lacp enum for the list of possible values. This field is a member of `oneof`_ `_lacp`.   
`max_lag_size100_gbps` |  `int`   
Output only. [Output Only] The maximum number of 100 Gbps ports supported in a link aggregation group (LAG). When linkType is 100 Gbps, requestedLinkCount cannot exceed max_lag_size_100_gbps. This field is a member of `oneof`_ `_max_lag_size100_gbps`.   
`max_lag_size10_gbps` |  `int`   
Output only. [Output Only] The maximum number of 10 Gbps ports supported in a link aggregation group (LAG). When linkType is 10 Gbps, requestedLinkCount cannot exceed max_lag_size_10_gbps. This field is a member of `oneof`_ `_max_lag_size10_gbps`.   
`max_lag_size400_gbps` |  `int`   
Output only. [Output Only] The maximum number of 400 Gbps ports supported in a link aggregation group (LAG). When linkType is 400 Gbps, requestedLinkCount cannot exceed max_lag_size_400_gbps. This field is a member of `oneof`_ `_max_lag_size400_gbps`.   
`name` |  `str`   
Output only. [Output Only] Name of the resource. This field is a member of `oneof`_ `_name`.   
`peeringdb_facility_id` |  `str`   
Output only. [Output Only] The peeringdb identifier for this facility (corresponding with a netfac type in peeringdb). This field is a member of `oneof`_ `_peeringdb_facility_id`.   
`permitted_connections` |  `MutableSequence[[google.cloud.compute_v1beta.types.InterconnectRemoteLocationPermittedConnections](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InterconnectRemoteLocationPermittedConnections)]`   
Output only. [Output Only] Permitted connections.   
`remote_service` |  `str`   
Output only. [Output Only] Indicates the service provider present at the remote location. Example values: "Amazon Web Services", "Microsoft Azure". This field is a member of `oneof`_ `_remote_service`.   
`self_link` |  `str`   
Output only. [Output Only] Server-defined URL for the resource. This field is a member of `oneof`_ `_self_link`.   
`status` |  `str`   
Output only. [Output Only] The status of this InterconnectRemoteLocation, which can take one of the following values: :: \- CLOSED: The InterconnectRemoteLocation is closed and is unavailable for provisioning new Cross-Cloud Interconnects. \- AVAILABLE: The InterconnectRemoteLocation is available for provisioning new Cross-Cloud Interconnects. Check the Status enum for the list of possible values. This field is a member of `oneof`_ `_status`.   
  
## Classes 

### Continent
    
    
    Continent(value)

Output only. [Output Only] Continent for this location, which can take one of the following values:

::

  * AFRICA
  * ASIA_PAC
  * EUROPE
  * NORTH_AMERICA
  * SOUTH_AMERICA



### Lacp
    
    
    Lacp(value)

Output only. [Output Only] Link Aggregation Control Protocol (LACP) constraints, which can take one of the following values: LACP_SUPPORTED, LACP_UNSUPPORTED

### Status
    
    
    Status(value)

Output only. [Output Only] The status of this InterconnectRemoteLocation, which can take one of the following values:

::

  * CLOSED: The InterconnectRemoteLocation is closed and is unavailable for provisioning new Cross-Cloud Interconnects.
  * AVAILABLE: The InterconnectRemoteLocation is available for provisioning new Cross-Cloud Interconnects.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
