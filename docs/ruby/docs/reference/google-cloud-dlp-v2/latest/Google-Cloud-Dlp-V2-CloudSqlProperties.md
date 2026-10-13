---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-CloudSqlProperties/
title: Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::CloudSqlProperties (v1.19.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:04:50.334772+00:00
---

# Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::CloudSqlProperties (v1.19.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-CloudSqlProperties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Data Loss Prevention (DLP) V2 API - Class Google::Cloud::Dlp::V2::CloudSqlProperties (v1.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.0 (latest)  1.18.1  1.17.0  1.16.1  1.15.2  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.2  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1 

Reference documentation and code samples for the Cloud Data Loss Prevention (DLP) V2 API class Google::Cloud::Dlp::V2::CloudSqlProperties.

Cloud SQL connection properties.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cloud_sql_iam
    
    
    def cloud_sql_iam() -> ::Google::Cloud::Dlp::V2::CloudSqlIamCredential

**Returns**

  * ([::Google::Cloud::Dlp::V2::CloudSqlIamCredential](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-CloudSqlIamCredential)) — Built-in IAM authentication (must be configured in Cloud SQL).

Note: The following fields are mutually exclusive: `cloud_sql_iam`, `username_password`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cloud_sql_iam=
    
    
    def cloud_sql_iam=(value) -> ::Google::Cloud::Dlp::V2::CloudSqlIamCredential

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::CloudSqlIamCredential](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-CloudSqlIamCredential)) — Built-in IAM authentication (must be configured in Cloud SQL).

Note: The following fields are mutually exclusive: `cloud_sql_iam`, `username_password`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dlp::V2::CloudSqlIamCredential](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-CloudSqlIamCredential)) — Built-in IAM authentication (must be configured in Cloud SQL).

Note: The following fields are mutually exclusive: `cloud_sql_iam`, `username_password`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #connection_name
    
    
    def connection_name() -> ::String

**Returns**

  * (::String) — Optional. Immutable. The Cloud SQL instance for which the connection is defined. Only one connection per instance is allowed. This can only be set at creation time, and cannot be updated.

It is an error to use a connection_name from different project or region than the one that holds the connection. For example, a Connection resource for Cloud SQL connection_name `project-id:us-central1:sql-instance` must be created under the parent `projects/project-id/locations/us-central1`




### #connection_name=
    
    
    def connection_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Immutable. The Cloud SQL instance for which the connection is defined. Only one connection per instance is allowed. This can only be set at creation time, and cannot be updated.

It is an error to use a connection_name from different project or region than the one that holds the connection. For example, a Connection resource for Cloud SQL connection_name `project-id:us-central1:sql-instance` must be created under the parent `projects/project-id/locations/us-central1`




**Returns**

  * (::String) — Optional. Immutable. The Cloud SQL instance for which the connection is defined. Only one connection per instance is allowed. This can only be set at creation time, and cannot be updated.

It is an error to use a connection_name from different project or region than the one that holds the connection. For example, a Connection resource for Cloud SQL connection_name `project-id:us-central1:sql-instance` must be created under the parent `projects/project-id/locations/us-central1`




### #database_engine
    
    
    def database_engine() -> ::Google::Cloud::Dlp::V2::CloudSqlProperties::DatabaseEngine

**Returns**

  * ([::Google::Cloud::Dlp::V2::CloudSqlProperties::DatabaseEngine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-CloudSqlProperties-DatabaseEngine)) — Required. The database engine used by the Cloud SQL instance that this connection configures. 



### #database_engine=
    
    
    def database_engine=(value) -> ::Google::Cloud::Dlp::V2::CloudSqlProperties::DatabaseEngine

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::CloudSqlProperties::DatabaseEngine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-CloudSqlProperties-DatabaseEngine)) — Required. The database engine used by the Cloud SQL instance that this connection configures. 



**Returns**

  * ([::Google::Cloud::Dlp::V2::CloudSqlProperties::DatabaseEngine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-CloudSqlProperties-DatabaseEngine)) — Required. The database engine used by the Cloud SQL instance that this connection configures. 



### #max_connections
    
    
    def max_connections() -> ::Integer

**Returns**

  * (::Integer) — Required. The DLP API will limit its connections to max_connections. Must be 2 or greater. 



### #max_connections=
    
    
    def max_connections=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Required. The DLP API will limit its connections to max_connections. Must be 2 or greater. 



**Returns**

  * (::Integer) — Required. The DLP API will limit its connections to max_connections. Must be 2 or greater. 



### #username_password
    
    
    def username_password() -> ::Google::Cloud::Dlp::V2::SecretManagerCredential

**Returns**

  * ([::Google::Cloud::Dlp::V2::SecretManagerCredential](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-SecretManagerCredential)) — A username and password stored in Secret Manager.

Note: The following fields are mutually exclusive: `username_password`, `cloud_sql_iam`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #username_password=
    
    
    def username_password=(value) -> ::Google::Cloud::Dlp::V2::SecretManagerCredential

**Parameter**

  * **value** ([::Google::Cloud::Dlp::V2::SecretManagerCredential](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-SecretManagerCredential)) — A username and password stored in Secret Manager.

Note: The following fields are mutually exclusive: `username_password`, `cloud_sql_iam`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dlp::V2::SecretManagerCredential](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dlp-v2/latest/Google-Cloud-Dlp-V2-SecretManagerCredential)) — A username and password stored in Secret Manager.

Note: The following fields are mutually exclusive: `username_password`, `cloud_sql_iam`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
