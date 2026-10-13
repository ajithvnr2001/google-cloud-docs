---
url: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.AbstractGoogleClient.Builder
title: Class AbstractGoogleClient.Builder (2.9.1) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:37.139029+00:00
---

# Class AbstractGoogleClient.Builder (2.9.1)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.AbstractGoogleClient.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AbstractGoogleClient.Builder (2.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.1 (latest)  2.9.0  2.8.1  2.7.2  2.6.0  2.5.1  2.4.1  2.1.2  2.0.1  1.35.2  1.34.1  1.33.4 
    
    
    public abstract static class AbstractGoogleClient.Builder

Builder for [AbstractGoogleClient](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.AbstractGoogleClient).

Implementation is not thread-safe.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AbstractGoogleClient.Builder

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

### Builder(HttpTransport transport, String rootUrl, String servicePath, ObjectParser objectParser, HttpRequestInitializer httpRequestInitializer)
    
    
    protected Builder(HttpTransport transport, String rootUrl, String servicePath, ObjectParser objectParser, HttpRequestInitializer httpRequestInitializer)

Returns an instance of a new builder.

**Parameters**  
---  
**Name** | **Description**  
`transport` | `com.google.api.client.http.HttpTransport`  
The transport to use for requests  
`rootUrl` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
root URL of the service. Must end with a "/"  
`servicePath` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
service path  
`objectParser` | `com.google.api.client.util.ObjectParser`  
object parser or `null` for none  
`httpRequestInitializer` | `com.google.api.client.http.HttpRequestInitializer`  
HTTP request initializer or `null` for none  
  
## Methods 

### build()
    
    
    public abstract AbstractGoogleClient build()

Builds a new instance of [AbstractGoogleClient](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.AbstractGoogleClient).

**Returns**  
---  
**Type** | **Description**  
`[AbstractGoogleClient](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.AbstractGoogleClient)` |   
  
### getApplicationName()
    
    
    public final String getApplicationName()

Returns the application name to be used in the UserAgent header of each request or ` null` for none.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getGoogleClientRequestInitializer()
    
    
    public final GoogleClientRequestInitializer getGoogleClientRequestInitializer()

Returns the Google client request initializer or `null` for none.

**Returns**  
---  
**Type** | **Description**  
`[GoogleClientRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.GoogleClientRequestInitializer)` |   
  
### getHttpRequestInitializer()
    
    
    public final HttpRequestInitializer getHttpRequestInitializer()

Returns the HTTP request initializer or `null` for none.

**Returns**  
---  
**Type** | **Description**  
`com.google.api.client.http.HttpRequestInitializer` |   
  
### getObjectParser()
    
    
    public ObjectParser getObjectParser()

Returns the object parser or `null` for none.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Returns**  
---  
**Type** | **Description**  
`com.google.api.client.util.ObjectParser` |   
  
### getRootUrl()
    
    
    public final String getRootUrl()

Returns the URL-encoded root URL of the service, for example ` <https://www.googleapis.com/>`.

Must be URL-encoded and must end with a "/".

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getServicePath()
    
    
    public final String getServicePath()

Returns the URL-encoded service path of the service, for example `"tasks/v1/"`.

Must be URL-encoded and must end with a "/" and not begin with a "/". It is allowed to be an empty string `""`.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getSuppressPatternChecks()
    
    
    public final boolean getSuppressPatternChecks()

Returns whether discovery pattern checks should be suppressed on required parameters.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSuppressRequiredParameterChecks()
    
    
    public final boolean getSuppressRequiredParameterChecks()

Returns whether discovery required parameter checks should be suppressed.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTransport()
    
    
    public final HttpTransport getTransport()

Returns the HTTP transport.

**Returns**  
---  
**Type** | **Description**  
`com.google.api.client.http.HttpTransport` |   
  
### setApplicationName(String applicationName)
    
    
    public AbstractGoogleClient.Builder setApplicationName(String applicationName)

Sets the application name to be used in the UserAgent header of each request or `null` for none.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`applicationName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AbstractGoogleClient.Builder](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.AbstractGoogleClient.Builder)` |   
  
### setBatchPath(String batchPath)
    
    
    public AbstractGoogleClient.Builder setBatchPath(String batchPath)

Sets the URL-encoded batch path of the service, for example `"batch/tasks"`.

**Parameter**  
---  
**Name** | **Description**  
`batchPath` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AbstractGoogleClient.Builder](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.AbstractGoogleClient.Builder)` |   
  
### setGoogleClientRequestInitializer(GoogleClientRequestInitializer googleClientRequestInitializer)
    
    
    public AbstractGoogleClient.Builder setGoogleClientRequestInitializer(GoogleClientRequestInitializer googleClientRequestInitializer)

Sets the Google client request initializer or `null` for none.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`googleClientRequestInitializer` | `[GoogleClientRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.GoogleClientRequestInitializer)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AbstractGoogleClient.Builder](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.AbstractGoogleClient.Builder)` |   
  
### setHttpRequestInitializer(HttpRequestInitializer httpRequestInitializer)
    
    
    public AbstractGoogleClient.Builder setHttpRequestInitializer(HttpRequestInitializer httpRequestInitializer)

Sets the HTTP request initializer or `null` for none.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`httpRequestInitializer` | `com.google.api.client.http.HttpRequestInitializer`  
  
**Returns**  
---  
**Type** | **Description**  
`[AbstractGoogleClient.Builder](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.AbstractGoogleClient.Builder)` |   
  
### setRootUrl(String rootUrl)
    
    
    public AbstractGoogleClient.Builder setRootUrl(String rootUrl)

Sets the URL-encoded root URL of the service, for example `<https://www.googleapis.com/>` .

If the specified root URL does not end with a "/" then a "/" is added to the end.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`rootUrl` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AbstractGoogleClient.Builder](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.AbstractGoogleClient.Builder)` |   
  
### setServicePath(String servicePath)
    
    
    public AbstractGoogleClient.Builder setServicePath(String servicePath)

Sets the URL-encoded service path of the service, for example `"tasks/v1/"`.

It is allowed to be an empty string `""` or a forward slash `"/"`, if it is a forward slash then it is treated as an empty string. This is determined when the library is generated and normally should not be changed.

If the specified service path does not end with a "/" then a "/" is added to the end. If the specified service path begins with a "/" then the "/" is removed.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`servicePath` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AbstractGoogleClient.Builder](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.AbstractGoogleClient.Builder)` |   
  
### setSuppressAllChecks(boolean suppressAllChecks)
    
    
    public AbstractGoogleClient.Builder setSuppressAllChecks(boolean suppressAllChecks)

Suppresses all discovery pattern and required parameter checks.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`suppressAllChecks` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AbstractGoogleClient.Builder](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.AbstractGoogleClient.Builder)` |   
  
### setSuppressPatternChecks(boolean suppressPatternChecks)
    
    
    public AbstractGoogleClient.Builder setSuppressPatternChecks(boolean suppressPatternChecks)

Sets whether discovery pattern checks should be suppressed on required parameters.

Default value is `false`.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`suppressPatternChecks` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AbstractGoogleClient.Builder](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.AbstractGoogleClient.Builder)` |   
  
### setSuppressRequiredParameterChecks(boolean suppressRequiredParameterChecks)
    
    
    public AbstractGoogleClient.Builder setSuppressRequiredParameterChecks(boolean suppressRequiredParameterChecks)

Sets whether discovery required parameter checks should be suppressed.

Default value is `false`.

Overriding is only supported for the purpose of calling the super implementation and changing the return type, but nothing else.

**Parameter**  
---  
**Name** | **Description**  
`suppressRequiredParameterChecks` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AbstractGoogleClient.Builder](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.AbstractGoogleClient.Builder)` |   
  
### setUniverseDomain(String universeDomain)
    
    
    public AbstractGoogleClient.Builder setUniverseDomain(String universeDomain)

Sets the user configured Universe Domain value. This value will be used to try and construct the endpoint to connect to GCP services.

**Parameter**  
---  
**Name** | **Description**  
`universeDomain` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AbstractGoogleClient.Builder](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.services.AbstractGoogleClient.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
