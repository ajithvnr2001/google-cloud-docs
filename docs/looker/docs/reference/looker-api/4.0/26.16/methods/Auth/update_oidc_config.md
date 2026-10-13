---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Auth/update_oidc_config/
title: Update OIDC Configuration \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:16.267303+00:00
---

# Update OIDC Configuration  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Auth/update_oidc_config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Update OIDC Configuration Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.18 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Update the OIDC configuration.

Configuring OIDC impacts authentication for all users. This configuration should be done carefully.

Only Looker administrators can read and update the OIDC configuration.

OIDC is enabled or disabled for Looker using the **enabled** field.

It is **highly** recommended that any OIDC setting changes be tested using the APIs below before being set globally.

Calls to this endpoint may be denied by [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/r/looker-core/overview).

## Request

PATCH /oidc_config 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[OIDCConfig](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/OIDCConfig)

OIDC Config

Expand OIDCConfig definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

alternate_email_login_allowed

boolean 

Allow alternate email-based login via '/login/email' for admins and for specified users with the 'login_special_email' permission. This option is useful as a fallback during ldap setup, if ldap config problems occur later, or if you need to support some users who are not in your ldap directory. Looker email/password logins are always disabled for regular users when ldap is enabled.

audience

string 

OpenID Provider Audience

auth_requires_role

boolean 

Users will not be allowed to login at all unless a role for them is found in OIDC if set to true

authorization_endpoint

string 

OpenID Provider Authorization Url

default_new_user_group_ids

string[] 

default_new_user_groups

[Group](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Group)[] 

default_new_user_role_ids

string[] 

default_new_user_roles

[Role](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Role)[] 

enabled

boolean 

Enable/Disable OIDC authentication for the server

groups

[OIDCGroupRead](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/OIDCGroupRead)[] 

groups_attribute

string 

Name of user record attributes used to indicate groups. Used when 'groups_finder_type' is set to 'grouped_attribute_values'

groups_with_role_ids

[OIDCGroupWrite](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/OIDCGroupWrite)[] 

identifier

string 

Relying Party Identifier (provided by OpenID Provider)

issuer

string 

OpenID Provider Issuer

modified_at

_lock_

string 

When this config was last modified

modified_by

_lock_

string 

User id of user who last modified this config

new_user_migration_types

string 

Merge first-time oidc login to existing user account by email addresses. When a user logs in for the first time via oidc this option will connect this user into their existing account by finding the account with a matching email address by testing the given types of credentials for existing users. Otherwise a new user account will be created for the user. This list (if provided) must be a comma separated list of string like 'email,ldap,google'

scopes

string[] 

secret

string 

(Write-Only) Relying Party Secret (provided by OpenID Provider)

set_roles_from_groups

boolean 

Set user roles in Looker based on groups from OIDC

test_slug

_lock_

string 

Slug to identify configurations that are created in order to run a OIDC config test

token_endpoint

string 

OpenID Provider Token Url

user_attribute_map_email

string 

Name of user record attributes used to indicate email address field

user_attribute_map_first_name

string 

Name of user record attributes used to indicate first name

user_attribute_map_last_name

string 

Name of user record attributes used to indicate last name

user_attributes

[OIDCUserAttributeRead](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/OIDCUserAttributeRead)[] 

user_attributes_with_ids

[OIDCUserAttributeWrite](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/OIDCUserAttributeWrite)[] 

userinfo_endpoint

string 

OpenID Provider User Information Url

allow_normal_group_membership

boolean 

Allow OIDC auth'd users to be members of non-reflected Looker groups. If 'false', user will be removed from non-reflected groups on login.

allow_roles_from_normal_groups

boolean 

OIDC auth'd users will inherit roles from non-reflected Looker groups.

allow_direct_roles

boolean 

Allows roles to be directly assigned to OIDC auth'd users.

url

_lock_

string 

Link to get this item

## Response

### 200: New state for OIDC Configuration.

Datatype

Description

(object)

[OIDCConfig](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/OIDCConfig)

can

_lock_

object 

Operations the current user is able to perform on this object

alternate_email_login_allowed

boolean 

Allow alternate email-based login via '/login/email' for admins and for specified users with the 'login_special_email' permission. This option is useful as a fallback during ldap setup, if ldap config problems occur later, or if you need to support some users who are not in your ldap directory. Looker email/password logins are always disabled for regular users when ldap is enabled.

audience

string 

OpenID Provider Audience

auth_requires_role

boolean 

Users will not be allowed to login at all unless a role for them is found in OIDC if set to true

authorization_endpoint

string 

OpenID Provider Authorization Url

default_new_user_group_ids

string[] 

default_new_user_groups

[Group](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Group)[] 

Expand Group definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

can_add_to_content_metadata

boolean 

Group can be used in content access controls

contains_current_user

_lock_

boolean 

Currently logged in user is group member

external_group_id

_lock_

string 

External Id group if embed group

externally_managed

_lock_

boolean 

Group membership controlled outside of Looker

id

_lock_

string 

Unique Id

include_by_default

_lock_

boolean 

New users are added to this group by default

name

string 

Name of group

user_count

_lock_

integer 

Number of users included in this group

default_new_user_role_ids

string[] 

default_new_user_roles

[Role](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Role)[] 

Expand Role definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

name

string 

Name of Role

permission_set

_lock_

[PermissionSet](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/PermissionSet)

(Read only) Permission set

Expand PermissionSet definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

all_access

_lock_

boolean 

built_in

_lock_

boolean 

id

_lock_

string 

Unique Id

name

string 

Name of PermissionSet

permissions

string[] 

url

_lock_

string 

Link to get this item

permission_set_id

string 

(Write-Only) Id of permission set

model_set

_lock_

[ModelSet](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/ModelSet)

(Read only) Model set

Expand ModelSet definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

all_access

_lock_

boolean 

built_in

_lock_

boolean 

id

_lock_

string 

Unique Id

models

string[] 

name

string 

Name of ModelSet

url

_lock_

string 

Link to get this item

model_set_id

string 

(Write-Only) Id of model set

internal

_lock_

boolean 

Is this a Looker internal role

url

_lock_

string 

Link to get this item

users_url

_lock_

string 

Link to get list of users with this role

enabled

boolean 

Enable/Disable OIDC authentication for the server

groups

[OIDCGroupRead](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/OIDCGroupRead)[] 

Expand OIDCGroupRead definition... 

id

_lock_

string 

Unique Id

looker_group_id

_lock_

string 

Unique Id of group in Looker

looker_group_name

_lock_

string 

Name of group in Looker

name

_lock_

string 

Name of group in OIDC

roles

[Role](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Role)[] 

Expand Role definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

name

string 

Name of Role

permission_set

_lock_

[PermissionSet](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/PermissionSet)

(Read only) Permission set

permission_set_id

string 

(Write-Only) Id of permission set

model_set

_lock_

[ModelSet](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/ModelSet)

(Read only) Model set

model_set_id

string 

(Write-Only) Id of model set

internal

_lock_

boolean 

Is this a Looker internal role

url

_lock_

string 

Link to get this item

users_url

_lock_

string 

Link to get list of users with this role

groups_attribute

string 

Name of user record attributes used to indicate groups. Used when 'groups_finder_type' is set to 'grouped_attribute_values'

groups_with_role_ids

[OIDCGroupWrite](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/OIDCGroupWrite)[] 

Expand OIDCGroupWrite definition... 

id

string 

Unique Id

looker_group_id

_lock_

string 

Unique Id of group in Looker

looker_group_name

string 

Name of group in Looker

name

string 

Name of group in OIDC

role_ids

string[] 

identifier

string 

Relying Party Identifier (provided by OpenID Provider)

issuer

string 

OpenID Provider Issuer

modified_at

_lock_

string 

When this config was last modified

modified_by

_lock_

string 

User id of user who last modified this config

new_user_migration_types

string 

Merge first-time oidc login to existing user account by email addresses. When a user logs in for the first time via oidc this option will connect this user into their existing account by finding the account with a matching email address by testing the given types of credentials for existing users. Otherwise a new user account will be created for the user. This list (if provided) must be a comma separated list of string like 'email,ldap,google'

scopes

string[] 

secret

string 

(Write-Only) Relying Party Secret (provided by OpenID Provider)

set_roles_from_groups

boolean 

Set user roles in Looker based on groups from OIDC

test_slug

_lock_

string 

Slug to identify configurations that are created in order to run a OIDC config test

token_endpoint

string 

OpenID Provider Token Url

user_attribute_map_email

string 

Name of user record attributes used to indicate email address field

user_attribute_map_first_name

string 

Name of user record attributes used to indicate first name

user_attribute_map_last_name

string 

Name of user record attributes used to indicate last name

user_attributes

[OIDCUserAttributeRead](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/OIDCUserAttributeRead)[] 

Expand OIDCUserAttributeRead definition... 

name

_lock_

string 

Name of User Attribute in OIDC

required

_lock_

boolean 

Required to be in OIDC assertion for login to be allowed to succeed

user_attributes

[UserAttribute](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/UserAttribute)[] 

Expand UserAttribute definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

name

string 

Name of user attribute

label

string 

Human-friendly label for user attribute

type

string 

Type of user attribute ("string", "number", "datetime", "yesno", "zipcode", "advanced_filter_string", "advanced_filter_number", "file")

default_value

string 

Default value for when no value is set on the user

is_system

_lock_

boolean 

Attribute is a system default

is_permanent

_lock_

boolean 

Attribute is permanent and cannot be deleted

value_is_hidden

boolean 

If true, users will not be able to view values of this attribute

user_can_view

boolean 

Non-admin users can see the values of their attributes and use them in filters

user_can_edit

boolean 

Users can change the value of this attribute for themselves

hidden_value_domain_whitelist

string 

Destinations to which a hidden attribute may be sent. Once set, cannot be edited.

needed_for_ci_run

boolean 

Whether this user attribute is needed for a CI run

value_for_ci_run

string 

The value to use for this user attribute during a CI run

user_attributes_with_ids

[OIDCUserAttributeWrite](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/OIDCUserAttributeWrite)[] 

Expand OIDCUserAttributeWrite definition... 

name

string 

Name of User Attribute in OIDC

required

boolean 

Required to be in OIDC assertion for login to be allowed to succeed

user_attribute_ids

string[] 

userinfo_endpoint

string 

OpenID Provider User Information Url

allow_normal_group_membership

boolean 

Allow OIDC auth'd users to be members of non-reflected Looker groups. If 'false', user will be removed from non-reflected groups on login.

allow_roles_from_normal_groups

boolean 

OIDC auth'd users will inherit roles from non-reflected Looker groups.

allow_direct_roles

boolean 

Allows roles to be directly assigned to OIDC auth'd users.

url

_lock_

string 

Link to get this item

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 422: Validation Error

Datatype

Description

(object)

[ValidationError](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/ValidationError)

message

_lock_

string 

Error details

errors

[ValidationErrorDetail](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/ValidationErrorDetail)[] 

Expand ValidationErrorDetail definition... 

field

_lock_

string 

Field with error

code

_lock_

string 

Error code

message

_lock_

string 

Error info message

documentation_url

_lock_

string 

Documentation link

documentation_url

_lock_

string 

Documentation link

### 429: Too Many Requests

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

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

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
