---
url: https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes/
title: Using version control and deploying \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:41.360510+00:00
---

# Using version control and deploying  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Using version control and deploying Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page assumes that your project has already been set up for version control. If you see a **Configure Git** button instead of the choices described here, you need to first [set up Git for your project](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#integrating_looker_with_git).

Looker uses Git to record changes and manage file versions. Each LookML project corresponds to a Git repository, and each developer branch correlates to a Git branch.

Looker can be configured to work with many Git providers, such as GitHub, GitLab, and Bitbucket. See the [Setting up and testing a Git connection](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#integrating_looker_with_git) documentation page for information on setting up Git for your Looker project.

## Working with Git branches

One of the main benefits of Git is that a Looker developer can work in a _branch_ , an isolated version of a file repository. You can develop and test without affecting other users. As a developer in Looker, you're using a Git branch whenever you're in [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode).

Another major feature of Git is the ease of collaborating with other developers that it provides. You can create a branch and (if desired) make changes, and then other developers can switch to that branch to review or make changes to the branch. If another developer has committed changes to the branch, Looker displays the **Pull Remote Changes** button. You should pull those committed changes to the branch before making additional changes.

You can also [delete a branch](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deleting_git_branches) other than the main branch, your current branch, or a developer's personal branch.

### Personal branches

To increase performance, the first time you open a LookML project in Development Mode, the Looker IDE displays the [Production Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#production_mode) version of the project, along with the **Create Developer Copy** button. Once you click the **Create Developer Copy** button for the project, Looker creates a local clone of the project's Git repository, creates your [personal Git branch](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#personal_branches), and loads the LookML project in [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#development_mode) for you.

Your personal branch starts with `dev-` and includes your name.

![Developer personal branch](https://docs.cloud.google.com/static/looker/docs/images/dev-git-default-personal-branch-2206.png)

Your personal branch is specific to you, and it _cannot_ be deleted. Your personal branch is read-only to all other developers. If you're collaborating with other developers on a project, you may want to create a new branch so that others can switch to that branch and contribute changes as well.

**Note:** You can't make changes to another developer's personal branch. To build on work in somebody else's personal branch, create a new branch starting from their branch.

### Creating a new Git branch

If you're working on a small fix and not collaborating with other developers, your personal branch is usually a good place to work. You can use your personal branch to make quick updates, and then commit the changes and push them to production.

However, you may also want to create new Git branches in addition to your personal branch. A new Git branch makes sense in these situations:

  * **You're working with other developers**. Since your personal branch is read-only to other developers, if you want to collaborate with others, you should create a new Git branch so that other developers can write to the branch. When you're collaborating with others, be sure to pull changes each time you resume work. That way, you'll have the latest updates from all developers before continuing work.
  * **You're working on multiple sets of features at once**. Sometimes you may be in the middle of a major project, but want to resolve a minor issue or make a quick fix. In this case, you can commit your changes to the branch you're on and then create or switch to another branch to work on a separate set of features. You can make your fix in the new branch, and then deploy that branch's changes to production — before resuming work in your original branch.



Before creating a new branch:

  * If you have a merge conflict on your current branch, you must resolve the conflict before you can create a new branch.
  * If you have any uncommitted changes on the current branch, you must [commit the changes](https://docs.cloud.google.com/looker/docs/git-command-reference#commit) on your current branch before creating a new branch.
  * If you want to create a branch starting from an existing development branch (and not the production branch), first get the latest version of the development branch by switching to that development branch, and then [pull remote changes](https://docs.cloud.google.com/looker/docs/git-command-reference#pull_dev) to sync your local version of that branch.



To create a new Git branch:

![Develop menu with a LookML project selected](https://docs.cloud.google.com/static/looker/docs/images/dev-open-project-b-2402.png)

  1. Verify that you have [Development Mode turned on](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#switching_in_and_out_of_development_mode).
  2. [Navigate to your project files](https://docs.cloud.google.com/looker/docs/accessing-project-files) in the **Develop** menu.

![Git Actions panel](https://docs.cloud.google.com/static/looker/docs/images/dev-git-new-branch-2120.png)

  3. Select the **Git** icon in the left-hand icon menu to open the **Git Actions** panel.

  4. Select the **View Branches** drop-down menu.

  5. Select **New Branch**.

![New Branch dialog](https://docs.cloud.google.com/static/looker/docs/images/dev-git-new-branch-dialog-2120.png)

  6. In the **New Branch** window, enter a name for your branch. Note that there are limitations for Git branch names; for naming requirements, see Rules for naming a Git branch on this page.

  7. Select the **Create From** drop-down menu and select an existing branch to use as the starting point for your new branch.

  8. Select **Create** to create your branch.




Alternatively, you can create Git branches from the **Branch Management** tab of the project's settings.

#### Rules for naming a Git branch

Looker uses the branch-naming-convention requirements specified by Git.

Git branch names must _not_ :

  * Contain a space character
  * Contain a double period: `..`
  * Contain a backslash: `\`
  * Contain the sequence: `@{`
  * Contain a question mark: `?`
  * Contain an opening square bracket: `[`
  * Contain an ASCII control character: `~` or `\^` or `:`
  * Begin with a period: `.`
  * Begin with the prefix: `dev-` (reserved for the personal branches of Looker developers)
  * End with a forward slash: `/`
  * End with the extension: `.lock`



In addition, the branch name can only contain an asterisk (`*`) if the asterisk represents an entire path component (for example, `foo/*` or `bar/*/baz`), in which case it is interpreted as a wildcard and not as part of the actual branch name.

### Switching to another Git branch

**Notes:**

  * If you have a merge conflict on your current branch, you must resolve the conflict before you can switch to a different branch.
  * If you have uncommitted changes on your current branch, you can't switch to an existing branch until you [commit the changes](https://docs.cloud.google.com/looker/docs/git-command-reference#commit) on your current branch. 



To switch to a different Git branch, follow these steps:

**Tip:** If you use the [Looker extension for VS Code](https://docs.cloud.google.com/looker/docs/getting-started-vscode-extension), switching branches locally by using `git checkout` automatically synchronizes your branch session on the Looker server. 

![Git branch drop-down menu](https://docs.cloud.google.com/static/looker/docs/images/dev-git-switch-branch-2120.png)

  1. In the project, navigate to the **Git Actions** panel by selecting the **Git** icon in the left-hand icon menu.
  2. In the **Git Actions** panel, select the Git branch drop-down menu to the right of your current Git branch name.
  3. Select the branch you want to switch to by selecting it in the menu, or by typing the branch name into the search box. Branch name search is case-insensitive. For example, you can search for "DEV" and see all branches with names that include "dev", "DEV", and "Dev".



### Managing Git branches

The **Branch Management** tab of the [project settings](https://docs.cloud.google.com/looker/docs/git-options#project_settings) shows a table of all the Git branches for the Looker project. To open the **Branch Management** tab, first navigate to the project settings by selecting the **Settings** icon from the left-hand icon menu. Next, select the **Branch Management** tab.

![Branch Management tab](https://docs.cloud.google.com/static/looker/docs/images/develop-branch-mgmt-2206.png)

On the **Branch Management** tab, you can:

  1. Create a new branch by selecting the **New Branch** button. See the Creating a new Git branch section on this page for more information.
  2. Search for branch names in the **Search Bar**.
  3. Refresh the table by selecting the **Refresh** button.
  4. Sort the table by selecting a column name.



The table includes the following information:

  * **Name** : Name of the Git branch. Looker developers' personal branches start with `dev-` and include the first and last name of the developer.
  * **Status** : The difference between your local version of the branch and the remote version of the branch. For example, a status of `3 commits behind` means that your local version of the branch is behind the remote version of the branch by three commits. Because Looker always uses the remote version of the main branch, the **Branch Management** tab doesn't show the status of the local version of the main branch. The main branch can always be considered to be up to date.
  * **Last Updated** : Amount of time since a Looker developer made a commit to the branch.
  * **Actions** : A button to delete the branch, or the reason that the branch isn't eligible for deletion.



### Deleting Git branches

From the **Branch Management** tab, you can delete branches that have a **Delete** button in the table. You cannot delete the following branches:

  * The main branch
  * Your current branch
  * A Looker developer's personal branch



In the table, these branches don't have a **Delete** button. Instead, the **Action** column of the table shows the reason that the branch can't be deleted.

**Note:** You can't restore a branch once it's been deleted. When you delete a branch, Looker removes both your local version of the branch and the remote version of the branch. 

However, if the branch was created by another Looker developer, or if other developers have checked out the branch, those developers will still have their local version of the branch. If a Looker developer makes commits to their local version of the branch and pushes it to production, you will once again see a remote version of the branch. This can be handy if you _do_ want to restore the branch. Otherwise, when you delete a branch, all other Looker developers should delete the same branch to ensure that it can't be accidentally resurfaced by someone pushing it to remote.

To delete one or more Git branches from your project, first navigate to the project settings by selecting the **Settings** icon from the left-hand icon menu. Then select the **Branch Management** tab. In the **Branch Management** tab, you can delete branches in two ways:

![Branch Management tab delete options](https://docs.cloud.google.com/static/looker/docs/images/develop-branch-delete-2206.png)

  1. Delete multiple branches by first selecting the branch checkboxes and then selecting **Delete Selected Branches**.
  2. Delete a single branch by selecting **Delete** next to the branch name.



## Executing Git commands in Looker

Looker has a built-in interface that integrates with your Git service. Looker displays the **Git button** in the upper right corner of the LookML IDE.

![Git button in the Looker IDE](https://docs.cloud.google.com/static/looker/docs/images/dev-git-button-718.png)

The Git button shows different options depending on where you are in the process of making changes and deploying to production. In general, the option shown on the button is the best guide for your next action.

If your developer branch is in sync with the production branch, the Git button displays the **Up to Date** message and isn't selectable.

![Git button showing Up to Date status](https://docs.cloud.google.com/static/looker/docs/images/dev-git-button-uptodate-718.png)

Once your project is [configured for Git](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#integrating_looker_with_git), you can select the **Git Actions** button to open the **Git Actions** panel.

![Git Actions panel in the Looker IDE](https://docs.cloud.google.com/static/looker/docs/images/git-actions-menu-git-actions-718.png)

The commands available on the **Git Actions** panel depend on where you are in the process of making changes and deploying to production.

## Getting your changes to production

With the default Looker Git integration, Looker prompts developers through the following Git workflow:

  * Committing changes to the developer's current development branch (and running data tests if your project is set up to [require tests before deploying](https://docs.cloud.google.com/looker/docs/git-options#require-data-tests))
  * Merging the development branch into the production branch, which by default is called `master`
  * Deploying the production branch to the Looker production environment that will be presented to your Looker end users



This means that, with the default Git integration, all developers merge their changes into a branch called `master`, and the latest commit on the `master` branch is what is used for the production environment of Looker.

For advanced Git implementations, you can customize this workflow:

  * You can have your developers submit pull requests for your Git production branch, instead of allowing developers to merge their changes through the Looker IDE. See the [Configuring project version control settings](https://docs.cloud.google.com/looker/docs/git-options#integrating_pull_requests_for_your_project) documentation page for details.
  * You can use the **Git Production Branch Name** field to specify which branch from your Git repository Looker should use as the target branch into which your Looker developers' branches are merged. See the [Configuring project version control settings](https://docs.cloud.google.com/looker/docs/git-options#git_production_branch_name) documentation page for details.
  * You can use [advanced deploy mode](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode) for specifying a different commit SHA or tag name to deploy to your Looker production environment, instead of using the latest commit on the production branch. (If you want to deploy a commit from a different branch, you can use the advanced deploy mode [webhook](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode#deploying_with_webhooks) or [API endpoint](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode#deploying_with_the_api).) See the [Advanced deploy mode](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode) documentation page for details.

**Note:** If you see a **Configure Git** button instead of the choices that are described in this section, you need to first [set up Git for your project](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#integrating_looker_with_git).

### Viewing uncommitted changes

The LookML IDE has several indicators that are displayed when you're in Development Mode and have uncommitted changes, as described in the [Marking additions, changes, and deletions](https://docs.cloud.google.com/looker/docs/looker-ide#marking_additions,_changes,_and_deletions) section of the [Looker IDE overview](https://docs.cloud.google.com/looker/docs/looker-ide) documentation page.

You can get a difference summary for all files by selecting the **View Uncommitted Changes** option from the **Git Actions** panel.

![View Uncommitted Changes](https://docs.cloud.google.com/static/looker/docs/images/dev-git-view-uncommitted-718.png)

In the **Uncommitted Changes to Project** window, Looker displays a summary of all the uncommitted, saved changes in all the project's files. For each change, Looker shows the following:

  * The name of the replaced file and the name of the added file. 
    * The name of the replaced file (indicated with `---`) and the name of the added file (indicated with `+++`). In many cases, this may show different versions of the same file, with revisions identified by `--- a/` and `+++ b/`.
    * Deleted files are shown as replacing a null file (`+++ /dev/null`).
    * Added files are shown as replacing a null file (`--- /dev/null`).
  * The line number where the change begins.

For example, `-101,4 +101,4` indicates that, at the 101st line in the file, 4 lines were removed and 4 lines were added. A deleted file with 20 lines would show `-1,20 +0,0` to indicate that, at the first line in the file, 20 lines were removed and replaced by zero lines.
  * The text that was updated: 
    * Deleted lines are displayed in red.
    * Added lines are displayed in green.



To display a difference summary for a single file, select the **View Changes** option from the file's menu.

![View Changes option in a file's menu](https://docs.cloud.google.com/static/looker/docs/images/dev-git-view-uncommitted-file-718.png)

### Committing changes

After you have made and saved any changes to your LookML project, the IDE may require you to validate your LookML. The Git button displays the text **Validate LookML** in this scenario.

![Git button showing the Validate LookML option](https://docs.cloud.google.com/static/looker/docs/images/dev-git-validate-718.png)

Whether this is required depends on your project's setting for [code quality](https://docs.cloud.google.com/looker/docs/git-command-reference#code_quality). For more information on the Content Validator, see the [Validating your LookML](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_changes) documentation page.

If another developer has made changes to the production branch since you last updated your local branch, Looker requires you to pull those updates from the production branch. The Git button displays the text **Pull from Production** in this scenario.

![Git button showing the Pull from Production option](https://docs.cloud.google.com/static/looker/docs/images/dev-git-pull-718.png)

**Note:** If your project is enabled for [advanced deploy mode](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode), the Git button instead displays the text **Pull from Primary Branch**.

Once you save your changes (and fix any LookML warnings or errors, [if required](https://docs.cloud.google.com/looker/docs/git-command-reference#code_quality)) and pull from production (if required), the Git button displays the text **Commit Changes & Push**.

![Git button showing the Commit Changes & Push option](https://docs.cloud.google.com/static/looker/docs/images/dev-git-commit-changes-718.png)

You can first review your uncommitted changes before committing.

When you're ready to commit the changes, use the Git button to commit these changes to your current branch. Looker displays the **Commit** dialog, which lists the files that have been added, changed, or deleted.

![Commit dialog showing files that have been updated](https://docs.cloud.google.com/static/looker/docs/images/dev-git-commit-dialog-718.png)

Enter a message that briefly describes your changes, and clear the checkboxes next to any files that you don't want to include in the sync. Then select **Commit** to commit the changes.

### Checking for unbuilt PDTs

If you have made changes to any PDTs in your project, it is optimal that all of your PDTs be built when you deploy to production so that the tables can be used immediately as the production versions. To check the status of PDTs in the project, select the **Project Health** icon to open the **Project Health** panel, and then select the **Validate PDT Status** button.

![Validate PDT Status button](https://docs.cloud.google.com/static/looker/docs/images/dev-check-unbuilt-pdts-2300.png)

See the [Derived tables in Looker](https://docs.cloud.google.com/looker/docs/derived-tables#checking_for_unbuilt_pdts_in_development_mode) documentation page for more information about checking for unbuilt PDTs in your LookML project and about working with derived tables in Development Mode.

### Running data tests

Your project may include one or more [`test`](https://docs.cloud.google.com/looker/docs/reference/param-model-test) parameters that define data tests to verify the logic of your LookML model. See the [`test`](https://docs.cloud.google.com/looker/docs/reference/param-model-test) parameter documentation page for information on setting up data tests in your project.

**Note:** By default, new LookML projects [require data tests to pass](https://docs.cloud.google.com/looker/docs/git-options#require-data-tests). If your project has one or more `test` parameters, the data tests must pass before you can deploy the project to production.

If your project contains data tests and you're in [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode), you can initiate your project's data tests in several ways:

![Different ways to access the Run Tests option](https://docs.cloud.google.com/static/looker/docs/images/dev-git-data-tests-run-2112.png)

  1. If your project settings are configured to [require data tests to pass before deploying your files to production](https://docs.cloud.google.com/looker/docs/git-options#require-data-tests), the IDE will present the **Run Tests** button after you commit changes to the project to run all the tests for your project, no matter which file defines the test. You must pass the data tests before you can deploy your changes to production.
  2. Select the **Run Data Tests** button in the **Project Health** panel. Looker will run all data tests in your project, no matter which file defines the test.
  3. Select the **Run LookML Tests** option from the file's menu. Looker will run only the tests defined in the current file.



Once you run the data tests, the **Project Health** panel will display the progress and results.

![Data test results in the Project Health panel](https://docs.cloud.google.com/static/looker/docs/images/dev-git-data-tests-results-2112.png)

  * A data test passes when the test's assertion is true for every row in the test's query. See the [`test`](https://docs.cloud.google.com/looker/docs/reference/param-model-test) parameter documentation page for details on setting up test assertions and queries.
  * If a data test fails, the **Project Health** panel will provide information about why the test failed, whether the test found errors in your model's logic or if it was the test itself that was invalid.
  * From the data test results, you can select the name of a data test to go directly to the LookML for the data test, or you can select the **Explore Query** button to open an Explore with the query defined in the data test.



### Deploying to production

Once you have committed changes to your branch, the Looker IDE will prompt you to merge your changes to the primary branch. The type of prompt you'll see in the IDE will depend on your project's configuration:

  * If your project is configured for [advanced deploy mode](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode), the IDE will prompt you to merge your changes into the primary branch. Once you merge your commit, a Looker developer with the [`deploy` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#deploy) can deploy your commit to production by using the Looker IDE [deployment manager](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode#deployment_manager), or by using a [webhook](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode#deploying_with_webhooks) or an [API endpoint](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode#deploying_with_the_api).
  * If your project is configured for Git integration using [pull requests](https://docs.cloud.google.com/looker/docs/git-options#integrating_pull_requests_for_your_project), you will be prompted to open a pull request using your Git provider's interface.
  * Otherwise, with the default Looker Git integration, if you have [`deploy` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#deploy), the Looker IDE will prompt you to merge your changes to the production branch and deploy your changes to the production version of your Looker instance.



When you deploy changes, the Looker IDE shows a **Deployment Submitted** dialog to confirm that your changes are deploying. You can click the **Go to Deployment Manager** button in the dialog to go to the **Deploy** tab of your project and check the progress of the deployment.

The **Deployment Manager** is visible in Development Mode only and it shows a list of recent deployments and their status. If a deployment is still running, such as in the case of a very large LookML model, a **Refresh** icon appears in the deployment table. You can click the **Refresh** icon to get an updated status of the deployment.

If any of your deployments were made with [advanced deploy mode](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode#deploying_a_commit_from_the_deployment_manager), the **Deployment Manager** displays the tag that was specified by the LookML developer, if any.

## Unlocking a locked Git branch

**Preview:** This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms](https://cloud.google.com/terms/service-terms#1) section of the Service Specific Terms. Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

If you encounter an issue during the Public Preview of unlocking a Git branch, report it to [looker-git-dev-external@google.com](mailto:looker-git-dev-external@google.com).

Now available in preview, LookML developers can unlock a Git branch in cases where their Git branch is locked as a result of another Git operation in progress or a previous Git operation failing. When the Git repository is locked, Looker displays the **Unlock Branch** option in the [**Git Actions** panel](https://docs.cloud.google.com/looker/docs/git-command-reference#git_actions_panel) of the Looker IDE. In addition, if a LookML developer tries to commit a change on a locked Git branch, Looker displays a warning in the **Commit** dialog, along with an option to delete the Git lock.

## Deleting your developer copy of the LookML project

**Preview:** This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms](https://cloud.google.com/terms/service-terms#1) section of the Service Specific Terms. Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

If you encounter an issue during the Public Preview of deleting your developer copy, report it to [looker-git-dev-external@google.com](mailto:looker-git-dev-external@google.com).

The first time you open a LookML project in Development Mode, the Looker IDE displays the [Production Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#production_mode) version of the project, along with the [**Create Developer Copy**](https://docs.cloud.google.com/looker/docs/git-command-reference#create-developer-copy) button. When you click the **Create Developer Copy** button for the project, Looker creates a local clone of the project's Git repository, creates your [personal Git branch](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#personal_branches), and loads the LookML project in [Development Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#development_mode) for you.

If you don't need your local developer copy of the Git repository, if you're in an inconsistent Git state, or if you're unable to edit your LookML files, you can delete your developer copy as described in this section.

If you delete your developer copy of the project's Git repository, you will lose the following:

  * Any changes that you haven't [committed and pushed to the remote repository](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#committing_changes)
  * Any [Git branch that you created](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#creating_a_new_git_branch), if you haven't yet committed and pushed a change on that branch

**Tip:** Before deleting your developer copy, try diagnosing and repairing your project from the [**LookML Projects**](https://docs.cloud.google.com/looker/docs/manage-projects) page. The [**Diagnose & Repair**](https://docs.cloud.google.com/looker/docs/diagnosing-and-repairing-git-projects) tool can detect and automatically resolve stale lock files, repository index corruptions, and permission issues while automatically preserving your uncommitted work on a dedicated recovery branch.**Warning:** If you want to keep any uncommitted changes or any Git branches on which you haven't yet pushed commits, preserve your updates by copying them to external files on your local computer; and then, after you complete the procedure to delete your developer copy, manually re-enter your updates.

Follow these steps to delete your developer copy of the LookML project's repository:

  1. Open your LookML project in the Looker IDE.
  2. Select the **Settings** icon from the Looker IDE icon menu to display the project settings. The [**Configuration**](https://docs.cloud.google.com/looker/docs/git-options#configuration) tab opens by default.
  3. In the **Configuration** tab, click the **Delete Developer Copy** button.
  4. To prevent you from accidentally deleting your devloper copy of the project's repository, Looker displays a confirmation dialog. In the confirmation dialog, enter the name of the LookML project in the text field.
  5. To prevent you from accidentally deleting your developer copy of the project's repository, Looker displays a confirmation dialog. In the confirmation dialog, enter the name of the LookML project in the text field.
  6. Click the **Delete Developer Copy for <your project's name>** button.



When Looker has deleted your developer copy of the project's repository, the Looker IDE displays the Production Mode version of the LookML project.

If you want to create a new developer copy of the project's repository, click the **Create Developer Copy** button.

## Advanced deploy mode

With the default Looker Git integration, Looker developers commit their changes to their development branch, then merge their development branch into the production branch. Then, when you deploy to the Looker environment, Looker uses the latest commit on the production branch. (See the Getting your changes to production section on this page for the default Git workflow and other options for advanced Git implementations.)

For cases where you don't want the to always use the latest commit on the production branch for your Looker environment, a developer with [`deploy` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#deploy) can use advanced deploy mode to specify the exact commit to be used for your Looker environment. This is useful in multi-environment developer workflows, where each environment points to a different version of a codebase. It also gives one or several developers or administrators greater control over the changes that are deployed to production.

When advanced deploy mode is enabled, the Looker IDE does not prompt developers to deploy their changes to production. Instead, the IDE prompts developers to merge their changes into the production branch. From there, changes can be deployed only in the following ways:

  * Using the [deployment manager](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode#deployment_manager) in the Looker IDE
  * Triggering a [webhook](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode#deploying_with_webhooks)
  * Using an [API endpoint](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode#deploying_with_the_api)

**Note:** For projects with advanced deploy mode enabled, if the project has never been deployed to production, the initial deployment to production must be made using the [deployment manager](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode#deployment_manager) in the Looker IDE. You can't use the API or the webhook for the initial deployment of a project that uses advanced deploy mode. After the initial deployment to production (even if it was initially deployed without advanced deployment mode), you can use the webhook or the API to deploy subsequent changes to production using advanced deploy mode.



See the [Advanced deploy mode](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode) documentation page for details.

## Checking the impact of your changes

After making your changes available to the organization, you can use [content validation](https://docs.cloud.google.com/looker/docs/content-validation) to make sure you have not invalidated any dashboards or saved Looks. You'll have the opportunity to fix them if you have.

## Handling typical issues

While working on your model, you may need to take one of the following actions:

  * Abandon your changes

Occasionally you may want to abandon your data-modeling changes. If you haven't saved your changes yet, you can refresh or navigate away from the page and then accept the warning prompt. If you have saved the changes, you can revert the uncommitted changes as described in the Reverting uncommitted changes section.

  * Handle merge conflicts with other developers' work

If you have more than one developer working on your data model, Git typically handles the situation. However, occasionally Git needs a human to resolve merge conflicts.




Some changes, such as changing the name of a field, can affect existing dashboards and Looks. As mentioned earlier, after making your changes available to the organization, you can use [content validation](https://docs.cloud.google.com/looker/docs/content-validation) to check your content and fix any issues.

### Reverting uncommitted changes

When working on your personal development branch, you can revert uncommitted changes that you have saved if you don't want to deploy them. You can revert all the uncommitted changes for all files in the project or just the changes in a single file.

Note the following about reverting changes:

  * When you rename a file, you're essentially deleting the original file and creating a new file with a new name. Because this involves more than one file, you can't use the **Revert File** option to undo the renaming of a file. If you want to undo a file rename, use the **Revert to...** option from the **Git Actions** panel.
  * When you delete a file, the file is no longer displayed in the IDE file browser. If you want to revert the deletion of a file, use the **Revert to...** option from the **Git Actions** panel.



To revert uncommitted changes for **all files** , follow these steps:

![Revert uncommitted changes option](https://docs.cloud.google.com/static/looker/docs/images/dev-git-revert-all-changes-718.png)

  1. Select the **Revert to...** option in the **Git Actions** panel.
  2. Select a revert option: 
     * To revert only _uncommitted_ changes, select **Revert uncommitted changes**. You can also select the **View changes** link to view the changes that would be reverted.
     * To revert all changes, including uncommitted and committed changes, select **Revert to Production**
  3. To complete the revert process, select **Confirm**.



To revert any additions or deletions in the contents of a single file, select the **Revert File** option from that file's menu:

![Revert File option](https://docs.cloud.google.com/static/looker/docs/images/dev-git-revert-single-file-718.png)

### Resolving merge conflicts

Typically, Git can automatically merge your new changes with the production version of your LookML files. A merge conflict occurs when Git encounters conflicting changes and can't identify which changes should be kept, usually when another developer has made changes since you last pulled and you have made changes in the same area. If you have a merge conflict in your code, Looker displays a **Merge conflicts** warning after you commit changes and pull from production.

![Merge conflicts warning](https://docs.cloud.google.com/static/looker/docs/images/develop-merge-conflict-warning-718.png)

When Looker shows the merge-conflict warning, we recommend that you resolve the merge conflict before making any further changes. Pushing a merge conflict to production will cause parse errors that may prevent exploration of your data. If you're an advanced Git user and you want to move forward with pushing changes, select the **Don't Resolve** button.

In the LookML file itself, the lines with conflicts are marked like this:
    
    
    <<<<<<< HEAD
    Your code
    &#61;&#61;&#61;&#61;&#61;&#61;&#61;
    Production code
    >>>>>>> branch 'master'
    

Looker shows the following _merge markers_ to indicate the merge conflicts:

  * **< <<<<<< `HEAD`** marks the beginning of the conflicting lines.
  * **> >>>>>> `branch 'master'`** marks the end of the conflicting lines.
  * **=======** separates each version of the code so you can compare them.



In the preceding example, `your code` represents the changes you committed, and `production code` represents the code into which Git couldn't automatically merge your changes.

To resolve a merge conflict:

![Merge conflict marked in file](https://docs.cloud.google.com/static/looker/docs/images/develop-merge-conflict-718.png)

  1. Find the files with merge conflicts. Looker marks these files in red, or you can also [search your project](https://docs.cloud.google.com/looker/docs/looker-ide#find-and-replace) for merge markers, such as <<<< or `HEAD`, to find all the conflicts in your project. You can also find affected files by selecting the **files** link in the merge warning that appears in the **Git Actions** panel.
  2. In the file, go to the lines with merge conflicts and delete the version of the text that you do **NOT** want to keep, and also delete all the merge conflict markers.
  3. Save the file, and repeat the preceding steps for any other files marked with merge conflicts.

**Tip:** [Search your project](https://docs.cloud.google.com/looker/docs/looker-ide#find-and-replace) for each of the merge markers to verify that you have resolved all conflicts and deleted all the merge markers. Make sure to remove all instances of merge markers in your LookML files. These markers will cause parse errors that can prevent users from exploring your data.
  4. After you have resolved all merge conflicts and deleted all merge markers from your project, [commit the changes](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#committing_changes) and [deploy them to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production).




Now that you have resolved the merge conflict and pushed your resolution to production, other developers can pull from production and continue work as usual.

### Troubleshooting silent deployment failures and out-of-sync commits

You may experience unexpected behavior in the Looker Deployment Manager, such as the following:

  * Minor deployments failing silently without presenting an error in the Looker UI
  * The Looker UI incorrectly showing hundreds of commit differences between Looker and the production branch
  * Subsequent rollback or re-deployment attempts resulting in completely different commit hashes
  * An inability to accurately inspect past deployments in the Looker UI



#### Cause

These symptoms are typically caused by a Git stale lock or a conflicting reference (such as an existing tag that points to a specific commit SHA) in the backend repository. This triggers an internal `Branch already exists` error, which prevents the production LookML from updating and causes the deployment to fail silently.

#### Resolution

To resolve these silent deployment failures and re-sync your project, reset your Git connection by following these steps:

  1. In Looker, navigate to the settings of the affected LookML project.
  2. Select **Reset Git Connection**.
  3. Re-enter your Repository URL and click **Continue**.
  4. Looker will generate a new SSH deploy key. Add this new public key to your Git provider as a deploy key for the repository. 
     * Make sure to **Allow write access** (if using GitHub) or the equivalent permission for your Git provider.
  5. Click **Test and Finalize Setup** to establish the new connection.



### Resolving the `Pull Remote Changes Failed. Pull Incomplete` error

  * **Diagnose and repair the project** : You can use the [**Diagnose & Repair**](https://docs.cloud.google.com/looker/docs/diagnosing-and-repairing-git-projects) tool from the **LookML Projects** page to check repository health, clear stale lock files, and repair repository inconsistencies without manually losing uncommitted changes.
  * **Manually preserve local changes** : If you want to keep any uncommitted changes or any Git branches on which you haven't yet pushed commits, manually preserve your updates by copying them to your local computer. Then, pull from production, manually re-apply your changes, commit them, and push them to resolve the conflict.
  * **Delete your developer copy** : Alternatively, you can use the **Delete Developer Copy** option to reset the Git state for your branch and clear conflicts. For more information, see the Deleting your developer copy of the LookML project section on this page.



### Resolving the `Pull Production Failed` error with the `MERGING_RESOLVED` state

If you receive the error message `Pull Production Failed: Cannot pull into a repository with state: MERGING_RESOLVED`, it indicates that the Git repository is stuck in a `MERGING_RESOLVED` state. This is typically caused by an incomplete merge or a lingering merge conflict.

To clear this state and resolve the error, perform one of the following actions:

  * **Diagnose and repair the project** : Run the [**Diagnose & Repair**](https://docs.cloud.google.com/looker/docs/diagnosing-and-repairing-git-projects) tool on your project from the **LookML Projects** page. The tool can automatically repair broken repository states and clear interrupted merge locks.
  * **Delete your developer copy** : You can delete and recreate your local workspace to clean references in the Git repository. For instructions on how to do this, see the Deleting your developer copy of the LookML project section on this page.
  * **Create a clean branch** : Alternatively, you can create a new, clean branch and push it to production. This can resolve the merge conflict state and allow development branches to pull from production without issues.



### Resolving the `Production HTTPS credentials are OK but your development HTTPS credentials are failing to authorize to the remote` error

If you use [HTTPs credentials to connect to your Git provider](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#connecting_to_git_using_https), you may see the error `Production HTTPS credentials are OK but your development HTTPS credentials are failing to authorize to the remote` when you [pull remote changes](https://docs.cloud.google.com/looker/docs/git-command-reference#pull_dev) to sync the most recent versions of any changed files on the branch from the remote end to your local files.

This error can occur when the personal access token or credentials that are configured for your Looker development environment are incorrect, are invalid, or have expired.

To resolve this error, generate a new personal access token from the Git provider (for example, Azure DevOps or GitLab) and update your Looker development credentials with the newly generated token. To prevent this error in the future, monitor the expiration date of your personal Git access token to ensure that it's proactively updated in Looker before it expires.

### Unable to delete personal Git branches

By default, the Looker UI restricts you from manually deleting personal branches that belong to other users or service accounts. In the **Branch Management** tab, the checkboxes for selecting and deleting these branches are unavailable, and they don't have a **Delete** button.

Furthermore, deleting these branches directly on your Git provider (such as GitHub) won't automatically remove them from Looker's local Git clone, and they will continue to appear in the Looker UI.

#### Resolution

To delete personal branches that belong to other users or service accounts from Looker, use the Looker API or an SDK to delete them programmatically.

Use the [`delete_git_branch`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Project/delete_git_branch) API endpoint, specifying the `project_id` and the `branch_name` that you want to delete.

Alternatively, use one of the Looker [SDKs](https://docs.cloud.google.com/looker/docs/api-sdk). For example, this example uses the SDK method:

`delete_git_branch(<PROJECT_ID>, <BRANCH_NAME>)`

## Git garbage collection

[Git garbage collection](https://git-scm.com/docs/git-gc) cleans up unnecessary files and compresses file revisions to optimize your Git repository. Git garbage collection (`git gc`) is run automatically when your Looker instance is updated or rebooted. To keep from running `git gc` too often, Looker waits 30 days since the last `git gc` and then runs `git gc` on the next reboot.

In rare cases, you might try to [**Push Changes to Remote**](https://docs.cloud.google.com/looker/docs/git-command-reference#push_changes_remote) or [**Push Branch to Remote**](https://docs.cloud.google.com/looker/docs/git-command-reference#push_branch) while `git gc` is running. If Looker displays an error, wait for a minute or two and then try again to push your changes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
