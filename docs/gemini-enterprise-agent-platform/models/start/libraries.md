---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/libraries/
title: Google Gen AI libraries \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:42:06.323719+00:00
---

# Google Gen AI libraries  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Google Gen AI libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information on downloading and installing the latest libraries for the Gemini API. If you're new to the Gemini API, get started with the [API quickstart](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start).

## Important note about google-genai libraries

We've recently launched a new set of libraries that provide a more consistent and streamlined experience for accessing Google's generative AI models across different Google services. 

Gemini Enterprise Agent Platform libraries are only supported on Gemini Enterprise Agent Platform.

## Key library updates

Language | Gemini Enterprise Agent Platform library | New library (Recommended)  
---|---|---  
[**Python**](https://ai.google.dev/gemini-api/docs/libraries#python) | [`google-cloud-aiplatform`](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform)  
GenerativeModel Module Deprecated in May 2026  | [`google-genai`](https://github.com/googleapis/python-genai)  
[**Go**](https://ai.google.dev/gemini-api/docs/libraries#go) | [`cloud.google.com/vertexai`](https://pkg.go.dev/cloud.google.com/go/vertexai)  
Deprecated in May 2026  | [`google.golang.org/genai`](http://google.golang.org/genai)  
[**JavaScript and TypeScript**](https://ai.google.dev/gemini-api/docs/libraries#javascript) | [`@google-cloud/vertexai`](https://www.npmjs.com/package/@google-cloud/vertexai)  
Deprecated in May 2026  | [`@google/genai`](https://www.npmjs.com/package/@google/genai)  
Available in Preview  
[**Java**](https://ai.google.dev/gemini-api/docs/libraries#java) | [`google-cloud-vertexai`](https://mvnrepository.com/artifact/com.google.cloud/google-cloud-vertexai)  
Deprecated in May 2026  | [`java-genai`](https://github.com/googleapis/java-genai)  
Available in Preview  
[**.NET**](https://ai.google.dev/gemini-api/docs/libraries#csharp) | [`Google.Cloud.AIPlatform.V1`](https://www.nuget.org/packages/Google.Cloud.AIPlatform.V1)  
Deprecated in May 2026  | [`Google.GenAI`](https://github.com/googleapis/dotnet-genai)  
Available in Preview  
  
Users are encouraged to start with the new library and migrate from previous libraries.

## Install a library

The following examples can help you get started in various programming languages.

PythonGoJavaScript/TypeScriptJava.NET

Install our [Python library](https://pypi.org/project/google-genai) by running: 
    
    
        pip install google-genai
      

Install our [Go library](https://pkg.go.dev/google.golang.org/genai) by running: 
    
    
        go get google.golang.org/genai
      

Install our [JavaScript/TypeScript library](https://www.npmjs.com/package/@google/genai) by running: 
    
    
        npm install @google/genai
      

The [new JavaScript and TypeScript library](https://ai.google.dev/gemini-api/docs/libraries) is available in [_preview_](https://cloud.google.com/products#product-launch-stages), which means it may not be feature complete and that we may need to introduce breaking changes. 

However, we recommend that you start using the [new SDK](https://www.npmjs.com/package/@google/genai) instead of the previous, deprecated version as long as you're comfortable with these caveats. 

Install our [Java library](https://github.com/googleapis/java-genai) by adding the dependencies in Maven: 
    
    
    <dependencies>
      <dependency>
        <groupId>com.google.genai</groupId>
        <artifactId>google-genai</artifactId>
        <version>0.8.0</version>
      </dependency>
    </dependencies>
      

The new Java library is available in [_preview_](https://cloud.google.com/products#product-launch-stages), which means it may not be feature complete and that we may need to introduce breaking changes. 

However, we recommend that you start using the [new SDK](https://github.com/googleapis/java-genai) instead of the previous, deprecated version as long as you're comfortable with these caveats. 

Install our [.NET library](https://www.nuget.org/packages/Google.GenAI) by running: 
    
    
        dotnet add package Google.GenAI
      

The new .NET library is available in [_preview_](https://cloud.google.com/products#product-launch-stages), which means it may not be feature complete and that we may need to introduce breaking changes. 

However, we recommend that you start using the [new SDK](https://github.com/googleapis/dotnet-genai) instead of the previous, deprecated version as long as you're comfortable with these caveats. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
