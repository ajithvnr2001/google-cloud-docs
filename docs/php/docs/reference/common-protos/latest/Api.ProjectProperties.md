---
url: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.ProjectProperties
title: Google API Common Protos Client - Class ProjectProperties (4.14.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:23.384470+00:00
---

# Google API Common Protos Client - Class ProjectProperties (4.14.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.ProjectProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Common Protos Client - Class ProjectProperties (4.14.3) Stay organized with collections  Save and categorize content based on your preferences. 

4.14.3 (latest)  4.14.1  4.13.0  4.12.5  4.11.0  4.10.0  4.9.0  4.8.3 

Reference documentation and code samples for the Google API Common Protos Client class ProjectProperties.

A descriptor for defining project properties for a service. One service may have many consumer projects, and the service may want to behave differently depending on some properties on the project. For example, a project may be associated with a school, or a business, or a government agency, a business type property on the project may affect how a service responds to the client.

This descriptor defines which properties are allowed to be set on a project. Example: project_properties: properties:

  * name: NO_WATERMARK type: BOOL description: Allows usage of the API without watermarks.
  * name: EXTENDED_TILE_CACHE_PERIOD type: INT64



Generated from protobuf message `google.api.ProjectProperties`

## Namespace

Google \ Api

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ properties` |  `array<[Property](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.Property)>`   
List of per consumer project-specific properties.  
  
### getProperties

List of per consumer project-specific properties.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField.html)<[Property](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.Property)>` |   
  
### setProperties

List of per consumer project-specific properties.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[Property](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.Property)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
