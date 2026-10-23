---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-iterate-googleapis-translate/
title: Use Google Translate in a for-in loop \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:58.586310+00:00
---

# Use Google Translate in a for-in loop  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-iterate-googleapis-translate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Use Google Translate in a for-in loop Stay organized with collections  Save and categorize content based on your preferences. 

Uses the Cloud Translation API connector in a for-in loop.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Iteration](https://docs.cloud.google.com/workflows/docs/reference/syntax/iteration)



## Code sample

### YAML
    
    
    - init:
        assign:
          - textAndSourceLang:
              "Hello": "en"
              "Ciao": "it"
              "Auf wiedersehen": "de"
              "Goodbye": "en"
              "Bonjour": "fr"
              "lkajshflkj": "unknown"
          - allowedSourceLang: ["en", "de", "it", "fr"]
    - translateToFrench:
        for:
          value: text
          in: ${keys(textAndSourceLang)}
          steps:
            - verifySource:
                switch:
                  - condition: ${not(textAndSourceLang[text] in allowedSourceLang)}
                    next: continue
                  - condition: ${textAndSourceLang[text] == "fr"}
                    next: skipFrenchTranslation
            - translate:
                call: googleapis.translate.v2.translations.translate
                args:
                  q: ${text}
                  target: "fr"
                  format: "text"
                  source: ${textAndSourceLang[text]}
                result: translation
            - getTranslation:
                assign:
                  - translated: ${translation.data.translations[0].translatedText}
                next: print
            - skipFrenchTranslation:
                assign:
                  - translated: ${text}
            - print:
                call: sys.log
                args:
                  text: '${"Original: " + text + ", Translation: " + translated}'

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
