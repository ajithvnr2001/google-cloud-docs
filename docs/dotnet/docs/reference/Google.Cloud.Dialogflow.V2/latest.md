---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/
title: Google.Cloud.Dialogflow.V2 \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:49.281639+00:00
---

# Google.Cloud.Dialogflow.V2  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.Dialogflow.V2 Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 

`Google.Cloud.Dialogflow.V2` is a.NET client library for the [Google Cloud Dialogflow API](https://cloud.google.com/dialogflow-enterprise/).

Note: This documentation is for version `4.33.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Dialogflow.V2` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

All operations are performed through the following client classes:

  * [AgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AgentsClient)
  * [AnswerRecordsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.AnswerRecordsClient)
  * [CompanionAgentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CompanionAgentsClient)
  * [ContextsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ContextsClient)
  * [ConversationDatasetsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationDatasetsClient)
  * [ConversationModelsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationModelsClient)
  * [ConversationProfilesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationProfilesClient)
  * [ConversationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ConversationsClient)
  * [DocumentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.DocumentsClient)
  * [EncryptionSpecServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EncryptionSpecServiceClient)
  * [EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EntityTypesClient)
  * [EnvironmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.EnvironmentsClient)
  * [FulfillmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.FulfillmentsClient)
  * [GeneratorEvaluationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GeneratorEvaluationsClient)
  * [GeneratorsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.GeneratorsClient)
  * [IntentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.IntentsClient)
  * [KnowledgeBasesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.KnowledgeBasesClient)
  * [ParticipantsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ParticipantsClient)
  * [SessionEntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SessionEntityTypesClient)
  * [SessionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SessionsClient)
  * [SipTrunksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.SipTrunksClient)
  * [ToolsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.ToolsClient)
  * [VersionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.VersionsClient)



Create a client instance by calling the static `Create` or `CreateAsync` methods. Alternatively, use the builder class associated with each client class (e.g. AgentsClientBuilder for AgentsClient) as an easy way of specifying custom credentials, settings, or a custom endpoint. Clients are thread-safe, and we recommend using a single instance across your entire application unless you have a particular need to configure multiple client objects separately.

### Using the REST (HTTP/1.1) transport

This library defaults to performing RPCs using [gRPC](https://grpc.io/) using the binary [Protocol Buffer](https://protobuf.dev) wire format. However, it also supports HTTP/1.1 and JSON, for situations where gRPC doesn't work as desired. (This is typically due to an incompatible proxy or other network issue.) To create a client using HTTP/1.1, specify a `RestGrpcAdapter` reference for the `GrpcAdapter` property in the client builder. Sample code:
    
    
    var client = new AgentsClientBuilder
    {
        GrpcAdapter = RestGrpcAdapter.Default
    }.Build();
    

For more details, see the [transport selection](https://cloud.google.com/dotnet/docs/reference/help/transports) page.

## Implementing a web hook

You don't _need_ this package in order to implement a webhook as a [Dialogflow fulfillment](https://dialogflow.com/docs/fulfillment). You can accept a JSON request dynamically and respond to it with JSON, for example using `JObject` from Json.NET.

This package allows you to work with a more statically-typed view of the request and response using the Protocol Buffers representation of `WebhookRequest` and `WebhookResponse`, however. In order to do this, you **must** use the JSON parser and formatted provided for Protocol Buffers. You will run into problems if you use Json.NET or similar general-purpose JSON libraries, as they don't know the details of Protocol Buffer JSON representations.

Additionally, it's worth configuring the Protocol Buffer JSON parser to ignore unknown fields. This means your webhook won't break if additional fields are added to `WebhookRequest` in the future.

Please refer to the [fulfillment documentation](https://dialogflow.com/docs/fulfillment) for more details around authentication, and the schema of requests and responses.

The samples below provide a starting point for ASP.NET Core and ASP.NET. Note that by default, ASP.NET Core 3.x does not allow synchronous IO, and the Google.Protobuf library does not yet support asynchronous parsing from a reader, so you need to asynchronously read the JSON directly as a string first, then parse the string. It's likely that in the future, Google.Protobuf will allow asynchronous parsing.

### Web hook template code for ASP.NET Core (asynchronous-only)
    
    
    public class DialogflowController : ControllerBase
    {
        // A Protobuf JSON parser configured to ignore unknown fields. This makes
        // the action robust against new fields being introduced by Dialogflow.
        private static readonly JsonParser jsonParser =
            new JsonParser(JsonParser.Settings.Default.WithIgnoreUnknownFields(true));
    
        public async Task<ContentResult> DialogAction()
        {
            // Read the request JSON asynchronously, as the Google.Protobuf library
            // doesn't (yet) support asynchronous parsing.
            string requestJson;
            using (TextReader reader = new StreamReader(Request.Body))
            {
                requestJson = await reader.ReadToEndAsync();
            }
    
            // Parse the body of the request using the Protobuf JSON parser,
            // *not* Json.NET.
            WebhookRequest request = jsonParser.Parse<WebhookRequest>(requestJson);
    
            // Note: you should authenticate the request here.
    
            // Populate the response
            WebhookResponse response = new WebhookResponse
            {
                // ...
            };
    
            // Ask Protobuf to format the JSON to return.
            // Again, we don't want to use Json.NET - it doesn't know how to handle Struct
            // values etc.
            string responseJson = response.ToString();
            return Content(responseJson, "application/json");
        }
    }
    

### Web hook template code for ASP.NET Core (synchronous parsing)
    
    
    public class DialogflowController : ControllerBase
    {
        // A Protobuf JSON parser configured to ignore unknown fields. This makes
        // the action robust against new fields being introduced by Dialogflow.
        private static readonly JsonParser jsonParser =
            new JsonParser(JsonParser.Settings.Default.WithIgnoreUnknownFields(true));
    
        public ContentResult DialogAction()
        {
            // Parse the body of the request using the Protobuf JSON parser,
            // *not* Json.NET.
            WebhookRequest request;
            using (TextReader reader = new StreamReader(Request.Body))
            {
                request = jsonParser.Parse<WebhookRequest>(reader);
            }
    
            // Note: you should authenticate the request here.
    
            // Populate the response
            WebhookResponse response = new WebhookResponse
            {
                // ...
            };
    
            // Ask Protobuf to format the JSON to return.
            // Again, we don't want to use Json.NET - it doesn't know how to handle Struct
            // values etc.
            string responseJson = response.ToString();
            return Content(responseJson, "application/json");
        }
    }
    

### Web hook template code for ASP.NET (classic) Web API
    
    
    public class WebApiController : ApiController
    {
        // A Protobuf JSON parser configured to ignore unknown fields. This makes
        // the action robust against new fields being introduced by Dialogflow.
        private static readonly JsonParser jsonParser =
            new JsonParser(JsonParser.Settings.Default.WithIgnoreUnknownFields(true));
    
        [HttpPost]
        public async Task<HttpResponseMessage> Post()
        {
            WebhookRequest request;
            using (var stream = await Request.Content.ReadAsStreamAsync())
            {
                using (var reader = new StreamReader(stream))
                {
                    request = jsonParser.Parse<WebhookRequest>(reader);
                }
            }
            WebhookResponse webhookResponse = new WebhookResponse
            {
                // ...
            };
            HttpResponseMessage httpResponse = new HttpResponseMessage(HttpStatusCode.OK)
            {
                // Ask Protobuf to format the JSON to return.
                // Again, we don't want to use Json.NET - it doesn't know how to handle Struct
                // values etc.
                Content = new StringContent(webhookResponse.ToString())
                {
                    Headers = { ContentType = new MediaTypeHeaderValue("text/json") }
                }
            };
    
            return httpResponse;
        }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
