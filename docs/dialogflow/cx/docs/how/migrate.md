---
url: https://docs.cloud.google.com/dialogflow/cx/docs/how/migrate/
title: Migrating from Dialogflow ES to Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:56.470810+00:00
---

# Migrating from Dialogflow ES to Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/how/migrate/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Migrating from Dialogflow ES to Dialogflow CX Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow CX agents provide you with [more powerful conversation controls and tools](https://docs.cloud.google.com/dialogflow/docs/editions#agent-types) than Dialogflow ES agents. If your Dialogflow ES agent handles complex conversations, you should consider migrating to Dialogflow CX.

This guide describes how to migrate an agent from Dialogflow Dialogflow ES to Dialogflow CX. These two agent types have many fundamental differences, so there is no straightforward way to perform this migration.

If you use this guide for a migration, please provide positive or negative feedback by clicking the **Send feedback** button above. We will use this feedback to improve this guide over time.

At a high level, the recommended process is an automated/manual hybrid process. You will use a tool that reads some of your Dialogflow ES agent data, writes that data to your Dialogflow CX agent, and captures a TODO list. You then re-create your complete Dialogflow CX agent using best practices, the TODO list, and the data that was migrated by the tool.

## Understand Dialogflow CX

Before attempting this migration, you should have a solid understanding of how Dialogflow CX flows work. You can start here:

  * [Flow basics](https://docs.cloud.google.com/dialogflow/cx/docs/basics)



You should also read through additional concept documents that have features you are likely to need in your new agent. Focus on the following:

  * [Console overview](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console)
  * [Agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent)
  * [Flows](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow)
  * [Pages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page)
  * [State handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler)
  * [Intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent)
  * [Parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter)
  * [Fulfillments](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment)
  * [Webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook)



## Understand Dialogflow ES/Dialogflow CX differences

This section lists the most important differences between Dialogflow ES and Dialogflow CX. When performing manual migration steps later, you should refer to this section for guidance.

### Structure and conversation path control

Dialogflow ES provides the following for structure and conversation path control:

  * [Intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) are used as the building blocks of the agent. At any point in the conversation, an intent is matched, and in a sense, each intent is a node for the conversation.
  * [Context](https://docs.cloud.google.com/dialogflow/es/docs/contexts-overview) is used to control the conversation. Context is used to control which intents can be matched at any given time. Context expires after a certain number of conversational turns, so this type of control can be inaccurate for long conversations.



Dialogflow CX provides a hierarchy of structure resources and more precise controls over the conversation path:

  * [Pages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page) are graph nodes for the conversation. Dialogflow CX conversations are similar to state machines. At any given point in the conversation, one page is active. Based on end-user input or events, the conversation may transition to another page. It is common for a page to remain active for multiple conversational turns.
  * [Flows](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow) are groups of related pages. Each flow should handle a high-level conversation topic.
  * [State handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler) are used to control transitions and responses. There are three types of state handlers: 
    * **Intent route** : contains an intent that must be matched, optional responses, and optional page transition.
    * **Condition route** : contains a condition that must be met, optional responses, and optional page transition.
    * **Event handler** : contains an event name that must be invoked, optional responses, and optional page transition.
  * [Scope](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#scope) is used to control whether a state handler can be called. Most handlers are associated with a page or entire flow. If the associated page or flow is active, then the handler is in scope, and it can be called. A Dialogflow CX intent route in scope is similar to an Dialogflow ES intent with an input context that is active.



When designing the flows and pages of your agent, be sure to understand the advice in the [flow section of the agent design guide](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-design#flow-page).

### Form filling

Dialogflow ES uses [slot filling](https://docs.cloud.google.com/dialogflow/es/docs/intents-actions-parameters#required) to collect required parameters from the end-user:

  * These parameters are intent parameters marked as required.
  * The intent continues being matched until all required parameters are collected.
  * You can define a prompt asking the end-user to provide a value.



Dialogflow CX uses [form filling](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form) to collect required parameters from the end-user:

  * These parameters are associated with a page and are collected while the page is active.
  * You use condition routes for pages to determine that [form filling is complete](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form-ref). These condition routes typically transition to another page.
  * You can define a prompt, as well as [re-prompt handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#form-reprompt) to gracefully handle multiple attempts to collect a value.



### Transitions

Dialogflow ES automatically transitions from one intent to the next when end-user input is matched to an intent. This match can only occur for intents that have no input context or intents that have an active input context.

Dialogflow CX transitions from one page to the next when a state handler in scope satisfies its requirements and provides a transition target. Using these transitions, you can reliably guide end-users through conversations. There are multiple ways to control these transitions:

  * Intent matching can trigger an intent route.
  * Satisfying a condition can trigger a condition route.
  * Invocation of an event can trigger an event handler.
  * Re-prompt handlers can cause a transition when the end-user fails to provide a value after multiple attempts.
  * You can use [symbolic transition targets](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#symbolic) for transition targets.



### Agent responses

Dialogflow ES agent responses are sent to the end-user when an intent is matched:

  * The agent can select one message for the response from a list of possible responses.
  * Responses can be platform-specific, which can use [rich response formats](https://docs.cloud.google.com/dialogflow/es/docs/intents-rich-messages).
  * Responses can be driven by webhooks.



Dialogflow CX agent responses are sent to the end-user when [fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment) is called. Unlike Dialogflow ES fulfillment, which always involves a webhook, Dialogflow CX fulfillment may or may not involve calling a webhook, depending on whether the fulfillment resource has a webhook configured. Both static and dynamic responses based on webhook responses are controlled by fulfillment. There are multiple ways to create agent responses:

  * Fulfillment can be provided to any type of state handler.
  * Multiple responses can be concatenated during a conversational turn via the [response queue](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#queue). This feature can simplify your agent design in some cases.
  * Dialogflow CX does not support built-in platform-specific responses. However, it provides [multiple response types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#static), including a custom payload which can be used for platform-specific responses.



### Parameters

[Dialogflow ES parameters](https://docs.cloud.google.com/dialogflow/es/docs/intents-actions-parameters) have the following characteristics:

  * Defined only in intents.
  * Set by end-user input, events, webhooks, and API calls.
  * Referenced in responses, parameter prompts, webhook code, and [parameter values](https://docs.cloud.google.com/dialogflow/es/docs/intents-actions-parameters#valfield): 
    * Basic reference format is `$parameter-name`.
    * References support `.original`, `.partial`, and `.recent` suffix syntax.
    * References can specify the active context: `#context-name.parameter-name`.
    * References can specify event parameters: `#event-name.parameter-name`.



[Dialogflow CX parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter) have the following characteristics:

  * Defined in intents and page forms.
  * Intent and form parameters are [propagated to session parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#prop), where they are available for referencing for the duration of the session.
  * Set by end-user input, webhooks, [fulfillment parameter preset](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#param-preset), and API calls.
  * Referenced in responses, parameter prompts, re-prompt handlers, parameter presets, and webhook code: 
    * Reference format is `$session.params.parameter-id` for session parameters and `$intent.params.parameter-id` for intent parameters.
    * Intent parameter references support `.original` and `.resolved` suffix syntax. Session parameters do not support this syntax.



### System entities

Dialogflow ES supports many [system entities](https://docs.cloud.google.com/dialogflow/es/docs/reference/system-entities).

Dialogflow CX supports many of the same [system entities](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-entities), but there are some differences. When migrating, verify that system entities you are using in Dialogflow ES are also supported by Dialogflow CX for the same language. If not, you should create custom entities for these.

### Events

[Dialogflow ES events](https://docs.cloud.google.com/dialogflow/es/docs/events-overview) have the following characteristics:

  * Can be invoked from API calls or webhooks to match an intent.
  * Can set parameters.
  * A small number of events are invoked by integration platforms.



[Dialogflow CX events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event) have the following characteristics:

  * Can be invoked from API calls or webhooks to call an event handler.
  * Cannot set parameters.
  * Many built-in events can be used for handling lack of end-user input, unrecognized end-user input, parameters invalidated by a webhook, and webhook errors.
  * Invocations can be controlled by the same [scoping rules](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#scope) as other state handlers.



### Built-in intents

Dialogflow ES supports the following built-in intents:

  * [Welcome intent](https://docs.cloud.google.com/dialogflow/es/docs/intents-default#welcome)
  * [Fallback intents](https://docs.cloud.google.com/dialogflow/es/docs/intents-default#fallback)
  * [Predefined follow-up intents](https://docs.cloud.google.com/dialogflow/es/docs/reference/follow-up-intent-expressions)



The following describes the Dialogflow CX support for built-in intents:

  * [Welcome intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#welcome) are supported.
  * Fallback intents are not provided. Use the [no-match](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in) events in event handlers instead.
  * For negative examples, use the [default negative intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#negative).
  * Predefined follow-up intents are not provided. You must create these intents as required by your agent. For example, you will likely need to create an intent to handle negative answers to an agent question ("no", "no thanks", "no I don't", and so on). Dialogflow CX intents are reusable across your agent, so you only need to define these once. Using different intent routes for these common intents, in different scopes, gives you much better control over the conversation.



### Webhooks

[Dialogflow ES webhooks](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook) have the following characteristics:

  * You can configure one webhook service for the agent.
  * Each intent can be marked as using the webhook.
  * There is no built-in support for handling webhook errors.
  * Intent actions or intent names are used by webhooks to determine where in the agent it was called from.
  * The console provides the [inline editor](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-inline-editor).



[Dialogflow CX webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook) have the following characteristics:

  * You can configure multiple webhook services for the agent.
  * Each fulfillment can optionally specify a webhook call.
  * There is built-in support for [webhook error handling](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#errors).
  * A Dialogflow CX fulfillment webhook contains a [tag](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#webhook). This tag is similar to an Dialogflow ES action, but it is only used when calling webhooks. The webhook service can use these tags to determine where in the agent it was called from.
  * The console does not have a built-in webhook code editor. It is common to use [Cloud Run functions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#cloud-run), but there are many options.



When migrating to Dialogflow CX, you will need to change your webhook code, as the request and response properties are different.

### Integrations

[Dialogflow ES integrations](https://docs.cloud.google.com/dialogflow/es/docs/integrations) and [Dialogflow CX integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration) support different platforms. For platforms that are supported by both agent types, there may be differences in configuration.

If the Dialogflow ES integration you were using is not supported by Dialogflow CX, you may need to switch platforms or implement the integration yourself.

### More Dialogflow CX-only features

There are many other features only provided by Dialogflow CX. You should consider using these features while migrating. For example:

  * [Advanced NLU](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-ml)
  * [Advanced speech settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-speech) (end of speech sensitivity, no speech timeout, and so on)
  * [Change history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/change-history)
  * [Conditional logic](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#cond)
  * [DTMF input for telephony integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#dtmf)
  * [Environment-specific webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#environment-specific)
  * [Experiments](https://docs.cloud.google.com/dialogflow/cx/docs/concept/experiments)
  * [Route groups](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route-group)
  * [Search agent data](https://docs.cloud.google.com/dialogflow/cx/docs/concept/search)
  * [Security settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/security-settings) (redaction and data retention)
  * [System functions for advanced responses and conditions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions)
  * [Test cases](https://docs.cloud.google.com/dialogflow/cx/docs/concept/test-case)
  * [Validation of agent data](https://docs.cloud.google.com/dialogflow/cx/docs/concept/validation)



## Best practices

Before migrating, familiarize yourself with [Dialogflow CX agent design best practices](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-design). Many of these Dialogflow CX best practices are similar to Dialogflow ES best practices, but some are unique to Dialogflow CX.

## About the migration tool

The migration tool copies the bulk of the Dialogflow ES data to your Dialogflow CX agent, and it writes to a TODO file with a list of items that must be manually migrated. The tool only copies custom entity types and intent training phrases. You should consider customizing this tool for your specific needs.

### Migration tool code

Here is the code for the tool. You should review the code for this tool, so you understand what it does. You may want to change this code to handle specific situations in your agent. In steps below, you will execute this tool.
    
    
    // Package main implements the ES to CX migration tool.
    package main
    
    import (
    	"context"
    	"encoding/csv"
    	"flag"
    	"fmt"
    	"os"
    	"strings"
    	"time"
    
    	v2 "cloud.google.com/go/dialogflow/apiv2"
    	proto2 "cloud.google.com/go/dialogflow/apiv2/dialogflowpb"
    	v3 "cloud.google.com/go/dialogflow/cx/apiv3"
    	proto3 "cloud.google.com/go/dialogflow/cx/apiv3/cxpb"
    	"google.golang.org/api/iterator"
    	"google.golang.org/api/option"
    )
    
    // Commandline flags
    var v2Project *string = flag.String("es-project-id", "", "ES project")
    var v3Project *string = flag.String("cx-project-id", "", "CX project")
    var v2Region *string = flag.String("es-region-id", "", "ES region")
    var v3Region *string = flag.String("cx-region-id", "", "CX region")
    var v3Agent *string = flag.String("cx-agent-id", "", "CX region")
    var outFile *string = flag.String("out-file", "", "Output file for CSV TODO items")
    var dryRun *bool = flag.Bool("dry-run", false, "Set true to skip CX agent writes")
    
    // Map from entity type display name to fully qualified name.
    var entityTypeShortToLong = map[string]string{}
    
    // Map from ES system entity to CX system entity
    var convertSystemEntity = map[string]string{
    	"sys.address":         "sys.address",
    	"sys.any":             "sys.any",
    	"sys.cardinal":        "sys.cardinal",
    	"sys.color":           "sys.color",
    	"sys.currency-name":   "sys.currency-name",
    	"sys.date":            "sys.date",
    	"sys.date-period":     "sys.date-period",
    	"sys.date-time":       "sys.date-time",
    	"sys.duration":        "sys.duration",
    	"sys.email":           "sys.email",
    	"sys.flight-number":   "sys.flight-number",
    	"sys.geo-city-gb":     "sys.geo-city",
    	"sys.geo-city-us":     "sys.geo-city",
    	"sys.geo-city":        "sys.geo-city",
    	"sys.geo-country":     "sys.geo-country",
    	"sys.geo-state":       "sys.geo-state",
    	"sys.geo-state-us":    "sys.geo-state",
    	"sys.geo-state-gb":    "sys.geo-state",
    	"sys.given-name":      "sys.given-name",
    	"sys.language":        "sys.language",
    	"sys.last-name":       "sys.last-name",
    	"sys.street-address":  "sys.location",
    	"sys.location":        "sys.location",
    	"sys.number":          "sys.number",
    	"sys.number-integer":  "sys.number-integer",
    	"sys.number-sequence": "sys.number-sequence",
    	"sys.ordinal":         "sys.ordinal",
    	"sys.percentage":      "sys.percentage",
    	"sys.person":          "sys.person",
    	"sys.phone-number":    "sys.phone-number",
    	"sys.temperature":     "sys.temperature",
    	"sys.time":            "sys.time",
    	"sys.time-period":     "sys.time-period",
    	"sys.unit-currency":   "sys.unit-currency",
    	"sys.url":             "sys.url",
    	"sys.zip-code":        "sys.zip-code",
    }
    
    // Issues found for the CSV output
    var issues = [][]string{
    	{"Field", "Issue"},
    }
    
    // logIssue logs an issue for the CSV output
    func logIssue(field string, issue string) {
    	issues = append(issues, []string{field, issue})
    }
    
    // convertEntityType converts an ES entity type to CX
    func convertEntityType(et2 *proto2.EntityType) *proto3.EntityType {
    	var kind3 proto3.EntityType_Kind
    	switch kind2 := et2.Kind; kind2 {
    	case proto2.EntityType_KIND_MAP:
    		kind3 = proto3.EntityType_KIND_MAP
    	case proto2.EntityType_KIND_LIST:
    		kind3 = proto3.EntityType_KIND_LIST
    	case proto2.EntityType_KIND_REGEXP:
    		kind3 = proto3.EntityType_KIND_REGEXP
    	default:
    		kind3 = proto3.EntityType_KIND_UNSPECIFIED
    	}
    	var expansion3 proto3.EntityType_AutoExpansionMode
    	switch expansion2 := et2.AutoExpansionMode; expansion2 {
    	case proto2.EntityType_AUTO_EXPANSION_MODE_DEFAULT:
    		expansion3 = proto3.EntityType_AUTO_EXPANSION_MODE_DEFAULT
    	default:
    		expansion3 = proto3.EntityType_AUTO_EXPANSION_MODE_UNSPECIFIED
    	}
    	et3 := &proto3.EntityType{
    		DisplayName:           et2.DisplayName,
    		Kind:                  kind3,
    		AutoExpansionMode:     expansion3,
    		EnableFuzzyExtraction: et2.EnableFuzzyExtraction,
    	}
    	for _, e2 := range et2.Entities {
    		et3.Entities = append(et3.Entities, &proto3.EntityType_Entity{
    			Value:    e2.Value,
    			Synonyms: e2.Synonyms,
    		})
    	}
    	return et3
    }
    
    // convertParameterEntityType converts a entity type found in parameters
    func convertParameterEntityType(intent string, parameter string, t2 string) string {
    	if len(t2) == 0 {
    		return ""
    	}
    	t2 = t2[1:] // remove @
    	if strings.HasPrefix(t2, "sys.") {
    		if val, ok := convertSystemEntity[t2]; ok {
    			t2 = val
    		} else {
    			t2 = "sys.any"
    			logIssue("Intent<"+intent+">.Parameter<"+parameter+">",
    				"This intent parameter uses a system entity not supported by CX English agents. See the migration guide for advice. System entity: "+t2)
    		}
    		return fmt.Sprintf("projects/-/locations/-/agents/-/entityTypes/%s", t2)
    	}
    	return entityTypeShortToLong[t2]
    }
    
    // convertIntent converts an ES intent to CX
    func convertIntent(intent2 *proto2.Intent) *proto3.Intent {
    	if intent2.DisplayName == "Default Fallback Intent" ||
    		intent2.DisplayName == "Default Welcome Intent" {
    		return nil
    	}
    
    	intent3 := &proto3.Intent{
    		DisplayName: intent2.DisplayName,
    	}
    
    	// WebhookState
    	if intent2.WebhookState != proto2.Intent_WEBHOOK_STATE_UNSPECIFIED {
    		logIssue("Intent<"+intent2.DisplayName+">.WebhookState",
    			"This intent has webhook enabled. You must configure this in your CX agent.")
    	}
    
    	// IsFallback
    	if intent2.IsFallback {
    		logIssue("Intent<"+intent2.DisplayName+">.IsFallback",
    			"This intent is a fallback intent. CX does not support this. Use no-match events instead.")
    	}
    
    	// MlDisabled
    	if intent2.MlDisabled {
    		logIssue("Intent<"+intent2.DisplayName+">.MlDisabled",
    			"This intent has ML disabled. CX does not support this.")
    	}
    
    	// LiveAgentHandoff
    	if intent2.LiveAgentHandoff {
    		logIssue("Intent<"+intent2.DisplayName+">.LiveAgentHandoff",
    			"This intent uses live agent handoff. You must configure this in a fulfillment.")
    	}
    
    	// EndInteraction
    	if intent2.EndInteraction {
    		logIssue("Intent<"+intent2.DisplayName+">.EndInteraction",
    			"This intent uses end interaction. CX does not support this.")
    	}
    
    	// InputContextNames
    	if len(intent2.InputContextNames) > 0 {
    		logIssue("Intent<"+intent2.DisplayName+">.InputContextNames",
    			"This intent uses context. See the migration guide for alternatives.")
    	}
    
    	// Events
    	if len(intent2.Events) > 0 {
    		logIssue("Intent<"+intent2.DisplayName+">.Events",
    			"This intent uses events. Use event handlers instead.")
    	}
    
    	// TrainingPhrases
    	var trainingPhrases3 []*proto3.Intent_TrainingPhrase
    	for _, tp2 := range intent2.TrainingPhrases {
    		if tp2.Type == proto2.Intent_TrainingPhrase_TEMPLATE {
    			logIssue("Intent<"+intent2.DisplayName+">.TrainingPhrases",
    				"This intent has a training phrase that uses a template (@...) training phrase type. CX does not support this.")
    		}
    		var parts3 []*proto3.Intent_TrainingPhrase_Part
    		for _, part2 := range tp2.Parts {
    			parts3 = append(parts3, &proto3.Intent_TrainingPhrase_Part{
    				Text:        part2.Text,
    				ParameterId: part2.Alias,
    			})
    		}
    		trainingPhrases3 = append(trainingPhrases3, &proto3.Intent_TrainingPhrase{
    			Parts:       parts3,
    			RepeatCount: 1,
    		})
    	}
    	intent3.TrainingPhrases = trainingPhrases3
    
    	// Action
    	if len(intent2.Action) > 0 {
    		logIssue("Intent<"+intent2.DisplayName+">.Action",
    			"This intent sets the action field. Use a fulfillment webhook tag instead.")
    	}
    
    	// OutputContexts
    	if len(intent2.OutputContexts) > 0 {
    		logIssue("Intent<"+intent2.DisplayName+">.OutputContexts",
    			"This intent uses context. See the migration guide for alternatives.")
    	}
    
    	// ResetContexts
    	if intent2.ResetContexts {
    		logIssue("Intent<"+intent2.DisplayName+">.ResetContexts",
    			"This intent uses context. See the migration guide for alternatives.")
    	}
    
    	// Parameters
    	var parameters3 []*proto3.Intent_Parameter
    	for _, p2 := range intent2.Parameters {
    		if len(p2.Value) > 0 && p2.Value != "$"+p2.DisplayName {
    			logIssue("Intent<"+intent2.DisplayName+">.Parameters<"+p2.DisplayName+">.Value",
    				"This field is not set to $parameter-name. This feature is not supported by CX. See: https://cloud.google.com/dialogflow/es/docs/intents-actions-parameters#valfield.")
    		}
    		if len(p2.DefaultValue) > 0 {
    			logIssue("Intent<"+intent2.DisplayName+">.Parameters<"+p2.DisplayName+">.DefaultValue",
    				"This intent parameter is using a default value. CX intent parameters do not support default values, but CX page form parameters do. This parameter should probably become a form parameter.")
    		}
    		if p2.Mandatory {
    			logIssue("Intent<"+intent2.DisplayName+">.Parameters<"+p2.DisplayName+">.Mandatory",
    				"This intent parameter is marked as mandatory. CX intent parameters do not support mandatory parameters, but CX page form parameters do. This parameter should probably become a form parameter.")
    		}
    		for _, prompt := range p2.Prompts {
    			logIssue("Intent<"+intent2.DisplayName+">.Parameters<"+p2.DisplayName+">.Prompts",
    				"This intent parameter has a prompt. Use page form parameter prompts instead. Prompt: "+prompt)
    		}
    		if len(p2.EntityTypeDisplayName) == 0 {
    			p2.EntityTypeDisplayName = "@sys.any"
    			logIssue("Intent<"+intent2.DisplayName+">.Parameters<"+p2.DisplayName+">.EntityTypeDisplayName",
    				"This intent parameter does not have an entity type. CX requires an entity type for all parameters..")
    		}
    		parameters3 = append(parameters3, &proto3.Intent_Parameter{
    			Id:         p2.DisplayName,
    			EntityType: convertParameterEntityType(intent2.DisplayName, p2.DisplayName, p2.EntityTypeDisplayName),
    			IsList:     p2.IsList,
    		})
    		//fmt.Printf("Converted parameter: %+v\n", parameters3[len(parameters3)-1])
    	}
    	intent3.Parameters = parameters3
    
    	// Messages
    	for _, message := range intent2.Messages {
    		m, ok := message.Message.(*proto2.Intent_Message_Text_)
    		if ok {
    			for _, t := range m.Text.Text {
    				warnings := ""
    				if strings.Contains(t, "#") {
    					warnings += " This message may contain a context parameter reference, but CX does not support this."
    				}
    				if strings.Contains(t, ".original") {
    					warnings += " This message may contain a parameter reference suffix of '.original', But CX only supports this for intent parameters (not session parameters)."
    				}
    				if strings.Contains(t, ".recent") {
    					warnings += " This message may contain a parameter reference suffix of '.recent', but CX does not support this."
    				}
    				if strings.Contains(t, ".partial") {
    					warnings += " This message may contain a parameter reference suffix of '.partial', but CX does not support this."
    				}
    				logIssue("Intent<"+intent2.DisplayName+">.Messages",
    					"This intent has a response message. Use fulfillment instead."+warnings+" Message: "+t)
    			}
    		} else {
    			logIssue("Intent<"+intent2.DisplayName+">.Messages",
    				"This intent has a non-text response message. See the rich response message information in the migration guide.")
    		}
    		if message.Platform != proto2.Intent_Message_PLATFORM_UNSPECIFIED {
    			logIssue("Intent<"+intent2.DisplayName+">.Platform",
    				"This intent has a message with a non-default platform. See the migration guide for advice.")
    		}
    	}
    
    	return intent3
    }
    
    // migrateEntities migrates ES entities to your CX agent
    func migrateEntities(ctx context.Context) error {
    	var err error
    
    	// Create ES client
    	var client2 *v2.EntityTypesClient
    	options2 := []option.ClientOption{}
    	if len(*v2Region) > 0 {
    		options2 = append(options2,
    			option.WithEndpoint(*v2Region+"-dialogflow.googleapis.com:443"))
    	}
    	client2, err = v2.NewEntityTypesClient(ctx, options2...)
    	if err != nil {
    		return err
    	}
    	defer client2.Close()
    	var parent2 string
    	if len(*v2Region) == 0 {
    		parent2 = fmt.Sprintf("projects/%s/agent", *v2Project)
    	} else {
    		parent2 = fmt.Sprintf("projects/%s/locations/%s/agent", *v2Project, *v2Region)
    	}
    
    	// Create CX client
    	var client3 *v3.EntityTypesClient
    	options3 := []option.ClientOption{}
    	if len(*v3Region) > 0 {
    		options3 = append(options3,
    			option.WithEndpoint(*v3Region+"-dialogflow.googleapis.com:443"))
    	}
    	client3, err = v3.NewEntityTypesClient(ctx, options3...)
    	if err != nil {
    		return err
    	}
    	defer client3.Close()
    	parent3 := fmt.Sprintf("projects/%s/locations/%s/agents/%s", *v3Project, *v3Region, *v3Agent)
    
    	// Read each V2 entity type, convert, and write to V3
    	request2 := &proto2.ListEntityTypesRequest{
    		Parent: parent2,
    	}
    	it2 := client2.ListEntityTypes(ctx, request2)
    	for {
    		var et2 *proto2.EntityType
    		et2, err = it2.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Printf("Entity Type: %s\n", et2.DisplayName)
    
    		if *dryRun {
    			convertEntityType(et2)
    			continue
    		}
    
    		request3 := &proto3.CreateEntityTypeRequest{
    			Parent:     parent3,
    			EntityType: convertEntityType(et2),
    		}
    		et3, err := client3.CreateEntityType(ctx, request3)
    		entityTypeShortToLong[et3.DisplayName] = et3.Name
    		if err != nil {
    			return err
    		}
    
    		// ES and CX each have a quota limit of 60 design-time requests per minute
    		time.Sleep(2 * time.Second)
    	}
    	return nil
    }
    
    // migrateIntents migrates intents to your CX agent
    func migrateIntents(ctx context.Context) error {
    	var err error
    
    	// Create ES client
    	var client2 *v2.IntentsClient
    	options2 := []option.ClientOption{}
    	if len(*v2Region) > 0 {
    		options2 = append(options2,
    			option.WithEndpoint(*v2Region+"-dialogflow.googleapis.com:443"))
    	}
    	client2, err = v2.NewIntentsClient(ctx, options2...)
    	if err != nil {
    		return err
    	}
    	defer client2.Close()
    	var parent2 string
    	if len(*v2Region) == 0 {
    		parent2 = fmt.Sprintf("projects/%s/agent", *v2Project)
    	} else {
    		parent2 = fmt.Sprintf("projects/%s/locations/%s/agent", *v2Project, *v2Region)
    	}
    
    	// Create CX client
    	var client3 *v3.IntentsClient
    	options3 := []option.ClientOption{}
    	if len(*v3Region) > 0 {
    		options3 = append(options3,
    			option.WithEndpoint(*v3Region+"-dialogflow.googleapis.com:443"))
    	}
    	client3, err = v3.NewIntentsClient(ctx, options3...)
    	if err != nil {
    		return err
    	}
    	defer client3.Close()
    	parent3 := fmt.Sprintf("projects/%s/locations/%s/agents/%s", *v3Project, *v3Region, *v3Agent)
    
    	// Read each V2 entity type, convert, and write to V3
    	request2 := &proto2.ListIntentsRequest{
    		Parent:     parent2,
    		IntentView: proto2.IntentView_INTENT_VIEW_FULL,
    	}
    	it2 := client2.ListIntents(ctx, request2)
    	for {
    		var intent2 *proto2.Intent
    		intent2, err = it2.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Printf("Intent: %s\n", intent2.DisplayName)
    		intent3 := convertIntent(intent2)
    		if intent3 == nil {
    			continue
    		}
    
    		if *dryRun {
    			continue
    		}
    
    		request3 := &proto3.CreateIntentRequest{
    			Parent: parent3,
    			Intent: intent3,
    		}
    		_, err := client3.CreateIntent(ctx, request3)
    		if err != nil {
    			return err
    		}
    
    		// ES and CX each have a quota limit of 60 design-time requests per minute
    		time.Sleep(2 * time.Second)
    	}
    	return nil
    }
    
    // checkFlags checks commandline flags
    func checkFlags() error {
    	flag.Parse()
    	if len(*v2Project) == 0 {
    		return fmt.Errorf("Need to supply es-project-id flag")
    	}
    	if len(*v3Project) == 0 {
    		return fmt.Errorf("Need to supply cx-project-id flag")
    	}
    	if len(*v2Region) == 0 {
    		fmt.Printf("No region supplied for ES, using default\n")
    	}
    	if len(*v3Region) == 0 {
    		return fmt.Errorf("Need to supply cx-region-id flag")
    	}
    	if len(*v3Agent) == 0 {
    		return fmt.Errorf("Need to supply cx-agent-id flag")
    	}
    	if len(*outFile) == 0 {
    		return fmt.Errorf("Need to supply out-file flag")
    	}
    	return nil
    }
    
    // closeFile is used as a convenience for defer
    func closeFile(f *os.File) {
    	err := f.Close()
    	if err != nil {
    		fmt.Fprintf(os.Stderr, "ERROR closing CSV file: %v\n", err)
    		os.Exit(1)
    	}
    }
    
    func main() {
    	if err := checkFlags(); err != nil {
    		fmt.Fprintf(os.Stderr, "ERROR checking flags: %v\n", err)
    		os.Exit(1)
    	}
    	ctx := context.Background()
    	if err := migrateEntities(ctx); err != nil {
    		fmt.Fprintf(os.Stderr, "ERROR migrating entities: %v\n", err)
    		os.Exit(1)
    	}
    	if err := migrateIntents(ctx); err != nil {
    		fmt.Fprintf(os.Stderr, "ERROR migrating intents: %v\n", err)
    		os.Exit(1)
    	}
    	csvFile, err := os.Create(*outFile)
    	if err != nil {
    		fmt.Fprintf(os.Stderr, "ERROR opening output file: %v", err)
    		os.Exit(1)
    	}
    	defer closeFile(csvFile)
    	csvWriter := csv.NewWriter(csvFile)
    	if err := csvWriter.WriteAll(issues); err != nil {
    		fmt.Fprintf(os.Stderr, "ERROR writing CSV output file: %v", err)
    		os.Exit(1)
    	}
    	csvWriter.Flush()
    }

### Tool migration of entity types

[Dialogflow ES entity types](https://docs.cloud.google.com/dialogflow/es/docs/entities-custom) and [Dialogflow CX entity types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-custom) are very similar, so they are the easiest datatype to migrate. The tool simply copies entity types as-is.

### Tool migration of intents

[Dialogflow ES intents](https://docs.cloud.google.com/dialogflow/es/docs/intents-overview) and [Dialogflow CX intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) are very different.

Dialogflow ES intents are used as the building blocks of the agent; and they contain training phrases, responses, context for conversation control, webhook configurations, events, actions, and slot filling parameters.

Dialogflow CX has moved most of this data to other resources. Dialogflow CX intents only have training phrases and parameters, which makes intents reusable across the agent. The tool only copies these two types of intent data to your Dialogflow CX intents.

### Migration tool limitations

The migration tool does not support the following:

  * **Mega agents** : The tool cannot read from multiple sub-agents, but you can call the tool multiple times against each sub-agent.
  * **Multilingual agents** : You should modify the tool to create multilingual training phrases and entity entries.
  * **System entity verification for non-English languages** : The tool creates TODO items when it finds system entities that are not [supported by Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-entities), with an assumption that English is the default language, and that it uses a US region. System entity support varies by language and region. For other languages and regions, you should modify the tool to perform this check.



## Essential migration steps

The following subsections outline migration steps to be taken. You do not need to follow these manual steps in order, and you may even need to do these steps simultaneously or in a different order. Read through the steps and begin planning your changes before you actually make changes.

After you run the migration tool, you can rebuild your Dialogflow CX agent. You will still have a fair amount of migration work to do, but the bulk of the hand entered data will be present in your Dialogflow CX agent and the TODO file.

### Create your Dialogflow CX agent

If you haven't already, [create your Dialogflow CX agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#create). Be sure to use the same default language as your Dialogflow ES agent.

### Run the migration tool

Take the following steps to execute the tool:

  1. If you haven't already, [install Go on your machine](https://go.dev/doc/install).
  2. Create a directory for the tool code called `migrate`.
  3. Copy the tool code above to a file in this directory called `main.go`.
  4. Modify the code if needed for your case.
  5. Create a [Go module](https://go.dev/ref/mod#go-mod-init) in this directory. For example:
         
         go mod init migrate
         

  6. Install the Dialogflow ES V2 and Dialogflow CX V3 Go client libraries:
         
         go get cloud.google.com/go/dialogflow/apiv2
         go get cloud.google.com/go/dialogflow/cx/apiv3
         

  7. Ensure you have set up [client library authentication](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup#auth).

  8. Run the tool, and save the output to file:
         
         go run main.go -es-project-id=<ES_PROJECT_ID> -cx-project-id=<CX_PROJECT_ID> \
         -cx-region-id=<CX_REGION_ID> -cx-agent-id=<CX_AGENT_ID> -out-file=out.csv
         




### Migration tool troubleshooting

If you experience errors when running the tool, check the following:

Error | Resolution  
---|---  
RPC error that a training phrase part mentions a parameter not defined for the intent. | This may happen if you previously used the Dialogflow ES API to create intent parameters in a way that was inconsistent with the training phrases. To fix this, rename the Dialogflow ES parameter from the console, check that your training phrases are using the parameter properly, then click save. This may also happen if your training phrases reference nonexistent parameters.  
  
After fixing errors, you will need to clear the Dialogflow CX agent of intents and entities before running the migration tool again.

### Moving Dialogflow ES intent data to Dialogflow CX

The tool migrates intent training phrases and parameters to Dialogflow CX intents, but there are many other Dialogflow ES intent fields to migrate manually.

An Dialogflow ES intent may need a corresponding Dialogflow CX page, a corresponding Dialogflow CX intent, or both.

If an Dialogflow ES intent match is used to transition the conversation from a particular conversation node to another, you should have two pages in your agent related to this intent:

  * **The original page that contains the intent route, which will transition to the next page** : The intent route in the original page may have Dialogflow CX fulfillment messages similar to the Dialogflow ES intent responses. You may have many intent routes in this page. While the original page is active, these intent routes can transition the conversation to many possible paths. Many Dialogflow ES intents will share the same corresponding Dialogflow CX original page.
  * **The next page, which is the transition target for the intent route in the original page** : The Dialogflow CX entry fulfillment for the next page may have Dialogflow CX fulfillment messages similar to the Dialogflow ES intent responses.



If an Dialogflow ES intent contains required parameters, you should create a corresponding Dialogflow CX page with the same parameters in a form.

It is common for a Dialogflow CX intent and a Dialogflow CX page to share the same parameter list, which would mean that a single Dialogflow ES intent has a corresponding Dialogflow CX page and a corresponding Dialogflow CX intent. When a Dialogflow CX intent with parameters in an intent route is matched, the conversation often transitions to a page with the same parameters. The parameters extracted from the intent match are [propagated to session parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#prop), which are available to partially or fully fill page form parameters.

Fallback intents and predefined follow-up intents do not exist in Dialogflow CX. See built-in intents.

The following table describes how to map specific intent data from Dialogflow ES to Dialogflow CX resources:

Dialogflow ES Intent data | Corresponding Dialogflow CX data | Action required  
---|---|---  
Training phrases | Intent training phrases | Migrated by tool. Tool checks for system entity support, and creates TODO items for unsupported system entities.  
Agent responses | Fulfillment response messages | See agent responses.  
Context for conversation control | None | See Structure and conversation path control.  
Webhook setting | Fulfillment webhook configuration | See webhooks.  
Events | Flow-level or Page-level event handlers | See events.  
Actions | Fulfillment webhook tags | See webhooks.  
Parameters | Intent parameters and/or Page form parameters | Migrated to intent parameters by tool. If the parameters are required, tool creates TODO items to possibly migrate to a page. See parameters.  
Parameter prompts | Page form parameter prompts | See form filling.  
  
### Create flows

Create a flow for each high-level conversation topic. The topics in each flow should be distinct, so that the conversation does not frequently jump back and forth between flows.

If you were using a mega agent, each sub-agent should become one or more flows.

### Start with basic conversation paths

It is best to test your agent with the simulator while iterating on changes. So, you should initially focus on the basic conversation paths early in the conversation, and test as you make changes. Once you get these working, move on to more detailed conversation paths.

### Flow-level versus page-level state handlers

When creating state handlers, consider whether they should be applied at flow-level or page-level. A flow-level handler is in scope whenever the flow (and hence any page within the flow) is active. A page-level handler is only in scope when the particular page is active. Flow-level handlers are similar to Dialogflow ES intents with no input context. Page-level handlers are similar to Dialogflow ES intents with input context.

### Webhook code

The webhook request and response properties are different for Dialogflow CX. See the webhooks section.

### Knowledge connectors

Dialogflow CX does not support [knowledge connectors](https://docs.cloud.google.com/dialogflow/es/docs/knowledge-connectors) yet. You will need to implement these as normal intents or wait until Dialogflow CX supports knowledge connectors.

### Agent settings

Review your [Dialogflow ES agent settings](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings), and adjust your [Dialogflow CX agent settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings) as needed.

**Note:** If your agent settings do not have automatic training configured, you will need to manually train the agent before testing changes.

### Use the TODO file

The migration tool outputs a CSV file. The items in this list are focused on particular pieces of data that may need attention. Import this file to a spreadsheet. Resolve each item in the spreadsheet, using a column for marking completion.

### API usage migration

If your system uses the Dialogflow ES API for runtime or design-time calls, you will need to update this code to use the [Dialogflow CX API](https://docs.cloud.google.com/dialogflow/cx/docs/reference/api-overview). If you only use the detect intent calls at runtime, this update should be fairly straightforward.

### Integrations

If your agent uses integrations, see the integrations section, and make changes as necessary.

## Recommended migration steps

The following subsections outline recommended migration steps.

### Validation

Use [agent validation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/validation) to check that your agent follows best practices.

### Testing

While performing manual migration steps above, you should test your agent with the [simulator](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console#simulator). Once your agent appears to be working, you should compare conversations between your Dialogflow ES and Dialogflow CX agents, and verify that behavior is similar or improved.

While testing these conversations with the simulator, you should create [test cases](https://docs.cloud.google.com/dialogflow/cx/docs/concept/test-case) to prevent future regressions.

### Environments

Review your [Dialogflow ES environments](https://docs.cloud.google.com/dialogflow/es/docs/agents-versions) and update your [Dialogflow CX environments](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version) as needed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
