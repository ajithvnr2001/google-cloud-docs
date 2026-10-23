---
url: https://docs.cloud.google.com/java/docs/common-configuration-options/
title: Common configuration options \u00a0|\u00a0 Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:06.695172+00:00
---

# Common configuration options  |  Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/common-configuration-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Common configuration options Stay organized with collections  Save and categorize content based on your preferences. 

The following options are typically configured using the `Settings.newBuilder()` method any client.

Setting Method | Description  
---|---  
`setCredentialsProvider` | Provides the credentials (Service Account, API Key, etc.) for authentication.  
`setEndpoint` | The address of the API remote host. Used for Regional Endpoints (e.g., `us-central1-pubsub.googleapis.com:443`) or Private Service Connect.  
`setTransportChannelProvider` | Specifies the transport type (gRPC or HTTP/REST) and manages connection pools.  
`setHeaderProvider` | Allows adding custom headers to every request made by the client.  
`setUniverseDomain` | Overrides the default service domain (defaults to `googleapis.com`) for Cloud Universe support.  
`setQuotaProjectId` | Sets the project ID used for quota and billing, which may be different from the project being operated on.  
      
    
    // The project that will be billed and have its quota consumed for these API calls
    String billingProjectId = "my-central-billing-project";
    CloudTasksSettings cloudTasksSettings =
            .setQuotaProjectId(billingProjectId)
            .setTransportChannelProvider(transportChannelProvider)
            .build();
    CloudTasksClient cloudTasksClient = CloudTasksClient.create(cloudTasksSettings);
    

## Customize the API Endpoint

See [Configure Cloud Client Libraries endpoints](https://docs.cloud.google.com/java/docs/endpoints).

## Authentication Configuration

See [Authenticate your requests](https://docs.cloud.google.com/java/docs/authentication).

## Logging

See the [Logging](https://docs.cloud.google.com/java/docs/troubleshooting#logging) section in [Troubleshooting](https://docs.cloud.google.com/java/docs/troubleshooting).

## Configure a Proxy

See [Configure a proxy](https://docs.cloud.google.com/java/docs/configuring-a-proxy).

## Configure Retries and Timeouts

See [Configure client-side retries](https://docs.cloud.google.com/java/docs/client-retries).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
