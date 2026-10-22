---
url: https://docs.cloud.google.com/livestream/docs/how-to/configure-cors/
title: Configure cross-origin resource sharing (CORS) \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:16.469601+00:00
---

# Configure cross-origin resource sharing (CORS)  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/how-to/configure-cors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Guides ](https://docs.cloud.google.com/livestream/docs/overview)



Send feedback 

#  Configure cross-origin resource sharing (CORS) Stay organized with collections  Save and categorize content based on your preferences. 

Cross Origin Resource Sharing (CORS) allows interactions between resources from different origins, something that is normally prohibited in order to prevent malicious behavior. This page explains how to configure CORS on a Cloud Storage bucket for a sample origin, the origin of the online [Shaka](https://shaka-player-demo.appspot.com/demo/) media player.

To [enable cross-origin resource sharing (CORS) on a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/using-cors#configure-cors-bucket), do the following: 

  1. Create a JSON file that contains the following: 
         
         [
           {
             "origin": ["https://shaka-player-demo.appspot.com/"],
             "responseHeader": ["Content-Type", "Range"],
             "method": ["GET", "HEAD"],
             "maxAgeSeconds": 3600
           }
         ]

  2. Run the following command after replacing `JSON_FILE_NAME` with the name of the JSON file you created in the previous step: 
         
         gcloud storage buckets update gs://BUCKET_NAME --cors-file=JSON_FILE_NAME.json




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
