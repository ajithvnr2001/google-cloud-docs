---
url: https://docs.cloud.google.com/gemini/docs/discover/responsible-ai/
title: Google Cloud with Gemini and responsible AI \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:15.214718+00:00
---

# Google Cloud with Gemini and responsible AI  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/discover/responsible-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Google Cloud with Gemini and responsible AI Stay organized with collections  Save and categorize content based on your preferences. 

Gemini products in Google Cloud, such as Gemini Code Assist, incorporate responsible AI design principles to help you navigate the capabilities, limitations, and risks of generative AI. Understanding these safety controls and operational boundaries lets you evaluate and deploy AI assistance across your workflows.

## Capabilities and risks of large language models

Large language models (LLMs) can perform many useful tasks such as the following:

  * Translate language.
  * Summarize text.
  * Generate code and creative writing.
  * Power chatbots and virtual assistants.
  * Complement search engines and recommendation systems.



At the same time, the evolving technical capabilities of LLMs create the potential for misapplication, misuse, and unintended or unforeseen consequences.

LLMs can generate output that you don't expect, including text that's offensive, insensitive, or factually incorrect. Because LLMs are incredibly versatile, it can be difficult to predict exactly what kinds of unintended or unforeseen outputs they might produce.

Given these risks and complexities, products such as Gemini Code Assist are designed with [Google's AI principles](https://ai.google/responsibility/principles/) in mind. However, it's important for users to understand some of the limitations of Gemini products to work safely and responsibly.

## Limitations of Gemini products in Google Cloud

Some of the limitations that you might encounter using Gemini products in Google Cloud include (but aren't limited to) the following:

  * **Edge cases.** Edge cases refer to unusual, rare, or exceptional situations that aren't well represented in the training data. These cases can lead to limitations in the output of Gemini models, such as model overconfidence, misinterpretation of context, or inappropriate outputs.

  * **Model hallucinations, grounding, and factuality.** Gemini models might lack grounding and factuality in real-world knowledge, physical properties, or accurate understanding. This limitation can lead to model hallucinations, where Gemini might generate outputs that are plausible-sounding but factually incorrect, irrelevant, inappropriate, or nonsensical. Hallucinations can also include fabricating links to web pages that don't exist and have never existed. For more information, see [Write better prompts for Gemini in Google Cloud](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).

  * **Data quality and tuning.** The quality, accuracy, and bias of the prompt data that's entered into Gemini products in Google Cloud can have a significant impact on its performance. If users enter inaccurate or incorrect prompts, Gemini might return suboptimal or false responses.

  * **Bias amplification.** Language models can inadvertently amplify existing biases in their training data, leading to outputs that might further reinforce societal prejudices and unequal treatment of certain groups.

  * **Language quality.** While Gemini products in Google Cloud yield impressive multilingual capabilities on the benchmarks that we evaluated against, the majority of our benchmarks (including all of the fairness evaluations) are in American English.

Language models might provide inconsistent service quality to different users. For example, text generation might not be as effective for some dialects or language varieties because they are underrepresented in the training data. Performance might be worse for non-English languages or English language varieties with less representation.

  * **Fairness benchmarks and subgroups.** Google Research's fairness analyses of Gemini models don't provide an exhaustive account of the various potential risks. For example, we focus on biases along gender, race, ethnicity, and religion axes, but perform the analysis only on the American English language data and model outputs.

  * **Limited domain expertise.** Gemini models have been trained on Google Cloud technology, but it might lack the depth of knowledge that's required to provide accurate and detailed responses on highly specialized or technical topics, leading to superficial or incorrect information.

When you use the **Gemini** pane in the Google Cloud console, Gemini is not context aware of your specific environment, so it cannot answer questions such as "When was the last time I created a VM?"

In some cases, Gemini products in Google Cloud send a specific segment of your context to the model to receive a context-specific response—for example, when you click the **Troubleshooting suggestions** button in the Error Reporting service page.




## Gemini safety and toxicity filtering

Prompts and responses for Gemini products in Google Cloud, such as Gemini Code Assist, are checked against a comprehensive list of safety attributes as applicable for each use case. These safety attributes aim to filter out content that violates our [Acceptable Use Policy](https://cloud.google.com/terms/aup). If an output is considered harmful, the response will be blocked.

## What's next

  * Learn more about [how Gemini cites sources when helps you generate code](https://docs.cloud.google.com/gemini/docs/discover/works#how-when-gemini-cites-sources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
