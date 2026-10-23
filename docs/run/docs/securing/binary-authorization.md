---
url: https://docs.cloud.google.com/run/docs/securing/binary-authorization/
title: Use Binary Authorization \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:26.498913+00:00
---

# Use Binary Authorization  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/securing/binary-authorization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Use Binary Authorization Stay organized with collections  Save and categorize content based on your preferences. 

Binary Authorization is a deploy-time security control that ensures only trusted container images are deployed to your Cloud Run resources. With Binary Authorization, you can require images to be signed by trusted authorities during the development process and then enforce signature validation when deploying. By enforcing validation, you can gain tighter control over your container environment by ensuring only verified images are integrated into the build-and-release process.

Learn how to [set up Binary Authorization for Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/overview).

## Exempt Cloud Run functions images from Binary Authorization policy

To deploy functions in Cloud Run, the Binary Authorization policy administrator must configure a Binary Authorization policy using [allowlist patterns](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#allowlist_patterns) to exempt all images from the specified repository and its subdirectories.

### Functions using the Cloud Run Admin API

If you are deploying your function with the [`gcloud run deploy...`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--binary-authorization) command, use this allowlist pattern: 

`REGION-docker.pkg.dev/PROJECT_ID/cloud-run-source-deploy/**`

With the allowlist enabled, deploy your function with [Binary Authorization enabled and set to `default`](https://docs.cloud.google.com/binary-authorization/docs/run/enabling-binauthz-cloud-run#enable-on-new-job):
    
    
      gcloud run deploy YOUR_FUNCTION_NAME \
        ...
        --binary-authorization default
    

### Functions using the Cloud Functions v2 API

If you are deploying your function with the [`gcloud functions deploy...`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--binary-authorization) command, use this allowlist pattern:

`REGION-docker.pkg.dev/PROJECT_ID/gcf-artifacts/**`

With the allowlist enabled, deploy your function with Binary Authorization enabled and set to `default`:
    
    
      gcloud functions deploy YOUR_FUNCTION_NAME \
        ...
        --binary-authorization default
    

## What's next

  * Learn how to [set up Binary Authorization for Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
