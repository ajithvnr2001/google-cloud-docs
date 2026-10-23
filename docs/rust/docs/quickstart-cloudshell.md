---
url: https://docs.cloud.google.com/rust/docs/quickstart-cloudshell/
title: Quickstart: Set up Rust on Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:23.836977+00:00
---

# Quickstart: Set up Rust on Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/quickstart-cloudshell/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Quickstart: Set up Rust on Cloud Shell Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Shell is a great environment to run small examples and tests. This guide shows you how to configure Rust and install one of the Cloud Client Libraries in Cloud Shell.

### Start up Cloud Shell

  1. In the Google Cloud console [project selector](https://console.cloud.google.com/projectselector2/home/dashboard) , select a project.
  2. Open [`https://shell.cloud.google.com`](https://shell.cloud.google.com) to start a new shell. You might be prompted to [authorize Cloud Shell](https://docs.cloud.google.com/shell/docs/auth) to use your credentials for Google Cloud API calls.



### Configure Rust

  1. Cloud Shell comes with [`rustup`](https://rust-lang.github.io/rustup/) pre-installed. You can use it to install and configure the default version of Rust:
         
         rustup default stable
         

  2. Confirm that you have the most recent version of Rust installed:
         
         cargo --version
         




### Install Rust client libraries in Cloud Shell

  1. Create a new Rust project:
         
         cargo new my-project
         

  2. Change your directory to the new project:
         
         cd my-project
         

  3. Add the [Secret Manager client library](https://docs.cloud.google.com/secret-manager/docs/overview) to the new project:
         
         cargo add google-cloud-secretmanager-v1
         

  4. Add the [google-cloud-gax crate](https://crates.io/crates/google-cloud-gax) to the new project:
         
         cargo add google-cloud-gax
         

  5. Add the [tokio crate](https://crates.io/crates/tokio) to the new project:
         
         cargo add tokio --features macros
         

  6. Edit `src/main.rs` in your project to use the Secret Manager client library:
         
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
         

  7. Run your program, supplying your Google Cloud project ID:
         
         PROJECT_ID=$(gcloud config get project)
         cargo run ${PROJECT_ID}
         

The program will print the secrets associated with your project ID. If you don't see any secrets, you might not have any in Secret Manager. [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) and rerun the program, and you should see the secret printed in the output.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
