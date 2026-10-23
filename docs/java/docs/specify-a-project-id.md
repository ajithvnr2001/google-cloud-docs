---
url: https://docs.cloud.google.com/java/docs/specify-a-project-id/
title: Specify a project ID \u00a0|\u00a0 Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:07.925801+00:00
---

# Specify a project ID  |  Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/specify-a-project-id/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Specify a project ID Stay organized with collections  Save and categorize content based on your preferences. 

Most Google Cloud libraries require a project ID. There are multiple ways to specify this project ID.

When using Google Cloud libraries from within Compute Engine or App Engine, the project ID is often automatically inferred.

In other environments, use one of the following methods: * Supply the project ID when you build the service-specific settings object. For example, to use Firestore in Datastore mode (Datastore) from a project with ID `PROJECT_ID`, write:
    
    
       Datastore datastore = DatastoreOptions.newBuilder().setProjectId("PROJECT_ID").build().getService();
    

  * Specify your project ID as the `GOOGLE_CLOUD_PROJECT` environment variable.

For example: `none export GOOGLE_CLOUD_PROJECT=PROJECT_ID`

  * Set the project ID by using the [Google Cloud SDK](https://docs.cloud.google.com/java/sdk/). To use the SDK, [download the SDK](https://docs.cloud.google.com/java/sdk/), and set the project ID from the command line.

For example: `none gcloud config set project PROJECT_ID`




Google Cloud determines the project ID from the following sources, in the listed order, and stops once it finds a value:

  1. The project ID supplied when building the service options.
  2. The project ID specified by the environment variable `GOOGLE_CLOUD_PROJECT`.
  3. The App Engine or Compute Engine project ID.
  4. The project ID specified in the JSON credentials file pointed to by the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.
  5. The Google Cloud SDK project ID.



If you need to programmatically access the project ID that the client library will use based on the environment, you can use the following helper method:
    
    
         import com.google.cloud.[ServiceOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions.html);
         // Additional imports or code here
         [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId = [ServiceOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ServiceOptions.html).getDefaultProjectId();
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
