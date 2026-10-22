---
url: https://docs.cloud.google.com/docs/ai-ml/generative-ai/generative-ai-or-traditional-ai/
title: When to use generative AI or traditional AI \u00a0|\u00a0 Generative AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:47.979240+00:00
---

# When to use generative AI or traditional AI  |  Generative AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/ai-ml/generative-ai/generative-ai-or-traditional-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Generative AI ](https://docs.cloud.google.com/docs/generative-ai)
  * [ Guides ](https://docs.cloud.google.com/docs/ai-ml/generative-ai/generative-ai-or-traditional-ai)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# When to use generative AI or traditional AI

This document helps you identify when generative AI, traditional AI, or a combination of both might suit your business use case.

In this document, _traditional AI_ refers to AI capabilities and use cases that might not require employing generative AI capabilities, like some [classification](https://developers.google.com/machine-learning/crash-course/classification/video-lecture) and [predictive](https://cloud.google.com/learn/what-is-predictive-analytics) AI use cases. Traditional AI models excel at learning from existing data to classify information or predict future outcomes based on historical patterns. Generative AI models expand these capabilities to create summaries, uncover complex hidden correlations, or generate new content—like text, images, or videos—that reflect the style and patterns within the training data.

## When to use generative AI

In general, generative AI solutions excel at tasks like the following:

  * Creating and recommending content.
  * Powering conversational search and chatbots.
  * Scaling and automating workflow for repetitive tasks.
  * Using associative reasoning to find insights and relationships within documents and data.
  * Generating code and assisting developers in writing, explaining, and documenting code.



The following sections provide examples of these common, general generative AI use cases that can be customized to different industries.

### Content creation and recommendation

  * Generating marketing related content such as product images, social media posts, and emails with relevant images.
  * Translating content such as documents, website content, and multilingual chatbot conversations.
  * Summarizing text content, including documents, articles, customer feedback, and reports, to help with more informed data-driven decisions.
  * Creating summaries of information from multiple sources that can include text, images, and video or audio components.
  * Automatic captioning or subtitling of videos.
  * Creating creative multimedia content such as creating new images from text prompt descriptions, modifying or fixing images using text prompts (for example, removing an object or changing color scheme), and generating short videos or animations from text prompts or scripts.
  * Generating realistic synthetic voices for audio such as voice-over tracks and music.
  * Analyzing and understanding user behavior, preferences, reviews, and past interactions to provide personalized content recommendations. Analysis can be combined with real-time factors like location to tailor content recommendations across content like products, articles, and videos.



### Conversational search and chatbots

  * Building virtual assistants for user interactions like customer support and online sales.
  * Enabling conversational search through large knowledge bases with natural language queries.
  * Finding answers to complex questions that combine textual inquiries with related images.



### Document and data understanding

  * Extracting data and analyzing content from text such as reports, invoices, receipts, financial transactions, or contracts to highlight possible errors or compliance issues, identify potential risks, or uncover anomalies that are indicative of fraud.
  * Analyzing the sentiment of user-generated content like social media posts and product reviews.
  * Analyzing transcribed call center conversations to extract insights such as the most common reasons that customers give a low rating to call center interactions.
  * Analyzing cybersecurity data such as threat reports, articles, and repositories to extract key threat indicators. This analysis enables proactive cybersecurity defense to summarize and prioritize mitigation strategies with recommendations for faster response.

Analysis can translate complex attack graphs to plain-text explanations of exposure. It can also simulate possible attack paths to highlight impacted assets, and it can recommend mitigations before assets can be exploited.




### Code generation and developer assistance

Generative AI can help with the following kinds of tasks at all stages of the software development lifecycle (SDLC):

  * Generating APIs specs and documentation by using natural language prompts.
  * Creating assets such as code, functions, command-line commands, and Terraform scripts from natural language prompts.
  * Generating tests and code explanations, including comments and documentation to explain code.



For more information about how generative AI can transform business operations like customer service, employee productivity, and process automation, see [Business use cases](https://docs.cloud.google.com/ai/generative-ai#business-use-cases) in "Generative AI on Google Cloud."

## When to use traditional AI

Traditional AI use cases typically focus on predicting future outcomes or classifying a category based on an AI model that's trained on existing historical data sources like [tabular](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/tabular101) data and images. Traditional AI solutions often suffice to address several classification and predictive AI use cases such as the following:

  * **Classification use cases** : 
    * Filtering email spam by classifying emails as _spam_ or _not spam_ , based on a traditional classification AI model that's trained on historical data.
    * Training a traditional image classification model on specific images of good and defective products to effectively help with real-time inspection and defect detection in manufacturing.
  * **Regression use cases** : 
    * Predicting continuous numerical values like predicting house prices based on specific house features and location.
    * Predicting how much revenue a customer of an ecommerce platform will generate during their relationship with the company based on historical purchase data.
  * **Time series forecasting use cases** : Forecasting sales and demand.
  * **Clustering use cases** : Performing customer segmentation.



For more information about using traditional AI, see [Uses and examples of predictive analytics](https://cloud.google.com/learn/what-is-predictive-analytics#section-5) in "What is predictive analytics?"

## Decide between traditional AI and generative AI

The following simplified decision tree provides a high-level reference for some use case-based decision paths. In some cases, it might be best to use both traditional AI and generative AI, as described in the next section, "When to combine generative AI with traditional AI."

A decision tree shows when to use generative AI, traditional classification or predictive AI, or a pre-trained AI model.[ ![A decision tree shows when to use generative AI, traditional classification or predictive AI, or a pre-trained AI model.](https://docs.cloud.google.com/static/docs/ai-ml/generative-ai/images/evaluate-define-generative-ai-use-case-decision-tree.svg)](https://docs.cloud.google.com/static/docs/ai-ml/generative-ai/images/evaluate-define-generative-ai-use-case-decision-tree.svg) Click diagram to enlarge.**Note:** in some scenarios, the complexity of model selection might require a more in-depth analysis that's beyond the scope of this decision tree. An in-depth analysis involves a more comprehensive analysis of the data, anticipated outcomes, expected serving latency (such as real-time serving use cases), specific model metrics, and other influential factors.

The decision tree includes the following use case-driven questions and answers:

  * If your use case is related to classification or detection, check whether a [pre-trained traditional AI model](https://docs.cloud.google.com/vertex-ai/docs#vertex-ai-and-cloud-ml-products) can meet your use case requirements. Pre-trained traditional models include AI APIs like Document AI, Vision AI, Natural Language API, and Video Intelligence API.

    * If a pre-trained model meets your requirements, use the pre-trained model.
    * If a pre-trained model can't meet your requirements, check whether enough training data is available to custom train a model. 
      * If sufficient training data is available, what should be prioritized: more control of model training or achieving faster go-to-market (GTM)? 
        * If you require high control of the model training with customizations like using any preferred model algorithm, developing your own loss functions, using specific features of model [explainability](https://docs.cloud.google.com/explainable-ai), the number of layers in the model, learning rate, and other model [hyperparameters](https://developers.google.com/machine-learning/guides/text-classification/step-5), use a custom training of a traditional AI model. For information about the differences between custom training or training a model in Vertex AI by using AutoML, see [Choose a training method](https://docs.cloud.google.com/vertex-ai/docs/start/training-methods).
        * If your business priority is a faster GTM, use generative AI. If your use case is specialized, you can improve the performance of a model by using model tuning like [supervised tuning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models#how-tuning-works) for classification, sentiment analysis, or entity extraction.
      * If a training dataset isn't available, or if available datasets aren't large enough to custom train a model, use generative AI models with [prompt engineering](https://docs.cloud.google.com/discover/what-is-prompt-engineering). These models can be tuned further to perform specialized tasks by using [data examples](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-supervised-tuning-prepare).
  * If your use case is related to predictive AI use cases, use traditional AI. Traditional predictive AI is particularly effective with structured data.

  * If your use case is related to generative AI use cases like summarization, content generation, or advanced transcription, use generative AI. Use of generative AI includes use cases that require processing and inputting information from multiple modalities like text, images, videos, or audio.




Although data scientists and ML engineers commonly lead the model selection process, it's important to also consider the input of key stakeholders like business leaders, product owners, domain experts, and end users. For example, these stakeholders might engage in the following ways:

  * **Business leaders and decision-makers** : Approve the selection when it's aligned with the business priorities.
  * **Product owners** : Might require influence or have more control of the model behavior to align it with the product priorities.
  * **Domain experts** : Apply their domain expertise to improve model effectiveness.
  * **End users** : Might need to understand the output of the model, and how to incorporate the output for more informed decision-making.



## When to combine generative AI with traditional AI

Traditional AI and generative AI aren't mutually exclusive. In some business use cases, they can be used to complement each other to address the ultimate business goal. For example, you can use output from a traditional AI model as part of the prompt for a generative AI model. The following are some examples of use cases for combining traditional and generative AI capabilities:

  * Traditional predictive AI can analyze historical data to forecast customer churn probability. This analysis can be integrated with an LLM or generative AI-powered chatbot, which empowers your sales team to explore the predictions by using natural language conversations. You can also generate business intelligence (BI) dashboards through simple conversation with the chatbot.
  * Traditional predictive AI can forecast risks of a specific use case, while generative AI can simulate different scenarios to help in formulating possible mitigation strategies.
  * Traditional predictive AI can identify customer segments to help create personalized marketing and campaign creation. You can then use generative AI to generate personalized marketing content that's tailored to each identified segment.
  * Traditional AI computer vision can detect and classify sign language to translate video input into text. Generative AI can add understanding of context and nuance within sign language, allowing for more optimized translation into written text, including multiple languages. Generative AI can also generate voice output from the text translation, enabling seamless two-way communication between signers and non-signers.
  * Traditional AI can perform video analytics and use video intelligence capabilities to extract vital insights and features from video assets. For example, it can perform object detection, person detection, text detection, and extraction from video assets. Generative AI can then use those insights to create novel experiences like chatbots, listings, reports, or articles.



To maximize the business benefits of your generative AI and traditional AI investments, prioritize necessary business outcomes and user needs (business-driven and user-centric AI solutions). This approach ensures that solutions stay relevant, drive adoption, enhance efficiency, and foster innovation. Prioritizing the user experience in AI-powered solutions helps to align expectations and deliver meaningful results.

## What's next

  * Learn how to [evaluate and define your generative AI business use case](https://docs.cloud.google.com/docs/ai-ml/generative-ai/evaluate-define-generative-ai-use-case).
  * Learn more about the stages of developing a generative AI application and choose the best products and tools for your use case in [Build a generative AI application on Google Cloud](https://docs.cloud.google.com/docs/ai-ml/generative-ai).
  * Assess your AI capabilities and create a roadmap to harness its potential with the [AI Readiness Workshop](https://docs.cloud.google.com/consulting/ai-readiness-workshop).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
