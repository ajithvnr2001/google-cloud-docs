---
url: https://docs.cloud.google.com/kms/known-issues/
title: Known issues \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:32.737406+00:00
---

# Known issues  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Resources ](https://docs.cloud.google.com/kms/docs/resources)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

If you find any way in which the service isn't working as well as it could be, [let us know](https://docs.cloud.google.com/kms/docs/support), but first, check this list to make sure we're not already working on it.

  * Limitations in Cloud console: 
    * Cloud Audit Logs for Cloud KMS in the Activity stream read like generic logs, and are not easily read by a human.
    * Currently, you can only display and manage up to 1,000 keys in the Cloud console. If you would like to manage more keys, use the `gcloud` Command Line Interface. This limitation also applies to viewing key rings and versions. 
  * Client libraries are [Google API Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained#google_api_client_libraries) instead of the newer [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained#google_cloud_client_libraries). This is for better compatibility with the use of Cloud KMS from within Google App Engine. 
    * Batch operations in the libraries are not possible.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
