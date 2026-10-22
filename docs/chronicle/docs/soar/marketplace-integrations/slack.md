---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/slack/
title: Slack \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:32.315644+00:00
---

# Slack  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/slack/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Slack

This document provides guidance on how to integrate Slack with Google SecOps.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/Slack.zip).

## Configure Slack to work with Google Security Operations

To configure Slack to work with Google SecOps, firstly you need to create a New App:

  1. Go to <https://api.slack.com/> and click **Start Building**.

  2. Enter the **App Name** and **Development Slack Workspace** parameters. Click **Create App**.

![Create a Slack App
dialog](https://docs.cloud.google.com/static/chronicle/images/integrations/slack-create-slack-app.png)

  3. Go to the **OAuth & Permissions** tab and scroll down to the **Scopes** sections.

![OAuth & Permissions
tab](https://docs.cloud.google.com/static/chronicle/images/integrations/slack-oauth-and-permissions.png)

  4. Add the following Scopes/Permissions. It is recommended by Slack to add OAuth Token scopes for a bot, not user permissions:

     * channels:history
     * channels:manage
     * channels:read
     * chat:write
     * files:write
     * groups:history
     * groups:write
     * groups:read
     * im:read
     * im:write
     * im:history
     * mpim:read
     * mpim:history
     * mpim:write
     * users:read
     * users:read.email
**Note:** Any time you add/remove scopes, OAuth tokens need to be regenerated.

![Permission Scopes dialog](https://docs.cloud.google.com/static/chronicle/images/integrations/slack-scopes.png)

  5. To allow app interactivity for actions like "Send Interactive Message" and "Wait for Reply with Webhook", add a request URL for your app. For more information, see the [Handling user interaction in your Slack apps](https://api.slack.com/interactivity/handling) document available within the Slack documentation.

  6. Scroll up and click **Install App to Workspace**.

![Install App to Workspace button
location](https://docs.cloud.google.com/static/chronicle/images/integrations/slack-install-app-to-workplace.png)

  7. Click **Allow**.

![LabBot permission access
settings](https://docs.cloud.google.com/static/chronicle/images/integrations/slack-labbot-permissions.png)

  8. Copy one of the tokens that were created, depending on whether you want to use a bot or user.

  9. Configure integration with one of those tokens.


**Note:** For detailed information, see [Slack API Page](https://api.slack.com/start).

### Network

Function | Default Port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apitoken  
  
## Configure Slack integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Api Token | String | N/A | Yes | API Token generated in Slack console.  
Verify SSL | Checkbox | Unchecked | No | Use this checkbox, if your Slack connection requires an SSL verification (unchecked by default).  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ask Question

#### Description

Ask question in Slack.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Channel | String | N/A | Yes | Target Channel.  
Question | String | N/A | Yes | Question content.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    N/A
    

### Build Block

#### Description

Build a slack message block based on provided input criteria. This action creates a block with a webhook that can be later passed to the "Send Interactive Message" action to send a message with.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Question | String | N/A | Yes | Specify the question text to add to the block.  
Answers Buttons | String | N/A | Yes | Specify the answer buttons to add to the block.  
Siemplify Base URL | String | N/A | Yes | Specify the Google SecOps server base URL to add to the block.  
Case ID | String | N/A | Yes | Specify the Google SecOps case ID to add to the block.  
Webhook Token UUID | String | N/A | Yes | Specify the Webhook token UUID to monitor for the user's response.  
  
#### Playbook Use Cases Examples

Build a block that can be later passed to the "Send Advanced Message" action to send a message with a block.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    {
      "result": "[{\"type\": \"section\", \"block_id\": \"f99958f1-c1f1-4fdb-bb8b-a382d952d5bd\", \"text\": {\"type\": \"mrkdwn\", \"text\": \"yes?\", \"verbatim\": false}},{\"type\": \"actions\", \"block_id\": \"2850e684-472a-472f-9a32-96294cbe9046\", \"elements\": [{\"type\": \"button\", \"text\": {\"type\": \"plain_text\", \"text\": \"y\"}, \"action_id\": \"y\", \"url\": \"...\"}, {\"type\": \"button\", \"text\": {\"type\": \"plain_text\", \"text\": \"n\"}, \"action_id\": \"n\", \"url\": \"...\"}, {\"type\": \"button\", \"text\": {\"type\": \"plain_text\", \"text\": \"View Case in Siemplify\"}, \"action_id\": \"View Case in Siemplify\", \"url\": \"...\"}]}]"
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** ___If a build block is created successfully (is_succeed=True):_ "Slack block was created successfully."_If failed to create a slack block because of some general error (is_succeed=False):_ "Failed to create a block because of the occurred error: {0}".format(error text)**The action should fail and stop a playbook execution:******_If a webhook based URL is not specified in the integration configuration:_ "Failed to execute action, please specify the "Webhook Base URL" integration parameter."If a fatal error, like wrong credentials, no connection to the server, or other is reported: "Failed to execute "Send Advanced Message" action! Error is {0}".format(exception.stacktrace) | General  
  
### Create Channel

#### Description

Create Slack channel.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Channel Name | String | N/A | Yes | Specify the name of the channel.**Note:** Channel names may only contain lowercase letters, numbers, hyphens, and underscores, and must be 80 characters or less.  
User IDs | String | N/A | Yes | Specify the IDs of the users that should be invited to the newly created channel.Example: U014JDHLW87, U08544ABC85.  
Is Private | Checkbox | Unchecked | No | If enabled, the action creates a private channel.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "is_general": "False",
        "name_normalized": "12asd1237712318",
        "is_channel": "True",
        "creator": "U014J4NFQQG",
        "is_member": "True",
        "is_archived": "False",
        "topic": {
            "last_set": "0",
            "value": " ",
            "creator": " "
        },
        "parent_conversation": "None",
        "is_im": "False",
        "is_ext_shared": "False",
        "previous_names": [],
        "last_read": "0000000000.000000",
        "id": "C014S1G6DB4",
        "is_org_shared": "False",
        "pending_connected_team_ids": [],
        "is_pending_ext_shared": "False",
        "is_mpim": "False",
        "is_group": "False",
        "shared_team_ids": ["T013MJHSNCT"],
        "purpose": {
            "last_set": 0,
            "value": " ",
            "creator": " "
        },
        "is_private": "False",
        "is_shared": "False",
        "name": "12asd1237712318",
        "created": "1591194197",
        "pending_shared": [],
        "unlinked": 0,
        "priority": 0
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If "ok"== true and "Private" action parameter is false and User IDs parameter is empty (is_success=true):_ "Successfully created channel {0}".format(name)  
_If "ok"== true and "Private" action parameter is true and User IDs parameter is empty (is_success=true):_ "Successfully created private channel {0}".format(name)_If "ok"== true and "Private" action parameter is false and User IDs are available (is_success=true):_ "Successfully created channel {0} and added {1} users".format(name, user_ids)_If "ok"== true and "Private" action parameter is true and User IDs are available (is_success=true):_ "Successfully created private channel {0} and added {1} users".format(name, user_ids)_If "ok" == false. In the first request (is_success=false):_ "Failed to create channel {0}. Reason: {1}".format(name, value of error parameter from response)_If "ok" == false in the second request (is_success=false):_ "Channel {0} was created, but users were not invited. Reason:".format(name, value of error parameter from response)_If "ok" == false and error == "user_not_found" (is_success=false):_ "Failed to add users to channel {0}. Reason: {1} of the specified User IDs does not exist in Slack".format(name, len(errors) from the response)  
**The action should fail and stop a playbook execution:******_If_ ****a _fatal error (wrong credentials, connection error, action crashes) is reported:_ "Error executing action "Create Channel". Reason: {0}''.format(error.Stacktrace) | General  
  
### Get Channel Or User Conversation History

#### Description

Get conversation history for a user or a channel based on provided input criteria. This action works with either channel or user ID, which could be searched with either the "List Channels" or "List User" actions.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Channel or User ID | String | N/A | Yes | Specify the channel or user ID to fetch the conversation history for.  
Time Frame | DDL | Last HourPossible Values:

  * Last Hour
  * Last 6 Hours
  * Last 24 Hours
  * Last Week
  * Last Month
  * Custom

| No | Specify a time frame for the results.If "Custom" is selected, you also need to provide the "Start Time" parameter.  
Start Time | String | N/A | No | Specify the start time for the results.This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter.Format: ISO 8601.Example: 2021-08-05T05:18:42Z  
End Time | String | N/A | No | Specify the end time for the results.If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter uses current time.Format: ISO 8601. Example: 2021-08-05T05:18:42Z.  
Max Records To Return | Integer | 20 | No | Specify the number of records to return.If nothing is provided, the action returns 20 records.  
  
#### Playbook Use Cases Examples

Fetch conversation history to investigate alerts.

#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
      {
        "bot_id": "B02D9QYM7P0",
        "type": "message",
        "text": "test",
        "user": "U02D1RPLVST",
        "ts": "1665988448.627219",
        "app_id": "A02DDGD942Z",
        "team": "T02CX3N6B0B",
        "bot_profile": {
          "id": "B02D9QYM7P0",
          "deleted": false,
          "name": "Siemplify-test",
          "updated": 1630908872,
          "app_id": "A02DDGD942Z",
          "icons": {
            "image_36": "https://a.slack-edge.com/80588/img/plugins/app/bot_36.png",
            "image_48": "https://a.slack-edge.com/80588/img/plugins/app/bot_48.png",
            "image_72": "https://a.slack-edge.com/80588/img/plugins/app/service_72.png"
          },
          "team_id": "T02CX3N6B0B"
        },
        "blocks": [
          {
            "type": "rich_text",
            "block_id": "JbVUf",
            "elements": [
              {
                "type": "rich_text_section",
                "elements": [
                  {
                    "type": "text",
                    "text": "test"
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** ___If the conversation history is found successfully (is_succeed=True):_ "Conversation history was fetched successfully."_If the conversation with provided ID is not found (is_succeed=False):_ "Failed to find conversation for provided id {0}".format(channel_or_user_id)_If the conversation with provided ID is found and no messages are found for the provided time frame (is_succeed=False):_ "Conversation with id {0} was found, but no messages were found for the provided time frame.".format(channel_or_user_id)**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Failed to execute "Send Advanced Message" action! Error is {0}".format(exception.stacktrace)_If an invalid value is provided for the "Max Records to Return" parameter:_ "Error executing action "{action name}". Reason: "Invalid value was provided for "Max Records to Return": . Positive number should be provided"."_If "Custom" is selected for the "Time Frame" parameter and the "Start Time" parameter is not specified:_ "Error executing action "{action name}". Reason: "Start time was not provided for the custom Time Frame."" | General  
  
### Get User Details

#### Description

Get Slack user details based on provided input criteria.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Search By | DDL | EmailPossible Values:

  * Email
  * Name
  * ID

| Yes | Specify the parameter to search user details by.  
User Value | String | N/A | Yes | Specify the user value to search by.  
  
#### Playbook Use Cases Examples

Get user details to enrich alert processing in Google SecOps.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
      "id": "U043FPEMATG",
      "team_id": "T02CX3N6B0B",
      "name": "example.user",
      "deleted": false,
      "color": "3c989f",
      "real_name": "Example User",
      "tz": "Europe/Europe",
      "tz_label": "Central European Summer Time",
      "tz_offset": 7200,
      "profile": {
        "title": "",
        "phone": "",
        "skype": "",
        "real_name": "Example User",
        "real_name_normalized": "Example User",
        "display_name": "Example User",
        "display_name_normalized": "Example User",
        "fields": null,
        "status_text": "",
        "status_emoji": "",
        "status_emoji_display_info": [],
        "status_expiration": 0,
        "avatar_hash": "gc297456197c",
        "email": "example.user@example.com",
        "first_name": "Example",
        "last_name": "User",
        "image_24": "https://secure.gravatar.com/avatar/c297456197c0de7baa8c4b9a2398ecd1.jpg?s=24&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0011-24.png",
        "image_32": "https://secure.gravatar.com/avatar/c297456197c0de7baa8c4b9a2398ecd1.jpg?s=32&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0011-32.png",
        "image_48": "https://secure.gravatar.com/avatar/c297456197c0de7baa8c4b9a2398ecd1.jpg?s=48&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0011-48.png",
        "image_72": "https://secure.gravatar.com/avatar/c297456197c0de7baa8c4b9a2398ecd1.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0011-72.png",
        "image_192": "https://secure.gravatar.com/avatar/c297456197c0de7baa8c4b9a2398ecd1.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0011-192.png",
        "image_512": "https://secure.gravatar.com/avatar/c297456197c0de7baa8c4b9a2398ecd1.jpg?s=512&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0011-512.png",
        "status_text_canonical": "",
        "team": "T02CX3N6B0B"
      },
      "is_admin": false,
      "is_owner": false,
      "is_primary_owner": false,
      "is_restricted": false,
      "is_ultra_restricted": false,
      "is_bot": false,
      "is_app_user": false,
      "updated": 1663939355,
      "is_email_confirmed": true,
      "who_can_share_contact_card": "EVERYONE"
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message\\* | **The action should not fail nor stop a playbook execution:** ___If user details are found successfully (is_succeed=True):_ "User details were fetched successfully."_If user details are not found based on provided criteria (is_succeed=False):_ "Failed to find user details based on the provided criteria: Search by: <0> User value: <1>".format(search_by, user_value)_If user details are found by name, and more than one match is found (is_succeed=True):_ "For the provided search criteria multiple matches were found: Search by: <0> User value: <1>".format(search_by, user_value)_If the user is not found (is_succeed=False) because of some general error:_ "Failed to fetch user details because of occurred error: (0}" (error text)**The action should fail and stop a playbook execution:******If a fatal error, like wrong credentials, no connection to the server, or other is reported: "Failed to execute "Send Advanced Message" action! Error is {0}".format(exception.stacktrace) | General  
Case Wall Table | **Table Name:** Slack User Details**Table Columns:**

  * ID
  * Team ID
  * Name
  * Real Name
  * Display Name
  * First Name
  * Last Name
  * Updated Time
  * Timezone
  * Title
  * Phone
  * Is Admin
  * Is Owner
  * Is Primary Owner
  * Is Restricted
  * Is Ultra Restricted
  * Is Bot
  * Is App User
  * Is Email Confirmed

| General  
  
### Get User Details by ID

#### Description

Get user details by their ID.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
User ID | String | N/A | Yes | User's ID.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    N/A
    

### List Channels

#### Description

Get a list of Slack channels.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    [
        {
            "is_org_shared": false,
            "is_general": true,
            "name_normalized": "general",
            "name": "general",
            "is_channel": true,
            "created": 1575550599,
            "is_member": true,
            "is_mpim": false,
            "is_archived": false,
            "creator": "URALP6WRJ",
            "topic": {
                "last_set": 1575550599,
                "value": "Company-wide announcements and work-based matters",
                "creator": "URALP6WRJ"
            },
            "num_members": 1,
            "purpose": {
                "last_set": 1575550599,
                "value": "This channel is for workspace-wide communication and announcements. All members are in this channel.",
                "creator": "URALP6WRJ"
            },
            "members": ["URALP6WRJ"],
            "unlinked": 0,
            "is_shared": false,
            "id": "CRB4ZHGNR",
            "is_private": false,
            "previous_names": []
        }, {
            "is_org_shared": false,
            "is_general": false,
            "name_normalized": "random",
            "name": "random",
            "is_channel": true,
            "created": 1575550599,
            "is_member": true,
            "is_mpim": false,
            "is_archived": false,
            "creator": "URALP6WRJ",
            "topic": {
                "last_set": 1575550599,
                "value": "Non-work banter and water cooler conversation",
                "creator": "URALP6WRJ"
            },
            "num_members": 1,
            "purpose": {
                "last_set": 1575550599,
                "value": "A place for non-work-related flimflam, faffing, hodge-podge or jibber-jabber you'd prefer to keep out of more focused work-related channels.",
                "creator": "URALP6WRJ"
            },
            "members": ["URALP6WRJ"],
            "unlinked": 0,
            "is_shared": false,
            "id": "CRD0KF9T9",
            "is_private": false,
            "previous_names": []
        }, {
            "is_org_shared": false,
            "is_general": false,
            "name_normalized": "website",
            "name": "website",
            "is_channel": true,
            "created": 1575550600,
            "is_member": true,
            "is_mpim": false,
            "is_archived": false,
            "creator": "URALP6WRJ",
            "topic": {
                "last_set": 0,
                "value": " ",
                "creator": " "
            },
            "num_members": 1,
            "purpose": {
                "last_set": 0,
                "value": " ",
                "creator": " "
            },
            "members": ["URALP6WRJ"],
            "unlinked": 0,
            "is_shared": false,
            "id": "CRDAUBZP0",
            "is_private": false,
            "previous_names": []
        }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If "ok" == false (is_success=false)_ : ****"Failed to list channels. Reason: {0}".format(value of error parameter from response) | General  
  
### List User

#### Description

This action has the role of getting a list of Slack users.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    [
        {
            "profile": {
                "status_text": " ",
                "display_name": " ",
                "status_emoji": " ",
                "title": " ",
                "status_text_canonical": " ",
                "team": "TRALP6VNY",
                "real_name": "somerealname",
                "image_24": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=24&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-24.png",
                "phone": " ",
                "real_name_normalized": "somerealnamen",
                "image_512": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=512&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-512.png",
                "image_72": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-72.png",
                "image_32": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=32&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-32.png",
                "image_48": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=48&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-48.png",
                "skype": " ",
                "avatar_hash": "g2d62053d7f7",
                "display_name_normalized": " ",
                "status_expiration": 0,
                "email": "mail@seimplify.co",
                "image_192": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-192.png"
            },
            "updated": 1575550598,
            "tz": "Europe/Moscow",
            "name": "name",
            "deleted": false,
            "is_app_user": false,
            "is_bot": false,
            "tz_label": "Moscow Time",
            "real_name": "realname",
            "color": "9f69e7",
            "team_id": "TRALP6VNY",
            "is_admin": true,
            "is_ultra_restricted": false,
            "is_restricted": false,
            "is_owner": true,
            "tz_offset": 14400,
            "has_2fa": false,
            "id": "URALP6WRJ",
            "is_primary_owner": true
        }, {
            "profile": {
                "last_name": " ",
                "status_emoji": " ",
                "display_name_normalized": "Slackbot",
                "image_32": "https://a.slack-edge.com/80588/img/slackbot_32.png",
                "skype": " ",
                "image_72": "https://a.slack-edge.com/80588/img/slackbot_72.png",
                "status_expiration": 0,
                "image_192": "https://a.slack-edge.com/80588/marketing/img/avatars/slackbot/avatar-slackbot.png",
                "first_name": "slackbot",
                "display_name": "Slackbot",
                "title": " ",
                "real_name_normalized": "Slackbot",
                "always_active": true,
                "status_text_canonical": " ",
                "image_24": "https://a.slack-edge.com/80588/img/slackbot_24.png",
                "phone": " ",
                "image_48": "https://a.slack-edge.com/80588/img/slackbot_48.png",
                "fields": null,
                "real_name": "Slackbot",
                "image_512": "https://a.slack-edge.com/80588/img/slackbot_512.png",
                "team": "TRALP6VNY",
                "avatar_hash": "sv41d8cd98f0",
                "status_text": " "
            },
            "updated": 0,
            "tz": null,
            "name": "slackbot",
            "deleted": false,
            "is_app_user": false,
            "is_bot": false,
            "tz_label": "Pacific Standard Time",
            "real_name": "Slackbot",
            "color": "757575",
            "team_id": "TRALP6VNY",
            "is_admin": false,
            "is_ultra_restricted": false,
            "is_restricted": false,
            "is_owner": false,
            "tz_offset": -28800,
            "id": "USLACKBOT",
            "is_primary_owner": false
        }
    ]
    

### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    N/A
    

### Rename Channel

#### Description

Rename Slack channel.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Channel Name | String | N/A | No | Specify the name of the channel, which you want to rename. **Note:** If both the "Channel Name" and "Channel ID" parameters are specified, the action only works with ID.   
Channel ID | String | N/A | No | Specify the ID of the channel, which you want to rename.**Note:** If both the "Channel Name" and "Channel ID" parameters are specified, the action only works with ID.  
New Name | String | N/A | Yes | Specify a new name for the channel.**Note:** Channel names may only contain lowercase letters, numbers, hyphens, and underscores, and must be 80 characters or less.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result

When "ok" == true:
    
    
    {
        "channel": {
            "id": "C013ELA1YVC",
            "name": "project_old",
            "is_channel": true,
            "is_group": false,
            "is_im": false,
            "created": 1589444943,
            "is_archived": false,
            "is_general": false,
            "unlinked": 0,
            "name_normalized": "project_old",
            "is_shared": false,
            "parent_conversation": null,
            "creator": "U0136KZ0P5M",
            "is_ext_shared": false,
            "is_org_shared": false,
            "shared_team_ids": [
                "T013MJHSNCT"
            ],
            "pending_shared": [],
            "pending_connected_team_ids": [],
            "is_pending_ext_shared": false,
            "is_member": true,
            "is_private": false,
            "is_mpim": false,
            "last_read": "1595242486.000300",
            "topic": {
                "value": "",
                "creator": "",
                "last_set": 0
            },
            "purpose": {
                "value": "This *channel* is for working on a project. Hold meetings, share docs, and make decisions together with your team.",
                "creator": "U0136KZ0P5M",
                "last_set": 1589444943
            },
            "previous_names": [
                "project_new",
                "project"
            ]
        },
        "ok": true,
        "warning": "missing_charset",
        "response_metadata": {
            "warnings": [
                "missing_charset"
            ]
        }
    }
    

When "ok" == false:
    
    
    {
        "ok": false,
        "error": "name_taken",
        "warning": "missing_charset",
        "response_metadata": {
            "warnings": [
                "missing_charset"
            ]
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If "ok"== true (is_success=true):_ "Successfully renamed channel {0} to {1} {0}".format(name/ID, new name)  
_If "ok"== false (is_success=false):_ "Action wasn't able to rename channel {0}. Reason: {1}".format(name,error from the response)_If channel wasn't found by channel name (is_success=false):_ "Action wasn't able to rename channel {0}. Reason: Channel was not found".format(name)  
**The action should fail and stop a playbook execution:**___If a fatal error (wrong credentials, connection error, action crashes) is reported:_ "Error executing action "Rename Channel". Reason: {0}''.format(error.Stacktrace)  
_If the "Channel Name" and "Channel ID" parameters are not specified:_ "Error executing action "Rename Channel". Reason: you need to specify 'Channel Name' or 'Channel ID'." | General  
  
### Send Advanced Message

#### Description

Send an advanced message to a Slack channel or user. This action provides an ability to send simple text messages and rich Slack block messages with buttons, advanced formatting, and more. For more information on block messages, see [Slack Block Kit ](https://api.slack.com/block-kit).

This action can be used together with the "Wait for Reply With Webhook" action to first send a block message with a webhook to a user, and later with the "Wait for Reply With Webhook" action check for the user's response.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Message Type | DDL | TextPossible Values:

  * Text
  * Block

| Yes | Specify the type of the message to send.  
Recipient Type | DDL | NamePossible Values:

  * Name
  * ID
  * Email

| Yes | Specify the channel or user name (full name) to send message to.Optionally specify channel or user ID, or email address of a user.  
Recipient | String | N/A | Yes | Specify the recipient to send a message to.  
Message | String | N/A | Yes | Specify the content of the message to send.  
  
#### Playbook Use Cases Examples

Send a message with rich content such as buttons, links, or pictures.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    [
      {
        "Entity": "U043FPEMATG",
        "EntityResult": {
          "channel": "D044C3DUMB2",
          "message": {
            "bot_id": "B02D9QYM7P0",
            "type": "message",
            "text": "test msg",
            "user": "U02D1RPLVST",
            "ts": "1666008612.116169",
            "app_id": "A02DDGD942Z",
            "team": "T02CX3N6B0B",
            "bot_profile": {
              "id": "B02D9QYM7P0",
              "app_id": "A02DDGD942Z",
              "name": "test",
              "icons": {
                "image_36": "https://a.slack-edge.com/80588/img/plugins/app/bot_36.png",
                "image_48": "https://a.slack-edge.com/80588/img/plugins/app/bot_48.png",
                "image_72": "https://a.slack-edge.com/80588/img/plugins/app/service_72.png"
              },
              "deleted": false,
              "updated": 1630908872,
              "team_id": "T02CX3N6B0B"
            },
            "blocks": [
              {
                "type": "rich_text",
                "block_id": "RJvg",
                "elements": [
                  {
                    "type": "rich_text_section",
                    "elements": [
                      {
                        "type": "text",
                        "text": "test msg"
                      }
                    ]
                  }
                ]
              }
            ]
          },
          "ts": "1666008612.116169",
          "ok": true
        }
      }
    ]
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** ___If the message is sent successfully (is_succeed=True):_ "Message was sent successfully"_If the message is not sent successfully (is_succeed=False) because the specified recipient is not found:_ "Message was not sent as the specified recipient {0} with type {1} was not found." (recipient, recipient type)_If the message is not sent successfully (is_succeed=False) because of some general error:_ "Message was not sent because of occurred error: (0}" (error text)**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Failed to execute "Send Advanced Message" action! Error is {0}".format(exception.stacktrace) | General  
  
### Send Interactive Message

#### Description

Send an interactive message to a channel or a user and when based on the provided Webhook UUID check the user's response. This action is similar to the "Send Advanced Message" action, but it allows to send only block content (not plain text messages) and also requires a webhook UUID to check the user's response to a webhook.

The action is asynchronous, adjust the action timeout in IDE accordingly.

Configure the Slack app used in the integration to allow interactive messages. For more information on the Slack app configuration, see [Readying your application for interactive messages](https://api.slack.com/legacy/interactive-messages#readying_app).

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Recipient Type | DDL | Name Possible Values:

  * Name
  * ID
Email | Yes | Specify the channel or user name (full name) to send message to. Optionally specify channel or user ID, or email address of a user. 
  
Recipient | String | N/A | Yes | Specify the recipient to send a message to.  
Message | String | N/A | Yes | Specify the content of the message to send.  
Webhook Token UUID | String | N/A | Yes | Specify the webhook token UUID to monitor for the user's response.  
  
#### Playbook Use Cases Examples

Send a message with rich content such as buttons, links, or pictures.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    [
      {
        "uuid": "10953f8e-7ef8-4bde-9e9b-212005e0e737",
        "type": "web",
        "token_id": "47289ba5-277e-4ab9-9238-eb31080530ca",
        "ip": "0000:a000000:ad80:000:20ea:653:fb97",
        "hostname": "webhook.site",
        "method": "GET",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
        "content": "",
        "query": {
          "Answer": "yes"
        },
        "headers": {
          "connection": [
            "close"
          ],
          "accept-encoding": [
            "gzip, deflate, br"
          ],
          "accept-language": [
            "en-US,en;q=0.9"
          ],
          "user-agent": [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
          ],
          "cookie": [
            "_ga=GA"
          ],
          "accept": [
            "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
          ],
          "host": [
            "webhook.site"
          ],
          "content-length": [
            ""
          ],
          "content-type": [
            ""
          ]
        },
        "url": "https://webhook.site/47289ba5-277e-4ab9-9238-xx0000000xx?Answer=yes",
        "size": 0,
        "files": [],
        "created_at": "2022-10-14 19:45:40",
        "updated_at": "2022-10-14 19:45:40",
        "sorting": 1665776740032262,
        "custom_action_output": []
      }
    ]
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** ___If the message is sent successfully (is_succeed=True):_ "Message was sent successfully"_If the message is not sent successfully (is_succeed=False) because the specified recipient is not found:_ "Message was not sent as the specified recipient {0} with type {1} was not found." (recipient, recipient type)_If the message is not sent successfully (is_succeed=False) because of some general error:_ "Message was not sent because of occurred error: (0}" (error text)**Case Wall messages for the asynchronous functionality:** _A case wall message for the iterations while waiting for the reply:_ "Waiting for the response to the sent message with a webhook. Webhook url with uuid: {0}".format(webhook url from integration configuration + web token uuid)_If the response is fetched successfully (is_succeed=True):_ "Successfully fetched the user's response to a webhook! Response content: {0}".format(payload that was sent from user to a webhook)_If failed to fetch the response until timeout:_ "A user response to a webhook was not found and the action stopped due to the timeout."**The action should fail and stop a playbook execution:******_If a webhook based URL is not specified in the integration configuration and a webhook UUID token is specified:_ "Failed to execute action, please specify the "Webhook Base URL" integration parameter. "_If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Failed to execute "Send Interactive Message" action! Error is {0}".format(exception.stacktrace) | General  
  
### Send Message

#### Description

Send a message to a user or multiple users/channels.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Channel | String | N/A | Yes | The name of the Slack channel or the email address of the user to whom to send the message.Entered values need to be comma-separated.  
Message | String | N/A | Yes | Message content.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    N/A
    

### Upload File

#### Description

Add files to Slack and share them with your teammates to help you collaborate. You can choose and upload files to Slack from your device or your preferred file management app. Uploaded files are stored, searchable, and shareable across your workspace.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
File Name | String | N/A | Yes | Target File Name.  
File Path | String | N/A | Yes | Target File Path.  
Channel | String | N/A | Yes | Target Channel.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    N/A
    

### Wait For Reply

#### Description

Wait for a thread reply to a message in a channel.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Channel | String | N/A | Yes | Target Channel.  
Message Timestamp | String | N/A | Yes | The timestamp of the message to get the replies from (in milliseconds).  
Channel ID | String | N/A | No | The ID of the target Slack channel.  
**Note:** In case both the "Channel" and "Channel ID" parameters are provided, the action takes into account only the ID.

#### Playbook use cases

Playbook with send message action and after wait for a reply (with the channel as placeholder from previous action - Channel ID)

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    N/A
    

### Wait For Reply With Webhook

#### Description

Wait for a user to reply to a message sent with a webhook. This action periodically checks the provided webhook to see if the user had provided any reply to it. Action can be used with the "Send Advanced Message" action, if the block message with webhook was sent, to check if the user's response was provided to the webhook.

This action is asynchronous, adjust the script timeout value in IDE accordingly.

**Note:** To configure Slack for the interactivity handling and clarify what webhook UUID you work with, see [Send Interactive Message](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/slack#send-interactive-message).

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Webhook Token UUID | String | N/A | Yes | Specify the webhook token UUID to monitor for the user's response.  
  
#### Playbook Use Cases Examples

Wait for a reply to a message with a webhook.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    {
      "client_msg_id": "00000000-0000-0000-0000-000000000000",
      "type": "message",
      "text": "Yes",
      "user": "U0000000",
      "ts": "1578390603.001200",
      "team": "T0000000",
      "blocks": [
        {
          "type": "rich_text",
          "block_id": "2Bb=",
          "elements": [
            {
              "type": "rich_text_section",
              "elements": [
                {
                  "type": "text",
                  "text": "Example"
                }
              ]
            }
          ]
        }
      ],
      "thread_ts": "1578390492.001100",
      "parent_user_id": "U0000000"
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** ___A case wall message for the iterations while waiting for the reply:_ "Waiting for the response to the sent message with a webhook. Webhook url with uuid: {0}".format(webhook url from integration configuration + web token uuid)_If response is fetched successfully (is_succeed=True):_ "Successfully fetched the user's response to a webhook! Response content: {0}".format(payload that was sent from user to a webhook)_If failed to fetch the response until timeout:_ "A user response to a webhook was not found and the action stopped due to the timeout."**The action should fail and stop a playbook execution:******_If the webhook based URL is not specified in the integration configuration and the webhook UUID token is specified:_ "Failed to execute action, please specify the "Webhook Base URL" integration parameter. "_If a fatal error, like wrong credentials, no connection to the server, or other is reported:_ "Failed to execute "Send Advanced Message" action! Error is {0}".format(exception.stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
