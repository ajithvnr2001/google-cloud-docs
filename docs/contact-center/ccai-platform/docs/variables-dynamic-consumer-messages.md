---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/variables-dynamic-consumer-messages/
title: Variables for dynamic consumer messages \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:59.495712+00:00
---

# Variables for dynamic consumer messages  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/variables-dynamic-consumer-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Variables for dynamic consumer messages Stay organized with collections  Save and categorize content based on your preferences. 

Variables are dynamic content tags that allow you to personalize messaging configuration in order to manage secure payments, configure greeting and after-hours messaging, and inform customers of their wait time and place in queue.

**Important:** Variables can only be used for specific channels and message configuration. The CVC variable, for example, can only be used when creating IVR payment flow messaging.

## IVR

The following variables can be used in IVR specific messages.

Messages can be created at **Settings > Languages and Messages > IVR-specific Messages**.

### @{ESTIMATED_WAIT_TIME_IN_MINUTES}

Description: the numerical value for minutes and / or hours for the current estimated queue wait time is inserted. This message can be used in the greeting and deflection messages.

After the numerical value, the word `Minutes` will be appended and will be translated to the associated language.

Sample Input

**English** :`A representative will be with you ASAP. The current estimated wait is @{ESTIMATED_WAIT_TIME_IN_MINUTES}.`

### @{QUEUE}

Description: this is the name of queue the consumer selected. This message can be used in the IVR menu as well as in overcapacity and voicemail.

Sample input

`We're assigning a representative to help you with @{QUEUE}`

## Secure Payments

The following variables can be used for secure payments messaging.

Messages can be created at **Settings > Languages and Messages > IVR Purchase Flow Messages**.

To create a complete purchase flow messaging using variables see [IVR Purchase Flow Messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ivr-purchase-flow-messages#UUID-1ed7ab28-cbc0-ac39-3ad9-2478e29dde19).

### @{CREDIT_CARD}

Description: inserts the credit card number entered by the customer.

Sample input

`Your credit card number is @{CREDIT_CARD}. Please press 1 to confirm, press 2 to try again.`

### @{CVC}

Description: inserts the CVC code as entered by the consumer.

Sample input

`Your CVC code is @{CVC}. Please press 1 to confirm, press 2 to try again.`

### @{EXPIRY_DATE}

Description: inserts the expiry date as entered by the consumer.

Sample Input

`Your expiry date is @{EXPIRY_DATE}. Please press 1 to confirm, press 2 to try again.`

### @{TOTAL_AMOUNT}

Description: inserts the total purchase amount including taxes and shipping.

Sample Input

`The total purchase amount including taxes and shipping is @{TOTAL_AMOUNT}. Please press 1 to confirm, press 2 if it is the incorrect product or price. If you would like to return to the agent at any time please press the star key.`

### @{ZIP_CODE}

Description: inserts the zip code as entered by the consumer.

Sample Input

`Your Zip Code is @{ZIP_CODE}. Please press 1 to confirm, press 2 to try again.`

## Chat

Variables can be used to customize the default greeting and after-hours messaging for the Chat channel. For more information, see [Customizing Mobile and Web SDK Messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/customize-mobile-web-messages#customize-mobile-and-web-messages).

The following variables are available for Chat.

### @{END_USER}

Description: inserts the full name of the consumer.

**Important:** This variable is limited by the amount of information CCAI Platform can pass from your Web or Mobile SDK.

If you have the Web SDK configured on an unauthenticated page (no login required by the consumer) CCAI Platform will not be able to pass individual information about the consumer.

When authenticated, the consumer's first and last name is shown.

When unauthenticated, the term `Customer` is shown.

Sample input

`Hi @{END_USER}, thank you for contacting us.`

### @{AGENT}

Description: inserts the first name of the Agent.

### @{QUEUE_SIZE}

Description: this is the position in queue; the numerical value representing the current total number of consumers waiting in queue including the consumer seeing the number is inserted.

When configuring the message, add the `supporting label` to the end of the variable in the associated language. For the example below, we added `in line`.

Sample input

`A representative will be with you ASAP. You are number @{QUEUE_SIZE} in line.`

### @{TIME_UNTIL_DISMISSAL}

Description: this variable contains the remaining time until the chat is dismissed.

For example, when the Chat dismissal timer = 3min, the dismissal notification timer = 1min TIME_UNTIL_DISMISSAL will insert 2.

When configuring this message, add the `supporting label` to the end of the variable in the associated language (minute(s)).

Sample Input

`Are you still there? Please respond in the next @{TIME_UNTIL_DISMISSAL} minute(s) or the chat session will be closed.`

## SMS, Social

The following variables are available for SMS, Social (currently only WhatsApp is available).

Pre-defined SMS messages can be created at **Settings > Languages and Messages > Pre-session SMS Deflection**

Global messages for WhatsApp can be created at **Settings > Languages and Messages > WhatsApp**

### @{COMPANY_NAME}

Description: inserts the company name as defined in **Support Center Details > Display Name**. This is part of the SMS preset message.

Sample input

`Thank you for contacting @{COMPANY_NAME}. We're assigning a representative to help you.`

### @{END_USER}

Description: inserts the full name of the consumer.

**Important:** This variable is limited by the amount of information CCAI Platform can pass from your Web or Mobile SDK.

If you have the Web SDK configured on an unauthenticated page (no login required by the consumer) CCAI Platform will not be able to pass individual information about the consumer.

When authenticated, the consumer's first and last name is shown.

When unauthenticated, the term `Customer` is shown.

Sample input

`Hi @{END_USER}, thank you for contacting us.`

### @{QUEUE_NAME}

Description: this is the name of queue the consumer selected.

**Note:** This if for **SMS** and **Social** **only** , for IVR and Chat use @{QUEUE}

Sample input

`We're assigning a representative to help you with @{QUEUE_NAME}`

### @{TIME_UNTIL_DISMISSAL}

Description: this variable contains the remaining time until the chat is dismissed.

For example, when the Chat dismissal timer = 3min, the dismissal notification timer = 1min TIME_UNTIL_DISMISSAL will insert 2.

When configuring this message, add the `supporting label` to the end of the variable in the associated language (minute(s)).

Sample Input

`Are you still there? Please respond in the next @{TIME_UNTIL_DISMISSAL} minute(s) or the chat session will be closed.`

## Operation Hours

The following variable can be used to automatically display opening time based on operation hours.

### @{NEXT_REOPEN_HOUR}

Description: include this variable to automatically display opening time based on operation hours. display opening time based on operation hours set globally or per-queue (operation hours that apply to the queue the message is sent in). This is part of the SMS preset message.

**Note:** If there's a queue level override, operation hours for the queue will display.

Sample Input

`Please try again tomorrow as we are closed today. We will open at @{NEXT_REOPEN_HOUR}.`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
