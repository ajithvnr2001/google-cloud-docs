---
url: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.0.x/reference/
title: Reference \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:27:59.769222+00:00
---

# Reference  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.0.x/reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Reference Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The `apigee-remote-service-cli` Command Line Interface (CLI) helps you provision and manage Apigee Adapter for Envoy.

## Binding commands

Binding associates a service deployed to the Istio mesh with an Apigee API product. The CLI lets you create, remove, and list bindings.

Note: In the Create Product UI, you can specify one or more services with a product. Doing so is equivalent to creating the binding using the CLI. 

### Add a binding

Adds a remote target binding to an API product.

#### Usage

For Apigee hybrid:
    
    
    apigee-remote-service-cli bindings add [service_name] [product_name]  -o [organization] -e [environment] -t [token]

#### Parameters

Parameters  | Type  | Description   
---|---|---  
`-c, --config` | String  | (Required) The path to the Apigee Remote Service config file. **Tip** : When you specify this option, you can omit most other command parameters. See [ Using the `--config` option](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.0.x/reference#using-the---config-command-option).   
`-e, --env` | String  | (Required) An environment in your organization.   
`-h, --help` |  | Displays help for the command parameters.   
`--insecure` |  | Allow insecure server connections when using SSL   
`--legacy` |  | Set this flag if you are using Apigee Cloud. It sets the management and runtime URLs for Edge Cloud.   
`--opdk` |  | Set this flag if you are using Apigee for Private Cloud.   
`-o, --org` | String  | (Required) An Apigee organization. You must be an org administrator.   
`-p, --password` | String  | (Required for basic authentication only) Your Apigee password. You can optionally specify the password in a `.netrc` file. If you do so, then you are not required to provide your password on the command line. See also Using .netrc for credentials.   
`-r, --runtime` | String  | Apigee runtime base URL (required for hybrid or opdk).   
`-t, --token` | String  | (Required for OAuth token authentication only) An OAuth or SAML token that you generate from your Apigee account information. For information on generating tokens, see [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20) and [SAML overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/saml-overview).   
`-u, --username` | String  | (Required for basic authentication only) Your Apigee username (typically an email address). You can optionally specify the username in a `.netrc` file. If you do so, then you are not required to provide your username on the command line. See also Using .netrc for credentials.   
`-v, --verbose` |  | (Optional) Produces verbose output.   
  
#### Example
    
    
    ./apigee-remote-service-cli bindings add httpbin.org envoy-test -o myorg -e test -u user@example.com -c config.yaml -p xxxxxx
    product envoy-test is now bound to: httpbin.org

### List bindings

List all API products that are bound to the Remote Service. 

#### Usage

#### Parameters

Parameters  | Type  | Description   
---|---|---  
`-c, --config` | String  | (Required) The path to the Apigee Remote Service config file. **Tip** : When you specify this option, you can omit most other command parameters. See [ Using the `--config` option](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.0.x/reference#using-the---config-command-option).   
`-e, --env` | String  | (Required) An environment in your organization.   
`-h, --help` |  | Displays help for the command parameters.   
`--insecure` |  | Allow insecure server connections when using SSL   
`--legacy` |  | Set this flag if you are using Apigee Cloud. It sets the management and runtime URLs for Edge Cloud.   
`--opdk` |  | Set this flag if you are using Apigee for Private Cloud.   
`-o, --org` | String  | (Required) An Apigee organization. You must be an org administrator.   
`-p, --password` | String  | (Required for basic authentication only) Your Apigee password. You can optionally specify the password in a `.netrc` file. If you do so, then you are not required to provide your password on the command line. See also Using .netrc for credentials.   
`-r, --runtime` | String  | Apigee runtime base URL (required for hybrid or opdk).   
`-t, --token` | String  | (Required for OAuth token authentication only) An OAuth or SAML token that you generate from your Apigee account information. For information on generating tokens, see [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20) and [SAML overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/saml-overview).   
`-u, --username` | String  | (Required for basic authentication only) Your Apigee username (typically an email address). You can optionally specify the username in a `.netrc` file. If you do so, then you are not required to provide your username on the command line. See also Using .netrc for credentials.   
`-v, --verbose` |  | (Optional) Produces verbose output.   
  
#### Example
    
    
    apigee-remote-service-cli bindings list -o myorg -e test -u user@example.com -c config.yaml -p abc123
    PI Products
    ============
    Bound
    -----
    envoy-test:
      Quota: 5 requests every 1 minute
      Target bindings:
        httpbin.org
      Paths:
    httpbin:
      Quota: 5 requests every 1 minute
      Target bindings:
        httpbin.org
      Paths:
        /httpbin
        /
    
    Unbound
    -------
    product-1:
      Quota: 100 requests every 1 hour
    product-2:
      Quota: 1000 requests every 1 month
    product-3:
    product-4:
    

### Remove a binding

Remove the binding of Remote Service for Envoy from an API product.

Note: You can also remove a Remote Service for Envoy binding by removing the service name from the product in the UI. 

#### Usage

For Apigee hybrid:
    
    
    apigee-remote-service-cli bindings remove [service_name] [product_name]  -o [organization] -e [environment] -t [token]

#### Parameters

Parameters  | Type  | Description   
---|---|---  
`-c, --config` | String  | (Required) The path to the Apigee Remote Service config file. **Tip** : When you specify this option, you can omit most other command parameters. See [ Using the `--config` option](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.0.x/reference#using-the---config-command-option).   
`-e, --env` | String  | (Required) An environment in your organization.   
`-h, --help` |  | Displays help for the command parameters.   
`--insecure` |  | Allow insecure server connections when using SSL   
`--legacy` |  | Set this flag if you are using Apigee Cloud. It sets the management and runtime URLs for Edge Cloud.   
`--opdk` |  | Set this flag if you are using Apigee for Private Cloud.   
`-o, --org` | String  | (Required) An Apigee organization. You must be an org administrator.   
`-p, --password` | String  | (Required for basic authentication only) Your Apigee password. You can optionally specify the password in a `.netrc` file. If you do so, then you are not required to provide your password on the command line. See also Using .netrc for credentials.   
`-r, --runtime` | String  | Apigee runtime base URL (required for hybrid or opdk).   
`-t, --token` | String  | (Required for OAuth token authentication only) An OAuth or SAML token that you generate from your Apigee account information. For information on generating tokens, see [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20) and [SAML overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/saml-overview).   
`-u, --username` | String  | (Required for basic authentication only) Your Apigee username (typically an email address). You can optionally specify the username in a `.netrc` file. If you do so, then you are not required to provide your username on the command line. See also Using .netrc for credentials.   
`-v, --verbose` |  | (Optional) Produces verbose output.   
  
#### Example
    
    
    ./apigee-remote-service-cli bindings remove httpbin.org envoy-test -o myorg -e test -u user@example.com -c config.yaml -p xxxxxx
    product envoy-test is no longer bound to: httpbin.org

## Help command

Online help is provided for all `apigee-remote-service-cli` commands. Just type:
    
    
    apigee-remote-service-cli help

For help on any command, type:
    
    
    apigee-remote-service-cli [command] help
    

For example:
    
    
    apigee-remote-service-cli provision help
    

## Provision command

The `apigee-remote-service-cli provision` command installs a proxy in your Apigee organization, sets up a certificate, and generates credentials that you'll need to configure the Apigee Adapter for Envoy.

#### Usage

#### Parameters

Parameters  | Type  | Description   
---|---|---  
`-c, --config` | String  | Path to Apigee Remote Service config file. **Tip** : When you specify this option, you can omit most other command parameters. See [ Using the `--config` option](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.0.x/reference#using-the---config-command-option).   
`-e, --environment` | String  | (Required) An environment in your organization.   
`-f, --force-proxy-install` |  | (Optional) Forces the `remote-service` proxy to be re-installed if it is already installed in your org. **UPGRADE NOTE:** If you are upgrading to v1.0-beta.4 or a later version, you must include the `--force-proxy-install` flag to replace the existing remote service proxy deployed on Apigee.  
`-h, --help` |  | Displays help for the command parameters.   
`-k, --key` | String  | Specifies the key returned from the `apigee-remote-service-cli provision` command.   
`--legacy` |  | Apigee Edge (sets management and runtime URL)   
`-m, --management` | String  | (Required if you are on Apigee Private Cloud) Your Apigee management base URL. Default: `https://api.enterprise.apigee.com`  
`-n, --namespace` | String  | emit configuration as an Envoy ConfigMap in the specified namespace.   
`--opdk` | String  | Apigee OPDK.   
`-o, --organization` | String  | (Required) Your Apigee organization. You must be an org administrator.   
`-p, --password` | String  | (Required for basic authentication only) Your Apigee password. You can optionally specify the password in a `.netrc` file. If you do so, then you are not required to provide your password on the command line. See also Using .netrc for credentials.   
`--rotate-int` | int  | If _n_ > 0, generate new private key and keep _n_ public keys (hybrid only)   
`-r, --runtime` | String  | Apigee runtime base URL (required for hybrid or opdk)   
`-s, --secret` | String  | Specifies the secret returned from the `apigee-remote-service-cli provision` command.   
`--strength` | int  | (Optional) Specifies the encryption strength for SSL certificates used in provisioning the adapter. Default 2048   
`-t, --token` | String  | (Hybrid only) Apigee OAuth or SAML token.   
`-u, --username` | String  | (Required for basic authentication only) Your Apigee username (typically an email address). You can optionally specify the username in a `.netrc` file. See also Using .netrc for credentials.   
`-v, --verbose` |  | (Optional) Produces verbose output.   
`--virtual-hosts` | String  | Overrides the default virtual hosts.   
`--years` | int  | (Optional) The number of years before the SSL certificate used in the provisioning expires. Default: 1   
  
####  Example 

Be sure to capture the output of the `provision` command in a file, which is used as input for other Apigee Adapter for Envoy operations. 

Apigee hybrid example: 
    
    
    apigee-remote-service-cli provision --organization $ORG --environment $ENV --runtime $RUNTIME --namespace $NAMESPACE --token $TOKEN > config.yaml

## Token commands

You can use a JWT token to make authenticated API proxy calls instead of using an API key. The token commands let you create, inspect, and rotate JWT tokens for this purpose.

### Create a JWT token

You can use a JWT token to make authenticated API proxy calls to a remote service target. See also [Using JWT based authentication](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.0.x/operation#using-jwt-based-authentication). 

#### Usage

For Apigee hybrid: 
    
    
    apigee-remote-service-cli token create -c [config_file] --id [consumer_key] --secret [consumer_secret] -r [runtime] -o [org] -e [env]
    

#### Parameters

Parameters  | Type  | Description   
---|---|---  
`-c, --config` | String  | (Required) The path to the Apigee Remote Service config file. **Tip** : When you specify this option, you can omit most other command parameters. See [ Using the `--config` option](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.0.x/reference#using-the---config-command-option).   
`-e, --env` | String  | (Required) An environment in your organization.   
`-h, --help` |  | Displays help for the command parameters.   
`--insecure` |  | Allow insecure server connections when using SSL.   
`-o, --org` | String  | (Required) An Apigee organization. You must be an org administrator.   
`-r, --runtime` | String  | Apigee runtime base URL (required only for hybrid or opdk).   
`-v, --verbose` |  | (Optional) Produces verbose output.   
  
#### Example
    
    
    apigee-remote-service-cli token create -o myorg -e test -i YUmlZAcBKNsTAelJqPZFl3sh58ObATX9 -s icTARgaKHqvUH1dq -c config.yaml
    

#### Output

On success, you'll see a JST token output similar to the following: 
    
    
    eyJraWQiOiIxIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJhY2Nlc3NfdG9rZW4iOiJ0a2tlVzVKQTY2a0pZYTB4bFV1cVBsUW1BMU43IiwiYXVkIjoiaXN0aW8iLCJuYmYiOjE1MzAxMzg1OTEsImFwaV9wcm9kdWN0X2xpc3QiOlsiaXN0aW8tcHJvZHVjdCJdLCJhcHBsaWNhdGlvbl9uYW1lIjoiaXN0aW8tYXBwIiwiZGV2ZWxvcGVyX2VtYWlsIjoicFluZ2Zsb3lkQGdvb2dsZS5jb20iLCJpc3MiOiJodHRwczovL2FwaWdlZXNlYXJjaC10ZXN0LmFwaWdlZS5uZXQvaXN0aW8tYXV0aC90b2tlbiIsImV4cCI6MTUzMDEzOTQ5MSwiaWF0IjoxNTMwMTM4NTkxLCJqdGkiOiIxODgzMzViZi0wMmE4LTRjZGUsOGFkOS0yMWJmNDZjNmRjZDkiLCJjbGllbnRfaWQiOiJZVW1sWkFjQktOc1RBZWxKcVBZRmwzc2g1OE9iQVRYOSJ9.AL7pKSTmond-NSPRNNHVbIzTdAnZjOXcjQ-BbOJ_8lsQvF7PuiOUrGIhY5XTcJusisKgbCdtIxBl8Wq1EiQ_fKnUc3JYYOqzpTB5bGoFy0Yqbfu96dneuWyzgZnoQBkqwZkbQTIg7WNTGx1TJX-UTePvBPxAefiAbaEUcigX9tTsXPoRJZOTrm7IOeKpxpB_gQYkxQtV1_NbERxjTPyMbHdMWal9_xRVzSt7mpTGudMN9OR-VtQ1uXA67GOqhZWcOzq57qImOiCMbaoKnKUADevyWjX_VscN5ZZUtzQUQhTrmv8aR69-uVhMIPKp9juMyYKaYn2IsYZEeCWfhfV45Q
    

### Inspect a JWT token

You can inspect a JWT token with this command. See also [Inspect a token](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.0.x/operation#inspect-a-token). 

#### Usage

For Apigee hybrid: 
    
    
    apigee-remote-service-cli token inspect -o [organization] -e [environment] -f [token_file] --runtime [host_alias]
    

#### Parameters

Parameters  | Type  | Description   
---|---|---  
`-c, --config` | String  | (Required) The path to the Apigee Remote Service config file. **Tip** : When you specify this option, you can omit most other command parameters. See [ Using the `--config` option](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.0.x/reference#using-the---config-command-option).   
`-e, --env` | String  | (Required) An environment in your organization.   
`-h, --help` |  | Displays help for the command parameters.   
`--insecure` |  | Allow insecure server connections when using SSL.   
`-o, --org` | String  | (Required) An Apigee organization. You must be an org administrator.   
`-r, --runtime` | String  | Apigee runtime base URL (required only for hybrid or opdk).   
`-v, --verbose` |  | (Optional) Produces verbose output.   
  
#### Example
    
    
    apigee-remote-service-cli token inspect -c config.yaml <<< $TOKEN

#### Output

On success, you'll see output similar to the following: 
    
    
    {
    	"aud": [
    		"remote-service-client"
    	],
    	"exp": 1591741549,
    	"iat": 1591740649,
    	"iss": "https://apigee-docs-test.apigee.net/remote-service/token",
    	"jti": "99325d2e-6440-4278-9f7f-b252a1a79e53",
    	"nbf": 1591740649,
    	"access_token": "VfzpXzBGAQ07po0bPMKY4JgQjus",
    	"api_product_list": [
    		"httpbin"
    	],
    	"application_name": "httpbin",
    	"client_id": "GYDGHy5TRpV8AejXCOlreP7dPVepA8H",
    	"developer_email": "user@example.com",
    	"scope": ""
    }
    verifying...
    token ok.
    

### Rotate a JWT token

At some time after you initially generate a JWT, you might need to change the public/private key pair stored by Apigee in its encrypted key-value map (KVM). This process of generating a new key pair is called key rotation. When you rotate keys, a new private/public key pair is generated and stored in the "istio" KVM in your Apigee organization/environment. In addition, the old public key is retained along with its original key ID value. 

#### Usage

#### Parameters

Parameters  | Type  | Description   
---|---|---  
`-c, --config` | String  | (Required) The path to the Apigee Remote Service config file. **Tip** : When you specify this option, you can omit most other command parameters. See [ Using the `--config` option](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.0.x/reference#using-the---config-command-option).   
`-e, --env` | String  | (Required) An environment in your organization.   
`-h, --help` |  | Displays help for the command parameters.   
`--insecure` |  | Allow insecure server connections when using SSL   
`--truncate` | int  | Number of certs to keep in jwks (default 2)   
`-o, --org` | String  | (Required) An Apigee organization. You must be an org administrator.   
`-r, --runtime` | String  | Apigee runtime base URL (required for hybrid or opdk).   
`-v, --verbose` |  | (Optional) Produces verbose output.   
  
#### Example
    
    
    apigee-remote-service-cli token rotate-cert -c config.yaml -o myorg -e test -k 2e238ffa15dc5ab6a1e97868e7581f6c60ddb8575478582c256d8b7e5b2677a8 -s 51058077223fa7b683c3bea845c5cca138340d1d5583922b6d465f9f918a4b08
    

#### Output
    
    
    certificate successfully rotated
    

## Using .netrc for credentials

`apigee-remote-service-cli` automatically picks up the `username` and `password` (for basic authentication where needed) from a `.netrc` file in your home directory if you are on Apigee and have an entry for the machine `api.enterprise.apigee.com`. If you are on Apigee Private Cloud, the machine value is the same as your `management` URL (for example: `http://192.162.55.100`). 

## Version command

Print the CLI version.
    
    
    apigee-remote-service-cli version
    

##  Using the `--config` command option 

The `--config` option specifies the location of the config file generated by the `provision` command. A helplful benefit of this option is that it allows you to skip most other command parameters, which the CLI pulls from the config file. These options include: 

  * organization
  * environment
  * runtime
  * management
  * insecure
  * namespace
  * legacy
  * opdk



For example, you could execute the `provision` command like this: 
    
    
    apigee-remote-service-cli provision --config='old-config.yaml' > new-config.yaml

##  Configuration file 

This section shows an example configuration file with all of the available options. 
    
    
    global:
      temp_dir: /tmp/apigee-istio
      keep_alive_max_connection_age: 10m
      api_address: :5000
      metrics_address: :5001
      tls:
        cert_file: tls.crt
        key_file: tls.key
    tenant:
      internal_api: https://istioservices.apigee.net/edgemicro
      remote_service_api: https://org-test.apigee.net/remote-service
      org_name: org
      env_name: env
      key: mykey
      secret: mysecret
      client_timeout: 30s
      allow_unverified_ssl_cert: false
    products:
      refresh_rate: 2m
    analytics:
      legacy_endpoint: false
      file_limit: 1024
      send_channel_size: 10
      collection_interval: 10s
      fluentd_endpoint: apigee-udca-myorg-test.apigee.svc.cluster.local:20001
      tls:
        ca_file: /opt/apigee/tls/ca.crt
        cert_file: /opt/apigee/tls/tls.crt
        key_file: /opt/apigee/tls/tls.key
        allow_unverified_ssl_cert: false
    auth:
      api_key_claim: claim
      api_key_cache_duration: 30m
      api_key_header: x-api-key
      api_target_header: :authority
      reject_unauthorized: true
      jwks_poll_interval: 0s

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
