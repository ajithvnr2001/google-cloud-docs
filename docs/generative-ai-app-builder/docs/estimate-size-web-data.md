---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/estimate-size-web-data/
title: Get an estimate of monthly storage costs \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:27.946340+00:00
---

# Get an estimate of monthly storage costs  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/estimate-size-web-data/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Get an estimate of monthly storage costs Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

[Advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing) incurs monthly data storage charges based on the size of the web data that you import into your data store. To get an estimate of the size of your web data before importing it, you can call the [`estimateDataSize`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/estimateDataSize) method and specify the web pages that you want to import. The `estimateDataSize` method is a [long-running operation](https://google.aip.dev/151) that runs until the process for estimating the data size is complete. This can take from a few minutes to over an hour, depending on the number of web pages that you specify. After you have an estimate of the size of your web data, you can get an estimate of your monthly data storage costs using the [Agent Search pricing page](https://cloud.google.com/generative-ai-app-builder/pricing#data_index_pricing).

**Important:**

  * You're permitted to use the `estimateDataSize` method only on web domains that your company owns or is authorized to use.
  * This method provides a very rough initial estimate. It assumes each page is 500 KB and counts only webpage URLs that are currently known to Google.



## Before you begin

Determine the URL patterns for the websites that you intend to include (and optionally exclude) when you import web data into your data store. You specify these URL patterns when you call the `estimateDataSize` method.

## Procedure

To get an estimate of the size of your web data, follow these steps:

  1. Call the [`estimateDataSize`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations/estimateDataSize) method.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global:estimateDataSize" \
         -d '{
           "website_data_source": {
             "estimator_uri_patterns": [
               {
                 "provided_uri_pattern": "URI_PATTERN_TO_INCLUDE",
                 "exact_match": EXACT_MATCH_BOOLEAN_1
               },
               {
                 "provided_uri_pattern": "URI_PATTERN_TO_EXCLUDE",
                 "exact_match": EXACT_MATCH_BOOLEAN_2,
                 "exclusive": EXCLUSIVE_BOOLEAN
               }
             ]
           }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.

     * `URI_PATTERN_TO_INCLUDE`: the URL patterns for the websites that you want to include in your data size estimate.

     * `URI_PATTERN_TO_EXCLUDE`: (Optional) The URL patterns for the websites that you want to exclude from your data size estimate.

For `URI_PATTERN_TO_INCLUDE` and `URI_PATTERN_TO_EXCLUDE`, you can use patterns similar to the following:

       * Entire website: `www.mysite.com`
       * Parts of a website: `www.mysite.com/faq`
       * Entire domain: `mysite.com` or `*.mysite.com`
     * `EXCLUSIVE_BOOLEAN`: (Optional) If `true`, then the provided URI pattern represents web pages that are excluded from your data size estimate. The default is `false`, which means that the provided URI pattern represents web pages that are included in your data size estimate.

     * `EXACT_MATCH_BOOLEAN`: (Optional) If `true`, then the provided URI pattern represents a single web page, instead of the web page and all of its children. The default is `false`, which means that the provided URI pattern represents the web page and all of its children.

The output includes the `name` field, which is the name of the long-running operation. Save the `name` value to use in the following step.

#### Click for an example curl command and response.
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    -H "Content-Type: application/json" \
    "https://discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/global:estimateDataSize" \
    -d '{
      "website_data_source": {
        "estimator_uri_patterns": [
          {
            "provided_uri_pattern": "docs.cloud.google.com/generative-ai-app-builder",
            "exact_match": false
          },
          {
            "provided_uri_pattern": "docs.cloud.google.com/generative-ai-app-builder/apis",
            "exact_match": false,
            "exclusive": true
          }
        ]
      }
    }'
    {
      "name": "projects/my-project-123/locations/global/operations/estimate-data-size-4312594881427311412",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.EstimateDataSizeMetadata"
      }
    }

  2. Poll the [`operations.get`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.operations/get) method.
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://discoveryengine.googleapis.com/v1/OPERATION_NAME"
         

Replace `OPERATION_NAME` with the `name` value that you saved in the previous step. You can also get the operation name by [listing long-running operations](https://docs.cloud.google.com/generative-ai-app-builder/docs/long-running-operations#list-lros).

  3. Evaluate each response.

     * If a response does not contain `"done": true`, then the process for estimating the data size is not complete. Continue polling.

The output is similar to the following:
           
           {
             "name": "projects/PROJECT_ID/locations/global/operations/estimate-data-size-4312594881427311412",
             "metadata": {
               "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.EstimateDataSizeMetadata",
               "createTime": "2026-07-14T18:40:39.365840Z"
             }
           }
           

     * If a response contains `"done": true`, then the process for estimating the data size is complete. Save the `DATA_SIZE_BYTES` value from the response to use in the following step.

The output is similar to the following:
           
           {
             "name": "projects/PROJECT_ID/locations/global/operations/estimate-data-size-4312594881427311412",
             "metadata": {
               "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.EstimateDataSizeMetadata",
               "createTime": "2026-07-14T18:40:39.365840Z"
             },
             "done": true,
             "response": {
               "@type": "type.googleapis.com/google.cloud.discoveryengine.v1alpha.EstimateDataSizeResponse",
               "dataSizeBytes": DATA_SIZE_BYTES,
               "documentCount": DOCUMENT_COUNT
             }
           }
           

This output includes the following values:

       * `DATA_SIZE_BYTES`: the estimated size of your web data, in bytes.

       * `DOCUMENT_COUNT`: the estimated number of web pages in your web data.

  4. Divide the `DATA_SIZE_BYTES` value from the previous step by 1,000,000,000 to get gigabytes. Save this value for the following step.

  5. To get an estimate for your monthly data storage costs:

     1. Go [Google Cloud's pricing calculator](https://cloud.google.com/products/calculator).

     2. Click **Add to estimate**.

     3. Search for `Agent Search` and then click the **Agent Search** box.

     4. In the **Data Index** box, enter the estimated size of your web data, in gigabytes, from the previous step.

See the **Estimated cost** box for your estimated data storage cost.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
