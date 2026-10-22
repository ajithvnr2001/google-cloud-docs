---
url: https://docs.cloud.google.com/natural-language/docs/sentiment-analysis-client-libraries/
title: Quickstart: Perform sentiment analysis by using client libraries \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:44.575241+00:00
---

# Quickstart: Perform sentiment analysis by using client libraries  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/sentiment-analysis-client-libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Guides ](https://docs.cloud.google.com/natural-language/docs/setup)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Perform sentiment analysis by using client libraries

This page shows you how to get started with the Cloud Natural Language API in your favorite programming language using the Google Cloud Client Libraries. 

## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

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

  7. Enable the Cloud Natural Language API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable language.googleapis.com

  8. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

**Note:** If the gcloud CLI prints a warning that your account doesn't have the `serviceusage.services.use` permission, then some gcloud CLI commands and client libraries might not work. Ask an administrator to grant you the Service Usage Consumer IAM role (`roles/serviceusage.serviceUsageConsumer`), then run the following command: 
         
         gcloud auth application-default set-quota-project PROJECT_ID

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the Cloud Natural Language API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable language.googleapis.com

  15. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

**Note:** If the gcloud CLI prints a warning that your account doesn't have the `serviceusage.services.use` permission, then some gcloud CLI commands and client libraries might not work. Ask an administrator to grant you the Service Usage Consumer IAM role (`roles/serviceusage.serviceUsageConsumer`), then run the following command: 
         
         gcloud auth application-default set-quota-project PROJECT_ID

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




## Install the client library

### Go
    
    
    go get cloud.google.com/go/language/apiv1

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
        <artifactId>google-cloud-language</artifactId>
      </dependency>
    </dependencies>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.90.0')
    
    implementation 'com.google.cloud:google-cloud-language'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-language" % "2.100.0"

If you're using Visual Studio Code or IntelliJ, you can add client libraries to your project using the following IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

**Note:** Cloud Java client libraries do not currently support Android.

### Node.js

Before installing the library, make sure you've [prepared your environment for Node.js development](https://docs.cloud.google.com/nodejs/docs/setup).
    
    
    npm install @google-cloud/language

### Python

Before installing the library, make sure you've [prepared your environment for Python development](https://docs.cloud.google.com/python/docs/setup).
    
    
    pip install --upgrade google-cloud-language

## Analyze some text

Now you can use the Natural Language API to analyze some text. Run the following code to perform your first text sentiment analysis:

### Go
    
    
    // Sample language-quickstart uses the Google Cloud Natural API to analyze the
    // sentiment of "Hello, world!".
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	language "cloud.google.com/go/language/apiv1"
    	"cloud.google.com/go/language/apiv1/languagepb"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Creates a client.
    	client, err := language.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_Close)()
    
    	// Sets the text to analyze.
    	text := "Hello, world!"
    
    	// Detects the sentiment of the text.
    	sentiment, err := client.AnalyzeSentiment(ctx, &languagepb.AnalyzeSentimentRequest{
    		Document: &languagepb.Document{
    			Source: &languagepb.Document_Content{
    				Content: text,
    			},
    			Type: languagepb.[Document_PLAIN_TEXT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb.html#cloud_google_com_go_language_apiv1_languagepb_Document_TYPE_UNSPECIFIED_Document_PLAIN_TEXT_Document_HTML),
    		},
    		EncodingType: languagepb.[EncodingType_UTF8](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb.html#cloud_google_com_go_language_apiv1_languagepb_EncodingType_NONE_EncodingType_UTF8_EncodingType_UTF16_EncodingType_UTF32),
    	})
    	if err != nil {
    		log.Fatalf("Failed to analyze text: %v", err)
    	}
    
    	fmt.Printf("Text: %v\n", text)
    	if sentiment.DocumentSentiment.Score >= 0 {
    		fmt.Println("Sentiment: positive")
    	} else {
    		fmt.Println("Sentiment: negative")
    	}
    }
    

### Java
    
    
    // Imports the Google Cloud client library
    import com.google.cloud.language.v1.[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Document.html);
    import com.google.cloud.language.v1.[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Document.html).Type;
    import com.google.cloud.language.v1.[LanguageServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.LanguageServiceClient.html);
    import com.google.cloud.language.v1.[Sentiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Sentiment.html);
    
    public class QuickstartSample {
      public static void main(String... args) throws Exception {
        // Instantiates a client
        try ([LanguageServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.LanguageServiceClient.html) language = [LanguageServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.LanguageServiceClient.html).create()) {
    
          // The text to analyze
          String text = "Hello, world!";
          [Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Document.html) doc = [Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Document.html).newBuilder().setContent(text).setType(Type.PLAIN_TEXT).build();
    
          // Detects the sentiment of the text
          [Sentiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Sentiment.html) sentiment = language.analyzeSentiment(doc).getDocumentSentiment();
    
          System.out.printf("Text: %s%n", text);
          System.out.printf("Sentiment: %s, %s%n", sentiment.[getScore](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Sentiment.html#com_google_cloud_language_v1_Sentiment_getScore__)(), sentiment.[getMagnitude](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1.Sentiment.html#com_google_cloud_language_v1_Sentiment_getMagnitude__)());
        }
      }
    }

### Node.js

Before running the example, make sure you've [prepared your environment for Node.js development](https://docs.cloud.google.com/nodejs/docs/setup).
    
    
    async function quickstart() {
      // Imports the Google Cloud client library
      const language = require('[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)');
    
      // Instantiates a client
      const client = new language.[LanguageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)();
    
      // The text to analyze
      const text = 'Hello, world!';
    
      const document = {
        content: text,
        type: 'PLAIN_TEXT',
      };
    
      // Detects the sentiment of the text
      const [result] = await client.analyzeSentiment({document: document});
      const sentiment = result.documentSentiment;
    
      console.log(`Text: ${text}`);
      console.log(`Sentiment score: ${sentiment.score}`);
      console.log(`Sentiment magnitude: ${sentiment.magnitude}`);
    }

### Python

Before running the example, make sure you've [prepared your environment for Python development](https://docs.cloud.google.com/python/docs/setup).
    
    
    # Imports the Google Cloud client library.
    from google.cloud import language_v1
    
    # Instantiates a client.
    client = language_v1.LanguageServiceClient()
    
    # The text to analyze.
    text = "Hello, world!"
    document = language_v1.types.Document(
        content=text, type_=language_v1.types.Document.Type.PLAIN_TEXT
    )
    
    # Detects the sentiment of the text.
    sentiment = client.[analyze_sentiment](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.services.language_service.LanguageServiceClient.html#google_cloud_language_v1_services_language_service_LanguageServiceClient_analyze_sentiment)(
        request={"document": document}
    ).document_sentiment
    
    print(f"Text: {text}")
    print(f"Sentiment: {sentiment.score}, {sentiment.magnitude}")

Congratulations! You've sent your first request to the Natural Language API.

## How did it go?

It worked!  **Great!** What did you like about the quickstart? What could we have done better?  Let us know!.  I got stuck.  **We're sorry to hear that.** Let us know what went wrong. We'll want to fix it. 

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

  * Use the [Google Cloud console](https://console.cloud.google.com/) to delete your project if you do not need it.



## What's next

  * Find out more about our [Cloud Natural Language API Client Libraries](https://docs.cloud.google.com/natural-language/docs/reference/libraries).
  * Consult the [Natural Language Basics](https://docs.cloud.google.com/natural-language/docs/basics) for conceptual information on forming Natural Language API requests and handling responses.
  * Work through the [Sentiment Analysis Tutorial](https://docs.cloud.google.com/natural-language/docs/sentiment-tutorial) and browse the [Sample Applications](https://docs.cloud.google.com/natural-language/docs/sample-apps). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
