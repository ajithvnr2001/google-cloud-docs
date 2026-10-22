---
url: https://docs.cloud.google.com/dataflow/docs/hpc-ep/hpc-tutorial/
title: Use custom containers with C++ libraries \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:57.187662+00:00
---

# Use custom containers with C++ libraries  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/hpc-ep/hpc-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use custom containers with C++ libraries Stay organized with collections  Save and categorize content based on your preferences. 

In this tutorial, you create a pipeline that uses custom containers with C++ libraries to run a Dataflow HPC highly parallel workflow. Use this tutorial to learn how to use Dataflow and Apache Beam to run grid computing applications that require data to be distributed to functions running on many cores.

The tutorial demonstrates how to run the pipeline first by using the [Direct Runner](https://beam.apache.org/documentation/runners/direct/) and then by using the [Dataflow Runner](https://beam.apache.org/documentation/runners/dataflow/). By running the pipeline locally, you can test the pipeline before deploying it.

This example uses [Cython](https://cython.org/) bindings and functions from the [GMP library](https://gmplib.org/). Regardless of the library or binding tool that you use, you can apply the same principles to your pipeline.

The example code is [available on GitHub](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/tree/master/beam-cpp-example).

## Objectives

  * Create a pipeline that uses custom containers with C++ libraries.

  * Build a Docker container image using a Dockerfile.

  * Package the code and dependencies into a Docker container.

  * Run the pipeline locally to test it.

  * Run the pipeline in a distributed environment.




## Costs

In this document, you use the following billable components of Google Cloud: 

  * Artifact Registry
  * Cloud Build
  * Cloud Storage
  * Compute Engine
  * Dataflow



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Storage, Cloud Storage JSON, Compute Engine, Dataflow, Resource Manager, Artifact Registry, and Cloud Build APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com dataflow.googleapis.com storage_component storage_api cloudresourcemanager.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com

  8. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/iam.serviceAccountUser`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  10. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  11. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  12. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  13. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Cloud Storage, Cloud Storage JSON, Compute Engine, Dataflow, Resource Manager, Artifact Registry, and Cloud Build APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com dataflow.googleapis.com storage_component storage_api cloudresourcemanager.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com

  16. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  17. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/iam.serviceAccountUser`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  18. Create a user-managed worker service account for your new pipeline and grant the necessary roles to the service account.

     1. To create the service account, run the [`gcloud iam service-accounts create`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create) command:
            
            gcloud iam service-accounts create parallelpipeline \
                --description="Highly parallel pipeline worker service account" \
                --display-name="Highly parallel data pipeline access"

     2. Grant roles to the service account. Run the following command once for each of the following IAM roles:

        * `roles/dataflow.admin`
        * `roles/dataflow.worker`
        * `roles/storage.objectAdmin`
        * `roles/artifactregistry.reader`
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:parallelpipeline@PROJECT_ID.iam.gserviceaccount.com" --role=SERVICE_ACCOUNT_ROLE

Replace `SERVICE_ACCOUNT_ROLE` with each individual role.

     3. Grant your Google Account a role that lets you create access tokens for the service account:
            
            gcloud iam service-accounts add-iam-policy-binding parallelpipeline@PROJECT_ID.iam.gserviceaccount.com --member="user:EMAIL_ADDRESS" --role=roles/iam.serviceAccountTokenCreator




## Download the code sample and change directories

Download the code sample and then change directories. The code samples in the GitHub repository provide all the code that you need to run this pipeline. When you are ready to build your own pipeline, you can use this sample code as a template.

Clone the [beam-cpp-example repository](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/tree/master/beam-cpp-example).

  1. Use the `git clone` command to clone the GitHub repository:
         
         git clone https://github.com/GoogleCloudPlatform/dataflow-sample-applications.git
         

  2. Switch to the application directory:
         
         cd dataflow-sample-applications/beam-cpp-example
         




### Pipeline code

You can customize the pipeline code from this tutorial. This pipeline completes the following tasks:

  * Dynamically produces all integers in an input range.
  * Runs the integers through a C++ function and filters bad values.
  * Writes the bad values to a side channel.
  * Counts the occurrence of each stopping time and normalizes the results.
  * Prints the output, formatting and writing the results to a text file.
  * Creates a `PCollection` with a single element.
  * Processes the single element with a `map` function and passes the frequency `PCollection` as a side input.
  * Processes the `PCollection` and produces a single output.



The starter file looks like the following:
    
    
    #
    # Licensed to the Apache Software Foundation (ASF) under one or more
    # contributor license agreements.  See the NOTICE file distributed with
    # this work for additional information regarding copyright ownership.
    # The ASF licenses this file to You under the Apache License, Version 2.0
    # (the "License"); you may not use this file except in compliance with
    # the License.  You may obtain a copy of the License at
    #
    #    http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    #
    
    
    import argparse
    import logging
    import os
    import sys
    
    
    def run(argv):
      # Import here to avoid __main__ session pickling issues.
      import io
      import itertools
      import matplotlib.pyplot as plt
      import collatz
    
      import apache_beam as beam
      from apache_beam.io import restriction_trackers
      from apache_beam.options.pipeline_options import PipelineOptions
    
      class RangeSdf(beam.DoFn, beam.RestrictionProvider):
        """An SDF producing all the integers in the input range.
    
        This is preferable to beam.Create(range(...)) as it produces the integers
        dynamically rather than materializing them up front.  It is an SDF to do
        so with perfect dynamic sharding.
        """
        def initial_restriction(self, desired_range):
          start, stop = desired_range
          return restriction_trackers.OffsetRange(start, stop)
    
        def restriction_size(self, _, restriction):
          return restriction.size()
    
        def create_tracker(self, restriction):
          return restriction_trackers.OffsetRestrictionTracker(restriction)
    
        def process(self, _, active_range=beam.DoFn.RestrictionParam()):
          for i in itertools.count(active_range.current_restriction().start):
            if active_range.try_claim(i):
              yield i
            else:
              break
    
      class GenerateIntegers(beam.PTransform):
        def __init__(self, start, stop):
          self._start = start
          self._stop = stop
    
        def expand(self, p):
          return (
              p
              | beam.Create([(self._start, self._stop + 1)])
              | beam.ParDo(RangeSdf()))
    
      parser = argparse.ArgumentParser()
      parser.add_argument('--start', dest='start', type=int, default=1)
      parser.add_argument('--stop', dest='stop', type=int, default=10000)
      parser.add_argument('--output', default='./out.png')
    
      known_args, pipeline_args = parser.parse_known_args(argv)
      # Store this as a local to avoid capturing the full known_args.
      output_path = known_args.output
    
      with beam.Pipeline(options=PipelineOptions(pipeline_args)) as p:
    
        # Generate the integers from start to stop (inclusive).
        integers = p | GenerateIntegers(known_args.start, known_args.stop)
    
        # Run them through our C++ function, filtering bad records.
        # Requires apache beam 2.34 or later.
        stopping_times, bad_values = (
            integers
            | beam.Map(collatz.total_stopping_time).with_exception_handling(
                use_subprocess=True))
    
        # Write the bad values to a side channel.
        bad_values | 'WriteBadValues' >> beam.io.WriteToText(
            os.path.splitext(output_path)[0] + '-bad.txt')
    
        # Count the occurrence of each stopping time and normalize.
        total = known_args.stop - known_args.start + 1
        frequencies = (
            stopping_times
            | 'Aggregate' >> (beam.Map(lambda x: (x, 1)) | beam.CombinePerKey(sum))
            | 'Normalize' >> beam.MapTuple(lambda x, count: (x, count / total)))
    
        if known_args.stop <= 10:
          # Print out the results for debugging.
          frequencies | beam.Map(print)
        else:
          # Format and write them to a text file.
          (
              frequencies
              | 'Format' >> beam.MapTuple(lambda count, freq: f'{count}, {freq}')
              | beam.io.WriteToText(os.path.splitext(output_path)[0] + '.txt'))
    
        # Define some helper functions.
        def make_scatter_plot(xy):
          x, y = zip(*xy)
          plt.plot(x, y, '.')
          png_bytes = io.BytesIO()
          plt.savefig(png_bytes, format='png')
          png_bytes.seek(0)
          return png_bytes.read()
    
        def write_to_path(path, content):
          """Most Beam IOs write multiple elements to some kind of a container
          file (e.g. strings to lines of a text file, avro records to an avro file,
          etc.)  This function writes each element to its own file, given by path.
          """
          # Write to a temporary path and to a rename for fault tolerence.
          tmp_path = path + '.tmp'
          fs = beam.io.filesystems.FileSystems.get_filesystem(path)
          with fs.create(tmp_path) as fout:
            fout.write(content)
          fs.rename([tmp_path], [path])
    
        (
            p
            # Create a PCollection with a single element.
            | 'CreateSingleton' >> beam.Create([None])
            # Process the single element with a Map function, passing the frequency
            # PCollection as a side input.
            # This will cause the normally distributed frequency PCollection to be
            # colocated and processed as a single unit, producing a single output.
            | 'MakePlot' >> beam.Map(
                lambda _,
                data: make_scatter_plot(data),
                data=beam.pvalue.AsList(frequencies))
            # Pair this with the desired filename.
            |
            'PairWithFilename' >> beam.Map(lambda content: (output_path, content))
            # And actually write it out, using MapTuple to split the tuple into args.
            | 'WriteToOutput' >> beam.MapTuple(write_to_path))
    
    
    if __name__ == '__main__':
      logging.getLogger().setLevel(logging.INFO)
      run(sys.argv)
    

## Set up your development environment

  1. Use the [Apache Beam SDK](https://docs.cloud.google.com/dataflow/docs/guides/installing-beam-sdk#python) for Python.

  2. Install the GMP library:
         
         apt-get install libgmp3-dev
         

  3. To install the dependencies, use the `requirements.txt` file.
         
         pip install -r requirements.txt
         

  4. To build the Python bindings, run the following command.
         
         python setup.py build_ext --inplace
         




You can customize the `requirements.txt` file from this tutorial. The starter file includes the following dependencies:
    
    
    #
    #    Licensed to the Apache Software Foundation (ASF) under one or more
    #    contributor license agreements.  See the NOTICE file distributed with
    #    this work for additional information regarding copyright ownership.
    #    The ASF licenses this file to You under the Apache License, Version 2.0
    #    (the "License"); you may not use this file except in compliance with
    #    the License.  You may obtain a copy of the License at
    #
    #       http://www.apache.org/licenses/LICENSE-2.0
    #
    #    Unless required by applicable law or agreed to in writing, software
    #    distributed under the License is distributed on an "AS IS" BASIS,
    #    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    #    See the License for the specific language governing permissions and
    #    limitations under the License.
    #
    
    apache-beam[gcp]==2.46.0
    cython==0.29.24
    pyparsing==2.4.2
    matplotlib==3.4.3
    

## Run the pipeline locally

Running the pipeline locally is useful for testing. By running the pipeline locally, you can confirm that the pipeline runs and behaves as expected before you deploy the pipeline to a distributed environment.

You can run the pipeline locally by using the following command. This command outputs an image named `out.png`.
    
    
    python pipeline.py
    

## Create the Google Cloud resources

This section explains how to create the following resources:

  * A Cloud Storage bucket to use as a temporary storage location and an output location.
  * A Docker container to package the pipeline code and dependencies.



### Create a Cloud Storage bucket

Begin by creating a Cloud Storage bucket using Google Cloud CLI. This bucket is used as a temporary storage location by the Dataflow pipeline.

To create the bucket, use the [`gcloud storage buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create):
    
    
    gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION
    

Replace the following:

  * BUCKET_NAME: a name for your Cloud Storage bucket that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). Cloud Storage bucket names must be globally unique.
  * LOCATION: the [location](https://docs.cloud.google.com/storage/docs/locations#available-locations) for the bucket.



### Create and build a container image

You can customize the Dockerfile from this tutorial. The starter file looks like the following:

**Note:** You might need to update the Python version in the Dockerfile when you run the pipeline in a distributed environment. When you use a custom container image, the Python interpreter minor version in your image must match the version used at pipeline construction time.
    
    
    FROM apache/beam_python3.9_sdk:2.46.0
    
    # Install a C++ library.
    RUN apt-get update
    RUN apt-get install -y libgmp3-dev
    
    # Install Python dependencies.
    COPY requirements.txt requirements.txt
    RUN pip install -r requirements.txt
    
    # Install the code and some python bindings.
    COPY pipeline.py pipeline.py
    COPY collatz.pyx collatz.pyx
    COPY setup.py setup.py
    RUN python setup.py install
    

This Dockerfile contains the `FROM`, `COPY`, and `RUN` commands, which you can read about in the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/).

  1. To upload artifacts, create an Artifact Registry repository. Each repository can contain artifacts for a single supported format.

All repository content is encrypted using either Google-owned and Google-managed encryption keys or customer-managed encryption keys. Artifact Registry uses Google-owned and Google-managed encryption keys by default and no configuration is required for this option.

You must have at least [Artifact Registry Writer access](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions) to the repository.

Run the following command to create a new repository. The command uses the `--async` flag and returns immediately, without waiting for the operation in progress to complete.
         
         gcloud artifacts repositories create REPOSITORY \
            --repository-format=docker \
            --location=LOCATION \
            --async
         

Replace `REPOSITORY` with a name for your repository. For each repository location in a project, repository names must be unique.

  2. Create the Dockerfile.

For packages to be part of the Apache Beam container, you must specify them as part of the `requirements.txt` file. Ensure that you don't specify `apache-beam` as part of the `requirements.txt` file. The Apache Beam container already has `apache-beam`.

**Note:** Dependencies installed with the Dockerfile are only available when launching the pipeline. Job dependencies must be included in the requirements file. As in the example, Apache Beam does not need to be in this file, and it is encouraged to keep it separate for faster launches.
  3. Before you can push or pull images, configure Docker to authenticate requests for Artifact Registry. To set up authentication to Docker repositories, run the following command:
         
         gcloud auth configure-docker LOCATION-docker.pkg.dev
         

The command updates your Docker configuration. You can now connect with Artifact Registry in your Google Cloud project to push images.

  4. Build the [Docker](https://docs.docker.com/) image using your [`Dockerfile`](https://docs.cloud.google.com/build/docs/build-push-docker-image#build_using_dockerfile) with Cloud Build.

Update the path in the following command to match the Dockerfile that you created. This command builds the file and pushes it to your Artifact Registry repository.
         
         gcloud builds submit --tag LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/dataflow/cpp_beam_container:latest .
         




## Package the code and dependencies in a Docker container

  1. To run this pipeline in a distributed environment, package the code and dependencies into a Docker container.
         
         docker build . -t cpp_beam_container
         

  2. After you package the code and dependencies, you can run the pipeline locally to test it.
         
         python pipeline.py \
            --runner=PortableRunner \
            --job_endpoint=embed \
            --environment_type=DOCKER \
            --environment_config="docker.io/library/cpp_beam_container"
         

This command writes the output inside the Docker image. To view the output, run the pipeline with the `--output` flag, and write the output to a Cloud Storage bucket. For example, run the following command.
         
         python pipeline.py \
            --runner=PortableRunner \
            --job_endpoint=embed \
            --environment_type=DOCKER \
            --environment_config="docker.io/library/cpp_beam_container" \
            --output=gs://BUCKET_NAME/out.png
         




## Run the pipeline

You can now run the Apache Beam pipeline in Dataflow by referring to the file with the pipeline code and passing the [parameters](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options) required by the pipeline.

In your shell or terminal, run the pipeline with the Dataflow Runner.

**Note:** If you're using **Apache Beam SDK 2.74 or later** , use the updated flag `--experiments=enable_portable_runner` to enable the Portable Runner. 
    
    
    python pipeline.py \
        --runner=DataflowRunner \
        --project=PROJECT_ID \
        --region=REGION \
        --temp_location=gs://BUCKET_NAME/tmp \
        --sdk_container_image="LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/dataflow/cpp_beam_container:latest" \
        --experiment=use_runner_v2 \
        --output=gs://BUCKET_NAME/out.png
    

After you execute the command to run the pipeline, Dataflow returns a Job ID with the job status **Queued**. It might take several minutes before the job status reaches **Running** and you can access the [job graph](https://docs.cloud.google.com/dataflow/docs/guides/job-graph).

## View your results

View data written to your Cloud Storage bucket. Use the [`gcloud storage ls` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls) to list the contents at the top level of your bucket:
    
    
    gcloud storage ls gs://BUCKET_NAME
    

If successful, the command returns a message similar to:
    
    
    gs://BUCKET_NAME/out.png
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

The easiest way to eliminate billing is to delete the Google Cloud project that you created for the tutorial.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resources

If you want to reuse the project, then delete the resources that you created for the tutorial.

#### Clean up Google Cloud project resources

  1. Delete the Artifact Registry repository.
         
         gcloud artifacts repositories delete REPOSITORY \
            --location=LOCATION --async
         

  2. Delete the Cloud Storage bucket and its objects. This bucket alone does not incur any charges.
         
         gcloud storage rm gs://BUCKET_NAME --recursive
         




#### Revoke credentials

  1. Revoke the roles that you granted to the user-managed worker service account. Run the following command once for each of the following IAM roles:

     * `roles/dataflow.admin`
     * `roles/dataflow.worker`
     * `roles/storage.objectAdmin`
     * `roles/artifactregistry.reader`
    
    gcloud projects remove-iam-policy-binding PROJECT_ID \
      --member=serviceAccount:parallelpipeline@PROJECT_ID.iam.gserviceaccount.com \
      --role=SERVICE_ACCOUNT_ROLE

  2. Optional: Revoke the authentication credentials that you created, and delete the local credential file. 
         
         gcloud auth application-default revoke

  3. Optional: Revoke credentials from the gcloud CLI. 
         
         gcloud auth revoke




## What's next

  * View [the sample application on GitHub](https://github.com/GoogleCloudPlatform/dataflow-sample-applications/tree/master/beam-cpp-example).
  * [Use custom containers in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers).
  * Learn more about using [container environments](https://beam.apache.org/documentation/runtime/environments/) with Apache Beam.
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
