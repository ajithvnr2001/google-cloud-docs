---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/PeerAuthenticator/
title: PeerAuthenticator (endpoints-framework 2.0.0-beta.5 API) \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:47:00.656869+00:00
---

# PeerAuthenticator (endpoints-framework 2.0.0-beta.5 API)  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/PeerAuthenticator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  PeerAuthenticator (endpoints-framework 2.0.0-beta.5 API) Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Interface PeerAuthenticator

  * * * *

  

        
        public interface PeerAuthenticator

Peer authenticators aim to verify the peer and run before `Authenticator`. It returns false if authentication failed and stops handling the rest of the request; true if authentication succeeds and continue to execute rest of peer authenticators. 

If no peer authenticator is set, `EndpointsPeerAuthenticator` will be the default to verify the request is from Google. If you supply your own peer authenticator, make sure you also put `EndpointsPeerAuthenticator` to the head of peerAuthenticators list to verify the request is from Google.




  *     * ### Method Summary

All Methods Instance Methods Abstract Methods Modifier and Type | Method and Description  
---|---  
`boolean` | `[authenticate](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/PeerAuthenticator.html#authenticate-HttpServletRequest-)(HttpServletRequest request)`  



  *     * ### Method Detail

      * #### authenticate
            
            boolean authenticate(HttpServletRequest request)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
