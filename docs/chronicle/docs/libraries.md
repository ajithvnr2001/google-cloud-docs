---
url: https://docs.cloud.google.com/chronicle/docs/libraries/
title: Client libraries and SDK \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:42.153082+00:00
---

# Client libraries and SDK  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Client libraries and SDK Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to get started with the Cloud Client Libraries for the Google Security Operations API. Client libraries make it easier to access Google Cloud APIs from a supported language. Although you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

Read more about the Cloud Client Libraries and the older Google API Client Libraries in [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

## Install the client library

### C++

Follow the `[Quickstart](https://github.com/googleapis/google-cloud-cpp/blob/main/google/cloud/chronicle/quickstart/README.md)`.

### C#

Install the `[Google.Cloud.Chronicle.V1](https://www.nuget.org/packages/Google.Cloud.Chronicle.V1)` package from NuGet.

For more information, see [Setting Up a C# Development Environment](https://docs.cloud.google.com/dotnet/docs/setup).

### Go
    
    
    go get cloud.google.com/go/chronicle/apiv1

For more information, see [Setting Up a Go Development Environment](https://docs.cloud.google.com/go/docs/setup).

### Java

If you are using [Maven](https://maven.apache.org/), add the following to your `pom.xml` file. For more information about BOMs, see [The Google Cloud Platform Libraries BOM](https://cloud.google.com/java/docs/bom).
    
    
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>libraries-bom</artifactId>
          <version>26.90.0</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    
    <dependencies>
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-chronicle</artifactId>
      </dependency>
    </dependencies>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.90.0')
    
    implementation 'com.google.cloud:google-cloud-chronicle'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-chronicle" % "0.37.0"

For more information, see [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).

### Node.js
    
    
    npm install @google-cloud/chronicle

For more information, see [Setting Up a Node.js Development Environment](https://docs.cloud.google.com/nodejs/docs/setup).

### PHP
    
    
    composer require google/cloud-chronicle

For more information, see [Using PHP on Google Cloud](https://docs.cloud.google.com/php/docs).

### Python
    
    
    pip install --upgrade google-cloud-chronicle

For more information, see [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).

### Ruby
    
    
    gem install google-cloud-chronicle-v1

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

The following example shows how to use the client library to list reference list. 

### C++
    
    
    #include "google/cloud/chronicle/v1/chronicle_client.h"
    #include "google/cloud/common_options.h"
    #include <iostream>
    #include <string>
    
    int main(int argc, char* argv[]) {
      // TODO(developer): Replace these variables before running the sample.
      std::string const project_id = "";
      std::string const instance_id = "";
      std::string const location = ""; 
      std::string const endpoint = "-chronicle.googleapis.com";
    
      namespace chronicle = ::google::cloud::chronicle_v1;
    
      auto options = google::cloud::Options{}.set<google::cloud::EndpointOption>(endpoint);
      auto client = chronicle::ChronicleClient(chronicle::MakeChronicleConnection(options));
    
      // Construct the parent resource name
      // Format: projects/{project}/locations/{location}/instances/{instance}
      std::string parent = "projects/" + project_id + "/locations/" + location + "/instances/" + instance_id;
    
      google::cloud::chronicle::v1::ListReferenceListsRequest request;
      request.set_parent(parent);
      std::cout << "Listing reference lists for parent: " << parent << std::endl;
      for (auto const& reference_list : client.ListReferenceLists(request)) {
        if (!reference_list) {
          std::cerr << "Error listing reference lists: " << reference_list.status().message() << std::endl;
          return 1;
        }
        std::cout << "Name: " << reference_list->name() <<std::endl;
        std::cout << "Display Name: " << reference_list->display_name() << std::endl;
      }
      return 0;
    }

### C#
    
    
    using [Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.html);
    
    // TODO(developer): Replace these variables before running the sample.
    const string project  = "";
    const string location = "";
    const string instance = "";
    const string endpoint = ".googleapis.com";
    
    [ReferenceListServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ReferenceListServiceClient.html) client = new [ReferenceListServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ReferenceListServiceClientBuilder.html)
    {
      Endpoint = endpoint,
    }.Build();
    
    string parent = [InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName.html).[FromProjectLocationInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName.html#Google_Cloud_Chronicle_V1_InstanceName_FromProjectLocationInstance_System_String_System_String_System_String_)(project, location, instance).ToString();
    
    foreach ([ReferenceList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ReferenceList.html) referenceList in client.[ListReferenceLists](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ReferenceListServiceClient.html#Google_Cloud_Chronicle_V1_ReferenceListServiceClient_ListReferenceLists_Google_Cloud_Chronicle_V1_InstanceName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(parent))
    {
      Console.WriteLine($"Name:        {referenceList.Name}");
      Console.WriteLine($"Description: {referenceList.Description}");
    }

### Go
    
    
    package main
    import (
      "context"
      "fmt"
      "log"
      chronicle "cloud.google.com/go/chronicle/apiv1"
      chroniclepb "cloud.google.com/go/chronicle/apiv1/chroniclepb"
      "google.golang.org/api/iterator"
      "google.golang.org/api/option"
    )
    
    // TODO(developer): Replace these variables before running the sample.
    const (
      project    = ""
      location   = "us"
      instance   = ""
      apiEndpoint = "us-chronicle.googleapis.com:443"
    )
    
    func main() {
      ctx := context.Background()
      client, err := chronicle.[NewReferenceListClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/chronicle/latest/apiv1.html#cloud_google_com_go_chronicle_apiv1_ReferenceListClient_NewReferenceListClient)(ctx, option.WithEndpoint(apiEndpoint),)
      if err != nil {
        log.Fatalf("failed to create client: %v", err)
      }
      defer client.Close()
    
      parent := fmt.Sprintf("projects/%s/locations/%s/instances/%s", project, location, instance)
    
      req := &chroniclepb.ListReferenceListsRequest{
        Parent: parent,
      }
    
      it := client.ListReferenceLists(ctx, req)
      for {
        resp, err := it.Next()
        if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/chronicle/latest/apiv1.html#cloud_google_com_go_chronicle_apiv1_CreateRetrohuntOperation_Done) {
          break
        }
        if err != nil {
          log.Fatalf("error listing reference lists: %v", err)
        }
        fmt.Printf("Name: %s\n", resp.GetName())
        fmt.Printf("Description: %s\n", resp.GetDescription())
        fmt.Printf("---\n")
        }
    }

### Java
    
    
    package com.example;
    
    import com.google.cloud.chronicle.v1.[InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.InstanceName.html);
    import com.google.cloud.chronicle.v1.[ReferenceList](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ReferenceList.html);
    import com.google.cloud.chronicle.v1.[ReferenceListServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ReferenceListServiceClient.html);
    import com.google.cloud.chronicle.v1.[ReferenceListServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ReferenceListServiceSettings.html);
    
    public class ListReferenceLists {
      // TODO(developer): Replace these variables before running the sample.
      private static final String PROJECT  = "";
      private static final String LOCATION = "";
      private static final String INSTANCE = "";
      private static final String ENDPOINT = "s-chronicle.googleapis.com:443";
    
      public static void main(String[] args) throws Exception {
        [ReferenceListServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ReferenceListServiceSettings.html) settings = [ReferenceListServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ReferenceListServiceSettings.html).newBuilder().setEndpoint(ENDPOINT).build();
    
        try ([ReferenceListServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ReferenceListServiceClient.html) client = [ReferenceListServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ReferenceListServiceClient.html).create(settings)) {
          String parent = [InstanceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.InstanceName.html).of(PROJECT, LOCATION, INSTANCE).toString();
          for ([ReferenceList](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.ReferenceList.html) referenceList : client.listReferenceLists(parent).iterateAll()) {
            System.out.println("Name:        " + referenceList.getName());
            System.out.println("Description: " + referenceList.getDescription());
            System.out.println("---");
          }
        }
      }
    }

### Node.js
    
    
    'use strict';
    
    function main(parent) {
      const {ReferenceListServiceClient} = require('[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)').v1;
    
      const chronicleClient = new [ReferenceListServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)({
        apiEndpoint: 'us-chronicle.googleapis.com',
      });
    
      async function callListReferenceLists() {
        // TODO(developer): Replace these variables before running the sample.
        const request = {
          parent: 'projects/<project-number>/locations/us/instances/<instance-id>'
        };
    
        const iterable = chronicleClient.[listReferenceListsAsync](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/v1.referencelistserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListReferenceLists();
    }
    
    process.on('unhandledRejection', err=> {
      console.error(err.message);
      process.exitCode = 1;
    });
    main(...process.argv.slice(2));

### PHP
    
    
    use Google\ApiCore\ApiException;
    use Google\ApiCore\PagedListResponse;
    use Google\Cloud\Chronicle\V1\Client\ReferenceListServiceClient;
    use Google\Cloud\Chronicle\V1\ListReferenceListsRequest;
    use Google\Cloud\Chronicle\V1\ReferenceList;
    
    // TODO(developer): Replace these variables before running the sample.
    const PROJECT  = '';
    const LOCATION = '';
    const INSTANCE = '';
    const ENDPOINT = '-chronicle.googleapis.com';
    
    $client = new ReferenceListServiceClient([
        'apiEndpoint' => ENDPOINT,
    ]);
    
    $parent = ReferenceListServiceClient::instanceName(PROJECT, LOCATION, INSTANCE);
    
    $request = (new ListReferenceListsRequest())->setParent($parent);
    
    try {
        /** @var PagedListResponse $response _/_
        $response = $client->listReferenceLists($request);
    
        /* @var ReferenceList $referenceList */
        foreach ($response as $referenceList) {
            printf('Name:        %s' . PHP_EOL, $referenceList->getName());
            printf('Description: %s' . PHP_EOL, $referenceList->getDescription());
            printf('---' . PHP_EOL);
        }
    } catch (ApiException $ex) {
        printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
    }

### Python
    
    
    from google.cloud import [chronicle_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest)
    
    # TODO(developer): Replace these variables before running the sample.
    PROJECT_ID = ""
    LOCATION = ""
    INSTANCE_ID = ""
    
    def list_reference_lists():
      client = [chronicle_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest).[ReferenceListServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.services.reference_list_service.ReferenceListServiceClient.html)(client_options={"api_endpoint":"us-chronicle.googleapis.com"})
      parent = f"projects/{PROJECT_ID}/locations/{LOCATION}/instances/{INSTANCE_ID}"
      response = client.[list_reference_lists](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.services.reference_list_service.ReferenceListServiceClient.html#google_cloud_chronicle_v1_services_reference_list_service_ReferenceListServiceClient_list_reference_lists)(parent=parent)
      for reference_list in response:
        print(f"Name: {reference_list.name}")
        print(f"Display Name: {reference_list.display_name}")
    
    if __name__=="__main__":
      list_reference_lists()

### Ruby
    
    
    require "google/cloud/chronicle/v1"
    
    # TODO(developer): Replace these variables before running the sample.
    PROJECT_ID  = ""
    LOCATION    = ""
    INSTANCE_ID = ""
    ENDPOINT    = "-chronicle.googleapis.com"
    
    client = Google::Cloud::Chronicle::V1::ReferenceListService::Client.new do |config|
      config.endpoint = ENDPOINT
    end
    
    parent = "projects/#{PROJECT_ID}/locations/#{LOCATION}/instances/#{INSTANCE_ID}"
    
    request = Google::Cloud::Chronicle::V1::ListReferenceListsRequest.new(parent: parent)
    
    begin
      response = client.list_reference_lists request
    
      response.each do |reference_list|
        puts "Name:        #{reference_list.name}"
        puts "Description: #{reference_list.description}"
      end
    rescue Google::Cloud::Error => e
      puts "API call failed: #{e.message}"
    end

## Additional resources

### C++

The following list contains links to more resources related to the client library for C++:

  * [API reference](https://docs.cloud.google.com/cpp/docs/reference/chronicle/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues)
  * [`google-cloud-chronicle` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-chronicle%5D%5Bc%2B%2B%5D)
  * [Source code](https://github.com/googleapis/google-cloud-cpp)



### C#

The following list contains links to more resources related to the client library for C#:

  * [API reference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues)
  * [`google-cloud-chronicle` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-chronicle%5D+%5Bc%23%5D)
  * [Source code](https://github.com/googleapis/google-cloud-dotnet)



### Go

The following list contains links to more resources related to the client library for Go:

  * [API reference](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/chronicle/latest/apiv1)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-go/issues)
  * [`google-cloud-chronicle` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-chronicle%5D+%5Bgo%5D)
  * [Source code](https://github.com/googleapis/google-cloud-go)



### Java

The following list contains links to more resources related to the client library for Java:

  * [API reference](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/overview)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-java/issues)
  * [`google-cloud-chronicle` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-chronicle%5D+%5Bjava%5D)
  * [Source code](https://github.com/googleapis/google-cloud-java)



### Node.js

The following list contains links to more resources related to the client library for Node.js:

  * [API reference](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-node/issues)
  * [`google-cloud-chronicle` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-chronicle%5D+%5Bnode.js%5D)
  * [Source code](https://github.com/googleapis/google-cloud-node)



### PHP

The following list contains links to more resources related to the client library for PHP:

  * [API reference](https://docs.cloud.google.com/php/docs/reference/cloud-chronicle/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-php/issues)
  * [`google-cloud-chronicle` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-chronicle%5D+%5Bphp%5D)
  * [Source code](https://github.com/googleapis/google-cloud-php)



### Python

The following list contains links to more resources related to the client library for Python:

  * [API reference](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-python/issues)
  * [`google-cloud-chronicle` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-chronicle%5D+%5Bpython%5D)
  * [Source code](https://github.com/googleapis/google-cloud-python)



### Ruby

The following list contains links to more resources related to the client library for Ruby:

  * [API reference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-ruby/issues)
  * [`google-cloud-chronicle` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-chronicle%5D+%5Bruby%5D)
  * [Source code](https://github.com/googleapis/google-cloud-ruby)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
