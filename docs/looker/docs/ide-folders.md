---
url: https://docs.cloud.google.com/looker/docs/ide-folders/
title: Working with the IDE file browser \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:43.512874+00:00
---

# Working with the IDE file browser  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/ide-folders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Working with the IDE file browser Stay organized with collections  Save and categorize content based on your preferences. 

Organize your Looker project files more effectively by using folders in the Looker IDE. Folders prevent a flat, alphabetically sorted file structure, making it easier to manage and navigate complex projects. Access the Looker IDE through the Looker **Develop** menu. Folders are shown in the left navigation pane of the IDE. For more details and other options for accessing project files, see [Accessing project files](https://docs.cloud.google.com/looker/docs/accessing-project-files).

![Looker IDE with the file browser showing folders in an example project.](https://docs.cloud.google.com/static/looker/docs/images/ide-file-browser-icon-2414.png)

If your Looker project isn't organized into folders, your project will have a flat file structure, with files listed alphabetically in the **File Browser** panel. See Organizing an existing project with IDE folders for information on updating your project to use IDE folders.

The Looker IDE persists your open file and the expanded or collapsed status of the **File Browser** panel. You can reset the persistence in the [**IDE Settings**](https://docs.cloud.google.com/looker/docs/looker-ide#reset-layout).

You can select the icons in the toolbar at the top of the **File Browser** panel to collapse all folders, [move](https://docs.cloud.google.com/looker/docs/creating-project-files#moving_files_and_folders_in_bulk) and [delete](https://docs.cloud.google.com/looker/docs/creating-project-files#deleting_files_and_folders_in_bulk) files and folders, [search for a project file](https://docs.cloud.google.com/looker/docs/accessing-project-files#searching_for_and_jumping_to_lookml_objects_or_project_files), or create [new folders](https://docs.cloud.google.com/looker/docs/creating-project-files#creating_folders) and [new files](https://docs.cloud.google.com/looker/docs/creating-project-files#creating_files).

![](https://docs.cloud.google.com/static/looker/docs/images/ide-folders-search-collapse-icons-2104.png)

## Imported projects folder

If you [import a project](https://docs.cloud.google.com/looker/docs/importing-projects), the Looker IDE automatically creates an `imported_projects` folder. Files from both [local projects](https://docs.cloud.google.com/looker/docs/importing-projects#specifying_local_projects) and [remote projects](https://docs.cloud.google.com/looker/docs/importing-projects#specifying_remote_projects) are listed in the `imported_projects` folder. Select an imported project file from the list of files in the `imported_projects` to view that file's contents.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-import-files-2104.png)

Because they cannot be edited, imported project files are not visible when you are bulk-editing files in the IDE to [move](https://docs.cloud.google.com/looker/docs/creating-project-files#moving_files_and_folders_in_bulk) or [delete](https://docs.cloud.google.com/looker/docs/creating-project-files#moving_files_and_folders_in_bulk) those files.

## Organizing an existing project with IDE folders

If your project previously had the legacy flat file structure or if you want to reorganize the files in a folder, you can choose to keep this structure; but if you choose to organize your project files into folders, we strongly recommend that you make the following preparations:

  * Plan the file structure ahead of time with all developers.
  * Ensure that all your Looker developers have [deployed all their updates to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production). If a developer has undeployed changes, their branch(es) will reflect the file structure that existed when they last [pulled from production](https://docs.cloud.google.com/looker/docs/git-command-reference#pull_prod). If the project had a flat file structure at that time, the developer's version of the file will be pushed to production in its original location, so you will end up with two copies of the file. In addition, if a developer has undeployed changes during the migration to folders, that developer will face a merge conflict when they pull from production after the migration.
  * Enact a temporary code freeze with all your developers until the project has been fully migrated to the new directory structure.
  * Assign a single developer to move the files. The following procedure assumes a single developer will be migrating the project to IDE folders. If you need to have multiple developers move files, divide the task among the developers to avoid merge conflicts. If you do encounter merge conflicts, see the [Using version control and deploying](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#resolving_merge_conflicts) documentation page for information on resolving them.

**Note:** Be aware that when you move a file in Git, you are effectively deleting the file and creating a new file with a new path. This means that the Git history for the file will be empty, because Git will consider it a new file. To see the file's Git history before it was moved, use your Git interface to navigate to the file in its original location and view the Git history from there.

Once all your developers have pushed and committed their changes and paused all work on the project, you can then migrate the project to its new directory structure.

Assign a single developer to do all the following steps:

  1. Verify that all updates on all development branches have been [deployed to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production). This includes the development branches of the developer performing the migration to IDE folders.
  2. Verify that all other developers have stopped making changes to the project.
  3. [Pull from production](https://docs.cloud.google.com/looker/docs/git-command-reference#pull_prod).
  4. [Create the project's folders](https://docs.cloud.google.com/looker/docs/creating-project-files#creating_folders).
  5. Move the project files into the folders, either [one file at a time](https://docs.cloud.google.com/looker/docs/creating-project-files#moving_items_in_a_foldered_project) or [using bulk edit](https://docs.cloud.google.com/looker/docs/creating-project-files#moving_files_and_folders_in_bulk).
  6. [Validate the project's LookML](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_lookml). It is expected that you will have multiple LookML errors and warnings, since the `include` and `map_layer` statements use references to file locations that likely will have been moved during this procedure.
  7. Update any `include` and `map_layer` statements in your project to match the file's new path. In addition, you may see LookML validation errors for referenced objects that can no longer be found because their file paths have changed. For more information, see the documentation on [using `include` with IDE folders](https://docs.cloud.google.com/looker/docs/reference/param-model-include#using_include_with_ide_folders) and on [using `map_layer` with IDE folders](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer#using_map_layer_with_ide_folders). **Tip:** You can use [wildcards](https://docs.cloud.google.com/looker/docs/reference/param-model-include#wildcard_examples) to create a temporary fix for LookML validation warnings and errors resulting from `include` statements. Using view files as an example, you can specify `include: "/**/*.view"` to include all files in all your project folders. This will prevent LookML validation problems while you continue developing. However, this is not a recommended solution for the long term, since including more files than are needed can [affect performance](https://docs.cloud.google.com/looker/docs/reference/param-model-include#including_all_view_files_can_affect_performance).

  8. [Commit the changes](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#committing_changes).

  9. [Deploy the updates to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production).

  10. Inform the other Looker developers that they can now [pull the updates from production](https://docs.cloud.google.com/looker/docs/git-command-reference#pull_prod) and resume developing in the project.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
