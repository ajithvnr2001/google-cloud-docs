---
url: https://docs.cloud.google.com/rust/docs/pagination/
title: Working with list operations \u00a0|\u00a0 Rust \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:54.088196+00:00
---

# Working with list operations  |  Rust  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/pagination/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Working with list operations Stay organized with collections  Save and categorize content based on your preferences. 

Some services return potentially large lists of items, such as rows or resource descriptions. To keep CPU and memory usage under control, services return these resources in `pages`: smaller subsets of the items with a continuation token to request the next subset.

Iterating over items by page can be tedious. The client libraries provide adapters to convert the pages into asynchronous iterators. This guide shows you how to work with these adapters.

## Prerequisites

This guide uses the Secret Manager service to demonstrate list operations. The concepts included in this guide also apply to other services.

To follow this guide, you'll need to to have enabled the Secret Manager service, logged in, and ensured that your account has the necessary permissions. For guidance on how to fulfill these prerequisites, follow the service [quickstart](https://cloud.google.com/secret-manager/docs/quickstart).

For complete setup instructions for the Rust libraries, see [Setting up your development environment](https://docs.cloud.google.com/rust/quickstart).

## Dependencies

Add the Secret Manager library to your `Cargo.toml` file:
    
    
    cargo add google-cloud-secretmanager-v1
    

## Iterating list methods

To help iterate the items in a list method, the APIs return an implementation of the `ItemPaginator` trait. Introduce the trait into scope using a `use` declaration:
    
    
    use google_cloud_gax::paginator::ItemPaginator as _;

To iterate over the items, use the `by_item` method.
    
    
    let mut list = client
        .list_secrets()
        .set_parent(format!("projects/{project_id}"))
        .by_item();
    while let Some(secret) = list.next().await {
        let secret = secret?;
        println!("  secret={}", secret.name)
    }

In rare cases, pages might contain extra information that you need access to, or you may need to checkpoint your progress across processes. If needed, you can iterate over full pages instead of individual items.

  1. Introduce `Paginator` into scope using a `use` declaration: 
         
         use google_cloud_gax::paginator::Paginator as _;

  2. Iterate over the pages using `by_page`: 
         
         let mut list = client
             .list_secrets()
             .set_parent(format!("projects/{project_id}"))
             .by_page();
         while let Some(page) = list.next().await {
             let page = page?;
             println!("  next_page_token={}", page.next_page_token);
             page.secrets
                 .into_iter()
                 .for_each(|secret| println!("    secret={}", secret.name));
         }




### Working with `futures::Stream`

You may want to use these APIs in the larger Rust ecosystem of asynchronous streams, such as `tokio::Stream`. This can be achieved as follows:

  1. Enable the `unstable-streams` feature in the `google_cloud_gax` crate. The name of this feature serves as notice that these APIs are unstable. You should only use them if you are prepared to deal with any breaks that result from incompatible changes to the [`futures::Stream`](https://docs.rs/futures/latest/futures/stream/) trait.
         
         cargo add google-cloud-gax --features unstable-stream
         

  2. The following examples also use the `futures::stream::StreamExt` trait, which you enable by adding the `futures` crate.
         
         cargo add futures
         

  3. Add the required `use` declarations: 
         
         use futures::stream::StreamExt;
         use google_cloud_gax::paginator::ItemPaginator as _;

  4. Use the `into_stream` function to convert `ItemPaginator` into a `futures::Stream`. 
         
         let list = client
             .list_secrets()
             .set_parent(format!("projects/{project_id}"))
             .by_item()
             .into_stream();
         list.map(|secret| -> gax::Result<()> {
             println!("  secret={}", secret?.name);
             Ok(())
         })
         .fold(Ok(()), async |acc, result| -> gax::Result<()> {
             acc.and(result)
         })
         .await?;




Similarly, you can use the `into_stream` function to convert `Paginator` into a `futures::Stream`.
    
    
    let list = client
        .list_secrets()
        .set_parent(format!("projects/{project_id}"))
        .by_page()
        .into_stream();
    list.enumerate()
        .map(|(index, page)| -> gax::Result<()> {
            println!("page={}, next_page_token={}", index, page?.next_page_token);
            Ok(())
        })
        .fold(Ok(()), async |acc, result| -> gax::Result<()> {
            acc.and(result)
        })
        .await?;

## Resuming list methods by setting next page token

In some cases, such as an interrupted list operation, you can set the next page token to resume paginating from a specific page.
    
    
    let page = client
        .list_secrets()
        .set_parent(format!("projects/{project_id}"))
        .send()
        .await;
    let page = page?;
    let mut next_page_token = page.next_page_token.clone();
    page.secrets
        .into_iter()
        .for_each(|secret| println!("    secret={}", secret.name));
    
    while !next_page_token.is_empty() {
        println!("  next_page_token={next_page_token}");
    
        let page = client
            .list_secrets()
            .set_parent(format!("projects/{project_id}"))
            .set_page_token(next_page_token)
            .send()
            .await;
        let page = page?;
        next_page_token = page.next_page_token.clone();
    
        page.secrets
            .into_iter()
            .for_each(|secret| println!("    secret={}", secret.name));
    }

## When to use the paginator helpers

The Google Cloud Client Libraries for Rust provide an adapter to convert the list RPCs as defined by [AIP-4233](https://google.aip.dev/client-libraries/4233) into types implementing `ItemPaginator` and `Paginator` if the [Google API List](https://google.aip.dev/132) method follows the pagination guideline defined by [AIP-158](https://google.aip.dev/158). In brief, this guideline requires that each call to a `List` method returns a page of resource items (for example, secrets) along with a token that you can pass to the `List` method to retrieve the next page.

Most Google Cloud services follow these guidelines. In the cases in which they don't, you must implement your own adapter to iterate over the results.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
