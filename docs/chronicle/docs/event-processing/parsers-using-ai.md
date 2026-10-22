---
url: https://docs.cloud.google.com/chronicle/docs/event-processing/parsers-using-ai/
title: Create custom parsers and parser extensions with Gemini \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:24:35.221466+00:00
---

# Create custom parsers and parser extensions with Gemini  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/event-processing/parsers-using-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create custom parsers and parser extensions with Gemini

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

**Note:** This feature may not be available to all customers in all regions. Private preview features are not manageable in the Public Preview Manager page in the Google SecOps platform. 

This guide helps security analysts and detection engineers use AI Parsing in Google Security Operations to build custom parsers from scratch or create parser extensions that augment existing parsers. Using natural language prompts and vendor documentation, you can map raw logs to the Unified Data Model (UDM) without writing complex parser syntax or regular expressions.

## Choose between AI custom parsers and AI parser extensions

The following table compares the Create Parser with AI and Write Extension with AI capabilities in AI Parsing:

Feature aspect | Create Parser with AI | Write Extension with AI  
---|---|---  
Output | A complete, standalone custom parser | An extension layered on an existing parser  
Primary use case | New or unsupported log sources, or a full parser rewrite | Adding or fixing specific fields on a working parser  
Input | Log type, ingested raw logs, and optional documentation links | Log type, sample raw log, and a prompt describing the fields to map  
  
## Key terminology

  * **AI Parsing:** The suite of AI-assisted parsing capabilities in Google SecOps, including AI custom parser generation (**Create Parser with AI**) and AI parser extensions (**Write Extension with AI**).
  * **Unified Data Model (UDM):** The standard data structure used in Google SecOps to store and analyze log data.



## Before you begin

Before you use AI Parsing, confirm that the following prerequisites are met:

  * Confirm that AI Parsing capabilities are enabled for your Google SecOps instance. If you don't see the **Create Parser with AI** or **Write Extension with AI** options, contact your Google SecOps representative.
  * For AI parser extensions, verify that the target log type already has an active prebuilt or custom parser, and prepare a sample raw log to test your extraction.
  * For AI custom parser generation, ingest a representative sample of the log source before you start. The Parser Agent learns from logs that you have already ingested for the selected log type. If no logs are found for the log type, generation can't start. Failed start attempts don't count against your quota.
  * For AI custom parser generation, prepare one to five publicly accessible links to the vendor's log format reference, such as a field dictionary, event schema, or log samples page (recommended). Comprehensive documentation is the single biggest factor in parser quality.



## Create a custom parser with AI

Create Parser with AI builds a complete custom parser for a log source from scratch. You select a log type and optionally provide links to the vendor's log documentation. The Parser Agent samples your ingested logs, researches the log schema, plans the raw-field-to-UDM mapping, and writes the parser code in JavaScript. You then review the result and refine it using plain-English instructions that reference raw field names and UDM fields. When the output is ready, you submit the parser like any other custom parser.

With AI custom parser generation, you can do the following:

  * Onboard a log source that has no prebuilt parser, or whose prebuilt parser doesn't fit your log format.
  * Generate a complete parser that covers every distinct log format found in your ingested data, rather than only a single sample.
  * Refine the generated parser through follow-up prompts without writing parser code yourself.



### Start an AI-generated custom parser

  1. In Google SecOps, go to **SIEM Settings > Parsers**.
  2. Click **Add New Parser**.
  3. In the **Create New Custom Parser** dialog, select the **Log Source** that you want to parse (for example, `GCP DNS`).
  4. Under **How will you create the parser?** , select **Create Parser with AI**.
  5. Click **Create**.



### Add product documentation and start generation

**Note:** Documentation links are optional. If you don't add any links, the research stage searches the web to find the vendor's documentation and infers the schema directly from your raw logs. This approach works well for common, well-documented products. For niche or internal log sources, adding links provides better field coverage.

  1. Optional: In the **Parser Agent** pane, in the **Add product link** field, paste a link to the vendor's log documentation and click **Add**. You can add up to five links. The **Documentation** counter displays how many links you have added.
  2. Click **Generate Parser**.



#### Guidelines for documentation links

To improve field coverage in the generated parser, follow these guidelines when selecting documentation links:

  * Provide only public links to vendor documentation. If a link is private or inaccessible, the Parser Agent ignores the link and searches the web instead without failing the generation.
  * Link to pages that describe log fields and event types, such as a log schema, field dictionary, or event reference. Avoid marketing pages or product overviews.
  * Select pages that match the log format you ingest. For example, if you ingest JSON audit logs, link to the JSON audit log reference rather than the syslog reference.
  * Add a link for each event category if the vendor documents different event categories on separate pages (for example, DNS queries, firewall events, and administrator activity).



### Track generation progress

When custom parser generation begins, the status changes to **GENERATING IN PROGRESS**. The generation process consists of the following stages:

Stage | Agent action | Output passed to next stage  
---|---|---  
**Fetching raw logs** | The agent samples your ingested logs for the log type. It clusters the logs to select a set of example logs that covers every distinct log format and event shape. | Representative example logs  
**Research documentation** | The agent reads the documentation links you provided, or searches the web if you didn't provide links. It combines that information with the example logs to build a log schema and field dictionary. | Log schema and field dictionary  
**Create a mapping plan** | The agent identifies each event type in the logs and plans how each raw log field maps to the corresponding UDM field. | Mapping plan from raw field to UDM field for each event type  
**Generate parser code** | The agent converts the mapping plan into JavaScript parser code. It tests the code against the example logs and resolves errors until the parser runs cleanly. | Ready-to-review parser  
**Note:** The generation process typically takes 30 to 90 minutes, depending on the number of distinct log formats, the complexity of the log source, and the size of the log schema. You don't need to keep the page open. Click **Close** and return to **SIEM Settings > Parsers** later. When generation completes, the parser appears in the list with an **AI GENERATED** badge.

If parser generation fails because no logs are found for the selected log type, ingest raw logs for that log type before you start generation again. For any other generation failure, no manual triage options are available. Trigger a new generation session. If the failure persists, contact Support to open a support case.

### Review and refine the custom parser

When custom parser generation finishes, the status changes to **AI GENERATED** and the page displays the following panes:

  * **Parser Agent:** Displays the **Refine Parser with AI** prompt field where you can enter follow-up instructions.
  * **Parser Code:** Displays the generated JavaScript parser code for review. The generated code is read-only before submission. To modify the logic, enter a prompt in the **Refine Parser with AI** field.
  * **Raw Log:** Displays sample raw logs for the log type. You can click edit **Edit** to paste your own log line, or click refresh **Refresh** to load other samples.
  * **Show UDM Output:** Runs the current parser code against the raw log and displays the resulting UDM event so you can verify each mapping.



#### Review the generated output

Before activating the parser, review the generated mappings across your sample logs:

  1. Load several raw logs, including each event type that you want to parse, and click **Show UDM Output** for each log.
  2. Verify that the parser maps raw log fields to the appropriate UDM fields and populates their values accurately (for example, event metadata, entity fields such as `principal` and `target`, and security result fields).
  3. Check for any important raw fields that remain unmapped.



#### Refine the custom parser with AI

If a mapping is incorrect or missing, enter an instruction in the **Refine Parser with AI** field and click **Confirm**. The Parser Agent updates the existing parser rather than starting over and preserves all mappings that you didn't mention. Each refinement creates a new version of the parser code that you can review.

Follow these guidelines to craft effective refinement prompts:

  1. State both the raw source field (or a sample value from the log) and the exact target UDM field path.
  2. Group related changes together, and avoid mixing unrelated fixes in a single long prompt.
  3. Enclose exact strings from the raw log in single quotation marks, such as `'NXDOMAIN'` or `'allow'`.
  4. State conditional mappings explicitly using an `if ... then ... otherwise ...` structure when a mapping depends on a field value.
  5. Instruct the agent to map vendor-specific attributes that don't have a matching UDM field to `additional.fields` with a clear key name.



The following table provides example refinement prompts for `GCP DNS` logs:

Goal | Example prompt  
---|---  
Fix an incorrect mapping | `"Map jsonPayload.sourceIP to principal.ip instead of target.ip."`  
Add a missing field | `"Map jsonPayload.vmInstanceName to principal.hostname."`  
Map a nested or repeated value | `"Map jsonPayload.queryName to network.dns.questions.name and jsonPayload.queryType to network.dns.questions.type."`  
Apply conditional logic | `"If jsonPayload.responseCode is 'NXDOMAIN', set security_result.summary to 'Domain does not exist'. Otherwise, leave it empty."`  
Set the event type | `"Set metadata.event_type to NETWORK_DNS for all DNS query logs."`  
Map a vendor-specific field | `"Map jsonPayload.alias_query_response_code to additional.fields with key 'alias_query_response_code'."`  
Remove a mapping | `"Stop mapping jsonPayload.protocol to network.application_protocol."`  
**Note:** You can't edit the generated code directly in the **Parser Code** pane before submission. After you submit and activate the parser, you can edit its code manually like any other custom parser.

### Submit and activate the custom parser

When the UDM output is accurate, click **Submit** to save and activate your generated custom parser.

To abandon the draft parser instead, click **Discard**. To remove a saved AI-generated custom parser later, open the parser and click **Delete** under **Delete Custom Parser**.

**Caution:** AI custom parser generation is an experimental feature. Generated parser quality can vary. Always review the UDM output for each event type and validate the parser before you activate it in production.

### Troubleshoot AI custom parser generation

The following table lists common issues you might encounter when generating a custom parser with AI and how to resolve them:

Issue or symptom | Resolution  
---|---  
You don't see the **Create Parser with AI** option. | The feature isn't enabled for your instance. Contact your Google SecOps representative.  
Generation fails because no logs are found for the log type. | The Parser Agent requires ingested raw logs for the selected log type. Ingest raw logs for the log type before you start generation again.  
Generation fails for another reason. | No manual triage options are available for a failed generation. Trigger the generation again. If the failure persists, contact Support to open a support case.  
Generation takes a long time to complete. | Generation typically takes 30 to 90 minutes. Complex log sources with many distinct formats or large schemas take longer. You can close the page and return to **SIEM Settings > Parsers** later.  
Many fields remain unmapped. | Add documentation links that describe the log fields and start a new session, or use refinement prompts to map the missing fields.  
A refinement prompt changed an unrelated mapping. | Describe the correction in a follow-up prompt (for example, `"Revert the change to principal.ip and map jsonPayload.sourceIP to it again."`). Alternatively, submit and activate the parser to edit the code manually.  
Some logs fail to parse in **Show UDM Output**. | Paste the failing log into the **Raw Log** pane and send a refinement prompt that quotes the unparsed portion of the log.  
  
## Create a parser extension with AI

When a default log parser in Google SecOps parses your log source, it might omit customer-specific custom attributes, optional fields, or specialized telemetry. Using AI parser extensions (**Write Extension with AI**) lets you do the following:

  * Extract additional fields from raw logs and map them to standard UDM fields or custom `additional.fields`.
  * Apply conditional logic and value transformations, such as mapping string actions to UDM enumerated types.
  * Refine generated extensions interactively across multi-turn chat sessions without starting from scratch.



### Best practices for crafting prompts

To get accurate parser extensions, follow these prompting guidelines:

  1. Clearly state which part of the raw log to extract and which exact UDM field path it populates (for example, `principal.ip`, `target.user.email_addresses`, or `security_result.action`).
  2. Enclose literal strings, delimiters, or sample values in unstructured logs in single quotation marks, such as `'198.51.100.0'` or `'allow'`.
  3. Instruct the AI to map proprietary or vendor-specific attributes that don't have a dedicated UDM field into `additional.fields` with a clear key name (for example, `additional.fields["application"]`).



### Generate a parser extension

You can start the parser extension workflow from either of the following locations in Google SecOps:

  * Go to **SIEM Settings > Parsers** to select and extend any existing log parser.
  * Open the extension creation flow directly from an event with unparsed fields when investigating logs on the **Search** page.



To generate a parser extension from the **Parsers** page, follow these steps:

  1. In Google SecOps, go to **SIEM Settings > Parsers**.
  2. Search the **Parsers** table for the log type that you want to extend.
  3. In the row for the parser, click more_vert **Menu** and select **Extend Parser > Create Extension**.
  4. In the **Raw Log** pane, verify the sample raw log or click edit **Edit** to paste a sample of the log that you want to parse.
  5. In the **Extension** pane, under **Extension Method** , select **Write Extension with AI**.
  6. In the prompt field, enter a plain-English description of the fields that you want to extract.
  7. Click **Confirm**.

The system generates the extension code and updates the **UDM Output** pane.




### Refine the parser extension

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



### Validate the parser extension

  1. Click **Validate**.
  2. Review the validation metrics after the process completes.



### Access reference information

Use the following examples to craft accurate prompts for parser extensions.

#### Structured logs prompts

For structured logs where data is organized into named keys, attributes, or XML tags, specify the field names or paths in your prompt.

##### Sample structured log - JSON format
    
    
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
    

##### Prompt examples for structured logs

Prompt instruction | Source field or key | Target UDM field  
---|---|---  
`"Map principalEmail to principal.user.email_addresses."` | `principalEmail` | `principal.user.email_addresses`  
`"Extract callerIp to principal.ip and methodName to metadata.product_event_type."` | `callerIp`, `methodName` | `principal.ip`, `metadata.product_event_type`  
`"Map resourceName to target.resource.name and serviceName to target.application."` | `resourceName`, `serviceName` | `target.resource.name`, `target.application`  
`"From XML tags, map /Event/System/Hostname to principal.hostname."` | `/Event/System/Hostname` | `principal.hostname`  
  
#### Unstructured logs prompts

For unstructured logs, specify literal values directly from the sample log, positional references, or descriptive labels.

##### Sample unstructured syslog message
    
    
    <14>Nov  9 18:52:45 198.51.100.1 1,2021/11/09 18:52:45,007051000184334,TRAFFIC,start,2561,2021/11/09 18:52:45,198.51.100.0,198.51.100.1,0.0.0.0,0.0.0.0,any allow,,,ping,vsys1,LAN,LAN,ethernet1/2,ethernet1/2,LFPpan,2021/11/09 18:52:45,9729,6,0,0,2048,0,0x100000,icmp,allow,444,444,0,6
    

##### Prompt examples for unstructured logs

Prompt instruction | Sample literal value or description | Target UDM field  
---|---|---  
`"Extract source IP '198.51.100.0' to principal.ip and destination IP '198.51.100.1' to target.ip."` | `'198.51.100.0'`, `'198.51.100.1'` | `principal.ip`, `target.ip`  
`"Extract the application string 'ping' from the log and map it to additional.fields['application']."` | `'ping'` | `additional.fields["application"]`  
`"Map rule name 'any allow' to security_result.rule_id."` | `'any allow'` | `security_result[0].rule_id`  
`"Extract sent bytes and received bytes into network.sent_bytes and network.received_bytes."` | Numeric byte counters in log | `network.sent_bytes`, `network.received_bytes`  
  
#### Conditional logic prompts

Describe conditional logic to normalize raw log values to specific UDM enumerations.

  * **Enumeration normalization:** `"If the firewall action in the log is 'allow', set security_result.action to ALLOW; otherwise set security_result.action to BLOCK."`
  * **Conditional field mapping:** `"If the protocol is 'icmp', map the ICMP type and code into network.icmp.type and network.icmp.code."`
  * **Status mapping:** `"When the log status contains 'success' or '0', set security_result.severity to INFO; if it contains 'error', set it to ERROR."`



## Usage limits

To maintain optimal performance and resource availability, AI Parsing capabilities enforce the following default usage quotas:

  * You can start up to 10 AI custom parser generation or AI parser extension sessions per instance in a rolling 24-hour window. For custom parsers, each click of **Generate Parser** for a new parser starts a session.
  * Each session enforces the following interaction limits: 
    * For AI custom parser generation, each session supports up to 6 turns in total, which includes the initial generation plus up to 5 refinement prompts.
    * For AI parser extensions, each session supports up to 5 messages in total, which includes your initial prompt and subsequent refinement turns.



If you reach the turn or message limit for a session, you can submit or save your current work, or start a new session (subject to the daily session quota). For custom parsers, after you submit and activate the parser, you can edit its code manually like any other custom parser.

## What's next

  * For more information about creating and managing custom parsers, see [Configure custom parsers](https://docs.cloud.google.com/chronicle/docs/event-processing/configure-custom-parsers).
  * For more details on other parser extension methods, see [Develop parser extensions](https://docs.cloud.google.com/chronicle/docs/event-processing/using-parser-extensions).
  * For sample extension snippets and scenarios, see [Parser extension examples](https://docs.cloud.google.com/chronicle/docs/event-processing/parser-extension-examples).
  * For an overview of how raw logs are parsed to UDM, see [Overview of log parsing](https://docs.cloud.google.com/chronicle/docs/event-processing/parsing-overview).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
