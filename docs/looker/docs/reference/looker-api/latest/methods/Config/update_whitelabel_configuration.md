---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/update_whitelabel_configuration/
title: Update Private label configuration \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:30.902550+00:00
---

# Update Private label configuration  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/update_whitelabel_configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Update Private label configuration Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Update the private label configuration

This endpoint is deprecated. [Set Setting](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/set_setting) should be used to update private label settings instead

## Request

PUT /whitelabel_configuration 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[WhitelabelConfiguration](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/WhitelabelConfiguration)

Private label configuration

Expand WhitelabelConfiguration definition... 

id

_lock_

string 

Unique Id

logo_file

string 

Customer logo image. Expected base64 encoded data (write-only)

logo_url

_lock_

string 

Logo image url (read-only)

favicon_file

string 

Custom favicon image. Expected base64 encoded data (write-only)

favicon_url

_lock_

string 

Favicon image url (read-only)

default_title

string 

Default page title

show_help_menu

boolean 

Boolean to toggle showing help menus

show_docs

boolean 

Boolean to toggle showing docs

show_email_sub_options

boolean 

Boolean to toggle showing email subscription options.

allow_looker_mentions

boolean 

Boolean to toggle mentions of Looker in emails

allow_looker_links

boolean 

Boolean to toggle links to Looker in emails

custom_welcome_email_advanced

boolean 

Allow subject line and email heading customization in customized emails”

setup_mentions

boolean 

Remove the word Looker from appearing in the account setup page

alerts_logo

boolean 

Remove Looker logo from Alerts

alerts_links

boolean 

Remove Looker links from Alerts

folders_mentions

boolean 

Remove Looker mentions in home folder page when you don’t have any items saved

## Response

### 200: Private label configuration

Datatype

Description

(object)

[WhitelabelConfiguration](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/WhitelabelConfiguration)

id

_lock_

string 

Unique Id

logo_file

string 

Customer logo image. Expected base64 encoded data (write-only)

logo_url

_lock_

string 

Logo image url (read-only)

favicon_file

string 

Custom favicon image. Expected base64 encoded data (write-only)

favicon_url

_lock_

string 

Favicon image url (read-only)

default_title

string 

Default page title

show_help_menu

boolean 

Boolean to toggle showing help menus

show_docs

boolean 

Boolean to toggle showing docs

show_email_sub_options

boolean 

Boolean to toggle showing email subscription options.

allow_looker_mentions

boolean 

Boolean to toggle mentions of Looker in emails

allow_looker_links

boolean 

Boolean to toggle links to Looker in emails

custom_welcome_email_advanced

boolean 

Allow subject line and email heading customization in customized emails”

setup_mentions

boolean 

Remove the word Looker from appearing in the account setup page

alerts_logo

boolean 

Remove Looker logo from Alerts

alerts_links

boolean 

Remove Looker links from Alerts

folders_mentions

boolean 

Remove Looker mentions in home folder page when you don’t have any items saved

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
