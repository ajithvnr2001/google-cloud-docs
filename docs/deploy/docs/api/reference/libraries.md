---
url: https://docs.cloud.google.com/deploy/docs/api/reference/libraries/
title: Cloud Deploy client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:25.492197+00:00
---

# Cloud Deploy client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  Cloud Deploy client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to get started with the Cloud Client Libraries for the Cloud Deploy API. Client libraries make it easier to access Google Cloud APIs from a supported language. Although you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

However, we recommend using the older Google API Client Libraries if running on [ App Engine standard environment](https://docs.cloud.google.com/appengine/docs/about-the-standard-environment). Read more about the Cloud Client Libraries and the older Google API Client Libraries in [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

## Install the client library

### C++

See [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup) for details about this client library's requirements and install dependencies.

### C#
    
    
    Install-Package Google.Cloud.Deploy.V1 -Pre
      
        
        
    
    For more information, see [Setting Up a C# Development Environment](https://docs.cloud.google.com/dotnet/docs/setup).
    
    
        
      
    

### Go
    
    
    go get cloud.google.com/go/storage

For more information, see [Setting Up a Go Development Environment](https://docs.cloud.google.com/go/docs/setup).

### Java

If you are using Maven, add this to your pom.xml file: 
    
    
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-deploy</artifactId>
        <version>1.85.0</version>
    </dependency>

If you are using Gradle, add this to your dependencies:
    
    
    compile group: 'com.google.cloud', name: 'google-cloud-deploy', version: '1.85.0'

For more information, see [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).

### Node.js
    
    
    npm install @google-cloud/deploy

For more information, see [Setting Up a Node.js Development Environment](https://docs.cloud.google.com/nodejs/docs/setup).

### PHP
    
    
    composer require google/cloud-deploy

For more information, see [Using PHP on Google Cloud](https://docs.cloud.google.com/php/docs).

### Python
    
    
    pip install --upgrade google-cloud-deploy

For more information, see [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).

### Ruby
    
    
    gem install google-cloud-deploy

For more information, see [Setting Up a Ruby Development Environment](https://docs.cloud.google.com/ruby/docs/setup).

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
    
    
    #include "google/cloud/deploy/v1/cloud_deploy_client.h"
    #include "google/cloud/location.h"
    #include <iostream>
    
    int main(int argc, char* argv[]) try {
      if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " project-id location-id\n";
        return 1;
      }
    
      auto const location = google::cloud::Location(argv[1], argv[2]);
    
      namespace deploy = ::google::cloud::deploy_v1;
      auto client = deploy::CloudDeployClient(deploy::MakeCloudDeployConnection());
    
      for (auto dp : client.ListDeliveryPipelines(location.FullName())) {
        if (!dp) throw std::move(dp).status();
        std::cout << dp->DebugString() << "\n";
      }
    
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }

### Node.js
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The parent, which owns this collection of pipelines. Format must be
     *  projects/{project_id}/locations/{location_name}.
     */
    // const parent = 'abc123'
    /**
     *  The maximum number of pipelines to return. The service may return
     *  fewer than this value. If unspecified, at most 50 pipelines will
     *  be returned. The maximum value is 1000; values above 1000 will be set
     *  to 1000.
     */
    // const pageSize = 1234
    /**
     *  A page token, received from a previous `ListDeliveryPipelines` call.
     *  Provide this to retrieve the subsequent page.
     *  When paginating, all other provided parameters match
     *  the call that provided the page token.
     */
    // const pageToken = 'abc123'
    /**
     *  Filter builds to be returned. See https://google.aip.dev/160 for more
     *  details.
     */
    // const filter = 'abc123'
    /**
     *  Field to sort by. See https://google.aip.dev/132#ordering for more details.
     */
    // const orderBy = 'abc123'
    
    // Imports the Deploy library
    const {CloudDeployClient} = require('[@google-cloud/deploy](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)').v1;
    
    // Instantiates a client
    const deployClient = new [CloudDeployClient](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)();
    
    async function listDeliveryPipelines() {
      // Construct request
      const request = {
        parent,
      };
    
      // Run request
      const iterable = await deployClient.[listDeliveryPipelinesAsync](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/v1.clouddeployclient.html)(request);
      for await (const response of iterable) {
        console.log(response);
      }
    }
    
    listDeliveryPipelines();

## Additional resources

### C++

The following list contains links to more resources related to the client library for C++:

  * [API reference](https://docs.cloud.google.com/cpp/docs/reference/deploy/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues)
  * [`google-cloud-deploy` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-deploy%5D%5Bc%2B%2B%5D)
  * [Source code](https://github.com/googleapis/google-cloud-cpp)



### C#

The following list contains links to more resources related to the client library for C#:

  * [API reference](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Deploy.V1/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues)
  * [`google-cloud-deploy` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-deploy%5D+%5Bc%23%5D)
  * [Source code](https://github.com/googleapis/google-cloud-dotnet)



### Go

The following list contains links to more resources related to the client library for Go:

  * [API reference](https://pkg.go.dev/cloud.google.com/go/deploy)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-go/tree/main/deploy/issues)
  * [`google-cloud-deploy` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-deploy%5D+%5Bgo%5D)
  * [Source code](https://github.com/googleapis/google-cloud-go/tree/main/deploy)



### Java

The following list contains links to more resources related to the client library for Java:

  * [API reference](https://cloud.google.com/java/docs/reference/google-cloud-deploy/latest/overview)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/java-deploy/issues)
  * [`google-cloud-deploy` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-deploy%5D+%5Bjava%5D)
  * [Source code](https://github.com/googleapis/java-deploy)



### Node.js

The following list contains links to more resources related to the client library for Node.js:

  * [API reference](https://cloud.google.com/nodejs/docs/reference/deploy/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/nodejs-deploy/issues)
  * [`google-cloud-deploy` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-deploy%5D+%5Bnode.js%5D)
  * [Source code](https://github.com/googleapis/nodejs-deploy)



### PHP

The following list contains links to more resources related to the client library for PHP:

  * [API reference](https://googleapis.github.io/google-cloud-php/#/docs/cloud-deploy)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-php-deploy/issues)
  * [`google-cloud-deploy` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-deploy%5D+%5Bphp%5D)
  * [Source code](https://github.com/googleapis/google-cloud-php-deploy)



### Python

The following list contains links to more resources related to the client library for Python:

  * [API reference](https://cloud.google.com/python/docs/reference/clouddeploy/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/python-deploy/issues)
  * [`google-cloud-deploy` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-deploy%5D+%5Bpython%5D)
  * [Source code](https://github.com/googleapis/python-deploy)



### Ruby

The following list contains links to more resources related to the client library for Ruby:

  * [API reference](https://googleapis.dev/ruby/google-cloud-deploy-v1/latest/Google/Cloud/Deploy/V1.html)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-ruby/tree/main/google-cloud-deploy/issues)
  * [`google-cloud-deploy` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-deploy%5D+%5Bruby%5D)
  * [Source code](https://github.com/googleapis/google-cloud-ruby/tree/main/google-cloud-deploy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
