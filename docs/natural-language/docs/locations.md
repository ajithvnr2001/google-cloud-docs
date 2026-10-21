---
url: https://docs.cloud.google.com/natural-language/docs/locations/
title: Locations \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:31:37.952691+00:00
---

# Locations  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Reference ](https://docs.cloud.google.com/natural-language/docs/apis)



Send feedback 

#  Locations Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Natural Language offers you some control over where the resources for your project are processed. In particular, you can configure Cloud Natural Language to perform machine learning processing on your data only in the EU or the US.

By default Cloud Natural Language processes resources in a **Global** location, which means that Cloud Natural Language doesn't guarantee that your resources will remain within a particular location or region. If you choose the **European Union** location, Google will perform machine learning with it only in the EU. If you choose the **United States** location, Google will perform machine learning with it only in the US. You and your users can access the data from any location.

## Setting the location using the API

Cloud Natural Language supports a global API endpoint (`language.googleapis.com`), a European Union endpoint (`eu-language.googleapis.com`), and a United States endpoint (`us-language.googleapis.com`). To process your data in the European Union only, use the URI `eu-language.googleapis.com` in place of `language.googleapis.com` for your REST API calls. To process your data in the United States only, use the URI `us-language.googleapis.com` in place of `language.googleapis.com` for your REST API calls.

The text moderation API is also available in Australia, which can be accessed by using the URI `au-language.googleapis.com` in place of `language.googleapis.com` for your REST API calls.

## Setting the location using client libraries

The client libraries access the global API endpoint (`language.googleapis.com`) by default. To store and process your data in the European Union or United States only, you need to explicitly set the endpoint. The code samples below show how to configure this setting.

### Python

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Google Cloud client library
    from google.cloud import language_v1
    
    client_options = {"api_endpoint": "eu-language.googleapis.com:443"}
    
    # Instantiates a client.
    client = language_v1.LanguageServiceClient(client_options=client_options)

### Java

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/overview). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    LanguageServiceSettings settings =
        LanguageServiceSettings.newBuilder().setEndpoint("eu-language.googleapis.com:443").build();
    
    // Initialize client that will be used to send requests. This client only needs to be created
    // once, and can be reused for multiple requests. After completing all of your requests, call
    // the "close" method on the client to safely clean up any remaining background resources.
    LanguageServiceClient client = LanguageServiceClient.create(settings);

### Node.js

To learn how to install and use the client library for Natural Language, see [Natural Language client libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries). For more information, see the [Natural Language Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/language/latest). 

To authenticate to Natural Language, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const language = require('[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)');
    
    // Specifies the location of the api endpoint
    const clientOptions = {apiEndpoint: 'eu-language.googleapis.com'};
    
    // Instantiates a client
    const client = new language.[LanguageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)(clientOptions);

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
