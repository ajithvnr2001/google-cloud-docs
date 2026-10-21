---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/modular-components/
title: Modular components \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T22:53:14.665624+00:00
---

# Modular components  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/modular-components/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Modular components Stay organized with collections  Save and categorize content based on your preferences. 

Modular components let you dynamically adapt a single set of [agent instructions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/instruction) at runtime using template syntax. You can customize agent persona, constraints, formatting, and task flows based on the active channel (API, telephony, web), modality (voice or text), and session [variables](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/variable).

Instructions that use modular component syntax are compiled and resolved automatically before each model invocation, so the underlying language model only sees the rendered instructions that apply to the current turn.

## Variable syntax and evaluation behavior

Choosing the right variable syntax in your instructions depends on how frequently a variable changes and whether it controls conditional logic:

Syntax | Type | Runtime behavior | Best used for  
---|---|---|---  
`{{variable_name}}` | [Static variable](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/variable#static) (Substitution) | Replaced directly in the instructions with its value at render time before the model call. If a variable is missing or `null` in the session state, the literal `{{variable_name}}` placeholder is preserved. Supports nested object paths (for example, `{{user.profile.name}}`). | 1:1 text substitutions, configuration values, and prompt fields that don't change on every turn.  
`{variable_name}` | [Dynamic variable](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/variable#dynamic) (Tracking) | Preserved literally as `{variable_name}` in the instructions. When the variable changes during the conversation, its value is appended to the conversation history as `<state_update>variable_name: value</state_update>`. | Tracking runtime values extracted from the user or returned by tools across turns without invalidating the instruction prefix cache.  
`{@AGENT: Agent Name}` | Agent reference | Explicitly references a sub-agent in your application. | Directing the agent when to transfer or delegate to another agent.  
`{@TOOL: tool_name}` | Tool reference | Explicitly references a tool added to the current agent. | Directing the agent when to invoke a specific tool.  
  
### Literal preservation

To avoid breaking JSON examples or telephony prompts in your instructions, the template renderer preserves non-variable placeholders as literal text:

  * Single-brace JSON objects (for example, `{"key": "value"}`) and DTMF pound strings (for example, `{#}` or `{#1234#}`) are preserved verbatim.
  * Non-variable double-brace spans, such as inline JSON examples or unrecognized expressions, fall back cleanly to literal text without affecting other substitutions in the same instruction.



### Turn execution lifecycle and callback timing

Variables referenced inside control flow blocks, including `{% if %}`, `{% elif %}`, `{% for %}`, macros, and filters, are evaluated immediately against session state when the instructions are rendered for a turn.

**Note:** Reference variables directly by their identifier inside `{% ... %}` control blocks (for example, `{% if balance > 100 %}`). Don't wrap variable names in `{var}` or `{{var}}` braces inside a control block tag.

Because instructions are rendered _before_ the `before_model` callback executes, the turn execution order is:

  1. **`before_agent` callback executes**: State variable changes made in a `before_agent` callback are visible to the instruction renderer for the current turn.
  2. **Instruction rendering occurs** : All `{% if %}`, `{% for %}`, and `{{var}}` expressions are evaluated against the current session state.
  3. **`before_model` callback executes**: State changes made in a `before_model` callback occur _after_ the current turn's instructions have already been rendered and only take effect on subsequent turns.
  4. **Model invocation** : The model receives the rendered instructions. If the model calls a tool that updates `context.variables` (or `context.state`), the instructions are re-rendered before the post-tool model call in the same turn.



## Channel and modality block tags

You can use shorthand block tags to scope sections of your instructions to a specific modality or channel. At runtime, these tags are translated into conditional checks against the built-in [`_session`](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/python#variable-_session) variable (`_session.modality` and `_session.channel`).

### Modality block tags

Be sure to select the matching **Modality** in your deployment settings.

Opening tag | Closing tag | Equivalent condition | Description  
---|---|---|---  
`{@startModality_Text}` | `{@endModality_Text}` | `{% if _session.modality == 'TEXT' %}` | Includes the enclosed instructions only during text/chat interactions.  
`{@startModality_Voice}` | `{@endModality_Voice}` | `{% if _session.modality == 'VOICE' %}` | Includes the enclosed instructions only during voice interactions.  
  
Sample:
    
    
    {@startModality_Voice}
    Speak concisely using natural conversational pacing. Spell out confirmation
    codes digit by digit.
    {@endModality_Voice}
    {@startModality_Text}
    Format responses using bulleted lists and markdown links where helpful.
    {@endModality_Text}
    

### Channel block tags

You can optimize instructions for individual integration channels using `{@startChannel_<Channel>}` and `{@endChannel_<Channel>}`:

Opening tag | Closing tag | Target `_session.channel` value | Description  
---|---|---|---  
`{@startChannel_API}` | `{@endChannel_API}` | `API` | Applies to API-driven sessions.  
`{@startChannel_WEB_UI}` | `{@endChannel_WEB_UI}` | `WEB_UI` | Applies to [web widget](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/web-widget) sessions.  
`{@startChannel_GoogleTelephonyPlatform}` | `{@endChannel_GoogleTelephonyPlatform}` | `GOOGLE_TELEPHONY_PLATFORM` | Applies to [Google Telephony Platform](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/google-telephony-platform) voice calls.  
`{@startChannel_Twilio}` | `{@endChannel_Twilio}` | `TWILIO` | Applies to [Twilio](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/twilio) telephony sessions.  
`{@startChannel_Five9}` | `{@endChannel_Five9}` | `FIVE9` | Applies to [Five9](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/five9) telephony sessions.  
`{@startChannel_AudioCodes}` | `{@endChannel_AudioCodes}` | `CONTACT_CENTER_INTEGRATION` | Applies to [AudioCodes](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/audiocodes) telephony integrations.  
`{@startChannel_GoogleCCaaSVoice}` | `{@endChannel_GoogleCCaaSVoice}` | `CONTACT_CENTER_AS_A_SERVICE` | Applies to [Google Cloud CCaaS](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/ccaas) voice sessions.  
`{@startChannel_GoogleCCaaSChat}` | `{@endChannel_GoogleCCaaSChat}` | `CONTACT_CENTER_AS_A_SERVICE_CHAT` | Applies to [Google Cloud CCaaS](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/ccaas) chat sessions.  
`{@startChannel_Whatsapp}` (or `{@startChannel_WhatsApp}`) | `{@endChannel_Whatsapp}` (or `{@endChannel_WhatsApp}`) | `WHATSAPP` | Applies to [WhatsApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/whatsapp) messaging sessions.  
`{@startChannel_Instagram}` | `{@endChannel_Instagram}` | `INSTAGRAM` | Applies to [Instagram](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/whatsapp) messaging sessions.  
  
Sample:
    
    
    {@startChannel_Twilio}
    If the caller presses {#}, repeat the main menu options.
    {@endChannel_Twilio}
    

## Conditional logic and expressions

For multi-branch conditions across custom session variables, `_session.modality`, or `_session.channel`, use Jinja-style `{% if %}`, `{% elif %}` (or `{% else if %}`), `{% else %}`, and `{% endif %}` blocks.
    
    
    {% if _session.modality == 'TEXT' %}
    Welcome to Customer Support! I am your virtual assistant.
    {% else %}
    Hi there! Thank you for calling customer support.
    {% endif %}
    
    {% if brand_name == 'Cymbal Retail' or brand_name == 'Cymbal Wholesale' %}
    You represent Cymbal Support.
    {% elif brand_name == 'Acme Corp' %}
    You represent Acme Corp Support.
    {% else %}
    You represent General Customer Support.
    {% endif %}
    

### Supported operators and tests

Category | Syntax | Description  
---|---|---  
**Logical** | `and`, `or`, `not` | Combines or negates boolean expressions.  
**Equality** | `==`, `!=` | Checks whether two values are equal or not equal.  
**Relational** | `<`, `>`, `<=`, `>=` | Compares numeric values. Numeric strings (such as `"42"`) are coerced to numbers automatically. Comparisons against `null` or empty strings `""` safely evaluate to `false` without throwing an error.  
**Membership** | `in` | Checks if an item exists in a list, a key exists in a map/object, or a substring exists in a string (for example, `{% if department in ["security", "audit"] %}`). Combine with `not` (`{% if not (item in list) %}`) to negate.  
**State tests (`is` / `is not`)** | `is defined`, `is not defined`, `is undefined`, `is not undefined` | Evaluates to `true` if the variable exists and is non-null in the session state (or is missing/`null` for `undefined`).  
**Null & boolean tests** | `is none`, `is not none`, `is true`, `is not true`, `is false`, `is not false` | Checks explicitly for `null` (`none`) or boolean `true`/`false`.  
**Grouping & literals** | `(...)`, `"string"`, `'string'`, `42`, `3.14`, `true`, `false`, `[1, 2, 3]`, `null` / `none` | Groups expressions to control evaluation order and compares against literal values.  
  
### Operator precedence

Expressions are evaluated from highest precedence (1) to lowest precedence (7):

  1. **Primary expressions** : Parentheses `(...)`, literals, variable lookups (`a.b`), and function or macro calls (`fn(...)`).
  2. **Filters** : `|` (`x | upper`, `x | length`, `x | default(...)`).
  3. **State tests** : `is`, `is not` (`defined`, `undefined`, `none`, `true`, `false`).
  4. **Comparisons and membership** : `==`, `!=`, `<`, `>`, `<=`, `>=`, `in`.
  5. **Unary negation** : `not`.
  6. **Logical AND** : `and`.
  7. **Logical OR** : `or`.



## Filters and built-in functions

You can transform variable values inline or inside conditional expressions using [Jinja-style pipe filters](https://jinja.palletsprojects.com/en/stable/templates/#filters) (`|`) or built-in functions. A pipe filter passes the value on the left side of the pipe symbol (`|`) into the filter on the right side to transform the value before rendering or comparing it:

Filter / Function | Description | Example  
---|---|---  
`value | length` or `length(value)` | Returns the number of elements in a list or map, or the character length of a string (`0` for `null`). | `{% if length(user.recent_orders) >= 3 %}`  
`value | upper` | Converts a value to an uppercase string. | `{{ user.loyalty_tier | upper }}`  
`value | default(fallback)`, `value | default(fallback, true)`, or `default(value, fallback)` | Returns `fallback` when `value` is `null`. When `true` is passed as the optional second positional argument, also returns `fallback` when `value` is empty or falsy (`""`, `0`, `false`, or `[]`). | `{{ user.preferred_name | default("Valued Customer", true) }}`  
  
## Loops (`for`)

Use `{% for item in collection %}...{% endfor %}` to iterate over lists in session state. Inside a loop, the built-in `loop.last` boolean variable is `true` on the final iteration, which helps you format comma-separated lists without trailing commas:
    
    
    Product Catalog:
    {% for category in catalog.categories %}
    ### {{ category.name | upper }} ({{ category.products | length }} items)
    Available: {% for item in category.products %}{{ item.title }} (${{ item.price
    }}){% if not loop.last %}, {% endif %}{% endfor %}
    {% endfor %}
    

Given the following session variable `catalog`:
    
    
    {
      "categories": [
        {
          "name": "Electronics",
          "products": [
            {"title": "Phone", "price": 699.99},
            {"title": "Tablet", "price": 399.99}
          ]
        },
        {
          "name": "Books",
          "products": [
            {"title": "Novel", "price": 19.99}
          ]
        }
      ]
    }
    

The rendered instructions sent to the model are:
    
    
    Product Catalog:
    ### ELECTRONICS (2 items)
    Available: Phone ($699.99), Tablet ($399.99)
    ### BOOKS (1 items)
    Available: Novel ($19.99)
    

## Reusable macros (`macro`)

Use `{% macro name(param1, param2) %}...{% endmacro %}` to define a reusable instruction snippet and invoke it anywhere in the same instruction with `{{ name(arg1, arg2) }}`:
    
    
    {% macro format_dest(name, price, climate) %}- **{{ name | upper
    }}** (Estimated Cost: **${{ price }}**) - *{{ climate }}* climate{% endmacro %}
    
    Recommended destinations:
    {% for dest in catalog.destinations %}
    {{ format_dest(dest.name, dest.price, dest.climate) }}
    {% endfor %}
    

## Advanced examples

The following examples demonstrate how to combine expressions, state checks, filters, loops, and macros in your instructions.

### Complex access control (`and`, `or`, `not`, `in`, parentheses)
    
    
    {% if user.is_authenticated and (
      user.role == "admin" or (
        user.department in ["security", "audit"] and not user.is_on_probation
      )
    ) %}
    [AUTHORIZED] Access to sensitive account logs granted.
    {% else %}
    [DENIED] Do not disclose sensitive account logs.
    {% endif %}
    

  * When `user` is `{"is_authenticated": true, "role": "user", "department": "security", "is_on_probation": false}`, the model receives: `[AUTHORIZED] Access to sensitive account logs granted.`
  * When `user` is `{"is_authenticated": true, "role": "user", "department": "engineering", "is_on_probation": false}`, the model receives: `[DENIED] Do not disclose sensitive account logs.`



### State existence checks (`is defined`, `is not none`) and fallbacks
    
    
    Customer: {{ user.preferred_name | default("Valued Customer", true) }}
    Caller ID: {{ caller_id | default("Unknown") }}
    {% if user.loyalty_tier is defined and user.loyalty_tier is not none %}
    Loyalty Tier: {{ user.loyalty_tier | upper }}
    {% elif length(user.recent_orders) >= 3 %}
    Loyalty Tier: SILVER ({{ user.recent_orders | length }} recent orders)
    {% else %}
    Loyalty Tier: STANDARD
    {% endif %}
    

When `user` is `{"preferred_name": "", "loyalty_tier": null, "recent_orders": ["ORD-1", "ORD-2", "ORD-3"]}` and `caller_id` is `"+1-800-555-0199"`, the rendered output is:
    
    
    Customer: Valued Customer
    Caller ID: +1-800-555-0199
    Loyalty Tier: SILVER (3 recent orders)
    

### End-to-end instruction template

The following example combines static variables, dynamic variables, macros, filters, `is defined` tests, loops, and conditional blocks inside the [recommended XML instruction structure](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/instruction#restructure):
    
    
    CURRENT CUSTOMER: {{ user.name | default("Guest", true) }}
    CALLER ID: {{ caller_id }}
    CURRENT DATE: {{ current_date }}
    {% macro format_dest(name, price, climate) %}- **{{ name | upper
    }}** (Estimated Cost: **${{ price }}**) - *{{ climate }}* climate{% endmacro %}
    <role>
      A professional Travel Assistant matching users with their dream vacations.
    </role>
    {% if user.is_authenticated and (
      user.role == "VIP" or (
        preferences.budget == "high" and not user.is_restricted
      )
    ) %}
    <persona>
      <primary_goal>
        Provide exclusive luxury travel recommendations and white-glove service.
      </primary_goal>
      You are serving a high-value customer. Emphasize luxury options.
    </persona>
    <constraints>
      1. Use {@TOOL: book_luxury_trip} for all booking requests.
      2. Always offer access to the **VIP Lounge**.
    </constraints>
    {% elif user.is_authenticated and user.loyalty_points is defined
      and user.loyalty_points >= 5000 %}
    <persona>
      <primary_goal>
        Reward loyal travelers with priority upgrades and curated packages.
      </primary_goal>
      Acknowledge the customer's loyalty points ({{ user.loyalty_points }}) and
      offer complimentary seat upgrades.
    </persona>
    <constraints>
      1. Use {@TOOL: book_standard_trip} for all booking requests.
      2. Offer priority boarding on eligible flights.
    </constraints>
    {% else %}
    <persona>
      <primary_goal>
        Provide high-value, accessible travel recommendations.
      </primary_goal>
      Be friendly, helpful, and focused on finding the best value for the customer.
    </persona>
    <constraints>
      1. Use {@TOOL: book_standard_trip} for all booking requests.
      2. Focus on standard packages.
    </constraints>
    {% endif %}
    <taskflow>
      <subtask name="Destination Recommendations">
        <step name="List Matching Destinations">
          <trigger>User asks for vacation ideas.</trigger>
          <action>
            Here are curated options for your trip (out of
            {{ catalog.destinations | length }} total destinations):
    {% for dest in catalog.destinations %}
    {% if dest.climate == preferences.climate
      or (dest.is_featured and dest.price <= 2000) %}
            {{ format_dest(dest.name, dest.price, dest.climate) }}
    {% endif %}
    {% endfor %}
            {% if preferences.climate in ["tropical", "subtropical"] %}
            Remind the customer to pack sunscreen for this climate.
            {% endif %}
            Dynamic tracking for next turn: {user_reaction}
          </action>
        </step>
      </subtask>
    </taskflow>
    

## Error handling and fallback behavior

  * **Isolated print expressions (`{{ ... }}`)**: Each `{{ ... }}` expression is parsed independently. If a single `{{ ... }}` tag contains unsupported syntax or an unknown filter, only that individual tag falls back to literal text; all other valid substitutions and control blocks in the instruction continue to render normally.
  * **Control flow blocks (`{% ... %}`)**: Control flow blocks (`if`/`elif`/`else`/`endif`, `for`/`endfor`, and `macro`/`endmacro`) must be properly balanced and closed. If an instruction contains a malformed or unclosed control block tag, the runtime logs a diagnostic with the line and column number and falls back to basic `{{variable}}` substitution for that render.



## Syntax highlighting and editor shortcuts

When authoring modular components in the console, valid references and tags are highlighted with colored chips:

  * Typing `@` in the instructions editor opens a context menu to insert agent references, tool references, and channel or modality block tags.
  * Typing `{` opens a context menu showing available variables for quick insertion.

**Note:** For the **Tool** option, only tools that have been added to the current agent appear in the context menu.

## Testing modular components

  * **Simulator** : When testing an agent that uses modular components in the [simulator](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator), the trace view displays the active `_session` variable values (`modality` and `channel`) alongside custom variables for each turn.
  * **Evaluations** : When running [evaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation) against instructions that branch on modality or channel, set the `_session` [scenario variable](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation#scenario_variables) in your test scenario. For example, to test the `TEXT` modality on the `API` channel:
        
        {
          "modality": "TEXT",
          "channel": "API"
        }
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
