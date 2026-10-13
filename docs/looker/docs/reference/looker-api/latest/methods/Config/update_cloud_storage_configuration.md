---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/update_cloud_storage_configuration/
title: Update Cloud Storage \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:10.601689+00:00
---

# Update Cloud Storage  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/update_cloud_storage_configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Update Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

Update the current Cloud Storage Configuration.

## Request

PATCH /cloud_storage 

Datatype

Description

Request

HTTP Request 

body

HTTP Body 

Expand HTTP Body definition... 

body

[BackupConfiguration](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/BackupConfiguration)

Options for Cloud Storage Configuration

Expand BackupConfiguration definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

type

string 

Type of backup: looker-s3 or custom-s3

custom_s3_bucket

string 

Name of bucket for custom-s3 backups

custom_s3_bucket_region

string 

Name of region where the bucket is located

custom_s3_key

string 

(Write-Only) AWS S3 key used for custom-s3 backups

custom_s3_secret

string 

(Write-Only) AWS S3 secret used for custom-s3 backups

url

_lock_

string 

Link to get this item

## Response

### 200: New state for specified model set.

Datatype

Description

(object)

[BackupConfiguration](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/BackupConfiguration)

can

_lock_

object 

Operations the current user is able to perform on this object

type

string 

Type of backup: looker-s3 or custom-s3

custom_s3_bucket

string 

Name of bucket for custom-s3 backups

custom_s3_bucket_region

string 

Name of region where the bucket is located

custom_s3_key

string 

(Write-Only) AWS S3 key used for custom-s3 backups

custom_s3_secret

string 

(Write-Only) AWS S3 secret used for custom-s3 backups

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
