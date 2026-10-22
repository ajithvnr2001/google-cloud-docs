---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/dtmf/
title: DTMF for telephony integrations \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:08.705779+00:00
---

# DTMF for telephony integrations  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/dtmf/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  DTMF for telephony integrations Stay organized with collections  Save and categorize content based on your preferences. 

You can enable and configure DTMF (Dual-tone multi-frequency signaling) for telephony [integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration). When enabled, end-user telephone key-presses are converted to normal text and processed as end-user input by the agent. This conversion can be as simple as the characters associated with telephone keypresses (`12*34#`), or you can use [regular expressions (Regex)](https://www.regular-expressions.info/) for more complicated sequences.

## Matching rules

DTMF settings have three different matching rules:

  * Match to an [intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent).
  * Match to a [custom entity](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-custom).
  * Match to a system entity type



You can associate DTMF patterns with individual [intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) and [entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-options) to trigger a match to end-user input sequences. When you enable DTMF globally, system entities are enabled by default.

## System entity rule

[System entity](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-system) rules are enabled by default when you enable DTMF.

Type name | DTMF pattern | Example  
---|---|---  
`sys.percentage` | any integer number | 29 -> 29%  
`sys.temperature` | any integer number | 30 -> 30C or 30F  
`sys.phone-number` | any digit sequence | 4081111111  
`sys.date` | (depending on locale) YYYYMMDD (en-us) or MMDDYYY | 20231001 -> 2023-10-01, 10-01-2023 -> 10-01-2023  
`sys.zip-code` | any digit sequence | 94043  
`sys.number` | digit sequence with period represented by '*' key | 123 -> 123, 123*45 -> 123.45  
`sys.cardinal` | any digit sequence | 12345  
`sys.number-integer` | any digit sequence | 12345  
`sys.number-sequence` | any digit sequence | 12345  
`sys.ordinal` | any digit sequence | 12345  
  
## Settings

This section outlines the additional settings that you can configure when you enable DTMF.

### Finish digit

This setting controls the keypress that will immediately terminate DTMF input, without waiting for any more input. It is common to use `#` for this setting. The finish digit is not included in the converted end-user input. For example, if the finish digit is `#`, and the input is `123#`, then the converted end-user input provided to agent processing is `123`.

### Disable speech detection

With this setting enabled, the agent ignores speech inputs and uses DTMF-only input mode.

### Interdigit timeout duration

An end-user might pause while entering a sequence of keypresses. If this pause duration is greater than the _interdigit timeout duration_ , Dialogflow aborts DTMF processing for the sequence.

If Dialogflow aborts DTMF processing, it provides the unconverted sequence captured up to that point to the agent as end-user input. This input is unlikely to match any intent or form parameters, so Dialogflow will likely invoke a [no-match event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in).

When using the console, this field is in seconds.

### Endpointing timeout duration

After a match for a keypress sequence is made, Dialogflow continues to process keypresses. _Endpointing timeout duration_ is the duration that Dialogflow will wait for more input after a match is made before ending detection. This behavior handles scenarios where the sequence is a variable length, like unbounded numbers.

If the end-user pauses entry for than the time set in _endpointing timeout duration_ , Dialogflow aborts DTMF processing and converts the currently-matched sequence as it normally would.

## Enable DTMF

**Note:** To enable this feature on a [form parameter](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form) you must set **`dtmf`** to **`Required`** in the parameter's settings.

You can enable DTMF at the agent, page, or parameter level. DTMF will be applied to everything within that scope. This section describes enabling DTMF for an agent as an example. You can also enable DTMF using **Page settings** (pages), **Flow settings** (flows), or by selecting a parameter and viewing the settings menu. In all cases, DTMF settings are found at the bottom of the page.

  1. Go to **Agent settings** and select the **Speech and IVR** tab.

  2. Go to the bottom of the page and click the **Enable DTMF** checkbox.

  3. Set the values for **Finish digit** , **Interdigit timeout duration** , and **Enpointing timeout duration**. DTMF is now enabled for everything within the scope of that agent. If set at a lower level, these settings now override any upper-level settings. Any active intents or entity types of the active slots within that scope might be triggered if they have DTMF patterns defined.




### Add a DTMF pattern to an intent

  1. In the left-hand navigation menu, select the **Manage** tab and click **Intents**.

  2. Select an intent from the list that appears and go to the **DTMF pattern** box.

  3. Enter a DTMF sequence. You can use [regex patterns](https://www.regular-expressions.info/) in cases of more complex DTMF patterns.

  4. Click **Save** to save your changes.




### Add a DTMF pattern to an entity

  1. In the left-hand navigation menu, select the **Manage** tab and click **Entity types**.

  2. Select an entity type from the list that appears. Go to the **DTMF Pattern** column in the **Entities** table.

  3. Set a DTMF pattern for each entity in the table. You can use [regex patterns](https://www.regular-expressions.info/) in cases of more complex DTMF patterns.

  4. Click **Save** to save your changes.




## Use DTMF in the simulator

You can test your DTMF configuration in the console simulator.

  1. In the Dialogflow console, click **Test Agent** in the upper right hand corner of the screen.

  2. In the panel that pops up, click the **+** symbol next to the **Talk to agent** text input box. Select **DTMF**.

  3. Enter the DTMF pattern you want to test and the DTMF finish digit. Make sure that the **Send new DTMF input** box is checked, then click **Send**. The response to the DTMF input will appear in the simulator.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
