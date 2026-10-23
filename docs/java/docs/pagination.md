---
url: https://docs.cloud.google.com/java/docs/pagination/
title: Manage pagination \u00a0|\u00a0 Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:57.824358+00:00
---

# Manage pagination  |  Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/pagination/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Manage pagination Stay organized with collections  Save and categorize content based on your preferences. 

Most list methods in the Google Cloud Java library return a `PagedResponse` object. This lets you iterate over results without manually managing page tokens.

The easiest way to handle pagination is to use the `iterateAll()` method. The library automatically fetches new pages in the background as you iterate through the collection.
    
    
    import com.google.cloud.secretmanager.v1.[ListSecretsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ListSecretsRequest.html);
    import com.google.cloud.secretmanager.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ProjectName.html);
    import com.google.cloud.secretmanager.v1.[Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    
    try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) secretManager = [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create()) {
        // Prepare the request
        [ListSecretsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ListSecretsRequest.html) request = [ListSecretsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ListSecretsRequest.html).newBuilder()
            .setParent([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ProjectName.html).of("my-project").toString())
            .build();
    
        // Call the API
        // This returns a PagedResponse
        [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).[ListSecretsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.ListSecretsPagedResponse.html) response = secretManager.listSecrets(request);
    
        // Automatically fetches subsequent pages of secrets
        for ([Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) secret : response.iterateAll()) {
            System.out.printf("Secret: %s%n", secret.getName());
        }
    }
    

### Manual pagination (accessing tokens)

If you need to control pagination manually (e.g., for a web API that sends tokens to a frontend), you can access the `nextPageToken` from the response.
    
    
    // Prepare request with page size and optional token
    ListSecretsRequest.Builder requestBuilder = ListSecretsRequest.newBuilder()
        .setParent(ProjectName.of("my-project").toString())
        .setPageSize(10);
    
    // Check if we have a token from a previous request (e.g., from a query parameter)
    String pageToken = request.getParameter("page_token");
    if (pageToken != null) {
        requestBuilder.setPageToken(pageToken);
    }
    
    SecretManagerServiceClient.ListSecretsPagedResponse response = secretManager.listSecrets(requestBuilder.build());
    
    // Process current page items
    for (Secret secret : response.getPage().getValues()) {
        // Process current page items
    }
    
    // Get the token for the next page (empty string if no more pages)
    String nextToken = response.getNextPageToken();
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
