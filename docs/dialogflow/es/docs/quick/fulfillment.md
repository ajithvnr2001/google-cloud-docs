---
url: https://docs.cloud.google.com/dialogflow/es/docs/quick/fulfillment/
title: Quickstart: Fulfillment \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:35.246666+00:00
---

# Quickstart: Fulfillment  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/quick/fulfillment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Quickstart: Fulfillment Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to integrate your agent with your services using [fulfillment](https://docs.cloud.google.com/dialogflow/docs/fulfillment-overview). Integrating your service allows you to take actions based on end-user expressions and send dynamic responses back to the end-user.

**Note:** If you are using Google Assistant, check options on the [Google Assistant](https://docs.cloud.google.com/dialogflow/es/docs/integrations/aog) page.

## Before you begin

If you don't plan on using fulfillment, you can skip this quickstart.

These steps use [Cloud Functions](https://docs.cloud.google.com/functions/docs) and assume basic Node.js knowledge. If you want to create fulfillment using your own server or another language, see the more detailed [fulfillment documentation](https://docs.cloud.google.com/dialogflow/docs/fulfillment-overview).

You should do the following before reading this guide:

  1. Read [Dialogflow basics](https://docs.cloud.google.com/dialogflow/docs/basics).
  2. Perform [setup steps](https://docs.cloud.google.com/dialogflow/docs/quick/setup).
  3. Perform steps in the [Build an agent](https://docs.cloud.google.com/dialogflow/docs/quick/build-agent) quickstart guide. Steps below continue working on the same agent. If you no longer have that agent, you can download [`build-agent-quickstart.zip`](https://docs.cloud.google.com/static/dialogflow/es/docs/data/build-agent-quickstart.zip) and [import the file](https://docs.cloud.google.com/dialogflow/docs/agents-settings#export).



## The inline editor

The Dialogflow Console has a built-in code editor, called the [inline editor](https://docs.cloud.google.com/dialogflow/docs/fulfillment-inline-editor) that you can use to create fulfillment code and deploy the code to [Cloud Functions](https://docs.cloud.google.com/functions/docs). Cloud Functions has associated charges, but the service is available for no charge up to a [significant number of monthly invocations](https://docs.cloud.google.com/functions/pricing). Note that you still must register and provide a valid billing account. Cancel anytime. 

When you initially enable the inline editor, Node.js fulfillment code is pre-populated with default handlers for [default intents](https://docs.cloud.google.com/dialogflow/docs/intents-default) that are included for all agents. The code also has commented instructions for adding handlers for developer-defined intents. 

The inline editor is intended for simple fulfillment testing and prototyping. Once you are ready to build a production application, you should create a [webhook service](https://docs.cloud.google.com/dialogflow/docs/fulfillment-webhook). 

## Enable and deploy fulfillment with the Inline Editor

To enable and deploy the default fulfillment code using the Inline Editor:

  1. Click **Fulfillment** in the left sidebar menu.
  2. Toggle the **Inline Editor** to **Enabled**.
  3. If you did not [enable billing in setup steps](https://docs.cloud.google.com/dialogflow/docs/quick/setup#billing), you are prompted to enable billing now. Cloud Functions has associated charges, but the service is available for no charge up to a [significant number of monthly invocations](https://cloud.google.com/functions/pricing). Note that you still must register and provide a billing account. Cancel anytime.
  4. Click **Deploy** at the bottom of the form, and wait until dialogs indicate that it has been deployed.



For each intent that requires fulfillment, you must enable fulfillment for the intent. To enable fulfillment for the Default Welcome Intent:

  1. Click **Intents** in the left sidebar menu.
  2. Click **Default Welcome Intent**.
  3. Scroll down to the **Fulfillment** section and toggle **Enable webhook call for this intent** on.

**Note:** Enabling fulfillment overrides responses set in the **Responses** section of the intent. If fulfillment fails, the entries in the **Responses** section will be used.
  4. Click the **Save** button and wait until the **Agent Training** dialog indicates that training is complete. 




Now you can test your fulfillment in the simulator. Enter `Hi` in the simulator, and it responds with `Welcome to my agent!`. This response is sent from the fulfillment webhook you just deployed. In particular, the response came from this code:
    
    
    function welcome(agent) {
      agent.add(`Welcome to my agent!`);
    }
    

## Create a custom fulfillment handler

The steps above use a handler supplied by the default inline editor code. To create a custom handler:

  1. Enable fulfillment for the `get-agent-name` intent you created in previous steps.
  2. Click **Fulfillment** in the left sidebar menu, and examine the code in the inline editor.
  3. Find this line:
         
         exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
         

The `onRequest` function handles all requests from Dialogflow. Within the body of this function, specific handler functions are defined. These handler functions are invoked when associated intents are matched. For example, the function used in the previous section is `function welcome(agent)`.

  4. Below the existing handlers, add this function for the `get-agent-name` intent:
         
         function getAgentNameHandler(agent) {
           agent.add('From fulfillment: My name is Dialogflow!');
         }
         

  5. Below the handler function definitions, there are `intentMap.set()` calls. These calls associate specific handlers with intents by name. For example, `intentMap.set('Default Welcome Intent', welcome)` associates the `welcome` handler with the intent named `Default Welcome Intent`.

  6. Below the existing `intentMap.set` calls, add this line for the `get-agent-name` intent:
         
         intentMap.set('get-agent-name', getAgentNameHandler);
         

  7. Click **Deploy** at the bottom of the form.

  8. Enter `What's your name?` in the simulator. The `From fulfillment: My name is Dialogflow!` response is sent from your new handler.




## Access parameter values

In previous steps, you created a `set-language` intent to identify human and programming languages. The intent uses the `language` and `language-programming` parameters. In this section, you access values for these parameters in your fulfillment handler.

To add the handler:

  1. Enable fulfillment for the `set-language` intent.
  2. Click **Fulfillment** in the left sidebar menu.
  3. Similar to steps above, add the following handler and `intentMap` call:
         
         function languageHandler(agent) {
             const language = agent.parameters.language;
             const programmingLanguage = agent.parameters['language-programming'];
             if (language) {
                 agent.add(`From fulfillment: Wow! I didn't know you knew ${language}`);
             } else if (programmingLanguage) {
                 agent.add(`From fulfillment: ${programmingLanguage} is cool`);
             } else {
                 agent.add(`From fulfillment: What language do you know?`);
             }
         }
         
         
         intentMap.set('set-language', languageHandler);
         

  4. Click **Deploy**.




This handler retrieves the parameters `language` and `language-programming` and stores them in variables. It retrieves these values from the `agent.parameters` attribute, which is an object that contains all of the parameter names and values that end-users specify in their requests.

To try it, enter `I know how to speak German` in the simulator.

[ Previous arrow_back  Build an agent  ](https://docs.cloud.google.com/dialogflow/es/docs/quick/build-agent)

[ Next Interactions with an integration  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/quick/integration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
