---
url: https://docs.cloud.google.com/looker/docs/create-projects/
title: Creating a new LookML project \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:52.877909+00:00
---

# Creating a new LookML project  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/create-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Creating a new LookML project Stay organized with collections  Save and categorize content based on your preferences. 

A project is a collection of LookML files that describe how your database tables are related to each other and how Looker should interpret those tables. You can learn more about projects on the [LookML projects and development model](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#lookml_projects) and [LookML terms and concepts](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#lookml_project) documentation pages. For information about accessing and editing existing projects, see the [Accessing and editing project information](https://docs.cloud.google.com/looker/docs/manage-projects) documentation page.

A LookML project can contain more than one [model file](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files). However, if you want to specify permissions for users around seeing and editing LookML for a specific model file, you might want to create a new project. Although most permissions in Looker apply at the [model level](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_list), there are some permissions that apply to the project level, including `see_lookml`, which lets you view LookML for a project, and `develop`, which lets you edit the LookML.

Looker users with the [`manage_models`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_models) permission can create LookML models on a Looker instance.

## Creating a project

**Caution:** The **New Project** page in Looker that is described in this documentation has been replaced with the [**Create a Model**](https://docs.cloud.google.com/looker/docs/generating-a-model) page. However, you can still access the **New Project** page if you are using a Looker (original) instance and your Looker admin has enabled the [Use Legacy Project Creation Page](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#legacy_project_creation) legacy feature, or through the informational banner at the top of the **Create a Model** page, or from the **Add LookML** button in the [**Pending Projects** section](https://docs.cloud.google.com/looker/docs/manage-projects#viewing_the_listing_for_a_pending_project) of the **Projects** page.

To create a project, perform the following steps:

  1. [Verify that you're in Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#switching_in_and_out_of_development_mode).

  2. Select **Projects** from the **Develop** section of the navigation panel.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-generate-project-mng-a-2216.png)

  3. On the **LookML Projects** page, select **New LookML Project** to select the options for your project.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-new-project-from-db-2112.png)




This action opens the **New Project** page, where you can specify settings for your project, including the project's name and starting point.

Looker can create a project in several ways, and the steps taken depend on the **Starting Point** option that you choose on the **New Project** page. The following sections describe how these starting points work:

  * Automatically generating a model from your database
  * Cloning a public Git repository
  * Creating a blank project



### Automatically generating a model from your database

From the **New Project** page, specify the following options to automatically generate a model from a database.

  1. **Project Name** : Give your project a name. Project names are case-sensitive and only allow alphanumeric characters, `_`, `.`, and `-`. Choose the project name carefully and consider it a permanent ID for the project, since Looker uses the project name in the following ways:

     * To identify the project for API calls that have the `project_id` parameter.
     * To identify the project in the Looker instance's internal database.
     * To identify the project for [local project import](https://docs.cloud.google.com/looker/docs/importing-projects#importing_local_projects).
     * To display the project on the [**LookML Projects** page](https://docs.cloud.google.com/looker/docs/manage-projects).
     * To display the project in the **Develop** section of the [Looker navigation panel](https://docs.cloud.google.com/looker/docs/finding-content).
     * As part of the URL for project files. For example, on a Looker instance with a URL of `example.looker.com`, the project manifest file for the project named `ecommerce` can be found at this URL: `https://example.looker.com/projects/ecommerce/files/manifest.lkml`.
  2. **Starting Point** : Choose **Generate Model from Database Schema**.

  3. **Connection** : From the drop-down menu, select the name of your database connection.

  4. **Build Views From** : Select one of the following options:

     * **All Tables** : The LookML generator creates a view file for each table in your database.
     * **Single Table** : The LookML generator creates a view for one table in your database. If you choose this option, enter the name of the database table.
  5. **Schemas** : To generate files for only one schema in your database, enter the name of the schema in the **Schemas** text field. You can list multiple schemas, separated by commas.

**Note:** For [connections to Databricks databases with Unity Catalog enabled](https://docs.cloud.google.com/looker/docs/db-config-databricks#unity_catalog), Looker can generate models only for the Databricks catalog that is specified in the Looker connection to the Databricks database. If your connection doesn't specify a catalog, Looker can generate models only for your database's default catalog.
  6. **Ignore Prefixes** : To leave table prefixes out of your view file names, enter your database's prefixes in the **Ignore Prefixes** field. This field is case-sensitive. You can list multiple prefixes, separated by commas. For example, your tables are titled `dwh_orders` and `DBS_users`. If you enter `dwh, DBS` in the **Ignore Prefixes** text field, then Looker creates view files named `orders` and `users`.




Finally, click **Create Project** to create a project that contains the generated model.

  * The LookML generator creates one model file for the project as well as a view file for each table in the database (unless otherwise specified). Then, Looker opens the new project in the [Looker IDE](https://docs.cloud.google.com/looker/docs/looker-ide).
  * The LookML generator creates [IDE folders](https://docs.cloud.google.com/looker/docs/ide-folders) for your view and model files. If your database has more than one schema, the LookML generator creates a folder for schemas.



For BigQuery connections, if you [generate a LookML project from your database](https://docs.cloud.google.com/looker/docs/generating-a-model#automatically_generating_a_model_from_your_database), Looker autopopulates field descriptions with the descriptions from your BigQuery column metadata, if any.

The generator also creates an Explore for each database table. To start querying your data, use the **Explore** panel to select the name of an Explore.

### Cloning a public Git repository from the **New Project** page

If you select **Clone Public Git Repository** as the starting point from the **New Project** page, Looker copies the files from a public Git repository into a new LookML project.

Looker supports cloning a public Git repository using the repository's HTTPS web URL.

**Note:** If the public Git repository uses "master" as the name for its main branch, Looker does not support using HTTPS for connecting to the repository. Instead of cloning with HTTPS, you can use the [alternate method](https://docs.cloud.google.com/looker/docs/create-projects#alternative_method_for_cloning_a_public_git_repository) of creating a blank project and then connecting to the public repository using SSH.

To clone an existing public Git repository into a Looker project, follow these steps:

  1. [Verify that you're in Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#switching_in_and_out_of_development_mode).
  2. From the **Develop** section of the Looker navigation panel, select **Projects**.
  3. On the **LookML Projects** page, depending on your instance's configuration, do one of the following:

     * Click the **New LookML Project** button to open the **New Project** page.
     * Click the **New Model** button to open the **Create a Model** page, and then in the information banner on the **Create a Model** page, click the **click here** link to open the **New Project** page.
  4. In the **Project Name** field, give your project a name. Project names are case-sensitive and [can't use spaces or certain special characters](https://docs.cloud.google.com/looker/docs/creating-project-files#before_you_begin_important_file_and_folder_naming_conventions). Choose the project name carefully and consider it a permanent ID for the project, since Looker uses the project name in the following ways:

     * To identify the project for API calls that have the `project_id` parameter.
     * To identify the project in the Looker instance's internal database.
     * To identify the project for [local project import](https://docs.cloud.google.com/looker/docs/importing-projects#importing_local_projects).
     * To display the project on the [**LookML Projects** page](https://docs.cloud.google.com/looker/docs/manage-projects).
     * To display the project in the **Develop** section of the [Looker navigation panel](https://docs.cloud.google.com/looker/docs/finding-content).
     * As part of the URL for project files. For example, on a Looker instance with a URL of `example.looker.com`, the project manifest file for the project named `ecommerce` can be found at this URL: `https://example.looker.com/projects/ecommerce/files/manifest.lkml`.
  5. For the **Starting Point** field, select **Clone Public Git Repository**.

  6. In the **Git Repository URL** field, enter the URL for the public Git repository. Make sure that the URL is in the format `https://github.com/example/my-repository.git`.

  7. Click **Create Project**. Looker clones the repository and opens the Looker IDE to the new LookML project with the project files from the cloned repository.




Once Looker has created your new LookML project, you must set up Git version control by connecting to a Git repository. See the Setting up and testing a Git connection documentation page for the procedures on connecting to Git using either [HTTPS](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#configuring_https_git_authentication) or [SSH](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#connecting_to_git_using_ssh).

Depending on your situation, you may want to set up your Git connection to push changes to your own Git repository, or you may want to push changes back to the original, cloned Git repository:

  * If you want to use the cloned files as a starting point for your own project independent of the public Git repository, set up your project's Git connection to point to your own Git repository and push your changes there.
  * If you want to contribute updates back to the public Git repository that you cloned, and you have a personal access token with read-write access to the public repository, set up your project's Git connection to point to the public Git repository and push your changes there.



After setting up the Git connection to a repository, you can edit the files in the Looker IDE, and then [use version control and deploy changes to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes) as with any standard LookML project.

#### Alternative method for cloning a public Git repository

The easiest way to clone a public Git repository is to use the **New Project** page in Looker.

Alternatively, you can fork the repository and connect it to a blank project in Looker by performing these steps:

  1. Navigate to your Git provider and fork the repository.
  2. In Looker, create a blank project as described in the Creating a blank project section of this page.
  3. Once you create the new blank LookML project, set up the project's Git connection to your Git repository fork by using either [HTTPS](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#configuring_https_git_authentication) or [SSH](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#connecting_to_git_using_ssh).



After setting up the Git connection to your repository fork, you can edit the files in the Looker IDE, and then [use version control and deploy changes to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes) as with any standard LookML project.

### Creating a blank project

If you select **Blank Project** as the starting point from the **New Project** page, Looker creates an empty project so that you can create your LookML files from scratch.

To create a blank project, follow these steps:

  1. [Verify that you're in Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#switching_in_and_out_of_development_mode).
  2. From the **Develop** section of the Looker navigation panel, select **Projects**.
  3. On the **LookML Projects** page, depending on your instance's configuration, do one of the following:

     * Click the **New LookML Project** button to open the **New Project** page.
     * Click the **New Model** button to open the **Create a Model** page, and then in the information banner on the **Create a Model** page, click the **click here** link to open the **New Project** page.
  4. In the **Project Name** field, give your project a name. Project names are case sensitive and [can't use spaces or certain special characters](https://docs.cloud.google.com/looker/docs/creating-project-files#before_you_begin_important_file_and_folder_naming_conventions). Choose the project name carefully and consider it a permanent ID for the project, since Looker uses the project name in the following ways:

     * To identify the project for API calls that have the `project_id` parameter.
     * To identify the project in the Looker instance's internal database.
     * To identify the project for [local project import](https://docs.cloud.google.com/looker/docs/importing-projects#importing_local_projects).
     * To display the project on the [**LookML Projects** page](https://docs.cloud.google.com/looker/docs/manage-projects).
     * To display the project in the **Develop** section of the [Looker navigation panel](https://docs.cloud.google.com/looker/docs/finding-content).
     * As part of the URL for project files. For example, on a Looker instance with a URL of `example.looker.com`, the project manifest file for the project named `ecommerce` can be found at this URL: `https://example.looker.com/projects/ecommerce/files/manifest.lkml`.
  5. For the **Starting Point** field, choose **Blank Project**.

  6. Click **Create Project**. Looker creates the project and opens it in the [Looker IDE](https://docs.cloud.google.com/looker/docs/looker-ide).




## Troubleshooting the "Project already exists" error

When creating a new project in the Looker IDE, you might receive a `Project already exists` error, even if the project is not visible in the Looker UI (including to users with admin permissions). This issue occurs if a user previously created a project with the same name in Development Mode but did not deploy a model or push the changes to production. In Looker, a project in this uncommitted state is visible only to the user who created it.

To resolve this issue, identify the project creator and act as that user to commit and deploy the project or delete it, as follows. You must be a Looker admin or have the [`sudo` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#sudo) to sudo as the project creator.

1 **Identify the project creator** : Run a query in the [System Activity explores](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores) using the project name to identify the user who originally created the project. 1 **Sudo as the creator** : Use the Looker [**Sudo** feature](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#impersonating_users) to impersonate the identified user. 1 **Manage or delete the project** : While logged in as the creator, switch to **Development Mode**. The project is now visible in the IDE. You can configure or deploy the project, or [delete the project](https://docs.cloud.google.com/looker/docs/manage-projects#deleting_a_project) to free up the project name.

## Next steps

After a project is created, you can do the following:

  * [Manually create](https://docs.cloud.google.com/looker/docs/creating-project-files#creating_files) additional new models for your project.
  * [Edit existing LookML files](https://docs.cloud.google.com/looker/docs/looker-ide).
  * [Configure models](https://docs.cloud.google.com/looker/docs/generating-a-model#when_you_need_to_configure_models) for use in production.
  * [Rename the project](https://docs.cloud.google.com/looker/docs/manage-projects#renaming_a_project).
  * [Connect the Looker project to Git](https://docs.cloud.google.com/looker/docs/setting-up-git-connection).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
