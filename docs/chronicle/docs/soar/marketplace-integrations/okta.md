---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/okta/
title: Integrate Okta with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:06.453020+00:00
---

# Integrate Okta with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/okta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Okta with Google SecOps

This document provides guidance on how to integrate Okta with Google Security Operations.

## Use cases

The **Okta** integration uses Google SecOps capabilities to support the following use cases:

  * **Manage user lifecycles** : Automatically enable, disable, or reset passwords for users based on security alerts to mitigate risk.

  * **Terminate active sessions** : Instantly clear all active Okta sessions for compromised accounts to prevent unauthorized access across integrated applications.

  * **Automate role assignments** : Dynamically assign or unassign administrative roles to users to maintain the principle of least privilege during investigations.

  * **Synchronize threat signals** : Send Identity Threat Protection (ITP) signals to Okta to share risk context and trigger automated security responses.

  * **Enrich identity context** : Retrieve detailed user profiles and group memberships to provide analysts with deep visibility into account activity.




## Before you begin

Before you configure the integration in Google SecOps, verify that you have the following requirements met in your Okta environment:

  * **Authentication method** : Determine whether your organization uses an API Token (SSWS) or OAuth 2.0 for authentication.

    * **API token** : Generate an SSWS token. For details, see the [Okta API token documentation](https://developer.okta.com/docs/guides/create-an-api-token/).
    * **OAuth 2.0** : Register a service app to obtain a `Client ID`, `Key ID`, and `Private Key`. For details, see the [Okta OAuth documentation](https://developer.okta.com/docs/guides/implement-oauth-for-okta-service-apps/).
  * **Account permissions** : Verify the account has sufficient permissions to perform user management and session termination actions.




## Integration parameters

The **Okta** integration requires the following parameters:

Parameter | Description  
---|---  
`Api Root` | Required. The base URL of your Okta instance, used to access the API. The default value is `https://{okta_domain}.com/`.  
`Api Token` | Optional. The API token (SSWS) used for authentication with the Okta instance. If `Use Oauth Authentication` is disabled, this parameter is mandatory.  
`Use Oauth Authentication` | Required. If enabled, the integration uses OAuth 2.0 for authentication instead of an API token. When using OAuth, `Client ID`, `Key ID`, and `Private Key` are mandatory, and `Api Token` should be left blank. If disabled, `Api Token` is mandatory.  
`Client ID` | Optional. The unique identifier for the Okta OAuth application. If `Use Oauth Authentication` is enabled, this parameter is mandatory. If authenticating using an API token, leave this field blank.  
`Key ID` | Optional. The ID of the public key associated with the private key used for OAuth authentication. If `Use Oauth Authentication` is enabled, this parameter is mandatory. If authenticating using an API token, leave this field blank.  
`Private Key` | Optional. The private key in PEM format used for OAuth authentication. If `Use Oauth Authentication` is enabled, this parameter is mandatory. If authenticating using an API token, leave this field blank.  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to the Okta server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Group

Add a group.

#### Parameters

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Assign Role

Assign a role to a user.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
User IDs | String | N/A | IDs of users in Okta.  
Role Types | String | N/A | The type of role to assign to the users.  
Also Run On Scope | Checkbox | Checked | Whether to run on entities as well as the input.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * User
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
Roles | Returns if it exists in JSON result  
  
##### Insights

N/A

### Clear Okta User Session

Use the **Clear Okta User Session** action to terminate all active Okta sessions for specific users across all devices and integrated applications.

This action runs on the Google SecOps `Username` entity.

#### Action inputs

The **Clear Okta User Session** action requires the following parameters:

Parameter | Description  
---|---  
`User IDs Or Logins` | Optional. A comma-separated list of Okta user IDs or login identifiers.  
`Also Run On Scope` | Optional. If selected, the action revokes active Identity Provider (IdP) sessions for all users identified in the entity scope, in addition to those explicitly listed in `User IDs Or Logins`.  
  
#### Action outputs

The **Clear Okta User Session** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Clear Okta User Session** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully cleared sessions for the following users: ENTITY_IDS.` `The sessions failed to clear for the following user in Okta: ENTITY_ID.` `No users were found to clear sessions.` | The action succeeded.  
`Error executing action "Clear Okta User Session". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Clear Okta User Session** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Disable User

Disables the specified user.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
User IDs Or Logins | String | N/A | IDs of users in Okta.  
Is Deactivate | Checkbox | Checked | Whether to deactivate or only suspend the user.  
Send Email If Deactivate | Checkbox | Checked | Whether to send an email after deactivating or not.  
Also Run On Scope | Checkbox | Checked | Whether to run on entities as well as the input.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * User
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
is_deactivate | If it's True, the user is disabled. Otherwise: False  
is_send_email_deactivate | If it's True, the user is disabled. Otherwise: False  
  
##### Insights

N/A

### Enable User

Enables the specified user.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
User IDs Or Logins | String | N/A | IDs or logins of users in Okta.  
Is Activate | Checkbox | Checked | Whether to activate the user or just unsuspend.  
Send Email If Activate | Checkbox | Checked | Whether to send an email after activating or not.  
Also Run On Scope | Checkbox | Checked | Whether to run on entities as well as the input.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * User
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
is_reactivate | If it's True, the user is enabled. Otherwise: False  
is_send_email_reactivate | If it's True, the user is disabled. Otherwise: False  
  
##### Insights

N/A

### Get Group

Get information about a group.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
Group IDs Or Names | String | N/A | IDs or names of groups in Okta.  
Is Id | Checkbox | Checked | Whether the value is an ID or a name.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Get user

Get information about a user

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
User IDs Or Logins | String | N/A | IDs or logins (email or short email name) of a user in Okta, for example: test@gmail.com or simply 'test'.  
Also Run On Scope | Checkbox | Checked | Whether to run on entities as well as the input.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * User
  * Hostname



#### Action Result

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    [
      {
        "status": "ACTIVE",
        "profile": {
          "mobilePhone": null,
          "firstName": "Test",
          "lastName": "User",
          "secondEmail": null,
          "login": "test.user@asd.com",
          "email": "test.user@asd.com"
        },
        "passwordChanged": "2022-07-11T06:11:25.000Z",
        "created": "2022-07-11T06:07:55.000Z",
        "activated": null,
        "lastUpdated": "2022-07-11T06:11:25.000Z",
        "_links": {
          "schema": {
            "href": "https://trial-0000.okta.com/api/v1/meta/schemas/user/osc1xxxxxxxx"
          },
          "suspend": {
            "href": "https://trial-0000.okta.com/api/v1/users/00u1xxxxxxxx/lifecycle/suspend",
            "method": "POST"
          },
          "forgotPassword": {
            "href": "https://trial-0000.okta.com/api/v1/users/00u1xxxxxxxx/credentials/forgot_password",
            "method": "POST"
          },
          "self": {
            "href": "https://trial-0000.okta.com/api/v1/users/00u1xxxxxxxx"
          },
          "expirePassword": {
            "href": "https://trial-0000.okta.com/api/v1/users/00u1xxxxxxxx/lifecycle/expire_password",
            "method": "POST"
          },
          "resetFactors": {
            "href": "https://trial-0000.okta.com/api/v1/users/00u1xxxxxxxx/lifecycle/reset_factors",
            "method": "POST"
          },
          "deactivate": {
            "href": "https://trial-0000.okta.com/api/v1/users/00u1xxxxxxxx/lifecycle/deactivate",
            "method": "POST"
          },
          "changePassword": {
            "href": "https://trial-0000.okta.com/api/v1/users/00u1xxxxxxxx/credentials/change_password",
            "method": "POST"
          },
          "changeRecoveryQuestion": {
            "href": "https://trial-0000.okta.com/api/v1/users/00u1xxxxxxxx/credentials/change_recovery_question",
            "method": "POST"
          },
          "type": {
            "href": "https://trial-0000.okta.com/api/v1/users/00u1xxxxxxxx"
          },
          "resetPassword": {
            "href": "https://trial-0000.okta.com/api/v1/users/00u1xxxxxxxx/lifecycle/reset_password",
            "method": "POST"
          }
        },
        "lastLogin": "2022-07-11T06:15:14.000Z",
        "credentials": {
          "password": {},
          "provider": {
            "type": "OKTA",
            "name": "OKTA"
          }
        },
        "type": {
          "id": "oty1xxxxxxxxxxxxx"
        },
        "id": "oty1xxxxxxxxxxxxx",
        "statusChanged": "2022-07-11T06:11:25.000Z"
      }
    ]
    

##### Entity Enrichment

N/A

##### Insights

N/A

### List Providers

List identity providers (IdPs) in your organization.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
Query | String | N/A | Search the name property for a match.  
Type | Checkbox | Checked | Filter by type.  
Limit | String | 20 | Max amount of results to return.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### List Roles

Lists all roles assigned to a user.

#### Parameters

User IDs | String | N/A | IDs of users in Okta.  
---|---|---|---  
Also Run On Scope | Checkbox | Checked | Whether to run on entities as well as the input.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * User
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### List User Groups

Get the groups that the user is a member of.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
User IDs Or Logins | String | N/A | IDs or logins of users in Okta.  
Also Run On Scope | Checkbox | Checked | Whether to run on entities as well as the input.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * User
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
profile | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
  
##### Insights

N/A

### List Users

Get the list of users.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
Query | String | N/A | Search for a match in the firstname, lastname or in the email.  
Filter | String | N/A | Custom search query for a subset of properties.  
Search | String | N/A | Custom search query for most properties.  
Limit | String | 200 | Max amount of results to return.  
  
#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
profile | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
  
##### Insights

N/A

### Ping

Test Connection with Okta.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Reset Password

Generate a one-time token that can be used to reset a user's password.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
User IDs Or Logins | String | N/A | IDs or logins of users in Okta.  
Send Email | Checkbox | Unchecked | Whether to send an email for the password reset or return the token for every user.  
Also Run On Scope | Checkbox | Unchecked | Whether to run on entities as well as the input.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * User
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
send_email | Returns if it exists in JSON result  
  
##### Insights

N/A

### Set Password

Set the password of a user without validating the existing credentials.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
User IDs Or Logins | String | N/A | IDs or logins of users in Okta.  
New Password | String | N/A | The new password.  
Add 10 Random Chars | Checkbox | Unchecked | Whether to add extra characters to every user password or not.  
Also Run On Scope | Checkbox | Unchecked | Whether to run on entities as well as the input.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * User
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
set_password | Returns if it exists in JSON result  
  
##### Insights

N/A

### Send ITP Signal

Distribute Identity Threat Protection (ITP) signals to relevant consumers using the Shared Signals Framework (SSF).

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
Key ID | String | N/A | The ID of the public key used to verify the private key's signature.  
Private Key String | Password | N/A | The private key used to sign the signal. The key is provided in a string format and includes the "BEGIN" and "END" statements.  
User Email | Mail Address | N/A | The email address of the affected user.  
Timestamp | timestamp | N/A | The timestamp of the signal occurrence. The timestamp format is ISO 8601.  
Reason | String | N/A | A brief description explaining why the signal was generated.  
Severity | String or DDL | N/A | The severity level of the signal.  
Issuer URL | URL | N/A | The source system that created the signal.  
  
#### Action Results

##### JSON Result
    
    
    {
       "status":200,
       "payload":{
          "iss":"https://www.google.com/",
          "jti":"3c5fbf0c-3977-11f0-a195-7e498c84a3dd",
          "iat":1748184472,
          "aud":"https://<your-okta-domain>.oktapreview.com",
          "events":{
             "https://schemas.okta.com/secevent/okta/event-type/user-risk-change":{
                "subject":{
                   "user":{
                      "format":"email",
                      "email":"user@domain.net"
                   }
                },
                "current_level":"medium",
                "previous_level":"low",
                "reason_admin":{
                   "en":"BadNavigationEvent"
                },
                "event_timestamp":1742199770057
             }
          }
       }
    }
    

##### Output messages

Output message | Message description  
---|---  
`Successfully sent the ITP signal to Okta. ` `Context value was not found for the provided context key CONTEXT_KEY and connector identifier CONNECTOR_IDENTIFIER.` `Action can't return the Case Wall table as the context values are too big.` | The action succeeded.  
`Failed to send the ITP signal to Okta. Error is {0}".format(exception.stacktrace)` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script Result

Script Result Name | Value Options  
---|---  
is_success | `True` or `False`  
  
### Unassign Role

Unassign a role from a user.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
User IDs | String | N/A | IDs of users in Okta.  
Role IDs Or Names | String | N/A | IDs or names of roles in Okta.  
Also Run On Scope | Checkbox | Unchecked | Whether to run on entities as well as the input.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * User
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
ScriptResult | N/A | N/A  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
unassign_role | Returns if it exists in JSON result  
  
##### Insights

N/A

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
