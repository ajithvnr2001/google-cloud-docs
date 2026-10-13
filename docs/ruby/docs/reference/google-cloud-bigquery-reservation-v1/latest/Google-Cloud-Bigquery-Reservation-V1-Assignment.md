---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment/
title: BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::Assignment (v1.14.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:18.129907+00:00
---

# BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::Assignment (v1.14.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::Assignment (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.1  1.12.1  1.11.0  1.10.0  1.9.2  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.12.0  0.11.2  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.2 

Reference documentation and code samples for the BigQuery Reservation V1 API class Google::Cloud::Bigquery::Reservation::V1::Assignment.

An assignment allows a project to submit jobs of a certain type using slots from the specified reservation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #assignee
    
    
    def assignee() -> ::String

**Returns**

  * (::String) — Optional. The resource which will use the reservation. E.g. `projects/myproject`, `folders/123`, or `organizations/456`. 



### #assignee=
    
    
    def assignee=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The resource which will use the reservation. E.g. `projects/myproject`, `folders/123`, or `organizations/456`. 



**Returns**

  * (::String) — Optional. The resource which will use the reservation. E.g. `projects/myproject`, `folders/123`, or `organizations/456`. 



### #condition
    
    
    def condition() -> ::Google::Type::Expr

**Returns**

  * ([::Google::Type::Expr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Type-Expr)) — Optional. Common Expression Language (CEL) condition that defines the matching criteria for this assignment. The condition must resolve to a boolean value. Supported variables will be added later. 



### #condition=
    
    
    def condition=(value) -> ::Google::Type::Expr

**Parameter**

  * **value** ([::Google::Type::Expr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Type-Expr)) — Optional. Common Expression Language (CEL) condition that defines the matching criteria for this assignment. The condition must resolve to a boolean value. Supported variables will be added later. 



**Returns**

  * ([::Google::Type::Expr](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Type-Expr)) — Optional. Common Expression Language (CEL) condition that defines the matching criteria for this assignment. The condition must resolve to a boolean value. Supported variables will be added later. 



### #enable_gemini_in_bigquery
    
    
    def enable_gemini_in_bigquery() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Deprecated: "Gemini in BigQuery" is now available by default for all BigQuery editions and should not be explicitly set. Controls if "Gemini in BigQuery" (https://cloud.google.com/gemini/docs/bigquery/overview) features should be enabled for this reservation assignment. 



### #enable_gemini_in_bigquery=
    
    
    def enable_gemini_in_bigquery=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Deprecated: "Gemini in BigQuery" is now available by default for all BigQuery editions and should not be explicitly set. Controls if "Gemini in BigQuery" (https://cloud.google.com/gemini/docs/bigquery/overview) features should be enabled for this reservation assignment. 



**Returns**

  * (::Boolean) — Optional. Deprecated: "Gemini in BigQuery" is now available by default for all BigQuery editions and should not be explicitly set. Controls if "Gemini in BigQuery" (https://cloud.google.com/gemini/docs/bigquery/overview) features should be enabled for this reservation assignment. 



### #job_type
    
    
    def job_type() -> ::Google::Cloud::Bigquery::Reservation::V1::Assignment::JobType

**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Assignment::JobType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment-JobType)) — Optional. Which type of jobs will use the reservation. 



### #job_type=
    
    
    def job_type=(value) -> ::Google::Cloud::Bigquery::Reservation::V1::Assignment::JobType

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Reservation::V1::Assignment::JobType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment-JobType)) — Optional. Which type of jobs will use the reservation. 



**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Assignment::JobType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment-JobType)) — Optional. Which type of jobs will use the reservation. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Name of the resource. E.g.: `projects/myproject/locations/US/reservations/team1-prod/assignments/123`. The assignment_id must only contain lower case alphanumeric characters or dashes and the max length is 64 characters. 



### #precedence
    
    
    def precedence() -> ::Integer

**Returns**

  * (::Integer) — Optional. Specifies the priority precedence for this assignment. Used to resolve ambiguity when multiple assignments match a single job. Higher numerical values represent higher priority (e.g., 20 is higher than 10). If unspecified, it defaults to 0. Multiple assignments can share the same precedence, but it is recommended to use unique precedence values for assignments within the same assignee scope. 



### #precedence=
    
    
    def precedence=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Specifies the priority precedence for this assignment. Used to resolve ambiguity when multiple assignments match a single job. Higher numerical values represent higher priority (e.g., 20 is higher than 10). If unspecified, it defaults to 0. Multiple assignments can share the same precedence, but it is recommended to use unique precedence values for assignments within the same assignee scope. 



**Returns**

  * (::Integer) — Optional. Specifies the priority precedence for this assignment. Used to resolve ambiguity when multiple assignments match a single job. Higher numerical values represent higher priority (e.g., 20 is higher than 10). If unspecified, it defaults to 0. Multiple assignments can share the same precedence, but it is recommended to use unique precedence values for assignments within the same assignee scope. 



### #principal
    
    
    def principal() -> ::String

**Returns**

  * (::String) — 

Optional. Represents the principal for this assignment. If not empty, jobs run by this principal utilize the associated reservation. Otherwise, jobs fall back to using the reservation assigned to the project, folder, or organization, in that order. If no reservation is assigned at any of these levels, on-demand capacity is used.

The supported formats are:

    * `principal://goog/subject/USER_EMAIL_ADDRESS` for users,
    * `principal://iam.googleapis.com/projects/-/serviceAccounts/SA_EMAIL_ADDRESS` for service accounts,
    * `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT_ID` for workload identity pool identities.
    * The special value `unknown_or_deleted_user` represents principals which cannot be read from the user info service, for example, deleted users.



### #principal=
    
    
    def principal=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. Represents the principal for this assignment. If not empty, jobs run by this principal utilize the associated reservation. Otherwise, jobs fall back to using the reservation assigned to the project, folder, or organization, in that order. If no reservation is assigned at any of these levels, on-demand capacity is used.

The supported formats are:

    * `principal://goog/subject/USER_EMAIL_ADDRESS` for users,
    * `principal://iam.googleapis.com/projects/-/serviceAccounts/SA_EMAIL_ADDRESS` for service accounts,
    * `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT_ID` for workload identity pool identities.
    * The special value `unknown_or_deleted_user` represents principals which cannot be read from the user info service, for example, deleted users.



**Returns**

  * (::String) — 

Optional. Represents the principal for this assignment. If not empty, jobs run by this principal utilize the associated reservation. Otherwise, jobs fall back to using the reservation assigned to the project, folder, or organization, in that order. If no reservation is assigned at any of these levels, on-demand capacity is used.

The supported formats are:

    * `principal://goog/subject/USER_EMAIL_ADDRESS` for users,
    * `principal://iam.googleapis.com/projects/-/serviceAccounts/SA_EMAIL_ADDRESS` for service accounts,
    * `principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT_ID` for workload identity pool identities.
    * The special value `unknown_or_deleted_user` represents principals which cannot be read from the user info service, for example, deleted users.



### #scheduling_policy
    
    
    def scheduling_policy() -> ::Google::Cloud::Bigquery::Reservation::V1::SchedulingPolicy

**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::SchedulingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SchedulingPolicy)) — Optional. The scheduling policy to use for jobs and queries of this assignee when running under the associated reservation. The scheduling policy controls how the reservation's resources are distributed. This overrides the default scheduling policy specified on the reservation.

This feature is not yet generally available. 




### #scheduling_policy=
    
    
    def scheduling_policy=(value) -> ::Google::Cloud::Bigquery::Reservation::V1::SchedulingPolicy

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Reservation::V1::SchedulingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SchedulingPolicy)) — Optional. The scheduling policy to use for jobs and queries of this assignee when running under the associated reservation. The scheduling policy controls how the reservation's resources are distributed. This overrides the default scheduling policy specified on the reservation.

This feature is not yet generally available. 




**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::SchedulingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SchedulingPolicy)) — Optional. The scheduling policy to use for jobs and queries of this assignee when running under the associated reservation. The scheduling policy controls how the reservation's resources are distributed. This overrides the default scheduling policy specified on the reservation.

This feature is not yet generally available. 




### #state
    
    
    def state() -> ::Google::Cloud::Bigquery::Reservation::V1::Assignment::State

**Returns**

  * ([::Google::Cloud::Bigquery::Reservation::V1::Assignment::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-Assignment-State)) — Output only. State of the assignment. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
