---
url: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/libraries/
title: Client libraries and sample code for Cloud SQL \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:50:51.333511+00:00
---

# Client libraries and sample code for Cloud SQL  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/sqlserver/apis)



Send feedback 

#  Client libraries and sample code for Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/admin-api/libraries "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/admin-api/libraries "View this page for the PostgreSQL database engine") | SQL Server

The Cloud SQL Admin API is built on HTTP and JSON, so any standard HTTP client can send requests to it and parse the responses. However, instead of creating HTTP requests and parsing responses manually, you may want to use the Google APIs client libraries. The client libraries provide better language integration, improved security, and support for making calls that require user authorization.

Client libraries can use [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to easily authenticate with Google APIs and send requests to those APIs. With Application Default Credentials, you can test your application locally and deploy it without changing the underlying code. For more information, see [ Authenticate for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

Application Default Credentials are part of the client libraries you can use to access Cloud SQL. Default credentials identify your application with either a user credential or a default service account. When working with a library, it's typical to choose credentials based on the type of environment where you run code. For example, in a development environment, you can authenticate with the [`gcloud auth`](https://docs.cloud.google.com/sdk/gcloud/reference/auth) command and the client libraries will use those credentials. For more information about environments, see [Authentication overview](https://docs.cloud.google.com/docs/authentication) in the _Google Cloud Platform Auth Guide_.

## Access the service

Depending on the Cloud SQL Admin API client library you use, you may need to configure how the library discovers the default service path. For client libraries that use the Google APIs Discovery Service, use the API name `sqladmin` to build a client. This includes libraries for Python and JavaScript.

The following code snippets show how to create a client and list Cloud SQL instances in a project.

### C++

For the [C++ Client Library](https://github.com/googleapis/google-cloud-cpp), follow [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup) to install the library. 
    
    
    #include "google/cloud/sql/v1/sql_instances_client.h"
    #include "google/cloud/project.h"
    #include <iostream>
    
    int main(int argc, char* argv[]) try {
      if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " project-id\n";
        return 1;
      }
    
      namespace sql = ::google::cloud::sql_v1;
      auto client = sql::SqlInstancesServiceClient(
          sql::MakeSqlInstancesServiceConnectionRest());
    
      google::cloud::sql::v1::SqlInstancesListRequest request;
      request.set_project(argv[1]);
      for (auto database : client.List(request)) {
        if (!database) throw std::move(database).status();
        std::cout << database->DebugString() << "\n";
      }
    
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }

### Java

For the [Client Library for Java](https://developers.google.com/api-client-library/java/google-api-java-client/dev-guide), you can optionally specify the service path directly.
    
    
    // Set up global SQLAdmin instance.
    client = new SQLAdmin.Builder(httpTransport, JSON_FACTORY, credential)
        .setServicePath("**sql/v1beta4/** ")
        .setApplicationName(APPLICATION_NAME).build();
    InstancesListResponse resp = client.instances().list("PROJECT_ID").execute();
    List<DatabaseInstance> list = resp.getItems();
    for (DatabaseInstance d : list) {
        System.out.println(d.getName());
    }

### Go

For the [Client Library for Go](https://github.com/google/google-api-go-client), import the [`sqladmin`](https://godoc.org/google.golang.org/api/sqladmin) package. 
    
    
    func ListInstances(projectId string) ([]*sqladmin.DatabaseInstance, error) {
    	ctx := context.Background()
    
    	// Create an http.Client that uses Application Default Credentials.
    	hc, err := google.DefaultClient(ctx, sqladmin.SqlserviceAdminScope)
    	if err != nil {
    		return nil, err
    	}
    
    	// Create the Google Cloud SQL service.
    	service, err := sqladmin.New(hc)
    	if err != nil {
    		return nil, err
    	}
    
    	// List instances for the project ID.
    	instances, err := service.Instances.List(projectId).Do()
    	if err != nil {
    		return nil, err
    	}
    	return instances.Items, nil
    }

### Java

For the [Client Library for Java](https://developers.google.com/api-client-library/java/google-api-java-client/dev-guide), you can optionally specify the service path directly.
    
    
    // Set up global SQLAdmin instance.
    client = new SQLAdmin.Builder(httpTransport, JSON_FACTORY, credential)
        .setApplicationName(APPLICATION_NAME).build();
    InstancesListResponse resp = client.instances().list("PROJECT_ID").execute();
    List<DatabaseInstance> list = resp.getItems();
    for (DatabaseInstance d : list) {
        System.out.println(d.getName());
    }

### JavaScript

For the [Client Library for JavaScript](https://developers.google.com/api-client-library/javascript/start/start-js), specify `sqladmin` to build a client.
    
    
    gapi.client.load('**sqladmin** ', 'v1beta4', function() { console.log('loaded');});
    gapi.client.sql.instances.list({'project': PROJECT_ID}).execute(showResult);
    function showResult(result) {
      // Process the result.
    };

### Python

For the [Client Library for Python](https://developers.google.com/api-client-library/python/), specify `sqladmin` to build a client.
    
    
    from googleapiclient import discovery
    
    # Construct the service object for the interacting with the Cloud SQL Admin API.
    service = discovery.build('**sqladmin** ', 'v1beta4', http=http)
    
    req = service.instances().list(project="PROJECT_ID")
    resp = req.execute()
    print(json.dumps(resp, indent=2))

The `service` object queries the discovery document and uses the correct service path, in this case, "sql/v1beta4/projects/".

If you are looking for code samples that show how applications can connect to Cloud SQL, see the [Connecting overview](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview#languages) page.

## Libraries and sample code

Language | Documentation | C++ | [Google API Client Library](https://github.com/googleapis/google-cloud-cpp)  
---|---  
Dart | [Google API Client Library](https://github.com/dart-lang/googleapis)  
Go | [Google API Client Library](https://github.com/googleapis/google-api-go-client)   
[Sample code: Cloud SQL Auth Proxy](https://github.com/GoogleCloudPlatform/cloudsql-proxy)  
Java | [Google API Client Library](https://developers.google.com/api-client-library/java/)   
[Google Client Developer's Guide](https://developers.google.com/api-client-library/java/google-api-java-client/dev-guide)   
[Sample code: Cloud SQL Java Connector](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory)  
JavaScript | [Google API Client Library](https://github.com/google/google-api-javascript-client)  
.NET | [Google API Client Library](https://www.nuget.org/packages/Google.Apis)   
[Google Client Developer's Guide](https://developers.google.com/api-client-library/dotnet/get_started)  
Node.js | [Google API Client Library](https://github.com/googleapis/google-api-nodejs-client)  
Objective-C | [Google API Client Library](https://github.com/google/google-api-objectivec-client-for-rest/tree/master/Examples)  
PHP | [Google API Client Library](https://github.com/googleapis/google-api-php-client)  
Python |  [Google API Client Library](https://github.com/googleapis/google-api-python-client)   
[Google Client Developer's Guide](https://github.com/googleapis/google-api-python-client)   
[Cloud SQL Python Connector](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector)   
[Sample code: MySQL, PostgreSQL, SQL Server](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/cloud-sql)  
Ruby | [Google API Client Library](https://github.com/googleapis/google-api-ruby-client)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
