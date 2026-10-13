---
url: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.testing.auth.oauth2.MockTokenServerTransport
title: Class MockTokenServerTransport (2.9.1) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:41.592843+00:00
---

# Class MockTokenServerTransport (2.9.1)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.testing.auth.oauth2.MockTokenServerTransport

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MockTokenServerTransport (2.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.1 (latest)  2.9.0  2.8.1  2.7.2  2.6.0  2.5.1  2.4.1  2.1.2  2.0.1  1.35.2  1.34.1  1.33.4 
    
    
    public class MockTokenServerTransport extends MockHttpTransport

Beta   
A test transport that simulates Google's token server for refresh tokens and service accounts.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > com.google.api.client.http.HttpTransport > com.google.api.client.testing.http.MockHttpTransport > MockTokenServerTransport

## Inherited Members

com.google.api.client.http.HttpTransport.createRequestFactory()

com.google.api.client.http.HttpTransport.createRequestFactory(com.google.api.client.http.HttpRequestInitializer)

com.google.api.client.http.HttpTransport.isMtls()

com.google.api.client.http.HttpTransport.isShutdown()

com.google.api.client.http.HttpTransport.shutdown()

com.google.api.client.testing.http.MockHttpTransport.buildRequest(java.lang.String,java.lang.String)

com.google.api.client.testing.http.MockHttpTransport.getLowLevelHttpRequest()

com.google.api.client.testing.http.MockHttpTransport.getSupportedMethods()

com.google.api.client.testing.http.MockHttpTransport.supportsMethod(java.lang.String)

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

### MockTokenServerTransport()
    
    
    public MockTokenServerTransport()

### MockTokenServerTransport(String tokenServerUrl)
    
    
    public MockTokenServerTransport(String tokenServerUrl)

**Parameter**  
---  
**Name** | **Description**  
`tokenServerUrl` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
## Methods 

### addClient(String clientId, String clientSecret)
    
    
    public void addClient(String clientId, String clientSecret)

**Parameters**  
---  
**Name** | **Description**  
`clientId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`clientSecret` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### addRefreshToken(String refreshToken, String accessTokenToReturn)
    
    
    public void addRefreshToken(String refreshToken, String accessTokenToReturn)

**Parameters**  
---  
**Name** | **Description**  
`refreshToken` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`accessTokenToReturn` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### addServiceAccount(String email, String accessToken)
    
    
    public void addServiceAccount(String email, String accessToken)

**Parameters**  
---  
**Name** | **Description**  
`email` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`accessToken` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### buildRequest(String method, String url)
    
    
    public LowLevelHttpRequest buildRequest(String method, String url)

**Parameters**  
---  
**Name** | **Description**  
`method` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`url` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.client.http.LowLevelHttpRequest` |   
**Overrides**

com.google.api.client.testing.http.MockHttpTransport.buildRequest(java.lang.String,java.lang.String)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
