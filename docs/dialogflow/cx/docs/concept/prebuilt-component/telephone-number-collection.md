---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telephone-number-collection/
title: Telephone number collection prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:11.903096+00:00
---

# Telephone number collection prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telephone-number-collection/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Telephone number collection prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

This [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) captures and validates country code and telephone number.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * Telephone numbers more than 16 digits long are not accepted.



## Recommended agent settings

[Enable DTMF](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#dtmf) to allow users to input numeric values using the telephone keypad.

## Additional features

The following additional functionalities are provided by this prebuilt component:

  * [Repeat](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#repeat-functionality)
  * [Waiting room](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#waiting-room-functionality)
  * [Playback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#playback-functionality)



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Valid telephone number in two turns

End-user provides country code first followed by telephone number; agent successfully validates and accepts it.

User input | Agent response  
---|---  
| What is your country name or code?  
+1 |   
| Got it, your country code is plus 1. Please say your telephone number.  
6502530000 |   
| Got it. The number you mentioned is plus 1 6502530000, is that correct?  
Yes, it's correct |   
| Great, I'm done collecting the telephone number.  
  
### Valid telephone number in single turn

End-user provides country code and telephone number at the same time, agent successfully validates and accepts it.

User input | Agent response  
---|---  
| What is your country name or code?  
+1 6502530000 |   
| Got it. The number you mentioned is plus 1 6502530000, is that correct?  
Yes, it's correct |   
| Great, I'm done collecting the telephone number.  
  
### Invalid phone number

End-user provides a country code and telephone number in one turn; agent checks and finds the provided telephone number is of valid length (within 16 digits) but not a valid telephone number. Then agent re-prompts the end-user to provide telephone number.

User input | Agent response  
---|---  
| What is your country name or code?  
+1 6502530001 |   
| Sorry, but this telephone number cannot be recognized. I have collected the country code as plus 1. Please provide a valid telephone number.  
6502530000 |   
| Got it. The number you mentioned is plus 1 6502530000, is that correct?  
Yes, it's correct |   
| Great, I'm done collecting the telephone number.  
  
### Invalid country code and telephone number

End-user provides a country code and telephone number in one turn; agent checks and finds the provided country code and telephone number is invalid. The agent then re-prompts the end-user to provide country code and telephone number.

User input | Agent response  
---|---  
| What is your country name or code?  
+0080000000000 |   
| Sorry, it seems the provided country code or telephone number is invalid. Let's start again. Please say your country name or code.  
1 |   
| Got it, your country code is plus 1 . What is your telephone number?  
6502530000 |   
| Got it. The number you mentioned is plus 1 6502530000, is that correct?  
Yes, it's correct |   
| Great, I'm done collecting the telephone number.  
  
### Unrecognized input

Component exits the flow after the end-user provides unrecognized input three times.

User input | Agent response  
---|---  
| What is your country name or code?  
It's fine |   
| Sorry, I didn't get that. Can you please say or enter the country code again?  
nice |   
| Hmm, I still wasn't able to get that. Please make sure you're saying the country code. If I am having trouble hearing you, you can also use the keypad to enter the country code.  
good |   
| Sorry, I'm having difficulty understanding your response.  
  
## Telephone number validation

The telephone number prebuilt component uses the [IS_PHONE_NUMBER system function](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions#func-isphonenumber) to validate that the phone number matches a valid pattern.

## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Telephone Number Collection  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_telephone_number_collection_incorrect_country_code  
Parameter | [param_name] | telephone_number  
Entity Type | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_telephone_no_country_code  
  
## Output parameters

Output parameters are session parameters that will remain active after exiting the component. These parameters contain important information collected by the component. This prebuilt component provides values for the following output parameters:

Parameter Name | Description | Output Format  
---|---|---  
telephone_number_collection_telephone_number | This parameter returns the telephone number captured by the component | string  
telephone_number_collection_country_code | This parameter returns the country code captured by the component | string  
  
## Basic setup

To set up this prebuilt component:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).



### Complete

Your agent should now be set up and ready to test.

[ Previous arrow_back  Telecommunications steering  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telecommunications-steering)

[ Next Transaction history  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/transaction-history)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
