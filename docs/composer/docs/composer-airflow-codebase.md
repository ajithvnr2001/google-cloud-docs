---
url: https://docs.cloud.google.com/composer/docs/composer-airflow-codebase/
title: Managed Airflow's Airflow code repository \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:45.145750+00:00
---

# Managed Airflow's Airflow code repository  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-airflow-codebase/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Resources ](https://docs.cloud.google.com/composer/docs/resources)



Send feedback 

#  Managed Airflow's Airflow code repository Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the repository that stores patched Apache Airflow code used in Managed Airflow.

## About the repository

The [Composer-Airflow repository](https://github.com/GoogleCloudPlatform/composer-airflow/) is a read-only repository that contains the patched Apache Airflow code running in Managed Airflow.

**Warning:** Managed Airflow doesn't support on-premise or production usage of this code. We strongly recommend to **avoid using the code from this repository in production**. Instead, see Usage examples for some ways in which you can use this repository.

A particular version of Apache Airflow found in Managed Airflow is not always an exact match of the corresponding version in upstream Airflow because Managed Airflow uses a patched version of Airflow. This repository holds the code for every patched version of Airflow used in Managed Airflow. For information about which versions of Airflow are found in Managed Airflow, see [Managed Airflow versions list](https://docs.cloud.google.com/composer/docs/composer-versions).

### Contributing

This code is not a fork of [Apache Airflow](https://github.com/apache/airflow). The code found in this repository comes directly from the Apache Airflow repository, but at a different timeline than normal Apache Airflow releases.

If you would like to contribute to this codebase, then [contribute to Airflow directly](https://github.com/apache/airflow/blob/master/CONTRIBUTING.rst) instead. Don't do so in this repository because Pull Requests aren't accepted in it.

### Issues and support

  * If you have an issue with the code found in this repository, you can create an issue directly [in the Airflow repository](https://github.com/apache/airflow/issues).
  * If you have an issue with Managed Airflow, please use [Managed Airflow support channels](https://docs.cloud.google.com/composer/docs/getting-support).



## Navigating the repository

The repository has one branch for each version of Airflow available in Managed Service for Apache Airflow. Not all versions of Airflow are supported in Managed Airflow. You can see which Airflow versions are supported by a particular Managed Airflow version in the [Managed Airflow versions list](https://docs.cloud.google.com/composer/docs/composer-versions).

## Usage examples

This section lists usage examples for the repository.

### Is this commit from the Airflow repository in my version of Managed Airflow?

SHA1s of commits in the [Composer-Airflow](https://github.com/GoogleCloudPlatform/composer-airflow/) repository don't correspond to commit SHA1s in the [upstream Airflow repository](https://github.com/apache/airflow). One of the ways to search for a specific commit is by looking for the corresponding commit message.

It is not possible to use the GitHub UI to search through commit messages in branches other than the default branch, however, it is possible to do so using the `git` CLI. To search for a particular commit in this repository, you need to have [`git` installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

To search for a commit message using the `git` CLI:

  1. Clone the repository and change to the repository directory using the following command:
         
         git clone git@github.com:GoogleCloudPlatform/composer-airflow.git && \
         cd composer-airflow
         

  2. Search for the commit message:
         
         git log --source --grep="COMMIT_MESSAGE" --all
         

In this command:

     * `--source` shows the branch where the commit is found
     * `--grep` specifies the message that must be searched the log
     * `--all` searches in all branches
  3. The branch is located next to the commit hash in the first line of every result. If the command returns a commit, this means it's in your version of Managed Airflow. Additionally, if the version of Airflow in your environment is later than the branch version, then the commit is used in your environment's Airflow version.




For example, if you want to search for the commit message `Force explicit choice on GPL dependency`, then your command would be:
    
    
    git log --source --grep="Force explicit choice on GPL dependency" --all
    

If there is a [matching commit](https://github.com/apache/airflow/commit/c37fc0b6ba19e3fe5656ae37cef9b59cef3c29e8), then your results would look like the following output example. There might be more than one result.
    
    
    commit 64ff1089e30e80b08bf5155edd9e49f5293ebbe4 refs/heads/<strong>1.10.2</strong>
    Author: example_airflow_committer <example_airflow_committer@users.noreply.github.com>
    Date:   Wed Aug 1 11:25:31 2018 +0200
    
        [AIRFLOW-2817] Force explicit choice on GPL dependency (#3660)
    
        By default one of Apache Airflow's dependencies pulls in a GPL
        library. Airflow should not install (and upgrade) without an explicit choice.
    
        This is part of the Apache requirements as we cannot depend on Category X
        software.
    
        (cherry picked from commit c37fc0b6ba19e3fe5656ae37cef9b59cef3c29e8)
        Signed-off-by: Example Airflow Committer  <example_airflow_committer@users.noreply.github.com>
        (cherry picked from commit b39e4532d9d1086c60b31553d08972bcc68df641)
        Signed-off-by: Example Airflow Committer  <example_airflow_committer@users.noreply.github.com>
        GitOrigin-RevId: cefcf4c61f64be3792cbfed509b82a9eb4cc47be
    

### What does this Airflow operator look like in my version of Managed Airflow?

Airflow operators and accompanying code are packaged and released separately from core Airflow in PyPI packages called [provider packages](https://airflow.apache.org/docs/apache-airflow-providers/).

Some of these packages are installed by default in Managed Airflow. To know which version is installed in your environment, check the list of packages for your environment's version of Managed Airflow in the [versions list](https://docs.cloud.google.com/composer/docs/composer-versions).

###  GitHub UI 

To look at the code for an operator in a particular provider package version:

  1. Go to the [upstream Airflow repo](https://github.com/apache/airflow).

  2. Enter the name of the operator you are searching for in the GitHub search bar.

  3. If more than one file is returned, click the code file with a path that begins in `airflow/providers`.

For example, if you search for the `GoogleCloudStorageCreateBucketOperator`, then choose `airflow/providers/google/cloud/operators/gcs.py`.

  4. Click the branch selector, which opens up the **Switch branches/tags** drop-down list.

  5. Click the **Tags** tab.

  6. For `providers` packages, search for the name of your provider and the version by typing `providers-PROVIDER_NAME/PROVIDER_VERSION` in the drop-down list's search bar, where `PROVIDER_NAME` is the name of the provider, and `PROVIDER_VERSION` is the name of the version you are looking for.

For example, if you want to see version `10.0.0` of the `apache-airflow-providers-google` package, you would search for `providers-google/10.0.0`.

  7. For `backport-providers` packages, which are used in Airflow 1, search for `backport-providers-PROVIDER_VERSION` in the drop-down list's search bar.

For example, if you want to see version `2021.3.3` of the `apache-airflow-backport-providers-google` package, then search for `backport-providers-2021.3.3`.

  8. Click the result that matches your query.

  9. The code on the screen is what is running in your version of that operator. You can also click **History** to see the commit history up until this point.




###  git CLI 

To look at the code for an operator in a particular provider package version:

  1. Clone the [upstream Airflow repo](https://github.com/apache/airflow).

  2. For `providers` packages, run `git checkout providers-PROVIDER_NAME/PROVIDER_VERSION`, where `PROVIDER_NAME` is the name of the provider, and `PROVIDER_VERSION` is the name of the version you are looking for.

For example, if you want to see version `10.0.0` of the `apache-airflow-providers-google` package, then run `git checkout providers-google/10.0.0`.

  3. For `backport-providers` packages, which are used in Airflow 1, run `git checkout backport-providers-PROVIDER_VERSION`.

For example, if you want to see version `2021.3.3` of the `apache-airflow-backport-providers-google` package,then run `git checkout backport-providers-2021.3.3`.

  4. If you don't know the filepath for the operator, you can search for it with the `git grep` command. The following example demonstrates how to search for GoogleCloudStorageCreateBucketOperator.
         
         git grep GoogleCloudStorageCreateBucketOperator
         

The output is a list of files where the string (in this case, the operator's name) can be found. From that list, navigate to the file and examine its contents further.
         
         airflow/contrib/operators/gcs_operator.py:class
         GoogleCloudStorageCreateBucketOperator(BaseOperator):
         
         airflow/contrib/operators/gcs_operator.py:            CreateBucket =
         GoogleCloudStorageCreateBucketOperator(
         
         airflow/contrib/operators/gcs_operator.py:        super(
         GoogleCloudStorageCreateBucketOperator, self).__init__(*args, **kwargs)
         docs/code.rst:.. autoclass:: airflow.contrib.operators.gcs_operator.Google
         CloudStorageCreateBucketOperator
         docs/integration.rst:- :ref:`GoogleCloudStorageCreateBucketOperator` :
         Creates a new cloud storage bucket.
         docs/integration.rst:.. _GoogleCloudStorageCreateBucketOperator:
         docs/integration.rst:GoogleCloudStorageCreateBucketOperator
         docs/integration.rst:.. autoclass:: airflow.contrib.operators.gcs_operator
         .GoogleCloudStorageCreateBucketOperator
         tests/contrib/operators/test_gcs_operator.py:from
         airflow.contrib.operators.gcs_operator import
         GoogleCloudStorageCreateBucketOperator
         tests/contrib/operators/test_gcs_operator.py:        operator =
         GoogleCloudStorageCreateBucketOperator(
         


**Note:** Running these commands switches your local repository to this tag and leaves it in a ['detached HEAD' state](https://git-scm.com/docs/git-checkout). This is expected. Follow the instructions in your terminal to switch back to a branch.

## What's next

  * Run a local Airflow environment with the [Composer Local Development CLI tool](https://docs.cloud.google.com/composer/docs/latest/run-local-airflow-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
