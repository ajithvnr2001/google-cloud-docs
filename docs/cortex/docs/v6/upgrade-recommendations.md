---
url: https://docs.cloud.google.com/cortex/docs/v6/upgrade-recommendations/
title: Upgrade recommendations \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:37.161956+00:00
---

# Upgrade recommendations  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/upgrade-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Upgrade recommendations

This page describes recommendations to upgrade to new versions from customized [Cortex Framework Data Foundation](https://github.com/GoogleCloudPlatform/cortex-data-foundation). On every release, the Cortex team commits to minimize disruptions while it add new features to the Cortex Framework. New updates prioritize backward compatibility. However, this guide helps you minimize the possible issues.

[Cortex Framework Data Foundation](https://github.com/GoogleCloudPlatform/cortex-data-foundation) provides a set of predefined content and templates to accelerate value from data replicated into [BigQuery](https://cloud.google.com/bigquery). Organizations adapt these templates, modules, SQL, Python scripts, pipelines and other content provided to fit their needs.

## Core components

Cortex Framework Data Foundation content is designed with a principle of openness in mind. Organizations can use the tools that work best for them when working with the BigQuery data models provided. The only platform on which the foundation has a tight dependency on is BigQuery. All other tools can be interchanged as required:

  * **Data Integration:** Any integration tool that has interconnectivity with BigQuery can be leveraged provided it can replicate raw tables and structures. For example, raw tables should resemble the same schema as they were created in SAP (same names, fields, and data types). In addition, the integration tool should be able to provide basic transformation services such as updating target data types for BigQuery compatibility as well as adding additional fields like timestamp or operations flag for highlighting new and changed records.
  * **Data Processing:** The Change Data Capture (CDC) processing scripts provide work with [Managed Service for Apache Airflow](https://cloud.google.com/composer) (or Apache Airflow) are optional. Conversely, the SQL statements are produced separately from the Airflow-specific files where possible, so that customers can make use of the separate SQL files in another tool as needed.
  * **Data Visualization:** While [Looker](https://cloud.google.com/looker) dashboarding templates are provided and contain visualizations and minimum logic, the core logic remains available in the data foundation within BigQuery by design to create visualizations with their reporting tool of choice.



## Key benefits

Cortex Framework Data Foundation is designed to be adaptable to various business needs. Its components are built with flexibility, allowing organizations to tailor the platform to their specific requirements and getting the following benefits:

  * **Openness** : Integrates seamlessly with various data integration, processing, and visualization tools beyond BigQuery.
  * **Customization:** Organizations can modify and expand pre built components like SQL views to match their data models and business logic.
  * **Performance Optimization:** Techniques like partitioning, data quality checks, and clustering can be adjusted based on individual workloads and data volumes.
  * **Backward Compatibility:** Cortex strives to maintain backward compatibility in future releases, minimizing disruption to existing implementations. For information about version changes, see the [Release Notes](https://docs.cloud.google.com/cortex/docs/release-notes).
  * **Community Contribution:** Encourages knowledge sharing and collaboration among users.



## Update process

The following sections share the instructions for one way in which developers can keep their code up-to-date with the Cortex Framework Data Foundation repository while retaining their customizations. Use of the pre-delivered deployment scripts in CI/CD pipelines. However, organizations can employ alternative tools and methodologies to suit their preferences, such as [Dataform](https://docs.cloud.google.com/dataform/docs), or automation tools provided by the different Git hosts, such as GitHub actions.

### Set up your repository

This section outlines one approach to setting up your repository. Before following these steps, a solid understanding of Git is recommended.

  1. **[Fork](https://github.com/GoogleCloudPlatform/cortex-data-foundation/fork) core repository**: Create a fork of the Cortex Framework Data Foundation repository. The fork keeps that repository receiving updates from the Google Cloud repository, and a separate repository for the _Company's main_.

  2. **Create Company Repository** : Establish a new Git host for your company's repository (for example, Cloud Source). Create a repository with the same names as your forked repository on the new host.

  3. **Initialize Company Repository** : Copy the code from your forked Repository into the newly created company repository. Add the original forked repository as an [upstream remote repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/configuring-a-remote-repository-for-a-fork) with the following command, and verify the remote has been added. This establishes a connection between your company repository and the original repository.
         
         git remote add google <<remote URL>>
         git remote -v
         git push --all google
         

  4. **Verify Repository Setup** : Ensure your company repository contains the cloned code and history. You should see the two remotes, origin and the one you added after using the command:
         
         git remote -v:
         

You now have the repository, the _Company's repository_ , where developers can submit their changes. Developers can now clone and work in branches in the new repository.




### Merge your changes with a new Cortex release

This section describes the process of merging changes from the _Company's repository_ and changes coming from the Google Cloud repository.

  1. **Update forks** : Click **Sync fork** to update your forks for your repository with the changes from the Google Cloud repository. For example, the following changes to the _Company's repository_ are done. And there has been some other changes in the Data Foundation repository by Google Cloud in a new release.

     * Created and incorporated the use of a new view in SQL
     * Modified existing views
     * Replaced a script entirely with our own logic

The following commands sequence adds the fork repository as an upstream remote repository to pull the updated release from as _GitHub_ and checks out its main branch as _GitHub-main._ Then, this example checks out the main branch from the _Company's repository_ in Google Cloud Source and creates a branch for merging called `merging_br`.
    
    git remote add github <<github fork>>
    git fetch github main
    git checkout -b github-main github/main
    git checkout  main
    git checkout -b merging_br
    

There are multiple ways to build this flow. The merging process could also happen in the fork in GitHub, be replaced by a rebase instead of a merge, and the merging branch could also be sent as a merge request. These variations of the process depend on current organizational policies, depth of changes and convenience.

With this setup in place, you can compare the incoming changes to your local changes. It's recommended to use a tool in a graphic IDE of choice to see the changes and choose what gets merged. For example, Visual Studio.

It's recommended flagging customizations using comments that stand out visually, to make the diff process easier.

  2. **Start the merge process** : Use the created branch (in this example, is the branch called `merging_br`) to converge all changes and discard files. When ready, you can merge this branch back into the main or another branch for your Company's repository to create a merge request. From that merging branch that was checked out from your Company's repository's main (`git checkout merging_br`), merge the incoming changes from the remote fork.
         
         ## git branch -a
             ## The command shows github-main which was created from the GitHub fork
             ## You are in merging_br
         
             git merge github-main
         
             ## If you don't want a list of the commits coming from GitHub in your history, use `--squash`
         

This command generates a list of conflicts. Use the graphical IDE comparison to understand the changes and choose between _current_ , _incoming_ and _both_. This is where having a comment in the code around customizations becomes handy. Choose to discard changes altogether, delete files that you don't want to merge at all and ignore changes to views or scripts that you have already customized.

  3. **Merge changes** : After you have decided on the changes to apply, check the summary and commit them with the command:
         
         git status
             ## If something doesn't look right, you can use git rm or git restore accordingly
             git add --all #Or . or individual files
             git commit -m "Your commit message"
         

If you feel insecure about any step, see [Git basic undoing things](https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things).

  4. **Test and deploy** : So far you are only merging into a "temporary" branch. It's recommended running a test deployment from the `cloudbuild\*.yaml` scripts at this point to make sure everything is executing as expected. Automated testing can help streamline this process. Once this merging branch looks good, you can checkout your main target branch and merge the `merging_br` branch into it.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
