---
url: https://docs.cloud.google.com/translate/docs/migrate-to-v3/
title: Migrate to Advanced from Basic \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:39:50.236868+00:00
---

# Migrate to Advanced from Basic  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/migrate-to-v3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate to Advanced from Basic

Existing Cloud Translation - Basic (v2) users who want to use the latest Cloud Translation features, such as glossaries and AutoML models, must migrate their applications to use Cloud Translation - Advanced (v3). For a comparison, see [Compare Basic and Advanced](https://docs.cloud.google.com/translate/docs/editions).

Migrating to the Advanced edition includes using Identity and Access Management (IAM) and the Advanced edition client libraries. The following sections outline migration tasks and the key differences between the two editions.

## Migrating to Advanced

The following steps outline the actions required to update your existing applications from using Cloud Translation - Basic to Cloud Translation - Advanced.

  1. Take inventory of your Google Cloud projects, applications, and users that access the Cloud Translation - Basic API. You will need to provide service accounts and update them to use the Cloud Translation - Advanced client libraries.
  2. Set up service accounts and authentication for your application.
  3. Use IAM roles to set permissions on service accounts.
  4. Enable Cloud Translation - Advanced for your project. If you use AutoML models with the Cloud Translation - Advanced, you must enable AutoML as well. For more information, see the [Setup](https://docs.cloud.google.com/translate/docs/setup) guide
  5. Use the Cloud Translation - Advanced client libraries and methods. For Cloud Translation - Advanced requests, you must include your project number (or project ID), and project location, such as `global` or `us-central1`.
  6. Check that the size of your translation requests to Cloud Translation - Advanced do not exceed the limit.
  7. Plan your translation request quota monitoring. Both versions of the API share the same daily and monthly [quotas](https://docs.cloud.google.com/translate/quotas).
  8. Review any potential changes in [billing](https://cloud.google.com/translate/pricing).



## Key differences between Advanced and Basic

To help you understand your migration tasks, the following sections describe key differences between the Advanced and Basic editions.

### Service accounts

For Cloud Translation - Basic, you can send authenticated requests by using API keys or service accounts.

Cloud Translation - Advanced has features that require customer-managed resources; these resources require IAM role and permissions management. Because of this, you cannot use API keys to authenticate to the service. Instead, you must use service accounts when authenticating to Cloud Translation - Advanced.

For more information, see the [setup](https://docs.cloud.google.com/translate/docs/setup) guide.

### IAM roles

When you use service accounts for Cloud Translation - Basic, the service accounts are used for authentication only. You can make any calls to Cloud Translation - Basic no matter what permissions are associated with the service account. However, for Cloud Translation - Advanced, the permissions do apply.

To grant service accounts permissions to call Cloud Translation - Advanced, you assign IAM roles to them. Cloud Translation - Advanced has several IAM roles that you can assign to your service account to access specific resources in your project. For example, if you want to use your service account to translate text, you assign the `roles/cloudtranslate.user` role to it. For more information, see IAM roles in [Cloud Translation - Advanced details](https://docs.cloud.google.com/translate/docs/intro-to-v3#iam).

If you plan to use AutoML models or any features that rely on Cloud Storage, you must also include the appropriate roles for those services. To view a list of all IAM roles, see the [IAM roles](https://docs.cloud.google.com/iam/docs/roles-permissions) documentation.

### Translation models

When you request a translation by using Cloud Translation - Basic, Google uses a pre-trained Neural Machine Translation (NMT) model. For Cloud Translation - Advanced, you can use the pre-trained NMT model, the Translation LLM, or a custom AutoML Translation model.

Service accounts that you use for translation requests must have the permissions to access the NMT and AutoML models, which can be located in different projects. For example, you might have a central project that contains your translation models to simplify maintenance and billing. Service accounts in that project or other projects can use those models but require permissions to do so.

For more information about translation models, refer to [Translating text (Advanced)](https://docs.cloud.google.com/translate/docs/advanced/translating-text-v3).

### Client libraries

The client libraries and methods for Cloud Translation - Advanced differ from Cloud Translation - Basic. For example, calls to Cloud Translation - Advanced require resource names. For more information, see the Cloud Translation - Advanced client libraries [overview](https://docs.cloud.google.com/translate/docs/reference/libraries/v3/overview-v3) or try the translate text (advanced edition) [quickstart](https://docs.cloud.google.com/translate/docs/advanced/translate-text-advance).

#### Resources, projects, and locations

Requests to Cloud Translation - Advanced require the name of the [resource](https://docs.cloud.google.com/apis/design/resources) that you want to use. A resource is typically a qualified name that includes the project name and its [location](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources), which specifies where the request is run. For example, the name of an AutoML model is a resource name.

If your Google Cloud project has the name `my-project` and the location for the resource is `us-central1`, then the full name of your resources might look like the following:
    
    
    projects/MY_PROJECT/locations/us-central1/...
    

The URL that you send a [`getSupportedLanguages`](https://docs.cloud.google.com/translate/docs/reference/rest/v3beta1/projects.locations/getSupportedLanguages) request might look like the following:
    
    
    https://translation.googleapis.com/v3/projects/my-project/locations/us-central1/supportedLanguages
    

**Note:** All of your resources in a single request to Cloud Translation - Advanced must have the same location. Currently, only `global` and `us-central1` locations are supported. For all custom resources—AutoML models, glossaries, long-running-operations—you must use `us-central1`. You can also use `us-central1` when you use general translation models and language detection. You can only use the `global` location when you use general translation models and language detection. Cloud Translation - Advanced also provides multi-regional endpoints, such as `translate-eu.googleapis.com` to keep data handling within the EU. This is a unique endpoint for EU and not a location setting on the global API. For more information, see [Global and multi-regional endpoints](https://docs.cloud.google.com/translate/docs/advanced/endpoints).

### Content limit per request

The Cloud Translation API is optimized for translating of smaller requests. The recommended maximum length for each request is 5K characters ([code points](https://wikipedia.org/wiki/UTF-8)). However, the more characters that you include, the higher the response latency. For Cloud Translation - Advanced, the maximum number of code points for a single request is 30K. Cloud Translation - Basic has a maximum request size of 100K bytes. 

The Cloud Translation API rejects requests larger than the maximum and gives a `400 INVALID_ARGUMENT` error regardless of the available quota. 

For more information about quotas and limits, see [Quotas](https://docs.cloud.google.com/translate/quotas).

## What's next

Use Cloud Translation - Advanced to [translate text](https://docs.cloud.google.com/translate/docs/advanced/translating-text-v3), [create glossaries](https://docs.cloud.google.com/translate/docs/advanced/glossary), or [make batch requests](https://docs.cloud.google.com/translate/docs/advanced/batch-translation). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
