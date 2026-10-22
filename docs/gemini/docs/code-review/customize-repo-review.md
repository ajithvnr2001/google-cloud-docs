---
url: https://docs.cloud.google.com/gemini/docs/code-review/customize-repo-review/
title: Customize Gemini Code Assist behavior in GitHub \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:41.041224+00:00
---

# Customize Gemini Code Assist behavior in GitHub  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/code-review/customize-repo-review/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Customize Gemini Code Assist behavior in GitHub Stay organized with collections  Save and categorize content based on your preferences. 

[Gemini Code Assist on GitHub](https://docs.cloud.google.com/gemini/docs/code-review/review-repo-code) lets you tailor code review behaviors for individual repositories or apply group configurations across multiple repositories.

Gemini Code Assist on GitHub also supports adding a `styleguide.md` file. For more information about this functionality, see [Code review style guide](https://docs.cloud.google.com/gemini/docs/code-review/style-guide).

## Configuration fields

You modify Gemini Code Assist on GitHub behavior by adding a `config.yaml` file to a `.gemini/` folder located in the root of each of your repositories. The `config.yaml` file contains various configurable features that you can enable or disable. For a complete listing of fields, see the `config.yaml` schema.

The following is a list of considerations for specific customizable fields in Gemini Code Assist on GitHub:

  * **`code_review: comment_severity_threshold`** : This field sets the minimum severity for which Gemini Code Assist posts comments. For example, if you have set `code_review: comment_severity_threshold: HIGH`, Gemini Code Assist won't provide pull request comments for issues it considers to be of `LOW` or `MEDIUM` severity, such as minor refactorings. Gemini Code Assist determines the severity of a comment based on the type and significance of the issue under consideration, with violations of your [custom style guide](https://docs.cloud.google.com/gemini/docs/code-review/style-guide) typically meeting or exceeding the severity threshold.

  * **`ignore_patterns`** : This field uses [glob patterns](https://code.visualstudio.com/docs/editor/glob-patterns). When interacting with the repository, Gemini Code Assist ignores files that match any pattern in this list.

  * **`memory_config`** : This field is applicable if you have previously enabled improved response quality for multiple repositories. When you enable improved response quality for multiple repositories, you can set `memory_config: disabled: true` for a specific repository within the grouping, which disables the feature for that repository.




### `config.yaml` schema

The following code snippet is the schema for the `config.yaml` file. It defines all of the possible configuration options and their accepted values:
    
    
    $schema: "http://json-schema.org/draft-07/schema#"
    title: RepoConfig
    description: Configuration for Gemini Code Assist on a repository. All fields are optional and have default values.
    type: object
    properties:
      have_fun:
        type: boolean
        description: Enables fun features such as a poem in the initial pull request summary. Default: false.
      ignore_patterns:
        type: array
        items:
          type: string
        description: A list of glob patterns for files and directories that Gemini Code Assist should ignore. Default: [].
      memory_config:
        type: object
        description: Configuration for persistent memory, which is used to improve responses.
        properties:
          disabled:
            type: boolean
            description: Whether to disable persistent memory for this specific repository. Default: false.
      code_review:
        type: object
        description: Configuration for code reviews. All fields are optional and have default values.
        properties:
          disable:
            type: boolean
            description: Disables Gemini from acting on pull requests. Default: false.
          comment_severity_threshold:
            type: string
            enum:
              - LOW
              - MEDIUM
              - HIGH
              - CRITICAL
            description: The minimum severity of review comments to consider. Default: MEDIUM.
          max_review_comments:
            type: integer
            format: int64
            description: The maximum number of review comments to consider. Use -1 for unlimited. Default: -1.
          pull_request_opened:
            type: object
            description: Configuration for pull request opened events. All fields are optional and have default values.
            properties:
              help:
                type: boolean
                description: Posts a help message on pull request open. Default: false.
              summary:
                type: boolean
                description: Posts a pull request summary on the pull request open. Default: false.
              code_review:
                type: boolean
                description: Posts a code review on pull request open. Default: true.
              include_drafts:
                type: boolean
                description: Enables agent functionality on draft pull requests. Default: true.

### `config.yaml` example

The following code snippet is an example of a `config.yaml` file. In this example, each property is set to the default value used by Gemini Code Assist. You can use this snippet as a template to create your own `config.yaml` file:
    
    
    have_fun: false
    memory_config:
      disabled: false
    code_review:
      disable: false
      comment_severity_threshold: MEDIUM
      max_review_comments: -1
      pull_request_opened:
        help: false
        summary: false
        code_review: true
        include_drafts: true
    ignore_patterns: []
    

## Manage configurations across multiple repositories

You can toggle certain settings for multiple repositories when they are grouped by a [Developer Connect connection](https://docs.cloud.google.com/gemini/docs/code-review/review-repo-code#considerations). These collective settings are managed through the Google Cloud console.

If a repository is managed as part of a group but also has its own `config.yaml`, the repository's `config.yaml` settings override the group settings.

For specific setting behavior and exceptions, review the config.yaml schema.

The following steps show how to control one set of configurations across multiple repositories. These steps assume you have previously [set up Gemini Code Assist on GitHub](https://docs.cloud.google.com/gemini/docs/code-review/set-up-code-assist-github).

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms for Google Cloud](https://cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [Google Cloud launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. In the Google Cloud console, go to the Gemini Code Assist **Agents & Tools** page.

[Go to Agents & Tools](https://console.cloud.google.com/gemini-code-assist/agents-tools)

  2. In the **Agents** section, locate the **Code Assist Source Code Management** card, and click **Advanced**.

The **Edit Code Assist Source Code Management** pane opens.

  3. In the **Connections** table, click the name of the connection that you want to apply a configuration to.

The details page for the connection opens.

  4. In the **Settings** tab, update the settings that you want to change.

**Note:** If you want to enable **Improve response quality** , you shouldn't place your Google Cloud project within a [VPC Service Controls service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).
  5. Click **Save**.




## What's next

  * [Add a style guide](https://docs.cloud.google.com/gemini/docs/code-review/style-guide) for Gemini Code Assist in GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
