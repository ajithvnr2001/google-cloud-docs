---
url: https://docs.cloud.google.com/dialogflow/es/docs/entities-session/
title: Session entities \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:38.190310+00:00
---

# Session entities  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/entities-session/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Session entities Stay organized with collections  Save and categorize content based on your preferences. 

A _session_ represents a conversation between a Dialogflow agent and an end-user. You can create special entities, called _session entities_ , during a session. Session entities can extend or replace custom entity types and only exist during the session that they were created for. All session data, including session entities, is stored by Dialogflow for 20 minutes.

For example, if your agent has a `@fruit` entity type that includes "pear" and "grape", that entity type could be updated to include "apple" or "orange", depending on the information your agent collects from the end-user. The updated entity type would have the "apple" or "orange" entity entry for the rest of the session.

## Creating session entities with fulfillment

You can create session entities with [fulfillment](https://docs.cloud.google.com/dialogflow/docs/fulfillment-overview). The [`WebhookResponse`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#webhookresponse) type contains a field called `sessionEntityTypes` that is used to set session entities.

The following examples show how to set a `fruit` entity type's entity entries to `apple` and `orange` for the current session.

### Example WebhookResponse:
    
    
    {
      "fulfillmentMessages": [
        {
          "text": {
            "text": [
              "Choose apple or orange"
            ]
          }
        }
      ],
      "sessionEntityTypes":[
        {
          "name":"projects/project-id/agent/sessions/session-id/entityTypes/fruit",
          "entities":[
            {
              "value":"APPLE_KEY",
              "synonyms":[
                "apple",
                "green apple",
                "crabapple"
              ]
            },
            {
              "value":"ORANGE_KEY",
              "synonyms":[
                "orange"
              ]
            }
          ],
          "entityOverrideMode":"ENTITY_OVERRIDE_MODE_OVERRIDE"
        }
      ]
    }
    

### Example using the Actions on Google client library:

If you are using the [Actions on Google client library](https://github.com/actions-on-google/actions-on-google-nodejs), you can use the [Session Entities plugin](https://github.com/actions-on-google/dialogflow-session-entities-plugin-nodejs).

Your code would look similar to the following:
    
    
    const { sessionEntitiesHelper } = require('actions-on-google-dialogflow-session-entities-plugin')
    
    const app = dialogflow()
        .use(sessionEntitiesHelper())
    
    app.intent('input.welcome', (conv) => {
      conv.ask('make your choice: apple or orange?');
      // Set the fruit session entity values to 'apple' and 'orange'.
      conv.sessionEntities.add({
        name: 'fruit',
        entities: [{
          value: 'APPLE_KEY',
          synonyms: [
            'apple', 'green apple', 'crabapple'
          ]
        }, {
          value: 'ORANGE_KEY',
          synonyms: ['orange']
        }]
      });
      conv.sessionEntities.send();
    });

## Creating session entities with the API

**Note:** Session entity API methods do not work with Google Assistant integration. Use the fulfillment option for Google Assistant integration.

You create, manage, and update session entities using the [`SessionEntityTypes`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#sessionentitytypes) type.

[ Previous arrow_back  Custom entities  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-custom)

[ Next Regexp entities  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-regexp)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
