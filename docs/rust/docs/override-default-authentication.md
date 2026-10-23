---
url: https://docs.cloud.google.com/rust/docs/override-default-authentication/
title: Override the default authentication method \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:55:49.828353+00:00
---

# Override the default authentication method  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/override-default-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Override the default authentication method Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to override the default authentication used by Rust. The Rust automatically authenticate your requests to Google Cloud services, but you may occasionally need to override your default credentials.

## Prerequisites

This guide uses the [Cloud Natural Language API](https://cloud.google.com/natural-language). To install this API follow the [service quickstart](https://cloud.google.com/natural-language/docs/setup), which shows you how to enable a service.

For complete setup instructions for the Rust libraries, see [Getting started with Rust](https://docs.cloud.google.com/rust/quickstart).

### Dependencies

You must declare the dependencies in your `Cargo.toml` file:
    
    
    cargo add google-cloud-language-v2 google-cloud-auth
    

## The default credentials

The recommended way to authenticate applications in Google Cloud is to use Application Default Credentials, without any configuration the client libraries default to this credential type. See [How Application Default Credentials work](https://cloud.google.com/docs/authentication/application-default-credentials) for information about you can configure this default without any code changes in your application.

  1. Add some use declarations to simplify the rest of the example: 
         
         use google_cloud_language_v2::client::LanguageService;
         use google_cloud_language_v2::model::{Document, document::Type};

  2. Initialize the client using the defaults: 
         
         let client = LanguageService::builder().build().await?;

  3. Use this client as usual: 
         
         let response = client
             .analyze_sentiment()
             .set_document(
                 Document::new()
                     .set_content("Hello World!")
                     .set_type(Type::PlainText),
             )
             .send()
             .await?;
         println!("response={response:?}");




## Override the default credentials: API keys

[API keys](https://cloud.google.com/docs/authentication/api-keys) are text strings that grant access to some Google Cloud services. Using API keys may simplify development as they require less configuration than other [authentication methods](https://cloud.google.com/docs/authentication). There are some risks associated with API keys, we recommended you read [Best practices for managing API keys](https://cloud.google.com/docs/authentication/api-keys-best-practices) if you plan to use them.

  1. Write a function that receives the API key string as an input parameter: 
         
         pub async fn sample(key: &str) -> anyhow::Result<()> {

  2. Add some use declarations simplify the rest of the example: 
         
         use google_cloud_auth::credentials::api_key_credentials::Builder as ApiKeyCredentialsBuilder;
         use google_cloud_language_v2::client::LanguageService;
         use google_cloud_language_v2::model::{Document, document::Type};

  3. Use the API Keys [Builder](https://docs.rs/google-cloud-auth/latest/google_cloud_auth/credentials/api_key_credentials/struct.Builder.html) to create the credentials: 
         
         let credentials = ApiKeyCredentialsBuilder::new(key).build();

  4. Initialize the client using the `credentials` object: 
         
         let client = LanguageService::builder()
             .with_credentials(credentials)
             .build()
             .await?;

  5. And use this client as usual: 
         
         let response = client
             .analyze_sentiment()
             .set_document(
                 Document::new()
                     .set_content("Hello World!")
                     .set_type(Type::PlainText),
             )
             .send()
             .await?;
         println!("response={response:?}");




## Override the default credentials: service account impersonation

Service account impersonation lets you make API calls on behalf of a service account. [Use service account impersonation](https://cloud.google.com/docs/authentication/use-service-account-impersonation) discusses this form of authentication in detail.

When you use service account impersonation, you start with an authenticated principal (your user account or a service account) and request short-lived credentials for a service account that has the authorization that your use case requires.

It is more secure than downloading a service account key for the target service account, as you don't need to hold the credentials in the file system or even in memory.

  1. Write the example in a function that receives the service account identifier as an input parameter. This can be the service account email or the unique numeric Google-assigned identifier of the service account. 
         
         /// # Parameters
         /// * `target_principal`: the email or unique id of the target service account.
         ///   For example: `my-service-account@my-project.iam.gserviceaccount.com`.
         pub async fn sample(target_principal: &str) -> anyhow::Result<()> {

  2. Add some use declarations simplify the rest of the example: 
         
         use google_cloud_auth::credentials::Builder as AdcCredentialsBuilder;
         use google_cloud_auth::credentials::impersonated::Builder as ImpersonatedCredentialsBuilder;
         use google_cloud_language_v2::client::LanguageService;
         use google_cloud_language_v2::model::{Document, document::Type};

  3. Use the impersonated service account [Builder](https://docs.rs/google-cloud-auth/latest/google_cloud_auth/credentials/impersonated/struct.Builder.html) to create the credentials: 
         
         let credentials = ImpersonatedCredentialsBuilder::from_source_credentials(
             AdcCredentialsBuilder::default().build()?,
         )
         .with_target_principal(target_principal)
         .build()?;

  4. Initialize the client using the `credentials` object: 
         
         let client = LanguageService::builder()
             .with_credentials(credentials)
             .build()
             .await?;

  5. And use this client as usual: 
         
         let response = client
             .analyze_sentiment()
             .set_document(
                 Document::new()
                     .set_content("Hello World!")
                     .set_type(Type::PlainText),
             )
             .send()
             .await?;
         println!("response={response:?}");




## More Information

Learn about other authentication methods in the Rust client libraries:

  * [Anonymous Credentials](https://docs.rs/google-cloud-auth/latest/google_cloud_auth/credentials/anonymous/struct.Builder.html): to access services or resources that don't require authentication.
  * [External Accounts](https://docs.rs/google-cloud-auth/latest/google_cloud_auth/credentials/external_account/struct.Builder.html): to use [Workload identity federation](https://cloud.google.com/iam/docs/workload-identity-federation) with the Rust client libraries.
  * [Service Accounts](https://docs.rs/google-cloud-auth/latest/google_cloud_auth/credentials/impersonated/struct.Builder.html): to initialize credentials from a [service account key](https://cloud.google.com/iam/docs/service-account-creds#key-types).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
