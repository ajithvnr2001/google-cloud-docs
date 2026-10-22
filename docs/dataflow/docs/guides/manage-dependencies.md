---
url: https://docs.cloud.google.com/dataflow/docs/guides/manage-dependencies/
title: Manage pipeline dependencies in Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:16.073559+00:00
---

# Manage pipeline dependencies in Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/manage-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Manage pipeline dependencies in Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Many Apache Beam pipelines can run using the default Dataflow runtime environments. However, some data processing use cases benefit from using additional libraries or classes. In these cases, you might need to manage your pipeline dependencies.

The following list provides some reasons you might need to manage your pipeline dependencies:

  * The dependencies provided by the default runtime environment are insufficient for your use case.
  * The default dependencies either have version collisions or have classes and libraries that are incompatible with your pipeline code.
  * You need to pin to specific library versions for your pipeline.
  * You have a Python pipeline that needs to run with a consistent set of dependencies.



How you manage dependencies depends on whether your pipeline uses Java, Python, or Go.

## Java

Incompatible classes and libraries can cause Java dependency issues. If your pipeline contains user-specific code and settings, the code can't contain mixed versions of libraries.

### Java dependency issues

When your pipeline has Java dependency issues, one of the following errors might occur:

  * `NoClassDefFoundError`: This error occurs when an entire class is not available during runtime.
  * `NoSuchMethodError`: This error occurs when the class in the classpath uses a version that doesn't contain the correct method or when the method signature changed.
  * `NoSuchFieldError`: This error occurs when the class in the classpath uses a version that doesn't have a field required during runtime.
  * `FATAL ERROR`: This error occurs when a built-in dependency can't be loaded properly. When using an uber JAR file (shaded), don't include libraries that use signatures in the same JAR file, such as Conscrypt.



### Dependency management

To simplify dependency management for Java pipelines, Apache Beam uses [Bill of Materials (BOM)](https://docs.cloud.google.com/java/docs/bom) artifacts. The BOM helps dependency management tools select compatible dependency combinations. For more information, see [Apache Beam SDK for Java dependencies](https://beam.apache.org/documentation/sdks/java-dependencies/) in the Apache Beam documentation.

To use a BOM with your pipeline and to explicitly add other dependencies to the dependency list, add the following information to the `pom.xml` file for the SDK artifact. To import the correct libraries BOM, use `beam-sdks-java-google-cloud-platform-bom`.
    
    
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>org.apache.beam</groupId>
          <artifactId>beam-sdks-java-google-cloud-platform-bom</artifactId>
          <version>LATEST</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    
    <dependencies>
      <dependency>
        <groupId>org.apache.beam</groupId>
        <artifactId>beam-sdks-java-core</artifactId>
      </dependency>
      <dependency>
        <groupId>org.apache.beam</groupId>
        <artifactId>beam-runners-google-cloud-dataflow-java</artifactId>
      </dependency>
      <dependency>
        <groupId>org.apache.beam</groupId>
        <artifactId>beam-sdks-java-io-google-cloud-platform</artifactId>
      </dependency>
    </dependencies>
    

The `beam-sdks-java-core` artifact contains only the core SDK. You need to explicitly add other dependencies, such as I/O and runners, to the dependency list.

## Python

When you run Dataflow jobs by using the Apache Beam Python SDK, dependency management is useful in the following scenarios:

  * Your pipeline uses public packages from the [Python Package Index](https://pypi.python.org/) (PiPy), and you want to make these packages available remotely.
  * You want to create a reproducible environment.
  * To reduce startup time, you want to avoid dependency installation on the workers at runtime.



### Define Python pipeline dependencies

Although you can use a single Python script or notebook to write an Apache Beam pipeline, in the Python ecosystem, software is often distributed as packages. To make your pipeline easier to maintain, when your pipeline code spans multiple files, group the pipeline files as a Python package.

  * Define the dependencies of the pipeline in the `setup.py` file of your package.
  * Stage the package to the workers using the `--setup_file` pipeline option.



When the remote workers start, they install your package. For an example, see [juliaset](https://github.com/apache/beam/tree/master/sdks/python/apache_beam/examples/complete/juliaset) in the Apache Beam GitHub.

To structure your pipeline as a Python package, follow these steps:

  1. Create a `setup.py` file for your project. In the `setup.py` file, include the [`install_requires`](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#install-requires) argument to specify the minimal set of dependencies for your pipeline. The following example shows a basic `setup.py` file.
         
         import setuptools
         
         setuptools.setup(
           name='PACKAGE_NAME',
           version='PACKAGE_VERSION',
           install_requires=[],
           packages=setuptools.find_packages(),
         )
         

  2. Add the `setup.py` file, the main workflow file, and a directory with the rest of the files to the root directory of your project. This file grouping is the Python package for your pipeline. The file structure looks like the following example:
         
         root_dir/
           package_name/
             __init__.py
             my_pipeline_launcher.py
             my_custom_transforms.py
             ...other files...
           setup.py
           main.py
         

  3. To run your pipeline, install the package in the submission environment. Use the `--setup_file` pipeline option to stage the package to the workers. For example:
         
         python -m pip install -e .
         python main.py --runner DataflowRunner --setup_file ./setup.py  <...other options...>
         




These steps simplify pipeline code maintenance, particularly when the code grows in size and complexity. For other ways to specify dependencies, see [Managing Python pipeline dependencies](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/) in the Apache Beam documentation.

### Use custom containers to control the runtime environment

To run a pipeline with the Apache Beam Python SDK, Dataflow workers need a Python environment that contains an interpreter, the Apache Beam SDK, and the pipeline dependencies. Docker container images provide the appropriate environment for running your pipeline code.

Stock container images are released with each version of the Apache Beam SDK, and these images include the Apache Beam SDK dependencies. For more information, see [Apache Beam SDK for Python dependencies](https://beam.apache.org/documentation/sdks/python-dependencies/) in the Apache Beam documentation.

When your pipeline requires a dependency that isn't included in the default container image, the dependency must be installed at runtime. Installing packages at runtime can have the following consequences:

  * Worker startup time increases due to dependency resolution, download, and installation.
  * The pipeline requires a connection to the internet to run.
  * Non-determinism occurs due to software releases in dependencies.



To avoid these issues, supply the runtime environment in a custom Docker container image. Using a custom Docker container image that has the pipeline dependencies preinstalled has the following benefits:

  * Ensures that the pipeline runtime environment has the same set of dependencies every time you launch your Dataflow job.
  * Lets you control the runtime environment of your pipeline.
  * Avoids potentially time-consuming dependency resolution at startup.



When you use custom container images, consider the following guidance:

  * Avoid using the tag `:latest` with your custom images. Tag your builds with a date, version, or a unique identifier. This step lets you revert to a known working configuration if needed.
  * Use a launch environment that is compatible with your container image. For more guidance about using custom containers, see [Build a container image](https://docs.cloud.google.com/dataflow/docs/guides/build-container-image).



For details about pre-installing Python dependencies, see [Pre-install Python dependencies](https://docs.cloud.google.com/dataflow/docs/guides/build-container-image#preinstall_using_a_dockerfile).

### Control the launch environment with Dataflow Templates

If your pipeline requires additional dependencies, you might need to install them in both the runtime environment and the launch environment. The launch environment runs the production version of the pipeline. Because the launch environment must be compatible with the runtime environment, use the same versions of dependencies in both environments.

To have a containerized, reproducible launch environment, use Dataflow Flex Templates. For more information, see [Use Flex Templates to package a Dataflow pipeline for deployment](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates). When using Flex Templates, consider the following factors:

  * If you configure the pipeline as a package, install the package in your template Dockerfile. To configure the Flex Template, specify `FLEX_TEMPLATE_PYTHON_SETUP_FILE`. For more information, see [Set required Dockerfile environment variables](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates#env-variables).
  * If you use a custom container image with your pipeline, supply it when you launch your template. For more information, see [Use a custom container for dependencies](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates#use_a_custom_container_for_dependencies).
  * To build your Dataflow Flex Template Docker image, use the same custom container image as the base image. For more information, see [Use custom container images](https://docs.cloud.google.com/dataflow/docs/guides/templates/configuring-flex-templates#use_custom_container_images).



This construction makes your launch environment both reproducible and compatible with your runtime environment.

For an example that follows this approach, see the [Flex Template for a pipeline with dependencies and a custom container](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/dataflow/flex-templates/pipeline_with_dependencies) tutorial in GitHub.

For more information, see [Make the launch environment compatible with the runtime environment](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/#make-the-launch-environment-compatible-with-the-runtime-environment) and [Control the dependencies the pipeline uses](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/#pipeline-environments) in the Apache Beam documentation.

## Go

When you run Dataflow jobs by using the Apache Beam Go SDK, [Go Modules](https://pkg.go.dev/cmd/go#hdr-Modules__module_versions__and_more) are used to manage dependencies. The following file contains the default compile and runtime dependencies used by your pipeline:
    
    
    https://raw.githubusercontent.com/apache/beam/vVERSION_NUMBER/sdks/go.sum
    

Replace VERSION_NUMBER with the SDK version that you're using.

For information about managing dependencies for your Go pipeline, see [Managing dependencies](https://go.dev/doc/modules/managing-dependencies) in the Go documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
