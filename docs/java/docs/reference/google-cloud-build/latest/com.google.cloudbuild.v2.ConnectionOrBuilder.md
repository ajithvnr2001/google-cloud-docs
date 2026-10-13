---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ConnectionOrBuilder
title: Interface ConnectionOrBuilder (3.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:43:31.000928+00:00
---

# Interface ConnectionOrBuilder (3.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ConnectionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ConnectionOrBuilder (3.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.101.0 (latest)  3.97.0  3.96.0  3.95.0  3.93.0  3.90.0  3.89.0  3.87.0  3.85.0  3.84.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.74.0  3.72.0  3.70.0  3.69.0  3.66.0  3.65.0  3.64.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.6  3.4.1  3.3.12 
    
    
    public interface ConnectionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsAnnotations(String key)
    
    
    public abstract boolean containsAnnotations(String key)

Allows clients to store small amounts of arbitrary data.

`map<string, string> annotations = 15;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnnotations() (deprecated)
    
    
    public abstract Map<String,String> getAnnotations()

Use [#getAnnotationsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ConnectionOrBuilder#com_google_cloudbuild_v2_ConnectionOrBuilder_getAnnotationsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsCount()
    
    
    public abstract int getAnnotationsCount()

Allows clients to store small amounts of arbitrary data.

`map<string, string> annotations = 15;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnnotationsMap()
    
    
    public abstract Map<String,String> getAnnotationsMap()

Allows clients to store small amounts of arbitrary data.

`map<string, string> annotations = 15;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsOrDefault(String key, String defaultValue)
    
    
    public abstract String getAnnotationsOrDefault(String key, String defaultValue)

Allows clients to store small amounts of arbitrary data.

`map<string, string> annotations = 15;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAnnotationsOrThrow(String key)
    
    
    public abstract String getAnnotationsOrThrow(String key)

Allows clients to store small amounts of arbitrary data.

`map<string, string> annotations = 15;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getBitbucketCloudConfig()
    
    
    public abstract BitbucketCloudConfig getBitbucketCloudConfig()

Configuration for connections to Bitbucket Cloud.

`.google.devtools.cloudbuild.v2.BitbucketCloudConfig bitbucket_cloud_config = 9;`

**Returns**  
---  
**Type** | **Description**  
`[BitbucketCloudConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.BitbucketCloudConfig)` | The bitbucketCloudConfig.  
  
### getBitbucketCloudConfigOrBuilder()
    
    
    public abstract BitbucketCloudConfigOrBuilder getBitbucketCloudConfigOrBuilder()

Configuration for connections to Bitbucket Cloud.

`.google.devtools.cloudbuild.v2.BitbucketCloudConfig bitbucket_cloud_config = 9;`

**Returns**  
---  
**Type** | **Description**  
`[BitbucketCloudConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.BitbucketCloudConfigOrBuilder)` |   
  
### getBitbucketDataCenterConfig()
    
    
    public abstract BitbucketDataCenterConfig getBitbucketDataCenterConfig()

Configuration for connections to Bitbucket Data Center.

` .google.devtools.cloudbuild.v2.BitbucketDataCenterConfig bitbucket_data_center_config = 8; `

**Returns**  
---  
**Type** | **Description**  
`[BitbucketDataCenterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.BitbucketDataCenterConfig)` | The bitbucketDataCenterConfig.  
  
### getBitbucketDataCenterConfigOrBuilder()
    
    
    public abstract BitbucketDataCenterConfigOrBuilder getBitbucketDataCenterConfigOrBuilder()

Configuration for connections to Bitbucket Data Center.

` .google.devtools.cloudbuild.v2.BitbucketDataCenterConfig bitbucket_data_center_config = 8; `

**Returns**  
---  
**Type** | **Description**  
`[BitbucketDataCenterConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.BitbucketDataCenterConfigOrBuilder)` |   
  
### getConnectionConfigCase()
    
    
    public abstract Connection.ConnectionConfigCase getConnectionConfigCase()

**Returns**  
---  
**Type** | **Description**  
`[Connection.ConnectionConfigCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.Connection.ConnectionConfigCase)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Server assigned timestamp for when the connection was created.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Server assigned timestamp for when the connection was created.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDisabled()
    
    
    public abstract boolean getDisabled()

If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled.

`bool disabled = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The disabled.  
  
### getEtag()
    
    
    public abstract String getEtag()

This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.

`string etag = 16;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public abstract ByteString getEtagBytes()

This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.

`string etag = 16;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getGithubConfig()
    
    
    public abstract GitHubConfig getGithubConfig()

Configuration for connections to github.com.

`.google.devtools.cloudbuild.v2.GitHubConfig github_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[GitHubConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GitHubConfig)` | The githubConfig.  
  
### getGithubConfigOrBuilder()
    
    
    public abstract GitHubConfigOrBuilder getGithubConfigOrBuilder()

Configuration for connections to github.com.

`.google.devtools.cloudbuild.v2.GitHubConfig github_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[GitHubConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GitHubConfigOrBuilder)` |   
  
### getGithubEnterpriseConfig()
    
    
    public abstract GitHubEnterpriseConfig getGithubEnterpriseConfig()

Configuration for connections to an instance of GitHub Enterprise.

`.google.devtools.cloudbuild.v2.GitHubEnterpriseConfig github_enterprise_config = 6; `

**Returns**  
---  
**Type** | **Description**  
`[GitHubEnterpriseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GitHubEnterpriseConfig)` | The githubEnterpriseConfig.  
  
### getGithubEnterpriseConfigOrBuilder()
    
    
    public abstract GitHubEnterpriseConfigOrBuilder getGithubEnterpriseConfigOrBuilder()

Configuration for connections to an instance of GitHub Enterprise.

`.google.devtools.cloudbuild.v2.GitHubEnterpriseConfig github_enterprise_config = 6; `

**Returns**  
---  
**Type** | **Description**  
`[GitHubEnterpriseConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GitHubEnterpriseConfigOrBuilder)` |   
  
### getGitlabConfig()
    
    
    public abstract GitLabConfig getGitlabConfig()

Configuration for connections to gitlab.com or an instance of GitLab Enterprise.

`.google.devtools.cloudbuild.v2.GitLabConfig gitlab_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[GitLabConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GitLabConfig)` | The gitlabConfig.  
  
### getGitlabConfigOrBuilder()
    
    
    public abstract GitLabConfigOrBuilder getGitlabConfigOrBuilder()

Configuration for connections to gitlab.com or an instance of GitLab Enterprise.

`.google.devtools.cloudbuild.v2.GitLabConfig gitlab_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[GitLabConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GitLabConfigOrBuilder)` |   
  
### getInstallationState()
    
    
    public abstract InstallationState getInstallationState()

Output only. Installation state of the Connection.

` .google.devtools.cloudbuild.v2.InstallationState installation_state = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[InstallationState](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.InstallationState)` | The installationState.  
  
### getInstallationStateOrBuilder()
    
    
    public abstract InstallationStateOrBuilder getInstallationStateOrBuilder()

Output only. Installation state of the Connection.

` .google.devtools.cloudbuild.v2.InstallationState installation_state = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[InstallationStateOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.InstallationStateOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Immutable. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connection_id}`.

`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Immutable. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connection_id}`.

`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getReconciling()
    
    
    public abstract boolean getReconciling()

Output only. Set to true when the connection is being set up or updated in the background.

`bool reconciling = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The reconciling.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. Server assigned timestamp for when the connection was updated.

`.google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Server assigned timestamp for when the connection was updated.

`.google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasBitbucketCloudConfig()
    
    
    public abstract boolean hasBitbucketCloudConfig()

Configuration for connections to Bitbucket Cloud.

`.google.devtools.cloudbuild.v2.BitbucketCloudConfig bitbucket_cloud_config = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bitbucketCloudConfig field is set.  
  
### hasBitbucketDataCenterConfig()
    
    
    public abstract boolean hasBitbucketDataCenterConfig()

Configuration for connections to Bitbucket Data Center.

` .google.devtools.cloudbuild.v2.BitbucketDataCenterConfig bitbucket_data_center_config = 8; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bitbucketDataCenterConfig field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Server assigned timestamp for when the connection was created.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasGithubConfig()
    
    
    public abstract boolean hasGithubConfig()

Configuration for connections to github.com.

`.google.devtools.cloudbuild.v2.GitHubConfig github_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the githubConfig field is set.  
  
### hasGithubEnterpriseConfig()
    
    
    public abstract boolean hasGithubEnterpriseConfig()

Configuration for connections to an instance of GitHub Enterprise.

`.google.devtools.cloudbuild.v2.GitHubEnterpriseConfig github_enterprise_config = 6; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the githubEnterpriseConfig field is set.  
  
### hasGitlabConfig()
    
    
    public abstract boolean hasGitlabConfig()

Configuration for connections to gitlab.com or an instance of GitLab Enterprise.

`.google.devtools.cloudbuild.v2.GitLabConfig gitlab_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gitlabConfig field is set.  
  
### hasInstallationState()
    
    
    public abstract boolean hasInstallationState()

Output only. Installation state of the Connection.

` .google.devtools.cloudbuild.v2.InstallationState installation_state = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the installationState field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. Server assigned timestamp for when the connection was updated.

`.google.protobuf.Timestamp update_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
