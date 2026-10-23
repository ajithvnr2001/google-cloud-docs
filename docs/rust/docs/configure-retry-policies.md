---
url: https://docs.cloud.google.com/rust/docs/configure-retry-policies/
title: Configuring retry policies \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:43:00.747945+00:00
---

# Configuring retry policies  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/configure-retry-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Configuring retry policies Stay organized with collections  Save and categorize content based on your preferences. 

The Google Cloud client libraries for Rust can automatically retry operations that fail due to transient errors. Learn how to create and customize retry loops, implement a common retry policy for all requests, and override default policies for specific requests.

## Prerequisites

The examples in this guide use the Secret Manager service. However, the same concepts work for other Google Cloud services.

Before continuing, follow [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart) to enable and authenticate the Secret Manager API.

## Dependencies

After enabling Secret Manager, declare your dependencies in your `Cargo.toml` file:
    
    
    cargo add google-cloud-secretmanager-v1
    

## Configure the default retry policy

This example uses the `Aip194Strict` policy. This policy is based on the guidelines in [AIP-194](https://google.aip.dev/194), which documents the conditions under which a Google API client should automatically retry a request.

**Note:** The `AIP-194` policy is fairly strict, and won't retry any error that indicates the request might have reached the service, unless the request is idempotent. As such, the policy is safe to use as a default. The only downside might be additional requests to the service, consuming some quota and billing.

To make the `Aip194Strict` policy the default policy for a service, set the policy during [client initialization](https://docs.cloud.google.com/rust/initialize-client):
    
    
       let client = SecretManagerService::builder()
           .with_retry_policy(Aip194Strict)
           .build()
           .await?;
    

Once you've set the policy, you can use the service as usual:
    
    
       let mut list = client
           .list_secrets()
           .set_parent(format!("projects/{project_id}"))
           .by_item();
       while let Some(secret) = list.next().await {
           let secret = secret?;
           println!("  secret={}", secret.name);
       }
    

### Configuring the default retry policy: complete code

This code sample applies the `Aip194Strict` policy to the Secret Manager service.
    
    
    use google_cloud_gax::paginator::ItemPaginator as _;
    use google_cloud_gax::retry_policy::Aip194Strict;
    use google_cloud_secretmanager_v1::client::SecretManagerService;
    
    pub async fn sample(project_id: &str) -> anyhow::Result<()> {
       let client = SecretManagerService::builder()
           .with_retry_policy(Aip194Strict)
           .build()
           .await?;
    
       let mut list = client
           .list_secrets()
           .set_parent(format!("projects/{project_id}"))
           .by_item();
       while let Some(secret) = list.next().await {
           let secret = secret?;
           println!("  secret={}", secret.name);
       }
    
       Ok(())
    }
    

## Configure the default retry policy with limits

By default, the `Aip194Strict` policy does not limit the number of retry attempts or the time spent retrying requests. However, you can add limits to the policy.

For example, you can limit both the number of attempts and the time spent in the retry loop:
    
    
       let client = SecretManagerService::builder()
           .with_retry_policy(
               Aip194Strict
                   .with_attempt_limit(5)
                   .with_time_limit(Duration::from_secs(15)),
           )
           .build()
           .await?;
    

With this configuration, requests will work as usual:
    
    
       let mut list = client
           .list_secrets()
           .set_parent(format!("projects/{project_id}"))
           .by_item();
       while let Some(secret) = list.next().await {
           let secret = secret?;
           println!("  secret={}", secret.name);
       }
    

### Configure the default retry policy with limits: complete code

This code sample applies the `Aip194Strict` policy to the Secret Manager service with a custom attempt limit and time limit.
    
    
    use google_cloud_gax::paginator::ItemPaginator as _;
    use google_cloud_gax::retry_policy::Aip194Strict;
    use google_cloud_gax::retry_policy::RetryPolicyExt;
    use google_cloud_secretmanager_v1::client::SecretManagerService;
    use std::time::Duration;
    
    
    pub async fn sample(project_id: &str) -> anyhow::Result<()> {
       let client = SecretManagerService::builder()
           .with_retry_policy(
               Aip194Strict
                   .with_attempt_limit(5)
                   .with_time_limit(Duration::from_secs(15)),
           )
           .build()
           .await?;
    
    
       let mut list = client
           .list_secrets()
           .set_parent(format!("projects/{project_id}"))
           .by_item();
       while let Some(secret) = list.next().await {
           let secret = secret?;
           println!("  secret={}", secret.name);
       }
    
    
       Ok(())
    }
    

## Override the retry policy for a request

Sometimes applications need to override the retry policy for a specific request. For example, the application developer might know specific details of the service or application and determine it is safe to tolerate more errors.

For example, deleting a secret is idempotent, because it can only succeed once. But the client library assumes all delete operations are unsafe. You can override the policy for a request:
    
    
       client
           .delete_secret()
           .set_name(format!("projects/{project_id}/secrets/{secret_id}"))
           .with_retry_policy(
               AlwaysRetry
                   .with_attempt_limit(5)
                   .with_time_limit(Duration::from_secs(15)),
           )
           .send()
           .await?;
    

### Override the retry policy for a request: complete code

This code sample overrides the attempt limit and time limit for a specific request to the Secret Manager service.
    
    
    use google_cloud_gax::options::RequestOptionsBuilder;
    use google_cloud_gax::retry_policy::AlwaysRetry;
    use google_cloud_gax::retry_policy::RetryPolicyExt;
    use google_cloud_secretmanager_v1::client::SecretManagerService;
    use std::time::Duration;
    
    
    pub async fn sample(
       client: &SecretManagerService,
       project_id: &str,
       secret_id: &str,
    ) -> anyhow::Result<()> {
       client
           .delete_secret()
           .set_name(format!("projects/{project_id}/secrets/{secret_id}"))
           .with_retry_policy(
               AlwaysRetry
                   .with_attempt_limit(5)
                   .with_time_limit(Duration::from_secs(15)),
           )
           .send()
           .await?;
    
    
       Ok(())
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
