---
url: https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies/
title: Install Python dependencies \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:40:42.729461+00:00
---

# Install Python dependencies  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Install Python dependencies Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies "View this page for Managed Airflow \(Legacy Gen 1\)")

This page describes how to install Python packages for your Managed Airflow environment.

## About packages in Managed Airflow

This section explains how PyPI packages work in Managed Airflow.

### Preinstalled and custom PyPI packages in Managed Airflow images

Managed Airflow images contains both preinstalled and custom PyPI packages.

  * _Preinstalled PyPI packages_ are packages that are included in the Managed Airflow image of your environment. Each [Managed Airflow image](https://docs.cloud.google.com/composer/docs/composer-versions#images) contains [PyPI packages](https://pypi.org) that are specific for your version of Managed Airflow and Airflow.

  * _Custom PyPI packages_ are packages that you can install in your environment in addition to preinstalled packages.


**Note:** If you plan to upgrade your environment, then you can do an [upgrade check](https://docs.cloud.google.com/composer/docs/composer-3/upgrade-environments#upgrade-check). This check reports if custom PyPI packages in your environment have any conflicts with preinstalled packages in a later Airflow build.

### Options to manage PyPI packages for Managed Airflow environments

Option | Use if  
---|---  
Install from PyPI |  The default way to install packages in your environment  
Install from a repository with a public IP address |  The package is hosted in a package repository other than PyPI. This repository has a public IP address  
Install from an Artifact Registry repository |  The package is hosted in an Artifact Registry repository  
Install from a repository in your project's network |  Your environment does not have access to public internet. The package is hosted in a package repository in your project's network.  
Install as a local Python library |  The package cannot be found in PyPI, and the library does not have any external dependencies, such as `dist-packages`.  
[Install a plugin](https://docs.cloud.google.com/composer/docs/composer-3/install-plugins) |  The package provides plugin-specific functionality, such as modifying the Airflow web interface.  
[PythonVirtualenvOperator](https://airflow.apache.org/docs/apache-airflow-providers-standard/stable/operators/python.html#pythonvirtualenvoperator) |  You don't want the package to be installed for all Airflow workers, or the dependency conflicts with preinstalled packages. The package can be found in the PyPI and has no external dependencies.  
[KubernetesPodOperator](https://docs.cloud.google.com/composer/docs/composer-3/use-kubernetes-pod-operator) and [GKE operators](https://docs.cloud.google.com/composer/docs/composer-3/use-gke-operator) |  You require external dependencies that cannot be installed from `pip`, such as `dist-packages`, or are on an internal pip server. This option requires more setup and maintenance. Consider it only if other options don't work.  
  
## Before you begin

  * You must have a role that can trigger environment update operations. In addition, the service account of the environment must have [a role](https://docs.cloud.google.com/composer/docs/composer-3/access-control) that has enough permissions to perform update operations.

**Important:** When you install PyPI packages in your environment, **Airflow executes Python code from the installed package**. Make sure that you install packages that come from sources that you can trust. Users with the `composer.environments.update` permission can execute Python code on behalf of the environment's service account when installing packages in your environment. For more information, see [Access control](https://docs.cloud.google.com/composer/docs/composer-3/access-control#service-account-security).
  * If your environment is protected by a VPC Service Controls perimeter, then before installing PyPI dependencies you must [grant additional user identities](https://docs.cloud.google.com/composer/docs/composer-3/configure-vpc-sc) with access to services that the service perimeter protects and enable support for a private PyPI repository.

  * Requirements must follow the format specified in [PEP-508](https://peps.python.org/pep-0508/#grammar) where each requirement is specified in lowercase and consists of the package name with optional extras and version specifiers.

  * If a dependency conflict causes the update to fail, your environment continues running with its existing dependencies. If the operation succeeds, you can begin using the newly installed Python dependencies in your DAGs.

  * PythonVirtualenvOperator doesn't use the configuration from your environment's `pip.conf` file. If you want to use specific dependencies, including installing them from a custom index, pass requirements in the `requirements` parameter as a list of strings. For more information about the format, see [Requirements File Format](https://pip.pypa.io/en/stable/reference/requirements-file-format/#supported-options) in the pip documentation.




## View the list of PyPI packages

You can get the list of packages for your environment in several formats.

### View preinstalled packages

To view the list of preinstalled packages for your environment, see the list of packages for the [Managed Airflow image of your environment](https://docs.cloud.google.com/composer/docs/composer-versions).

### View all packages

To view all packages (both preinstalled and custom) in your environment:

###  gcloud 

The following gcloud CLI command returns the result of the `python -m pip list` command for an Airflow worker in your environment. You can use the `--tree` argument to get the result of the `python -m pipdeptree --warn` command.
    
    
    gcloud beta composer environments list-packages \
        ENVIRONMENT_NAME \
        --location LOCATION
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



### View custom PyPI packages

###  Console 

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **PyPI Packages** tab.




###  gcloud 
    
    
    gcloud composer environments describe ENVIRONMENT_NAME \
      --location LOCATION \
      --format="value(config.softwareConfig.pypiPackages)"
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



## Install custom packages in a Managed Airflow environment

This section describes different methods for installing custom packages in your environment.

### Install packages from PyPI

A package can be installed from [Python Package Index](https://pypi.org) if it has no external dependencies or conflicts with preinstalled packages.

**Note:** You can loosen version constraints for installed custom PyPI packages. For example, instead of specifying a version as `==1.0.1`, specify it as `>=1.0.1`.

To add, update, or delete the Python dependencies for your environment:

###  Console 

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **PyPI packages** tab.

  4. Click **Edit**

  5. Click **Add package**.

  6. In the **PyPI packages** section, specify package names, with optional version specifiers and extras.

For example:

     * `scikit-learn`
     * `scipy`, `>=0.13.3`
     * `nltk`, `[machine_learning]`
  7. Click **Save**.




###  gcloud 

gcloud CLI has several arguments for working with custom PyPI packages:

  * `--update-pypi-packages-from-file` replaces all existing custom PyPI packages with the specified packages. Packages that you don't specify are removed.
  * `--update-pypi-package` updates or installs one package.
  * `--remove-pypi-packages` removes specified packages.
  * `--clear-pypi-packages` removes all packages.



**Installing requirements from a file**

The `requirements.txt` file must have each [requirement specifier](https://peps.python.org/pep-0508/#grammar) on a separate line.

For example:
    
    
    scipy>=0.13.3
    scikit-learn
    nltk[machine_learning]
    

Update your environment, and specify the `requirements.txt` file in the `--update-pypi-packages-from-file` argument.
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
        --location LOCATION \
         --update-pypi-packages-from-file requirements.txt
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



**Installing one package**

Update your environment, and specify the package, version, and extras in the `--update-pypi-package` argument.
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
        --location LOCATION \
         --update-pypi-package PACKAGE_NAMEEXTRAS_AND_VERSION
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `PACKAGE_NAME` with the name of the package.
  * `EXTRAS_AND_VERSION` with the optional version and extras specifier. To omit versions and extras, specify an empty value.

**Note:** Depending on your execution environment, you might need to escape special characters such as `>`. To avoid potential issues, put the package name and version in quotes, for example: `"scipy>=0.13.0"`.

Example:
    
    
    gcloud composer environments update example-environment \
        --location us-central1 \
        --update-pypi-package "scipy>=0.13.3"
    

**Removing packages**

Update your environment, and specify the packages that you want to delete in the `--remove-pypi-packages` argument:
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
        --location LOCATION \
         --remove-pypi-packages PACKAGE_NAMES
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `PACKAGE_NAMES` with a comma-separated list of packages.



Example:
    
    
    gcloud composer environments update example-environment \
        --location us-central1 \
        --remove-pypi-packages scipy,scikit-learn
    

###  API 

Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

In this request:

  1. In the `updateMask` parameter, specify the mask:

     * Use `config.softwareConfig.pypiPackages` mask to replace all existing packages with the specified packages. Packages that you don't specify are deleted.
     * Use `config.softwareConfig.pypiPackages.PACKAGE_NAME` to add or update a specific package. To add or update several packages, specify several masks with commas.
  2. In the request body, specify packages and values for versions and extras:
         
         {
           "config": {
             "softwareConfig": {
               "pypiPackages": {
                 "PACKAGE_NAME": "EXTRAS_AND_VERSION"
               }
             }
           }
         }
         

Replace:

     * `PACKAGE_NAME` with the name of the package.
     * `EXTRAS_AND_VERSION` with the optional version and extras specifier. To omit versions and extras, specify an empty value.
     * To add more than one package, add extra entries for packages to `pypiPackages`.



Example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.softwareConfig.pypiPackages.EXAMPLE_PACKAGE,
    // config.softwareConfig.pypiPackages.ANOTHER_PACKAGE
    {
      "config": {
        "softwareConfig": {
          "pypiPackages": {
            "EXAMPLE_PACKAGE": "",
            "ANOTHER_PACKAGE": ">=1.10.3"
          }
        }
      }
    }
    

###  Terraform 

The `pypi_packages` block in the `software_config` block specifies packages.
    
    
    resource "google_composer_environment" "example" {
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
    
        software_config {
    
          pypi_packages = {
              PACKAGE_NAME = "EXTRAS_AND_VERSION"
          }
    
        }
      }
    }
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `PACKAGE_NAME` with the name of the package.
  * `EXTRAS_AND_VERSION` with the optional version and extras specifier. To omit versions and extras, specify an empty value.
  * To add more than one package, add extra entries for packages to `pypi_packages`.



Example:
    
    
    resource "google_composer_environment" "example" {
      name = "example-environment"
      region = "us-central1"
    
      config {
    
        software_config {
          pypi_packages = {
              scipy = ">=1.10.3"
              scikit-learn = ""
              nltk = "[machine_learning]"
          }
        }
      }
    }
    

### Install packages from a public repository

You can install packages hosted in other repositories that have a public IP address.

The packages must be [properly configured](https://pip.pypa.io/en/stable/topics/configuration/), so that the default `pip` tool can install it.

**Note:** Managed Airflow does not support `pip` customization and does not resolve package dependencies and conflicts outside of the resolution mechanisms that the default `pip` tool provides.

To install from a package repository that has a public address:

  1. Create a [pip.conf](https://pip.pypa.io/en/stable/topics/configuration/) file and include the following information in the file, if applicable:

     * URL of the repository (in the `index-url` parameter)
     * Access credentials for the repository
     * Non-default `pip` installation options

Example:
    
    [global]
    index-url=https://example.com/
    

  2. (Optional) In some cases, you might want to fetch packages from multiple repositories, such as when the public repository contains some specific packages that you want to install, and you want to install all other packages from PyPI:

     1. Configure an [Artifact Registry virtual repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo).
     2. Add configuration for multiple repositories (including PyPI, if needed) and define the order in which `pip` searches the repositories.
     3. Specify the virtual repository's URL in the `index-url` parameter.
  3. [Determine the URI of your environment's bucket](https://docs.cloud.google.com/composer/docs/composer-3/manage-dags#bucket).

  4. [Upload](https://docs.cloud.google.com/storage/docs/uploading-objects) the pip.conf file to the `/config/pip/` folder in your environment's bucket.

  5. Install packages using one of the available methods.




### Install packages from an Artifact Registry repository

You can [store packages in an Artifact Registry repository](https://docs.cloud.google.com/artifact-registry/docs/python/store-python) in your project, and configure your environment to install from it.

**Note:** If you use VPC Service Controls, then you can [create Artifact Registry PyPI repository in VPC mode](https://docs.cloud.google.com/artifact-registry/docs/securing-with-vpc-sc#ar-vpc). In this case, follow the procedure for private repositories when assigning permissions.

Configure roles and permissions:

  1. Make sure that the Cloud Build service account has [permissions to read from your Artifact Registry repository](https://docs.cloud.google.com/artifact-registry/docs/access-control#roles).

  2. If your environment has restricted access to other services in your project, for example, if you use VPC Service Controls:

     1. Assign permissions to access your Artifact Registry repository to the environment's service account instead of the Cloud Build service account.

     2. Make sure that connectivity to the Artifact Registry repository is configured in your project.




To install custom PyPI packages from an Artifact Registry repository:

  1. Create a [pip.conf](https://pip.pypa.io/en/stable/topics/configuration/) file and include the following information in the file, if applicable:

     * URL of the Artifact Registry repository (in the `index-url` parameter)
     * Access credentials for the repository
     * Non-default `pip` installation options

For an Artifact Registry repository, append `/simple/` to the repository URL:
    
    [global]
    index-url = https://us-central1-python.pkg.dev/example-project/example-repository/simple/
    

  2. (Optional) In some cases, you might want to fetch packages from multiple repositories, such as when your Artifact Registry repository contains some specific packages that you want to install, and you want to install all other packages from PyPI:

     1. Configure an [Artifact Registry virtual repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo).
     2. Add configuration for multiple repositories (including PyPI, if needed) and define the order in which `pip` searches the repositories.
     3. Specify the virtual repository's URL in the `index-url` parameter.
  3. [Upload](https://docs.cloud.google.com/composer/docs/composer-3/manage-dags#add) this pip.conf file to the `/config/pip/` folder in your environment's bucket. For example: `gs://us-central1-example-bucket/config/pip/pip.conf`.

  4. Install packages using one of the available methods.




### Install packages from a private repository

You can host a private repository in your project's network and configure your environment to install Python packages from it.

Configure roles and permissions:

  1. If you install custom PyPI packages from a repository in your project's network, and this repository does not have a public IP address:

     1. Assign permissions to access this repository to the environment's service account.

     2. Make sure that connectivity to this repository is configured in your project.




To install packages from a private repository hosted in your project's network:

  1. Create a [pip.conf](https://pip.pypa.io/en/stable/topics/configuration/) file and include the following information in the file, if applicable:

     * IP address of the repository in your project's network
     * Access credentials for the repository
     * Non-default `pip` installation options

Example:
    
    [global]
    index-url=https://192.0.2.10/
    

  2. (Optional) In some cases, you might want to fetch packages from multiple repositories, such as when the private repository contains some specific packages that you want to install, and you want to install all other packages from PyPI:

     1. Configure an [Artifact Registry virtual repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo).
     2. Add configuration for multiple repositories (including PyPI, if needed) and define the order in which `pip` searches the repositories.
     3. Specify the virtual repository's URL in the `index-url` parameter.
  3. (Optional) You can use a custom certificate when installing packages from your private repository. To do so:

     1. [Upload](https://docs.cloud.google.com/composer/docs/composer-3/manage-dags#add) the certificate file to the `/config/pip/` folder in your environment's bucket.

**Caution:** **Don't upload private keys**. Upload only a public certificate bundle in the PEM format. Verify that the certificate bundle contains the correct root CA.
     2. In pip.conf, specify the name of the certificate file in the `cert` parameter. Don't change the `/etc/pip/` folder.

Example:
            
            [global]
            cert =/etc/pip/example-certificate.pem
            

  4. [Upload](https://docs.cloud.google.com/composer/docs/composer-3/manage-dags#add) the pip.conf file to the `/config/pip/` folder in your environment's bucket. For example: `gs://us-central1-example-bucket/config/pip/pip.conf`.

  5. Install packages using one of the available methods.




### Install a local Python library

To install an in-house or local Python library:

  1. Place the dependencies within a subdirectory in the `dags/` folder in your environment's bucket. To import a module from a subdirectory, each subdirectory in the module's path must contain an `__init__.py` package marker file.

In the following example, the dependency is [`coin_module.py`](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/composer/workflows/dependencies):
         
         dags/
           use_local_deps.py  # A DAG file.
           dependencies/
             __init__.py
             coin_module.py
         

  2. Import the dependency from the DAG definition file.

For example:



    
    
    from dependencies import coin_module
    

**Note:** An import error occurs if an `__init__.py` file is missing. Directory and file names must be valid Python identifiers.

### Use packages that depend on shared object libraries

Certain PyPI packages depend on system-level libraries. While Managed Airflow does not support system libraries, you can use the following options:

  * Use the [KubernetesPodOperator](https://docs.cloud.google.com/composer/docs/composer-3/use-kubernetes-pod-operator). Set the Operator image to a custom build image. If you experience packages that fail during installation due to an unmet system dependency, use this option.

  * Upload the shared object libraries to your environment's bucket. If your PyPI packages have installed successfully but fail at runtime, use this option.

    1. Manually find the shared object libraries for the PyPI dependency (an .so file).
    2. Upload the shared object libraries to the `/plugins` folder in your environment's bucket.
    3. [Set the following environment variable](https://docs.cloud.google.com/composer/docs/composer-3/set-environment-variables): `LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/airflow/gcs/plugins`

**Note:** Files in the `plugins/` folders [are synced to the local file system](https://docs.cloud.google.com/composer/docs/composer-3/cloud-storage). Uploading large .so files can affect the performance of your environment and the Airflow web server.

## Install packages in private IP environments

Depending on how you configure your project, your environment might not have access to the public internet.

By default, your Managed Airflow (Gen 3) environment **can access the internet when installing PyPI packages**. This works in all environment's networking types (Private and Public IP). For example, you can install packages from [Python Package Index](https://pypi.org) in a Private IP environment.

For more information, see [Configure access to the internet when installing PyPI packages](https://docs.cloud.google.com/composer/docs/composer-3/packages-internet-access).

### Private IP environment with public internet access

If your private IP environment can access public internet, then you can install packages using options for public IP environments:

  * Install from PyPI. In this case, no special configuration is required. Follow the procedure described in Install packages from PyPI.
  * Install from a repository with a public IP address. Follow the procedure described in Install packages from a public repository.
  * Install from a private PyPI repository hosted in your project's network.



### Private IP environment without internet access

If your private IP environment does not have access to public internet, then you can install packages using one of the following ways:

  * Use a private PyPI repository hosted in your project's network.
  * Use a [proxy server](https://pip.pypa.io/en/stable/user_guide/#using-a-proxy-server) VM in your project's network to connect to a PyPI repository on the public internet. Specify the proxy address in the `/config/pip/pip.conf` file in your environment's bucket.
  * Use an Artifact Registry repository as the only source of packages. To do so, redefine the `index-url` parameter, as described.
  * If your security policy permits access to external IP addresses from your VPC network, you can enable the installation of packages from repositories on the public internet by configuring [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview).
  * Put Python dependencies into the `/dags` folder in your environment's bucket to install them as local libraries. This might not be a good option if the dependency tree is large.



### Install to a private IP environment under resource location restrictions

Keeping your project in line with Resource Location Restriction requirements prohibits the use of some tools. In particular, Cloud Build cannot be used for package installation, preventing direct access to repositories on the public internet.

To install Python dependencies in such an environment, follow the guidance for a private IP environments without internet access.

### Install a Python dependency to a private IP environment in a VPC Service Controls perimeter

Protecting your project with a [VPC Service Controls perimeter](https://docs.cloud.google.com/composer/docs/composer-3/composer-security-overview#vpc_sc_support) results in further security restrictions. In particular, Cloud Build cannot be used for package installation, preventing direct access to repositories on the public internet.

To install Python dependencies for a private IP environment inside a perimeter, follow the guidance for private IP environments without internet access.

## What's next

  * [Troubleshooting package installation](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-package-installation)
  * [Troubleshooting updates and upgrades](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-updates-upgrades)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
