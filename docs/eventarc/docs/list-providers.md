---
url: https://docs.cloud.google.com/eventarc/docs/list-providers/
title: List event providers \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:11.859385+00:00
---

# List event providers  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/list-providers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  List event providers Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

**Preview — Third-party events in Eventarc**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

An Eventarc _provider_ is a service or entity that can emit events directly to Google Cloud which are then routed to your project.

First-party providers are Google Cloud sources; for example, Cloud Storage. Third-party providers are non-Google Cloud entities that offer an Eventarc source.

You can list all providers and retrieve their details, including supported event types, by running `gcloud` commands along with required and optional flags.

## Prerequisites

Before running the `gcloud` commands, ensure that you have done the following:

  1. Set your Google Cloud project ID:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with your Google Cloud project ID.

You can find your project ID on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console.

  2. Enable the Eventarc API:
         
         gcloud services enable eventarc.googleapis.com
         




## List all providers in a specific location

To list all providers in a specific location:
    
    
    gcloud eventarc providers list \
        --location=LOCATION
    

Replace `LOCATION` with a supported Eventarc [region](https://docs.cloud.google.com/eventarc/docs/locations).

For example: `gcloud eventarc providers list --location=us-central1`

The output is similar to the following:
    
    
    NAME                       LOCATION
    bigquery.googleapis.com    us-central1
    cloudbuild.googleapis.com  us-central1
    storage.googleapis.com     us-central1
    workflows.googleapis.com   us-central1
    [...]
    

**Note:** If you run into a `Location is not found` error, confirm the supported Eventarc locations by running `gcloud eventarc locations list`.

## List all providers in any location

To list all providers in any location:
    
    
    gcloud eventarc providers list
    

The output is similar to the following:
    
    
    NAME                       LOCATION
    workflows.googleapis.com   asia-northeast3
    pubsub.googleapis.com      europe-west3
    storage.googleapis.com     nam4
    bigquery.googleapis.com    us-central1
    cloudbuild.googleapis.com  us-central1
    storage.googleapis.com     us-central1
    workflows.googleapis.com   us-central1
    storage.googleapis.com     us-east1
    [...]
    

## List a specific provider in any location

To list a specific provider in any location:
    
    
    gcloud eventarc providers list \
        --name=PROVIDER
    

Replace `PROVIDER` with the name of the provider.

For example: `gcloud eventarc providers list --name=storage.googleapis.com`

The output is similar to the following:
    
    
    NAME                    LOCATION
    storage.googleapis.com  nam4
    storage.googleapis.com  us-central1
    storage.googleapis.com  us-east1
    

## List all third-party providers in any location

To list all third-party providers in any location:
    
    
    gcloud eventarc providers list --filter='eventTypes.type!~^google*'
    

The output is a list of all third-party providers.

## Describe a specific provider and its supported event types

To describe a specific provider and its supported event types:
    
    
      gcloud eventarc providers describe PROVIDER \
          --location=LOCATION
    

Replace the following:

  * `PROVIDER`: the name of a specific provider.
  * `LOCATION`: a supported Eventarc [region](https://docs.cloud.google.com/eventarc/docs/locations).



For example: `gcloud eventarc providers describe storage.googleapis.com --location=us-central1`

The output is similar to the following:
    
    
    displayName: Cloud Storage
    eventTypes:
    - description: 'The live version of an object has become a noncurrent version, either
        because it was explicitly made noncurrent or because it was replaced by the upload
        of an object of the same name. Only sent when a bucket has enabled object versioning. '
      filteringAttributes:
      - attribute: bucket
        description: The bucket name being watched.
        required: true
      - attribute: type
        required: true
      type: google.cloud.storage.object.v1.archived
    [...]
    

Make note of the event type to use when creating an Eventarc trigger.

**Note:** If you run into a `Resource was not found` error, the provider might not be available in the specified location. To verify the location, run `gcloud eventarc providers list --location=- --name=PROVIDER`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
