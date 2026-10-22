---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/name-collection/
title: Name collection prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:38.287354+00:00
---

# Name collection prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/name-collection/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Name collection prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

This [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) captures first, last, and optional middle name along with any spaces, hyphens or apostrophes.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * Names having special characters outside of spaces, apostrophes and hyphens are not supported by this component.



## Additional features

The following additional functionalities are provided by this prebuilt component:

  * [Waiting room](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#waiting-room-functionality)



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Full name

End-user provides a full name in the first turn; the agent successfully accepts it.

User input | Agent response  
---|---  
| What is your full name? Please tell me your first, last, and middle name, if you have one.  
Sundar Pichai |   
| To confirm, your first name is Sundar, and your last name is Pichai. Did I spell your full name correctly?  
Yes |   
| Do you have a middle name?  
no |   
| Thank you, Sundar.  
  
### Full name in parts

End-user is unable to provide a full name on the first attempt. The end-user then provides their first, last, and middle names in separate turns; the agent successfully accepts it.

User input | Agent response  
---|---  
| What is your full name? Please tell me your first, last, and middle name, if you have one.  
nice |   
| Sorry, I didn't get that right. Let's start capturing the name again.  
Before capturing your name, could you please help me confirm whether you have any hyphens, extra spaces, or apostrophes in your name?  
No |   
| Let's start by capturing your first name.  
What is your first name?  
Lawrence |   
| Lawrence. Did I spell your first name correctly?  
yes |   
| What is your last name?  
Page |   
| Page. Did I spell your last name correctly?  
yes |   
| Do you have a middle name?  
yes |   
| What is your middle name?  
Edward |   
| Edward. Did I spell your middle name correctly?  
yes |   
| Thank you, Lawrence.  
  
### Special characters

End-user is unable to provide a full name on the first attempt. The end-user then provides their first, last, and middle names in separate turns with special characters; agent successfully accepts it.

User input | Agent response  
---|---  
| What is your full name? Please tell me your first, last, and middle name, if you have one.  
nice |   
| Sorry, I didn't get that right. Let's start capturing the name again.  
Before capturing your name, could you please help me confirm whether you have any hyphens, extra spaces, or apostrophes in your name?  
Yes I have |   
| Got it. Are these special characters in your first name, middle name, or last name?  
First name |   
| Please tell me the first part of your first name before any special characters.  
Evan |   
| Evan. Did I spell the first part correctly?  
yes |   
| Please tell me what's next: a space, apostrophe, or hyphen.  
hyphen |   
| "hyphen". Did I capture the name separator after the first part of your first name correctly?  
yes |   
| Please spell out the next part of your first name, after the hyphen. Say only the letters, for example J-O-H-N.  
James |   
| James. Tell me if that's wrong, if that's the end, or, what's next: a space, apostrophe, or hyphen.  
I am done |   
| What is your last name?  
Mady |   
| Mady. Did I spell your last name correctly?  
yes |   
| Do you have a middle name?  
no |   
| Thank you, Evan-James.  
  
### No input

Component exits the flow after the end-user provides no input three times.

User input | Agent response  
---|---  
| What is your full name? Please tell me your first, last, and middle name, if you have one.  
[No-input] |   
| Sorry, I wasn't able to hear you. What is your full name?  
[No-input] |   
| Hmm, I still cannot hear you. Try speaking louder or moving to a quieter area.  
[No-input] |   
| Sorry, I'm having difficulty understanding your response.  
  
## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Name Collection  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_name_collection_special_characters_decider  
Entity Type | prebuilt_components_[component_name]_[entity_type_name] | prebuilt_components_name_collection_first_name  
Parameter | [param_name] | user_provided_first_name  
  
## Output parameters

Output parameters are session parameters that will remain active after exiting the component. These parameters contain important information collected by the component. This prebuilt component provides values for the following output parameters:

Parameter Name | Description | Output Format  
---|---|---  
name_collection_first_name | This parameter returns the user-provided first name that is captured by the component | string  
name_collection_last_name | This parameter returns the user-provided last name that is captured by the component | string  
name_collection_middle_name | This parameter returns the user-provided middle name that is captured by the component. If no middle name is collected, the parameter will be an empty string | string  
  
## Basic setup

To set up this prebuilt component:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).



### Complete

Your agent should now be set up and ready to test.

[ Previous arrow_back  Make a payment  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/make-a-payment)

[ Next Numeric collection  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/numeric-collection)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
