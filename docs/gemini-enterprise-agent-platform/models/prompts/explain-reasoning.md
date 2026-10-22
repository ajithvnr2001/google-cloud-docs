---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/explain-reasoning/
title: Instruct the model to explain its reasoning \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:25:34.625119+00:00
---

# Instruct the model to explain its reasoning  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/explain-reasoning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Instruct the model to explain its reasoning Stay organized with collections  Save and categorize content based on your preferences. 

When you tell the model to explain its reasoning, the model responds with the steps that it employs to solve the problem. Going through this process can sometimes improve accuracy and nuance, especially for challenging queries.

The reasoning steps are included as part of the response. To parse out the reasoning steps from the answer that you're looking for, you can specify an output format by using XML or other separators.

## Examples

For example, suppose you're writing a cooking blog and you want the model to tell you how readers might interpret different parts of the blog. If you don't instruct the model to explain its reasoning, the response from the model might not be as useful as you'd like:

No reasoning  
---  
**Prompt:**
    
    
        **What is the most likely interpretation of this sentence?**
        The sentence: "The chef seasoned the chicken and put it in the oven because it looked pale."
        

**Response:**
    
    
        The chef seasoned the chicken and put it in the oven because it lacked color and needed cooking.
        

(gemini-pro)  
  
While you learned about how the model predicts readers might interpret the sentence, it might be useful for you to understand more about the specific predictions that the model made to produce the response. As demonstrated in the following example, the quality of the response might also improve:

Explain reasoning  
---  
**Prompt:**
    
    
        **What is the most likely interpretation of this sentence? Explain your reasoning**
        The sentence: "The chef seasoned the chicken and put it in the oven because it looked pale."
        

**Response:**
    
    
          Interpreting "The chef seasoned the chicken and put it in the oven because it looked pale."
    
          The most likely interpretation is that the chef seasoned the chicken to add flavor and color, then put it in the oven to cook it.
    
          Here's the reasoning:
    
          - Seasoning is typically used to enhance the flavor of food. Chefs often use spices, herbs, and other ingredients to make their dishes more appealing.
          - "Pale" suggests the chicken lacked visual appeal before being seasoned. This could imply it was unseasoned or simply lacking color from spices.
          - Putting the chicken in the oven is a common cooking method. The sentence implies the chef's intention is to cook the chicken, not just season it.
    
          Therefore, the chef's actions are likely aimed at both improving the taste and appearance of the chicken through seasoning and then cooking it in the oven.
        

(gemini-pro)  
  
Another technique you can use to improve the model's response is to instruct the model to think step-by-step and explain it's reasoning. This requires the model to break down the input into steps and provide the reasoning its using to solve the problem:

Think step-by-step  
---  
**Prompt:**
    
    
        **What is the most likely interpretation of this sentence? Think step by step and print out
        the thinking process.
    
        Please output in JSON format with final answer in 'answer', and thinking steps in 'think' fields.**
        The sentence: "The chef seasoned the chicken and put it in the oven because it looked pale."
        

**Response:**
    
    
        {
          "answer": "The chef seasoned the chicken to enhance its flavor and put it in the oven to cook it because it appeared to be undercooked.",
          "think": [
            {
              "step": 1,
              "thought": "The chef seasoned the chicken. This suggests that the chef is preparing the chicken for cooking."
            },
            {
              "step": 2,
              "thought": "The chef put the chicken in the oven. This indicates that the chef is cooking the chicken."
            },
            {
              "step": 3,
              "thought": "The sentence states that the chicken looked pale. Pale chicken is often undercooked."
            },
            {
              "step": 4,
              "thought": "Combining these observations, it is most likely that the chef seasoned the chicken to enhance its flavor and put it in the oven to cook it because it appeared to be undercooked."
            }
          ]
        }
        

(gemini-pro)  
  
By prompting the model to print out its thinking process, the model generated a more thorough response and you learned more about how it generated that response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
