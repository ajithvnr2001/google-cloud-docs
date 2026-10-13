---
url: https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/reference/password-policy-flags/
title: Password policy flags \u00a0|\u00a0 AlloyDB Omni for containers: 16.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:32.561625+00:00
---

# Password policy flags  |  AlloyDB Omni for containers: 16.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/reference/password-policy-flags/

This page documents AlloyDB Omni version **16.3.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/choose-compatible-versions)



Send feedback 

#  Password policy flags Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.3.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/reference/password-policy-flags)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/reference/password-policy-flags)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/reference/password-policy-flags)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/reference/password-policy-flags)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/reference/password-policy-flags)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/password-policy-flags)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/reference/password-policy-flags)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/reference/password-policy-flags)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/reference/password-policy-flags)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/reference/password-policy-flags)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/reference/password-policy-flags)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/reference/password-policy-flags)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/reference/password-policy-flags)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/reference/password-policy-flags)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/reference/password-policy-flags)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/reference/password-policy-flags)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/reference/password-policy-flags)

This page describes the database flags that AlloyDB Omni uses to enforce a set of restrictions specific to their [password policy](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/manage-password-policy). For a list of all database flags that AlloyDB Omni supports, see [Supported database flags](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/reference/database-flags). 

## `password.enforce_password_does_not_contain_username`

Type| `Boolean`  
---|---  
Default| `OFF`  
Instance restarts| No  
  
If `on`, prohibits using a username as part of a password. This password policy is case sensitive, so if a username is `Alex`, then a password that contains `alex` is allowed.

## `password.enforce_expiration`

Type| `Boolean`  
---|---  
Default| `OFF`  
Instance restarts| No  
  
Manages a lifetime of a password.

## `password.enforce_complexity`

Type| `Boolean`  
---|---  
Default| `OFF`  
Instance restarts| No  
  
Enforces the password complexity policy when new passwords must meet the guidelines specified by other password flags.

## `password.expiration_in_days`

Type| `Integer`  
---|---  
Default| `90`  
Valid values| `0 ... 10000`  
Instance restarts| No  
  
Requires passwords to be changed within the specified number of days.

## `password.min_uppercase_letters`

Type| `Integer`  
---|---  
Default| `0`  
Valid values| `0 ... 10000`  
Instance restarts| No  
  
Sets the minimum number of uppercase letters for a password.

## `password.max_uppercase_letters`

Type| `Integer`  
---|---  
Default| `10000`  
Valid values| `0 ... 10000`  
Instance restarts| No  
  
Sets the maximum number of uppercase letters for a password.

## `password.min_lowercase_letters`

Type| `Integer`  
---|---  
Default| `0`  
Valid values| `0 ... 10000`  
Instance restarts| No  
  
Sets the minimum number of lowercase letters for a password.

## `password.max_lowercase_letters`

Type| `Integer`  
---|---  
Default| `10000`  
Valid values| `0 ... 10000`  
Instance restarts| No  
  
Sets the maximum number of lowercase letters for a password.

## `password.min_numerical_chars`

Type| `Integer`  
---|---  
Default| `0`  
Valid values| `0 ... 10000`  
Instance restarts| No  
  
Sets the minimum number of numerical characters for a password.

## `password.max_numerical_chars`

Type| `Integer`  
---|---  
Default| `10000`  
Valid values| `0 ... 10000`  
Instance restarts| No  
  
Sets the maximum number of numerical characters for a password.

## `password.min_special_chars`

Type| `Integer`  
---|---  
Default| `0`  
Valid values| `0 ... 10000`  
Instance restarts| No  
  
Sets the minimum number of special characters for a password.

## `password.max_special_chars`

Type| `Integer`  
---|---  
Default| `10000`  
Valid values| `0 ... 10000`  
Instance restarts| No  
  
Sets the maximum number of special characters for a password.

## `password.min_pass_length`

Type| `Integer`  
---|---  
Default| `0`  
Valid values| `0 ... 10000`  
Instance restarts| No  
  
Specifies the minimum number of characters allowed in a password.

## `password.max_pass_length`

Type| `Integer`  
---|---  
Default| `10000`  
Valid values| `0 ... 10000`  
Instance restarts| No  
  
Sets the maximum number of characters allowed in a password.

## `password.notify_expiration_in_days`

Type| `Integer`  
---|---  
Default| `30`  
Valid values| `0 ... 10000`  
Instance restarts| No  
  
Sets the number of days when a user starts receiving notifications that their password is about to expire.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
