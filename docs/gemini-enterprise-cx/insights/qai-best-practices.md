---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/qai-best-practices/
title: Quality AI best practices \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:22.663467+00:00
---

# Quality AI best practices  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/qai-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Quality AI best practices Stay organized with collections  Save and categorize content based on your preferences. 

This document outlines Google's recommendations for how best to use Quality AI. Following the guidelines in this document will ensure that Quality AI provides the most accurate and useful information possible for your business needs.

## Scorecards

Scorecards provide access to agent performance metrics and detailed instructions for answering questions about a conversation. You must enter your conversation data, questions, and possible answer options, along with instructions for how to interpret those answers. For best results, use the **Scorecards** page in the Quality AI console to upload your example conversations.

Scorecards provide one way to group your questions and view separate scores for each grouping. Create multiple scorecards with different questions in each, to evaluate conversations against different criteria. You can then view quality and conversation scores for each scorecard to evaluate an agent based on separate criteria.

### Conversation data

Conversation data are transcripts of either voice or chat conversations with personally identifiable information redacted. Upload at least 2,000 conversations for each business unit or call center.

You can also upload audio recordings of voice conversations. For best results, record audio using the following specifications:

  * Two channels
  * 16,000 Hz sampling rate (or 8,000-48,000 Hz)
  * Lossless encoding: FLAC or LINEAR16
  * Lossless encoding for WAV audio files: LINEAR16 or MULAW



The metadata for audio recordings of a voice call should include the following information:

  * Channel labels to identify the agent and customer
  * Agent ID, name, location, team, and CSAT
  * Audio language as a BCP-47 language tag, such as en-US

**Note:** Each conversation is automatically evaluated against a scorecard.

### Questions

Within each scorecard, the questions and instructions for answering them provide valuable information for Quality AI to evaluate conversations and agent performance. To maximize the accuracy of automatic evaluations, write questions and instructions with the following concepts in mind:

  * **Clarity** : Write questions that are clear and a human can understand.
  * **Specificity** : Add answer options and instructions that are as specific as possible.
  * **Details** : Include instructions that provide enough details for a human to confidently and reliably evaluate the conversations.
  * **Examples** : Quality AI is even more accurate if you provide examples from real conversations that illustrate each answer to your questions.



Questions can take a variety of forms. The following are some useful question templates:

  1. "Did the agent…?" with a specific action. This format indicates that the evaluator must look for something the agent said. 
  2. "Did the customer…?" with a specific action. This format indicates that the evaluator must look for something the customer said. 
  3. Beginning with question words such as _what_ or _why_ encourages evaluation of the whole conversation.



#### Questions with multiple answers

Users often write questions with only yes and no answers. However, a question might not apply to the conversation, which warrants **N/A**.

Alternatively, the question could be interpreted as yes or no in a variety of circumstances, which leads to inconsistent responses with only two options. Including questions that require other types of answers gives the AI model a greater depth of understanding of the conversation.

#### Acoustic analysis

Quality AI evaluates conversation transcripts and cannot perform acoustic analysis. Exclude questions that require acoustic analysis. For example, neither a person nor Quality AI can answer the question "Did the agent use a greeting with an upbeat tone of voice?" solely by reading a transcript of the conversation.

### Tags

The optional tag provides a smaller category to group related questions together. For a single conversation, Quality AI calculates an overall conversation score. You can group questions using one of three tags: business, customer, or compliance. For each tag, Quality AI also calculates a score that includes only questions with that tag applied.

### Instructions

Instructions define how each answer is interpreted; so instructions must be specific and leave no room for interpretation. The definition ensures that each evaluation of a conversation provides the same answer.

#### Format

Include a brief description of the question's purpose followed by a description of the criteria for each possible answer choice. This means you must define the precise circumstance in which someone would give each answer choice.

For example, the following instructions apply to a yes/no question that asks, "Did the agent address the customer's primary concern before cross-selling?"

Instructions:

The purpose of this question is to understand if the agent addressed the customer's primary concern before trying to sell an additional product. This creates a more positive experience for our brand.

  * Score "Yes" if the agent resolved the primary issue and then attempted sales. Example: "I just updated your account information. I see that you marked your smart home device as broken. Would you like to order a replacement?"

  * Score "No" if the agent tried to sell a product before resolving the primary issue. Example: "Before I update your account information, I see that you bought a laptop from us five years ago. Do you want to try our new model?"

  * Score "N/A" if there was no sales attempt.




### Trace data

To improve QAI scorecard accuracy, enable data tracing. Tracing captures system events and metadata during a customer service conversation. System events include tool calls and Dialogflow intents. Tracing specifically enhances the accuracy for tool-dependent questions in QAI scorecards.

### Answer types

The answer type depends on the structure of the question. This section provides suggestions to help you get started, but not an exhaustive list of uses.

#### Yes/No

Yes/No is the most common answer type because you can quickly evaluate these questions, and the answers are often more intuitive than other answer types. Questions that benefit from a yes/no answer type often begin with "Did..." and ask if a specific action took place. These questions can also be written as true or false questions.

In example conversations, yes/no answers are recorded as a true or false value with the following formats:

  * A Yes answer is `true`.
  * A No answer is`false`.



#### Numbers

Numerical answers are useful for questions that ask for a count of something, a dollar amount, or ask you to rate something on a scale. Questions that benefit from this answer type often begin with "How many...", "How much...", or "On a scale of..." and ask you to determine a single answer.

In example conversations, numeric answers have the following format:

  * A 40.5 answer is `40.5`.



#### Text

Text answers would require the most work from a human annotator. Questions that benefit from text answers often begin with question words, such as "What..." or "Why..." and often require evaluation of the conversation as a whole. Text answers encourage more variety in the responses, so the instructions must clearly explain how to interpret the question and when to assign each answer choice.

In example conversations, text answers have the following format:

  * An answer of Concluded is `"CONCLUDED"`.



#### Assign scores

When you create a question, you can assign a numerical score to each answer choice. These scores represent the importance of each answer choice for the overall [conversation score calculation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/qai-basics#conversation_scores).

A useful range for answer choice scores is 0-10. This range provides some variation for specificity and is comparable to a percentage. An answer choice with a score of 0 has no effect on the conversation score calculation. An answer choice with a score of 10 has the most impact on the conversation score. In other words, the answer choice with a 10 raises the conversation score more than any answer choice with a lower score. An answer choice with a score of 5 raises the conversation score by half as much as the answer with 10.

#### N/A

Click the checkbox to enable **N/A** as an answer choice when a question doesn't apply to a conversation. When Quality AI chooses N/A as the answer, the question is removed from the conversation score calculation.

### Example scorecard inputs

The following examples illustrate how to add all the information needed for a useful scorecard. Each scorecard requires the following information:

  * Any questions about the conversation.
  * Instructions for interpreting the question and defining each answer choice.
  * Tracing data.
  * Answer type (can be text, number, or yes/no).
  * Answer choices that define the possible answers based on answer type (can be yes and no, a list of numbers, or some text responses).
  * Score to set the points earned for each answer choice. The maximum score for a single question is determined by the highest score among all the answer choices.



You can include the following to help organize the questions on your scorecard, but they aren't required:

  * Tag to group the questions into categories (can be business, customer, or compliance).



#### Example 1

  * **Question** : What was the outcome of the conversation?
  * **Tag** : Customer
  * **Instructions** : The goal of any conversation is to reach a resolution or outcome that falls into one of four possible categories: concluded, transferred, redirected, or escalated.

    * Concluded conversations are those that have been successfully resolved and don't require any further action. The customer's issue has been addressed, and the conversation has been concluded.

    * Transferred conversations are those that need to be handled by a different department or agent. The customer might have been transferred to a specialist who can better assist them with their issue.

    * Redirected conversations are those that need to be handled by a different channel. For example, a customer might have been redirected from a phone call to an online chat session.

    * Escalated conversations are those that require the involvement of a manager or supervisor. The customer might have been escalated due to the severity of their issue or because they are not satisfied with the resolution offered by the initial agent.

  * **Answer type** : Text

Answer choice | Score  
---|---  
Concluded | 1  
Transferred | 1  
Redirected | 1  
Escalated | 0  
  
Add N/A as an answer choice. If selected, the question won't be included in the total score calculation.




#### Example 2

  * **Question** : On a scale of 0-5, how effective was the communication between the agent and the customer?
  * **Tag** : Business, Compliance, Customer
  * **Instructions** : Scale and Criteria

    * 0, Extremely Poor: No communication or complete misunderstanding. Offensive, abusive, or harmful language. Total lack of respect or empathy.

    * 1, Very Poor: Significant communication difficulties. Frequent interruptions or talking over each other. Minimal effort to understand or connect. Dismissive or disrespectful behavior.

    * 2, Poor: Some communication challenges. Occasional misunderstandings or lack of clarity. Limited engagement or interest. Occasional disrespect or insensitivity.

    * 3, Average: Basic communication achieved. Some effort to understand and be understood.Moderate level of engagement and connection. Generally respectful, but with room for improvement.

    * 4, Good: Clear and effective communication. Active listening and understanding. Meaningful engagement and connection. Mutual respect and empathy demonstrated.

    * 5, Excellent: Exceptional communication and understanding. Deep engagement and connection. Strong sense of collaboration and mutual support. High levels of respect, empathy, and compassion.

Factors to consider when evaluating:

    * **Clarity** : Was the communication clear and easy to understand?

    * **Understanding** : Did participants demonstrate active listening and understanding of each other's perspectives?

    * **Engagement** : Were participants actively engaged in the conversation and interested in what others had to say?

    * **Respect** : Was there mutual respect and consideration shown throughout the conversation?

    * **Empathy** : Did participants demonstrate empathy and understanding of each other's feelings?

    * **Collaboration** : Was there a sense of collaboration and teamwork, or did participants feel like they were competing against each other?

    * **Outcome** : Did the conversation achieve its intended goals or lead to a positive outcome?

Remember: Context matters. Consider the context and purpose of the conversation. What might be appropriate in one setting might not be in another.

Subjectivity: Evaluation can be subjective. Different people might have slightly different interpretations of the same conversation.

Focus on improvement: Use evaluations as a tool for learning and improvement rather than just a way to judge or criticize.

This framework provides a basic guide for evaluating conversations, but you can adapt and adjust the criteria based on your specific needs and goals.

  * **Answer type** : Number

  * **Answer choices and scores** :

Answer choice | Score  
---|---  
0 | 0  
1 | 1  
2 | 2  
3 | 3  
4 | 4  
5 | 5  



Add N/A as an answer choice. If selected, the question won't be included in the total score calculation.

#### Example 3

  * **Question** : Did the representative (agent) greet the customer with a proper opening?
  * **Tag** : Customer
  * **Instructions** : The representative (agent) should always start the conversations with a proper opening, greeting. This serves as a crucial step in establishing a positive and professional rapport with the customer. The opening should be warm, friendly, and welcoming, setting a tone that makes the customer feel valued and respected. The representative (agent) should also ensure that the greeting is appropriate for the context and the customer's cultural background. By starting the conversation with a proper opening and greeting, the representative can create a positive first impression, build rapport, and lay the foundation for a successful interaction with the customer.
  * **Answer type** : Yes/No
  * **Answer choices and scores** : 

Answer choice | Score  
---|---  
"Yes" | 1  
"No" | 0  



Add N/A as an answer choice. If selected, the question won't be included in the total score calculation.

## Add example conversations

Example conversations are useful for clarifying question interpretation. Calibrating and customizing the AI model requires example conversations with answers assigned for each question. The AI model learns from real conversation data, so take examples from your existing conversations in Customer Experience Insights. If you don't provide any example conversations, Quality AI uses a foundational model which doesn't know the expected answers for your questions.

To improve the AI model's performance, include at least the following:

  * 100 example conversations per question
  * 40 example conversations per answer choice



If you provide fewer than 100 example conversations for a single question, the AI model won't learn how to accurately score that specific question. Your example conversations are stored and the model learns after you have enough. A single conversation can teach the model how to score multiple questions, and you can further improve scoring accuracy for any question by adding more example conversations.

For each question in your scorecard, include a percentage of conversations to illustrate each answer choice. The following example shows how many conversations you might include to illustrate two possible answer choices. This specific split isn't required.

If a question on a scorecard is "Did the agent exhibit empathy towards the customer?" and the response to that question can be yes or no, include both of the following:

Question | Possible answers | Share of conversations  
---|---|---  
Did the agent exhibit empathy towards the customer? | "Yes" | 75%  
| "No" | 25%  
  
### Example conversation format

Example conversations minimally must include identifiers for each conversation, scorecard, and question as well as the expected answer. Your example conversations can also include the answer choices, scores, and instructions. Example conversations are uploaded as the [FeedbackLabel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.feedbackLabels) resource. For information about editing example conversations using the API, see [Setup Guide](https://docs.cloud.google.com/gemini-enterprise-cx/insights/qai-setup-guide).

#### CSV

You must upload example conversations in a CSV file. The first line of your CSV file must be the header, and the file must contain the following categories:

  * **ConversationId**
  * **QaScorecardId**
  * **QaQuestionId**
  * **QaAnswerLabel** or individualized fields such as **QaAnswerScore** and **QaAnswerValue**



Quality AI can automatically create an example conversation template with the preceding IDs filled in. You can choose which scorecard to use for your example conversations and filter the template to include only some of your conversations. For instructions on creating a template and uploading example conversations, see the [Quality AI setup guide](https://docs.cloud.google.com/gemini-enterprise-cx/insights/qai-setup-guide#calibrate_the_ai_model).

CSV example conversation files can have a variety of formats. For example, yes/no answers correspond to a true or false value, numbers remain the same, and text answers are surrounded by quotation marks. This means that `true` is displayed as a Yes/No answer type and the selected the answer choice is Yes. On the other hand, `"Yes"` is displayed as a text answer type with a selected answer choice of Yes. The following examples illustrate some possible CSV formats.

  * The individual header `QaAnswerValue` does not assign a score. 
        
        ConversationId,QaScorecardId,QaQuestionId,QaAnswerValue
        convo_id,scorecard_test_id,question_id_q3,"NO"
        convo_id,scorecard_test_id,question_id_q6,"YES"
        convo_id,scorecard_test_id,question_id_q6,true
        convo_id,scorecard_test_id,question_id_q6,false
        convo_id,scorecard_test_id,question_id_q6,40.5
        

  * Includes both `QaAnswerValue` and `QaAnswerScore` headers. 
        
        ConversationId,QaScorecardId,QaQuestionId,QaAnswerValue,QaAnswerScore
        convo_id,scorecard_test_id,question_id_q3,"NO",score: 1.0
        convo_id,scorecard_test_id,question_id_q6,"YES",score: 1.0
        

  * The `QaAnswerLabel` header encompasses both a score and an answer but does not separate them with a comma. 
        
        ConversationId,QaScorecardId,QaQuestionId,QaAnswerLabel
        convo_id,scorecard_test_id,question_id_q3,score: 1.0 "NO"
        convo_id,scorecard_test_id,question_id_q6,score: 0.5 40.5
        convo_id,scorecard_test_id,question_id_q6,na_value:true
        convo_id,scorecard_test_id,question_id_q3,true
        




#### Table

Within a spreadsheet, the visual format for your example conversations is a table with each row containing information to identify a single answer and each column containing separate identifications, as shown in the following table:

Conversation ID | Scorecard ID | Question ID | Answer  
---|---|---|---  
44748735396 | 5727080762913918243 | 4097398336657302301 | `"YES"`  
44748735396 | 5727080762913918243 | 3576133206121890384 | `"NO"`  
3495523396 | 5727080762913918243 | 4097398336657302301 | `"YES"`  
3495523396 | 5727080762913918243 | 3576133206121890384 | `"NO"`  
  
## Evaluating a conversation

Human annotators use scorecard questions and instructions to manually evaluate conversations and determine the correct answers to each question in example conversations. When multiple people evaluate the same conversation, they sometimes provide different answers to each question. This inconsistency between evaluations introduces noise and confusion to the machine learning process. Within a conversation, if the same or a similar question is associated with multiple different answers, Quality AI has no way to learn the mapping between questions and answers.

Any of the following can cause inconsistency when multiple people answer the same questions for a single conversation:

  * Subjective questions that lead to different interpretations between annotators.
  * Rubrics with insufficient details or unclear guidelines.
  * Different versions of a question, answer options, or instructions, for example: 
    * You can begin with only yes/no answer options, then later change to a more fine-grained approach with no-a, no-b, and no-c options. 
    * However, combining the yes/no approach with no-a, no-b, and no-c options will confuse the model.
  * An evaluation task that requires a large cognitive load.



### Measure consistency

To measure consistency in your example conversations, ask multiple annotators to independently evaluate the same conversation. Then, compute agreements between them using the [Cohen's kappa coefficient](https://datatab.net/tutorial/cohens-kappa). You want to see a Cohen's kappa coefficient of no less than 0.2. If consistency is low, try one of the following options:

  * Refine the question and instructions to provide less room for interpretation.
  * Communicate between annotators so they can resolve discrepancies and agree on a single grading standard.
  * Continuously monitor consistencies among annotators.
  * Provide additional training to annotators whose answers frequently differ from the grading standard.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
