---
url: https://docs.cloud.google.com/service-extensions/docs/plugin-best-practices/
title: Best practices for plugins \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:39.176066+00:00
---

# Best practices for plugins  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/plugin-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Best practices for plugins Stay organized with collections  Save and categorize content based on your preferences. 

This page provides tips for writing Service Extensions plugins that are correct, perform well, and are well isolated. Correctness is critical because plugins run in a constrained engine sandbox with a limited API surface. Performance is critical because plugins run during end-user requests, with [small amounts of resources](https://docs.cloud.google.com/service-extensions/docs/quotas#limits). Isolation is provided at the project level.

## Getting started

**Best practices**  
Start from the samples  
Use supported APIs  
Run functional tests and benchmarks  


### Start from the samples

A good way to get started is browsing our [plugin code samples](https://github.com/GoogleCloudPlatform/service-extensions/tree/main/plugins#docs). These are examples of common plugin patterns, such as path or query parsing, header rewrites, custom logging, and custom authentication.

### Use supported APIs

Plugins must be compiled against the [Proxy-Wasm](https://github.com/proxy-wasm) binary interface (ABI). Service Extensions supports a subset of the Proxy-Wasm ABI that includes HTTP header and body mutations, local responses, custom logging, and plugin configuration. Proxy-Wasm also supports a small subset of [WASI preview 1](https://github.com/WebAssembly/WASI/blob/main/legacy/preview1/docs.md#modules), including `stdout` and `stderr` for logging, `clock_time_get` and `random_get`.

Service Extensions doesn't support timers, custom metrics, shared data, shared queues, or outbound network calls. Service Extensions also doesn't support plugin callback return values that attempt to pause request processing, and ignores them.

### Run functional tests and benchmarks

To evaluate correctness and performance, we provide a local plugin tester tool that can run, test, and benchmark your plugin. You invoke this tool in a Docker container, passing a plugin binary and a text proto of inputs and expectations. See the [local tester documentation](https://github.com/GoogleCloudPlatform/service-extensions/tree/main/plugins#docs) and [test input example](https://github.com/GoogleCloudPlatform/service-extensions/blob/main/plugins/samples/testing/tests.textpb).

## Correctness

**Best practices**  
Don't rely on clocks  
Treat header names as case-insensitive  


### Don't rely on clocks

For security reasons, clock time is set at context creation (for a plugin or a request) and kept frozen during plugin invocations. This means that WebAssembly plugins must not sleep; a sleep times out because time doesn't advance. It also means that plugins can't measure their own execution time, though this information is available in Cloud Monitoring.

### Treat header names as case-insensitive

According to [HTTP semantics](https://datatracker.ietf.org/doc/html/rfc9110#name-field-names), HTTP header field names must be treated as case-insensitive. Header case written by a plugin can be changed before being sent to clients or backends.

## Performance

**Best practices**  
Avoid plugin crashes  
Compile for execution speed  
Precompile regular expressions  
Avoid copying data into HTTP contexts  


### Avoid plugin crashes

When a plugin crashes, the triggering request receives an error. If this happens frequently, plugin restarts are throttled, which leads to bursts of errors that affect multiple users.

To avoid plugin crashes, try the following:

  * Avoid assertions of all kinds. Instead, configure error logging or local responses to users.
  * In Rust, avoid using methods, such as `unwrap`, that can result in panics. Additionally, you can configure the plugin to handle crashes by using `panic::set_hook`.
  * Test your plugin by using the Google-provided [plugin tester](https://docs.cloud.google.com/service-extensions/docs/plugin-best-practices#testing) and ensure that malformed or empty inputs are handled without the plugin crashing.



### Compile for execution speed

Compile your WebAssembly code to achieve the best execution speed by using build option `-O3` (for C++) or `opt-level=3` (for Rust).

### Precompile regular expressions

Avoid compute-heavy operations on the per-request path (in HTTP handlers). Instead, perform any work that's not request-specific at plugin configuration time, and pass any precomputed state into each HTTP request context (also known as stream context).

In particular, precompile any regular expressions at plugin configuration time. Our [regex code sample](https://github.com/GoogleCloudPlatform/service-extensions/tree/main/plugins/samples/regex_rewrite) shows how to achieve this.

### Avoid copying data into HTTP contexts

When sharing data between the root context and HTTP contexts, avoid expensive copies or clone calls. Instead, share pointers or references. In C++, this can be done with `std::shared_ptr` or raw pointers and references because the root context outlives any HTTP context. In Rust, values can be shared by using `std::rc::Rc`. In Go, values can be shared by storing pointers to the values, which are removed by the garbage collector.

## Security

**Best practices**  
Isolate workloads by project  
Restrict secrets on Media CDN  


### Isolate workloads by project

On Google's infrastructure, plugins owned by the same Google Cloud project can run in the same secure sandbox. This means that the WebAssembly runtime is the only security barrier between plugins in the same project.

Use separate Google Cloud projects for workloads that need security separation. This practice also provides separation of resources and permissions.

### Restrict secrets on Media CDN

By design, Media CDN runs on a fleet of hardware operated outside of Google's physical control. When writing security-related plugins for Media CDN, use dedicated hostnames or subdomains, and configure plugins with signing keys that are rotated frequently.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
