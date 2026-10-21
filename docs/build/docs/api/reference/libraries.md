---
url: https://docs.cloud.google.com/build/docs/api/reference/libraries/
title: Cloud Build client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:16:41.685212+00:00
---

# Cloud Build client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/api/reference/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Reference ](https://docs.cloud.google.com/build/docs/api)



Send feedback 

#  Cloud Build client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to get started with the Cloud Client Libraries for the Cloud Build API. Client libraries make it easier to access Google Cloud APIs from a supported language. Although you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

However, we recommend using the older Google API Client Libraries if running on [ App Engine standard environment](https://docs.cloud.google.com/appengine/docs/about-the-standard-environment). Read more about the Cloud Client Libraries and the older Google API Client Libraries in [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

## Install the client library

### C++

See [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup) for details about this client library's requirements and install dependencies.

### Go
    
    
    go get cloud.google.com/go/cloudbuild

For more information, see [Setting Up a Go Development Environment](https://docs.cloud.google.com/go/docs/setup).

### Java

If you are using Maven, add this to your pom.xml file: 
    
    
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-build</artifactId>
        <version>3.8.0</version>
    </dependency>

If you are using Gradle, add this to your dependencies:
    
    
    compile group: 'com.google.cloud', name: 'google-cloud-build', version: '3.8.0'

For more information, see [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).

### Node.js
    
    
    npm install @google-cloud/cloudbuild

For more information, see [Setting Up a Node.js Development Environment](https://docs.cloud.google.com/nodejs/docs/setup).

### Python
    
    
    pip install --upgrade google-cloud-build

For more information, see [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).

## Set up authentication

To authenticate calls to Google Cloud APIs, client libraries support [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials); the libraries look for credentials in a set of defined locations and use those credentials to authenticate requests to the API. With ADC, you can make credentials available to your application in a variety of environments, such as local development or production, without needing to modify your application code. 

For production environments, the way you set up ADC depends on the service and context. For more information, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

For a local development environment, you can set up ADC with the credentials that are associated with your Google Account:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

A sign-in screen appears. After you sign in, your credentials are stored in the [ local credential file used by ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal). 




## Use the client library

The following example shows how to use the client library. 

### C++
    
    
    #include "google/cloud/cloudbuild/v1/cloud_build_client.h"
    #include <iostream>
    
    int main(int argc, char* argv[]) try {
      if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " project-id\n";
        return 1;
      }
    
      namespace cloudbuild = ::google::cloud::cloudbuild_v1;
      auto client =
          cloudbuild::CloudBuildClient(cloudbuild::MakeCloudBuildConnection());
      auto const* filter = R"""(status="WORKING")""";  // List only running builds
      for (auto b : client.ListBuilds(argv[1], filter)) {
        if (!b) throw std::move(b).status();
        std::cout << b->DebugString() << "\n";
      }
    
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }

### Node.js
    
    
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
    
    

## Additional resources

### C++

The following list contains links to more resources related to the client library for C++:

  * [API reference](https://docs.cloud.google.com/cpp/docs/reference/cloudbuild/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues)
  * [`google-cloudbuild` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloudbuild%5D%5Bc%2B%2B%5D)
  * [Source code](https://github.com/googleapis/google-cloud-cpp)



### Go

The following list contains links to more resources related to the client library for Go:

  * [API reference](https://docs.cloud.google.com/go/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-go/issues)
  * [`google-cloudbuild` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloudbuild%5D+%5Bgo%5D)
  * [Source code](https://github.com/googleapis/google-cloud-go)



### Java

The following list contains links to more resources related to the client library for Java:

  * [API reference](https://docs.cloud.google.com/java/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-java/issues)
  * [`google-cloudbuild` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloudbuild%5D+%5Bjava%5D)
  * [Source code](https://github.com/googleapis/google-cloud-java)



### Node.js

The following list contains links to more resources related to the client library for Node.js:

  * [API reference](https://docs.cloud.google.com/nodejs/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/GoogleCloudPlatform/google-cloud-node/issues)
  * [`google-cloudbuild` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloudbuild%5D+%5Bnode.js%5D)
  * [Source code](https://github.com/GoogleCloudPlatform/google-cloud-node)



### Python

The following list contains links to more resources related to the client library for Python:

  * [API reference](https://docs.cloud.google.com/python/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-python/issues)
  * [`google-cloudbuild` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloudbuild%5D+%5Bpython%5D)
  * [Source code](https://github.com/googleapis/google-cloud-python)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
