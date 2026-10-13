---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictionService-Rest-Client/
title: Retail V2 API - Class Google::Cloud::Retail::V2::PredictionService::Rest::Client (v2.10.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:05.964123+00:00
---

# Retail V2 API - Class Google::Cloud::Retail::V2::PredictionService::Rest::Client (v2.10.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictionService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Retail V2 API - Class Google::Cloud::Retail::V2::PredictionService::Rest::Client (v2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.0 (latest)  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.3.0  1.2.0  1.1.0  1.0.1  0.21.0  0.20.0  0.19.0  0.18.2  0.17.0  0.16.1  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4 

Reference documentation and code samples for the Retail V2 API class Google::Cloud::Retail::V2::PredictionService::Rest::Client.

REST client for the PredictionService service.

Service for making recommendation prediction.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Retail::V2::PredictionService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictionService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the PredictionService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictionService-Rest-Client-Configuration "Google::Cloud::Retail::V2::PredictionService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictionService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictionService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all PredictionService clients
    ::Google::Cloud::Retail::V2::PredictionService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the PredictionService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictionService-Rest-Client#Google__Cloud__Retail__V2__PredictionService__Rest__Client_configure_class_ "Google::Cloud::Retail::V2::PredictionService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictionService-Rest-Client-Configuration "Google::Cloud::Retail::V2::PredictionService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictionService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictionService-Rest-Client-Configuration)) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new PredictionService REST client object.

**Yields**

  * (config) — Configure the PredictionService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictionService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictionService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Retail::V2::PredictionService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Retail::V2::PredictionService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #location_client
    
    
    def location_client() -> Google::Cloud::Location::Locations::Rest::Client

Get the associated client for mix-in of the Locations.

**Returns**

  * (Google::Cloud::Location::Locations::Rest::Client) 



### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #predict
    
    
    def predict(request, options = nil) -> ::Google::Cloud::Retail::V2::PredictResponse
    def predict(placement: nil, user_event: nil, page_size: nil, page_token: nil, filter: nil, validate_only: nil, params: nil, labels: nil) -> ::Google::Cloud::Retail::V2::PredictResponse

Makes a recommendation prediction.

**Overloads**
    
    
    def predict(request, options = nil) -> ::Google::Cloud::Retail::V2::PredictResponse

Pass arguments to `predict` via a request object, either of type [Google::Cloud::Retail::V2::PredictRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictRequest "Google::Cloud::Retail::V2::PredictRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Retail::V2::PredictRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def predict(placement: nil, user_event: nil, page_size: nil, page_token: nil, filter: nil, validate_only: nil, params: nil, labels: nil) -> ::Google::Cloud::Retail::V2::PredictResponse

Pass arguments to `predict` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **placement** (::String) — Required. Full resource name of the format: `{placement=projects/*/locations/global/catalogs/default_catalog/servingConfigs/*}` or `{placement=projects/*/locations/global/catalogs/default_catalog/placements/*}`. We recommend using the `servingConfigs` resource. `placements` is a legacy resource. The ID of the Recommendations AI serving config or placement. Before you can request predictions from your model, you must create at least one serving config or placement for it. For more information, see [Manage serving configs](https://cloud.google.com/retail/docs/manage-configs).

The full list of available serving configs can be seen at https://console.cloud.google.com/ai/retail/catalogs/default_catalog/configs 

  * **user_event** ([::Google::Cloud::Retail::V2::UserEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-UserEvent), ::Hash) — Required. Context about the user, what they are looking at and what action they took to trigger the predict request. Note that this user event detail won't be ingested to userEvent logs. Thus, a separate userEvent write request is required for event logging.

Don't set [UserEvent.visitor_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-UserEvent#Google__Cloud__Retail__V2__UserEvent_visitor_id_instance_ "Google::Cloud::Retail::V2::UserEvent#visitor_id \(method\)") or [UserInfo.user_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-UserInfo#Google__Cloud__Retail__V2__UserInfo_user_id_instance_ "Google::Cloud::Retail::V2::UserInfo#user_id \(method\)") to the same fixed ID for different users. If you are trying to receive non-personalized recommendations (not recommended; this can negatively impact model performance), instead set [UserEvent.visitor_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-UserEvent#Google__Cloud__Retail__V2__UserEvent_visitor_id_instance_ "Google::Cloud::Retail::V2::UserEvent#visitor_id \(method\)") to a random unique ID and leave [UserInfo.user_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-UserInfo#Google__Cloud__Retail__V2__UserInfo_user_id_instance_ "Google::Cloud::Retail::V2::UserInfo#user_id \(method\)") unset. 

  * **page_size** (::Integer) — Maximum number of results to return. Set this property to the number of prediction results needed. If zero, the service will choose a reasonable default. The maximum allowed value is 100. Values above 100 will be coerced to 100. 
  * **page_token** (::String) — This field is not used; leave it unset. 
  * **filter** (::String) — Filter for restricting prediction results with a length limit of 5,000 characters. Accepts values for tags and the `filterOutOfStockItems` flag.

    * Tag expressions. Restricts predictions to products that match all of the specified tags. Boolean operators `OR` and `NOT` are supported if the expression is enclosed in parentheses, and must be separated from the tag values by a space. `-"tagA"` is also supported and is equivalent to `NOT "tagA"`. Tag values must be double quoted UTF-8 encoded strings with a size limit of 1,000 characters.

Note: "Recently viewed" models don't support tag filtering at the moment.

    * filterOutOfStockItems. Restricts predictions to products that do not have a stockState value of OUT_OF_STOCK.

Examples:

    * tag=("Red" OR "Blue") tag="New-Arrival" tag=(NOT "promotional")
    * filterOutOfStockItems tag=(-"promotional")
    * filterOutOfStockItems

If your filter blocks all prediction results, the API will return _no_ results. If instead you want empty result sets to return generic (unfiltered) popular products, set `strictFiltering` to False in `PredictRequest.params`. Note that the API will never return items with storageStatus of "EXPIRED" or "DELETED" regardless of filter choices.

If `filterSyntaxV2` is set to true under the `params` field, then attribute-based expressions are expected instead of the above described tag-based syntax. Examples:

    * (colors: ANY("Red", "Blue")) AND NOT (categories: ANY("Phones"))
    * (availability: ANY("IN_STOCK")) AND (colors: ANY("Red") OR categories: ANY("Phones"))

For more information, see [Filter recommendations](https://cloud.google.com/retail/docs/filter-recs). 

  * **validate_only** (::Boolean) — Use validate only mode for this prediction query. If set to true, a dummy model will be used that returns arbitrary products. Note that the validate only mode should only be used for testing the API, or if the model is not ready. 
  * **params** (::Hash{::String => ::Google::Protobuf::Value, ::Hash}) — 

Additional domain specific parameters for the predictions.

Allowed values:

    * `returnProduct`: Boolean. If set to true, the associated product object will be returned in the `results.metadata` field in the prediction response.
    * `returnScore`: Boolean. If set to true, the prediction 'score' corresponding to each returned product will be set in the `results.metadata` field in the prediction response. The given 'score' indicates the probability of a product being clicked/purchased given the user's context and history.
    * `strictFiltering`: Boolean. True by default. If set to false, the service will return generic (unfiltered) popular products instead of empty if your filter blocks all prediction results.
    * `priceRerankLevel`: String. Default empty. If set to be non-empty, then it needs to be one of 'low-price-reranking', 'medium-price-reranking', 'high-price-reranking'. This gives request-level control and adjusts prediction results based on product price.
    * `diversityLevel`: String. Default empty. If set to be non-empty, then it needs to be one of 'low-diversity', 'medium-diversity', 'high-diversity', 'auto-diversity'. This gives request-level control and adjusts prediction results based on product category.
    * `filterSyntaxV2`: Boolean. False by default. If set to true, the `filter` field is interpreteted according to the new, attribute-based syntax.
  * **labels** (::Hash{::String => ::String}) — The labels applied to a resource must meet the following requirements:

    * Each resource can have multiple labels, up to a maximum of 64.
    * Each label must be a key-value pair.
    * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
    * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
    * The key portion of a label must be unique. However, you can use the same key with multiple resources.
    * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Retail::V2::PredictResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Retail::V2::PredictResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-PredictResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/retail/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Retail::V2::PredictionService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Retail::V2::PredictRequest.new
    
    # Call the predict method.
    result = client.predict request
    
    # The returned object is of type Google::Cloud::Retail::V2::PredictResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
