---
url: https://docs.cloud.google.com/rust/docs/quickstart-storage/
title: Quickstart: Use Cloud Storage with Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:22.083907+00:00
---

# Quickstart: Use Cloud Storage with Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/quickstart-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Quickstart: Use Cloud Storage with Rust Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Storage is a managed service for storing unstructured data.

The Rust client library provides an idiomatic API to access this service. The client library resumes interrupted downloads and uploads, and automatically performs integrity checks on the data. For metadata operations, the client library can retry failed requests, and automatically poll long-running operations.

This guide shows you how to create a Cloud Storage bucket, upload an object to this bucket, and then read the object back.

Before you start this guide, create a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) with [billing enabled](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).

## Add the client library dependency
    
    
    cargo add google-cloud-storage
    

## Create a storage bucket

The client to perform operations on buckets and object metadata is called `StorageControl`.
    
    
        use google_cloud_storage::model::{Bucket, bucket::IamConfig, bucket::iam_config::UniformBucketLevelAccess};
        use google_cloud_storage::client::StorageControl;
        let control = StorageControl::builder().build().await?;
    

To create a bucket, you must provide your project name and the bucket ID.
    
    
        let bucket = control
            .create_bucket()
            .set_parent("projects/_")
            .set_bucket_id(bucket_id)
            .set_bucket(
                gcs::model::Bucket::new()
                    .set_project(format!("projects/{project_id}"))
            )
    

You can also provide other attributes for the bucket. For example, if you want all objects in the bucket to use the same permissions, you can enable [Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access).
    
    
        Bucket::new()
            .set_project(format!("projects/{project_id}"))
            .set_iam_config(
                IamConfig::new()
                    .set_uniform_bucket_level_access(
                        UniformBucketLevelAccess::new()
                            .set_enabled(true),
                ),
            ),
    

Then send this request and wait for the response.
    
    
            .send()
            .await?;
        println!("bucket successfully created {bucket:?}");
    

## Upload an object

The client to perform operations on object data is called Storage.
    
    
        use google_cloud_storage::client::Storage;
        let client = Storage::builder().build().await?;
    

In this case, you create an object called `hello.txt` with the greeting **Hello World!**.
    
    
        let object = client
            .upload_object(&bucket.name, "hello.txt", "Hello World!")
            .send_buffered()
            .await?;
        println!("object successfully uploaded {object:?}");
    

## Download an object

To download the contents of an object, use the `read_object()` method.
    
    
        let mut reader = client.read_object(&bucket.name, "hello.txt").send().await?;
        let mut contents = Vec::new();
        while let Some(chunk) = reader.next().await.transpose()? {
            contents.extend_from_slice(&chunk);
        }
        println!(
            "object contents successfully downloaded {:?}",
            bytes::Bytes::from_owner(contents)
        );
    

## Clean up resources

Finally, remove the object and bucket to clean up the resources used in this guide.
    
    
        control
            .delete_object()
            .set_bucket(&bucket.name)
            .set_object(&object.name)
            .set_generation(object.generation)
            .send()
            .await?;
        control
            .delete_bucket()
            .set_name(&bucket.name)
            .send()
            .await?;
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
