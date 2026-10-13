---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ImportAppRequest/
title: Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::ImportAppRequest (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:36.293222+00:00
---

# Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::ImportAppRequest (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ImportAppRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience V1BETA API - Class Google::Cloud::Ces::V1beta::ImportAppRequest (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Gemini Enterprise for Customer Experience V1BETA API class Google::Cloud::Ces::V1beta::ImportAppRequest.

Request message for [AgentService.ImportApp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-AgentService-Client#Google__Cloud__Ces__V1beta__AgentService__Client_import_app_instance_ "Google::Cloud::Ces::V1beta::AgentService::Client#import_app \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #app_content
    
    
    def app_content() -> ::String

**Returns**

  * (::String) — Raw bytes representing the compressed zip file with the app folder structure.

Note: The following fields are mutually exclusive: `app_content`, `gcs_uri`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #app_content=
    
    
    def app_content=(value) -> ::String

**Parameter**

  * **value** (::String) — Raw bytes representing the compressed zip file with the app folder structure.

Note: The following fields are mutually exclusive: `app_content`, `gcs_uri`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Raw bytes representing the compressed zip file with the app folder structure.

Note: The following fields are mutually exclusive: `app_content`, `gcs_uri`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #app_id
    
    
    def app_id() -> ::String

**Returns**

  * (::String) — 

Optional. The ID to use for the imported app.

    * If not specified, a unique ID will be automatically assigned for the app.
    * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced.



### #app_id=
    
    
    def app_id=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. The ID to use for the imported app.

    * If not specified, a unique ID will be automatically assigned for the app.
    * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced.



**Returns**

  * (::String) — 

Optional. The ID to use for the imported app.

    * If not specified, a unique ID will be automatically assigned for the app.
    * Otherwise, the imported app will use this ID as the final component of its resource name. If an app with the same ID already exists at the specified location in the project, the content of the existing app will be replaced.



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — 

Optional. The display name of the app to import.

    * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique.
    * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error.



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. The display name of the app to import.

    * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique.
    * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error.



**Returns**

  * (::String) — 

Optional. The display name of the app to import.

    * If the app is created on import, and the display name is specified, the imported app will use this display name. If a conflict is detected with an existing app, a timestamp will be appended to the display name to make it unique.
    * If the app is a reimport, this field should not be set. Providing a display name during reimport will result in an INVALID_ARGUMENT error.



### #gcs_uri
    
    
    def gcs_uri() -> ::String

**Returns**

  * (::String) — The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI from which to import app. The format of this URI must be `gs://<bucket-name>/<object-name>`.

Note: The following fields are mutually exclusive: `gcs_uri`, `app_content`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_uri=
    
    
    def gcs_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI from which to import app. The format of this URI must be `gs://<bucket-name>/<object-name>`.

Note: The following fields are mutually exclusive: `gcs_uri`, `app_content`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The [Google Cloud Storage](https://cloud.google.com/storage/docs/) URI from which to import app. The format of this URI must be `gs://<bucket-name>/<object-name>`.

Note: The following fields are mutually exclusive: `gcs_uri`, `app_content`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #ignore_app_lock
    
    
    def ignore_app_lock() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Flag for overriding the app lock during import. If set to true, the import process will ignore the app lock. 



### #ignore_app_lock=
    
    
    def ignore_app_lock=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Flag for overriding the app lock during import. If set to true, the import process will ignore the app lock. 



**Returns**

  * (::Boolean) — Optional. Flag for overriding the app lock during import. If set to true, the import process will ignore the app lock. 



### #import_options
    
    
    def import_options() -> ::Google::Cloud::Ces::V1beta::ImportAppRequest::ImportOptions

**Returns**

  * ([::Google::Cloud::Ces::V1beta::ImportAppRequest::ImportOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ImportAppRequest-ImportOptions)) — Optional. Options governing the import process for the app. 



### #import_options=
    
    
    def import_options=(value) -> ::Google::Cloud::Ces::V1beta::ImportAppRequest::ImportOptions

**Parameter**

  * **value** ([::Google::Cloud::Ces::V1beta::ImportAppRequest::ImportOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ImportAppRequest-ImportOptions)) — Optional. Options governing the import process for the app. 



**Returns**

  * ([::Google::Cloud::Ces::V1beta::ImportAppRequest::ImportOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ces-v1beta/latest/Google-Cloud-Ces-V1beta-ImportAppRequest-ImportOptions)) — Optional. Options governing the import process for the app. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent resource name with the location of the app to import. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent resource name with the location of the app to import. 



**Returns**

  * (::String) — Required. The parent resource name with the location of the app to import. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
