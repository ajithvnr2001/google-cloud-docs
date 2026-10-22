---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telecommunications-steering/
title: Telecommunications steering prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:06.549089+00:00
---

# Telecommunications steering prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telecommunications-steering/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Telecommunications steering prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

This [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) identifies the end-user's intent and routes them to the appropriate topic within the telecommunications (telco) domain. When the relevant topic is identified, the component transitions to an empty placeholder [flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow) with the name of the identified topic. Placeholder flows may be customized to take actions including [live agent handoff](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#handoff), transition to a prebuilt component, or transition to another Dialogflow CX resource such as a [page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page) or flow.

## Sample utterances

The following sample utterances demonstrate common topics handled by this prebuilt component.

### Accounts

This topic covers questions about accounts, including:

  * _I need to review my account information._
  * _Can I get long distance calling on my phone?_
  * _I'm looking to open an account, what are my options?_
  * _How long until my services are activated?_
  * _I would like to add one more person to my account._
  * _I need to change my number._
  * _Does your company service my area?_
  * _I would like to know who has access to my account._
  * _Could you help me with transferring service?_
  * _I am moving to a new house and need to update my address._



### Billing

This topic covers questions about billing, including:

  * _I would like to know how much I need to pay on my next bill._
  * _I want to change my billing date._
  * _I think I should be getting a credit on my bill._
  * _Can you tell me what this charge is for?_
  * _I need a physical copy of my monthly bill, how can I get one?_
  * _I would like to switch to electronic billing, can I receive my bills through email instead?_



### Disconnect

This topic covers questions about disconnecting or ending service, including:

  * _I would like to cancel one of my phone lines. Can you help me with that?_
  * _I want to end my service._
  * _I'd like to know how to pay my phone off early._
  * _If I cancel my contract, will I have to pay an early termination fee?_
  * _I'd like to cancel my contract, but not my account._
  * _I closed my account and want to know when I can expect my refund._



### Equipment

This topic covers questions about equipment, including:

  * _I just got my new phone and I need to activate it_
  * _How can I activate my SIM card?_
  * _I'm not sure if I'm eligible for an upgrade, can you tell me what phones I'm eligible for?_
  * _I would like to purchase a phone._
  * _Can you repair my phone or just replace it?_
  * _I want to get my phone unlocked._



### Payment

This topic covers questions about payment, including:

  * _I would like to update the credit card I use for payments._
  * _I can't afford to pay my bill and need an arrangement._
  * _I overpaid my account by mistake._
  * _I am trying to find out how much I owe this month on my account._
  * _I need to have my payment extended until next Monday._
  * _I'd like to set up automatic payments._
  * _How do I see a list of the payments I made?_



### Plans

This topic covers questions about plans, including:

  * _I would like to add a mobile phone plan._
  * _I'd like to add a new line to my account._
  * _I was wondering if I could sign up for a service package with internet and mobile?_
  * _Can you remind me what's included my plan per month?_
  * _I am trying to find the best deal for international travel using my mobile phone. Can you help me?_
  * _I want to switch up my TV plan a little but want to know first how much a channel costs to add._



### Technical support

This topic covers technical support questions, including:

  * _I need to find the closest location to pick up equipment I ordered._
  * _I have a conflict on the tech appointment time. Can I reschedule?_
  * _I've been having trouble with the mobile internet, are there any outages?_
  * _I can't seem to send text messages. What should I try?_
  * _How do I connect to the internet?_



### Usage

This topic covers questions about usage, including:

  * _How much data do I have left?_
  * _I don't understand how my data usage is so high._
  * _I need to add data to my phone for this billing cycle._
  * _Can you limit my data to three gigs a month?_



## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Telecommunications Steering  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_telco_steering_bill_customer_support  
  
## Basic setup

To set up this prebuilt component:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).



### Complete

Your agent should now be set up and ready to test.

[ Previous arrow_back  Return and refund  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/return-and-refund)

[ Next Telephone number collection  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telephone-number-collection)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
