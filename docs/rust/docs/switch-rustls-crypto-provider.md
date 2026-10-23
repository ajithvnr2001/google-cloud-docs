---
url: https://docs.cloud.google.com/rust/docs/switch-rustls-crypto-provider/
title: Switch the default crypto provider \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:20.553982+00:00
---

# Switch the default crypto provider  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/switch-rustls-crypto-provider/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Switch the default crypto provider Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to switch the default `rustls` crypto provider in Rust. You may want to switch the default crypto provider if your application has specific requirements not met by our default.

The Rust client libraries use [Rustls](https://docs.cloud.google.com/rust/docs/a%20modern%20TLS%20library) to secure the communication between your application and Google Cloud. Rustls can use different providers for cryptographic functions. By default, the client libraries enable the [aws-lc-rs](https://crates.io/crates/aws-lc-rs) provider. The client libraries use this as a default as it is based on BoringSSL, a well-regarded crypto library implemented by Google, and it is the only Rust crypto provider that is [FIPS](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) certified.

Nevertheless, some applications may need to use a different provider. This guide shows you how to disable the default provider and configure your own, using `google-cloud-storage` to illustrate how to change the requirements for Rust, with [ring](https://crates.io/crates/ring) as an alternative crypto provider. This process can be customized for other client libraries. Consult the [rustls documentation](https://docs.rs/rustls) for additional providers.

## Use the client libraries with the default crypto provider

To use the default crypto provider, add the client library as a dependency to your `Cargo.toml` file:
    
    
    [dependencies]
    google-cloud-storage = { version = "1" }
    

## Use the default crypto provider with other default features disabled

Some applications prefer to disable all the default features in their dependencies and then only enable the features they want to use. For example, your `Cargo.toml` may read:
    
    
    [dependencies]
    google-cloud-storage = { version = "1", default-features = false }
    

To enable only the default provider feature use:
    
    
    [dependencies]
    google-cloud-storage = { version = "1", default-features = false, features = ["default-rustls-provider"] }
    

## Use your own crypto provider

To select your own provider:

  1. Add Rust with the default features disabled and include any dependencies needed for your provider. In this guide, we are using `ring`:

You must use the same version of `rustls` as `google-cloud-storage`. 
         
         [dependencies]
         google-cloud-storage = { version = "1", default-features = false }
         rustls               = { version = "0.23", features = ["ring"] }
         

  2. Change your `main()` function to install this provider:
         
         use rustls::crypto::{CryptoProvider, ring::default_provider};
         
         #[tokio::main]
         async fn main() -> anyhow::Result<()> {
             // Install a default crypto provider.
             CryptoProvider::install_default(default_provider())
                 .map_err(|_| anyhow::anyhow!("default crypto provider already installed"))?;
             // ... ... ...
             Ok(())
         }
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
