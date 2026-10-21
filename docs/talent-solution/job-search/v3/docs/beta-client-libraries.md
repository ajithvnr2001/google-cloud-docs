---
url: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/beta-client-libraries/
title: CTS client libraries \u00a0|\u00a0 Cloud Talent Solution - Job Search v3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:25.288393+00:00
---

# CTS client libraries  |  Cloud Talent Solution - Job Search v3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v3/docs/beta-client-libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v3 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v3/docs)



Send feedback 

#  CTS client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to get started with the Cloud Client Libraries for the Cloud Talent Solution API. Client libraries make it easier to access Google Cloud Platform APIs from a supported language. Although you can use Google Cloud Platform APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

Read more about the Cloud Client Libraries and the older Google API Client Libraries in [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

**Beta**

This library is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA libraries are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Client libraries for more languages are coming soon.

## Install the client library

### C#

If you are using Visual Studio 2017 or higher, open nuget package manager window and type the following: 
    
    
    Install-Package Google.Apis

If you are using .NET Core command-line interface tools to install your dependencies, run the following command:
    
    
    dotnet add package Google.Apis

For more information, see [Setting Up a C# Development Environment](https://docs.cloud.google.com/dotnet/docs/setup).

### Go
    
    
    go get google.golang.org/api/jobs/v3p1beta1

For more information, see [Setting Up a Go Development Environment](https://docs.cloud.google.com/go/docs/setup).

### Java

If you are using Maven, add this to your pom.xml file: 
    
    
    <dependency>
        <groupId>com.google.apis</groupId>
        <artifactId>google-api-services-jobs</artifactId>
        <version>LATEST</version>
    </dependency>

**Note:** Google Cloud Java client libraries do not currently support Android.

For more information, see [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).

### Node.js
    
    
    npm install googleapis

For more information, see [Setting Up a Node.js Development Environment](https://docs.cloud.google.com/nodejs/docs/setup).

### PHP
    
    
    composer require google/apiclient

For more information, see [Using PHP on Google Cloud](https://docs.cloud.google.com/php/docs).

### Python
    
    
    pip install --upgrade google-api-python-client

For more information, see [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).

### Ruby
    
    
    gem install google-api-client

For more information, see [Setting Up a Ruby Development Environment](https://docs.cloud.google.com/ruby/docs/setup).

## Set up authentication

To authenticate calls to Google Cloud Platform APIs, client libraries support [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials); the libraries look for credentials in a set of defined locations and use those credentials to authenticate requests to the API. With ADC, you can make credentials available to your application in a variety of environments, such as local development or production, without needing to modify your application code. 

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

### Go
    
    
    // Command quickstart is an example of using the Google Cloud Talent Solution API.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"os"
    
    	"golang.org/x/oauth2/google"
    	talent "google.golang.org/api/jobs/v3"
    )
    
    func main() {
    	projectID := os.Getenv("GOOGLE_CLOUD_PROJECT")
    	parent := fmt.Sprintf("projects/%s", projectID)
    
    	// Authorize the client using Application Default Credentials.
    	// See https://g.co/dv/identity/protocols/application-default-credentials
    	ctx := context.Background()
    	client, err := google.DefaultClient(ctx, talent.CloudPlatformScope)
    	if err != nil {
    		log.Fatal(err)
    	}
    
    	// Create the jobs service client.
    	ctsService, err := talent.New(client)
    	if err != nil {
    		log.Fatal(err)
    	}
    
    	// Make the RPC call.
    	response, err := ctsService.Projects.Companies.List(parent).Do()
    	if err != nil {
    		log.Fatalf("Failed to list Companies: %v", err)
    	}
    
    	// Print the request id.
    	fmt.Printf("Request ID: %q\n", response.Metadata.RequestId)
    
    	// Print the returned companies.
    	for _, company := range response.Companies {
    		fmt.Printf("Company: %q\n", company.Name)
    	}
    }
    

### Java
    
    
    private static final JsonFactory JSON_FACTORY = new GsonFactory();
    private static final NetHttpTransport NET_HTTP_TRANSPORT = new NetHttpTransport();
    private static final String DEFAULT_PROJECT_ID =
        "projects/" + System.getenv("GOOGLE_CLOUD_PROJECT");
    
    private static CloudTalentSolution talentSolutionClient =
        createTalentSolutionClient(generateCredential());
    
    private static CloudTalentSolution createTalentSolutionClient(GoogleCredentials credential) {
      String url = "https://jobs.googleapis.com";
    
      HttpRequestInitializer requestInitializer =
          request -> {
            new HttpCredentialsAdapter(credential).initialize(request);
            request.setConnectTimeout(60000); // 1 minute connect timeout
            request.setReadTimeout(60000); // 1 minute read timeout
          };
    
      return new CloudTalentSolution.Builder(NET_HTTP_TRANSPORT, JSON_FACTORY, requestInitializer)
          .setApplicationName("JobServiceClientSamples")
          .setRootUrl(url)
          .build();
    }
    
    private static GoogleCredentials generateCredential() {
      try {
        // Credentials could be downloaded after creating service account
        // set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable, for example:
        // export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/key.json
        return GoogleCredentials.getApplicationDefault()
            .createScoped(Collections.singleton(CloudTalentSolutionScopes.JOBS));
      } catch (Exception e) {
        System.out.println("Error in generating credential");
        throw new RuntimeException(e);
      }
    }
    
    public static CloudTalentSolution getTalentSolutionClient() {
      return talentSolutionClient;
    }
    
    public static void main(String... args) throws Exception {
      try {
        ListCompaniesResponse listCompaniesResponse =
            talentSolutionClient.projects().companies().list(DEFAULT_PROJECT_ID).execute();
        System.out.println("Request Id is " + listCompaniesResponse.getMetadata().getRequestId());
        if (listCompaniesResponse.getCompanies() != null) {
          for (Company company : listCompaniesResponse.getCompanies()) {
            System.out.println(company.getName());
          }
        }
      } catch (IOException e) {
        System.out.println("Got exception while listing companies");
        throw e;
      }
    }
    

### Node.js

### Python

## Additional resources

### C#

The following list contains links to more resources related to the client library for C#:

  * [API reference](https://developers.google.com/api-client-library/dotnet)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-dotnet-client/issues)
  * [`google-api-services-jobs` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-api-services-jobs%5D+%5Bc%23%5D)
  * [Source code](https://github.com/google/google-api-dotnet-client)



### Go

The following list contains links to more resources related to the client library for Go:

  * [API reference](https://godoc.org/google.golang.org/api)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-go-client/issues)
  * [`google-api-services-jobs` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-api-services-jobs%5D+%5Bgo%5D)
  * [Source code](https://github.com/google/google-api-go-client)



### Java

The following list contains links to more resources related to the client library for Java:

  * [API reference](https://developers.google.com/api-client-library/java/apis/)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-java-client/issues)
  * [`google-api-services-jobs` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-api-services-jobs%5D+%5Bjava%5D)
  * [Source code](https://github.com/google/google-api-java-client)



### Node.js

The following list contains links to more resources related to the client library for Node.js:

  * [API reference](https://github.com/google/google-api-nodejs-client/tree/master/src/apis/jobs)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-nodejs-client/tree/master/src/apis/jobs/issues)
  * [`google-api-services-jobs` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-api-services-jobs%5D+%5Bnode.js%5D)
  * [Source code](https://github.com/google/google-api-nodejs-client/tree/master/src/apis/jobs)



### PHP

The following list contains links to more resources related to the client library for PHP:

  * [API reference](https://developers.google.com/api-client-library/php/)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-php-client/issues)
  * [`google-api-services-jobs` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-api-services-jobs%5D+%5Bphp%5D)
  * [Source code](https://github.com/google/google-api-php-client)



### Python

The following list contains links to more resources related to the client library for Python:

  * [API reference](https://developers.google.com/api-client-library/python/apis/)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-python-client/issues)
  * [`google-api-services-jobs` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-api-services-jobs%5D+%5Bpython%5D)
  * [Source code](https://github.com/google/google-api-python-client)



### Ruby

The following list contains links to more resources related to the client library for Ruby:

  * [API reference](https://developers.google.com/api-client-library/ruby/apis/)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-ruby-client/issues)
  * [`google-api-services-jobs` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-api-services-jobs%5D+%5Bruby%5D)
  * [Source code](https://github.com/google/google-api-ruby-client)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
