---
url: https://docs.cloud.google.com/rust/docs/enable-logging/
title: Enable logging \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:02:05.237318+00:00
---

# Enable logging  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/enable-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Enable logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to enable logging in Rust. Logging requests and responses to the console can make it easier to troubleshoot applications.

**Warning:** These logs described in this document are meant to be used for debugging applications. The logs include full requests and response messages, which may include sensitive information. If you decide to enable these logs in production, consider the security and privacy implications first.

## Prerequisites

This guide uses the [Secret Manager API](https://cloud.google.com/secret-manager), which must be enabled before you begin. To learn how to enable services, follow the [service quickstart](https://cloud.google.com/secret-manager/docs/quickstart).

For complete setup instructions for the Rust libraries, see [Getting started with Rust](https://docs.cloud.google.com/rust/quickstart).

### Dependencies

You must declare the dependencies in your `Cargo.toml` file:
    
    
    cargo add google-cloud-secretmanager-v1 google-cloud-gax
    

## Enable logging

The Rust client libraries use Tokio's [tracing](https://docs.rs/tracing/latest/tracing/index.html) crate to collect scoped, structured, and async-aware diagnostics. The tracing crate separates sources of diagnostics (such as the Rust client libraries) from the components that collect these diagnostics using the `Subscriber` trait. There are many implementations available for the `Subscriber`. In this example we will use the [fmt](https://docs.rs/tracing-subscriber/latest/tracing_subscriber/fmt/index.html) subscriber included with the `tracing-subscriber` crate.

  1. Add a dependency on the `tracing-subscriber` crate:
         
         cargo add tracing tracing-subscriber
         

  2. Write a function that receives the project ID as a function parameter: 
         
         /// # Parameters
         /// - `project_id`: the id of a Google Cloud project, or its numeric ID.
         ///   For example: `my-project`.
         pub async fn sample(project_id: &str) -> anyhow::Result<()> {

  3. Introduce a few use declarations to make the example more readable: 
         
         use google_cloud_gax::paginator::ItemPaginator;
         use google_cloud_secretmanager_v1::client::SecretManagerService;
         use tracing_subscriber;

  4. Initialize the default tracing subscriber: 
         
         tracing_subscriber::fmt::init();

  5. Initialize a client with tracing enabled. Note the call to `.with_tracing()`: 
         
         let client = SecretManagerService::builder()
             .with_tracing()
             .build()
             .await?;

  6. Then use the client to send a request: 
         
         let mut items = client
             .list_secrets()
             .set_parent(format!("projects/{project_id}"))
             .by_item();
         println!("listing all secrets in project {project_id}");
         while let Some(secret) = items.next().await.transpose()? {
             println!("  {secret:?}");
         }
         println!("DONE");




### Expected output

The output (slightly edited for readability) will include a line such as:
    
    
    2025-11-03T14:17:31.759452Z  INFO list_secrets{self=SecretManagerService ...
    

This line includes the request:
    
    
    req=ListSecretsRequest { parent: "projects/... }
    

The response:
    
    
    return=Ok(Response { parts: ..., body: ListSecretsResponse { ...
    

## More information

The default subscriber created using `tracing_subscriber::fmt::init()` can be configured dynamically using the `RUST_LOG` environment variable. See [its documentation](https://docs.rs/tracing-subscriber/latest/tracing_subscriber/fmt/fn.init.html) for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
