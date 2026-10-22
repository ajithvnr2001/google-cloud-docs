---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-soar-ops-module/
title: soar_ops module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:01.969126+00:00
---

# soar_ops module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-soar-ops-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# soar_ops module

### TIPCommon.soar_ops.create_slo_message

`TIPCommon.soar_ops.create_slo_message(slo: int, interval_days: Iterable[int], existing_comments: Iterable[str])`

Gets SLO warning messages based on time intervals and existing comments.

For the `interval_days=[0, 1, 7, 14]` parameter, the function sends a message warning that the SLO would be breached following the next schedule:

  * 7-14 days until the expiration time.
  * 1-7 days until the expiration time.
  * When the SLO was breached.



If a comment was already sent in the current breached interval, no new comment is returned (`None` is returned).

Parameters  
---  
`slo` | `int`The SLO breach date in Unix microseconds (for example, 1_673_774_674_567)  
`interval_days` | `Iterable[int]`An iterable containing the number of days from time breach warnings should be sent (for example, [0, 1, 3, 7, 14])   
`existing_comments` | `Iterable[int]`The existing comments to check if a comment was already sent.  
  
#### Raises

`ValueError`\- When one of the time intervals is negative.

#### Returns

The comment is returned if applicable. Otherwise `None` is returned.

### TIPCommon.soar_ops.get_clean_comment_body

`TIPCommon.soar_ops.get_clean_comment_body(comment: str | CaseComment, prefix: str)`

Removes a prefix from the comment string or comment object.

Parameters  
---  
`comment` | `str | CaseComment`The comment string or comment object to remove the prefix from.  
`prefix` | `str`The prefix to remove.  
  
#### Raises

`TypeError`\- When the type of comment is neither `str` or `CaseComment`.

#### Returns

The comment without the prefix.

#### Return type

`str`

### TIPCommon.soar_ops.get_file

`TIPCommon.soar_ops.get_file(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, identifier: str)→ bytes | None`

Returns file content in bytes.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`identifier` | `str`The filename identifier along with the full path.  
  
#### Returns

Bytes data of the provided identifier.

#### Return type

`bytes | None`

### TIPCommon.soar_ops.get_secops_mode

`TIPCommon.soar_ops.get_secops_mode()→ str | None`

Returns the `SECOPS_MODE` environment variable.

#### Returns

The `SECOPS_MODE` environment variable.

#### Return type

`str | None`

### TIPCommon.soar_ops.get_soar_case_comments

`TIPCommon.soar_ops.get_soar_case_comments(chronicle_soar: SiemplifyAction | SiemplifyJob, case_id: str | int)`

Returns a list of comment objects from a case, using its ID.

Parameters  
---  
`chronicle_soar` | `SiemplifyAction | SiemplifyJob`The SDK object.  
`case_id` | `str | int`The ID of the case whose comments are fetched.  
  
#### Returns

A list of comment objects.

#### Return type

`list[base.action.CaseComment]`

### TIPCommon.soar_ops.get_user_by_id

`TIPCommon.soar_ops.get_user_by_id(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, user_id: str)→ UserProfileCard | None`

Gets a `UserProfileCard` datamodel Python object from a user ID.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`user_id` | `str`The user ID. For example, `f6dc053c-58bb-4da5-95bb-739be7d297a2`.  
  
#### Returns

The `UserProfileCard` datamodel object if the `user_id` exists in the platform; otherwise, `None` is returned. 

The attribute `raw_data` of the `UserProfileCard` object contains the user details as a JSON.

##### Example JSON response in `user.raw_data`:

The following example shows the JSON response structure for the `raw_data` attribute:
    
    
    {
        "name": "projects/project/locations/location/instances/instance/legacySoarUsers/1",
        "id": 1,
        "displayName": "84b44ee6-d372-43c9-8abe-ae14b8421492",
        "permissionGroups": [
            {
                "id": 1,
                "name": "Admins"
            }
        ],
        "lastLoginTime": 1769503546327,
        "userFullName": "Test Admin",
        "socRoles": [1],
        "email": "admin@example.com",
        "userType": "Internal",
        "environmentsJson": "[\"*\"]",
        "accountState": "Active",
        "providerName": "Internal",
        "allowedPlatforms": [0],
        "loginIdentifier": "admin@example.com",
        "firstName": "Test",
        "lastName": "Admin"
    }
    

#### Return type

`UserProfileCard | None`

### TIPCommon.soar_ops.get_users_profile_cards_with_pagination

`TIPCommon.soar_ops.get_users_profile_cards_with_pagination(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, search_term: str = '', page_size: int = 20, filter_by_role: bool = False, filter_disabled_users: bool = False, filter_support_users: bool = False, fetch_only_support_users: bool = False, filter_permission_types: list[int] | None = None)→ list[UserProfileCard]`

Gets all user profile cards using pagination. The page size serves as the limit for the number of users in each iteration.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`search_term` | `str`The search terms.Defaults to `''`.  
`page_size` | `int`The number of users to return.Defaults to `20`.  
`filter_by_role` | `bool`Define whether to filter by role.Defaults to `False`.  
`filter_disabled_users` | `bool`Define whether to filter disabled users.Defaults to `False`.  
`filter_support_users` | `bool`Define whether to filter support users.Defaults to `False`.  
`fetch_only_support_users` | `bool`Define whether to return only support users.Defaults to `False`.  
`filter_permission_types` | `list[int] | None`A list of filter permission types (e.g. `0`).Defaults to `None`.  
  
#### Returns

A list of all users.

#### Return type

`list[UserProfileCard]`

### TIPCommon.soar_ops.is_slo_comment

`TIPCommon.soar_ops.is_slo_comment(comment: str)`

Checks if a comment is an SLO warning comment.

An SLO comment is either an SLO warning ("SLO will be breached in {int} days") or an SLO breached message ("SLO was breached").

Parameters  
---  
`comment` | `str`The comment to check.  
  
#### Returns

`True` if the comment is an SLO comment. Otherwise, `False` is returned.

#### Return type

`bool`

### TIPCommon.soar_ops.remove_prefix_from_comments

`TIPCommon.soar_ops.remove_prefix_from_comments(comments: list[str], prefix: str)`

Removes a prefix (when present) from a list of comments.

Parameters  
---  
`comments` | `list[str]`The comments to remove the prefix from.  
`prefix` | `str`The prefix to remove.  
  
#### Returns

A list of all comments after the prefix was removed from them

#### Return type

`list[str]`

### TIPCommon.soar_ops.save_file

`TIPCommon.soar_ops.save_file(chronicle_soar: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, path: str, name: str, content: bytes)→ bytes | None`

Saves a file to a Google Cloud bucket or local path.

#### Parameters

Parameters  
---  
`chronicle_soar` | `ChronicleSOAR`A Google SecOps SDK object.  
`path` | `str`The path of the folder where files should be saved.  
`name` | `str`The filename to be saved.  
`content` | `bytes`The file content in bytes format.  
  
#### Returns

The path to the downloaded files.

#### Return type

`str | None`

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
