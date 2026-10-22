---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/zip-code-collection/
title: Zip code collection prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:59.805459+00:00
---

# Zip code collection prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/zip-code-collection/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Zip code collection prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

This [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) collects five-digit zip codes.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * Zip codes longer than five digits are not accepted.
  * Alphanumeric zip codes are not accepted.



## Recommended agent settings

[Enable DTMF](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#dtmf) to allow users to input numeric values using the telephone keypad.

## Additional features

The following additional functionalities are provided by this prebuilt component:

  * [Repeat](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#repeat-functionality)
  * [Waiting room](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#waiting-room-functionality)
  * [Playback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#playback-functionality)



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Valid zip code

End-user provides a five-digit zip code; agent successfully collects it.

User input | Agent response  
---|---  
| Please say or enter the five digit zip code.  
27656 |   
| You mentioned the zip code is 27656, is that correct?  
yes |   
| Great, I'm done with collecting the zip code.  
  
### Retry

End-user provides a five-digit zip code in the second attempt; agent successfully accepts it.

User input | Agent response  
---|---  
| Please say or enter the five digit zip code.  
27656 |   
| You mentioned the zip code is 27657, is that correct?  
no |   
| Sorry I didn't get it right.  
Please say or enter the five digit zip code.  
27656 |   
| You mentioned the zip code is 27656, is that correct?  
yes |   
| Great, I'm done with collecting the zip code.  
  
### Invalid zip code

End-user provides an invalid zip code that is over five digits long; agent reprompts and successfully collects the corrected zip code.

User input | Agent response  
---|---  
| Please say or enter the five digit zip code.  
276566 |   
| I heard 123456, which is not a valid five digit zip code.  
Please say or enter the five digit zip code.  
27656 |   
| You mentioned the zip code is 27656, is that correct?  
yes |   
| Great, I'm done with collecting the zip code.  
  
### Unrecognized input

Component exits the flow after the end-user provides unrecognized input three times.

User input | Agent response  
---|---  
| Please say or enter the five digit zip code.  
It's fine |   
| Sorry, I didn't get that. Can you please say or enter the five digit zip code again?  
Good |   
| Hmm, I still wasn't able to get that. Please make sure you're saying the five digit zip code. You can also use the keypad to enter the zip code.  
Nice |   
| Sorry, I'm having difficulty understanding your response.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Zip Code Collection  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_zip_code_collection_collect_zip_code  
Parameter | [param_name] | zip_code  
  
### Output parameters

Output parameters are session parameters that will remain active after exiting the component. These parameters contain important information collected by the component. This prebuilt component provides values for the following output parameters:

Parameter Name | Description | Output Format  
---|---|---  
zip_code_collection_zip_code | This parameter returns the zip code collected by the conversation flow | string  
  
## Basic setup

To set up this prebuilt component:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).



### Complete

Your agent and should now be set up and ready to test.

[ Previous arrow_back  Waiting room  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/waiting-room)

[ Next Agent settings  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
