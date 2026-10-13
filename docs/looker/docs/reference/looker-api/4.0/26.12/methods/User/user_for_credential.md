---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user_for_credential/
title: Get User by Credential Id \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:07:20.242824+00:00
---

# Get User by Credential Id  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/User/user_for_credential/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Get User by Credential Id Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.12 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Get information about the user with a credential of given type with specific id.

This is used to do things like find users by their embed external_user_id. Or, find the user with a given api3 client_id, etc. The 'credential_type' matches the 'type' name of the various credential types. It must be one of the values listed in the table below. The 'credential_id' is your unique Id for the user and is specific to each type of credential.

An example using the Ruby sdk might look like:

`sdk.user_for_credential('embed', 'customer-4959425')`

This table shows the supported 'Credential Type' strings. The right column is for reference; it shows which field in the given credential type is actually searched when finding a user with the supplied 'credential_id'.

Credential Types | Id Field Matched  
---|---  
email | email  
google | google_user_id  
saml | saml_user_id  
oidc | oidc_user_id  
ldap | ldap_id  
api | token  
api3 | client_id  
embed | external_user_id  
looker_openid | email  
  
**NOTE** : The 'api' credential type was only used with the legacy Looker query API and is no longer supported. The credential type for API you are currently looking at is 'api3'.

Calls to this endpoint may be denied by [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/r/looker-core/overview).

## Request

GET /users/credential/{credential_type}/{credential_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

credential_type

string 

Type name of credential

credential_id

string 

Id of credential

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields.

## Response

### 200: Specified user.

Datatype

Description

(object)

[User](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/User)

can

_lock_

object 

Operations the current user is able to perform on this object

avatar_url

_lock_

string 

URL for the avatar image (may be generic)

avatar_url_without_sizing

_lock_

string 

URL for the avatar image (may be generic), does not specify size

credentials_api3

[CredentialsApi3](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CredentialsApi3)[] 

Expand CredentialsApi3 definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

client_id

_lock_

string 

API key client_id

created_at

_lock_

string 

Timestamp for the creation of this credential

is_disabled

_lock_

boolean 

Has this credential been disabled?

type

_lock_

string 

Short name for the type of this kind of credential

purpose

string 

User defined purpose for this credential.

url

_lock_

string 

Link to get this item

credentials_email

_lock_

[CredentialsEmail](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CredentialsEmail)

Email/Password login credentials

Expand CredentialsEmail definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

created_at

_lock_

string 

Timestamp for the creation of this credential

email

string 

EMail address used for user login

forced_password_reset_at_next_login

boolean 

Force the user to change their password upon their next login

user_id

_lock_

string 

Unique Id of the user

is_disabled

_lock_

boolean 

Has this credential been disabled?

logged_in_at

_lock_

string 

Timestamp for most recent login using credential

password_reset_url

_lock_

string 

Url with one-time use secret token that the user can use to reset password

account_setup_url

_lock_

string 

Url with one-time use secret token that the user can use to setup account

password_reset_url_expired

_lock_

boolean 

Is password_reset_url expired or not present?

account_setup_url_expired

_lock_

boolean 

Is account_setup_url expired or not present?

type

_lock_

string 

Short name for the type of this kind of credential

url

_lock_

string 

Link to get this item

user_url

_lock_

string 

Link to get this user

credentials_embed

[CredentialsEmbed](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CredentialsEmbed)[] 

Expand CredentialsEmbed definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

created_at

_lock_

string 

Timestamp for the creation of this credential

external_group_id

_lock_

string 

Embedder's id for a group to which this user was added during the most recent login

external_user_id

_lock_

string 

Embedder's unique id for the user

id

_lock_

string 

Unique Id

is_disabled

_lock_

boolean 

Has this credential been disabled?

logged_in_at

_lock_

string 

Timestamp for most recent login using credential

type

_lock_

string 

Short name for the type of this kind of credential

url

_lock_

string 

Link to get this item

credentials_google

_lock_

[CredentialsGoogle](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CredentialsGoogle)

Google auth credentials

Expand CredentialsGoogle definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

created_at

_lock_

string 

Timestamp for the creation of this credential

domain

_lock_

string 

Google domain

email

_lock_

string 

EMail address

google_user_id

_lock_

string 

Google's Unique ID for this user

is_disabled

_lock_

boolean 

Has this credential been disabled?

logged_in_at

_lock_

string 

Timestamp for most recent login using credential

type

_lock_

string 

Short name for the type of this kind of credential

url

_lock_

string 

Link to get this item

credentials_ldap

_lock_

[CredentialsLDAP](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CredentialsLDAP)

LDAP credentials

Expand CredentialsLDAP definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

created_at

_lock_

string 

Timestamp for the creation of this credential

email

_lock_

string 

EMail address

is_disabled

_lock_

boolean 

Has this credential been disabled?

ldap_dn

_lock_

string 

LDAP Distinguished name for this user (as-of the last login)

ldap_id

_lock_

string 

LDAP Unique ID for this user

logged_in_at

_lock_

string 

Timestamp for most recent login using credential

type

_lock_

string 

Short name for the type of this kind of credential

url

_lock_

string 

Link to get this item

credentials_looker_openid

_lock_

[CredentialsLookerOpenid](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CredentialsLookerOpenid)

LookerOpenID credentials. Used for login by Looker Analysts

Expand CredentialsLookerOpenid definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

created_at

_lock_

string 

Timestamp for the creation of this credential

email

_lock_

string 

EMail address used for user login

is_disabled

_lock_

boolean 

Has this credential been disabled?

logged_in_at

_lock_

string 

Timestamp for most recent login using credential

logged_in_ip

_lock_

string 

IP address of client for most recent login using credential

type

_lock_

string 

Short name for the type of this kind of credential

url

_lock_

string 

Link to get this item

user_url

_lock_

string 

Link to get this user

credentials_oidc

_lock_

[CredentialsOIDC](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CredentialsOIDC)

OpenID Connect auth credentials

Expand CredentialsOIDC definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

created_at

_lock_

string 

Timestamp for the creation of this credential

email

_lock_

string 

EMail address

is_disabled

_lock_

boolean 

Has this credential been disabled?

logged_in_at

_lock_

string 

Timestamp for most recent login using credential

oidc_user_id

_lock_

string 

OIDC OP's Unique ID for this user

type

_lock_

string 

Short name for the type of this kind of credential

url

_lock_

string 

Link to get this item

credentials_saml

_lock_

[CredentialsSaml](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CredentialsSaml)

Saml auth credentials

Expand CredentialsSaml definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

created_at

_lock_

string 

Timestamp for the creation of this credential

email

_lock_

string 

EMail address

is_disabled

_lock_

boolean 

Has this credential been disabled?

logged_in_at

_lock_

string 

Timestamp for most recent login using credential

saml_user_id

_lock_

string 

Saml IdP's Unique ID for this user

type

_lock_

string 

Short name for the type of this kind of credential

url

_lock_

string 

Link to get this item

credentials_totp

_lock_

[CredentialsTotp](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CredentialsTotp)

Two-factor credentials

Expand CredentialsTotp definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

created_at

_lock_

string 

Timestamp for the creation of this credential

is_disabled

_lock_

boolean 

Has this credential been disabled?

type

_lock_

string 

Short name for the type of this kind of credential

verified

_lock_

boolean 

User has verified

url

_lock_

string 

Link to get this item

credentials_workforce

_lock_

[CredentialsWorkforce](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CredentialsWorkforce)

Workforce Identity auth credentials

Expand CredentialsWorkforce definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

created_at

_lock_

string 

Timestamp for the creation of this credential

email

_lock_

string 

Email address

is_disabled

_lock_

boolean 

Has this credential been disabled?

logged_in_at

_lock_

string 

Timestamp for most recent login using credential

workforce_user_id

_lock_

string 

Workforce Unique ID for this user

type

_lock_

string 

Short name for the type of this kind of credential

url

_lock_

string 

Link to get this item

display_name

_lock_

string 

Full name for display (available only if both first_name and last_name are set)

email

_lock_

string 

EMail address

embed_group_space_id

_lock_

string 

(DEPRECATED) (Embed only) ID of user's group space based on the external_group_id optionally specified during embed user login

first_name

string 

First name

group_ids

string[] 

home_folder_id

string 

ID string for user's home folder

id

_lock_

string 

Unique Id

is_disabled

boolean 

Account has been disabled

last_name

string 

Last name

locale

string 

User's preferred locale. User locale takes precedence over Looker's system-wide default locale. Locale determines language of display strings and date and numeric formatting in API responses. Locale string must be a 2 letter language code or a combination of language code and region code: 'en' or 'en-US', for example.

looker_versions

string[] 

models_dir_validated

boolean 

User's dev workspace has been checked for presence of applicable production projects

personal_folder_id

_lock_

string 

ID of user's personal folder

presumed_looker_employee

_lock_

boolean 

(DEPRECATED) User is identified as an employee of Looker

role_ids

string[] 

sessions

[Session](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Session)[] 

Expand Session definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

ip_address

_lock_

string 

IP address of user when this session was initiated

browser

_lock_

string 

User's browser type

operating_system

_lock_

string 

User's Operating System

city

_lock_

string 

City component of user location (derived from IP address)

state

_lock_

string 

State component of user location (derived from IP address)

country

_lock_

string 

Country component of user location (derived from IP address)

credentials_type

_lock_

string 

Type of credentials used for logging in this session

extended_at

_lock_

string 

Time when this session was last extended by the user

extended_count

_lock_

integer 

Number of times this session was extended

sudo_user_id

_lock_

string 

Actual user in the case when this session represents one user sudo'ing as another

created_at

_lock_

string 

Time when this session was initiated

expires_at

_lock_

string 

Time when this session will expire

url

_lock_

string 

Link to get this item

ui_state

object 

Per user dictionary of undocumented state information owned by the Looker UI.

verified_looker_employee

_lock_

boolean 

User is identified as an employee of Looker who has been verified via Looker corporate authentication

roles_externally_managed

_lock_

boolean 

User's roles are managed by an external directory like SAML or LDAP and can not be changed directly.

allow_direct_roles

_lock_

boolean 

User can be directly assigned a role.

allow_normal_group_membership

_lock_

boolean 

User can be a direct member of a normal Looker group.

allow_roles_from_normal_groups

_lock_

boolean 

User can inherit roles from a normal Looker group.

embed_group_folder_id

_lock_

string 

(Embed only) ID of user's group folder based on the external_group_id optionally specified during embed user login

is_iam_admin

_lock_

boolean 

User is an IAM Admin. This field may only be applicable for [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/r/looker-core/overview). The is_iam_admin is not returned by default. Please explicitly request this attribute if needed via the fields query param. Note: Including the optional is_iam_admin attribute can increase API latency. For best performance, use this attribute only when filtering for users with the 'Admin via IAM' role. When using this filter, always paginate your results with the offset and limit fields to optimize response time.

can_manage_api3_creds

boolean 

Indicates if the user can manage API3 credentials. This is an experimental feature and may not yet be available on your instance.

is_service_account

_lock_

boolean 

Indicates if this user is a service account.

service_account_name

_lock_

string 

The display name of the service account. This field is omitted for non service account users.

url

_lock_

string 

Link to get this item

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 403: Permission Denied

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

## Examples

### C#

[https://github.com/looker-open-source/sdk-codegen/blob/main/csharp/sdk/4.0/methods.cs ](https://github.com/looker-open-source/sdk-codegen/blob/main/csharp/sdk/4.0/methods.cs#L9607 "https://github.com/looker-open-source/sdk-codegen/blob/main/csharp/sdk/4.0/methods.cs")  
---  
  
### Go

[https://github.com/looker-open-source/sdk-codegen/blob/main/go/sdk/v4/methods.go ](https://github.com/looker-open-source/sdk-codegen/blob/main/go/sdk/v4/methods.go#L7242 "https://github.com/looker-open-source/sdk-codegen/blob/main/go/sdk/v4/methods.go")  
---  
  
### Kotlin

[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/main/com/looker/sdk/4.0/methods.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/main/com/looker/sdk/4.0/methods.kt#L9817 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/main/com/looker/sdk/4.0/methods.kt")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/main/com/looker/sdk/4.0/streams.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/main/com/looker/sdk/4.0/streams.kt#L9815 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/main/com/looker/sdk/4.0/streams.kt")  
  
### TypeScript

[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk/src/4.0/funcs.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk/src/4.0/funcs.ts#L12386 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk/src/4.0/funcs.ts")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk/src/4.0/methods.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk/src/4.0/methods.ts#L11675 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk/src/4.0/methods.ts")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk/src/4.0/methodsInterface.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk/src/4.0/methodsInterface.ts#L8303 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk/src/4.0/methodsInterface.ts")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk/src/4.0/streams.ts ](https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk/src/4.0/streams.ts#L13304 "https://github.com/looker-open-source/sdk-codegen/blob/main/packages/sdk/src/4.0/streams.ts")  
  
### Python

[https://github.com/looker-open-source/sdk-codegen/blob/main/python/looker_sdk/sdk/api40/methods.py ](https://github.com/looker-open-source/sdk-codegen/blob/main/python/looker_sdk/sdk/api40/methods.py#L12071 "https://github.com/looker-open-source/sdk-codegen/blob/main/python/looker_sdk/sdk/api40/methods.py")  
---  
  
### Swift

[https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/sdk/methods.swift ](https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/sdk/methods.swift#L11209 "https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/sdk/methods.swift")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/sdk/streams.swift ](https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/sdk/streams.swift#L11207 "https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/sdk/streams.swift")  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
