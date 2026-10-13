---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/update_ldap_config/
title: Update LDAP Configuration \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:11.841786+00:00
---

# Update LDAP Configuration  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/update_ldap_config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Update LDAP Configuration Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Update the LDAP configuration.

Configuring LDAP impacts authentication for all users. This configuration should be done carefully.

Only Looker administrators can read and update the LDAP configuration.

LDAP is enabled or disabled for Looker using the **enabled** field.

It is **highly** recommended that any LDAP setting changes be tested using the APIs below before being set globally.

See the [Looker LDAP docs](https://docs.cloud.google.com/looker/docs/r/api/ldap_setup) for additional information.

Calls to this endpoint may be denied by [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/r/looker-core/overview).

## Request

PATCH /ldap_config 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[LDAPConfig](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LDAPConfig)

LDAP Config

Expand LDAPConfig definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

alternate_email_login_allowed

boolean 

Allow alternate email-based login via '/login/email' for admins and for specified users with the 'login_special_email' permission. This option is useful as a fallback during ldap setup, if ldap config problems occur later, or if you need to support some users who are not in your ldap directory. Looker email/password logins are always disabled for regular users when ldap is enabled.

auth_password

string 

(Write-Only) Password for the LDAP account used to access the LDAP server

auth_requires_role

boolean 

Users will not be allowed to login at all unless a role for them is found in LDAP if set to true

auth_username

string 

Distinguished name of LDAP account used to access the LDAP server

connection_host

string 

LDAP server hostname

connection_port

string 

LDAP host port

connection_tls

boolean 

Use Transport Layer Security

connection_tls_no_verify

boolean 

Do not verify peer when using TLS

default_new_user_group_ids

string[] 

default_new_user_groups

[Group](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Group)[] 

default_new_user_role_ids

string[] 

default_new_user_roles

[Role](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Role)[] 

enabled

boolean 

Enable/Disable LDAP authentication for the server

force_no_page

boolean 

Don't attempt to do LDAP search result paging (RFC 2696) even if the LDAP server claims to support it.

groups

[LDAPGroupRead](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LDAPGroupRead)[] 

groups_base_dn

string 

Base dn for finding groups in LDAP searches

groups_finder_type

string 

Identifier for a strategy for how Looker will search for groups in the LDAP server

groups_member_attribute

string 

LDAP Group attribute that signifies the members of the groups. Most commonly 'member'

groups_objectclasses

string 

Optional comma-separated list of supported LDAP objectclass for groups when doing groups searches

groups_user_attribute

string 

LDAP Group attribute that signifies the user in a group. Most commonly 'dn'

groups_with_role_ids

[LDAPGroupWrite](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LDAPGroupWrite)[] 

has_auth_password

_lock_

boolean 

(Read-only) Has the password been set for the LDAP account used to access the LDAP server

merge_new_users_by_email

boolean 

Merge first-time ldap login to existing user account by email addresses. When a user logs in for the first time via ldap this option will connect this user into their existing account by finding the account with a matching email address. Otherwise a new user account will be created for the user.

modified_at

_lock_

string 

When this config was last modified

modified_by

_lock_

string 

User id of user who last modified this config

set_roles_from_groups

boolean 

Set user roles in Looker based on groups from LDAP

test_ldap_password

string 

(Write-Only) Test LDAP user password. For ldap tests only.

test_ldap_user

string 

(Write-Only) Test LDAP user login id. For ldap tests only.

user_attribute_map_email

string 

Name of user record attributes used to indicate email address field

user_attribute_map_first_name

string 

Name of user record attributes used to indicate first name

user_attribute_map_last_name

string 

Name of user record attributes used to indicate last name

user_attribute_map_ldap_id

string 

Name of user record attributes used to indicate unique record id

user_attributes

[LDAPUserAttributeRead](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LDAPUserAttributeRead)[] 

user_attributes_with_ids

[LDAPUserAttributeWrite](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LDAPUserAttributeWrite)[] 

user_bind_base_dn

string 

Distinguished name of LDAP node used as the base for user searches

user_custom_filter

string 

(Optional) Custom RFC-2254 filter clause for use in finding user during login. Combined via 'and' with the other generated filter clauses.

user_id_attribute_names

string 

Name(s) of user record attributes used for matching user login id (comma separated list)

user_objectclass

string 

(Optional) Name of user record objectclass used for finding user during login id

allow_normal_group_membership

boolean 

Allow LDAP auth'd users to be members of non-reflected Looker groups. If 'false', user will be removed from non-reflected groups on login.

allow_roles_from_normal_groups

boolean 

LDAP auth'd users will be able to inherit roles from non-reflected Looker groups.

allow_direct_roles

boolean 

Allows roles to be directly assigned to LDAP auth'd users.

url

_lock_

string 

Link to get this item

## Response

### 200: New state for LDAP Configuration.

Datatype

Description

(object)

[LDAPConfig](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LDAPConfig)

can

_lock_

object 

Operations the current user is able to perform on this object

alternate_email_login_allowed

boolean 

Allow alternate email-based login via '/login/email' for admins and for specified users with the 'login_special_email' permission. This option is useful as a fallback during ldap setup, if ldap config problems occur later, or if you need to support some users who are not in your ldap directory. Looker email/password logins are always disabled for regular users when ldap is enabled.

auth_password

string 

(Write-Only) Password for the LDAP account used to access the LDAP server

auth_requires_role

boolean 

Users will not be allowed to login at all unless a role for them is found in LDAP if set to true

auth_username

string 

Distinguished name of LDAP account used to access the LDAP server

connection_host

string 

LDAP server hostname

connection_port

string 

LDAP host port

connection_tls

boolean 

Use Transport Layer Security

connection_tls_no_verify

boolean 

Do not verify peer when using TLS

default_new_user_group_ids

string[] 

default_new_user_groups

[Group](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Group)[] 

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

[Role](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Role)[] 

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

[PermissionSet](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/PermissionSet)

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

[ModelSet](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ModelSet)

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

Enable/Disable LDAP authentication for the server

force_no_page

boolean 

Don't attempt to do LDAP search result paging (RFC 2696) even if the LDAP server claims to support it.

groups

[LDAPGroupRead](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LDAPGroupRead)[] 

Expand LDAPGroupRead definition... 

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

Name of group in LDAP

roles

[Role](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Role)[] 

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

[PermissionSet](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/PermissionSet)

(Read only) Permission set

permission_set_id

string 

(Write-Only) Id of permission set

model_set

_lock_

[ModelSet](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ModelSet)

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

url

_lock_

string 

Link to ldap config

groups_base_dn

string 

Base dn for finding groups in LDAP searches

groups_finder_type

string 

Identifier for a strategy for how Looker will search for groups in the LDAP server

groups_member_attribute

string 

LDAP Group attribute that signifies the members of the groups. Most commonly 'member'

groups_objectclasses

string 

Optional comma-separated list of supported LDAP objectclass for groups when doing groups searches

groups_user_attribute

string 

LDAP Group attribute that signifies the user in a group. Most commonly 'dn'

groups_with_role_ids

[LDAPGroupWrite](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LDAPGroupWrite)[] 

Expand LDAPGroupWrite definition... 

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

Name of group in LDAP

role_ids

string[] 

url

_lock_

string 

Link to ldap config

has_auth_password

_lock_

boolean 

(Read-only) Has the password been set for the LDAP account used to access the LDAP server

merge_new_users_by_email

boolean 

Merge first-time ldap login to existing user account by email addresses. When a user logs in for the first time via ldap this option will connect this user into their existing account by finding the account with a matching email address. Otherwise a new user account will be created for the user.

modified_at

_lock_

string 

When this config was last modified

modified_by

_lock_

string 

User id of user who last modified this config

set_roles_from_groups

boolean 

Set user roles in Looker based on groups from LDAP

test_ldap_password

string 

(Write-Only) Test LDAP user password. For ldap tests only.

test_ldap_user

string 

(Write-Only) Test LDAP user login id. For ldap tests only.

user_attribute_map_email

string 

Name of user record attributes used to indicate email address field

user_attribute_map_first_name

string 

Name of user record attributes used to indicate first name

user_attribute_map_last_name

string 

Name of user record attributes used to indicate last name

user_attribute_map_ldap_id

string 

Name of user record attributes used to indicate unique record id

user_attributes

[LDAPUserAttributeRead](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LDAPUserAttributeRead)[] 

Expand LDAPUserAttributeRead definition... 

name

_lock_

string 

Name of User Attribute in LDAP

required

_lock_

boolean 

Required to be in LDAP assertion for login to be allowed to succeed

user_attributes

[UserAttribute](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/UserAttribute)[] 

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

url

_lock_

string 

Link to ldap config

user_attributes_with_ids

[LDAPUserAttributeWrite](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LDAPUserAttributeWrite)[] 

Expand LDAPUserAttributeWrite definition... 

name

string 

Name of User Attribute in LDAP

required

boolean 

Required to be in LDAP assertion for login to be allowed to succeed

user_attribute_ids

string[] 

url

_lock_

string 

Link to ldap config

user_bind_base_dn

string 

Distinguished name of LDAP node used as the base for user searches

user_custom_filter

string 

(Optional) Custom RFC-2254 filter clause for use in finding user during login. Combined via 'and' with the other generated filter clauses.

user_id_attribute_names

string 

Name(s) of user record attributes used for matching user login id (comma separated list)

user_objectclass

string 

(Optional) Name of user record objectclass used for finding user during login id

allow_normal_group_membership

boolean 

Allow LDAP auth'd users to be members of non-reflected Looker groups. If 'false', user will be removed from non-reflected groups on login.

allow_roles_from_normal_groups

boolean 

LDAP auth'd users will be able to inherit roles from non-reflected Looker groups.

allow_direct_roles

boolean 

Allows roles to be directly assigned to LDAP auth'd users.

url

_lock_

string 

Link to get this item

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

### 403: Permission Denied

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

### 422: Validation Error

Datatype

Description

(object)

[ValidationError](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ValidationError)

message

_lock_

string 

Error details

errors

[ValidationErrorDetail](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ValidationErrorDetail)[] 

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
