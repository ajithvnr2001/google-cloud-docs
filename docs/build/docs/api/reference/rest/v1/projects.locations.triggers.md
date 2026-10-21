---
url: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers
title: REST Resource: projects.locations.triggers \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:22.417679+00:00
---

# REST Resource: projects.locations.triggers  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Reference ](https://docs.cloud.google.com/build/docs/api)



Send feedback 

#  REST Resource: projects.locations.triggers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: BuildTrigger
    * JSON representation
    * GitHubEventsConfig
      * JSON representation
    * PullRequestFilter
      * JSON representation
    * CommentControl
    * PushFilter
      * JSON representation
    * PubsubConfig
      * JSON representation
    * State
    * WebhookConfig
      * JSON representation
    * State
    * BitbucketServerTriggerConfig
      * JSON representation
    * GitFileSource
      * JSON representation
    * RepoType
    * GitRepoSource
      * JSON representation
    * EventType
    * IncludeBuildLogs
    * RepositoryEventConfig
      * JSON representation
    * RepositoryType
    * DeveloperConnectEventConfig
      * JSON representation
    * GitRepositoryLinkType
  * Methods



## Resource: BuildTrigger

Configuration for an automated build in response to source repository changes.

JSON representation  
---  
      
    
    {
      "resourceName": string,
      "id": string,
      "description": string,
      "name": string,
      "tags": [
        string
      ],
      "triggerTemplate": {
        object ([RepoSource](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/RepoSource))
      },
      "github": {
        object ([GitHubEventsConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.GitHubEventsConfig))
      },
      "pubsubConfig": {
        object ([PubsubConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PubsubConfig))
      },
      "webhookConfig": {
        object ([WebhookConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.WebhookConfig))
      },
      "bitbucketServerTriggerConfig": {
        object ([BitbucketServerTriggerConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.BitbucketServerTriggerConfig))
      },
      "createTime": string,
      "disabled": boolean,
      "substitutions": {
        string: string,
        ...
      },
      "ignoredFiles": [
        string
      ],
      "includedFiles": [
        string
      ],
      "sourceToBuild": {
        object ([GitRepoSource](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.GitRepoSource))
      },
      "approvalConfig": {
        object ([ApprovalConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/ApprovalConfig))
      },
      "filter": string,
      "serviceAccount": string,
      "eventType": enum ([EventType](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.EventType)),
      "includeBuildLogs": enum ([IncludeBuildLogs](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.IncludeBuildLogs)),
      "repositoryEventConfig": {
        object ([RepositoryEventConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.RepositoryEventConfig))
      },
      "developerConnectEventConfig": {
        object ([DeveloperConnectEventConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.DeveloperConnectEventConfig))
      },
    
      // Union field build_template can be only one of the following:
      "autodetect": boolean,
      "build": {
        object ([Build](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#Build))
      },
      "filename": string,
      "gitFileSource": {
        object ([GitFileSource](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.GitFileSource))
      }
      // End of list of possible types for union field build_template.
    }  
  
Fields  
---  
`resourceName` |  `string` The `Trigger` name with format: `projects/{project}/locations/{location}/triggers/{trigger}`, where {trigger} is a unique identifier generated by the service.  
`id` |  `string` Output only. Unique identifier of the trigger.  
`description` |  `string` Human-readable description of this trigger.  
`name` |  `string` User-assigned name of the trigger. Must be unique within the project. Trigger names must meet the following requirements:

  * They must contain only alphanumeric characters and dashes.
  * They can be 1-64 characters long.
  * They must begin and end with an alphanumeric character.

  
`tags[]` |  `string` Tags for annotation of a `BuildTrigger`  
`triggerTemplate` |  `object (`[RepoSource](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/RepoSource)`)` Template describing the types of source changes to trigger a build.Branch and tag names in trigger templates are interpreted as regular expressions. Any branch or tag change that matches that regular expression will trigger a build.Mutually exclusive with `github`.  
`github` |  `object (`[GitHubEventsConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.GitHubEventsConfig)`)` GitHubEventsConfig describes the configuration of a trigger that creates a build whenever a GitHub event is received.Mutually exclusive with `triggerTemplate`.  
`pubsubConfig` |  `object (`[PubsubConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PubsubConfig)`)` PubsubConfig describes the configuration of a trigger that creates a build whenever a Pub/Sub message is published.  
`webhookConfig` |  `object (`[WebhookConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.WebhookConfig)`)` WebhookConfig describes the configuration of a trigger that creates a build whenever a webhook is sent to a trigger's webhook URL.  
`bitbucketServerTriggerConfig` |  `object (`[BitbucketServerTriggerConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.BitbucketServerTriggerConfig)`)` BitbucketServerTriggerConfig describes the configuration of a trigger that creates a build whenever a Bitbucket Server event is received.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the trigger was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`disabled` |  `boolean` If true, the trigger will never automatically execute a build.  
`substitutions` |  `map (key: string, value: string)` Substitutions for Build resource. The keys must match the following regular expression: `^_[A-Z0-9_]+$`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`ignoredFiles[]` |  `string` ignoredFiles and includedFiles are file glob matches using <https://golang.org/pkg/path/filepath/#Match> extended with support for "**".If ignoredFiles and changed files are both empty, then they are not used to determine whether or not to trigger a build.If ignoredFiles is not empty, then we ignore any files that match any of the ignored_file globs. If the change has no files that are outside of the ignoredFiles globs, then we do not trigger a build.  
`includedFiles[]` |  `string` If any of the files altered in the commit pass the ignoredFiles filter and includedFiles is empty, then as far as this filter is concerned, we should trigger the build.If any of the files altered in the commit pass the ignoredFiles filter and includedFiles is not empty, then we make sure that at least one of those files matches a includedFiles glob. If not, then we do not trigger a build.  
`sourceToBuild` |  `object (`[GitRepoSource](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.GitRepoSource)`)` The repo and ref of the repository from which to build. This field is used only for those triggers that do not respond to SCM events. Triggers that respond to such events build source at whatever commit caused the event. This field is currently only used by Webhook, Pub/Sub, Manual, and Cron triggers.  
`approvalConfig` |  `object (`[ApprovalConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/ApprovalConfig)`)` Configuration for manual approval to start a build invocation of this BuildTrigger.  
`filter` |  `string` A Common Expression Language string.  
`serviceAccount` |  `string` The service account used for all user-controlled operations including triggers.patch, triggers.run, builds.create, and builds.cancel. If no service account is set and the legacy Cloud Build service account ([PROJECT_NUM]@cloudbuild.gserviceaccount.com) is the default for the project then it will be used instead. Format: `projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT_ID_OR_EMAIL}`  
`eventType` |  `enum (`[EventType](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.EventType)`)` EventType allows the user to explicitly set the type of event to which this BuildTrigger should respond. This field will be validated against the rest of the configuration if it is set.  
`includeBuildLogs` |  `enum (`[IncludeBuildLogs](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.IncludeBuildLogs)`)` If set to INCLUDE_BUILD_LOGS_WITH_STATUS, log url will be shown on GitHub page when build status is final. Setting this field to INCLUDE_BUILD_LOGS_WITH_STATUS for non GitHub triggers results in INVALID_ARGUMENT error.  
`repositoryEventConfig` |  `object (`[RepositoryEventConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.RepositoryEventConfig)`)` The configuration of a trigger that creates a build whenever an event from Repo API is received.  
`developerConnectEventConfig` |  `object (`[DeveloperConnectEventConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.DeveloperConnectEventConfig)`)` Optional. The configuration of a trigger that creates a build whenever an event from the DeveloperConnect API is received.  
Union field `build_template`. Template describing the Build request to make when the trigger is matched. At least one of the template fields must be provided. `build_template` can be only one of the following:  
`autodetect` |  `boolean` Autodetect build configuration. The following precedence is used (case insensitive):

  1. cloudbuild.yaml
  2. cloudbuild.yml
  3. cloudbuild.json
  4. Dockerfile

Currently only available for GitHub App Triggers.  
`build` |  `object (`[Build](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#Build)`)` Contents of the build template.  
`filename` |  `string` Path, from the source root, to the build configuration file (i.e. cloudbuild.yaml).  
`gitFileSource` |  `object (`[GitFileSource](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.GitFileSource)`)` The file source describing the local or remote Build template.  
  
### GitHubEventsConfig

GitHubEventsConfig describes the configuration of a trigger that creates a build whenever a GitHub event is received.

JSON representation  
---  
      
    
    {
      "installationId": string,
      "owner": string,
      "name": string,
      "enterpriseConfigResourceName": string,
    
      // Union field event can be only one of the following:
      "pullRequest": {
        object ([PullRequestFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PullRequestFilter))
      },
      "push": {
        object ([PushFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PushFilter))
      }
      // End of list of possible types for union field event.
    }  
  
Fields  
---  
`installationId  
**(deprecated)**` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!The installationID that emits the GitHub event.  
`owner` |  `string` Owner of the repository. For example: The owner for <https://github.com/googlecloudplatform/cloud-builders> is "googlecloudplatform".  
`name` |  `string` Name of the repository. For example: The name for <https://github.com/googlecloudplatform/cloud-builders> is "cloud-builders".  
`enterpriseConfigResourceName` |  `string` The resource name of the github enterprise config that should be applied to this installation. For example: "projects/{$projectId}/locations/{$locationId}/githubEnterpriseConfigs/{$configId}"  
Union field `event`. Filter describing the types of events to trigger a build. Currently supported event types: push, pull_request. `event` can be only one of the following:  
`pullRequest` |  `object (`[PullRequestFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PullRequestFilter)`)` filter to match changes in pull requests.  
`push` |  `object (`[PushFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PushFilter)`)` filter to match changes in refs like branches, tags.  
  
### PullRequestFilter

PullRequestFilter contains filter properties for matching GitHub Pull Requests.

JSON representation  
---  
      
    
    {
      "commentControl": enum ([CommentControl](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.CommentControl)),
      "invertRegex": boolean,
    
      // Union field git_ref can be only one of the following:
      "branch": string
      // End of list of possible types for union field git_ref.
    }  
  
Fields  
---  
`commentControl` |  `enum (`[CommentControl](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.CommentControl)`)` If CommentControl is enabled, depending on the setting, builds may not fire until a repository writer comments `/gcbrun` on a pull request or `/gcbrun` is in the pull request description. Only PR comments that contain `/gcbrun` will trigger builds.If CommentControl is set to disabled, comments with `/gcbrun` from a user with repository write permission or above will still trigger builds to run.  
`invertRegex` |  `boolean` If true, branches that do NOT match the gitRef will trigger a build.  
Union field `git_ref`. Target refs to match. A target ref is the git reference where the pull request will be applied. `git_ref` can be only one of the following:  
`branch` |  `string` Regex of branches to match.The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at <https://github.com/google/re2/wiki/Syntax>  
  
### CommentControl

Controls whether or not a `/gcbrun` comment is required from a user with repository write permission or above in order to trigger Build runs for pull requests. Pull Request update events differ between repo types. Check repo specific guides ([GitHub](https://cloud.google.com/build/docs/automating-builds/github/build-repos-from-github-enterprise#creating_a_github_enterprise_trigger), [Bitbucket](https://cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-server#creating_a_bitbucket_server_trigger), [GitLab](https://cloud.google.com/build/docs/automating-builds/gitlab/build-repos-from-gitlab#creating_a_gitlab_trigger) for details.

Enums  
---  
`COMMENTS_DISABLED` | Do not require `/gcbrun` comments from a user with repository write permission or above on pull requests before builds are triggered. Comments that contain `/gcbrun` will still fire builds so this should be thought of as comments not required.  
`COMMENTS_ENABLED` | Builds will only fire in response to pull requests if: 1. The pull request author has repository write permission or above and `/gcbrun` is in the PR description. 2. A user with repository writer permissions or above comments `/gcbrun` on a pull request authored by any user.  
`COMMENTS_ENABLED_FOR_EXTERNAL_CONTRIBUTORS_ONLY` | Builds will only fire in response to pull requests if: 1. The pull request author is a repository writer or above. 2. If the author does not have write permissions, a user with write permissions or above must comment `/gcbrun` in order to fire a build.  
  
### PushFilter

Push contains filter properties for matching GitHub git pushes.

JSON representation  
---  
      
    
    {
      "invertRegex": boolean,
    
      // Union field git_ref can be only one of the following:
      "branch": string,
      "tag": string
      // End of list of possible types for union field git_ref.
    }  
  
Fields  
---  
`invertRegex` |  `boolean` When true, only trigger a build if the revision regex does NOT match the gitRef regex.  
Union field `git_ref`. Modified refs to match. A modified refs are the refs modified by a git push operation. `git_ref` can be only one of the following:  
`branch` |  `string` Regexes matching branches to build.The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at <https://github.com/google/re2/wiki/Syntax>  
`tag` |  `string` Regexes matching tags to build.The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at <https://github.com/google/re2/wiki/Syntax>  
  
### PubsubConfig

PubsubConfig describes the configuration of a trigger that creates a build whenever a Pub/Sub message is published.

JSON representation  
---  
      
    
    {
      "subscription": string,
      "topic": string,
      "serviceAccountEmail": string,
      "state": enum ([State](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.State))
    }  
  
Fields  
---  
`subscription` |  `string` Output only. Name of the subscription. Format is `projects/{project}/subscriptions/{subscription}`.  
`topic` |  `string` Optional. The name of the topic from which this subscription is receiving messages. Format is `projects/{project}/topics/{topic}`.  
`serviceAccountEmail` |  `string` Service account that will make the push request.  
`state` |  `enum (`[State](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.State)`)` Potential issues with the underlying Pub/Sub subscription configuration. Only populated on get requests.  
  
### State

Enumerates potential issues with the underlying Pub/Sub subscription configuration.

Enums  
---  
`STATE_UNSPECIFIED` | The subscription configuration has not been checked.  
`OK` | The Pub/Sub subscription is properly configured.  
`SUBSCRIPTION_DELETED` | The subscription has been deleted.  
`TOPIC_DELETED` | The topic has been deleted.  
`SUBSCRIPTION_MISCONFIGURED` | Some of the subscription's field are misconfigured.  
  
### WebhookConfig

WebhookConfig describes the configuration of a trigger that creates a build whenever a webhook is sent to a trigger's webhook URL.

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.State_1)),
    
      // Union field auth_method can be only one of the following:
      "secret": string
      // End of list of possible types for union field auth_method.
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.State_1)`)` Potential issues with the underlying Pub/Sub subscription configuration. Only populated on get requests.  
Union field `auth_method`. Auth method specifies how the webhook authenticates with GCP. `auth_method` can be only one of the following:  
`secret` |  `string` Required. Resource name for the secret required as a URL parameter.  
  
### State

Enumerates potential issues with the Secret Manager secret provided by the user.

Enums  
---  
`STATE_UNSPECIFIED` | The webhook auth configuration not been checked.  
`OK` | The auth configuration is properly setup.  
`SECRET_DELETED` | The secret provided in auth_method has been deleted.  
  
### BitbucketServerTriggerConfig

BitbucketServerTriggerConfig describes the configuration of a trigger that creates a build whenever a Bitbucket Server event is received.

JSON representation  
---  
      
    
    {
      "repoSlug": string,
      "projectKey": string,
      "bitbucketServerConfigResource": string,
      "bitbucketServerConfig": {
        object ([BitbucketServerConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs#BitbucketServerConfig))
      },
    
      // Union field event can be only one of the following:
      "pullRequest": {
        object ([PullRequestFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PullRequestFilter))
      },
      "push": {
        object ([PushFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PushFilter))
      }
      // End of list of possible types for union field event.
    }  
  
Fields  
---  
`repoSlug` |  `string` Required. Slug of the repository. A repository slug is a URL-friendly version of a repository name, automatically generated by Bitbucket for use in the URL. For example, if the repository name is 'test repo', in the URL it would become 'test-repo' as in <https://mybitbucket.server/projects/TEST/repos/test-repo>.  
`projectKey` |  `string` Required. Key of the project that the repo is in. For example: The key for <https://mybitbucket.server/projects/TEST/repos/test-repo> is "TEST".  
`bitbucketServerConfigResource` |  `string` Required. The Bitbucket server config resource that this trigger config maps to.  
`bitbucketServerConfig` |  `object (`[BitbucketServerConfig](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.bitbucketServerConfigs#BitbucketServerConfig)`)` Output only. The BitbucketServerConfig specified in the bitbucketServerConfigResource field.  
Union field `event`. Filter describing the types of events to trigger a build. Currently supported event types: push, pull_request. `event` can be only one of the following:  
`pullRequest` |  `object (`[PullRequestFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PullRequestFilter)`)` Filter to match changes in pull requests.  
`push` |  `object (`[PushFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PushFilter)`)` Filter to match changes in refs like branches, tags.  
  
### GitFileSource

GitFileSource describes a file within a (possibly remote) code repository.

JSON representation  
---  
      
    
    {
      "path": string,
      "uri": string,
      "repoType": enum ([RepoType](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.RepoType)),
      "revision": string,
    
      // Union field source can be only one of the following:
      "repository": string
      // End of list of possible types for union field source.
    
      // Union field enterprise_config can be only one of the following:
      "githubEnterpriseConfig": string,
      "bitbucketServerConfig": string
      // End of list of possible types for union field enterprise_config.
    }  
  
Fields  
---  
`path` |  `string` The path of the file, with the repo root as the root of the path.  
`uri` |  `string` The URI of the repo. Either uri or repository can be specified. If unspecified, the repo from which the trigger invocation originated is assumed to be the repo from which to read the specified path.  
`repoType` |  `enum (`[RepoType](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.RepoType)`)` See RepoType above.  
`revision` |  `string` The branch, tag, arbitrary ref, or SHA version of the repo to use when resolving the filename (optional). This field respects the same syntax/resolution as described here: <https://git-scm.com/docs/gitrevisions> If unspecified, the revision from which the trigger invocation originated is assumed to be the revision from which to read the specified path.  
Union field `source`. The source of the SCM repo. `source` can be only one of the following:  
`repository` |  `string` The fully qualified resource name of the Repos API repository. Either URI or repository can be specified. If unspecified, the repo from which the trigger invocation originated is assumed to be the repo from which to read the specified path.  
Union field `enterprise_config`. The resource name of the enterprise config that should be applied to this source. `enterprise_config` can be only one of the following:  
`githubEnterpriseConfig` |  `string` The full resource name of the github enterprise config. Format: `projects/{project}/locations/{location}/githubEnterpriseConfigs/{id}`. `projects/{project}/githubEnterpriseConfigs/{id}`.  
`bitbucketServerConfig` |  `string` The full resource name of the bitbucket server config. Format: `projects/{project}/locations/{location}/bitbucketServerConfigs/{id}`.  
  
### RepoType

The type of the repo, since it may not be explicit from the `repo` field (e.g from a URL).

Enums  
---  
`UNKNOWN` | The default, unknown repo type. Don't use it, instead use one of the other repo types.  
`CLOUD_SOURCE_REPOSITORIES` | A Google Cloud Source Repositories-hosted repo.  
`GITHUB` | A GitHub-hosted repo not necessarily on "github.com" (i.e. GitHub Enterprise).  
`BITBUCKET_SERVER` | A Bitbucket Server-hosted repo.  
`GITLAB` | A GitLab-hosted repo.  
`BITBUCKET_CLOUD` | A Bitbucket Cloud-hosted repo.  
  
### GitRepoSource

GitRepoSource describes a repo and ref of a code repository.

JSON representation  
---  
      
    
    {
      "uri": string,
      "ref": string,
      "repoType": enum ([RepoType](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.RepoType)),
    
      // Union field source can be only one of the following:
      "repository": string
      // End of list of possible types for union field source.
    
      // Union field enterprise_config can be only one of the following:
      "githubEnterpriseConfig": string,
      "bitbucketServerConfig": string
      // End of list of possible types for union field enterprise_config.
    }  
  
Fields  
---  
`uri` |  `string` The URI of the repo (e.g. <https://github.com/user/repo.git)>. Either `uri` or `repository` can be specified and is required.  
`ref` |  `string` The branch or tag to use. Must start with "refs/" (required).  
`repoType` |  `enum (`[RepoType](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.RepoType)`)` See RepoType below.  
Union field `source`. The source of the SCM repo. `source` can be only one of the following:  
`repository` |  `string` The connected repository resource name, in the format `projects/*/locations/*/connections/*/repositories/*`. Either `uri` or `repository` can be specified and is required.  
Union field `enterprise_config`. The resource name of the enterprise config that should be applied to this source. `enterprise_config` can be only one of the following:  
`githubEnterpriseConfig` |  `string` The full resource name of the github enterprise config. Format: `projects/{project}/locations/{location}/githubEnterpriseConfigs/{id}`. `projects/{project}/githubEnterpriseConfigs/{id}`.  
`bitbucketServerConfig` |  `string` The full resource name of the bitbucket server config. Format: `projects/{project}/locations/{location}/bitbucketServerConfigs/{id}`.  
  
### EventType

EventType represents the type of event to which a BuildTrigger responds.

Enums  
---  
`EVENT_TYPE_UNSPECIFIED` | EVENT_TYPE_UNSPECIFIED event_types are ignored.  
`REPO` | REPO corresponds to the supported VCS integrations.  
`WEBHOOK` | WEBHOOK corresponds to webhook triggers.  
`PUBSUB` | PUBSUB corresponds to pubsub triggers.  
`MANUAL` | MANUAL corresponds to manual-only invoked triggers.  
  
### IncludeBuildLogs

The options of enabling showing build logs on GitHub.

Enums  
---  
`INCLUDE_BUILD_LOGS_UNSPECIFIED` | Build logs will not be shown on GitHub.  
`INCLUDE_BUILD_LOGS_WITH_STATUS` | Build logs will be shown on GitHub.  
  
### RepositoryEventConfig

The configuration of a trigger that creates a build whenever an event from Repo API is received.

JSON representation  
---  
      
    
    {
      "repository": string,
      "repositoryType": enum ([RepositoryType](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.RepositoryType)),
    
      // Union field filter can be only one of the following:
      "pullRequest": {
        object ([PullRequestFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PullRequestFilter))
      },
      "push": {
        object ([PushFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PushFilter))
      }
      // End of list of possible types for union field filter.
    }  
  
Fields  
---  
`repository` |  `string` The resource name of the Repo API resource.  
`repositoryType` |  `enum (`[RepositoryType](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.RepositoryType)`)` Output only. The type of the SCM vendor the repository points to.  
Union field `filter`. The types of filter to trigger a build. `filter` can be only one of the following:  
`pullRequest` |  `object (`[PullRequestFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PullRequestFilter)`)` Filter to match changes in pull requests.  
`push` |  `object (`[PushFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PushFilter)`)` Filter to match changes in refs like branches, tags.  
  
### RepositoryType

All possible SCM repo types from Repo API.

Enums  
---  
`REPOSITORY_TYPE_UNSPECIFIED` | If unspecified, RepositoryType defaults to GITHUB.  
`GITHUB` | The SCM repo is GITHUB.  
`GITHUB_ENTERPRISE` | The SCM repo is GITHUB Enterprise.  
`GITLAB_ENTERPRISE` | The SCM repo is GITLAB Enterprise.  
`BITBUCKET_DATA_CENTER` | The SCM repo is BITBUCKET Data Center.  
`BITBUCKET_CLOUD` | The SCM repo is BITBUCKET Cloud.  
  
### DeveloperConnectEventConfig

The configuration of a trigger that creates a build whenever an event from the DeveloperConnect API is received.

JSON representation  
---  
      
    
    {
      "gitRepositoryLink": string,
      "gitRepositoryLinkType": enum ([GitRepositoryLinkType](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.GitRepositoryLinkType)),
    
      // Union field filter can be only one of the following:
      "pullRequest": {
        object ([PullRequestFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PullRequestFilter))
      },
      "push": {
        object ([PushFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PushFilter))
      }
      // End of list of possible types for union field filter.
    }  
  
Fields  
---  
`gitRepositoryLink` |  `string` Required. The Developer Connect Git repository link, formatted as `projects/*/locations/*/connections/*/gitRepositoryLink/*`.  
`gitRepositoryLinkType` |  `enum (`[GitRepositoryLinkType](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.GitRepositoryLinkType)`)` Output only. The type of DeveloperConnect GitRepositoryLink.  
Union field `filter`. The types of filter to trigger a build. `filter` can be only one of the following:  
`pullRequest` |  `object (`[PullRequestFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PullRequestFilter)`)` Filter to match changes in pull requests.  
`push` |  `object (`[PushFilter](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers#BuildTrigger.PushFilter)`)` Filter to match changes in refs like branches and tags.  
  
### GitRepositoryLinkType

All possible SCM repo types from DeveloperConnect

Enums  
---  
`GIT_REPOSITORY_LINK_TYPE_UNSPECIFIED` | If unspecified, GitRepositoryLinkType defaults to GITHUB.  
`GITHUB` | The SCM repo is GITHUB.  
`GITHUB_ENTERPRISE` | The SCM repo is GITHUB_ENTERPRISE.  
`GITLAB` | The SCM repo is GITLAB.  
`GITLAB_ENTERPRISE` | The SCM repo is GITLAB_ENTERPRISE.  
`BITBUCKET_DATA_CENTER` | The SCM repo is BITBUCKET_DATA_CENTER.  
`BITBUCKET_CLOUD` | The SCM repo is BITBUCKET_CLOUD.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers/create)`

|  Creates a new `BuildTrigger`.  
  
### `[delete](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers/delete)`

|  Deletes a `BuildTrigger` by its project ID and trigger ID.  
  
### `[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers/get)`

|  Returns information about a `BuildTrigger`.  
  
### `[list](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers/list)`

|  Lists existing `BuildTrigger`s.  
  
### `[patch](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers/patch)`

|  Updates a `BuildTrigger` by its project ID and trigger ID.  
  
### `[run](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers/run)`

|  Runs a `BuildTrigger` at a particular source revision.  
  
### `[webhook](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.locations.triggers/webhook)`

|  ReceiveTriggerWebhook [Experimental] is called when the API receives a webhook request targeted at a specific trigger.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
