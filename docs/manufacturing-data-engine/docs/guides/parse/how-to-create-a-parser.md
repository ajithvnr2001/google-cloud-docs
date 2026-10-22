---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/parse/how-to-create-a-parser/
title: Create a parser \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:07.007027+00:00
---

# Create a parser  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/parse/how-to-create-a-parser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a parser

This guide explains how to create a parser. Parsers perform data transformation and mapping. The exact transformation steps are defined on the [_whistle_ script documentation](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/parse/how-to-write-a-whiste-script) for Manufacturing Data Engine (MDE).

## Create a parser

Parsers perform source-to-target mappings by means of a Whistle script. When creating a parser, you must define three core elements:

  1. The _message class_ to whose message stream a parser subscribes (input).
  2. _Type version_ of the proto record stream that the parser emits (output).
  3. The Whistle script to transform source messages from the specified _message class_ (input) to proto records of the defined _type version_ (output).



The Whistle script is applied to every message in the source message class stream, and it outputs _proto records_ of a specific _type_ version. We recommend that you take time to model your source message classes so they share a common semantic and schematic structure. Well-defined source message classes help minimize complex conditional logic in _parsers_. See the section on [modelling source message classes](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/ingest/how-to-create-a-source-message-class#modeling-a-source-message-class) for more guidance.

**Important:** As of Manufacturing Data Engine (MDE) release 1.4.1, the Pub/Sub message headers are now stored in a reserved attribute called `mdeHeaders`. If your input messages contain that attribute, then an expression like `embeddedMetadata: $root[where ($.field !=...)]` will overwrite the reserved attribute and result in the loss of the Pub/Sub header data that was provided with the edge message. Make sure that you use the generic Whistle filter expression with caution so that it won't result in data loss.

You can create a parser using the configuration API or the Console:

### REST

`POST /configuration/v1/parsers`
    
    
    {
      "name": "PARSER_NAME",
      "messageClassName": "SOURCE_MESSAGE_CLASS_NAME",
      "typeReference": {
        "name": "TYPE_NAME",
        "version": TYPE_VERSION
      },
      "script": "WHISTLE_SCRIPT"
    }
    

Replace the following:

  * `PARSER_NAME`: the name of the parser.
  * `SOURCE_MESSAGE_CLASS_NAME`: the name of the _Source Message Class_ to whose message stream this parser subscribes.
  * `TYPE_NAME`: the name of _type_ that is shared by the proto records emitted by this parser.
  * `TYPE_VERSION`: the _version_ of _type_ that is shared by the proto records emitted by this parser.
  * `WHISTLE_SCRIPT`: the Whistle script that defines the transformation.



### Console

  1. To create a new **parser** using the console, select the **PARSERS** section on the top menu. A list of the available parsers is displayed:

![Parsers - List of available parsers](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-parsers-list-default.png)

  2. For each available parser the following information is shown in the list:

     * **`Name`** :Name of the parser.
     * **`Message Class Name`** : Name of the message class the parser is feeding from.
     * **`Type`** : Destination type that the parser emits.
     * **`Type Version`** : Destination type version that the parser emits.
     * **`Enabled`** : Status of the parser (enabled or disabled).
     * **`Actions`** : Available actions for the parser: 
       * **'View/Edit'** : Opens the edit menu for a given parser.
       * **'Disable/Enable** : Allows disabling an enabled parser or enabling a disabled parser.
       * **'Test parser'** : Opens a dedicated interface to test the parser using a given `JSON` file.
       * **'Delete'** : Deletes the parser from MDE.
  3. To create a new parser click **ADD NEW PARSER**.

  4. To open the edit section of a given parser click **View/Edit** in the **Actions** icon. The side menu exposing all required parameters to create a new parser is displayed on the right side of the screen:

![Parsers - New parser](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-parsers-new.png)

  5. To define the new parser the following parameters must be supplied:

     * **`Name`** : Name of the parser. Can't be edited once created.
     * **`Message Class`** : Name of the **Message Class** the parser feeds from. Can't be modified once the parser is created. Select the Message Class from the list of available Message Classes.
     * **`Parser Code`** : **Whistle** file that defines the mapping associated to the parser. It can be modified at any time. Modifying the Whistle code won't generate a new version of the parsers. Parsers are indeed not versioned.
     * **`Type`** : Output **Type** emitted by the parser. It can't be modified after the parser is created. Select the type from the list of available types available. For new parsers the latest type version is selected by default.



To create the parser modify the parser parameters and click **CREATE** at the bottom. A confirmation message is displayed if the new parser has been created successfully.

## Test a parser

You can test a parser by providing a Whistle script and a sample input message:

### REST

`POST /configuration/v1/parsers:test`
    
    
    {
      "script": "SCRIPT",
      "testMessage": TEST_MESSAGE
    }
    

Replace the following:

  * `SCRIPT`: Whistle script to be tested (formatted as string).
  * `TEST_MESSAGE`: Input test message (formatted as JSON object).



### Console

You can test the parser directly from the **Actions** menu as well as in the **Edit Parser** menu. 

  1. To test a parser click **TEST**. A testing screen opens:

![Parsers - List of available parsers](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-parsers-test.png)

  2. Provide a sample **JSON Message** to test the parser.

  3. Introduce the message in the **Input** box and click the **RUN TEST** button.



  * If the transformation is successful, the output message is displayed in the **Result** box.
  * If the transformation is unsuccessful, an error message is displayed with the likely cause of the error.


  1. Use a valid `JSON` file as test message that has a structure that can be processed by the Whistle file of the parser. For example, this is a sample of a numerical payload generated by Manufactueing Connect edge that can be tested in the **`default-numeric-value-to-default-numeric-records`** parser:


    
    
    {
      "datatype": "int",
      "description": "",
      "deviceID": "0619E715-D1B8-438F-A1AB-E4D65D27EE83",
      "deviceName": "MicroLogix1100",
      "metadata": {
        "location": "ES-BCN-GRA",
        "manufacturer": "AllenBradley",
        "model": "MicroLogix1100",
        "os_revision": "Series B FRN 12.0",
        "source": "mce"
      },
      "registerId": "0997D2ED-B2AB-434C-9754-C1A3C2E9C165",
      "success": true,
      "tagName": "Manufactueing Connect edge_July_test_tag",
      "timestamp": 1691163012045,
      "value": 8004
    }
    

## Edit a parser

You can update an existing parser, including updating the Whistle script:

### REST

`PATCH /configuration/v1/parsers/NAME`
    
    
    {
      "disabled": DISABLED,
      "script": "SCRIPT",
      "typeReference": {
        "name": "TYPE_NAME",
        "version": TYPE_VERSION
      },
      "script": "WHISTLE_SCRIPT"
    }
    

Replace the following:

  * `DISABLED`: State of the parser (true or false).
  * `NAME`: Name of the parser.
  * `TYPE_NAME`: Name of _type_ that is shared by the proto records emitted by this parser.
  * `TYPE_VERSION`: _Version_ of _type_ that is shared by the proto records emitted by this parser.
  * `WHISTLE_SCRIPT`: Whistle script that defines the transformation.



### Console

  1. To open the edit section of a given parser click **View/Edit** in the **Actions** icon:

![Parsers - List of available Actions](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-parsers-actions.png)

  2. The **Edit Parser** side menu opens exposing the required parameters to configure the parser:

![Parsers - Edit parser side menu](https://docs.cloud.google.com/static/manufacturing-data-engine/images/ui-parsers-edit.png)



  * **`Name`** : Name of the parser. Can't be edited once created.
  * **`Message Class`** : Name of the **Message Class** the parser feeds from. Can't be modified once the parser is created.
  * **`Parser Code`** : **Whistle** file that defines the mapping associated to the parser. It can be modified at any time. Modifying the Whistle code won't generate a new version of the parsers. Parsers are not versioned.
  * **`Type`** : Output **Type** emitted by the parser. It can't be modified after the parser is created.
  * **`Version`** : Output type **version** emitted by the parser. Can be modified at any time for higher versions.


  1. To edit a parser, modify the parser parameters and click **SAVE**.
  2. A confirmation messages is displayed if the parser has been created successfully.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
