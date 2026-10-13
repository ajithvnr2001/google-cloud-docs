---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Application (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:09.970815+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Application (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Application (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::Application.

An Application resource contains the top-level configuration of an App Engine application.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #auth_domain
    
    
    def auth_domain() -> ::String

**Returns**

  * (::String) — Google Apps authentication domain that controls which users can access this application.

Defaults to open access for any Google Account. 




### #auth_domain=
    
    
    def auth_domain=(value) -> ::String

**Parameter**

  * **value** (::String) — Google Apps authentication domain that controls which users can access this application.

Defaults to open access for any Google Account. 




**Returns**

  * (::String) — Google Apps authentication domain that controls which users can access this application.

Defaults to open access for any Google Account. 




### #code_bucket
    
    
    def code_bucket() -> ::String

**Returns**

  * (::String) — Google Cloud Storage bucket that can be used for storing files associated with this application. This bucket is associated with the application and can be used by the gcloud deployment commands. 



### #code_bucket=
    
    
    def code_bucket=(value) -> ::String

**Parameter**

  * **value** (::String) — Google Cloud Storage bucket that can be used for storing files associated with this application. This bucket is associated with the application and can be used by the gcloud deployment commands. 



**Returns**

  * (::String) — Google Cloud Storage bucket that can be used for storing files associated with this application. This bucket is associated with the application and can be used by the gcloud deployment commands. 



### #database_type
    
    
    def database_type() -> ::Google::Cloud::AppEngine::V1::Application::DatabaseType

**Returns**

  * ([::Google::Cloud::AppEngine::V1::Application::DatabaseType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application-DatabaseType)) — The type of the Cloud Firestore or Cloud Datastore database associated with this application. 



### #database_type=
    
    
    def database_type=(value) -> ::Google::Cloud::AppEngine::V1::Application::DatabaseType

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::Application::DatabaseType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application-DatabaseType)) — The type of the Cloud Firestore or Cloud Datastore database associated with this application. 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::Application::DatabaseType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application-DatabaseType)) — The type of the Cloud Firestore or Cloud Datastore database associated with this application. 



### #default_bucket
    
    
    def default_bucket() -> ::String

**Returns**

  * (::String) — Google Cloud Storage bucket that can be used by this application to store content. 



### #default_bucket=
    
    
    def default_bucket=(value) -> ::String

**Parameter**

  * **value** (::String) — Google Cloud Storage bucket that can be used by this application to store content. 



**Returns**

  * (::String) — Google Cloud Storage bucket that can be used by this application to store content. 



### #default_cookie_expiration
    
    
    def default_cookie_expiration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Cookie expiration policy for this application. 



### #default_cookie_expiration=
    
    
    def default_cookie_expiration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Cookie expiration policy for this application. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Duration)) — Cookie expiration policy for this application. 



### #default_hostname
    
    
    def default_hostname() -> ::String

**Returns**

  * (::String) — Hostname used to reach this application, as resolved by App Engine. 



### #default_hostname=
    
    
    def default_hostname=(value) -> ::String

**Parameter**

  * **value** (::String) — Hostname used to reach this application, as resolved by App Engine. 



**Returns**

  * (::String) — Hostname used to reach this application, as resolved by App Engine. 



### #dispatch_rules
    
    
    def dispatch_rules() -> ::Array<::Google::Cloud::AppEngine::V1::UrlDispatchRule>

**Returns**

  * (::Array<[::Google::Cloud::AppEngine::V1::UrlDispatchRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-UrlDispatchRule)>) — HTTP path dispatch rules for requests to the application that do not explicitly target a service or version. Rules are order-dependent. Up to 20 dispatch rules can be supported. 



### #dispatch_rules=
    
    
    def dispatch_rules=(value) -> ::Array<::Google::Cloud::AppEngine::V1::UrlDispatchRule>

**Parameter**

  * **value** (::Array<[::Google::Cloud::AppEngine::V1::UrlDispatchRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-UrlDispatchRule)>) — HTTP path dispatch rules for requests to the application that do not explicitly target a service or version. Rules are order-dependent. Up to 20 dispatch rules can be supported. 



**Returns**

  * (::Array<[::Google::Cloud::AppEngine::V1::UrlDispatchRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-UrlDispatchRule)>) — HTTP path dispatch rules for requests to the application that do not explicitly target a service or version. Rules are order-dependent. Up to 20 dispatch rules can be supported. 



### #feature_settings
    
    
    def feature_settings() -> ::Google::Cloud::AppEngine::V1::Application::FeatureSettings

**Returns**

  * ([::Google::Cloud::AppEngine::V1::Application::FeatureSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application-FeatureSettings)) — The feature specific settings to be used in the application. 



### #feature_settings=
    
    
    def feature_settings=(value) -> ::Google::Cloud::AppEngine::V1::Application::FeatureSettings

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::Application::FeatureSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application-FeatureSettings)) — The feature specific settings to be used in the application. 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::Application::FeatureSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application-FeatureSettings)) — The feature specific settings to be used in the application. 



### #gcr_domain
    
    
    def gcr_domain() -> ::String

**Returns**

  * (::String) — The Google Container Registry domain used for storing managed build docker images for this application. 



### #gcr_domain=
    
    
    def gcr_domain=(value) -> ::String

**Parameter**

  * **value** (::String) — The Google Container Registry domain used for storing managed build docker images for this application. 



**Returns**

  * (::String) — The Google Container Registry domain used for storing managed build docker images for this application. 



### #iap
    
    
    def iap() -> ::Google::Cloud::AppEngine::V1::Application::IdentityAwareProxy

**Returns**

  * ([::Google::Cloud::AppEngine::V1::Application::IdentityAwareProxy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application-IdentityAwareProxy)) 



### #iap=
    
    
    def iap=(value) -> ::Google::Cloud::AppEngine::V1::Application::IdentityAwareProxy

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::Application::IdentityAwareProxy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application-IdentityAwareProxy)) 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::Application::IdentityAwareProxy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application-IdentityAwareProxy)) 



### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Identifier of the Application resource. This identifier is equivalent to the project ID of the Google Cloud Platform project where you want to deploy your application. Example: `myapp`. 



### #id=
    
    
    def id=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier of the Application resource. This identifier is equivalent to the project ID of the Google Cloud Platform project where you want to deploy your application. Example: `myapp`. 



**Returns**

  * (::String) — Identifier of the Application resource. This identifier is equivalent to the project ID of the Google Cloud Platform project where you want to deploy your application. Example: `myapp`. 



### #location_id
    
    
    def location_id() -> ::String

**Returns**

  * (::String) — Location from which this application runs. Application instances run out of the data centers in the specified location, which is also where all of the application's end user content is stored.

Defaults to `us-central`.

View the list of [supported locations](https://cloud.google.com/appengine/docs/locations). 




### #location_id=
    
    
    def location_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Location from which this application runs. Application instances run out of the data centers in the specified location, which is also where all of the application's end user content is stored.

Defaults to `us-central`.

View the list of [supported locations](https://cloud.google.com/appengine/docs/locations). 




**Returns**

  * (::String) — Location from which this application runs. Application instances run out of the data centers in the specified location, which is also where all of the application's end user content is stored.

Defaults to `us-central`.

View the list of [supported locations](https://cloud.google.com/appengine/docs/locations). 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Full path to the Application resource in the API. Example: `apps/myapp`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Full path to the Application resource in the API. Example: `apps/myapp`. 



**Returns**

  * (::String) — Full path to the Application resource in the API. Example: `apps/myapp`. 



### #service_account
    
    
    def service_account() -> ::String

**Returns**

  * (::String) — The service account associated with the application. This is the app-level default identity. If no identity provided during create version, Admin API will fallback to this one. 



### #service_account=
    
    
    def service_account=(value) -> ::String

**Parameter**

  * **value** (::String) — The service account associated with the application. This is the app-level default identity. If no identity provided during create version, Admin API will fallback to this one. 



**Returns**

  * (::String) — The service account associated with the application. This is the app-level default identity. If no identity provided during create version, Admin API will fallback to this one. 



### #serving_status
    
    
    def serving_status() -> ::Google::Cloud::AppEngine::V1::Application::ServingStatus

**Returns**

  * ([::Google::Cloud::AppEngine::V1::Application::ServingStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application-ServingStatus)) — Serving status of this application. 



### #serving_status=
    
    
    def serving_status=(value) -> ::Google::Cloud::AppEngine::V1::Application::ServingStatus

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::Application::ServingStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application-ServingStatus)) — Serving status of this application. 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::Application::ServingStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application-ServingStatus)) — Serving status of this application. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
