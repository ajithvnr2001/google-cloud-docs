---
url: https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-package-installation/
title: Troubleshooting PyPI package installation \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:52.459372+00:00
---

# Troubleshooting PyPI package installation  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-package-installation/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Troubleshooting PyPI package installation Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-package-installation "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-package-installation "View this page for Managed Airflow \(Legacy Gen 1\)")

This page explains how to troubleshoot dependency conflicts when installing custom PyPI packages.

The most common problem with PyPI packages that you might encounter in Managed Airflow are dependency conflicts.

When you specify a new custom PyPI package to install, this package or its version might cause dependency conflicts with other custom PyPI packages or preinstalled packages in your environment. In this case, the environment update operation fails with an error.

## Cloud Build and in-cluster build errors

If a problem with packages occurs, you get the error message about it in two ways, depending on the way your environment is deployed:

  * **Cloud Build**. An error message and a link to the Cloud Build log. For example:
        
        UPDATE operation on this environment failed 25 minutes ago with the
        following error message:
        Failed to install PyPI packages.  Check the Cloud Build log at ...
        

  * **In-cluster builds**. An error message and the location of build logs. For example:
        
        UPDATE operation on this environment failed 17 minutes ago with the
        following error message:
        Failed to install PyPI packages.  Check the in-cluster build logs for
        details. They can be found in the Environment logs under the build-log-*
        log name.
        




## See the detailed error message

When a package installation fails, `pip` reports the detailed error message. You can find this error message in the build logs.

### Locate the `pip` error in Cloud Build logs

You can follow the link from the Cloud Build error message, or locate build logs:

  1. Locate build logs:

     1. In Google Cloud console, go to the **Build history** page.

[Go to Build history](https://console.cloud.google.com/cloud-build/builds)

     2. Select the failed build to see its logs.

  2. In the build log, find the error message from `pip`. For example:
         
         ERROR: apache-airflow-backport-providers-google 2021.2.5 has requirement
         google-cloud-logging<3.0.0,>=2.1.1, but you'll have google-cloud-logging
         1.15.0 which is incompatible.
         




### Locate the `pip` error in in-cluster build logs

  1. Locate build logs:

     1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

     2. Select your environment.

     3. Open the **Logs** tab.

     4. Select **All logs** > **Composer logs** > **Builds** > **Worker & Scheduler image**.

     5. In the **Severity** drop-down list, select **Info**.

  2. In the displayed logs:

     1. Locate the `installer.sh` error message. For example:
            
            The command '/bin/sh -c bash installer.sh $COMPOSER_PYTHON_VERSION
            fail' returned a non-zero code: 1
            

     2. The preceding info messages have the detailed `pip` error. For example:
            
            apache-airflow-backport-providers-google 2021.2.5 has requirement
            google-cloud-logging<3.0.0,>=2.1.1, but you have
            google-cloud-logging 1.15.0.
            




## Timeouts during Python package installation

In recent versions, the `pip` utility changed its behavior when attempting to satisfy dependencies. If specified dependencies can't be satisfied, `pip` goes through all available versions of a package.

When you install a package, the following happens:

  1. If the package is [already preinstalled](https://docs.cloud.google.com/composer/docs/composer-versions) in your environment and Python dependencies that you specify don't require any changes, the package remains as it is.

Example: `aiodebug==2.3.0` is installed and you specify `aiodebug` or `aiodebug>=2`.

  2. If the package isn't already installed in your environment or it doesn't satisfy Python dependencies you specify, then `pip` tries to use the latest version that satisfies dependencies. This is either the latest version of the package if you didn't specify a version, or the latest version of the package that satisfies the specified restrictions.

Example: If you specify `aiodebug`, then the latest will be installed (2.*.*). If you specify `aiodebug<2`, then 1.*.* will be installed.

If this version causes dependency conflicts with preinstalled packages, `pip` **goes through all available versions** of the package to try to satisfy the specified dependency. When it happens, the following messages will be visible in the build log:
         
         INFO: pip is looking at multiple versions of PYTHON_PACKAGE_NAME
         to determine which version is compatible with other requirements.
         This could take a while.
         

Before the change, `pip` failed with a dependency conflict without checking other versions.




Going through all available versions can take a significant amount of time and lead to a downgrade of packages or to a timeout during the Python package installation.

Preinstalled packages in Managed Airflow are regularly updated to the latest versions for security reasons. Therefore, a timeout can also occur when you upgrade an environment to a later Managed Airflow version.

**Possible solutions:**

  * Regularly update custom Python dependencies.

  * Use [PythonVirtualenvOperator](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/operators/python.html#pythonvirtualenvoperator) to isolate code snippets that require conflicting packages.




## Conflicts with preinstalled PyPI packages

Some package conflicts occur between custom PyPI packages that you install and the preinstalled packages.

You can see the full list of preinstalled packages for your version of Managed Airflow on the [Managed Airflow versions](https://docs.cloud.google.com/composer/docs/composer-versions) page.

To solve this problem, you can:

  * Install a different version of the custom PyPI package.

  * Install a different version of the preinstalled package. To do so, [install a custom PyPI package](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies#install-pypi) with the name of the preinstalled package and specify the required version. We do not recommend downgrading preinstalled packages.

  * See if later [Managed Airflow versions](https://docs.cloud.google.com/composer/docs/composer-versions) use a different version of the preinstalled package. You can [check for potential PyPI package conflicts](https://docs.cloud.google.com/composer/docs/composer-2/upgrade-environments#upgrade-check) before you upgrade your environment to a later version of Managed Airflow.

  * Use [PythonVirtualenvOperator](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/operators/python.html#pythonvirtualenvoperator) to isolate code snippets that require conflicting packages.




## Metadata server unavailable when installing PyPI packages

If your environment uses a [custom `pip.conf` file](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies), then you might face a problem when no new PyPI packages can be installed in your environment. In Cloud Build logs related to the package installation error, you can see the following warning message:
    
    
    WARNING: Compute Engine Metadata server unavailable on attempt 3 of 3. Reason:
    timed out
    WARNING: Authentication failed using Compute Engine authentication due to
    unavailable metadata server.
    

This problem is caused by a `pip.conf` file that does not allow access to the [default package index](https://pypi.org/simple) at `https://pypi.org/simple`. For example, if your `pip.conf` file only permits installing packages from a custom Artifact Registry repository because of the redefined `index-url` parameter, installing packages from the default package index is not available.

To solve this problem, make sure that `https://pypi.org/simple` package index is added to your `pip.conf` file. For example, if your primary package index is defined in the `index-url` parameter, add the `https://pypi.org/simple` index in the `extra-index-url` parameter.

**Warning:** When using `extra-index-url` parameter, make sure that the packages are installed from the repository you want to use. Sometimes, usage of `extra-index-url` parameter might lead to [Dependency Confusion](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies#public-dependencies) situations where a different version of a package might be installed than originally intended.

## What's next

  * [Installing Python dependencies](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies)
  * [Troubleshooting environment updates and upgrades](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-updates-upgrades)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
