---
url: https://docs.cloud.google.com/managed-spark/docs/guides/docker-yarn/
title: Customize your Spark job runtime environment with Docker on YARN \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:44.484778+00:00
---

# Customize your Spark job runtime environment with Docker on YARN  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/docker-yarn/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Customize your Spark job runtime environment with Docker on YARN Stay organized with collections  Save and categorize content based on your preferences. 

The Managed Service for Apache Spark **Docker on YARN** feature allows you to create and use a Docker image to customize your Spark job runtime environment. The image can include customizations to Java, Python, and R dependencies, and to your job jar.

### Limitations

Feature availability or support is **not available** with:

  * Managed Service for Apache Spark image versions prior to 2.0.49 (not available in 1.5 images)
  * MapReduce jobs (only supported for Spark jobs )
  * Spark client mode (only supported with Spark cluster mode)
  * [Kerberos clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/security#create_the_cluster): cluster creation fails if you create a cluster with Docker on YARN and Kerberos enabled.
  * Customizations of JDK, Hadoop and Spark: the host JDK, Hadoop, and Spark are used, not your customizations.



## Create a Docker image

The first step to customize your Spark environment is [building a Docker image](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/).

### Dockerfile

You can use the following Dockerfile as an example, making changes and additions to meet you needs.
    
    
    FROM debian:10-slim
    
    # Suppress interactive prompts.
    ENV DEBIAN_FRONTEND=noninteractive
    
    # Required: Install utilities required by Spark scripts.
    RUN apt update && apt install -y procps tini
    
    # Optional: Add extra jars.
    ENV SPARK_EXTRA_JARS_DIR=/opt/spark/jars/
    ENV SPARK_EXTRA_CLASSPATH='/opt/spark/jars/*'
    RUN mkdir -p "${SPARK_EXTRA_JARS_DIR}"
    COPY *.jar "${SPARK_EXTRA_JARS_DIR}"
    
    # Optional: Install and configure Miniconda3.
    ENV CONDA_HOME=/opt/miniconda3
    ENV PYSPARK_PYTHON=${CONDA_HOME}/bin/python
    ENV PYSPARK_DRIVER_PYTHON=${CONDA_HOME}/bin/python
    
    ENV PATH=${CONDA_HOME}/bin:${PATH}
    COPY Miniconda3-py39_4.10.3-Linux-x86_64.sh .
    RUN bash Miniconda3-py39_4.10.3-Linux-x86_64.sh -b -p /opt/miniconda3 \
      && ${CONDA_HOME}/bin/conda config --system --set always_yes True \
      && ${CONDA_HOME}/bin/conda config --system --set auto_update_conda False \
      && ${CONDA_HOME}/bin/conda config --system --prepend channels conda-forge \
      && ${CONDA_HOME}/bin/conda config --system --set channel_priority strict
    
    # Optional: Install Conda packages.
    #
    # The following packages are installed in the default image. It is strongly
    # recommended to include all of them.
    #
    # Use mamba to install packages quickly.
    RUN ${CONDA_HOME}/bin/conda install mamba -n base -c conda-forge \
        && ${CONDA_HOME}/bin/mamba install \
          conda \
          cython \
          fastavro \
          fastparquet \
          gcsfs \
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
          koalas \
          matplotlib \
          nltk \
          numba \
          numpy \
          openblas \
          orc \
          pandas \
          pyarrow \
          pysal \
          pytables \
          python \
          regex \
          requests \
          rtree \
          scikit-image \
          scikit-learn \
          scipy \
          seaborn \
          sqlalchemy \
          sympy \
          virtualenv
    
    # Optional: Add extra Python modules.
    ENV PYTHONPATH=/opt/python/packages
    RUN mkdir -p "${PYTHONPATH}"
    COPY test_util.py "${PYTHONPATH}"
    
    # Required: Create the 'yarn_docker_user' group/user.
    # The GID and UID must be 1099. Home directory is required.
    RUN groupadd -g 1099 yarn_docker_user
    RUN useradd -u 1099 -g 1099 -d /home/yarn_docker_user -m yarn_docker_user
    USER yarn_docker_user
    

### Build and push the image

The following is commands for building and pushing the example Docker image, you can make changes according to your customizations.
    
    
    # Increase the version number when there is a change to avoid referencing
    # a cached older image. Avoid reusing the version number, including the default
    # `latest` version.
    IMAGE=gcr.io/my-project/my-image:1.0.1
    
    # Download the BigQuery connector.
    gcloud storage cp \
      gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.22.2.jar .
    
    # Download the Miniconda3 installer.
    wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh
    
    # Python module example:
    cat >test_util.py <<EOF
    def hello(name):
      print("hello {}".format(name))
    
    def read_lines(path):
      with open(path) as f:
        return f.readlines()
    EOF
    
    # Build and push the image.
    docker build -t "${IMAGE}" .
    docker push "${IMAGE}"
    

## Create a Managed Service for Apache Spark cluster

After creating a Docker image that customizes your Spark environment, create a Managed Service for Apache Spark cluster that will use your Docker image when running Spark jobs.

### gcloud
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --image-version=DP_IMAGE \
        --optional-components=DOCKER \
        --properties=dataproc:yarn.docker.enable=true,dataproc:yarn.docker.image=DOCKER_IMAGE \
        other flags
    

Replace the following;

  * CLUSTER_NAME: The cluster name.
  * REGION: The cluster region.
  * DP_IMAGE: Managed Service for Apache Spark image version must be `2.0.49` or later (`--image-version=2.0` will use a qualified minor version later than `2.0.49`).
  * `--optional-components=DOCKER`: Enables the [Docker component](https://docs.cloud.google.com/managed-spark/docs/concepts/components/docker) on the cluster.
  * `--properties` flag: 
    * `dataproc:yarn.docker.enable=true`: Required property to enable the Managed Service for Apache Spark Docker on YARN feature.
    * `dataproc:yarn.docker.image`: Optional property that you can add to specify your DOCKER_IMAGE using the following Container Registry image naming format: `{hostname}/{project-id}/{image}:{tag}`. 

Example:
          
          dataproc:yarn.docker.image=gcr.io/project-id/image:1.0.1
          

**Requirement:** You must host your Docker image on [Container Registry](https://docs.cloud.google.com/container-registry) or [Artifact Registry](https://docs.cloud.google.com/artifact-registry). (Managed Service for Apache Spark cannot fetch containers from other registries).

**Recommendation:** Add this property when you create your cluster to cache your Docker image and avoid YARN timeouts later when you submit a job that uses the image.




When `dataproc:yarn.docker.enable` is set to `true`, Dataproc updates Hadoop and Spark configurations to enable the Docker on YARN feature in the cluster. For example, `spark.submit.deployMode` is set to `cluster`, and `spark.yarn.appMasterEnv.YARN_CONTAINER_RUNTIME_DOCKER_MOUNTS` and `spark.executorEnv.YARN_CONTAINER_RUNTIME_DOCKER_MOUNTS` are set to mount directories from the host into the container.

## Submit a Spark job to the cluster

After creating a Managed Service for Apache Spark cluster, submit a Spark job to the cluster that uses your Docker image. The example in this section submits a PySpark job to the cluster.

Set job properties:
    
    
    # Set the Docker image URI.
    IMAGE=(e.g., gcr.io/my-project/my-image:1.0.1)
    
    # Required: Use `#` as the delimiter for properties to avoid conflicts.
    JOB_PROPERTIES='^#^'
    
    # Required: Set Spark properties with the Docker image.
    JOB_PROPERTIES="${JOB_PROPERTIES}#spark.yarn.appMasterEnv.YARN_CONTAINER_RUNTIME_DOCKER_IMAGE=${IMAGE}"
    JOB_PROPERTIES="${JOB_PROPERTIES}#spark.executorEnv.YARN_CONTAINER_RUNTIME_DOCKER_IMAGE=${IMAGE}"
    
    # Optional: Add custom jars to Spark classpath. Don't set these properties if
    # there are no customizations.
    JOB_PROPERTIES="${JOB_PROPERTIES}#spark.driver.extraClassPath=/opt/spark/jars/*"
    JOB_PROPERTIES="${JOB_PROPERTIES}#spark.executor.extraClassPath=/opt/spark/jars/*"
    
    # Optional: Set custom PySpark Python path only if there are customizations.
    JOB_PROPERTIES="${JOB_PROPERTIES}#spark.pyspark.python=/opt/miniconda3/bin/python"
    JOB_PROPERTIES="${JOB_PROPERTIES}#spark.pyspark.driver.python=/opt/miniconda3/bin/python"
    
    # Optional: Set custom Python module path only if there are customizations.
    # Since the `PYTHONPATH` environment variable defined in the Dockerfile is
    # overridden by Spark, it must be set as a job property.
    JOB_PROPERTIES="${JOB_PROPERTIES}#spark.yarn.appMasterEnv.PYTHONPATH=/opt/python/packages"
    JOB_PROPERTIES="${JOB_PROPERTIES}#spark.executorEnv.PYTHONPATH=/opt/python/packages"
    

Notes:

  * See [Launching Applications Using Docker Containers](https://hadoop.apache.org/docs/r3.2.3/hadoop-yarn/hadoop-yarn-site/DockerContainers.html) information on related properties.



### gcloud

Submit the job to the cluster.
    
    
    gcloud dataproc jobs submit pyspark PYFILE \
        --cluster=CLUSTER_NAME \
        --region=REGION \
        --properties=${JOB_PROPERTIES}
    

Replace the following;

  * PYFILE: The file path to your PySpark job file. It can be a local file path or the URI of the file in Cloud Storage (`gs://BUCKET_NAME/PySpark filename`).
  * CLUSTER_NAME: The cluster name.
  * REGION: The cluster region.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
