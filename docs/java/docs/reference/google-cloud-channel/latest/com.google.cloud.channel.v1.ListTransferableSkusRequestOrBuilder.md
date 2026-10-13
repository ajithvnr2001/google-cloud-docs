---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableSkusRequestOrBuilder
title: Interface ListTransferableSkusRequestOrBuilder (3.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:09.861231+00:00
---

# Interface ListTransferableSkusRequestOrBuilder (3.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableSkusRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ListTransferableSkusRequestOrBuilder (3.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.103.0 (latest)  3.99.0  3.98.0  3.97.0  3.95.0  3.92.0  3.91.0  3.89.0  3.87.0  3.86.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.78.0  3.77.0  3.76.0  3.74.0  3.72.0  3.71.0  3.68.0  3.67.0  3.66.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.6  3.6.1  3.5.1  3.3.1 
    
    
    public interface ListTransferableSkusRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAuthToken()
    
    
    public abstract String getAuthToken()

Optional. The super admin of the resold customer generates this token to authorize a reseller to access their Cloud Identity and purchase entitlements on their behalf. You can omit this token after authorization. See <https://support.google.com/a/answer/7643790> for more details.

`string auth_token = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The authToken.  
  
### getAuthTokenBytes()
    
    
    public abstract ByteString getAuthTokenBytes()

Optional. The super admin of the resold customer generates this token to authorize a reseller to access their Cloud Identity and purchase entitlements on their behalf. You can omit this token after authorization. See <https://support.google.com/a/answer/7643790> for more details.

`string auth_token = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for authToken.  
  
### getCloudIdentityId()
    
    
    public abstract String getCloudIdentityId()

Customer's Cloud Identity ID

`string cloud_identity_id = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cloudIdentityId.  
  
### getCloudIdentityIdBytes()
    
    
    public abstract ByteString getCloudIdentityIdBytes()

Customer's Cloud Identity ID

`string cloud_identity_id = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cloudIdentityId.  
  
### getCustomerName()
    
    
    public abstract String getCustomerName()

A reseller is required to create a customer and use the resource name of the created customer here. Customer_name uses the format: accounts/{account_id}/customers/{customer_id}

`string customer_name = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The customerName.  
  
### getCustomerNameBytes()
    
    
    public abstract ByteString getCustomerNameBytes()

A reseller is required to create a customer and use the resource name of the created customer here. Customer_name uses the format: accounts/{account_id}/customers/{customer_id}

`string customer_name = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for customerName.  
  
### getLanguageCode()
    
    
    public abstract String getLanguageCode()

The BCP-47 language code. For example, "en-US". The response will localize in the corresponding language code, if specified. The default value is "en-US". Optional.

`string language_code = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The languageCode.  
  
### getLanguageCodeBytes()
    
    
    public abstract ByteString getLanguageCodeBytes()

The BCP-47 language code. For example, "en-US". The response will localize in the corresponding language code, if specified. The default value is "en-US". Optional.

`string language_code = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for languageCode.  
  
### getPageSize()
    
    
    public abstract int getPageSize()

The requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 SKUs. The maximum value is 1000; the server will coerce values above 1000. Optional.

`int32 page_size = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pageSize.  
  
### getPageToken()
    
    
    public abstract String getPageToken()

A token for a page of results other than the first page. Obtained using ListTransferableSkusResponse.next_page_token of the previous CloudChannelService.ListTransferableSkus call. Optional.

`string page_token = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pageToken.  
  
### getPageTokenBytes()
    
    
    public abstract ByteString getPageTokenBytes()

A token for a page of results other than the first page. Obtained using ListTransferableSkusResponse.next_page_token of the previous CloudChannelService.ListTransferableSkus call. Optional.

`string page_token = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pageToken.  
  
### getParent()
    
    
    public abstract String getParent()

Required. The reseller account's resource name. Parent uses the format: accounts/{account_id}

`string parent = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The reseller account's resource name. Parent uses the format: accounts/{account_id}

`string parent = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getTransferredCustomerIdentityCase()
    
    
    public abstract ListTransferableSkusRequest.TransferredCustomerIdentityCase getTransferredCustomerIdentityCase()

**Returns**  
---  
**Type** | **Description**  
`[ListTransferableSkusRequest.TransferredCustomerIdentityCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableSkusRequest.TransferredCustomerIdentityCase)` |   
  
### hasCloudIdentityId()
    
    
    public abstract boolean hasCloudIdentityId()

Customer's Cloud Identity ID

`string cloud_identity_id = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudIdentityId field is set.  
  
### hasCustomerName()
    
    
    public abstract boolean hasCustomerName()

A reseller is required to create a customer and use the resource name of the created customer here. Customer_name uses the format: accounts/{account_id}/customers/{customer_id}

`string customer_name = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customerName field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
