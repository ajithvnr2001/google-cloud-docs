---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute/
title: Google Cloud Compute API - Module Google::Cloud::Compute (v1.22.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:59.545614+00:00
---

# Google Cloud Compute API - Module Google::Cloud::Compute (v1.22.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute API - Module Google::Cloud::Compute (v1.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.22.0 (latest)  1.19.1  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.2  1.10.0  1.9.0  1.8.1  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Google Cloud Compute API module Google::Cloud::Compute.

## Methods 

### .accelerator_types
    
    
    def self.accelerator_types(version: :v1, &block) -> ::Object

Create a new client object for AcceleratorTypes.

By default, this returns an instance of [Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorTypes-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the AcceleratorTypes service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the AcceleratorTypes service. You can determine whether the method will succeed by calling [Compute.accelerator_types_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_accelerator_types_available__class_ "Google::Cloud::Compute.accelerator_types_available? \(method\)").

#### About AcceleratorTypes

Services

The AcceleratorTypes API.

This client uses AcceleratorTypes version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .accelerator_types_available?
    
    
    def self.accelerator_types_available?(version: :v1) -> boolean

Determines whether the AcceleratorTypes service is supported by the current client. If true, you can retrieve a client object by calling [Compute.accelerator_types](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_accelerator_types_class_ "Google::Cloud::Compute.accelerator_types \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the AcceleratorTypes service, or if the versioned client gem needs an update to support the AcceleratorTypes service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .addresses
    
    
    def self.addresses(version: :v1, &block) -> ::Object

Create a new client object for Addresses.

By default, this returns an instance of [Google::Cloud::Compute::V1::Addresses::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Addresses-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Addresses service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Addresses service. You can determine whether the method will succeed by calling [Compute.addresses_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_addresses_available__class_ "Google::Cloud::Compute.addresses_available? \(method\)").

#### About Addresses

The Addresses API.

This client uses Addresses version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .addresses_available?
    
    
    def self.addresses_available?(version: :v1) -> boolean

Determines whether the Addresses service is supported by the current client. If true, you can retrieve a client object by calling [Compute.addresses](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_addresses_class_ "Google::Cloud::Compute.addresses \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Addresses service, or if the versioned client gem needs an update to support the Addresses service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .advice
    
    
    def self.advice(version: :v1, &block) -> ::Object

Create a new client object for Advice.

By default, this returns an instance of [Google::Cloud::Compute::V1::Advice::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Advice-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Advice service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Advice service. You can determine whether the method will succeed by calling [Compute.advice_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_advice_available__class_ "Google::Cloud::Compute.advice_available? \(method\)").

#### About Advice

The Advice API.

This client uses Advice version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .advice_available?
    
    
    def self.advice_available?(version: :v1) -> boolean

Determines whether the Advice service is supported by the current client. If true, you can retrieve a client object by calling [Compute.advice](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_advice_class_ "Google::Cloud::Compute.advice \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Advice service, or if the versioned client gem needs an update to support the Advice service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .autoscalers
    
    
    def self.autoscalers(version: :v1, &block) -> ::Object

Create a new client object for Autoscalers.

By default, this returns an instance of [Google::Cloud::Compute::V1::Autoscalers::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Autoscalers-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Autoscalers service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Autoscalers service. You can determine whether the method will succeed by calling [Compute.autoscalers_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_autoscalers_available__class_ "Google::Cloud::Compute.autoscalers_available? \(method\)").

#### About Autoscalers

The Autoscalers API.

This client uses Autoscalers version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .autoscalers_available?
    
    
    def self.autoscalers_available?(version: :v1) -> boolean

Determines whether the Autoscalers service is supported by the current client. If true, you can retrieve a client object by calling [Compute.autoscalers](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_autoscalers_class_ "Google::Cloud::Compute.autoscalers \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Autoscalers service, or if the versioned client gem needs an update to support the Autoscalers service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .backend_buckets
    
    
    def self.backend_buckets(version: :v1, &block) -> ::Object

Create a new client object for BackendBuckets.

By default, this returns an instance of [Google::Cloud::Compute::V1::BackendBuckets::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-BackendBuckets-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the BackendBuckets service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the BackendBuckets service. You can determine whether the method will succeed by calling [Compute.backend_buckets_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_backend_buckets_available__class_ "Google::Cloud::Compute.backend_buckets_available? \(method\)").

#### About BackendBuckets

The BackendBuckets API.

This client uses BackendBuckets version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .backend_buckets_available?
    
    
    def self.backend_buckets_available?(version: :v1) -> boolean

Determines whether the BackendBuckets service is supported by the current client. If true, you can retrieve a client object by calling [Compute.backend_buckets](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_backend_buckets_class_ "Google::Cloud::Compute.backend_buckets \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the BackendBuckets service, or if the versioned client gem needs an update to support the BackendBuckets service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .backend_services
    
    
    def self.backend_services(version: :v1, &block) -> ::Object

Create a new client object for BackendServices.

By default, this returns an instance of [Google::Cloud::Compute::V1::BackendServices::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-BackendServices-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the BackendServices service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the BackendServices service. You can determine whether the method will succeed by calling [Compute.backend_services_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_backend_services_available__class_ "Google::Cloud::Compute.backend_services_available? \(method\)").

#### About BackendServices

The BackendServices API.

This client uses BackendServices version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .backend_services_available?
    
    
    def self.backend_services_available?(version: :v1) -> boolean

Determines whether the BackendServices service is supported by the current client. If true, you can retrieve a client object by calling [Compute.backend_services](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_backend_services_class_ "Google::Cloud::Compute.backend_services \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the BackendServices service, or if the versioned client gem needs an update to support the BackendServices service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .configure
    
    
    def self.configure() -> ::Google::Cloud::Config

Configure the google-cloud-compute library.

The following configuration parameters are supported:

  * `credentials` (_type:_ `String, Hash, Google::Auth::Credentials`) - The path to the keyfile as a String, the contents of the keyfile as a Hash, or a Google::Auth::Credentials object.
  * `lib_name` (_type:_ `String`) - The library name as recorded in instrumentation and logging.
  * `lib_version` (_type:_ `String`) - The library version as recorded in instrumentation and logging.
  * `timeout` (_type:_ `Numeric`) - Default timeout in seconds.
  * `metadata` (_type:_ `Hash{Symbol=>String}`) - Additional headers to be sent with the call.
  * `retry_policy` (_type:_ `Hash`) - The retry policy. The value is a hash with the following keys: 
    * `:initial_delay` (_type:_ `Numeric`) - The initial delay in seconds.
    * `:max_delay` (_type:_ `Numeric`) - The max delay in seconds.
    * `:multiplier` (_type:_ `Numeric`) - The incremental backoff multiplier.
    * `:jitter` (_type:_ `Numeric`) - The jitter in seconds. Default: 1.0.
    * `:retry_codes` (_type:_ `Array<String>`) - The error codes that should trigger a retry.



**Yields**

  * (::Google::Cloud.configure.compute) 



**Returns**

  * (::Google::Cloud::Config) — The default configuration used by this library 



### .cross_site_networks
    
    
    def self.cross_site_networks(version: :v1, &block) -> ::Object

Create a new client object for CrossSiteNetworks.

By default, this returns an instance of [Google::Cloud::Compute::V1::CrossSiteNetworks::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CrossSiteNetworks-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the CrossSiteNetworks service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the CrossSiteNetworks service. You can determine whether the method will succeed by calling [Compute.cross_site_networks_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_cross_site_networks_available__class_ "Google::Cloud::Compute.cross_site_networks_available? \(method\)").

#### About CrossSiteNetworks

The CrossSiteNetworks API.

This client uses CrossSiteNetworks version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .cross_site_networks_available?
    
    
    def self.cross_site_networks_available?(version: :v1) -> boolean

Determines whether the CrossSiteNetworks service is supported by the current client. If true, you can retrieve a client object by calling [Compute.cross_site_networks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_cross_site_networks_class_ "Google::Cloud::Compute.cross_site_networks \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the CrossSiteNetworks service, or if the versioned client gem needs an update to support the CrossSiteNetworks service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .disk_types
    
    
    def self.disk_types(version: :v1, &block) -> ::Object

Create a new client object for DiskTypes.

By default, this returns an instance of [Google::Cloud::Compute::V1::DiskTypes::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DiskTypes-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the DiskTypes service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the DiskTypes service. You can determine whether the method will succeed by calling [Compute.disk_types_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_disk_types_available__class_ "Google::Cloud::Compute.disk_types_available? \(method\)").

#### About DiskTypes

The DiskTypes API.

This client uses DiskTypes version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .disk_types_available?
    
    
    def self.disk_types_available?(version: :v1) -> boolean

Determines whether the DiskTypes service is supported by the current client. If true, you can retrieve a client object by calling [Compute.disk_types](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_disk_types_class_ "Google::Cloud::Compute.disk_types \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the DiskTypes service, or if the versioned client gem needs an update to support the DiskTypes service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .disks
    
    
    def self.disks(version: :v1, &block) -> ::Object

Create a new client object for Disks.

By default, this returns an instance of [Google::Cloud::Compute::V1::Disks::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Disks-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Disks service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Disks service. You can determine whether the method will succeed by calling [Compute.disks_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_disks_available__class_ "Google::Cloud::Compute.disks_available? \(method\)").

#### About Disks

The Disks API.

This client uses Disks version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .disks_available?
    
    
    def self.disks_available?(version: :v1) -> boolean

Determines whether the Disks service is supported by the current client. If true, you can retrieve a client object by calling [Compute.disks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_disks_class_ "Google::Cloud::Compute.disks \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Disks service, or if the versioned client gem needs an update to support the Disks service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .external_vpn_gateways
    
    
    def self.external_vpn_gateways(version: :v1, &block) -> ::Object

Create a new client object for ExternalVpnGateways.

By default, this returns an instance of [Google::Cloud::Compute::V1::ExternalVpnGateways::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ExternalVpnGateways-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ExternalVpnGateways service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the ExternalVpnGateways service. You can determine whether the method will succeed by calling [Compute.external_vpn_gateways_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_external_vpn_gateways_available__class_ "Google::Cloud::Compute.external_vpn_gateways_available? \(method\)").

#### About ExternalVpnGateways

The ExternalVpnGateways API.

This client uses ExternalVpnGateways version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .external_vpn_gateways_available?
    
    
    def self.external_vpn_gateways_available?(version: :v1) -> boolean

Determines whether the ExternalVpnGateways service is supported by the current client. If true, you can retrieve a client object by calling [Compute.external_vpn_gateways](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_external_vpn_gateways_class_ "Google::Cloud::Compute.external_vpn_gateways \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ExternalVpnGateways service, or if the versioned client gem needs an update to support the ExternalVpnGateways service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .firewall_policies
    
    
    def self.firewall_policies(version: :v1, &block) -> ::Object

Create a new client object for FirewallPolicies.

By default, this returns an instance of [Google::Cloud::Compute::V1::FirewallPolicies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-FirewallPolicies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the FirewallPolicies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the FirewallPolicies service. You can determine whether the method will succeed by calling [Compute.firewall_policies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_firewall_policies_available__class_ "Google::Cloud::Compute.firewall_policies_available? \(method\)").

#### About FirewallPolicies

The FirewallPolicies API.

This client uses FirewallPolicies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .firewall_policies_available?
    
    
    def self.firewall_policies_available?(version: :v1) -> boolean

Determines whether the FirewallPolicies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.firewall_policies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_firewall_policies_class_ "Google::Cloud::Compute.firewall_policies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the FirewallPolicies service, or if the versioned client gem needs an update to support the FirewallPolicies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .firewalls
    
    
    def self.firewalls(version: :v1, &block) -> ::Object

Create a new client object for Firewalls.

By default, this returns an instance of [Google::Cloud::Compute::V1::Firewalls::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Firewalls-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Firewalls service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Firewalls service. You can determine whether the method will succeed by calling [Compute.firewalls_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_firewalls_available__class_ "Google::Cloud::Compute.firewalls_available? \(method\)").

#### About Firewalls

The Firewalls API.

This client uses Firewalls version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .firewalls_available?
    
    
    def self.firewalls_available?(version: :v1) -> boolean

Determines whether the Firewalls service is supported by the current client. If true, you can retrieve a client object by calling [Compute.firewalls](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_firewalls_class_ "Google::Cloud::Compute.firewalls \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Firewalls service, or if the versioned client gem needs an update to support the Firewalls service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .forwarding_rules
    
    
    def self.forwarding_rules(version: :v1, &block) -> ::Object

Create a new client object for ForwardingRules.

By default, this returns an instance of [Google::Cloud::Compute::V1::ForwardingRules::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ForwardingRules-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ForwardingRules service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the ForwardingRules service. You can determine whether the method will succeed by calling [Compute.forwarding_rules_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_forwarding_rules_available__class_ "Google::Cloud::Compute.forwarding_rules_available? \(method\)").

#### About ForwardingRules

The ForwardingRules API.

This client uses ForwardingRules version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .forwarding_rules_available?
    
    
    def self.forwarding_rules_available?(version: :v1) -> boolean

Determines whether the ForwardingRules service is supported by the current client. If true, you can retrieve a client object by calling [Compute.forwarding_rules](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_forwarding_rules_class_ "Google::Cloud::Compute.forwarding_rules \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ForwardingRules service, or if the versioned client gem needs an update to support the ForwardingRules service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .future_reservations
    
    
    def self.future_reservations(version: :v1, &block) -> ::Object

Create a new client object for FutureReservations.

By default, this returns an instance of [Google::Cloud::Compute::V1::FutureReservations::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-FutureReservations-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the FutureReservations service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the FutureReservations service. You can determine whether the method will succeed by calling [Compute.future_reservations_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_future_reservations_available__class_ "Google::Cloud::Compute.future_reservations_available? \(method\)").

#### About FutureReservations

The FutureReservations API.

This client uses FutureReservations version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .future_reservations_available?
    
    
    def self.future_reservations_available?(version: :v1) -> boolean

Determines whether the FutureReservations service is supported by the current client. If true, you can retrieve a client object by calling [Compute.future_reservations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_future_reservations_class_ "Google::Cloud::Compute.future_reservations \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the FutureReservations service, or if the versioned client gem needs an update to support the FutureReservations service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .global_addresses
    
    
    def self.global_addresses(version: :v1, &block) -> ::Object

Create a new client object for GlobalAddresses.

By default, this returns an instance of [Google::Cloud::Compute::V1::GlobalAddresses::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalAddresses-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the GlobalAddresses service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the GlobalAddresses service. You can determine whether the method will succeed by calling [Compute.global_addresses_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_addresses_available__class_ "Google::Cloud::Compute.global_addresses_available? \(method\)").

#### About GlobalAddresses

The GlobalAddresses API.

This client uses GlobalAddresses version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .global_addresses_available?
    
    
    def self.global_addresses_available?(version: :v1) -> boolean

Determines whether the GlobalAddresses service is supported by the current client. If true, you can retrieve a client object by calling [Compute.global_addresses](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_addresses_class_ "Google::Cloud::Compute.global_addresses \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the GlobalAddresses service, or if the versioned client gem needs an update to support the GlobalAddresses service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .global_forwarding_rules
    
    
    def self.global_forwarding_rules(version: :v1, &block) -> ::Object

Create a new client object for GlobalForwardingRules.

By default, this returns an instance of [Google::Cloud::Compute::V1::GlobalForwardingRules::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalForwardingRules-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the GlobalForwardingRules service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the GlobalForwardingRules service. You can determine whether the method will succeed by calling [Compute.global_forwarding_rules_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_forwarding_rules_available__class_ "Google::Cloud::Compute.global_forwarding_rules_available? \(method\)").

#### About GlobalForwardingRules

The GlobalForwardingRules API.

This client uses GlobalForwardingRules version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .global_forwarding_rules_available?
    
    
    def self.global_forwarding_rules_available?(version: :v1) -> boolean

Determines whether the GlobalForwardingRules service is supported by the current client. If true, you can retrieve a client object by calling [Compute.global_forwarding_rules](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_forwarding_rules_class_ "Google::Cloud::Compute.global_forwarding_rules \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the GlobalForwardingRules service, or if the versioned client gem needs an update to support the GlobalForwardingRules service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .global_frontend_settings_service
    
    
    def self.global_frontend_settings_service(version: :v1, &block) -> ::Object

Create a new client object for GlobalFrontendSettingsService.

By default, this returns an instance of [Google::Cloud::Compute::V1::GlobalFrontendSettingsService::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalFrontendSettingsService-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the GlobalFrontendSettingsService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the GlobalFrontendSettingsService service. You can determine whether the method will succeed by calling [Compute.global_frontend_settings_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_frontend_settings_service_available__class_ "Google::Cloud::Compute.global_frontend_settings_service_available? \(method\)").

#### About GlobalFrontendSettingsService

The GlobalFrontendSettings API.

This client uses GlobalFrontendSettingsService version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .global_frontend_settings_service_available?
    
    
    def self.global_frontend_settings_service_available?(version: :v1) -> boolean

Determines whether the GlobalFrontendSettingsService service is supported by the current client. If true, you can retrieve a client object by calling [Compute.global_frontend_settings_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_frontend_settings_service_class_ "Google::Cloud::Compute.global_frontend_settings_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the GlobalFrontendSettingsService service, or if the versioned client gem needs an update to support the GlobalFrontendSettingsService service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .global_network_endpoint_groups
    
    
    def self.global_network_endpoint_groups(version: :v1, &block) -> ::Object

Create a new client object for GlobalNetworkEndpointGroups.

By default, this returns an instance of [Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalNetworkEndpointGroups-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the GlobalNetworkEndpointGroups service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the GlobalNetworkEndpointGroups service. You can determine whether the method will succeed by calling [Compute.global_network_endpoint_groups_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_network_endpoint_groups_available__class_ "Google::Cloud::Compute.global_network_endpoint_groups_available? \(method\)").

#### About GlobalNetworkEndpointGroups

The GlobalNetworkEndpointGroups API.

This client uses GlobalNetworkEndpointGroups version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .global_network_endpoint_groups_available?
    
    
    def self.global_network_endpoint_groups_available?(version: :v1) -> boolean

Determines whether the GlobalNetworkEndpointGroups service is supported by the current client. If true, you can retrieve a client object by calling [Compute.global_network_endpoint_groups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_network_endpoint_groups_class_ "Google::Cloud::Compute.global_network_endpoint_groups \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the GlobalNetworkEndpointGroups service, or if the versioned client gem needs an update to support the GlobalNetworkEndpointGroups service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .global_operations
    
    
    def self.global_operations(version: :v1, &block) -> ::Object

Create a new client object for GlobalOperations.

By default, this returns an instance of [Google::Cloud::Compute::V1::GlobalOperations::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalOperations-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the GlobalOperations service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the GlobalOperations service. You can determine whether the method will succeed by calling [Compute.global_operations_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_operations_available__class_ "Google::Cloud::Compute.global_operations_available? \(method\)").

#### About GlobalOperations

The GlobalOperations API.

This client uses GlobalOperations version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .global_operations_available?
    
    
    def self.global_operations_available?(version: :v1) -> boolean

Determines whether the GlobalOperations service is supported by the current client. If true, you can retrieve a client object by calling [Compute.global_operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_operations_class_ "Google::Cloud::Compute.global_operations \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the GlobalOperations service, or if the versioned client gem needs an update to support the GlobalOperations service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .global_organization_operations
    
    
    def self.global_organization_operations(version: :v1, &block) -> ::Object

Create a new client object for GlobalOrganizationOperations.

By default, this returns an instance of [Google::Cloud::Compute::V1::GlobalOrganizationOperations::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalOrganizationOperations-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the GlobalOrganizationOperations service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the GlobalOrganizationOperations service. You can determine whether the method will succeed by calling [Compute.global_organization_operations_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_organization_operations_available__class_ "Google::Cloud::Compute.global_organization_operations_available? \(method\)").

#### About GlobalOrganizationOperations

The GlobalOrganizationOperations API.

This client uses GlobalOrganizationOperations version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .global_organization_operations_available?
    
    
    def self.global_organization_operations_available?(version: :v1) -> boolean

Determines whether the GlobalOrganizationOperations service is supported by the current client. If true, you can retrieve a client object by calling [Compute.global_organization_operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_organization_operations_class_ "Google::Cloud::Compute.global_organization_operations \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the GlobalOrganizationOperations service, or if the versioned client gem needs an update to support the GlobalOrganizationOperations service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .global_public_delegated_prefixes
    
    
    def self.global_public_delegated_prefixes(version: :v1, &block) -> ::Object

Create a new client object for GlobalPublicDelegatedPrefixes.

By default, this returns an instance of [Google::Cloud::Compute::V1::GlobalPublicDelegatedPrefixes::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalPublicDelegatedPrefixes-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the GlobalPublicDelegatedPrefixes service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the GlobalPublicDelegatedPrefixes service. You can determine whether the method will succeed by calling [Compute.global_public_delegated_prefixes_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_public_delegated_prefixes_available__class_ "Google::Cloud::Compute.global_public_delegated_prefixes_available? \(method\)").

#### About GlobalPublicDelegatedPrefixes

The GlobalPublicDelegatedPrefixes API.

This client uses GlobalPublicDelegatedPrefixes version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .global_public_delegated_prefixes_available?
    
    
    def self.global_public_delegated_prefixes_available?(version: :v1) -> boolean

Determines whether the GlobalPublicDelegatedPrefixes service is supported by the current client. If true, you can retrieve a client object by calling [Compute.global_public_delegated_prefixes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_public_delegated_prefixes_class_ "Google::Cloud::Compute.global_public_delegated_prefixes \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the GlobalPublicDelegatedPrefixes service, or if the versioned client gem needs an update to support the GlobalPublicDelegatedPrefixes service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .global_vm_extension_policies
    
    
    def self.global_vm_extension_policies(version: :v1, &block) -> ::Object

Create a new client object for GlobalVmExtensionPolicies.

By default, this returns an instance of [Google::Cloud::Compute::V1::GlobalVmExtensionPolicies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalVmExtensionPolicies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the GlobalVmExtensionPolicies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the GlobalVmExtensionPolicies service. You can determine whether the method will succeed by calling [Compute.global_vm_extension_policies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_vm_extension_policies_available__class_ "Google::Cloud::Compute.global_vm_extension_policies_available? \(method\)").

#### About GlobalVmExtensionPolicies

The GlobalVmExtensionPolicies API.

This client uses GlobalVmExtensionPolicies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .global_vm_extension_policies_available?
    
    
    def self.global_vm_extension_policies_available?(version: :v1) -> boolean

Determines whether the GlobalVmExtensionPolicies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.global_vm_extension_policies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_global_vm_extension_policies_class_ "Google::Cloud::Compute.global_vm_extension_policies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the GlobalVmExtensionPolicies service, or if the versioned client gem needs an update to support the GlobalVmExtensionPolicies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .health_checks
    
    
    def self.health_checks(version: :v1, &block) -> ::Object

Create a new client object for HealthChecks.

By default, this returns an instance of [Google::Cloud::Compute::V1::HealthChecks::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-HealthChecks-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the HealthChecks service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the HealthChecks service. You can determine whether the method will succeed by calling [Compute.health_checks_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_health_checks_available__class_ "Google::Cloud::Compute.health_checks_available? \(method\)").

#### About HealthChecks

The HealthChecks API.

This client uses HealthChecks version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .health_checks_available?
    
    
    def self.health_checks_available?(version: :v1) -> boolean

Determines whether the HealthChecks service is supported by the current client. If true, you can retrieve a client object by calling [Compute.health_checks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_health_checks_class_ "Google::Cloud::Compute.health_checks \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the HealthChecks service, or if the versioned client gem needs an update to support the HealthChecks service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .hosts
    
    
    def self.hosts(version: :v1, &block) -> ::Object

Create a new client object for Hosts.

By default, this returns an instance of [Google::Cloud::Compute::V1::Hosts::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Hosts-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Hosts service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Hosts service. You can determine whether the method will succeed by calling [Compute.hosts_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_hosts_available__class_ "Google::Cloud::Compute.hosts_available? \(method\)").

#### About Hosts

The Hosts API.

This client uses Hosts version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .hosts_available?
    
    
    def self.hosts_available?(version: :v1) -> boolean

Determines whether the Hosts service is supported by the current client. If true, you can retrieve a client object by calling [Compute.hosts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_hosts_class_ "Google::Cloud::Compute.hosts \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Hosts service, or if the versioned client gem needs an update to support the Hosts service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .image_family_views
    
    
    def self.image_family_views(version: :v1, &block) -> ::Object

Create a new client object for ImageFamilyViews.

By default, this returns an instance of [Google::Cloud::Compute::V1::ImageFamilyViews::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ImageFamilyViews-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ImageFamilyViews service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the ImageFamilyViews service. You can determine whether the method will succeed by calling [Compute.image_family_views_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_image_family_views_available__class_ "Google::Cloud::Compute.image_family_views_available? \(method\)").

#### About ImageFamilyViews

The ImageFamilyViews API.

This client uses ImageFamilyViews version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .image_family_views_available?
    
    
    def self.image_family_views_available?(version: :v1) -> boolean

Determines whether the ImageFamilyViews service is supported by the current client. If true, you can retrieve a client object by calling [Compute.image_family_views](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_image_family_views_class_ "Google::Cloud::Compute.image_family_views \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ImageFamilyViews service, or if the versioned client gem needs an update to support the ImageFamilyViews service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .image_views
    
    
    def self.image_views(version: :v1, &block) -> ::Object

Create a new client object for ImageViews.

By default, this returns an instance of [Google::Cloud::Compute::V1::ImageViews::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ImageViews-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ImageViews service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the ImageViews service. You can determine whether the method will succeed by calling [Compute.image_views_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_image_views_available__class_ "Google::Cloud::Compute.image_views_available? \(method\)").

#### About ImageViews

The ImageViews API.

This client uses ImageViews version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .image_views_available?
    
    
    def self.image_views_available?(version: :v1) -> boolean

Determines whether the ImageViews service is supported by the current client. If true, you can retrieve a client object by calling [Compute.image_views](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_image_views_class_ "Google::Cloud::Compute.image_views \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ImageViews service, or if the versioned client gem needs an update to support the ImageViews service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .images
    
    
    def self.images(version: :v1, &block) -> ::Object

Create a new client object for Images.

By default, this returns an instance of [Google::Cloud::Compute::V1::Images::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Images-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Images service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Images service. You can determine whether the method will succeed by calling [Compute.images_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_images_available__class_ "Google::Cloud::Compute.images_available? \(method\)").

#### About Images

The Images API.

This client uses Images version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .images_available?
    
    
    def self.images_available?(version: :v1) -> boolean

Determines whether the Images service is supported by the current client. If true, you can retrieve a client object by calling [Compute.images](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_images_class_ "Google::Cloud::Compute.images \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Images service, or if the versioned client gem needs an update to support the Images service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .instance_group_manager_resize_requests
    
    
    def self.instance_group_manager_resize_requests(version: :v1, &block) -> ::Object

Create a new client object for InstanceGroupManagerResizeRequests.

By default, this returns an instance of [Google::Cloud::Compute::V1::InstanceGroupManagerResizeRequests::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroupManagerResizeRequests-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the InstanceGroupManagerResizeRequests service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the InstanceGroupManagerResizeRequests service. You can determine whether the method will succeed by calling [Compute.instance_group_manager_resize_requests_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instance_group_manager_resize_requests_available__class_ "Google::Cloud::Compute.instance_group_manager_resize_requests_available? \(method\)").

#### About InstanceGroupManagerResizeRequests

The InstanceGroupManagerResizeRequests API.

This client uses InstanceGroupManagerResizeRequests version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .instance_group_manager_resize_requests_available?
    
    
    def self.instance_group_manager_resize_requests_available?(version: :v1) -> boolean

Determines whether the InstanceGroupManagerResizeRequests service is supported by the current client. If true, you can retrieve a client object by calling [Compute.instance_group_manager_resize_requests](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instance_group_manager_resize_requests_class_ "Google::Cloud::Compute.instance_group_manager_resize_requests \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the InstanceGroupManagerResizeRequests service, or if the versioned client gem needs an update to support the InstanceGroupManagerResizeRequests service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .instance_group_managers
    
    
    def self.instance_group_managers(version: :v1, &block) -> ::Object

Create a new client object for InstanceGroupManagers.

By default, this returns an instance of [Google::Cloud::Compute::V1::InstanceGroupManagers::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroupManagers-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the InstanceGroupManagers service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the InstanceGroupManagers service. You can determine whether the method will succeed by calling [Compute.instance_group_managers_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instance_group_managers_available__class_ "Google::Cloud::Compute.instance_group_managers_available? \(method\)").

#### About InstanceGroupManagers

The InstanceGroupManagers API.

This client uses InstanceGroupManagers version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .instance_group_managers_available?
    
    
    def self.instance_group_managers_available?(version: :v1) -> boolean

Determines whether the InstanceGroupManagers service is supported by the current client. If true, you can retrieve a client object by calling [Compute.instance_group_managers](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instance_group_managers_class_ "Google::Cloud::Compute.instance_group_managers \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the InstanceGroupManagers service, or if the versioned client gem needs an update to support the InstanceGroupManagers service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .instance_groups
    
    
    def self.instance_groups(version: :v1, &block) -> ::Object

Create a new client object for InstanceGroups.

By default, this returns an instance of [Google::Cloud::Compute::V1::InstanceGroups::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroups-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the InstanceGroups service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the InstanceGroups service. You can determine whether the method will succeed by calling [Compute.instance_groups_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instance_groups_available__class_ "Google::Cloud::Compute.instance_groups_available? \(method\)").

#### About InstanceGroups

The InstanceGroups API.

This client uses InstanceGroups version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .instance_groups_available?
    
    
    def self.instance_groups_available?(version: :v1) -> boolean

Determines whether the InstanceGroups service is supported by the current client. If true, you can retrieve a client object by calling [Compute.instance_groups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instance_groups_class_ "Google::Cloud::Compute.instance_groups \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the InstanceGroups service, or if the versioned client gem needs an update to support the InstanceGroups service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .instance_settings_service
    
    
    def self.instance_settings_service(version: :v1, &block) -> ::Object

Create a new client object for InstanceSettingsService.

By default, this returns an instance of [Google::Cloud::Compute::V1::InstanceSettingsService::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceSettingsService-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the InstanceSettingsService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the InstanceSettingsService service. You can determine whether the method will succeed by calling [Compute.instance_settings_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instance_settings_service_available__class_ "Google::Cloud::Compute.instance_settings_service_available? \(method\)").

#### About InstanceSettingsService

The InstanceSettings API.

This client uses InstanceSettingsService version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .instance_settings_service_available?
    
    
    def self.instance_settings_service_available?(version: :v1) -> boolean

Determines whether the InstanceSettingsService service is supported by the current client. If true, you can retrieve a client object by calling [Compute.instance_settings_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instance_settings_service_class_ "Google::Cloud::Compute.instance_settings_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the InstanceSettingsService service, or if the versioned client gem needs an update to support the InstanceSettingsService service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .instance_templates
    
    
    def self.instance_templates(version: :v1, &block) -> ::Object

Create a new client object for InstanceTemplates.

By default, this returns an instance of [Google::Cloud::Compute::V1::InstanceTemplates::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceTemplates-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the InstanceTemplates service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the InstanceTemplates service. You can determine whether the method will succeed by calling [Compute.instance_templates_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instance_templates_available__class_ "Google::Cloud::Compute.instance_templates_available? \(method\)").

#### About InstanceTemplates

The InstanceTemplates API.

This client uses InstanceTemplates version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .instance_templates_available?
    
    
    def self.instance_templates_available?(version: :v1) -> boolean

Determines whether the InstanceTemplates service is supported by the current client. If true, you can retrieve a client object by calling [Compute.instance_templates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instance_templates_class_ "Google::Cloud::Compute.instance_templates \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the InstanceTemplates service, or if the versioned client gem needs an update to support the InstanceTemplates service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .instances
    
    
    def self.instances(version: :v1, &block) -> ::Object

Create a new client object for Instances.

By default, this returns an instance of [Google::Cloud::Compute::V1::Instances::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Instances-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Instances service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Instances service. You can determine whether the method will succeed by calling [Compute.instances_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instances_available__class_ "Google::Cloud::Compute.instances_available? \(method\)").

#### About Instances

The Instances API.

This client uses Instances version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .instances_available?
    
    
    def self.instances_available?(version: :v1) -> boolean

Determines whether the Instances service is supported by the current client. If true, you can retrieve a client object by calling [Compute.instances](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instances_class_ "Google::Cloud::Compute.instances \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Instances service, or if the versioned client gem needs an update to support the Instances service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .instant_snapshot_groups
    
    
    def self.instant_snapshot_groups(version: :v1, &block) -> ::Object

Create a new client object for InstantSnapshotGroups.

By default, this returns an instance of [Google::Cloud::Compute::V1::InstantSnapshotGroups::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstantSnapshotGroups-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the InstantSnapshotGroups service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the InstantSnapshotGroups service. You can determine whether the method will succeed by calling [Compute.instant_snapshot_groups_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instant_snapshot_groups_available__class_ "Google::Cloud::Compute.instant_snapshot_groups_available? \(method\)").

#### About InstantSnapshotGroups

The InstantSnapshotGroups API.

This client uses InstantSnapshotGroups version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .instant_snapshot_groups_available?
    
    
    def self.instant_snapshot_groups_available?(version: :v1) -> boolean

Determines whether the InstantSnapshotGroups service is supported by the current client. If true, you can retrieve a client object by calling [Compute.instant_snapshot_groups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instant_snapshot_groups_class_ "Google::Cloud::Compute.instant_snapshot_groups \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the InstantSnapshotGroups service, or if the versioned client gem needs an update to support the InstantSnapshotGroups service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .instant_snapshots
    
    
    def self.instant_snapshots(version: :v1, &block) -> ::Object

Create a new client object for InstantSnapshots.

By default, this returns an instance of [Google::Cloud::Compute::V1::InstantSnapshots::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstantSnapshots-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the InstantSnapshots service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the InstantSnapshots service. You can determine whether the method will succeed by calling [Compute.instant_snapshots_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instant_snapshots_available__class_ "Google::Cloud::Compute.instant_snapshots_available? \(method\)").

#### About InstantSnapshots

The InstantSnapshots API.

This client uses InstantSnapshots version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .instant_snapshots_available?
    
    
    def self.instant_snapshots_available?(version: :v1) -> boolean

Determines whether the InstantSnapshots service is supported by the current client. If true, you can retrieve a client object by calling [Compute.instant_snapshots](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_instant_snapshots_class_ "Google::Cloud::Compute.instant_snapshots \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the InstantSnapshots service, or if the versioned client gem needs an update to support the InstantSnapshots service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .interconnect_attachment_groups
    
    
    def self.interconnect_attachment_groups(version: :v1, &block) -> ::Object

Create a new client object for InterconnectAttachmentGroups.

By default, this returns an instance of [Google::Cloud::Compute::V1::InterconnectAttachmentGroups::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectAttachmentGroups-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the InterconnectAttachmentGroups service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the InterconnectAttachmentGroups service. You can determine whether the method will succeed by calling [Compute.interconnect_attachment_groups_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_interconnect_attachment_groups_available__class_ "Google::Cloud::Compute.interconnect_attachment_groups_available? \(method\)").

#### About InterconnectAttachmentGroups

The InterconnectAttachmentGroups API.

This client uses InterconnectAttachmentGroups version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .interconnect_attachment_groups_available?
    
    
    def self.interconnect_attachment_groups_available?(version: :v1) -> boolean

Determines whether the InterconnectAttachmentGroups service is supported by the current client. If true, you can retrieve a client object by calling [Compute.interconnect_attachment_groups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_interconnect_attachment_groups_class_ "Google::Cloud::Compute.interconnect_attachment_groups \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the InterconnectAttachmentGroups service, or if the versioned client gem needs an update to support the InterconnectAttachmentGroups service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .interconnect_attachments
    
    
    def self.interconnect_attachments(version: :v1, &block) -> ::Object

Create a new client object for InterconnectAttachments.

By default, this returns an instance of [Google::Cloud::Compute::V1::InterconnectAttachments::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectAttachments-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the InterconnectAttachments service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the InterconnectAttachments service. You can determine whether the method will succeed by calling [Compute.interconnect_attachments_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_interconnect_attachments_available__class_ "Google::Cloud::Compute.interconnect_attachments_available? \(method\)").

#### About InterconnectAttachments

The InterconnectAttachments API.

This client uses InterconnectAttachments version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .interconnect_attachments_available?
    
    
    def self.interconnect_attachments_available?(version: :v1) -> boolean

Determines whether the InterconnectAttachments service is supported by the current client. If true, you can retrieve a client object by calling [Compute.interconnect_attachments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_interconnect_attachments_class_ "Google::Cloud::Compute.interconnect_attachments \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the InterconnectAttachments service, or if the versioned client gem needs an update to support the InterconnectAttachments service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .interconnect_groups
    
    
    def self.interconnect_groups(version: :v1, &block) -> ::Object

Create a new client object for InterconnectGroups.

By default, this returns an instance of [Google::Cloud::Compute::V1::InterconnectGroups::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectGroups-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the InterconnectGroups service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the InterconnectGroups service. You can determine whether the method will succeed by calling [Compute.interconnect_groups_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_interconnect_groups_available__class_ "Google::Cloud::Compute.interconnect_groups_available? \(method\)").

#### About InterconnectGroups

The InterconnectGroups API.

This client uses InterconnectGroups version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .interconnect_groups_available?
    
    
    def self.interconnect_groups_available?(version: :v1) -> boolean

Determines whether the InterconnectGroups service is supported by the current client. If true, you can retrieve a client object by calling [Compute.interconnect_groups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_interconnect_groups_class_ "Google::Cloud::Compute.interconnect_groups \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the InterconnectGroups service, or if the versioned client gem needs an update to support the InterconnectGroups service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .interconnect_locations
    
    
    def self.interconnect_locations(version: :v1, &block) -> ::Object

Create a new client object for InterconnectLocations.

By default, this returns an instance of [Google::Cloud::Compute::V1::InterconnectLocations::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectLocations-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the InterconnectLocations service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the InterconnectLocations service. You can determine whether the method will succeed by calling [Compute.interconnect_locations_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_interconnect_locations_available__class_ "Google::Cloud::Compute.interconnect_locations_available? \(method\)").

#### About InterconnectLocations

The InterconnectLocations API.

This client uses InterconnectLocations version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .interconnect_locations_available?
    
    
    def self.interconnect_locations_available?(version: :v1) -> boolean

Determines whether the InterconnectLocations service is supported by the current client. If true, you can retrieve a client object by calling [Compute.interconnect_locations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_interconnect_locations_class_ "Google::Cloud::Compute.interconnect_locations \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the InterconnectLocations service, or if the versioned client gem needs an update to support the InterconnectLocations service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .interconnect_remote_locations
    
    
    def self.interconnect_remote_locations(version: :v1, &block) -> ::Object

Create a new client object for InterconnectRemoteLocations.

By default, this returns an instance of [Google::Cloud::Compute::V1::InterconnectRemoteLocations::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InterconnectRemoteLocations-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the InterconnectRemoteLocations service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the InterconnectRemoteLocations service. You can determine whether the method will succeed by calling [Compute.interconnect_remote_locations_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_interconnect_remote_locations_available__class_ "Google::Cloud::Compute.interconnect_remote_locations_available? \(method\)").

#### About InterconnectRemoteLocations

The InterconnectRemoteLocations API.

This client uses InterconnectRemoteLocations version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .interconnect_remote_locations_available?
    
    
    def self.interconnect_remote_locations_available?(version: :v1) -> boolean

Determines whether the InterconnectRemoteLocations service is supported by the current client. If true, you can retrieve a client object by calling [Compute.interconnect_remote_locations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_interconnect_remote_locations_class_ "Google::Cloud::Compute.interconnect_remote_locations \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the InterconnectRemoteLocations service, or if the versioned client gem needs an update to support the InterconnectRemoteLocations service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .interconnects
    
    
    def self.interconnects(version: :v1, &block) -> ::Object

Create a new client object for Interconnects.

By default, this returns an instance of [Google::Cloud::Compute::V1::Interconnects::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Interconnects-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Interconnects service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Interconnects service. You can determine whether the method will succeed by calling [Compute.interconnects_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_interconnects_available__class_ "Google::Cloud::Compute.interconnects_available? \(method\)").

#### About Interconnects

The Interconnects API.

This client uses Interconnects version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .interconnects_available?
    
    
    def self.interconnects_available?(version: :v1) -> boolean

Determines whether the Interconnects service is supported by the current client. If true, you can retrieve a client object by calling [Compute.interconnects](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_interconnects_class_ "Google::Cloud::Compute.interconnects \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Interconnects service, or if the versioned client gem needs an update to support the Interconnects service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .license_codes
    
    
    def self.license_codes(version: :v1, &block) -> ::Object

Create a new client object for LicenseCodes.

By default, this returns an instance of [Google::Cloud::Compute::V1::LicenseCodes::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-LicenseCodes-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the LicenseCodes service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the LicenseCodes service. You can determine whether the method will succeed by calling [Compute.license_codes_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_license_codes_available__class_ "Google::Cloud::Compute.license_codes_available? \(method\)").

#### About LicenseCodes

The LicenseCodes API.

This client uses LicenseCodes version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .license_codes_available?
    
    
    def self.license_codes_available?(version: :v1) -> boolean

Determines whether the LicenseCodes service is supported by the current client. If true, you can retrieve a client object by calling [Compute.license_codes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_license_codes_class_ "Google::Cloud::Compute.license_codes \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the LicenseCodes service, or if the versioned client gem needs an update to support the LicenseCodes service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .licenses
    
    
    def self.licenses(version: :v1, &block) -> ::Object

Create a new client object for Licenses.

By default, this returns an instance of [Google::Cloud::Compute::V1::Licenses::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Licenses-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Licenses service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Licenses service. You can determine whether the method will succeed by calling [Compute.licenses_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_licenses_available__class_ "Google::Cloud::Compute.licenses_available? \(method\)").

#### About Licenses

The Licenses API.

This client uses Licenses version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .licenses_available?
    
    
    def self.licenses_available?(version: :v1) -> boolean

Determines whether the Licenses service is supported by the current client. If true, you can retrieve a client object by calling [Compute.licenses](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_licenses_class_ "Google::Cloud::Compute.licenses \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Licenses service, or if the versioned client gem needs an update to support the Licenses service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .machine_images
    
    
    def self.machine_images(version: :v1, &block) -> ::Object

Create a new client object for MachineImages.

By default, this returns an instance of [Google::Cloud::Compute::V1::MachineImages::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-MachineImages-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the MachineImages service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the MachineImages service. You can determine whether the method will succeed by calling [Compute.machine_images_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_machine_images_available__class_ "Google::Cloud::Compute.machine_images_available? \(method\)").

#### About MachineImages

The MachineImages API.

This client uses MachineImages version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .machine_images_available?
    
    
    def self.machine_images_available?(version: :v1) -> boolean

Determines whether the MachineImages service is supported by the current client. If true, you can retrieve a client object by calling [Compute.machine_images](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_machine_images_class_ "Google::Cloud::Compute.machine_images \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the MachineImages service, or if the versioned client gem needs an update to support the MachineImages service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .machine_types
    
    
    def self.machine_types(version: :v1, &block) -> ::Object

Create a new client object for MachineTypes.

By default, this returns an instance of [Google::Cloud::Compute::V1::MachineTypes::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-MachineTypes-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the MachineTypes service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the MachineTypes service. You can determine whether the method will succeed by calling [Compute.machine_types_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_machine_types_available__class_ "Google::Cloud::Compute.machine_types_available? \(method\)").

#### About MachineTypes

The MachineTypes API.

This client uses MachineTypes version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .machine_types_available?
    
    
    def self.machine_types_available?(version: :v1) -> boolean

Determines whether the MachineTypes service is supported by the current client. If true, you can retrieve a client object by calling [Compute.machine_types](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_machine_types_class_ "Google::Cloud::Compute.machine_types \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the MachineTypes service, or if the versioned client gem needs an update to support the MachineTypes service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .managed_rulesets
    
    
    def self.managed_rulesets(version: :v1, &block) -> ::Object

Create a new client object for ManagedRulesets.

By default, this returns an instance of [Google::Cloud::Compute::V1::ManagedRulesets::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ManagedRulesets-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ManagedRulesets service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the ManagedRulesets service. You can determine whether the method will succeed by calling [Compute.managed_rulesets_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_managed_rulesets_available__class_ "Google::Cloud::Compute.managed_rulesets_available? \(method\)").

#### About ManagedRulesets

The ManagedRulesets API.

This client uses ManagedRulesets version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .managed_rulesets_available?
    
    
    def self.managed_rulesets_available?(version: :v1) -> boolean

Determines whether the ManagedRulesets service is supported by the current client. If true, you can retrieve a client object by calling [Compute.managed_rulesets](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_managed_rulesets_class_ "Google::Cloud::Compute.managed_rulesets \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ManagedRulesets service, or if the versioned client gem needs an update to support the ManagedRulesets service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .network_attachments
    
    
    def self.network_attachments(version: :v1, &block) -> ::Object

Create a new client object for NetworkAttachments.

By default, this returns an instance of [Google::Cloud::Compute::V1::NetworkAttachments::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkAttachments-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the NetworkAttachments service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the NetworkAttachments service. You can determine whether the method will succeed by calling [Compute.network_attachments_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_network_attachments_available__class_ "Google::Cloud::Compute.network_attachments_available? \(method\)").

#### About NetworkAttachments

The NetworkAttachments API.

This client uses NetworkAttachments version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .network_attachments_available?
    
    
    def self.network_attachments_available?(version: :v1) -> boolean

Determines whether the NetworkAttachments service is supported by the current client. If true, you can retrieve a client object by calling [Compute.network_attachments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_network_attachments_class_ "Google::Cloud::Compute.network_attachments \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the NetworkAttachments service, or if the versioned client gem needs an update to support the NetworkAttachments service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .network_edge_security_services
    
    
    def self.network_edge_security_services(version: :v1, &block) -> ::Object

Create a new client object for NetworkEdgeSecurityServices.

By default, this returns an instance of [Google::Cloud::Compute::V1::NetworkEdgeSecurityServices::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEdgeSecurityServices-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the NetworkEdgeSecurityServices service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the NetworkEdgeSecurityServices service. You can determine whether the method will succeed by calling [Compute.network_edge_security_services_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_network_edge_security_services_available__class_ "Google::Cloud::Compute.network_edge_security_services_available? \(method\)").

#### About NetworkEdgeSecurityServices

The NetworkEdgeSecurityServices API.

This client uses NetworkEdgeSecurityServices version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .network_edge_security_services_available?
    
    
    def self.network_edge_security_services_available?(version: :v1) -> boolean

Determines whether the NetworkEdgeSecurityServices service is supported by the current client. If true, you can retrieve a client object by calling [Compute.network_edge_security_services](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_network_edge_security_services_class_ "Google::Cloud::Compute.network_edge_security_services \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the NetworkEdgeSecurityServices service, or if the versioned client gem needs an update to support the NetworkEdgeSecurityServices service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .network_endpoint_groups
    
    
    def self.network_endpoint_groups(version: :v1, &block) -> ::Object

Create a new client object for NetworkEndpointGroups.

By default, this returns an instance of [Google::Cloud::Compute::V1::NetworkEndpointGroups::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroups-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the NetworkEndpointGroups service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the NetworkEndpointGroups service. You can determine whether the method will succeed by calling [Compute.network_endpoint_groups_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_network_endpoint_groups_available__class_ "Google::Cloud::Compute.network_endpoint_groups_available? \(method\)").

#### About NetworkEndpointGroups

The NetworkEndpointGroups API.

This client uses NetworkEndpointGroups version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .network_endpoint_groups_available?
    
    
    def self.network_endpoint_groups_available?(version: :v1) -> boolean

Determines whether the NetworkEndpointGroups service is supported by the current client. If true, you can retrieve a client object by calling [Compute.network_endpoint_groups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_network_endpoint_groups_class_ "Google::Cloud::Compute.network_endpoint_groups \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the NetworkEndpointGroups service, or if the versioned client gem needs an update to support the NetworkEndpointGroups service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .network_firewall_policies
    
    
    def self.network_firewall_policies(version: :v1, &block) -> ::Object

Create a new client object for NetworkFirewallPolicies.

By default, this returns an instance of [Google::Cloud::Compute::V1::NetworkFirewallPolicies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkFirewallPolicies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the NetworkFirewallPolicies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the NetworkFirewallPolicies service. You can determine whether the method will succeed by calling [Compute.network_firewall_policies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_network_firewall_policies_available__class_ "Google::Cloud::Compute.network_firewall_policies_available? \(method\)").

#### About NetworkFirewallPolicies

The NetworkFirewallPolicies API.

This client uses NetworkFirewallPolicies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .network_firewall_policies_available?
    
    
    def self.network_firewall_policies_available?(version: :v1) -> boolean

Determines whether the NetworkFirewallPolicies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.network_firewall_policies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_network_firewall_policies_class_ "Google::Cloud::Compute.network_firewall_policies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the NetworkFirewallPolicies service, or if the versioned client gem needs an update to support the NetworkFirewallPolicies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .network_profiles
    
    
    def self.network_profiles(version: :v1, &block) -> ::Object

Create a new client object for NetworkProfiles.

By default, this returns an instance of [Google::Cloud::Compute::V1::NetworkProfiles::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkProfiles-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the NetworkProfiles service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the NetworkProfiles service. You can determine whether the method will succeed by calling [Compute.network_profiles_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_network_profiles_available__class_ "Google::Cloud::Compute.network_profiles_available? \(method\)").

#### About NetworkProfiles

The NetworkProfiles API.

This client uses NetworkProfiles version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .network_profiles_available?
    
    
    def self.network_profiles_available?(version: :v1) -> boolean

Determines whether the NetworkProfiles service is supported by the current client. If true, you can retrieve a client object by calling [Compute.network_profiles](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_network_profiles_class_ "Google::Cloud::Compute.network_profiles \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the NetworkProfiles service, or if the versioned client gem needs an update to support the NetworkProfiles service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .networks
    
    
    def self.networks(version: :v1, &block) -> ::Object

Create a new client object for Networks.

By default, this returns an instance of [Google::Cloud::Compute::V1::Networks::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Networks-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Networks service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Networks service. You can determine whether the method will succeed by calling [Compute.networks_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_networks_available__class_ "Google::Cloud::Compute.networks_available? \(method\)").

#### About Networks

The Networks API.

This client uses Networks version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .networks_available?
    
    
    def self.networks_available?(version: :v1) -> boolean

Determines whether the Networks service is supported by the current client. If true, you can retrieve a client object by calling [Compute.networks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_networks_class_ "Google::Cloud::Compute.networks \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Networks service, or if the versioned client gem needs an update to support the Networks service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .node_groups
    
    
    def self.node_groups(version: :v1, &block) -> ::Object

Create a new client object for NodeGroups.

By default, this returns an instance of [Google::Cloud::Compute::V1::NodeGroups::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NodeGroups-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the NodeGroups service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the NodeGroups service. You can determine whether the method will succeed by calling [Compute.node_groups_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_node_groups_available__class_ "Google::Cloud::Compute.node_groups_available? \(method\)").

#### About NodeGroups

The NodeGroups API.

This client uses NodeGroups version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .node_groups_available?
    
    
    def self.node_groups_available?(version: :v1) -> boolean

Determines whether the NodeGroups service is supported by the current client. If true, you can retrieve a client object by calling [Compute.node_groups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_node_groups_class_ "Google::Cloud::Compute.node_groups \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the NodeGroups service, or if the versioned client gem needs an update to support the NodeGroups service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .node_templates
    
    
    def self.node_templates(version: :v1, &block) -> ::Object

Create a new client object for NodeTemplates.

By default, this returns an instance of [Google::Cloud::Compute::V1::NodeTemplates::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NodeTemplates-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the NodeTemplates service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the NodeTemplates service. You can determine whether the method will succeed by calling [Compute.node_templates_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_node_templates_available__class_ "Google::Cloud::Compute.node_templates_available? \(method\)").

#### About NodeTemplates

The NodeTemplates API.

This client uses NodeTemplates version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .node_templates_available?
    
    
    def self.node_templates_available?(version: :v1) -> boolean

Determines whether the NodeTemplates service is supported by the current client. If true, you can retrieve a client object by calling [Compute.node_templates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_node_templates_class_ "Google::Cloud::Compute.node_templates \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the NodeTemplates service, or if the versioned client gem needs an update to support the NodeTemplates service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .node_types
    
    
    def self.node_types(version: :v1, &block) -> ::Object

Create a new client object for NodeTypes.

By default, this returns an instance of [Google::Cloud::Compute::V1::NodeTypes::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NodeTypes-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the NodeTypes service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the NodeTypes service. You can determine whether the method will succeed by calling [Compute.node_types_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_node_types_available__class_ "Google::Cloud::Compute.node_types_available? \(method\)").

#### About NodeTypes

The NodeTypes API.

This client uses NodeTypes version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .node_types_available?
    
    
    def self.node_types_available?(version: :v1) -> boolean

Determines whether the NodeTypes service is supported by the current client. If true, you can retrieve a client object by calling [Compute.node_types](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_node_types_class_ "Google::Cloud::Compute.node_types \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the NodeTypes service, or if the versioned client gem needs an update to support the NodeTypes service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .organization_security_policies
    
    
    def self.organization_security_policies(version: :v1, &block) -> ::Object

Create a new client object for OrganizationSecurityPolicies.

By default, this returns an instance of [Google::Cloud::Compute::V1::OrganizationSecurityPolicies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-OrganizationSecurityPolicies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the OrganizationSecurityPolicies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the OrganizationSecurityPolicies service. You can determine whether the method will succeed by calling [Compute.organization_security_policies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_organization_security_policies_available__class_ "Google::Cloud::Compute.organization_security_policies_available? \(method\)").

#### About OrganizationSecurityPolicies

The OrganizationSecurityPolicies API.

This client uses OrganizationSecurityPolicies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .organization_security_policies_available?
    
    
    def self.organization_security_policies_available?(version: :v1) -> boolean

Determines whether the OrganizationSecurityPolicies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.organization_security_policies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_organization_security_policies_class_ "Google::Cloud::Compute.organization_security_policies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the OrganizationSecurityPolicies service, or if the versioned client gem needs an update to support the OrganizationSecurityPolicies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .packet_mirrorings
    
    
    def self.packet_mirrorings(version: :v1, &block) -> ::Object

Create a new client object for PacketMirrorings.

By default, this returns an instance of [Google::Cloud::Compute::V1::PacketMirrorings::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-PacketMirrorings-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the PacketMirrorings service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the PacketMirrorings service. You can determine whether the method will succeed by calling [Compute.packet_mirrorings_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_packet_mirrorings_available__class_ "Google::Cloud::Compute.packet_mirrorings_available? \(method\)").

#### About PacketMirrorings

The PacketMirrorings API.

This client uses PacketMirrorings version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .packet_mirrorings_available?
    
    
    def self.packet_mirrorings_available?(version: :v1) -> boolean

Determines whether the PacketMirrorings service is supported by the current client. If true, you can retrieve a client object by calling [Compute.packet_mirrorings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_packet_mirrorings_class_ "Google::Cloud::Compute.packet_mirrorings \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the PacketMirrorings service, or if the versioned client gem needs an update to support the PacketMirrorings service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .preview_features
    
    
    def self.preview_features(version: :v1, &block) -> ::Object

Create a new client object for PreviewFeatures.

By default, this returns an instance of [Google::Cloud::Compute::V1::PreviewFeatures::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-PreviewFeatures-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the PreviewFeatures service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the PreviewFeatures service. You can determine whether the method will succeed by calling [Compute.preview_features_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_preview_features_available__class_ "Google::Cloud::Compute.preview_features_available? \(method\)").

#### About PreviewFeatures

The PreviewFeatures API.

This client uses PreviewFeatures version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .preview_features_available?
    
    
    def self.preview_features_available?(version: :v1) -> boolean

Determines whether the PreviewFeatures service is supported by the current client. If true, you can retrieve a client object by calling [Compute.preview_features](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_preview_features_class_ "Google::Cloud::Compute.preview_features \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the PreviewFeatures service, or if the versioned client gem needs an update to support the PreviewFeatures service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .project_views
    
    
    def self.project_views(version: :v1, &block) -> ::Object

Create a new client object for ProjectViews.

By default, this returns an instance of [Google::Cloud::Compute::V1::ProjectViews::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ProjectViews-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ProjectViews service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the ProjectViews service. You can determine whether the method will succeed by calling [Compute.project_views_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_project_views_available__class_ "Google::Cloud::Compute.project_views_available? \(method\)").

#### About ProjectViews

The ProjectViews API.

This client uses ProjectViews version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .project_views_available?
    
    
    def self.project_views_available?(version: :v1) -> boolean

Determines whether the ProjectViews service is supported by the current client. If true, you can retrieve a client object by calling [Compute.project_views](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_project_views_class_ "Google::Cloud::Compute.project_views \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ProjectViews service, or if the versioned client gem needs an update to support the ProjectViews service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .projects
    
    
    def self.projects(version: :v1, &block) -> ::Object

Create a new client object for Projects.

By default, this returns an instance of [Google::Cloud::Compute::V1::Projects::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Projects-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Projects service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Projects service. You can determine whether the method will succeed by calling [Compute.projects_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_projects_available__class_ "Google::Cloud::Compute.projects_available? \(method\)").

#### About Projects

The Projects API.

This client uses Projects version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .projects_available?
    
    
    def self.projects_available?(version: :v1) -> boolean

Determines whether the Projects service is supported by the current client. If true, you can retrieve a client object by calling [Compute.projects](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_projects_class_ "Google::Cloud::Compute.projects \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Projects service, or if the versioned client gem needs an update to support the Projects service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .public_advertised_prefixes
    
    
    def self.public_advertised_prefixes(version: :v1, &block) -> ::Object

Create a new client object for PublicAdvertisedPrefixes.

By default, this returns an instance of [Google::Cloud::Compute::V1::PublicAdvertisedPrefixes::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-PublicAdvertisedPrefixes-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the PublicAdvertisedPrefixes service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the PublicAdvertisedPrefixes service. You can determine whether the method will succeed by calling [Compute.public_advertised_prefixes_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_public_advertised_prefixes_available__class_ "Google::Cloud::Compute.public_advertised_prefixes_available? \(method\)").

#### About PublicAdvertisedPrefixes

The PublicAdvertisedPrefixes API.

This client uses PublicAdvertisedPrefixes version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .public_advertised_prefixes_available?
    
    
    def self.public_advertised_prefixes_available?(version: :v1) -> boolean

Determines whether the PublicAdvertisedPrefixes service is supported by the current client. If true, you can retrieve a client object by calling [Compute.public_advertised_prefixes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_public_advertised_prefixes_class_ "Google::Cloud::Compute.public_advertised_prefixes \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the PublicAdvertisedPrefixes service, or if the versioned client gem needs an update to support the PublicAdvertisedPrefixes service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .public_delegated_prefixes
    
    
    def self.public_delegated_prefixes(version: :v1, &block) -> ::Object

Create a new client object for PublicDelegatedPrefixes.

By default, this returns an instance of [Google::Cloud::Compute::V1::PublicDelegatedPrefixes::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-PublicDelegatedPrefixes-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the PublicDelegatedPrefixes service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the PublicDelegatedPrefixes service. You can determine whether the method will succeed by calling [Compute.public_delegated_prefixes_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_public_delegated_prefixes_available__class_ "Google::Cloud::Compute.public_delegated_prefixes_available? \(method\)").

#### About PublicDelegatedPrefixes

The PublicDelegatedPrefixes API.

This client uses PublicDelegatedPrefixes version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .public_delegated_prefixes_available?
    
    
    def self.public_delegated_prefixes_available?(version: :v1) -> boolean

Determines whether the PublicDelegatedPrefixes service is supported by the current client. If true, you can retrieve a client object by calling [Compute.public_delegated_prefixes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_public_delegated_prefixes_class_ "Google::Cloud::Compute.public_delegated_prefixes \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the PublicDelegatedPrefixes service, or if the versioned client gem needs an update to support the PublicDelegatedPrefixes service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_autoscalers
    
    
    def self.region_autoscalers(version: :v1, &block) -> ::Object

Create a new client object for RegionAutoscalers.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionAutoscalers::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionAutoscalers-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionAutoscalers service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionAutoscalers service. You can determine whether the method will succeed by calling [Compute.region_autoscalers_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_autoscalers_available__class_ "Google::Cloud::Compute.region_autoscalers_available? \(method\)").

#### About RegionAutoscalers

The RegionAutoscalers API.

This client uses RegionAutoscalers version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_autoscalers_available?
    
    
    def self.region_autoscalers_available?(version: :v1) -> boolean

Determines whether the RegionAutoscalers service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_autoscalers](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_autoscalers_class_ "Google::Cloud::Compute.region_autoscalers \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionAutoscalers service, or if the versioned client gem needs an update to support the RegionAutoscalers service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_backend_buckets
    
    
    def self.region_backend_buckets(version: :v1, &block) -> ::Object

Create a new client object for RegionBackendBuckets.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionBackendBuckets::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionBackendBuckets-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionBackendBuckets service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionBackendBuckets service. You can determine whether the method will succeed by calling [Compute.region_backend_buckets_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_backend_buckets_available__class_ "Google::Cloud::Compute.region_backend_buckets_available? \(method\)").

#### About RegionBackendBuckets

The RegionBackendBuckets API.

This client uses RegionBackendBuckets version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_backend_buckets_available?
    
    
    def self.region_backend_buckets_available?(version: :v1) -> boolean

Determines whether the RegionBackendBuckets service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_backend_buckets](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_backend_buckets_class_ "Google::Cloud::Compute.region_backend_buckets \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionBackendBuckets service, or if the versioned client gem needs an update to support the RegionBackendBuckets service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_backend_services
    
    
    def self.region_backend_services(version: :v1, &block) -> ::Object

Create a new client object for RegionBackendServices.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionBackendServices::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionBackendServices-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionBackendServices service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionBackendServices service. You can determine whether the method will succeed by calling [Compute.region_backend_services_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_backend_services_available__class_ "Google::Cloud::Compute.region_backend_services_available? \(method\)").

#### About RegionBackendServices

The RegionBackendServices API.

This client uses RegionBackendServices version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_backend_services_available?
    
    
    def self.region_backend_services_available?(version: :v1) -> boolean

Determines whether the RegionBackendServices service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_backend_services](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_backend_services_class_ "Google::Cloud::Compute.region_backend_services \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionBackendServices service, or if the versioned client gem needs an update to support the RegionBackendServices service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_commitments
    
    
    def self.region_commitments(version: :v1, &block) -> ::Object

Create a new client object for RegionCommitments.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionCommitments::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionCommitments-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionCommitments service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionCommitments service. You can determine whether the method will succeed by calling [Compute.region_commitments_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_commitments_available__class_ "Google::Cloud::Compute.region_commitments_available? \(method\)").

#### About RegionCommitments

The RegionCommitments API.

This client uses RegionCommitments version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_commitments_available?
    
    
    def self.region_commitments_available?(version: :v1) -> boolean

Determines whether the RegionCommitments service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_commitments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_commitments_class_ "Google::Cloud::Compute.region_commitments \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionCommitments service, or if the versioned client gem needs an update to support the RegionCommitments service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_composite_health_checks
    
    
    def self.region_composite_health_checks(version: :v1, &block) -> ::Object

Create a new client object for RegionCompositeHealthChecks.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionCompositeHealthChecks::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionCompositeHealthChecks-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionCompositeHealthChecks service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionCompositeHealthChecks service. You can determine whether the method will succeed by calling [Compute.region_composite_health_checks_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_composite_health_checks_available__class_ "Google::Cloud::Compute.region_composite_health_checks_available? \(method\)").

#### About RegionCompositeHealthChecks

The RegionCompositeHealthChecks API.

This client uses RegionCompositeHealthChecks version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_composite_health_checks_available?
    
    
    def self.region_composite_health_checks_available?(version: :v1) -> boolean

Determines whether the RegionCompositeHealthChecks service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_composite_health_checks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_composite_health_checks_class_ "Google::Cloud::Compute.region_composite_health_checks \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionCompositeHealthChecks service, or if the versioned client gem needs an update to support the RegionCompositeHealthChecks service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_disk_types
    
    
    def self.region_disk_types(version: :v1, &block) -> ::Object

Create a new client object for RegionDiskTypes.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionDiskTypes::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionDiskTypes-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionDiskTypes service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionDiskTypes service. You can determine whether the method will succeed by calling [Compute.region_disk_types_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_disk_types_available__class_ "Google::Cloud::Compute.region_disk_types_available? \(method\)").

#### About RegionDiskTypes

The RegionDiskTypes API.

This client uses RegionDiskTypes version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_disk_types_available?
    
    
    def self.region_disk_types_available?(version: :v1) -> boolean

Determines whether the RegionDiskTypes service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_disk_types](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_disk_types_class_ "Google::Cloud::Compute.region_disk_types \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionDiskTypes service, or if the versioned client gem needs an update to support the RegionDiskTypes service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_disks
    
    
    def self.region_disks(version: :v1, &block) -> ::Object

Create a new client object for RegionDisks.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionDisks::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionDisks-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionDisks service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionDisks service. You can determine whether the method will succeed by calling [Compute.region_disks_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_disks_available__class_ "Google::Cloud::Compute.region_disks_available? \(method\)").

#### About RegionDisks

The RegionDisks API.

This client uses RegionDisks version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_disks_available?
    
    
    def self.region_disks_available?(version: :v1) -> boolean

Determines whether the RegionDisks service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_disks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_disks_class_ "Google::Cloud::Compute.region_disks \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionDisks service, or if the versioned client gem needs an update to support the RegionDisks service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_health_aggregation_policies
    
    
    def self.region_health_aggregation_policies(version: :v1, &block) -> ::Object

Create a new client object for RegionHealthAggregationPolicies.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionHealthAggregationPolicies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionHealthAggregationPolicies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionHealthAggregationPolicies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionHealthAggregationPolicies service. You can determine whether the method will succeed by calling [Compute.region_health_aggregation_policies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_health_aggregation_policies_available__class_ "Google::Cloud::Compute.region_health_aggregation_policies_available? \(method\)").

#### About RegionHealthAggregationPolicies

The RegionHealthAggregationPolicies API.

This client uses RegionHealthAggregationPolicies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_health_aggregation_policies_available?
    
    
    def self.region_health_aggregation_policies_available?(version: :v1) -> boolean

Determines whether the RegionHealthAggregationPolicies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_health_aggregation_policies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_health_aggregation_policies_class_ "Google::Cloud::Compute.region_health_aggregation_policies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionHealthAggregationPolicies service, or if the versioned client gem needs an update to support the RegionHealthAggregationPolicies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_health_check_services
    
    
    def self.region_health_check_services(version: :v1, &block) -> ::Object

Create a new client object for RegionHealthCheckServices.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionHealthCheckServices::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionHealthCheckServices-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionHealthCheckServices service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionHealthCheckServices service. You can determine whether the method will succeed by calling [Compute.region_health_check_services_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_health_check_services_available__class_ "Google::Cloud::Compute.region_health_check_services_available? \(method\)").

#### About RegionHealthCheckServices

The RegionHealthCheckServices API.

This client uses RegionHealthCheckServices version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_health_check_services_available?
    
    
    def self.region_health_check_services_available?(version: :v1) -> boolean

Determines whether the RegionHealthCheckServices service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_health_check_services](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_health_check_services_class_ "Google::Cloud::Compute.region_health_check_services \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionHealthCheckServices service, or if the versioned client gem needs an update to support the RegionHealthCheckServices service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_health_checks
    
    
    def self.region_health_checks(version: :v1, &block) -> ::Object

Create a new client object for RegionHealthChecks.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionHealthChecks::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionHealthChecks-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionHealthChecks service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionHealthChecks service. You can determine whether the method will succeed by calling [Compute.region_health_checks_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_health_checks_available__class_ "Google::Cloud::Compute.region_health_checks_available? \(method\)").

#### About RegionHealthChecks

The RegionHealthChecks API.

This client uses RegionHealthChecks version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_health_checks_available?
    
    
    def self.region_health_checks_available?(version: :v1) -> boolean

Determines whether the RegionHealthChecks service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_health_checks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_health_checks_class_ "Google::Cloud::Compute.region_health_checks \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionHealthChecks service, or if the versioned client gem needs an update to support the RegionHealthChecks service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_health_sources
    
    
    def self.region_health_sources(version: :v1, &block) -> ::Object

Create a new client object for RegionHealthSources.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionHealthSources::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionHealthSources-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionHealthSources service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionHealthSources service. You can determine whether the method will succeed by calling [Compute.region_health_sources_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_health_sources_available__class_ "Google::Cloud::Compute.region_health_sources_available? \(method\)").

#### About RegionHealthSources

The RegionHealthSources API.

This client uses RegionHealthSources version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_health_sources_available?
    
    
    def self.region_health_sources_available?(version: :v1) -> boolean

Determines whether the RegionHealthSources service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_health_sources](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_health_sources_class_ "Google::Cloud::Compute.region_health_sources \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionHealthSources service, or if the versioned client gem needs an update to support the RegionHealthSources service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_instance_group_manager_resize_requests
    
    
    def self.region_instance_group_manager_resize_requests(version: :v1, &block) -> ::Object

Create a new client object for RegionInstanceGroupManagerResizeRequests.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionInstanceGroupManagerResizeRequests::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionInstanceGroupManagerResizeRequests-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionInstanceGroupManagerResizeRequests service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionInstanceGroupManagerResizeRequests service. You can determine whether the method will succeed by calling [Compute.region_instance_group_manager_resize_requests_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_instance_group_manager_resize_requests_available__class_ "Google::Cloud::Compute.region_instance_group_manager_resize_requests_available? \(method\)").

#### About RegionInstanceGroupManagerResizeRequests

The RegionInstanceGroupManagerResizeRequests API.

This client uses RegionInstanceGroupManagerResizeRequests version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_instance_group_manager_resize_requests_available?
    
    
    def self.region_instance_group_manager_resize_requests_available?(version: :v1) -> boolean

Determines whether the RegionInstanceGroupManagerResizeRequests service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_instance_group_manager_resize_requests](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_instance_group_manager_resize_requests_class_ "Google::Cloud::Compute.region_instance_group_manager_resize_requests \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionInstanceGroupManagerResizeRequests service, or if the versioned client gem needs an update to support the RegionInstanceGroupManagerResizeRequests service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_instance_group_managers
    
    
    def self.region_instance_group_managers(version: :v1, &block) -> ::Object

Create a new client object for RegionInstanceGroupManagers.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionInstanceGroupManagers::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionInstanceGroupManagers-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionInstanceGroupManagers service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionInstanceGroupManagers service. You can determine whether the method will succeed by calling [Compute.region_instance_group_managers_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_instance_group_managers_available__class_ "Google::Cloud::Compute.region_instance_group_managers_available? \(method\)").

#### About RegionInstanceGroupManagers

The RegionInstanceGroupManagers API.

This client uses RegionInstanceGroupManagers version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_instance_group_managers_available?
    
    
    def self.region_instance_group_managers_available?(version: :v1) -> boolean

Determines whether the RegionInstanceGroupManagers service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_instance_group_managers](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_instance_group_managers_class_ "Google::Cloud::Compute.region_instance_group_managers \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionInstanceGroupManagers service, or if the versioned client gem needs an update to support the RegionInstanceGroupManagers service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_instance_groups
    
    
    def self.region_instance_groups(version: :v1, &block) -> ::Object

Create a new client object for RegionInstanceGroups.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionInstanceGroups::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionInstanceGroups-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionInstanceGroups service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionInstanceGroups service. You can determine whether the method will succeed by calling [Compute.region_instance_groups_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_instance_groups_available__class_ "Google::Cloud::Compute.region_instance_groups_available? \(method\)").

#### About RegionInstanceGroups

The RegionInstanceGroups API.

This client uses RegionInstanceGroups version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_instance_groups_available?
    
    
    def self.region_instance_groups_available?(version: :v1) -> boolean

Determines whether the RegionInstanceGroups service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_instance_groups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_instance_groups_class_ "Google::Cloud::Compute.region_instance_groups \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionInstanceGroups service, or if the versioned client gem needs an update to support the RegionInstanceGroups service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_instance_templates
    
    
    def self.region_instance_templates(version: :v1, &block) -> ::Object

Create a new client object for RegionInstanceTemplates.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionInstanceTemplates::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionInstanceTemplates-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionInstanceTemplates service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionInstanceTemplates service. You can determine whether the method will succeed by calling [Compute.region_instance_templates_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_instance_templates_available__class_ "Google::Cloud::Compute.region_instance_templates_available? \(method\)").

#### About RegionInstanceTemplates

The RegionInstanceTemplates API.

This client uses RegionInstanceTemplates version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_instance_templates_available?
    
    
    def self.region_instance_templates_available?(version: :v1) -> boolean

Determines whether the RegionInstanceTemplates service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_instance_templates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_instance_templates_class_ "Google::Cloud::Compute.region_instance_templates \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionInstanceTemplates service, or if the versioned client gem needs an update to support the RegionInstanceTemplates service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_instances
    
    
    def self.region_instances(version: :v1, &block) -> ::Object

Create a new client object for RegionInstances.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionInstances::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionInstances-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionInstances service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionInstances service. You can determine whether the method will succeed by calling [Compute.region_instances_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_instances_available__class_ "Google::Cloud::Compute.region_instances_available? \(method\)").

#### About RegionInstances

The RegionInstances API.

This client uses RegionInstances version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_instances_available?
    
    
    def self.region_instances_available?(version: :v1) -> boolean

Determines whether the RegionInstances service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_instances](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_instances_class_ "Google::Cloud::Compute.region_instances \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionInstances service, or if the versioned client gem needs an update to support the RegionInstances service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_instant_snapshot_groups
    
    
    def self.region_instant_snapshot_groups(version: :v1, &block) -> ::Object

Create a new client object for RegionInstantSnapshotGroups.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionInstantSnapshotGroups::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionInstantSnapshotGroups-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionInstantSnapshotGroups service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionInstantSnapshotGroups service. You can determine whether the method will succeed by calling [Compute.region_instant_snapshot_groups_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_instant_snapshot_groups_available__class_ "Google::Cloud::Compute.region_instant_snapshot_groups_available? \(method\)").

#### About RegionInstantSnapshotGroups

The RegionInstantSnapshotGroups API.

This client uses RegionInstantSnapshotGroups version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_instant_snapshot_groups_available?
    
    
    def self.region_instant_snapshot_groups_available?(version: :v1) -> boolean

Determines whether the RegionInstantSnapshotGroups service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_instant_snapshot_groups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_instant_snapshot_groups_class_ "Google::Cloud::Compute.region_instant_snapshot_groups \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionInstantSnapshotGroups service, or if the versioned client gem needs an update to support the RegionInstantSnapshotGroups service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_instant_snapshots
    
    
    def self.region_instant_snapshots(version: :v1, &block) -> ::Object

Create a new client object for RegionInstantSnapshots.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionInstantSnapshots::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionInstantSnapshots-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionInstantSnapshots service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionInstantSnapshots service. You can determine whether the method will succeed by calling [Compute.region_instant_snapshots_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_instant_snapshots_available__class_ "Google::Cloud::Compute.region_instant_snapshots_available? \(method\)").

#### About RegionInstantSnapshots

The RegionInstantSnapshots API.

This client uses RegionInstantSnapshots version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_instant_snapshots_available?
    
    
    def self.region_instant_snapshots_available?(version: :v1) -> boolean

Determines whether the RegionInstantSnapshots service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_instant_snapshots](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_instant_snapshots_class_ "Google::Cloud::Compute.region_instant_snapshots \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionInstantSnapshots service, or if the versioned client gem needs an update to support the RegionInstantSnapshots service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_network_endpoint_groups
    
    
    def self.region_network_endpoint_groups(version: :v1, &block) -> ::Object

Create a new client object for RegionNetworkEndpointGroups.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionNetworkEndpointGroups::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionNetworkEndpointGroups-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionNetworkEndpointGroups service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionNetworkEndpointGroups service. You can determine whether the method will succeed by calling [Compute.region_network_endpoint_groups_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_network_endpoint_groups_available__class_ "Google::Cloud::Compute.region_network_endpoint_groups_available? \(method\)").

#### About RegionNetworkEndpointGroups

The RegionNetworkEndpointGroups API.

This client uses RegionNetworkEndpointGroups version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_network_endpoint_groups_available?
    
    
    def self.region_network_endpoint_groups_available?(version: :v1) -> boolean

Determines whether the RegionNetworkEndpointGroups service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_network_endpoint_groups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_network_endpoint_groups_class_ "Google::Cloud::Compute.region_network_endpoint_groups \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionNetworkEndpointGroups service, or if the versioned client gem needs an update to support the RegionNetworkEndpointGroups service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_network_firewall_policies
    
    
    def self.region_network_firewall_policies(version: :v1, &block) -> ::Object

Create a new client object for RegionNetworkFirewallPolicies.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionNetworkFirewallPolicies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionNetworkFirewallPolicies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionNetworkFirewallPolicies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionNetworkFirewallPolicies service. You can determine whether the method will succeed by calling [Compute.region_network_firewall_policies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_network_firewall_policies_available__class_ "Google::Cloud::Compute.region_network_firewall_policies_available? \(method\)").

#### About RegionNetworkFirewallPolicies

The RegionNetworkFirewallPolicies API.

This client uses RegionNetworkFirewallPolicies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_network_firewall_policies_available?
    
    
    def self.region_network_firewall_policies_available?(version: :v1) -> boolean

Determines whether the RegionNetworkFirewallPolicies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_network_firewall_policies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_network_firewall_policies_class_ "Google::Cloud::Compute.region_network_firewall_policies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionNetworkFirewallPolicies service, or if the versioned client gem needs an update to support the RegionNetworkFirewallPolicies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_notification_endpoints
    
    
    def self.region_notification_endpoints(version: :v1, &block) -> ::Object

Create a new client object for RegionNotificationEndpoints.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionNotificationEndpoints::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionNotificationEndpoints-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionNotificationEndpoints service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionNotificationEndpoints service. You can determine whether the method will succeed by calling [Compute.region_notification_endpoints_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_notification_endpoints_available__class_ "Google::Cloud::Compute.region_notification_endpoints_available? \(method\)").

#### About RegionNotificationEndpoints

The RegionNotificationEndpoints API.

This client uses RegionNotificationEndpoints version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_notification_endpoints_available?
    
    
    def self.region_notification_endpoints_available?(version: :v1) -> boolean

Determines whether the RegionNotificationEndpoints service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_notification_endpoints](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_notification_endpoints_class_ "Google::Cloud::Compute.region_notification_endpoints \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionNotificationEndpoints service, or if the versioned client gem needs an update to support the RegionNotificationEndpoints service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_operations
    
    
    def self.region_operations(version: :v1, &block) -> ::Object

Create a new client object for RegionOperations.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionOperations::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionOperations-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionOperations service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionOperations service. You can determine whether the method will succeed by calling [Compute.region_operations_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_operations_available__class_ "Google::Cloud::Compute.region_operations_available? \(method\)").

#### About RegionOperations

The RegionOperations API.

This client uses RegionOperations version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_operations_available?
    
    
    def self.region_operations_available?(version: :v1) -> boolean

Determines whether the RegionOperations service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_operations_class_ "Google::Cloud::Compute.region_operations \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionOperations service, or if the versioned client gem needs an update to support the RegionOperations service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_security_policies
    
    
    def self.region_security_policies(version: :v1, &block) -> ::Object

Create a new client object for RegionSecurityPolicies.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionSecurityPolicies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionSecurityPolicies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionSecurityPolicies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionSecurityPolicies service. You can determine whether the method will succeed by calling [Compute.region_security_policies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_security_policies_available__class_ "Google::Cloud::Compute.region_security_policies_available? \(method\)").

#### About RegionSecurityPolicies

The RegionSecurityPolicies API.

This client uses RegionSecurityPolicies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_security_policies_available?
    
    
    def self.region_security_policies_available?(version: :v1) -> boolean

Determines whether the RegionSecurityPolicies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_security_policies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_security_policies_class_ "Google::Cloud::Compute.region_security_policies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionSecurityPolicies service, or if the versioned client gem needs an update to support the RegionSecurityPolicies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_snapshot_settings
    
    
    def self.region_snapshot_settings(version: :v1, &block) -> ::Object

Create a new client object for RegionSnapshotSettings.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionSnapshotSettings::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionSnapshotSettings-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionSnapshotSettings service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionSnapshotSettings service. You can determine whether the method will succeed by calling [Compute.region_snapshot_settings_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_snapshot_settings_available__class_ "Google::Cloud::Compute.region_snapshot_settings_available? \(method\)").

#### About RegionSnapshotSettings

The RegionSnapshotSettings API.

This client uses RegionSnapshotSettings version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_snapshot_settings_available?
    
    
    def self.region_snapshot_settings_available?(version: :v1) -> boolean

Determines whether the RegionSnapshotSettings service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_snapshot_settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_snapshot_settings_class_ "Google::Cloud::Compute.region_snapshot_settings \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionSnapshotSettings service, or if the versioned client gem needs an update to support the RegionSnapshotSettings service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_snapshots
    
    
    def self.region_snapshots(version: :v1, &block) -> ::Object

Create a new client object for RegionSnapshots.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionSnapshots::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionSnapshots-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionSnapshots service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionSnapshots service. You can determine whether the method will succeed by calling [Compute.region_snapshots_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_snapshots_available__class_ "Google::Cloud::Compute.region_snapshots_available? \(method\)").

#### About RegionSnapshots

The RegionSnapshots API.

This client uses RegionSnapshots version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_snapshots_available?
    
    
    def self.region_snapshots_available?(version: :v1) -> boolean

Determines whether the RegionSnapshots service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_snapshots](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_snapshots_class_ "Google::Cloud::Compute.region_snapshots \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionSnapshots service, or if the versioned client gem needs an update to support the RegionSnapshots service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_ssl_certificates
    
    
    def self.region_ssl_certificates(version: :v1, &block) -> ::Object

Create a new client object for RegionSslCertificates.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionSslCertificates::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionSslCertificates-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionSslCertificates service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionSslCertificates service. You can determine whether the method will succeed by calling [Compute.region_ssl_certificates_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_ssl_certificates_available__class_ "Google::Cloud::Compute.region_ssl_certificates_available? \(method\)").

#### About RegionSslCertificates

The RegionSslCertificates API.

This client uses RegionSslCertificates version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_ssl_certificates_available?
    
    
    def self.region_ssl_certificates_available?(version: :v1) -> boolean

Determines whether the RegionSslCertificates service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_ssl_certificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_ssl_certificates_class_ "Google::Cloud::Compute.region_ssl_certificates \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionSslCertificates service, or if the versioned client gem needs an update to support the RegionSslCertificates service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_ssl_policies
    
    
    def self.region_ssl_policies(version: :v1, &block) -> ::Object

Create a new client object for RegionSslPolicies.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionSslPolicies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionSslPolicies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionSslPolicies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionSslPolicies service. You can determine whether the method will succeed by calling [Compute.region_ssl_policies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_ssl_policies_available__class_ "Google::Cloud::Compute.region_ssl_policies_available? \(method\)").

#### About RegionSslPolicies

The RegionSslPolicies API.

This client uses RegionSslPolicies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_ssl_policies_available?
    
    
    def self.region_ssl_policies_available?(version: :v1) -> boolean

Determines whether the RegionSslPolicies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_ssl_policies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_ssl_policies_class_ "Google::Cloud::Compute.region_ssl_policies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionSslPolicies service, or if the versioned client gem needs an update to support the RegionSslPolicies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_target_http_proxies
    
    
    def self.region_target_http_proxies(version: :v1, &block) -> ::Object

Create a new client object for RegionTargetHttpProxies.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionTargetHttpProxies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionTargetHttpProxies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionTargetHttpProxies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionTargetHttpProxies service. You can determine whether the method will succeed by calling [Compute.region_target_http_proxies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_target_http_proxies_available__class_ "Google::Cloud::Compute.region_target_http_proxies_available? \(method\)").

#### About RegionTargetHttpProxies

The RegionTargetHttpProxies API.

This client uses RegionTargetHttpProxies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_target_http_proxies_available?
    
    
    def self.region_target_http_proxies_available?(version: :v1) -> boolean

Determines whether the RegionTargetHttpProxies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_target_http_proxies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_target_http_proxies_class_ "Google::Cloud::Compute.region_target_http_proxies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionTargetHttpProxies service, or if the versioned client gem needs an update to support the RegionTargetHttpProxies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_target_https_proxies
    
    
    def self.region_target_https_proxies(version: :v1, &block) -> ::Object

Create a new client object for RegionTargetHttpsProxies.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionTargetHttpsProxies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionTargetHttpsProxies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionTargetHttpsProxies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionTargetHttpsProxies service. You can determine whether the method will succeed by calling [Compute.region_target_https_proxies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_target_https_proxies_available__class_ "Google::Cloud::Compute.region_target_https_proxies_available? \(method\)").

#### About RegionTargetHttpsProxies

The RegionTargetHttpsProxies API.

This client uses RegionTargetHttpsProxies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_target_https_proxies_available?
    
    
    def self.region_target_https_proxies_available?(version: :v1) -> boolean

Determines whether the RegionTargetHttpsProxies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_target_https_proxies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_target_https_proxies_class_ "Google::Cloud::Compute.region_target_https_proxies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionTargetHttpsProxies service, or if the versioned client gem needs an update to support the RegionTargetHttpsProxies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_target_tcp_proxies
    
    
    def self.region_target_tcp_proxies(version: :v1, &block) -> ::Object

Create a new client object for RegionTargetTcpProxies.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionTargetTcpProxies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionTargetTcpProxies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionTargetTcpProxies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionTargetTcpProxies service. You can determine whether the method will succeed by calling [Compute.region_target_tcp_proxies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_target_tcp_proxies_available__class_ "Google::Cloud::Compute.region_target_tcp_proxies_available? \(method\)").

#### About RegionTargetTcpProxies

The RegionTargetTcpProxies API.

This client uses RegionTargetTcpProxies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_target_tcp_proxies_available?
    
    
    def self.region_target_tcp_proxies_available?(version: :v1) -> boolean

Determines whether the RegionTargetTcpProxies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_target_tcp_proxies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_target_tcp_proxies_class_ "Google::Cloud::Compute.region_target_tcp_proxies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionTargetTcpProxies service, or if the versioned client gem needs an update to support the RegionTargetTcpProxies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_url_maps
    
    
    def self.region_url_maps(version: :v1, &block) -> ::Object

Create a new client object for RegionUrlMaps.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionUrlMaps::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionUrlMaps-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionUrlMaps service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionUrlMaps service. You can determine whether the method will succeed by calling [Compute.region_url_maps_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_url_maps_available__class_ "Google::Cloud::Compute.region_url_maps_available? \(method\)").

#### About RegionUrlMaps

The RegionUrlMaps API.

This client uses RegionUrlMaps version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_url_maps_available?
    
    
    def self.region_url_maps_available?(version: :v1) -> boolean

Determines whether the RegionUrlMaps service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_url_maps](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_url_maps_class_ "Google::Cloud::Compute.region_url_maps \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionUrlMaps service, or if the versioned client gem needs an update to support the RegionUrlMaps service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .region_zones
    
    
    def self.region_zones(version: :v1, &block) -> ::Object

Create a new client object for RegionZones.

By default, this returns an instance of [Google::Cloud::Compute::V1::RegionZones::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionZones-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RegionZones service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RegionZones service. You can determine whether the method will succeed by calling [Compute.region_zones_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_zones_available__class_ "Google::Cloud::Compute.region_zones_available? \(method\)").

#### About RegionZones

The RegionZones API.

This client uses RegionZones version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .region_zones_available?
    
    
    def self.region_zones_available?(version: :v1) -> boolean

Determines whether the RegionZones service is supported by the current client. If true, you can retrieve a client object by calling [Compute.region_zones](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_region_zones_class_ "Google::Cloud::Compute.region_zones \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RegionZones service, or if the versioned client gem needs an update to support the RegionZones service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .regions
    
    
    def self.regions(version: :v1, &block) -> ::Object

Create a new client object for Regions.

By default, this returns an instance of [Google::Cloud::Compute::V1::Regions::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Regions-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Regions service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Regions service. You can determine whether the method will succeed by calling [Compute.regions_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_regions_available__class_ "Google::Cloud::Compute.regions_available? \(method\)").

#### About Regions

The Regions API.

This client uses Regions version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .regions_available?
    
    
    def self.regions_available?(version: :v1) -> boolean

Determines whether the Regions service is supported by the current client. If true, you can retrieve a client object by calling [Compute.regions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_regions_class_ "Google::Cloud::Compute.regions \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Regions service, or if the versioned client gem needs an update to support the Regions service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .reliability_risks
    
    
    def self.reliability_risks(version: :v1, &block) -> ::Object

Create a new client object for ReliabilityRisks.

By default, this returns an instance of [Google::Cloud::Compute::V1::ReliabilityRisks::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReliabilityRisks-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ReliabilityRisks service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the ReliabilityRisks service. You can determine whether the method will succeed by calling [Compute.reliability_risks_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_reliability_risks_available__class_ "Google::Cloud::Compute.reliability_risks_available? \(method\)").

#### About ReliabilityRisks

The ReliabilityRisks API.

This client uses ReliabilityRisks version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .reliability_risks_available?
    
    
    def self.reliability_risks_available?(version: :v1) -> boolean

Determines whether the ReliabilityRisks service is supported by the current client. If true, you can retrieve a client object by calling [Compute.reliability_risks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_reliability_risks_class_ "Google::Cloud::Compute.reliability_risks \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ReliabilityRisks service, or if the versioned client gem needs an update to support the ReliabilityRisks service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .reservation_blocks
    
    
    def self.reservation_blocks(version: :v1, &block) -> ::Object

Create a new client object for ReservationBlocks.

By default, this returns an instance of [Google::Cloud::Compute::V1::ReservationBlocks::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationBlocks-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ReservationBlocks service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the ReservationBlocks service. You can determine whether the method will succeed by calling [Compute.reservation_blocks_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_reservation_blocks_available__class_ "Google::Cloud::Compute.reservation_blocks_available? \(method\)").

#### About ReservationBlocks

The ReservationBlocks API.

This client uses ReservationBlocks version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .reservation_blocks_available?
    
    
    def self.reservation_blocks_available?(version: :v1) -> boolean

Determines whether the ReservationBlocks service is supported by the current client. If true, you can retrieve a client object by calling [Compute.reservation_blocks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_reservation_blocks_class_ "Google::Cloud::Compute.reservation_blocks \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ReservationBlocks service, or if the versioned client gem needs an update to support the ReservationBlocks service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .reservation_slots
    
    
    def self.reservation_slots(version: :v1, &block) -> ::Object

Create a new client object for ReservationSlots.

By default, this returns an instance of [Google::Cloud::Compute::V1::ReservationSlots::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSlots-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ReservationSlots service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the ReservationSlots service. You can determine whether the method will succeed by calling [Compute.reservation_slots_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_reservation_slots_available__class_ "Google::Cloud::Compute.reservation_slots_available? \(method\)").

#### About ReservationSlots

The ReservationSlots API.

This client uses ReservationSlots version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .reservation_slots_available?
    
    
    def self.reservation_slots_available?(version: :v1) -> boolean

Determines whether the ReservationSlots service is supported by the current client. If true, you can retrieve a client object by calling [Compute.reservation_slots](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_reservation_slots_class_ "Google::Cloud::Compute.reservation_slots \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ReservationSlots service, or if the versioned client gem needs an update to support the ReservationSlots service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .reservation_sub_blocks
    
    
    def self.reservation_sub_blocks(version: :v1, &block) -> ::Object

Create a new client object for ReservationSubBlocks.

By default, this returns an instance of [Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocks-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ReservationSubBlocks service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the ReservationSubBlocks service. You can determine whether the method will succeed by calling [Compute.reservation_sub_blocks_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_reservation_sub_blocks_available__class_ "Google::Cloud::Compute.reservation_sub_blocks_available? \(method\)").

#### About ReservationSubBlocks

The ReservationSubBlocks API.

This client uses ReservationSubBlocks version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .reservation_sub_blocks_available?
    
    
    def self.reservation_sub_blocks_available?(version: :v1) -> boolean

Determines whether the ReservationSubBlocks service is supported by the current client. If true, you can retrieve a client object by calling [Compute.reservation_sub_blocks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_reservation_sub_blocks_class_ "Google::Cloud::Compute.reservation_sub_blocks \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ReservationSubBlocks service, or if the versioned client gem needs an update to support the ReservationSubBlocks service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .reservations
    
    
    def self.reservations(version: :v1, &block) -> ::Object

Create a new client object for Reservations.

By default, this returns an instance of [Google::Cloud::Compute::V1::Reservations::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Reservations-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Reservations service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Reservations service. You can determine whether the method will succeed by calling [Compute.reservations_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_reservations_available__class_ "Google::Cloud::Compute.reservations_available? \(method\)").

#### About Reservations

The Reservations API.

This client uses Reservations version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .reservations_available?
    
    
    def self.reservations_available?(version: :v1) -> boolean

Determines whether the Reservations service is supported by the current client. If true, you can retrieve a client object by calling [Compute.reservations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_reservations_class_ "Google::Cloud::Compute.reservations \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Reservations service, or if the versioned client gem needs an update to support the Reservations service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .resource_policies
    
    
    def self.resource_policies(version: :v1, &block) -> ::Object

Create a new client object for ResourcePolicies.

By default, this returns an instance of [Google::Cloud::Compute::V1::ResourcePolicies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ResourcePolicies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ResourcePolicies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the ResourcePolicies service. You can determine whether the method will succeed by calling [Compute.resource_policies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_resource_policies_available__class_ "Google::Cloud::Compute.resource_policies_available? \(method\)").

#### About ResourcePolicies

The ResourcePolicies API.

This client uses ResourcePolicies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .resource_policies_available?
    
    
    def self.resource_policies_available?(version: :v1) -> boolean

Determines whether the ResourcePolicies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.resource_policies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_resource_policies_class_ "Google::Cloud::Compute.resource_policies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ResourcePolicies service, or if the versioned client gem needs an update to support the ResourcePolicies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .rollout_plans
    
    
    def self.rollout_plans(version: :v1, &block) -> ::Object

Create a new client object for RolloutPlans.

By default, this returns an instance of [Google::Cloud::Compute::V1::RolloutPlans::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RolloutPlans-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the RolloutPlans service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the RolloutPlans service. You can determine whether the method will succeed by calling [Compute.rollout_plans_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_rollout_plans_available__class_ "Google::Cloud::Compute.rollout_plans_available? \(method\)").

#### About RolloutPlans

The RolloutPlans API.

This client uses RolloutPlans version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .rollout_plans_available?
    
    
    def self.rollout_plans_available?(version: :v1) -> boolean

Determines whether the RolloutPlans service is supported by the current client. If true, you can retrieve a client object by calling [Compute.rollout_plans](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_rollout_plans_class_ "Google::Cloud::Compute.rollout_plans \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the RolloutPlans service, or if the versioned client gem needs an update to support the RolloutPlans service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .rollouts
    
    
    def self.rollouts(version: :v1, &block) -> ::Object

Create a new client object for Rollouts.

By default, this returns an instance of [Google::Cloud::Compute::V1::Rollouts::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Rollouts-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Rollouts service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Rollouts service. You can determine whether the method will succeed by calling [Compute.rollouts_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_rollouts_available__class_ "Google::Cloud::Compute.rollouts_available? \(method\)").

#### About Rollouts

The Rollouts API.

This client uses Rollouts version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .rollouts_available?
    
    
    def self.rollouts_available?(version: :v1) -> boolean

Determines whether the Rollouts service is supported by the current client. If true, you can retrieve a client object by calling [Compute.rollouts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_rollouts_class_ "Google::Cloud::Compute.rollouts \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Rollouts service, or if the versioned client gem needs an update to support the Rollouts service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .routers
    
    
    def self.routers(version: :v1, &block) -> ::Object

Create a new client object for Routers.

By default, this returns an instance of [Google::Cloud::Compute::V1::Routers::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Routers-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Routers service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Routers service. You can determine whether the method will succeed by calling [Compute.routers_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_routers_available__class_ "Google::Cloud::Compute.routers_available? \(method\)").

#### About Routers

The Routers API.

This client uses Routers version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .routers_available?
    
    
    def self.routers_available?(version: :v1) -> boolean

Determines whether the Routers service is supported by the current client. If true, you can retrieve a client object by calling [Compute.routers](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_routers_class_ "Google::Cloud::Compute.routers \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Routers service, or if the versioned client gem needs an update to support the Routers service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .routes
    
    
    def self.routes(version: :v1, &block) -> ::Object

Create a new client object for Routes.

By default, this returns an instance of [Google::Cloud::Compute::V1::Routes::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Routes-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Routes service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Routes service. You can determine whether the method will succeed by calling [Compute.routes_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_routes_available__class_ "Google::Cloud::Compute.routes_available? \(method\)").

#### About Routes

The Routes API.

This client uses Routes version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .routes_available?
    
    
    def self.routes_available?(version: :v1) -> boolean

Determines whether the Routes service is supported by the current client. If true, you can retrieve a client object by calling [Compute.routes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_routes_class_ "Google::Cloud::Compute.routes \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Routes service, or if the versioned client gem needs an update to support the Routes service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .security_policies
    
    
    def self.security_policies(version: :v1, &block) -> ::Object

Create a new client object for SecurityPolicies.

By default, this returns an instance of [Google::Cloud::Compute::V1::SecurityPolicies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SecurityPolicies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the SecurityPolicies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the SecurityPolicies service. You can determine whether the method will succeed by calling [Compute.security_policies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_security_policies_available__class_ "Google::Cloud::Compute.security_policies_available? \(method\)").

#### About SecurityPolicies

The SecurityPolicies API.

This client uses SecurityPolicies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .security_policies_available?
    
    
    def self.security_policies_available?(version: :v1) -> boolean

Determines whether the SecurityPolicies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.security_policies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_security_policies_class_ "Google::Cloud::Compute.security_policies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the SecurityPolicies service, or if the versioned client gem needs an update to support the SecurityPolicies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .service_attachments
    
    
    def self.service_attachments(version: :v1, &block) -> ::Object

Create a new client object for ServiceAttachments.

By default, this returns an instance of [Google::Cloud::Compute::V1::ServiceAttachments::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ServiceAttachments-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ServiceAttachments service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the ServiceAttachments service. You can determine whether the method will succeed by calling [Compute.service_attachments_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_service_attachments_available__class_ "Google::Cloud::Compute.service_attachments_available? \(method\)").

#### About ServiceAttachments

The ServiceAttachments API.

This client uses ServiceAttachments version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .service_attachments_available?
    
    
    def self.service_attachments_available?(version: :v1) -> boolean

Determines whether the ServiceAttachments service is supported by the current client. If true, you can retrieve a client object by calling [Compute.service_attachments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_service_attachments_class_ "Google::Cloud::Compute.service_attachments \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ServiceAttachments service, or if the versioned client gem needs an update to support the ServiceAttachments service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .snapshot_settings_service
    
    
    def self.snapshot_settings_service(version: :v1, &block) -> ::Object

Create a new client object for SnapshotSettingsService.

By default, this returns an instance of [Google::Cloud::Compute::V1::SnapshotSettingsService::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SnapshotSettingsService-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the SnapshotSettingsService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the SnapshotSettingsService service. You can determine whether the method will succeed by calling [Compute.snapshot_settings_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_snapshot_settings_service_available__class_ "Google::Cloud::Compute.snapshot_settings_service_available? \(method\)").

#### About SnapshotSettingsService

The SnapshotSettings API.

This client uses SnapshotSettingsService version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .snapshot_settings_service_available?
    
    
    def self.snapshot_settings_service_available?(version: :v1) -> boolean

Determines whether the SnapshotSettingsService service is supported by the current client. If true, you can retrieve a client object by calling [Compute.snapshot_settings_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_snapshot_settings_service_class_ "Google::Cloud::Compute.snapshot_settings_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the SnapshotSettingsService service, or if the versioned client gem needs an update to support the SnapshotSettingsService service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .snapshots
    
    
    def self.snapshots(version: :v1, &block) -> ::Object

Create a new client object for Snapshots.

By default, this returns an instance of [Google::Cloud::Compute::V1::Snapshots::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Snapshots-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Snapshots service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Snapshots service. You can determine whether the method will succeed by calling [Compute.snapshots_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_snapshots_available__class_ "Google::Cloud::Compute.snapshots_available? \(method\)").

#### About Snapshots

The Snapshots API.

This client uses Snapshots version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .snapshots_available?
    
    
    def self.snapshots_available?(version: :v1) -> boolean

Determines whether the Snapshots service is supported by the current client. If true, you can retrieve a client object by calling [Compute.snapshots](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_snapshots_class_ "Google::Cloud::Compute.snapshots \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Snapshots service, or if the versioned client gem needs an update to support the Snapshots service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .ssl_certificates
    
    
    def self.ssl_certificates(version: :v1, &block) -> ::Object

Create a new client object for SslCertificates.

By default, this returns an instance of [Google::Cloud::Compute::V1::SslCertificates::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SslCertificates-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the SslCertificates service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the SslCertificates service. You can determine whether the method will succeed by calling [Compute.ssl_certificates_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_ssl_certificates_available__class_ "Google::Cloud::Compute.ssl_certificates_available? \(method\)").

#### About SslCertificates

The SslCertificates API.

This client uses SslCertificates version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .ssl_certificates_available?
    
    
    def self.ssl_certificates_available?(version: :v1) -> boolean

Determines whether the SslCertificates service is supported by the current client. If true, you can retrieve a client object by calling [Compute.ssl_certificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_ssl_certificates_class_ "Google::Cloud::Compute.ssl_certificates \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the SslCertificates service, or if the versioned client gem needs an update to support the SslCertificates service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .ssl_policies
    
    
    def self.ssl_policies(version: :v1, &block) -> ::Object

Create a new client object for SslPolicies.

By default, this returns an instance of [Google::Cloud::Compute::V1::SslPolicies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SslPolicies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the SslPolicies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the SslPolicies service. You can determine whether the method will succeed by calling [Compute.ssl_policies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_ssl_policies_available__class_ "Google::Cloud::Compute.ssl_policies_available? \(method\)").

#### About SslPolicies

The SslPolicies API.

This client uses SslPolicies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .ssl_policies_available?
    
    
    def self.ssl_policies_available?(version: :v1) -> boolean

Determines whether the SslPolicies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.ssl_policies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_ssl_policies_class_ "Google::Cloud::Compute.ssl_policies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the SslPolicies service, or if the versioned client gem needs an update to support the SslPolicies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .storage_pool_types
    
    
    def self.storage_pool_types(version: :v1, &block) -> ::Object

Create a new client object for StoragePoolTypes.

By default, this returns an instance of [Google::Cloud::Compute::V1::StoragePoolTypes::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-StoragePoolTypes-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the StoragePoolTypes service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the StoragePoolTypes service. You can determine whether the method will succeed by calling [Compute.storage_pool_types_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_storage_pool_types_available__class_ "Google::Cloud::Compute.storage_pool_types_available? \(method\)").

#### About StoragePoolTypes

The StoragePoolTypes API.

This client uses StoragePoolTypes version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .storage_pool_types_available?
    
    
    def self.storage_pool_types_available?(version: :v1) -> boolean

Determines whether the StoragePoolTypes service is supported by the current client. If true, you can retrieve a client object by calling [Compute.storage_pool_types](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_storage_pool_types_class_ "Google::Cloud::Compute.storage_pool_types \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the StoragePoolTypes service, or if the versioned client gem needs an update to support the StoragePoolTypes service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .storage_pools
    
    
    def self.storage_pools(version: :v1, &block) -> ::Object

Create a new client object for StoragePools.

By default, this returns an instance of [Google::Cloud::Compute::V1::StoragePools::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-StoragePools-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the StoragePools service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the StoragePools service. You can determine whether the method will succeed by calling [Compute.storage_pools_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_storage_pools_available__class_ "Google::Cloud::Compute.storage_pools_available? \(method\)").

#### About StoragePools

The StoragePools API.

This client uses StoragePools version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .storage_pools_available?
    
    
    def self.storage_pools_available?(version: :v1) -> boolean

Determines whether the StoragePools service is supported by the current client. If true, you can retrieve a client object by calling [Compute.storage_pools](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_storage_pools_class_ "Google::Cloud::Compute.storage_pools \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the StoragePools service, or if the versioned client gem needs an update to support the StoragePools service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .subnetworks
    
    
    def self.subnetworks(version: :v1, &block) -> ::Object

Create a new client object for Subnetworks.

By default, this returns an instance of [Google::Cloud::Compute::V1::Subnetworks::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Subnetworks-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Subnetworks service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Subnetworks service. You can determine whether the method will succeed by calling [Compute.subnetworks_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_subnetworks_available__class_ "Google::Cloud::Compute.subnetworks_available? \(method\)").

#### About Subnetworks

The Subnetworks API.

This client uses Subnetworks version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .subnetworks_available?
    
    
    def self.subnetworks_available?(version: :v1) -> boolean

Determines whether the Subnetworks service is supported by the current client. If true, you can retrieve a client object by calling [Compute.subnetworks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_subnetworks_class_ "Google::Cloud::Compute.subnetworks \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Subnetworks service, or if the versioned client gem needs an update to support the Subnetworks service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .target_grpc_proxies
    
    
    def self.target_grpc_proxies(version: :v1, &block) -> ::Object

Create a new client object for TargetGrpcProxies.

By default, this returns an instance of [Google::Cloud::Compute::V1::TargetGrpcProxies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TargetGrpcProxies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the TargetGrpcProxies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the TargetGrpcProxies service. You can determine whether the method will succeed by calling [Compute.target_grpc_proxies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_grpc_proxies_available__class_ "Google::Cloud::Compute.target_grpc_proxies_available? \(method\)").

#### About TargetGrpcProxies

The TargetGrpcProxies API.

This client uses TargetGrpcProxies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .target_grpc_proxies_available?
    
    
    def self.target_grpc_proxies_available?(version: :v1) -> boolean

Determines whether the TargetGrpcProxies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.target_grpc_proxies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_grpc_proxies_class_ "Google::Cloud::Compute.target_grpc_proxies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the TargetGrpcProxies service, or if the versioned client gem needs an update to support the TargetGrpcProxies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .target_http_proxies
    
    
    def self.target_http_proxies(version: :v1, &block) -> ::Object

Create a new client object for TargetHttpProxies.

By default, this returns an instance of [Google::Cloud::Compute::V1::TargetHttpProxies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TargetHttpProxies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the TargetHttpProxies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the TargetHttpProxies service. You can determine whether the method will succeed by calling [Compute.target_http_proxies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_http_proxies_available__class_ "Google::Cloud::Compute.target_http_proxies_available? \(method\)").

#### About TargetHttpProxies

The TargetHttpProxies API.

This client uses TargetHttpProxies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .target_http_proxies_available?
    
    
    def self.target_http_proxies_available?(version: :v1) -> boolean

Determines whether the TargetHttpProxies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.target_http_proxies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_http_proxies_class_ "Google::Cloud::Compute.target_http_proxies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the TargetHttpProxies service, or if the versioned client gem needs an update to support the TargetHttpProxies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .target_https_proxies
    
    
    def self.target_https_proxies(version: :v1, &block) -> ::Object

Create a new client object for TargetHttpsProxies.

By default, this returns an instance of [Google::Cloud::Compute::V1::TargetHttpsProxies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TargetHttpsProxies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the TargetHttpsProxies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the TargetHttpsProxies service. You can determine whether the method will succeed by calling [Compute.target_https_proxies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_https_proxies_available__class_ "Google::Cloud::Compute.target_https_proxies_available? \(method\)").

#### About TargetHttpsProxies

The TargetHttpsProxies API.

This client uses TargetHttpsProxies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .target_https_proxies_available?
    
    
    def self.target_https_proxies_available?(version: :v1) -> boolean

Determines whether the TargetHttpsProxies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.target_https_proxies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_https_proxies_class_ "Google::Cloud::Compute.target_https_proxies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the TargetHttpsProxies service, or if the versioned client gem needs an update to support the TargetHttpsProxies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .target_instances
    
    
    def self.target_instances(version: :v1, &block) -> ::Object

Create a new client object for TargetInstances.

By default, this returns an instance of [Google::Cloud::Compute::V1::TargetInstances::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TargetInstances-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the TargetInstances service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the TargetInstances service. You can determine whether the method will succeed by calling [Compute.target_instances_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_instances_available__class_ "Google::Cloud::Compute.target_instances_available? \(method\)").

#### About TargetInstances

The TargetInstances API.

This client uses TargetInstances version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .target_instances_available?
    
    
    def self.target_instances_available?(version: :v1) -> boolean

Determines whether the TargetInstances service is supported by the current client. If true, you can retrieve a client object by calling [Compute.target_instances](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_instances_class_ "Google::Cloud::Compute.target_instances \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the TargetInstances service, or if the versioned client gem needs an update to support the TargetInstances service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .target_pools
    
    
    def self.target_pools(version: :v1, &block) -> ::Object

Create a new client object for TargetPools.

By default, this returns an instance of [Google::Cloud::Compute::V1::TargetPools::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TargetPools-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the TargetPools service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the TargetPools service. You can determine whether the method will succeed by calling [Compute.target_pools_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_pools_available__class_ "Google::Cloud::Compute.target_pools_available? \(method\)").

#### About TargetPools

The TargetPools API.

This client uses TargetPools version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .target_pools_available?
    
    
    def self.target_pools_available?(version: :v1) -> boolean

Determines whether the TargetPools service is supported by the current client. If true, you can retrieve a client object by calling [Compute.target_pools](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_pools_class_ "Google::Cloud::Compute.target_pools \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the TargetPools service, or if the versioned client gem needs an update to support the TargetPools service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .target_ssl_proxies
    
    
    def self.target_ssl_proxies(version: :v1, &block) -> ::Object

Create a new client object for TargetSslProxies.

By default, this returns an instance of [Google::Cloud::Compute::V1::TargetSslProxies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TargetSslProxies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the TargetSslProxies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the TargetSslProxies service. You can determine whether the method will succeed by calling [Compute.target_ssl_proxies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_ssl_proxies_available__class_ "Google::Cloud::Compute.target_ssl_proxies_available? \(method\)").

#### About TargetSslProxies

The TargetSslProxies API.

This client uses TargetSslProxies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .target_ssl_proxies_available?
    
    
    def self.target_ssl_proxies_available?(version: :v1) -> boolean

Determines whether the TargetSslProxies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.target_ssl_proxies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_ssl_proxies_class_ "Google::Cloud::Compute.target_ssl_proxies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the TargetSslProxies service, or if the versioned client gem needs an update to support the TargetSslProxies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .target_tcp_proxies
    
    
    def self.target_tcp_proxies(version: :v1, &block) -> ::Object

Create a new client object for TargetTcpProxies.

By default, this returns an instance of [Google::Cloud::Compute::V1::TargetTcpProxies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TargetTcpProxies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the TargetTcpProxies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the TargetTcpProxies service. You can determine whether the method will succeed by calling [Compute.target_tcp_proxies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_tcp_proxies_available__class_ "Google::Cloud::Compute.target_tcp_proxies_available? \(method\)").

#### About TargetTcpProxies

The TargetTcpProxies API.

This client uses TargetTcpProxies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .target_tcp_proxies_available?
    
    
    def self.target_tcp_proxies_available?(version: :v1) -> boolean

Determines whether the TargetTcpProxies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.target_tcp_proxies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_tcp_proxies_class_ "Google::Cloud::Compute.target_tcp_proxies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the TargetTcpProxies service, or if the versioned client gem needs an update to support the TargetTcpProxies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .target_vpn_gateways
    
    
    def self.target_vpn_gateways(version: :v1, &block) -> ::Object

Create a new client object for TargetVpnGateways.

By default, this returns an instance of [Google::Cloud::Compute::V1::TargetVpnGateways::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TargetVpnGateways-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the TargetVpnGateways service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the TargetVpnGateways service. You can determine whether the method will succeed by calling [Compute.target_vpn_gateways_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_vpn_gateways_available__class_ "Google::Cloud::Compute.target_vpn_gateways_available? \(method\)").

#### About TargetVpnGateways

The TargetVpnGateways API.

This client uses TargetVpnGateways version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .target_vpn_gateways_available?
    
    
    def self.target_vpn_gateways_available?(version: :v1) -> boolean

Determines whether the TargetVpnGateways service is supported by the current client. If true, you can retrieve a client object by calling [Compute.target_vpn_gateways](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_target_vpn_gateways_class_ "Google::Cloud::Compute.target_vpn_gateways \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the TargetVpnGateways service, or if the versioned client gem needs an update to support the TargetVpnGateways service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .url_maps
    
    
    def self.url_maps(version: :v1, &block) -> ::Object

Create a new client object for UrlMaps.

By default, this returns an instance of [Google::Cloud::Compute::V1::UrlMaps::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-UrlMaps-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the UrlMaps service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the UrlMaps service. You can determine whether the method will succeed by calling [Compute.url_maps_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_url_maps_available__class_ "Google::Cloud::Compute.url_maps_available? \(method\)").

#### About UrlMaps

The UrlMaps API.

This client uses UrlMaps version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .url_maps_available?
    
    
    def self.url_maps_available?(version: :v1) -> boolean

Determines whether the UrlMaps service is supported by the current client. If true, you can retrieve a client object by calling [Compute.url_maps](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_url_maps_class_ "Google::Cloud::Compute.url_maps \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the UrlMaps service, or if the versioned client gem needs an update to support the UrlMaps service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .vpn_gateways
    
    
    def self.vpn_gateways(version: :v1, &block) -> ::Object

Create a new client object for VpnGateways.

By default, this returns an instance of [Google::Cloud::Compute::V1::VpnGateways::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-VpnGateways-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the VpnGateways service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the VpnGateways service. You can determine whether the method will succeed by calling [Compute.vpn_gateways_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_vpn_gateways_available__class_ "Google::Cloud::Compute.vpn_gateways_available? \(method\)").

#### About VpnGateways

The VpnGateways API.

This client uses VpnGateways version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .vpn_gateways_available?
    
    
    def self.vpn_gateways_available?(version: :v1) -> boolean

Determines whether the VpnGateways service is supported by the current client. If true, you can retrieve a client object by calling [Compute.vpn_gateways](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_vpn_gateways_class_ "Google::Cloud::Compute.vpn_gateways \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the VpnGateways service, or if the versioned client gem needs an update to support the VpnGateways service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .vpn_tunnels
    
    
    def self.vpn_tunnels(version: :v1, &block) -> ::Object

Create a new client object for VpnTunnels.

By default, this returns an instance of [Google::Cloud::Compute::V1::VpnTunnels::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-VpnTunnels-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the VpnTunnels service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the VpnTunnels service. You can determine whether the method will succeed by calling [Compute.vpn_tunnels_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_vpn_tunnels_available__class_ "Google::Cloud::Compute.vpn_tunnels_available? \(method\)").

#### About VpnTunnels

The VpnTunnels API.

This client uses VpnTunnels version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .vpn_tunnels_available?
    
    
    def self.vpn_tunnels_available?(version: :v1) -> boolean

Determines whether the VpnTunnels service is supported by the current client. If true, you can retrieve a client object by calling [Compute.vpn_tunnels](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_vpn_tunnels_class_ "Google::Cloud::Compute.vpn_tunnels \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the VpnTunnels service, or if the versioned client gem needs an update to support the VpnTunnels service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .wire_groups
    
    
    def self.wire_groups(version: :v1, &block) -> ::Object

Create a new client object for WireGroups.

By default, this returns an instance of [Google::Cloud::Compute::V1::WireGroups::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-WireGroups-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the WireGroups service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the WireGroups service. You can determine whether the method will succeed by calling [Compute.wire_groups_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_wire_groups_available__class_ "Google::Cloud::Compute.wire_groups_available? \(method\)").

#### About WireGroups

The WireGroups API.

This client uses WireGroups version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .wire_groups_available?
    
    
    def self.wire_groups_available?(version: :v1) -> boolean

Determines whether the WireGroups service is supported by the current client. If true, you can retrieve a client object by calling [Compute.wire_groups](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_wire_groups_class_ "Google::Cloud::Compute.wire_groups \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the WireGroups service, or if the versioned client gem needs an update to support the WireGroups service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .zone_operations
    
    
    def self.zone_operations(version: :v1, &block) -> ::Object

Create a new client object for ZoneOperations.

By default, this returns an instance of [Google::Cloud::Compute::V1::ZoneOperations::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ZoneOperations-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ZoneOperations service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the ZoneOperations service. You can determine whether the method will succeed by calling [Compute.zone_operations_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_zone_operations_available__class_ "Google::Cloud::Compute.zone_operations_available? \(method\)").

#### About ZoneOperations

The ZoneOperations API.

This client uses ZoneOperations version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .zone_operations_available?
    
    
    def self.zone_operations_available?(version: :v1) -> boolean

Determines whether the ZoneOperations service is supported by the current client. If true, you can retrieve a client object by calling [Compute.zone_operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_zone_operations_class_ "Google::Cloud::Compute.zone_operations \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ZoneOperations service, or if the versioned client gem needs an update to support the ZoneOperations service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .zone_vm_extension_policies
    
    
    def self.zone_vm_extension_policies(version: :v1, &block) -> ::Object

Create a new client object for ZoneVmExtensionPolicies.

By default, this returns an instance of [Google::Cloud::Compute::V1::ZoneVmExtensionPolicies::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ZoneVmExtensionPolicies-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ZoneVmExtensionPolicies service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the ZoneVmExtensionPolicies service. You can determine whether the method will succeed by calling [Compute.zone_vm_extension_policies_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_zone_vm_extension_policies_available__class_ "Google::Cloud::Compute.zone_vm_extension_policies_available? \(method\)").

#### About ZoneVmExtensionPolicies

The ZoneVmExtensionPolicies API.

This client uses ZoneVmExtensionPolicies version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .zone_vm_extension_policies_available?
    
    
    def self.zone_vm_extension_policies_available?(version: :v1) -> boolean

Determines whether the ZoneVmExtensionPolicies service is supported by the current client. If true, you can retrieve a client object by calling [Compute.zone_vm_extension_policies](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_zone_vm_extension_policies_class_ "Google::Cloud::Compute.zone_vm_extension_policies \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ZoneVmExtensionPolicies service, or if the versioned client gem needs an update to support the ZoneVmExtensionPolicies service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .zones
    
    
    def self.zones(version: :v1, &block) -> ::Object

Create a new client object for Zones.

By default, this returns an instance of [Google::Cloud::Compute::V1::Zones::Rest::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Zones-Rest-Client) for a REST client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Zones service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned.

Raises an exception if the currently installed versioned client gem for the given API version does not support the Zones service. You can determine whether the method will succeed by calling [Compute.zones_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_zones_available__class_ "Google::Cloud::Compute.zones_available? \(method\)").

#### About Zones

The Zones API.

This client uses Zones version 2026-09-01.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .zones_available?
    
    
    def self.zones_available?(version: :v1) -> boolean

Determines whether the Zones service is supported by the current client. If true, you can retrieve a client object by calling [Compute.zones](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest/Google-Cloud-Compute#Google__Cloud__Compute_zones_class_ "Google::Cloud::Compute.zones \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Zones service, or if the versioned client gem needs an update to support the Zones service.

**Parameter**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 



**Returns**

  * (boolean) — Whether the service is available. 



## Constants 

### VERSION

**value:** "1.22.0"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
