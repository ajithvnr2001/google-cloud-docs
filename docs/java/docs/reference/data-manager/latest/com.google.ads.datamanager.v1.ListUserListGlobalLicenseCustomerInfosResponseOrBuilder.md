---
url: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListGlobalLicenseCustomerInfosResponseOrBuilder
title: Interface ListUserListGlobalLicenseCustomerInfosResponseOrBuilder (0.20.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:41.548839+00:00
---

# Interface ListUserListGlobalLicenseCustomerInfosResponseOrBuilder (0.20.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ListUserListGlobalLicenseCustomerInfosResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ListUserListGlobalLicenseCustomerInfosResponseOrBuilder (0.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.16.0  0.15.0  0.14.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ListUserListGlobalLicenseCustomerInfosResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getNextPageToken()
    
    
    public abstract String getNextPageToken()

A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
### getUserListGlobalLicenseCustomerInfos(int index)
    
    
    public abstract UserListGlobalLicenseCustomerInfo getUserListGlobalLicenseCustomerInfos(int index)

The customer information for the given license in the request.

` repeated .google.ads.datamanager.v1.UserListGlobalLicenseCustomerInfo user_list_global_license_customer_infos = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserListGlobalLicenseCustomerInfo](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListGlobalLicenseCustomerInfo)` |   
  
### getUserListGlobalLicenseCustomerInfosCount()
    
    
    public abstract int getUserListGlobalLicenseCustomerInfosCount()

The customer information for the given license in the request.

` repeated .google.ads.datamanager.v1.UserListGlobalLicenseCustomerInfo user_list_global_license_customer_infos = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getUserListGlobalLicenseCustomerInfosList()
    
    
    public abstract List<UserListGlobalLicenseCustomerInfo> getUserListGlobalLicenseCustomerInfosList()

The customer information for the given license in the request.

` repeated .google.ads.datamanager.v1.UserListGlobalLicenseCustomerInfo user_list_global_license_customer_infos = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UserListGlobalLicenseCustomerInfo](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListGlobalLicenseCustomerInfo)>` |   
  
### getUserListGlobalLicenseCustomerInfosOrBuilder(int index)
    
    
    public abstract UserListGlobalLicenseCustomerInfoOrBuilder getUserListGlobalLicenseCustomerInfosOrBuilder(int index)

The customer information for the given license in the request.

` repeated .google.ads.datamanager.v1.UserListGlobalLicenseCustomerInfo user_list_global_license_customer_infos = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserListGlobalLicenseCustomerInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.UserListGlobalLicenseCustomerInfoOrBuilder)` |   
  
### getUserListGlobalLicenseCustomerInfosOrBuilderList()
    
    
    public abstract List<? extends UserListGlobalLicenseCustomerInfoOrBuilder> getUserListGlobalLicenseCustomerInfosOrBuilderList()

The customer information for the given license in the request.

` repeated .google.ads.datamanager.v1.UserListGlobalLicenseCustomerInfo user_list_global_license_customer_infos = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.ads.datamanager.v1.UserListGlobalLicenseCustomerInfoOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
