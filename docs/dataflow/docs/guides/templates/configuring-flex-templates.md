---
url: https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates/
title: Use Flex Templates to package a Dataflow pipeline for deployment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:39.326090+00:00
---

# Use Flex Templates to package a Dataflow pipeline for deployment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use Flex Templates to package a Dataflow pipeline for deployment Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a Flex Template for a Dataflow pipeline. Flex Templates let you package your Apache Beam pipeline code so that you can run the pipeline without having a development environment. By creating a Flex Template, anyone with the correct permissions can run your pipeline as a Dataflow job.

For an end-to-end tutorial on creating and running a Flex Template, see [Build and run an example Flex Template](https://docs.cloud.google.com/dataflow/docs/guides/templates/using-flex-templates).

## Overview

A Flex Template consists of the following components:

  * A container image stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview). The container is responsible for launching the Dataflow job.

  * A JSON specification file stored in [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction). This file contains a pointer to the container image and other metadata.




Before you create a Flex Template, you must use the Apache Beam SDK to write your pipeline code. For more information, see [Use Apache Beam to build pipelines](https://docs.cloud.google.com/dataflow/docs/guides/use-beam).

The program that constructs the pipeline must exit after `run` is called, in order for the pipeline to start. Don't call `waitUntilFinish` (Java) or `wait_until_finish` (Python), as these functions block and prevent the Flex Template from running.

## Required permissions

To get the permissions that you need to build a Flex Template, ask your administrator to grant you the following IAM roles on your project: 

  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Artifact Registry Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer) (`roles/artifactregistry.writer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Template metadata

Optionally, you can provide additional metadata for your template, including the following:

  * **Pipeline parameters** : Declare any [custom pipeline options](https://beam.apache.org/documentation/programming-guide/#creating-custom-options) that your pipeline uses. Dataflow validates the parameters when you submit the Flex Template job. If you run the template by using the Google Cloud console, the **Create job from template** dialog includes the pipeline parameters declared in the metadata.

  * **Streaming support** : You can specify whether the pipeline supports streaming, and if so, whether it supports exactly-once mode or at-least-once mode. This metadata enables the Google Cloud console to display the relevant pipeline options when you run the template.




To include additional metadata, create a JSON file with the metadata parameters. Specify this file in the [`--metadata-file`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/build#--metadata-file) flag of the `gcloud dataflow flex-template build` command. The contents of the metadata file are merged into the template specification file. For more information, see Build a Flex Template.

### Metadata parameters

Parameter key |  | Required | Description of the value  
---|---|---|---  
**`name`** |  | Yes | The name of your template.  
**`description`** |  | No | A short paragraph of text describing the template.  
**`streaming`** |  | No | If `true`, this template supports streaming. The default value is `false`.  
**`supportsAtLeastOnce`** |  | No | If `true`, this template supports at-least-once processing. The default value is `false`. Set this parameter to `true` if the template is designed to work with [at-least-once streaming mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes).   
**`supportsExactlyOnce`** |  | No | If `true`, this template supports [exactly-once processing](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once). The default value is `true`.  
**`defaultStreamingMode`** |  | No | The default streaming mode, for templates that support both at-least-once mode and exactly-once mode. Use one of the following values: `"AT_LEAST_ONCE"`, `"EXACTLY_ONCE"`. If unspecified, the default streaming mode is exactly-once.   
**`parameters`** |  | No | An array of additional parameters that the template uses. An empty array is used by default.  
**`name`** | Yes | The name of the parameter that is used in your template.  
**`label`** | Yes | A human readable string that is used in the Google Cloud console to label the parameter.  
**`helpText`** | Yes | A short paragraph of text that describes the parameter.  
**`isOptional`** | No | `false` if the parameter is required and `true` if the parameter is optional. Unless set with a value, `isOptional` defaults to `false`. If you do not include this parameter key for your metadata, the metadata becomes a required parameter.  
**`regexes`** | No | An array of POSIX-egrep regular expressions in string form that is used to validate the value of the parameter. For example, `["^[a-zA-Z][a-zA-Z0-9]+"]` is a single regular expression that validates that the value starts with a letter and then has one or more characters. An empty array is used by default.  
  
### Example metadata file

### Java
    
    
    {
      "name": "Streaming Beam SQL",
      "description": "An Apache Beam streaming pipeline that reads JSON encoded messages from Pub/Sub, uses Beam SQL to transform the message data, and writes the results to a BigQuery",
      "parameters": [
        {
          "name": "inputSubscription",
          "label": "Pub/Sub input subscription.",
          "helpText": "Pub/Sub subscription to read from.",
          "regexes": [
            "[a-zA-Z][-_.~+%a-zA-Z0-9]{2,}"
          ]
        },
        {
          "name": "outputTable",
          "label": "BigQuery output table",
          "helpText": "BigQuery table spec to write to, in the form 'project:dataset.table'.",
          "isOptional": true,
          "regexes": [
            "[^:]+:[^.]+[.].+"
          ]
        }
      ]
    }

### Python
    
    
    {
      "name": "Streaming beam Python flex template",
      "description": "Streaming beam example for python flex template.",
      "parameters": [
        {
          "name": "input_subscription",
          "label": "Input PubSub subscription.",
          "helpText": "Name of the input PubSub subscription to consume from.",
          "regexes": [
            "projects/[^/]+/subscriptions/[a-zA-Z][-_.~+%a-zA-Z0-9]{2,}"
          ]
        },
        {
          "name": "output_table",
          "label": "BigQuery output table name.",
          "helpText": "Name of the BigQuery output table name.",
          "isOptional": true,
          "regexes": [
            "([^:]+:)?[^.]+[.].+"
          ]
        }
      ]
    }

You can download metadata files for the Google-provided templates from the Dataflow [template directory](https://console.cloud.google.com/storage/browser/dataflow-templates/latest). 

**Note:** Changing launch parameters in the `metadata.json` file might cause the job to ignore, override, or discard the pipeline options passed by the template launcher. The job might fail to launch, or a job that doesn't use the Flex Template might launch. For more information, see [Specify pipeline options](https://docs.cloud.google.com/dataflow/docs/guides/templates/run-flex-templates#specify-options) and [Failed to read the job file](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-templates#read-job-file).

## Environment variables

When you build a Flex template, specify the following environment variables in the [`--env`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/build#--env) flag of the `gcloud dataflow flex-template build` command. If you are using a custom image, set these environment variables in your Dockerfile.

### Java

ENV | Description | Required  
---|---|---  
`FLEX_TEMPLATE_JAVA_MAIN_CLASS` |  Specifies which Java class to run in order to launch the Flex Template.  | YES  
`FLEX_TEMPLATE_JAVA_CLASSPATH` |  Specifies the location of class files.  | YES  
`FLEX_TEMPLATE_JAVA_OPTIONS` |  Specifies the Java options to be passed while launching the Flex Template.  | NO  
  
Specify `FLEX_TEMPLATE_JAVA_MAIN_CLASS` and `FLEX_TEMPLATE_JAVA_CLASSPATH` in your Dockerfile.

### Python

ENV | Description | Required  
---|---|---  
`FLEX_TEMPLATE_PYTHON_PY_FILE` |  Specifies which Python file to run to launch the Flex Template.  | YES  
`FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE` |  Specifies the requirements file with pipeline dependencies. For more information, see [PyPI dependencies](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/#pypi-dependencies) in the Apache Beam documentation.  | NO  
`FLEX_TEMPLATE_PYTHON_SETUP_FILE` |  Specifies the path to the pipeline package `setup.py` file. For more information, see [Multiple File Dependencies](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/#multiple-file-dependencies) in the Apache Beam documentation.  | NO  
`FLEX_TEMPLATE_PYTHON_EXTRA_PACKAGES` |  Specifies the packages that are not available publicly. For information on how using extra packages, read [Local or non-PyPI Dependencies](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/#local-or-nonpypi). | NO  
`FLEX_TEMPLATE_PYTHON_PY_OPTIONS` |  Specifies the Python options to be passed while launching the Flex Template.  | NO  
  
Specify `FLEX_TEMPLATE_PYTHON_PY_FILE` in your Dockerfile.

To manage pipeline dependencies, set variables in your Dockerfile, such as the following:

  * `FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE`
  * `FLEX_TEMPLATE_PYTHON_PY_OPTIONS`
  * `FLEX_TEMPLATE_PYTHON_SETUP_FILE`
  * `FLEX_TEMPLATE_PYTHON_EXTRA_PACKAGES`



For example, the following environment variables are set in the [Streaming in Python Flex Template tutorial](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/dataflow/flex-templates/streaming_beam/Dockerfile) in GitHub:
    
    
    ENV FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE="${WORKDIR}/requirements.txt"
    ENV FLEX_TEMPLATE_PYTHON_PY_FILE="${WORKDIR}/streaming_beam.py"
    

### Go

ENV | Description | Required  
---|---|---  
`FLEX_TEMPLATE_GO_BINARY` |  Specifies the Go binary file to run.  | YES  
  
Specify `FLEX_TEMPLATE_GO_BINARY` in your Dockerfile.

## Flex Template images

A Flex Template includes a container image that starts the Dataflow pipeline. When you run a Flex Template job, the Dataflow service downloads the container image from Artifact Registry and starts the container. The container is responsible for launching the Dataflow job.

Google maintains a set of [Flex Template base images](https://docs.cloud.google.com/dataflow/docs/reference/flex-templates-base-images) that you can use. However, if your pipeline requires a [custom container image](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers), then we recommend using the same image for the Flex Template. That way, the Flex Template launcher contains the same dependencies as the pipeline's runtime container.

### Custom container images

To create a custom Flex Template image, include the following steps in your Dockerfile:

  * Copy the Flex Template launcher binary from one of the Google-provided [base images](https://docs.cloud.google.com/dataflow/docs/reference/flex-templates-base-images) onto your image. The launcher binary is located at the following path:

### Java

`/opt/google/dataflow/java_template_launcher`

### Python

`/opt/google/dataflow/python_template_launcher`

### Go

`/opt/google/dataflow/go_template_launcher`

  * Copy the artifacts needed to launch the pipeline job, such as Python files, JAR files, or Go binaries.

  * Set the environment variables listed Environment variables.




The following example shows a Dockerfile for a Python pipeline:
    
    
    # Flex Template base image. Used here to get the launcher binary.
    FROM gcr.io/dataflow-templates-base/IMAGE_NAME:TAG as template_launcher
    
    # Apache Beam SDK image. This is the base image for the pipeline job.
    FROM apache/beam_python3.10_sdk:2.76.0
    
    # Customize the image for your pipeline.
    # [...]
    
    # Configure the Flex Template.
    COPY --from=template_launcher /opt/google/dataflow/python_template_launcher /opt/google/dataflow/python_template_launcher
    COPY my_pipeline.py /template/
    ENV FLEX_TEMPLATE_PYTHON_PY_FILE="/template/my_pipeline.py"
    

Replace the following:

  * `IMAGE_NAME`: a Google-provided base image. For example: `python311-template-launcher-base`.
  * `TAG`: a version tag for the base image listed in [Flex Templates base images](https://docs.cloud.google.com/dataflow/docs/reference/flex-templates-base-images). For better stability and troubleshooting, avoid using `latest`. Instead, pin to a specific version tag.

**Note:** The `COPY --from=template_launcher` instruction copies only the standalone launcher binary into the final image stage. Any OS, JDK, or Python runtime vulnerabilities detected by security scanners in your final custom image are likely inherited from the second-stage `FROM` base image (such as `apache/beam_python3.10_sdk`), not from Google's `dataflow-templates-base` image.

For a tutorial that follows this approach, see [Flex Template for a pipeline with dependencies and a custom container image](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/dataflow/flex-templates/pipeline_with_dependencies).

## Build a Flex Template

To build a Flex Template, use the [`gcloud dataflow flex-template build`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/build) command. This command creates the following artifacts:

  * The template specification file, stored in Cloud Storage
  * The launcher container image, stored in Artifact Registry



### Use a Google-provided base image

To run a Flex Template using a Google-provided base image, run the following command:

###  Java 
    
    
    gcloud dataflow flex-template build gs://BUCKET_NAME/TEMPLATE_FILE_NAME \
      --image-gcr-path "LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE:TAG" \
      --sdk-language "JAVA" \
      --flex-template-base-image "BASE_IMAGE" \
      --metadata-file "METADATA_FILE" \
      --jar "JAR_FILE" \
      --env "FLEX_TEMPLATE_JAVA_MAIN_CLASS=JAVA_MAIN_CLASS"

Replace the following:

  * `BUCKET_NAME`: the name of a Cloud Storage bucket to store the template specification file 
  * `TEMPLATE_FILE_NAME`: the name of the template specification file to create. Example: `my_template.json`
  * `LOCATION`: the location of your Artifact Registry repository 
  * `PROJECT_ID`: the Google Cloud project ID 
  * `REPOSITORY`: the name of your Artifact Registry repository 
  * `IMAGE`: the name of the Flex Template container image 
  * `TAG`: the tag for the Flex Template container image 
  * BASE_IMAGE: the base image to use. Specify one of the following: 
    * A predefined label, such as "JAVA17". For more information, see the documentation for the [ `--flex-template-base-image`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/build#--flex-template-base-image) flag. 
    * The full `gcr.io` path to a specific container version, in the following format: `gcr.io/dataflow-templates-base/IMAGE:TAG`. 
  * `METADATA_FILE`: the local path to a metafile file. For more information, see [Template metadata](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates#metadata). 
  * `JAR_FILE`: the local path to the JAR file for your pipeline code. If there are multiple JAR files, format them as a comma separated list or specify them in separate `--jar` flags. 
  * `JAVA_MAIN_CLASS`: the name of the Java class to run. For more information, see Environment variables. 



###  Python 
    
    
    gcloud dataflow flex-template build gs://BUCKET_NAME/TEMPLATE_FILE_NAME \
      --image-gcr-path "LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE:TAG" \
      --sdk-language "PYTHON" \
      --flex-template-base-image "BASE_IMAGE" \
      --metadata-file "METADATA_FILE" \
      --py-path "PYTHON_FILE_PATH" \
      --env "FLEX_TEMPLATE_PYTHON_PY_FILE=PYTHON_FILE"

Replace the following:

  * `BUCKET_NAME`: the name of a Cloud Storage bucket to store the template specification file 
  * `TEMPLATE_FILE_NAME`: the name of the template specification file to create. Example: `my_template.json`
  * `LOCATION`: the location of your Artifact Registry repository 
  * `PROJECT_ID`: the Google Cloud project ID 
  * `REPOSITORY`: the name of your Artifact Registry repository 
  * `IMAGE`: the name of the Flex Template container image 
  * `TAG`: the tag for the Flex Template container image 
  * BASE_IMAGE: the base image to use. Specify one of the following: 
    * A predefined label, such as "PYTHON3". For more information, see the documentation for the [ `--flex-template-base-image`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/build#--flex-template-base-image) flag. 
    * The full `gcr.io` path to a specific container version, in the following format: `gcr.io/dataflow-templates-base/IMAGE:TAG`. 
  * `METADATA_FILE`: the local path to a metafile file. For more information, see [Template metadata](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates#metadata). 
  * `PYTHON_FILE_PATH`: the local path to the Python files for your pipeline, and all of their dependent files. You can specify multiple paths as a comma-separated list or as separate `--py-path` flags. 
  * `PYTHON_FILE`: the Python file to run. For more information, see Environment variables. 



###  Go 
    
    
    gcloud dataflow flex-template build gs://BUCKET_NAME/TEMPLATE_FILE_NAME \
      --image-gcr-path "LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE:TAG" \
      --sdk-language "GO" \
      --flex-template-base-image "BASE_IMAGE" \
      --metadata-file "METADATA_FILE" \
      --go-binary-path="GO_FILE_PATH" \
      --env "FLEX_TEMPLATE_GO_BINARY=GO_BINARY"

Replace the following:

  * `BUCKET_NAME`: the name of a Cloud Storage bucket to store the template specification file 
  * `TEMPLATE_FILE_NAME`: the name of the template specification file to create. Example: `my_template.json`
  * `LOCATION`: the location of your Artifact Registry repository 
  * `PROJECT_ID`: the Google Cloud project ID 
  * `REPOSITORY`: the name of your Artifact Registry repository 
  * `IMAGE`: the name of the Flex Template container image 
  * `TAG`: the tag for the Flex Template container image 
  * BASE_IMAGE: the base image to use. Specify one of the following: 
    * A predefined label, such as "GO". For more information, see the documentation for the [ `--flex-template-base-image`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/build#--flex-template-base-image) flag. 
    * The full `gcr.io` path to a specific container version, in the following format: `gcr.io/dataflow-templates-base/IMAGE:TAG`. 
  * `METADATA_FILE`: the local path to a metafile file. For more information, see [Template metadata](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates#metadata). 
  * `GO_FILE_PATH`: the local path to the compiled Go binary for the pipeline 
  * `GO_BINARY`: the Go binary to run. For more information, see Environment variables. 



### Use a custom image

To run a Flex Template using a custom container image, run the following command:

###  Java 
    
    
    gcloud dataflow flex-template build gs://BUCKET_NAME/TEMPLATE_FILE_NAME \
      --image "CUSTOM_IMAGE" \
      --sdk-language "JAVA" \
      --metadata-file "METADATA_FILE"
    

###  Python 
    
    
    gcloud dataflow flex-template build gs://BUCKET_NAME/TEMPLATE_FILE_NAME \
      --image "CUSTOM_IMAGE" \
      --sdk-language "PYTHON" \
      --metadata-file "METADATA_FILE"
    

###  Go 
    
    
    gcloud dataflow flex-template build gs://BUCKET_NAME/TEMPLATE_FILE_NAME \
      --image "CUSTOM_IMAGE" \
      --sdk-language "GO" \
      --metadata-file "METADATA_FILE"
    

Replace the following:

  * `BUCKET_NAME`: the name of a Cloud Storage bucket to store the template specification file.

  * `TEMPLATE_FILE_NAME`: the name of the template specification file. Example: `my_template.json`.

  * `CUSTOM_IMAGE`: the image registry location of the custom image.

  * `METADATA_FILE`: the local path to a metafile file.




## Package dependencies for Python

When a Dataflow Python pipeline uses additional dependencies, you might need to configure the Flex Template to install additional dependencies on Dataflow worker VMs.

When you run a Python Dataflow job that uses Flex Templates in an environment that restricts access to the internet, you must prepackage the dependencies when you create the template.

Use one of the following options to prepackage Python dependencies.

  * Use a requirements file and prepackage the dependencies with the template.
  * Structure the pipeline as a package and use local packages.
  * Use a custom container that preinstalls all dependencies.



For instructions for managing pipeline dependencies in Java and Go pipelines, see [Manage pipeline dependencies in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/manage-dependencies).

### Use a requirements file and prepackage the dependencies with the template

If you are using your own Dockerfile to define the Flex Template image, follow these steps:

  1. Create a `requirements.txt` file that lists your pipeline dependencies.
         
         COPY requirements.txt /template/
         ENV FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE="/template/requirements.txt"
         

  2. Install the dependencies in the Flex Template image.
         
         RUN pip install --no-cache-dir -r $FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE
         

  3. Download the dependencies into the local requirements cache, which is staged to the Dataflow workers when the template launches.
         
         RUN pip download --no-cache-dir --dest /tmp/dataflow-requirements-cache -r $FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE
         




When you use this approach, dependencies from the `requirements.txt` file are installed onto Dataflow workers at runtime. An insight in the Google Cloud console recommendations tab might note this behavior. To avoid installing dependencies at runtime, use a custom container image.

The following is a code sample that uses a requirements file in the Flex Template.
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #    http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    FROM gcr.io/dataflow-templates-base/python3-template-launcher-base
    
    # Configure the Template to launch the pipeline with a --requirements_file option.
    # See: https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/#pypi-dependencies
    ENV FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE="/template/requirements.txt"
    ENV FLEX_TEMPLATE_PYTHON_PY_FILE="/template/streaming_beam.py"
    
    COPY . /template
    
    RUN apt-get update \
        # Install any apt packages if required by your template pipeline.
        && apt-get install -y libffi-dev git \
        && rm -rf /var/lib/apt/lists/* \
        # Upgrade pip and install the requirements.
        && pip install --no-cache-dir --upgrade pip \
        # Install dependencies from requirements file in the launch environment.
        && pip install --no-cache-dir -r $FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE \
        # When FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE  option is used,
        # then during Template launch Beam downloads dependencies
        # into a local requirements cache folder and stages the cache to workers.
        # To speed up Flex Template launch, pre-download the requirements cache
        # when creating the Template.
        && pip download --no-cache-dir --dest /tmp/dataflow-requirements-cache -r $FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE
    
    # Set this if using Beam 2.37.0 or earlier SDK to speed up job submission.
    ENV PIP_NO_DEPS=True
    
    ENTRYPOINT ["/opt/google/dataflow/python_template_launcher"]
    

### Structure the pipeline as a package and use local packages

When you use multiple Python local files or modules, structure your pipeline as a package. The file structure might look like the following example:
    
    
    main.py
    pyproject.toml
    setup.py
    src/
      my_package/
        __init__.py
        my_custom_dofns_and_transforms.py
        my_pipeline_launcher.py
        other_utils_and_helpers.py
    

  1. Place the top-level entry point, for example, the `main.py` file, in the root directory. Place the rest of the files in a separate folder in the `src` directory, for example, `my_package`.

  2. Add the package configuration files to the root directory with the package details and requirements.

### pyproject.toml
         
         [project]
         name = "my_package"
         version = "package_version"
         dependencies = [
           # Add list of packages (and versions) that my_package depends on.
           # Example:
           "apache-beam[gcp]==2.54.0",
         ]
         

### setup.py
         
         """An optional setuptools configuration stub for the pipeline package.
         
           Use pyproject.toml to define the package. Add this file only if you must
           use the --setup_file pipeline option or the
           FLEX_TEMPLATE_PYTHON_SETUP_FILE configuration option.
           """
         
           import setuptools
           setuptools.setup()
         

For more information about how to configure your local package, see [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

  3. When you import local modules or files for your pipeline, use the `my_package` package name as the import path.
         
         from my_package import word_count_transform
         

  4. Install your pipeline package in the Flex Template image. Your Flex Template Dockerfile might include content similar to the following example:

### Dockerfile
         
         ENV FLEX_TEMPLATE_PYTHON_PY_FILE="${WORKDIR}/main.py"
         ENV FLEX_TEMPLATE_PYTHON_SETUP_FILE="${WORKDIR}/setup.py"
         
         # Copy pipeline, packages and requirements.
         WORKDIR ${WORKDIR}
         COPY main.py .
         COPY pyproject.toml .
         COPY setup.py .
         COPY src src
         
         # Install local package.
         RUN pip install -e .
         




When you use this approach, dependencies from the `requirements.txt` file are installed onto Dataflow workers at runtime. An insight in the Google Cloud console recommendations tab might note this behavior. To avoid installing dependencies at runtime, use a custom container image.

For an example that follows the recommended approach, see the [Flex Template for a pipeline with dependencies and a custom container image](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/dataflow/flex-templates/pipeline_with_dependencies) tutorial in GitHub.

### Use a custom container that preinstalls all dependencies

To avoid dependency installation at runtime, use custom containers. This option is preferred for pipelines that run in environments without internet access.

Follow these steps to use a custom container:

  1. Build a custom container image that [preinstalls necessary dependencies](https://docs.cloud.google.com/dataflow/docs/guides/build-container-image#preinstall_using_a_dockerfile).

  2. Preinstall the same dependencies in the Flex Template Dockerfile.

To prevent dependency installation at runtime, don't use the `FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE` or `FLEX_TEMPLATE_PYTHON_SETUP_FILE` options in your Flex Template configuration.

A modified Flex Template `Dockerfile` might look like the following example:
         
         FROM gcr.io/dataflow-templates-base/python3-template-launcher-base
         ENV FLEX_TEMPLATE_PYTHON_PY_FILE="/template/main.py"
         COPY . /template
         # If you use a requirements file, pre-install the requirements.txt.
         RUN pip install --no-cache-dir -r /template/requirements.txt
         # If you supply the pipeline in a package, pre-install the local package and its dependencies.
         RUN pip install -e /template
         

When you use this approach, you do the following:

     * build the Flex Template image
     * build the custom SDK container image
     * install the same dependencies in both images

Alternatively, to reduce the number of images to maintain, use your custom container image as a base image for the Flex Template.

  3. If you use the Apache Beam SDK version 2.49.0 or earlier, add the `--sdk_location=container` pipeline option in your pipeline launcher. This option tells your pipeline to use the SDK from your custom container instead of downloading the SDK.
         
         options = PipelineOptions(beam_args, save_main_session=True, streaming=True, sdk_location="container")
         

  4. Set the `sdk_container_image` parameter in the `flex-template run` command. For example:
         
         gcloud dataflow flex-template run $JOB_NAME \
            --region=$REGION \
            --template-file-gcs-location=$TEMPLATE_PATH \
            --parameters=sdk_container_image=$CUSTOM_CONTAINER_IMAGE \
            --additional-experiments=use_runner_v2
         

For Beam SDK versions 2.74 and later, use `--additional-experiments=enable_portable_runner`.

For more information, see [Use custom containers in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers).




## Use a private Docker registry with Flex Templates

You can build a Flex Template image stored in a private [Docker registry](https://docs.docker.com/registry/), if the private registry uses HTTPS and has a valid certificate.

To use an image from a private registry, specify the path to the image and a username and password for the registry. The username and password must be stored in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs). You can provide the secret in one of the following formats:

  * `projects/{project}/secrets/{secret}/versions/{secret_version}`
  * `projects/{project}/secrets/{secret}`



If you use the second format, because it doesn't specify the version, Dataflow uses the latest version.

If the registry uses a self-signed certificate, you also need to specify the path to the self-signed certificate in Cloud Storage.

The following table describes the gcloud CLI options that you can use to configure a private registry.

Parameter | Description  
---|---  
`image` | The address of the registry. For example: `gcp.repository.example.com:9082/registry/example/image:latest`.   
`image-repository-username-secret-id` | The Secret Manager secret ID for the username to authenticate to the private registry. For example: `projects/example-project/secrets/username-secret`.   
`image-repository-password-secret-id` | The Secret Manager secret ID for the password to authenticate to the private registry. For example: `projects/example-project/secrets/password-secret/versions/latest`.   
`image-repository-cert-path` | The full Cloud Storage URL for a self-signed certificate for the private registry. This value is only required if the registry uses a self-signed certificate. For example: `gs://example-bucket/self-signed.crt`.   
  
Here's an example Google Cloud CLI command that builds a Flex Template using an image in a private registry with a self-signed certificate.
    
    
    gcloud dataflow flex-template build gs://example-bucket/custom-pipeline-private-repo.json
    --sdk-language=JAVA
    --image="gcp.repository.example.com:9082/registry/example/image:latest"
    --image-repository-username-secret-id="projects/example-project/secrets/username-secret"
    --image-repository-password-secret-id="projects/example-project/secrets/password-secret/versions/latest"
    --image-repository-cert-path="gs://example-bucket/self-signed.crt"
    --metadata-file=metadata.json

To build your own Flex Template, you need to replace the example values, and you might need to specify different or additional options.

## What's next

  * Learn how to [run a Flex Template](https://docs.cloud.google.com/dataflow/docs/guides/templates/run-flex-templates).
  * [Build and run an example Flex Template](https://docs.cloud.google.com/dataflow/docs/guides/templates/using-flex-templates).
  * To know more about Classic Templates, Flex Templates, and their use-case scenarios, see [Dataflow templates](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates).
  * For Flex Templates troubleshooting information, see [Troubleshoot Flex Template timeouts](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-templates).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
