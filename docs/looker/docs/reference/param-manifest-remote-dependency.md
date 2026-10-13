---
url: https://docs.cloud.google.com/looker/docs/reference/param-manifest-remote-dependency/
title: remote_dependency \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:16.615277+00:00
---

# remote_dependency  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-manifest-remote-dependency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  remote_dependency Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    remote_dependency:  public_project {
      url:  "https://github.com/llooker/google_ga360"
      ref:  "07a20007b6876d349ccbcacccdc400f668fd8147f1"
      override_constant: constant_name {
        value: "string"
      }
    }
    

Hierarchy [Manifest File](https://docs.cloud.google.com/looker/docs/reference/param-project-manifest) `remote_dependency` |  Default Value None Accepts

  * A `url` subparameter that includes the URL of the Git repository 
  * A `ref` subparameter that specifies a Git branch, a Git release tag, or the SHA of a commit in the Git repository 
  * An `override_constant` subparameter, which is used to override the value of a constant imported from another project 

  
---|---  
  
## Definition

The `remote_dependency` parameter provides the details of an external Git repository containing a LookML project that has files that you want to use in this project. You can include multiple `remote_dependency` statements in the manifest file to import multiple projects.

The `remote_dependency` parameter goes in your project's manifest file. If your project doesn't have one, you can [create a manifest file](https://docs.cloud.google.com/looker/docs/importing-projects#creating_a_project_manifest_file).

The `remote_dependency` parameter takes a name, which can be anything you like. This name is what you use in `include` statements to [reference the imported files in LookML projects](https://docs.cloud.google.com/looker/docs/importing-projects#include_files_from_an_imported_project). The name is also used as the folder name under the [`imported_projects` folder of the Looker IDE](https://docs.cloud.google.com/looker/docs/ide-folders#imported_projects_folder).

In addition, the `remote_dependency` parameter has the following subparameters:

  * `url`
  * `ref`
  * `override_constant`



### `url`

The `url` subparameter specifies the address of the external Git repository. Use the main URL of the repository. For example, using HTTPS:
    
    
    url: "https://github.com/llooker/google_ga360"
    

Or using SSH:
    
    
    url: "git@github.com:llooker/google_ga360.git"
    

### `ref`

The `ref` subparameter specifies a Git branch, a Git release tag, or a commit SHA of the remote project's Git repository that Looker should bring into your Looker project:

  * **Git branch** : You can specify a Git branch if you want Looker to automatically detect new commits for that branch from the remote project. For more information, see the [Importing files from other projects](https://docs.cloud.google.com/looker/docs/importing-projects#autodetect) documentation page.
  * **Git release tag** : You can specify a Git release tag if you want Looker to automatically detect new commits for that tag from the remote project. For more information, see the [Importing files from other projects](https://docs.cloud.google.com/looker/docs/importing-projects#autodetect) documentation page.
  * **Git commit SHA** : You can specify a commit SHA if you want to have static versioning, so that changes in the imported project won't be automatically reflected in your project. Typically, this would be the most recent commit, but it is not required to be. You can find commit SHAs anywhere you can browse the commit history. Git service providers usually make the SHA clearly visible and copyable. This is a good option for [Looker Blocks](https://docs.cloud.google.com/looker/docs/blocks).



Here is an example remote dependency that specifies a commit SHA from the remote Git project:
    
    
    remote_dependency: ga_360 {
      url: "https://github.com/llooker/google_ga360"
      ref: "f99720c597f524d0756b8194990342efa11b3813"
      }
    

Here is an example remote dependency that specifies the main branch on the remote Git project:
    
    
    remote_dependency: ga_360 {
      url: "https://github.com/llooker/google_ga360"
      ref: "main"
    }
    

Regardless of the type of `ref` you specify, when you add a `remote_dependency` to your project and [validate your LookML](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_changes), the IDE will display the **Update Dependencies** button. Click the button to bring in the remote project files. If this is the first remote project that you added to your project, updating dependencies will also prompt Looker to create a [manifest lock file](https://docs.cloud.google.com/looker/docs/other-project-files#manifest_lock_files). Looker uses the manifest lock file to track the version of the remote project(s). See the [Automatically detecting new versions of a remote project](https://docs.cloud.google.com/looker/docs/importing-projects#autodetect) section of the [Importing files from other projects](https://docs.cloud.google.com/looker/docs/importing-projects) documentation page for more information.

### `override_constant`

The `override_constant` parameter lets you override the value of a constant that was defined in an imported project.

> The `override_constant` parameter can also be used with the [`local_dependency`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-local-dependency) parameter for local project import.

When [importing files from one project into another](https://docs.cloud.google.com/looker/docs/importing-projects), you can override the values of [constants](https://docs.cloud.google.com/looker/docs/reference/param-manifest-constant) defined in the imported project's manifest file. When you override a constant's value, imported files that reference that constant will use the new value provided in the importing project.

When the `export` parameter is set to `override_required` or `override_optional` for a constant defined in the imported project, the `override_constant` subparameter of `local_dependency` can be used to provide a new value for that constant. For example, suppose you have a constant `connection` defined in the imported project's manifest file:
    
    
    constant: connection {
      value: "imported_project_connection"
      export: override_required
    }
    
    

In this example, because the `export` parameter is set to `override_required`, its value must be overridden in the importing project's manifest file:
    
    
    project_name: "importing_project"
    
    remote_dependency: public_project {
      url: "https://github.com/llooker/project"
      ref: "07a20007b6876d349ccbcacccdc400f668fd8147f1"
      override_constant: connection {
        value: "importing_project_connection"
      }
    }
    

See the [Importing files from other projects](https://docs.cloud.google.com/looker/docs/importing-projects#passing_constants_between_projects) documentation page for more information and another example of overriding constants in importing projects.

## Example

In a manifest file, add the "Google GA 360" Git repository as a source to import files from:
    
    
    project_name: "thelook"
    
    remote_dependency: ga_360 {
      url: "https://github.com/llooker/google_ga360"
      ref: "6a95679c92efa56243c17fb4d66c820cd4a8db03"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
