---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/libraries/
title: Sensitive Data Protection client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:21.701815+00:00
---

# Sensitive Data Protection client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/libraries/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  Sensitive Data Protection client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to get started with the Cloud Client Libraries for the Cloud Data Loss Prevention API. Client libraries make it easier to access Google Cloud APIs from a supported language. Although you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

Read more about the Cloud Client Libraries and the older Google API Client Libraries in [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

The Cloud Data Loss Prevention API (DLP API) is part of [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). Sensitive Data Protection client libraries mentioned on this page are supported on Compute Engine, App Engine - Flexible Environment, Google Kubernetes Engine, and Cloud Run functions. Sensitive Data Protection client library for Java is supported on Java 8 on App Engine standard environment.

If you are using Java 7 on App Engine standard environment, or App Engine - Standard environment with Go, PHP, or Python, use the [REST Interface](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest) to access Sensitive Data Protection.

## Install the client library

### C#

To build and run a sample, open the solution file (Dlp.sln) with Visual Studio 2015 or later and build it. 

For more information, see the [README](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/). 

For more information, see [Setting Up a C# Development Environment](https://docs.cloud.google.com/dotnet/docs/setup).

### Go
    
    
    go get cloud.google.com/go/dlp

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
        <artifactId>google-cloud-dlp</artifactId>
      </dependency>
    </dependencies>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.90.0')
    
    implementation 'com.google.cloud:google-cloud-dlp'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-dlp" % "3.103.0"

If you're using Visual Studio Code or IntelliJ, you can add client libraries to your project using the following IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

For more information, see [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).

### Node.js
    
    
    npm install @google-cloud/dlp

For more information, see [Setting Up a Node.js Development Environment](https://docs.cloud.google.com/nodejs/docs/setup).

### PHP
    
    
    composer require google/cloud-dlp

**Note:** Sensitive Data Protection client library requires you install and enable the [gRPC Extension](https://docs.cloud.google.com/php/grpc) for PHP.

For more information, see [Using PHP on Google Cloud](https://docs.cloud.google.com/php/docs).

### Python

  1. Install [pip](https://pip.pypa.io/) and [virtualenv](https://virtualenv.pypa.io/) if you do not already have them. You may want to refer to the [Python Development Environment Setup Guide for Google Cloud](https://docs.cloud.google.com/python/docs/setup) for instructions.
  2. Clone or download the [Google Cloud Python Docs Samples](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/dlp/snippets) on GitHub.
  3. Create a virtualenv. Samples are compatible with Python 2.7.x and 3.4 and higher. 
         
         $ python -m venv dlp
         $ source dlp/bin/activate

  4. From the **dlp** directory within the cloned or unzipped Google Cloud Python Docs Samples directory, install the dependencies needed to run the samples. 
         
         $ pip install -r requirements.txt

**Important:** You must `cd` into the Google Cloud Python Docs Samples' **dlp** directory before running the previous command. 

For more information, see [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).




### Ruby
    
    
    gem install google-api-client

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

### C#
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class ClientLibraryQuickStart
    {
        public static InspectContentResponse QuickStart(
            string projectId,
            string text,
            IEnumerable<InfoType> infoTypes = null)
        {
            // Instantiate a client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the byte content item by specifying the type of data to be inspected
            // and data to be inspected.
            var byteContentItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
            {
                Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[TextUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_TextUtf8),
                Data = Google.Protobuf.ByteString.CopyFromUtf8(text)
            };
    
            // Construct content item by setting byte item.
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { ByteItem = byteContentItem };
    
            // Set minimum likelihood and limits.
            var minLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[Possible](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_Possible);
            var limits = new InspectConfig.Types.FindingLimits
            {
                // Specifying 0 means use the maximum allowed findings.
                MaxFindingsPerRequest = 0
            };
    
            // Construct a inspect config by specifying the type of info to be inspected.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes =
                {
                    infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[]
                    {
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" },
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "US_STATE" }
                    }
                },
                MinLikelihood = minLikelihood,
                Limits = limits,
                IncludeQuote = true,
            };
    
            // Construct a request config.
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                Item = contentItem,
                InspectConfig = inspectConfig
            };
    
            // Call the API.
            [InspectContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentResponse.html) response = dlp.InspectContent(request);
    
            // Inspect the response.
            var resultFindings = response.[Result](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentResponse.html#Google_Cloud_Dlp_V2_InspectContentResponse_Result).Findings;
    
            Console.WriteLine($"Findings: {resultFindings.Count}");
    
            foreach (var f in resultFindings)
            {
                Console.WriteLine("\tQuote: " + f.Quote);
                Console.WriteLine("\tInfo type: " + f.[InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html).Name);
                Console.WriteLine("\tLikelihood: " + f.[Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html));
            }
            return response;
        }
    }
    

### Go
    
    
    // The quickstart program is an example of using the Data Loss Prevention API.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    func main() {
    	ctx := context.Background()
    
    	projectID := "PROJECT_ID"
    
    	// Creates a DLP client.
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("error creating DLP client: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// The string to inspect.
    	input := "Robert Frost"
    
    	// The minimum likelihood required before returning a match.
    	minLikelihood := dlppb.[Likelihood_POSSIBLE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY)
    
    	// The maximum number of findings to report (0 = server maximum).
    	maxFindings := int32(0)
    
    	// Whether to include the matching string.
    	includeQuote := true
    
    	// The infoTypes of information to match.
    	infoTypes := []*dlppb.InfoType{
    		{
    			Name: "PERSON_NAME",
    		},
    		{
    			Name: "US_STATE",
    		},
    	}
    
    	// Construct item to inspect.
    	item := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Value{
    			Value: input,
    		},
    	}
    
    	// Construct request.
    	req := &dlppb.InspectContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		InspectConfig: &dlppb.InspectConfig{
    			InfoTypes:     infoTypes,
    			MinLikelihood: minLikelihood,
    			Limits: &dlppb.InspectConfig_FindingLimits{
    				MaxFindingsPerRequest: maxFindings,
    			},
    			IncludeQuote: includeQuote,
    		},
    		Item: item,
    	}
    
    	// Run request.
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		log.Fatal(err)
    	}
    	findings := resp.GetResult().GetFindings()
    	if len(findings) == 0 {
    		fmt.Println("No findings.")
    	}
    	fmt.Println("Findings:")
    	for _, f := range findings {
    		if includeQuote {
    			fmt.Println("\tQuote: ", f.GetQuote())
    		}
    		fmt.Println("\tInfo type: ", f.GetInfoType().GetName())
    		fmt.Println("\tLikelihood: ", f.GetLikelihood())
    	}
    }
    

### Java
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[InspectResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectResult.html);
    import com.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    public class QuickStart {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        quickstart(projectId);
      }
    
      public static void quickstart(String projectId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlpServiceClient = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Configure that content that will be inspected
          String text = "His name was Robert Frost";
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteContentItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder()
                  .setType([ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).BytesType.TEXT_UTF8)
                  .[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(text))
                  .build();
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setByteItem(byteContentItem).build();
    
          // The types of information to match:
          // See: https://cloud.google.com/dlp/docs/infotypes-reference
          List<InfoType> infoTypes =
              Stream.of("PERSON_NAME", "US_STATE")
                  .map(it -> [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(it).build())
                  .collect(Collectors.toList());
    
          // The minimum likelihood required before returning a match:
          // See: https://cloud.google.com/dlp/docs/likelihood
          [Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html) minLikelihood = [Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).POSSIBLE;
    
          // The maximum number of findings to report (0 = server maximum)
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).[FindingLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.FindingLimits.html) findingLimits =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).FindingLimits.newBuilder().[setMaxFindingsPerItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.FindingLimits.Builder.html#com_google_privacy_dlp_v2_InspectConfig_FindingLimits_Builder_setMaxFindingsPerItem_int_)(0).build();
    
          // Specify the inspection configuration
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addAllInfoTypes(infoTypes)
                  .setMinLikelihood(minLikelihood)
                  .[setLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setLimits_com_google_privacy_dlp_v2_InspectConfig_FindingLimits_)(findingLimits)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .build();
    
          // Create the request from previous configs
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) request =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setInspectConfig(inspectConfig)
                  .setItem(contentItem)
                  .build();
    
          // Send the request to the service and receive the results
          [InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html) response = dlpServiceClient.inspectContent(request);
    
          // Process the results
          System.out.println("Inspect of text complete: ");
          [InspectResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectResult.html) result = response.[getResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html#com_google_privacy_dlp_v2_InspectContentResponse_getResult__)();
          if (result.[getFindingsCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectResult.html#com_google_privacy_dlp_v2_InspectResult_getFindingsCount__)() < 0) {
            System.out.println("No findings.");
            return;
          }
          System.out.println("Findings: ");
          for ([Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html) finding : result.[getFindingsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectResult.html#com_google_privacy_dlp_v2_InspectResult_getFindingsList__)()) {
            System.out.println("\tQuote: " + finding.getQuote());
            System.out.println("\tInfo type: " + finding.getInfoType().getName());
            System.out.println("\tLikelihood: " + finding.getLikelihood());
          }
        }
      }
    }
    

### Node.js
    
    
    // Instantiates a client
    const dlp = new DLP.DlpServiceClient();
    
    // The string to inspect
    const string = 'Robert Frost';
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    async function quickStart() {
      // The minimum likelihood required before returning a match
      const minLikelihood = 'LIKELIHOOD_UNSPECIFIED';
    
      // The maximum number of findings to report (0 = server maximum)
      const maxFindings = 0;
    
      // The infoTypes of information to match
      const infoTypes = [{name: 'PERSON_NAME'}, {name: 'US_STATE'}];
    
      // Whether to include the matching string
      const includeQuote = true;
    
      // Construct item to inspect
      const item = {value: string};
    
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: {
          infoTypes: infoTypes,
          minLikelihood: minLikelihood,
          limits: {
            maxFindingsPerRequest: maxFindings,
          },
          includeQuote: includeQuote,
        },
        item: item,
      };
    
      // Run request
      const [response] = await dlp.inspectContent(request);
      const findings = response.result.findings;
      if (findings.length > 0) {
        console.log('Findings:');
        findings.forEach(finding => {
          if (includeQuote) {
            console.log(`\tQuote: ${finding.quote}`);
          }
          console.log(`\tInfo type: ${finding.infoType.name}`);
          console.log(`\tLikelihood: ${finding.likelihood}`);
        });
      } else {
        console.log('No findings.');
      }
    }
    quickStart();

### PHP
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectConfig\FindingLimits;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\Likelihood;
    
    // Instantiate a client.
    $dlp = new DlpServiceClient();
    
    // The infoTypes of information to match
    $usNameInfoType = (new InfoType())
        ->setName('PERSON_NAME');
    $phoneNumberInfoType = (new InfoType())
        ->setName('PHONE_NUMBER');
    $infoTypes = [$usNameInfoType, $phoneNumberInfoType];
    
    // Set the string to inspect
    $stringToInspect = 'Robert Frost';
    
    // Only return results above a likelihood threshold, 0 for all
    $minLikelihood = likelihood::LIKELIHOOD_UNSPECIFIED;
    
    // Limit the number of findings, 0 for no limit
    $maxFindings = 0;
    
    // Whether to include the matching string in the response
    $includeQuote = true;
    
    // Specify finding limits
    $limits = (new FindingLimits())
        ->setMaxFindingsPerRequest($maxFindings);
    
    // Create the configuration object
    $inspectConfig = (new InspectConfig())
        ->setMinLikelihood($minLikelihood)
        ->setLimits($limits)
        ->setInfoTypes($infoTypes)
        ->setIncludeQuote($includeQuote);
    
    $content = (new ContentItem())
        ->setValue($stringToInspect);
    
    $projectId = getenv('GCLOUD_PROJECT');
    $parent = $dlp->projectName($projectId);
    
    // Run request
    $inspectContentRequest = (new InspectContentRequest())
        ->setParent($parent)
        ->setInspectConfig($inspectConfig)
        ->setItem($content);
    $response = $dlp->inspectContent($inspectContentRequest);
    
    // Print the results
    $findings = $response->getResult()->getFindings();
    if (count($findings) == 0) {
        print('No findings.' . PHP_EOL);
    } else {
        print('Findings:' . PHP_EOL);
        foreach ($findings as $finding) {
            if ($includeQuote) {
                print('  Quote: ' . $finding->getQuote() . PHP_EOL);
            }
            print('  Info type: ' . $finding->getInfoType()->getName() . PHP_EOL);
            $likelihoodString = Likelihood::name($finding->getLikelihood());
            print('  Likelihood: ' . $likelihoodString . PHP_EOL);
        }
    }

### Python
    
    
    # Import the client library
    import google.cloud.dlp
    
    # Instantiate a client.
    dlp_client = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
    # The string to inspect
    content = "Robert Frost"
    
    # Construct the item to inspect.
    item = {"value": content}
    
    # The info types to search for in the content. Required.
    info_types = [{"name": "FIRST_NAME"}, {"name": "LAST_NAME"}]
    
    # The minimum likelihood to constitute a match. Optional.
    min_likelihood = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Likelihood](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html).LIKELIHOOD_UNSPECIFIED
    
    # The maximum number of findings to report (0 = server maximum). Optional.
    max_findings = 0
    
    # Whether to include the matching string in the results. Optional.
    include_quote = True
    
    # Construct the configuration dictionary. Keys which are None may
    # optionally be omitted entirely.
    inspect_config = {
        "info_types": info_types,
        "min_likelihood": min_likelihood,
        "include_quote": include_quote,
        "limits": {"max_findings_per_request": max_findings},
    }
    
    # Convert the project id into a full resource id.
    parent = f"projects/{project_id}"
    
    # Call the API.
    response = dlp_client.[inspect_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_inspect_content)(
        request={"parent": parent, "inspect_config": inspect_config, "item": item}
    )
    
    # Print out the results.
    if response.result.findings:
        for finding in response.result.findings:
            try:
                print(f"Quote: {finding.quote}")
            except AttributeError:
                pass
            print(f"Info type: {finding.info_type.name}")
            # Convert likelihood value to string respresentation.
            likelihood = finding.likelihood.name
            print(f"Likelihood: {likelihood}")
    else:
        print("No findings.")

## Additional resources

### C#

The following list contains links to more resources related to the client library for C#:

  * [API reference](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-dotnet/issues)
  * [`cloud-dlp` on Stack Overflow](https://stackoverflow.com/search?q=%5Bcloud-dlp%5D+%5Bc%23%5D)
  * [Source code](https://github.com/googleapis/google-cloud-dotnet)



### Go

The following list contains links to more resources related to the client library for Go:

  * [API reference](https://pkg.go.dev/cloud.google.com/go/dlp/apiv2)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-go/issues)
  * [`cloud-dlp` on Stack Overflow](https://stackoverflow.com/search?q=%5Bcloud-dlp%5D+%5Bgo%5D)
  * [Source code](https://github.com/googleapis/google-cloud-go)



### Java

The following list contains links to more resources related to the client library for Java:

  * [API reference](https://cloud.google.com/java/docs/reference/google-cloud-dlp/latest/overview)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/java-dlp/issues)
  * [`cloud-dlp` on Stack Overflow](https://stackoverflow.com/search?q=%5Bcloud-dlp%5D+%5Bjava%5D)
  * [Source code](https://github.com/googleapis/java-dlp)



### Node.js

The following list contains links to more resources related to the client library for Node.js:

  * [API reference](https://googleapis.dev/nodejs/dlp/latest/index.html)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/nodejs-dlp/issues)
  * [`cloud-dlp` on Stack Overflow](https://stackoverflow.com/search?q=%5Bcloud-dlp%5D+%5Bnode.js%5D)
  * [Source code](https://github.com/googleapis/nodejs-dlp)



### PHP

The following list contains links to more resources related to the client library for PHP:

  * [API reference](https://googleapis.github.io/google-cloud-php/#/docs/cloud-dlp)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-php-dlp/issues)
  * [`cloud-dlp` on Stack Overflow](https://stackoverflow.com/search?q=%5Bcloud-dlp%5D+%5Bphp%5D)
  * [Source code](https://github.com/googleapis/google-cloud-php-dlp)



### Python

The following list contains links to more resources related to the client library for Python:

  * [API reference](https://docs.cloud.google.com/python/docs/reference/dlp/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/python-dlp/issues)
  * [`cloud-dlp` on Stack Overflow](https://stackoverflow.com/search?q=%5Bcloud-dlp%5D+%5Bpython%5D)
  * [Source code](https://github.com/googleapis/python-dlp)



### Ruby

The following list contains links to more resources related to the client library for Ruby:

  * [API reference](https://developers.google.com/api-client-library/ruby/apis/)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-ruby-client/issues)
  * [`cloud-dlp` on Stack Overflow](https://stackoverflow.com/search?q=%5Bcloud-dlp%5D+%5Bruby%5D)
  * [Source code](https://github.com/google/google-api-ruby-client)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
