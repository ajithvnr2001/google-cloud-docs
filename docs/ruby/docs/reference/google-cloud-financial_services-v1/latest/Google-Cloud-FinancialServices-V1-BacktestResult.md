---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BacktestResult/
title: Financial Services V1 API - Class Google::Cloud::FinancialServices::V1::BacktestResult (v1.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:18.886818+00:00
---

# Financial Services V1 API - Class Google::Cloud::FinancialServices::V1::BacktestResult (v1.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BacktestResult/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Financial Services V1 API - Class Google::Cloud::FinancialServices::V1::BacktestResult (v1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  0.7.0  0.6.1  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Financial Services V1 API class Google::Cloud::FinancialServices::V1::BacktestResult.

BacktestResult is created to test the performance of a model on a dataset.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #backtest_periods
    
    
    def backtest_periods() -> ::Integer

**Returns**

  * (::Integer) — The number of consecutive months to conduct backtesting for, ending with the last full month prior to the end_time according to the dataset's timezone. 



### #backtest_periods=
    
    
    def backtest_periods=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The number of consecutive months to conduct backtesting for, ending with the last full month prior to the end_time according to the dataset's timezone. 



**Returns**

  * (::Integer) — The number of consecutive months to conduct backtesting for, ending with the last full month prior to the end_time according to the dataset's timezone. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp of creation of this resource. 



### #dataset
    
    
    def dataset() -> ::String

**Returns**

  * (::String) — Required. The resource name of the Dataset to backtest on Format: `/projects/{project_num}/locations/{location}/instances/{instance}/datasets/{dataset}`



### #dataset=
    
    
    def dataset=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the Dataset to backtest on Format: `/projects/{project_num}/locations/{location}/instances/{instance}/datasets/{dataset}`



**Returns**

  * (::String) — Required. The resource name of the Dataset to backtest on Format: `/projects/{project_num}/locations/{location}/instances/{instance}/datasets/{dataset}`



### #end_time
    
    
    def end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Protobuf-Timestamp)) — Required. End_time specifies the latest time from which labels are used and from which data is used to generate features for backtesting. End_time should be no later than the end of the date_range of the primary dataset. 



### #end_time=
    
    
    def end_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Protobuf-Timestamp)) — Required. End_time specifies the latest time from which labels are used and from which data is used to generate features for backtesting. End_time should be no later than the end of the date_range of the primary dataset. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Protobuf-Timestamp)) — Required. End_time specifies the latest time from which labels are used and from which data is used to generate features for backtesting. End_time should be no later than the end of the date_range of the primary dataset. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels 



### #line_of_business
    
    
    def line_of_business() -> ::Google::Cloud::FinancialServices::V1::LineOfBusiness

**Returns**

  * ([::Google::Cloud::FinancialServices::V1::LineOfBusiness](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-LineOfBusiness)) — Output only. The line of business (Retail/Commercial) this backtest is for. Determined by Model, cannot be set by user. 



### #model
    
    
    def model() -> ::String

**Returns**

  * (::String) — Required. The resource name of the Model to use or to backtest. Format: `/projects/{project_num}/locations/{location}/instances/{instance}/models/{model}`



### #model=
    
    
    def model=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the Model to use or to backtest. Format: `/projects/{project_num}/locations/{location}/instances/{instance}/models/{model}`



**Returns**

  * (::String) — Required. The resource name of the Model to use or to backtest. Format: `/projects/{project_num}/locations/{location}/instances/{instance}/models/{model}`



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The resource name of the BacktestResult. format: `/projects/{project_num}/locations/{location}/instances/{instance}/backtestResults/{backtest_result}`



### #performance_target
    
    
    def performance_target() -> ::Google::Cloud::FinancialServices::V1::BacktestResult::PerformanceTarget

**Returns**

  * ([::Google::Cloud::FinancialServices::V1::BacktestResult::PerformanceTarget](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BacktestResult-PerformanceTarget)) — Required. PerformanceTarget gives information on how the test will be evaluated. 



### #performance_target=
    
    
    def performance_target=(value) -> ::Google::Cloud::FinancialServices::V1::BacktestResult::PerformanceTarget

**Parameter**

  * **value** ([::Google::Cloud::FinancialServices::V1::BacktestResult::PerformanceTarget](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BacktestResult-PerformanceTarget)) — Required. PerformanceTarget gives information on how the test will be evaluated. 



**Returns**

  * ([::Google::Cloud::FinancialServices::V1::BacktestResult::PerformanceTarget](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BacktestResult-PerformanceTarget)) — Required. PerformanceTarget gives information on how the test will be evaluated. 



### #state
    
    
    def state() -> ::Google::Cloud::FinancialServices::V1::BacktestResult::State

**Returns**

  * ([::Google::Cloud::FinancialServices::V1::BacktestResult::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Cloud-FinancialServices-V1-BacktestResult-State)) — Output only. State of the BacktestResult (creating, active, deleting, etc.) 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-financial_services-v1/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp of the most recent update of this resource. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
