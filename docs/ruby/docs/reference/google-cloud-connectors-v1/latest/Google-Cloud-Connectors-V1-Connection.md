---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connection/
title: Connectors V1 API - Class Google::Cloud::Connectors::V1::Connection (v1.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:03.764436+00:00
---

# Connectors V1 API - Class Google::Cloud::Connectors::V1::Connection (v1.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Connectors V1 API - Class Google::Cloud::Connectors::V1::Connection (v1.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.1 (latest)  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Connectors V1 API class Google::Cloud::Connectors::V1::Connection.

Connection represents an instance of connector.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #auth_config
    
    
    def auth_config() -> ::Google::Cloud::Connectors::V1::AuthConfig

**Returns**

  * ([::Google::Cloud::Connectors::V1::AuthConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-AuthConfig)) — Optional. Configuration for establishing the connection's authentication with an external system. 



### #auth_config=
    
    
    def auth_config=(value) -> ::Google::Cloud::Connectors::V1::AuthConfig

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::AuthConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-AuthConfig)) — Optional. Configuration for establishing the connection's authentication with an external system. 



**Returns**

  * ([::Google::Cloud::Connectors::V1::AuthConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-AuthConfig)) — Optional. Configuration for establishing the connection's authentication with an external system. 



### #config_variables
    
    
    def config_variables() -> ::Array<::Google::Cloud::Connectors::V1::ConfigVariable>

**Returns**

  * (::Array<[::Google::Cloud::Connectors::V1::ConfigVariable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConfigVariable)>) — Optional. Configuration for configuring the connection with an external system. 



### #config_variables=
    
    
    def config_variables=(value) -> ::Array<::Google::Cloud::Connectors::V1::ConfigVariable>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Connectors::V1::ConfigVariable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConfigVariable)>) — Optional. Configuration for configuring the connection with an external system. 



**Returns**

  * (::Array<[::Google::Cloud::Connectors::V1::ConfigVariable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConfigVariable)>) — Optional. Configuration for configuring the connection with an external system. 



### #connector_version
    
    
    def connector_version() -> ::String

**Returns**

  * (::String) — Required. Connector version on which the connection is created. The format is: projects/_/locations/_ /providers/_/connectors/_ /versions/* Only global location is supported for ConnectorVersion resource. 



### #connector_version=
    
    
    def connector_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Connector version on which the connection is created. The format is: projects/_/locations/_ /providers/_/connectors/_ /versions/* Only global location is supported for ConnectorVersion resource. 



**Returns**

  * (::String) — Required. Connector version on which the connection is created. The format is: projects/_/locations/_ /providers/_/connectors/_ /versions/* Only global location is supported for ConnectorVersion resource. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Protobuf-Timestamp)) — Output only. Created time. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. Description of the resource. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Description of the resource. 



**Returns**

  * (::String) — Optional. Description of the resource. 



### #destination_configs
    
    
    def destination_configs() -> ::Array<::Google::Cloud::Connectors::V1::DestinationConfig>

**Returns**

  * (::Array<[::Google::Cloud::Connectors::V1::DestinationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-DestinationConfig)>) — Optional. Configuration of the Connector's destination. Only accepted for Connectors that accepts user defined destination(s). 



### #destination_configs=
    
    
    def destination_configs=(value) -> ::Array<::Google::Cloud::Connectors::V1::DestinationConfig>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Connectors::V1::DestinationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-DestinationConfig)>) — Optional. Configuration of the Connector's destination. Only accepted for Connectors that accepts user defined destination(s). 



**Returns**

  * (::Array<[::Google::Cloud::Connectors::V1::DestinationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-DestinationConfig)>) — Optional. Configuration of the Connector's destination. Only accepted for Connectors that accepts user defined destination(s). 



### #envoy_image_location
    
    
    def envoy_image_location() -> ::String

**Returns**

  * (::String) — Output only. GCR location where the envoy image is stored. formatted like: gcr.io/{bucketName}/{imageName} 



### #image_location
    
    
    def image_location() -> ::String

**Returns**

  * (::String) — Output only. GCR location where the runtime image is stored. formatted like: gcr.io/{bucketName}/{imageName} 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources 



### #lock_config
    
    
    def lock_config() -> ::Google::Cloud::Connectors::V1::LockConfig

**Returns**

  * ([::Google::Cloud::Connectors::V1::LockConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-LockConfig)) — Optional. Configuration that indicates whether or not the Connection can be edited. 



### #lock_config=
    
    
    def lock_config=(value) -> ::Google::Cloud::Connectors::V1::LockConfig

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::LockConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-LockConfig)) — Optional. Configuration that indicates whether or not the Connection can be edited. 



**Returns**

  * ([::Google::Cloud::Connectors::V1::LockConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-LockConfig)) — Optional. Configuration that indicates whether or not the Connection can be edited. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Resource name of the Connection. Format: projects/{project}/locations/{location}/connections/{connection} 



### #node_config
    
    
    def node_config() -> ::Google::Cloud::Connectors::V1::NodeConfig

**Returns**

  * ([::Google::Cloud::Connectors::V1::NodeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-NodeConfig)) — Optional. Node configuration for the connection. 



### #node_config=
    
    
    def node_config=(value) -> ::Google::Cloud::Connectors::V1::NodeConfig

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::NodeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-NodeConfig)) — Optional. Node configuration for the connection. 



**Returns**

  * ([::Google::Cloud::Connectors::V1::NodeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-NodeConfig)) — Optional. Node configuration for the connection. 



### #service_account
    
    
    def service_account() -> ::String

**Returns**

  * (::String) — Optional. Service account needed for runtime plane to access GCP resources. 



### #service_account=
    
    
    def service_account=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Service account needed for runtime plane to access GCP resources. 



**Returns**

  * (::String) — Optional. Service account needed for runtime plane to access GCP resources. 



### #service_directory
    
    
    def service_directory() -> ::String

**Returns**

  * (::String) — Output only. The name of the Service Directory service name. Used for Private Harpoon to resolve the ILB address. e.g. "projects/cloud-connectors-e2e-testing/locations/us-central1/namespaces/istio-system/services/istio-ingressgateway-connectors" 



### #ssl_config
    
    
    def ssl_config() -> ::Google::Cloud::Connectors::V1::SslConfig

**Returns**

  * ([::Google::Cloud::Connectors::V1::SslConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-SslConfig)) — Optional. Ssl config of a connection 



### #ssl_config=
    
    
    def ssl_config=(value) -> ::Google::Cloud::Connectors::V1::SslConfig

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::SslConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-SslConfig)) — Optional. Ssl config of a connection 



**Returns**

  * ([::Google::Cloud::Connectors::V1::SslConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-SslConfig)) — Optional. Ssl config of a connection 



### #status
    
    
    def status() -> ::Google::Cloud::Connectors::V1::ConnectionStatus

**Returns**

  * ([::Google::Cloud::Connectors::V1::ConnectionStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConnectionStatus)) — Output only. Current status of the connection. 



### #suspended
    
    
    def suspended() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Suspended indicates if a user has suspended a connection or not. 



### #suspended=
    
    
    def suspended=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Suspended indicates if a user has suspended a connection or not. 



**Returns**

  * (::Boolean) — Optional. Suspended indicates if a user has suspended a connection or not. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Protobuf-Timestamp)) — Output only. Updated time. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
