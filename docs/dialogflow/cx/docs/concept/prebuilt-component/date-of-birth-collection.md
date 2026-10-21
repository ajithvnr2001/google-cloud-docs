---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection/
title: Date of birth collection prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:42.404464+00:00
---

# Date of birth collection prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Date of birth collection prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

This [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) captures and validates a date of birth by collecting month, date, and year.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * This component does not support verification of end-user's date of birth via ID verification.



## Recommended agent settings

[Enable DTMF](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#dtmf) to allow users to input numeric values using the telephone keypad.

## Additional functionalities

The following additional functionalities are provided by this prebuilt component:

  * [Repeat](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#repeat-functionality)
  * [Waiting room](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#waiting-room-functionality)
  * [Playback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#playback-functionality)



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Full date of birth

End-user provides complete date of birth in one turn; agent successfully accepts it.

User input | Agent response  
---|---  
| Please provide your date of birth. Please say your birth month, followed by your birth day, and then your birth year.  
September 9th 1995 |   
| Okay, your birthdate is September 9, 1995. Is that correct?  
yes |   
| Great, I've collected your birthdate.  
  
### Partial date of birth

End-user provides date of birth by saying month first followed by date and year; agent successfully accepts it.

User input | Agent response  
---|---  
| Please provide your date of birth. Please say your birth month, followed by your birth day, and then your birth year.  
March |   
| What day were you born on?  
12 |   
| What year were you born in?  
1999 |   
| Okay, your birthdate is March 12, 1999. Is that correct?  
yes |   
| Great, I've collected your birthdate.  
  
### Future date validation

This scenario assumes the current date is March 22, 2023. End-user provides a future date of birth; agent validates it and re-prompts end-user to provide the correct date of birth.

User input | Agent response  
---|---  
| Please provide your date of birth. Please say your birth month, followed by your birth day, and then your birth year.  
September 9th 2023 |   
| What year were you born in?  
2023 |   
| Okay, your birthdate is September 9, 2023. Is that correct?  
yes |   
| Sorry, you have provided a future date. Let's start again.  
Which month were you born in?  
March |   
| What day were you born on?  
12 |   
| What year were you born in?  
1999 |   
| Okay, your birthdate is March 12, 1999. Is that correct?  
yes |   
| Great, I've collected your birthdate.  
  
### Invalid date

End-user provides an invalid date of birth such as February 30th 1999 or April 31st 1999; agent validates it and re-prompts end-user to provide the correct date of birth.

User input | Agent response  
---|---  
| Please provide your date of birth. Please say your birth month, followed by your birth day, and then your birth year.  
February 30th 1999 |   
| Okay, your birthdate is February 30, 1999. Is that correct?  
yes |   
| The date you have provided is invalid. Let's start again.  
Which month were you born in?  
March |   
| What day were you born on?  
12 |   
| What year were you born in?  
1999 |   
| Okay, your birthdate is March 12,1999. Is that correct?  
yes |   
| Great, I've collected your birthdate.  
  
### Unrecognized input

Component exits the flow after the end-user provides unrecognized input three times.

User input | Agent response  
---|---  
| Please provide your date of birth. Please say your birth month, followed by your birth day, and then your birth year.  
It's fine |   
| Sorry, I didn't get that. Can you please say or enter your date of birth again?  
nice |   
| Sorry I did not get your date of birth. Let's start with month. Please say which month were you born in?  
good |   
| Sorry, I didn't get that. Can you please say or enter the month number again?  
nice |   
| Hmm, I still wasn't able to get that. Please make sure you're saying the month. If I am having trouble hearing you, you can also use the keypad to enter the month number.  
nice |   
| Sorry, I'm having difficulty understanding your response.  
  
## Date of birth validation

This prebuilt component uses the [IS_DATE](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions#func-isdate) and [IS_FUTURE_DATE](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions#func-isfuturedate) system functions to check whether a collected date is valid and in the past. In addition:

  * Inputs such as "this month", "next month" or "last month" are converted into the appropriate months. For example, if the end-user is interacting with the agent in March, then "this month", "next month" and "last month" are converted into "March", "April" and "February" respectively.
  * Validates that the year should be four digits. If the year input contains only two digits, the component converts it into a four-digit year. For example, "98" is converted to "1998".
  * Input such as "this Thursday", "last Thursday", and "next Thursday" are captured as the appropriate month and day and the agent prompts to provide the year. For example, if end-user is interacting with the agent on March 22, 2023, which is a Wednesday, then "this Thursday", "last Thursday", and "next Thursday" are converted into "March 23", "March 16", and "March 30" respectively.



## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | DOB Collection  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_dob_collection_collect_month  
Parameter | [param_name] | dob  
Entity Type | prebuilt_components_[component_name]_[entity_type] | prebuilt_components_dob_collection_dob_day  
  
## Output parameters

Output parameters are session parameters that will remain active after exiting the component. These parameters contain important information collected by the component. This prebuilt component provides values for the following output parameters:

Parameter Name | Description | Output Format  
---|---|---  
dob_collection_dob | This parameter returns an object containing date of birth elements: day, month and year | 
    
    
    {  
      "year": integer,  
      "month": integer,  
      "day": integer  
    }  
  
## Basic setup

To set up this prebuilt component:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).



### Complete

Your agent and should now be set up and ready to test.

[ Previous arrow_back  Credit card statement  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-statement)

[ Next Disputes  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/disputes)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
