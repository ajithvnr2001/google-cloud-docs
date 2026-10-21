---
url: https://docs.cloud.google.com/chronicle/docs/event-processing/parsers-using-ai/
title: Create parser extensions with Gemini \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:43:30.837209+00:00
---

# Create parser extensions with Gemini  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/event-processing/parsers-using-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create parser extensions with Gemini

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

**Note:** This feature may not be available to all customers in all regions. Private preview features are not manageable in the Public Preview Manager page in the Google SecOps platform. 

This guide explains how security analysts and detection engineers can use natural language prompts to augment default log parsers. Using the AI Parser Extension feature, you can quickly extract additional fields, apply conditional logic, and map raw logs to the Unified Data Model (UDM) without writing complex parser syntax or regular expressions.

When a default log parser in Google SecOps parses your log source, it might omit customer-specific custom attributes, optional fields, or specialized telemetry. Using the AI Parser Extension feature lets you do the following:

  * Extract additional fields from raw logs and map them to standard UDM fields or custom `additional.fields`.
  * Apply conditional logic and value transformations, such as mapping string actions to UDM enumerated types.
  * Refine generated extensions interactively across multi-turn chat sessions without starting from scratch.



## Key terminology

  * Unified Data Model (UDM): The standard data structure used in Google SecOps to store and analyze log data.



## Before you begin

Before you begin, confirm the following prerequisites are met:

  * **Usage quotas:** You can run a maximum of 10 AI Parser Extension generation sessions per 24-hour window, with up to 5 messages per session.



## Best practices for crafting prompts

To get accurate parser extensions on your first attempt, follow these prompting guidelines:

  1. **Specify source and target explicitly:** Clearly state which part of the raw log to extract and which exact UDM field path it populates, for example, `principal.ip`, `target.user.email_addresses`, or `security_result.action`.
  2. **Use quotes for exact match literals:** When referring to literal strings, delimiters, or sample values in unstructured logs, enclose them in quotation marks, for example, `"198.51.100.0"` or `"allow"`.
  3. **Handle custom fields using additional.fields:** For proprietary or vendor-specific attributes that don't have a dedicated UDM field, instruct the AI to map them into `additional.fields` with a clear key name, for example, `additional.fields["application"]`.



## Generate a parser extension

You can start the parser extension workflow from either of the following locations in Google SecOps:

  * **Parsers settings page:** Navigate to the **Parsers** page to select and extend any existing log parser.
  * **Search page:** When investigating logs on the **Search** page, open the extension creation flow directly from an event with unparsed fields.



To generate a parser extension from the **Parsers** settings page, follow these steps:

  1. In Google SecOps, navigate to the **Parsers** settings page.
  2. Search for the log type you want to extend.
  3. Click the menu next to the parser and select the option to extend it.
  4. In the **RAW LOG** field, paste a sample of the log you want to parse.
  5. In the **Extension Method** section, select the **Generate with AI** tab.
  6. In the prompt field, enter a plain English description of the extraction.
  7. Click **Confirm**.

The system generates the extension code and updates the **UDM Output**.




## Refine the parser extension

You can build and refine your parser extension iteratively across multi-turn chat sessions. When you submit a follow-up prompt, the AI applies your new instructions on top of the previously generated extension. Existing mappings and conditional logic from earlier turns are preserved automatically unless you explicitly ask to override or remove them.

**Note:** Sessions don't persist after you leave the page. To avoid losing your work, complete or save your extension before navigating away.

  1. In the prompt field, enter a follow-up instruction to adjust the generated code.
  2. Click **Confirm**.
  3. After each prompt, preview the generated extension code, inspect sample UDM outputs, and confirm or adjust the logic.

**Note:** If you need to correct a mistake from a previous turn, state what to change in plain English, for example, `"Change the target field for callerIp from target.ip to principal.ip"`.

The following example workflow shows how iterative refinement builds a parser extension across multiple turns:

  1. **Turn 1 (initial extraction):**
     * **User prompt:** `"Extract source IP '198.51.100.0' to principal.ip and destination IP '198.51.100.1' to target.ip."`
     * **Result:** The AI generates an extension mapping `principal.ip` and `target.ip`.
  2. **Turn 2 (additive mapping):**
     * **User prompt:** `"Also map virtual system string 'vsys1' to observer.administrative_domain."`
     * **Result:** The AI updates the extension to map `observer.administrative_domain` while maintaining the IP mappings from turn 1.
  3. **Turn 3 (conditional refinement):**
     * **User prompt:** `"In addition, map action string 'allow' to security_result[0].action as ALLOW."`
     * **Result:** The AI incorporates the conditional action enumeration mapping on top of all previous extractions.



## Validate the parser extension

  1. Click **Validate**.
  2. Review the validation metrics after the process completes.



## Access reference information

Use the following examples to craft accurate prompts.

### Structured logs prompts

For structured logs where data is organized into named keys, attributes, or XML tags, specify the field names or paths in your prompt.

#### Sample structured log - JSON format
    
    
    {
      "insertId": "u0mlpdesys",
      "logName": "projects/sample-project-id/logs/cloudaudit.googleapis.com%2Fdata_access",
      "protoPayload": {
        "authenticationInfo": {
          "principalEmail": "analyst@example-domain.com"
        },
        "methodName": "GenerateAccessToken",
        "requestMetadata": {
          "callerIp": "203.0.113.195",
          "callerSuppliedUserAgent": "google-cloud-sdk gcloud/392.0.0"
        },
        "resourceName": "projects/-/serviceAccounts/110649196922301550006",
        "serviceName": "iamcredentials.googleapis.com"
      }
    }
    

#### Prompt examples for structured logs

Prompt instruction | Source field or key | Target UDM field  
---|---|---  
`"Map principalEmail to principal.user.email_addresses."` | `principalEmail` | `principal.user.email_addresses`  
`"Extract callerIp to principal.ip and methodName to metadata.product_event_type."` | `callerIp`, `methodName` | `principal.ip`, `metadata.product_event_type`  
`"Map resourceName to target.resource.name and serviceName to target.application."` | `resourceName`, `serviceName` | `target.resource.name`, `target.application`  
`"From XML tags, map /Event/System/Hostname to principal.hostname."` | `/Event/System/Hostname` | `principal.hostname`  
  
### Unstructured logs prompts

For unstructured logs, specify literal values directly from the sample log, positional references, or descriptive labels.

#### Sample unstructured syslog message
    
    
    <14>Nov  9 18:52:45 198.51.100.1 1,2021/11/09 18:52:45,007051000184334,TRAFFIC,start,2561,2021/11/09 18:52:45,198.51.100.0,198.51.100.1,0.0.0.0,0.0.0.0,any allow,,,ping,vsys1,LAN,LAN,ethernet1/2,ethernet1/2,LFPpan,2021/11/09 18:52:45,9729,6,0,0,2048,0,0x100000,icmp,allow,444,444,0,6
    

#### Prompt examples for unstructured logs

Prompt instruction | Sample literal value or description | Target UDM field  
---|---|---  
`"Extract source IP '198.51.100.0' to principal.ip and destination IP '198.51.100.1' to target.ip."` | `'198.51.100.0'`, `'198.51.100.1'` | `principal.ip`, `target.ip`  
`"Extract the application string 'ping' from the log and map it to additional.fields['application']."` | `'ping'` | `additional.fields["application"]`  
`"Map rule name 'any allow' to security_result.rule_id."` | `'any allow'` | `security_result[0].rule_id`  
`"Extract sent bytes and received bytes into network.sent_bytes and network.received_bytes."` | Numeric byte counters in log | `network.sent_bytes`, `network.received_bytes`  
  
### Conditional logic prompts

Describe conditional logic to normalize raw log values to specific UDM enumerations.

  * **Enumeration normalization:** `"If the firewall action in the log is 'allow', set security_result.action to ALLOW; otherwise set security_result.action to BLOCK."`
  * **Conditional field mapping:** `"If the protocol is 'icmp', map the ICMP type and code into network.icmp.type and network.icmp.code."`
  * **Status mapping:** `"When the log status contains 'success' or '0', set security_result.severity to INFO; if it contains 'error', set it to ERROR."`



## Usage limits

To maintain optimal performance and resource availability, the AI Parser Extension feature enforces the following usage quotas:

  * **10 sessions per 24 hours:** Each customer is allotted a maximum of 10 AI Parser Extension generation sessions per 24-hour window.
  * **5 messages per session:** Within a single session, you can send up to 5 messages, including your initial prompt and subsequent refinement turns, to craft and refine your parser extension.



If you reach the session message limit, you can save your current extension or start a new session.

## What's next

  * For more details on other parser extension methods, see [Develop parser extensions](https://docs.cloud.google.com/chronicle/docs/event-processing/using-parser-extensions).
  * For sample extension snippets and scenarios, see [Parser extension examples](https://docs.cloud.google.com/chronicle/docs/event-processing/parser-extension-examples).
  * For an overview of how raw logs are parsed to UDM, see [Overview of log parsing](https://docs.cloud.google.com/chronicle/docs/event-processing/parsing-overview).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
