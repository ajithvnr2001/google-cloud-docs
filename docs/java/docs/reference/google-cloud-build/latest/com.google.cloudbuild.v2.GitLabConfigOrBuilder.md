---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GitLabConfigOrBuilder
title: Interface GitLabConfigOrBuilder (3.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:43:33.787202+00:00
---

# Interface GitLabConfigOrBuilder (3.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GitLabConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GitLabConfigOrBuilder (3.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.101.0 (latest)  3.97.0  3.96.0  3.95.0  3.93.0  3.90.0  3.89.0  3.87.0  3.85.0  3.84.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.74.0  3.72.0  3.70.0  3.69.0  3.66.0  3.65.0  3.64.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.6  3.4.1  3.3.12 
    
    
    public interface GitLabConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAuthorizerCredential()
    
    
    public abstract UserCredential getAuthorizerCredential()

Required. A GitLab personal access token with the `api` scope access.

` .google.devtools.cloudbuild.v2.UserCredential authorizer_credential = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[UserCredential](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.UserCredential)` | The authorizerCredential.  
  
### getAuthorizerCredentialOrBuilder()
    
    
    public abstract UserCredentialOrBuilder getAuthorizerCredentialOrBuilder()

Required. A GitLab personal access token with the `api` scope access.

` .google.devtools.cloudbuild.v2.UserCredential authorizer_credential = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[UserCredentialOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.UserCredentialOrBuilder)` |   
  
### getHostUri()
    
    
    public abstract String getHostUri()

The URI of the GitLab Enterprise host this connection is for. If not specified, the default value is <https://gitlab.com>.

`string host_uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The hostUri.  
  
### getHostUriBytes()
    
    
    public abstract ByteString getHostUriBytes()

The URI of the GitLab Enterprise host this connection is for. If not specified, the default value is <https://gitlab.com>.

`string host_uri = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for hostUri.  
  
### getReadAuthorizerCredential()
    
    
    public abstract UserCredential getReadAuthorizerCredential()

Required. A GitLab personal access token with the minimum `read_api` scope access.

` .google.devtools.cloudbuild.v2.UserCredential read_authorizer_credential = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[UserCredential](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.UserCredential)` | The readAuthorizerCredential.  
  
### getReadAuthorizerCredentialOrBuilder()
    
    
    public abstract UserCredentialOrBuilder getReadAuthorizerCredentialOrBuilder()

Required. A GitLab personal access token with the minimum `read_api` scope access.

` .google.devtools.cloudbuild.v2.UserCredential read_authorizer_credential = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[UserCredentialOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.UserCredentialOrBuilder)` |   
  
### getServerVersion()
    
    
    public abstract String getServerVersion()

Output only. Version of the GitLab Enterprise server running on the `host_uri`.

`string server_version = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serverVersion.  
  
### getServerVersionBytes()
    
    
    public abstract ByteString getServerVersionBytes()

Output only. Version of the GitLab Enterprise server running on the `host_uri`.

`string server_version = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serverVersion.  
  
### getServiceDirectoryConfig()
    
    
    public abstract ServiceDirectoryConfig getServiceDirectoryConfig()

Configuration for using Service Directory to privately connect to a GitLab Enterprise server. This should only be set if the GitLab Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitLab Enterprise server will be made over the public internet.

`.google.devtools.cloudbuild.v2.ServiceDirectoryConfig service_directory_config = 5; `

**Returns**  
---  
**Type** | **Description**  
`[ServiceDirectoryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ServiceDirectoryConfig)` | The serviceDirectoryConfig.  
  
### getServiceDirectoryConfigOrBuilder()
    
    
    public abstract ServiceDirectoryConfigOrBuilder getServiceDirectoryConfigOrBuilder()

Configuration for using Service Directory to privately connect to a GitLab Enterprise server. This should only be set if the GitLab Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitLab Enterprise server will be made over the public internet.

`.google.devtools.cloudbuild.v2.ServiceDirectoryConfig service_directory_config = 5; `

**Returns**  
---  
**Type** | **Description**  
`[ServiceDirectoryConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ServiceDirectoryConfigOrBuilder)` |   
  
### getSslCa()
    
    
    public abstract String getSslCa()

SSL certificate to use for requests to GitLab Enterprise.

`string ssl_ca = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sslCa.  
  
### getSslCaBytes()
    
    
    public abstract ByteString getSslCaBytes()

SSL certificate to use for requests to GitLab Enterprise.

`string ssl_ca = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sslCa.  
  
### getWebhookSecretSecretVersion()
    
    
    public abstract String getWebhookSecretSecretVersion()

Required. Immutable. SecretManager resource containing the webhook secret of a GitLab Enterprise project, formatted as `projects/*/secrets/*/versions/*`.

` string webhook_secret_secret_version = 2 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The webhookSecretSecretVersion.  
  
### getWebhookSecretSecretVersionBytes()
    
    
    public abstract ByteString getWebhookSecretSecretVersionBytes()

Required. Immutable. SecretManager resource containing the webhook secret of a GitLab Enterprise project, formatted as `projects/*/secrets/*/versions/*`.

` string webhook_secret_secret_version = 2 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IMMUTABLE, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for webhookSecretSecretVersion.  
  
### hasAuthorizerCredential()
    
    
    public abstract boolean hasAuthorizerCredential()

Required. A GitLab personal access token with the `api` scope access.

` .google.devtools.cloudbuild.v2.UserCredential authorizer_credential = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the authorizerCredential field is set.  
  
### hasReadAuthorizerCredential()
    
    
    public abstract boolean hasReadAuthorizerCredential()

Required. A GitLab personal access token with the minimum `read_api` scope access.

` .google.devtools.cloudbuild.v2.UserCredential read_authorizer_credential = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the readAuthorizerCredential field is set.  
  
### hasServiceDirectoryConfig()
    
    
    public abstract boolean hasServiceDirectoryConfig()

Configuration for using Service Directory to privately connect to a GitLab Enterprise server. This should only be set if the GitLab Enterprise server is hosted on-premises and not reachable by public internet. If this field is left empty, calls to the GitLab Enterprise server will be made over the public internet.

`.google.devtools.cloudbuild.v2.ServiceDirectoryConfig service_directory_config = 5; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the serviceDirectoryConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
