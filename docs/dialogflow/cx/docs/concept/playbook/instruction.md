---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/instruction/
title: Playbook instructions \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:35.204247+00:00
---

# Playbook instructions  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/instruction/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Playbook instructions Stay organized with collections  Save and categorize content based on your preferences. 

Playbook **instructions** define the process that should be taken to accomplish the playbook goal.

Each step contains a natural language instruction that may contain any of the following:

  * A basic instruction that the LLM can understand.
  * An instruction to route the user to another playbook. Playbooks are referenced using the form `${PLAYBOOK: playbook_name}`.
  * An instruction to use a specific [playbook tool](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool). Tools are referenced using the form `${TOOL: tool_name}`.
  * An instruction to route the user to a [flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow). Flows are referenced using the form `${FLOW: flow_name}`.
  * A reference to a [playbook parameter](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/parameter). Parameters are referenced using the form `$parameter_name`.
  * An instruction to call a [code block](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/code-block). Code blocks are referenced using the form ``function_name``.



Each step description starts with `-` and an optional numbered step, and you can define subinstructions using indentation.

Sample:
    
    
    - greet the customer and ask them how you can help.
        - If the customer wants to book flights, route them to ${PLAYBOOK: flight_booking}.
        - If the customer wants to book hotels, route them to  ${PLAYBOOK: hotel_booking}.
        - If the customer wants to know trending attractions, use the ${TOOL: attraction_tool} to show them the list.
    - help the customer to pay for their booking by routing them to ${FLOW: make_payment}.
    

**Note:** When editing instructions, you may see a warning indicating that a resource reference has no corresponding [playbook examples](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/example). You can still save and use the playbook with this warning present, but it's unlikely to work reliably until examples that use the resource are added.

## Instruction steps

To add structure to your instructions, you can optionally define steps with a hierarchical numbering system. If you do not provide step numbers, and a code block references a particular step, the ordering of steps will be used to determine step position values.

Sample:
    
    
    - Step 1. Greet the user and ask how you can assist them today.
    - Step 2. Collect the user's basic flight information in the following order
      from (a) to (f). Do not deviate from this order, and do not proceed until the
      user has specified each piece of information. Ask clarifying questions if
      necessary, and make sure that the answers the user give make sense.
        - Step 2.1 The traveler's $origin city. Do not proceed until the user has
          made this clear.
        - Step 2.2 The traveler's $destination city. Do not proceed until the user
          has made this clear.
        - Step 2.3 When the traveler will leave their origin city. If the user
          specifies one departure date, collect their $earliest_departure_date. If
          the user specifies a range of departure dates, collect their
          $earliest_departure_date and $latest_departure_date. Unless otherwise
          specified, assume all dates are from 2024 to 2025. If the user provides
          a vague departure date, ask them follow-up questions to determine their
          precise departure date(s). All dates should be in YYYY-MM-DD format. If
          the user does not provide their departure date(s) in YYYY-MM-DD format,
          then convert the dates for them.
        - Step 2.4 When the traveler will leave from their destination city and
          return home. If the user specifies one return date, collect their
          $earliest_return_date. If the user specifies a range of return dates,
          collect their $earliest_return_date and $latest_return_date. Unless
          otherwise specified, assume all dates are from 2024 to 2025. If the user
          provides a vague return date or a vague return date range, ask them
          follow-up questions to determine their precise return date(s). All dates
          should be in YYYY-MM-DD format. If the user does not provide their return
          dates in YYYY-MM-DD format, then convert the dates for them.
        - Step 2.5 The $num_adult_passengers the user wishes to buy tickets for. All
          people 12 years old or older are adult passengers. This value must be a
          precise whole number. Do not proceed until the user has provided a valid
          number of adult passengers.
        - Step 2.6 The $num_child_passengers the user wishes to buy tickets for.
          This value must be a precise whole number. Do not proceed until the user
          has provided a valid number of child passengers.
        - Assume the user is an adult.
    

[ Previous arrow_back  Playbook goals  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/goal)

[ Next Code blocks  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/code-block)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
