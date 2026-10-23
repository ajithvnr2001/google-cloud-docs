---
url: https://docs.cloud.google.com/rust/docs/configure-polling-policies/
title: Configuring polling policies \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:44:01.755203+00:00
---

# Configuring polling policies  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/configure-polling-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Configuring polling policies Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to configure polling policies for long-running operations. The Google Cloud client libraries for Rust provide helper functions to simplify the progress monitoring of long-running operations (LROs). These helpers use policies to configure polling frequency and determine which polling errors are transient (and can be safely retried) and which are unrecoverable.

Two policies control the behavior of the LRO loops:

  * The **polling backoff policy** controls how long the loops wait before polling the status of an LRO that is still in progress.
  * The **polling error policy** controls what to do on a polling error. Some polling errors are unrecoverable and indicate that the operation was aborted or the caller has no permissions to check the status of the LRO. Other polling errors are transient and indicate a temporary problem in the client network or the service.



You can set each of these policies independently. Additionally, you can apply a policy to all LROs started on a client or change the policy for a single request.

## Prerequisites

This guide uses the Cloud Storage service to keep the code snippets concrete, but the same concepts apply to any other service using LROs.

Before using this guide, follow [Using Cloud Storage with Rust](https://docs.cloud.google.com/rust/docs/quickstart-storage) to enable and authenticate the Cloud Storage API.

For complete setup instructions for the Rust libraries, see [Setting up your development environment](https://docs.cloud.google.com/rust/docs/quickstart).

## Dependencies

Add the following dependencies to your `Cargo.toml` file:
    
    
    cargo add google-cloud-storage google-cloud-lro
    

## Configure the polling frequency for all requests in a client

If you plan to use the same polling backoff policy for most requests with the same client, consider setting the policy as a client option. This code sample configures the polling frequency for all requests to the Cloud Storage service.
    
    
    pub async fn client_backoff(bucket: &str, folder: &str, dest: &str) -> Result<()> {
        // Use a type that implements the `PollingBackoffPolicy` trait, in this case
        // `ExponentialBackoffBuilder`.
        use google_cloud_gax::exponential_backoff::ExponentialBackoffBuilder;
        use google_cloud_lro::Poller;
        use std::time::Duration;
    
        let client = StorageControl::builder()
            // Initialize the policy with a chosen delay duration.
            .with_polling_backoff_policy(
                ExponentialBackoffBuilder::new()
                    .with_initial_delay(Duration::from_millis(250))
                    .with_maximum_delay(Duration::from_secs(10))
                    .build()?,
            )
            .build()
            .await?;
    
        // Initiate an LRO using polling.
        let response = client
            .rename_folder()
            .set_name(format!("projects/_/buckets/{bucket}/folders/{folder}"))
            .set_destination_folder_id(dest)
            .poller()
            .until_done()
            .await?;
    
        println!("LRO completed, response={response:?}");
    
        Ok(())
    }
    

Unless you override the policy with a per-request setting, the policy remains in effect for any long-running operation started by the client.

For example, the following call will use this policy:
    
    
        let mut operation = client
            .rename_folder()
            /* more stuff */
            .send()
            .await?;
    

In this example call, the client library waits for 250 ms after the first polling attempt, then for 500 ms for the second attempt. Subsequent attempts wait for 1 s, 2 s, 4 s, and 8 s, and then all further attempts wait for 10 s.

## Configure the polling frequency for a specific request

You can configure the polling frequency for an individual request, which overrides any policy set at the client level. For example:
    
    
    pub async fn rpc_backoff(bucket: &str, folder: &str, dest: &str) -> Result<()> {
        // Use a type that implements the `PollingBackoffPolicy` trait, in this case
        // `ExponentialBackoffBuilder`.
        use google_cloud_gax::exponential_backoff::ExponentialBackoffBuilder;
        use std::time::Duration;
    
        // To configure the request, bring the RequestOptionsBuilder trait into
        // scope.
        use google_cloud_gax::options::RequestOptionsBuilder;
        use google_cloud_lro::Poller;
    
        let client = StorageControl::builder().build().await?;
        // Create the request builder.
        let response = client
            .rename_folder()
            // Configure the polling backoff policy.
            .with_polling_backoff_policy(
                ExponentialBackoffBuilder::new()
                    .with_initial_delay(Duration::from_millis(250))
                    .with_maximum_delay(Duration::from_secs(10))
                    .build()?,
            )
            .set_name(format!("projects/_/buckets/{bucket}/folders/{folder}"))
            .set_destination_folder_id(dest)
            // Issue the polling request as normal.
            .poller()
            .until_done()
            .await?;
    
        println!("LRO completed, response={response:?}");
    
        Ok(())
    }
    

## Configure retryable polling errors for all requests in a client

To configure retryable errors, use a type that implements the `PollingErrorPolicy` trait. The client libraries provide several policies; a conservative choice is `Aip194Strict`. If you plan to use the same polling policy for most requests with the same client, consider setting the policy as a client option.

This code sample configures the retryable polling errors for all requests to the Cloud Storage service:
    
    
    pub async fn client_error_policy(bucket: &str, folder: &str, dest: &str) -> Result<()> {
        // Use a type that implements the `PollingErrorPolicy` trait, in this case
        // `Aip194Strict`.
        use google_cloud_gax::polling_error_policy::Aip194Strict;
        use google_cloud_gax::polling_error_policy::PollingErrorPolicyExt;
        use google_cloud_lro::Poller;
        use std::time::Duration;
    
        // Add the polling policy that you want to use for all long-running
        // operations.
        let client = StorageControl::builder()
            .with_polling_error_policy(
                Aip194Strict
                    .with_attempt_limit(100)
                    .with_time_limit(Duration::from_secs(300)),
            )
            .build()
            .await?;
    
        // Initiate an LRO using polling.
        let response = client
            .rename_folder()
            .set_name(format!("projects/_/buckets/{bucket}/folders/{folder}"))
            .set_destination_folder_id(dest)
            .poller()
            .until_done()
            .await?;
    
        println!("LRO completed, response={response:?}");
    
        Ok(())
    }
    

While the polling error policy handles errors during the LRO wait loop, you can also add a standard retry policy to handle transient errors that might occur when initially sending the request to start the LRO:
    
    
        let client = StorageControl::builder()
            .with_retry_policy(
                retry_policy::Aip194Strict
                    .with_attempt_limit(100)
                    .with_time_limit(Duration::from_secs(300)),
            )
            .build()
            .await?;
    

Unless you override the policy with a per-request setting, this policy remains in effect for any long-running operation started by the client. For example, if you make the following call:
    
    
        let mut operation = client
            .rename_folder()
            /* more stuff */
            .send()
            .await?;
    

**Note:** The client library treats only `UNAVAILABLE` (see [AIP-194](https://google.aip.dev/194)) as a retryable error and stops polling after 100 attempts or 300 seconds, whichever comes first.

## Configure retryable polling errors for a specific request

You can configure retryable polling errors for a specific request by using a type that implements the `PollingErrorPolicy` trait and bringing the `RequestOptionsBuilder` trait into scope.

This code sample configures retryable polling errors for a specific request to the Cloud Storage service.
    
    
    pub async fn rpc_error_policy(bucket: &str, folder: &str, dest: &str) -> Result<()> {
        // Use a type that implements the `PollingErrorPolicy` trait, in this case
        // `Aip194Strict`.
        use google_cloud_gax::polling_error_policy::Aip194Strict;
        use google_cloud_gax::polling_error_policy::PollingErrorPolicyExt;
        // Bring `RequestOptionsBuilder` into scope.
        use google_cloud_gax::options::RequestOptionsBuilder;
        use std::time::Duration;
        use google_cloud_lro::Poller;
    
        let client = StorageControl::builder().build().await?;
    
        // Create the request builder.
        let response = client
            .rename_folder()
            // Configure the polling error policy.
            .with_polling_error_policy(
                Aip194Strict
                    .with_attempt_limit(100)
                    .with_time_limit(Duration::from_secs(300)),
            )
            .set_name(format!("projects/_/buckets/{bucket}/folders/{folder}"))
            .set_destination_folder_id(dest)
            // Initialize the request.
            .poller()
            .until_done()
            .await?;
    
        println!("LRO completed, response={response:?}");
    
        Ok(())
    }
    

You might also consider adding a retry policy, in the event that the initial request to start the LRO fails:
    
    
        let client = StorageControl::builder()
            .with_retry_policy(
                retry_policy::Aip194Strict
                    .with_attempt_limit(100)
                    .with_time_limit(Duration::from_secs(300)),
            )
            .build()
            .await?;
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
