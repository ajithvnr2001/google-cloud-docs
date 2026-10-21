---
url: https://docs.cloud.google.com/java/getting-started/background-processing/
title: Background processing \u00a0|\u00a0 Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:47.764649+00:00
---

# Background processing  |  Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/getting-started/background-processing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Background processing Stay organized with collections  Save and categorize content based on your preferences. 

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



This tutorial is intended for anyone who is interested in learning about background processing with Google Cloud. No prior experience is required with Pub/Sub, Firestore, Cloud Run. However, to understand all of the code, some experience with Java and HTML is helpful.

## Objectives

  * Understand and deploy a Cloud Run service.
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

  4. Enable the Firestore, Pub/Sub, and Cloud Translation APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=firestore.googleapis.com,pubsub.googleapis.com,translate.googleapis.com)

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

  10. Enable the Firestore, Pub/Sub, and Cloud Translation APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=firestore.googleapis.com,pubsub.googleapis.com,translate.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Update `gcloud` components: 
         
         gcloud components update

  15. Prepare your development environment. 

[ Go to the Java setup guide ](https://docs.cloud.google.com/java/docs/setup)




## Preparing the app

  1. In your terminal window, clone the sample app repository to your local machine:
         
         git clone https://github.com/GoogleCloudPlatform/getting-started-java.git

Alternatively, you can [ download the sample ](https://github.com/GoogleCloudPlatform/getting-started-java/archive/master.zip) as a zip file and extract it. 

  2. Change to the directory that contains the background processing sample code:
         
         cd getting-started-java/background




## Understanding the app

There are two main components for the web app:

  * A Java HTTP server to handle web requests. The server has the following two endpoints: 
    * `/translate`
      * `GET` (by using a web browser): Displays 10 most recent processed translation requests submitted by users.
      * `POST` (with a Pub/Sub subscription): Processes translation requests using the Cloud Translation API and stores the results in Firestore.
    * `/create`: The form to submit new translate requests.
  * Service clients that process the translation requests submitted by the web form. There are three clients that work together: 
    * Pub/Sub: When the web form is submitted by a user, the Pub/Sub client publishes a message with the request details. A subscription created in this tutorial relays those messages to the Cloud Run endpoint that you create to perform translations.
    * Translation: This client handles Pub/Sub requests by performing the translations.
    * Firestore: When the translation is complete, this client stores the request data along with the translation in Firestore. This client also reads the most recent requests on the main `/translate` endpoint.



## Understanding the Cloud Run code

  * The Cloud Run app has dependencies on Firestore, Translation, and Pub/Sub.
        
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>google-cloud-firestore</artifactId>
          <version>3.13.2</version>
        </dependency>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>google-cloud-translate</artifactId>
          <version>2.20.0</version>
        </dependency>
        
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>google-cloud-pubsub</artifactId>
          <version>1.123.17</version>
        </dependency>

  * The global Firestore, Translation, and Pub/Sub clients are initialized so they can be reused between invocations. That way, you don't have to initialize new clients for every invocation, which would slow down execution.
        
        @WebListener("Creates Firestore and TranslateServlet service clients for reuse between requests.")
        public class BackgroundContextListener implements ServletContextListener {
          @Override
          public void contextDestroyed(javax.servlet.ServletContextEvent event) {}
        
          @Override
          public void contextInitialized(ServletContextEvent event) {
            String firestoreProjectId = System.getenv("FIRESTORE_CLOUD_PROJECT");
            Firestore firestore = (Firestore) event.getServletContext().getAttribute("firestore");
            if (firestore == null) {
              firestore =
                  FirestoreOptions.getDefaultInstance().toBuilder()
                      .setProjectId(firestoreProjectId)
                      .build()
                      .getService();
              event.getServletContext().setAttribute("firestore", firestore);
            }
        
            Translate translate = (Translate) event.getServletContext().getAttribute("translate");
            if (translate == null) {
              translate = TranslateOptions.getDefaultInstance().getService();
              event.getServletContext().setAttribute("translate", translate);
            }
        
            String topicId = System.getenv("PUBSUB_TOPIC");
            TopicName topicName = TopicName.of(firestoreProjectId, topicId);
            Publisher publisher = (Publisher) event.getServletContext().getAttribute("publisher");
            if (publisher == null) {
              try {
                publisher = Publisher.newBuilder(topicName).build();
                event.getServletContext().setAttribute("publisher", publisher);
              } catch (IOException e) {
                e.printStackTrace();
              }
            }
          }
        }

  * The index handler (`/`) gets all existing translations from Firestore and fills an HTML template with the list:
        
        @Override
        public void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
          Firestore firestore = (Firestore) this.getServletContext().getAttribute("firestore");
          CollectionReference translations = firestore.collection("translations");
          QuerySnapshot snapshot;
          try {
            snapshot = translations.limit(10).get().get();
          } catch (InterruptedException | ExecutionException e) {
            throw new ServletException("Exception retrieving documents from Firestore.", e);
          }
          List<TranslateMessage> translateMessages = Lists.newArrayList();
          List<QueryDocumentSnapshot> documents = Lists.newArrayList(snapshot.getDocuments());
          documents.sort(Comparator.comparing(DocumentSnapshot::getCreateTime));
        
          for (DocumentSnapshot document : Lists.reverse(documents)) {
            String encoded = gson.toJson(document.getData());
            TranslateMessage message = gson.fromJson(encoded, TranslateMessage.class);
            message.setData(decode(message.getData()));
            translateMessages.add(message);
          }
          req.setAttribute("messages", translateMessages);
          req.setAttribute("page", "list");
          req.getRequestDispatcher("/base.jsp").forward(req, resp);
        }

  * New translations are requested by submitting an HTML form. The request translation handler, registered at `/create`, parses the form submission, validates the request, and publishes a message to Pub/Sub:
        
        @Override
        public void doPost(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
          String text = req.getParameter("data");
          String sourceLang = req.getParameter("sourceLang");
          String targetLang = req.getParameter("targetLang");
        
          Enumeration<String> paramNames = req.getParameterNames();
          while (paramNames.hasMoreElements()) {
            String paramName = paramNames.nextElement();
            logger.warning("Param name: " + paramName + " = " + req.getParameter(paramName));
          }
        
          Publisher publisher = (Publisher) getServletContext().getAttribute("publisher");
        
          PubsubMessage pubsubMessage =
              PubsubMessage.newBuilder()
                  .setData(ByteString.copyFromUtf8(text))
                  .putAttributes("sourceLang", sourceLang)
                  .putAttributes("targetLang", targetLang)
                  .build();
        
          try {
            publisher.publish(pubsubMessage).get();
          } catch (InterruptedException | ExecutionException e) {
            throw new ServletException("Exception publishing message to topic.", e);
          }
        
          resp.sendRedirect("/");
        }

  * The Pub/Sub subscription that you create forwards those requests to the Cloud Run endpoint, which parses the Pub/Sub message to get the text to translate and the desired target language. The Translation API then translates the string to the language you selected.
        
        String body = req.getReader().lines().collect(Collectors.joining(System.lineSeparator()));
        
        PubSubMessage pubsubMessage = gson.fromJson(body, PubSubMessage.class);
        TranslateMessage message = pubsubMessage.getMessage();
        
        // Use Translate service client to translate the message.
        Translate translate = (Translate) this.getServletContext().getAttribute("translate");
        message.setData(decode(message.getData()));
        Translation translation =
            translate.translate(
                message.getData(),
                Translate.TranslateOption.sourceLanguage(message.getAttributes().getSourceLang()),
                Translate.TranslateOption.targetLanguage(message.getAttributes().getTargetLang()));

  * The app stores the translation data in a new document it creates in Firestore.
        
        // Use Firestore service client to store the translation in Firestore.
        Firestore firestore = (Firestore) this.getServletContext().getAttribute("firestore");
        
        CollectionReference translations = firestore.collection("translations");
        
        ApiFuture<WriteResult> setFuture = translations.document().set(message, SetOptions.merge());
        
        setFuture.get();
        resp.getWriter().write(translation.getTranslatedText());




## Deploying the Cloud Run app

  1. Choose a Pub/Sub Topic Name and generate a Pub/Sub Verification Token using `uuidgen` or an online UUID generator such as [uuidgenerator.net](https://www.uuidgenerator.net/). This token will ensure that the Cloud Run endpoint only accepts requests from the Pub/Sub subscription you create.
         
         export PUBSUB_TOPIC=background-translate
         export PUBSUB_VERIFICATION_TOKEN=your-verification-token

  2. Create a Pub/Sub topic:
         
         gcloud pubsub topics create $PUBSUB_TOPIC
         

     * Replace `MY_PROJECT` in the `pom.xml` file with your Google Cloud project ID.
  3. Build and deploy an image of your code to GCR (an image repository) with the [Jib](https://github.com/GoogleContainerTools/jib) Maven plugin.
         
         mvn clean package jib:build
         

  4. Deploy the app to Cloud Run:
         
         gcloud run deploy background --image gcr.io/MY_PROJECT/background \
               --platform managed --region us-central1 --memory 512M \
               --update-env-vars PUBSUB_TOPIC=$PUBSUB_TOPIC,PUBSUB_VERIFICATION_TOKEN=$PUBSUB_VERIFICATION_TOKEN

Where `MY_PROJECT` is the name of the Google Cloud project you created. This command outputs the endpoint to which your Pub/Sub subscription pushes translation requests. Make note of this endpoint, because you will need it to create the Pub/Sub subscription, and you will visit the endpoint in a browser to request a new translation.




## Testing the app

After you've deployed the Cloud Run service, try requesting a translation.

  1. To view the app in your browser, go to the Cloud Run endpoint that you previously created.

There is a page with an empty list of translations and a form to request new translations.

  2. Click **\+ Request Translation** , fill out the request form, and then click **Submit**.

  3. Submission automatically brings you back to the `/translate` path, but the new translation might not appear yet. To refresh the page, click **Refresh** _refresh_. There is a new row in the translation list. If you don't see a translation, wait a few more seconds and try again. If you still don't see a translation, see the next section about debugging the app.




## Debugging the app

If you cannot connect to your Cloud Run service or don't see new translations, check the following:

  * Check that the `gcloud run deploy` command successfully completed and didn't output any errors. If there were errors (for example, `message=Build failed`), fix them, and try running again.

  * Check for errors in the logs:

    1. In the Google Cloud console, go to the Cloud Run page.

[Go to Cloud Run page](https://console.cloud.google.com/run)

    2. Click the service name, **`background`**.

    3. Click **Logs**.




## Clean up

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the Cloud Run services.

  * Delete the Cloud Run services you created in this tutorial:
        
        gcloud run services delete --region=$region background




## What's next

  * [Learn more about Cloud Run](https://docs.cloud.google.com/run/docs).
  * [Try Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/deploy-container), which lets you run stateless containers on a fully managed environment or in your own Google Kubernetes Engine cluster.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
