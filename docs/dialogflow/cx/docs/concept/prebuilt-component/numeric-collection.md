---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/numeric-collection/
title: Numeric collection prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:44:18.960940+00:00
---

# Numeric collection prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/numeric-collection/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Numeric collection prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

This [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) collects numeric sequences from the end-user. The minimum and maximum length accepted can be configured via input parameters.

The component captures chunks of digits from the user on each conversational turn and concatenates them to form the final sequence. The minimum and maximum length accepted per chunk can be configured via input parameters.

The sequence capture will continue until the end-user indicates they are done with the sequence with input that matches the [prebuilt_components_confirmation_done intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#common-intents).

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * Non-numeric characters are not supported. See [alphanumeric collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/alphanumeric-collection) for support of letters and numbers.



## Recommended agent settings

[Enable DTMF](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#dtmf) to allow users to input numeric values using the telephone keypad.

## Additional functionalities

The following additional functionalities are provided by this prebuilt component:

  * [Repeat](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#repeat-functionality)
  * [Waiting room](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#waiting-room-functionality)
  * [Playback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#playback-functionality)



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Single chunk

End-user provides numeric sequence in the first attempt; agent successfully accepts it.

User input | Agent response  
---|---  
| Please start by saying the first 1 to 30 digits of the numeric sequence. Once you're done, say "I'm done" to finish the collection. You can also say "playback" at any time to check the current collected sequence.  
2374 30940 029 30 |   
| I got 23743094002930, is that correct?  
Yes |   
| Okay. Please say or enter the next part of the numeric sequence.  
done |   
| Thank you, the numeric sequence I've collected is 23743094002930. Is that correct?  
yes |   
| Great, I'm done collecting the numeric sequence.  
  
### Multiple chunks

End-user provides numeric sequence in multiple chunks; agent successfully accepts it.

User input | Agent response  
---|---  
| Please start by saying the first 1 to 30 digits of the numeric sequence. Once you're done, say "I'm done" to finish the collection. You can also say "playback" at any time to check the current collected sequence.  
2374 30940 029 30 |   
| I got 23743094002930, is that correct?  
No |   
| No worries, can you please provide the first 1 to 30 digits of the numeric sequence again?  
2374 |   
| I got 2374, is that correct?  
Yes |   
| Okay. Please say or enter the next part of the numeric sequence.  
3094 |   
| I got 3094, is that correct?  
Yeah |   
| Okay. Please say or enter the next part of the numeric sequence.  
002930 |   
| I got 002930, is that correct?  
No |   
| No worries, what is after 23743094?  
2930 |   
| I got 2930, is that correct?  
Yes, that's all |   
| Thank you, the numeric sequence I've collected is 237430942930. Is that correct?  
Yes |   
| Great, I'm done collecting the numeric sequence.  
  
### Successful retry

End-user provides a numeric sequence in the first attempt; agent re-confirms it but end-user says "no". Agent asks end-user to provide the sequence again. End-user provides and confirms the sequence and agent successfully accepts it.

User input | Agent response  
---|---  
| Please start by saying the first 1 to 30 digits of the numeric sequence. Once you're done, say "I'm done" to finish the collection. You can also say "playback" at any time to check the current collected sequence.  
92832938 3489 |   
| I got 928329383459, is that correct?  
no |   
| No worries, can you please provide the first 1 to 30 digits of the numeric sequence again?  
928329383435 |   
| I got 928329383435, is that correct?  
Yes and that's all for me |   
| Thank you, the numeric sequence I've collected is 928329383435. Is that correct?  
yes |   
| Great, I'm done collecting the numeric sequence.  
  
### Unsuccessful retries

End-user provides a numeric sequence thrice and says "no" on the re-confirmation step; component exits the flow on third failed confirmation.

User input | Agent response  
---|---  
| Please start by saying the first 1 to 30 digits of the numeric sequence. Once you're done, say "I'm done" to finish the collection. You can also say "playback" at any time to check the current collected sequence.  
928329383435 |   
| I got 928329383835, is that correct?  
no |   
| No worries, can you please provide the first 1 to 30 digits of the numeric sequence again?  
23 289 0239 903 |   
| I got 232890239953, is that correct?  
no |   
| No worries, can you please provide the first 1 to 30 digits of the numeric sequence again?  
23847 02938 |   
| I got 2384702938, is that correct?  
no |   
| Sorry, I've used too many tries and failed to collect your response.  
  
### Unrecognized input

Component exits the flow after the end-user provides unrecognized input three times.

User input | Agent response  
---|---  
| Please start by saying the first 1 to 30 digits of the numeric sequence. Once you're done, say "I'm done" to finish the collection. You can also say "playback" at any time to check the current collected sequence.  
It's fine |   
| Sorry, I didn't get that. Please start by saying the first 1 to 30 digits of the numeric sequence. Once you're done, say "I'm done" to finish the collection. You can also say "playback" at any time to check the current collected sequence.  
nice |   
| Hmm, I still wasn't able to get that. Please make sure you're saying the first 1 to 30 digits of the numeric sequence. Once you're done, say "I'm done" to finish the collection. You can also say "playback" at any time to check the current collected sequence. If we're having trouble hearing you, you can also use the keypad to enter the numeric sequence.  
great |   
| Sorry, I'm having difficulty understanding your response.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Numeric Collection  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_numeric_collection_collect_numeric_sequence  
Parameter | [param_name] | user_provided_cur_seq  
  
## Input parameters

Input parameters are parameters that are used to configure certain behaviors of the component. The parameters will be used by one or more conditions within the flow to determine how the component should behave. Flow-scoped parameters must be set on the start page of the component as described below. Session-scoped parameters may be set either by a calling flow, or on the start page of this component.

You can configure the minimum and maximum lengths accepted per capture and for the final collected sequence by modifying [parameter presets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset) in the [flow's start page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#data).

This prebuilt component accepts the following input parameters:

Parameter Name | Description | Input Format  
---|---|---  
$flow.numeric_min_length | Minimum length of the final numeric sequence | integer  
$flow.numeric_max_length | Maximum length of the final numeric sequence | integer  
$flow.lower_limit | Minimum length of the chunk a user can provide each turn | integer  
$flow.upper_limit | Maximum length of the chunk a user can provide each turn | integer  
  
####  To configure the input parameters for this component, expand for instructions. 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). 
  2. Choose your Google Cloud project. 
  3. Select your agent. 
  4. Select the **Build** tab. 
  5. Click the imported component in the **Flows** section. 
  6. Click the Start Page in the **Pages** section. 
  7. Click the **true** Route in the Start Page. 
  8. In the Route window, edit the **Parameter Presets** values as needed. 
  9. Click **Save**. 



## Output parameters

Output parameters are session parameters that will remain active after exiting the component. These parameters contain important information collected by the component. This prebuilt component provides values for the following output parameters:

Parameter Name | Description | Output Format  
---|---|---  
numeric_collection_numeric_sequence | This parameter returns the numeric sequence captured during the session | string  
  
## Basic setup

To set up this prebuilt component:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).



### Complete

Your agent should now be set up and ready to test.

[ Previous arrow_back  Name collection  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/name-collection)

[ Next Offers and deals  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/offers-and-deals)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
