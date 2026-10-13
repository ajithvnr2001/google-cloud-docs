---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.EnvironmentOrBuilder
title: Interface EnvironmentOrBuilder (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:11.808209+00:00
---

# Interface EnvironmentOrBuilder (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.EnvironmentOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface EnvironmentOrBuilder (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 
    
    
    public interface EnvironmentOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsSecretVariables(String key)
    
    
    public abstract boolean containsSecretVariables(String key)

A map of environment variable names to Secret Manager secret names. The VM will access the named secrets to set the value of each environment variable.

`map<string, string> secret_variables = 2;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsVariables(String key)
    
    
    public abstract boolean containsVariables(String key)

A map of environment variable names to values.

`map<string, string> variables = 1;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getEncryptedVariables()
    
    
    public abstract Environment.KMSEnvMap getEncryptedVariables()

An encrypted JSON dictionary where the key/value pairs correspond to environment variable names and their values.

`.google.cloud.batch.v1.Environment.KMSEnvMap encrypted_variables = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Environment.KMSEnvMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Environment.KMSEnvMap)` | The encryptedVariables.  
  
### getEncryptedVariablesOrBuilder()
    
    
    public abstract Environment.KMSEnvMapOrBuilder getEncryptedVariablesOrBuilder()

An encrypted JSON dictionary where the key/value pairs correspond to environment variable names and their values.

`.google.cloud.batch.v1.Environment.KMSEnvMap encrypted_variables = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Environment.KMSEnvMapOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.Environment.KMSEnvMapOrBuilder)` |   
  
### getSecretVariables() (deprecated)
    
    
    public abstract Map<String,String> getSecretVariables()

Use [#getSecretVariablesMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.EnvironmentOrBuilder#com_google_cloud_batch_v1_EnvironmentOrBuilder_getSecretVariablesMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getSecretVariablesCount()
    
    
    public abstract int getSecretVariablesCount()

A map of environment variable names to Secret Manager secret names. The VM will access the named secrets to set the value of each environment variable.

`map<string, string> secret_variables = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSecretVariablesMap()
    
    
    public abstract Map<String,String> getSecretVariablesMap()

A map of environment variable names to Secret Manager secret names. The VM will access the named secrets to set the value of each environment variable.

`map<string, string> secret_variables = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getSecretVariablesOrDefault(String key, String defaultValue)
    
    
    public abstract String getSecretVariablesOrDefault(String key, String defaultValue)

A map of environment variable names to Secret Manager secret names. The VM will access the named secrets to set the value of each environment variable.

`map<string, string> secret_variables = 2;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getSecretVariablesOrThrow(String key)
    
    
    public abstract String getSecretVariablesOrThrow(String key)

A map of environment variable names to Secret Manager secret names. The VM will access the named secrets to set the value of each environment variable.

`map<string, string> secret_variables = 2;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getVariables() (deprecated)
    
    
    public abstract Map<String,String> getVariables()

Use [#getVariablesMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1.EnvironmentOrBuilder#com_google_cloud_batch_v1_EnvironmentOrBuilder_getVariablesMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getVariablesCount()
    
    
    public abstract int getVariablesCount()

A map of environment variable names to values.

`map<string, string> variables = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getVariablesMap()
    
    
    public abstract Map<String,String> getVariablesMap()

A map of environment variable names to values.

`map<string, string> variables = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getVariablesOrDefault(String key, String defaultValue)
    
    
    public abstract String getVariablesOrDefault(String key, String defaultValue)

A map of environment variable names to values.

`map<string, string> variables = 1;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getVariablesOrThrow(String key)
    
    
    public abstract String getVariablesOrThrow(String key)

A map of environment variable names to values.

`map<string, string> variables = 1;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### hasEncryptedVariables()
    
    
    public abstract boolean hasEncryptedVariables()

An encrypted JSON dictionary where the key/value pairs correspond to environment variable names and their values.

`.google.cloud.batch.v1.Environment.KMSEnvMap encrypted_variables = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptedVariables field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
