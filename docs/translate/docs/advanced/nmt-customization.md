---
url: https://docs.cloud.google.com/translate/docs/advanced/nmt-customization/
title: Customizing the NMT model \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:12.202635+00:00
---

# Customizing the NMT model  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/nmt-customization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Customizing the NMT model

Cloud Translation - Advanced API lets you customize the Google [Neural Machine Translation (NMT)](https://docs.cloud.google.com/translate/docs/advanced/nmt-model) model without writing code. This means you can tailor a custom model to your domain-specific content and produce more accurate translations than the default Google NMT model would.

The NMT model covers a large number of language pairs and does well with general-purpose text. Where a custom model excels is in handling specific, niche vocabularies. Customizing the NMT model lets you get the right translation of domain-specific terminology that matters to you.

If you run a specialized reporting service that has the opportunity to expand into new countries. Those markets require that your time-sensitive content be translated correctly in real time, including specialized terminology. Instead of having to hire bilingual staff or contract with specialist translators, both of which come at a high price, you can create and refine a custom model to do the job in real time at a much lower cost.

**Note** : You can customize the Google Neural Machine Translation (NMT) model using the Cloud Translation - Advanced API. We recommend that you use the Cloud Translation API to create datasets and models because any future enhancements will apply only to the Cloud Translation API. If you have existing AutoML resources, you can upgrade them to work with the Cloud Translation API. For more information, see [Upgrade AutoML resources](https://docs.cloud.google.com/translate/docs/advanced/automl-upgrade). 

## Data Preparation

In order to train a custom model, you supply matching pairs of segments in the source and target languages. These are pairs of words or phrases that mean the same thing in the language you want to translate from and the language you want to translate to. The closer in meaning your segment pairs are, the better your model can work.

While putting together the dataset of matching segment pairs, start with the use case:

  * What outcome are you trying to achieve?

  * What kinds of segments are important to translate correctly in order to achieve that outcome? Can the NMT model achieve that out of the box?

  * Is it possible for humans to translate these key segments in a way that satisfies you? If the translation task is ambiguous enough that a person fluent in both languages would have a hard time doing a satisfactory job, the NMT model might perform as well as a custom model.

  * What kinds of examples best reflect the type and range of segment pairs that your system will need to translate?




### Match data to your problem domain

You're training a custom translation model because you need a model that fits a particular linguistic domain. Make sure your segment pairs do the best possible job of covering the vocabulary, usage, and grammatical quirks of your industry or area of focus. Find documents that contain typical usages you'd find in the translation tasks you want accomplished, and make sure your parallel phrases match as closely in meaning as you can arrange. Of course, sometimes languages don't map perfectly in vocabulary or syntax, but try to capture the full diversity of semantics you expect to encounter in use if that's possible. You're building on top of a model that already does a pretty good job with general-purpose translation - your examples are the special last step that makes custom models work for your use case in particular, so make sure they're relevant and representative of usage you expect to see.

### Capture the diversity of your linguistic space

It's tempting to assume that the way people write about a specific domain is uniform enough that a small number of text samples translated by a small number of translators should be sufficient to train a model that works well for anyone else writing about that domain. But we're all individuals, and we each bring our own personality to the words we write. A training dataset with segment pairs from a broad selection of authors and translators is more likely to give you a model that's useful for translating writing from a diverse organization. In addition, consider the variety of segment lengths and structures; a dataset where all the segments are the same size or share a similar grammatical structure won't produce build a good custom model that captures all the possibilities.

### Source your data

After you've established what data you need, you need to find a way to source it. You can begin by taking into account all the data your organization collects. You might find that you're already collecting the data you would need to train a translation model. In case you don't have the data you need, you can obtain it manually or outsource it to a third-party provider.

### Keep humans in the loop

If it's at all feasible, make sure a person who understands both languages well has validated that the segment pairs match up correctly and represent understandable, accurate translations. A common mistake like misaligning the rows of your training data spreadsheet can yield translations that sound like nonsense. High-quality data is the most important thing you can provide to Cloud Translation - Advanced API to get a model that's usable for your business.

### Keep in mind fairness in developing segment pairs

A core principle underpinning Google's ML products is human-centered machine learning, an approach that promotes [responsible AI practices](https://ai.google/education/responsible-ai-practices), including fairness. The goal of fairness in ML is to understand and prevent unjust or prejudicial treatment of people related to race, income, sexual orientation, religion, gender, and other characteristics historically associated with discrimination and marginalization, when and where they manifest in algorithmic systems or algorithmically aided decision-making. You can read more in our [guide](https://docs.cloud.google.com/inclusive-ml) and in these _fair-aware_ notes:

> **Tip:** **Be Fair-aware!**
> 
>   * Review regulations in both your region and the locations your application will serve, as well as existing research or product information in your domain to learn about legal guidelines and possible cultural issues. [Read more...](https://docs.cloud.google.com/inclusive-ml#assess-your-use-case)
> 
>   * Consider whether your use case or product might negatively impact individuals' economic or other important life opportunities, and if so [read more...](https://docs.cloud.google.com/inclusive-ml#assess-your-use-case)
> 
>   * If you have scarce data about a particular subgroup, make sure that data is spread representatively between your training and test sets by performing the train-test split yourself.
> 
>   * When testing, think carefully about your problem domain and its potential for unfairness and bias. Come up with cases that would adversely impact your users if they were found in production, and test those first. [Read more...](https://docs.cloud.google.com/translate/docs/advanced/inclusive-ml#predict)
> 
>   * If you have a use case that warrants fairness considerations, read more about how to use your model in a manner that mitigates biases or adverse outcomes. [Read more...](https://docs.cloud.google.com/inclusive-ml#use-your-model)
> 
>   * [More data guidelines for fairness](https://docs.cloud.google.com/inclusive-ml#data-guidelines).
> 
> 


### Clean up messy data

You may make mistakes when preprocessing data, and some mistakes can really confuse a custom model. In particular, look for the following data issues that you can fix:

  * Remove duplicate source segments, particularly if they have different target translations. Cloud Translation - Advanced API uses only the first seen example and drops all other pairs at import time. By removing duplicates, you ensure that Cloud Translation - Advanced API uses your preferred translation.
  * Align source segments to the correct target segments.
  * Match segments to the specified language; for example, include only Chinese segments in a Chinese dataset.
  * For target segments that include mixed languages, check that untranslated words are intentionally untranslated, such as names of products or organizations. Target segments that mistakenly include untranslated words add noise to your training data, which can result in a lower quality model.
  * Fix segments with typographical or grammatical errors so that your model doesn't learn these errors.
  * Remove non-translatable content such as placeholder tags and HTML tags. Non-translatable content can result in punctuation errors.
  * Don't include segment pairs that replace general entities with specific nouns. For example, avoid an example that translates a general term like _president_ to the name of a specific president like _JFK_. That could teach the model to change all instances of _president_ to _JFK_. Instead, remove these segment pairs or change the specific nouns to general ones.
  * Remove duplicate segments in the training and test sets (see Dataset division about splitting your dataset into three subsets).
  * Split multiple segments into different segment pairs. Training on a dataset where many items have more than about 50 tokens (words) in them yields lower quality models. Split items into individual sentences where possible.
  * Use consistent casing. Casing affects how a model learns, for example, to distinguish a headline versus body text.
  * Remove TMX tags when importing data from a TSV file. In some cases, you might export your existing translation memory to a TSV file, which might include TMX tags. However, Cloud Translation - Advanced API cleans up translation unit tags only when you import from a TMX file (not for TSV files).



## Data processing

Cloud Translation - Advanced API stops parsing your data input file when:

  * There is invalid formatting.
  * There is an unreasonably long segment pair (10 MB).
  * The file uses an encoding other than UTF-8.



Cloud Translation - Advanced API ignores errors for problems it cannot detect, such as:

  * A `<tu>` element in a TMX file that doesn't specify the source or target language.
  * One of the input segment pairs is empty.



For automatic data splitting, Cloud Translation - Advanced API performs additional processing (see Dataset division):

  * After the dataset is uploaded, it removes segment pairs with identical source segments.

  * It randomly splits your data into three sets with a ratio of 8:1:1 (train:validation:test) before training.




### Dataset division

Your dataset of segment pairs is divided into three subsets, for training, validation and testing:

  * **Training Set**  
Most of your data should be in the training set. This is the data your model "sees" during training: it's used to learn the parameters of the model and calculate the weights of the connections between nodes of the neural network.

  * **Validation Set**  
The validation set, sometimes called the _dev_ set, is also used during the training process. During model learning, the framework uses the training set to train a suite of candidate models, and then uses the model's performance on the validation set to choose the best model generated. It uses the model's performance on the validation set to tune the model's hyperparameters, which are variables that specify the model's structure. If you used the training set to tune the hyperparameters, the model would end up overly focused on your training data. Using a somewhat novel dataset to fine-tune model structure means your model will generalize better.

  * **Test Set**  
The test set is not involved in the training process at all. After the model has completed its training entirely, the test set is used as an entirely new challenge for your model. The performance of your model on the test set is intended to give you a pretty good idea of how your model will perform on real-world data.




If you don't manually specify how your dataset is split between these functions as described in [Preparing your training data](https://docs.cloud.google.com/translate/docs/advanced/automl-prepare), and if your dataset contains fewer than 100,000 segment pairs, then Cloud Translation - Advanced API automatically uses 80% of your content documents for training, 10% for validating, and 10% for testing. If your data is larger than that, you must explicitly specify how it is split. Manual splitting gives you more control over the process, not only letting you determine the split percentages, but also letting you specify particular sets in which to include particular segment pairs.

## Importing data

After you've decided whether a manual or automatic split of your data is right for you, there are two ways to add data:

  * You can import data as a tab-separated values (TSV) file containing source and target segments, one segment pair per line.

  * You can import data as a [TMX file](https://www.ttt.org/oscarStandards/tmx/tmx13.htm), a standard format for providing segment pairs to automatic translation model tools (see [Prepare training data](https://docs.cloud.google.com/translate/docs/advanced/automl-prepare)) for more about the TMX format). If a TMX file contains invalid XML tags, Cloud Translation - Advanced API ignores them. If the TMX file contains XML or TMX errors, like if an end tag or `<tmx>` element is missing, Cloud Translation - Advanced API ends processing and returns an error if it skips more than 1024 invalid `' elements.




## Preliminary evaluation of your custom model

After your model is trained, you receive a summary of your model performance. Click the **Train** tab to view a detailed analysis. The BLEU score of your custom model and of the standard Google NMT model are shown in the **Train** tab, along with the BLEU score performance gain from using the custom mode.

The higher the BLEU score, the better translations your model can give you for segments that are similar to your training data. Scores in the range 30-40 are considered good. For a detailed explanation of BLEU scores, see [The BLEU translation quality metric BLEU](https://docs.cloud.google.com/translate/docs/bleu_scores).

There are other evaluation metrics that are often more reliable than the BLEU score. For information about those evaluation options, see [Evaluate translation models](https://docs.cloud.google.com/translate/docs/advanced/translation-model-valuation). 

### Debugging

Debugging a custom model is more about debugging the data than the model itself. If your model is not translating the way you intend, check your data to see where it can be improved.

### Testing

Even if your BLEU score looks okay, it's a good practice to check the model yourself to make sure its performance matches your expectations. If your training and test data are drawn from the same incorrect set of samples, the scores might be excellent even if the translation is nonsense. Add some examples as input on the **Predict** tab and compare the results from the custom model with the Google NMT base model. You might notice that your model comes up with the same predictions as the base model, especially on short segments or if you have a smaller training set, since the base model is already pretty good for a wide variety of use cases. In that case, try longer or more complex segments. However, if all of your segments come back identical to the predictions from the base model, it might indicate a data problem.

If there's a mistake that you're particularly worried about your model making (like a translation mistake that might be costly in money or reputation) make sure your test set or procedure covers that case adequately for you to feel safe using your model in everyday tasks.

## What's next

  * For details about how to create your own dataset and custom model, see [Prepare training data](https://docs.cloud.google.com/translate/docs/advanced/automl-prepare). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
