---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections-best-practices/
title: Best practices: Summarization with custom sections \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:57.051448+00:00
---

# Best practices: Summarization with custom sections  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Best practices: Summarization with custom sections Stay organized with collections  Save and categorize content based on your preferences. 

Summarization with custom sections uses an LLM to summarize customer service conversations. With this feature, summaries are generated after the model takes in the conversations and custom sections, which are parts of text prompts that define the task the model performs.

This feature provides six predefined sections similar to those found in the [summarization V2 baseline](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections), from which you can select and use. You can also write your own summarization task definitions in custom sections. Both predefined sections and custom sections are described in a generator.

## Write section definitions

A section minimally consists of a name and a value, defined as follows:

  * **Section name** : Make this a friendly-sounding name for section management. It must be different from any predefined section name. Use a meaningful name that reflects the task objective described in the section definition.

  * **Section definition** : The value consists of a task description that defines a summarization task or subtask, telling the model to generate a specific type of summary.




For example, a custom section that ensures the summary uses certain terminology could look like the following:
    
    
    section name: custom_action
    section definition: Based on the conversation, summarize what the agent does to help the customer. Use "representative" in place of "agent" in the summary.
    

To generate more precise and accurate summaries, use the recommendations that follow when writing custom section definitions.

### Clear instructions

The section definition should provide specific descriptions of the details you want included in the summary. Specify the context, format, and style of the summary, including any specific terminology and sentence structures you want to see. For example, you can specify that a summary must be written in the present tense as follows:
    
    
    Recommended: Summarize what the customer needs help with or has questions about in the past tense. For example, The sentence "The customer wants to cancel an order." isn't in the past tense as indicated by the verb "wants". The sentence "The customer wanted to cancel an order." is in the past tense.
    Not recommended: Summarize customer issues in the past tense.
    

When your section definition is specific, summarization with custom sections is more likely to generate the style and format that you're looking for.

### Emphasis

You can use capital letters to emphasize important information within your section definition. If you need a summary to include some information but the model ignores that information within your section definition, you can have a keyword written in all capital letters. For example, to ensure that the order number is part of the summary, the following section definition emphasizes the verb _include_.
    
    
    Recommended: Summarize what the customer needs help with or has questions about. If there is an order number mentioned in the conversation, INCLUDE the order number.
    Not recommended: Summarize what the customer needs help with or has questions about with order numbers.
    

### Guided reasoning

Breaking down complex tasks into a sequence of subtasks can help the model to parse the entire task accurately. For example, to ensure summarization with custom sections can accurately determine whether or not a customer service issue was resolved, add a subtask at the beginning of the section definition to contextualize the issue.
    
    
    Recommended: First explain what actions are taken to handle the customer issue, then determine whether the issue is resolved.
    Not recommended: Determine whether the issue is resolved.
    

### Language choices

Write your section definition in the same language as the summary. For example, write section definitions in French to generate a summary in French.
    
    
    Recommended: Résumez ce pour quoi le client a besoin d'aide ou sur quoi il a des questions.
    Not recommended: Summarize what the customer needs help with or has questions about.
    

### Few-shot examples

If your custom section definitions don't generate the summaries you want to see, you can add up to 10 examples that demonstrate how to perform the task. Such examples include a conversation transcript and an expected summary. You don't need to provide expected summaries for predefined sections. These few-shot examples illustrate the precise vocabulary, format, style, and context for what you want to see in an generated summary.

To effectively illustrate the types of summaries you want to see, try using a diverse selection of few-shot examples to cover all possible answers for your task. For the following task, answers may or may not contain an order number, and each example covers one case.

Custom section:
    
    
    section_name: custom_situation
    section_definition: summarize what the customer needs help with or has questions about. If there is an order number in the conversation, add the order number after "Order Number:" at the end.
    

Few-shot example 1:
    
    
    [Conversation transcript]
    CUSTOMER: cancel order.
    AGENT: Hi, this is Joe. I can definitely help with order cancellation. Can you share the order number?
    CUSTOMER: Z12345
    AGENT: Thanks. Give me a second to pull the order.
    AGENT: May I know why you want to cancel the order?
    CUSTOMER: I ordered the wrong color.
    AGENT: Noted.
    AGENT: I have canceled the order for you. You should receive a confirmation email soon.
    CUSTOMER: Thanks.
    
    [Expected summary]
    Customer wants to cancel an order because they ordered the wrong color. Order Number: Z12345
    

Few-shot example 2:
    
    
    [Conversation transcript]
    AGENT: Hi this Ralph. How can I help you?
    CUSTOMER: I have some questions about the latest bill.
    AGENT: Sure, I can help you with that.
    AGENT: Can I have your name and phone number?
    AGENT: Are you still there?
    
    [Expected summary]
    Customer calls to ask about the latest bill.
    

Few-shot examples are also useful when the model misinterprets information within the conversation transcript. For example, using the same preceding custom section, if the model doesn't recognize "order ID" as a synonym for "order number," then you might need to add an example like the one here.
    
    
    [Conversation transcript]
    CUSTOMER: order status
    CUSTOMER: order ID X12345
    AGENT: Thank you for contacting us
    
    [Expected summary]
    Customer wants to check order status Order Number: X12345
    

### Start with the basics and iterate

Section definition design uses an iterative process to get optimal results from summarization. Start with basic definitions. As you learn what's needed to improve your summary, add more elements. The following list includes three possible iteration steps to improve a summary:
    
    
    1. Summarize agent actions.
    2. Summarize what actions the agent took to help the customer.
    3. Summarize what actions the agent took to help the customer. Exclude actions relevant to authentications.
    

The first iteration generates a summary. The second will generate one that's relevant to customer service. The last summary is relevant to customer service and excludes authentication actions. Each iteration generates a more accurate and precise summary.

## Main use cases

Here are some examples of use cases of custom sections.

### Vocabulary

Customize the terminology used in a summary. For example, the default names of participants are customer and agent, you can specify customized names of participants for your tasks.
    
    
    Summarize what the customer needs help with or has questions about. Use "user" in place of "customer".
    

### Format and style

Customize the format and style of a summary. For example, you can specify bullet points for extracted entities:
    
    
    Extract entities and output name/value pairs in bullet points. For example:
    - {entity name 1}: {entity value 1}
    - {entity name 2}: {entity value 2}
    ...
    Leave it blank if there are no entities.
    

Another example is to format dates:
    
    
    Summarize what the customer needs help with or has questions about. Format dates as "MM/DD/YYYY" in the summary.
    

### Rewrite

Rewrite the predefined section to meet your specific requirements. For example, you can select the predefined section "action" and use customized names of participants:
    
    
    Rewrite "action" and use "representative" in place of "agent".
    

## What's next

For more information on accessing the feature, see [Summarization with custom sections](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
