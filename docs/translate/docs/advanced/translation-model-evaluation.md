---
url: https://docs.cloud.google.com/translate/docs/advanced/translation-model-evaluation/
title: Evaluate translation models \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:00.063092+00:00
---

# Evaluate translation models  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/translation-model-evaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Evaluate translation models

The best way to evaluate a translation model is to use the Gen AI evaluation service. However, for custom NMT models, you can also generate a BLEU score directly on Google Cloud console that can help in evaluating the mode, with some limitations.

## Use Gen AI evaluation service

The [Gen AI evaluation service](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview) offers the following translation task evaluation metrics:

  * [MetricX](https://github.com/google-research/metricx)

  * [COMET](https://huggingface.co/Unbabel/wmt22-comet-da)

  * [BLEU](https://docs.cloud.google.com/translate/docs/bleu_scores)




MetricX and COMET are pointwise model-based metrics that have been trained for translation tasks. You can evaluate the quality and accuracy of translation model results for your content, whether they are outputs of NMT, TranslationLLM, or Gemini models.

You can also use Gemini as a judge model to evaluate your model for fluency, coherence, verbosity, and text quality in combination with MetricX, COMET, or BLEU.

  * [MetricX](https://github.com/google-research/metricx) is an error-based metric developed by Google that predicts a floating point score between 0 and 25 to represent the quality of a translation. MetricX is available both as a referenced-based and as a reference-free (QE) method. When you use this metric, a lower score is better because it means there are fewer errors.

  * [COMET](https://huggingface.co/Unbabel/wmt22-comet-da) employs a reference-based regression approach that provides scores ranging from 0 to 1, where 1 signifies a perfect translation.

  * [BLEU](https://docs.cloud.google.com/translate/docs/bleu-scores) (Bilingual Evaluation Understudy) is a [computation-based metric](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/eval-python-sdk/determine-eval#computation-based-metrics). A BLEU score indicates how similar candidate text is to reference text. The closer a BLEU score value is to one, the closer the translation is to the reference text.

BLEU scores are best for comparisons in one language or body of data. For example, an English to German BLEU score of 50 is not comparable to a Japanese to English BLEU score of 50. Many translation experts use model-based metric approaches, which have higher correlation with human ratings and are more granular in identifying error scenarios.




To learn how to run evaluations for translation models using Gen AI evaluation service, see [Evaluate a translation model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/eval-python-sdk/run-evaluation#translation).

## Evaluate a custom NMT model on Google Cloud console

After you have trained a new custom NMT model, you can use your `TEST` set to evaluate the model's quality and accuracy directly on the Google Cloud console. The model quality will be expressed using a [BLEU](https://docs.cloud.google.com/translate/docs/bleu-scores) score, which indicates how similar the candidate text is to the reference text. If the score is low, consider adding more (and more diverse) training segment pairs. After you adjust your dataset, train a new model by using the improved dataset.

Evaluating on the Google Cloud console only supports BLEU scores. To evaluate your translation model using model-based metrics, you have to use the Gen AI evaluation service.

## Get the model's BLEU score

  1. Go to the Cloud Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. From the navigation menu, click **Models** to view a list of your models.

  3. Click the model to evaluate.

  4. Click the **Train** tab to see the model's evaluation metrics such as its BLEU score.




## Test model predictions

By using the Google Cloud console, you compare translation results for your custom model against the default NMT model.

  1. Go to the Cloud Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. From the navigation menu, click **Models** to view a list of your models.

  3. Click the model to test.

  4. Click the **Predict** tab.

  5. Add input text in the source language field.

  6. Click **Translate**.

The translation results for the custom model and general NMT model are shown.




## Evaluate and compare models with a new test set

From the Google Cloud console, you can reevaluate existing models by using a new set of test data. In a single evaluation, you can include up to five different models and then compare their results. Upload your test data to Cloud Storage as a tab-separated values (TSV) or as a [Translation Memory eXchange](https://wikipedia.org/wiki/Translation_Memory_eXchange) (TMX) file. Your model is evaluated against the test set and an evaluation score is produced.

You can optionally save the results for each model as a TSV file in a Cloud Storage bucket, where each row has the following format:
    
    
    Source segment _tab_ Model candidate translation _tab_ Reference translation
    

  1. Go to the Cloud Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. From the navigation menu, click **Models** to view a list of your models.

  3. Click the model to evaluate.

  4. Click the **Evaluate** tab.

  5. In the **Evaluate** tab, click **New Evaluation**.

  6. Select the models that you want to evaluate and compare, and then click **Next**.

The current model must be selected, and Google NMT is selected by default, which you can deselect.

  7. Specify a name for the **Test set name** to help you distinguish it from other evaluations, and then select your new test set from Cloud Storage.

  8. Click **Next**.

  9. To export predictions, specify a Cloud Storage destination folder.

  10. Click **Start evaluation**.

An evaluation score in a table format is presented in the console after the evaluation is done. You can run only one evaluation at a time. If you specified a folder to store prediction results, TSV files will be written to that location. These files will be named with the associated model ID with the test set name appended. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
