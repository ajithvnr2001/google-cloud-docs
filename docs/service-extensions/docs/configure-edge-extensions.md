---
url: https://docs.cloud.google.com/service-extensions/docs/configure-edge-extensions/
title: Configure an edge extension \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:36.006612+00:00
---

# Configure an edge extension  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/configure-edge-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Configure an edge extension Stay organized with collections  Save and categorize content based on your preferences. 

Service Extensions enables [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) to use plugins to insert custom processing in the processing path. [Edge extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#edge-extensions) run in the request processing path when the load balancer receives request headers and before it evaluates the [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts) or calls Cloud CDN, which lets you influence caching and routing. This page describes how to configure edge extensions.

For an overview about Application Load Balancer extensions, see [Cloud Load Balancing extensions overview](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview).

An extension for an Application Load Balancer points to the following resources:

  * A forwarding rule to attach to
  * A plugin



The extension references the load balancer [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) to attach to. After you configure the resource, the load balancer starts sending matching requests to extension services. You can attach only one edge extension to a forwarding rule and include only one plugin in an edge extension chain.

For information about the limits related to Application Load Balancer extensions, see the [Quotas and limits](https://docs.cloud.google.com/service-extensions/docs/quotas#lb-extensions) page.

## Configure using plugins

This section uses an example to show you how to configure an edge extension by using a plugin that rewrites the `:host` request header to `service-extensions.com` when the path matches `/extensions`. The earlier host and the newly configured host are mapped to backend services in different regions, which demonstrates the routing behavior.

All extension resources that reference a given plugin must be of the same type. The extensions must also have the same load balancing scheme. You can't configure Cloud Load Balancing extensions with plugins that are already used in Media CDN extensions.

### Before you begin

  1. [Create a plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin) that contains your [custom code](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code).

  2. Create and configure an [Application Load Balancer that supports edge extension plugins](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs).

Follow the instructions on the [Set up a global external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute) page for all steps, except the following:

     * Name the backend service as `service-one`.
     * Point `service-one` to a virtual machine (VM) instance in region `A`.
     * Point `gl7-gxlb-url-map` to `service-one` by default.
  3. Set up an additional backend service, `service-two` and point it to a VM in region `B`.

  4. To the URL map, add a path matcher pointing to `service-two`. Use the [`gcloud compute url-maps add-path-matcher` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher) with the following sample values:
         
         gcloud compute url-maps add-path-matcher gl7-gxlb-url-map \
             --path-matcher-name=rewrite-host \
             --default-service=service-two \
             --new-hosts=service-extensions.com \
             --location=global
         

  5. Set up a way to send test requests to your service (for example, by running curl).




### Configure an edge extension by using a plugin

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
            

  2. Configure the edge extension.

### Console

     1. In the Google Cloud console, go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

     2. Click **Create extension**.

A wizard opens to guide you through some initial steps.

     3. For the product, select **Load Balancing**. Then, click **Continue**.

A list of [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) appears.

     4. For the load balancer type, select global external Application Load Balancer. Then, click **Continue**.

     5. For the extension type, select **Edge extensions** , and then click **Continue**.

     6. To open the **Create extension** form, click **Continue**.

In the **Create extension** form, notice that the preceding selections aren't editable.

     7. In the **Basics** section, do the following:

        1. Specify a unique name for the extension.

The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens and must not end with a hyphen.

        2. Optional: Enter a brief description about the extension by using a maximum of 1,024 characters.

     8. Optional: In the **Labels** section, click **Add label**. Then, in the row that appears, do the following:

        * For **Key** , enter a key name.
        * For **Value** , enter a value for the key.

To add more key-value pairs, click **Add label**. You can add a maximum of 64 key-value pairs.

For more information about labels, see [Create and update labels for projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels).

     9. For **Forwarding rules** , select one or more forwarding rules to associate with the extension—for example, `cr-xlb-forwarding-rule`.

Forwarding rules that are already associated with another extension can't be selected and appear disabled.

     10. For **Extension** , to add an extension to execute for a matching request, do the following:

        * To match requests for which the extension chain is executed, for **Match condition** , specify a Common Expression Language (CEL) expression—for example, `request.path.startsWith("/extensions")`.

Edge extensions let you use only one regular expression for each CEL expression.

For more information about CEL expressions, click **Get syntax help** or see [CEL matcher language reference](https://docs.cloud.google.com/service-extensions/docs/cel-matcher-language-reference).

        * For **Programmability type** , select **Plugins**.

        * For **Plugin** , select a plugin [created using Service Extensions](https://docs.cloud.google.com/service-extensions/docs/create-plugin) or the same product and extension type. You can include only one plugin in an edge extension.

        * For **Forward attributes** , select the request, connection, and location attributes that you want the load balancer to forward to your Wasm plugin or callout. You can configure a maximum of 16 attributes for each extension. For more information, see [Supported attributes](https://docs.cloud.google.com/service-extensions/docs/attributes).

        * For **Forward headers** , click **Add header** , and then add HTTP headers to forward to the extension (from the client or the backend). If a header isn't specified, all headers are sent.

        * Optional: For **Fail open** , if you want the extension to fail open, select **Enabled**. In this case, if the call to the extension fails or times out, request or response processing continues without error.

By default, the **Fail open** field isn't selected. In this case, if response headers have not been delivered to the downstream client, a generic HTTP `500` status code is returned to the client. If response headers have been delivered, the HTTP stream to the downstream client is reset.

For an edge extension, you can specify only one extension for each extension chain.

If you want to specify more than one extension or extension chains rather than a single extension, click the **Switch to advanced mode** button at the end of the form and specify the required extensions and chains. The extensions run in the sequence in which they are listed.

Specify unique names for each extension and extension chain. The names must conform with RFC-1034, use only lowercase letters, numbers, and hyphens, and have a maximum length of 63 characters. Additionally, the first character must be a letter and the last character must be a letter or a number.

     11. Click **Create extension**.

### gcloud

     1. Define the plugin in a YAML file and associate it with a global forwarding rule—for example, `cr-xlb-forwarding-rule`.
            
            cat >edge-plugin.yaml <<EOF
                name: edge-ext
                forwardingRules:
                - https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/global/forwardingRules/cr-xlb-forwarding-rule
                loadBalancingScheme: EXTERNAL_MANAGED
                extensionChains:
                - name: "chain1"
                  matchCondition:
                    celExpression: 'request.path.startsWith("/extensions")'
                  extensions:
                  - name: 'ext1'
                    service: projects/PROJECT_ID/locations/global/wasmPlugins/WASM_PLUGIN
                    failOpen: false
                    supportedEvents:
                    - REQUEST_HEADERS
                    forwardAttributes:
                    - request.host
                    - request.path
            EOF
            

Replace the following:

        * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
        * `WASM_PLUGIN`: the ID or the fully qualified name of the plugin

Edge extensions let you use only one regular expression for each CEL expression.

For more information about the fields in the YAML file, see [ExtensionChain](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/ExtensionChain) in the API documentation.

The `forwardAttributes` field lets you specify the request, connection, and location attributes that you can forward to Wasm plugins or callout services. You can configure a maximum of 16 attributes for each extension. For more information about supported attributes, see [Supported attributes](https://docs.cloud.google.com/service-extensions/docs/attributes).

     2. Import the edge extension. Use the [`gcloud service-extensions lb-edge-extensions import` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/lb-edge-extensions/import) with the following sample values:
            
            gcloud service-extensions lb-edge-extensions import edge-ext \
                --source=edge-plugin.yaml \
                --location=global
            

After an edge extension is created, it takes a little time for the new plugin to be distributed across all locations. The time might vary across locations because the plugin isn't delivered to all locations simultaneously.

  3. To verify that the edge extension works as expected, use the same `curl` command:
         
         curl FORWARDING_RULE_IP/extensions
         

The output is similar to the following and indicates that the page is served from a VM in `region B`:
         
         Page served from region-B-vm
         

To verify that the plugin runs only for requests with the `/extension` path prefix, repeat the `curl` command without a path.
         
         curl FORWARDING_RULE_IP
         

The output is similar to the following:
         
         Page served from region-A-vm
         




## Limitations for edge extensions

  * You can attach only one edge extension to a forwarding rule.
  * Edge extensions don't support HTTP body processing.
  * Edge extensions let you use only one regular expression for each CEL expression.



For limitations that are applicable to all extensions, see [Limitations for extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#limitations).

## What's next

  * View Rust, Go, and C++ plugin examples and testing tools in the [Service Extensions GitHub repository for plugins](https://github.com/GoogleCloudPlatform/service-extensions/tree/main/plugins#docs).
  * [Manage extensions](https://docs.cloud.google.com/service-extensions/docs/manage-extensions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
