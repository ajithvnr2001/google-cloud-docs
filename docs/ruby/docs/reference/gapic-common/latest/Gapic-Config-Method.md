---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Config-Method/
title: gapic-common - Class Gapic::Config::Method (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:09.795580+00:00
---

# gapic-common - Class Gapic::Config::Method (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Config-Method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Class Gapic::Config::Method (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common class Gapic::Config::Method.

Config::Method is a configuration class that represents the configuration for an API RPC call.

## Inherits

  * Object 



## Extended By

  * [Gapic::Config](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Config)



## Example
    
    
    require "gapic/config"
    
    class ServiceConfig
      extend Gapic::Config
    
      config_attr :host,     "localhost", String
      config_attr :port,     443,         Integer
      config_attr :timeout,  nil,         Numeric, nil
      config_attr :metadata, nil,         Hash, nil
    
      attr_reader :rpc_method
    
      def initialize parent_config = nil
        @parent_config = parent_config unless parent_config.nil?
        @rpc_method = Gapic::Config::Method.new
    
        yield self if block_given?
      end
    end
    
    config = ServiceConfig.new
    
    config.timeout = 60
    config.rpc_method.timeout = 120

## Methods 

### #initialize
    
    
    def initialize(parent_method = nil) { |_self| ... } -> Method

Create a new Config::Method object instance.

**Parameter**

  * **parent_method** ([Gapic::Config::Method](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Config-Method), nil) — The config to look to values for. 



**Yields**

  * (_self) 



**Yield Parameter**

  * **_self** ([Gapic::Config::Method](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Config-Method)) — the object that the method was called on 



**Returns**

  * ([Method](https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Config-Method)) — a new instance of Method 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
