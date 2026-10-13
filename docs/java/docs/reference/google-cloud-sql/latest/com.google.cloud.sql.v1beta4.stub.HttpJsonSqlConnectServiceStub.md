---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.HttpJsonSqlConnectServiceStub
title: Class HttpJsonSqlConnectServiceStub (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:22.096678+00:00
---

# Class HttpJsonSqlConnectServiceStub (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.HttpJsonSqlConnectServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HttpJsonSqlConnectServiceStub (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public class HttpJsonSqlConnectServiceStub extends SqlConnectServiceStub

REST stub implementation for the SqlConnectService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [SqlConnectServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.SqlConnectServiceStub) > HttpJsonSqlConnectServiceStub

## Inherited Members

[SqlConnectServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.SqlConnectServiceStub#com_google_cloud_sql_v1beta4_stub_SqlConnectServiceStub_close__)

[SqlConnectServiceStub.generateEphemeralCertCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.SqlConnectServiceStub#com_google_cloud_sql_v1beta4_stub_SqlConnectServiceStub_generateEphemeralCertCallable__)

[SqlConnectServiceStub.getConnectSettingsCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.SqlConnectServiceStub#com_google_cloud_sql_v1beta4_stub_SqlConnectServiceStub_getConnectSettingsCallable__)

[SqlConnectServiceStub.resolveConnectSettingsCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.SqlConnectServiceStub#com_google_cloud_sql_v1beta4_stub_SqlConnectServiceStub_resolveConnectSettingsCallable__)

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

### create(ClientContext clientContext)
    
    
    public static final HttpJsonSqlConnectServiceStub create(ClientContext clientContext)

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonSqlConnectServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.HttpJsonSqlConnectServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    public static final HttpJsonSqlConnectServiceStub create(ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

**Parameters**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[HttpJsonStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.HttpJsonStubCallableFactory.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonSqlConnectServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.HttpJsonSqlConnectServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlConnectServiceStubSettings settings)
    
    
    public static final HttpJsonSqlConnectServiceStub create(SqlConnectServiceStubSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlConnectServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.SqlConnectServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HttpJsonSqlConnectServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.HttpJsonSqlConnectServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getMethodDescriptors()
    
    
    public static List<ApiMethodDescriptor> getMethodDescriptors()

**Internal Only** : This feature is not stable for application use.

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ApiMethodDescriptor](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.ApiMethodDescriptor.html)>` |   
  
## Constructors 

### HttpJsonSqlConnectServiceStub(SqlConnectServiceStubSettings settings, ClientContext clientContext)
    
    
    protected HttpJsonSqlConnectServiceStub(SqlConnectServiceStubSettings settings, ClientContext clientContext)

Constructs an instance of HttpJsonSqlConnectServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[SqlConnectServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.SqlConnectServiceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
  
### HttpJsonSqlConnectServiceStub(SqlConnectServiceStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)
    
    
    protected HttpJsonSqlConnectServiceStub(SqlConnectServiceStubSettings settings, ClientContext clientContext, HttpJsonStubCallableFactory callableFactory)

Constructs an instance of HttpJsonSqlConnectServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[SqlConnectServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.SqlConnectServiceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[HttpJsonStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.HttpJsonStubCallableFactory.html)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### close()
    
    
    public final void close()

**Overrides**

[SqlConnectServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.SqlConnectServiceStub#com_google_cloud_sql_v1beta4_stub_SqlConnectServiceStub_close__)

### generateEphemeralCertCallable()
    
    
    public UnaryCallable<GenerateEphemeralCertRequest,GenerateEphemeralCertResponse> generateEphemeralCertCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GenerateEphemeralCertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.GenerateEphemeralCertRequest),[GenerateEphemeralCertResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.GenerateEphemeralCertResponse)>` |   
**Overrides**

[SqlConnectServiceStub.generateEphemeralCertCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.SqlConnectServiceStub#com_google_cloud_sql_v1beta4_stub_SqlConnectServiceStub_generateEphemeralCertCallable__)

### getConnectSettingsCallable()
    
    
    public UnaryCallable<GetConnectSettingsRequest,ConnectSettings> getConnectSettingsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetConnectSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.GetConnectSettingsRequest),[ConnectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.ConnectSettings)>` |   
**Overrides**

[SqlConnectServiceStub.getConnectSettingsCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.SqlConnectServiceStub#com_google_cloud_sql_v1beta4_stub_SqlConnectServiceStub_getConnectSettingsCallable__)

### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### resolveConnectSettingsCallable()
    
    
    public UnaryCallable<ResolveConnectSettingsRequest,ConnectSettings> resolveConnectSettingsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResolveConnectSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.ResolveConnectSettingsRequest),[ConnectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.ConnectSettings)>` |   
**Overrides**

[SqlConnectServiceStub.resolveConnectSettingsCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.stub.SqlConnectServiceStub#com_google_cloud_sql_v1beta4_stub_SqlConnectServiceStub_resolveConnectSettingsCallable__)

### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
