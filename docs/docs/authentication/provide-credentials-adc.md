---
url: https://docs.cloud.google.com/docs/authentication/provide-credentials-adc/
title: Set up Application Default Credentials \u00a0|\u00a0 Authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:09.609923+00:00
---

# Set up Application Default Credentials  |  Authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/authentication/provide-credentials-adc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Authentication ](https://docs.cloud.google.com/docs/authentication)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Set up Application Default Credentials Stay organized with collections  Save and categorize content based on your preferences. 

How you set up Application Default Credentials (ADC) for use by Cloud Client Libraries, Google API Client Libraries, and the REST and RPC APIs depends on the environment where your code is running. 

For information about where ADC looks for credentials and in what order, see [How Application Default Credentials works](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

If you are using API keys, then you don't need to set up ADC. For more information, see [Use API keys to access APIs](https://docs.cloud.google.com/docs/authentication/api-keys-use).

## Provide credentials to ADC

Select the environment where your code is running:

  * [Local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment)

  * [Resource with an attached service account](https://docs.cloud.google.com/docs/authentication/set-up-adc-attached-service-account)

  * [Containerized environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-containerized-environment)

  * [On-premises or another cloud provider](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises)

  * [Cloud-based development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-cloud-dev-environment)




## The gcloud CLI and ADC

You can provide credentials to ADC by using the [`gcloud auth application-default login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login) command. This makes credentials available to the Cloud Client Libraries and Google API Client Libraries.

The gcloud CLI itself doesn't use ADC to access Google Cloud resources. To learn how to provide credentials to the gcloud CLI, see [Authentication for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate).

## What's next

  * Learn more about [how ADC finds credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials).
  * [Authenticate for using Cloud Client Libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).
  * [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest).
  * Explore [authentication methods](https://docs.cloud.google.com/docs/authentication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
