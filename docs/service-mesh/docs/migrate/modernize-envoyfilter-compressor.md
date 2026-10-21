---
url: https://docs.cloud.google.com/service-mesh/docs/migrate/modernize-envoyfilter-compressor/
title: Update EnvoyFilter compressor configurations \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:11.071789+00:00
---

# Update EnvoyFilter compressor configurations  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/migrate/modernize-envoyfilter-compressor/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update EnvoyFilter compressor configurations

Several top-level fields in the API surface of the `envoy.extensions.filters.http.compressor.v3.Compressor` filter are [deprecated in Envoy](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/http/compressor/v3/compressor.proto) (see the [source definition](https://github.com/envoyproxy/envoy/blob/main/api/envoy/extensions/filters/http/compressor/v3/compressor.proto#L113-L154)). These settings have been moved into dedicated `response_direction_config.common_config` and `request_direction_config.common_config` blocks.

This guide provides the context and steps necessary for updating your `EnvoyFilter` resources to a supported format. Moving to this modern format ensures your configurations remain compatible with subsequent updates, benefits from improved structural clarity, and aligns with Cloud Service Mesh modernization best practices.

## Understanding the need for modernization

The Envoy Compressor filter provides on-the-fly compression and decompression of HTTP bodies, helping to reduce bandwidth usage and improve application performance.

Cloud Service Mesh with the `TRAFFIC_DIRECTOR` control plane (see [Check control plane implementation](https://docs.cloud.google.com/service-mesh/docs/check-control-plane-implementation)) requires using the supported version of the EnvoyFilter API. Legacy deployments using deprecated top-level fields (such as `content_length`, `content_type`, `disable_on_etag_header`, `remove_accept_encoding_header`, or `runtime_enabled`) will continue to function but are recommended to be updated immediately for reliability purposes.

When using these deprecated fields, validations are being rolled out progressively across release channels (`Rapid`, then `Regular`, then `Stable`). The control plane validations apply based on when the deployments occurred:

Deployment Type | Validation Behavior  
---|---  
**Legacy Deployments** (Deployed before validations were enabled) | The control plane sets a _warning_ status on your `EnvoyFilter` custom resource (CR) that reads: `found usage of unsupported fields: [...]`. The configuration will still be applied for backward compatibility, but you need to migrate to the supported fields to ensure continued support.  
**Supported Deployments** (Deployed after validations were enabled) | The control plane strictly blocks the use of unsupported fields. Applying the configuration results in an _error_ on the `EnvoyFilter` resource with the message: `found usage of unsupported fields: [...]`, and the unsupported configuration will be rejected.  
  
Updating your configurations resolves these warnings and errors in your resource status, and ensures your configurations comply with the validations.

## Identify deprecated configurations

Your `EnvoyFilter` configuration needs to be updated if you are setting any of the following fields directly under the `typed_config` block:

  * `min_content_length`
  * `content_length`
  * `content_type`
  * `disable_on_etag_header`
  * `remove_accept_encoding_header`



You can list your EnvoyFilters using:
    
    
    kubectl get envoyfilters --all-namespaces -o yaml
    

Inspect the output for EnvoyFilters patching `envoy.filters.http.compressor`.

## Configuration formats

The following sections provide examples of both the deprecated and modernized configurations for the Compressor Envoy filter within an `EnvoyFilter` resource.

### Example of a deprecated configuration

If your `EnvoyFilter`'s patch section resembles the following snippet, it uses the deprecated format:
    
    
    apiVersion: networking.istio.io/v1alpha3
    kind: EnvoyFilter
    metadata:
      name: compressor-filter-update
      namespace: istio-system
    spec:
      configPatches:
      - applyTo: HTTP_FILTER
        match:
          context: GATEWAY
          listener:
            filterChain:
              filter:
                name: envoy.filters.network.http_connection_manager
                subFilter:
                  name: envoy.filters.http.router
        patch:
          operation: INSERT_BEFORE
          value:
            name: envoy.filters.http.compressor
            typed_config:
              '@type': type.googleapis.com/envoy.extensions.filters.http.compressor.v3.Compressor
              # These top-level fields are DEPRECATED
              min_content_length: 1024
              content_type:
              - "application/javascript"
              - "application/json"
              disable_on_etag_header: true
              remove_accept_encoding_header: true
              compressor_library:
                name: gzip
                typed_config:
                  '@type': type.googleapis.com/envoy.extensions.compression.gzip.compressor.v3.Gzip
    

### Example of the modernized configuration

The deprecated fields must be moved into the `response_direction_config` object (or `request_direction_config` if applicable):
    
    
    apiVersion: networking.istio.io/v1alpha3
    kind: EnvoyFilter
    metadata:
      name: compressor-filter-update
      namespace: istio-system
    spec:
      configPatches:
      - applyTo: HTTP_FILTER
        match:
          context: GATEWAY
          listener:
            filterChain:
              filter:
                name: envoy.filters.network.http_connection_manager
                subFilter:
                  name: envoy.filters.http.router
        patch:
          operation: INSERT_BEFORE
          value:
            name: envoy.filters.http.compressor
            typed_config:
              '@type': type.googleapis.com/envoy.extensions.filters.http.compressor.v3.Compressor
              compressor_library:
                name: gzip
                typed_config:
                  '@type': type.googleapis.com/envoy.extensions.compression.gzip.compressor.v3.Gzip
              response_direction_config:
                disable_on_etag_header: true # MOVED
                remove_accept_encoding_header: true # MOVED
                common_config:
                  min_content_length: 1024  # MOVED
                  content_type:          # MOVED
                  - "application/javascript"
                  - "application/json"
                  enabled:
                    default_value: true
                    runtime_key: "compressor.enabled"
    

## Supported fields and migration paths

For a complete list of supported fields, see the [Data plane extensibility using EnvoyFilter](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility#typegoogleapiscomenvoyextensionsfiltershttpcompressorv3compressor) guide. The following table details the mapping for migrating the most common deprecated fields.

Deprecated Field Path | Modern Field Path | Notes  
---|---|---  
`typed_config.min_content_length` | `typed_config.response_direction_config.common_config.min_content_length`  
OR  
`typed_config.request_direction_config.common_config.min_content_length` | Sets the minimum response OR request size respectively to trigger compression.  
`typed_config.content_length` | `typed_config.response_direction_config.common_config.min_content_length`  
OR  
`typed_config.request_direction_config.common_config.min_content_length` | Earlier alias for `min_content_length`. Rename to `min_content_length` in the new path.  
`typed_config.content_type` | `typed_config.response_direction_config.common_config.content_type`  
OR  
`typed_config.request_direction_config.common_config.content_type` | Array of content types to compress.  
`typed_config.disable_on_etag_header` | `typed_config.response_direction_config.disable_on_etag_header` | Disables compression if the response contains an `ETag` header.  
`typed_config.remove_accept_encoding_header` | `typed_config.response_direction_config.remove_accept_encoding_header` | Removes the `Accept-Encoding` header from requests before dispatching to upstream.  
  
## Migration plan

We recommend updating your `EnvoyFilter` configurations following your organization's standard deployment and testing best practices. Consider these general steps during your migration:

  * **Identify:** Find all `EnvoyFilter` resources using the Compressor filter with deprecated fields as described in Identify deprecated configurations.
  * **Test:** Modify the YAML of your `EnvoyFilter` resource(s) and test the changes in a pre-prod environment. Verify that compression is active for the expected content types and sizes.
  * **Monitor and validate:**
    * Check your `EnvoyFilter` resource status to confirm the `found usage of unsupported fields: [...]` warnings or errors are no longer present.
    * Monitor key metrics: CPU usage, latency, and bandwidth consumption.
    * Inspect response headers (for example, `Content-Encoding: gzip`) and confirm compression.
  * **Deploy:** Apply the supported `EnvoyFilter` configurations to production workloads.



## Benefits of modernization

  * Resource Status clarity: Removes `found usage of unsupported fields: [...]` warnings and errors from your compressor `EnvoyFilter` resource status.
  * Standardization: Aligns with current Envoy configuration best practices and the `TRAFFIC_DIRECTOR` validations.
  * Future compatibility: Ensures your configurations work seamlessly with upcoming Envoy and Cloud Service Mesh versions.



## Troubleshooting and support

If you encounter issues, consider the following:

  * Double-check the YAML syntax and field placement.
  * Examine Envoy proxy logs for detailed error messages: `kubectl logs -l app=your-app -c istio-proxy -n your-namespace`.
  * Rollback to the previous `EnvoyFilter` configuration if necessary.
  * Contact Google Cloud Support for further assistance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
