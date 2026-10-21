---
url: https://docs.cloud.google.com/docs/quotas/reference/libraries/
title: Cloud Quotas client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:19.691969+00:00
---

# Cloud Quotas client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/reference/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Reference ](https://docs.cloud.google.com/docs/quotas/apis)



Send feedback 

#  Cloud Quotas client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to get started with the Cloud Client Libraries for the Cloud Quotas API. Client libraries make it easier to access Google Cloud APIs from a supported language. Although you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

Read more about the Cloud Client Libraries and the older Google API Client Libraries in [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

## Install the client library

### C++

For information about this client library's requirements and install dependencies, see [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup). 

### C#

Install the `Google.Cloud.CloudQuotas.V1` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages..."). 

For more information, see [Setting Up a C# Development Environment](https://docs.cloud.google.com/dotnet/docs/setup).

### Go
    
    
    go get cloud.google.com/go/cloudquotas

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
        <artifactId>google-cloud-cloudquotas</artifactId>
      </dependency>
    </dependencies>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.90.0')
    
    implementation 'com.google.cloud:google-cloud-cloudquotas'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-cloudquotas" % "0.67.0"

For more information, see [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).

### Node.js
    
    
    npm install @google-cloud/cloudquotas

For more information, see [Setting Up a Node.js Development Environment](https://docs.cloud.google.com/nodejs/docs/setup).

### PHP
    
    
    composer require google/cloud

For more information, see [Using PHP on Google Cloud](https://docs.cloud.google.com/php/docs).

### Python
    
    
    pip install google-cloud-quotas

For more information, see [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).

### Ruby
    
    
    gem install google-cloud-cloud_quotas

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
    
    
    // Copyright 2024 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    // https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    //! [all]
    #include "google/cloud/cloudquotas/v1/cloud_quotas_client.h"
    #include "google/cloud/location.h"
    #include <iostream>
    #include <string>
    
    int main(int argc, char* argv[]) try {
      if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " project-id\n";
        return 1;
      }
    
      namespace cloudquotas = ::google::cloud::cloudquotas_v1;
      auto client =
          cloudquotas::CloudQuotasClient(cloudquotas::MakeCloudQuotasConnection());
    
      auto const parent = google::cloud::Location(argv[1], "global").FullName();
      for (auto r : client.ListQuotaPreferences(parent)) {
        if (!r) throw std::move(r).status();
        std::cout << r->DebugString() << "\n";
      }
    
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }
    //! [all]
    

### C#
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    // Generated code. DO NOT EDIT!
    
    namespace GoogleCSharpSnippets
    {
        using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
        using [Google.Cloud.CloudQuotas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.html);
        using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
        using System;
        using System.Threading.Tasks;
    
        /// <summary>Generated snippets.</summary>
        public sealed class AllGeneratedCloudQuotasClientSnippets
        {
            /// <summary>Snippet for ListQuotaInfos</summary>
            public void ListQuotaInfosRequestObject()
            {
                // Snippet: ListQuotaInfos(ListQuotaInfosRequest, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                [ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest.html) request = new [ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest.html)
                {
                    ParentAsServiceName = [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html).[FromProjectLocationService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html#Google_Cloud_CloudQuotas_V1_ServiceName_FromProjectLocationService_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[SERVICE]"),
                };
                // Make the request
                PagedEnumerable<ListQuotaInfosResponse, QuotaInfo> response = cloudQuotasClient.[ListQuotaInfos](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaInfos_Google_Cloud_CloudQuotas_V1_ListQuotaInfosRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
                // Iterate over all response items, lazily performing RPCs as required
                foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in response)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                foreach ([ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse.html) page in response.AsRawResponses())
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<QuotaInfo> singlePage = response.ReadPage(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
                // End snippet
            }
    
            /// <summary>Snippet for ListQuotaInfosAsync</summary>
            public async Task ListQuotaInfosRequestObjectAsync()
            {
                // Snippet: ListQuotaInfosAsync(ListQuotaInfosRequest, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                [ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest.html) request = new [ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest.html)
                {
                    ParentAsServiceName = [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html).[FromProjectLocationService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html#Google_Cloud_CloudQuotas_V1_ServiceName_FromProjectLocationService_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[SERVICE]"),
                };
                // Make the request
                PagedAsyncEnumerable<ListQuotaInfosResponse, QuotaInfo> response = cloudQuotasClient.[ListQuotaInfosAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaInfosAsync_Google_Cloud_CloudQuotas_V1_ListQuotaInfosRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
                // Iterate over all response items, lazily performing RPCs as required
                await foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in response)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                await foreach ([ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse.html) page in response.AsRawResponses())
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<QuotaInfo> singlePage = await response.ReadPageAsync(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
                // End snippet
            }
    
            /// <summary>Snippet for ListQuotaInfos</summary>
            public void ListQuotaInfos()
            {
                // Snippet: ListQuotaInfos(string, string, int?, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
                // Make the request
                PagedEnumerable<ListQuotaInfosResponse, QuotaInfo> response = cloudQuotasClient.[ListQuotaInfos](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaInfos_Google_Cloud_CloudQuotas_V1_ListQuotaInfosRequest_Google_Api_Gax_Grpc_CallSettings_)(parent);
    
                // Iterate over all response items, lazily performing RPCs as required
                foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in response)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                foreach ([ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse.html) page in response.AsRawResponses())
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<QuotaInfo> singlePage = response.ReadPage(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
                // End snippet
            }
    
            /// <summary>Snippet for ListQuotaInfosAsync</summary>
            public async Task ListQuotaInfosAsync()
            {
                // Snippet: ListQuotaInfosAsync(string, string, int?, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                string parent = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]";
                // Make the request
                PagedAsyncEnumerable<ListQuotaInfosResponse, QuotaInfo> response = cloudQuotasClient.[ListQuotaInfosAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaInfosAsync_Google_Cloud_CloudQuotas_V1_ListQuotaInfosRequest_Google_Api_Gax_Grpc_CallSettings_)(parent);
    
                // Iterate over all response items, lazily performing RPCs as required
                await foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in response)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                await foreach ([ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse.html) page in response.AsRawResponses())
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<QuotaInfo> singlePage = await response.ReadPageAsync(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
                // End snippet
            }
    
            /// <summary>Snippet for ListQuotaInfos</summary>
            public void ListQuotaInfosResourceNames()
            {
                // Snippet: ListQuotaInfos(ServiceName, string, int?, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html) parent = [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html).[FromProjectLocationService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html#Google_Cloud_CloudQuotas_V1_ServiceName_FromProjectLocationService_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[SERVICE]");
                // Make the request
                PagedEnumerable<ListQuotaInfosResponse, QuotaInfo> response = cloudQuotasClient.[ListQuotaInfos](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaInfos_Google_Cloud_CloudQuotas_V1_ListQuotaInfosRequest_Google_Api_Gax_Grpc_CallSettings_)(parent);
    
                // Iterate over all response items, lazily performing RPCs as required
                foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in response)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                foreach ([ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse.html) page in response.AsRawResponses())
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<QuotaInfo> singlePage = response.ReadPage(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
                // End snippet
            }
    
            /// <summary>Snippet for ListQuotaInfosAsync</summary>
            public async Task ListQuotaInfosResourceNamesAsync()
            {
                // Snippet: ListQuotaInfosAsync(ServiceName, string, int?, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html) parent = [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html).[FromProjectLocationService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.html#Google_Cloud_CloudQuotas_V1_ServiceName_FromProjectLocationService_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[SERVICE]");
                // Make the request
                PagedAsyncEnumerable<ListQuotaInfosResponse, QuotaInfo> response = cloudQuotasClient.[ListQuotaInfosAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaInfosAsync_Google_Cloud_CloudQuotas_V1_ListQuotaInfosRequest_Google_Api_Gax_Grpc_CallSettings_)(parent);
    
                // Iterate over all response items, lazily performing RPCs as required
                await foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in response)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                await foreach ([ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse.html) page in response.AsRawResponses())
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<QuotaInfo> singlePage = await response.ReadPageAsync(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach ([QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
                // End snippet
            }
    
            /// <summary>Snippet for GetQuotaInfo</summary>
            public void GetQuotaInfoRequestObject()
            {
                // Snippet: GetQuotaInfo(GetQuotaInfoRequest, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                [GetQuotaInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest.html) request = new [GetQuotaInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest.html)
                {
                    QuotaInfoName = [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html).[FromProjectLocationServiceQuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html#Google_Cloud_CloudQuotas_V1_QuotaInfoName_FromProjectLocationServiceQuotaInfo_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]"),
                };
                // Make the request
                [QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) response = cloudQuotasClient.[GetQuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaInfo_Google_Cloud_CloudQuotas_V1_GetQuotaInfoRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
                // End snippet
            }
    
            /// <summary>Snippet for GetQuotaInfoAsync</summary>
            public async Task GetQuotaInfoRequestObjectAsync()
            {
                // Snippet: GetQuotaInfoAsync(GetQuotaInfoRequest, CallSettings)
                // Additional: GetQuotaInfoAsync(GetQuotaInfoRequest, CancellationToken)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                [GetQuotaInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest.html) request = new [GetQuotaInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest.html)
                {
                    QuotaInfoName = [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html).[FromProjectLocationServiceQuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html#Google_Cloud_CloudQuotas_V1_QuotaInfoName_FromProjectLocationServiceQuotaInfo_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]"),
                };
                // Make the request
                [QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) response = await cloudQuotasClient.[GetQuotaInfoAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaInfoAsync_Google_Cloud_CloudQuotas_V1_GetQuotaInfoRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
                // End snippet
            }
    
            /// <summary>Snippet for GetQuotaInfo</summary>
            public void GetQuotaInfo()
            {
                // Snippet: GetQuotaInfo(string, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/quotaInfos/[QUOTA_INFO]";
                // Make the request
                [QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) response = cloudQuotasClient.[GetQuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaInfo_Google_Cloud_CloudQuotas_V1_GetQuotaInfoRequest_Google_Api_Gax_Grpc_CallSettings_)(name);
                // End snippet
            }
    
            /// <summary>Snippet for GetQuotaInfoAsync</summary>
            public async Task GetQuotaInfoAsync()
            {
                // Snippet: GetQuotaInfoAsync(string, CallSettings)
                // Additional: GetQuotaInfoAsync(string, CancellationToken)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                string name = "projects/[PROJECT]/locations/[LOCATION]/services/[SERVICE]/quotaInfos/[QUOTA_INFO]";
                // Make the request
                [QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) response = await cloudQuotasClient.[GetQuotaInfoAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaInfoAsync_Google_Cloud_CloudQuotas_V1_GetQuotaInfoRequest_Google_Api_Gax_Grpc_CallSettings_)(name);
                // End snippet
            }
    
            /// <summary>Snippet for GetQuotaInfo</summary>
            public void GetQuotaInfoResourceNames()
            {
                // Snippet: GetQuotaInfo(QuotaInfoName, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html) name = [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html).[FromProjectLocationServiceQuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html#Google_Cloud_CloudQuotas_V1_QuotaInfoName_FromProjectLocationServiceQuotaInfo_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]");
                // Make the request
                [QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) response = cloudQuotasClient.[GetQuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaInfo_Google_Cloud_CloudQuotas_V1_GetQuotaInfoRequest_Google_Api_Gax_Grpc_CallSettings_)(name);
                // End snippet
            }
    
            /// <summary>Snippet for GetQuotaInfoAsync</summary>
            public async Task GetQuotaInfoResourceNamesAsync()
            {
                // Snippet: GetQuotaInfoAsync(QuotaInfoName, CallSettings)
                // Additional: GetQuotaInfoAsync(QuotaInfoName, CancellationToken)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html) name = [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html).[FromProjectLocationServiceQuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.html#Google_Cloud_CloudQuotas_V1_QuotaInfoName_FromProjectLocationServiceQuotaInfo_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]");
                // Make the request
                [QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.html) response = await cloudQuotasClient.[GetQuotaInfoAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaInfoAsync_Google_Cloud_CloudQuotas_V1_GetQuotaInfoRequest_Google_Api_Gax_Grpc_CallSettings_)(name);
                // End snippet
            }
    
            /// <summary>Snippet for ListQuotaPreferences</summary>
            public void ListQuotaPreferencesRequestObject()
            {
                // Snippet: ListQuotaPreferences(ListQuotaPreferencesRequest, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                [ListQuotaPreferencesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest.html) request = new [ListQuotaPreferencesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest.html)
                {
                    ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                    Filter = "",
                    OrderBy = "",
                };
                // Make the request
                PagedEnumerable<ListQuotaPreferencesResponse, QuotaPreference> response = cloudQuotasClient.[ListQuotaPreferences](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaPreferences_Google_Cloud_CloudQuotas_V1_ListQuotaPreferencesRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
                // Iterate over all response items, lazily performing RPCs as required
                foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in response)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                foreach ([ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse.html) page in response.AsRawResponses())
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<QuotaPreference> singlePage = response.ReadPage(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
                // End snippet
            }
    
            /// <summary>Snippet for ListQuotaPreferencesAsync</summary>
            public async Task ListQuotaPreferencesRequestObjectAsync()
            {
                // Snippet: ListQuotaPreferencesAsync(ListQuotaPreferencesRequest, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                [ListQuotaPreferencesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest.html) request = new [ListQuotaPreferencesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest.html)
                {
                    ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                    Filter = "",
                    OrderBy = "",
                };
                // Make the request
                PagedAsyncEnumerable<ListQuotaPreferencesResponse, QuotaPreference> response = cloudQuotasClient.[ListQuotaPreferencesAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaPreferencesAsync_Google_Cloud_CloudQuotas_V1_ListQuotaPreferencesRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
                // Iterate over all response items, lazily performing RPCs as required
                await foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in response)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                await foreach ([ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse.html) page in response.AsRawResponses())
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<QuotaPreference> singlePage = await response.ReadPageAsync(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
                // End snippet
            }
    
            /// <summary>Snippet for ListQuotaPreferences</summary>
            public void ListQuotaPreferences()
            {
                // Snippet: ListQuotaPreferences(string, string, int?, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                string parent = "projects/[PROJECT]/locations/[LOCATION]";
                // Make the request
                PagedEnumerable<ListQuotaPreferencesResponse, QuotaPreference> response = cloudQuotasClient.[ListQuotaPreferences](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaPreferences_Google_Cloud_CloudQuotas_V1_ListQuotaPreferencesRequest_Google_Api_Gax_Grpc_CallSettings_)(parent);
    
                // Iterate over all response items, lazily performing RPCs as required
                foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in response)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                foreach ([ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse.html) page in response.AsRawResponses())
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<QuotaPreference> singlePage = response.ReadPage(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
                // End snippet
            }
    
            /// <summary>Snippet for ListQuotaPreferencesAsync</summary>
            public async Task ListQuotaPreferencesAsync()
            {
                // Snippet: ListQuotaPreferencesAsync(string, string, int?, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                string parent = "projects/[PROJECT]/locations/[LOCATION]";
                // Make the request
                PagedAsyncEnumerable<ListQuotaPreferencesResponse, QuotaPreference> response = cloudQuotasClient.[ListQuotaPreferencesAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaPreferencesAsync_Google_Cloud_CloudQuotas_V1_ListQuotaPreferencesRequest_Google_Api_Gax_Grpc_CallSettings_)(parent);
    
                // Iterate over all response items, lazily performing RPCs as required
                await foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in response)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                await foreach ([ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse.html) page in response.AsRawResponses())
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<QuotaPreference> singlePage = await response.ReadPageAsync(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
                // End snippet
            }
    
            /// <summary>Snippet for ListQuotaPreferences</summary>
            public void ListQuotaPreferencesResourceNames()
            {
                // Snippet: ListQuotaPreferences(LocationName, string, int?, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]");
                // Make the request
                PagedEnumerable<ListQuotaPreferencesResponse, QuotaPreference> response = cloudQuotasClient.[ListQuotaPreferences](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaPreferences_Google_Cloud_CloudQuotas_V1_ListQuotaPreferencesRequest_Google_Api_Gax_Grpc_CallSettings_)(parent);
    
                // Iterate over all response items, lazily performing RPCs as required
                foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in response)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                foreach ([ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse.html) page in response.AsRawResponses())
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<QuotaPreference> singlePage = response.ReadPage(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
                // End snippet
            }
    
            /// <summary>Snippet for ListQuotaPreferencesAsync</summary>
            public async Task ListQuotaPreferencesResourceNamesAsync()
            {
                // Snippet: ListQuotaPreferencesAsync(LocationName, string, int?, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]");
                // Make the request
                PagedAsyncEnumerable<ListQuotaPreferencesResponse, QuotaPreference> response = cloudQuotasClient.[ListQuotaPreferencesAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_ListQuotaPreferencesAsync_Google_Cloud_CloudQuotas_V1_ListQuotaPreferencesRequest_Google_Api_Gax_Grpc_CallSettings_)(parent);
    
                // Iterate over all response items, lazily performing RPCs as required
                await foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in response)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
    
                // Or iterate over pages (of server-defined size), performing one RPC per page
                await foreach ([ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse.html) page in response.AsRawResponses())
                {
                    // Do something with each page of items
                    Console.WriteLine("A page of results:");
                    foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in page)
                    {
                        // Do something with each item
                        Console.WriteLine(item);
                    }
                }
    
                // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
                int pageSize = 10;
                Page<QuotaPreference> singlePage = await response.ReadPageAsync(pageSize);
                // Do something with the page of items
                Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
                foreach ([QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) item in singlePage)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
                // Store the pageToken, for when the next page is required.
                string nextPageToken = singlePage.NextPageToken;
                // End snippet
            }
    
            /// <summary>Snippet for GetQuotaPreference</summary>
            public void GetQuotaPreferenceRequestObject()
            {
                // Snippet: GetQuotaPreference(GetQuotaPreferenceRequest, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                [GetQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest.html) request = new [GetQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest.html)
                {
                    QuotaPreferenceName = [QuotaPreferenceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html).[FromProjectLocationQuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html#Google_Cloud_CloudQuotas_V1_QuotaPreferenceName_FromProjectLocationQuotaPreference_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[QUOTA_PREFERENCE]"),
                };
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient.[GetQuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaPreference_Google_Cloud_CloudQuotas_V1_GetQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
                // End snippet
            }
    
            /// <summary>Snippet for GetQuotaPreferenceAsync</summary>
            public async Task GetQuotaPreferenceRequestObjectAsync()
            {
                // Snippet: GetQuotaPreferenceAsync(GetQuotaPreferenceRequest, CallSettings)
                // Additional: GetQuotaPreferenceAsync(GetQuotaPreferenceRequest, CancellationToken)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                [GetQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest.html) request = new [GetQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest.html)
                {
                    QuotaPreferenceName = [QuotaPreferenceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html).[FromProjectLocationQuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html#Google_Cloud_CloudQuotas_V1_QuotaPreferenceName_FromProjectLocationQuotaPreference_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[QUOTA_PREFERENCE]"),
                };
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient.[GetQuotaPreferenceAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_GetQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
                // End snippet
            }
    
            /// <summary>Snippet for GetQuotaPreference</summary>
            public void GetQuotaPreference()
            {
                // Snippet: GetQuotaPreference(string, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                string name = "projects/[PROJECT]/locations/[LOCATION]/quotaPreferences/[QUOTA_PREFERENCE]";
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient.[GetQuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaPreference_Google_Cloud_CloudQuotas_V1_GetQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(name);
                // End snippet
            }
    
            /// <summary>Snippet for GetQuotaPreferenceAsync</summary>
            public async Task GetQuotaPreferenceAsync()
            {
                // Snippet: GetQuotaPreferenceAsync(string, CallSettings)
                // Additional: GetQuotaPreferenceAsync(string, CancellationToken)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                string name = "projects/[PROJECT]/locations/[LOCATION]/quotaPreferences/[QUOTA_PREFERENCE]";
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient.[GetQuotaPreferenceAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_GetQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(name);
                // End snippet
            }
    
            /// <summary>Snippet for GetQuotaPreference</summary>
            public void GetQuotaPreferenceResourceNames()
            {
                // Snippet: GetQuotaPreference(QuotaPreferenceName, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                [QuotaPreferenceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html) name = [QuotaPreferenceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html).[FromProjectLocationQuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html#Google_Cloud_CloudQuotas_V1_QuotaPreferenceName_FromProjectLocationQuotaPreference_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[QUOTA_PREFERENCE]");
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient.[GetQuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaPreference_Google_Cloud_CloudQuotas_V1_GetQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(name);
                // End snippet
            }
    
            /// <summary>Snippet for GetQuotaPreferenceAsync</summary>
            public async Task GetQuotaPreferenceResourceNamesAsync()
            {
                // Snippet: GetQuotaPreferenceAsync(QuotaPreferenceName, CallSettings)
                // Additional: GetQuotaPreferenceAsync(QuotaPreferenceName, CancellationToken)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                [QuotaPreferenceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html) name = [QuotaPreferenceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html).[FromProjectLocationQuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.html#Google_Cloud_CloudQuotas_V1_QuotaPreferenceName_FromProjectLocationQuotaPreference_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[QUOTA_PREFERENCE]");
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient.[GetQuotaPreferenceAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_GetQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_GetQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(name);
                // End snippet
            }
    
            /// <summary>Snippet for CreateQuotaPreference</summary>
            public void CreateQuotaPreferenceRequestObject()
            {
                // Snippet: CreateQuotaPreference(CreateQuotaPreferenceRequest, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                [CreateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest.html) request = new [CreateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest.html)
                {
                    ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                    QuotaPreferenceId = "",
                    QuotaPreference = new [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html)(),
                    IgnoreSafetyChecks =
                    {
                        [QuotaSafetyCheck](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html).[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html#Google_Cloud_CloudQuotas_V1_QuotaSafetyCheck_Unspecified),
                    },
                };
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient.[CreateQuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreference_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
                // End snippet
            }
    
            /// <summary>Snippet for CreateQuotaPreferenceAsync</summary>
            public async Task CreateQuotaPreferenceRequestObjectAsync()
            {
                // Snippet: CreateQuotaPreferenceAsync(CreateQuotaPreferenceRequest, CallSettings)
                // Additional: CreateQuotaPreferenceAsync(CreateQuotaPreferenceRequest, CancellationToken)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                [CreateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest.html) request = new [CreateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest.html)
                {
                    ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                    QuotaPreferenceId = "",
                    QuotaPreference = new [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html)(),
                    IgnoreSafetyChecks =
                    {
                        [QuotaSafetyCheck](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html).[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html#Google_Cloud_CloudQuotas_V1_QuotaSafetyCheck_Unspecified),
                    },
                };
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient.[CreateQuotaPreferenceAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
                // End snippet
            }
    
            /// <summary>Snippet for CreateQuotaPreference</summary>
            public void CreateQuotaPreference1()
            {
                // Snippet: CreateQuotaPreference(string, QuotaPreference, string, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                string parent = "projects/[PROJECT]/locations/[LOCATION]";
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html)();
                string quotaPreferenceId = "";
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient.[CreateQuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreference_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(parent, quotaPreference, quotaPreferenceId);
                // End snippet
            }
    
            /// <summary>Snippet for CreateQuotaPreferenceAsync</summary>
            public async Task CreateQuotaPreference1Async()
            {
                // Snippet: CreateQuotaPreferenceAsync(string, QuotaPreference, string, CallSettings)
                // Additional: CreateQuotaPreferenceAsync(string, QuotaPreference, string, CancellationToken)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                string parent = "projects/[PROJECT]/locations/[LOCATION]";
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html)();
                string quotaPreferenceId = "";
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient.[CreateQuotaPreferenceAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(parent, quotaPreference, quotaPreferenceId);
                // End snippet
            }
    
            /// <summary>Snippet for CreateQuotaPreference</summary>
            public void CreateQuotaPreference1ResourceNames()
            {
                // Snippet: CreateQuotaPreference(LocationName, QuotaPreference, string, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]");
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html)();
                string quotaPreferenceId = "";
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient.[CreateQuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreference_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(parent, quotaPreference, quotaPreferenceId);
                // End snippet
            }
    
            /// <summary>Snippet for CreateQuotaPreferenceAsync</summary>
            public async Task CreateQuotaPreference1ResourceNamesAsync()
            {
                // Snippet: CreateQuotaPreferenceAsync(LocationName, QuotaPreference, string, CallSettings)
                // Additional: CreateQuotaPreferenceAsync(LocationName, QuotaPreference, string, CancellationToken)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]");
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html)();
                string quotaPreferenceId = "";
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient.[CreateQuotaPreferenceAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(parent, quotaPreference, quotaPreferenceId);
                // End snippet
            }
    
            /// <summary>Snippet for CreateQuotaPreference</summary>
            public void CreateQuotaPreference2()
            {
                // Snippet: CreateQuotaPreference(string, QuotaPreference, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                string parent = "projects/[PROJECT]/locations/[LOCATION]";
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html)();
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient.[CreateQuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreference_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(parent, quotaPreference);
                // End snippet
            }
    
            /// <summary>Snippet for CreateQuotaPreferenceAsync</summary>
            public async Task CreateQuotaPreference2Async()
            {
                // Snippet: CreateQuotaPreferenceAsync(string, QuotaPreference, CallSettings)
                // Additional: CreateQuotaPreferenceAsync(string, QuotaPreference, CancellationToken)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                string parent = "projects/[PROJECT]/locations/[LOCATION]";
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html)();
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient.[CreateQuotaPreferenceAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(parent, quotaPreference);
                // End snippet
            }
    
            /// <summary>Snippet for CreateQuotaPreference</summary>
            public void CreateQuotaPreference2ResourceNames()
            {
                // Snippet: CreateQuotaPreference(LocationName, QuotaPreference, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]");
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html)();
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient.[CreateQuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreference_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(parent, quotaPreference);
                // End snippet
            }
    
            /// <summary>Snippet for CreateQuotaPreferenceAsync</summary>
            public async Task CreateQuotaPreference2ResourceNamesAsync()
            {
                // Snippet: CreateQuotaPreferenceAsync(LocationName, QuotaPreference, CallSettings)
                // Additional: CreateQuotaPreferenceAsync(LocationName, QuotaPreference, CancellationToken)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.html#Google_Cloud_CloudQuotas_V1_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]");
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html)();
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient.[CreateQuotaPreferenceAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_CreateQuotaPreferenceRequest_Google_Api_Gax_Grpc_CallSettings_)(parent, quotaPreference);
                // End snippet
            }
    
            /// <summary>Snippet for UpdateQuotaPreference</summary>
            public void UpdateQuotaPreferenceRequestObject()
            {
                // Snippet: UpdateQuotaPreference(UpdateQuotaPreferenceRequest, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                [UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest.html) request = new [UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest.html)
                {
                    UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)(),
                    QuotaPreference = new [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html)(),
                    AllowMissing = false,
                    ValidateOnly = false,
                    IgnoreSafetyChecks =
                    {
                        [QuotaSafetyCheck](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html).[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html#Google_Cloud_CloudQuotas_V1_QuotaSafetyCheck_Unspecified),
                    },
                };
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient.[UpdateQuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_UpdateQuotaPreference_Google_Cloud_CloudQuotas_V1_QuotaPreference_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(request);
                // End snippet
            }
    
            /// <summary>Snippet for UpdateQuotaPreferenceAsync</summary>
            public async Task UpdateQuotaPreferenceRequestObjectAsync()
            {
                // Snippet: UpdateQuotaPreferenceAsync(UpdateQuotaPreferenceRequest, CallSettings)
                // Additional: UpdateQuotaPreferenceAsync(UpdateQuotaPreferenceRequest, CancellationToken)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                [UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest.html) request = new [UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest.html)
                {
                    UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)(),
                    QuotaPreference = new [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html)(),
                    AllowMissing = false,
                    ValidateOnly = false,
                    IgnoreSafetyChecks =
                    {
                        [QuotaSafetyCheck](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html).[Unspecified](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck.html#Google_Cloud_CloudQuotas_V1_QuotaSafetyCheck_Unspecified),
                    },
                };
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient.[UpdateQuotaPreferenceAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_UpdateQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_QuotaPreference_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(request);
                // End snippet
            }
    
            /// <summary>Snippet for UpdateQuotaPreference</summary>
            public void UpdateQuotaPreference()
            {
                // Snippet: UpdateQuotaPreference(QuotaPreference, FieldMask, CallSettings)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_Create)();
                // Initialize request argument(s)
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html)();
                [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) updateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)();
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = cloudQuotasClient.[UpdateQuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_UpdateQuotaPreference_Google_Cloud_CloudQuotas_V1_QuotaPreference_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(quotaPreference, updateMask);
                // End snippet
            }
    
            /// <summary>Snippet for UpdateQuotaPreferenceAsync</summary>
            public async Task UpdateQuotaPreferenceAsync()
            {
                // Snippet: UpdateQuotaPreferenceAsync(QuotaPreference, FieldMask, CallSettings)
                // Additional: UpdateQuotaPreferenceAsync(QuotaPreference, FieldMask, CancellationToken)
                // Create client
                [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html) cloudQuotasClient = await [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_CreateAsync_System_Threading_CancellationToken_)();
                // Initialize request argument(s)
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) quotaPreference = new [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html)();
                [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) updateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)();
                // Make the request
                [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference.html) response = await cloudQuotasClient.[UpdateQuotaPreferenceAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient.html#Google_Cloud_CloudQuotas_V1_CloudQuotasClient_UpdateQuotaPreferenceAsync_Google_Cloud_CloudQuotas_V1_QuotaPreference_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(quotaPreference, updateMask);
                // End snippet
            }
        }
    }
    

### Go
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    // Code generated by protoc-gen-go_gapic. DO NOT EDIT.
    
    package cloudquotas_test
    
    import (
    	"context"
    
    	cloudquotas "cloud.google.com/go/cloudquotas/apiv1"
    	cloudquotaspb "cloud.google.com/go/cloudquotas/apiv1/cloudquotaspb"
    	"google.golang.org/api/iterator"
    )
    
    func ExampleNewClient() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    
    func ExampleNewRESTClient() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewRESTClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	// TODO: Use client.
    	_ = c
    }
    
    func ExampleClient_CreateQuotaPreference() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.CreateQuotaPreferenceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1/cloudquotaspb#CreateQuotaPreferenceRequest.
    	}
    	resp, err := c.CreateQuotaPreference(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    
    func ExampleClient_GetQuotaInfo() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.GetQuotaInfoRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1/cloudquotaspb#GetQuotaInfoRequest.
    	}
    	resp, err := c.GetQuotaInfo(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    
    func ExampleClient_GetQuotaPreference() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.GetQuotaPreferenceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1/cloudquotaspb#GetQuotaPreferenceRequest.
    	}
    	resp, err := c.GetQuotaPreference(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    
    func ExampleClient_ListQuotaInfos() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.ListQuotaInfosRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1/cloudquotaspb#ListQuotaInfosRequest.
    	}
    	it := c.ListQuotaInfos(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cloudquotaspb.ListQuotaInfosResponse)
    	}
    }
    
    func ExampleClient_ListQuotaPreferences() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.ListQuotaPreferencesRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1/cloudquotaspb#ListQuotaPreferencesRequest.
    	}
    	it := c.ListQuotaPreferences(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*cloudquotaspb.ListQuotaPreferencesResponse)
    	}
    }
    
    func ExampleClient_UpdateQuotaPreference() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := cloudquotas.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1.html#cloud_google_com_go_cloudquotas_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &cloudquotaspb.UpdateQuotaPreferenceRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/cloudquotas/apiv1/cloudquotaspb#UpdateQuotaPreferenceRequest.
    	}
    	resp, err := c.UpdateQuotaPreference(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java
    
    
    /*
     * Copyright 2026 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
     *
     *      https://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     */
    
    package com.google.api.cloudquotas.v1.samples;
    
    import com.google.api.cloudquotas.v1.[CloudQuotasClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.CloudQuotasClient.html);
    import com.google.api.cloudquotas.v1.[GetQuotaInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.GetQuotaInfoRequest.html);
    import com.google.api.cloudquotas.v1.[QuotaInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaInfo.html);
    import com.google.api.cloudquotas.v1.[QuotaInfoName](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaInfoName.html);
    
    public class SyncGetQuotaInfo {
    
      public static void main(String[] args) throws Exception {
        syncGetQuotaInfo();
      }
    
      public static void syncGetQuotaInfo() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CloudQuotasClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.CloudQuotasClient.html) cloudQuotasClient = [CloudQuotasClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.CloudQuotasClient.html).create()) {
          [GetQuotaInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.GetQuotaInfoRequest.html) request =
              [GetQuotaInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.GetQuotaInfoRequest.html).newBuilder()
                  .setName(
                      [QuotaInfoName](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaInfoName.html).[ofProjectLocationServiceQuotaInfoName](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaInfoName.html#com_google_api_cloudquotas_v1_QuotaInfoName_ofProjectLocationServiceQuotaInfoName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(
                              "[PROJECT]", "[LOCATION]", "[SERVICE]", "[QUOTA_INFO]")
                          .toString())
                  .build();
          [QuotaInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaInfo.html) response = cloudQuotasClient.getQuotaInfo(request);
        }
      }
    }
    

### Node.js
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    //
    // ** This file is automatically generated by gapic-generator-typescript. **
    // ** https://github.com/googleapis/gapic-generator-typescript **
    // ** All changes to this file may be overwritten. **
    
    
    
    'use strict';
    
    function main(name) {
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Identifier. The resource name of the quota info.
       *  An example name:
       *  `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`
       */
      // const name = 'abc123'
    
      // Imports the Cloudquotas library
      const {CloudQuotasClient} = require('[@google-cloud/cloudquotas](https://docs.cloud.google.com/nodejs/docs/reference/cloudquotas/latest/overview.html)').v1;
    
      // Instantiates a client
      const cloudquotasClient = new [CloudQuotasClient](https://docs.cloud.google.com/nodejs/docs/reference/cloudquotas/latest/overview.html)();
    
      async function callGetQuotaInfo() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await cloudquotasClient.getQuotaInfo(request);
        console.log(response);
      }
    
      callGetQuotaInfo();
    }
    
    process.on('unhandledRejection', err => {
      console.error(err.message);
      process.exitCode = 1;
    });
    main(...process.argv.slice(2));
    

### PHP
    
    
    <?php
    /*
     * Copyright 2026 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
     *
     *     https://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     */
    
    /*
     * GENERATED CODE WARNING
     * This file was automatically generated - do not edit!
     */
    
    require_once __DIR__ . '/../../../vendor/autoload.php';
    
    use Google\ApiCore\ApiException;
    use Google\Cloud\CloudQuotas\V1\Client\CloudQuotasClient;
    use Google\Cloud\CloudQuotas\V1\GetQuotaInfoRequest;
    use Google\Cloud\CloudQuotas\V1\QuotaInfo;
    
    /**
     * Retrieve the QuotaInfo of a quota for a project, folder or organization.
     *
     * @param string $formattedName Identifier. The resource name of the quota info.
     *
     *                              An example name:
     *                              `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`
     *                              Please see {@see CloudQuotasClient::quotaInfoName()} for help formatting this field.
     */
    function get_quota_info_sample(string $formattedName): void
    {
        // Create a client.
        $cloudQuotasClient = new CloudQuotasClient();
    
        // Prepare the request message.
        $request = (new GetQuotaInfoRequest())
            ->setName($formattedName);
    
        // Call the API and handle any network failures.
        try {
            /** @var QuotaInfo $response */
            $response = $cloudQuotasClient->getQuotaInfo($request);
            printf('Response data: %s' . PHP_EOL, $response->serializeToJsonString());
        } catch (ApiException $ex) {
            printf('Call failed with message: %s' . PHP_EOL, $ex->getMessage());
        }
    }
    
    /**
     * Helper to execute the sample.
     *
     * This sample has been automatically generated and should be regarded as a code
     * template only. It will require modifications to work:
     *  - It may require correct/in-range values for request initialization.
     *  - It may require specifying regional endpoints when creating the service client,
     *    please see the apiEndpoint client configuration option for more details.
     */
    function callSample(): void
    {
        $formattedName = CloudQuotasClient::quotaInfoName(
            '[PROJECT]',
            '[LOCATION]',
            '[SERVICE]',
            '[QUOTA_INFO]'
        );
    
        get_quota_info_sample($formattedName);
    }
    

### Python
    
    
    # -*- coding: utf-8 -*-
    # Copyright 2026 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    #
    # Generated code. DO NOT EDIT!
    #
    # Snippet for GetQuotaInfo
    # NOTE: This snippet has been automatically generated for illustrative purposes only.
    # It may require modifications to work in your environment.
    
    # To install the latest published package dependency, execute the following:
    #   python3 -m pip install google-cloud-quotas
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest)
    
    
    def sample_get_quota_info():
        # Create a client
        client = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[CloudQuotasClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html)()
    
        # Initialize request argument(s)
        request = [cloudquotas_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest).[GetQuotaInfoRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.types.GetQuotaInfoRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_quota_info](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest/google.cloud.cloudquotas_v1.services.cloud_quotas.CloudQuotasClient.html#google_cloud_cloudquotas_v1_services_cloud_quotas_CloudQuotasClient_get_quota_info)(request=request)
    
        # Handle the response
        print(response)
    
    
    

### Ruby
    
    
    # frozen_string_literal: true
    
    # Copyright 2026 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    # Auto-generated by gapic-generator-ruby. DO NOT EDIT!
    
    require "google/cloud/cloud_quotas/v1"
    
    ##
    # Snippet for the get_quota_info call in the CloudQuotas service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::CloudQuotas::V1::CloudQuotas::Client#get_quota_info.
    #
    def get_quota_info
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::CloudQuotas::V1::CloudQuotas::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::CloudQuotas::V1::GetQuotaInfoRequest.new
    
      # Call the get_quota_info method.
      result = client.get_quota_info request
    
      # The returned object is of type Google::Cloud::CloudQuotas::V1::QuotaInfo.
      p result
    end
    

## Additional resources

### C++

The following list contains links to more resources related to the client library for C++:

  * [API reference](https://docs.cloud.google.com/cpp/docs/reference/cloudquotas/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues)
  * [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D%5Bc%2B%2B%5D)
  * [Source code](https://github.com/googleapis/google-cloud-cpp)



### C#

The following list contains links to more resources related to the client library for C#:

  * [API reference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues)
  * [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D+%5Bc%23%5D)
  * [Source code](https://github.com/googleapis/google-cloud-dotnet)



### Go

The following list contains links to more resources related to the client library for Go:

  * [API reference](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/cloudquotas/latest/apiv1)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-go/issues)
  * [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D+%5Bgo%5D)
  * [Source code](https://github.com/googleapis/google-cloud-go)



### Java

The following list contains links to more resources related to the client library for Java:

  * [API reference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/overview)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-java/issues)
  * [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D+%5Bjava%5D)
  * [Source code](https://github.com/googleapis/google-cloud-java)



### Node.js

The following list contains links to more resources related to the client library for Node.js:

  * [API reference](https://docs.cloud.google.com/nodejs/docs/reference/cloudquotas/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/GoogleCloudPlatform/google-cloud-node/issues)
  * [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D+%5Bnode.js%5D)
  * [Source code](https://github.com/GoogleCloudPlatform/google-cloud-node)



### PHP

The following list contains links to more resources related to the client library for PHP:

  * [API reference](https://docs.cloud.google.com/php/docs/reference/cloud-quotas/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-php/issues)
  * [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D+%5Bphp%5D)
  * [Source code](https://github.com/googleapis/google-cloud-php)



### Python

The following list contains links to more resources related to the client library for Python:

  * [API reference](https://docs.cloud.google.com/python/docs/reference/google-cloud-cloudquotas/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-python/issues)
  * [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D+%5Bpython%5D)
  * [Source code](https://github.com/googleapis/google-cloud-python)



### Ruby

The following list contains links to more resources related to the client library for Ruby:

  * [API reference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-ruby/issues)
  * [`google-cloud-quotas` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-cloud-quotas%5D+%5Bruby%5D)
  * [Source code](https://github.com/googleapis/google-cloud-ruby)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
