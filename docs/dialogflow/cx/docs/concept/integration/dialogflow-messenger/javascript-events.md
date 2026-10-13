---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger/javascript-events/
title: Dialogflow CX Messenger JavaScript events \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:49.753284+00:00
---

# Dialogflow CX Messenger JavaScript events  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger/javascript-events/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Dialogflow CX Messenger JavaScript events Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow CX Messenger triggers a variety of events that you can create [event listeners](https://developer.mozilla.org/en-US/docs/Web/API/EventListener) for. Some events have a `detail` object field, which provides more information about the event.

## `df-messenger-loaded`

The agent dialog is first loaded.

Detail properties:

  * none



For example:
    
    
    window.addEventListener('df-messenger-loaded', () => {
      // Messenger is now ready.
    });
    

## `df-chat-open-changed`

The chat is opened or closed.

**Note:** Only active if the `df-messenger-chat-bubble` is used.

Detail properties:

  * `isOpen` (`boolean`): new state of the chat



For example:
    
    
    window.addEventListener('df-chat-open-changed', (event) => {
      console.log(`Chat is ${event.detail.isOpen ? 'open' : 'closed'}`);
    });
    

## `df-user-input-entered`

The user entered text.

Detail properties:

  * `input` (`string`): value the user entered



For example:
    
    
    window.addEventListener('df-user-input-entered', (event) => {
      console.log(event.detail.input);
    });
    

## `df-request-sent`

A request sent to the Dialogflow CX backend.

**Note:** The request can be manipulated. The changes are reflected in the request being sent. If the event's default is prevented, the request won't be sent.

Detail properties:

  * `data` (`object`): data container
  * `data.requestBody` (`object`): request that was sent



For example:
    
    
    window.addEventListener('df-request-sent', (event) => {
      console.log('Request', event.detail.data.requestBody);
    });
    
    
    
    window.addEventListener('df-request-sent', (event) => {
      event.preventDefault(); // Messenger won't send the request.
    
      // Send request yourself.
    });
    

## `df-response-received`

A response has arrived to the agent dialog.

**Note:** Messages can be manipulated, the changes will be reflected in the agent's response handling. If the event's default is prevented, the agent won't handle the response.

Detail properties:

  * `data` (`object`): data container
  * `data.messages` (`object[]`): list of [parsed response messages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment)
  * `raw` (`object`): verbatim response that was received



For example:
    
    
    window.addEventListener('df-response-received', (event) => {
      // Remove all non-text messages.
      event.detail.data.messages = event.detail.data.messages.filter(message => {
        return message.type === 'text';
      });
    });
    
    
    
    window.addEventListener('df-response-received', (event) => {
      event.preventDefault(); // Messenger won't handle the response.
    
      const messenger = document.querySelector('df-messenger');
      event.detail.data.messages.forEach(message => {
        if (message.type === 'text') {
          messenger.renderCustomText(message.text);
        }
      });
    });
    

## `df-messenger-error`

A request to the backend fails.

Detail properties:

  * `error` (`object`): error that occurred



For example:
    
    
    window.addEventListener('df-messenger-error', (event) => {
      console.log(event.detail.error);
    });
    

## `df-session-expired`

The session with the agent expired.

Detail properties:

  * none



For example:
    
    
    window.addEventListener('df-session-expired', () => {
      const messenger = document.querySelector('df-messenger');
      messenger.renderCustomText(`*Session expired*`, /* isBot= */ true);
      messenger.startNewSession({ retainHistory: true });
    });
    

## `df-session-ended`

The session has ended.

Detail properties:

  * none



For example:
    
    
    window.addEventListener('df-session-ended', () => {
      const messenger = document.querySelector('df-messenger');
      messenger.renderCustomText(`*Session ended*`, /* isBot= */ true);
      messenger.startNewSession({ retainHistory: true });
    });
    

## `df-url-suggested`

URLs of suggested resources.

Detail properties:

  * `suggestedUrls` (`string[]`): list of suggested URLs



For example:
    
    
    window.addEventListener('df-url-suggested', (event) => {
      if (event.detail.suggestedUrls.length === 1) {
        window.location.href = event.detail.suggestedUrls[0];
      }
    });
    

## `df-accordion-clicked`

User clicked the accordion.

Detail properties:

  * none



## `df-button-clicked`

User clicked a button.

Detail properties:

  * `actionLink` (`string`): anchor href of the clicked button, if specified
  * `event` (`string`): [event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-custom) of the clicked button, if specified
  * `languageCode` (`string`): language code of the event if specified, otherwise the main language code
  * `text` (`string`): text of the clicked button


    
    
    window.addEventListener('df-button-clicked', (event) => {
      event.preventDefault(); // Messenger won't send the "event" request.
    
      // Handle "event" yourself.
    });
    

## `df-chip-clicked`

User clicked a chip.

Detail properties:

  * `actionLink` (`string`): anchor href of the clicked chip, if specified
  * `text` (`string`): text of the clicked chip



## `df-citation-clicked`

User clicked a citation.

Detail properties:

  * `actionLink` (`string`): anchor href of the citation
  * `title` (`string`): title of the citation



## `df-info-card-clicked`

User clicked an info-card.

Detail properties:

  * `actionLink` (`string`): anchor href of the info-card
  * `title` (`string`): title of the info-card



## `df-list-element-clicked`

User clicked a list element.

Detail properties:

  * `actionLink` (`string`): anchor href of the list element, if specified
  * `event` (`string`): [event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-custom) of the clicked list element, if specified
  * `languageCode` (`string`): language code of the event if specified, otherwise the main language code
  * `title` (`string`): title of the list element


    
    
    window.addEventListener('df-list-element-clicked', (event) => {
      event.preventDefault(); // Messenger won't send the "event" request.
    
      // Handle "event" yourself.
    });
    

## `df-image-clicked`

User clicked an image.

Detail properties:

  * `actionLink` (`string`): anchor href of the image, if specified



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
