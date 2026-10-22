---
url: https://docs.cloud.google.com/java/docs/authentication/
title: Authenticate your requests \u00a0|\u00a0 Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:01.009924+00:00
---

# Authenticate your requests  |  Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Authenticate your requests Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Client Libraries for Java uses the [Google Auth Library for Java](https://github.com/googleapis/google-auth-library-java) to authenticate requests. This library supports multiple authentication types. For more details, see the project's [`README.md`](https://github.com/googleapis/google-auth-library-java/blob/main/README.md) and [javadoc](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/overview).

## Authentication in a Google Cloud environment

When using Google Cloud libraries from a Google Cloud environment (such as Compute Engine, Google Kubernetes Engine, or App Engine) you don't need to perform additional authentication steps.

An example call without additional authentication:
    
    
    Storage storage = StorageOptions.getDefaultInstance().getService();
    

## Authentication in non-Google Cloud environments

To authenticate in a non-Google Cloud environment, there are three common options:

  1. (Recommended) Use a service account.
  2. Use the Google Cloud SDK with a local test environment.
  3. Use an existing OAuth2 access token.



### Use a service account

  1. [Generate a JSON service account key](https://docs.cloud.google.com/storage/docs/authentication#service_accounts).

  2. After downloading the key, you must do one of the following:

     * Define the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to be the location of the key. For example:
    
    export GOOGLE_APPLICATION_CREDENTIALS=/path/to/my/key.json
    

     * Supply the JSON credentials file when building the service options. For example, this `Storage` object has the necessary permissions to interact with your Cloud Storage data:
    
    Storage storage = StorageOptions.newBuilder()
        .setCredentials(ServiceAccountCredentials.fromStream(new FileInputStream("/path/to/my/key.json")))
        .build()
        .getService();
    




### Use the Google Cloud SDK with a local test environment

If you are using a local environment for development or testing, you can use the [Google Cloud SDK](https://docs.cloud.google.com/sdk).

Create Application Default Credentials with `gcloud auth application-default login`. Cloud Client Libraries for Java will automatically detect these credentials.

### Use an existing OAuth2 access token

If you have an OAuth2 access token, you can use it to authenticate. If you do, the access token isn't automatically refreshed:
    
    
    Credentials credentials = GoogleCredentials.create(new AccessToken(accessToken, expirationTime));
    Storage storage = StorageOptions.newBuilder()
        .setCredentials(credentials)
        .build()
        .getService();
    

Another example:
    
    
    Credentials credentials = GoogleCredentials.create(new AccessToken(accessToken, expirationTime));
    CloudTasksSettings cloudTasksSettings = CloudTasksSettings.newBuilder()
        .setCredentialProvider(FixedCredentialsProvider.create(credentials))
        .build();
    CloudTasksClient cloudTasksClient = CloudTasksClient.create(cloudTasksSettings);
    

### Application Default Credentials

If you don't provide credentials, Cloud Client Libraries for Java will attempt to detect them from the environment using `GoogleCredentials.getApplicationDefault()`. This method searches for Application Default Credentials in the following locations, in order:

  1. The credentials file pointed to by the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.
  2. Credentials provided by the Google Cloud SDK `gcloud auth application-default login` command.
  3. Google App Engine's built-in credentials.
  4. Google Cloud Shell's built-in credentials.
  5. Google Compute Engine's built-in service account credentials.



## Authentication with an API key

Some Google Cloud APIs support [authenticating with API keys](https://cloud.google.com/docs/authentication/api-keys).

To use an API key with Cloud Client Libraries for Java, you must manually set the `x-goog-api-key` header for the relevant service client.

For example, to set the API key with the [`Language service`](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/overview):
    
    
    public LanguageServiceClient createGrpcClientWithApiKey(String apiKey) throws Exception {
        // Manually set the API key using the header
        Map<String, String> header = new HashMap<String, String>() { {put("x-goog-api-key", apiKey);}};
        FixedHeaderProvider headerProvider = FixedHeaderProvider.create(header);
    
        // Create the client
        TransportChannelProvider transportChannelProvider = InstantiatingGrpcChannelProvider.newBuilder().setHeaderProvider(headerProvider).build();
        LanguageServiceSettings settings = LanguageServiceSettings.newBuilder().setTransportChannelProvider(transportChannelProvider).build();
        LanguageServiceClient client = LanguageServiceClient.create(settings);
        return client;
      }
    

An example instantiation with the Language Client using REST:
    
    
     public LanguageServiceClient createRestClientWithApiKey(String apiKey) throws Exception {
        // Manually set the API key header
        Map<String, String> header = new HashMap<String, String>() { {put("x-goog-api-key", apiKey);}};
        FixedHeaderProvider headerProvider = FixedHeaderProvider.create(header);
    
        // Create the client
        TransportChannelProvider transportChannelProvider = InstantiatingHttpJsonChannelProvider.newBuilder().setHeaderProvider(headerProvider).build();
        LanguageServiceSettings settings = LanguageServiceSettings.newBuilder().setTransportChannelProvider(transportChannelProvider).build();
        LanguageServiceClient client = LanguageServiceClient.create(settings);
        return client;
      }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
