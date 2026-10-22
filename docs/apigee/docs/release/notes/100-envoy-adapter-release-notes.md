---
url: https://docs.cloud.google.com/apigee/docs/release/notes/100-envoy-adapter-release-notes/
title: Apigee Adapter for Envoy release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:33.966844+00:00
---

# Apigee Adapter for Envoy release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/release/notes/100-envoy-adapter-release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Apigee Adapter for Envoy release notes Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

For more information, see the following resources: 

  * _[Apigee Adapter for Envoy documentation](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/latest/concepts)_
  * _Questions or issues?_ Contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/)
  * _Release notifications_ : Go to the [Apigee Adapter for Envoy release notes](https://docs.cloud.google.com/apigee/docs/apigee-envoy-adapter-release-notes) and click **Subscribe** to follow the page with a feed reader



This page documents release notes for all Apigee Adapter for Envoy software for 2021 and prior.

See [Adapter for Envoy](https://docs.cloud.google.com/apigee/docs/apigee-envoy-adapter-release-notes) for current release notes (2022 and later). 

## v2.0.4

On December 3, 2021, we released version 2.0.4 of Apigee Adapter for Envoy.

**Note:** If you are **upgrading** an existing Apigee Adapter for Envoy, you **must** add the `--force-proxy-install` flag to the `provision` command. This flag forces the Apigee proxy to be replaced with the latest proxy. See [Apigee hybrid example](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/latest/example-hybrid).

#### _Click to see the list of supported platforms._

We publish binaries for MacOS, Linux, and Windows, and in this version, we support the following platforms: 

  * Apigee hybrid version 1.4.x, 1.5.x, 1.6.x
  * Apigee
  * Apigee Edge for Public Cloud
  * Apigee Edge for Private Cloud
  * Istio versions 1.10, 1.11, 1.12
  * Envoy versions 1.17, 1.18, 1.19, 1.20



###  Features and improvements 

  * The list of supported Envoy and Istio versions for the CLI [`samples` command](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/reference#samples-command) has been updated. These versions are now supported for samples: 
    * Envoy versions 1.18 to 1.20
    * Istio versions 1.10 to 1.12



###  Issues fixed 

  * A nil-check was added for the PEM block private key loading to avoid panic. ([Issue #360](https://github.com/apigee/apigee-remote-service-envoy/pull/360))
  * Remote service authorization errors are now logged at the Debug level. An exception to this categorization is made for token fetching errors for API keys. In that case, errors are logged at the Error level so that they are visible even if Debug log level for `apigee-remote-service-envoy` is disabled. See also [Setting remote service log levels](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/troubleshooting#settingremoteserviceloglevels). ([Issue #104](https://github.com/apigee/apigee-remote-service-golib/pull/104))



## v2.0.3

On September 21, 2021, we released version 2.0.3 of Apigee Adapter for Envoy.

**Note:** If you are **upgrading** an existing Apigee Adapter for Envoy, you **must** add the `--force-proxy-install` flag to the `provision` command. This flag forces the Apigee proxy to be replaced with the latest proxy. See [Apigee hybrid example](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/latest/example-hybrid).

#### _Click to see the list of supported platforms._

We publish binaries for MacOS, Linux, and Windows, and in this version, we support the following platforms: 

  * Apigee hybrid version 1.4.x, 1.5.x, 1.6.x
  * Apigee
  * Apigee Edge for Public Cloud
  * Apigee Edge for Private Cloud
  * Istio versions 1.10, 1.11, 1.12
  * Envoy versions 1.17, 1.18, 1.19



###  Issues fixed 

  * An analytics logging issue with direct responses was fixed. The issue only occurred under certain circumstances. For example: 
    * For requests not requiring authn/z check, no `authContext` was generated and dynamic metadata was nil causing the access log entry to be ignored.
    * The denied response used RPC code instead of HTTP code, causing records to be shown in the Apigee UI as success.



## v2.0.2

On June 7, 2021, we released version 2.0.2 of Apigee Adapter for Envoy.

**Note:** If you are **upgrading** an existing Apigee Adapter for Envoy, you **must** add the `--force-proxy-install` flag to the `provision` command. This flag forces the Apigee proxy to be replaced with the latest proxy. See [Apigee hybrid example](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/latest/example-hybrid).

#### _Click to see the list of supported platforms._

We publish binaries for MacOS, Linux, and Windows, and in this version, we support the following platforms: 

  * Apigee hybrid version 1.3.x, 1.4.x
  * Apigee
  * Apigee Edge for Public Cloud
  * Apigee Edge for Private Cloud
  * Istio versions 1.7, 1.8, 1.9
  * Envoy versions 1.15, 1.16, 1.17



###  Issues fixed 

  * A race condition was fixed that could cause 403 errors and panics when JWT claims scopes were nil. 



## v2.0.1

On Tuesday, April 29, 2021, we released version 2.0.1 of Apigee Adapter for Envoy.

**Note:** If you are **upgrading** an existing Apigee Adapter for Envoy, you **must** add the `--force-proxy-install` flag to the `provision` command. This flag forces the Apigee proxy to be replaced with the latest proxy. See [Apigee hybrid example](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/latest/example-hybrid).

#### _Click to see the list of supported platforms._

We publish binaries for MacOS, Linux, and Windows, and in this version, we support the following platforms: 

  * Apigee hybrid version 1.3.x, 1.4.x
  * Apigee
  * Apigee Edge for Public Cloud
  * Apigee Edge for Private Cloud
  * Istio versions 1.7, 1.8, 1.9
  * Envoy versions 1.15, 1.16, 1.17



###  Issues fixed 

Feature | Description  
---|---  
**Bug** |  An issue was fixed that caused v2.0.0 to malfunction when used with Apigee hybrid v1.5.0 or Apigee. If you are upgrading your Apigee hybrid installation to v1.5.x, the recommended upgrade path for the adapter is: 

  1. Upgrade Apigee Adapter for Envoy to v2.0.1.
  2. Upgrade Apigee hybrid to v1.5.1.

If you are using Apigee, then just upgrade the adapter to v2.0.1.  **Notes:** This fix only works with Apigee hybrid v1.5.1 and later versions; it will not work with Apigee hybrid v1.5.0. This issue also exists for Apigee Adapter for Envoy versions v1.x.x. We have no plans to apply this fix to any v1.x.x versions.**Note:** At this time, Apigee hybrid v1.5.1 has not yet been publicly released. For updates, see [Apigee release notes](https://docs.cloud.google.com/apigee/docs/release/notes/apigee-release-notes).   
  
## v2.0.0

On Tuesday, April 6, 2021, we released version 2.0.0 of Apigee Adapter for Envoy.

**Note:** If you are **upgrading** an existing Apigee Adapter for Envoy, you **must** add the `--force-proxy-install` flag to the `provision` command. This flag forces the Apigee proxy to be replaced with the latest proxy. See [Apigee hybrid example](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/latest/example-hybrid).

#### _Click to see the list of supported platforms._

We publish binaries for MacOS, Linux, and Windows, and in this version, we support the following platforms: 

  * Apigee hybrid version 1.3.x, 1.4.x
  * Apigee
  * Apigee Edge for Public Cloud
  * Apigee Edge for Private Cloud
  * Istio versions 1.7, 1.8, 1.9
  * Envoy versions 1.15, 1.16, 1.17



### Features and improvements

Feature | Description  
---|---  
**Multi-tenant environment support** | **Breaking change:** Because the quota identifier must now include the environment name, existing quota counts for versions before v2.0.0 will not be carried forward.You can now enable the adapter to service multiple environments in an Apigee organization. This feature allows you to use one Apigee Adapter for Envoy associated with one Apigee organization to service multiple environments. Before this change, one adapter was always tied to one Apigee environment. For more information about this feature, see [Multi-tenant environment support](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/operation#multi-tenant-environment-support).  
**Envoy v3 API support** | **Breaking change:** Envoy v2 APIs are deprecated in Envoy (v1.15+) and Istio (v1.7+) and have been removed from [later versions](https://www.envoyproxy.io/docs/envoy/latest/api/api_supported_versions). The Apigee Adapter only supports v3 APIs. Any Envoy configuration files that use v2 APIs must be updated to v3.  
**Envoy metadata support** | **Breaking change:** To support this feature, the property `auth:allow_unauthorized` replaces the property `auth:reject_unauthorized` in the adapter's `config.yaml` file. Envoy 1.16+ allows sending `ext_authz` metadata without having to use headers. By using this and related changes, we now provide better HTTP response codes for denied requests, and we no longer need to install an RBAC filter in Envoy. See  This feature is only supported for Envoy 1.16+ and Istio 1.9+.  With this change, the following configuration is no longer added to the Envoy configuration file (`envoy-config.yaml`): 
    
    
    additional_request_headers_to_log:
        - x-apigee-accesstoken
        - x-apigee-api
        - x-apigee-apiproducts
        - x-apigee-application
        - x-apigee-clientid
        - x-apigee-developeremail
        - x-apigee-environment
    

If you want to append headers to requests for a special case, just set the property `append_metadata_headers:true` in the adapter's `config.yaml` file.  
**Split the`remote-token` proxy from the `remote-service` proxy** |  The **remote-service** proxy has been refactored into two separate proxies. The v2.0.x, provisioning will install two API proxies: **remote-service** and **remote-token**. The `/token` and `/certs` endpoints were moved from the **remote-service** proxy to **remote-token**.  This change creates a useful separation of functions. Now, the **remote-service** proxy is only used for internal Adapter communications, while the **remote-token** proxy provides a sample OAuth workflow that you can customize. We will never overwrite your custom **remote-token** proxy, even if the `provision --force-proxy-install` command is used.  **Note:** As installed by default, the two proxies share OAuth certificates, but they are not required to do so.   
**Data capture support** |  The Adapter now supports passing Envoy metadata to Apigee's data capture feature, which sends data captured in variables that you specify to Apigee analytics for use in custom reports. This feature provides a capability that is similar to the Apigee [Data Capture policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy). For more information about this feature, see [ Capturing data for custom reports](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/operation#capturing-data-for-custom-reports).   
**RBAC not required** |  As noted previously under **Envoy metadata support** , we now immediately reject unauthorized requests without requiring a separate RBAC filter. Because RBAC is not used, clients will now receive these HTTP status codes as appropriate from the Adapter: 

  * 401 Unauthorized
  * 403 Forbidden
  * 429 Too Many Requests
  * 500 Internal Server Error

If you want to allow unauthorized requests to continue, you can do so by setting `auth:allow_unauthorized:true` in the adapter's `config.yaml` file.   
**`x-apigee-*` headers are no longer appended by default** |  As noted previously in the **Envoy metadata support** section, `x-apigee-*` headers are no longer appended by default. If you want to add them, set `append_metadata_headers:true` in the `config.yaml` file. This configuration is completely optional and should only need to be used when it's desirable to forward headers to the upstream target service.   
**Custom matching a request to an Apigee API Product Operation** | **Breaking change:** The adapter config element `target_header` has been renamed to `api_header`. The semantics of the `api_header` config property remain the same as the former `target_header` property (the default is still the target host name), and the specified header's contents still will match either the API Product [Remote service target](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#ops) attribute or **Source** field in an [API Product Operations configuration](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#ops).  To override this header value using Envoy metadata, you can pass the `apigee_api` metadata element from Envoy to the adapter to directly specify the API Product's **Remote Service Target** or API Product Operation's API Source. To configure, add code similar to the following to the Envoy configuration file (which you can generate using the Adapter's CLI): 
    
    
    typed_per_filter_config:
      envoy.filters.http.ext_authz:
        "@type": type.googleapis.com/envoy.extensions.filters.http.ext_authz.v3.ExtAuthzPerRoute
        check_settings:
          context_extensions:
            apigee_api: httpbin.org  
  
**Analytics for rejected requests are logged immediately** | Envoy Adapter will now log rejected requests immediately to analytics as required instead of waiting for the request to return in the access log. This is more efficient and doesn't require any metadata be attached to the request.  
**UDCA support has been removed** |  Streaming to Apigee's Universal Data Collection Agent (UDCA) in Apigee hybrid and Apigee is no longer needed for analytics as it has been replaced by direct upload. This change simply removes the legacy support for this option.   
**mTLS support added for Edge for Private Cloud in the provision/bindings CLI commands** |  Apigee Edge for Private Cloud users can supply client-side TLS certificates and root cert via `‑‑tls‑cert`, `‑‑tls‑key` and `‑‑tls‑ca` respectively when provisioning or listing products bindings using the CLI.   
**mTLS support between the adapter and Apigee runtime** | **Breaking change:** The config attribute `allow_unverified_ssl_cert` was moved from `tenant` to `tenant:tls`. The `analytics:tls` configuration section is obsolete and has been removed. You can supply client-side TLS certificates in the `tenant` section of the adapter's `config.yaml` file to use mTLS between the adapter and the Apigee runtime. This change applies to all supported Apigee platforms. It also enables mTLS for analytics for the Apigee Edge for Private Cloud platform. For more information, see [Configuring mTLS between the adapter and Apigee runtime](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/operation#configuring-mtls-between-the-adapter-and-apigee-runtime).   
  
###  Other issues and fixes 

  * An issue was fixed where multiple operation configs with the same API source shared the same quota bucket identifiers and caused conflicts in quota calculation. (Issue [#34](https://github.com/apigee/apigee-remote-service-golib/issues/34))
  * An issue was fixed where operations with no specified verbs caused the request to be denied (the expected behavior is to allow all verbs if none are specified). (Issue [#39](https://github.com/apigee/apigee-remote-service-golib/issues/39))



## v1.4.0

On Wednesday, December 16, 2020, we released the version 1.4.0 of Apigee Adapter for Envoy.

**Note:** If you are **upgrading** an existing Apigee Adapter for Envoy, you **must** add the `--force-proxy-install` flag to the `provision` command. This flag forces the Apigee proxy to be replaced with the latest proxy. See [Apigee hybrid example](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/latest/example-hybrid).

##  Supported platforms 

We publish binaries for MacOS, Linux, and Windows. 

We publish docker images from Google's distroless, Ubuntu, and Ubuntu with Boring Crypto. 

In this version we support the following platforms: 

  * Apigee hybrid version 1.3.x, 1.4.x (release date pending), Apigee for Public Cloud, Apigee for Private Cloud, and Apigee on Google Cloud
  * Istio versions 1.5, 1.6, 1.7, 1.8
  * Envoy versions 1.14, 1.15, 1.16



### Features and improvements

Feature | Description  
---|---  
**The`remote-service` proxy no longer requires association with an API product that uses Remote Service Targets.** | Because this association is no longer required, note the following changes:

  * A **remote-service** API product is no longer created during provisioning.
  * The `bindings verify` CLI command is no longer relevant and has been deprecated.

  
**The Apigee Organization Admin role is no longer required for provisioning.** |  Rather than require the org admin permission for provisioning, you can now use the IAM roles API Creator and Deployer instead. You must grant both of these roles to successfully provision.   
(Applies to Apigee on Google Cloud and Apigee hybrid only)   
  
###  Other issues and fixes 

  * An issue was fixed where re-provisioning Apigee without the `--rotate` option exited with an error. 
  * The provisioning CLI now reads and reuses the analytics service account credentials from a given `config.yaml` file ([Issue #133](https://github.com/apigee/apigee-remote-service-cli/issues/133)).



## v1.3.0

On Monday, November 23, 2020, we released the version 1.3.0 of Apigee Adapter for Envoy.

**Note:** If you are **upgrading** an existing Apigee Adapter for Envoy, you **must** add the `--force-proxy-install` flag to the `provision` command. This flag forces the Apigee proxy to be replaced with the latest proxy. See [Apigee hybrid example](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/latest/example-hybrid).

##  Supported platforms 

We publish binaries for MacOS, Linux, and Windows. 

We publish docker images from Google's distroless, Ubuntu, and Ubuntu with Boring Crypto. 

In this version we support the following platforms: 

  * Apigee hybrid version 1.3.x, 1.4.x (release date pending), Apigee for Public Cloud, Apigee for Private Cloud, and Apigee on Google Cloud
  * Istio versions 1.5, 1.6, 1.7, 1.8
  * Envoy versions 1.14, 1.15, 1.16



### Features and improvements

Feature | Description  
---|---  
**Support for API product OperationGroups.** | OperationGroups bind the resources and associated quota enforcement in a proxy or remote service with HTTP methods. For details, see [OperationGroup](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts#operationgroup).   
(Applies to Apigee on Google Cloud and Apigee hybrid only)  
**Remove support for dynamic forward proxy from samples generation.** | Because of this change, clients must include the `HOST` header if the hostname is different than the remote service target host that is set in the API product. For example: 
    
    
    curl -i http://localhost:8080/httpbin/headers -H "HOST:httpbin.org"

See [Create an API product.](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.3.x/operation#3.-create-an-api-product)  
**Support service accounts and Workload Identity.** | To allow analytics data to be uploaded to Apigee when running the adapter outside an Apigee hybrid cluster, you must use the `analytics-sa` parameter with the `apigee-remote-service-cli provision` command. In addition, the adapter now supports Workload Identity on Google Kubernetes Engine (GKE). See [Provision command](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.3.x/reference#provision-command).   
(Applies to Apigee on Google Cloud and Apigee hybrid only)  
**New`jwt_provider_key` configuration attribute.** | This key is added to the [config file](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.3.x/reference#configuration-file). It represents the JWT provider's `payload_in_metadata` key in [Envoy config](https://github.com/envoyproxy/envoy/blob/fc9f014e70f1ece97dbe3dcafd55935a59f2ffae/api/envoy/config/filter/http/jwt_authn/v2alpha/config.proto#L443) or the RequestAuthentication JWT issuer in [Istio config](https://istio.io/latest/docs/reference/config/security/request_authentication/).  
**`KeepAliveMaxConnectionAge` configuration attribute now defaults to 1 minute.** | The previous default was 10 minutes. This change allows smoother scaling. This value is also used for the access log stream lifetime. See [config file](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.3.x/reference#configuration-file).  
**Removed CLI commands.** | The following CLI commands have been deprecated. We recommend that you use the [Apigee APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts) instead to update remote service targets for API products: 

  * `apigee-remote-service-cli bindings add`
  * `apigee-remote-service-cli bindings remove`

  
**Added new CLI command.** | The command: 
    
    
    apigee-remote-service-cli samples templates

lists the available options that you can use with the `--template` flag in the `samples create` command. See [CLI reference](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.3.x/reference#list-available-template-options).  
**Changed existing CLI command.** | A change was made to the `apigee-remote-service-cli samples create` command. Flags specific to Envoy or Istio templates are strictly checked, and errors are returned on wrongly used flags. The `native `template option is deprecated. To get a list of available templates, use the `apigee-remote-service-cli samples templates` command. See also [CLI reference](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.3.x/reference#list-available-template-options).   
**The`/token` endpoint response now follows the [OAuth2 spec](https://tools.ietf.org/html/rfc6749#section-5.1).** | The `access_token` parameter was added to the response, and the `token` parameter is deprecated.  
  
## v1.2.0

On Wednesday, September 30, 2020, we released the version 1.2.0 of Apigee Adapter for Envoy.

**Note:** If you are **upgrading** an existing Apigee Adapter for Envoy, you **must** add the `--force-proxy-install` flag to the `provision` command. This flag forces the Apigee proxy to be replaced with the latest proxy. See [Apigee hybrid example](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/latest/example-hybrid).

##  Supported platforms 

We publish binaries for MacOS, Linux, and Windows. 

We publish docker images from Google's distroless, Ubuntu, and Ubuntu with Boring Crypto. 

In this version we support the following platforms: 

  * Apigee hybrid version 1.3.x
  * Istio versions 1.5, 1.6, 1.7
  * Envoy versions 1.14, 1.15



### Features and improvements

Feature | Description  
---|---  
**Support for Apigee on Google Cloud** | You can now use Apigee Adapter for Envoy with [Apigee on Google Cloud](https://cloud.google.com/apigee/docs/). You can run the adapter in its own cluster or by running the [Remote Service for Envoy](https://github.com/apigee/apigee-remote-service-envoy) as a native binary or in a container. Provision the adapter on Apigee using the [provision command](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.1.x/reference#provision-command).  
**Direct upload for analytics data** | You can now configure the Apigee Adapter to upload analytics data to Apigee directly. If you are using Apigee hybrid, this new feature makes it possible to deploy the adapter to its own Kubernetes cluster, outside of the cluster where Apigee hybrid is installed. To enable direct upload, use the new `--analytics-sa` flag with the `provision` command. See [provision command](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.2.x/reference#provision-command). **Note:** We recommend that you update your installation to use direct analytics upload. The non-direct method for uploading analytics that used Fluentd is deprecated.  
**Health check returns "Ready" after API product data is loaded from Apigee** | The Kubernetes health check will not return "Ready" until the API product data is loaded from Apigee. This change helps with scaling and upgrading, because no traffic will be sent to the newly instantiated adapter until it is ready.  
  
###  Other issues and fixes 

  * An issue was fixed to address a potential quota sync deadlock ([Issue #17](https://github.com/apigee/apigee-remote-service-golib/issues/17)). 
  * Prometheus annotations were moved to pod spec ([Issue #69](https://github.com/apigee/apigee-remote-service-cli/issues/69)).
  * An issue was fixed to address improperly emitted verify errors ([Issue #62](https://github.com/apigee/apigee-remote-service-cli/issues/62)).



## v1.1.0

On Wednesday, August 26, 2020, we released the version 1.1.0 of Apigee Adapter for Envoy.

**Note:** If you are **upgrading** an existing Apigee Adapter for Envoy, you **must** add the `--force-proxy-install` flag to the `provision` command. This flag forces the Apigee proxy to be replaced with the latest proxy. See [Apigee hybrid example](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/latest/example-hybrid).

##  Supported platforms 

We publish binaries for MacOS, Linux, and Windows. 

We publish docker images from Google's distroless, Ubuntu, and Ubuntu with Boring Crypto. 

In version 1.1.0 we support the following platforms: 

  * Apigee hybrid version 1.3
  * Istio versions 1.5, 1.6, 1.7
  * Envoy versions 1.14, 1.15



### Features and improvements

Feature | Description  
---|---  
Verify bindings | A new command `apigee-remote-service-cli bindings verify` was added to the CLI. This command verifies that the specified bound API product and its associated developer apps also have a remote service product associated with them. See [Verify a binding](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.1.x/reference#verify-a-binding).  
Generate samples | A new command `apigee-remote-service-cli samples create` was added to the CLI. This command creates sample configuration files for native Envoy or Istio deployments. The config files you generate with this command replace the sample files that were installed with the Adapter for Envoy in previous versions. See [Samples command](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.1.x/reference#samples-command).  
OAuth2 authentication | The adapter now uses OAuth2 authentication when multi-factor auth (MFA) is enabled for Apigee. Use the `--mfa` flag whenever you use the `--legacy` flag.  
Distroless container | The adapter now uses Google's distroless (`gcr.io/distroless/base`) image instead of `scratch` for the default Docker image base.  
  
###  Other issues and fixes 

  * A CLI issue was fixed for bindings commands in OPDK. (#29)
  * Quota could become stuck when connection lost (apigee/apigee-remote-service-envoy. (#31)
  * Docker images are now built with non-root user (999).
  * Kubernetes samples enforce the user must not be root.
  * The `--http1.1` is no longer needed for curl commands against proxy endpoints. The flag has been removed from examples.



## v1.0.0

On Friday, July 31, 2020, we released the GA version of Apigee Adapter for Envoy.

**Note:** If you are **upgrading** an existing Apigee Adapter for Envoy, you **must** add the `--force-proxy-install` flag to the `provision` command. This flag forces the Apigee proxy to be replaced with the latest proxy. See [Apigee hybrid example](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/latest/example-hybrid).

##  Supported platforms 

We publish binaries for MacOS, Linux, and Windows. 

We publish docker images from scratch, Ubuntu, and Ubuntu with Boring Crypto. 

In version 1.0.0 we support the following platforms: 

  * Apigee hybrid version 1.3
  * Istio versions 1.5, 1.6
  * Envoy versions 1.14, 1.15



### Additions and changes

Between the v1.0-beta4 release and GA, the following additions changes were made to the adapter: 

  * **Go Boring builds**

A new build is now available that uses [FIPS compliant Go BoringSSL libraries](https://kupczynski.info/2019/12/15/fips-golang.html). 

  * **Log level flag changes**

The logging level flags for the apigee-remote-service-envoy service have been changed for consistency:

Old flag | New flag  
---|---  
`log_level` | `log-level`  
`json_log` | `json-log`  
  * **New CLI flags**

New flags were added to the CLI `token` commands: 

Flag | Description  
---|---  
`--legacy` | Set this flag if you are using Apigee Cloud.  
`--opdk` | Set this flag if you are using Apigee for Private Cloud.  



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
