---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/ingest/how-to-create-a-source-message-class/
title: Create a source message class \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:45.648250+00:00
---

# Create a source message class  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/ingest/how-to-create-a-source-message-class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a source message class

This guide describes how to create a [source message class](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/source-message-class) for the Manufacturing Data Engine (MDE).

## Source message class modelling

Source messages classes should be defined to capture a set of source messages that share a common structure.

The more specific you design your source message classes, the fewer conditional statements you need to write in your _Whistle_ scripts to handle schema differences between different source messages. However, creating more specific source message classes comes at the expense of requiring more parsers.

Therefore, modeling source message classes involves finding the right balance between, on one hand, having source message classes with uniform message schemas and, on the other hand, the number of parsers you need to manage.

## Source message class creation

This section outlines the process of creating a source message class using either API calls or the console interface.

**Important:** As of MDE release 1.4.1 and later versions, the Pub/Sub message headers are stored in a reserved attribute called `mdeHeaders`. The existing message-classes from previous releases that used expressions like `#root.headers['SOME_ATTRIBUTE']` will continue to work for a limited number of future releases before it's deprecated. Make sure that you update your message-class expressions to use `#root.mdeHeaders['SOME_ATTRIBUTE']` instead.

### REST

`POST /configuration/v1/message-classes`
    
    
    {
      "name": "MESSAGE_CLASS_NAME",
      "MESSAGE_CLASS_NAME": "PRIORITY",
      "expression": "SPEL_EXPRESSION"
    }
    

Replace the following:

  * `MESSAGE_CLASS_NAME`: the name of the message class to be created.
  * `PRIORITY`: the priority of the message class. The priority of a message class is an integer from 0 to 65535 , inclusive. Lower integers indicate higher priorities.
  * `SPEL_EXPRESSION`: the SpEL expression defining the message class. For example `#root.event['value'] instanceof T(Number)`



### Console

  1. Open the **'MESSAGE CLASSES'** section of the UI to create a **Source Message Class**. A list of all available **Message Classes** is displayed in this section of the UI:

![Message Classes – List Messages](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-message-classes-list.png)

For each Message Class the following parameters are displayed in the List:

     * **Message Class Name** : the name of the Message Class. Has to be unique.
     * **Message Class Expression** : the actual SpEL expression associated to the Message Class.
     * **Priority** : the priority of the Message Class (lower numbers represent higher priorities).
     * **Enabled** : the status of the message classes. Disabled Message Classes won't be part of the ingestion.
     * **Actions** : a contextual button providing access to the **'View / Edit'** function and the '**Enable / Disable'** functions for the selected Message Class.
  2. To add a new **Message Class** click the **'ADD NEW MESSAGE CLASS'** button at the top. A new side menu is displayed containing all the required **Message Class** parameters to be provided:

![Message Classes – Create New Message Class](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-message-classes-new-message-class.png)

     * **Message Class Name** : a unique String defining the Message Class.
     * **Message Class Expression** : refers to the SpEL expression defining the message class.
     * **Priority** : defines the priority associated to the Message Class. The priority of a message class is an integer from 0 to 65535 , inclusive. Lower integers indicate higher priorities. If a messages validates the expression of 2 Message Classes, only the one with the lower priority value will be triggered.
  3. To create a new **Message Class** fill in the Message Class Expression field with a valid SpEL expression and set the priority

  4. Click **'CREATE'** button to save the changes. A confirmation message is displayed if the new Message Class is created successfully.


**Note:** At runtime, all active source message classes are sorted on priority, and for any given message, each message class expression is evaluated until one that evaluates to `true` is found. At that point, further message class evaluation stops.

## Testing a source message class expression

You can experiment and test your source message class expressions before creating a source message class.

### REST

`POST /configuration/v1/message-classes:test`
    
    
    {
      "expression": "SPEL_EXPRESSION",
      "testMessage": "TEST_MESSAGE"
    }
    

Replace the following:

  * `SPEL_EXPRESSION`: the SpEL expression defining the message class.
  * `TEST_MESSAGE`: the test source message object.



The return object informs you whether the provided expression is syntactically correct, and whether it would evaluate to `true` of `false` for the provided message.

### Console

The UI provides the option to test the SpEL expression of the new Message Class with a test message. 

  1. Fill in the **'Test Message'** box with the sample `JSON` message.
  2. Click **'RUN TEST'** to run the validation. The result of the test is a **'Matched'** or **'Not matched'** result and short explanation of the matching criteria.



![Message Classes – Test Message Class](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-message-classes-test-message.png)

## Evaluating a test message against all active message classes

You can evaluate a message to determine in which source message class a test message would fall for a set of active source message classes.

### REST

`POST /configuration/v1/message-classes:evaluate`
    
    
    {
      "testMessage": "TEST_MESSAGE"
    }
    

Replace the following:

  * `TEST_MESSAGE` with the test source message object.



The return object informs you which source message class was matched for the provided message, if any.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
