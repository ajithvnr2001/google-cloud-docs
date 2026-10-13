---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Condition
title: Class Condition (2.77.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:20.203933+00:00
---

# Class Condition (2.77.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Condition

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Condition (2.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.77.0 (latest)  2.73.0  2.72.0  2.71.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.1  2.63.1  2.62.2  2.61.0  2.60.3  2.59.0  2.58.2  2.57.0  2.56.0  2.55.0  2.53.1  2.52.0  2.51.0  2.50.0  2.49.1  2.48.0  2.47.0  2.45.0  2.44.1  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.1  2.37.0  2.36.1  2.35.0  2.33.0  2.32.0  2.31.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.1  2.23.0  2.22.1  2.21.1  2.20.1  2.13.0  2.12.0  2.11.0  2.9.4  2.8.27  2.7.1  2.6.1  2.5.11  2.4.0  2.3.5 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public abstract class Condition

Class for Identity and Access Management (IAM) policies. IAM policies are used to specify access settings for Cloud Platform resources. A policy is a list of bindings. A binding assigns a set of identities to a role, where the identities can be user accounts, Google groups, Google domains, and service accounts. A role is a named list of permissions defined by IAM. See Also: [Policy](https://cloud.google.com/iam/docs/reference/rest/v1/Policy), [IAM Conditions](https://cloud.google.com/iam/docs/conditions-overview)

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Condition

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### newBuilder()
    
    
    public static Condition.Builder newBuilder()

Create a new Condition.Builder

**Returns**  
---  
**Type** | **Description**  
`[Condition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Condition.Builder)` |   
  
## Constructors 

### Condition()
    
    
    public Condition()

## Methods 

### getDescription()
    
    
    public abstract String getDescription()

Get IAM Policy Binding Condition Description

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getExpression()
    
    
    public abstract String getExpression()

Get IAM Policy Binding Condition Expression

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getTitle()
    
    
    public abstract String getTitle()

Get IAM Policy Binding Condition Title

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### toBuilder()
    
    
    public abstract Condition.Builder toBuilder()

Create a new Condition.Builder from an existing Condition

**Returns**  
---  
**Type** | **Description**  
`[Condition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.Condition.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
