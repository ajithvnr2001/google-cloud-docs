---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiNamespace/
title: ApiNamespace \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:04.675963+00:00
---

# ApiNamespace  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiNamespace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  ApiNamespace Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Annotation Type ApiNamespace

  * * * *

  

        
        @Retention(value=RUNTIME)
         @Target(value=TYPE)
        public @interface ApiNamespace

Fields populated in Discovery in order to proper namespace generated clients.




  *     * ### Required Element Summary

Required Elements Modifier and Type | Required Element and Description  
---|---  
`java.lang.String` | `[ownerDomain](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiNamespace.html#ownerDomain--)` This is the domain name commonly associated with owner.  
`java.lang.String` | `[ownerName](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiNamespace.html#ownerName--)` This is a canonical company name obeying the same rules as the canonical API name.  
    * ### Optional Element Summary

Optional Elements Modifier and Type | Optional Element and Description  
---|---  
`java.lang.String` | `[packagePath](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiNamespace.html#packagePath--)` This is an optional way to further scope a generated client library.  



  *     * ### Element Detail

      * #### ownerDomain
            
            public abstract java.lang.String ownerDomain

This is the domain name commonly associated with owner. If, for instance, this is an API owned by NASA, then "nasa.gov" would be a reasonable choice for domain name. It does not necessarily need to be the same as the serving domain, though the latter will be picked as a default if `ownerDomain` is not set. Required for a specified namespace.

    *       * #### ownerName
            
            public abstract java.lang.String ownerName

This is a canonical company name obeying the same rules as the canonical API name. It obeys the exact capitalization a company would like to use to represent themselves. If their name is really two dwords, they are separated by spaces. E.g. "YouTube", "NASA" , "3Com", "Fox News". Required for a specified namespace.

    *       * #### packagePath
            
            public abstract java.lang.String packagePath

This is an optional way to further scope a generated client library. It follows the same name rules for ownerName, with the restriction that words must be alphanumeric. This feature allows an enterprise to group one or more of their APIs from different Endpoints instances together in a logical space more fine-grained than just their domain name. If the package includes multiple words, each word will, when possible, be used as an additional level in the scope of the package.

Default:
    ""



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
