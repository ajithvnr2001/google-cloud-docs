---
url: https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions/
title: Configure a route extension \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:10.331654+00:00
---

# Configure a route extension  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Configure a route extension Stay organized with collections  Save and categorize content based on your preferences. 

Service Extensions enables [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) to use plugins or send callouts to backend services to insert custom processing in the processing path. [Route extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#route-extensions) run in the request processing path when the load balancer receives request headers and before it evaluates the [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts). This page describes how to configure route extensions.

For an overview about Application Load Balancer extensions, see [Cloud Load Balancing extensions overview](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview).

A route extension for an Application Load Balancer points to the following resources:

  * A forwarding rule to attach to
  * A plugin or a callout backend service whose backends run the `ext_proc` gRPC API



A route extension groups related extension services into a chain. You can configure both plugins and callouts in the same extension chain. The extension chain selects the traffic to act on by using [Common Expression Language (CEL)](https://docs.cloud.google.com/service-extensions/docs/cel-matcher-language-reference) match conditions. The load balancer evaluates a request against match conditions for a chain in a sequential manner. When a request matches the conditions defined by a chain, all extensions in the chain act on the request. Only one chain matches a given request.

The extension references the load balancer [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) to attach to. After you configure the resource, the load balancer starts sending matching requests to extension services.

For information about the limits related to Application Load Balancer extensions, see the [Quotas and limits](https://docs.cloud.google.com/service-extensions/docs/quotas#lb-extensions) page.

**Important:** You can attach only one route extension to a forwarding rule.

## Configure using plugins

This section uses an example to show you how to configure a route extension by using a plugin that rewrites the `:host` request header to `service-extensions.com` when the path matches `/extensions`. The earlier host and the newly configured host are mapped to backend services in different regions, which demonstrates the routing behavior.

All extension resources that reference a given plugin must be of the same type. The extensions must also have the same load balancing scheme. You can't configure Cloud Load Balancing extensions with plugins that are already used in Media CDN extensions.

### Before you begin

  1. [Create a plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin) that contains your [custom code](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code).

  2. Create and configure an [Application Load Balancer that supports route extension plugins](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs).

Follow the instructions on the [Set up a cross-region internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-internal) page for all steps, except the following:

     * Name the backend service as `service-one`.
     * Point `service-one` to a virtual machine (VM) instance in region `A`.
     * Point `gl7-gilb-url-map` to `service-one` by default.
  3. Set up an additional backend service, `service-two` and point it to a VM in region `B`.

  4. To the URL map, add a path matcher pointing to `service-two`. Use the [`gcloud compute url-maps add-path-matcher` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher) with the following sample values:
         
         gcloud compute url-maps add-path-matcher gl7-gilb-url-map \
               --path-matcher-name=rewrite-host \
               --default-service=service-two \
               --new-hosts=service-extensions.com \
               --location=global
         

  5. Set up a way to send test requests to your service (for example, by running curl). If you're using an internal load balancer, [create a client VM for testing](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#test_client).




### Configure a route extension by using a plugin

  1. Check the behavior before an extension is configured.

     1. Verify that a request without an explicit path goes to region `A`:
            
            curl FORWARDING_RULE_IP
            

Replace `FORWARDING_RULE_IP` with the IP address of the forwarding rule. To find the IP address, use the [`gcloud compute forwarding-rules describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/describe).

The output is similar to the following and indicates that the page is served from a VM in `region A`:
            
            Page served from region-A-vm
            

     2. Verify that there is no match for `/extensions` in the URL map:
            
            curl FORWARDING_RULE_IP/extensions
            

Replace `FORWARDING_RULE_IP` with the IP address of the forwarding rule. To find the IP address, use the [`gcloud compute forwarding-rules describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/describe).

The output indicates that there is no match for `/extensions` in the URL map. The output is similar to the following:
            
            <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
            <html><head>
            <title>404 Not Found</title>
            </head><body>
            ...
            

  2. Configure the route extension.

### Console

     1. In the Google Cloud console, go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

     2. Click **Create extension**.

A wizard opens to guide you through some initial steps.

     3. For the product, select **Load Balancing**. Then, click **Continue**.

A list of [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) appears.

     4. For the load balancer type, select cross-region internal Application Load Balancer. Then, click **Continue**.

     5. For the extension type, select **Route extensions** , and then click **Continue**.

     6. To open the **Create extension** form, click **Continue**.

In the **Create extension** form, notice that the preceding selections, which appear at the top of the page, are not editable.

     7. In the **Basics** section, do the following:

        1. Specify a unique name for the extension.

The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens and must not end with a hyphen.

        2. Optional: Enter a brief description about the extension by using a maximum of 1,024 characters.

     8. Optional: In the **Labels** section, click **Add label**. Then, in the row that appears, do the following:

        * For **Key** , enter a key name.
        * For **Value** , enter a value for the key.

To add more key-value pairs, click **Add label**. You can add a maximum of 64 key-value pairs.

For more information about labels, see [Create and update labels for projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels).

     9. For **Forwarding rules** , select one or more forwarding rules to associate with the extension—for example, `cr-ilb-forwarding-rule`.

Forwarding rules that are already associated with another extension can't be selected and appear disabled.

     10. For **Extension** , to add an extension to execute for a matching request, do the following:

        * To match requests for which the extension chain is executed, for **Match condition** , specify a Common Expression Language (CEL) expression—for example, `request.path.startsWith("/extensions")`.

For more information about CEL expressions, click **Get syntax help** or see [CEL matcher language reference](https://docs.cloud.google.com/service-extensions/docs/cel-matcher-language-reference).

        * For **Programmability type** , select **Plugins**.

        * For **Plugin** , select a plugin [created using Service Extensions](https://docs.cloud.google.com/service-extensions/docs/create-plugin) for the same product and extension type.

        * For **Forward attributes** , select the request, connection, and location attributes that you want the load balancer to forward to your Wasm plugin. You can configure a maximum of 16 attributes for each extension. For more information, see [Supported attributes](https://docs.cloud.google.com/service-extensions/docs/attributes).

        * For **Forward headers** , click **Add header** , and then add HTTP headers to forward to the extension (from the client or the backend). If a header isn't specified, all headers are sent.

        * Optional: if the extension times out or fails and you want request or response processing to continue, for **Fail open** , select **Enabled**.

By default, the **Fail open** option isn't selected. In this case, when an error occurs, request or response processing stops. If response headers haven't been delivered to the downstream client, a generic HTTP `500` status code is returned to the client. If response headers have been delivered, the HTTP stream to the client is reset.

The default option of keeping **Fail open** unselected is preferred when prioritizing security or integrity. Enabling **Fail open** , especially for non-critical operations, helps when prioritizing availability.

If you want to specify more than one extension or extension chains rather than a single extension, click the **Switch to advanced mode** button at the end of the form and specify the required extensions and chains. The extensions run in the sequence in which they are listed.

Specify unique names for each extension and extension chain. The names must conform with RFC-1034, use only lowercase letters, numbers, and hyphens, and have a maximum length of 63 characters. Additionally, the first character must be a letter and the last character must be a letter or a number.

     11. Click **Create extension**.

###  gcloud 

     1. Define the plugin in a YAML file and associate it with a global forwarding rule—for example, `cr-ilb-forwarding-rule`.
            
            cat >route-plugin.yaml <<EOF
                name: route-ext
                forwardingRules:
                - https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/forwardingRules/cr-ilb-forwarding-rule
                loadBalancingScheme: INTERNAL_MANAGED
                extensionChains:
                - name: "chain1"
                  matchCondition:
                    celExpression: 'request.path.startsWith("/extensions")'
                  extensions:
                  - name: 'ext1'
                    service: projects/PROJECT_ID/locations/LOCATION/wasmPlugins/WASM_PLUGIN
                    failOpen: false
                    supportedEvents:
                    - REQUEST_HEADERS
                    forwardAttributes:
                    - request.host
                    - request.path
            EOF
            

Replace the following:

        * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
        * `REGION`: the region of the forwarding rule. The value must match the value specified for the location of the plugin.
        * `LOCATION`: the location of the plugin as either `global` or a region.
        * `WASM_PLUGIN`: the ID or the fully qualified name of the plugin.

For more information about the fields in the YAML file, see [ExtensionChain](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/ExtensionChain) in the API documentation.

The `forwardAttributes` field lets you specify the request, connection, and location attributes to forward to your Wasm plugin. You can configure a maximum of 16 attributes for each extension. For more information about supported attributes, see [Supported attributes](https://docs.cloud.google.com/service-extensions/docs/attributes).

     2. Import the route extension. Use the [`gcloud service-extensions lb-route-extensions import` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/lb-route-extensions/import) with the following sample values.
            
            gcloud service-extensions lb-route-extensions import route-ext \
                --source=route-plugin.yaml \
                --location=global
            

After a route extension is created, it takes a little time for the new plugin to be distributed across all locations. The time might vary across locations because the plugin isn't delivered to all locations simultaneously.

  3. To verify that the route extension works as expected, use the same `curl` command:
         
         curl FORWARDING_RULE_IP/extensions
         

The output is similar to the following and indicates that the page is served from a VM in `region B`:
         
         Page served from region-B-vm
         

To verify that the plugin runs only for requests with the `/extension` path prefix, repeat the `curl` command without a path.
         
         curl FORWARDING_RULE_IP
         

The output is similar to the following:
         
         Page served from region-A-vm
         




## Configure using callouts

This section shows you how to configure a route extension by using a callout.

### Before you begin

Create the required resources as described in [Configure a callout backend service](https://docs.cloud.google.com/service-extensions/docs/configure-callout-backend-service).

### Configure a route extension by using a callout

The following example shows how to configure a route extension to call when the path matches `/extensions`. The route callout server in the `callout-vm` changes the `Host` header to `service-extensions.com`, sets the path to `/`, and then sends an instruction to the load balancer to recompute the route. The traffic then flows to `l7-ilb-backend-service2` instead of `l7-ilb-backend-service`.

  1. Check if there's a match for `/extensions` in the URL map.

     1. Run the following `curl` command against the forwarding rule in the client VM:
            
            curl FORWARDING_RULE_IP/extensions
            

Replace `FORWARDING_RULE_IP` with the IP address of the forwarding rule. To find the IP address, use the [`gcloud compute forwarding-rules describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/describe).

The output indicates that there is no match for `/extensions` in the URL map. The output is similar to the following:
            
            <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
            <html><head>
            <title>404 Not Found</title>
            </head><body>
            ...
            

  2. Configure the route extension.

### Console

     1. In the Google Cloud console, go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

     2. Click **Create extension**.

A wizard opens to guide you through some initial steps.

     3. For the product, select **Load Balancing**. Then, click **Continue**.

A list of [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) appears.

     4. Select a load balancer type. For regional load balancers, also specify the region. Click **Continue**.

     5. For the extension type, select **Route extensions** , and then click **Continue**.

     6. To open the **Create extension** form, click **Continue**.

In the **Create extension** form, notice that the preceding selections, which appear at the top of the page, are not editable.

     7. In the **Basics** section, do the following:

        1. Specify a unique name for the extension.

The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens and must not end with a hyphen.

        2. Optional: Enter a brief description about the extension by using a maximum of 1,024 characters.

     8. Optional: In the **Labels** section, click **Add label**. Then, in the row that appears, do the following:

        * For **Key** , enter a key name.
        * For **Value** , enter a value for the key.

To add more key-value pairs, click **Add label**. You can add a maximum of 64 key-value pairs.

For more information about labels, see [Create and update labels for projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels).

     9. For **Forwarding rules** , select one or more forwarding rules to associate with the extension—for example, `l7-ilb-forwarding-rule`.

Forwarding rules that are already associated with another extension can't be selected and appear disabled.

     10. For **Extension** , to add an extension to execute for a matching request, do the following:

        * To match requests for which the extension chain is executed, for **Match condition** , specify a Common Expression Language (CEL) expression—for example, `request.path.startsWith("/extensions")`.

For more information about CEL expressions, click **Get syntax help** or see [CEL matcher language reference](https://docs.cloud.google.com/service-extensions/docs/cel-matcher-language-reference).

        * For **Programmability type** , select **Callouts**.

          * For **Extension name** , specify a unique name.

The name must conform with RFC-1034, use only lowercase letters, numbers, and hyphens, and have a maximum length of 63 characters. Additionally, the first character must be a letter and the last a letter or a number.

          * For **Authority** , enter the `authority` header from the gRPC request sent from load balancer to the extension service.

          * For **Backend service** , select a backend service created by following the instructions in [Configure a callout backend service](https://docs.cloud.google.com/service-extensions/docs/configure-callout-backend-service).

          * For **Timeout** , specify a value between 10 and 1000 milliseconds, after which a message on the stream times out while the load balancer is still waiting for a response from the `ext_proc` service.

          * For **Forward attributes** , select the request, connection, and location attributes that you want the load balancer to forward to your callout service. You can configure a maximum of 16 attributes for each extension. For more information, see [Supported attributes](https://docs.cloud.google.com/service-extensions/docs/attributes).

          * For **Forward headers** , click **Add header** , and then add HTTP headers to forward to the extension (from the client or the backend). If a header isn't specified, all headers are sent.

          * Optional: if the extension times out or fails and you want request or response processing to continue, for **Fail open** , select **Enabled**. Subsequent extensions in the chain are also executed.

By default, the **Fail open** option isn't selected. In this case, when an error occurs, request or response processing stops. If response headers haven't been delivered to the downstream client, a generic HTTP `500` status code is returned to the client. If response headers have been delivered, the HTTP stream to the client is reset.

The default option of keeping **Fail open** unselected is preferred when prioritizing security or integrity. Enabling **Fail open** , especially for non-critical operations, helps when prioritizing availability.

        * For **Metadata** , click **Add metadata** and specify sample values as suggested. For **Key** , specify `key`, and for **Value** , specify `value`.

Click **Add metadata** to add another key-value pair. For **Key** , specify `fr`, and for **Value** , specify `forwarding_rule_id`.

The **Metadata** field lets you pass any additional information from the load balancer to the extension server. The metadata is sent in a `ProcessingRequest` message and encoded as `protobuf.Struct`. Any text within the metadata that matches the specified forwarding rule ID is replaced with the fully qualified resource URL of the forwarding rule associated with the client request.

The total size of the metadata must be less than 1 KiB. The total number of keys in the metadata must be less than 16. The length of each key must be less than 64 characters. The length of each value must be less than 1024 characters. All values must be strings.

If you want to specify more than one extension or extension chains rather than a single extension, click the **Switch to advanced mode** button at the end of the form and specify the required extensions and chains. The extensions run in the sequence in which they are listed.

Specify unique names for each extension and extension chain. The names must conform with RFC-1034, use only lowercase letters, numbers, and hyphens, and have a maximum length of 63 characters. Additionally, the first character must be a letter and the last character must be a letter or a number.

     11. Click **Create extension**.

###  gcloud 

     1. Define the callout in a YAML file and associate it with the forwarding rule. Use the sample values provided.
            
            cat >route.yaml <<EOF
                name: route-ext
                forwardingRules:
                - https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules/l7-ilb-forwarding-rule
                loadBalancingScheme: INTERNAL_MANAGED
                extensionChains:
                - name: "chain1"
                  matchCondition:
                    celExpression: 'request.path.startsWith("/extensions")'
                  extensions:
                  - name: 'ext11'
                    authority: ext11.com
                    service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/l7-ilb-callout-service
                    failOpen: false
                    timeout: 0.1s
                    metadata:
                      "key": "value"
                      "fr": "forwarding_rule_id"
                    forwardAttributes:
                    - request.host
                    - request.path
            EOF
            

Replace `PROJECT_ID` with the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

The `metadata` field in the extension configuration lets you pass any additional information from the load balancer to the extension server. The metadata is sent in a `ProcessingRequest` message and encoded as `protobuf.Struct`. Any text within the metadata that matches the specified forwarding rule ID is replaced with the fully qualified resource URL of the forwarding rule associated with the client request.

The total size of `metadata` must be less than 1 KiB. The total number of keys in the metadata must be less than 16. The length of each key must be less than 64 characters. The length of each value must be less than 1024 characters. All values must be strings.

For more information about the fields in the YAML file, see [ExtensionChain](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/ExtensionChain) in the API documentation.

The `forwardAttributes` field lets you specify the request, connection, and location attributes to forward to your callout service. You can configure a maximum of 16 attributes for each extension. For more information about supported attributes, see [Supported attributes](https://docs.cloud.google.com/service-extensions/docs/attributes).

     2. Import the route extension. Use the [`gcloud service-extensions lb-route-extensions import` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/lb-route-extensions/import) with the following sample values.
            
            gcloud service-extensions lb-route-extensions import route-ext \
                --source=route.yaml \
                --location=us-west1
            

  3. Verify that the route extension works as expected. Use the same `curl` command:
         
         curl FORWARDING_RULE_IP/extensions
         

The output indicates that the traffic matched the virtual host `service-extensions.com` and reached the `l7-ilb-backend-service2` service even though the original request did not. The output is similar to the following:
         
         Page served from second backend service
         

To validate that the callout is targeting only requests with the `/extension` prefix, repeat the `curl` command without the `path` prefix.
         
         curl FORWARDING_RULE_IP
         

The output is similar to the following:
         
         Page served from: l7-ilb-backend-example-1c7t
         




## Limitations for route extensions

  * Route extensions don't support HTTP body processing.
  * A direct response from the extension to the client isn't supported for route extensions. If your route extension server responds to a processing request with a processing response that contains a direct response, the load balancer ignores the processing response.



For limitations that are applicable to all extensions, see [Limitations for extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#limitations).

## What's next

  * View Rust, Go, and C++ plugin examples and testing tools in the [Service Extensions GitHub repository for plugins](https://github.com/GoogleCloudPlatform/service-extensions/tree/main/plugins#docs).
  * View Python and Go samples of `ext_proc` servers in the [Service Extensions GitHub repository for callouts](https://github.com/GoogleCloudPlatform/service-extensions/tree/main/callouts).
  * [Configure traffic extensions](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions)
  * [Manage extensions](https://docs.cloud.google.com/service-extensions/docs/manage-extensions)
  * [Manage plugins](https://docs.cloud.google.com/service-extensions/docs/manage-plugins)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
