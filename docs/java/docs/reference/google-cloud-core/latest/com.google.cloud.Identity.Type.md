---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Identity.Type
title: Class Identity.Type (2.77.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:32.301485+00:00
---

# Class Identity.Type (2.77.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Identity.Type

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Identity.Type (2.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.77.0 (latest)  2.73.0  2.72.0  2.71.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.1  2.63.1  2.62.2  2.61.0  2.60.3  2.59.0  2.58.2  2.57.0  2.56.0  2.55.0  2.53.1  2.52.0  2.51.0  2.50.0  2.49.1  2.48.0  2.47.0  2.45.0  2.44.1  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.1  2.37.0  2.36.1  2.35.0  2.33.0  2.32.0  2.31.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.1  2.23.0  2.22.1  2.21.1  2.20.1  2.13.0  2.12.0  2.11.0  2.9.4  2.8.27  2.7.1  2.6.1  2.5.11  2.4.0  2.3.5 
    
    
    public static final class Identity.Type extends StringEnumValue

The types of IAM identities.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StringEnumValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.StringEnumValue) > Identity.Type

## Inherited Members

[StringEnumValue.equals(Object)](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.StringEnumValue#com_google_cloud_StringEnumValue_equals_java_lang_Object_)

[StringEnumValue.hashCode()](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.StringEnumValue#com_google_cloud_StringEnumValue_hashCode__)

[StringEnumValue.name()](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.StringEnumValue#com_google_cloud_StringEnumValue_name__)

[StringEnumValue.toString()](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.StringEnumValue#com_google_cloud_StringEnumValue_toString__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields 

### ALL_AUTHENTICATED_USERS
    
    
    public static final Identity.Type ALL_AUTHENTICATED_USERS

Represents anyone who is authenticated with a Google account or a service account.

**Field Value**  
---  
**Type** | **Description**  
`[Identity.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Identity.Type)` |   
  
### ALL_USERS
    
    
    public static final Identity.Type ALL_USERS

Represents anyone who is on the internet; with or without a Google account.

**Field Value**  
---  
**Type** | **Description**  
`[Identity.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Identity.Type)` |   
  
### DOMAIN
    
    
    public static final Identity.Type DOMAIN

Represents all the users of a Google Apps domain name.

**Field Value**  
---  
**Type** | **Description**  
`[Identity.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Identity.Type)` |   
  
### GROUP
    
    
    public static final Identity.Type GROUP

Represents a Google group.

**Field Value**  
---  
**Type** | **Description**  
`[Identity.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Identity.Type)` |   
  
### PROJECT_EDITOR
    
    
    public static final Identity.Type PROJECT_EDITOR

Represents editors of a Google Cloud Platform project.

**Field Value**  
---  
**Type** | **Description**  
`[Identity.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Identity.Type)` |   
  
### PROJECT_OWNER
    
    
    public static final Identity.Type PROJECT_OWNER

Represents owners of a Google Cloud Platform project.

**Field Value**  
---  
**Type** | **Description**  
`[Identity.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Identity.Type)` |   
  
### PROJECT_VIEWER
    
    
    public static final Identity.Type PROJECT_VIEWER

Represents viewers of a Google Cloud Platform project.

**Field Value**  
---  
**Type** | **Description**  
`[Identity.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Identity.Type)` |   
  
### SERVICE_ACCOUNT
    
    
    public static final Identity.Type SERVICE_ACCOUNT

Represents a service account.

**Field Value**  
---  
**Type** | **Description**  
`[Identity.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Identity.Type)` |   
  
### USER
    
    
    public static final Identity.Type USER

Represents a specific Google account.

**Field Value**  
---  
**Type** | **Description**  
`[Identity.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Identity.Type)` |   
  
## Static Methods 

### valueOf(String constant)
    
    
    public static Identity.Type valueOf(String constant)

Get the Type for the given String constant, and allow unrecognized values.

**Parameter**  
---  
**Name** | **Description**  
`constant` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Identity.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Identity.Type)` |   
  
### valueOfStrict(String constant)
    
    
    public static Identity.Type valueOfStrict(String constant)

Get the Type for the given String constant, and throw an exception if the constant is not recognized.

**Parameter**  
---  
**Name** | **Description**  
`constant` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Identity.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Identity.Type)` |   
  
### values()
    
    
    public static Identity.Type[] values()

Return the known values for Type.

**Returns**  
---  
**Type** | **Description**  
`[Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Identity.Type)[]` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
