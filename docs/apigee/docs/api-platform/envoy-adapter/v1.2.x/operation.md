---
url: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.2.x/operation/
title: Operations guide \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:52:01.949156+00:00
---

# Operations guide  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.2.x/operation/

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

**NOTE:** If you are an experienced Apigee user, the following steps will be familiar, as they are standard Apigee configurations; however, **please follow these instructions carefully, as they require you to insert specific Product and Developer App configurations**.

### 1\. Log in to Apigee

  1. Open the Apigee UI in a browser.
  2. Once your in the UI, select the same organization that you used to configure Apigee Adapter for Envoy.



### 2\. Create a Developer

You can use an existing developer for testing, or create a new one as follows:

  1. Select **Publish > Developers** in the side navigation menu.
  2. Click **\+ Developer.**
  3. Fill out the dialog to create a new developer. You can use any developer name/email that you wish.



### 3\. Create an API Product

Follow the Product creation example provided below. See also [About the API product configuration](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.2.x/operation#about_the_api_product_configuration).

  1. Select **Publish > API Products** in the side navigation menu.
  2. Click **\+ API Product**.
  3. Fill out the Product details page as follows. Do not click **Save** until instructed to do so.
Field | Value  
---|---  
**Name** | `httpbin-product`  
**Display Name** | `httpbin product`  
**Environment** | your_environment Set this to the environment you used when you provisioned Apigee Adapter for Envoy with the [`apigee-remote-service-cli`](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.2.x/example-hybrid#provision-apigee-hybrid).   
**Access** | `Private`  
**Quota** | **5 requests every 1 minute** See also About the API product configuration.   
  4. In the **Apigee remote service targets** section, click **Add an Apigee remote service target**.
  5. In the Apigee remote service target dialog, add the following values: Attribute | Value | Description  
---|---|---  
**Target name** | Enter the name of the target service. For example: `httpbin.org` | The target endpoint fronted by the Envoy proxy.  
**API proxy** | `remote-service` | The `remote-service` proxy that was provisioned on Apigee during the Envoy Adapter installation.  
**Path** | Enter a `/resource_path` to match a specific path. For example: `/httpbin`. | The request path to match on the target endpoint. API proxy calls to this path will match this API product.  
  6. Click **Save**.



### 4\. Create a Developer App

  1. Select **Publish > Apps** in the side navigation menu.
  2. Click **\+ App**.
  3. Fill out the Developer App page as follows. Do not Save until instructed to do so.
**Name** | `httpbin-app`  
---|---  
**Display Name** | `httpbin app`  
**Developer** | Select the developer you created previously, or pick any developer you wish from the list.   
  4. Next, add two products to the app: 
     1. First, in the Credentials section, click **\+ Add product** and select the product you just configured: **httpbin-product**. 
     2. Then, add the **remote-service** product. This product was created automatically when you provisioned Apigee.
  5. Click **Create**.
  6. Under Credentials, click **Show** next to the **Key**.
  7. **Copy the value of the Consumer Key.** This value is the **API key** that you will use to make API calls to the `httpbin` service.



## About API products

[API Products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product) are the primary control point for the Apigee Remote Service. When you create an API Product and bind it to a target service, you're creating a policy that will be applied to any requests that you configure your Apigee Adapter for Envoy to handle.

### API Product definition

When you define an API Product in Apigee, you can set a number of parameters that will be used to evaluate requests:

  * Target
  * Request path
  * Quota
  * OAuth scopes



#### Remote Service Targets

The API Product definition will apply to a request if the request matches both the target binding (for example, `httpbin.org`) and the request path (for example `/httpbin`). A list of potential targets is stored as an attribute on the API Product.

By default, the Apigee Remote Service checks Envoy's special `:authority (host)` header against its list of targets; however it can be configured to use other headers.

#### API Resource Path

The entered Path matches according to the following rules:

  * A single slash (`/`) by itself matches any path.
  * `*` is valid anywhere and matches within a segment (between slashes).
  * `**` is valid at the end and matches anything to the end of line.



#### Quota

A quota specifies the number of request messages that an app is allowed to submit to an API over the course of an hour, day, week, or month. When an app reaches its quota limit, subsequent API calls are rejected. 

_Quota use cases_

Quotas allow you to enforce the number of requests a client can make to a service in a given amount of time. Quotas are often used to enforce business contracts or SLAs with developers and partners, rather than for operational traffic management. For example, a quota might be used to limit traffic for a free service, while allowing full access for paying customers.

_Quota is defined in an API Product_

Quota parameters are configured in API Products. For example, when you create an API Product, you can optionally set the allowed quota limit, time unit, and interval.

![Setting a quota limit in the Apigee UI.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/quota-field.png)

Because API keys map back to API Products, each time an API key is verified the appropriate quota counter can be decremented (if a Quota is defined in the associated Product).

Unlike within the Apigee runtime, Quotas entered in the Product definition are automatically enforced by the Apigee Remote Service. If the request is authorized, the request will counted against the allowed quota.

_Where quotas are maintained_

Quotas are maintained and checked locally by the Remote Service process and asynchronously maintained with Apigee Runtime. This means the quotas are not precised and likely to have some overrun if you have more than one Remote Service that is maintaining the quota. If the connection to Apigee Runtime is disrupted, the local quota will continue as a stand-alone quota until such time as it can reconnect to the Apigee Runtime.

### OAuth Scopes

If you're using JWT tokens, you may restrict the tokens to subsets of the allowed OAuth scopes. The scopes assigned to your issued JWT token will be checked against the API Product's scopes.

## About Developer apps

Once you've configured your API Products, you will create an App associated with a Developer. The app allows a client access to the associated API Products with an API Key or JWT Token.

##  Using JWT based authentication 

You can use a JWT token to make authenticated API proxy calls instead of using an API key. This section explains how to use the `apigee-remote-service-cli token` command to create, inspect, and rotate JWT tokens. For Apigee hybrid environment, you can use this command to create Kubernetes secret to hold the JWT(s). 

###  Overview 

JWT verification and authentication is handled by Envoy using its [ JWT Authentication Filter](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/security/jwt_authn_filter).

Once authenticated, the Envoy `ext-authz` filter sends the request headers and JWT to `apigee-remote-service-envoy`. It matches the JWT's `api_product_list` and `scope` claims against Apigee API Products to authorize it against the target of the request.

### Creating Apigee JWT tokens

Apigee JWT Tokens can be created using the CLI:
    
    
    apigee-remote-service-cli token create -c config.yaml --id $KEY --secret $SECRET

Or by using the standard OAuth token endpoint. Curl example:
    
    
    curl https://org-env.apigee.net/remote-service/token -d '{"client_id":"myclientid","client_secret":"myclientsecret","grant_type":"client_credentials"}' -H "Content-type: application/json"

**NOTE:** The Content-type header is required.

### Using the JWT token

Once you have the token, you simply pass it to Envoy in the Authorization header. Example:
    
    
    curl localhost:8080/httpbin/headers -i -H "Authorization:Bearer $TOKEN"

### JWT token failure

#### Envoy rejection

If Envoy rejects the token, you may see a message like:
    
    
    Jwks remote fetch is failed

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

See [Valid API key fails](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.2.x/troubleshooting#valid-api-key-fails). 

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

A Prometheus metrics endpoint is available at `:5001/metrics`. You can configure this port number. See [Configuration file](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.2.x/reference#configuration-file).

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

## 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
