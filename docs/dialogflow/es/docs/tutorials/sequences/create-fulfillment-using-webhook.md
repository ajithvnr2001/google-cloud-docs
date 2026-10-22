---
url: https://docs.cloud.google.com/dialogflow/es/docs/tutorials/sequences/create-fulfillment-using-webhook/
title: Create fulfillment using webhook \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:02.451644+00:00
---

# Create fulfillment using webhook  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/tutorials/sequences/create-fulfillment-using-webhook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Create fulfillment using webhook Stay organized with collections  Save and categorize content based on your preferences. 

Webhook fulfillment in Dialogflow gives us a lot of control over the flow of our agent. In this tutorial, you need a webhook to validate the alphanumeric sequences collected in the "Sequence" intent. The webhook will loop that intent repeatedly to collect a long sequence in more manageable iterations.

## Create a webhook with the inline editor

Dialogflow has an inline editor in the console that allows you to directly write _NodeJS_ code, which then can be deployed to run as a webhook on _Cloud Functions_.

To create a webhook using Dialogflow's inline editor, follow these steps:

  1. Click the **Fulfillment** tab on the navigation bar to go to the fulfillment page. ![](https://docs.cloud.google.com/static/dialogflow/es/docs/images/tutorials/build-an-agent/build-an-agent-27.png)
  2. Toggle the inline editor's button to ENABLED. ![](https://docs.cloud.google.com/static/dialogflow/es/docs/images/tutorials/build-an-agent/build-an-agent-28.png)
  3. Delete the existing content in the `package.json` tab of the inline editor. ![](https://docs.cloud.google.com/static/dialogflow/es/docs/images/tutorials/build-an-agent/build-an-agent-29.png)
  4. Copy and paste the JSON content below to the `package.json` tab of the inline editor:
         
         {
           "name": "DialogflowFirebaseWebhook",
           "description": "Firebase Webhook dependencies for a Dialogflow agent.",
           "version": "0.0.1",
           "private": true,
           "license": "Apache Version 2.0",
           "author": "Google Inc.",
           "engines": {
             "node": "10"
           },
           "scripts": {
             "lint": "semistandard --fix \"**/*.js\"",
             "start": "firebase deploy --only functions",
             "deploy": "firebase deploy --only functions"
           },
           "dependencies": {
             "firebase-functions": "^2.0.2",
             "firebase-admin": "^5.13.1"
           }
         }
         

  5. Delete the existing code in the `index.js` tab of the inline editor. ![](https://docs.cloud.google.com/static/dialogflow/es/docs/images/tutorials/build-an-agent/build-an-agent-30.png)

  6. Copy and paste the code below to the `index.js` tab of the inline editor:
         
         /**
          * Copyright 2020 Google Inc. All Rights Reserved.
          *
          * Licensed under the Apache License, Version 2.0 (the "License");
          * you may not use this file except in compliance with the License.
          * You may obtain a copy of the License at
          *
          *      http://www.apache.org/licenses/LICENSE-2.0
          *
          * Unless required by applicable law or agreed to in writing, software
          * distributed under the License is distributed on an "AS IS" BASIS,
          * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
          * See the License for the specific language governing permissions and
          * limitations under the License.
          */
         
         'use strict';
         
         const functions = require('firebase-functions');
         
         // TODO: set this to the minimum valid length for your sequence.
         // There's no logic in here to enforce this length, but once the
         // user has said this many digits, the slot-filling prompt will
         // also instruct the user to say "that's all" to end the slot-filling.
         const MIN_SEQUENCE_LENGTH = 10;
         
         exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
           let dfRequest = request.body;
           let action = dfRequest.queryResult.action;
           switch (action) {
             case 'handle-sequence':
               handleSequence(dfRequest, response);
               break;
             case 'validate-sequence':
               validateSequence(dfRequest, response);
               break;
             default:
               response.json({
                 fulfillmentText: `Webhook for action "${action}" not implemented.`
               });
           }
         });
         
         ////
         // Helper functions
         
         /* Send an SSML response.
          * @param request: Dialogflow WebhookRequest JSON with camelCase keys.
          *     See https://cloud.google.com/dialogflow/es/docs/reference/common-types#webhookrequest
          * @param response: Express JS response object
          * @param ssml: SSML string.
          * @example: sendSSML(request, response, 'hello')
          *     Will call response.json() with SSML payload '<speak>hello</speak>'
          */
         function sendSSML(request, response, ssml) {
           ssml = `<speak>${ssml}</speak>`;
         
           if (request.originalDetectIntentRequest.source == 'GOOGLE_TELEPHONY') {
             // Dialogflow Phone Gateway Response
             // see https://cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2beta1#google.cloud.dialogflow.v2beta1.Intent.Message.TelephonySynthesizeSpeech
             response.json({
               fulfillmentMessages: [{
                 platform: 'TELEPHONY',
                 telephonySynthesizeSpeech: {ssml: ssml}
               }]
             });
           }
           else {
             // Some CCAI telephony partners accept SSML in a plain text response.
             // Check your specific integration and customize the payload here.
             response.json({
               fulfillmentText: ssml
             });
           }
         }
         
         /* Extract an output context from the incoming WebhookRequest.
          * @param request: Dialogflow WebhookRequest JSON with camelCase keys.
          *     See https://cloud.google.com/dialogflow/es/docs/reference/common-types#webhookrequest
          * @param name: A string
          * @return: The context object if found, or undefined
          * @see: https://cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2#google.cloud.dialogflow.v2.Context
          *     and note this webhook uses JSON camelCase instead of RPC snake_case.
          * @example:
          *     // Modify an existing output content
          *     let context = getOutputContext(request, 'some-context');
          *     context.lifespanCount = 5;
          *     context.parameters.some_parameter = 'new value';
          *     response.json({
          *       fulfillmentText: 'new value set',
          *       outputContexts: [context]
          *     });
          */
         function getOutputContext(request, name) {
           return request.queryResult.outputContexts.find(
               context => context.name.endsWith(`/contexts/${name}`)
           );
         }
         
         ////
         // Action handler functions
         
         /*
          * Fulfillment function for:
          *     actions: handle-sequence
          *     intents: "Sequence", "Sequence - Edit"
          * @param request: Dialogflow WebhookRequest JSON with camelCase keys.
          *     See https://cloud.google.com/dialogflow/es/docs/reference/common-types#webhookrequest
          * @param response: Express JS response object
          */
         function handleSequence(request, response) {
           let parameters = request.queryResult.parameters;
           let isSlotFilling = !request.queryResult.allRequiredParamsPresent;
           let isEditing = getOutputContext(request, 'editing-sequence');
           console.log(request.queryResult.action + ': ' + JSON.stringify(parameters));
         
           if (isSlotFilling) {
             // Prompt the user for the sequence
         
             let verbatim = `<prosody rate="slow"><say-as interpret-as="verbatim">${parameters.existing_sequence}</say-as></prosody>`;
         
             if (!parameters.existing_sequence && !parameters.new_sequence) {
               // Initial prompt
               response.json({
                 fulfillmentText: "What is your sequence? Please pause after a few characters so I can confirm as we go."
               });
             }
             else if (!isEditing) {
               // Confirm what the system heard with the user. We customize the response
               // according to how many sequences we've heard to make the prompts less
               // verbose.
               if (!parameters.previous_sequence) {
                 // after the first input
                 sendSSML(request, response,
                     `Say "no" to correct me at any time. Otherwise, what comes after ${verbatim}`);
               }
               else if (parameters.existing_sequence.length < MIN_SEQUENCE_LENGTH) {
                 // we know there are more characters to go
                 sendSSML(request, response,
                     `${verbatim} What's next?`);
               }
               else {
                 // we might have all we need
                 sendSSML(request, response,
                     `${verbatim} What's next? Or say "that's all".`);
               }
             }
             else {
               // User just said "no"
               sendSSML(request, response,
                   `Let's try again. What comes after ${verbatim}`);
             }
           }
           else {
             // Slot filling is complete.
         
             // Construct the full sequence.
             let sequence = (parameters.existing_sequence || '') + (parameters.new_sequence || '');
         
             // Trigger the follow up event to get back into slot filling for the
             // next sequence.
             response.json({
               followupEventInput: {
                 name: 'continue-sequence',
                 parameters: {
                   existing_sequence: sequence,
                   previous_sequence: parameters.existing_sequence || ''
                 }
               }
             });
         
             // TODO: CHALLENGE: consider validating the sequence here.
             // The user has already confirmed existing_sequence, so if you find a unique
             // record in your database with this existing_sequence prefix, you could send
             // a followUpEventInput like 'validated-sequence' to skip to the next part
             // of the flow. You could either create a new intent for this event, or
             // reuse the "Sequence - done" intent. If you reuse the "done" intent, you
             // could add another parameter "assumed_sequence" with value
             // "#validated-sequence.sequence", then modify the validateSequence function
             // below to customize the response for this case.
           }
         }
         
         /*
          * Fulfillment function for:
          *     action: validate-sequence
          *     intents: "Sequence - Done"
          * @param request: Dialogflow WebhookRequest JSON with camelCase keys.
          *     See https://cloud.google.com/dialogflow/es/docs/reference/common-types#webhookrequest
          * @param response: Express JS response object
          */
         function validateSequence(request, response) {
           let parameters = request.queryResult.parameters;
           // TODO: add logic to validate the sequence and customize your response
           let verbatim = `<say-as interpret-as="verbatim">${parameters.sequence}</say-as>`;
           sendSSML(request, response, `Thank you. Your sequence is ${verbatim}`);
         }
         

  7. Click **DEPLOY**.




You should now be able to test the integration by calling the agent. If you haven't already, now would be a good time to set up one of the one-click [telephony integrations](https://docs.cloud.google.com/dialogflow/docs/integrations) from our partners, or set up the Dialogflow Phone Gateway to test your agent over the phone.

## Understanding the code

As the entrypoint to the webhook, the `dialogflowFirebaseFulfillment` function here is called everytime webhook is triggered. With each request, Dialogflow sends the "action" name you specified in the Dialogflow console for an intent. The code uses this action name to determine what webhook function to call, `handleSequence` or `validateSequence`.

### Handle Sequence

`handleSequence` is the core function for this tutorial. It is responsible for all aspects of the sequence slot-filling including:

  * Speaking the initial instructions when a session first enters the intent.
  * Repeating the sequence back before prompting for the next set.
  * Telling end-users how to correct the bot.
  * Recognizing when there are enough digits for a valid sequence and telling the end-user how to finalize the input (see `MIN_SEQUENCE_LENGTH' in the code).
  * Looping the slot-filling to collect multiple partial sequences.
  * Concatenating the partial sequences together into one long sequence.



### Validate Sequence

`validateSequence` is where you'll want to add a connection to your data store to validate the final sequence and return a custom message to the user based on that data. If you are building an order lookup agent, for example, you might customize the response here to say:

`Thank you. Your order ${verbatim} will arrive on ${lookup.date} and will ${lookup.require_signature ? '' : 'not'} require a signature.`

Where `lookup` is some object you found in your data store for this order.

### Helper functions

This example does not use any Dialogflow-specific dependencies. Instead, follow the [WebhookRequest reference](https://cloud.google.com/dialogflow/es/docs/reference/common-types#webhookrequest) for what to expect in `request.body`, and the [WebhookResponse reference](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#webhookresponse) for what to respond with `response.json({...})`.

The code includes two helper functions to make it easier to:

  * Send the proper response JSON for the current platform by passing a string to `sendSSML`.
  * Look for an active Dialogflow context from the request by passing the context name to `getOutputContext`.



## Further improvement

This should get you started on using webhook for advanced use-cases. You designed an agent that can loop a sequence prompt while an end-user speaks their sequence, reassuring along the way that the virtual agent is hearing them properly.

Here are some ideas for improving the experience even more:

  * Change some of the webhook responses to match your brand. For example, instead of the generic "What is your sequence?..." prompt, you could edit the code to say "What is your order number? You can find it on ..." instead.
  * Consider adding another output context to the "Sequence - Done" intent, then create some new intents under that input context to allow users to ask follow-up questions about their order.
  * If you want to dive further into this use-case, do check out the `TODO: CHALLENGE` in the sample code above for how you might improve this experience even further for your users.



[ Previous arrow_back  Creating the sequence flow intents  ](https://docs.cloud.google.com/dialogflow/es/docs/tutorials/sequences/create-intent-with-parameters)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
