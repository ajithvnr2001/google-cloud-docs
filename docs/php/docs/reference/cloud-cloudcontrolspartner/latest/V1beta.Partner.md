---
url: https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.Partner
title: Google Cloud Cloud Controls Partner V1beta Client - Class Partner (0.6.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:24.128900+00:00
---

# Google Cloud Cloud Controls Partner V1beta Client - Class Partner (0.6.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.Partner

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Cloud Controls Partner V1beta Client - Class Partner (0.6.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.3 (latest)  0.5.3  0.4.1  0.3.0  0.2.2  0.1.4 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Cloud Controls Partner V1beta Client class Partner.

Message describing Partner resource

Generated from protobuf message `google.cloud.cloudcontrolspartner.v1beta.Partner`

## Namespace

Google \ Cloud \ CloudControlsPartner \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Identifier. The resource name of the partner. Format: `organizations/{organization}/locations/{location}/partner` Example: "organizations/123456/locations/us-central1/partner"  
`↳ skus` |  `array<[Sku](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.Sku)>`   
List of SKUs the partner is offering  
`↳ ekm_solutions` |  `array<[EkmMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.EkmMetadata)>`   
List of Google Cloud supported EKM partners supported by the partner  
`↳ operated_cloud_regions` |  `string[]`   
List of Google Cloud regions that the partner sells services to customers. Valid Google Cloud regions found here: <https://cloud.google.com/compute/docs/regions-zones>  
`↳ partner_project_id` |  `string`   
Google Cloud project ID in the partner's Google Cloud organization for receiving enhanced Logs for Partners.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. Time the resource was created  
`↳ update_time` |  `Google\Protobuf\Timestamp`   
Output only. The last time the resource was updated  
  
### getName

Identifier. The resource name of the partner.

Format: `organizations/{organization}/locations/{location}/partner` Example: "organizations/123456/locations/us-central1/partner"

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. The resource name of the partner.

Format: `organizations/{organization}/locations/{location}/partner` Example: "organizations/123456/locations/us-central1/partner"

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSkus

List of SKUs the partner is offering

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[Sku](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.Sku)>` |   
  
### setSkus

List of SKUs the partner is offering

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[Sku](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.Sku)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEkmSolutions

List of Google Cloud supported EKM partners supported by the partner

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[EkmMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.EkmMetadata)>` |   
  
### setEkmSolutions

List of Google Cloud supported EKM partners supported by the partner

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[EkmMetadata](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.EkmMetadata)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOperatedCloudRegions

List of Google Cloud regions that the partner sells services to customers.

Valid Google Cloud regions found here: <https://cloud.google.com/compute/docs/regions-zones>

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setOperatedCloudRegions

List of Google Cloud regions that the partner sells services to customers.

Valid Google Cloud regions found here: <https://cloud.google.com/compute/docs/regions-zones>

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPartnerProjectId

Google Cloud project ID in the partner's Google Cloud organization for receiving enhanced Logs for Partners.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPartnerProjectId

Google Cloud project ID in the partner's Google Cloud organization for receiving enhanced Logs for Partners.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. Time the resource was created

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. Time the resource was created

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Output only. The last time the resource was updated

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Output only. The last time the resource was updated

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
