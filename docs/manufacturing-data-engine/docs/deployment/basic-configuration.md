---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/basic-configuration/
title: Basic configuration \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:57.903061+00:00
---

# Basic configuration  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/basic-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Basic configuration

The standard Manufacturing Data Engine (MDE) deployment doesn't apply any configuration settings by default, which are needed to start ingesting data. 

This guide walks you through a basic MDE setup. For example, for testing that the system works end to end. With this guide you can create message classes, types, and parsers for all three Archetypes.

If you intend to use Manufacturing Connect edge (MCe) to ingest data, deploy the [default configuration package](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/default-config-package) instead.

You can use either the MDE API or the web interface to complete this configuration.

**Note:** To use the API you should have configured [SSH tunneling over IAP](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/step-three-configure-access#ssh-tunneling-over-IAP) before.**Warning:** This configuration is not intended for production use cases. Always tailor your configuration to specific use cases.

## Message classes

This section provides examples of the message classes available in MDE.

**Important:** As of MDE release 1.4.1, the message headers are stored in a reserved attribute called `mdeHeaders`. The existing message-classes that used expressions like `#root.headers['SOME_ATTRIBUTE']` will continue to work for a couple of future releases before it's deprecated. Make sure that you update your message-class expressions to use `#root.mdeHeaders['SOME_ATTRIBUTE']` instead.

### Message class for `numeric`

The following is an example of a `basic-numeric` message class:

### REST

`POST /configuration/v1/message-classes`
    
    
    {
       "name": "basic-numeric",
       "priority": 2000,
       "expression": "#root.event['value'] instanceof T(Number) && #root.event['timestamp'] != null && #root.event['tagName'] != null"
    }
    
    

### Web interface

Message Class Name: `basic-numeric`

  1. On the MDE web interface, click **Message Classes**.
  2. Click **Add new Message Class**.
  3. Fill in the **Message Class name** as `basic-numeric`.
  4. Copy the following expression and paste it on the **Expression** box:
         
         #root.event['value'] instanceof T(Number) && #root.event['timestamp'] != null && #root.event['tagName'] != null
         

  5. Change the priority to `2000`.

  6. Click **Create**.

![Basic-numeric MC](https://docs.cloud.google.com/static/manufacturing-data-engine/images/basic_config-basic-numeric-mc.png)




### Message class for `discrete`

The following is an example of a `basic-discrete` message class:

### REST

`POST /configuration/v1/message-classes`
    
    
       {
          "name": "basic-discrete",
          "priority": 1975,
          "expression": "#root.event['value'] != null && !(#root.event['value'] instanceof T(Number)) && #root.event['timestamp'] != null && #root.event['tagName'] != null"
       }
    

### Web interface

Message Class Name: `basic-discrete`

  1. On the MDE web interface, click **Message Classes**.
  2. Click **Add new Message Class**.
  3. Fill in the **Message Class name** as `basic-discrete`.
  4. Copy the following expression and paste it on the **Expression** box:
         
         #root.event['value'] != null && !(#root.event['value'] instanceof T(Number)) && #root.event['timestamp'] != null  && #root.event['tagName'] != null
         

  5. Change the priority to `1975`.

  6. Click **Create**.

![Basic-discrete MC](https://docs.cloud.google.com/static/manufacturing-data-engine/images/basic_config-basic-discrete-mc.png)




### Message class for `continuous`

The following is an example of a `basic-continuous` message class:

### REST

`POST /configuration/v1/message-classes`
    
    
       {
          "name": "basic-continuous",
          "priority": 1950,
          "expression": "#root.event['value'] != null && !(#root.event['value'] instanceof T(Number)) && #root.event['startTimestamp'] != null && #root.event['endTimestamp'] != null && #root.event['tagName'] != null"
       }
    

### Web interface

Message Class Name: `basic-continuous`

  1. On the MDE web interface, click **Message Classes**.
  2. Click **Add new Message Class**.
  3. Fill in the **Message Class name** as `basic-continuous`.
  4. Copy the following expression and paste it on the **Expression** box:
         
         #root.event['value'] != null && !(#root.event['value'] instanceof T(Number)) && #root.event['startTimestamp'] != null && #root.event['endTimestamp'] != null && #root.event['tagName'] != null
         

  5. Change the priority to `1950`.

  6. Click **Create**.

![Basic-continuous MC](https://docs.cloud.google.com/static/manufacturing-data-engine/images/basic_config-basic-continuous-mc.png)




## Types

This section provides an overview of the types available in MDE.

**Important:** When creating the types make sure you wait for them to fully provision and activate before creating the parsers. It can take up to 2-3 minutes.

### Type for `numeric`

The following is an example of a `basic-numeric` type:

### REST

`POST /configuration/v1/types`
    
    
    {
       "archetype": "NUMERIC_DATA_SERIES",
       "name": "basic-numeric"
    }
    

### Web interface

Name: `basic-numeric`

  1. On the MDE web interface, click **Types**.
  2. Click **Add new Type**.
  3. Fill in the **Type name** as `basic-numeric`.
  4. Select `NUMERIC_DATA_SERIES` in the drop-down for **Archetype** :

![Basic-numeric Type](https://docs.cloud.google.com/static/manufacturing-data-engine/images/basic_config-basic-numeric-type.png)

  5. Open the **Storage Settings** section.

  6. Toggle the **Send to BigQuery** option.

  7. Click **Create**.




### Type for `discrete`

The following is an example of a `basic-discrete` type:

### REST

`POST /configuration/v1/types`
    
    
    {
       "archetype": "DISCRETE_DATA_SERIES",
       "name": "basic-discrete"
    }
    

### Web interface

Name: `basic-discrete`

  1. On the MDE web interface, click **Types**.
  2. Click **Add new Type**.
  3. Fill in the **Type name** as `basic-discrete`.
  4. Select ``DISCRETE_DATA_SERIES` in the drop-down for **Archetype** :

![Basic-discrete Type](https://docs.cloud.google.com/static/manufacturing-data-engine/images/basic_config-basic-discrete-type.png)

  5. Open the **Storage Settings** section.

  6. Toggle the **Send to BigQuery** option.

  7. Click **Create**.




### Type for `continuous`

The following is an example of a `basic-continuous` type:

### REST

`POST /configuration/v1/types`
    
    
    {
       "archetype": "CONTINUOUS_DATA_SERIES",
       "name": "basic-continuous"
    }
    

### Web interface

Name: `basic-continuous`

  1. On the MDE web interface, click **Types**.
  2. Click **Add new Type**.
  3. Fill in the **Type name** as `basic-continuous`.
  4. Select ``CONTINUOUS_DATA_SERIES` in the drop-down for **Archetype** :

![Basic-continuous Type](https://docs.cloud.google.com/static/manufacturing-data-engine/images/basic_config-basic-continuous-type.png)

  5. Open the **Storage Settings** section.

  6. Toggle the **Send to BigQuery** option.

  7. Click **Create**.




## Parsers

This section provides an overview of the various parsers available in MDE. Make sure that the types are fully provisioned and `active` before creating the parsers. This process can take up to three minutes.

**Important:** As of MDE release 1.4.1, the message headers are now stored in a reserved attribute called `mdeHeaders`. If your input messages contain that attribute, then an expression like `embeddedMetadata: $root[where ($.field !=...)]` will overwrite the reserved attribute and result in a loss of the header data that was provided with the edge message. **Make sure that you use the generic Whistle filter expression with caution so that it won't result in data loss**.

### Parser for `numeric`

The following is an example of a `basic-numeric` parser:

### REST

`POST /configuration/v1/parsers`
    
    
    {
       "name": "basic-numeric-to-basic-numeric",
       "messageClassName": "basic-numeric",
       "typeReference": {
             "name": "basic-numeric",
             "version": 1
       },
       "script": "package mde\n\n[{\ntagName: $root.tagName;\ntimestamps: MapTimestamp($root);\ndata: MapData($root);\nembeddedMetadata: $root[where ($.field != \"value\" and $.field != \"tagName\" and $.field != \"timestamp\" and $.field != \"messageId\")];\n}]\n\ndef MapTimestamp(input) {\n    eventTimestamp: input.timestamp;\n}\n\ndef MapData(input) {\n    numeric: input.value;\n}"
    }
    

### Web interface

Name: `basic-numeric-to-basic-numeric`

  1. On the MDE web interface, click **Parsers**.
  2. Click **Add new Parser**.
  3. Fill in the **Parser name** as `basic-numeric-to-basic-numeric`.
  4. Select `basic-numeric` in the drop-down for **Message Class Name**.
  5. Copy and paste the following Whistle code in the **Parser** box:
         
         package mde
         
          [{
          tagName: $root.tagName;
          timestamps: MapTimestamp($root);
          data: MapData($root);
          embeddedMetadata: $root[where ($.field != "value" and $.field != "tagName" and $.field != "timestamp" and $.field != "messageId")];
          }]
         
          def MapTimestamp(input) {
             eventTimestamp: input.timestamp;
          }
         
          def MapData(input) {
             numeric: input.value;
          }
         

  6. Select `basic-numeric | version: 1` in the drop-down for **Type**.

  7. Click **Create**.

![Basic-numeric Parser](https://docs.cloud.google.com/static/manufacturing-data-engine/images/basic_config-basic-numeric-parser.png)




### Parser for `discrete`

The following is an example of a `basic-discrete` parser:

### REST

`POST /configuration/v1/parsers`
    
    
    {
       "name": "basic-discrete-to-basic-discrete",
       "messageClassName": "basic-discrete",
       "typeReference": {
             "name": "basic-discrete",
             "version": 1
       },
       "script": "package mde\n\n[{\ntagName: $root.tagName;\ntimestamps: MapTimestamp($root);\ndata: MapData($root);\nembeddedMetadata: $root[where ($.field != \"value\" and $.field != \"tagName\" and $.field != \"timestamp\" and $.field != \"messageId\")];\n}]\n\ndef MapTimestamp(input) {\n    eventTimestamp: input.timestamp;\n}\n\ndef MapData(input) {\n    complex: input.value;\n}\n"
    }
    

### Web interface

Name: `basic-discrete-to-basic-discrete`

  1. On the MDE web interface, click **Parsers**.
  2. Click **Add new Parser**.
  3. Fill in the **Parser name** as `basic-numeric-to-basic-discrete`.
  4. Select `basic-discrete` in the drop-down for **Message Class Name**.
  5. Copy and paste the following Whistle code in the **Parser** box:
         
         package mde
         
          [{
          tagName: $root.tagName;
          timestamps: MapTimestamp($root);
          data: MapData($root);
          embeddedMetadata: $root[where ($.field != "value" and $.field != "tagName" and $.field != "timestamp" and $.field != "messageId")];
          }]
         
          def MapTimestamp(input) {
             eventTimestamp: input.timestamp;
          }
         
          def MapData(input) {
             complex: input.value;
          }
         

  6. Select `basic-discrete | version: 1` in the drop-down for **Type**.

  7. Click **Create**.

![Basic-discrete Parser](https://docs.cloud.google.com/static/manufacturing-data-engine/images/basic_config-basic-discrete-parser.png)




### Parser for `continuous`

The following is an example of a `basic-continuous` parser:

### REST

`POST /configuration/v1/parsers`
    
    
    {
       "name": "basic-continuous-to-basic-continuous",
       "messageClassName": "basic-continuous",
       "typeReference": {
             "name": "basic-continuous",
             "version": 1
       },
       "script": "package mde\n\n[{\ntagName: $root.tagName;\ntimestamps: MapTimestamp($root);\ndata: MapData($root);\nduration: $root.duration;\nembeddedMetadata: $root[where ($.field != \"value\" and $.field != \"tagName\" and $.field != \"startTimestamp\" and $.field != \"endTimestamp\" and $.field != \"messageId\")];\n}]\n\ndef MapTimestamp(input) {\n    continuousTimestamp: {\n        eventTimestampStart: input.startTimestamp;\n        eventTimestampEnd: input.endTimestamp;\n    };\n}\n\ndef MapData(input) {\n    complex: input.value;\n}\n"
    }
    

### Web interface

Name: `basic-continuous-to-basic-continuous`

  1. On the MDE web interface, click **Parsers**.
  2. Click **Add new Parser**.
  3. Fill in the **Parser name** as `basic-numeric-to-basic-continuous`.
  4. Select `basic-continuous` in the drop-down for **Message Class Name**.
  5. Copy and paste the following Whistle code in the **Parser** box:
         
         package mde
         
          [{
          tagName: $root.tagName;
          timestamps: MapTimestamp($root);
          data: MapData($root);
          duration: $root.duration;
          embeddedMetadata: $root[where ($.field != "value" and $.field != "tagName" and $.field != "startTimestamp" and $.field != "endTimestamp" and $.field != "messageId")];
          }]
         
          def MapTimestamp(input) {
             continuousTimestamp: {
                eventTimestampStart: input.startTimestamp;
                eventTimestampEnd: input.endTimestamp;
             };
          }
         
          def MapData(input) {
             complex: input.value;
          }
         

  6. Select `basic-continuous | version: 1` in the drop-down for **Type**.

  7. Click **Create**.

![Basic-continuous parser](https://docs.cloud.google.com/static/manufacturing-data-engine/images/basic_config-basic-continuous-parser.png)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
