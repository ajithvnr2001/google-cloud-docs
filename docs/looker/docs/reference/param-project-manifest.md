---
url: https://docs.cloud.google.com/looker/docs/reference/param-project-manifest/
title: Project manifest parameters \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:16.565011+00:00
---

# Project manifest parameters  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-project-manifest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  Project manifest parameters Stay organized with collections  Save and categorize content based on your preferences. 

Your project may contain a [project manifest file](https://docs.cloud.google.com/looker/docs/other-project-files#project_manifest_files), which is used for project-level settings such as those for specifying other projects to [import into the current project](https://docs.cloud.google.com/looker/docs/importing-projects), defining [LookML constants](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#lookml_constants), specifying [model localization settings](https://docs.cloud.google.com/looker/docs/model-localization), and adding [extensions](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework#adding_an_extension_to_looker) and [custom visualizations](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization) to your project.

> [Model localization](https://docs.cloud.google.com/looker/docs/model-localization) is not currently compatible with [project import](https://docs.cloud.google.com/looker/docs/importing-projects).

Each project can have only one manifest file. The file must be named `manifest.lkml` and be located at the root level of your project's [directory structure](https://docs.cloud.google.com/looker/docs/ide-folders). Also, Looker does not support an empty project manifest file. If your manifest file is empty, [delete the file](https://docs.cloud.google.com/looker/docs/creating-project-files#deleting_files_and_folders).

This page links to the project manifest-level LookML parameters.

## Example usage

Hover over a parameter name to see a quick description. Click a parameter to visit its reference page.

When a parameter can be set to one of several specific options, the default value is listed first.
    
    
    ## STRUCTURAL PARAMETERS
    [project_name](https://docs.cloud.google.com/looker/docs/reference/param-manifest-project-name "Name of the current project"): "Current Project Name"
    [new_lookml_runtime](https://docs.cloud.google.com/looker/docs/reference/param-manifest-new-lookml-runtime "Enables or disables New LookML Runtime for a LookML project"): yes 
    [local_dependency](https://docs.cloud.google.com/looker/docs/reference/param-manifest-local-dependency "Makes another project on the current instance available to include files from"): {
      [project](https://docs.cloud.google.com/looker/docs/reference/param-manifest-local-dependency "Specifies a project to import files from"): "project_name"
      [override_constant](https://docs.cloud.google.com/looker/docs/reference/param-manifest-local-dependency "Overrides the value of an imported constant"): constant_name {
        [value](https://docs.cloud.google.com/looker/docs/reference/param-manifest-local-dependency "Specifies a new value for an imported constant"): "string value" 
      }
    }
    ## Possibly more local_dependency statements
    
    [remote_dependency](https://docs.cloud.google.com/looker/docs/reference/param-manifest-remote-dependency "Makes another project on a public, remote site available to include files from"): remote_project_name {
      [url](https://docs.cloud.google.com/looker/docs/reference/param-manifest-remote-dependency "The URL of the Git repository to include files from"): "remote_project_url"
      [ref](https://docs.cloud.google.com/looker/docs/reference/param-manifest-remote-dependency "The SHA key of the Git commit to includes files from"): "remote_project_ref"
      [override_constant](https://docs.cloud.google.com/looker/docs/reference/param-manifest-remote-dependency "Overrides the value of an imported constant"): constant_name {
        [value](https://docs.cloud.google.com/looker/docs/reference/param-manifest-remote-dependency "Specifies a new value for an imported constant"): "string value" 
      }
    }
    # Possibly more remote_dependency statements
    
    [constant](https://docs.cloud.google.com/looker/docs/reference/param-manifest-constant "Defines a constant that can be used throughout a LookML project"): constant_name {
      [value](https://docs.cloud.google.com/looker/docs/reference/param-manifest-constant "Specifies a string value for a LookML constant"): "string value"
      [export](https://docs.cloud.google.com/looker/docs/reference/param-manifest-constant "Specifies whether importing projects can override the value of the constant"): none | override_optional | override_required
    }
    # Possibly more constant statements
    
    ## LOCALIZATION PARAMETERS
    [localization_settings](https://docs.cloud.google.com/looker/docs/reference/param-manifest-localization-settings "Sets the behavior for localization of your model"): {
      [localization_level](https://docs.cloud.google.com/looker/docs/reference/param-manifest-localization-settings "Specifies whether strings with no translation are allowed in your model"): strict | permissive
      [default_locale](https://docs.cloud.google.com/looker/docs/reference/param-manifest-localization-settings "Specifies the default locale used as your model's default for translating strings"): locale_name
    }
    
    ## EXTENSION FRAMEWORK PARAMETERS
    [application](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application "Defines an application for the Looker extension framework"): application_name {
      [label](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#label "Specifies the name of the application that is displayed to the user"): "Application Label" 
      [url](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#url "Provides the URL of the application"): "application_url" 
      [file](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#file "Provides the path to a JavaScript file that defines the application"): "application_file_path" 
      [mount_points](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#mount_points "Specifies the location in the Looker UI where the application will be listed and where the application will retrieve data"): {
        # Desired mount points (described on [application](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#entitlements) page)
      }
      [entitlements](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#entitlements "Specifies the entitlements to control access to the extension features of the application"): {
        # Desired entitlements (described on [application](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#entitlements) page)
      }
    }
    ## Possibly more application statements
    
    ## CUSTOM VISUALIZATION PARAMETERS
    [visualization](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization "Defines a custom visualization for your Looker project"):{
      [id](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#id "Specifies a unique identifier for the visualization"): "unique-id" 
      [label](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#label "Specifies the name of the visualization that is displayed to the user"): "Visualization Label" 
      [url](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#url "Provides the URL to the visualization's JavaScript file"): "visualization_url" 
      [sri_hash](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#sri_hash "Specifies the subresource integrity hash for the visualization"): "SRI hash" 
      [dependencies](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#dependencies "Provides a comma-separated list of dependency URLs required to load the visualization"): ["dependency_url_1","dependency_url_2"]
      [file](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#file "Specifies the path to a JavaScript file that defines the visualization"): "visualization_file_path" 
    }
    ## Possibly more visualization statements
    

## Parameter definitions

Parameter Name | Description  
---|---  
Structural Parameters  
[`project_name`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-project-name) | Specifies the name of the current project.  
[`new_lookml_runtime`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-new-lookml-runtime) | Enables or disables New LookML Runtime for a LookML project.  
[`local_dependency`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-local-dependency) | Specifies that this project depends on another project. This parameter has the `project` and `override_constant`subparameters.  
[`project`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-local-dependency) | Specifies a project that contains files that you want to include.  
[`remote_dependency`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-remote-dependency) | Specifies one or more remote projects that contain files that you want to include. This parameter has `url` and `ref` subparameters, as well as the subparameter `override_constant`.  
[`constant`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-constant) | Defines a LookML constant that can be used throughout your project. This parameter has the subparameters `value` and `export`.  
Localization Parameters  
[`localization_settings`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-localization-settings) | Specifies the localization information for your model. This parameter has `default_locale` and `localization_level` subparameters.  
[`localization_level`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-localization-settings) | Specifies whether strings with no translation are allowed in your model.  
[`default_locale`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-localization-settings) | Specifies the locale that will be used as your model's default for translating strings.  
Extension Framework Parameters  
[`application`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application) | Defines an application for the Looker [extension framework](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework).  
[`label`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#label) | Specifies the name of the application that is displayed to the user.  
[`url`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#url) | Provides the URL of the application.  
[`file`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#file) | Provides the path to a JavaScript file (with a `.js` extension) that defines the application. The path is relative to the project root.  
[`entitlements`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#entitlements) | Specifies the entitlements to control access to the extension features of the application. This parameter has many subparameters listed on the [`application`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-application#entitlements) parameter page.  
Custom Visualization Parameters  
[`visualization`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization) | Defines a custom visualization for your Looker project.  
[`id`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#id) | Specifies a unique identifier for the visualization.  
[`label`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#label) | Specifies the name of the visualization that is displayed to the user.  
[`url`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#url) | Provides the URL to the visualization's JavaScript file.  
[`sri_hash`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#sri_hash) | Specifies the subresource integrity hash for the visualization.  
[`dependencies`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#dependencies) | Provides a comma-separated list of dependency URLs required to load the visualization.  
[`file`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization#file) | Specifies the path to a JavaScript file that defines the visualization.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
