---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Transformer/
title: Transformer \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:48:26.141292+00:00
---

# Transformer  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Transformer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  Transformer Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Interface Transformer<TFrom,TTo>

  * Type Parameters:
    `TFrom` \- The type being transformed
    `TTo` \- The type being transformed to

* * *

  

        
        public interface Transformer<TFrom,TTo>

An interface used to transform between a bean type and another type during JSON serialization. 

A serializer is constructed using one of the following constructor signatures (sorted by precedence): 

    1. A constructor taking in a single `java.lang.reflect.Type`. This is the type being serialized.
    2. A constructor taking in a single `java.lang.Class`. This is the class being serialized. 
    3. A no-arg constructor




  *     * ### Method Summary

All Methods Instance Methods Abstract Methods Modifier and Type | Method and Description  
---|---  
`[TFrom](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Transformer.html "type parameter in Transformer")` | `[transformFrom](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Transformer.html#transformFrom-TTo-)([TTo](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Transformer.html "type parameter in Transformer") in)` Converts an object from the destination type into the source type.  
`[TTo](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Transformer.html "type parameter in Transformer")` | `[transformTo](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Transformer.html#transformTo-TFrom-)([TFrom](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Transformer.html "type parameter in Transformer") in)` Converts the source object into the destination type.  



  *     * ### Method Detail

      * #### transformTo
            
            [TTo](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Transformer.html "type parameter in Transformer") transformTo([TFrom](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Transformer.html "type parameter in Transformer") in)

Converts the source object into the destination type.

      * #### transformFrom
            
            [TFrom](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Transformer.html "type parameter in Transformer") transformFrom([TTo](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Transformer.html "type parameter in Transformer") in)

Converts an object from the destination type into the source type.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
