---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ai-coach-best-practices/
title: AI coach: Best practices \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:02.469359+00:00
---

# AI coach: Best practices  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ai-coach-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  AI coach: Best practices Stay organized with collections  Save and categorize content based on your preferences. 

To optimize AI coach suggestions, you must provide the following information:

  * A set of written instructions
  * A conversation transcript
  * Data from the API



In return, AI coach provides applicable instructions and suggested agent responses.

## Recommended uses

To receive the most helpful suggestions, use AI coach in the following scenarios.

### Up selling and cross selling

When a contact center agent must offer another product or service, AI coach can provide the following helpful information.

  * Suggest when to start sales and when not to attempt sales at all.
  * Ask probing questions to understand customer needs.
  * Recommend a product from a short list based on the conversation context.
  * Suggest how to handle objections.



### Customer retention

When a contact center agent tries to convince someone to remain with their company, AI coach can provide the following helpful information.

  * Suggest when to make retention offers.
  * Ask probing questions to understand the customer's cancellation reason.
  * Recommend retention offers based on the conversation context.



### One step automation with tools

AI coach can also automate following repetitive business processes based on a customer service conversation.

  * Retrieve order status when the customer is authenticated and provided the order number.
  * Cancel an order when the order number and cancellation reason are available.
  * Configure risky automations to require manual review and approval.



#### Risky operations

Risky operations are automated business processes, which can cause heavy financial loss, a data breach, or regulatory non-compliance. Some examples include writing databases and retrieving sensitive information without authentication. AI coach can suggest timing and extract parameters from a conversation, but risky operations require manual review and approval and shouldn't be fully automated.

## AI coach instructions

Write a set of instructions to teach an AI coach what actions an agent should take and when those actions are needed throughout a customer service conversation. The instructions can specify any agent action, such as _ask the customer for their account PIN_ , _check the order status and inform the customer_ , or _submit a cancellation request_.

AI coach instructions include the following information:

  * **Display title** : Helps you manage multiple instructions. The display title is not visible to the LLM.

  * **Display details** : Specifies the static content that the model should return when the instruction is applicable. Display details can include a URL, shortcut to an internal tool or system, cheatsheet for the agents, or backend API call. These details are only accessible to the human agents. The display detail is _not_ visible to the model.

  * **Condition** : Specifies when in the conversation an instruction is applicable. The condition is visible to the model.

  * **Agent action** : Specifies what steps the agent should take when an instruction is applicable. The agent action is visible to the model.

  * **System action** : Specifies what tools to use for automation when an instruction is applicable. The system action is visible to the model.

  * **Triggering event** : Specifies this instruction's trigger event. If left unspecified, it mirrors the [generator's](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/build-your-own-genai-assist#generator_inputs) trigger event.




The condition, agent action, and system action affect AI coach's suggestions.

### Condition

The condition must be clear, concise, and self-contained. You can use a brief description of a customer's issue. Write the condition as if you're describing it to an average person who isn't familiar with your product. Following are a few examples of useful conditions:

  * The customer wants to cancel an order.
  * The customer wants to purchase a new phone.
  * The customer is having a very slow internet connection.



#### Example

The following is an example of a condition and an agent action that you might use.

  * **Condition** : Customer asks to update the shipping address to a new address.
  * **Agent action** : If the new address wasn't provided yet, ask the customer which is the new address that they want to use for the shipment.



In general, only show the text of a company policy after the relevant condition is met. In this example, that means AI coach only displays the cancellation policy after the customer expresses that they want to cancel. In the following example input, the intended topic of the conversation is reflected in both the display title and the condition. The content of the text shown to the agent is defined in the display detail. 

The input to AI coach:
    
    
    display_title: order cancellation
    display_detail: Company cancellation policy: Orders cannot be canceled more than 30 days after they have been placed. Only the cancellation team can process order cancellations.
    condition: the customer wants to cancel an order
    agent_action: N/A
    

### Agent action

Ideally, you can verify each step of the agent action based on the following three sources of information:

  * **Instructions** : See details in the previous section.
  * **Conversation transcript** : Documents what an agent and a customer say throughout a customer service conversation.
  * **Ingested data** : Consists of relevant customer data that is not found directly in the conversation, such as recent transactions, bills, and ongoing promotions.



An example of some ingested data that AI coach could use:
    
    
    ingested_data_key: Product Recommendation
    ingested_data_value:
    * Microwave-safe, glass food container set, $29.99
    * Gila Complete Window Film Application Kit, $19.99
    

#### Missing data

If an agent action requires information that's missing from the other pieces of the instruction and the conversation transcript, then the API that provides the ingested data must also provide the missing information. 

  * Avoid writing any action that requires information not found in those sources. 

  * If you cannot find the corresponding data, avoid:

    * Explaining the bill to the customer. 
    * Informing the customer of their balance, due date, or order status.



#### Multiple verbs

While the preceding list of agent actions contains only one verb, indicating an action for the agent to take, a step can have more than one verb. For example, if a business wants their agents to recommend a specific product and relate that product back to the condition all in one response, then you can write a single agent action step as in the following input.
    
    
    display_title: recommend device protection
    display_detail:
     trade-in process: [list steps for trade-in]
     device protection plan: [list plan details]
    condition: the customer has issues/questions about trade-in
    agent_action:
    Recommend the device protection plan and tell the customer it can help them get better trade-in values in the future.
    

#### Sample response output

An agent action can also utilize ingested data and specify a template for the sample response output. For example, if a business has multiple products to recommend and wants their agents to make recommendations that are relevant to the conversation context, then the agent action can prompt AI coach to make specific suggestions in the sample response outputs. Plus, this example illustrates how to write an agent action that prompts AI coach to generate sample responses which follow a template.
    
    
    display_title: cross-selling
    display_detail: see `Product Recommendations` for a relevant product
    condition: the customer is inquiring about product availability
    agent_action:
    Summarize to the customer what product you have been discussing, then recommend a relevant product from the section titled "Product Recommendation" and provide a brief explanation of how the two products are relevant to each other. Use this template for sample responses: "Since we've been talking about ..., I'd like to recommend ... because ...".
    
    Some examples:
    - For TVs, recommend TV stands.
    - For storage, recommend label writers.
    - For slow cookers and microwaves, recommend food container sets.
    - For air conditioners, recommend humidifiers.
    

#### Multi-step action

Lastly, the agent action can consist of more than one step. A multi-step agent action indicates how the agent should proceed through a conversation when a single condition is met.

Consider the following example for an order cancellation conversation the agent needs to ask a series of questions before they can process the cancellation. Each step will generate a separate sample response.
    
    
    display_title: order cancellation
    display_detail:
     cancellation policy: [list policies]
     look up `[order number]` in ordering system
     how to cancel an order [list steps]
    condition: the customer wants to cancel an order
    agent_action:
    1. Ask the customer for the order number.
    2. Ask the customer why they want to cancel the order.
    3. Inform the customer you are working on the cancellation.
    4. Inform the customer that you have canceled the order.
    5. Inform the customer that they will receive the refund in 5-7 business days.
    

Note that a step like _cancel the order_ can be difficult to verify without additional integrations. In the previous example, we replace it with the step _inform the customer you are working on the cancellation_.

### System action

In system action, we can reference tools that are already defined. This section in an instruction specifies which tools to consider when the instruction condition is met. The reference to a tool should be in this format: `${tool:tool_name|action_name}`. For details on how to set up tools, see the [OpenAPI and Integration Connectors tools](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tools) page.

The following are some system action examples:

Example 1: List the tool and action names. 
    
    
    ...
    system_action:
    ${tool:order_management|cancel_order}, ${tool:order_management|check_order}
    

Example 2: Add conditional behavior.
    
    
    ...
    system_action:
    * if "RESPONSE TO ${TOOL:ORDER_MANAGEMENT|CANCEL_ORDER}" is already present without any error, skip ${tool:order_management|cancel_order} 
    * if the order number has been provided, use ${tool:order_management|cancel_order} 
    * if "RESPONSE TO ${TOOL:GETORDERDETAILS|GETORDERDETAILS}" shows errors or failures, retry ${tool: order_management | cancel_order}
    

## Usage of overarching guidance in AI coach

AI coach adds a configurable prompt section called overarching guidance, which specifies the following:

  * Glossary
  * Guidelines of style, format, and tone for the sample response suggestions
  * Important notes on how to use and follow the instructions



### Glossary

The following glossary clearly defines _vulnerable customer_ and _account authentication_. With this glossary in the overarching guidance, you can use terms in the instructions without the need to repetitively define them like in earlier versions of AI coach.
    
    
    #### Vulnerable customer
    
    A customer is considered a vulnerable customer when at least one of the following is true:
    
    - The customer is experiencing financial hardship.
    - The customer has a physical disability or chronic health condition.
    - The customer is facing domestic abuse or is in an unsafe situation.
    
    #### Account authentication
    
    Account authentication is considered completed if the account PIN provided by the customer matches the account PIN in the data section *Account PIN*.
    

### Style, format, and tone guidelines

Follow these style, format, and tone guidelines in your sample responses:

  * Always be empathetic, patient, and reassuring.
  * Avoid overly casual language or slang. Maintain a respectful yet warm tone.
  * Responses must always acknowledge the customer's feelings or concerns explicitly (example: "I understand you're frustrated").
  * Use short sentences, and avoid complex language or jargon.
  * Never blame or contradict the customer. Instead, gently guide them toward correct information.
  * Begin every response with a clear acknowledgment of the customer's primary concern.



### Instruction-following notes

Add notes on how to follow your instructions. To improve automatic suggestions, you can also use notes to specify the thinking or reasoning process.

#### Examples

Example 1: Configure the model behavior
    
    
    ### Follow instructions
    * An instruction is applicable if and only if both of the following are true:
      * The condition is met by the conversation and the contexts.
      * Some of the agent actions are not completed yet. (If all the agent actions are done, then the instruction no longer applies.)
    * Notes on following the applicable instructions:
      * Do not suggest any sample responses or agent actions that are not specified in the applicable instructions.
      * Do not ask for information not specified in the instructions.
      * If an agent action step is to ask for information that the customer has already provided, then the step should be skipped.
      * **Your suggested responses should fit into the conversation flow**. For example, if the customer and the support agent has moved on to a new issue, you should stop making suggestions for the old issue.
    * Each sample response (or agent action suggestion) must be concise and only carry out one step in the applicable instruction. Do not cover multiple steps within one sample response (or agent action suggestion).
    * Avoid repetition:
      * Do not suggest sample responses or agent actions that the agent has already said or done earlier in the conversation.
      * Do not ask for information that is already available in the conversation or the contexts.
    * For product names, when you provide parameters in system action suggestions, provide the full names, including available specs.
    * If multiple instructions lead to the same or similar suggestion, give one suggestion, but with multiple sources.
    
    

Example 2: Adjust the instruction priorities and specify the thinking process to get more accurate suggestions
    
    
    ### Notes on how to use or follow instructions
    If there are multiple instructions applicable at the same time, **suggest only one instruction as applicable based on the following priority (from highest to lowest)**:
    * [Highest priority] security related
    
    Example: Account authentication is required before anything else.
    
    * [High priority] customer retention
    * [Medium priority] issue resolution
    * [Low priority] upselling or cross-selling
    
    ### Thinking process
    Before you make any suggestions, answer the following questions in this output section:
    * For each instruction, is it applicable? If yes, what is its priority?
    * Which instruction has the highest priority?
    

The following example illustrates the same instruction priority with examples of what the model should suggest under certain circumstances.
    
    
    ### Notes on how to use or follow instructions
    If there are multiple instructions applicable at the same time, **suggest only one instruction as applicable based on the following priority (from highest to lowest)**:
    * [Highest priority] security related
    
    Examnple: Account authentication is required before anything else.
    
    * [High priority] customer retention
    * [Medium priority] issue resolution
    * [Low priority] up-selling or cross-selling
    
    #### Examples to follow
    <example_1>
    <instructions>
    ...
    instruction I1
    condition: the customer wants to inquire about their current plan
    agent action: inform the customer of what plan they have and what features they get
    ...
    instruction I2
    condition: the authentication is not done yet
    agent action: ask for the account PIN
    ...
    </instructions>
    <conversation>
    customer: can you tell me what plan I have?
    </conversation>
    <good_suggestion>
    may I have your account PIN, please?
    </good_suggestion>
    <bad_suggestion>
    sure, let me pull up your account information.
    </bad_suggestion>
    <comment>
    Both instructions I1 and I2 are applicable, but I1 should have the highest priority because it's security related. Therefore, asking for the account PIN is a good suggestion.
    </comment>
    </example_1>
    

## Entity extraction in AI coach

Entity extraction allows AI coach to do the following:

  * Automatically identify and save important information (user address, account number, or a product name from the live transcript).
  * Prevent you from entering data manually.
  * Make sure your CRM systems are accurate.
  * Speed up your workflow. 



To optimize the feature's performance, ensure your AI coach generator configuration includes the following details:

  * Clear instructions
  * Defined tool structure
  * Overarching guidance



### Define the function tool

A tool definition specifies the set of instructions for the data to be extracted. The following example illustrates a _Function tool_ defined with JSON for address entity extraction.
    
    
    {
      "type": "object",
      "properties": {
        "phone_number": {
          "description": "A complete US phone number. ONLY extract if a fully visible 10 or 11-digit number is present. CRITICAL: If no valid value is found, you are FORBIDDEN from generating this key. DO NOT output 'phone_number': null.",
          "type": "string"
        },
        "full_person_name": {
          "description": "The full name of a real person. EXCLUDE: Generic roles, pronouns, or objects. CRITICAL: If no valid value is found, you are FORBIDDEN from generating this key. DO NOT output 'full_person_name': null.",
          "type": "string"
        },
        "address": {
          "description": "A complete physical address. MUST contain ALL FOUR: street number, street name, city and zipcode. Omit if incomplete.",
          "type": "string"
        }
      },
      "required": []
    }
    

The following example shows the output schema.
    
    
    {
      "properties": {
        "status": {
          "description": "Execution status indicating if entities were processed.",
          "type": "string"
        }
      },
      "type": "object"
    }
    

### Generator configuration

The generator configuration contains the high-level rules and logic that tell the AI coach when and how to perform the entity extraction. For example:
    
    
    {
      "displayName": "Address Extraction Generator",
      "instructions": [
        {
          "displayTitle": "Extract Address Update",
          "condition": "The customer's most recent message explicitly mentions an address",
          "agentAction": "N/A",
          "systemAction": "${tool:crm_update|update_member_address}"
        }
      ],
      "overarchingGuidance": "Prioritize current address over previous mentioned addresses. If unsure about address type, default to 'Permanent'."
    }
    

### Data delivery

When AI coach successfully extracts entity data and initiates a tool, the API delivers results in a [ToolCall object](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/GeneratorSuggestion#toolcall) to the backend system. This data delivery consists of the following components:

  * **Field** : The collected data is encoded in the `inputParameters` section of the message.
  * **Structure** : Backend systems are set up to receive this `toolCall` object. The system uses the `inputParameters` and maps them to the corresponding field to update the databases. The structure is encoded in the `toolCall` field of a `GeneratorSuggestion`.



#### Example

The following table shows the real time interaction between the customer and agent. The last column shows how an AI coach guides the agent by analyzing the customer utterances.

Turn | Role | Utterances | AI coach Logic & Action  
---|---|---|---  
1 | Customer | "Hi, I just moved and need to update my address." | Intent detected: `update_address`.  
2 | Agent | "Sure, I can help with that. What is the new address?" | \--  
3 | Customer | "It's 123 Main Street in Austin, Texas." | Analysis: Detects Street, City, and State. Feedback: "Zip code is missing. Ask the customer for the zip code."  
4 | Agent | "Got it. And what is the zip code for that location?" | \--  
5 | Customer | "Oh, it's 78701." | Analysis: Mandatory entities complete. System action: Triggers the `update_member_address` tool. Data is returned in `inputParameters`.  
6 | Agent | "Great, I've updated your permanent address to 123 Main Street, Austin, TX 78701." | Agent verifies pre-filled form in CRM.  
  
Key takeaways from the interaction include the following:

  * **Intent detection** : In turn 1, AI coach immediately identifies the customer's goal: update address.
  * **Analysis and coaching** : In turn 3, AI coach determines that the zip code is missing and sends feedback to ensure the agent collects the zip code.
  * **Automated Action** : After all the required entities are gathered in turn 5, AI coach activates the system tool. This sends the data directly to the CRM, meaning the agent doesn't have to manually enter the address into the database.



### Overarching guidance

AI coach adds a configurable prompt section called [overarching guidance](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ai-coach-best-practices#overarching-guidance), where you can set global rules that apply to all data extractions. This overarching guidance specifies the following details:

  * **Glossary** : You can define what terms mean. For example, define _Effective Date_ as the day a change becomes active.
  * **Thinking process** : You can tell AI coach to perform specific reasoning steps, such as _look back at the last five turns to confirm names and numbers before taking any action._



### Implementation plan

Follow these steps to successfully deploy your AI coach entity extraction feature. The first phase is setup:

  1. Create your tool and define the schema for all the key data you want to capture.
  2. Specify the high-level intent that should activate AI coach. For example, _Customer wants to update address_. Define the system actions as well.



The second phase involves testing and improvement:

  1. Use real transcripts to narrow down triggers and reduce false positives.
  2. Update your instructions to tell the agent what to do when the customer is missing a required piece of information.
  3. Confirm that the collected data flows correctly from the customer conversation, through `inputParameters` into your CRM or other systems.



## AI coach output language

AI coach generates suggestions in the specified output language. The model decides the output language of the suggestions if output language is not specified.

## AI coach outputs

AI coach returns either or both of the following results:

  * **Applicable instructions** : Multiple applicable instructions can be returned and each has its display title and details.

  * **Sample responses** : AI coach also generates samples of how an agent might respond in a conversation. These sample responses are based on the instructions, the conversation contexts, and the ingested data. The sample response can also be empty.




## Quality improvement

The following recommendations for writing AI coach instructions can help improve the quality of sample responses, but don't prevent AI coach from making unexpected suggestions.

### Text formatting for display details

Use Markdown syntax to display details in a rich format (links, bold text, etc.). This is rendered in the Google Cloud console simulator, but also helps to implement in the web interface.

### Text formatting for agent action

When the AI coach often misses a certain step or requirement, use bold text to help guide the model to pay more attention to a specific piece of text. To create bold text with Markdown syntax, add two asterisks on either side of the text.
    
    
    display_title: order cancellation
    display_detail:
     cancellation policy: [list policies]
     look up `[order number]` in ordering system
     how to cancel an order [list steps]
    condition: the customer wants to cancel an order
    agent_action:
    1. ask the customer for the order number
    2. **ask the customer why they want to cancel the order**
    3. inform the customer you are working on the cancellation
    4. inform the customer that you have canceled the order
    5. inform the customer that they will receive the refund in 5-7 business days
    

Bold text becomes less effective if, for example, every step of the agent action is made bold. So use this technique sparingly.

### Adding concrete examples

When AI coach fails to give the sample responses you expect, adding some examples of what you want to see to the agent action can help. The following detailed example illustrates how lightweight examples (highlighted) can be used:
    
    
    display_title: smartwatch recommendation
    display_detail: see `Smartwatch Catalog` for a relevant smartwatch
    condition: the customer recently purchased phones
    agent action:
    recommend a specific smartwatch from the section titled "Smartwatch Catalog"; the recommendation should match the recently purchased phones from the section titled "Recent Purchases".
    Following are some examples:
    - For Galaxy phones, recommend Galaxy watch.
    - For iPhones, recommend Apple Watch.
    - For Pixel phones, recommend Pixel Watch. 
    - For other phones, recommend Fitbit Sense.
    

Without the lightweight examples, AI coach would suggest Apple Watch for Androids or list all the available smartwatches. With the lightweight examples, the suggestions are precise.

### Message templates

For control over the wording and format of the generated sample responses, append a message template or even a static fixed message to the agent action. Unlike the lightweight examples, these templates indicate the exact wording that should be used in a sample response. Following is an example with the message templates highlighted.
    
    
    display_title: bill explanation
    display_detail:
     look up `[account number]`
     check `Recent Bills` to compare amounts
     https://www.[company name].com/promos
    condition: the customer wonders why the bill is getting higher this month
    agent_action:
    1. ask the customer for the account number. use this fixed message for sample responses: "May I have your account number, please?"
    2. compare the bills in the last two months from the section titled "Recent Bills" and inform the customer of the extra charge. use this template for sample responses: "Compared with last month, this month you have an extra charge for ..., which costs ..."
    

### Guided reasoning

If one or more instructions specify a goal without enough steps or without clarifying hidden reasoning to reach the goal, modify the steps for clarity. For example, when an agent is told to recommend a product, the suggested product should be relevant to the conversation. Help AI coach make relevant suggestions by adding a subtask to the start of the agent action that refers to the conversation context.
    
    
    display_title: cross-selling
    display_detail: sample response
    condition: the customer is inquiring about product availability
    agent_action:
    summarize to the customer what product you have been discussing, then recommend a relevant product from the section titled "Product Recommendation" and provide a brief explanation of how the two products are relevant to each other. Use this template for sample responses: "Since we've been talking about ..., I'd like to recommend ... because ...".
    

In the example, the main task is to suggest a product relevant to the conversation. AI coach can miss the point and recommend the first product listed in the **Product Recommendation** section. Adding the subtask can dramatically improve relevance. Also add a message template at the end of the agent action so the subtask result fits smoothly into the sample responses.

## Add suggestion deduplication

The AI coach suggestion deduplication feature prevents agents from being shown duplicate or highly similar suggestions. Use the `SuggestionDedupingConfig` field in the generator proto to compare the suggestion components (instructions, sample responses, etc.) against a history of recent suggestions. You can tune the sensitivity of _similarity_ using a configurable threshold. The `DuplicateCheckResult` message provides the outcomes of the deduplication check within the suggestion response.

### Configure suggestion deduplication

To manage duplicate suggestions from AI coach, configure the `SuggestionDedupingConfig` within your generator's configuration.

#### Configuration fields

`SuggestionDedupingConfig` has the following fields:

  * **`enable_deduping`** : Set this boolean field to true to enable the suggestion deduplication feature. Setting it to false or leaving it unset disables deduplication. Example:
        
        suggestion_deduping_config {
        enable_deduping: true
        }
        

  * **`similarity_threshold`** : Use this float-type threshold for similarity-based deduplication on certain fields. The deduplication process considers suggestions with a similarity score higher than this value as duplicates. The score ranges from 0.0 to 1.0. Setting this field to 0.0 or leaving it unset uses a default threshold of 0.8. Example:
        
        suggestion_deduping_config {
        enable_deduping: true
        similarity_threshold: 0.85
        }
        




### How deduplication works

When `enable_deduping` is true, you can compare suggestions against historical suggestions. The deduplication process assesses duplication for each of the following suggestion fields:

  * **Instructions (`applicable_instructions`)**: Checks for exact matches with the history suggestions.
  * **Sample responses (`sample_responses`)**: Checks for similarity between current suggestion and the history suggestions. The deduplication flags duplicate results if the similarity score exceeds the similarity threshold.
  * **Agent actions (`agent_action_suggestions`)**: Checks for similarity between current suggestion and the history suggestions, similar to sample responses. The deduplication flags duplicate results if the similarity score exceeds the similarity threshold. The results of the deduplication checks are returned in the `DuplicateCheckResult` message.



#### Output: DuplicateCheckResult

The `AgentCoachingSuggestion` message contains fields for different types of suggestions (e.g., `AgentActionSuggestion`, `SampleResponse`). Each of these fields will include a `DuplicateCheckResult` message to provide information about potential duplicates found in the history. Example:
    
    
    // Example within AgentActionSuggestion
    message AgentActionSuggestion {
      // ... other fields ...
      DuplicateCheckResult duplicate_check_result = 3;
    }
    
    // Duplication check for the suggestion.
    message DuplicateCheckResult {
      // The duplicate suggestions.
      repeated DuplicateSuggestion duplicate_suggestions = 1 [
        (google.api.field_behavior) = OUTPUT_ONLY,
        (datapol.semantic_type) = ST_NOT_REQUIRED
      ];
    
      // The duplicate suggestion details.
      message DuplicateSuggestion {
        // The answer record ID of the past duplicate suggestion.
        string answer_record = 1 [
          (google.api.field_behavior) = OUTPUT_ONLY,
          (datapol.semantic_type) = ST_IDENTIFYING_ID
        ];
        // Sources for the suggestion.
        Sources sources = 2 [(google.api.field_behavior) = OUTPUT_ONLY];
        // The index of the duplicate suggestion in the past suggestion list.
        int32 suggestion_index = 3 [(google.api.field_behavior) = OUTPUT_ONLY];
        // The similarity score of between the past and current suggestion.
        // This is only populated for fields using similarity checks.
        float similarity_score = 4 [(google.api.field_behavior) = OUTPUT_ONLY];
      }
    }
    

#### Example configuration

The example generator configuration enables the suggestion deduplication feature by setting `enable_deduping` to true. Additionally, it sets the `similarity_threshold` value to 0.75. This means that if a new suggestion's text (for sample responses and agent actions) has a similarity score greater than or equal to 0.75 with any of the historical suggestions, the deduplication flags it as a duplicate with `DuplicateCheckResult`.
    
    
    # Example Generator configuration with Deduping enabled
    generator {
      # ... other generator fields ...
    
      suggestion_deduping_config {
        enable_deduping: true
        similarity_threshold: 0.75 # Optional: Adjusts sensitivity for similarity checks
      }
    
      # ... rest of generator config ...
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
