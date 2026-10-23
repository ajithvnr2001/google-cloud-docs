---
url: https://docs.cloud.google.com/assured-open-source-software/docs/download-python-packages/
title: Download Python packages using direct repository access for the free tier \u00a0|\u00a0 Assured Open Source Software \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:58.003677+00:00
---

# Download Python packages using direct repository access for the free tier  |  Assured Open Source Software  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-open-source-software/docs/download-python-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Open Source Software ](https://docs.cloud.google.com/assured-open-source-software/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-open-source-software/docs/service-account-creation)



Send feedback 

#  Download Python packages using direct repository access for the free tier Stay organized with collections  Save and categorize content based on your preferences. 

In the free tier, Assured Open Source Software packages are hosted in a Google-managed Artifact Registry repository.

This page explains how you can connect to the Artifact Registry repository for Assured OSS to directly access and download the Python packages.

This document applies to the free tier only. For the premium tier, see [Download Python packages using direct repository access](https://docs.cloud.google.com/security-command-center/docs/aoss-download-python-packages).

## Before you begin

  1. Request your administrator to grant you the [Service Account Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions#iam.serviceAccountKeyAdmin) (`roles/iam.serviceAccountKeyAdmin`) IAM role on your organization. You need this permission to get the base64-encoded string of the service account key. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  2. Configure Assured OSS. For the free tier, submit the [customer enablement form](https://developers.google.com/assured-oss#get-started) to enable access to Assured OSS.

  3. [Validate connectivity](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection) to Assured OSS for the requested service accounts.

  4. [Enable the Artifact Registry API](https://docs.cloud.google.com/artifact-registry/docs/enable-service) for the parent Google Cloud project of the service accounts used to access Assured OSS.

  5. Install the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install). If you have installed the Google Cloud CLI previously, make sure you have the latest version by running this command:
         
         gcloud components update
         




## Set up authentication

You can authenticate to the Assured OSS Python package repository using one of the following methods:

  * Authenticate with Python keyring
  * Authenticate with a service account key



The following sections describe how to set up these authentication methods.

### Authenticate with Python keyring

To authenticate with the Artifact Registry using Python, we recommend using [Python keyring](https://pypi.org/project/keyring/). For more information, see [authenticating with keyring](https://docs.cloud.google.com/artifact-registry/docs/python/authentication#keyring) and [credential search order](https://docs.cloud.google.com/artifact-registry/docs/python/authentication#search-order).

To set up the Python keyring for authentication, do the following:

  1. Install the `keyring` library:
         
         pip install keyring
         

  2. Install the Artifact Registry backend:
         
         pip install keyrings.google-artifactregistry-auth
         

  3. List backends to confirm the installation:
         
         keyring --list-backends
         

The list should include the following:

     * `ChainerBackend(priority:10)`
     * `GooglePythonAuth(priority:9)`
  4. For information about setting up [Application Default Credentials](https://docs.cloud.google.com/docs/authentication#adc), see [Set up authentication](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection#set_up_authentication).

This step ensures that the Assured OSS credential helper obtains your key when connecting with the repositories.




### Authenticate with a service account key

Authenticate with a service account key when the application requires authentication with a username and a password.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

Replace the package repository URL `https://us-python.pkg.dev/cloud-aoss/cloud-aoss-python/simple` with the URL `https://_json_key_base64:$BASE64_KEY@us-python.pkg.dev/cloud-aoss/cloud-aoss-python/simple`

## Install packages

The following instructions assume that you're using PyPI and `requirements.txt` to download and manage your dependencies. If you're using any other dependency management process, you must use different steps.

### Install packages in Assured OSS

To specify the Assured OSS Python packages that you want to download, create two `requirements.txt` files. The sample files are the following:

  * `requirements-google.txt`
        
        # Packages present in Google's Artifact Registry
        
        urllib3==1.26.11 --hash=sha256:1cffe1aa066363a75c856f261c8fce62d87f7c40ce0f46453ea12bf652b12a13
        jsonschema==4.13.0 --hash=sha256:29895bfe55b93b75552fbdd1e09aa0c82b7c1c9395d4f267e10c7d43cd31a74e
        

  * `requirements-pypi.txt`
        
        # Packages present in Google's Artifact Registry are mentioned here so that pip
        # downloads their dependencies from PyPI.
        
        urllib3==1.26.11
        jsonschema==4.13.0
        
        # Below this comment, add any package version which you need but is NOT
        # present in Google's Artifact Registry and therefore needs to be downloaded from
        # PyPI.
        


**Note:** To generate the `requirements-google.txt` for your environment, see [Generating the `requirements-google.txt` file](https://docs.cloud.google.com/assured-open-source-software/docs/pythonaccess#download_hash).

To download the packages, run the following commands:

  * To download the required packages that are in the Artifact Registry for Assured OSS, run the following:
        
        pip install --require-hashes --requirement=requirements-google.txt \
             --index-url https://_json_key_base64:$BASE64_KEY@us-python.pkg.dev/cloud-aoss/cloud-aoss-python/simple -v \
             --no-deps
        

Consider the following:

    * `--require-hashes` is optional. If included, hashes are specified for all packages and for all package versions in the `requirements.txt` file.
    * `-v` is optional. If specified, the command gives more [output](https://pip.pypa.io/en/stable/cli/pip/#cmdoption-v). We recommend pinning dependencies with SHA-256 hashes in your `requirements.txt` file to ensure security and reproducibility.
  * To download the required packages that aren't in the Artifact Registry for Assured OSS, run the following:
        
        pip install --requirement=requirements-pypi.txt --index-url https://pypi.org/simple -v
        

This command also downloads the missing dependencies of the packages that you have downloaded using the previous command.




## Access packages not available in the Artifact Registry repository for Assured OSS

Assured OSS is pre-configured with Assured OSS as the preferred repository and canonical public repositories, such as Maven Central or PyPI, as secondary repositories.

To use this feature ([preview](https://cloud.google.com/products#product-launch-stages)), you can point to a single URL:

`https://us-python.pkg.dev/cloud-aoss/python/simple`

## List all Python packages available in Assured OSS

To use an [API](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.pythonPackages/list) to get a list of all the Python packages in the Artifact Registry repository, see [List all Python packages available in Assured OSS](https://docs.cloud.google.com/assured-open-source-software/docs/validate-connection#list_all_python_packages_available_in).

## Generating the `requirements-google.txt` file

This section provides additional information about generating the `requirements-google.txt` file that you need to download the Python packages. To download the hash and generate the `requirements-google.txt` file for your environment, you can use one of the following two options:

  * Use a script to generate a single requirements file for all artifacts.

  * Download a separate requirements file for each artifact.




The following sections provide more information about these options.

### Option 1: Use a script to generate a single requirements file for all artifacts

Use the `generator.sh` script to generate a single `requirements-google.txt` file for all the Python packages (along with their hashes) available with Assured OSS for Linux operating system. The packages must satisfy constraints such as Python version, machine architecture, and operating system. You can then delete the package versions that you don't need and use the resulting file.

The `generator.sh` script helps in the following two ways:

  * Generates the most recent list of Python package versions available with Assured OSS that can be successfully installed on your system.
  * Generates the `requirements-google.txt` file along with all the hashes.



The required script and its `README.md` file are available in a Cloud Storage bucket (`gs://cloud-aoss/utils/python-requirements-txt/v1.0`), which can be downloaded using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage).

To download the script and the `README.md` file, follow these steps:

  1. Authenticate with the service account to access the Cloud Storage bucket using the following command:
         
         gcloud auth activate-service-account --key-file KEY_FILE
         

Replace KEY_FILE with the path to the file containing the service account credentials.

  2. Download the `generator.sh` to your machine using the following command:
         
         gcloud storage cp gs://cloud-aoss/utils/python-requirements-txt/v1.0/generator.sh PATH_TO_LOCAL_STORE --recursive
         

Replace PATH_TO_LOCAL_STORE with the local path where you want to save the downloaded file.

  3. Download the `README.md` file using the following command:
         
         gcloud storage cp gs://cloud-aoss/utils/python-requirements-txt/v1.0/README.md PATH_TO_LOCAL_STORE --recursive
         

Replace PATH_TO_LOCAL_STORE with the local path where you want to save the downloaded file. The `README.md` file contains instructions on how to use the script.




To run the script, use the following commands:

  * To generate the `requirements-google.txt` file, run the following command:
        
        chmod +x generator.sh
         ./generator.sh
        

  * To get the information of the package in a CSV file, run the following command:
        
        chmod +x generator.sh
        ./generator.sh -i
        




### Option 2: Download `requirements.txt` for each required artifact

You can also download a separate `requirements.txt` (containing the hash) file for each Python artifact and then combine them into a single `requirements.txt` file.

Artifact hashes are available in a Cloud Storage bucket, which can be downloaded using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage). Hashes for each package and a version are located at the `gs://cloud-aoss/python/PACKAGE_NAME/VERSION` Cloud Storage bucket location.

To download the `requirements.txt` file, follow these steps:

  1. Authenticate with the service account to access the Cloud Storage bucket using the following command:
         
         gcloud auth activate-service-account --key-file KEY_FILE
         

Replace KEY_FILE with the path to the file containing the service account credentials.

  2. Download the `requirements.txt` of a specific package and version to your local machine using the following command:
         
         gcloud storage cp gs://cloud-aoss/python/PACKAGE_NAME/VERSION PATH_TO_LOCAL_STORE --recursive
         

Replace the following:

     * PACKAGE_NAME: the package name
     * VERSION: the version of the package
     * PATH_TO_LOCAL_STORE: the local path where you want to download the file

Sample command:

`gcloud storage cp gs://cloud-aoss/python/bleach/5.0.0 /tmp/bleach` \--recursive

Sample `requirements.txt` file:
    
    bleach==5.0.0 \
     --hash=sha256:6d286e765bfd3e309209cfa1d063e4d46afa966dea8cb97431c02b1e3067d812
    

The contents of each such `requirements.txt` file can be combined into a single `requirements-google.txt` file.




## What's next

  * [Set up virtual repository access](https://docs.cloud.google.com/assured-open-source-software/docs/virtual-repository-access)
  * [Supported Java and Python packages](https://docs.cloud.google.com/assured-open-source-software/docs/supported-packages)
  * [Access security metadata using Cloud Storage](https://docs.cloud.google.com/assured-open-source-software/docs/access-metadata-using-cloud-storage)
  * [Access security metadata using Artifact Analysis API](https://docs.cloud.google.com/assured-open-source-software/docs/access-metadata-using-container-analysis)
  * [Subscribe to notifications](https://docs.cloud.google.com/assured-open-source-software/docs/use-notifications)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
