---
url: https://docs.cloud.google.com/dialogflow/es/docs/agents-design/
title: General agent design best practices \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:38.140783+00:00
---

# General agent design best practices  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/agents-design/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  General agent design best practices Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides general best practices for designing all types of agents.

You should also see the [voice agent design](https://docs.cloud.google.com/dialogflow/es/docs/voice-agent-design) guide specifically for designing voice agents, and the [best practices](https://docs.cloud.google.com/dialogflow/es/docs/best-practices) guide for using the Dialogflow service.

## Before building an agent

This section provides information that you should consider before starting to build an agent.

### Objective

Consider the overall objective of your agent:

  * What is your business trying to achieve?
  * What will your users expect from your agent?
  * How often will users interact with your agent?



### Platform

Consider how users will access your agent. Review the [platforms supported by Dialogflow](https://docs.cloud.google.com/dialogflow/docs/integrations) before creating content. When you choose platforms to support, prepare your content accordingly. Some of Dialogflow's platform integrations support [rich messages](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages) that can include elements like images, links, and suggestion chips.

### Build agents iteratively

If your agent will be large or complex, start by building a dialog that only addresses the top level requests. Once the basic structure is established, iterate on the conversation paths to ensure you're covering all of the possible routes a user may take.

### Pre-built agents

Dialogflow offers pre-constructed agents to help you get started. [Pre-built agents](https://docs.cloud.google.com/dialogflow/docs/agents-prebuilt#prebuilt_agents) cover common use-cases like hotel booking, navigation, and online shopping. These agents come with intents and entities to cover the most common user queries. Add responses specific to your business, and you'll quickly build a functioning agent.

### System entities

When a user makes a request, there's important information to parse from what they said. In Dialogflow, these are called [entities](https://docs.cloud.google.com/dialogflow/docs/entities-overview). In particular, [system entities](https://docs.cloud.google.com/dialogflow/docs/entities-system) are pre-built entities provided by Dialogflow that handle the most popular types of information.

### Small talk

When developing your dialog, you may have considered handling requests that are off-topic. Dialogflow provides an optional feature called [small talk](https://docs.cloud.google.com/dialogflow/docs/agents-small-talk). With this feature enabled, your agent will respond to general conversation, emotional responses, and questions about the agent itself. All of the small talk responses can be customized to make sure the experience, whether casual, businesslike, or somewhere in between, is representative of your brand.

## Agent design best practices

This section provides a list of best practices for a robust, accurate, performant, and usable agent.

### Greetings and goodbyes

Best Practice | Details  
---|---  
Welcome intents should let users know about the agent's capabilities with branding in mind. | Your agent's welcome intent should inform the user of 2-3 tasks the agent can help with, as well as brief descriptions (as needed) of how to use these features.  
Agents should have a suitable exit message when a successful interaction has ended. | When a user completes a task in your agent, it should summarize the transaction/task and say something like "Until next time", etc.  
  
### Machine learning and training

Best Practice | Details  
---|---  
Intents should have at least 10-20 (depending on complexity of intent) training phrases. | The complexity of your agent will determine the actual number of [training phrases](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases) each intent should have, but 10-20 (depending on complexity of intent) is a good minimum. The more parameters you have in your intents, the more phrases you should provide to train the machine learning model.  
Training phrases should be varied. | Include variations of questions, commands, verbs, and synonyms for common nouns to ensure your phrases cover a broad spectrum of possible requests.  
Annotations should be consistent. | 

  * Review your [training phrases](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases) and ensure that highlighted annotations are pointing to the correct [entities](https://docs.cloud.google.com/dialogflow/docs/entities-overview).
  * You should not have text in training phrases that is annotated in some cases but not others.
  * The span of text selected for an annotation should include all of, and no more than, the text that is necessary to match an entity.
  * Be sure that the annotated text in multiple training phrases contains similar portions of the training phrase. For example, consider that you have a training phrase "Set alarm at 6 a.m.", where "6 a.m." is annotated as `@sys.date`. If you have another training phrase "wake me up at 7 a.m.", do annotate "7 a.m.", but do not annotate "up at 7 a.m.".

  
Use semantically meaningful annotations for system entities. | The semantic meaning of a training phrase part selected for an annotation can be affected by the rest of the text in a training phrase. For example: 

  * I am 7 years old (semantic meaning of annotated text is a person's age)
  * The contract is valid for 7 years (semantic meaning of annotated text is a time duration)

Dialogflow's machine learning models consider semantic meaning when matching system entities. The semantic meaning of the training phrase part must match the intended semantic meaning of the system entity.  
  
For example, do not use the `@sys.duration` system entity for annotation of the first "7 years" example above. The semantic meaning of "7 years" does not match a simple time duration. Instead, you should use the `@sys.age` system entity.  
Custom entities should cover a broad range of examples. | Entities are lists of items. Machine learning will take care of grammatical forms, but you have to include all possible items. Also, check the [define synonyms](https://docs.cloud.google.com/dialogflow/docs/entities-options) option and include some variations.  
Disable ML for as few intents as possible. | Training phrases for intents with ML disabled are not used when training your agent. A user query that is very similar to a training phrase in an intent with ML disabled may be matched to the wrong intent if other intents with ML enabled have a slight resemblance to the user query. If you are having problems with false positives, raise the [ML classification threshold](https://docs.cloud.google.com/dialogflow/docs/agents-settings#ml_settings_machine_learning) instead of disabling ML.  
Do not set a high [ML classification threshold](https://docs.cloud.google.com/dialogflow/docs/agents-settings#ml_settings_machine_learning) for an agent with only a little training data. | If the threshold is high, and there is not a lot of training data, only user queries that have near exact matches to training phrases will result in intent matching. You need to provide a lot of training data if you desire a high threshold.  
Agents should have a fallback intent. | Without fallback intents, unmatched user queries will result in empty responses.  
Agents should provide [negative examples](https://docs.cloud.google.com/dialogflow/docs/intents-default#negative-examples). | Negative examples prevent user queries that are slightly similar to training phrases from unintentionally matching intents.  
Do not define entities that match virtually anything. | This degrades the performance and quality of ML. Nearly everything in every training phrase will be evaluated as a possible match. Consider using `@sys.any` instead. Similarly, composite entities should not contain a single `@sys.any` as a synonym.  
Do not define entities that are composed of filler words or meaningless text. | Examples of filler words and meaningless text are: "hmmm", "let's see", "please", "could you please". If you are attempting to use entities like this to introduce variety, you are only degrading the performance of ML. Dialogflow already augments data to handle variety like this. You should add phrases like this to your training phrases, not your entities.  
Entities should have a limited scope that captures distinct values of one type of information. | Keep your entities focused, short, and simple. If your entity values are complicated, it may be because intent training phrases are better suited to your situation. For example, consider end-user expressions like "How can I make an international call with Plan A?" and "Using international data roaming with Plan B". Do not create entities for both the actions ("How can I make an international call" and "Using international data roaming") and the plans ("Plan A", "Plan B"). Instead, you should use training phrases and intent matching to capture the actions and entities to capture the plans.  
Annotated text in training phrases should have variety. | For example, if you are providing time values that should be parsed as `@sys.time` system entities in training phrases, do not provide the same time in all training phrases. Your training phrases should have a variety of time examples like: "7 a.m.", "8 p.m.", "9 o'clock".  
Intents with many parameters should also have many training phrases. | As a rule, try to have at least three times as many training phrases as parameters and at least 10-20 (depending on complexity of intent) training phrases.  
Each parameter should be used in many training phrases. | As a rule, each parameter should be used in at least 5 training phrases.  
Avoid using multiple `@sys.any` entities in a training phrase. | One training phrase shouldn't contain two consecutive @sys.any or a total of three @sys.any entities. Dialogflow may not be able to distinguish them.  
Do not use similar training phrases in different intents. | Different intents shouldn't contain similar training phrases, because this will prevent Dialogflow from learning how to recognize those phrases.  
Enable automatic spell correction. | If you are using text input, you should enable [automatic spell correction](https://docs.cloud.google.com/dialogflow/docs/agents-settings#ml_settings_machine_learning).  
Do not nest composite entities | Do not use more than one level of nesting in composite entities. Each level of nesting significantly degrades quality.  
Avoid special characters in training phrases. | Special characters in training phrases, like `{`, `_`, `#`, and `[` will be ignored. Emojis are an exception; they work as expected.  
  
### Intent naming

If your agent has many [intents](https://docs.cloud.google.com/dialogflow/es/docs/intents-overview), you should consider a naming scheme that helps you keep them organized. It is common to segment intent names with punctuation, where the specificity increases from left to right. In addition, an intent name should reflect the end-user's intention for a conversational turn.

There are many good naming schemes, but here is one example:

  * phone-service.order.cancel
  * phone-service.order.create
  * phone-service.order.change
  * tv-service.order.cancel
  * tv-service.order.create
  * tv-service.order.change
  * account.balance.get
  * account.balance.pay
  * account.address.get
  * account.address.update



### Helpful intent features

Best Practice | Details  
---|---  
Agents should support contextual requests. | For example, if your agent handles requests for the weather and a user asks "Weather in San Francisco", make sure to add [contexts](https://docs.cloud.google.com/dialogflow/docs/contexts-overview) to support further requests like "How about tomorrow?"  
Agents should have follow-ups for yes, no, cancel, next, back, etc. | Follow-up intents are used to reply to common responses. To add a follow-up intent, hover over an intent and click **Add follow-up**.  
Intents should have at least one text response. | The [response section](https://docs.cloud.google.com/dialogflow/docs/intents-responses) is at the bottom of the intent's page. Adding variations will shuffle the response chosen, making for a less repetitive experience.  
Agents should collect all of the necessary information to fulfill a user's request. | Consider making necessary [parameters required](https://docs.cloud.google.com/dialogflow/docs/intents-actions-parameters). Your agent will keep prompting the user until it gets the information it needs. This is called slot filling.  
Responses should repeat information as needed, like confirming an order. | When a user is making a request like placing an order or changing information, your agent should repeat what's happening for confirmation purposes. When creating these confirmation responses, make sure to include all possible combinations of repeated [entities](https://docs.cloud.google.com/dialogflow/docs/entities-overview) and parameters.  
  
### Conversation repair

Best Practice | Details  
---|---  
Agents should have helpful recovery prompts for each step of the dialog. | For example, if the initial prompt is "What color do you want?" and the user replies with "jungle parrot", a fallback/follow-up intent should rephrase the question, like "Sorry, what color was that?"  
Agents should have customized, brand-specific responses in the default fallback intent. | When a user says something that isn't matched to an intent, the default [fallback intent](https://docs.cloud.google.com/dialogflow/docs/intents-default#default_fallback_intent) is matched. This should be customized to reflect your brand, as well as provide information to guide the user to make a valid request.  
For customized fulfillment, agents should have an intent that allows users to repeat information. | One intent can handle requests like "say that again", "repeat that", "play that again", etc. This can be a follow-up intent.  
Help users to be successful, steer them to tell them exactly what you would like to hear as an answer | For example: if you provide options, don't ask "Would you like A or B?." - because then a user could answer "yes" Instead ask: "I have A and I have B. Which one do you prefer?  
  
### Persona

Best Practice | Details  
---|---  
Agent responses should have a style and tone that fits your brand and are consistent throughout the agent. | As your users converse with your agent, it should feel like they're speaking to one persona. Make sure the qualities and personality you've chosen are represented in all of your responses.  
Agents should be sensitive about cultures, genders, religious beliefs, abilities and ages. | Stereotyping may offend users, even in jokes, and they might not return to your agent.  
  
### Designing for voice

Best Practice | Details  
---|---  
Avoid content that requires visualization or keyboard and mouse interaction. | Don't use hyperLinks, tables, images, abbreviations. You can refer to a website by name. When presenting a list of options, return the best match and ask if the user would like to hear alternative options.  
Don't create awkward silences. Always end with a question. Steer the conversation and to get the interactions going. |   
Write compact dialogues which are easy to understand. | On a screen, text can be long and contain multiple paragraphs. You can skip the parts that are not interesting to you. But hearing a virtual agent talking for too long, won't make your users happy.  
Use [SSML](https://docs.cloud.google.com/text-to-speech/docs/ssml) | Use SSML to structure and to change the intonation of your sentences, so your voices will sound more natural.  
  
For more information on designing for voice, see [Voice agent design](https://docs.cloud.google.com/dialogflow/es/docs/voice-agent-design).

### Protection of consumer privacy

Best Practice | Details  
---|---  
Disable data logging in agent settings for [GDPR compliancy](https://cloud.google.com/security/gdpr/resource-center/compliance). | In the [agent settings](https://docs.cloud.google.com/dialogflow/docs/agents-settings#general), you can disable the logging of interactions in Dialogflow. By disabling this feature, no PII data will be stored in Dialogflow. This will also mean that certain features, such as analytics, won't be available.  
Store chat conversation data in BigQuery to have control over regional storage. | Via [Cloud Logging](https://docs.cloud.google.com/logging/docs) or by using the Dialogflow API, you can send incoming chat utterances to BigQuery. By taking this approach, you will have control over the region where you want to store the data. Additionally, you could make use of the [Data Loss Prevention API](https://cloud.google.com/dlp), to mask sensitive information. See the [blueprint for building an AI-powered customer service on GCP](https://cloud.google.com/blog/products/ai-machine-learning/simple-blueprint-for-building-ai-powered-customer-service-on-gcp).  
  
### Using the knowledge base connector

Best Practice | Details  
---|---  
When importing public FAQs, use valid HTML5 markup. | For example, use article elements with schema.org notation such as [schema.org/Question](http://schema.org/Question) and [schema.org/Answer](http://schema.org/Answer).  
Make sure your FAQ website is indexed by Google Robots | The website will need to allow Google Robots, and needs to be added to the Google search engine via the [Google Webmasters tool](https://www.google.com/intl/nl/webmasters/). Sites like pages.github will not work, because they are not crawable.  
Use 1-200 FAQs | You need more than one Q&A pair and not more than 200 per knowledge base. You can load multiple knowledge bases if you need more.  
  
### Implementing Dialogflow APIs

Best Practice | Details  
---|---  
Do not expose your service account private key in client codebases for mobile or web applications. | This is not considered safe. Anyone who is handy with Chrome Dev tools could steal your key and make (paid) API calls via your account. It's a better approach to always let an API proxy server handle the Google Cloud authentication. This way the service account won't be exposed to the public, and the keys can be safely stored.}  
  
### Designing for voice and text in one agent

Best Practice | Details  
---|---  
Don't use SSML in [default platform responses](https://docs.cloud.google.com/text-to-speech/docs/ssml). | When your agent can respond with both voice and text, a text response will include the raw SSML code. Use plain text in the default platform response and SSML in platform-specific responses. Alternatively, you can use a webhook to generate SSML only when a voice response is needed.  
  
### Testing

Best Practice | Details  
---|---  
Test your app thoroughly with someone that was not involved in its development. | Having someone unfamiliar with the agent use the app will give you insight to how naturally the conversation flows. Have them look out for accuracy, long pauses, missing conversational paths, pacing, awkward transitions, etc.  
Test your app on all platforms you plan on supporting. | If your agent will be available on one or more [platforms](https://docs.cloud.google.com/dialogflow/docs/integrations), make sure [rich messaging](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages) and responses show up as expected across all platforms.  
  
## Enterprise best practices

  * See the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework).



## Additional conversation design guides

  * See the [conversation design guide](https://designguidelines.withgoogle.com/conversation) provided by the Actions on Google team.
  * See the [SSML guide](https://developers.google.com/assistant/actions/reference/ssml) provided by the Actions on Google team.



[ Previous arrow_back  Integrations  ](https://docs.cloud.google.com/dialogflow/es/docs/integrations)

[ Next Voice agent design best practices  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/voice-agent-design)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
