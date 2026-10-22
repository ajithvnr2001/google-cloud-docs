---
url: https://docs.cloud.google.com/java/docs/endpoints/
title: Configure client library endpoints \u00a0|\u00a0 Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:56.671515+00:00
---

# Configure client library endpoints  |  Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Configure client library endpoints Stay organized with collections  Save and categorize content based on your preferences. 

Each Google Cloud API service is accessed through a service-specific endpoint.

For example, the Java-Speech and Java-Translate client libraries have default endpoints of `https://speech.googleapis.com:443` and `https://translate.googleapis.com:443` respectively.

The Cloud Client Libraries for Java automatically determine the correct service endpoint during client initialization. If no custom endpoint is configured, the libraries use the service's default endpoint.

## Anatomy of an endpoint

Using the Java-Speech endpoint as an example, the following table details the sections that make up the endpoint:

Scheme | Service Name | Universe Domain | Port  
---|---|---|---  
https:// | speech | googleapis.com | 443  
  
These are the default values of all Cloud Client Libraries for Java endpoints, apart from the service name. The service name does not have a default value because every Google Cloud service has a different value.

## When to configure a custom endpoint

There are certain use cases to replace the default endpoint, such as:

  * **The service offers[regional endpoints](https://docs.cloud.google.com/docs/geography-and-regions).** The default endpoint does not consider regional variants.
  * **You are not working in production.** For example, you are testing locally with an emulator without configuring TLS.



Only modify the endpoint configuration if necessary. When using a custom endpoint, you must include the port number (for example, `example.com:443`). The client libraries do not automatically append a default port like `443` to custom endpoints, unlike they do for default service endpoints.

## Configure a custom endpoint

You can set the endpoint from the service-specific `ClientSettings` in Cloud Client Libraries for Java.

The following example uses Java-KMS:

  1. Set the endpoint in the `ClientSettings.Builder` and create the `ClientSettings`:
         
         // Replace with your desired endpoint
         String endpoint = "customEndpoint.com:443";
         KeyManagementServiceSettings keyManagementServiceSettings =
          KeyManagementServiceSettings.newBuilder()
             .setEndpoint(endpoint)
             .build();
         

  2. Initiate the client with `ClientSettings`:
         
         try (KeyManagementServiceClient keyManagementServiceClient =
           KeyManagementServiceClient.create(keyManagementServiceSettings)) {
           ...
         }
         

The endpoint resolves to `customEndpoint.com:443`.

The client uses the endpoint from the first of the following sources that provides one:

     1. The endpoint set programmatically via `ClientSettings.Builder.setEndpoint()`.
     2. The service's default endpoint, such as `https://{serviceName}.googleapis.com:443`.



The following snippet shows how to determine the client's resolved endpoint:
    
    
    // The client's settings class contains a getter for the endpoint
    keyManagementServiceClient.getSettings().getEndpoint();
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
