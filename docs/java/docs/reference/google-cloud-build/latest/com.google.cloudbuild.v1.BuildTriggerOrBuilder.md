---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTriggerOrBuilder
title: Interface BuildTriggerOrBuilder (3.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:30.910871+00:00
---

# Interface BuildTriggerOrBuilder (3.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTriggerOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BuildTriggerOrBuilder (3.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.101.0 (latest)  3.97.0  3.96.0  3.95.0  3.93.0  3.90.0  3.89.0  3.87.0  3.85.0  3.84.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.74.0  3.72.0  3.70.0  3.69.0  3.66.0  3.65.0  3.64.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.6  3.4.1  3.3.12 
    
    
    public interface BuildTriggerOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsSubstitutions(String key)
    
    
    public abstract boolean containsSubstitutions(String key)

Substitutions for Build resource. The keys must match the following regular expression: `^_[A-Z0-9_]+$`.

`map<string, string> substitutions = 11;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAutodetect()
    
    
    public abstract boolean getAutodetect()

Autodetect build configuration. The following precedence is used (case insensitive):

  1. cloudbuild.yaml
  2. cloudbuild.yml
  3. cloudbuild.json
  4. Dockerfile

Currently only available for GitHub App Triggers.




`bool autodetect = 18;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The autodetect.  
  
### getBuild()
    
    
    public abstract Build getBuild()

Contents of the build template.

`.google.devtools.cloudbuild.v1.Build build = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build)` | The build.  
  
### getBuildOrBuilder()
    
    
    public abstract BuildOrBuilder getBuildOrBuilder()

Contents of the build template.

`.google.devtools.cloudbuild.v1.Build build = 4;`

**Returns**  
---  
**Type** | **Description**  
`[BuildOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOrBuilder)` |   
  
### getBuildTemplateCase()
    
    
    public abstract BuildTrigger.BuildTemplateCase getBuildTemplateCase()

**Returns**  
---  
**Type** | **Description**  
`[BuildTrigger.BuildTemplateCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger.BuildTemplateCase)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Time when the trigger was created.

`.google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Time when the trigger was created.

`.google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Human-readable description of this trigger.

`string description = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Human-readable description of this trigger.

`string description = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDisabled()
    
    
    public abstract boolean getDisabled()

If true, the trigger will never automatically execute a build.

`bool disabled = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The disabled.  
  
### getFilename()
    
    
    public abstract String getFilename()

Path, from the source root, to the build configuration file (i.e. cloudbuild.yaml).

`string filename = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The filename.  
  
### getFilenameBytes()
    
    
    public abstract ByteString getFilenameBytes()

Path, from the source root, to the build configuration file (i.e. cloudbuild.yaml).

`string filename = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for filename.  
  
### getFilter()
    
    
    public abstract String getFilter()

Optional. A Common Expression Language string.

`string filter = 30 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The filter.  
  
### getFilterBytes()
    
    
    public abstract ByteString getFilterBytes()

Optional. A Common Expression Language string.

`string filter = 30 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for filter.  
  
### getGitFileSource()
    
    
    public abstract GitFileSource getGitFileSource()

The file source describing the local or remote Build template.

`.google.devtools.cloudbuild.v1.GitFileSource git_file_source = 24;`

**Returns**  
---  
**Type** | **Description**  
`[GitFileSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GitFileSource)` | The gitFileSource.  
  
### getGitFileSourceOrBuilder()
    
    
    public abstract GitFileSourceOrBuilder getGitFileSourceOrBuilder()

The file source describing the local or remote Build template.

`.google.devtools.cloudbuild.v1.GitFileSource git_file_source = 24;`

**Returns**  
---  
**Type** | **Description**  
`[GitFileSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GitFileSourceOrBuilder)` |   
  
### getGithub()
    
    
    public abstract GitHubEventsConfig getGithub()

GitHubEventsConfig describes the configuration of a trigger that creates a build whenever a GitHub event is received.

Mutually exclusive with `trigger_template`.

`.google.devtools.cloudbuild.v1.GitHubEventsConfig github = 13;`

**Returns**  
---  
**Type** | **Description**  
`[GitHubEventsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GitHubEventsConfig)` | The github.  
  
### getGithubOrBuilder()
    
    
    public abstract GitHubEventsConfigOrBuilder getGithubOrBuilder()

GitHubEventsConfig describes the configuration of a trigger that creates a build whenever a GitHub event is received.

Mutually exclusive with `trigger_template`.

`.google.devtools.cloudbuild.v1.GitHubEventsConfig github = 13;`

**Returns**  
---  
**Type** | **Description**  
`[GitHubEventsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GitHubEventsConfigOrBuilder)` |   
  
### getId()
    
    
    public abstract String getId()

Output only. Unique identifier of the trigger.

`string id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

Output only. Unique identifier of the trigger.

`string id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getIgnoredFiles(int index)
    
    
    public abstract String getIgnoredFiles(int index)

ignored_files and included_files are file glob matches using <https://golang.org/pkg/path/filepath/#Match> extended with support for "**".

If ignored_files and changed files are both empty, then they are not used to determine whether or not to trigger a build.

If ignored_files is not empty, then we ignore any files that match any of the ignored_file globs. If the change has no files that are outside of the ignored_files globs, then we do not trigger a build.

`repeated string ignored_files = 15;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The ignoredFiles at the given index.  
  
### getIgnoredFilesBytes(int index)
    
    
    public abstract ByteString getIgnoredFilesBytes(int index)

ignored_files and included_files are file glob matches using <https://golang.org/pkg/path/filepath/#Match> extended with support for "**".

If ignored_files and changed files are both empty, then they are not used to determine whether or not to trigger a build.

If ignored_files is not empty, then we ignore any files that match any of the ignored_file globs. If the change has no files that are outside of the ignored_files globs, then we do not trigger a build.

`repeated string ignored_files = 15;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the ignoredFiles at the given index.  
  
### getIgnoredFilesCount()
    
    
    public abstract int getIgnoredFilesCount()

ignored_files and included_files are file glob matches using <https://golang.org/pkg/path/filepath/#Match> extended with support for "**".

If ignored_files and changed files are both empty, then they are not used to determine whether or not to trigger a build.

If ignored_files is not empty, then we ignore any files that match any of the ignored_file globs. If the change has no files that are outside of the ignored_files globs, then we do not trigger a build.

`repeated string ignored_files = 15;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of ignoredFiles.  
  
### getIgnoredFilesList()
    
    
    public abstract List<String> getIgnoredFilesList()

ignored_files and included_files are file glob matches using <https://golang.org/pkg/path/filepath/#Match> extended with support for "**".

If ignored_files and changed files are both empty, then they are not used to determine whether or not to trigger a build.

If ignored_files is not empty, then we ignore any files that match any of the ignored_file globs. If the change has no files that are outside of the ignored_files globs, then we do not trigger a build.

`repeated string ignored_files = 15;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the ignoredFiles.  
  
### getIncludedFiles(int index)
    
    
    public abstract String getIncludedFiles(int index)

If any of the files altered in the commit pass the ignored_files filter and included_files is empty, then as far as this filter is concerned, we should trigger the build.

If any of the files altered in the commit pass the ignored_files filter and included_files is not empty, then we make sure that at least one of those files matches a included_files glob. If not, then we do not trigger a build.

`repeated string included_files = 16;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The includedFiles at the given index.  
  
### getIncludedFilesBytes(int index)
    
    
    public abstract ByteString getIncludedFilesBytes(int index)

If any of the files altered in the commit pass the ignored_files filter and included_files is empty, then as far as this filter is concerned, we should trigger the build.

If any of the files altered in the commit pass the ignored_files filter and included_files is not empty, then we make sure that at least one of those files matches a included_files glob. If not, then we do not trigger a build.

`repeated string included_files = 16;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the includedFiles at the given index.  
  
### getIncludedFilesCount()
    
    
    public abstract int getIncludedFilesCount()

If any of the files altered in the commit pass the ignored_files filter and included_files is empty, then as far as this filter is concerned, we should trigger the build.

If any of the files altered in the commit pass the ignored_files filter and included_files is not empty, then we make sure that at least one of those files matches a included_files glob. If not, then we do not trigger a build.

`repeated string included_files = 16;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of includedFiles.  
  
### getIncludedFilesList()
    
    
    public abstract List<String> getIncludedFilesList()

If any of the files altered in the commit pass the ignored_files filter and included_files is empty, then as far as this filter is concerned, we should trigger the build.

If any of the files altered in the commit pass the ignored_files filter and included_files is not empty, then we make sure that at least one of those files matches a included_files glob. If not, then we do not trigger a build.

`repeated string included_files = 16;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the includedFiles.  
  
### getName()
    
    
    public abstract String getName()

User-assigned name of the trigger. Must be unique within the project. Trigger names must meet the following requirements:

  * They must contain only alphanumeric characters and dashes.
  * They can be 1-64 characters long.
  * They must begin and end with an alphanumeric character.



`string name = 21;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

User-assigned name of the trigger. Must be unique within the project. Trigger names must meet the following requirements:

  * They must contain only alphanumeric characters and dashes.
  * They can be 1-64 characters long.
  * They must begin and end with an alphanumeric character.



`string name = 21;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPubsubConfig()
    
    
    public abstract PubsubConfig getPubsubConfig()

PubsubConfig describes the configuration of a trigger that creates a build whenever a Pub/Sub message is published.

`.google.devtools.cloudbuild.v1.PubsubConfig pubsub_config = 29;`

**Returns**  
---  
**Type** | **Description**  
`[PubsubConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.PubsubConfig)` | The pubsubConfig.  
  
### getPubsubConfigOrBuilder()
    
    
    public abstract PubsubConfigOrBuilder getPubsubConfigOrBuilder()

PubsubConfig describes the configuration of a trigger that creates a build whenever a Pub/Sub message is published.

`.google.devtools.cloudbuild.v1.PubsubConfig pubsub_config = 29;`

**Returns**  
---  
**Type** | **Description**  
`[PubsubConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.PubsubConfigOrBuilder)` |   
  
### getRepositoryEventConfig()
    
    
    public abstract RepositoryEventConfig getRepositoryEventConfig()

The configuration of a trigger that creates a build whenever an event from Repo API is received.

`.google.devtools.cloudbuild.v1.RepositoryEventConfig repository_event_config = 39;`

**Returns**  
---  
**Type** | **Description**  
`[RepositoryEventConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.RepositoryEventConfig)` | The repositoryEventConfig.  
  
### getRepositoryEventConfigOrBuilder()
    
    
    public abstract RepositoryEventConfigOrBuilder getRepositoryEventConfigOrBuilder()

The configuration of a trigger that creates a build whenever an event from Repo API is received.

`.google.devtools.cloudbuild.v1.RepositoryEventConfig repository_event_config = 39;`

**Returns**  
---  
**Type** | **Description**  
`[RepositoryEventConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.RepositoryEventConfigOrBuilder)` |   
  
### getResourceName()
    
    
    public abstract String getResourceName()

The `Trigger` name with format: `projects/{project}/locations/{location}/triggers/{trigger}`, where {trigger} is a unique identifier generated by the service.

`string resource_name = 34;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resourceName.  
  
### getResourceNameBytes()
    
    
    public abstract ByteString getResourceNameBytes()

The `Trigger` name with format: `projects/{project}/locations/{location}/triggers/{trigger}`, where {trigger} is a unique identifier generated by the service.

`string resource_name = 34;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for resourceName.  
  
### getServiceAccount()
    
    
    public abstract String getServiceAccount()

The service account used for all user-controlled operations including UpdateBuildTrigger, RunBuildTrigger, CreateBuild, and CancelBuild. If no service account is set and the legacy Cloud Build service account (`[PROJECT_NUM]@cloudbuild.gserviceaccount.com`) is the default for the project then it will be used instead. Format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT_ID_OR_EMAIL}`

`string service_account = 33 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAccount.  
  
### getServiceAccountBytes()
    
    
    public abstract ByteString getServiceAccountBytes()

The service account used for all user-controlled operations including UpdateBuildTrigger, RunBuildTrigger, CreateBuild, and CancelBuild. If no service account is set and the legacy Cloud Build service account (`[PROJECT_NUM]@cloudbuild.gserviceaccount.com`) is the default for the project then it will be used instead. Format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT_ID_OR_EMAIL}`

`string service_account = 33 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAccount.  
  
### getSourceToBuild()
    
    
    public abstract GitRepoSource getSourceToBuild()

The repo and ref of the repository from which to build. This field is used only for those triggers that do not respond to SCM events. Triggers that respond to such events build source at whatever commit caused the event. This field is currently only used by Webhook, Pub/Sub, Manual, and Cron triggers.

`.google.devtools.cloudbuild.v1.GitRepoSource source_to_build = 26;`

**Returns**  
---  
**Type** | **Description**  
`[GitRepoSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GitRepoSource)` | The sourceToBuild.  
  
### getSourceToBuildOrBuilder()
    
    
    public abstract GitRepoSourceOrBuilder getSourceToBuildOrBuilder()

The repo and ref of the repository from which to build. This field is used only for those triggers that do not respond to SCM events. Triggers that respond to such events build source at whatever commit caused the event. This field is currently only used by Webhook, Pub/Sub, Manual, and Cron triggers.

`.google.devtools.cloudbuild.v1.GitRepoSource source_to_build = 26;`

**Returns**  
---  
**Type** | **Description**  
`[GitRepoSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GitRepoSourceOrBuilder)` |   
  
### getSubstitutions() (deprecated)
    
    
    public abstract Map<String,String> getSubstitutions()

Use [#getSubstitutionsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTriggerOrBuilder#com_google_cloudbuild_v1_BuildTriggerOrBuilder_getSubstitutionsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getSubstitutionsCount()
    
    
    public abstract int getSubstitutionsCount()

Substitutions for Build resource. The keys must match the following regular expression: `^_[A-Z0-9_]+$`.

`map<string, string> substitutions = 11;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSubstitutionsMap()
    
    
    public abstract Map<String,String> getSubstitutionsMap()

Substitutions for Build resource. The keys must match the following regular expression: `^_[A-Z0-9_]+$`.

`map<string, string> substitutions = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getSubstitutionsOrDefault(String key, String defaultValue)
    
    
    public abstract String getSubstitutionsOrDefault(String key, String defaultValue)

Substitutions for Build resource. The keys must match the following regular expression: `^_[A-Z0-9_]+$`.

`map<string, string> substitutions = 11;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getSubstitutionsOrThrow(String key)
    
    
    public abstract String getSubstitutionsOrThrow(String key)

Substitutions for Build resource. The keys must match the following regular expression: `^_[A-Z0-9_]+$`.

`map<string, string> substitutions = 11;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getTags(int index)
    
    
    public abstract String getTags(int index)

Tags for annotation of a `BuildTrigger`

`repeated string tags = 19;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tags at the given index.  
  
### getTagsBytes(int index)
    
    
    public abstract ByteString getTagsBytes(int index)

Tags for annotation of a `BuildTrigger`

`repeated string tags = 19;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the tags at the given index.  
  
### getTagsCount()
    
    
    public abstract int getTagsCount()

Tags for annotation of a `BuildTrigger`

`repeated string tags = 19;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of tags.  
  
### getTagsList()
    
    
    public abstract List<String> getTagsList()

Tags for annotation of a `BuildTrigger`

`repeated string tags = 19;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the tags.  
  
### getTriggerTemplate()
    
    
    public abstract RepoSource getTriggerTemplate()

Template describing the types of source changes to trigger a build.

Branch and tag names in trigger templates are interpreted as regular expressions. Any branch or tag change that matches that regular expression will trigger a build.

Mutually exclusive with `github`.

`.google.devtools.cloudbuild.v1.RepoSource trigger_template = 7;`

**Returns**  
---  
**Type** | **Description**  
`[RepoSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.RepoSource)` | The triggerTemplate.  
  
### getTriggerTemplateOrBuilder()
    
    
    public abstract RepoSourceOrBuilder getTriggerTemplateOrBuilder()

Template describing the types of source changes to trigger a build.

Branch and tag names in trigger templates are interpreted as regular expressions. Any branch or tag change that matches that regular expression will trigger a build.

Mutually exclusive with `github`.

`.google.devtools.cloudbuild.v1.RepoSource trigger_template = 7;`

**Returns**  
---  
**Type** | **Description**  
`[RepoSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.RepoSourceOrBuilder)` |   
  
### getWebhookConfig()
    
    
    public abstract WebhookConfig getWebhookConfig()

WebhookConfig describes the configuration of a trigger that creates a build whenever a webhook is sent to a trigger's webhook URL.

`.google.devtools.cloudbuild.v1.WebhookConfig webhook_config = 31;`

**Returns**  
---  
**Type** | **Description**  
`[WebhookConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WebhookConfig)` | The webhookConfig.  
  
### getWebhookConfigOrBuilder()
    
    
    public abstract WebhookConfigOrBuilder getWebhookConfigOrBuilder()

WebhookConfig describes the configuration of a trigger that creates a build whenever a webhook is sent to a trigger's webhook URL.

`.google.devtools.cloudbuild.v1.WebhookConfig webhook_config = 31;`

**Returns**  
---  
**Type** | **Description**  
`[WebhookConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WebhookConfigOrBuilder)` |   
  
### hasAutodetect()
    
    
    public abstract boolean hasAutodetect()

Autodetect build configuration. The following precedence is used (case insensitive):

  1. cloudbuild.yaml
  2. cloudbuild.yml
  3. cloudbuild.json
  4. Dockerfile

Currently only available for GitHub App Triggers.




`bool autodetect = 18;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the autodetect field is set.  
  
### hasBuild()
    
    
    public abstract boolean hasBuild()

Contents of the build template.

`.google.devtools.cloudbuild.v1.Build build = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the build field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Time when the trigger was created.

`.google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasFilename()
    
    
    public abstract boolean hasFilename()

Path, from the source root, to the build configuration file (i.e. cloudbuild.yaml).

`string filename = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the filename field is set.  
  
### hasGitFileSource()
    
    
    public abstract boolean hasGitFileSource()

The file source describing the local or remote Build template.

`.google.devtools.cloudbuild.v1.GitFileSource git_file_source = 24;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gitFileSource field is set.  
  
### hasGithub()
    
    
    public abstract boolean hasGithub()

GitHubEventsConfig describes the configuration of a trigger that creates a build whenever a GitHub event is received.

Mutually exclusive with `trigger_template`.

`.google.devtools.cloudbuild.v1.GitHubEventsConfig github = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the github field is set.  
  
### hasPubsubConfig()
    
    
    public abstract boolean hasPubsubConfig()

PubsubConfig describes the configuration of a trigger that creates a build whenever a Pub/Sub message is published.

`.google.devtools.cloudbuild.v1.PubsubConfig pubsub_config = 29;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pubsubConfig field is set.  
  
### hasRepositoryEventConfig()
    
    
    public abstract boolean hasRepositoryEventConfig()

The configuration of a trigger that creates a build whenever an event from Repo API is received.

`.google.devtools.cloudbuild.v1.RepositoryEventConfig repository_event_config = 39;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the repositoryEventConfig field is set.  
  
### hasSourceToBuild()
    
    
    public abstract boolean hasSourceToBuild()

The repo and ref of the repository from which to build. This field is used only for those triggers that do not respond to SCM events. Triggers that respond to such events build source at whatever commit caused the event. This field is currently only used by Webhook, Pub/Sub, Manual, and Cron triggers.

`.google.devtools.cloudbuild.v1.GitRepoSource source_to_build = 26;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sourceToBuild field is set.  
  
### hasTriggerTemplate()
    
    
    public abstract boolean hasTriggerTemplate()

Template describing the types of source changes to trigger a build.

Branch and tag names in trigger templates are interpreted as regular expressions. Any branch or tag change that matches that regular expression will trigger a build.

Mutually exclusive with `github`.

`.google.devtools.cloudbuild.v1.RepoSource trigger_template = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the triggerTemplate field is set.  
  
### hasWebhookConfig()
    
    
    public abstract boolean hasWebhookConfig()

WebhookConfig describes the configuration of a trigger that creates a build whenever a webhook is sent to a trigger's webhook URL.

`.google.devtools.cloudbuild.v1.WebhookConfig webhook_config = 31;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the webhookConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
