---
url: https://docs.cloud.google.com/docs/authentication/api-keys-use/
title: Use API keys to access APIs \u00a0|\u00a0 Authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:41.515054+00:00
---

# Use API keys to access APIs  |  Authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/authentication/api-keys-use/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Authentication ](https://docs.cloud.google.com/docs/authentication)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Use API keys to access APIs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use API keys to access Google Cloud APIs and services that accept API keys. 

Not all Google Cloud APIs accept API keys to authorize usage. Review the documentation for the service or API that you want to use to determine whether it accepts API keys.

For information about creating and managing API keys, including restricting API keys, see [Manage API keys](https://docs.cloud.google.com/docs/authentication/api-keys).

For information about using API keys with Google Maps Platform, see the [Google Maps Platform documentation](https://developers.google.com/maps/api-key-best-practices). For more information about the API Keys API, see the [API Keys API documentation](https://docs.cloud.google.com/api-keys/docs/overview). 

## Before you begin

Select the tab for how you plan to use the samples on this page:

### C#

To use the .NET samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### C++

To use the C++ samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Go

To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Node.js

To use the Node.js samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Python

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

## Using an API key with REST

To include an API key with a REST API call, use the `x-goog-api-key` HTTP header, as shown in the following example:
    
    
    curl -X POST \
        -H "X-goog-api-key: API_KEY" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d @request.json \
        "https://translation.googleapis.com/language/translate/v2"
    

If you can't use the HTTP header, you can use the `key` query parameter. However, this method includes your API key in the URL, exposing your key to theft through URL scans.

The following example shows how to use the `key` query parameter with a Cloud Natural Language API request for [`documents.analyzeEntities`](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeEntities). Replace `API_KEY` with the key string of your API key.
    
    
    POST https://language.googleapis.com/v1/documents:analyzeEntities?key=API_KEY

## Using an API key with client libraries

This example uses the Cloud Natural Language API, which accepts API keys, to demonstrate how you would provide an API key to the library.

###  C# 

To run this sample, you must install the [Natural Language client library](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest).
    
    
    using Google.Cloud.Language.V1;
    using System;
    
    public class UseApiKeySample
    {
        public void AnalyzeSentiment(string apiKey)
        {
            LanguageServiceClient client = new LanguageServiceClientBuilder
            {
                ApiKey = apiKey
            }.Build();
    
            string text = "Hello, world!";
    
            AnalyzeSentimentResponse response = client.AnalyzeSentiment(Document.FromPlainText(text));
            Console.WriteLine($"Text: {text}");
            Sentiment sentiment = response.DocumentSentiment;
            Console.WriteLine($"Sentiment: {sentiment.Score}, {sentiment.Magnitude}");
            Console.WriteLine("Successfully authenticated using the API key");
        }
    }
    

###  C++ 

To run this sample, you must install the [Natural Language client library](https://docs.cloud.google.com/cpp/docs/reference/language/latest).
    
    
    #include "google/cloud/language/v1/language_client.h"
    #include "google/cloud/credentials.h"
    #include "google/cloud/options.h"
    
    void AuthenticateWithApiKey(std::vector<std::string> const& argv) {
      if (argv.size() != 2) {
        throw google::cloud::testing_util::Usage{
            "authenticate-with-api-key <project-id> <api-key>"};
      }
      namespace gc = ::google::cloud;
      auto options = gc::Options{}.set<gc::UnifiedCredentialsOption>(
          gc::MakeApiKeyCredentials(argv[1]));
      auto client = gc::language_v1::LanguageServiceClient(
          gc::language_v1::MakeLanguageServiceConnection(options));
    
      auto constexpr kText = "Hello, world!";
    
      google::cloud::language::v1::Document d;
      d.set_content(kText);
      d.set_type(google::cloud::language::v1::Document::PLAIN_TEXT);
    
      auto response = client.AnalyzeSentiment(d, {});
      if (!response) throw std::move(response.status());
      auto const& sentiment = response->document_sentiment();
      std::cout << "Text: " << kText << "\n";
      std::cout << "Sentiment: " << sentiment.score() << ", "
                << sentiment.magnitude() << "\n";
      std::cout << "Successfully authenticated using the API key\n";
    }

###  Go 

To run this sample, you must install the [Natural Language client library](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	language "cloud.google.com/go/language/apiv1"
    	"cloud.google.com/go/language/apiv1/languagepb"
    	"google.golang.org/api/option"
    )
    
    // authenticateWithAPIKey authenticates with an API key for Google Language
    // service.
    func authenticateWithAPIKey(w io.Writer, apiKey string) error {
    	// apiKey := "api-key-string"
    
    	ctx := context.Background()
    
    	// Initialize the Language Service client and set the API key.
    	client, err := language.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_NewClient)(ctx, option.WithAPIKey(apiKey))
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1.html#cloud_google_com_go_language_apiv1_Client_Close)()
    
    	text := "Hello, world!"
    	// Make a request to analyze the sentiment of the text.
    	res, err := client.AnalyzeSentiment(ctx, &languagepb.AnalyzeSentimentRequest{
    		Document: &languagepb.Document{
    			Source: &languagepb.Document_Content{
    				Content: text,
    			},
    			Type: languagepb.[Document_PLAIN_TEXT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/language/latest/apiv1/languagepb.html#cloud_google_com_go_language_apiv1_languagepb_Document_TYPE_UNSPECIFIED_Document_PLAIN_TEXT_Document_HTML),
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("AnalyzeSentiment: %w", err)
    	}
    
    	fmt.Fprintf(w, "Text: %s\n", text)
    	fmt.Fprintf(w, "Sentiment score: %v\n", res.DocumentSentiment.Score)
    	fmt.Fprintln(w, "Successfully authenticated using the API key.")
    
    	return nil
    }
    

###  Node.js 

To run this sample, you must install the [Natural Language client library](https://docs.cloud.google.com/nodejs/docs/reference/language/latest).
    
    
    const {
      v1: {LanguageServiceClient},
    } = require('[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)');
    
    /**
     * Authenticates with an API key for Google Language service.
     *
     * @param {string} apiKey An API Key to use
     */
    async function authenticateWithAPIKey(apiKey) {
      const language = new [LanguageServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)({apiKey});
    
      // Alternatively:
      // const {GoogleAuth} = require('google-auth-library');
      // const auth = new GoogleAuth({apiKey});
      // const language = new LanguageServiceClient({auth});
    
      const text = 'Hello, world!';
    
      const [response] = await language.analyzeSentiment({
        document: {
          content: text,
          type: 'PLAIN_TEXT',
        },
      });
    
      console.log(`Text: ${text}`);
      console.log(
        `Sentiment: ${response.documentSentiment.score}, ${response.documentSentiment.magnitude}`,
      );
      console.log('Successfully authenticated using the API key');
    }
    
    authenticateWithAPIKey();

###  Python 

To run this sample, you must install the [Natural Language client library](https://docs.cloud.google.com/python/docs/reference/language/latest).
    
    
    from google.cloud import language_v1
    
    
    def authenticate_with_api_key(api_key_string: str) -> None:
        """
        Authenticates with an API key for Google Language service.
    
        TODO(Developer): Replace this variable before running the sample.
    
        Args:
            api_key_string: The API key to authenticate to the service.
        """
    
        # Initialize the Language Service client and set the API key
        client = language_v1.LanguageServiceClient(
            client_options={"api_key": api_key_string}
        )
    
        text = "Hello, world!"
        document = language_v1.Document(
            content=text, type_=language_v1.Document.Type.PLAIN_TEXT
        )
    
        # Make a request to analyze the sentiment of the text.
        sentiment = client.[analyze_sentiment](https://docs.cloud.google.com/python/docs/reference/language/latest/google.cloud.language_v1.services.language_service.LanguageServiceClient.html#google_cloud_language_v1_services_language_service_LanguageServiceClient_analyze_sentiment)(
            request={"document": document}
        ).document_sentiment
    
        print(f"Text: {text}")
        print(f"Sentiment: {sentiment.score}, {sentiment.magnitude}")
        print("Successfully authenticated using the API key")
    
    

###  Ruby 

To run this sample, you must install the [Natural Language client library](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language/latest).
    
    
    require "googleauth"
    require "google/cloud/language/v1"
    
    def authenticate_with_api_key api_key_string
      # Authenticates with an API key for Google Language service.
      #
      # TODO(Developer): Uncomment the following line and set the value before running this sample.
      #
      # api_key_string = "mykey12345"
      #
      # Note: You can also set the API key via environment variable:
      #   export GOOGLE_API_KEY=your-api-key
      # and use Google::Auth::APIKeyCredentials.from_env method to load it.
      # Example:
      #   credentials = Google::Auth::APIKeyCredentials.from_env
      #   if credentials.nil?
      #     puts "No API key found in environment"
      #     exit
      #   end
    
      # Initialize API key credentials using the class factory method
      credentials = Google::Auth::[APIKeyCredentials](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-APIKeyCredentials.html).[make_creds](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-APIKeyCredentials.html) api_key: api_key_string
    
      # Initialize the Language Service client with the API key credentials
      client = Google::Cloud::Language::V1::LanguageService::Client.new do |config|
        config.credentials = credentials
      end
    
      # Create a document to analyze
      text = "Hello, world!"
      document = {
        content: text,
        type: :PLAIN_TEXT
      }
    
      # Make a request to analyze the sentiment of the text
      sentiment = client.analyze_sentiment(document: document).document_sentiment
    
      puts "Text: #{text}"
      puts "Sentiment: #{sentiment.score}, #{sentiment.magnitude}"
      puts "Successfully authenticated using the API key"
    end

When you use API keys in your applications, ensure that they are kept secure during both storage and transmission. Publicly exposing your API keys can lead to unexpected charges on your account. For more information, see [Best practices for managing API keys](https://docs.cloud.google.com/docs/authentication/api-keys-best-practices).

## What's next

  * See an overview of [authentication methods](https://docs.cloud.google.com/docs/authentication).
  * Learn more about the [API Keys API](https://docs.cloud.google.com/api-keys/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
