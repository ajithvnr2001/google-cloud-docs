---
url: https://docs.cloud.google.com/dotnet/docs/getting-started/background-processing/
title: Background processing with .NET \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:05.638803+00:00
---

# Background processing with .NET  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/getting-started/background-processing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Guides ](https://docs.cloud.google.com/dotnet/docs/setup)



Send feedback 

#  Background processing with .NET Stay organized with collections  Save and categorize content based on your preferences. 

Many apps need to do background processing outside of the context of a web request. This tutorial creates a web app that lets users input text to translate, and then displays a list of previous translations. The translation is done in a background process to avoid blocking the user's request. 

The following diagram illustrates the translation request process. 

![Diagram of architecture.](https://docs.cloud.google.com/static/languages/images/background-event-architecture-cloud-run.svg)

Here is the sequence of events for how the tutorial app works: 

  1. Visit the web page to see a list of previous translations, stored in Firestore.
  2. Request a translation of text by entering an HTML form.
  3. The translation request is published to Pub/Sub.
  4. A Cloud Run service subscribed to that Pub/Sub topic is triggered.
  5. The Cloud Run service uses Cloud Translation to translate the text.
  6. The Cloud Run service stores the result in Firestore.



This tutorial is intended for anyone who is interested in learning about background processing with Google Cloud. No prior experience is required with Pub/Sub, Firestore, App Engine, or Cloud Run functions. However, to understand all of the code, some experience with .NET, JavaScript, and HTML is helpful. 

## Objectives

  * Understand and deploy Cloud Run services.
  * Try the app.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Run](https://docs.cloud.google.com/run/pricing)
  * [Firestore](https://docs.cloud.google.com/firestore/pricing)
  * [Pub/Sub](https://docs.cloud.google.com/pubsub/pricing)
  * [Cloud Translation](https://docs.cloud.google.com/translate/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Firestore, Cloud Run, Pub/Sub, and Cloud Translation APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=firestore.googleapis.com,run.googleapis.com,pubsub.googleapis.com,translate.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Firestore, Cloud Run, Pub/Sub, and Cloud Translation APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=firestore.googleapis.com,run.googleapis.com,pubsub.googleapis.com,translate.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Update `gcloud` components: 
         
         gcloud components update

  15. Prepare your development environment. 

[ Setting up a .NET development environment ](https://docs.cloud.google.com/dotnet/docs/setup)




## Preparing the app

  1. In your terminal window, clone the sample app repository to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/getting-started-dotnet.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/getting-started-dotnet/archive/master.zip) as a zip file and extract it. 

  2. Change to the directory that contains the background task sample code:
         
         cd getting-started-dotnet/BackgroundProcessing




## Understanding the `TranslateWorker` service

  * The service starts by importing several dependencies like Firestore and Translation.
        
        using [Google.Cloud.Firestore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.html);
        using [Google.Cloud.Translation.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translation.V2/latest/Google.Cloud.Translation.V2.html);
        

  * The Firestore and Translation clients are initialized so they can be reused between handler invocations. That way, you don't have to initialize new clients for every invocation, which would slow down execution.
        
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddSingleton<FirestoreDb>(provider =>
                FirestoreDb.Create(GetFirestoreProjectId()));
            services.AddSingleton<TranslationClient>(
                TranslationClient.Create());
            services.AddMvc().SetCompatibilityVersion(CompatibilityVersion.Version_2_1);
        }
        

  * The Translation API translates the string to the language you selected.
        
        var result = await _translator.TranslateTextAsync(sourceText, "es");
        

  * The controller's constructor receives the Firestore and Pub/Sub clients.

The `Post` method parses the Pub/Sub message to get the text to translate. It uses the message ID as a unique name for the translation request to make sure it doesn't store any duplicate translations.
        
        using [Google.Cloud.Firestore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.html);
        using [Google.Cloud.Translation.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translation.V2/latest/Google.Cloud.Translation.V2.html);
        using Microsoft.AspNetCore.Mvc;
        using Microsoft.Extensions.Logging;
        using System;
        using System.Collections.Generic;
        using System.Text;
        using System.Threading.Tasks;
        
        namespace TranslateWorker.Controllers
        {
            /// <summary>
            /// The message Pubsub posts to our controller.
            /// </summary>
            public class PostMessage
            {
                public PubsubMessage message { get; set; }
                public string subscription { get; set; }
            }
        
            /// <summary>
            /// Pubsub's inner message.
            /// </summary>
            public class PubsubMessage
            {
                public string data { get; set; }
                public string messageId { get; set; }
                public Dictionary<string, string> attributes { get; set; }
            }
        
        
            [Route("api/[controller]")]
            [ApiController]
            public class TranslateController : ControllerBase
            {
                private readonly ILogger<TranslateController> _logger;
                private readonly [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) _firestore;
                private readonly [TranslationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translation.V2/latest/Google.Cloud.Translation.V2.TranslationClient.html) _translator;
                // The Firestore collection where we store translations.
                private readonly [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) _translations;
        
                public TranslateController(ILogger<TranslateController> logger,
                    [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) firestore,
                    [TranslationClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translation.V2/latest/Google.Cloud.Translation.V2.TranslationClient.html) translator)
                {
                    _logger = logger ?? throw new ArgumentNullException(nameof(logger));
                    _firestore = firestore ?? throw new ArgumentNullException(
                        nameof(firestore));
                    _translator = translator ?? throw new ArgumentNullException(
                        nameof(translator));
                    _translations = _firestore.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("Translations");
                }
        
                /// <summary>
                /// Handle a posted message from Pubsub.
                /// </summary>
                /// <param name="request">The message Pubsub posts to this process.</param>
                /// <returns>NoContent on success.</returns>
                [HttpPost]
                public async Task<IActionResult> Post([FromBody] PostMessage request)
                {
                    // Unpack the message from Pubsub.
                    string sourceText;
                    try
                    {
                        byte[] data = Convert.FromBase64String(request.message.data);
                        sourceText = Encoding.UTF8.GetString(data);
                    }
                    catch (Exception e)
                    {
                        _logger.LogError(1, e, "Bad request");
                        return BadRequest();
                    }
                    // Translate the source text.
                    _logger.LogDebug(2, "Translating {0} to Spanish.", sourceText);
                    var result = await _translator.[TranslateTextAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translation.V2/latest/Google.Cloud.Translation.V2.TranslationClient.html#Google_Cloud_Translation_V2_TranslationClient_TranslateTextAsync_System_Collections_Generic_IEnumerable_System_String__System_String_System_String_System_Nullable_Google_Cloud_Translation_V2_TranslationModel__System_Threading_CancellationToken_)(sourceText, "es");
                    // Store the result in Firestore.
                    Translation translation = new Translation()
                    {
                        TimeStamp = DateTime.UtcNow,
                        SourceText = sourceText,
                        TranslatedText = result.[TranslatedText](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translation.V2/latest/Google.Cloud.Translation.V2.TranslationResult.html#Google_Cloud_Translation_V2_TranslationResult_TranslatedText)
                    };
                    _logger.LogDebug(3, "Saving translation {0} to {1}.",
                        translation.[TranslatedText](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Translation.V2/latest/Google.Cloud.Translation.V2.TranslationResult.html#Google_Cloud_Translation_V2_TranslationResult_TranslatedText), _translations.[Path](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Path));
                    await _translations.[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html#Google_Cloud_Firestore_CollectionReference_Document)(request.message.messageId)
                        .[SetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.DocumentReference.html#Google_Cloud_Firestore_DocumentReference_SetAsync_System_Object_Google_Cloud_Firestore_SetOptions_System_Threading_CancellationToken_)(translation);
                    // Return a success code.
                    return NoContent();
                }
        
                /// <summary>
                /// Serve a root page so Cloud Run knows this process is healthy.
                /// </summary>
                [Route("/")]
                public IActionResult Index()
                {
                    return Content("Serving translate requests...");
                }
            }
        }
        




## Deploying the `TranslateWorker` service

  * In the `BackgroundProcessing` directory, run the PowerShell script to build and deploy the service to Cloud Run:
        
        PublishTo-CloudRun.ps1




## Understanding the `PublishTo-CloudRun.ps1` script

The `PublishTo-CloudRun.ps1` script publishes the service to Cloud Run, and protects the TranslateWorker service from being abused. If the service permitted all incoming connections, then anyone could post translate requests to the controller and thereby incur costs. Therefore, you set up the service to only accept `POST` requests from Pub/Sub.

The script does the following:

  1. Builds the app locally using `dotnet publish`.
  2. Builds a container that runs the app using [Cloud Build](https://docs.cloud.google.com/build).
  3. Deploys the app to Cloud Run.
  4. Enables the project to create Pub/Sub authentication tokens.
  5. Creates a service account to represent the Pub/Sub subscription identity.
  6. Gives the service account permission to invoke `TranslateWorker` service.
  7. Creates a Pub/Sub topic and subscription.
         
         # 1. Build the application locally.
         dotnet publish -c Release
         
         # Collect some details about the project that we'll need later.
         $projectId = gcloud config get-value project
         $projectNumber = gcloud projects describe $projectId --format="get(projectNumber)"
         $region = "us-central1"
         
         # 2. Use Google Cloud Build to build the worker's container and publish to Google
         # Container Registry.
         gcloud builds submit --tag gcr.io/$projectId/translate-worker `
             TranslateWorker/bin/Release/netcoreapp2.1/publish
         
         # 3. Run the container with Google Cloud Run.
         gcloud beta run deploy translate-worker --region $region --platform managed `
             --image gcr.io/$projectId/translate-worker --no-allow-unauthenticated
         $url = gcloud beta run services describe translate-worker --platform managed `
             --region $region --format="get(status.address.hostname)"
         
         # 4. Enable the project to create pubsub authentication tokens.
         gcloud projects add-iam-policy-binding $projectId `
              --member=serviceAccount:service-$projectNumber@gcp-sa-pubsub.iam.gserviceaccount.com `
              --role=roles/iam.serviceAccountTokenCreator
         
         # 5. Create a service account to represent the Cloud Pub/Sub subscription identity.
         $serviceAccountExists = gcloud iam service-accounts describe `
             cloud-run-pubsub-invoker@$projectId.iam.gserviceaccount.com 2> $null
         if (-not $serviceAccountExists) {
             gcloud iam service-accounts create cloud-run-pubsub-invoker `
                 --display-name "Cloud Run Pub/Sub Invoker"
         }
         
         # 6. For Cloud Run, give this service account permission to invoke 
         # translate-worker service.
         gcloud beta run services add-iam-policy-binding translate-worker `
              --member=serviceAccount:cloud-run-pubsub-invoker@$projectId.iam.gserviceaccount.com `
              --role=roles/run.invoker --region=$region
         
         # 7. Create a pubsub topic and subscription, if they don't already exist.
         $topicExists = gcloud pubsub topics describe translate-requests 2> $null 
         if (-not $topicExists) {
             gcloud pubsub topics create translate-requests
         }
         $subscriptionExists = gcloud pubsub subscriptions describe translate-requests 2> $null
         if ($subscriptionExists) {
             gcloud beta pubsub subscriptions modify-push-config translate-requests `
                 --push-endpoint $url/api/translate `
                 --push-auth-service-account cloud-run-pubsub-invoker@$projectId.iam.gserviceaccount.com
         } else {
             gcloud beta pubsub subscriptions create translate-requests `
                 --topic translate-requests --push-endpoint $url/api/translate `
                 --push-auth-service-account cloud-run-pubsub-invoker@$projectId.iam.gserviceaccount.com
         }
         




## Understanding the `TranslateUI` service

The `TranslateUI` service renders a web page that displays recent translations, and accepts requests for new translations.

  * The `StartUp` class configures an ASP.NET app and creates Pub/Sub and Firestore clients.
        
        using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
        using [Google.Cloud.Firestore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.html);
        using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
        using Microsoft.AspNetCore.Builder;
        using Microsoft.AspNetCore.Hosting;
        using Microsoft.AspNetCore.Mvc;
        using Microsoft.Extensions.Configuration;
        using [Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.HypercomputeCluster.V1/latest/Microsoft.Extensions.DependencyInjection.html);
        using System;
        using System.Net.Http;
        
        namespace TranslateUI
        {
            public class Startup
            {
                public Startup(IConfiguration configuration)
                {
                    Configuration = configuration;
                }
        
                public IConfiguration Configuration { get; }
        
                // This method gets called by the runtime. Use this method to add services to the container.
                public void ConfigureServices(IServiceCollection services)
                {
                    services.AddSingleton<FirestoreDb>(
                        provider => [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Create_System_String_Google_Cloud_Firestore_V1_FirestoreClient_)(GetFirestoreProjectId()));
                    services.AddSingleton<PublisherClient>(
                        provider => [PublisherClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html#Google_Cloud_PubSub_V1_PublisherClient_CreateAsync_Google_Cloud_PubSub_V1_TopicName_)(new [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html)(
                            GetProjectId(), GetTopicName())).[Result](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.RunAggregationQueryResponse.html#Google_Cloud_Firestore_V1_RunAggregationQueryResponse_Result));
                    services.AddMvc().SetCompatibilityVersion(CompatibilityVersion.Version_2_1);
                }
        
                // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
                public void Configure(IApplicationBuilder app, IHostingEnvironment env)
                {
                    if (env.IsDevelopment())
                    {
                        app.UseDeveloperExceptionPage();
                    }
                    else
                    {
                        app.UseExceptionHandler("/Home/Error");
                        // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
                        app.UseHsts();
                    }
        
                    app.UseHttpsRedirection();
                    app.UseStaticFiles();
                    app.UseCookiePolicy();
        
                    app.UseMvc(routes =>
                    {
                        routes.MapRoute(
                            name: "default",
                            template: "{controller=Home}/{action=Index}/{id?}");
                    });
                }
        
            }
        }
        

  * The index handler `Index` gets all existing translations from Firestore and fills a `ViewModel` with the list:
        
        using [Google.Cloud.Firestore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.html);
        using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
        using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
        using Microsoft.AspNetCore.Mvc;
        using System.Diagnostics;
        using System.Linq;
        using System.Threading.Tasks;
        using TranslateUI.Models;
        
        namespace TranslateUI.Controllers
        {
            public class HomeController : Controller
            {
                private readonly [FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) _firestore;
                private readonly [PublisherClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html) _publisher;
                private [CollectionReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.CollectionReference.html) _translations;
        
                public HomeController([FirestoreDb](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html) firestore, [PublisherClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html) publisher)
                {
                    _firestore = firestore;
                    _publisher = publisher;
                    _translations = _firestore.[Collection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.FirestoreDb.html#Google_Cloud_Firestore_FirestoreDb_Collection_System_String_)("Translations");
                }
        
                [HttpPost]
                [HttpGet]
                public async Task<IActionResult> Index(string SourceText)
                {
                    // Look up the most recent 20 translations.
                    var query = _translations.[OrderByDescending](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore/latest/Google.Cloud.Firestore.Query.html#Google_Cloud_Firestore_Query_OrderByDescending_Google_Cloud_Firestore_FieldPath_)("TimeStamp")
                        .Limit(20);
                    var snapshotTask = query.GetSnapshotAsync();
        
                    if (!string.IsNullOrWhiteSpace(SourceText))
                    {
                        // Submit a new translation request.
                        await _publisher.[PublishAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherClient.html#Google_Cloud_PubSub_V1_PublisherClient_PublishAsync_Google_Cloud_PubSub_V1_PubsubMessage_)(new [PubsubMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PubsubMessage.html)()
                        {
                            Data = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFromUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFromUtf8_System_String_)(SourceText)
                        });
                    }
        
                    // Render the page.
                    var model = new HomeViewModel()
                    {
                        Translations = (await snapshotTask).Documents.Select(
                            doc => doc.ConvertTo<Translation>()).ToList(),
                        SourceText = SourceText
                    };
                    return View(model);
                }
        
                [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
                public IActionResult Error()
                {
                    return View(new ErrorViewModel { RequestId = Activity.[Current](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.TargetChange.Types.TargetChangeType.html#Google_Cloud_Firestore_V1_TargetChange_Types_TargetChangeType_Current)?.Id ?? HttpContext.TraceIdentifier });
                }
            }
        }

  * New translations are requested by submitting an HTML form. The request translation handler validates the request, and publishes a message to Pub/Sub:
        
        // Submit a new translation request.
        await _publisher.PublishAsync(new PubsubMessage()
        {
            Data = ByteString.CopyFromUtf8(SourceText)
        });
        




## Deploying the `TranslateUI` service

  * In the `BackgroundProcessing` directory, run the PowerShell script to build and deploy the service to Cloud Run:
        
        ./PublishTo-CloudRun.ps1




## Understanding the `PublishTo-CloudRun.ps1` script

The `PublishTo-CloudRun.ps1` script publishes the app to Cloud Run.

The script does the following:

  1. Builds the app locally using `dotnet publish`.
  2. Builds a container that runs the app by using [Cloud Build](https://docs.cloud.google.com/build).
  3. Deploys the app to Cloud Run.
         
         # 1. Build the application locally.
         dotnet publish -c Release
         # 2. Use Google Cloud Build to build the UI's container and publish to Google
         # Container Registry. 
         gcloud builds submit --tag gcr.io/$projectId/translate-ui `
             TranslateUI/bin/Release/netcoreapp2.1/publish
         
         # 3. Run the container with Google Cloud Run.
         gcloud beta run deploy translate-ui --region $region --platform managed `
             --image gcr.io/$projectId/translate-ui --allow-unauthenticated
         




## Testing the app

After successfully running the `PublishTo-CloudRun.ps1` script, try requesting a translation.

  1. The final command in the `PublishTo-CloudRun.ps1` script tells you the URL for your UI service. In your terminal window, find the URL for the `TranslateUI` service:
         
         gcloud beta run services describe translate-ui --region $region --format="get(status.address.hostname)"

  2. In your browser, go to the URL that you got from the previous step.

There is a page with an empty list of translations and a form to request new translations.

  3. In the **Text to translate** field, enter some text to translate, for example, `Hello, World.`

  4. Click **Submit**.

  5. To refresh the page, click **Refresh** _refresh_. There is a new row in the translation list. If you don't see a translation, wait a few more seconds and try again. If you still don't see a translation, see the next section about debugging the app.




## Debugging the app

If you cannot connect to your Cloud Run service or don't see new translations, check the following:

  * Check that the `PublishTo-CloudRun.ps1` script successfully completed and didn't output any errors. If there were errors (for example, `message=Build failed`), fix them, and try running again.

  * Check for errors in the logs:

    1. In the Google Cloud console, go to the Cloud Run page.

[Go to Cloud Run page](https://console.cloud.google.com/run)

    2. Click the service name, **`translate-ui`**.

    3. Click **Logs**.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the Google Cloud project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the Cloud Run services.

  * Delete the Cloud Run services you created in this tutorial:
        
        gcloud beta run services delete --region=$region translate-ui
        
        gcloud beta run services delete --region=$region translate-worker




## What's next

  * [Learn more about Cloud Run](https://docs.cloud.google.com/run/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
