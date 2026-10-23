---
url: https://docs.cloud.google.com/rust/docs/update-field-mask/
title: Update a resource using a field mask \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:23.630034+00:00
---

# Update a resource using a field mask  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/update-field-mask/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Update a resource using a field mask Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to selectively update resources using field masks. When updating a resource in Google Cloud, you might want to modify only specific fields rather than replacing the entire resource. The Rust client libraries support field masks, letting you precisely control which fields of a resource are updated while leaving other fields unchanged.

## Prerequisites

This guide uses the Secret Manager API, but the concepts apply to other Google Cloud resources and services.

Before continuing, follow [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart) to enable and authenticate the Secret Manager API.

For complete setup instructions for the Rust libraries, see [Setting up your development environment](https://docs.cloud.google.com/rust/docs/quickstart).

## Dependencies

After enabling Secret Manager, declare your dependencies in your `Cargo.toml` file:
    
    
    cargo add google-cloud-secretmanager-v1
    cargo add tokio
    

## Install well-known types

The `google_cloud_wkt` crate contains well-known types for Google Cloud APIs. These types typically have custom JSON encoding and might provide conversion functions to and from commonly used Rust types. The `google_cloud_wkt` crate contains the field mask type, `FieldMask`.

Add the crate as a dependency:
    
    
    cargo add google-cloud-wkt
    

## Field masks

A `FieldMask` represents a set of symbolic field paths. Field masks specify a subset of fields that an update operation modifies or a get operation returns.

In an update operation, a field mask specifies which fields of the targeted resource to update. The API changes only the values of the fields specified in the mask and leaves the others untouched. If you pass a resource to describe the updated values, the API ignores the values of all fields not covered by the mask. If you don't provide a field mask on update, the operation applies to all fields.

To reset a field to the default value, include the field in the mask and set the default value in the provided resource. To reset all fields of a resource, provide a default instance of the resource and set all fields in the mask, or don't provide a mask.

## Update fields on a resource

First, initialize a Secret Manager client and create a secret:
    
    
        let client = SecretManagerService::builder().build().await?;
    
        let secret = client
            .create_secret()
            .set_parent(format!("projects/{project_id}"))
            .set_secret_id("your-secret")
            .set_secret(
                Secret::new().set_replication(Replication::new().set_automatic(Automatic::new())),
            )
            .send()
            .await?;
        println!("CREATE = {secret:?}");
    

The output from the create operation shows that both the `labels` and `annotations` fields are empty.

The following code updates the `labels` and `annotations` fields:
    
    
        let tag = |mut labels: HashMap<_, _>, msg: &str| {
            labels.insert("updated".to_string(), msg.to_string());
            labels
        };
    
        let update = client
            .update_secret()
            .set_secret(
                Secret::new()
                    .set_name(&secret.name)
                    .set_etag(secret.etag)
                    .set_labels(tag(secret.labels, "your-label"))
                    .set_annotations(tag(secret.annotations, "your-annotations")),
            )
            .set_update_mask(FieldMask::default().set_paths(["annotations", "labels"]))
            .send()
            .await?;
        println!("UPDATE = {update:?}");
    

The `set_etag` method lets you set an etag on the secret, which prevents overwriting concurrent updates.

Having set labels and annotations on the updated secret, you pass a field mask to `set_update_mask` to specify the field paths to update:
    
    
            .set_update_mask(FieldMask::default().set_paths(["annotations", "labels"]))
    

The output from the update operation shows that the fields are updated:
    
    
    labels: {"updated": "your-label"},
    ...
    annotations: {"updated": "your-annotations"},
    

### Update a field: complete code

This sample code initializes and creates a secret and then applies a field mask:
    
    
    use google_cloud_secretmanager_v1::client::SecretManagerService;
    use google_cloud_secretmanager_v1::model::replication::Automatic;
    use google_cloud_secretmanager_v1::model::{Replication, Secret};
    use google_cloud_wkt::FieldMask;
    use std::collections::HashMap;
    
    pub async fn sample(project_id: &str) -> anyhow::Result<()> {
        let client = SecretManagerService::builder().build().await?;
    
        let secret = client
            .create_secret()
            .set_parent(format!("projects/{project_id}"))
            .set_secret_id("your-secret")
            .set_secret(
                Secret::new().set_replication(Replication::new().set_automatic(Automatic::new())),
            )
            .send()
            .await?;
        println!("CREATE = {secret:?}");
    
        let tag = |mut labels: HashMap<_, _>, msg: &str| {
            labels.insert("updated".to_string(), msg.to_string());
            labels
        };
    
        let update = client
            .update_secret()
            .set_secret(
                Secret::new()
                    .set_name(&secret.name)
                    .set_etag(secret.etag)
                    .set_labels(tag(secret.labels, "your-label"))
                    .set_annotations(tag(secret.annotations, "your-annotations")),
            )
            .set_update_mask(FieldMask::default().set_paths(["annotations", "labels"]))
            .send()
            .await?;
        println!("UPDATE = {update:?}");
    
        Ok(())
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
