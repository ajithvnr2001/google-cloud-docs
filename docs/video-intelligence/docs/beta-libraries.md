---
url: https://docs.cloud.google.com/video-intelligence/docs/beta-libraries/
title: Beta Client Libraries \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:58.769753+00:00
---

# Beta Client Libraries  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/beta-libraries/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)



Send feedback 

#  Beta Client Libraries Stay organized with collections  Save and categorize content based on your preferences. 

Depending on your application language, you may need to use a beta-specific client library to use the Video Intelligence beta features.

## Install the beta client library

The **v1p3beta1** client library is available for the [Streaming](https://docs.cloud.google.com/video-intelligence/docs/streaming/streaming) and [Live streaming](https://docs.cloud.google.com/video-intelligence/docs/streaming/live-streaming-overview) betas.

###  Java 

If you are using Maven, add this to your pom.xml file:
    
    
    <dependency>
      <groupId>com.google.cloud</groupId>
      <artifactId>google-cloud-video-intelligence</artifactId>
      <version>0.116.0-beta</version>
    </dependency>
    

If you are using Gradle, add this to your dependencies:
    
    
    compile 'com.google.cloud:google-cloud-video-intelligence:0.116.0-beta'
    

If you are using SBT, add this to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-video-intelligence" % "0.116.0-beta"
    

###  Node.js 

Beta features are available from the regular [Video Intelligence API client library for Node.js](https://docs.cloud.google.com/video-intelligence/docs/libraries#client-libraries-install-nodejs).

In your Node.js application, specify the beta version of the API with the following line:
    
    
    const videoIntelligence = require('@google-cloud/video-intelligence').v1p3beta1;
    

###  Python 

Beta features are available from the regular [Video Intelligence API client library for Python](https://docs.cloud.google.com/video-intelligence/docs/reference/libraries#client-libraries-install-python).

In your Python application, import the `v1p3beta1` version of the API:
    
    
    from google.cloud import videointelligence_v1p3beta1 as videointelligence
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
