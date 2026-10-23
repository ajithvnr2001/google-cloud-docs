---
url: https://docs.cloud.google.com/translate/docs/advanced/tllm-customization/
title: Customize the TLLM model \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:56.439335+00:00
---

# Customize the TLLM model  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/tllm-customization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Customize the TLLM model

Use Cloud Translation - Advanced API to customize the Google [Translation LLM (TLLM)](https://docs.cloud.google.com/translate/docs/translation-llm) model without writing code. Tailor a custom model to your domain-specific content, producing more accurate translations than with the default Google TLLM model. The TLLM model covers a large number of language pairs and does well with general-purpose text. A custom model excels in handling specific, niche vocabularies. If you run a specialized reporting service that has the opportunity to expand into new countries, instead of hiring specialists, create and refine a custom model to do the job in real time.

## Data preparation

To train a custom model, supply matching pairs of segments in the source and target languages. These are pairs of words or phrases that mean the same thing in the languages you're translating from and to. The closer in meaning your segment pairs are, the better your model can work. While putting together the dataset of matching segment pairs, start with the use case:

  * What outcome are you trying to achieve?

  * What kinds of segments are important to translate correctly, to achieve that outcome? Can the TLLM model achieve it out of the box?

  * Is it possible for humans to translate these key segments in a way that satisfies you? If the translation task is ambiguous enough that a person fluent in both languages would have a hard time doing a satisfactory job, the TLLM model might perform as well as a custom model.

  * What kinds of examples best reflect the type and range of segment pairs that your system will need to translate?




### Match data to your problem domain

Train a custom translation model to fit a particular linguistic domain. Ensure your segment pairs do the best possible job of covering the vocabulary, usage, and grammatical quirks of your industry or area of focus. Find documents with typical usages for the translation tasks you want accomplished, matching your parallel phrases as close in meaning as you can. Languages don't map perfectly in vocabulary or syntax, but try to capture the full diversity of semantics you expect to encounter. You're building on a model that already does a good job with general-purpose translation. Your examples are the last step to tweak custom models, so make sure they're relevant and representative.

### Capture the diversity of your linguistic space

Don't assume that how people write about a specific domain is uniform enough that a small number of text samples translated by a few translators should train a model that works for anyone else writing about that domain. We each bring a personality to the words we write, so a training dataset with segment pairs from many authors and translators is more likely to give you a model that's useful for translating writing from a diverse organization. Also consider the variety of segment lengths and structures: A dataset where all the segments are the same size or share a grammatical structure won't build a model that captures all the possibilities.

### Source your data

After you've established what data you need, find a way to source it. Take into account all data your organization collects. You might find that you're already collecting what you need to train a translation model. If you don't have the data you need, get it manually or outsource it to a third party.

### Keep humans in the loop

Try to make sure a person who understands both languages well has validated that the segment pairs match and represent understandable, accurate translations. A common mistake, like misaligning the rows of your training data spreadsheet, can yield nonsensical translations. High-quality data is needed for Cloud Translation - Advanced API to get a usable model.

### Keep fairness in mind with segment pairs

A core principle underpinning Google's ML products is human-centered machine learning, an approach that promotes [responsible AI practices](https://ai.google/education/responsible-ai-practices), including fairness. The goal of fairness in ML is to understand and prevent unjust or prejudicial treatment of people related to race, income, sexual orientation, religion, gender, and other characteristics historically associated with discrimination and marginalization, when and where they manifest in algorithmic systems or algorithmically aided decision-making.

### Clean up messy data

You might make mistakes when preprocessing data, which can confuse a custom model. Look for the following data issues that you can fix:

  * Remove duplicate source segments, particularly if they have different target translations, ensuring that Cloud Translation - Advanced API uses your preferred translation.
  * Align source segments to the correct target segments.
  * Match segments to the specified language. (Example: Include only Chinese segments in a Chinese dataset.)
  * For target segments with mixed languages, check that untranslated words are intentionally untranslated. Target segments that mistakenly include untranslated words add noise to your data, which can lower model quality.
  * Fix segments with typographical or grammatical errors.
  * Remove non-translatable content such as placeholder tags and HTML tags. Non-translatable content can result in punctuation errors.
  * Don't include segment pairs that replace general things with specific nouns. For example, translating a general term like _president_ to _JFK_. Instead, remove these or change the specific nouns to general ones.
  * Remove duplicate segments in the training and test sets.
  * Use consistent casing, which affects how a model learns, like distinguishing headline from body text.



## Process data

The following limitations apply:

  * Maximum input and output tokens: 
    * Serving: 1,000 (about 4,000 characters)
  * Validation dataset size: 1,024 examples
  * Training dataset file size: Up to 1GB for JSONL
  * Training example length: 1,000 (about 4,000 characters)
  * Adapter size: 
    * `Translation LLM V2`: Supported value is only 4. Using any other values (e.g., 1 or 8) will result in failure.



### Debug

Debugging a custom model is more about debugging the data than the model itself. If your model isn't translating the way you intend, check your data to see where it can be improved.

### Test

Even if your evaluation scores look okay, check the model to make sure its performance matches your expectations. If your training and test data are drawn from the same incorrect set of samples, the scores might be excellent even if the translation is nonsense. Prepare some examples that are not in the training set. Compare the results from the custom model with the Google TLLM base model. 

You might find that your model comes up with the same predictions as the base, especially on short segments or if you have a smaller training set, because the base model is already good. If so, try longer or more complex segments. If your segments come back identical to the predictions from the base model, it might indicate a data problem.

If there's a mistake that you're worried about your model making, make sure your test set or procedure covers that case adequately for you to feel safe using your model.

## What's next

  * For details about how to create your own dataset and custom model, see [Prepare training data](https://docs.cloud.google.com/translate/docs/advanced/custom-tllm-prepare). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
