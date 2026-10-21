---
url: https://docs.cloud.google.com/service-extensions/docs/plugins-overview/
title: Plugins overview \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:16.633573+00:00
---

# Plugins overview  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/plugins-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Plugins overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides overview information about the integration of plugins with Cloud Load Balancing Application Load Balancers and Media CDN.

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages) for Media CDN.

Plugins are built using WebAssembly (Wasm) format and use Proxy-Wasm APIs.

  * [Wasm](https://webassembly.org/) is an open and standardized binary instruction format that enables a host to load and run Wasm modules with customer-provided code. Wasm has a number of benefits for executing customer code, including sandboxing for security, support for multiple languages, portability, broad and growing support within the industry, and improved performance relative to other VM-based options such as JavaScript.

  * [Proxy-Wasm](https://github.com/proxy-wasm) is an open source project started by Google. It defines APIs that let you customize the behavior of network proxies by implementing callbacks to be executed during HTTP request and response processing.




## How plugins work

You can use Service Extensions with Application Load Balancers and Media CDN as follows:

  1. [Prepare plugin code](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code) as follows:

     1. Create custom code by using one of the Proxy-Wasm SDKs:

        * [Rust](https://github.com/proxy-wasm/proxy-wasm-rust-sdk)

        * [Go](https://github.com/proxy-wasm/proxy-wasm-go-sdk)

        * [C++](https://github.com/proxy-wasm/proxy-wasm-cpp-sdk)

     2. Compile your code into a Wasm module.

     3. Upload your compiled plugin code to an Artifact Registry repository.

  2. [Create a plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin) that contains the uploaded plugin code.

  3. Configure the plugin in [Cloud Load Balancing extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview) or [Media CDN extensions](https://docs.cloud.google.com/service-extensions/docs/media-cdn-extensions-overview).




## Plugin resources

Service Extensions helps you create the following key resources that help you add custom code in the processing path:

  * _Plugins_ , which contain the custom code that you want to deploy.

  * _Plugin versions_ , which are versions of your Wasm module. You can indicate which version of your Wasm module that a plugin is to use as its main (active) one.




## Access attributes in plugins

Wasm plugins can access forwarded attributes by using the `proxy_get_property` ABI call, which is part of the Proxy-Wasm ABI. The property name that you can retrieve corresponds to the attribute name.

You can access properties as a path representation of the attribute name. For example, to retrieve `request.host`, you can use a path representation such as `{"request", "host"}`.

The following conceptual Rust example demonstrates how to access forwarded attributes within an `HttpContext` implementation:
    
    
    use proxy_wasm::traits::{HttpContext, RootContext};
    use proxy_wasm::types::Action;
    
    // ... inside your HttpContext implementation ...
    
    fn on_request_headers(&mut self, _num_headers: usize, _end_of_stream: bool) -> Action {
        if let Some(host) = self.get_property(vec!["request", "host"]) {
            // host is a Vec, convert to string
            let host_str = String::from_utf8(host).unwrap_or_default();
            log::info!("Request host: {}", host_str);
        }
    
        if let Some(region) = self.get_property(vec!["source", "client_region"]) {
            let region_str = String::from_utf8(region).unwrap_or_default();
            log::info!("Client region: {}", region_str);
        }
    
        Action::Continue
    }

## Limitations

This section lists some limitations with plugins.

### Limitations on resources

Plugins are strictly constrained in how many resources they can use:

  * A plugin can use up to 1 msec of normalized vCPU for each invocation. A CPU millisecond is platform dependent, but the normalized platform is approximately equal to a processor with a 4 GHz clock speed. An invocation is an independently billed phase of execution, which can be request headers, request body, response headers, or response body.

  * A plugin can use up to 16 MiB of memory for each VM instance. An instance must be able to serve up to 1000 concurrent requests, which means that a plugin can hold up to 16 KiB of memory for each stream. Keep in mind that the total memory use includes global state and stack allocations.




Use the [plugin tester](https://docs.cloud.google.com/service-extensions/docs/plugin-best-practices#testing) to benchmark a plugin's CPU and memory characteristics.

### Limitations on APIs

  * Plugins can use a subset of the Proxy-Wasm ABI. Plugins don't support timers, custom metrics, shared data, shared queues, or outbound network calls.

  * HTTP trailer events aren't supported.




### Limitations with header manipulation

  * The maximum size of any mutation (headers or body chunks) is 128 KiB.

  * Plugins can't override the processing mode of the `ext_proc` stream.

  * Header manipulation through plugins is not supported for some headers. The processor ignores any modifications in these headers, and continues to process the request.

For Media CDN plugins, the following are not supported:

    * Headers: `CDN-Loop`, `connection`, `keep-alive`, `proxy-authenticate`, `proxy-authorization`, `proxy-connection`, `te`, `trailers`, `transfer-encoding`, `upgrade`, or `X-user-IP`.
    * Headers starting with: `x-forwarded`, `x-goog-`,`x-google`, `x-gfe`, or `x-amz-`.

For Cloud Load Balancing plugins, the following are not supported:

    * Headers: `connection`, `keep-alive`, `proxy-authenticate`, `proxy-authorization`, `proxy-connection`, `sec-user-ip`, `te`, `trailer`, `transfer-encoding`, `upgrade`, `x-dont-count-ads`, `x-dont-show-ads`, `x-gr`, `x-proxyuser-ip`, or `x-user-ip`.

Additionally, for `LbTrafficExtension`, these headers are also not supported: `method`, `authority`, `scheme`, or host headers.

    * Headers starting with: `sec-gfe-`, `sec-google-`, `x-amz-`, `x-forwarded-`, `x-gfe-`, `x-goog-`, `x-google-`, or `x-gproxy-`.




### Limitations with HTTP/1.1 clients and backends

When you configure either `REQUEST_BODY` or `RESPONSE_BODY` for an extension, if the load balancer receives a matching request, it removes the `Content-Length` header from the response and switches to chunked body encoding.

## What's next

  * [Prepare the plugin code](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code)
  * [Create a plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
