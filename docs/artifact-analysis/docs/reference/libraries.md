---
url: https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries/
title: Container Analysis client libraries \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:51.929595+00:00
---

# Container Analysis client libraries  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Reference ](https://docs.cloud.google.com/artifact-analysis/docs/apis)



Send feedback 

#  Container Analysis client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to get started with the Cloud Client Libraries for the Container Analysis API. Client libraries make it easier to access Google Cloud APIs from a supported language. Although you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

Read more about the Cloud Client Libraries and the older Google API Client Libraries in [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

## Install the client library

### C++

See [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup) for details about this client library's requirements and install dependencies.

### Go
    
    
    go get cloud.google.com/go/containeranalysis/apiv1

For more information, see [Setting Up a Go Development Environment](https://docs.cloud.google.com/go/docs/setup).

### Java

  
  


If you are using [Maven](https://maven.apache.org/) with a BOM, add the following to your `pom.xml` file:
    
    
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
        <artifactId>google-cloud-containeranalysis</artifactId>
      </dependency>
    </dependencies>

If you are using [Maven](https://maven.apache.org/) without a BOM, add this to your dependencies:
    
    
    <dependency>
      <groupId>com.google.cloud</groupId>
      <artifactId>google-cloud-containeranalysis</artifactId>
      <version>2.100.0</version>
    </dependency>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.90.0')
    
    implementation 'com.google.cloud:google-cloud-containeranalysis'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-containeranalysis" % "2.100.0"

If you're using Visual Studio Code or IntelliJ, you can add client libraries to your project using the following IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

For more information, see [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).

### Node.js

  

    
    
    npm install @google-cloud/containeranalysis

For more information, see [Setting Up a Node.js Development Environment](https://docs.cloud.google.com/nodejs/docs/setup).

### Python

  
It is recommended to install this library in a [virtualenv](https://virtualenv.pypa.io/en/latest/ "Virtualenv Documentation") using `pip`. Virtualenv allows you to install the Python libraries in an isolated environment, preventing conflicts with the system dependencies. 

  * **Mac and Linux**
        
        pip install virtualenv
        virtualenv <your-env>
        source <your-env>/bin/activate
        <your-env>/bin/pip install google-cloud-containeranalysis
        

  * **Windows**
        
        pip install virtualenv
        virtualenv <your-env>
        <your-env>\Scripts\activate
        <your-env>\Scripts\pip.exe install google-cloud-containeranalysis
        

For more information, see [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).




### Ruby
    
    
    gem install google-cloud-container_analysis

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
    
    
    #include "google/cloud/containeranalysis/v1/grafeas_client.h"
    #include "google/cloud/project.h"
    #include <iostream>
    
    int main(int argc, char* argv[]) try {
      if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " project-id\n";
        return 1;
      }
    
      namespace containeranalysis = ::google::cloud::containeranalysis_v1;
      auto client = containeranalysis::GrafeasClient(
          containeranalysis::MakeGrafeasConnection());
    
      auto const project = google::cloud::Project(argv[1]);
      for (auto n : client.ListNotes(project.FullName(), /*filter=*/"")) {
        if (!n) throw std::move(n).status();
        std::cout << n->DebugString() << "\n";
      }
    
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }

### Go
    
    
    import (
    	"context"
    	"fmt"
    
    	containeranalysis "cloud.google.com/go/containeranalysis/apiv1"
    	grafeaspb "google.golang.org/genproto/googleapis/grafeas/v1"
    )
    
    // getOccurrence retrieves and prints a specified Occurrence from the server.
    func getOccurrence(occurrenceID, projectID string) (*grafeaspb.[Occurrence](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1beta1/grafeas/grafeaspb.html#cloud_google_com_go_containeranalysis_apiv1beta1_grafeas_grafeaspb_Occurrence), error) {
    	// occurrenceID := path.Base(occurrence.Name)
    	ctx := context.Background()
    	client, err := containeranalysis.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1.html#cloud_google_com_go_containeranalysis_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1.html#cloud_google_com_go_containeranalysis_apiv1_Client_Close)()
    
    	req := &grafeaspb.[GetOccurrenceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1beta1/grafeas/grafeaspb.html#cloud_google_com_go_containeranalysis_apiv1beta1_grafeas_grafeaspb_GetOccurrenceRequest){
    		Name: fmt.Sprintf("projects/%s/occurrences/%s", projectID, occurrenceID),
    	}
    	occ, err := client.[GetGrafeasClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1.html#cloud_google_com_go_containeranalysis_apiv1_Client_GetGrafeasClient)().GetOccurrence(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("client.GetOccurrence: %w", err)
    	}
    	return occ, nil
    }
    

### Java
    
    
    import com.google.cloud.devtools.containeranalysis.v1.[ContainerAnalysisClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/com.google.cloud.devtools.containeranalysis.v1.ContainerAnalysisClient.html);
    import io.grafeas.v1.[GrafeasClient](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.GrafeasClient.html);
    import io.grafeas.v1.[Occurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Occurrence.html);
    import io.grafeas.v1.[OccurrenceName](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.OccurrenceName.html);
    import java.io.IOException;
    import java.lang.InterruptedException;
    
    public class GetOccurrence {
      // Retrieves and prints a specified Occurrence from the server
      public static [Occurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Occurrence.html) getOccurrence(String occurrenceId, String projectId) 
          throws IOException, InterruptedException {
        // String occurrenceId = "123-456-789";
        // String projectId = "my-project-id";
        final [OccurrenceName](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.OccurrenceName.html) occurrenceName = [OccurrenceName](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.OccurrenceName.html).of(projectId, occurrenceId);
    
        // Initialize client that will be used to send requests. After completing all of your requests, 
        // call the "close" method on the client to safely clean up any remaining background resources.
        [GrafeasClient](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.GrafeasClient.html) client = [ContainerAnalysisClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/com.google.cloud.devtools.containeranalysis.v1.ContainerAnalysisClient.html).create().[getGrafeasClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/com.google.cloud.devtools.containeranalysis.v1.ContainerAnalysisClient.html#com_google_cloud_devtools_containeranalysis_v1_ContainerAnalysisClient_getGrafeasClient__)();
        [Occurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Occurrence.html) occ = client.[getOccurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.GrafeasClient.html#io_grafeas_v1_GrafeasClient_getOccurrence__org_jspecify_annotations_Nullable_io_grafeas_v1_OccurrenceName_)(occurrenceName);
        System.out.println(occ);
        return occ;
      }
    }

### Node.js
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample
     */
    // const projectId = 'your-project-id', // Your GCP Project ID
    // const noteId = 'my-note-id' // Id of the note
    
    // Import the library and create a client
    const {ContainerAnalysisClient} = require('[@google-cloud/containeranalysis](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)');
    const client = new [ContainerAnalysisClient](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)();
    // Fetch an instance of a Grafeas client:
    // see: https://googleapis.dev/nodejs/grafeas/latest
    const grafeasClient = client.[getGrafeasClient](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/v1.containeranalysisclient.html)();
    
    // Construct request
    // Associate the Note with a metadata type
    // https://cloud.google.com/container-registry/docs/container-analysis#supported_metadata_types
    // Here, we use the type "vulnerabiltity"
    const formattedParent = grafeasClient.[projectPath](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/v1.containeranalysisclient.html)(projectId);
    
    // Creates and returns a new Note
    const [note] = await grafeasClient.createNote({
      parent: formattedParent,
      noteId: noteId,
      note: {
        vulnerability: {
          details: [
            {
              affectedCpeUri: 'foo.uri',
              affectedPackage: 'foo',
              minAffectedVersion: {
                kind: 'MINIMUM',
              },
              fixedVersion: {
                kind: 'MAXIMUM',
              },
            },
          ],
        },
      },
    });
    
    console.log(`Note ${note.name} created.`);

### Python
    
    
    from typing import List
    
    from grafeas.grafeas_v1 import types
    
    
    def find_high_severity_vulnerabilities_for_image(
        resource_url: str, project_id: str
    ) -> List[types.grafeas.Occurrence]:
        """Retrieves a list of only high vulnerability occurrences associated
        with a resource."""
        # resource_url = 'https://gcr.io/my-project/my-image@sha256:123'
        # project_id = 'my-gcp-project'
    
        from grafeas.grafeas_v1 import Severity
        from google.cloud.devtools import containeranalysis_v1
    
        client = containeranalysis_v1.ContainerAnalysisClient()
        grafeas_client = client.get_grafeas_client()
        project_name = f"projects/{project_id}"
    
        filter_str = 'kind="VULNERABILITY" AND resourceUrl="{}"'.format(resource_url)
        vulnerabilities = grafeas_client.list_occurrences(
            parent=project_name, filter=filter_str
        )
        filtered_list = []
        for v in vulnerabilities:
            if (
                v.vulnerability.effective_severity == Severity.HIGH
                or v.vulnerability.effective_severity == Severity.CRITICAL
            ):
                filtered_list.append(v)
        return filtered_list
    
    

### Ruby
    
    
    require "google/cloud/container_analysis/v1"
    
    ##
    # Snippet for the get_vulnerability_occurrences_summary call in the ContainerAnalysis service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::ContainerAnalysis::V1::ContainerAnalysis::Client#get_vulnerability_occurrences_summary.
    #
    def get_vulnerability_occurrences_summary
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::ContainerAnalysis::V1::ContainerAnalysis::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::ContainerAnalysis::V1::GetVulnerabilityOccurrencesSummaryRequest.new
    
      # Call the get_vulnerability_occurrences_summary method.
      result = client.get_vulnerability_occurrences_summary request
    
      # The returned object is of type Google::Cloud::ContainerAnalysis::V1::VulnerabilityOccurrencesSummary.
      p result
    end

## Additional resources

### C++

The following list contains links to more resources related to the client library for C++:

  * [API reference](https://docs.cloud.google.com/cpp/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues)
  * [`google-containeranalysis` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-containeranalysis%5D%5Bc%2B%2B%5D)
  * [Source code](https://github.com/googleapis/google-cloud-cpp)



### Go

The following list contains links to more resources related to the client library for Go:

  * [API reference](https://docs.cloud.google.com/go/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-go/issues)
  * [`google-containeranalysis` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-containeranalysis%5D+%5Bgo%5D)
  * [Source code](https://github.com/googleapis/google-cloud-go)



### Java

The following list contains links to more resources related to the client library for Java:

  * [API reference](https://docs.cloud.google.com/java/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-java/issues)
  * [`google-containeranalysis` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-containeranalysis%5D+%5Bjava%5D)
  * [Source code](https://github.com/googleapis/google-cloud-java)



### Node.js

The following list contains links to more resources related to the client library for Node.js:

  * [API reference](https://docs.cloud.google.com/nodejs/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-node/issues)
  * [`google-containeranalysis` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-containeranalysis%5D+%5Bnode.js%5D)
  * [Source code](https://github.com/googleapis/google-cloud-node)



### Python

The following list contains links to more resources related to the client library for Python:

  * [API reference](https://docs.cloud.google.com/python/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-python/issues)
  * [`google-containeranalysis` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-containeranalysis%5D+%5Bpython%5D)
  * [Source code](https://github.com/googleapis/google-cloud-python)



### Ruby

The following list contains links to more resources related to the client library for Ruby:

  * [API reference](https://docs.cloud.google.com/ruby/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-ruby/issues)
  * [`google-containeranalysis` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-containeranalysis%5D+%5Bruby%5D)
  * [Source code](https://github.com/googleapis/google-cloud-ruby)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
