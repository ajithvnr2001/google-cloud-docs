---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-autoeval-metrics/
title: Summarization automatic evaluation metrics \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:21.817520+00:00
---

# Summarization automatic evaluation metrics  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-autoeval-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Summarization automatic evaluation metrics Stay organized with collections  Save and categorize content based on your preferences. 

Summarization automatic evaluation (autoevaluation) uses generative AI to assess the quality of [AI-generated summaries](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections) based on accuracy, completeness, and adherence.

Sometimes, adherence and completeness scores display **N/A**.

  * Adherence only evaluates summaries that use custom sections. If a summary uses prebuilt sections, the score is **N/A**.
  * Completeness evaluates only noncategorical summaries with free-form text. If a summary uses categorical values, the score is **N/A**.



## Accuracy

Accuracy measures how closely a summary aligns with the factual details of the conversation transcript. For each summary, the autoevaluation determines a correctness percentage, along with a corresponding justification. A low accuracy score means there are factual problems in the summary.

Accuracy results look like the following:
    
    
    {
      "decomposition": [
        {
            "point": "The customer wants to cancel their subscription.",
            "accuracy": "This is accurate. The customer calls to get support of cancelling their subscription.",
            "is_accurate": true
        },
        {
            "point": "The customer asks about a $30 credit.",
            "accuracy": "This is inaccurate. The customer mentioned $10.",
            "is_accurate": false
        }
      ]
    }

  * Each `point` in the preceding example is a decomposed part of the summary. The binary parameter `is_accurate` displays the accuracy evaluation result. The `accuracy` parameter provides the justification.



## Adherence

Summarization autoevaluation applies a set of questions to the provided summary. The autoevaluation uses these questions and the conversation transcript to assess the summary's compliance with each instruction. However, summarization autoevaluation relies on Gemini, which might not accurately verify grammatical instructions. So summarization autoevaluation might not accurately assess whether a summary adheres to grammatical instructions.

A low adherence score means that summary fails to adhere to the instructions provided in the summary section's definition. Only summaries that used custom sections can generate an adherence score.

For adherence, summarization autoevaluation recognizes the following two types of summary tasks:

  * **Categorical summaries** : Provide a categorical value defined in the instructions. For example, the instructions ask for a _Sunny_ or _Cloudy_ response. Autoevaluation checks whether the summary provided only _Sunny_ or _Cloudy_ without descriptive text.
  * **Noncategorical summaries** : Provide free form text. Autoevaluation checks whether a noncategorical summary follows the instructions defined in the task description.



Adherence results look like the following:
    
    
    (Categorical):
    {
      "rubrics": [
        "question": "Does the summary follow the instruction and return only one of the allowed categorical values?",
        "reasoning": "The summary is not a categorical value. It contains descriptive text instead of providing only one of the allowed categorical values.",
        "is_addressed": "False"
      ]
    }
    (Noncategorical):
    {
      "rubrics": [
        {
          "question": "Does the summary follow the instruction 'State the product name being returned'?",
          "reasoning": "Summary followed instruction. It correctly stated the product name, for example: 'return the \\'Stealth Bomber X5\\' gaming mouse'.",
          "is_addressed": "True"
        }
      ]
    }

  * Each question is derived from the provided summary section definition. The binary parameter `is_addressed` displays the adherence evaluation result. The `reasoning` parameter provides a justification.

  * If any questions aren't aligned with your goal, the summary section definition of that goal was unclear. You can understand the issue and improve your section definitions.




## Completeness

Based on the instructions in an AI-generated summary's section definition, summarization autoevaluation applies rubrics to assess summary completeness. A low score means the summary lacked important information from the transcript.

The following is an example of completeness results:
    
    
    [
      {
            'question': "Does the summary follow 'Describe the specific actions the agent took to assist the customer with their issue  or request'?",
            'content_list': [
        {
            'transcript_content': 'The agent provided the customer with the arrival window for the ABC appointment.',
            'related_content_from_summary': 'The agent, Robyn, provided the customer with the arrival window for the ABC appointment, which is from 01:30 PM to 2:45 PM.',
            'is_covered': 'True'
        },
        {
            'transcript_content': 'The agent clarified that the arrival window information is sent via text message.',
            'related_content_from_summary': 'The agent also clarified that the arrival window information is sent via text message',
            'is_covered': 'True'
        },
        {
            'transcript_content': "The agent confirmed the phone number is 123-456-7890.",
            'related_content_from_summary': "and confirmed the phone number is 123-456-7890.",
            'is_covered': 'True'
        } ]
      },
      {
            'question': "Does the summary follow 'Identify any dates explicitly mentioned by the agent or the customer'?",
            'content_list': [
        {
            'transcript_content': 'The ABC appointment is on June 2nd.',
            'related_content_from_summary': '',
            'is_covered': 'False'
        } ]
      },
      {
            'question': "Does the summary follow 'Identify the brand and any relevant specifications mentioned in the conversation'?",
            'content_list': [
        {
            'transcript_content': 'The appointment is for a Google Pixel.',
            'related_content_from_summary': '',
            'is_covered': 'False'
        } ]
      },
      {
            'question': "Does the summary follow 'Describe any updates the agent made, such as price, address, or order updates'?",
            'content_list': []
      },
      {
            'question': "Does the summary follow 'Extract the customer's order number and include it in the summary'?",
            'content_list': []
      }
    ]

The preceding example presents the following scenarios:

  * If the summary covers the related content from the transcript, the binary parameter `is_covered` is set to `True`.
  * If the summary doesn't cover the related content from the transcript, the `related_content_from_summary` parameter comprises an empty string signifying that the summary didn't extract the relevant points. This, in turn, reduces the final score and that rubric's completeness score. Also, the binary parameter `is_covered` is set to `False`.
  * If no content relates to the question in the transcript, then the `content_list` parameter comprises an empty list, which doesn't penalize the summary. The final aggregated score doesn't include this case.



Each question in the example is derived from the provided task description. The relevant information from the transcript is included as the value of the `transcript_content` parameter. The binary parameter `is_covered` displays the completeness result of this particular point and `related_content_from_summary` displays the proof. If any of the questions aren't aligned with your goal, your summary's section definition was unclear. Understand the issue and improve your section definition.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
