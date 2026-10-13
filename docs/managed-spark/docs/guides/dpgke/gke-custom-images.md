---
url: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-custom-images/
title: Create a Google Kubernetes Engine custom container image \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:20.217250+00:00
---

# Create a Google Kubernetes Engine custom container image  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/gke-custom-images/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Create a Google Kubernetes Engine custom container image Stay organized with collections  Save and categorize content based on your preferences. 

You can specify a custom container image to use with Managed Service for Apache Spark on GKE . Your custom container image must use one of the Managed Service for Apache Spark on GKE base Spark images.

## Use a custom container image

To use a Managed Service for Apache Spark on GKE custom container image, set the `spark.kubernetes.container.image property` when you [create a Managed Service for Apache Spark on GKE virtual cluster](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/quickstarts/dataproc-gke-quickstart-create-cluster) or [submit a Spark job](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/quickstarts/dataproc-gke-quickstart-create-cluster#submit_a_spark_job) to the cluster.

**Note:** The `spark:` file prefix is needed when creating a cluster, but omitted when submitting a job (see [Cluster properties](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#formatting)).

  * gcloud CLI cluster creation example: 
        
        gcloud dataproc clusters gke create "${DP_CLUSTER}" \
            --properties=spark:spark.kubernetes.container.image=custom-image \
            ... other args ...
        

  * gcloud CLI job submit example: 
        
        gcloud dataproc jobs submit spark \
            --properties=spark.kubernetes.container.image=custom-image \
            ... other args ...
        




## Custom container image requirements and settings

### Base images

You can use `docker` tools for building customized docker based upon one of the published Managed Service for Apache Spark on GKE base Spark images.

### Container user

Managed Service for Apache Spark on GKE runs Spark containers as the Linux `spark` user with a `1099` UID and a `1099` GID. Use the UID and GID for filesystem permissions. For example, if you add a jar file at `/opt/spark/jars/my-lib.jar` in the image as a workload dependency, you must give the `spark` user read permission to the file.

### Components

  * **Java:** The `JAVA_HOME` environment variable points to the location of the Java installation. The current default value is `/usr/lib/jvm/adoptopenjdk-8-hotspot-amd64`, which is subject to change (see the [Managed Service for Apache Spark release notes](https://docs.cloud.google.com/managed-spark/docs/release-notes) for updated information).

    * If you customize the Java environment, make sure that `JAVA_HOME` is set to the correct location and `PATH` includes the path to binaries.
  * **Python:** Managed Service for Apache Spark on GKE [base Spark images](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/dataproc-gke-versions) have Miniconda3 installed at `/opt/conda`. `CONDA_HOME` points to this location, `${CONDA_HOME}/bin` is included in `PATH`, and `PYSPARK_PYTHON` is set to `${CONDA_HOME}/python`.

    * If you customize Conda, make sure that `CONDA_HOME` points to the Conda home directory ,`${CONDA_HOME}/bin` is included in `PATH`, and `PYSPARK_PYTHON` is set to `${CONDA_HOME}/python.`

    * You can install, remove, and update packages in the default base environment, or create a new environment, but it is strongly recommended that the environment include all packages installed in the base environment of the base container image.

    * If you add Python modules, such as a Python script with utility functions, to the container image, include the module directories in `PYTHONPATH`.

  * **Spark:** Spark is installed in `/usr/lib/spark`, and `SPARK_HOME` points to this location. **Spark cannot be customized.** If it is changed, the container image will be rejected or fail to operate correctly.

    * **Jobs** : You can customize Spark job dependencies. `SPARK_EXTRA_CLASSPATH` defines the extra classpath for Spark JVM processes. Recommendation: put jars under `/opt/spark/jars`, and set `SPARK_EXTRA_CLASSPATH` to `/opt/spark/jars/*`. 

If you embed the job jar in the image, the recommended directory is `/opt/spark/job`. When you submit the job, you can reference it with a local path, for example, `file:///opt/spark/job/my-spark-job.jar`.

    * **Cloud Storage connector:** The Cloud Storage connector is installed at `/usr/lib/spark/jars`.

    * **Utilities** : The `procps` and `tini` utility packages are required to run Spark. These utilities are included in the base Spark images, so custom images do not need to re-install them.

    * **Entrypoint:** **Managed Service for Apache Spark on GKE ignores any changes made to the`ENTRYPOINT` and `CMD` primitives in the container image.**

    * **Initialization scripts:** you can add an optional initialization script at `/opt/init-script.sh`. An initialization script can download files from Cloud Storage, start a proxy within the container, call other scripts, and perform other startup tasks. 

The entrypoint script calls the initialization script with all command line args (`$@`) before starting the Spark driver, Spark executor, and other processes. The initialization script can select the type of Spark process based on the first arg (`$1`): possible values include `spark-submit` for driver containers, and `executor` for executor containers.

  * **Configs:** Spark configs are located under `/etc/spark/conf`. The `SPARK_CONF_DIR` environment variable points to this location.

Don't customize Spark configs in the container image. Instead, submit any properties via the Managed Service for Apache Spark on GKE API for the following reasons:

    * Some properties, such as executor memory size, are determined at runtime, not at container image build time; they must be injected by Managed Service for Apache Spark on GKE .
    * Managed Service for Apache Spark on GKE places restrictions on the properties supplied by users. Managed Service for Apache Spark on GKE mounts configs from `configMap` into `/etc/spark/conf` in the container, overriding settings embedded in the image.



## Base Spark images

Managed Service for Apache Spark supports the following base Spark container images:

  * [Spark 3.5](https://docs.cloud.google.com/managed-spark/docs/guides/dpgke/dataproc-gke-versions#spark_engine_35): ${REGION}-docker.pkg.dev/cloud-dataproc/spark/dataproc_2.2



## Sample custom container image build

### Sample Dockerfile
    
    
    FROM us-central1-docker.pkg.dev/cloud-dataproc/spark/dataproc_2.0:latest
    
    # Change to root temporarily so that it has permissions to create dirs and copy
    # files.
    USER root
    
    # Add a BigQuery connector jar.
    ENV SPARK_EXTRA_JARS_DIR=/opt/spark/jars/
    ENV SPARK_EXTRA_CLASSPATH='/opt/spark/jars/*'
    RUN mkdir -p "${SPARK_EXTRA_JARS_DIR}" \
        && chown spark:spark "${SPARK_EXTRA_JARS_DIR}"
    COPY --chown=spark:spark \
        spark-bigquery-with-dependencies_2.12-0.22.2.jar "${SPARK_EXTRA_JARS_DIR}"
    
    # Install Cloud Storage client Conda package.
    RUN "${CONDA_HOME}/bin/conda" install google-cloud-storage
    
    # Add a custom Python file.
    ENV PYTHONPATH=/opt/python/packages
    RUN mkdir -p "${PYTHONPATH}"
    COPY test_util.py "${PYTHONPATH}"
    
    # Add an init script.
    COPY --chown=spark:spark init-script.sh /opt/init-script.sh
    
    # (Optional) Set user back to `spark`.
    USER spark
    

### Build the container image

Run the following commands in the Dockerfile directory

  1. Set image (example: `us-central1-docker.pkg.dev/my-project/spark/spark-test-image:latest`) and change to build directory. 
         
         IMAGE=custom container image \
             BUILD_DIR=$(mktemp -d) \
             cd "${BUILD_DIR}"
         

  2. Download the BigQuery connector. 
         
         gcloud storage cp \
             gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.22.2.jar .
         

  3. Create a Python example file. 
         
         cat >test_util.py <<'EOF'
         def hello(name):
           print("hello {}".format(name))  
         
         def read_lines(path):
           with open(path) as f:
             return f.readlines()
         EOF
         

  4. Create an example init script. 
         
         cat >init-script.sh <<EOF
         echo "hello world" >/tmp/init-script.out
         EOF
         

  5. Build and push the image. 
         
         docker build -t "${IMAGE}" . && docker push "${IMAGE}"
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
