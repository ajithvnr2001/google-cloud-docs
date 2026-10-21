---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-number-collection/
title: Credit card number collection prebuilt component \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:42.224376+00:00
---

# Credit card number collection prebuilt component  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-number-collection/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Credit card number collection prebuilt component Stay organized with collections  Save and categorize content based on your preferences. 

This [prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component) captures an 8 to 19 digit credit card number. Captured credit card numbers are validated using the [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm).

## Limitations

In addition to the [common prebuilt component limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#limits), this prebuilt component has the following limitations:

  * Payment gateway integration is not included in the component.
  * Credit card numbers shorter than 8 or longer than 19 digits are not supported.



## Recommended agent settings

[Enable DTMF](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#dtmf) to allow users to input numeric values using the telephone keypad.

## Additional features

The following additional functionalities are provided by this prebuilt component:

  * [Repeat](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#repeat-functionality)
  * [Waiting room](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#waiting-room-functionality)
  * [Playback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#playback-functionality)



## Sample dialogs

The following sample dialogs demonstrate common scenarios handled by this prebuilt component. The sample dialogs demonstrate behavior when the component is called via telephony, which triggers the Default Welcome Intent and the first agent response at the start of the conversation.

### Single chunk

End-user provides the entire credit card number in the first turn; agent successfully validates and accepts it.

User input | Agent response  
---|---  
| Please say or enter the first part of your credit card number. You can say "play back" at any time to hear the current collected numbers.  
4242 4242 4242 4242 |   
| I got 4242424242424242, is that correct?  
yes |   
| Please say or enter the next part of your credit card number, or say "that's all" if you are done.  
That's all |   
| To do a final confirmation with you, the credit card number I have got is 4242424242424242, is that correct?  
yes |   
| Thank you, your credit card number has been successfully verified.  
  
### Multiple chunks

End-user provides credit card number in three chunks; agent validates and accepts it.

User input | Agent response  
---|---  
| Please say or enter the first part of your credit card number. You can say "play back" at any time to hear the current collected numbers.  
4242 |   
| I got 4242, is that correct?  
yes |   
| Please say or enter the next part of your credit card number, or say "that's all" if you are done.  
424242 |   
| I got 424242, is that correct?  
yes |   
| Please say or enter the next part of your credit card number, or say "that's all" if you are done.  
424242 |   
| I got 424242, is that correct?  
yes |   
| Please say or enter the next part of your credit card number, or say "that's all" if you are done.  
done |   
| To do a final confirmation with you, the credit card number I have got is 4242424242424242, is that correct?  
yes |   
| Thank you, your credit card number has been successfully verified.  
  
### Successful retry

End-user provides the entire credit card number in the first turn; agent re-confirms it but end-user says "no". Agent asks end-user to provide the input again. End-user provides and confirms the number and agent successfully validates and accepts it. 

User input | Agent response  
---|---  
| Please say or enter the first part of your credit card number. You can say "play back" at any time to hear the current collected numbers.  
5105105105105100 |   
| I got 5105105105105101, is that correct?  
no |   
| No problem, please repeat the credit card number or try saying four digits at a time  
5105105105105100 |   
| I got 5105105105105100, is that correct?  
yes |   
| Please say or enter the next part of your credit card number, or say "that's all" if you are done.  
That's all |   
| To do a final confirmation with you, the credit card number I have got is 5105105105105100, is that correct?  
yes |   
| Thank you, your credit card number has been successfully verified.  
  
### Unrecognized input

Component exits the flow after the end-user provides unrecognized input three times.

User input | Agent response  
---|---  
| Please say or enter the first part of your credit card number. You can say "play back" at any time to hear the current collected numbers.  
It's fine |   
| Sorry, I didn't get that. Can you please say or enter the credit card number again?  
It's fine |   
| Hmm, I still wasn't able to get that. Please make sure you're saying the credit card number. You can also use the keypad to enter the credit card number.  
It's fine |   
| Sorry, I'm having difficulty understanding your response.  
  
## Credit card number validation

Valid credit card numbers must be between 8 and 19 digits long. This component also validates credit card numbers using the Luhn algorithm using the [IS_CREDIT_CARD_NUMBER system function](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions#func-iscreditcardnumber).

## Naming conventions

This prebuilt component uses the following naming conventions:

Feature | Format | Example  
---|---|---  
Flow | [Component Name] | Credit Card Number Collection  
Component Specific Intent | prebuilt_components_[component_name]_[intent_name] | prebuilt_components_credit_card_number_collection_credit_card_sequence  
Parameter | [param_name] | user_provided_new_seq  
  
## Output parameters

Output parameters are session parameters that will remain active after exiting the component. These parameters contain important information collected by the component. This prebuilt component provides values for the following output parameters:

Parameter Name | Description | Output Format  
---|---|---  
credit_card_status | This parameter indicates the collected credit card number's validity using [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm):   
"valid" indicates that the collected credit card number has been successfully validated and it is between 8 and 19 digits in length  
"invalid" indicates that the collected credit card number is invalid or it is not between 8 to 19 digits in length | string  
credit_card_number_collection_credit_card_number | This parameter returns the credit card number captured by the component | string  
  
## Basic setup

To set up this prebuilt component:

  1. [Import the prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component#import).



### Complete

Your agent should now be set up and ready to test.

[ Previous arrow_back  Credit card expiration date collection  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-expiration-date-collection)

[ Next Credit card statement  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-statement)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
