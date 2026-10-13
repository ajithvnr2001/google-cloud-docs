---
url: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet
title: Package com.google.api.client.http.javanet (2.2.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:55.799673+00:00
---

# Package com.google.api.client.http.javanet (2.2.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.api.client.http.javanet (2.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.2.0 (latest)  2.1.1  2.0.3  1.47.1  1.46.3  1.45.3  1.44.2  1.43.2  1.42.3  1.41.8 

HTTP Transport library for Google API's based on the `java.net` package.

## Classes 

### [DefaultConnectionFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.DefaultConnectionFactory)

Default implementation of [ConnectionFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.ConnectionFactory), which simply attempts to open the connection with an optional [Proxy](https://docs.oracle.com/javase/8/docs/api/java/net/Proxy.html).

### [NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport)

Thread-safe HTTP low-level transport based on the `java.net` package.

Users should consider modifying the keep alive property on [NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport) to control whether the socket should be returned to a pool of connected sockets. More information is available [here](http://docs.oracle.com/javase/7/docs/technotes/guides/net/http-keepalive.html).

We honor the default global caching behavior. To change the default behavior use HttpURLConnection#setDefaultUseCaches(boolean).

Implementation is thread-safe. For maximum efficiency, applications should use a single globally-shared instance of the HTTP transport.

### [NetHttpTransport.Builder](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.Builder)

Builder for [NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport).

Implementation is not thread-safe.

## Interfaces 

### [ConnectionFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.ConnectionFactory)

Given a [URL](https://docs.oracle.com/javase/8/docs/api/java/net/URL.html) instance, produces an [HttpURLConnection](https://docs.oracle.com/javase/8/docs/api/java/net/HttpURLConnection.html).

### [SslSocketConfigurator](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.SslSocketConfigurator)

A callback interface allowing users to programmatically configure active [SSLSocket](https://docs.oracle.com/javase/8/docs/api/javax/net/ssl/SSLSocket.html) parameters (e.g., named groups, cipher suites, application protocols) before the TLS handshake starts.

Exposing this hook allows users to customize advanced TLS capabilities that are not configurable via standard JVM system properties, or require custom security provider APIs (e.g., Conscrypt or BouncyCastle). Typical use cases include:

  * Enabling Post-Quantum Cryptography (PQC) hybrid curves (e.g., X25519MLKEM768). 
  * Configuring Application-Layer Protocol Negotiation (ALPN) for HTTP/2. 
  * Restricting cipher suites or protocol versions dynamically based on environment. 



### JDK Version and Provider Compatibility Matrix for PQC

  * **JDK 27+** : PQC algorithms are supported natively by default. No custom configurator or security provider is required. 
  * **JDK 20-26** : Callers can configure named groups natively using standard JRE JSSE APIs (via `SSLParameters.setNamedGroups(String[])`), as shown in the JDK 20+ example below. 
  * **JDK 8-19** : The standard JRE does not expose APIs to set named groups. Callers must register a custom security provider (like Conscrypt JNI or BouncyCastle) and configure sockets using the provider-specific APIs demonstrated in the examples below. 



### Conscrypt Configuration Example
    
    
     builder.setSslSocketConfigurator(new SslSocketConfigurator() {
       @Override
       public void configure(SSLSocket socket) {
         if (org.conscrypt.Conscrypt.isConscrypt(socket)) {
           org.conscrypt.Conscrypt.setNamedGroups(socket, new String[] {"X25519MLKEM768", "X25519"});
         }
       }
     });
     

### BouncyCastle Configuration Example
    
    
     builder.setSslSocketConfigurator(new SslSocketConfigurator() {
       @Override
       public void configure(SSLSocket socket) {
         if (socket instanceof org.bouncycastle.jsse.BCSSLSocket) {
           org.bouncycastle.jsse.BCSSLSocket bcSocket = (org.bouncycastle.jsse.BCSSLSocket) socket;
           org.bouncycastle.jsse.BCSSLParameters bcParams = bcSocket.getParameters();
           bcParams.setNamedGroups(new String[] {"X25519MLKEM768", "X25519"});
           bcSocket.setParameters(bcParams);
         }
       }
     });
     

### JDK 20+ Standard JSSE Configuration Example

Note: This example requires compilation and runtime environment running JDK 20+.
    
    
     builder.setSslSocketConfigurator(new SslSocketConfigurator() {
       @Override
       public void configure(SSLSocket socket) {
         javax.net.ssl.SSLParameters parameters = socket.getSSLParameters();
         parameters.setNamedGroups(new String[] {"X25519MLKEM768", "X25519"});
         socket.setSSLParameters(parameters);
       }
     });
     

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
