---
url: https://docs.cloud.google.com/translate/docs/bleu-scores/
title: The BLEU translation quality metric \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:06.951162+00:00
---

# The BLEU translation quality metric  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/bleu-scores/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# The BLEU translation quality metric

[BLEU](https://wikipedia.org/wiki/BLEU) (Bilingual Evaluation Understudy) is a metric for evaluating machine-translated text. A BLEU score is a number between zero and one that measures the similarity of the machine-translated text to a set of high-quality reference translations:

  * A score of 0 means that the machine-translated output has no overlap with the reference translation, which indicates a low quality of translation.
  * A score of 1 means there is perfect overlap with the reference translations, which indicates a high quality of translation.



## BLEU limitations

  * **BLEU is a Corpus-based Metric.** The BLEU metric performs poorly when used to evaluate individual sentences. Single sentences can get very low BLEU scores, even when they capture most of the meaning. Because n-gram statistics for individual sentences are less meaningful, BLEU is by design a corpus-based metric, where statistics are accumulated over an entire corpus when computing the score. The BLEU metric can't be factorized for individual sentences.

  * **BLEU makes no distinction between content and function words.** The BLEU metric doesn't distinguish content from function words. A dropped function word like _a_ gets the same penalty as if the name _NASA_ were erroneously replaced with _ESA_.

  * **BLEU is not good at capturing sentence meaning and grammaticality.** Dropping a single word like _not_ can change sentence polarity. Also, taking only n-grams into account with n≤4 ignores long-range dependencies, so BLEU often imposes only a small penalty for ungrammatical sentences.

  * **BLEU relies on normalization and tokenization.** Prior to computing the BLEU score, the reference and candidate translations are normalized and tokenized. The choice of steps in those processes significantly affect the final BLEU score.




## How to interpret BLEU scores

The following is a rough guideline suggesting how to interpret BLEU scores that are expressed as percentages, not decimals:

BLEU % Score | Interpretation  
---|---  
< 10 | Almost useless  
10 - 19 | Hard to get the gist  
20 - 29 | The gist is clear, but has significant grammatical errors  
30 - 40 | Understandable to good translations  
40 - 50 | High quality translations  
50 - 60 | Very high quality, adequate, and fluent translations  
> 60 | Quality often better than human  
  
The following color gradient can be used as a general scale [interpretation of the BLEU score](https://www.cs.cmu.edu/%7Ealavie/Presentations/MT-Evaluation-MT-Summit-Tutorial-19Sep11.pdf):

![General interpretability of scale](https://docs.cloud.google.com/static/translate/automl/docs/images/bleu_score_range.png)

## Mathematical details

Mathematically, the BLEU score is defined as:

$$ \text{BLEU} = \underbrace{\vphantom{\prod_i^4}\min\Big(1, \exp\big(1-\frac{\text{reference-length}} {\text{output-length}}\big)\Big)}_{\text{brevity penalty}} \underbrace{\Big(\prod_{i=1}^{4} precision_i\Big)^{1/4}}_{\text{n-gram overlap}} $$ 

with

\\[ precision_i = \dfrac{\sum_{\text{snt}\in\text{Cand-Corpus}}\sum_{i\in\text{snt}}\min(m^i_{cand}, m^i_{ref})} {w_t^i = \sum_{\text{snt'}\in\text{Cand-Corpus}}\sum_{i'\in\text{snt'}} m^{i'}_{cand}} \\]

where 

  * \\(m_{cand}^i\hphantom{xi}\\) is the count of i-gram in candidate matching the reference translation.
  * \\(m_{ref}^i\hphantom{xxx}\\) is the count of i-gram in the reference translation.
  * \\(w_t^i\hphantom{m_{max}}\\) is the total number of i-grams in candidate translation.



The formula consists of two parts: the brevity penalty and the n-gram overlap.

  * **Brevity penalty.** The brevity penalty penalizes generated translations that are too short compared to the closest reference length with an exponential decay. The brevity penalty compensates for the fact that the BLEU score has no [recall](https://developers.google.com/machine-learning/crash-course/glossary#recall) term.

  * **N-Gram overlap.** The n-gram overlap counts how many unigrams, bigrams, trigrams, and four-grams (_i_ =1,...,4) match their n-gram counterpart in the reference translations. This term acts as a [precision](https://developers.google.com/machine-learning/crash-course/glossary#precision) metric. Unigrams account for _adequacy_ while longer n-grams account for _fluency_ of the translation. To avoid overcounting, the n-gram counts are clipped to the maximal n-gram count occurring in the reference (\\(m_{ref}^n\\)).




### Example: Calculating \\(precision_1\\)

Consider this reference sentence and candidate translation:

**Reference:** `the cat is on the mat`  
**Candidate:** `the the the cat mat`

The first step is to count the occurrences of each unigram in the reference and the candidate. Note that the BLEU metric is case-sensitive.

Unigram | \\(m_{cand}^i\hphantom{xi}\\) | \\(m_{ref}^i\hphantom{xxx}\\) | \\(\min(m^i_{cand}, m^i_{ref})\\)  
---|---|---|---  
`the` | 3 | 2 | 2  
`cat` | 1 | 1 | 1  
`is` | 0 | 1 | 0  
`on` | 0 | 1 | 0  
`mat` | 1 | 1 | 1  
  
The total number of unigrams in the candidate (\\(w_t^1\\)) is 5, so \\(precision_1\\) = (2 + 1 + 1)/5 = 0.8.

### Example: Calculating the BLEU score

**Reference:** `The NASA Opportunity rover is battling a massive dust storm on Mars.`  
**Candidate 1:** `The Opportunity rover is combating a big sandstorm on Mars.`  
**Candidate 2:** `A NASA rover is fighting a massive storm on Mars.`

The preceding example consists of a single reference and two candidate translations. The sentences are tokenized prior to computing the BLEU score. For example, the final period is counted as a separate token.

To compute the BLEU score for each translation, we compute the following statistics.

  * **N-Gram Precisions.** The following table contains the n-gram precisions for both candidates.
  * **Brevity-Penalty.** The brevity-penalty is the same for candidate 1 and candidate 2 since both sentences consist of 11 tokens.
  * **BLEU-Score.** At least one matching 4-gram is required to get a BLEU score > 0\. Since candidate translation 1 has no matching 4-gram, it has a BLEU score of 0.

Metric | Candidate 1 | Candidate 2  
---|---|---  
\\(precision_1\\) (1gram) | 8/11 | 9/11  
\\(precision_2\\) (2gram) | 4/10 | 5/10  
\\(precision_3\\) (3gram) | 2/9 | 2/9  
\\(precision_4\\) (4gram) | 0/8 | 1/8  
Brevity-Penalty | 0.83 | 0.83  
**BLEU-Score** | **0.0** | **0.27**  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
