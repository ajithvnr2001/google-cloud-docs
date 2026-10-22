---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-soar-ops-module/
title: TIPCommon.soar_ops \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:03.884338+00:00
---

# TIPCommon.soar_ops  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-soar-ops-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TIPCommon.soar_ops

The **TIPCommon.soar_ops** module contains a collection of operational helpers designed to streamline common tasks in the Google Security Operations platform. These utilities range from managing Service Level Objectives (SLO) to handling cross-platform file storage and retrieving paginated user metadata.

## SLO monitoring and comments

These functions help maintain awareness of Service Level Objectives by generating warnings and identifying breach-related communications within case comments.

Function | Parameters | Description & Returns  
---|---|---  
`create_slo_message()` | 

  * `slo`: (int) Breach date in unix microseconds.
  * `interval_days`: (Iterable[int]) Warning intervals (such as `[0, 1, 7, 14]`).
  * `existing_comments`: (Iterable[str]) History to check for duplicates.

| Returns: `str | None` Generates an SLO warning message based on specified time intervals. For example, using `[0, 7, 14]` sends warnings at 14 days, 7 days, and upon breach. Raises `ValueError` if an interval is negative. Returns `None` if a comment was already sent for the current interval.  
`is_slo_comment()` | 

  * `comment`: (str) The text to evaluate.

| Returns: `bool` Identifies if a string is a standard platform SLO warning or breach message (such as "SLO was breached.").  
`get_clean_comment_body()` | 

  * `comment`: (str | CaseComment) The raw comment.
  * `prefix`: (str) The string to strip.

| Returns: `str` Removes a specific prefix from a comment string or object. Raises `TypeError` if the input is not a `str` or `CaseComment`.  
`remove_prefix_from_comments()` | 

  * `comments`: (list[str]) List of strings.
  * `prefix`: (str) Prefix to remove.

| Returns: `list[str]` Bulk utility to strip a specific prefix from a collection of comment strings.  
  
## File and storage operations

Operational helpers for interacting with the file system or Google Cloud storage buckets, ensuring consistent file handling across different execution environments.

Function | Parameters | Description & Returns  
---|---|---  
`get_file()` | 

  * `chronicle_soar`: (ChronicleSOAR) SDK instance.
  * `identifier`: (str) Full path and name.

| Returns: `bytes | None` Retrieves the raw content of a file from the environment. Returns `None` if the file cannot be accessed.  
`save_file()` | 

  * `chronicle_soar`: (ChronicleSOAR) SDK instance.
  * `path`: (str) Folder path.
  * `name`: (str) Filename.
  * `content`: (bytes) Raw data.

| Returns: `str | None` Persists a file to a Google Cloud bucket or a local path. Returns the final path to the saved file.  
`get_secops_mode()` |  None | Returns: `str | None` Retrieves the `SECOPS_MODE` environment variable, identifying the current platform runtime configuration (such as Cloud versus On-premise).  
  
## User management and profiles

Standardized functions for fetching user metadata and paginating through the platform's user directory.

Function | Parameters | Description & Returns  
---|---|---  
`get_user_by_id()` | 

  * `chronicle_soar`: (ChronicleSOAR) SDK instance.
  * `user_id`: (str) Unique UUID.

| Returns: `UserProfileCard | None` Fetches a specific user's profile card using their platform-wide unique identifier. Returns `None` if not found.  
`get_users_profile_cards_with_pagination()` | 

  * `chronicle_soar`: (ChronicleSOAR)
  * `search_term`: (str)
  * `page_size`: (int) Defaults to `20`.
  * `filter_by_role`: (bool)
  * `filter_disabled_users`: (bool)
  * `filter_support_users`: (bool)
  * `fetch_only_support_users`: (bool)
  * `filter_permission_types`: (list[int])

| Returns: `list[UserProfileCard]` Retrieves user profiles using iterative pagination. This handles the underlying offset logic automatically to prevent memory overhead in large environments.  
`get_soar_case_comments()` | 

  * `chronicle_soar`: (SiemplifyAction | SiemplifyJob)
  * `case_id`: (str | int) Target ID.

| Returns: `list[CaseComment]` Fetches a collection of all comment objects associated with a specific case ID.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
