---
url: https://docs.cloud.google.com/gemini/docs/discover/data-governance/
title: How Gemini products in Google Cloud use your data \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:54.780424+00:00
---

# How Gemini products in Google Cloud use your data  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/discover/data-governance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  How Gemini products in Google Cloud use your data Stay organized with collections  Save and categorize content based on your preferences. 

Gemini for Google Cloud lets you use AI-powered assistance while conforming to [Google's privacy commitment](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-unveils-ai-and-ml-privacy-commitment) with generative AI technologies. When you use Gemini in the Google Cloud console or in a development environment, Google Cloud handles your prompts in accordance with the [terms of service](https://cloud.google.com/terms) and [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum).

For more information about Gemini products in Google Cloud, see [Google Cloud with Gemini overview](https://docs.cloud.google.com/gemini/docs/overview).

## Google's privacy commitment

Google was one of the first in the industry to publish an [AI/ML privacy commitment](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-unveils-ai-and-ml-privacy-commitment), which outlines our belief that customers should have the highest level of security and control over their data that's stored in the cloud. That commitment extends to Google Cloud generative AI products. Google helps ensure that its teams are following these commitments through robust data governance practices, which include reviews of the data that Google Cloud uses in the development of its products. You can find more details about how Google processes data in [Customer Data Processing Addendum (CDPA)](https://cloud.google.com/terms/data-processing-addendum) or the data processing agreement applicable to your Google Cloud service.

## Data you submit and receive

The questions that you ask Gemini, including any input information or code that you submit to Gemini to analyze or complete, are called _prompts_. The answers or code completions that you receive from Gemini are called _responses_.

Gemini doesn't use your prompts or its responses as data to train its models. Some features are only available through the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/gemini-for-cloud/ttp/welcome), which lets you optionally share data, but the data is used for product improvements, not for training Gemini models.

[Code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview) lets you get code suggestions based on your organization's private codebase directly from Gemini Code Assist. When you use code customization, we securely access and store your private code. This access and storage is essential for delivering the code customization service you've requested. To configure and use code customization, see [Configure and use Gemini Code Assist code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization).

Because Gemini is an evolving technology, it can generate output that's plausible-sounding but factually incorrect. We recommend that you validate all output from Gemini before you use it. For more information, see [Gemini products in Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Encryption of prompts

When you submit prompts to Gemini, your data is encrypted in-transit as input to the underlying model in Gemini. For more information on Gemini data encryption, see [Default encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) and [Encryption in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit).

## Program data generated from Gemini

Gemini is trained on first-party Google Cloud code as well as selected third-party code. You're responsible for the security, testing, and effectiveness of your code, including any code completion, generation, or analysis that Gemini offers you.

Gemini also provides source citations when suggestions directly quote at length from a source to help you comply with any license requirements.

Because responses in Gemini are generated from a model that's trained on many lines of code, you should exercise the same care with Gemini-provided code that you would with any other code. Make sure that you test the code properly and check for security vulnerabilities, incompatibilities, and other potential issues.

## What's next

  * Learn about the [security, privacy, and compliance of Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/security-privacy-compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
