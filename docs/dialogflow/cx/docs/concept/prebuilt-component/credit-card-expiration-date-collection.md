---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-expiration-date-collection/
title: Credit card expiration date collection prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:04.307584+00:00
---

# Credit card expiration date collection prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-expiration-date-collection/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Credit card expiration date collection prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

This [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) captures a credit card expiration date from an end-user.

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * Payment gateway integration is not included in this component.



## Recommended agent settings

[Enable DTMF](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#dtmf) to allow users to input numeric values using the telephone keypad.

## Additional functionalities

The following additional functionalities are provided by this prebuilt component:

  * [Repeat](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#repeat-functionality)
  * [Waiting room](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#waiting-room-functionality)
  * [Playback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#playback-functionality)



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Successful input

End-user provides expiration date in the first attempt; agent successfully accepts it.

User input | Agent response  
---|---  
| Please say or enter the credit card's expiration date, starting with the month followed by the year.  
01/27 |   
| I have received the credit card's expiration date as January 2027. Is that correct?  
yes |   
| Great, I'm done with collecting the credit card's expiration date.  
  
### Retries

End-user provides expiration date in the first attempt; On agent's re-confirmation on collected expiration date; end-user says "it's wrong". Agent asks the end-user to confirm which part of the expiration date is incorrect - entire date, month or year and re-prompts to provide that details again. 

User input | Agent response  
---|---  
| Please say or enter the credit card's expiration date, starting with the month followed by the year.  
01/27 |   
| I have received the credit card's expiration date as January 2027. Is that correct?  
It's wrong |   
| Sorry I didn't get that right. Please let me know if you want to change the entire date or if you would like to change the month or year instead?  
month |   
| Sorry about that. Please say or enter your credit card's expiration month.  
feb |   
| I have received the credit card's expiration month as February. Is that correct?  
yes |   
| I have received the credit card's expiration date as February 2027. Is that correct?  
yes |   
| Great, I'm done with collecting the credit card's expiration date.  
  
### Partial input

Scenario - End-user isn't able to provide expiration date in the first attempt; agent splits the expiration date and asks for a month followed by year. End-user provides the input correctly this time and agent successfully accepts it.

User input | Agent response  
---|---  
| Please say or enter the credit card's expiration date, starting with the month followed by the year.  
13 |   
| Sorry, the expiration date does not look quite right. Let's try capturing the month again.  
  
Please say or enter your credit card's expiration month.  
1 |   
| I have received the credit card's expiration month as January. Is that correct?  
Yes, right |   
| Please say or enter your credit card's expiration year.  
26 |   
| I have received the credit card's expiration year as 2026. Is that correct?  
yes |   
| I have received the credit card's expiration date as January 2026. Is that correct?  
yes |   
| Great, I'm done with collecting the credit card's expiration date.  
  
### Unrecognized input

Component exits the flow after the end-user provides unrecognized input three times.

User input | Agent response  
---|---  
| Please say or enter the credit card's expiration date, starting with the month followed by the year.  
It's fine |   
| Sorry, I didn't get that. Can you please say or enter the credit card's expiration date again?  
nice |   
| Hmm, I still wasn't able to get that. Please make sure you're saying the credit card's expiration date. You can also use the keypad to enter the credit card's expiration date.  
good |   
| Sorry, I'm having difficulty understanding your response.  
  
## Credit card expiration date validation

Credit card expiration date months should be input as an integer between '01' and '12' or a string representing a month between 'January' and 'December'.

Credit card expiration date year should be four digits long. If the input is two digits long, it is converted to a four-digit year, e.g. '25' becomes '2025'. Additionally, the year should be no more than 10 years in the future from the current year.

The credit card expiration date, including month and year, must be a future date considering the current month and year.

## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Credit Card Expiration Date Collection  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_credit_card_expiration_date_collection_collect_date  
Entity Type | prebuilt_components_[component_name]_[entity_type_name] | prebuilt_components_credit_card_expiration_date_collection_month  
Parameter | [param_name] | expiration_date  
  
## Output parameters

Output parameters are session parameters that will remain active after exiting the component. These parameters contain important information collected by the component. This prebuilt component provides values for the following output parameters:

Parameter Name | Description | Output Format  
---|---|---  
credit_card_expiration_date_collection_credit_card_expiration_date | This parameter returns the object of expiration element types that will be captured during the conversation flow session | 
    
    
    {  
      "year": integer,  
      "month": integer  
    }  
  
## Basic setup

To set up this prebuilt component:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).



### Complete

Your agent should now be set up and ready to test.

[ Previous arrow_back  Credit card enrollment  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-enrollment)

[ Next Credit card number collection  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-number-collection)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
