---
url: https://docs.cloud.google.com/docs/authentication/client-libraries/
title: Authenticate with client libraries \u00a0|\u00a0 Authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:48.414416+00:00
---

# Authenticate with client libraries  |  Authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/authentication/client-libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Authentication ](https://docs.cloud.google.com/docs/authentication)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Authenticate with client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can use client libraries to access Google APIs. 

Client libraries make it easier to access [Google Cloud APIs](https://docs.cloud.google.com/apis/docs/overview) using a supported language. You can use Google Cloud APIs directly by making raw requests to the server, but client libraries provide simplifications that significantly reduce the amount of code you need to write. This is especially true for authentication, because the client libraries support [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

If you accept credential configurations (JSON, files, or streams) from an external source (for example, a customer), review the security requirements when using credential configurations from an external source.

## Use Application Default Credentials with client libraries

To use Application Default Credentials to authenticate your application, you must first [set up ADC](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) for the environment where your application is running. When you use the client library to create a client, the client library automatically checks for and uses the credentials you have provided to ADC to authenticate to the APIs your code uses. Your application does not need to explicitly authenticate or manage tokens; these requirements are managed automatically by the authentication libraries.

For a local development environment, you can set up ADC [with your user credentials](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) or [with service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation#adc) by using the gcloud CLI. For production environments, you set up ADC by [attaching a service account](https://docs.cloud.google.com/docs/authentication/set-up-adc-attached-service-account).

### Example client creation

The following code samples create a client for the Cloud Storage service. Your code is likely to need different clients; these samples are meant only to show how you can create a client and use it without any code to explicitly authenticate.

Before you can run the following samples, you must complete the following steps:

  * [ Set up ADC for your environment](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc)
  * [ Install the Cloud Storage client library](https://docs.cloud.google.com/storage/docs/reference/libraries)



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/storage"
    	"google.golang.org/api/iterator"
    )
    
    // authenticateImplicitWithAdc uses Application Default Credentials
    // to automatically find credentials and authenticate.
    func authenticateImplicitWithAdc(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), projectId string) error {
    	// projectId := "your_project_id"
    
    	ctx := context.Background()
    
    	// NOTE: Replace the client created below with the client required for your application.
    	// Note that the credentials are not specified when constructing the client.
    	// The client library finds your credentials using ADC.
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.Close()
    
    	it := client.[Buckets](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Buckets)(ctx, projectId)
    	for {
    		bucketAttrs, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "Bucket: %v\n", bucketAttrs.Name)
    	}
    
    	fmt.Fprintf(w, "Listed all storage buckets.\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.api.gax.paging.[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html);
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.io.IOException;
    
    public class AuthenticateImplicitWithAdc {
    
      public static void main(String[] args) throws IOException {
        // TODO(Developer):
        //  1. Before running this sample,
        //  set up Application Default Credentials as described in
        //  https://cloud.google.com/docs/authentication/external/set-up-adc
        //  2. Replace the project variable below.
        //  3. Make sure you have the necessary permission to list storage buckets
        //  "storage.buckets.list"
        String projectId = "your-google-cloud-project-id";
        authenticateImplicitWithAdc(projectId);
      }
    
      // When interacting with Google Cloud Client libraries, the library can auto-detect the
      // credentials to use.
      public static void authenticateImplicitWithAdc(String project) throws IOException {
    
        // *NOTE*: Replace the client created below with the client required for your application.
        // Note that the credentials are not specified when constructing the client.
        // Hence, the client library will look for credentials using ADC.
        //
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(project).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        System.out.println("Buckets:");
        Page<Bucket> buckets = storage.[list](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_list_com_google_cloud_storage_Storage_BucketListOption____)();
        for ([Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket : buckets.iterateAll()) {
          System.out.println(bucket.toString());
        }
        System.out.println("Listed all storage buckets.");
      }
    }

###  Node.js 
    
    
    /**
     * TODO(developer):
     *  1. Uncomment and replace these variables before running the sample.
     *  2. Set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc
     *  3. Make sure you have the necessary permission to list storage buckets "storage.buckets.list"
     *    (https://cloud.google.com/storage/docs/access-control/iam-permissions#bucket_permissions)
     */
    // const projectId = 'YOUR_PROJECT_ID';
    
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    async function authenticateImplicitWithAdc() {
      // This snippet demonstrates how to list buckets.
      // NOTE: Replace the client created below with the client required for your application.
      // Note that the credentials are not specified when constructing the client.
      // The client library finds your credentials using ADC.
      const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)({
        projectId,
      });
      const [buckets] = await storage.[getBuckets](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/storage_2.html)();
      console.log('Buckets:');
    
      for (const bucket of buckets) {
        console.log(`- ${bucket.name}`);
      }
    
      console.log('Listed all storage buckets.');
    }
    
    authenticateImplicitWithAdc();

###  PHP 
    
    
    // Imports the Cloud Storage client library.
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Authenticate to a cloud client library using a service account implicitly.
     *
     * @param string $projectId The Google project ID.
     */
    function auth_cloud_implicit($projectId)
    {
        $config = [
            'projectId' => $projectId,
        ];
    
        # If you don't specify credentials when constructing the client, the
        # client library will look for credentials in the environment.
        $storage = new StorageClient($config);
    
        # Make an authenticated API request (listing storage buckets)
        foreach ($storage->buckets() as $bucket) {
            printf('Bucket: %s' . PHP_EOL, $bucket->name());
        }
    }

###  Python 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def authenticate_implicit_with_adc(project_id: str = "your-google-cloud-project-id") -> None:
        """
        When interacting with Google Cloud Client libraries, the library can auto-detect the
        credentials to use.
    
        // TODO(Developer):
        //  1. Before running this sample,
        //  set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc
        //  2. Replace the project variable.
        //  3. Make sure that the user account or service account that you are using
        //  has the required permissions. For this sample, you must have "storage.buckets.list".
        Args:
            project_id: The project id of your Google Cloud project.
        """
    
        # This snippet demonstrates how to list buckets.
        # *NOTE*: Replace the client created below with the client required for your application.
        # Note that the credentials are not specified when constructing the client.
        # Hence, the client library will look for credentials using ADC.
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)(project=project_id)
        buckets = storage_client.[list_buckets](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_list_buckets)()
        print("Buckets:")
        for bucket in buckets:
            print(bucket.name)
        print("Listed all storage buckets.")
    

###  Ruby 
    
    
    def authenticate_implicit_with_adc project_id:
      # The ID of your Google Cloud project
      # project_id = "your-google-cloud-project-id"
    
      ###
      # When interacting with Google Cloud Client libraries, the library can auto-detect the
      # credentials to use.
      # TODO(Developer):
      #   1. Before running this sample,
      #      set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc
      #   2. Replace the project variable.
      #   3. Make sure that the user account or service account that you are using
      #      has the required permissions. For this sample, you must have "storage.buckets.list".
      ###
    
      require "google/cloud/storage"
    
      # This sample demonstrates how to list buckets.
      # *NOTE*: Replace the client created below with the client required for your application.
      # Note that the credentials are not specified when constructing the client.
      # Hence, the client library will look for credentials using ADC.
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html) project_id: project_id
      buckets = storage.buckets
      puts "Buckets: "
      buckets.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do |bucket|
        puts bucket.name
      end
      puts "Plaintext: Listed all storage buckets."
    end

## Use API keys with client libraries

You can use an API keys only with client libraries for APIs that accept API keys. In addition, the API key must not have an API restriction that prevents it from being used for the API.

For more information about API keys created in express mode, see the [Google Cloud express mode FAQ](https://cloud.google.com/resources/cloud-express-faqs).

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

## Security requirements when using credential configurations from an external source

Typically, you generate credential configurations by using gcloud CLI commands or by using the Google Cloud console. For example, you can use the gcloud CLI to generate a local ADC file or a login configuration file. Similarly, you can use the Google Cloud console to create and download a service account key.

For some use cases, however, credential configurations are provided to you by an external entity; these credential configurations are intended to be used to authenticate to Google APIs.

Some types of credential configurations include endpoints and file paths, which the authentication libraries use to acquire a token. When you accept credential configurations from an external source, you must validate the configuration before using it. If you don't validate the configuration, a malicious actor could use the credential to compromise your systems and data.

### Validate credential configurations from external sources

How you need to validate your external credentials depends on what types of credential your application accepts.

#### Validate service account keys

If your application accepts _only_ service account keys, use a credential loader specific to service account keys, as shown in the following examples. The type-specific credential loader parses only the fields present for service account keys, which don't expose any vulnerabilities.

###  C# 
    
    
    var saCredential = CredentialFactory.FromStream<ServiceAccountCredential>(stream);
    

###  C++ 
    
    
    auto cred = google::cloud::MakeServiceAccountCredentials(json)
    

###  Java 
    
    
    ServiceAccountCredentials credentials =
          ServiceAccountCredentials.fromStream(credentialsStream);
    

###  Node.js 
    
    
    const keys = JSON.parse(json_input)
    const authClient = JWT.fromJSON(keys);
    

###  PHP 
    
    
    $cred = new Google\Auth\Credentials\ServiceAccountCredentials($scope, $jsonKey);
    

###  Python 
    
    
    cred = service_account.Credentials.from_service_account_info(json_data)
    

###  Ruby 
    
    
    creds = Google::Auth::[ServiceAccountCredentials](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-ServiceAccountCredentials.html).[make_creds](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-ServiceAccountCredentials.html)(json_key_io: json_stream)
    

If you can't use a type-specific credential loader, validate the credential by confirming that the value for the `type` field is `service_account`. If the value for the `type` field is any other value, don't use the service account key.

#### Validate other credential configurations

If your application accepts _any_ type of credential besides a service account key, you must perform additional verification. Examples of other types of credential configurations include [ADC credential files](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal), [Workload Identity Federation credential files](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#create-cred-config), or [Workforce Identity Federation login configuration files](https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials#create-login-config).

The following table lists the fields you need to validate, if they are present in your credentials. Not all of these fields are present for all credential configurations.

**Important:** If any of these fields contain a value that does not conform to the expected value, don't use the credential.Field | Purpose | Expected value  
---|---|---  
`service_account_impersonation_url` |  The authentication libraries use this field to access an endpoint to generate an access token for the service account being impersonated.  | `https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/service account email:generateAccessToken`  
`token_url` |  The authentication libraries send an external token to this endpoint to exchange it for a [federated access token](https://docs.cloud.google.com/docs/authentication/token-types#fed-access-tokens).  | `https://sts.googleapis.com/v1/token`  
`credential_source.file` |  The authentication libraries read an external token from the file at the location specified by this field and send it to the `token_url` endpoint.  |  The path for a file containing an external token. You should recognize this path.   
`credential_source.url` |  An endpoint that returns an external token. The authentication libraries send a request to this URL and send the response to the `token_url` endpoint.  |  One of the following items:

  * A well-known endpoint provided by your cloud provider.
  * An endpoint that you have explicitly set up to provide tokens.

  
`credential_source.executable.command` |  If the `GOOGLE_EXTERNAL_ACCOUNT_ALLOW_EXECUTABLES` environment variable is set to `1`, the authentication libraries run this command or executable file.  |  An executable file or command that returns an external token. You should recognize this command and validate that it is safe.   
`credential_source.aws.url` |  The authentication libraries issue a request to this URL to retrieve an AWS security token.  |  Either one of these exact values:

  * `http://169.254.169.254/latest/meta-data/iam/security-credentials`
  * `http://[fd00:ec2::254]/latest/meta-data/iam/security-credentials`

  
`credential_source.aws.region_url` |  The authentication libraries issue a request to this URL to retrieve the active AWS region.  |  Either one of these exact values:

  * `http://169.254.169.254/latest/meta-data/placement/availability-zone`
  * `http://[fd00:ec2::254]/latest/meta-data/placement/availability-zone`

  
`credential_source.aws.imdsv2_session_token_url` |  The authentication libraries issue a request to this URL to retrieve the AWS session token.  |  Either one of these exact values:

  * `http://169.254.169.254/latest/api/token`
  * `http://[fd00:ec2::254]/latest/api/token`

  
  
## What's next

  * Learn more about [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials).
  * Learn more about [API keys](https://docs.cloud.google.com/docs/authentication/api-keys).
  * See an overview of [Authentication methods](https://docs.cloud.google.com/docs/authentication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
