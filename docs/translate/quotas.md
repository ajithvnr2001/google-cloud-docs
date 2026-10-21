---
url: https://docs.cloud.google.com/translate/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:08.842396+00:00
---

# Quotas and limits  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Resources ](https://docs.cloud.google.com/translate/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Translation enforces quotas on the content size of requests and the number of requests that you can send. Quotas protect the community of Google Cloud users by preventing unforeseen spikes in usage. You can also lower your quotas to prevent excessive usage and control costs.

If you exceed your quota, Cloud Translation returns a `403` error. The error message states `Daily Limit Exceeded` if you exceeded a daily quota or `User Rate Limit Exceeded` if you exceeded a per minute quota.

Daily quotas reset at midnight Pacific Time, which means new quotas can take up to 24 hours to become effective.

## Set usage quotas

By default, the number of characters that you can send per day is unlimited. If you have a set budget, we recommend monitoring your daily usage and adjusting quotas according to your planned spend.

You can edit your quotas by using the Google Cloud console [quotas page](https://console.cloud.google.com/iam-admin/quotas?service=translate.googleapis.com). _v2_ quotas apply to Cloud Translation - Basic and _v3_ quotas apply to Cloud Translation - Advanced.

## Content quotas

Content quotas apply to synchronous requests for the `translateText`, `detectLanguage`, and `translateDocument` methods. For asynchronous requests, such as batch text translations, only the rate quotas apply.

All characters that you send to the Cloud Translation API count toward content quotas, including whitespace characters. If you use Cloud Translation - Basic and Cloud Translation - Advanced together, these quotas are cumulative.

For text translations, custom model quotas are counted separately and don't count against the general model quotas. However, there is a limit on the number of custom models requested in a single day from a project. Also, if `translation-llm` model is used, there is no content quota.

Quota | Default  
---|---  
Characters sent to **general model** per project per day (v2 and v3) | unlimited  
Characters sent to **general model** per project per minute (v2 and v3) | 6,000,000  
Characters sent to **general model** per project per minute per user (v2 and v3) | 6,000,000  
Characters sent for **transliteration** per project per minute (v3) | 100,000 (also counts towards the characters sent to general model per project per minute quota)  
Characters sent for **romanization** per project per minute (v3) | 100,000  
Characters sent to **custom models** per project per minute (v3) | 100,000  
Characters sent to **custom models** per project per minute per user (v3) | up to the project limit  
Number of unique **custom models** called per project per day (v3) | 30  
For **document translation** , pages sent per project per minute (v3) | 2,400  
For **document translation** , pages sent per project per minute per user (v3) | 2,400  
  
Per user quotas apply to the number of requests that an end user, who is using a client application, can make per minute. When you use a service account, the service account's identity is the user for quota purposes. If you use Cloud Translation - Basic and an API key, Cloud Translation uses the client's IP address to enforce this limit.

**Note:** For Document Translation, Cloud Translation also checks that the number characters don't exceed your character quotas. For XLSX and XLS files, only the character quotas apply (not the page quotas).

### Content limit per request

The Cloud Translation API is optimized for translating smaller requests. The recommended maximum length for each request is 5K characters ([code points](https://wikipedia.org/wiki/UTF-8)). However, the more characters that you include, the higher the response latency. For Cloud Translation - Advanced, the maximum number of code points for a single request is 30K. Cloud Translation - Basic has a maximum request size of 100K bytes. An alternative option is to use batch translations to send more content per request as a long running operation. 

The Cloud Translation API rejects requests larger than the maximum and gives a `400 INVALID_ARGUMENT` error regardless of the available quota. 

## Rate quotas

Cloud Translation applies a quota on the number of requests that you can send to the service. These quotas apply to all Cloud Translation method calls except for the `translateDocument` and `getSupportedLanguages` methods, which have their own request or content quotas.

Custom model and `translation-llm` quotas are counted separately and don't count against the other v3 rate quotas.

Quota | Default  
---|---  
Requests for getting supported languages ([v2](https://docs.cloud.google.com/translate/docs/reference/languages) and [v3](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/getSupportedLanguages) combined) per project per minute | 600  
v2 requests per project per minute | 300,000  
v2 requests per project per minute per user | up to the v2 project limit  
v3 requests per project per minute | 6000  
v3 romanization requests per project per minute | 6000  
v3 requests per project per minute per user | up to the v3 project limit  
v3 batch translation requests (text and documents) per project per day | unlimited  
v3 custom model translation requests per project per day | unlimited  
v3 custom model translation requests per project per minute | 600  
v3 custom model batch translation requests per project per day | unlimited  
v3 model creation requests per project per minute | 10  
v3 concurrent model creation requests per project | 2  
v3 Translation LLM requests per project per minute | 900  
v3 Adaptive Translation requests per project per minute | 900  
  
Per user quotas apply to the number of requests that an end user, who is using a client application, can make per minute. When you use a service account, the service account's identity is the user for quota purposes. If you use Cloud Translation - Basic and an API key, Cloud Translation uses the client's IP address to enforce this limit.

## Counting quotas

For Cloud Translation - Basic, content and rate quotas are counted against the project that is making the request, which is determined by the key that is used in the request.

For Cloud Translation - Advanced, content quota is checked against the project that is associated with the [model](https://docs.cloud.google.com/translate/docs/advanced/translating-text-v3#comparing-models) in the request. The rate quotas are checked against the project that is making the request.

For example, in the following translate text request, the rate quotas are checked against `project-id-1` because the request is coming from `project-id-1`. The content quota is checked against `project-id-2` because the request is using a model in that project.
    
    
    POST https://translation.googleapis.com/v3/projects/project-id-1/locations/us-central1:translateText
    {
      "Model":"projects/project-id-2/locations/us-central1/models/model-id",
      "sourceLanguageCode": "en",
      "targetLanguageCode": "ru",
      "contents": ["Dr. Watson, please discard your trash."]
    }

## Cloud Translation - Advanced limits

The following table describes Cloud Translation - Advanced limits, which cannot be changed.

Description | Limit  
---|---  
Maximum number of files that you can include in a single batch request | 100 files  
Maximum number of glossary resources for a project | 10,000  
  
### Translation LLM

Description | Limit  
---|---  
Maximum number of characters you can send per request | 30,000  
  
### Adaptive translation

Description | Limit  
---|---  
Maximum number of segment pairs you can import | 10,000 (Google Cloud console)  
30,000 (API)  
Maximum number of characters you can send per request | 30,000  
Maximum number of output characters from adaptive translation per request | 30,000 for languages (any text past this limit is dropped)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
