---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/preference-tuning/prepare-data/
title: Prepare preference tuning data for Gemini models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:38:59.040361+00:00
---

# Prepare preference tuning data for Gemini models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/preference-tuning/prepare-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Prepare preference tuning data for Gemini models Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to define a preference tuning dataset for a Gemini model.

## About preference tuning datasets

The preference tuning dataset is created to capture human preference using signals like thumbs-up-thumbs-down, pairwise, and scored feedback.

## Prepare customized preference tuning data

In this example:

An `example` is composed of input and a pair of `completions` fields.

The input includes `contents` and an optional `system_instruction`. The sum of maximum input and maximum completion token counts must be <= 128K.

The `contents` field is in the same [format used for supervised fine-tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning/prepare-data#example-contents). It supports multi-turn text data that needs to end with a user turn. It doesn't support multi-modal data.

The `completions` field is composed of a pair of completions and their scores. The pair must have one preferred completion and one dispreferred completion.

A `completion` is a single model turn that indicates the model response. The `score` field indicates whether the completion is preferred or dispreferred. The only possible value is zero or one. Zero represents the dispreferred completion, while one is the preferred completion.

We only train on the `completions` turn for each `example`.

## Dataset example for Gemini
    
    
    {
      "system_instruction": {
        "parts": [
          {
            "text": "You are a chat bot."
          }
        ]
      },
      "contents": [
        {
          "role": "user",
          "parts": [
            {
              "text": "What is my favorite fruit?"
            }
          ]
        }
      ],
      "completions": [
        {
          "score": 1,
          "completion": {
            "role": "model",
            "parts": [
              {
                "text": "Apple! Apple! Apple!"
              }
            ]
          }
        },
        {
          "score": 0,
          "completion": {
            "role": "model",
            "parts": [
              {
                "text": "Your favorite fruit is apple."
              }
            ]
          }
        }
      ]
    }
    

## What's next

  * [Tune Gemini models by using preference tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/preference-tuning/use).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
