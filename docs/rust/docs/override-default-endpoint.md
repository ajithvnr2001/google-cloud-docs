---
url: https://docs.cloud.google.com/rust/docs/override-default-endpoint/
title: Override the default endpoint \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:36.959360+00:00
---

# Override the default endpoint  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/override-default-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Override the default endpoint Stay organized with collections  Save and categorize content based on your preferences. 

The Rust client libraries automatically configure the endpoint for each service. Some applications may need to override the default endpoint either because their network has specific requirements, or because they need to use regional versions of the service. This guide shows you how to override the default.

## Prerequisites

This guide uses the [Secret Manager API](https://cloud.google.com/secret-manager). To enable this API, follow the [service quickstart](https://cloud.google.com/secret-manager/docs/quickstart).

For complete setup instructions for the Rust client libraries, see [Getting started with Rust](https://docs.cloud.google.com/rust/quickstart).

### Dependencies

You must declare the dependencies in your `Cargo.toml` file:
    
    
    cargo add google-cloud-secretmanager-v1 google-cloud-gax
    

## The default endpoint

First, review how to use the client libraries with the default endpoint. Start by writing some use declarations to simplify the rest of the example:

  1. Write the example in a function that receives the project ID as a parameter: 
         
         /// # Parameters
         /// - `project_id`: the id of a Google Cloud project, or its numeric ID.
         ///   For example: `my-project`.
         pub async fn sample(project_id: &str) -> anyhow::Result<()> {

  2. Add some use declarations simplify the example code: 
         
         pub use google_cloud_gax::paginator::ItemPaginator;
         pub use google_cloud_secretmanager_v1::client::SecretManagerService;

  3. Initialize the client using the defaults: 
         
         let client = SecretManagerService::builder().build().await?;

  4. And use this client as usual: 
         
         let mut items = client
             .list_secrets()
             .set_parent(format!("projects/{project_id}"))
             .by_item();
         println!("listing all secrets in project {project_id}");
         while let Some(secret) = items.next().await.transpose()? {
             println!("  {secret:?}");
         }
         println!("DONE");




## Override the default endpoint

In this example we configure the client library to use secret manager's [regional endpoints](https://cloud.google.com/sovereign-controls-by-partners/docs/regional-endpoints). The same override can be used to configure the endpoint with one of the [private access options](https://docs.cloud.google.com/vpc/docs/private-access-options), or for [locational endpoints](https://docs.cloud.google.com/storage/docs/locational-endpoints) in the services that support them.

  1. As before, write an example that receives the project ID and region as parameters: 
         
         /// # Parameters
         /// - `project_id`: the id of a Google Cloud project, or its numeric ID.
         ///   For example: `my-project`.
         /// - `region`: the id of a Gooogle Cloud region. For example `us-central1`.
         pub async fn sample(project_id: &str, region: &str) -> anyhow::Result<()> {

  2. Add some use declarations to simplify the code: 
         
         pub use google_cloud_gax::paginator::ItemPaginator;
         pub use google_cloud_secretmanager_v1::client::SecretManagerService;

  3. Initialize the client using the target endpoint: 
         
         let client = SecretManagerService::builder()
             .with_endpoint(format!("https://secretmanager.{region}.rep.googleapis.com"))
             .build()
             .await?;

  4. And use this client as usual: 
         
         let mut items = client
             .list_secrets()
             .set_parent(format!("projects/{project_id}/locations/{region}"))
             .by_item();
         println!("listing all secrets in project {project_id} and region {region}");
         while let Some(secret) = items.next().await.transpose()? {
             println!("  {secret:?}");
         }
         println!("DONE");




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
