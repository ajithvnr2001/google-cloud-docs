---
url: https://docs.cloud.google.com/looker/docs/manage-projects/
title: Accessing and editing project information \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:47.871714+00:00
---

# Accessing and editing project information  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/manage-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Accessing and editing project information Stay organized with collections  Save and categorize content based on your preferences. 

The **LookML Projects** page provides a list of all the LookML projects on the Looker instance and shows all the models in each project.

To access the **LookML projects** page, perform the following steps:

  1. Open the **Develop** panel by selecting the **Develop** option in the [navigation panel](https://docs.cloud.google.com/looker/docs/finding-content).
  2. In the **Develop** panel, select **Projects**.



## Creating projects

This documentation page assumes that you have already created a project using one of the following methods:

  * As part of model generation through the [**Create a Model** page](https://docs.cloud.google.com/looker/docs/generating-a-model) in Looker
  * As a blank project through the [**Create a Model** page](https://docs.cloud.google.com/looker/docs/generating-a-model#blank-project) in Looker
  * By using the [legacy process for creating a project](https://docs.cloud.google.com/looker/docs/create-projects)



## Viewing existing projects and their models

To view a list of existing projects, navigate to the **LookML projects** page.

In Production Mode, the **LookML projects** page lists projects that have been generated and pushed to production. In Development Mode, the page lists projects that you have pulled from production or that you have generated yourself in Development Mode. The **LookML Projects** page includes the following tabs:

  * **Models and Projects** : Projects listed in the **Models and Projects** tab have been created and may include [generated model and view files](https://docs.cloud.google.com/looker/docs/generating-a-model). If you're a Looker admin, or if you have [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission for at least one model in a project, you can see the project in the **Develop** panel and in the **Models and Projects** tab.
  * **Pending Projects** : Projects listed in the **Pending Projects** tab are projects where the Looker admin has [configured the allowed connections for a model](https://docs.cloud.google.com/looker/docs/generating-a-model#configuring_planned_models) but the Looker developers have not yet [added the LookML](https://docs.cloud.google.com/looker/docs/create-projects). If you have [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission, you can see these projects.
  * **Marketplace Projects** : Projects listed in the **Marketplace Projects** tab were created when an application, a block, or a plug-in was installed using the [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace).

**Note:** To see a project, you must have either the [`manage_models`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage-models) permission, or the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission for at least one model in the project. If you have the [`manage_models`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage-models) permission, or have the [`manage_project_models`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage-project-models) permission for at least one model in the project you can add or edit the configuration for any model that is associated with a listed project.

For information on specifying a new project or a new model for an existing project, see the [**Generating a Model**](https://docs.cloud.google.com/looker/docs/generating-a-model) documentation page.

### Viewing the listing for a project

The **LookML Projects** page displays the following elements for each project:

  * **Project** column: The name of the project. Each project may have one or more models listed next to it. Select the project name to navigate to the LookML for that project.
  * **Models** column: The set of LookML model files for the given project. If your Development Mode environment differs from production, this list can change between Development Mode and Production Mode. For example, you might have created a new model in Development Mode that you have not yet pushed to production.
  * Configuration issues column: If there is a problem with a model, the model shows a status that indicates the problem with the configuration.
  * **Configure** button: If the **Configure** button is available for a project, you can add or edit the model configuration for that project.



If there is a problem with a model, the model shows a status that indicates the problem with the configuration.

Issue | Explanation  
---|---  
LookML model file doesn't exist yet | You see this issue if someone configured a model on this page but has not yet created a corresponding LookML file for it.  
Configuration required for use | You see this issue if someone created a new LookML model file in an existing project, but has not configured it on this page yet.  
Connection 'x' does not exist | The [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) declared in the model file does not exist (such as if someone misspelled it or has not created it yet).  
Model 'x' is not allowed to use connection 'y' | The [`connection`](https://docs.cloud.google.com/looker/docs/reference/param-model-connection) declared in the model file is not permitted according to the configuration on this page.  
A model named 'x' is already configured in project 'y' | Model names must be unique within your Looker instance, even if they are in different projects.  
  
### Viewing the listing for a Marketplace project

The **Marketplace Projects** tab on the **LookML Projects** page lists projects that were created during the [installation of a Marketplace application, block, or plug-in](https://docs.cloud.google.com/looker/docs/marketplace). The listing for each Marketplace project includes the following elements:

  * **Listing** : A link to the listing for the application, block, or plug-in in the [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace).
  * **Project** : The name of the project. You can click the name of the project to view or edit its LookML.
  * **View LookML** or **Edit LookML** button: You can navigate to a Marketplace project by selecting the **View LookML** button for a Marketplace block's read-only core project, or the **Edit LookML** for its config project, the latter of which can be customized. For more information on customizing Marketplace blocks, see the [Customizing Looker Marketplace Blocks](https://docs.cloud.google.com/looker/docs/marketplace-customize-blocks) documentation page.
  * **Models** : The set of LookML model files for the given project.
  * **Configure** button: If the **Configure** button is available next to the project's listing, then you can add or edit the project's model configuration.



### Viewing the listing for a pending project

The **Pending Projects** tab contains projects and models that are [configured](https://docs.cloud.google.com/looker/docs/generating-a-model#configuring_planned_models) but that don't yet have LookML [generated](https://docs.cloud.google.com/looker/docs/create-projects#automatically_generating_a_model_from_your_database) or [manually defined](https://docs.cloud.google.com/looker/docs/creating-project-files#creating_files).

Configuring models before the project exists is useful if you have developers who have not been given either the [`manage_models`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage-models) or the [`manage_project_models`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_project_models) permission. Because the model has already been configured, those developers can run queries as soon as they create the project and that model. When the project is generated, the listing for that project moves to the **Models and Projects** tab of the **LookML Projects** page.

The **Pending Projects** tab includes the following elements:

  * **Project** column: This section lists projects that are configured but not yet generated. The project name in this field is the intended name of the project. Select the project name to display the **New Project** page where you can generate that project. You must be in Development Mode to reach the **New Project** page.
  * **Models** column: The model name that was specified when creating the model configuration.
  * Allowed connections column: The column to the right of the model name shows the connections that were allowed for this model when the model configuration was created.
  * **Configure** button: The **Configuration** button lets you change the project name and the connections that are permitted for this model.
  * **Add LookML** button: The **Add LookML** button opens the [**New Project**](https://docs.cloud.google.com/looker/docs/create-projects) page for that project, where you can [automatically generate LookML](https://docs.cloud.google.com/looker/docs/create-projects#automatically_generating_a_model_from_your_database) that is based on a set of tables in your database.



### Adding and editing model configurations

If the **Configure** button is available next to an existing project's listing, you can add or edit the project's model configuration.

If the model does not have a configuration, when you click **Configure** , Looker displays the **Configure a Model** window. In the **Configure a Model** window, you can specify the model name, the project name, and the connections that are available to the model.

The list of connections includes only connections that can be used with the model's project. Connections that are configured for use across all projects have the label `(Instance wide)`.

You can also click the **Configure New Model** button at the top of the **Projects** page to open the **Configure a Model** window. In this scenario, you can use the **Configure a Model** window to create and configure a new model. The new model won't have any LookML but it will be associated with a connection. To complete this process, enter a new name for the model in the **Model** field and complete the **Project** field with a new name or select the same name as the model, select the connections, and click **Save**. Later, you or another Looker developer can add LookML to the new project to define the model.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-configure-a-model-2316.png)

If the model has a configuration, when you click **Configure** , Looker displays the **Edit Model Configuration** window. In the **Edit Model Configuration** window, you can change the connections that are available to the model.

![](https://docs.cloud.google.com/static/looker/docs/images/develop-edit-model-config-2316.png)

When you edit the configuration for a model, you can view the model name but not rename it. Models are named according to the filenames that you use when you [edit the model files in the Looker IDE](https://docs.cloud.google.com/looker/docs/ide-folders).

In the **Project** field, you can specify that the model should be associated with a different project. For example, if you created a new project including a model with the same name, you can transition the model configuration to be associated with the new project's model.

In the **Allowed Connections** field, you can limit the model to use a list of specific connections, or you can allow the model to use any connection (all current and future connections).

## Renaming a project

When a Looker admin [creates a LookML project](https://docs.cloud.google.com/looker/docs/create-projects), the admin provides a project name. The project name should be considered a permanent ID for the project, since Looker uses the project name in the following ways:

  * To identify the project for API calls that have `project_id` as parameter.
  * To identify the project in the Looker instance's internal database.
  * To identify the project for [local project import](https://docs.cloud.google.com/looker/docs/importing-projects#importing_local_projects).
  * To display the project on the [**LookML Projects** page](https://docs.cloud.google.com/looker/docs/manage-projects).
  * To display the project in the **Develop** section of the [Looker navigation panel](https://docs.cloud.google.com/looker/docs/finding-content).
  * As part of the URL for project files. For example, on a Looker instance with a URL of `example.looker.com`, the project manifest file for the project named `ecommerce` can be found at this URL: `https://example.looker.com/projects/ecommerce/files/manifest.lkml`.



If you have the Looker [`manage_models`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_models) permission, you can change a LookML project's name in the project's [**Project Configuration** page](https://docs.cloud.google.com/looker/docs/git-options#configuration). Looker developers who are not admins can view the **Project Configuration** page but cannot change the options on the page.

**Warning:** If you rename a LookML project, you will need to do the following: 

  * Update the [`local_dependency`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-local-dependency) parameter in the LookML manifest file of any LookML projects that use local project import to import the renamed project.
  * Update any web apps with API calls that use the `project_id` parameter to refer to the project.
  * Update the [`project_name`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-project-name) parameter in the LookML manifest file of the renamed LookML project, if the project has a manifest file.
  * Update any browser bookmarks or saved URLs, if you or any of your LookML developers rely on URLs to access the renamed project's LookML files.



To rename a project, perform the following steps:

  1. Verify that you have [Development Mode turned on](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#switching_in_and_out_of_development_mode).
  2. [Navigate to your project](https://docs.cloud.google.com/looker/docs/accessing-project-files) in the Looker IDE.
  3. In your project, click **Settings** tune in the IDE navigation bar to open the project settings panel.
  4. Select **Configuration** in the project settings panel.
  5. Use the **Name** field under **Project Configuration** to edit the name of your project.
  6. In the **Project Configuration** page, click **Save Project Configuration** to save the new project name.



## Deleting a project

If you're a Looker admin, you can delete an existing project with the project's [project settings](https://docs.cloud.google.com/looker/docs/git-options#project_settings). To see the project settings, [open your project](https://docs.cloud.google.com/looker/docs/accessing-project-files) and click **Settings** tune in the IDE navigation bar.

**Important:** Selecting the **Delete Project** button removes all LookML from the project, in all development and production environments across your Looker instance. Be certain that you want to delete a project before selecting this button. Once you delete a project, the deletion operation cannot be reversed, and it's difficult and laborious to recover a deleted project.

A deleted project no longer appears on the **Models and Projects** tab of the **LookML Projects** page, but _still appears_ on the **Pending Projects** tab.

To remove the project configuration, which removes the project from your development environment completely:

  1. [Navigate to your project](https://docs.cloud.google.com/looker/docs/accessing-project-files) in the Looker IDE.
  2. In your project, click **Settings** tune in the IDE navigation bar to open the project settings panel.
  3. In the project settings panel, choose **Configuration** to see the project configuration.
  4. Under **Project Configuration** , select **Delete Project**.
  5. In the **Delete Project** window, verify the warnings and the unsynced changes that are lost if the project is deleted.
  6. If you're sure that the project should be deleted, type the project's name in the field. To cancel the operation and navigate back to your project, use your browser's **Back** button.
  7. Click the **Permanently Delete <project name>** button.



### Troubleshooting bare repository remnants

When you delete a LookML project that is configured with a [bare Git repository](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#configuring_a_bare_git_repository) through the Looker UI, or when you move it to a remote repository, the underlying bare repository folder isn't completely deleted from the Looker instance's file system.

If you attempt to recreate the project with the same name, you may encounter the following error:

`Error Creating Bare Repository. Error: /looker_data/modelshare/bare_models/[project-name].git already exists.`

To resolve this issue and completely remove the stale bare repository remnants, try the following solutions:

  * **For Looker 26.0 and later versions** : [Delete your local developer copy](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#delete-dev-copy) of the project's Git repository.
  * **Use the Looker API** : If the feature to delete the developer copy is unavailable or you have lost access to the deleted project, use the [Looker API](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest) to clean up the remnants.
  * **Contact Google Cloud Support** : If you are using Looker (Google Cloud core) and the API deletion attempt fails, contact Google Cloud Support so they can request that the backend production team manually remove the stale bare Git repository from the file system.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
