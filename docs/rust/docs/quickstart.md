---
url: https://docs.cloud.google.com/rust/docs/quickstart/
title: Get started with Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:20.514400+00:00
---

# Get started with Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Get started with Rust Stay organized with collections  Save and categorize content based on your preferences. 

Before you get started, you should meet the following prerequisites:

  * Install Rust. If you have not yet installed Rust, see the Rust documentation on [Getting started](https://www.rust-lang.org/learn/get-started).

You can confirm that you have Rust installed (and your version of Rust) with the following command:
        
        cargo --version
        

  * Install an editor or IDE.

  * Install the Google Cloud CLI.




## Create a new Rust project

To create a new Rust project, run the following command:
    
    
    cargo new my-project
    

Change your directory to the new project by running the following command:
    
    
    cd my-project
    

## Install a Google Cloud Client Library

The Cloud Client Libraries for Rust is the idiomatic way for Rust developers to integrate with Google Cloud services, such as Secret Manager and Workflows.

  1. Add the [Secret Manager client library](https://docs.cloud.google.com/secret-manager/docs/overview) to your new project:
         
         cargo add google-cloud-secretmanager-v1
         

  2. If you haven't already enabled the Secret Manager API, enable it in [APIs and services](https://console.cloud.google.com/apis) or by running the following command:
         
         gcloud services enable secretmanager.googleapis.com
         

  3. Add the [`google-cloud-gax` crate](https://crates.io/crates/google-cloud-gax) to the new project:
         
         cargo add google-cloud-gax
         

  4. Add the [tokio crate](https://crates.io/crates/tokio) to the new project:
         
         cargo add tokio --features macros
         

  5. Edit `src/main.rs` in your project to use the Secret Manager client library:
         
         #[tokio::main]
         async fn main() -> Result<(), Box<dyn std::error::Error>> {
             use google_cloud_gax::paginator::ItemPaginator as _;
             use google_cloud_secretmanager_v1::client::SecretManagerService;
             let project_id = std::env::args().nth(1).unwrap();
             let client = SecretManagerService::builder().build().await?;
         
             let mut items = client
                 .list_secrets()
                 .set_parent(format!("projects/{project_id}"))
                 .by_item();
             while let Some(item) = items.next().await {
                 println!("{}", item?.name);
             }
             Ok(())
         }
         

  6. Finally, build your program:
         
         cargo build
         




The program should build without errors.

## Running your Rust application

To use the Cloud Client Libraries in a local development environment, set up Application Default Credentials.

To set up Application Default Credentials, run the following command:
    
    
    gcloud auth application-default login
    

**Note:** For more information, see [Authenticate for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

Run your program, supplying your Google Cloud project ID:
    
    
    PROJECT_ID=$(gcloud config get project)
    cargo run ${PROJECT_ID}
    

The program will print the secrets associated with your project ID. If you don't see any secrets, you might not have any in Secret Manager. [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) and rerun the program, and you should see the secret printed in the output.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
