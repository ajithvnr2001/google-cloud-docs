---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/financial-services-steering/
title: Financial services steering prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:43.100720+00:00
---

# Financial services steering prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/financial-services-steering/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Financial services steering prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

This [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) identifies the end-user's intent and routes them to the appropriate topic within the financial services (FSI) domain. When the relevant topic is identified, the component transitions to an empty placeholder [flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow) with the name of the identified topic. Placeholder flows may be customized to take actions including [live agent handoff](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#handoff), transition to a prebuilt component, or transition to another Dialogflow CX resource such as a [page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page) or flow.

## Sample utterances

The following sample utterances demonstrate common topics handled by this prebuilt component.

### Account balance

This topic covers questions about account balances, including:

  * _I want to know my account balance._
  * _What is the remaining balance in my account?_
  * _How much money do I have available in my bank account?_
  * _Can you provide me with my current balance?_
  * _I want to check the balance of my account ending with 1001._
  * _What are the funds in my account?_



### Account statement

This topic covers questions about account statements, including:

  * _I want to know my account statement._
  * _What was my recent account statement?_
  * _Please share my account statement for the last month._
  * _I want my account statement to be emailed to me._
  * _Tell me about my account statement from Jan to July._
  * _Please share the statement for my savings account._



### Arrange appointment

This topic covers questions about making appointments, including:

  * _I want to arrange a meeting with a bank representative to talk about opening a new account._
  * _I want to set up a video call for my e-verification._
  * _Can someone from the bank call me on my mobile?_
  * _I want to meet up with someone to talk about my investment options._
  * _Can I talk to someone about my wealth management options?_



### Credit card enrollment

This topic covers questions about enrolling for new credit cards, including:

  * _What is the credit card enrollment procedure?_
  * _What cards are available to me?_
  * _Please tell me what the best cards for me are._
  * _Show me the latest cards I'm eligible for._
  * _I want to get a new card._



### Credit card statement

This topic covers questions about credit card statements, including:

  * _I want to know my credit card statement._
  * _What was my recent card statement?_
  * _Please share my credit card statement for the last month._
  * _I want my card statement to be emailed to me._
  * _Tell me about my card statement from Jan to July._



### Disputes

This topic covers questions about registering disputes and claims, including:

  * _I am calling to dispute a transaction on my account._
  * _There is an extra charge on my credit card bill that I want to report._
  * _There is a suspicious transaction on my account._
  * _I want to talk about a fraudulent transaction_
  * _Some of the transactions on my account don't look right._
  * _Why have I been overcharged on my credit card bill?_



### Feedback

This topic covers questions about customer feedback, including:

  * _I want to share my feedback._
  * _I want to rate my recent interaction with the bank_
  * _I want to rate my recent interaction with the customer service_
  * _I want to share my review on the customer service_
  * _How do I give feedback on my recent interaction?_



### Locked card

This topic covers questions about locking and unlocking cards, including:

  * _I am calling to lock my card._
  * _I want to permanently block my card._
  * _I want to check if my card is locked._
  * _I want to unblock my card._
  * _I want to reactivate my card._
  * _I want to place a temporary lock on my card._
  * _Is my card locked?_



### Lost or stolen card

This topic covers questions about lost or stolen cards, including:

  * _I am calling to report a lost card._
  * _I am calling to report a stolen card._
  * _I have lost my card._
  * _My card has been stolen._
  * _Please help me deactivate my lost card._
  * _Please help me deactivate my stolen card._



### Make a payment

This topic covers questions about making payments, including:

  * _I want to make a payment._
  * _I want to pay my credit card bill._
  * _I'd like to pay my gas bill._
  * _I need to make a payment to my loan account._
  * _I'd like to pay my credit card bill for last month through my debit card._



### Open account

This topic covers questions about opening new bank accounts, including:

  * _What is the procedure to open a new account?_
  * _Am I eligible to open an account with the bank?_
  * _Please tell me how to open an account._
  * _I want to open a new account._



### Transaction history

This topic covers questions about transaction history for savings accounts, including:

  * _I want to know my transactions for last month._
  * _I was looking for yesterday's transactions._
  * _I want to verify some of my recent transactions._
  * _Please tell me about my last 10 transactions._
  * _I want my transaction history to be emailed to me._
  * _Tell me about my transactions from Jan to July._



## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Financial Services Steering  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_fsi_steering_account_statement  
  
## Basic setup

To set up this prebuilt component:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).



### Complete

Your agent should now be set up and ready to test.

[ Previous arrow_back  Fraud and dispute (Retail)  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/fraud-and-dispute-retail)

[ Next Greeting  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/greeting)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
