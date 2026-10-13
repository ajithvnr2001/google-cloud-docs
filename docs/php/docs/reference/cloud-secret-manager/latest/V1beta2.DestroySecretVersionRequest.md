---
url: https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.DestroySecretVersionRequest
title: Secret Manager V1beta2 Client - Class DestroySecretVersionRequest (2.5.4) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:00:40.420130+00:00
---

# Secret Manager V1beta2 Client - Class DestroySecretVersionRequest (2.5.4)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.DestroySecretVersionRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Secret Manager V1beta2 Client - Class DestroySecretVersionRequest (2.5.4) Stay organized with collections  Save and categorize content based on your preferences. 

2.5.4 (latest)  2.4.0  2.3.0  2.2.2  2.1.1  2.0.2  1.15.4  1.13.0  1.12.3  1.11.0  1.10.4  1.9.7 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Secret Manager V1beta2 Client class DestroySecretVersionRequest.

Request message for [SecretManagerService.DestroySecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.Client.SecretManagerServiceClient#_Google_Cloud_SecretManager_V1beta2_Client_SecretManagerServiceClient__destroySecretVersion__).

Generated from protobuf message `google.cloud.secretmanager.v1beta2.DestroySecretVersionRequest`

## Namespace

Google \ Cloud \ SecretManager \ V1beta2

## Methods 

### __construct

Constructor.

**Parameter**  
---  
**Name** | **Description**  
`data` |  `mixed`   
  
  
### getName

Required. The resource name of the [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion) to destroy in the format `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Required. The resource name of the [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion) to destroy in the format `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEtag

Optional. Etag of the [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion). The request succeeds if it matches the etag of the currently stored secret version object. If the etag is omitted, the request succeeds.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEtag

Optional. Etag of the [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion). The request succeeds if it matches the etag of the currently stored secret version object. If the etag is omitted, the request succeeds.

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
Required. The resource name of the [SecretVersion](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.SecretVersion) to destroy in the format `projects/*/secrets/*/versions/*` or `projects/*/locations/*/secrets/*/versions/*`. Please see SecretManagerServiceClient::secretVersionName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[DestroySecretVersionRequest](https://docs.cloud.google.com/php/docs/reference/cloud-secret-manager/latest/V1beta2.DestroySecretVersionRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
