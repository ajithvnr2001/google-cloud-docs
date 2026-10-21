---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/view-app/
title: Step 5: Test your IAP-secured app \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:39:55.729898+00:00
---

# Step 5: Test your IAP-secured app  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/view-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Step 5: Test your IAP-secured app Stay organized with collections  Save and categorize content based on your preferences. 

In this section, you test the app that you've deployed to Cloud Run by viewing it in your browser. You can view the app only after the status of the Google-managed certificate becomes `ACTIVE`. Provisioning a Google-managed certificate might take up to 60 minutes. For more information about Google-managed SSL certificates, see [Use Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#certificate-resource-status).

## Check the status of your certificate

  1. Go to the **Classic Certificates** tab in the Google Cloud console.

[Go to Classic Certificates](https://console.cloud.google.com/security/ccm/list/lbCertificates)

  2. In the **Status** column, check the status of the `my-genai-app-certificate` certificate.

You can proceed with the rest of the tutorial after the status changes to **Active**. Note that certificate provisioning might take up to 60 minutes.




## View the deployed app

  1. Sign in with a principal's account that you configured in IAP.

  2. In your browser, open the following URL:
         
         https://DOMAIN_NAME/app
         

Replace DOMAIN_NAME with domain name provided during certificate creation.




[ Previous arrow_back  Configure IAP  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/configure-iap)

[ Next Clean up your project  arrow_forward  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/clean-up)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
