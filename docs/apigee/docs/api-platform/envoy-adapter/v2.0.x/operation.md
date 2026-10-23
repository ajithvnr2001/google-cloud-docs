---
url: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/operation/
title: Operations guide \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:06.588035+00:00
---

# Operations guide  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/operation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Operations guide Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## How to obtain an API key

The following example explains how to obtain an API key that you can use to validate API calls to a target service proxied through Apigee Adapter for Envoy. 

**NOTE:** If you are an experienced Apigee user, the following steps will be familiar, as they are standard Edge configurations; however, **please follow these instructions carefully, as they require you to insert specific Product and Developer App configurations**.

### 1\. Log in to Apigee

  1. Sign in to the [Apigee UI](https://apigee.google.com/).
  2. Select the same organization that you used to provision Apigee Adapter for Envoy.



### 2\. Create a Developer

You can use an existing developer for testing, or create a new one as follows:

  1. Select **Publish > Developers** in the side navigation menu.
  2. Click **\+ Developer.**
  3. Fill out the dialog to create a new developer. You can use any developer name/email that you wish.



### 3\. Create an API Product

Follow the Product creation example provided below.

  1. Select **Publish > API Products** in the side navigation menu.
  2. Click **+CREATE**.
  3. Fill out the **Product details** section as follows. Only the required fields are mentioned in the following table: Field | Value | Description  
---|---|---  
**Name** |  `httpbin-product` | The unique name of the API product.  
**Display Name** |  `httpbin product` |  The descriptive name you want to see in the UI or other display contexts.   
**Access** |  `Public` |  For the purpose of this example, **Public** is a good choice.   
  4. In the Operations section, click **+ADD AN OPERATION**.
  5. In the **Source** section, select **Remote Service**.
  6. Switch the **Source** toggle to allow you to manually type the name of a remote service in the Remote Service field. 
  7. In the **Remote Service** field, enter the name of a remote service. This is a target service to which the adapter proxies incoming HTTP requests. For testing purposes, use [`httpbin.org`](https://httpbin.org) or [`httpbin.default.svc.cluster.local`](https://httpbin.default.svc.cluster.local) with Kubernetes. 

![The Remote Service radio button is selected, toggle enabling manual text entry is enabled, and the remote service httpbin.org is entered in the Remote Service field.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/operation-toggle.png)

  8. In the **Operation** section, enter `/` for the path. For information about path options, see [Configuring resource paths](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#behavior-resource-path).
  9. Click **SAVE** to save the operation.
  10. Click **SAVE** to save the API product.



For more information, see [Managing API products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products). 

### 4\. Create a Developer App

The developer app contains the API key that is required to make API proxy calls through the adapter. 

  1. Select **Publish Apps** in the side navigation menu.
  2. Click **\+ App**.
  3. Fill out the **App Details** section as follows. Only the required fields are mentioned in the following table: 
**Name** | `httpbin-app`  
---|---  
**Developer** | Select the developer you created previously, or pick any developer you wish from the list.   
  4. In the Credentials section, click **\+ Add product** and select the product you just configured: **httpbin-product**. 
  5. Click **Create**.
  6. Under Credentials, click **Show** next to the **Key**.
  7. **Copy the value of the Consumer Key.** This value is the **API key** that you will use to make API calls to the `httpbin` service through the Apigee Adapter for Envoy.



##  Using JWT based authentication 

You can use a JWT token to make authenticated API proxy calls instead of using an API key. This section explains how to use the `apigee-remote-service-cli token` command to create, inspect, and rotate JWT tokens. For an Apigee hybrid environment, you can use this command to create Kubernetes secret to hold the JWT(s). 

###  Overview 

JWT verification and authentication is handled by Envoy using its [ JWT Authentication Filter](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/security/jwt_authn_filter).

Once authenticated, the Envoy `ext-authz` filter sends the request headers and JWT to `apigee-remote-service-envoy`. It matches the JWT's `api_product_list` and `scope` claims against Apigee API Products to authorize it against the target of the request.

### Creating Apigee JWT tokens

Apigee JWT Tokens can be created using the CLI:
    
    
    apigee-remote-service-cli token create -c config.yaml --id $KEY --secret $SECRET

Or by using the standard OAuth token endpoint. Curl example:
    
    
    curl https://org-env.apigee.net/remote-token/token -d '{"client_id":"myclientid","client_secret":"myclientsecret","grant_type":"client_credentials"}' -H "Content-type: application/json"

**NOTE:** The Content-type header is required.

### Using the JWT token

Once you have the token, you simply pass it to Envoy in the Authorization header. Example:
    
    
    curl localhost:8080/httpbin/headers -i -H "Authorization:Bearer $TOKEN"

### JWT token failure

#### Envoy rejection

If Envoy rejects the token, you may see a message like:
    
    
    Jwks remote fetch has failed

If so, ensure that your Envoy configuration contains a valid URI in the `remote_jwks` section, that it's reachable by Envoy, and that you properly set the certificates when you installed the Apigee proxy. You should be able to call the URI directly with a GET call and receive a valid JSON response.

Example:
    
    
    curl https://myorg-eval-test.apigee.net/remote-service/certs

Other messages from Envoy may look like:

  * "Audiences in Jwt are not allowed"
  * "Jwt issuer is not configured"



These are from requirements in your Envoy configuration that you may need to modify.

### Inspect a token

You can use the CLI to inspect your token. Example
    
    
    apigee-remote-service-cli -c config.yaml token inspect -f path/to/file

or 
    
    
    apigee-remote-service-cli -c config.yaml token inspect <<< $TOKEN

###  Debugging 

See [Valid API key fails](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/troubleshooting#valid-api-key-fails). 

##  Using your own Identity Provider 

By default, Apigee Adapter for Envoy uses the `remote-token` API proxy as an identity provider service to authenticate client applications and deliver JWT tokens based on the OAuth 2.0 client credentials grant type. In some cases, however, you may not be able to use the `remote-token` proxy. If you must use an identity provider that is not the one provided by Apigee, you can configure the adapter to use another identity provider. For details on this non-Apigee identity provider use case and the required configuration, see this article on the Apigee Community: [ Using your own Identity Provider with the Apigee Envoy Adapter](https://www.googlecloudcommunity.com/gc/Cloud-Product-Articles/Using-your-own-Identity-Provider-with-the-Apigee-Envoy-Adapter/ta-p/489103). 

##  Logging 

You can adjust the logging level on the $REMOTE_SERVICE_HOME/apigee-remote-service-envoy service. All logging is sent to stderr.

Element | Required | Description  
---|---|---  
-l, --log-level |  Valid levels: debug, info, warn, error. | Adjusts the logging level. Default: info  
-j, --json-log |  | Emits log output as JSON records.  
  
Envoy provides logging. For more information, see the following Envoy documentation links:

  * [Application Logging](https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/application_logging)
  * [Access Logs](https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/access_log/access_log)
  * [Stackdriver logging with GKE](https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/application_logging#stackdriver-logging-with-gke)



##  Changing the policy secret name 

A Kubernetes Secret deployed to the cluster contains credentials that the adapter needs to authenticate communication with the remote service proxy. This Secret requires a volume mount point, which is configurable. By default, the mount point is `/policy-secret`. To change the mount point, follow these steps: 

  1. Execute this command: 
         
         $REMOTE_SERVICE_HOME/apigee-remote-service-envoy --policy-secret '/new-mount_point_name

For example: 
         
         $REMOTE_SERVICE_HOME/apigee-remote-service-envoy --policy-secret '/my-mount-point

  2. Open `$CLI_HOME/samples/apigee-envoy-adapter.yaml` in an editor.
  3. Change the mount point name to the new name: 
         
         volumeMounts:
           - mountPath: /config
             name: apigee-remote-service-envoy
             readOnly: true
           - mountPath: /opt/apigee/tls
             name: tls-volume
             readOnly: true
           - mountPath: **/my-mount-point**
             name: policy-secret
             readOnly: true

  4. Save the file and apply it to the service mesh: 
         
         kubectl apply -f $REMOTE_SERVICE_HOME/samples/apigee-envoy-adapter.yaml




##  Using a network proxy 

An HTTP proxy can be inserted by using the HTTP_PROXY and HTTPS_PROXY environment variables in the environment of the apigee-remote-service-envoy binary. When using these, the NO_PROXY environment variable can also be used to exclude specific hosts from being sent through the proxy.
    
    
    HTTP_PROXY=http://[user]:[pass]@[proxy_ip]:[proxy_port]
    HTTPS_PROXY=http://[user]:[pass]@[proxy_ip]:[proxy_port]
    NO_PROXY=127.0.0.1,localhost

Remember that the proxy must be reachable from apigee-remote-service-envoy.

##  About metrics and analytics 

A Prometheus metrics endpoint is available at `:5001/metrics`. You can configure this port number. See [Configuration file](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/reference#configuration-file).

### Envoy analytics

The following links provide information on obtaining Envoy proxy analytics data: 

  * [Admin interface](https://www.envoyproxy.io/docs/envoy/latest/operations/admin)
  * [Stats](https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/statistics)
  * [Cluster stats](https://www.envoyproxy.io/docs/envoy/latest/configuration/upstream/cluster_manager/cluster_stats)



### Istio analytics

The following links provide information on obtaining Envoy proxy analytics data: 

  * [Observability tasks](https://istio.io/docs/tasks/observability/)
  * [Telemetry configuration](https://istio.io/docs/ops/configuration/telemetry/)



###  Apigee analytics 

Apigee Remote Service for Envoy sends request statistics to Apigee for analytics processing. Apigee reports these requests under the associated API Product name.

For information about Apigee analytics, see [Analytics services overview](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview).

##  Multi-tenant environment support 

You can now enable the adapter to service multiple environments in an Apigee organization. This feature allows you to use one Apigee Adapter for Envoy associated with one Apigee organization to service multiple environments. Before this change, one adapter was always tied to one Apigee environment. 

To configure multiple environment support, change the value of `tenant:env_name` to `"*"` in the `config.yaml` file. For example: 

  1. Open the `config.yaml` file in an editor.
  2. Change the value of `tenant.env_name` to `"*"`. For example: 
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: apigee-remote-service-envoy
           namespace: apigee
         data:
           config.yaml: |
             tenant:
               remote_service_api: https://apitest.mydomain.net/remote-service
               org_name: my-org
               env_name: "*""
               allow_unverified_ssl_cert: true
             analytics:
               collection_interval: 10s
             auth:
               jwt_provider_key: https://apitest.mydomain.net/remote-token/token

  3. Save the file.
  4. Apply the file: 
         
         kubectl apply -f $CLI_HOME/config.yaml




When you configure multi-environment mode, you must also configure Envoy to send an appropriate environment value to the adapter by adding the following metadata in the `virtual_hosts:routes` section of the `envoy-config.yaml` file. For example: 

  1. Generate the `envoy-config.yaml` file using the CLI. For example: 
         
         $CLI_HOME/apigee-remote-service-cli samples create \
           -t envoy-1.16 -c ./config.yaml --out myconfigs

  2. Open the generated file (it's called `envoy-config.yaml`).
  3. Add the following metadata in either the `virtual_host` or `routes` section of the file: 
         
         typed_per_filter_config:
           envoy.filters.http.ext_authz:
             "@type": type.googleapis.com/envoy.extensions.filters.http.ext_authz.v3.ExtAuthzPerRoute
             check_settings:
               context_extensions:
                 apigee_environment: test

The following example illustrates configuration for a `virtual_host` with multiple routes defined, where each route sends traffic to a specific environment: 
         
         filter_chains:
             - filters:
               - name: envoy.filters.network.http_connection_manager
                 typed_config:
                   "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
                   stat_prefix: ingress_http
                   route_config:
                     virtual_hosts:
                     - name: default
                       domains: "*"
                       routes:
                       - match: { prefix: /test }
                         route:
                           cluster: httpbin
                         typed_per_filter_config:
                           envoy.filters.http.ext_authz:
                             "@type": type.googleapis.com/envoy.extensions.filters.http.ext_authz.v3.ExtAuthzPerRoute
                             check_settings:
                               context_extensions:
                                  apigee_environment: test
                       - match: { prefix: /prod }
                         route:
                           cluster: httpbin
                         typed_per_filter_config:
                           envoy.filters.http.ext_authz:
                             "@type": type.googleapis.com/envoy.extensions.filters.http.ext_authz.v3.ExtAuthzPerRoute
                             check_settings:
                               context_extensions:
                                  apigee_environment: prod

  4. Repeat the last step to add additional environments as needed.
  5. Save the file and apply it. **Note:** If `env_name` in `config.yaml` is set to any other value besides `"*"`, the adapter will return an error to Envoy and the request will be denied if the adapter's configuration of `env_name` is not set to `"*"`, or the `env_name` property does not match the passed the `apigee_environment` metadata.



##  Capturing data for custom reports 

The Adapter supports passing Envoy metadata to Apigee's data capture feature, which sends data captured in variables that you specify to Apigee analytics for use in custom reports. This feature provides a capability that is similar to the Apigee [Data Capture policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy). 

To use this feature:

  1. Create a [Data Collector REST resource](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy#data-collector-rest-resource).
  2. Define data capture variables using the [Apigee datacollectors API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors#DataCollector).
  3. If you haven't done so, generate the `envoy-config.yaml` file using the CLI. For example: 
         
         $CLI_HOME/apigee-remote-service-cli samples create \
           -t envoy-1.16 -c ./config.yaml --out myconfigs

  4. Open the generated file (it's called `envoy-config.yaml`).
  5. Use an Envoy filter to set values for your custom variables in the `envoy.filters.http.apigee.datacapture` namespace. For example, you can use a **Header to Metadata** filter or a **Lua** filter. For more information on these filters, see [Header-To-Metadata](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/http/header_to_metadata/v3/header_to_metadata.proto) and [Lua](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/http/lua/v3/lua.proto). 

The custom variable names must be formatted as `dc.XXXXX`. 

_Header to Metadata filter example:_
         
         - name: envoy.filters.http.header_to_metadata
           typed_config:
             "@type": type.googleapis.com/envoy.extensions.filters.http.header_to_metadata.v3.Config
             request_rules:
               - header: "Host"
                 on_header_present:
                   metadata_namespace: envoy.filters.http.apigee.datacapture
                   key: dc.host  # host (without the prefix) also works
                   type: STRING
                 remove: false

_Lua filter example:_
         
         - name: envoy.filters.http.lua
           typed_config:
             "@type": type.googleapis.com/envoy.extensions.filters.http.lua.v3.Lua
             inline_code: |
               function envoy_on_request(request_handle)
                 metadata = request_handle:streamInfo():dynamicMetadata()
                 metadata:set("envoy.filters.http.apigee.datacapture", "dc.test", "A test string.")
               end

  6. Add the desired filter to the file. See examples below. 
  7. Save the file and apply it.



##  Configuring mTLS between the adapter and Apigee runtime 

You can supply client-side TLS certificates in the `tenant` section of the adapter's `config.yaml` file to use mTLS between the adapter and the Apigee runtime. This change applies to all supported Apigee platforms. It also enables mTLS for analytics for the Apigee Edge for Private Cloud platform. For example: 
    
    
    tenant:
      tls:
        ca_file: path/ca.pem
        cert_file: path/cert.pem
        key_file: path/key.pem
        allow_unverified_ssl_cert: false

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
