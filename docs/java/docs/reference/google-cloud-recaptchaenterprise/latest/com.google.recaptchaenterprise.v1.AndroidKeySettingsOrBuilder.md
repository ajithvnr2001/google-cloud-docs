---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AndroidKeySettingsOrBuilder
title: Interface AndroidKeySettingsOrBuilder (3.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:19.614646+00:00
---

# Interface AndroidKeySettingsOrBuilder (3.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AndroidKeySettingsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AndroidKeySettingsOrBuilder (3.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.96.0 (latest)  3.92.0  3.91.0  3.90.0  3.88.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.77.0  3.75.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.67.0  3.65.0  3.64.0  3.61.0  3.60.0  3.59.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.12  2.6.1  2.5.0  2.4.10  2.3.1 
    
    
    public interface AndroidKeySettingsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAllowAllPackageNames()
    
    
    public abstract boolean getAllowAllPackageNames()

Optional. If set to true, allowed_package_names are not enforced.

`bool allow_all_package_names = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allowAllPackageNames.  
  
### getAllowedPackageNames(int index)
    
    
    public abstract String getAllowedPackageNames(int index)

Optional. Android package names of apps allowed to use the key. Example: 'com.companyname.appname' Each key supports a maximum of 250 package names. To use a key on more apps, set `allow_all_package_names` to true. When this is set, you are responsible for validating the package name by checking the `token_properties.android_package_name` field in each assessment response against your list of allowed package names.

`repeated string allowed_package_names = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The allowedPackageNames at the given index.  
  
### getAllowedPackageNamesBytes(int index)
    
    
    public abstract ByteString getAllowedPackageNamesBytes(int index)

Optional. Android package names of apps allowed to use the key. Example: 'com.companyname.appname' Each key supports a maximum of 250 package names. To use a key on more apps, set `allow_all_package_names` to true. When this is set, you are responsible for validating the package name by checking the `token_properties.android_package_name` field in each assessment response against your list of allowed package names.

`repeated string allowed_package_names = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the allowedPackageNames at the given index.  
  
### getAllowedPackageNamesCount()
    
    
    public abstract int getAllowedPackageNamesCount()

Optional. Android package names of apps allowed to use the key. Example: 'com.companyname.appname' Each key supports a maximum of 250 package names. To use a key on more apps, set `allow_all_package_names` to true. When this is set, you are responsible for validating the package name by checking the `token_properties.android_package_name` field in each assessment response against your list of allowed package names.

`repeated string allowed_package_names = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of allowedPackageNames.  
  
### getAllowedPackageNamesList()
    
    
    public abstract List<String> getAllowedPackageNamesList()

Optional. Android package names of apps allowed to use the key. Example: 'com.companyname.appname' Each key supports a maximum of 250 package names. To use a key on more apps, set `allow_all_package_names` to true. When this is set, you are responsible for validating the package name by checking the `token_properties.android_package_name` field in each assessment response against your list of allowed package names.

`repeated string allowed_package_names = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the allowedPackageNames.  
  
### getSupportNonGoogleAppStoreDistribution()
    
    
    public abstract boolean getSupportNonGoogleAppStoreDistribution()

Optional. Set to true for keys that are used in an Android application that is available for download in app stores in addition to the Google Play Store.

` bool support_non_google_app_store_distribution = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The supportNonGoogleAppStoreDistribution.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
