---
url: https://docs.cloud.google.com/rust/docs/initialize-client/
title: How to initialize a client \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:13.717635+00:00
---

# How to initialize a client  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/initialize-client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  How to initialize a client Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud Client Libraries for Rust use clients as the main abstraction to interface with specific services. Clients are implemented as Rust structs, with methods corresponding to each RPC offered by the service. To use a Google Cloud service using the Rust client libraries, you need to first initialize a client.

In this guide you'll initialize a client and then use the client to make an RPC using the [Secret Manager API](https://docs.cloud.google.com/secret-manager). The same structure applies to any other service in Google Cloud.

Before following this guide, you should do the following: 

  * Follow one of the Secret Manager getting started guides, such as the guide on how to [Create a secret](https://docs.cloud.google.com/rust/secret-manager/docs/creating-and-accessing-secrets). These guides cover service-specific concepts in more detail, and provide detailed guidance on project prerequisites.
  * Follow the instructions in the [Authenticate for using client libraries guide](https://cloud.google.com/docs/authentication/client-libraries). This guide will show you how to login to [configure Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials) used in this guide.



## Dependencies

With Rust, you must declare the dependency in your `Cargo.toml` file:
    
    
    $ cargo add google-cloud-secretmanager-v1
    

To initialize a client, you first call `Client::builder()` to obtain an appropriate [`ClientBuilder`](https://docs.rs/google-cloud-gax/latest/google_cloud_gax/client_builder/struct.ClientBuilder.html) and then call `build()` on that builder to create a client.

The following creates a client with the default configuration, which is designed to meet requirements for most use cases.
    
    
        let client = SecretManagerService::builder().build().await?;
    

Once the client is successfully initialized, you can use it to make RPCs:
    
    
        use google_cloud_gax::paginator::Paginator as _;
        let mut items = client
            .list_locations()
            .set_name(format!("projects/{project_id}"))
            .by_page();
        while let Some(page) = items.next().await {
            let page = page?;
            for location in page.locations {
                println!("{}", location.name);
            }
        }
    

This example shows a call to `list_locations`, which returns information about the supported locations for the service (in this case, Secret Manager).

The output of the example should look something like this:
    
    
    projects/123456789012/locations/europe-west8
    projects/123456789012/locations/europe-west9
    projects/123456789012/locations/us-east5
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
