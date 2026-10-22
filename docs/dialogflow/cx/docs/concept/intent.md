---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent/
title: Intents \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:08.952033+00:00
---

# Intents  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Intents Stay organized with collections  Save and categorize content based on your preferences. 

An _intent_ categorizes an end-user's intention for one conversation turn.

An intent contains the following data:

Term | Definition  
---|---  
Display name | Name displayed on the console for the intent.  
Labels | Labels that help categorize intents. For example: [head intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#head).  
Training phrases  | [Training phrases](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#tp) are example phrases for what end-users might type or say, known as _end-user input_. When end-user input resembles one of these phrases, Dialogflow CX matches the intent. You don't have to define every possible example, because Dialogflow CX's built-in machine learning expands on your list with other, similar phrases.  
Parameters  | You define your training phrases to use [parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#intent) to extract values from specific parts of the end-user input.  
DTMF patterns | See [DTMF for telephony integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/dtmf).  
  
## Intent matching

When an end-user enters input (text, speech, or telephone key-presses), Dialogflow CX compares the input to intent training phrases to find the best match. This process is called intent matching. Intent matching can only occur for intents associated with an [intent route](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route) (a state handler with an intent requirement) in [scope](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#scope).

Key-press input is matched according to [DTMF patterns](https://docs.cloud.google.com/dialogflow/cx/docs/concept/dtmf). When searching for a matching intent to text, however, Dialogflow CX scores potential matches with an _intent detection confidence_ , also known as the _confidence score_. These values range from 0.0 (completely uncertain) to 1.0 (completely certain).

Once intents are scored, there are two possible outcomes:

  * If the highest scoring intent has a confidence score greater than or equal to the [classification threshold](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-ml) setting, it is returned as a match.
  * If no intents meet the threshold, then a [no-match event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in) will be invoked.

**Note:** Dialogflow CX ML models have some level of case sensitivity, which might result in slightly different match scores for end-user inputs that differ only in capitalization. The advanced NLU model is case-sensitive, while the standard NLU model is not. See more in the [agent design best practices guide](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-design#phrase-capitalization-variety).

## Training phrases

**Note:** There are many important best practices for training phrases described in the [Agent design best practices guide](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-design#input).

_Training phrases_ are example phrases for what end-users might type or say, referred to as _end-user input_. For each intent, you create many training phrases. When an end-user input resembles one of these phrases, Dialogflow CX matches the intent.

For example, the training phrase "I want pizza" trains your agent to recognize end-user input that is similar to that phrase, like "Get a pizza" or "Order pizza."

You don't have to define every possible example because Dialogflow CX's built-in machine learning expands on your list with other, similar phrases. You should create at least 10-20 (depending on complexity of intent) training phrases so your agent can recognize a variety of end-user inputs. For example, if you want your intent to recognize an end-user's input about their favorite color, you could define the following training phrases:

  * "I like red"
  * "My favorite color is yellow"
  * "black"
  * "Blue is my favorite"
  * ...



### Auto-generate and auto-translate training phrases

You have the option of using AI generation to auto-generate training phrases instead of entering them manually. To use this feature:

  1. Navigate to the **Manage** tab and click **Intents**. Either choose an existing intent or to create a new one, click **\+ Create**.
  2. Make sure to enter a purpose for the intent in the **Description** field, for example "This intent is triggered when a user asks about their order status." The AI generator uses this field to generate more accurate training phrases.
  3. Click the **__ newly AI-generated phrases** radial button. The default value is 3. Generating more than 15 training phrases at a time can lead to errors.
  4. Click **\+ Add**. The AI will generate your specified number of training phrases and populate them into the table. Make sure to review all generated training phrases for accuracy.



For information about using this feature to auto-generate and auto-translate data for non-default languages, see the [multilingual agents documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual#ai_generate_language-specific_data)

### Annotate training phrases

**Note:** There are many important best practices for training phrase annotations described in the [agent design best practices guide](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-design#input).

You control how end-user data is extracted by _annotating_ parts of your training phrases and configuring the associated [parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter).

For example, consider a training phrase like "What is the forecast tomorrow for Tokyo?" You should annotate "tomorrow" with a `date` parameter and "Tokyo" with a `location` parameter. When you annotate parts of a training phrase, Dialogflow CX recognizes that these parts are just examples of actual values that will be provided by end-users at runtime.

For an end-user input like "What is the forecast on Friday for Sydney?", Dialogflow CX would extract the `date` parameter from "Friday" and the `location` parameter from "Sydney."

You must annotate all training phrase parts that are meant to be extracted as parameters. Otherwise, Dialogflow won't extract the values.

When building an agent with the console, most annotations are automatically created for you when you add training phrases that contain parts to be matched to an existing [entity type](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity). These parts are highlighted in the console, and you can edit annotations and parameters as needed.

To manually annotate a training phrase with the console:

  1. Select the part of the training phrase that you want to annotate.
  2. Select the wanted entity type from the list.
  3. A parameter is created for you in the following parameter table.



When building an agent with the API, you must annotate training phrase parts manually. See the `TrainingPhrase` type used by the `Intent` type. Go to the Intent API reference

**Select a protocol and version for the Intent reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Intent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents) |  [Intent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.intents)  
RPC |  [Intent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Intents) |  [Intent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Intents)  
C++ |  [IntentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1IntentsClient.html) |  Not available   
C# |  [IntentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentsClient) |  Not available   
Go |  [IntentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_IntentsClient) |  Not available   
Java |  [IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.IntentsClient) |  [IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.IntentsClient)  
Node.js |  [IntentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.IntentsClient.html) |  [IntentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.IntentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [IntentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.intents.IntentsClient) |  [IntentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.intents.IntentsClient)  
Ruby |  Not available  |  Not available   
  
Close

### Implicit entities created by training phrases

**Note:** You should define entities explicitly, rather than rely on implicitly defined custom entity values.

Most custom entities are defined explicitly by creating entity types and adding entity entries. However, custom entities may also contain implicit values. This happens when you annotate text of a training phrase, where the annotated text is not a value defined by the selected entity type. The annotated text becomes an entity reference value for the implicitly added entity entry. If the entity type is a map entity, the text also becomes a synonym for the entity entry.

## Default welcome intent

When you create an agent, a default welcome intent is created for you. For [some languages](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language#table), the intent has training phrases like "Hi" or "Hello" that are meant to match initial end-user input. You can edit this intent as needed.

When using the API, you can reference this intent with the following intent ID:
    
    
    00000000-0000-0000-0000-000000000000

If your agent initiates the conversation, you can trigger this intent using the API. Use the value `projects/<PROJECT_ID>/locations/<LOCATION_ID>/agents/<AGENT_ID>/intents/00000000-0000-0000-0000-000000000000` in the `QueryInput.intent.intent` field when calling the `detectIntent` or `streamingDetectIntent` method.

## Default negative intent

When you create an agent, a default negative intent is created for you. You can add training phrases to this intent that act as negative examples. There may be cases where end-user input has a slight resemblance to training phrases in normal intents, but you don't want these inputs to match any normal intents.

For example, a room booking agent may have a training phrase like "I'd like to book a room." If the end-user wants to purchase a book about rooms, they may say "I'd like to buy a book about rooms." To ensure that the end-user input does not match your intent, you can add that phrase as a negative example.

In addition, you should add possible phrases that are out of scope for the agent so they won't match any intent. However, avoid adding a very large quantity of these phrases. For example, if you define 10,000 default negative intent phrases, this negatively impacts normal intent matching.

You should regularly review these phrases as some of these phrases may have been originally out of scope for the agent, but were subsequently added to intents.

The default negative intent has impact across all intent matching. Phrases you add to it could benefit matching for one intent but harm matching for another. For example, you might add "international calling" to the default negative intent to avoid matching an international travel intent. However, this will also prevent that phrase from matching an international calling intent.

When using the API, you can reference this intent with the following intent ID:
    
    
    00000000-0000-0000-0000-000000000001

## Cancel intents

During a conversation, the end-user may want to cancel the current conversation topic. For example, the active page may be asking for a date for a new appointment, but the end-user has decided against creating a new appointment. The end-user may say something like "cancel" or "I don't want a new appointment." To handle this situation, you can create one or more _cancel intents_ for your agent. You can name these cancel intents anything you like, but it is customary to include "cancel" in the name. You should associate these cancel intents with intent routes that are in scope at relevant points in the conversation. These intent routes should transition to an appropriate page to handle the cancellation.

The training phrases for cancel intents should handle both generic and topic-specific attempts to cancel. For example:

  * Cancel
  * Stop
  * I changed my mind
  * Nevermind
  * Take me back
  * Go back
  * I don't want a new appointment
  * Cancel new appointment
  * Delete new appointment



## Create an intent

To create an intent:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Intents**.
  6. Click **+Create**.
  7. Enter intent data.
  8. Click **Save**.



###  API 

See the `create` method for the `Intent` type. Go to the Intent API reference

**Select a protocol and version for the Intent reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Intent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents) |  [Intent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.intents)  
RPC |  [Intent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Intents) |  [Intent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Intents)  
C++ |  [IntentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1IntentsClient.html) |  Not available   
C# |  [IntentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentsClient) |  Not available   
Go |  [IntentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_IntentsClient) |  Not available   
Java |  [IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.IntentsClient) |  [IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.IntentsClient)  
Node.js |  [IntentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.IntentsClient.html) |  [IntentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.IntentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [IntentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.intents.IntentsClient) |  [IntentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.intents.IntentsClient)  
Ruby |  Not available  |  Not available   
  
Close

## Delete an intent

To delete an intent:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Intents**.
  6. Hold the pointer over the intent you want to delete.
  7. Click the delete _delete_ button.



###  API 

See the `delete` method for the `Intent` type. Go to the Intent API reference

**Select a protocol and version for the Intent reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Intent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents) |  [Intent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.intents)  
RPC |  [Intent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Intents) |  [Intent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Intents)  
C++ |  [IntentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1IntentsClient.html) |  Not available   
C# |  [IntentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentsClient) |  Not available   
Go |  [IntentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_IntentsClient) |  Not available   
Java |  [IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.IntentsClient) |  [IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.IntentsClient)  
Node.js |  [IntentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.IntentsClient.html) |  [IntentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.IntentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [IntentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.intents.IntentsClient) |  [IntentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.intents.IntentsClient)  
Ruby |  Not available  |  Not available   
  
Close

## Access intent data

To access intent data:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Intents**.
  6. Click the intent you want to access.
  7. View or update intent data.
  8. Click **Save** to save any changes.



###  API 

See the `get` and `patch/update` methods for the `Intent` type. Go to the Intent API reference

**Select a protocol and version for the Intent reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Intent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents) |  [Intent resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.intents)  
RPC |  [Intent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Intents) |  [Intent interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Intents)  
C++ |  [IntentsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1IntentsClient.html) |  Not available   
C# |  [IntentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.IntentsClient) |  Not available   
Go |  [IntentsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_IntentsClient) |  Not available   
Java |  [IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.IntentsClient) |  [IntentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.IntentsClient)  
Node.js |  [IntentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.IntentsClient.html) |  [IntentsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.IntentsClient.html)  
PHP |  Not available  |  Not available   
Python |  [IntentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.intents.IntentsClient) |  [IntentsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.intents.IntentsClient)  
Ruby |  Not available  |  Not available   
  
Close

## Intent suggestions

**Note:** This feature is only available in the `global` and `us-central1` regions. If you need this feature for other regions, contact your Google Cloud account team.**Note:** Intent suggestions must be enabled in [general agent settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-general).

Dialogflow automatically analyzes no-match occurrences during conversations and can suggest new intents or recommend additional training phrases for existing intents. Accepting these suggestions can help to avoid future no-match occurrences.

When using suggestions, you can adjust the **Cluster Size**. Smaller values of cluster size suggest more intents with fewer training phrases per intent. Larger values of cluster size suggest fewer intents with more training phrases per intent.

To accept intent suggestions:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Intents**.
  6. Click the **Suggestions** tab.
  7. Adjust the **Cluster Size** as needed.
  8. Select a suggestion.
  9. Select the training phrases you want.
  10. For the target intent, add the training phrases to an existing or a new intent.
  11. Click **Save** or **Create New** to save any changes. When you accept intent suggestions, the intent remains in the suggestion list.



## Split intents

You can split one intent into two intents using the console. The interface lets you select training phrases from a source intent and move them to a new intent:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Intents**.
  6. Select the intent you want to split.
  7. Click **Split**.
  8. Select intents from the source intent.
  9. Click **Move right**.
  10. Provide other details for the target intent.
  11. Click **Split**.



## Compare and merge intents

You can compare or merge two intents to a single intent using the console:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Intents**.
  6. Select the two intents you want to compare or merge.
  7. Click **Compare**.
  8. The training phrases are shown side by side for comparison.
  9. To merge the two intents, click **Merge**.



## Export and import intents

You can export and import intents for sharing across agents.

One of the export format options is CSV, which has the following columns:

  * Intent Display Name
  * Language
  * Phrase



Each entry contains either the display name, language and first training phrase, or just a training phrase for the previously declared intent. Dialogflow encodes annotations in exported training phrases so that annotations are restored when importing. The format for this encoding is:
    
    
    (annotated part)[entity, parameter]
    

For example:
    
    
    Intent Display Name,Language,Phrase
    Shirt Selection,en,I want a (green)[@sys.color, color] shirt
    ,,I would like a (yellow)[@sys.color, color] shirt
    Store Hours,en,When are you open?
    ,,What are your hours?
    

When importing intents, there may be merge conflicts when the display name for an intent in your existing agent matches that of an imported intent. You can control the merge behavior when intent display names match by selecting one of the following:

  * **Replace existing intents:** An imported intent overwrites any same-named intent in your existing agent. Overwriting existing intents during import will also overwrite existing entities.
  * **Rename and import as new intents:** The imported intent is renamed by appending "_1" to the display name.
  * **Merge with existing intents:** The training phrases of an imported intent are added to the existing intent. If the same training phrases exist, they won't be duplicated.
  * **Keep original intents:** The existing intent remains unchanged, and the conflicting intent is ignored. Non-conflicting intents are imported.



To export intents:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Intents**.
  6. Select each intent you want to export.
  7. Click **Export selected intents**.
  8. Select the needed format and destination.
  9. Click **Submit**.



To import intents:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Intents**.
  6. Click **Import**.
  7. Select the source.
  8. If there are any conflicts, a dialog window is shown which allows to select the merge behavior.
  9. Click **Submit**.



## Export and import training phrases

You can export and import training phrases for an existing intent.

The file format for import is CSV without column heading, in a single column. For example:
    
    
    "I want a pony"
    "I need a pony"
    "I must have a pony"
    

When importing training phrases, you can choose one of the following import modes:

  * **Import as new training phrases:** The phrases in the files are added to the list of existing phrases.
  * **Replace existing training phrases:** The existing training phrases are deleted, and the training phrases from the files are added.



By default, imported training phrases are automatically annotated. You can disable this behavior by selecting **Skip auto annotation**.

To export training phrases for an intent:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Intents**.
  6. Select an intent.
  7. Go to the **Training phrases** section.
  8. Select the training phrases you want to export.
  9. Click **Export**.



To import training phrases for an intent:

###  Console 

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Intents**.
  6. Select an intent.
  7. Go to the **Training phrases** section.
  8. If needed, select **Skip auto annotation**.
  9. Click the import button above the training phrase list.
  10. Select a file and import mode.
  11. Click **Submit**.



## Head and supplemental intents

When designing agents, it is sometimes useful to think of intents as either _head intents_ or _supplemental intents_.

**Note:** The label "head intent" is a system label that you can apply to an intent. This may be useful when filtering [analytics](https://docs.cloud.google.com/dialogflow/cx/docs/concept/analytics) data.

A head intent identifies the end-user's primary purpose for interacting with an agent. A supplemental intent identifies an end-user's subsequent questions that are related to the head intent. These subsequent questions may provide additional context for the end-user's needs, or they may be follow-up questions that help the end-user clarify or better understand something.

A head intent is usually one of the first intents matched in a conversation, and further end-user questions match supplemental intents. For example:

Dialogue | Explanation  
---|---  
**End-user:** Activate new phone  
**Agent:** Sure, I can help you with that. What are the last 4 digits of the phone number you want to activate? | Head intent is matched.  
**End-user:** 1234  
**Agent:** Are you ready to activate your phone now? | A parameter is set.  
**End-user:** Will all of my messages carry over to my new phone?  
**Agent:** ... | Supplemental intent is matched.  
**Note:** A [route group](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route-group) provides a way to batch add related supplemental intents to multiple pages.

[ Previous arrow_back  State handlers  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler)

[ Next Entities  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
