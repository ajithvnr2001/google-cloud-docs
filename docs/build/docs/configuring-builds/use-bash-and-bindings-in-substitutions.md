---
url: https://docs.cloud.google.com/build/docs/configuring-builds/use-bash-and-bindings-in-substitutions/
title: Using payload bindings and bash parameter expansions in substitutions \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:03.043862+00:00
---

# Using payload bindings and bash parameter expansions in substitutions  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/configuring-builds/use-bash-and-bindings-in-substitutions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Using payload bindings and bash parameter expansions in substitutions Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use payload bindings and apply bash parameter expansions to substitution variables associated with your build trigger. If you are not familiar with how to use substitution variables in your build configuration, see [Substituting variable values](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values).

Cloud Build enables you to store parts of your trigger's event payload as a substitution variable. An event payload is the body of the event that invokes a trigger. Variables associated with a payload are referred to as bindings and are available for builds invoked by both push and pull events. Bindings allow you to access additional data related to your build, such as the language associated with your source code and the author of a pull request.

Cloud Build also enables users to apply bash parameter expansions to substitution variable values. Bash parameter expansions allows you to manipulate strings associated with existing variables. You can manipulate strings by capitalizing letters or replacing a substring.

You can use payload bindings and apply bash parameter expansions when defining or updating a build trigger in the Google Cloud console and in a [Cloud Build config file](https://docs.cloud.google.com/build/docs/build-config). Additionally, you can apply bash parameter expansions when running [manual builds](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually).

## Payload bindings

You can store parts of your trigger's event payload as a substitution variable value. Payload bindings are available as variable values for builds invoked by push and pull events, and can be used to access the JSON payload when your source code is in GitHub repositories or Cloud Source Repositories. To learn more about GitHub event payloads, see [Webhook event payloads](https://docs.github.com/webhooks/event-payloads/). To learn more about the event payloads for Cloud Source Repositories, see [Notifications for Cloud Source Repositories](https://docs.cloud.google.com/source-repositories/docs/pubsub-notifications/).

You can access information from an event payload by using a designated prefix, which represents the root of the event payload. Starting with the prefix, you can use the [JSONPath syntax](https://kubernetes.io/docs/reference/kubectl/jsonpath/) to access the payload and pull data from it. The following payload prefixes are available depending on your event type:

**Prefix** | **Source** | **Description**  
---|---|---  
`push` | GitHub | Enables you to access fields within your JSON payload for push events  
`pull_request` | GitHub | Enables you to access fields within your JSON payload for pull request events  
`issue_comment` | GitHub | Enables you to access fields within your JSON payload for issue comment events associated with a pull request  
`csr` | Cloud Source Repositories | Enables you to access fields within your JSON payload for push events  
**Note:** You may also access payloads using the prefix `body` instead of the listed prefix above for any event. For example, you can use the prefix `body` to access the payload body for a webhook trigger event or Pub/Sub event.

For any event associated with the GitHub app, the built-in variable values `is_collaborator` and `perm_level` are also available. The user's status is checked for push and pull events by the variable values `push.pusher.name`, `pull_request.pull_request.user.login`, and `issue_comment.comment.user.login`. The following table shows you how to include these as variable values for your trigger when your source code is in GitHub:

**Variable Name** | **Variable Value** | **Variable Description**  
---|---|---  
`_PERM_LEVEL` | `$(perm_level)` | Obtains the permission level of the user  
`_IS_COLLABORATOR` | `$(is_collaborator)` | Outputs `true` if the user is a collaborator  
  
You can use the variable values `is_collaborator` and `perm_level` for push events, pull request events, and pull request events gated by a comment. You do not need to precede these variable values with a prefix.

### Creating substitutions using payload bindings

To create a substitution variable that uses a payload binding:

  1. Open the [Triggers](https://console.cloud.google.com/cloud-build/triggers) page.

  2. If you have not created a build trigger, click **Create trigger**. Otherwise, select an existing trigger.

  3. Under **Substitution variables** , click **Add variable**.

  4. Add a name for your **Variable** following the outlined convention described below:

     * Substitutions must begin with an underscore (`_`) and use only uppercase-letters and numbers (respecting the regular expression `[A-Z0-9_]+`). This prevents conflicts with built-in substitutions.

     * The number of parameters is limited to 100 parameters. The length of a parameter key is limited to 100 bytes and the length of a parameter value is limited to 4000 bytes.

To learn more about how to define and use user-defined substitutions, see [Using user-defined substitutions](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_user-defined_substitutions).

  5. Add a **value** for your variable, using a supported prefix.

If your source code is in **GitHub** , you can refer to information in your event payload within substitution variables using payload bindings. To access the JSON payload of a push event, use the prefix `push` or `body`. In the following example, the `push` prefix in the variable value is used as an entrypoint to access information from the JSON payload of your build:

**Variable Name** | **Variable Value** | **Variable Description**  
---|---|---  
`_PUSH_NAME` | `$(push.repository.name)` | Obtains the name of the repository associated with the push event  
`_COMMITS` | `$(push.commits)` | Obtains the array of commit objects describing each pushed commit  
`_OWNER` | `$(push.repository.owner.name)` | Obtains the name of repository owner  
`_URL` | `$(push.repository.html_url)` | Obtains the URL for your GitHub repository  
`_LANGUAGE` | `$(push.repository.language)` | Obtains the language of your source code included in the push  
  
For a list of fields you can access using the `push` prefix, see [`PushEvent`](https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/github-event-types#pushevent).

To access the JSON payload of a pull request event, use the prefix `pull_request` or `body`. In the following example, the `pull_request` prefix in the variable value is used as an entrypoint to access information from the JSON payload of your build:

**Variable Name** | **Variable Value** | **Variable Description**  
---|---|---  
`_PULL_REQUEST_ID` | `$(pull_request.pull_request.id)` | Obtains the ID of the pull request  
`_PULL_REQUEST_TITLE` | `$(pull_request.pull_request.title)` | Obtains the title of the pull request  
`_PULL_REQUEST_BODY` | `$(pull_request.pull_request.body)` | Obtains the body of the pull request  
`_USERNAME` | `$(pull_request.pull_request.user.login)` | Obtains the username of the sender of the pull request  
`_MERGE_TIME` | `$(pull_request.pull_request.merged_at)` | Obtains the time the pull request was merged  
  
For a list of fields you can access using the `pull_request` prefix, see [`PullRequestEvent`](https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/github-event-types#pullrequestevent).

To access the JSON payload of a commit event, use the prefix `commit`. In the following example, the `commit` prefix in the variable value is used as an entrypoint to access information from the JSON payload of your build:

**Variable Name** | **Variable Value** | **Variable Description**  
---|---|---  
`_COMMIT_URL` | `$(commit.url)` | Obtains the URL associated with the commit  
`_COMMIT_USER` | `$(commit.author.login)` | Obtains the username of the author of the commit  
`_COMMIT_MESSAGE` | `$(commit.commit.message)` | Obtains the commit message associated with the commit  
`_COMMIT_DATE` | `$(commit.commit.committer.date)` | Obtains the date associated with the commit  
`_COMMIT_ADDITIONS` | `$(commit.files['*'].additions)` | Obtains the number of additions associated with files in the commit  
  
For a list of fields you can access using the `commit` prefix, see [Get a commit](https://developer.github.com/v3/repos/commits/#get-a-commit).

If you enable **Comment control** for a trigger that is invoked by a pull request, the event that invokes the trigger is instead an `IssueCommentEvent` and the associated prefix is `issue_comment`. In the following examples, the `issue_comment` prefix in the variable value is used as an entrypoint to access information from the JSON payload of your build:

**Variable Name** | **Variable Value** | **Variable Description**  
---|---|---  
`_PULL_REQUEST_ID` | `$(issue_comment.issue.id)` | Obtains the ID of the pull request  
`_PULL_REQUEST_TITLE` | `$(issue_comment.issue.title)` | Obtains the title of the pull request  
`_STATE` | `$(issue_comment.state)` | Obtains the state of the pull request (i.e. open, closed, etc.)  
`_LABELS` | `$(issue_comment.issue.labels)` | Obtains the list of labels associated with the pull request  
`_LABELS_URL` | `$(issue_comment.issue.labels[?(@.description=="Extra attention is needed")].url)` | Obtains the URL associated with the label matching the description  
  
For a list of fields you can access using the `issue_comment` prefix, see [`IssueCommentEvent`](https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/github-event-types#issuecommentevent).

**Note:** If you use `body` as your prefix, this will refer to `issue_comment` and not a [single pull request](https://docs.github.com/en/free-pro-team@latest/rest/reference/pulls#create-a-pull-request) event. To access fields associated with a single pull request, use the prefix `pull_request.`

If your source code is in **Cloud Source Repositories** , you can refer to information in your event payload within substitution variables using payload bindings. To access the JSON payload from a push event, use the prefix `csr` or `body`. In the following example, the `csr` prefix in the variable value is used as an entrypoint to access information from the JSON payload of your build.

**Variable Name** | **Variable Value** | **Variable Description**  
---|---|---  
`_REPO_NAME` | `$(csr.name)` | Obtains the name of your repository  
`_REPO_URL` | `$(csr.url)` | Obtains the URL of your repository  
`_CREATED_REPO` | `$(csr.createRepoEvent)` | Indicates if a user created a repository  
`_REF_EVENT_NAME` | `$(csr.refUpdateEvent.refUpdates['*'].refName)` | The name of the ref (e.g. "refs/heads/primary-branch")  
  
To see additional fields you can access in Cloud Source Repositories, see [Notification data](https://docs.cloud.google.com/source-repositories/docs/pubsub-notifications).


**Note:** You can also use payload bindings in build config file, but they will only be interpreted when your build is invoked by a trigger.

## Bash parameter expansions

You can apply bash parameter expansions to [default variables](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_default_substitutions) and [user-defined variables](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_user-defined_substitutions). Examples of supported operations include substring replacement, string slicing, and capitalization. For example, you may want to replace a substring in a default variable and use the variable as an image tag.

The bash parameter expansions you can specify for substitution variables are as follows:

**Bash expansions** | **Description**  
---|---  
`${var}` | Expands the string value stored in `var`  
`${var^}` | Capitalizes the first character in the string  
`${var^^}` | Capitalizes all characters in the string  
`${var,}` | Lowercases the first character in the string  
`${var,,}` | Lowercases all characters in the string  
`${var:position}` | Removes the first `position` characters from the string  
`${var:position:length}` | Slices the string starting at the numerical value specified in `position` and includes up to the numerical value specified in `length`  
`${var/substring/replacement}` | Replaces the leftmost instance of the value specified in `substring` with the value specified in `replacement`  
`${var//substring/replacement}` | Replaces all instances of the value specified in `substring` with the value specified in `replacement`  
`${var/#substring/replacement}` | Replaces the first instance of the value specified in `substring` with the value specified in `replacement` only if `substring` is a prefix of `var`  
`${var/%substring/replacement}` | Replaces the last instance of the value specified in `substring` with the value specified in `replacement` only if `substring` is a suffix of `var`  
`${#var}` | Retrieves the length of the string  
`${var:-default}` | Evaluates `var` to `default` unless `var` is already defined  
**Note:** `${var:=default}` and `${var=default}` behave similarly to `${var:-default}` and do not assign a value to `var` if it is not already defined.

You can also specify patterns to match for the following bash parameter expansions:

**Bash expansions** | **Description**  
---|---  
`${var#pattern}` | Removes characters from the left side of a string until and including the leftmost instance of the specified `pattern`  
`${var##pattern}` | Removes characters from the left side of a string until and including the rightmost instance of the specified `pattern`  
`${var%pattern}` | Removes characters from the right side of a string until and including the first instance of the specified `pattern`  
`${var%%pattern}` | Removes characters from the right side of a string until and including the leftmost instance of the specified `pattern`  
  
Patterns you can specify include:

**Pattern** | **Description**  
---|---  
`*` | Matches zero or more alphanumeric characters  
`?` | Matches any single alphanumeric character  
`[ccc]` | Matches any single character in `ccc` including ranges between `a-z` or `0-9`  
`[^c]` | Matches any alphanumeric character **not** in `c` including a range of characters where `lo` <= `c` <= `hi`  
`c` | Matches any alphanumeric character `c`  
`\c` | Matches any character `c` including non-alphanumeric characters such as `*`, `?`, or `\`  
  
### Applying bash parameter expansions

To apply a bash parameter expansions to a built-in or user-defined substitution variable:

  1. Open the [Triggers](https://console.cloud.google.com/cloud-build/triggers) page.

  2. If you have not created a build trigger, click **Create trigger**. Otherwise, select an existing trigger.

  3. Under **Substitution variables** , click **Add variable**.

  4. Add a name for your **Variable** following the outlined convention described below:

     * Substitutions must begin with an underscore (`_`) and use only uppercase-letters and numbers (respecting the regular expression `[A-Z0-9_]+`). This prevents conflicts with built-in substitutions.

     * The number of parameters is limited to 100 parameters. The length of a parameter key is limited to 100 bytes and the length of a parameter value is limited to 4000 bytes.

To learn more about how to define and use user-defined substitutions, see [Using user-defined substitutions](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values#using_user-defined_substitutions).

  5. Add a **value** for your variable, applying a [supported bash parameter expansion](https://docs.cloud.google.com/build/docs/configuring-builds/use-bash-and-bindings-in-substitutions#bash_parameter_expansions) to a built-in substitution variable or another user-defined substitution variable.

In the following example, the built-in substitution variable `$BRANCH_NAME` has a default value of `Feature_Secret_Project_#v2`. The following table shows examples of bash parameter expansions you can apply to `$BRANCH_NAME`:

**Variable Name** | **Bash expansion** | **Variable Value** | **Description**  
---|---|---|---  
`_BRANCH_LOWERCASE` | `${$BRANCH_NAME,,}` | `feature_secret_project_#v2` | lowercases all characters in the string  
`_BRANCH_NO_SUFFIX` | `${_BRANCH_LOWERCASE%_\#v2}` | `feature_secret_project` | deletes all characters from the right side of the string matching the specified pattern  
`_BRANCH_NO_PREFIX` | `${_BRANCH_NO_SUFFIX#*_}` | `secret_project` | deletes all characters up until the first underscore  
`_BRANCH_FOR_IMAGE_NAME` | `${_BRANCH_NO_PREFIX//_/-}` | `secret-project` | replaces all underscores with a dash  
`_IMAGE_NAME` | `my-app-${_BRANCH_FOR_IMAGE_NAME}-prod` | `my-app-secret-project-prod` | constructs name for image using `_BRANCH_FOR_IMAGE_NAME` variable defined above  
  
Say `_IMAGE_NAME` is defined in your trigger as the value specified in the table above, `my-app-secret-project-prod`. This value will now override any definition of `_IMAGE_NAME` in your build config file. In the following example, the specified variable value for `_IMAGE_NAME` (`my-app-secret-project-prod`) replaces the default value of `_IMAGE_NAME` (`test-image`) when the build trigger is invoked.

###  YAML 
         
         steps:
          - name: 'gcr.io/cloud-builders/docker'
            args: ['build',
                   '-t',
                   'gcr.io/$PROJECT_ID/${_IMAGE_NAME}',
                   '.']
          substitutions:
              _IMAGE_NAME: test-image #default value
          images: [
              'gcr.io/$PROJECT_ID/${_IMAGE_NAME}'
          ]
          options:
              dynamicSubstitutions: true
         

###  JSON 
         
         {
            'steps': [
              {
                'name': 'gcr.io/cloud-builders/docker',
                'args': [
                  'build',
                  '-t',
                  'gcr.io/$PROJECT_ID/${_IMAGE_NAME}',
                  '.'
                ]
              }
            ],
            'substitutions': {
              '_IMAGE_NAME': 'test-image' #default value
            },
            'images': [
              'gcr.io/$PROJECT_ID/${_IMAGE_NAME}'
            ],
            "options": {
              "dynamic_substitutions": true
            }
          }
         




The `dynamicSubstitutions` field, set to `true` in the above example, allows bash parameter expansions to be interpreted. If your build is invoked by a trigger, the `dynamicSubstitutions` field is always set to `true` and does not need to be specified in your build config file. If your build is invoked manually, you must set the `dynamicSubstitutions` field to `true` for bash parameter expansions to be interpreted when running your build.

## Using bash parameter expansions with payload bindings

You can apply bash parameter expansions to variables associated with payload bindings by either creating a new variable to reference the variable containing your binding or stringing together bindings with bash parameter expansions. The following table lists examples of how you can use bash parameter expansion with payload bindings:

**Variable Name** | **Variable Value** | **Variable Description**  
---|---|---  
`_URL` | `$(push.repository.html_url)` | Obtains the URL of the repository  
`_URL_CAPITAL` | `${_URL^^}` | Uses a bash parameter expansion to capitalize all characters in the URL  
`_APP_NAME` | `my-app-${_URL_CAPITAL}` | Adds a prefix to the capitalized URL of the repository  
`APP_NAME_ID` | `my-app-$(push.repository.html_url)-${_PAYLOAD_ID:0:7}` | Creates an application name that includes the repository URL and first seven characters of the payload ID  
**Note:** Nested operations are not allowed. For example, you cannot nest a payload binding within a bash parameter expansion: `${$(push.repository.html_url)^^}`.

## What's next

  * Learn how to [substitute variable values](https://docs.cloud.google.com/build/docs/configuring-builds/substitute-variable-values).
  * Learn how to [create a basic build configuration file](https://docs.cloud.google.com/build/docs/configuring-builds/create-basic-configuration).
  * Learn how to [create and manage build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).
  * Learn how to [run builds manually](https://docs.cloud.google.com/build/docs/running-builds/start-build-manually).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
