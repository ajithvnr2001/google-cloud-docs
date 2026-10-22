---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger/javascript-functions/
title: Dialogflow CX Messenger JavaScript \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:36.851205+00:00
---

# Dialogflow CX Messenger JavaScript  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger/javascript-functions/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Dialogflow CX Messenger JavaScript Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow CX Messenger provides [functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions) you can call to affect its behavior.

**Note:** Before calling any of these functions, make sure that the `df-messenger` element is loaded by listening for the `df-messenger-loaded` event.

## `renderCustomText`

This function renders a text message, as if it came from the agent or was user entered.

Arguments:

  * `string`: text message
  * `boolean`: true for a message from agent, false from end-user



Returns:

  * `void`



For example:
    
    
    const dfMessenger = document.querySelector('df-messenger');
    dfMessenger.renderCustomText('Custom text', true);
    

## `renderCustomCard`

This function renders a custom card as if it came from Dialogflow CX fulfillment.

Arguments:

  * `payload`: a list of custom payload responses, which are defined in the [Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger/fulfillment) section



Returns:

  * `void`



For example:
    
    
    const dfMessenger = document.querySelector('df-messenger');
    const payload = [
      {
        "type": "info",
        "title": "Info item title",
        "subtitle": "Info item subtitle",
        "image": {
          "rawUrl": "https://example.com/images/logo.png"
        },
        "anchor": {
          "href": "https://example.com",
          "target": "_blank"
        }
      }
    ];
    dfMessenger.renderCustomCard(payload);
    

## `sendQuery`

This function sends a query to the Dialogflow CX API and waits for the response. This simulates an end-user input that is normally provided to the agent dialog. The system handles the response like any end-user query.

Arguments:

  * `string`: text query



Returns:

  * `Promise<void>`: return value for the asynchronous operation



For example:
    
    
    const dfMessenger = document.querySelector('df-messenger');
    dfMessenger.sendQuery('Describe shipping costs.');
    

## `sendRequest`

This function sends a request to the Dialogflow CX API and waits for the response.

Arguments:

  * `string`: request type, supports `query` (see also `sendQuery` preceding) and `event` (see [custom event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-custom))
  * `any`: payload that corresponds to the request type, which is a string for both supported request types



Returns:

  * `Promise<void>`: return value for the asynchronous operation



For example:
    
    
    const dfMessenger = document.querySelector('df-messenger');
    dfMessenger.sendRequest('query', 'Describe shipping costs.');
    

## `setQueryParameters`

This function sets default values for the [queryParams](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/detectIntent) field of the Dialogflow CX API `detectIntent` request. Other Dialogflow CX Messenger methods can replace respective default values in the query parameters.

Arguments:

  * `object`: JSON data. For schema of query parameters, see [QueryParameters](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters).



Returns:

  * `void`



For example:
    
    
    const dfMessenger = document.querySelector('df-messenger');
    const queryParameters = {
      parameters: {
      timeZone: "America/New_York"
      }
    };
    dfMessenger.setQueryParameters(queryParameters);
    

## `setContext`

This function sends [generative personalization](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/performance#personalization) information from the end-user to Dialogflow CX. This information persists for the remainder of the session.

Arguments:

  * `object`: JSON data, see generative personalization documentation



Returns:

  * `void`



For example:
    
    
    const dfMessenger = document.querySelector('df-messenger');
    const metadata = {
      "subscription plan": "Business Premium Plus",
      "devices owned": [
        {
          model: "Google Pixel 7",
        },
        {
          model: "Google Pixel Tablet",
        },
      ],
    };
    dfMessenger.setContext(metadata);
    

## `clearStorage`

This function clears the persistent storage of the agent dialog. It also clears the current state of the agent dialog. By default, it preserves the user's authentication status. You can use the optional `args` to customize this behavior.

Arguments:

Name | Type | Description  
---|---|---  
`args` | `object?` | Optional argument to configure the clear storage operation.  
`args.clearAuthentication` | `boolean?` | Optional flag to clear the authentication status. If set to true the authentication status will be cleared, otherwise it will be kept.  
  
Returns:

  * `void`



For example:
    
    
    const dfMessenger = document.querySelector('df-messenger');
    dfMessenger.clearStorage();
    

## `clearAuthentication`

This function clears the authentication of the agent dialog.

Arguments:

  * none



Returns:

  * `void`



For example:
    
    
    const dfMessenger = document.querySelector('df-messenger');
    dfMessenger.clearAuthentication();
    

## `startNewSession`

This function starts a new session inside the agent dialog. By default, it clears the message history but preserves the user's authentication status. Customize this behavior by using the optional `args` parameter.

Arguments:

Name | Type | Description  
---|---|---  
`args` | `object?` | Optional argument to configure the new session creation.  
`args.retainHistory` | `boolean?` | Optional flag to retain history. If set to true the history will be kept, otherwise it will be erased.  
`args.clearAuthentication` | `boolean?` | Optional flag to clear the authentication status. If set to true the authentication status will be cleared, otherwise it will be kept.  
  
Returns:

  * `void`



For example:
    
    
    const dfMessenger = document.querySelector('df-messenger');
    dfMessenger.startNewSession({ retainHistory: true });
    

## `openChat`

Call this function on the `df-messenger-chat-bubble` element to open the chat. It doesn't do anything if the chat is already open.

Arguments:

  * none



Returns:

  * `void`



For example:
    
    
    const dfMessengerBubble = document.querySelector('df-messenger-chat-bubble');
    dfMessengerBubble.openChat();
    

## `closeChat`

This function closes the chat. Call it on the `df-messenger-chat-bubble` element to close the chat. Does nothing if the chat is already closed.

Arguments:

  * none



Returns:

  * `void`



For example:
    
    
    const dfMessengerBubble = document.querySelector('df-messenger-chat-bubble');
    dfMessengerBubble.closeChat();
    

## `openMinChat`

![Dialogflow CX Messenger minimized chat](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/dialogflow-messenger-minimized.png)

You can open the chat window in a minimized version by calling this function on the `df-messenger-chat-bubble` element. This function does nothing if the chat is already minimized.

Arguments:

Name | Type | Description  
---|---|---  
`args` | `object?` | Optional argument to configure the minimized chat.  
`args.anchor` | `string?` | Optional `anchor` to configure where the minimized chat is being opened. Same logic as the `anchor` attribute on the chat bubble element. Defaults to `left-top`.  
`args.showActorImages` | `boolean?` | Optional flag to show actor images (if specified on the `df-messenger-chat-bubble` element). Defaults to false.  
  
Example:
    
    
    const dfMessengerChatBubble = document.querySelector('df-messenger-chat-bubble');
    dfMessengerChatBubble.openMinChat({
      anchor: 'top-left'
    });
    

## `closeMinChat`

Call this function on the `df-messenger-chat-bubble` element to close the minimized chat. It doesn't do anything if the chat is already closed.

Example:
    
    
    const dfMessengerChatBubble = document.querySelector('df-messenger-chat-bubble');
    dfMessengerChatBubble.closeMinChat();
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
