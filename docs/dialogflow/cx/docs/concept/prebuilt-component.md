---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/
title: Prebuilt components overview \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:09.009873+00:00
---

# Prebuilt components overview  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Prebuilt components overview Stay organized with collections  Save and categorize content based on your preferences. 

Prebuilt components are a collection of prebuilt flows provided by Dialogflow CX for common tasks and scenarios. They can be used to accelerate development for both new and existing agents.

There are two types of prebuilt components:

  * **Building blocks:** components that collect specific parameters, such as name and address
  * **Use cases:** components that represent larger user journeys, like making a payment, which may make use of one or more building blocks



Prebuilt component flows include [intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) and [entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity) that are ready to use. For components that require integrations with external services, you need to modify the configuration of the [flexible webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible) to integrate with the proper endpoints.

The following building block components are available:

  * [Address collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/address-collection)
  * [Alphanumeric collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/alphanumeric-collection)
  * [Credit card CVV collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-cvv-collection)
  * [Credit card expiration date collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-expiration-date-collection)
  * [Credit card number collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-number-collection)
  * [Date of birth collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection)
  * [Feedback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/feedback)
  * [Greeting](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/greeting)
  * [Name collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/name-collection)
  * [Numeric collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/numeric-collection)
  * [Telephone number collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telephone-number-collection)
  * [Waiting room](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/waiting-room)
  * [Zip code collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/zip-code-collection)



The following use case components are available:

  * [Account balance](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/account-balance)
  * [Account statement](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/account-statement)
  * [Arrange appointment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/arrange-appointment)
  * [Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication)
  * [Cancel order](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/cancel-order)
  * [Credit card enrollment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-enrollment)
  * [Credit card statement](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-statement)
  * [Disputes](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/disputes)
  * [Exchange order](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/exchange-order)
  * [Financial services steering](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/financial-services-steering)
  * [Lock card](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/lock-card)
  * [Lost and stolen card](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/lost-stolen-card)
  * [Make a payment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/make-a-payment)
  * [Offers and deals](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/offers-and-deals)
  * [Open account](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/open-account)
  * [Order status](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/order-status)
  * [Retail authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail)
  * [Retail fraud and dispute](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/fraud-and-dispute-retail)
  * [Return and refund](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/return-and-refund)
  * [Telecommunications steering](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/telecommunications-steering)
  * [Transaction history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/transaction-history)



## Limitations

The following limitations apply:

  * Prebuilt components currently only support English (en).



## Import a prebuilt component

**Note:** If your project is within a [VPC Service Controls (VPC-SC)](https://docs.cloud.google.com/vpc-service-controls/docs/overview) perimeter, you may need to add an egress rule that authorizes traffic out from the VPC-SC perimeter to the Google-owned Google Cloud Storage bucket where the latest versions of prebuilt components are stored. See VPC Service Controls below for instructions.

To import a prebuilt component to your project:

  1. Go to the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent or [create a new agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#create).
  4. Select the **Manage** tab.
  5. Click **Prebuilt** in the **Manage** panel.
  6. Click the component of interest and click **Import as flow**.
  7. Refer to each component-specific documentation to determine whether additional setup for webhook is needed.
  8. Start testing and customizing.



### VPC Service Controls

If your project is within a VPC Service Controls (VPC-SC) [perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters), you may need to add an egress rule to enable import of the latest versions of prebuilt components from the external Google-hosted Google Cloud Storage bucket where they are stored. If your VPC-SC rules prevent egress to the Google-hosted bucket, you may see an error message on import that contains "Permission denied while accessing Google Cloud Storage URI 'gs://gassets-api-ai/prebuilt_components/cx-standard-prebuilt-components/resource-name'".

To enable import, you will need to [create an egress rule](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#updating) that allows access to the external Google Cloud project containing the Google Cloud Storage bucket `gs://gassets-api-ai`. The following attributes describe the resource and operations required to enable import from the Google-owned resource:

  * **Resource:** `projects/921279757870`
  * **Service Name:** `storage.googleapis.com`
  * **Method:** `google.storage.objects.get`



## Customizations and settings

To customize the component and improve settings:

  1. Edit agent responses and [custom entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-custom) to meet your business needs.
  2. For voice agents, the following speech settings are recommended: 
     * [Change STT model](https://docs.cloud.google.com/dialogflow/docs/support/troubleshooting#stt-empty-transcripts) to `latest_short`. To see which features are supported by this model for a particular language, check [Speech-to-Text supported languages](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages).
     * Enable [auto speech adaptation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-adaptation).
  3. If you use a telephony integration that allows parameter values extracted from telephone keypad presses, enable [DTMF for telephony integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#dtmf).
  4. [Test the agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console#simulator) using the simulator.
  5. To test your component over voice, it is recommended to use [Dialogflow CX Phone Gateway](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway).



## Handle exit events

Upon successful completion of the task, a prebuilt component will exit with the END_FLOW [symbolic transition target](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#symbolic).

When a prebuilt component isn't able to complete the task, the following events will be emitted for the calling page that caused the transition to the prebuilt component flow. It is a best practice to handle these events in your agent by creating the corresponding [event handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event) in the calling page.

See [built-in events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in):

  * flow-cancelled
  * flow-failed
  * flow-failed-human-escalation



## Additional functionalities

Some prebuilt components have additional functionality. See the component-specific documentation to check which features are implemented for a particular component.

### Repeat functionality

If the end-user has difficulty interpreting the virtual agent or missed hearing an agent response, they can ask for the last prompt to be repeated.

Sample utterances:

  * _What did you just say?_
  * _Say it again._
  * _Can you please repeat?_
  * _Pardon._



### Waiting room functionality

If the end-user wants to take a minute to get back to the agent and does not have an immediate answer to a prompt, they can ask the virtual agent to hold. When the end-user is ready to continue the conversation, they can tell the agent "I'm ready" to resume the conversation. The waiting room feature is enabled in some prebuilt components by calling the waiting room prebuilt component. The waiting room feature can also be enabled anywhere in the agent by following the setup instructions as described in the [waiting room prebuilt component overview](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/waiting-room).

Sample utterances:

  * _Please wait._
  * _Wait a second._
  * _Please hold, let me check._
  * _I'm checking, wait._
  * _I'm ready now._



### Playback functionality

If the end user wants to know what the agent has collected so far, they can ask the agent to playback. The agent will then play back the currently captured parameter(s).

Sample utterances:

  * _Playback._
  * _Play it back._
  * _Play that back please?_
  * _Read that back to me._



## Common intents

Common intents are intents that are used for common behaviors in multiple components.

Common intent | Description  
---|---  
prebuilt_components_confirmation_yes | Positive phrases used to express affirmation, assent or to mark the addition of something emphasizing and amplifying a statement in response to a question or request  
prebuilt_components_confirmation_no | Negative phrases used to express dissent, denial, or refusal in response to a question or request  
prebuilt_components_confirmation_done | Phrases used to express that the end-user is done with a task or request  
prebuilt_components_escalate_human_agent | Phrases used to request that the virtual agent connect the end-user to a human agent  
prebuilt_components_start_over | Phrases used to request that the entire experience starts over from the beginning  
prebuilt_components_playback | Specific phrases to request that the currently collected input is played back to the end-user so that the end-user can give confirmation  
prebuilt_components_replay | Phrases used to request that the previous prompt is said again  
prebuilt_components_waiting_room | Phrases used to express the need for time to review, find or provide information in response to a question or request  
prebuilt_components_ready | Phrases used to notify the virtual agent that the end-user would like to continue an action  
  
[ Previous arrow_back  Generative fallback  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative-fallback)

[ Next Account balance  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/account-balance)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
