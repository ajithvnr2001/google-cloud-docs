---
url: https://docs.cloud.google.com/php/docs/reference/cloud-networkservices/latest/V1beta1.DeleteExtensionBindingRequest
title: Google Cloud Network Services V1beta1 Client - Class DeleteExtensionBindingRequest (0.13.1) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:44.124390+00:00
---

# Google Cloud Network Services V1beta1 Client - Class DeleteExtensionBindingRequest (0.13.1)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-networkservices/latest/V1beta1.DeleteExtensionBindingRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Network Services V1beta1 Client - Class DeleteExtensionBindingRequest (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.10.0  0.8.2  0.7.1  0.6.1  0.5.0  0.4.0  0.3.0  0.2.3  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Network Services V1beta1 Client class DeleteExtensionBindingRequest.

Request used by the `DeleteExtensionBinding` method.

Generated from protobuf message `google.cloud.networkservices.v1beta1.DeleteExtensionBindingRequest`

## Namespace

Google \ Cloud \ NetworkServices \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Required. A name of the `ExtensionBinding` resource to delete. Must be in the format `projects/{project}/locations/{location}/extensionBindings/{extension_binding}`.  
`↳ etag` |  `string`   
Optional. The etag of the ExtensionBinding to delete.  
  
### getName

Required. A name of the `ExtensionBinding` resource to delete. Must be in the format `projects/{project}/locations/{location}/extensionBindings/{extension_binding}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Required. A name of the `ExtensionBinding` resource to delete. Must be in the format `projects/{project}/locations/{location}/extensionBindings/{extension_binding}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEtag

Optional. The etag of the ExtensionBinding to delete.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEtag

Optional. The etag of the ExtensionBinding to delete.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
Required. A name of the `ExtensionBinding` resource to delete. Must be in the format `projects/{project}/locations/{location}/extensionBindings/{extension_binding}`. Please see DepServiceClient::extensionBindingName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[DeleteExtensionBindingRequest](https://docs.cloud.google.com/php/docs/reference/cloud-networkservices/latest/V1beta1.DeleteExtensionBindingRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
