---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ConversationalAnalytics/get_conversation/
title: Get Conversation \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:44.154201+00:00
---

# Get Conversation  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/ConversationalAnalytics/get_conversation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get Conversation Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Get Conversation

Get an conversation.

## Request

GET /conversations/{conversation_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

conversation_id

string 

Conversation ID

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields

## Response

### 200: Conversation

Datatype

Description

(object)

[Conversation](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Conversation)

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Conversation unique identifier

name

string 

Conversation name

category

string 

The category of the conversation (e.g., dashboard, conversation)

sources

[Source](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Source)[] 

Expand Source definition... 

model

string 

Source model

explore

string 

Source explore

user_id

_lock_

string 

User id

agent_id

string 

Agent id

deleted

boolean 

Is conversation soft deleted

created_at

_lock_

string 

Conversation created_at

updated_at

_lock_

string 

Conversation updated_at

messages

[ConversationMessage](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ConversationMessage)[] 

Expand ConversationMessage definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Message unique identifier

message

object 

Message content

type

string 

Message type

order

_lock_

integer 

Message order

conversation_agent

_lock_

[Agent](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Agent)

Agent for this conversation

Expand Agent definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Agent unique identifier

created_by_user_id

string 

User that created the Agent

created_by_name

_lock_

string 

Name of user that created the Agent

created_by_first_name

_lock_

string 

Name of user that created the Agent

created_by_last_name

_lock_

string 

Name of user that created the Agent

created_by_avatar_url

_lock_

string 

Avatar URL of user that created the Agent

name

string 

Agent name

description

string 

Agent description

category

string 

The category of the agent (e.g., dashboard, conversation)

sources

[Source](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Source)[] 

Expand Source definition... 

model

string 

Source model

explore

string 

Source explore

has_inaccessible_source

_lock_

boolean 

Has inaccessible source

golden_queries

[GoldenQuery](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/GoldenQuery)[] 

Expand GoldenQuery definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

integer 

Unique identifier for the golden question

query_id

_lock_

integer 

ID of the associated Looker Query resolved from the answer

questions

string[] 

answer

string 

The Explore URL representing the answer to the question

is_active

_lock_

boolean 

Whether this golden question should be utilized by the agent

created_by_user_id

_lock_

integer 

ID of the user who created the question

last_updated_by_user_id

_lock_

integer 

ID of the user who last updated the question

created_at

_lock_

string 

Time when the question was created

last_updated_at

_lock_

string 

Time when the question was last updated

explore

_lock_

string 

The explore name of the golden query

model

_lock_

string 

The LookML model name of the golden query

fields

string[] 

filters

_lock_

object 

Filters of the associated Looker Query

sorts

string[] 

limit

_lock_

string 

Limit of the associated Looker Query

client_id

_lock_

string 

Client ID of the associated Looker Query

pivots

string[] 

dynamic_fields

_lock_

string 

Dynamic fields of the associated Looker Query

golden_query_ids

integer[] 

context

[Context](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Context)

Agent context

Expand Context definition... 

instructions

string 

Agent instructions

show_analytical_details

boolean 

Show analytical details in preview

show_debug

boolean 

Show debug info in preview

deleted

boolean 

Is Agent soft deleted

created_at

_lock_

string 

Agent created_at

updated_at

_lock_

string 

Agent updated_at

content_metadata_id

_lock_

string 

Content metadata ID for this Agent

code_interpreter

boolean 

Enables Code Interpreter for this Agent

studio_agent_id

_lock_

string 

Studio Agent ID (if this agent was migrated)

workflow_params

[WorkflowParams](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/WorkflowParams)

Workflow parameters

Expand WorkflowParams definition... 

primary_agent

string 

The ID of the primary parent agent

polling_frequency_cron

string 

Crontab specifying the execution frequency

destination

[WorkflowDestination](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/WorkflowDestination)

Workflow delivery destination

is_lookml

_lock_

boolean 

Whether the agent is defined in LookML

lookml_agent_id

_lock_

string 

LookML Agent ID

lookml_edit_uri

_lock_

string 

URI to edit the LookML definition of this agent

missing_agent

_lock_

boolean 

Agent associated with this conversation was deleted

studio_conversation_id

_lock_

string 

Studio Conversation ID (if this conversation was migrated)

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 404: Not Found

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 429: Too Many Requests

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
