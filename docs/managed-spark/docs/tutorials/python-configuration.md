---
url: https://docs.cloud.google.com/managed-spark/docs/tutorials/python-configuration/
title: Configure the Python environment \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:57.610149+00:00
---

# Configure the Python environment  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/tutorials/python-configuration/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Configure the Python environment Stay organized with collections  Save and categorize content based on your preferences. 

PySpark jobs on Managed Service for Apache Spark are run by a Python interpreter on the cluster. Job code must be compatible at runtime with the Python interpreter version and dependencies.

## Check interpreter version and modules

The following `check_python_env.py` sample program checks the Linux user running the job, the Python interpreter, and available modules.
    
    
    import getpass
    import importlib.util
    import sys
    
    print(f'This job is running as "{getpass.getuser()}".')
    print(sys.executable, sys.version_info)
    for package in sys.argv[1:]:
      print(importlib.util.find_spec(package))

Run the program:
    
    
    REGION=region
    gcloud dataproc jobs submit pyspark check_python_env.py \
        --cluster=my-cluster \
        --region=${REGION} \
        -- pandas scipy
    

Sample output: 
    
    
    This job is running as "root".
    /opt/conda/default/bin/python sys.version_info(major=3, minor=11, micro=8, releaselevel='final', serial=0)
    ModuleSpec(name='pandas', loader=<_frozen_importlib _external.SourceFileLoader object at 0x7f8b9c0a3d90 >, origin='/opt/conda/default/lib/python3.11/site-packages/pandas/__init_ _.py', submodule_search_locations=['/opt/conda/default/lib/python3.11/site-packages/pandas'])
    ModuleSpec(name='scipy', loader=<_frozen_importlib _external.SourceFileLoader object at 0x7f8b9c0a3e50 >, origin='/opt/conda/default/lib/python3.11/site-packages/scipy/__init_ _.py', submodule_search_locations=['/opt/conda/default/lib/python3.11/site-packages/scipy'])
    

## Managed Service for Apache Spark image Python environments

The following sections describe the Python environments for supported Managed Service for Apache Spark image version clusters.

### Managed Service for Apache Spark image version 2.x

[Conda](https://docs.conda.io/projects/conda/en/stable/) (or `micromamba` in 2.3 images) is installed on Managed Service for Apache Spark 2.x clusters. The default Python 3 interpreter is located on the VM instance under `/opt/conda/default/bin`. The following pages list the Python version included in supported Managed Service for Apache Spark 2.x image versions:

  * [2.1](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-2.1)
  * [2.2](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-2.2)
  * [2.3](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-2.3)



The non-default Python interpreter from the OS is available under `/usr/bin/`.

You can install `conda` and `pip` packages in the `base` environment or set up your own `conda` environment on the cluster using conda-related cluster properties.

**Conda channel note** : Default Managed Service for Apache Spark `2.1`, `2.2`, and `2.3` image versions don't include pre-configured Conda package channels (such as `defaults` or `conda-forge`) in `.condarc` (see the [September 4, 2026 release note](https://docs.cloud.google.com/managed-spark/docs/release-notes#September_04_2026)). Passing unprefixed package names to `dataproc:conda.packages` or running `conda install PACKAGE` without specifying a channel fails with `CondaValueError: No channels available to install from` or `PackagesNotFoundError`.

For more information, including affected image versions, extension requests, and recommended migration steps, see [Migrate and set up Conda channels](https://docs.cloud.google.com/managed-spark/docs/guides/conda-channel-migration). 

To install Conda packages, you must explicitly specify the channel:

  * When using the `dataproc:conda.packages` property, use the `CHANNEL::PACKAGE==VERSION` format (for example, `dataproc:conda.packages=conda-forge::pip==24.0`).
  * When running `conda install` on the command line, pass the `-c` (or `--channel`) flag (for example, `conda install PACKAGES -c conda-forge`).



Example:
    
    
    REGION=region
    gcloud dataproc clusters create my-cluster \
        --image-version=2.3 \
        --region=${REGION} \
        --properties=^#^dataproc:conda.packages='conda-forge::pytorch==2.1.0,conda-forge::coverage==6.5.0'#dataproc:pip.packages='tokenizers==0.15.0,datasets==2.16.1'
    

### Managed Service for Apache Spark image version 3.0

Python 3 is installed on Managed Service for Apache Spark [3.0](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-3.0) clusters. In 3.0 images, [Pixi](https://pixi.prefix.dev) is installed as part of the Python installation and is used to install Python packages instead of Conda.

### Avoid package download issues

Managed Service for Apache Spark cluster nodes download packages from external public Python repositories when installing custom `conda` and `pip` packages (see conda-related cluster properties). To avoid cluster creation failures due to the unavailability of public Python repositories, consider creating a Managed Service for Apache Spark custom image or uploading the dependencies to a Cloud Storage bucket (see [Download dependencies with internal-ip-only clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/network#download_dependencies_with_internal-ip-only_clusters)).

## Choose a Python interpreter for a job

If multiple Python interpreters are installed on your cluster, the system runs `/etc/profile.d/effective-python.sh`, which exports the `PYSPARK_PYTHON` environment variable to choose the default Python interpreter for your PySpark jobs. If you need a non-default Python interpreter for a PySpark job, when you submit the job to your cluster, set the `spark.pyspark.python` and `spark.pyspark.driver.python` properties to the required Python path or version (for example, "/usr/bin/python3" or "python3.11").

Example:
    
    
    REGION=region
    gcloud dataproc jobs submit pyspark check_python_env.py \
        --cluster=my-cluster \
        --region=${REGION} \
        --properties="spark.pyspark.python=/usr/bin/python3,spark.pyspark.driver.python=/usr/bin/python3"
    

## Python with sudo

If you connect to a cluster node using SSH, when you run `sudo python --version`, the displayed Python version can be different from the version displayed by `python --version`. This version difference can occur because `sudo` uses the default system Python `/usr/bin/python`, and does not execute `/etc/profile.d/effective-python.sh` to initialize the Python environment. For a consistent experience when using `sudo`, locate the Python path set in `/etc/profile.d/effective-python.sh`, then run the `env` command to set the `PATH` to this Python path. For example:
    
    
    sudo env PATH=/opt/conda/default/bin:${PATH} python --version
    

## Use conda-related cluster properties

You can customize the `conda` environment during cluster creation using conda-related [cluster properties](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#dataproc_service_properties_table).

There are two mutually exclusive ways to customize the conda environment when you create a Managed Service for Apache Spark cluster:

  1. Use the `dataproc:conda.env.config.uri` cluster property to create and activate a new conda environment on the cluster. **or**

  2. Use the `dataproc:conda.packages` and `dataproc:pip.packages` cluster properties to add `conda` and `pip` packages, respectively, to the `conda` `base` environment on the cluster.

**Warning:** Cluster creation can time out depending on the time required to install the new packages or environment specified by the properties. The timeout is set at 10 minutes.



### conda-related cluster properties

  * **`dataproc:conda.env.config.uri`:** The absolute path to a conda environment YAML config file located in Cloud Storage. This file is used to create and activate a new `conda` environment on the cluster. Because default images don't include pre-configured Conda channels, ensure that your `environment.yaml` file explicitly lists the required package channels (such as `conda-forge`) under `channels`.

**Note:** The `dataproc:conda.env.config.uri` cluster property cannot be used with the `dataproc:conda.packages` or `dataproc:pip.packages` cluster properties.

Example:

    1. Get or create a conda `environment.yaml` config file. You can [manually create the file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually), use an existing file, or [export an existing conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment) into an `environment.yaml` file using the following command: 
           
           conda env export --name=env-name > environment.yaml
           

    2. Copy the config file to your Cloud Storage bucket. 
           
           gcloud storage cp environment.yaml gs://bucket-name/environment.yaml
           

    3. Create the cluster and point to your environment config file in Cloud Storage. 
           
           REGION=region
           gcloud dataproc clusters create cluster-name \
               --region=${REGION} \
               --properties='dataproc:conda.env.config.uri=gs://bucket-name/environment.yaml' \
               ... other flags ...
           

  * **`dataproc:conda.packages`:** A list of `conda` packages with specific channels and versions to be installed in the base environment, formatted as `CHANNEL::PACKAGE==VERSION` (for example, `conda-forge::pkg1==v1,conda-forge::pkg2==v2...`). If `conda` fails to resolve conflicts with existing packages in the base environment, the conflicting packages won't be installed.

Notes:

    * Because default Managed Service for Apache Spark `2.1`, `2.2`, and `2.3` image versions don't include pre-configured Conda channels in `.condarc`, you must prefix each package name with its channel (such as `conda-forge::`). Passing unprefixed package names fails with `CondaValueError: No channels available to install from` or `PackagesNotFoundError`.

    * The `dataproc:conda.packages` and `dataproc:pip.packages` cluster properties cannot be used with the `dataproc:conda.env.config.uri` cluster property.

    * When specifying multiple packages (separated by a comma), you must specify an alternate delimiter character (see cluster property [Formatting](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#formatting)). The following example specifies "#" as the delimiter character to pass multiple, comma-separated, package names to the `dataproc:conda.packages` property.

Example:
    
    REGION=region
    gcloud dataproc clusters create cluster-name \
        --region=${REGION} \
        --properties='^#^dataproc:conda.packages=conda-forge::pytorch==2.1.0,conda-forge::coverage==6.5.0' \
        ... other flags ...
    




  * **`dataproc:pip.packages`:** A list of `pip` packages with specific versions to be installed in the base environment, formatted as `pkg1==v1,pkg2==v2...`. `pip` upgrades existing dependencies only if required. Conflicts can cause the environment to be inconsistent.

Notes:

    * The `dataproc:pip.packages` and `dataproc:conda.packages` cluster properties cannot be used with the `dataproc:conda.env.config.uri` cluster property.

    * When specifying multiple packages (separated by a comma), you must specify an alternate delimiter character (see cluster property [Formatting](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#formatting)). The following example specifies "#" as the delimiter character to pass multiple, comma-separated, package names to the `dataproc:pip.packages` property.

Example:
    
    REGION=region
    gcloud dataproc clusters create cluster-name \
        --region=${REGION} \
        --properties='^#^dataproc:pip.packages=tokenizers==0.15.0,datasets==2.16.1' \
        ... other flags ...
    

  * You can use both `dataproc:conda.packages` and `dataproc:pip.packages` when creating a cluster.

Example:
        
        REGION=region
        gcloud dataproc clusters create cluster-name \
            --region=${REGION} \
            --image-version=2.3 \
            --properties=^#^dataproc:conda.packages='conda-forge::pytorch==2.1.0,conda-forge::coverage==6.5.0'#dataproc:pip.packages='tokenizers==0.15.0,datasets==2.16.1' \
            ... other flags ...
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
