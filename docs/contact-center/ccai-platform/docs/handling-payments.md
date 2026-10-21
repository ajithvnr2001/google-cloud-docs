---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/handling-payments/
title: Handling Payments \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:37.994402+00:00
---

# Handling Payments  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/handling-payments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Handling Payments Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) provides the ability to handle payments from end-users through integration with secure payment services.

## Secure Payments: Handling Payments Over the Phone

The Secure Payments feature allows for payments to be made over the phone through a flow without the agent on the line during the transaction. As an Agent, you initiate the payment process and follow along using the agent adapter as the consumer progresses through.

### Agent experience

Once the payment action has been initiated, the caller is placed into a payment flow, which is a series of prompts. As an Agent, you should tell the caller what to expect and to have their credit card and associated billing information handy. Once you initiate the action, the caller won't be able to hear you, and you won't be able to hear them or anything they enter.

  1. From the Agent Adapter, click **Actions > Request Payment** to bring up the Payment Request form.

If you click before you are ready, you can click the exit button (X) to cancel the payment request.

  2. Enter the name of the item the caller is purchasing.

  3. Enter the total item amount to pay (including tax and shipping when applicable).

  4. Click **Send to Pay** to prompt the caller to begin the payment process.

**Note:** Agents will hear hold music and the caller will hear prompts for the following:
  5. **Entering status** : You are able to see when a caller is filling out each payment step.

  6. **Complete** : The payment step shows a green checkmark.

  7. **Payment Success** : If entered correctly, agents see a successful payment notification.

**Note:** At this point, agents are taken off of hold and returned to the call.

  8. **Payment status** : A comment or activity with the following information is posted in the CRM record:

Agent: [Agent's name]

Product Name: [Product Name as entered by the agent]

Transaction ID: [Transaction ID auto-generated]

Amount Charged: [$XX.XX]

Payment Status: [Success / Failed]

Timestamp: [Year-Month-Day Hour:Minute:Second]

  9. **Next Steps** : Follow your company's procedures following a completed payment.




### Caller experience

Once the payment is initialized by an Agent, the caller hears the following voice prompts. After every entry, the customer is told to press 1 to confirm their entry or to press 2 to re-enter the information for the following:

  1. **Total amount confirmed** : Confirms or denies the amount entered by the agent.

  2. **Credit Card Number** : Enters their credit or debit card information.

  3. **Expiry Date** : Enters the expiration date on their credit or debit card.

  4. **CVC Code** : Enters the three or four-digit code located on the back of their card.

  5. **Zip Code** : The customer enters the zip code associated with their billing address.

  6. **Fail/Success Message** : A message shown that indicates if the payment transaction was successful or failed.

**-** Failure occurs if the customer typed in incorrect information too many times or if they waited more than 60 seconds with no input following a voice prompt request.

**-** Consumers can press * to cancel the payment process and return to the call.




The consumer is reconnected with the agent after success or failure of the payment input.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
