---
url: https://docs.cloud.google.com/translate/docs/advanced/custom-translations/
title: Custom translations overview \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:58.213099+00:00
---

# Custom translations overview  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/custom-translations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Custom translations overview

The default Google Neural Machine Translation (NMT) model covers a wide range of languages and works well for general-purpose text. However, in cases where you're translating domain-specific or style-sensitive text, custom translations can help you get more relevant translations.

Custom translations require you to provide your own example translations. Then, Cloud Translation can generate results that closely follow the style, tone, and vocabulary of your examples.

The advanced version of the Cloud Translation API provides a variety of solutions for customizing translations:

  * [NMT customization](https://docs.cloud.google.com/translate/docs/advanced/nmt-customization): You can train your own custom version of the standard NMT model with a rich dataset of translation examples.

  * [TLLM customization](https://docs.cloud.google.com/translate/docs/advanced/tllm-customization): You can tune your own custom version of the standard Translation LLM (TLLM) model with either a limited or extensive dataset of translation examples.

  * [Adaptive Translation](https://docs.cloud.google.com/translate/docs/advanced/adaptive-translation): You can create a lightweight customization of the Translation LLM (TLLM) model with a limited dataset of translation examples.

  * [Glossary](https://docs.cloud.google.com/translate/docs/advanced/glossary): You can use a glossary to serve as a custom dictionary for correctly and consistently translating domain-specific terms.




## NMT customization

To train your own version of the NMT model, you import a substantial dataset of your own translation examples. You can then request translations that use your model instead of the default NMT model. A custom model of this kind can work well for translating domain-specific text, where using the correct terminology is extremely important.

You are charged both for the model training time and the number of input characters that you send for translation.

## TLLM customization

To train your own version of the TLLM model, you import a dataset of your own translation examples. You can then request translations that use your model instead of the default TLLM model. A custom model of this kind can work well for translating domain-specific text, where using the correct terminology is extremely important.

You are charged both for the model training time and the number of input characters that you send for translation.

## Adaptive Translation

Adaptive translations use LLMs combined with small datasets to provide high-quality translations, often on par with Cloud Translation custom models. You don't train or maintain any models. Compared to custom models, Adaptive Translation works well for getting responses that are similar in style, tone, and voice with your input.

For Adaptive Translation, you're charged on the number of input and output characters.

## Glossaries

Glossaries allow you to specify how particular terms should be translated. You provide a list of terms and their translations that Cloud Translation uses to ensure consistent and accurate translations for those terms. This is especially useful for domain-specific vocabulary.

You are charged for glossary usage based on the number of characters sent for translation.

## Prepare example translations

Prepare example translations as segment pairs, which consists of one sentence in a source language and a corresponding sentence that's translated in the target language. Save these segment pairs in a tab-separated values (TSV) file or Translation Memory eXchange (TMX) file.

Choose examples that represent the linguistic domain of the content that you plan to translation. For additional guidance, see the [Data preparation](https://docs.cloud.google.com/translate/docs/advanced/nmt-customization#data-preparation) section.

### TSV

For tab-separated files, each row has the following format:

  * `Source segment` _tab_ `Translated segment`



Don't include a header row with language codes to identify the source and target languages. You specify these languages when you create a dataset. The following example includes segment pairs for English to German translations:
    
    
    It's a beautiful day.**\t** Es ist ein schöner Tag.
    Tomorrow it will rain.**\t** Morgen wird es regnen.
    

All content in a TSV file must be plain text. If the text includes HTML tags or other markup, Cloud Translation treats the markup as plain text.

### TMX

TMX is a standard XML format for providing source and target translation segments. Cloud Translation supports input files in a format based on [TMX version 1.4](https://www.gala-global.org/lisa-oscar-standards). The following example illustrates the required structure:
    
    
    <?xml version='1.0' encoding='utf-8'?>
    <!DOCTYPE tmx SYSTEM "tmx14.dtd">
    <tmx version="1.4">
      <header segtype="sentence" o-tmf="UTF-8"
      adminlang="en" srclang="en" datatype="PlainText"/>
      <body>
        <tu>
          <tuv xml:lang="en">
            <seg>It's a beautiful day.</seg>
          </tuv>
          <tuv xml:lang="de">
            <seg>Es ist ein schöner Tag.</seg>
          </tuv>
        </tu>
        <tu>
          <tuv xml:lang="en">
            <seg>Tomorrow it will rain.</seg>
          </tuv>
          <tuv xml:lang="de">
            <seg>Morgen wird es regnen.</seg>
          </tuv>
        </tu>
      </body>
    </tmx>
    

The `<header>` element of a well-formed TMX file must identify the source language by using the `srclang` attribute, and every `<tuv>` element must identify the language of the contained text using the `xml:lang` attribute.

All `<tu>` elements must contain a pair of `<tuv>` elements with the same source and target languages. If a `<tu>` element contains more than two `<tuv>` elements, Cloud Translation processes only the first `<tuv>` matching the source language and the first matching the target language and ignores the rest. If a `<tu>` element does not have a matching pair of `<tuv>` elements, Cloud Translation skips over the invalid `<tu>` element.

Cloud Translation strips the markup tags from around a `<seg>` element before processing it. If a `<tuv>` element contains more than one `<seg>` element, Cloud Translation concatenates their text into a single element with a space between them.

If the file contains XML tags other than those shown earlier, Cloud Translation ignores them.

If the file does not conform to proper XML and TMX format (for example, if it is missing an end tag or a `<tmx>` element) Cloud Translation aborts processing it. Cloud Translation also aborts processing if it skips more than 1024 invalid `<tu>` elements.

The minimum required and maximum allowed number segment pairs for each feature is different. For more information, see the [Cloud Translation data preparation](https://docs.cloud.google.com/translate/docs/advanced/custom-nmt-prepare) or [adaptive translation data requirements](https://docs.cloud.google.com/translate/docs/advanced/adaptive-translation#data_requirements_and_suggestions).

To prepare a dataset for a custom TLLM model, see [Prepare data for supervised tuning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/translation-supervised-tuning-prepare).

## What's next

  * For more information about each feature, see [NMT customization overview](https://docs.cloud.google.com/translate/docs/advanced/nmt-customization) or [Adaptive translation](https://docs.cloud.google.com/translate/docs/advanced/adaptive-translation).
  * For language support, see [Supported languages](https://docs.cloud.google.com/translate/docs/languages).
  * For pricing details, see [Cloud Translation pricing](https://docs.cloud.google.com/translate/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
