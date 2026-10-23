---
url: https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions/
title: Configure a traffic extension \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:09.723562+00:00
---

# Configure a traffic extension  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Configure a traffic extension Stay organized with collections  Save and categorize content based on your preferences. 

Service Extensions enables [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) to use plugins or send callouts to backend services to insert custom processing in the processing path. [Traffic extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#traffic-extensions) run last in the request processing path and first in the response processing path to modify headers and payloads without impacting the choice of the backend service. This page describes how to configure traffic extensions.

For an overview about Application Load Balancer extensions, see [Cloud Load Balancing extensions overview](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview).

A traffic extension for an Application Load Balancer points to the following resources:

  * A forwarding rule to attach to
  * A plugin or a callout backend service whose backends run the `ext_proc` gRPC API



A traffic extension groups related extension services into one or more chains. You can configure both plugins and callouts in the same extension chain. Each extension chain selects the traffic to act on by using [Common Expression Language (CEL)](https://docs.cloud.google.com/service-extensions/docs/cel-matcher-language-reference) match conditions. The load balancer evaluates a request against each chain's match condition in a sequential manner. When a request matches the conditions defined by a chain, all extensions in the chain act on the request. Only one chain matches a given request.

Each extension in a chain can have its own set of supported events. The modifications that are made by an extension to request and response content are visible to the remaining extensions in the chain. For extensions that are configured to support response events, the sequence of extensions is reversed on the response path.

The traffic extension references the load balancer [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) to attach to. After you configure the resource, the load balancer starts sending matching requests to extension services.

For information about the limits related to extensions, see the [Quotas and limits](https://docs.cloud.google.com/service-extensions/docs/quotas#lb-extensions) page.

**Important:** You can attach only one traffic extension to a forwarding rule.

## Configure using plugins

This section shows you how to configure a traffic extension by using a plugin.

All extension resources that reference a given plugin must be of the same type. The extensions must also have the same load balancing scheme. You can't configure Cloud Load Balancing extensions with plugins that are already used in Media CDN extensions.

### Before you begin

  1. [Create a plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin) that contains your [custom code](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code).

  2. Create and configure an [Application Load Balancer that supports traffic extension plugins](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs).

For example, [set up a global external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute).

  3. Set up a way to send test requests to your service—for example, by running curl. If you're using an internal load balancer, [create a client VM for testing](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#test_client).




### Configure a traffic extension by using a plugin

The following example helps you configure a traffic extension by using a plugin that adds a response header, `hello: service-extensions`, when the host matches `example.com`.

  1. Check if there's a match for `example.com` in the URL map.

     1. Run the following `curl` command against the forwarding rule in the client VM:
            
            curl -D - -H "host: example.com" FORWARDING_RULE_IP
            

Replace `FORWARDING_RULE_IP` with the IP address of the forwarding rule. To find the IP address, use the [`gcloud compute forwarding-rules describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/describe).

The output is similar to the following:
            
            HTTP/1.1 200 OK
            ...
            content-length: 46
            content-type: text/html
            via: 1.1 google
            

  2. Configure the traffic extension.

### Console

     1. In the Google Cloud console, go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

     2. Click **Create extension**.

A wizard opens to guide you through some initial steps.

     3. For the product, select **Load Balancing**. Then, click **Continue**.

A list of [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) appears.

     4. For the load balancer type, select either global external Application Load Balancer or cross-region internal Application Load Balancer. Then, click **Continue**.

     5. For the extension type, select **Traffic extensions** , and then click **Continue**.

     6. To open the **Create extension** form, click **Continue**.

In the **Create extension** form, notice that the preceding selections, which appear at the top of the page, are not editable.

     7. In the **Basics** section, do the following:

        1. Specify a unique name for the extension.

The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens and must not end with a hyphen.

        2. Optional: Enter a brief description about the extension by using up to 1,024 characters.

     8. Optional: In the **Labels** section, click **Add label**. Then, in the row that appears, do the following:

        * For **Key** , enter a key name.
        * For **Value** , enter a value for the key.

To add more key-value pairs, click **Add label**. You can add a maximum of 64 key-value pairs.

For more information about labels, see [Create and update labels for projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels).

     9. For **Forwarding rules** , select one or more forwarding rules to associate with the extension—for example, `http-content-rule`.

Forwarding rules that are already associated with another extension can't be selected and appear unavailable.

     10. For **Extension** , to add an extension to execute for a matching request, do the following:

        * To match requests for which the extension chain is executed, for **Match condition** , specify a Common Expression Language (CEL) expression—for example, `request.host == "example.com"`.

For more information about CEL expressions, click **Get syntax help** or see [CEL matcher language reference](https://docs.cloud.google.com/service-extensions/docs/cel-matcher-language-reference).

        * For **Programmability type** , select **Plugins**.

        * For **Plugin** , select a plugin [created using Service Extensions](https://docs.cloud.google.com/service-extensions/docs/create-plugin) for the same product and extension type.

        * For **Events** , select one or more HTTP event types that call the extension.

        * For **Forward attributes** , select the request, connection, and location attributes that you want the load balancer to forward to your Wasm plugin. You can configure a maximum of 16 attributes for each extension. For more information, see [Supported attributes](https://docs.cloud.google.com/service-extensions/docs/attributes).

        * For **Forward headers** , click **Add header** , and then add HTTP headers to forward to the extension (from the client or the backend). If a header isn't specified, all headers are sent.

        * Optional: if the extension times out or fails and you want request or response processing to continue, for **Fail open** , select **Enabled**. Subsequent extensions in the chain are also executed.

By default, the **Fail open** option isn't selected. In this case, when an error occurs, request or response processing stops. If response headers haven't been delivered to the downstream client, a generic HTTP `500` status code is returned to the client. If response headers have been delivered, the HTTP stream to the client is reset.

The default option of keeping **Fail open** unselected is preferred when prioritizing security or integrity. Enabling **Fail open** , especially for non-critical operations, helps when prioritizing availability.

If you want to specify more than one extension or extension chains rather than a single extension, click the **Switch to advanced mode** button at the end of the form and specify the required extensions and chains. The extensions run in the sequence in which they are listed.

Specify unique names for each extension and extension chain. The names must conform with RFC-1034, use only lowercase letters, numbers, and hyphens, and have a maximum length of 63 characters. Additionally, the first character must be a letter and the last character must be a letter or a number.

     11. Click **Create extension**.

###  gcloud 

     1. Define the plugin in a YAML file and associate it with a forwarding rule—for example, `http-content-rule`.
            
            cat >traffic-plugin.yaml <<EOF
                name: traffic-ext
                forwardingRules:
                - https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/forwardingRules/http-content-rule
                loadBalancingScheme: EXTERNAL_MANAGED
                extensionChains:
                - name: "chain1"
                  matchCondition:
                    celExpression: 'request.host == "example.com"'
                  extensions:
                  - name: 'ext1'
                    service: projects/PROJECT_ID/locations/LOCATION/wasmPlugins/WASM_PLUGIN
                    failOpen: false
                    supportedEvents:
                    - RESPONSE_HEADERS
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

The `forwardAttributes` field lets you specify the request, connection, and location attributes that you can forward to your Wasm plugin. You can configure a maximum of 16 attributes for each extension. For more information about supported attributes, see [Supported attributes](https://docs.cloud.google.com/service-extensions/docs/attributes).

     2. Import the traffic extension. Use the [`gcloud service-extensions lb-traffic-extensions import` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/lb-traffic-extensions/import) with the following sample values.
            
            gcloud service-extensions lb-traffic-extensions import traffic-ext \
                --source=traffic-plugin.yaml \
                --location=global
            

After a traffic extension is created, it takes a little time for the new plugin to be distributed across all locations. The time might vary across locations because the plugin isn't delivered to all locations simultaneously.

  3. To verify that the traffic extension works as expected, use the same `curl` command:
         
         curl -D - -H "host: example.com" FORWARDING_RULE_IP
         

The output includes the `hello: service-extensions` response header.
         
         HTTP/1.1 200 OK
         ...
         content-length: 46
         content-type: text/
         hello: service-extensions
         via: 1.1 google
         

To validate that the extension targets only `example.com` traffic, repeat the `curl` command without the `host` header.
         
         curl -D - FORWARDING_RULE_IP
         

The output is similar to the following:
         
         HTTP/1.1 200 OK
         ...
         content-length: 46
         content-type: text/html
         via: 1.1 google
         




## Configure traffic extensions to user-managed services by using callouts

This section shows you how to configure a traffic extension to a user-managed callout backend service by using a callout.

### Before you begin

Create the required resources as described in [Configure a callout backend service](https://docs.cloud.google.com/service-extensions/docs/configure-callout-backend-service).

### Configure a traffic extension by using a callout

The following example helps you configure a traffic extension by using a callout to call when the host matches `example.com`. The traffic extension server in the `callout-vm` adds a response header, `hello: service-extensions`, to matching requests.

  1. Check if there's a match for `example.com` in the URL map.

     1. Run the following `curl` command against the forwarding rule in the client VM:
            
            curl -D - -H "host: example.com" FORWARDING_RULE_IP
            

Replace `FORWARDING_RULE_IP` with the IP address of the forwarding rule. To find the IP address, use the [`gcloud compute forwarding-rules describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/describe).

The output is similar to the following:
            
            HTTP/1.1 200 OK
            ...
            content-length: 46
            content-type: text/html
            via: 1.1 google
            
            Page served from: l7-ilb-backend-example-1c7t
            

  2. Configure the traffic extension.

### Console

     1. In the Google Cloud console, go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

     2. Click **Create extension**.

A wizard opens to guide you through some initial steps.

     3. For the product, select **Load Balancing**. Then, click **Continue**.

A list of [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) appears.

     4. Select a load balancer type. For regional load balancers, also specify the region. Click **Continue**.

     5. For the extension type, select **Traffic extensions** , and then click **Continue**.

     6. To open the **Create extension** form, click **Continue**.

In the **Create extension** form, notice that the preceding selections, which appear at the top of the page, are not editable.

     7. In the **Basics** section, do the following:

        1. Specify a unique name for the extension.

The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens and must not end with a hyphen.

        2. Optional: Enter a brief description about the extension by using up to 1,024 characters.

     8. Optional: In the **Labels** section, click **Add label**. Then, in the row that appears, do the following:

        * For **Key** , enter a key name.
        * For **Value** , enter a value for the key.

To add more key-value pairs, click **Add label**. You can add a maximum of 64 key-value pairs.

For more information about labels, see [Create and update labels for projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels).

     9. For **Forwarding rules** , select one or more forwarding rules to associate with the extension—for example, `l7-ilb-forwarding-rule`.

Forwarding rules that are already associated with another extension can't be selected and appear unavailable.

     10. For **Extension** , to add an extension to execute for a matching request, do the following:

        * For **Programmability type** , select **Callouts**.

        * To match requests for which the extension chain is executed, for **Match condition** , specify a Common Expression Language (CEL) expression—for example, `request.host == "example.com"`.

For more information about CEL expressions, click **Get syntax help** or see [CEL matcher language reference](https://docs.cloud.google.com/service-extensions/docs/cel-matcher-language-reference).

        * For **Authority** , enter the `authority` header from the gRPC request sent from the load balancer to the extension service.

        * For **Backend service** , select a backend service created by following the instructions in [Configure a callout backend service](https://docs.cloud.google.com/service-extensions/docs/configure-callout-backend-service).

        * For **Timeout** , specify a value between 10 and 1000 milliseconds after which a message on the stream times out.

        * For **Events** , select one or more HTTP event types that call the extension.

        * For **Forward attributes** , select the request, connection, and location attributes that you want the load balancer to forward to your callout service. You can configure a maximum of 16 attributes for each extension. For more information, see [Supported attributes](https://docs.cloud.google.com/service-extensions/docs/attributes).

        * For **Forward headers** , click **Add header** , and then add HTTP headers to forward to the extension (from the client or the backend). If a header isn't specified, all headers are sent.

        * Optional: if the extension times out or fails and you want request or response processing to continue, for **Fail open** , select **Enabled**. Subsequent extensions in the chain are also executed.

By default, the **Fail open** option isn't selected. In this case, when an error occurs, request or response processing stops. If response headers haven't been delivered to the downstream client, a generic HTTP `500` status code is returned to the client. If response headers have been delivered, the HTTP stream to the client is reset.

The default option of keeping **Fail open** unselected is preferred when prioritizing security or integrity. Enabling **Fail open** , especially for non-critical operations, helps when prioritizing availability.

        * For **Metadata** , click **Add metadata** and specify sample values as suggested. For **Key** , specify `key`, and for **Value** , specify `value`.

Click **Add metadata** to add another key-value pair. For **Key** , specify `fr`, and for **Value** , specify `forwarding_rule_id`.

The **Metadata** field lets you pass any additional information from the load balancer to the extension server. The metadata is sent in a `ProcessingRequest` message and encoded as `protobuf.Struct`. Any text within the metadata that matches the specified forwarding rule ID is replaced with the fully qualified resource URL of the forwarding rule associated with the client request.

The total size of the metadata must be less than 1 KiB. The total number of keys in the metadata must be less than 20. The length of each key must be less than 64 characters. The length of each value must be less than 1,024 characters. All values must be strings.

If you want to specify more than one extension or extension chains rather than a single extension, click the **Switch to advanced mode** button at the end of the form and specify the required extensions and chains. The extensions run in the sequence in which they are listed.

Specify unique names for each extension and extension chain. The names must conform with RFC-1034, use only lowercase letters, numbers, and hyphens, and have a maximum length of 63 characters. Additionally, the first character must be a letter and the last character must be a letter or a number.

     11. Click **Create extension**.

###  gcloud 

     1. Define the callout in a YAML file and associate it with the forwarding rule. Use the sample values provided.
            
            cat >traffic.yaml <<EOF
                name: traffic-ext
                forwardingRules:
                - https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules/l7-ilb-forwarding-rule
                loadBalancingScheme: INTERNAL_MANAGED
                extensionChains:
                - name: "chain1"
                  matchCondition:
                    celExpression: 'request.host == "example.com"'
                  extensions:
                  - name: 'ext11'
                    authority: ext11.com
                    service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/l7-ilb-callout-service
                    failOpen: false
                    timeout: 0.1s
                    metadata:
                      "key": "value"
                      "fr": "forwarding_rule_id"
                    supportedEvents:
                    - RESPONSE_HEADERS
                    forwardAttributes:
                    - request.host
                    - request.path
            EOF
            

Replace `PROJECT_ID` with the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

The `metadata` field in the extension configuration lets you pass any additional information from the load balancer to the extension server. The metadata is sent in a `ProcessingRequest` message and encoded as `protobuf.Struct`. Any text within the metadata that matches the specified forwarding rule ID is replaced with the fully qualified resource URL of the forwarding rule associated with the client request.

The total size of `metadata` must be less than 1 KiB. The total number of keys in the metadata must be less than 16. The length of each key must be less than 64 characters. The length of each value must be less than 1,024 characters. All values must be strings.

For more information about the fields in the YAML file, see [ExtensionChain](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/ExtensionChain) in the API documentation.

The `forwardAttributes` field lets you specify the request, connection, and location attributes to forward to your callout service. You can configure a maximum of 16 attributes for each extension. For more information about supported attributes, see [Supported attributes](https://docs.cloud.google.com/service-extensions/docs/attributes).

     2. Import the traffic extension. Use the [`gcloud service-extensions lb-traffic-extensions import` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/lb-traffic-extensions/import) with the following sample values.
            
            gcloud service-extensions lb-traffic-extensions import traffic-ext \
                --source=traffic.yaml \
                --location=us-west1
            

  3. Verify that the traffic extension works as expected. Use the same `curl` command:
         
         curl -D - -H "host: example.com" FORWARDING_RULE_IP
         

The output includes the `hello: service-extensions` response header.
         
         HTTP/1.1 200 OK
         ...
         content-length: 46
         content-type: text/
         hello: service-extensions
         via: 1.1 google
         
         Page served from: l7-ilb-backend-example-1c7t
         

To validate that the extension targets only `example.com` traffic, repeat the `curl` command without the `host` header.
         
         curl -D - FORWARDING_RULE_IP
         

The output is similar to the following:
         
         HTTP/1.1 200 OK
         ...
         content-length: 46
         content-type: text/html
         via: 1.1 google
         
         Page served from: l7-ilb-backend-example-1c7t
         




## What's next

  * View Rust, Go, and C++ plugin examples and testing tools in the [Service Extensions GitHub repository for plugins](https://github.com/GoogleCloudPlatform/service-extensions/tree/main/plugins#docs).
  * View Python and Go samples of `ext_proc` servers in the [Service Extensions GitHub repository for callouts](https://github.com/GoogleCloudPlatform/service-extensions/tree/main/callouts).
  * [Configure route extensions](https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions)
  * [Manage extensions](https://docs.cloud.google.com/service-extensions/docs/manage-extensions)
  * [Manage plugins](https://docs.cloud.google.com/service-extensions/docs/manage-plugins)
  * [Configure an extension to a Google service](https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
