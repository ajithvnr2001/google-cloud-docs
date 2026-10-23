---
url: https://docs.cloud.google.com/run/docs/functions-with-run/
title: When should I deploy a function to Cloud Run? \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:51.362508+00:00
---

# When should I deploy a function to Cloud Run?  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/functions-with-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  When should I deploy a function to Cloud Run? Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Cloud Functions has been renamed to Cloud Run functions. For more information, see the [Cloud Run functions blog post](https://cloud.google.com/blog/products/serverless/google-cloud-functions-is-now-cloud-run-functions).

Cloud Run functions let you build event-driven services, lightweight APIs, and background processing tasks on fully managed infrastructure. Google manages runtime configuration and OS patching, automatically scaling resources to match incoming traffic or events.

Deploying a function, source code, or container image to Cloud Run provides all benefits described in the [Container runtime contract](https://docs.cloud.google.com/run/docs/container-contract).

## Use cases for deploying functions

You can directly deploy a function bound to events in order to implement asynchronous workloads (such as lightweight [ETL](https://cloud.google.com/learn/what-is-etl)) or cloud automations (such as triggering application builds). In addition, the automatic provisioning of an HTTPS endpoint makes functions a perfect candidate for webhooks.

See the following table for additional common use cases for deploying a function to Cloud Run:

Use case | Description  
---|---  
Streaming data processing / ETL |  Listen and respond to [Cloud Storage](https://cloud.google.com/storage) events such as when a file is created, changed, or removed. Process images, perform video transcoding, validate and transform data, and invoke any service on the internet from Cloud Run.   
Webhooks |  Using an [HTTP trigger](https://docs.cloud.google.com/run/docs/triggering/https-request), respond to events originating from 3rd party systems like GitHub, Slack, Stripe, or from anywhere that can send HTTP requests.   
Mobile backend | Use Google's mobile platform for app developers, [Firebase](https://firebase.google.com/docs/functions/), and write your mobile backend in Cloud Run functions. Listen and respond to events from Firebase Analytics, Realtime Database, Authentication, and Storage.   
IoT |  Imagine tens or hundreds of thousands of devices streaming data into Pub/Sub, thereby launching Cloud Run functions to process, transform and store data. Cloud Run lets you do it in a way that's completely serverless.   
AI/ML |  Create a scalable image processing service with the [Cloud Vision API](https://docs.cloud.google.com/vision-ai/docs/model-event-notification), or post process output data from a [Vertex AI custom-trained model](https://docs.cloud.google.com/architecture/ai-ml/image-processing-cloud-functions).   
  
## Connect and extend cloud services

Cloud Run functions provides a connective layer of logic that lets you write code to connect and extend cloud services. Listen and respond to a file upload to Cloud Storage, a log change, or an incoming message on a Pub/Sub topic. Cloud Run functions augments existing cloud services and lets you address an increasing number of use cases with arbitrary programming logic. Cloud Run functions have access to the Google Service Account credential and are thus seamlessly authenticated with the majority of Google Cloud services, including Cloud Vision, as well as many others. In addition, Cloud Run functions are supported by numerous [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries), which further simplify these integrations.

## What's next

  * Try the [getting started guide for deploying a function](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console).
  * If you have existing functions and need to use the `gcloud functions deploy` command, the Cloud Functions v2 API, or the `google_cloudfunctions2_function` Terraform configuration for backward compatibility, you can [deploy functions with the `gcloud functions` command](https://docs.cloud.google.com/functions/docs/deploy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
