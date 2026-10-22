---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-consumer-privacy/
title: Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:31.106967+00:00
---

# Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-consumer-privacy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

## Consumer privacy

SMS Chat introduces unique obligations related to consumer privacy and it's important to train both managers and agents on the appropriate handling of SMS Chat sessions.

### Opting in

Consumers must consent to receiving SMS messages by opting in. When the consumer initiates a chat, they are assumed to have opted in but you still need to send a message that includes the following information:

  * Brand or product name

  * "Recurring messages" disclosure

  * "Message and data rates may apply" disclosure

  * Opt-out instructions




This can be achieved by composing an opt-in "greeting message" that is sent automatically when the first chat message is received.

Similarly, for outbound SMS messages, the agent should always initiate the session with an opt-in message. This can be achieved by setting up a chat shortcut.

### Unsubscribing and Do Not Contact list

A consumer can stop all future SMS messages by sending one of these default command words: STOP, STOPALL, UNSUBSCRIBE, CANCEL, END, QUIT.

These commands are not case sensitive but the word must be complete and the message cannot include any extra spaces or characters. The consumer can send the command at any time by texting the word to your SMS phone number or short code.

When the consumer opts out, their phone number is added to an encrypted "Do Not Contact" list maintained by CCAI Platform. The only phone number added to the list is the one used by the consumer to send the STOP command (even if the consumer has multiple phone numbers in their CRM record.)

For detailed information on the rules and regulations surrounding SMS messaging, refer to the [CTIA Short Code Monitoring Handbook v1.7](https://www.wmcglobal.com/storage/us_resources/ctia-short-code-monitoring-program-Short-Code-Monitoring-Handbook-v1.7.pdf).

When a consumer opts out of receiving future messages:

  1. The chat ends immediately and the agent adapter displays a message to the agent.

  2. The agent makes an entry in the CRM record, indicating that the consumer has opted out.

  3. CCAI Platform adds the consumer's phone number to a "Do Not Contact" list. If an agent tries to use the number, an error message is displayed.

  4. The consumer can opt back in at any time by texting START to any of the incoming SMS numbers.




When using outbound SMS, it is imperative that agents send an opt-in message before sending any other text to the consumer. The easiest way to achieve this is by using a chat shortcut. In this example, the agent types **/sms** to send a standard opt-in message:

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
