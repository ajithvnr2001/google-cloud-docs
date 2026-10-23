---
url: https://docs.cloud.google.com/rust/docs/long-running-operations/
title: Working with long-running operations \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:38.377673+00:00
---

# Working with long-running operations  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/long-running-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Working with long-running operations Stay organized with collections  Save and categorize content based on your preferences. 

Occasionally, an API might expose a method that takes a significant amount of time to complete. Instead of blocking while the task runs, you can return a promise and let the user check the status.

The Google Cloud Client Libraries for Rust provide helpers to work with these long-running operations (LROs). This guide shows you how to start LROs and wait for their completion.

## Prerequisites

This guide uses the Cloud Storage service to keep the code snippets concrete. These concepts apply to any other service that uses LROs.

Before following this guide, you should:

  * Create a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * Enable [billing](https://cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).



For complete setup instructions for the Rust libraries, see [Setting up your development environment](https://docs.cloud.google.com/rust/docs/quickstart).

## Dependencies

Declare Google Cloud dependencies in your `Cargo.toml` file:
    
    
    cargo add google-cloud-storage google-cloud-lro google-cloud-longrunning
    

You also need several `tokio` features:
    
    
    cargo add tokio --features full,macros
    

## Start a long-running operation

This example uses [rename folder](https://cloud.google.com/storage/docs/rename-hns-folders). This operation can take a long time for large folders, but it is relatively fast for smaller folders.

To start a long-running operation, you must initialize a client and make the RPC.

First, add `use` declarations to avoid long package names:
    
    
    use anyhow::anyhow;
    use google_cloud_longrunning as longrunning;
    use google_cloud_storage::client::StorageControl;

Next, create the client:
    
    
    let client = StorageControl::builder().build().await?;

In the Rust client libraries, each request is represented by a method that returns a request builder. Call the method on the client to create the request builder:
    
    
    let operation = client
        .rename_folder()
        .set_name(format!("projects/_/buckets/{bucket}/folders/{folder}"))
        .set_destination_folder_id(dest)

The sample functions accept the bucket and folder names as arguments:
    
    
    pub async fn manual(bucket: &str, folder: &str, dest: &str) -> anyhow::Result<()> {

Make the request and wait for an [Operation](https://docs.rs/google-cloud-longrunning/latest/google_cloud_longrunning/model/struct.Operation.html) to be returned. This `Operation` acts as a promise for the result of the long-running request:
    
    
        let operation =
            // ...
            .send()
            .await?;
    

This request starts the operation in the background. Wait until the operation completes to determine if it was successful.

## Automatically poll a long-running operation

To configure automatic polling, you will Start a long-running operation with a `Poller` rather than `.send().wait`, like so:
    
    
    .poller()
    .until_done()
    .await?;

First, introduce the `Poller` trait in scope using a `use` declaration:
    
    
    use google_cloud_lro::Poller;

Then initialize the client and prepare the request as before:
    
    
    let response = client
        .rename_folder()
        .set_name(format!("projects/_/buckets/{bucket}/folders/{folder}"))
        .set_destination_folder_id(dest)

Poll until the operation completes and print the result:
    
    
        .poller()
        .until_done()
        .await?;
    
    println!("LRO completed, response={response:?}");
    

## Poll a long-running operation with intermediate results

The `.until_done()` method is convenient, but it omits partial progress reports from long-running operations. If your application requires this information, use the poller directly:
    
    
        let mut poller = client
            .rename_folder()
            /* more stuff */
            .poller();
    

Then use the poller in a loop:
    
    
    while let Some(p) = poller.poll().await {
        match p {
            PollingResult::Completed(r) => {
                println!("LRO completed, response={r:?}");
            }
            PollingResult::InProgress(m) => {
                println!("LRO in progress, metadata={m:?}");
            }
            PollingResult::PollingError(e) => {
                println!("Transient error polling the LRO: {e}");
            }
        }
        tokio::time::sleep(std::time::Duration::from_millis(500)).await;
    }

This loop explicitly waits before polling again. The polling period depends on the specific operation and its payload. Consult the service documentation or experiment with your data to determine a good value.

## Manually poll a long-running operation

While we recommend automated polling approaches, it's also possible to manually poll a long-running operation. For more information, see the [Operation](https://docs.rs/google-cloud-longrunning/latest/google_cloud_longrunning/model/struct.Operation.html) message reference documentation.

Start the long-running operation using the client:
    
    
        let mut operation = client
            .rename_folder()
            /* more stuff */
            .send()
            .await?;
    

Start a polling loop, and check if the operation completed using the `done` field:
    
    
    let response: anyhow::Result<Folder> = loop {
        if operation.done {

When the operation completes, it usually contains a result. The result field is optional because the service could return `done` as true without a result. For example, a successful deletion operation has no return value. In this example, the Cloud Storage service always returns a value:
    
    
    match &operation.result {
        None => {
            break Err(anyhow!("missing result for finished operation"));
        }

A started operation might not complete successfully. The result can be an error or a valid response. Check for errors first:
    
    
    Some(r) => {
        break match r {
            longrunning::model::operation::Result::Error(s) => {
                Err(anyhow!("operation completed with error {s:?}"))
            }

The error type is a [Status](https://docs.rs/google-cloud-rpc/latest/google_cloud_rpc/model/struct.Status.html) message type. This does NOT implement the standard `Error` trait. Manually convert it to a valid error using [`Error::service`](https://docs.rs/google-cloud-gax/latest/google_cloud_gax/error/struct.Error.html).

If the result is successful, extract the response type. Find this type in the LRO method documentation or the service API documentation:
    
    
    longrunning::model::operation::Result::Response(any) => {
        let response = any.to_msg::<Folder>()?;
        Ok(response)
    }

Note that extraction of the value may fail if the type does not match what the service sent.

Google Cloud types might add fields and branches in the future. The Google Cloud Client Libraries for Rust mark all structs and enums as `#[non_exhaustive]`. Handle this case:
    
    
    _ => Err(anyhow!("unexpected result branch {r:?}")),

If the operation hasn't completed, it might contain metadata. Some services include initial information about the request, while other services include partial progress reports. You can extract and report this metadata:
    
    
    if let Some(any) = &operation.metadata {
        let metadata = any.to_msg::<RenameFolderMetadata>()?;
        println!("LRO in progress, metadata={metadata:?}");
    }

Wait before polling again. Consider adjusting the polling period using truncated [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff). This example polls every 500ms:
    
    
    tokio::time::sleep(std::time::Duration::from_millis(500)).await;

Query the operation status:
    
    
    if let Ok(attempt) = client
        .get_operation()
        .set_name(&operation.name)
        .send()
        .await
    {
        operation = attempt;
    }

For simplicity, this example ignores all errors. In your application, you can treat a subset of errors as non-recoverable and limit the number of polling attempts.

## What's next

  * View the source code for the examples on [GitHub](https://github.com/googleapis/google-cloud-rust/blob/main/guide/samples/tests/storage/lros.rs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
