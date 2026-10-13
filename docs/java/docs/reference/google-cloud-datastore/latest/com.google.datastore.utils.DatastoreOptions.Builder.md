---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.utils.DatastoreOptions.Builder
title: Class DatastoreOptions.Builder (3.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:25.136604+00:00
---

# Class DatastoreOptions.Builder (3.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.utils.DatastoreOptions.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DatastoreOptions.Builder (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.3.0  3.2.0  3.1.0  2.40.0  2.37.0  2.36.0  2.34.0  2.33.3  2.32.3  2.31.4  2.30.0  2.29.1  2.28.2  2.27.1  2.26.4  2.25.2  2.24.3  2.23.0  2.22.0  2.21.3  2.20.2  2.19.2  2.18.5  2.17.6 
    
    
    public static class DatastoreOptions.Builder

Builder for [DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.utils.DatastoreOptions).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DatastoreOptions.Builder

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

## Constructors 

### Builder()
    
    
    public Builder()

### Builder(DatastoreOptions options)
    
    
    public Builder(DatastoreOptions options)

**Parameter**  
---  
**Name** | **Description**  
`options` | `[DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.utils.DatastoreOptions)`  
  
  
## Methods 

### build()
    
    
    public DatastoreOptions build()

**Returns**  
---  
**Type** | **Description**  
`[DatastoreOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.utils.DatastoreOptions)` |   
  
### credential(Credential credential)
    
    
    public DatastoreOptions.Builder credential(Credential credential)

Sets the Google APIs Credential used to access Cloud Datastore.

**Parameter**  
---  
**Name** | **Description**  
`credential` | `com.google.api.client.auth.oauth2.Credential`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.utils.DatastoreOptions.Builder)` |   
  
### host(String host)
    
    
    public DatastoreOptions.Builder host(String host)

Sets the host used to access Cloud Datastore. To connect to the Cloud Datastore Emulator, use [#localHost](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.utils.DatastoreOptions.Builder#com_google_datastore_utils_DatastoreOptions_Builder_localHost_) instead.

**Parameter**  
---  
**Name** | **Description**  
`host` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.utils.DatastoreOptions.Builder)` |   
  
### initializer(HttpRequestInitializer initializer)
    
    
    public DatastoreOptions.Builder initializer(HttpRequestInitializer initializer)

Sets the (optional) initializer to run on HTTP requests to Cloud Datastore.

**Parameter**  
---  
**Name** | **Description**  
`initializer` | `com.google.api.client.http.HttpRequestInitializer`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.utils.DatastoreOptions.Builder)` |   
  
### localHost(String localHost)
    
    
    public DatastoreOptions.Builder localHost(String localHost)

Configures the client to access Cloud Datastore on a local host (typically a Cloud Datastore Emulator instance). Call this method also configures the client not to attach credentials to requests.

**Parameter**  
---  
**Name** | **Description**  
`localHost` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.utils.DatastoreOptions.Builder)` |   
  
### projectId(String projectId)
    
    
    public DatastoreOptions.Builder projectId(String projectId)

Sets the project ID used to access Cloud Datastore.

**Parameter**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.utils.DatastoreOptions.Builder)` |   
  
### transport(HttpTransport transport)
    
    
    public DatastoreOptions.Builder transport(HttpTransport transport)

Sets the transport used to access Cloud Datastore.

**Parameter**  
---  
**Name** | **Description**  
`transport` | `com.google.api.client.http.HttpTransport`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastoreOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.utils.DatastoreOptions.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
