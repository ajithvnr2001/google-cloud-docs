---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-compose-simulator/
title: Test smart compose results using the simulator \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:32.257751+00:00
---

# Test smart compose results using the simulator  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-compose-simulator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Test smart compose results using the simulator Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This feature is no longer supported. For an alternative, use [smart reply](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-reply).

This tutorial walks you through the process of testing the performance of your [smart compose model](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-compose-console) using the Agent Assist console simulator. If you prefer, you can also perform all of the following actions by calling the API directly. You can use the console to train a model and test its performance, but be aware that all runtime operations must be carried out by calling the API directly.

## Before you begin

  1. If you are using the publicly-available conversation dataset, review the [documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-data-format) that guides you through using these resources.
  2. If you are using your own data, make sure that you have created one or more [conversation datasets](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-dataset). At least one conversation dataset is required for model training.
  3. Create and deploy a [smart compose model](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-compose-console) and manage its allowlist.
  4. Create a [conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) that includes your smart compose model. You must create a conversation profile before you can use the simulator.



## Test your smart compose model using the simulator

  1. Navigate to the [Agent Assist console](https://agentassist.cloud.google.com) and click the **Conversation profiles** menu option on the left side of the page:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aa19.png)

  2. The conversation profiles page displays a list of your conversation profiles. To use the simulator, click the three vertical dots to the far right of the conversation profile that you want to test and click **Use simulator**. The simulator page appears:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/priv/images/aapriv11.png)

  3. In the simulator, you can test your conversation profile's performance by inputting text and evaluating the returned suggestions. If your conversation profile is configured to enable more features than smart compose, you can choose which features to include in the simulation by clicking the **Options** button at the top right of the simulator page and making a selection. Make sure that smart compose is selected.

  4. The following example tests a smart compose model's performance when a customer contacts a human agent to cancel an order. Smart compose is the only feature being tested in this example (all other options, such as smart reply, are unchecked under the **Options** menu).

The customer initiates the conversation by typing _Hi_. The human agent begins to respond by typing _H_. A smart compose suggestion appears in gray after this letter is typed:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/priv/images/aapriv12.png)

  5. The agent has the option to either hit the tab key to accept the smart compose suggestion or continue typing. Each time the agent either types a new character or hits tab to accept a suggestion, a new smart compose suggestion will appear. Suggestions are automatically generated until the sentence is completed. In this example, the agent hits tab to select the suggestion of _How can I help_ , which generates another suggestion to add on to the sentence:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/priv/images/aapriv13.png)

  6. The agent again hits tab to accept the _you today?_ suggestion and sends the response to the customer. The customer replies with _I want to cancel my order_. The agent begins to type a response asking the customer for the order number. Typing _D_ brings up the suggestion _Don't have the option to cancel your order_ , which is not the message that the agent wants to send:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/priv/images/aapriv14.png)

  7. Instead of accepting the suggestion, the agent continues to type. _Do_ brings up the same suggestion as _D_ , so the agent enters a space to continue their sentence. The space brings up the suggestion _Do you know the order_ , which the agent hits tab to accept. The agent accepts the next smart compose suggestion of _number?_ to complete the sentence: _Do you know the order number?_ :

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/priv/images/aapriv15.png)

  8. The customer responds with their order number. The agent then wants to ask them to wait while they look up the order number. _O_ brings up the suggestion _One moment_ which the agent accepts. The next suggestion is _while I pull_ which they also accept, then _up your order._ which they also accept. The agent sends the completed sentence to the customer:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/priv/images/aapriv16.png)

  9. Smart compose will make a new suggestion each time the human agent types a character in the response box until the agent concludes their interaction with the customer and ends the conversation.

  10. (Optional). Smart compose can be used in conjunction with smart reply. You must create a conversation profile that configures both smart compose and smart reply models to test both features at once using the simulator. If you have both features checked under the **Options** drop-down menu, the human agent will see bubbles containing smart reply text suggestions below the response box:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/priv/images/aapriv17.png)

  11. The agent can select a smart reply suggestion to copy it to the response box. If they choose to add another sentence or otherwise add characters to the suggestion, smart compose will make a suggestion to complete the agent's sentence.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
