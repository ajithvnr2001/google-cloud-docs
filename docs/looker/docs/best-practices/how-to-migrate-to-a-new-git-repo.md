---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-migrate-to-a-new-git-repo/
title: Migrating to a new Git repository \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:35.844795+00:00
---

# Migrating to a new Git repository  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-migrate-to-a-new-git-repo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Migrating to a new Git repository Stay organized with collections  Save and categorize content based on your preferences. 

If you have a LookML project that is connected to a Git repository, you might want to move that project's LookML to a new repository. 

There are two possible approaches to this problem, both of which are described in the following sections: 

  * **Reset the Git connection**: This simple solution preserves all personal and shared branches in Looker and is suitable for the majority of use cases.
  * **Clone the Git repository**: This advanced solution is preferred when it is important to be able to immediately see the complete history of all branches ever used through your Git provider's UI. 



## Simple solution: Resetting the Git connection

If you [reset the Git connection](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#integrating_looker_with_git) and enter a new Git repository URL, then the LookML will be moved over to that repository. All saved changes in personal and shared branches will be maintained and usable in Looker. At first, your Git provider's UI will only show the master branch and its history. Other branches and their history will appear the next time a commit is made to that branch. To migrate to a new repository using this method, follow these steps: 

  1. Navigate to the [**Project Settings** page](https://docs.cloud.google.com/looker/docs/git-options#project_settings) for that project.
  2. On the [**Configuration** tab](https://docs.cloud.google.com/looker/docs/git-options#configuration) of the **Project Settings** page, select the **Reset Git Connection** button.
  3. On the **Configure Git** page, enter the new Git URL (the Git URL for the repository to which you want to migrate), and then select **Continue**.
  4. If you are using SSH to connect, be sure to select **Reset Key**. Otherwise, the same SSH key will be used, which can cause a conflict if both repositories are hosted by the same service (in this case, GitHub).
  5. For SSH connections, add the new deploy key to your Git repo, and be sure to grant write access in the Git repo deploy key settings. If you are using HTTPS, enter the login credentials for your Git repo. See the [Setting up and testing a Git connection](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#integrating_looker_with_git) documentation page for full instructions on setting up Git.



Once you have followed these steps, your project will be connected to the new repository. 

> **Note:** Your project LookML will not appear in the master branch of the new repository until you [deploy your project to production](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#deploying_to_production). Unless you deploy to production, your LookML code will appear only on your development branch in the new repository after [you commit the code](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#committing_changes), or push it to remote (a [Git command](https://docs.cloud.google.com/looker/docs/git-command-reference#push_changes_remote) available in the [**Git Actions** panel](https://docs.cloud.google.com/looker/docs/git-command-reference)).

## Advanced solution: Cloning the repository

The simple solution described previously will preserve the history of all branches, but only the master branch and its history will be visible in the GitHub UI at first. Once a commit is made on a personal or shared branch in Looker, that branch and its history will appear in the GitHub UI. A more advanced solution is necessary to immediately view all branches and their history through the GitHub UI. 

First, you need to have access to the original repository in GitHub (or other Git provider). You can find the repository URL at the bottom of the project settings or project configuration page. 

For this example, suppose that `git@github.com:looker/PROJECT_NAME.git` is the original repo and `git@github.com:your_organization/PROJECT_NAME.git` is the new repo: 

  1. Clone the original repository onto your computer, and pull down the branches you want to preserve.
         
         git clone git@github.com:looker/PROJECT_NAME.git
         cd PROJECT_NAME
         git checkout master
         git pull
         

  2. Reset the repo's remote URL. See the [GitHub documentation](https://help.github.com/articles/changing-a-remote-s-url/) for more information.
         
         git remote -v
         

This shows you the remote(s) to which your repo is currently pointing. The results will look something like this:
         
         origin git@github.com:looker/PROJECT_NAME.git (fetch)
         origin git@github.com:looker/PROJECT_NAME.git (push)
         

  3. Next, set the origin remote to the new repo:
         
         git remote set-url origin git@github.com:your_organization/PROJECT_NAME.git
         git push origin master
         

  4. Now, to bring in history and files for dev branches, you'll need to do `git checkout dev_branch_name` and `git push origin` for each dev branch. This can be done manually or in a loop in a script such as shown in the following example:
         
         #!/bin/bash
         for branch in $(git branch --all | grep '^\s*remotes' | egrep --invert-match '(:?HEAD|master)$'); do
         git branch --track "${branch##*/}" "$branch"
         done
         

Then push the branches with `git push --all`.

  5. Reset the Git connection in Looker to this new URL and set up a deploy key on this new repo (see the steps in the simple solution section earlier on this page).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
