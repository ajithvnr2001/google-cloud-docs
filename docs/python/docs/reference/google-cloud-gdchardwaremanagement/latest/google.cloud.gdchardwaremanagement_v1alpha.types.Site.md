---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Site
title: Class Site (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:51.488845+00:00
---

# Class Site (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.Site

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Site (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.3.0  0.2.0  0.1.13 
    
    
    Site(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A physical site where hardware will be installed.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. Name of the site. Format: `projects/{project}/locations/{location}/sites/{site}`  
`display_name` |  `str`   
Optional. Display name of this Site.   
`description` |  `str`   
Optional. Description of this Site.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when this site was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Time when this site was last updated.   
`labels` |  `MutableMapping[str, str]`   
Optional. Labels associated with this site as key value pairs. For more information about labels, see `Create and manage labels   
`organization_contact` |  `[google.cloud.gdchardwaremanagement_v1alpha.types.OrganizationContact](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.OrganizationContact)`   
Required. Contact information for this site.   
`google_maps_pin_uri` |  `str`   
Optional. A URL to the Google Maps address location of the site. An example value is `https://goo.gl/maps/xxxxxxxxx`.   
`access_times` |  `MutableSequence[[google.cloud.gdchardwaremanagement_v1alpha.types.TimePeriod](https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.types.TimePeriod)]`   
Optional. The time periods when the site is accessible. If this field is empty, the site is accessible at all times. This field is used by Google to schedule the initial installation as well as any later hardware maintenance. You may update this at any time. For example, if the initial installation is requested during off-hours but maintenance should be performed during regular business hours, you should update the access times after initial installation is complete.   
`notes` |  `str`   
Optional. Any additional notes for this Site. Please include information about: \- security or access restrictions \- any regulations affecting the technicians visiting the site \- any special process or approval required to move the equipment \- whether a representative will be available during site visits   
`customer_site_id` |  `str`   
Optional. Customer defined identifier for this Site. This can be used to identify the site in the customer's own systems.   
  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
