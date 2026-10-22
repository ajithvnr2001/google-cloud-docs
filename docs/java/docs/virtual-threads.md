---
url: https://docs.cloud.google.com/java/docs/virtual-threads/
title: Configure virtual threads in Cloud Client Libraries for Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:45.442800+00:00
---

# Configure virtual threads in Cloud Client Libraries for Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/virtual-threads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Configure virtual threads in Cloud Client Libraries for Java Stay organized with collections  Save and categorize content based on your preferences. 

Virtual threads, made generally available in JDK 21, simplify the development of high concurrency applications. Some key benefits may include:

  * Higher throughput, especially in applications with blocking I/O operations.
  * Memory optimization due to their lightweight nature.
  * Simple concurrency model where the applications can be represented in a thread-per-request style.



Before applying virtual threads to your application, see the Open JDK documentation's [ JEP 444: Virtual Threads](https://openjdk.org/jeps/444) for a detailed description on both the benefits and limitations of this feature.

This guide walks through how to configure [Cloud Client Libraries for Java](https://docs.cloud.google.com/java/docs/reference) in the [googleapis/google-cloud-java repository](https://github.com/googleapis/google-cloud-java) to use virtual threads.

## Prerequisites

Follow these prerequisite steps to use virtual threads with the Cloud Client Libraries for Java that you want to use in your application.

  1. If you have not already, create a Google Cloud Project. See [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  2. Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), which lets you run the sample with your project's credentials.
  3. Log in with Application Default Credentials using the following command. For further instructions, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) :
         
         gcloud auth application-default login
         

  4. To make sure Java Development Kit (JDK) 21 or later is installed, run the `java -version` command and verify that you see the following output. For steps to install JDK, see [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).
         
         openjdk version "21.0.2" 2024-01-16 LTS
         OpenJDK Runtime Environment Temurin-21.0.2+13 (build 21.0.2+13-LTS)
         OpenJDK 64-Bit Server VM Temurin-21.0.2+13 (build 21.0.2+13-LTS, mixed mode, sharing)
         




## Import the library into your project

This example uses `google-cloud-translate`. For steps to use the library in Maven or Gradle, see [Use the Cloud Translation for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/overview#use-the-cloud-translation-for-java)

## Use the virtual thread executor in the client libraries

When you instantiate a client library class, you can choose its transport implementation (gRPC and REST).

### REST transport

The client libraries that implement REST transport use blocking network I/O calls, which benefit from the throughput improvements provided by virtual threads. The following code snippet demonstrates how blocking network I/O traffic in the Cloud Client Libraries for Java can be managed by virtual threads. You can implement this in your own application by overriding the default executor with a virtual thread executor in a [TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.InstantiatingHttpJsonChannelProvider.Builder) instance.
    
    
    import com.google.cloud.translate.*;
    import java.util.concurrent.Executors;
    
    ExecutorService virtualThreadExecutor = Executors.newVirtualThreadPerTaskExecutor();
    InstantiatingHttpJsonChannelProvider httpJsonChannelProvider =
            [TranslationServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceSettings.html).[defaultHttpJsonTransportProviderBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceSettings.html#com_google_cloud_translate_v3_TranslationServiceSettings_defaultHttpJsonTransportProviderBuilder__)()
                // Use virtual threads for network I/O calls.
                .setExecutor(virtualThreadExecutor)
                .build();
    
    try ([TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client =
        [TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html).create(
            [TranslationServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceSettings.html).[newHttpJsonBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceSettings.html#com_google_cloud_translate_v3_TranslationServiceSettings_newHttpJsonBuilder__)()
                .setTransportChannelProvider(httpJsonChannelProvider)
                .build())) {
      // Make translate requests
    }
    

### gRPC transport

Since gRPC already uses asynchronous logic to handle requests, throughput improvements from virtual threads may be less pronounced. However, they can still provide some memory optimization benefits due to their lightweight nature. The following code snippet demonstrates how gRPC transport operations can be managed by virtual threads. You can implement this in your own application by overriding the default executor with a virtual thread executor in a [TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder) instance.
    
    
    import com.google.cloud.translate.*;
    import java.util.concurrent.Executors;
    
    ExecutorService virtualThreadExecutor = Executors.newVirtualThreadPerTaskExecutor();
    InstantiatingGrpcChannelProvider grpcChannelProvider =
            [TranslationServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceSettings.html).[defaultGrpcTransportProviderBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceSettings.html#com_google_cloud_translate_v3_TranslationServiceSettings_defaultGrpcTransportProviderBuilder__)()
                // Use virtual threads for gRPC transport operations.
                .setExecutor(virtualThreadExecutor)
                .build();
    
    try ([TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client =
            [TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html).create(
                [TranslationServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceSettings.html).newBuilder()
                    .setTransportChannelProvider(grpcChannelProvider)
                    .build())) {
      // Make translate requests
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
