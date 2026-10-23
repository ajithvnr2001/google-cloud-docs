---
url: https://docs.cloud.google.com/rust/docs/error-handling/
title: Error handling \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:23.370712+00:00
---

# Error handling  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/error-handling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Error handling Stay organized with collections  Save and categorize content based on your preferences. 

Deliver a more consistent user experience by proactively interpreting and responding to errors. Whether you're developing automated cloud workflows or interacting with remote APIs, the Rust client libraries provide ways to gracefully handle errors. This guide explains how to:

  * **Handle errors:** Inspect error types and branch your application logic based on service status codes, such as creating a missing resource when encountering a `NotFound` error.
  * **Examine error details:** Extract and examine rich error details—such as bad request field violations or quota failures—returned by Google Cloud services to troubleshoot API issues and dynamically adjust runtime behavior.
  * **Resolve binding errors:** Interpret and resolve client-side HTTP binding errors caused by invalid or missing request fields to ensure your requests reach the service smoothly.

**Note:** In distributed systems, one of the most common reasons for error handling is to retry requests that fail due to transient errors. The Rust client libraries include a policy-based retry loop. For more information, see [Configuring retry policies](https://docs.cloud.google.com/rust/docs/configure-retry-policies).

## Prerequisites

This guide uses the [Secret Manager service](https://docs.cloud.google.com/secret-manager/docs/overview) and the [Cloud Natural Language API](https://docs.cloud.google.com/natural-language/docs/setup) to demonstrate error handling. To run the examples, first:

  1. Enable the [Secret Manager service](https://docs.cloud.google.com/secret-manager/docs/overview).
  2. Enable the [Cloud Natural Language API](https://docs.cloud.google.com/natural-language/docs/setup).
  3. Set up [authentication](https://docs.cloud.google.com/docs/authentication).



## Dependencies

Use the following command to add the required dependencies to your `Cargo.toml` file:
    
    
    cargo add google-cloud-secretmanager-v1 google-cloud-gax crc32c google-cloud-language-v2
    

## Handle errors

The Rust client libraries let you surface and react to errors. You might, for example, use error discovery to branch behavior: a common pattern in cloud services is to use a resource as if the container for it existed, only creating the container if you encounter an error. If the container usually exists, this approach is more efficient than checking whether the container exists before making the request.

The following example demonstrates how to handle a missing resource by catching the error when attempting to update a Secret Manager secret—and creating it if it doesn't already exist.

  1. Make an attempt to create a new secret version: 
         
         match update_attempt(&client, project_id, secret_id, data.clone()).await {

  2. If `update_attempt` succeeds, print the successful result and return: 
         
         Ok(version) => {
             println!("new version is {}", version.name);
             Ok(version)
         }

  3. If `update_attempt` fails, you must disambiguate the cause of the failure. The request might have failed for many reasons, such as a dropped connection or error with authentication tokens. Retry policies can deal with most of these errors. Look for errors returned by the service: 
         
         Err(e) => {
             if let Some(status) = e.downcast_ref::<Error>().and_then(|e| e.status()) {

  4. Look for an error that corresponds with a missing secret: 
         
         if status.code == Code::NotFound {

  5. If you have encountered a "not found" error (`Code::NotFound`), try to create the secret: 
         
         let _ = create_secret(&client, project_id, secret_id).await?;

  6. Try to add the secret version again. This time, return an error if anything fails: 
         
         let version = update_attempt(&client, project_id, secret_id, data).await?;
         println!("new version is {}", version.name);
         return Ok(version);




### Code sample: main function (`sample`)

The complete code for this example is broken into three parts: the main orchestration function (`sample`), followed by its two helper methods (`update_attempt` and `create_secret`).

The `sample` function attempts to add a new version to a secret. It catches the error returned by the client and checks if the error is a `Code::NotFound` error. If the secret is not found, the function creates the initially missing secret and retries the update.
    
    
    use google_cloud_gax::error::Error;
    use google_cloud_gax::error::rpc::Code;
    use google_cloud_secretmanager_v1::client::SecretManagerService;
    use google_cloud_secretmanager_v1::model::SecretVersion;
    
    pub async fn sample(
        project_id: &str,
        secret_id: &str,
        data: Vec<u8>,
    ) -> anyhow::Result<SecretVersion> {
        let client = SecretManagerService::builder().build().await?;
    
        match update_attempt(&client, project_id, secret_id, data.clone()).await {
            Ok(version) => {
                println!("new version is {}", version.name);
                Ok(version)
            }
            Err(e) => {
                if let Some(status) = e.downcast_ref::<Error>().and_then(|e| e.status()) {
                    if status.code == Code::NotFound {
                        let _ = create_secret(&client, project_id, secret_id).await?;
                        let version = update_attempt(&client, project_id, secret_id, data).await?;
                        println!("new version is {}", version.name);
                        return Ok(version);
                    }
                }
                Err(e)
            }
        }
    }

#### Code sample: helper method (`update_attempt`)

The helper method `update_attempt` tries to add a secret version, calculating the CRC32c checksum of the payload data:
    
    
    use google_cloud_secretmanager_v1::client::SecretManagerService;
    use google_cloud_secretmanager_v1::model::{SecretPayload, SecretVersion};
    
    pub(crate) async fn update_attempt(
        client: &SecretManagerService,
        project_id: &str,
        secret_id: &str,
        data: Vec<u8>,
    ) -> anyhow::Result<SecretVersion> {
        let checksum = crc32c::crc32c(&data) as i64;
        let version = client
            .add_secret_version()
            .set_parent(format!("projects/{project_id}/secrets/{secret_id}"))
            .set_payload(
                SecretPayload::new()
                    .set_data(data)
                    .set_data_crc32c(checksum),
            )
            .send()
            .await?;
        Ok(version)
    }

#### Code sample: helper method (`create_secret`)

The helper method `create_secret` creates a missing secret and configures a customized retry policy:
    
    
    use google_cloud_gax::options::RequestOptionsBuilder;
    use google_cloud_gax::retry_policy::AlwaysRetry;
    use google_cloud_gax::retry_policy::RetryPolicyExt;
    use google_cloud_secretmanager_v1::client::SecretManagerService;
    use google_cloud_secretmanager_v1::model::{Replication, Secret, replication};
    use std::time::Duration;
    
    pub async fn create_secret(
        client: &SecretManagerService,
        project_id: &str,
        secret_id: &str,
    ) -> anyhow::Result<Secret> {
        let secret = client
            .create_secret()
            .set_parent(format!("projects/{project_id}"))
            .with_retry_policy(
                AlwaysRetry
                    .with_attempt_limit(5)
                    .with_time_limit(Duration::from_secs(60)),
            )
            .set_secret_id(secret_id)
            .set_secret(
                Secret::new()
                    .set_replication(Replication::new().set_replication(
                        replication::Replication::Automatic(replication::Automatic::new().into()),
                    ))
                    .set_labels([("integration-test", "true")]),
            )
            .send()
            .await?;
        Ok(secret)
    }

## Examine error details

Some Google Cloud services include additional error details when requests fail. To help with troubleshooting, the Rust client libraries include these details when formatting errors using `std::fmt::Display`. You can examine these details and change your application behavior accordingly.

Only errors returned by the service contain detailed information. The client libraries return a [`StatusDetails`](https://docs.rs/google-cloud-gax/latest/google_cloud_gax/error/rpc/enum.StatusDetails.html) enum with the different types of error details.

### Extract error details

This example intentionally sends a bad request to the [Cloud Natural Language API](https://docs.cloud.google.com/natural-language/docs/setup) and examines the resulting error.

  1. Create a client: 
         
         let client = LanguageService::builder().build().await?;

  2. Send a request (in this example, a key field is missing): 
         
         let result = client
             .analyze_sentiment()
             .set_document(
                 Document::new()
                     // Missing document contents
                     // .set_content("Hello World!")
                     .set_type(Type::PlainText),
             )
             .send()
             .await;

  3. Extract the error from the result using standard Rust functions. The error type prints all the error details in human-readable form: 
         
         let err = result.expect_err("the request should have failed");
         println!("\nrequest failed with error {err:#?}");




The output is similar to the following:
    
    
    request failed with error Error {
        kind: Service {
            status_code: Some(
                400,
            ),
            headers: Some(
                {
                    "vary": "X-Origin",
                    "vary": "Referer",
                    "vary": "Origin,Accept-Encoding",
                    "content-type": "application/json; charset=UTF-8",
                    "date": "Sat, 24 May 2025 17:19:49 GMT",
                    "server": "scaffolding on HTTPServer2",
                    "x-xss-protection": "0",
                    "x-frame-options": "SAMEORIGIN",
                    "x-content-type-options": "nosniff",
                    "alt-svc": "h3=\":443\"; ma=2592000,h3-29=\":443\"; ma=2592000",
                    "accept-ranges": "none",
                    "transfer-encoding": "chunked",
                },
            ),
            status: Status {
                code: InvalidArgument,
                message: "One of content, or gcs_content_uri must be set.",
                details: [
                    BadRequest(
                        BadRequest {
                            field_violations: [
                                FieldViolation {
                                    field: "document.content",
                                    description: "Must have some text content to annotate.",
                                    reason: "",
                                    localized_message: None,
                                    _unknown_fields: {},
                                },
                            ],
                            _unknown_fields: {},
                        },
                    ),
                ],
            },
        },
    }
    

### Programmatically examine error details

Sometimes you might need to examine the error details programmatically. This example traverses the data structure and prints the most relevant fields.

Only errors returned by the service contain detailed information, so first query the error to see if it contains the correct error type. If it does, you can break down some top-level information about the error:
    
    
    if let Some(status) = err.status() {
        println!(
            "  status.code={}, status.message={}",
            status.code, status.message,
        );

Iterate over the details:
    
    
    for detail in status.details.iter() {
        match detail {

As mentioned earlier, the client libraries return a [`StatusDetails`](https://docs.rs/google-cloud-gax/latest/google_cloud_gax/error/rpc/enum.StatusDetails.html) enum with the different types of error details. This example only examines `BadRequest` errors:
    
    
    StatusDetails::BadRequest(bad) => {

A `BadRequest` contains a list of fields that are in violation. You can iterate and print the details for each:
    
    
    for f in bad.field_violations.iter() {
        println!(
            "  the request field {} has a problem: \"{}\"",
            f.field, f.description
        );
    }

Such information can be useful during development. Other branches of `StatusDetails`, such as [`QuotaFailure`](https://docs.rs/google-cloud-gax/latest/google_cloud_gax/error/rpc/enum.StatusDetails.html#variant.QuotaFailure), might be useful at runtime to throttle an application.

### Expected output

The output from the error details is similar to the following:
    
    
      status.code=400, status.message=One of content, or gcs_content_uri must be set., status.status=Some("INVALID_ARGUMENT")
      the request field document.content has a problem: "Must have some text content to annotate."
    

### Code sample: Examine error details

The `sample` function sends an intentionally invalid request to the Cloud Natural Language API to generate a service error. It then catches the error and programmatically extracts the `StatusDetails` to inspect and print specific `BadRequest` field violations.
    
    
    use google_cloud_gax::error::rpc::StatusDetails;
    use google_cloud_language_v2::client::LanguageService;
    use google_cloud_language_v2::model::Document;
    use google_cloud_language_v2::model::document::Type;
    
    pub async fn sample() -> anyhow::Result<()> {
        let client = LanguageService::builder().build().await?;
    
        let result = client
            .analyze_sentiment()
            .set_document(
                Document::new()
                    // Missing document contents
                    // .set_content("Hello World!")
                    .set_type(Type::PlainText),
            )
            .send()
            .await;
    
        let err = result.expect_err("the request should have failed");
        println!("\nrequest failed with error {err:#?}");
    
        if let Some(status) = err.status() {
            println!(
                "  status.code={}, status.message={}",
                status.code, status.message,
            );
            for detail in status.details.iter() {
                match detail {
                    StatusDetails::BadRequest(bad) => {
                        for f in bad.field_violations.iter() {
                            println!(
                                "  the request field {} has a problem: \"{}\"",
                                f.field, f.description
                            );
                        }
                    }
                    _ => {
                        println!("  additional error details: {detail:?}");
                    }
                }
            }
        }
    
        Ok(())
    }

## Resolve binding errors

When using HTTP to send requests to Google Cloud services, the request uses a Uniform Resource Identifier (URI) to specify a resource. Some RPCs correspond to multiple URIs, and the content of the request determines which URI is used.

The client library considers all possible URIs and only returns a binding error if no URIs work. Typically, this happens when a field is either missing or in an invalid format.

If your request fails to provide fields containing a valid format for any possible URI, you might encounter a binding error:
    
    
    Error: cannot find a matching binding to send the request: at least one of the
    conditions must be met: (1) field `name` needs to be set and match the template:
    'projects/*/secrets/*' OR (2) field `name` needs to be set and match the
    template: 'projects/*/locations/*/secrets/*'
    

The preceding example error occurred because the example tries to retrieve the details of a resource without providing its name. Specifically, the `name` field on a [`GetSecretRequest`](https://docs.rs/google-cloud-secretmanager-v1/latest/google_cloud_secretmanager_v1/model/struct.GetSecretRequest.html) is required, but not set by the example:
    
    
    let secret = client
        .get_secret()
        //.set_name("projects/my-project/secrets/my-secret")
        .send()
        .await;

### How to fix binding errors

To fix the error, set the required field so that it matches one of the templates shown in the error message:

  * `'projects/*/secrets/*'`
  * `'projects/*/locations/*/secrets/*'`



Either template allows the client library to make a request to the server. For example, the following code matches the first template:
    
    
    let secret = client
        .get_secret()
        .set_name("projects/my-project/secrets/my-secret")
        .send()
        .await;

Alternatively, the following code matches the second template:
    
    
    let secret = client
        .get_secret()
        .set_name("projects/my-project/locations/us-central1/secrets/my-secret")
        .send()
        .await;

### Interpreting templates

The error message for a binding error includes template strings showing possible values for the request fields. Most template strings include `*` and `**` as wildcards to match the field values.

#### Single wildcard

The `*` wildcard alone means a non-empty string without a `/`. It can be thought of as the regular expression `[^/]+`.

Here are some examples:

Template | Input | Match?  
---|---|---  
`*` | `simple-string-123` | `true`  
`projects/*` | `projects/p` | `true`  
`projects/*/locations` | `projects/p/locations` | `true`  
`projects/*/locations/*` | `projects/p/locations/l` | `true`  
`*` | `""` (empty) | `false`  
`*` | `string/with/slashes` | `false`  
`projects/*` | `projects/` (empty) | `false`  
`projects/*` | `projects/p/` (extra slash) | `false`  
`projects/*` | `projects/p/locations/l` | `false`  
`projects/*/locations` | `projects/p` | `false`  
`projects/*/locations` | `projects/p/locations/l` | `false`  
  
#### Double wildcard

Less common is the `**` wildcard, which means any string. The string can be empty or contain any number of slashes (`/`). It can be thought of as the regular expression `.*`.

When a template ends in `/**`, the initial slash is optional.

Template | Input | Match?  
---|---|---  
`**` | `""` | `true`  
`**` | `simple-string-123` | `true`  
`**` | `string/with/slashes` | `true`  
`projects/*/**` | `projects/p` | `true`  
`projects/*/**` | `projects/p/locations` | `true`  
`projects/*/**` | `projects/p/locations/l` | `true`  
`projects/*/**` | `locations/l` | `false`  
`projects/*/**` | `projects//locations/l` | `false`  
  
### Inspect binding errors

If you need to inspect the error programmatically, check whether it is a binding error and downcast it to a `BindingError`:
    
    
    let secret = client
        .get_secret()
        //.set_name("projects/my-project/secrets/my-secret")
        .send()
        .await;
    
    let e = secret.unwrap_err();
    assert!(e.is_binding(), "{e:?}");
    assert!(e.source().is_some(), "{e:?}");
    let _ = e
        .source()
        .and_then(|e| e.downcast_ref::<BindingError>())
        .expect("should be a BindingError");

## What's next

  * Learn about [Configuring retry policies](https://docs.cloud.google.com/rust/docs/configure-retry-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
