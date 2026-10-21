---
url: https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers/
title: Use custom containers \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:44.788894+00:00
---

# Use custom containers  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use custom containers Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark serverless runs workloads within [Docker](https://www.docker.com/) containers. The container provides the runtime environment for the workload's driver and executor processes. By default, Managed Service for Apache Spark uses a container image that includes the default Spark, Java, Python and R packages associated with a [runtime release version](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/spark-runtime-versions). The Managed Service for Apache Spark [batches](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.batches) API lets you use a custom container image instead of the default image. Typically, a custom container image adds Spark workload Java or Python dependencies not provided by the default container image. **Important:** Do not include Spark in your custom container image; Managed Service for Apache Spark will mount Spark into the container at runtime.

## Submit a Spark batch workload using a custom container image

### gcloud

Use the [gcloud dataproc batches submit spark](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit) command with the `--container-image` flag to specify your custom container image when you submit a Spark batch workload.
    
    
    gcloud dataproc batches submit spark \
        --container-image=custom-image, for example, "gcr.io/my-project-id/my-image:1.0.1" \
        --region=[region](https://docs.cloud.google.com/compute/docs/regions-zones#available) \
        --jars=path to user workload jar located in Cloud Storage or included in the custom container \
        --class=The fully qualified name of a class in the jar file, such as org.apache.spark.examples.SparkPi \
        -- add any workload arguments here
    

**Notes:**

  * **Custom-image:** Specify the custom container image using the following Container Registry image naming format: `{hostname}/{project-id}/{image}:{tag}`, for example, "gcr.io/my-project-id/my-image:1.0.1". **Note:** You must host your custom container image on [Container Registry](https://docs.cloud.google.com/container-registry) or [Artifact Registry (GAR)](https://docs.cloud.google.com/artifact-registry). (Managed Service for Apache Spark cannot fetch containers from other registries). 
  * **`--jars`:** Specify a path to a user workload included in your custom container image or located in Cloud Storage, for example, `file:///opt/spark/jars/spark-examples.jar` or `gs://my-bucket/spark/jars/spark-examples.jar`.
  * **Other batches command options:** You can add other optional batches command flags, for example, to use a [Persistent History Server (PHS)](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/history-server). Note: The PHS must be located in the region where you run batch workloads. See [`gcloud dataproc batches submit`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/batches/submit) for supported command flags.
  * **workload arguments:** You can add any workload arguments by adding a "--" to the end of the command, followed by the workload arguments.



### REST

The custom container image is provided through the [RuntimeConfig.containerImage](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/RuntimeConfig#FIELDS.container_image) field as part of a [batches.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.batches/create) API request.

The following example shows how to use a custom container to submit a batch workload using the Managed Service for Apache Spark batches.create API.

Before using any of the request data, make the following replacements: 

  * project-id: Google Cloud project ID
  * region: [region](https://docs.cloud.google.com/compute/docs/regions-zones#available)
  * custom-container-image: Specify the custom container image using the following Container Registry image naming format: `{hostname}/{project-id}/{image}:{tag}`, for example, "gcr.io/my-project-id/my-image:1.0.1". Note: You must host your custom container on [Container Registry](https://docs.cloud.google.com/container-registry) or [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry). (Managed Service for Apache Spark cannot fetch containers from other registries).
  * **[`jar-uri`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.batches#SparkBatch.FIELDS.jar_file_uris):** Specify a path to a workload jar included in your custom container image or located in Cloud Storage, for example, "/opt/spark/jars/spark-examples.jar" or "gs:///spark/jars/spark-examples.jar". 
  * **`class`:** The fully qualified name of a class in the jar file, such as "org.apache.spark.examples.SparkPi".
  * **Other options:** You can use other batch workload resource fields, for example, use the [](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.batches#SparkBatch.FIELDS.args)`sparkBatch.args` field to pass arguments to your workload (see the [`Batch`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.batches) resource documentation for more information). To use a [Persistent History Server (PHS)](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.batches#sparkhistoryserverconfig), see [Setting up a Persistent History Server](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/history-server#setting_up_a_persistent_history_server). Note: The PHS must be located in the region where you run batch workloads. 



HTTP method and URL: 
    
    
    POST https://dataproc.googleapis.com/v1/projects/project-id/locations/region/batches

Request JSON body: 
    
    
    {
      "runtimeConfig":{
        "containerImage":"custom-container-image
      },
      "sparkBatch":{
        "jarFileUris":[
          "jar-uri"
        ],
        "mainClass":"class"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataproc.googleapis.com/v1/projects/project-id/locations/region/batches"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataproc.googleapis.com/v1/projects/project-id/locations/region/batches" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
    "name":"projects/project-id/locations/region/batches/batch-id",
      "uuid":",uuid",
      "createTime":"2021-07-22T17:03:46.393957Z",
      "runtimeConfig":{
        "containerImage":"gcr.io/my-project/my-image:1.0.1"
      },
      "sparkBatch":{
        "mainClass":"org.apache.spark.examples.SparkPi",
        "jarFileUris":[
          "/opt/spark/jars/spark-examples.jar"
        ]
      },
      "runtimeInfo":{
        "outputUri":"gs://dataproc-.../driveroutput"
      },
      "state":"SUCCEEDED",
      "stateTime":"2021-07-22T17:06:30.301789Z",
      "creator":"account-email-address",
      "runtimeConfig":{
        "properties":{
          "spark:spark.executor.instances":"2",
          "spark:spark.driver.cores":"2",
          "spark:spark.executor.cores":"2",
          "spark:spark.app.name":"projects/project-id/locations/region/batches/batch-id"
        }
      },
      "environmentConfig":{
        "peripheralsConfig":{
          "sparkHistoryServerConfig":{
          }
        }
      },
      "operation":"projects/project-id/regions/region/operation-id"
    }
    

## Build a custom container image

Managed Service for Apache Spark custom container images are Docker images. You can use the tools for building Docker images to build custom container images, but there are conditions the images must meet to be compatible with Managed Service for Apache Spark. The following sections explain these conditions.

### Operating system

You can choose any operating system base image for your custom container image.

Recommendation: Use the default Debian 12 images, for example, `debian:12-slim`, since they have been tested to avoid compatibility issues.

### Utilities

You must include the following utility packages, which are required to run Spark, in your custom container image:

  * `procps`
  * `tini`



To run XGBoost from Spark (Java or Scala), you must include `libgomp1`

### Container user

Managed Service for Apache Spark runs containers as the `spark` Linux user with a `1099` UID and a `1099` GID. `USER` directives set in custom container image Dockerfiles are ignored at runtime. Use the UID and GID for file system permissions. For example, if you add a jar file at `/opt/spark/jars/my-lib.jar` in the image as a workload dependency, you must give the `spark` user read permission to the file.

### Image streaming

Managed Service for Apache Spark normally begins a workload requiring a custom container image by downloading the entire image to disk. This can mean a delay in initialization time, especially for customers with large images.

You can instead use image streaming, which is a method to pull image data on an as-needed basis. This lets the workload start up without waiting for the entire image to download, potentially improving initialization time. To enable image streaming, you must enable the [Container File System API](https://console.cloud.google.com/apis/library/containerfilesystem.googleapis.com). You must also store your container images in Artifact Registry, and the Artifact Registry repository must be in the same region as your Managed Service for Apache Spark workload or in a multi-region that corresponds with the region where your workload is running. If Managed Service for Apache Spark does not support the image or the image streaming service is not available, our streaming implementation downloads the entire image.

Note that we don't support the following for image streaming:

  * Images with empty layers or duplicate layers
  * Images that use the [V2 Image Manifest, schema version 1](https://docs.docker.com/registry/spec/manifest-v2-1/)



In these cases, Managed Service for Apache Spark pulls the entire image before starting the workload.

#### Additional requirements

  * If VPC Service Controls protects your container images and you use Image streaming, you must also include the Image streaming API (`containerfilesystem.googleapis.com`) in the service perimeter.

  * If the Spark workload doesn't use the default service account, you must ensure that your custom service account has the [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/understanding-roles) (`roles/serviceusage.serviceUsageConsumer`) IAM role in the project that hosts the container image.




### Spark

Don't include Spark in your custom container image. At runtime, Managed Service for Apache Spark mounts Spark binaries and configs from the host into the container: binaries are mounted to the `/usr/lib/spark` directory and configs are mounted to the `/etc/spark/conf` directory. Existing files in these directories are overridden by Managed Service for Apache Spark at runtime.

### Java Runtime Environment

Don't include your own Java Runtime Environment (JRE) in your custom container image. At run time, Managed Service for Apache Spark mounts `OpenJDK` from the host into the container. If you include a JRE in your custom container image, it will be ignored.

### Java packages

You can include jar files as Spark workload dependencies in your custom container image, and you can set the `SPARK_EXTRA_CLASSPATH` env variable to include the jars. Managed Service for Apache Spark will add the env variable value in the classpath of Spark JVM processes. Recommendation: put jars under the `/opt/spark/jars` directory and set `SPARK_EXTRA_CLASSPATH` to `/opt/spark/jars/*`.

You can include the workload jar in your custom container image, then reference it with a local path when submitting the workload, for example `file:///opt/spark/jars/my-spark-job.jar` (see Submit a Spark batch workload using a custom container image for an example).

### Python packages

By default, Managed Service for Apache Spark mounts a Conda environment build using an [OSS Conda-Forge repo](https://conda-forge.org/docs/) from the host to the `/opt/managed-spark/conda` directory in the container at runtime. `PYSPARK_PYTHON` is set to `/opt/managed-spark/conda/bin/python`. Its base directory, `/opt/managed-spark/conda/bin`, is included in `PATH`.

You can include your Python environment with packages in a different directory in your custom container image, for example in `/opt/conda`, and set the `PYSPARK_PYTHON` environment variable to `/opt/conda/bin/python`.

**Note:** Don't install your `pyspark` package. Managed Service for Apache Spark mounts `pyspark` into your container at runtime.

Your custom container image can include other Python modules that are not part of the Python environment, for example, Python scripts with utility functions. Set the `PYTHONPATH` environment variable to include the directories where the modules are located.

If your custom container sets Python-related environment variables that conflict with those set by Managed Service for Apache Spark, your values take precedence and will override the default values.

### R environment

You can customize the R environment in your custom container image using one of the following options:

  * Use Conda to manage and install R packages from `conda-forge` channel.
  * Add an R repository for your container image Linux OS, and install R packages using the Linux OS package manager (see the [R Software package index](https://cran.r-project.org/bin/linux/)).



When you use either option, you must set the `R_HOME` environment variable to point to your custom R environment. Exception: If you are using Conda to both manage your R environment and customize your Python environment, you don't need to set the `R_HOME` environment variable; it is automatically set based on the `PYSPARK_PYTHON` environment variable.

## Example custom container image build

This section includes custom container image build examples, which include sample [Dockerfiles](https://docs.docker.com/reference/dockerfile/), followed by build commands. One sample includes the minimum configuration required to build an image. The other sample includes examples of extra configuration, including Python and R libraries.

### Architecture co-location recommendation

To ensure rapid container initialization using Google Cloud Image streaming (Container File System API) and to prevent cross-regional data movement fees, the following services should all be located in the **same region** :

  * **Artifact Registry**
  * **Cloud Storage bucket**
  * **Managed Service for Apache Spark batch workload**



### Step 1: Environment configuration

Open your terminal or Google Cloud Shell and set up the following environment variables to simplify the deployment process.
    
    
    export PROJECT_ID="YOUR_PROJECT_ID"
    export REGION="us-east1"
    export REPO_NAME="spark-images"
    export BUCKET_NAME="spark-jobs-bucket-${PROJECT_ID}-${REGION}"
    

### Step 2: Dockerfile configuration

### Minimum configuration
    
    
    # Recommendation: Use Debian 12.
    FROM debian:12-slim
    
    # Suppress interactive prompts.
    ENV DEBIAN_FRONTEND=noninteractive
    
    # Install utilities required by Spark scripts.
    RUN apt update && apt install -y procps tini libjemalloc2
    
    # Enable jemalloc as default memory allocator.
    ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.2
    
    # Create the 'spark' group/user.
    # The GID and UID must be 1099. Home directory is required.
    RUN groupadd -g 1099 spark
    RUN useradd -u 1099 -g 1099 -d /home/spark -m spark
    
    USER spark
          

### Extra configuration
    
    
    # Recommendation: Use Debian 12.
    FROM debian:12-slim
    
    # Suppress interactive prompts.
    ENV DEBIAN_FRONTEND=noninteractive
    
    # Install utilities required by Spark scripts.
    RUN apt update && apt install -y procps tini libjemalloc2
    
    # Enable jemalloc as default memory allocator
    ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.2
    
    # Install utilities required by XGBoost for Spark.
    RUN apt install -y procps libgomp1
    
    # Install and configure Miniconda3.
    ENV CONDA_HOME=/opt/miniforge3
    ENV PYSPARK_PYTHON=${CONDA_HOME}/bin/python
    ENV PATH=${CONDA_HOME}/bin:${PATH}
    ADD https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh .
    RUN bash Miniforge3-Linux-x86_64.sh -b -p /opt/miniforge3 \
      && ${CONDA_HOME}/bin/conda config --system --set always_yes True \
      && ${CONDA_HOME}/bin/conda config --system --set auto_update_conda False \
      && ${CONDA_HOME}/bin/conda config --system --set channel_priority strict
    # Packages ipython and ipykernel are required if using custom conda and want to
    # use this container for running notebooks.
    RUN ${CONDA_HOME}/bin/mamba install ipython ipykernel
    
    # Install Google Cloud SDK.
    RUN ${CONDA_HOME}/bin/mamba install -n base google-cloud-sdk
    
    # Install Conda packages.
    #
    # The following packages are installed in the default image.
    # Recommendation: include all packages.
    #
    # Use mamba to quickly install packages.
    RUN ${CONDA_HOME}/bin/mamba install -n base \
        accelerate \
        bigframes \
        cython \
        deepspeed \
        evaluate \
        fastavro \
        fastparquet \
        gcsfs \
        google-cloud-aiplatform \
        google-cloud-bigquery-storage \
        google-cloud-bigquery[pandas] \
        google-cloud-bigtable \
        google-cloud-container \
        google-cloud-datacatalog \
        google-cloud-dataproc \
        google-cloud-datastore \
        google-cloud-language \
        google-cloud-logging \
        google-cloud-monitoring \
        google-cloud-pubsub \
        google-cloud-redis \
        google-cloud-spanner \
        google-cloud-speech \
        google-cloud-storage \
        google-cloud-texttospeech \
        google-cloud-translate \
        google-cloud-vision \
        langchain \
        lightgbm \
        koalas \
        matplotlib \
        mlflow \
        nltk \
        numba \
        numpy \
        openblas \
        orc \
        pandas \
        pyarrow \
        pynvml \
        pysal \
        pytables \
        python \
        pytorch-cpu \
        regex \
        requests \
        rtree \
        scikit-image \
        scikit-learn \
        scipy \
        seaborn \
        sentence-transformers \
        sqlalchemy \
        sympy \
        tokenizers \
        transformers \
        virtualenv \
        xgboost
    
    # Install pip packages.
    RUN ${PYSPARK_PYTHON} -m pip install \
        spark-tensorflow-distributor \
        torcheval
    
    # Install R and R libraries.
    RUN ${CONDA_HOME}/bin/mamba install -n base \
        r-askpass \
        r-assertthat \
        r-backports \
        r-bit \
        r-bit64 \
        r-blob \
        r-boot \
        r-brew \
        r-broom \
        r-callr \
        r-caret \
        r-cellranger \
        r-chron \
        r-class \
        r-cli \
        r-clipr \
        r-cluster \
        r-codetools \
        r-colorspace \
        r-commonmark \
        r-cpp11 \
        r-crayon \
        r-curl \
        r-data.table \
        r-dbi \
        r-dbplyr \
        r-desc \
        r-devtools \
        r-digest \
        r-dplyr \
        r-ellipsis \
        r-evaluate \
        r-fansi \
        r-fastmap \
        r-forcats \
        r-foreach \
        r-foreign \
        r-fs \
        r-future \
        r-generics \
        r-ggplot2 \
        r-gh \
        r-glmnet \
        r-globals \
        r-glue \
        r-gower \
        r-gtable \
        r-haven \
        r-highr \
        r-hms \
        r-htmltools \
        r-htmlwidgets \
        r-httpuv \
        r-httr \
        r-hwriter \
        r-ini \
        r-ipred \
        r-isoband \
        r-iterators \
        r-jsonlite \
        r-kernsmooth \
        r-knitr \
        r-labeling \
        r-later \
        r-lattice \
        r-lava \
        r-lifecycle \
        r-listenv \
        r-lubridate \
        r-magrittr \
        r-markdown \
        r-mass \
        r-matrix \
        r-memoise \
        r-mgcv \
        r-mime \
        r-modelmetrics \
        r-modelr \
        r-munsell \
        r-nlme \
        r-nnet \
        r-numderiv \
        r-openssl \
        r-pillar \
        r-pkgbuild \
        r-pkgconfig \
        r-pkgload \
        r-plogr \
        r-plyr \
        r-praise \
        r-prettyunits \
        r-processx \
        r-prodlim \
        r-progress \
        r-promises \
        r-proto \
        r-ps \
        r-purrr \
        r-r6 \
        r-randomforest \
        r-rappdirs \
        r-rcmdcheck \
        r-rcolorbrewer \
        r-rcpp \
        r-rcurl \
        r-readr \
        r-readxl \
        r-recipes \
        r-recommended \
        r-rematch \
        r-remotes \
        r-reprex \
        r-reshape2 \
        r-rlang \
        r-rmarkdown \
        r-rodbc \
        r-roxygen2 \
        r-rpart \
        r-rprojroot \
        r-rserve \
        r-rsqlite \
        r-rstudioapi \
        r-rvest \
        r-scales \
        r-selectr \
        r-sessioninfo \
        r-shape \
        r-shiny \
        r-sourcetools \
        r-spatial \
        r-squarem \
        r-stringi \
        r-stringr \
        r-survival \
        r-sys \
        r-teachingdemos \
        r-testthat \
        r-tibble \
        r-tidyr \
        r-tidyselect \
        r-tidyverse \
        r-timedate \
        r-tinytex \
        r-usethis \
        r-utf8 \
        r-uuid \
        r-vctrs \
        r-whisker \
        r-withr \
        r-xfun \
        r-xml2 \
        r-xopen \
        r-xtable \
        r-yaml \
        r-zip
    
    ENV R_HOME=/usr/lib/R
    
    # Add extra Python modules.
    ENV PYTHONPATH=/opt/python/packages
    RUN mkdir -p "${PYTHONPATH}"
    
    # Add extra jars.
    ENV SPARK_EXTRA_JARS_DIR=/opt/spark/jars/
    ENV SPARK_EXTRA_CLASSPATH='/opt/spark/jars/*'
    RUN mkdir -p "${SPARK_EXTRA_JARS_DIR}"
    
    # Uncomment below and replace EXTRA_JAR_NAME with the jar file name.
    # COPY "EXTRA_JAR_NAME" "${SPARK_EXTRA_JARS_DIR}"
    
    # Create the 'spark' group/user.
    # The GID and UID must be 1099. Home directory is required.
    RUN groupadd -g 1099 spark
    RUN useradd -u 1099 -g 1099 -d /home/spark -m spark
    
    USER spark
          

### Step 3: Build & push commands

Execute these commands to build and upload your container image into Artifact Registry using Cloud Build.

  1. **Create the Cloud Storage bucket:**
         
         gcloud storage buckets create gs://${BUCKET_NAME} --project=${PROJECT_ID} \
           --location=${REGION}
         

  2. **Create the Artifact Registry repository:**
         
         gcloud artifacts repositories create ${REPO_NAME} \
           --repository-format=docker --location=${REGION} --description="Custom Dataproc Serverless images"
         

  3. **Build and push the image using Cloud Build:**
         
         gcloud builds submit --tag ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/spark-custom:latest .
         




### Step 4: Job submission

Deploy the job by defining the runtime `--version=2.3` to avoid version drift issues. In production environments, providing the image version instead of the `:latest` tag is a best practice.

  * **Permissions:** Ensure the appropriate service account has the ** Artifact Registry Reader** ([`roles/artifactregistry.reader`](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader)) role on the Artifact Registry repository (recommended) or the project that hosts the container image. This is especially important if the image is hosted in a different project than where the workload runs. 
    * For runtime versions earlier than `3.0`, grant this permission to the workload or session [execution service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-accounts-serverless#pre-30_runtime_service_accounts). 
      * For runtime versions `3.0` and later, grant this permission to the [Dataproc Resource Manager Node Service Agent service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-accounts-serverless#30_runtime_service_accounts).


    
    
    gcloud dataproc batches submit pyspark \
      file:///usr/lib/spark/examples/src/main/python/pi.py \
      --region=${REGION} \
      --project=${PROJECT_ID} \
      --version=2.3 \
      --container-image=${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/spark-custom:latest \
      -- 10
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
