---
url: https://docs.cloud.google.com/code/docs/vscode/quickstart-clientlib/
title: Use the Cloud Client Libraries in Cloud Code \u00a0|\u00a0 Cloud Code for VS Code \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:12.790692+00:00
---

# Use the Cloud Client Libraries in Cloud Code  |  Cloud Code for VS Code  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/vscode/quickstart-clientlib/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for VS Code ](https://docs.cloud.google.com/code/docs/vscode)
  * [ Guides ](https://docs.cloud.google.com/code/docs/vscode/quickstart)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use the Cloud Client Libraries in Cloud Code

This page shows you how to get started quickly with Cloud Client Libraries and Cloud Code. You'll set up a new Kubernetes application using a Hello World sample application and then update the application to use the Cloud Translation API to translate the response to Spanish.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Google Kubernetes Engine and Cloud Translation APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,translate.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Google Kubernetes Engine and Cloud Translation APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,translate.googleapis.com)

  8. Install [Git](https://git-scm.com/downloads) so that Cloud Code can perform Git operations, like cloning a sample.
  9. Install the [Cloud Code plugin](https://docs.cloud.google.com/code/docs/vscode/install#installing) if you haven't already.



## Create an application

  1. From the command palette (`Cmd`/`Ctrl`+`Shift`+`P`), run **Cloud Code: New Application** , choose **Kubernetes Application** , and then choose a Hello World app in the language you prefer. For example, choose **Node.js: Hello World** to create a starter Node.js Hello World app.
  2. Save the new application. A notification confirms that your application has been created and a new window with your application opens.



## Set up credentials

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  1. To open a terminal, click **Terminal** > **New Terminal**.

  2. Create a service account to authenticate your API requests:
         
         gcloud iam service-accounts create \
         translation-quickstart \
         --project PROJECT_ID

  3. Grant your service account the Cloud Translation API User role:
         
         gcloud projects \
         add-iam-policy-binding \
         PROJECT_ID \
         --member='serviceAccount:translation-quickstart@PROJECT_ID.iam.gserviceaccount.com' \
         --role='roles/cloudtranslate.user'

  4. Create a service account key:
         
         gcloud iam service-accounts keys \
         create key.json --iam-account \
         translation-quickstart@PROJECT_ID.iam.gserviceaccount.com

  5. Set the key as your default credentials:
         
         export \
          GOOGLE_APPLICATION_CREDENTIALS=key.json
         




## Call the Cloud Translation API from your application

###  Go 

  1. Install the Cloud Translation API Cloud Client Libraries:

     1. To open a terminal, click **Terminal** > **New Terminal**.
     2. Run the following command:
            
            go get cloud.google.com/go/translate/apiv3
            

  2. Create an `app.go` file.

  3. Open `app.go` and add your package name, imports, and app skeleton:
         
         package main
         
         import (
           "context"
           "fmt"
         
           translate "cloud.google.com/go/translate/apiv3"
           translatepb "google.golang.org/genproto/googleapis/cloud/translate/v3"
         )
         
         func translateText(w io.Writer, projectID string, sourceLang string, targetLang string, text string) error {
         
         }
         
         func main() {
         
         }
         

  4. In your `translateText()` function, add the following code, which translates the specified text. Select **File > Save** to reformat your code:
         
         ctx := context.Background()
         client, err := translate.NewTranslationClient(ctx)
         if err != nil {
           return fmt.Errorf("NewTranslationClient: %v", err)
         }
         defer client.Close()
         
         req := &translatepb.TranslateTextRequest{
           Parent:             fmt.Sprintf("projects/%s/locations/global", projectID),
           SourceLanguageCode: sourceLang,
           TargetLanguageCode: targetLang,
           MimeType:           "text/plain", // Mime types: "text/plain", "text/html"
           Contents:           []string{text},
         }
         
         resp, err := client.TranslateText(ctx, req)
         if err != nil {
           return fmt.Errorf("TranslateText: %v", err)
         }
         
         // Display the translation for each input text provided
         for _, translation := range resp.GetTranslations() {
           fmt.Fprintf(w, "Translated text: %v\n", translation.GetTranslatedText())
         }
         
         return nil
         

  5. In your `main()` function, call `translateText()`. The following parameter values translate English to Spanish:
         
         projectID := "<var>PROJECT_ID</var>"
         sourceLang := "en-US"
         targetLang := "es"
         text := "Text to translate"
         
         err := translateText(os.Stdout, projectID, sourceLang, targetLang, text)
         if err != nil {
           fmt.Print(err)
         }
         

  6. From the terminal, run your application.
         
         go run app.go
         




###  Java 

  1. Open `pom.xml` and add the following code snippet to the `dependencies` section:
         
         <dependencies>
           <dependency>
             <groupId>junit</groupId>
             <artifactId>junit</artifactId>
             <version>4.11</version>
             <scope>test</scope>
           </dependency>
           <dependency>
             <groupId>com.google.cloud</groupId>
             <artifactId>google-cloud-translate</artifactId>
           </dependency>
         </dependencies>
         

  2. Then, in the `pom.xml` file, add the following code snippet to the `dependencyManagement` section:
         
         <dependencyManagement>
           <dependencies>
             <dependency>
               <groupId>com.google.cloud</groupId>
               <artifactId>libraries-bom</artifactId>
               <version>26.39.0</version>
               <type>pom</type>
               <scope>import</scope>
             </dependency>
           </dependencies>
         </dependencyManagement>
         

Make sure you're using the latest version of Google Cloud Supported Libraries. For a list of versions, see [Google Cloud Supported Libraries](https://mvnrepository.com/artifact/com.google.cloud/libraries-bom).

  3. When asked if you want to synchronize the Java classpath/configuration, click **Always**.

  4. Create a file named `app.java`.

  5. In`app.java`, include the following imports after the package definition:
         
         import com.google.cloud.translate.v3.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html);
         import com.google.cloud.translate.v3.[TranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextRequest.html);
         import com.google.cloud.translate.v3.[TranslateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextResponse.html);
         import com.google.cloud.translate.v3.[Translation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Translation.html);
         import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
         import java.io.IOException;
         

  6. Add the `translateText()` method to your `App` class. This method sets and passes variables to an overloaded `translateText()` method. The following values translate English to Spanish:
         
         public static void translateText() throws IOException {
           String projectId = "<walkthrough-project-id/>";
           String targetLanguage = "es";
           String text = "Hello world!";
           translateText(projectId, targetLanguage, text);
         }
         

  7. Add an overloaded `translateText()` method. This method takes text and translates it to the target language.
         
         public static void translateText(String projectId, String targetLanguage, String text)
           throws IOException {
         
           try (TranslationServiceClient client = TranslationServiceClient.create()) {
             LocationName parent = LocationName.of(projectId, "global");
         
             TranslateTextRequest request =
               TranslateTextRequest.newBuilder()
               .setParent(parent.toString())
               .setMimeType("text/plain")
               .setTargetLanguageCode(targetLanguage)
               .addContents(text)
               .build();
         
             TranslateTextResponse response = client.translateText(request);
         
             // Display the translation for each input text provided
             for (Translation translation : response.getTranslationsList()) {
               System.out.printf("Translated text: %s\n", translation.getTranslatedText());
             }
           }
         }
         

  8. Replace the print statement in your `main` with a call to `translateText()`:
         
         try {
           translateText();
         }
         catch (IOException e) {
           e.printStackTrace();
         }
         




###  Node.js 

  1. Install the Cloud Translation API Cloud Client Libraries:

     1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Cloud APIs** explorer.
     2. Expand **Cloud AI** and then click **Cloud Translation API**.
     3. To install the client library, click **NodeJS** and then click play_arrow **Run in terminal**.  

  2. Create an `app.js` file in your project.

  3. Open`app.js` and import the Translation client library at the beginning of the file:
         
         const {TranslationServiceClient} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)');
         

  4. Create a Translation API client and add variables for your project ID, location, and the text that you want to translate:
         
         // Instantiates a client
         const translationClient = new TranslationServiceClient();
         
         const projectId = 'PROJECT_ID';
         const location = 'global';
         const text = 'Hello, world!';
         

  5. Add the following `async` function, which detects the language of your `Hello, world!` text and translates the text to Spanish:
         
         async function translateText() {
             // Construct request
             const request = {
                 parent: `projects/PROJECT_ID/locations/LOCATION`,
                 contents: [text],
                 mimeType: 'text/plain', // mime types: text/plain, text/html
                 sourceLanguageCode: 'en',
                 targetLanguageCode: 'es',
             };
         
             // Run request
             const [response] = await translationClient.translateText(request);
         
             for (const translation of response.translations) {
                 console.log(`Translation: ${translation.translatedText}`);
             }
         }
         

  6. At the end of your `app.js` file, call `translateText()`:
         
         translateText();
         

  7. To run your application, open the command palette (press `Ctrl`/`Cmd` \+ `Shift` \+ `P`) and then run **Cloud Code: Run on Kubernetes**.

  8. After the application is deployed, view your running service by opening the URL displayed in the **webview**.




###  Python 

  1. Install the Cloud Translation API Cloud Client Libraries:

     1. Click ![](https://docs.cloud.google.com/static/code/images/cloud-code-icon.svg)**Cloud Code** and then expand the **Cloud APIs** explorer.
     2. Expand **Cloud AI** and then click **Cloud Translation API**.
     3. To install the client library, click **Python** and then click play_arrow **Run in terminal**.  
Note: If you're using a Linux-based operating system, including Chromebook, revise the command to use `pip3` instead of `pip`. If you're using a Mac, revise the command to use `pip3` and add the `--user` flag. 
  2. Create an `app.py` file in your project.

  3. In `app.py`, import the client library at the beginning of the file:
         
         from google.cloud import translate
         

  4. Add the `translate_text` function. This initializes a client to interact with Cloud Translation API.
         
         def translate_text(text="Hello, world!", project_id="PROJECT_ID"):
         
         client = translate.TranslationServiceClient()
         location = "global"
         parent = "projects/PROJECT_ID/locations/LOCATION"
         

  5. To translate text from English to Spanish and print the result, in your `translate_text` function, add the following call to the Cloud Translation API Cloud Client Libraries:
         
         response = client.translate_text(
             request={
                 "parent": parent,
                 "contents": [text],
                 "mime_type": "text/plain",
                 "source_language_code": "en-US",
                 "target_language_code": "es",
             }
         )
         
         for translation in response.translations:
             print("Translated text: {}".format(translation.translated_text))
         

  6. At the end of `app.py`, call `translate_text()`.
         
         translate_text()

  7. To run your application, open the command palette (press `Ctrl`/`Cmd` \+ `Shift` \+ `P`) and then run **Cloud Code: Run on Kubernetes**.

  8. After the application is deployed, view your running service by opening the URL displayed in the **webview**.




## Clean up

After you stop your application, all Kubernetes resources deployed during the run are deleted automatically.

To avoid incurring charges to your account for other resources used in this quickstart, be sure to delete the project or delete the cluster you created if you want to reuse the project.

To delete the cluster:

  1. In the Kubernetes Explorer, pause on your cluster name and then click open_in_new **Open in Google Cloud console**.
  2. Click **Delete** and then click **Delete**.



To delete your project (and associated resources, including any clusters):

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## Get Support

To send feedback, ask a question on [Stack Overflow](https://stackoverflow.com/questions/ask?tags=cloud-code-vscode). If you are a Google Cloud customer, you can file tickets through [standard Google Cloud support channels](https://cloud.google.com/support?e=48754805). 

## What's next

  * Learn more about the [Cloud Translation API](https://docs.cloud.google.com/translate/docs)
  * Learn more about the [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries)
  * Learn more about [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
