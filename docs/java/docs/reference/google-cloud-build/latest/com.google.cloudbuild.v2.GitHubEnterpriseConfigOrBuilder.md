---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GitHubEnterpriseConfigOrBuilder
title: Interface GitHubEnterpriseConfigOrBuilder (3.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:43:33.655425+00:00
---

# Interface GitHubEnterpriseConfigOrBuilder (3.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GitHubEnterpriseConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GitHubEnterpriseConfigOrBuilder (3.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.101.0 (latest)  3.97.0  3.96.0  3.95.0  3.93.0  3.90.0  3.89.0  3.87.0  3.85.0  3.84.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.74.0  3.72.0  3.70.0  3.69.0  3.66.0  3.65.0  3.64.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.6  3.4.1  3.3.12 
    
    
    public interface GitHubEnterpriseConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getApiKey()
    
    
    public abstract String getApiKey()

Required. API Key used for authentication of webhook events.

`string api_key = 12 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The apiKey.  
  
### getApiKeyBytes()
    
    
    public abstract ByteString getApiKeyBytes()

Required. API Key used for authentication of webhook events.

`string api_key = 12 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for apiKey.  
  
### getAppId()
    
    
    public abstract long getAppId()

Id of the GitHub App created from the manifest.

`int64 app_id = 2;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The appId.  
  
### getAppInstallationId()
    
    
    public abstract long getAppInstallationId()

ID of the installation of the GitHub App.

`int64 app_installation_id = 9;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The appInstallationId.  
  
### getAppSlug()
    
    
    public abstract String getAppSlug()

The URL-friendly name of the GitHub App.

`string app_slug = 13;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The appSlug.  
  
### getAppSlugBytes()
    
    
    public abstract ByteString getAppSlugBytes()

The URL-friendly name of the GitHub App.

`string app_slug = 13;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for appSlug.  
  
### getHostUri()
    
    
    public abstract String getHostUri()

Required. The URI of the GitHub Enterprise host this connection is for.

`string host_uri = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The hostUri.  
  
### getHostUriBytes()
    
    
    public abstract ByteString getHostUriBytes()

Required. The URI of the GitHub Enterprise host this connection is for.

`string host_uri = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for hostUri.  
  
### getPrivateKeySecretVersion()
    
    
    public abstract String getPrivateKeySecretVersion()

SecretManager resource containing the private key of the GitHub App, formatted as `projects/*/secrets/*/versions/*`.

`string private_key_secret_version = 4 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The privateKeySecretVersion.  
  
### getPrivateKeySecretVersionBytes()
    
    
    public abstract ByteString getPrivateKeySecretVersionBytes()

SecretManager resource containing the private key of the GitHub App, formatted as `projects/*/secrets/*/versions/*`.

`string private_key_secret_version = 4 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for privateKeySecretVersion.  
  
### getServerVersion()
    
    
    public abstract String getServerVersion()

Output only. GitHub Enterprise version installed at the host_uri.

`string server_version = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serverVersion.  
  
### getServerVersionBytes()
    
    
    public abstract ByteString getServerVersionBytes()

Output only. GitHub Enterprise version installed at the host_uri.

`string server_version = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serverVersion.  
  
### getServiceDirectoryConfig()
    
    
    public abstract ServiceDirectoryConfig getServiceDirectoryConfig()

Configuration for using Service Directory to privately connect to a GitHub Enterprise server. This should only be set if the GitHub Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitHub Enterprise server will be made over the public internet.

`.google.devtools.cloudbuild.v2.ServiceDirectoryConfig service_directory_config = 10; `

**Returns**  
---  
**Type** | **Description**  
`[ServiceDirectoryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ServiceDirectoryConfig)` | The serviceDirectoryConfig.  
  
### getServiceDirectoryConfigOrBuilder()
    
    
    public abstract ServiceDirectoryConfigOrBuilder getServiceDirectoryConfigOrBuilder()

Configuration for using Service Directory to privately connect to a GitHub Enterprise server. This should only be set if the GitHub Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitHub Enterprise server will be made over the public internet.

`.google.devtools.cloudbuild.v2.ServiceDirectoryConfig service_directory_config = 10; `

**Returns**  
---  
**Type** | **Description**  
`[ServiceDirectoryConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ServiceDirectoryConfigOrBuilder)` |   
  
### getSslCa()
    
    
    public abstract String getSslCa()

SSL certificate to use for requests to GitHub Enterprise.

`string ssl_ca = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sslCa.  
  
### getSslCaBytes()
    
    
    public abstract ByteString getSslCaBytes()

SSL certificate to use for requests to GitHub Enterprise.

`string ssl_ca = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sslCa.  
  
### getWebhookSecretSecretVersion()
    
    
    public abstract String getWebhookSecretSecretVersion()

SecretManager resource containing the webhook secret of the GitHub App, formatted as `projects/*/secrets/*/versions/*`.

`string webhook_secret_secret_version = 5 [(.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The webhookSecretSecretVersion.  
  
### getWebhookSecretSecretVersionBytes()
    
    
    public abstract ByteString getWebhookSecretSecretVersionBytes()

SecretManager resource containing the webhook secret of the GitHub App, formatted as `projects/*/secrets/*/versions/*`.

`string webhook_secret_secret_version = 5 [(.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for webhookSecretSecretVersion.  
  
### hasServiceDirectoryConfig()
    
    
    public abstract boolean hasServiceDirectoryConfig()

Configuration for using Service Directory to privately connect to a GitHub Enterprise server. This should only be set if the GitHub Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitHub Enterprise server will be made over the public internet.

`.google.devtools.cloudbuild.v2.ServiceDirectoryConfig service_directory_config = 10; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the serviceDirectoryConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
