---
url: https://docs.cloud.google.com/build/docs/samples/cloudbuild-quickstart/
title: Client Libraries - Cloud Build Quickstart \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:19:12.211865+00:00
---

# Client Libraries - Cloud Build Quickstart  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/samples/cloudbuild-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Samples ](https://docs.cloud.google.com/build/docs/samples)



#  Client Libraries - Cloud Build Quickstart Stay organized with collections  Save and categorize content based on your preferences. 

Quickstart for using the Cloud Build API 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Build client libraries](https://docs.cloud.google.com/build/docs/api/reference/libraries)



## Code sample

### Node.js

To authenticate to Cloud Build, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function quickstart(
      projectId = 'YOUR_PROJECT_ID', // Your Google Cloud Platform project ID
      triggerId = 'YOUR_TRIGGER_ID', // UUID for build trigger.
      branchName = 'BRANCH_TO_BUILD' // Branch to run build against.
    ) {
      // Imports the Google Cloud client library
      const {CloudBuildClient} = require('[@google-cloud/cloudbuild](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/overview.html)');
    
      // Creates a client
      const cb = new [CloudBuildClient](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/overview.html)();
    
      // Note: for Private Pools, you'll have to specify an API endpoint value
      // For example:
      // const cb = new CloudBuildClient({ apiEndpoint: '<YOUR_POOL_REGION>-cloudbuild.googleapis.com' });
    
      // Starts a build against the branch provided.
      const [resp] = await cb.runBuildTrigger({
        projectId,
        triggerId,
        source: {
          projectId,
          dir: './',
          branchName,
        },
      });
      console.info(`triggered build for ${triggerId}`);
      const [build] = await resp.promise();
    
      const STATUS_LOOKUP = [
        '[UNKNOWN](https://docs.cloud.google.com/nodejs/docs/reference/cloudbuild/latest/cloudbuild/protos.google.devtools.cloudbuild.v1.gitfilesource.repotype.html)',
        'Queued',
        'Working',
        'Success',
        'Failure',
        'Error',
        'Timeout',
        'Cancelled',
      ];
      for (const step of build.steps) {
        console.info(
          `step:\n\tname: ${step.name}\n\tstatus: ${STATUS_LOOKUP[build.status]}`
        );
      }
    }

### Python

To authenticate to Cloud Build, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.auth
    from google.cloud.devtools import cloudbuild_v1
    
    
    def quickstart() -> None:
        """Create and execute a simple Google Cloud Build configuration,
        print the in-progress status and print the completed status."""
    
        # Authorize the client with Google defaults
        credentials, project_id = google.auth.default()
        client = cloudbuild_v1.services.[cloud_build](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.html).[CloudBuildClient](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.CloudBuildClient.html)()
    
        # If you're using Private Pools or a non-global default pool, add a regional
        # `api_endpoint` to `CloudBuildClient()`
        # For example, '<YOUR_POOL_REGION>-cloudbuild.googleapis.com'
        #
        # from google.api_core import client_options
        # client_options = client_options.ClientOptions(
        #     api_endpoint="us-central1-cloudbuild.googleapis.com"
        # )
        # client = cloudbuild_v1.services.cloud_build.CloudBuildClient(client_options=client_options)
    
        build = cloudbuild_v1.[Build](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.types.Build.html)()
    
        # The following build steps will output "hello world"
        # For more information on build configuration, see
        # https://cloud.google.com/build/docs/configuring-builds/create-basic-configuration
        build.steps = [
            {"name": "ubuntu", "entrypoint": "bash", "args": ["-c", "echo hello world"]}
        ]
    
        operation = client.[create_build](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v1.services.cloud_build.CloudBuildClient.html#google_cloud_devtools_cloudbuild_v1_services_cloud_build_CloudBuildClient_create_build)(project_id=project_id, build=build)
        # Print the in-progress operation
        print("IN PROGRESS:")
        print(operation.metadata)
    
        result = operation.result()
        # Print the completed status
        print("RESULT:", result.status)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudbuild). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
