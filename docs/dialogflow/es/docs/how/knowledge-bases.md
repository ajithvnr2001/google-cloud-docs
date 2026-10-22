---
url: https://docs.cloud.google.com/dialogflow/es/docs/how/knowledge-bases/
title: Manage knowledge bases \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:21.022862+00:00
---

# Manage knowledge bases  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/how/knowledge-bases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Manage knowledge bases Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A _knowledge base_ represents a collection of _knowledge documents_ that you provide to Dialogflow. Your knowledge documents contain information that may be useful during conversations with end-users. Some Dialogflow features use knowledge bases when looking for a response to an end-user expression. This guide describes how to create and manage knowledge bases.

A knowledge base [is applied at the agent level](https://docs.cloud.google.com/dialogflow/es/docs/data-level).

## Before you begin

You should do the following before reading this guide:

  1. Read [Dialogflow basics](https://docs.cloud.google.com/dialogflow/docs/basics).
  2. Perform [setup steps](https://docs.cloud.google.com/dialogflow/docs/quick/setup).



## Create a knowledge base

The samples below show you how to use the Dialogflow Console, REST API (including command line), or client libraries to create a knowledge base. To use the API, call the `create` method on the [`KnowledgeBase`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#knowledgebases) type.

### Web UI

Use the Dialogflow Console to create a knowledge base: 

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com)
  2. Select an agent
  3. Click **Knowledge** on the left sidebar menu
  4. Click **Create Knowledge Base**
  5. Enter a knowledge base name
  6. Click **Save**



### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your GCP project ID
  * KNOWLEDGE_BASE_DISPLAY_NAME: desired knowledge base name



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2beta1/projects/PROJECT_ID/knowledgeBases

Request JSON body: 
    
    
    {
      "displayName": "KNOWLEDGE_BASE_DISPLAY_NAME"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dialogflow.googleapis.com/v2beta1/projects/PROJECT_ID/knowledgeBases"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dialogflow.googleapis.com/v2beta1/projects/PROJECT_ID/knowledgeBases" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/knowledgeBases/NDA4MTM4NzE2MjMwNDUxMjAwMA",
      "displayName": "KNOWLEDGE_BASE_DISPLAY_NAME"
    }
    

Take note of the value of the `name` field. This is the name of your new knowledge base. The path segment after `knowledgeBases` is your new knowledge base ID. Save this ID for requests below. 

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.dialogflow.v2.[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase.html);
    import com.google.cloud.dialogflow.v2.[KnowledgeBasesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesClient.html);
    import com.google.cloud.dialogflow.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.LocationName.html);
    import java.io.IOException;
    
    public class KnowledgeBaseManagement {
    
      public static void main(String[] args) throws [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html), IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "my-location";
    
        // Set display name of the new knowledge base
        String knowledgeBaseDisplayName = "my-knowledge-base-display-name";
    
        // Create a knowledge base
        createKnowledgeBase(projectId, location, knowledgeBaseDisplayName);
      }
    
      // Create a Knowledge base
      public static void createKnowledgeBase(String projectId, String location, String displayName)
          throws [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html), IOException {
        // Instantiates a client
        try ([KnowledgeBasesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesClient.html) knowledgeBasesClient = [KnowledgeBasesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesClient.html).create()) {
          [KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase.html) targetKnowledgeBase =
              [KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase.html).newBuilder().setDisplayName(displayName).build();
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.LocationName.html).of(projectId, location);
          [KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase.html) createdKnowledgeBase =
              knowledgeBasesClient.createKnowledgeBase(parent, targetKnowledgeBase);
          System.out.println("====================");
          System.out.format("Knowledgebase created:\n");
          System.out.format("Display Name: %s\n", createdKnowledgeBase.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase.html#com_google_cloud_dialogflow_v2_KnowledgeBase_getDisplayName__)());
          System.out.format("Name: %s\n", createdKnowledgeBase.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase.html#com_google_cloud_dialogflow_v2_KnowledgeBase_getName__)());
        }
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Dialogflow client library
    const dialogflow = require('[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)').v2beta1;
    
    // Instantiate a DialogFlow client.
    const client = new dialogflow.[KnowledgeBasesClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const projectId = 'ID of GCP project associated with your Dialogflow agent';
    // const displayName = `your knowledge base display name, e.g. myKnowledgeBase`;
    
    const formattedParent = 'projects/' + projectId;
    const knowledgeBase = {
      displayName: displayName,
    };
    const request = {
      parent: formattedParent,
      knowledgeBase: knowledgeBase,
    };
    
    const [result] = await client.createKnowledgeBase(request);
    console.log(`Name: ${result.name}`);
    console.log(`displayName: ${result.displayName}`);
    

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_knowledge_base(project_id, display_name):
        """Creates a Knowledge base.
    
        Args:
            project_id: The GCP project linked with the agent.
            display_name: The display name of the Knowledge base."""
        from google.cloud import dialogflow_v2beta1 as dialogflow
    
        client = dialogflow.KnowledgeBasesClient()
        project_path = client.common_project_path(project_id)
    
        knowledge_base = dialogflow.KnowledgeBase(display_name=display_name)
    
        response = client.create_knowledge_base(
            parent=project_path, knowledge_base=knowledge_base
        )
    
        print("Knowledge Base created:\n")
        print("Display Name: {}\n".format(response.display_name))
        print("Name: {}\n".format(response.name))
    
    

## Add a document to the knowledge base

Your new knowledge base currently has no documents, so you should add a document to it. See Supported content below for a description of all supported content options. You can use the [Cloud Storage FAQ](https://cloud.google.com/storage/docs/faq) document for this example.

**Note:** Knowledge documents are only parsed when explicitly creating or updating them. If your source content changes after creating a knowledge document, you need to update the knowledge document.

The samples below show you how to use the Dialogflow Console, REST API (including command line), or client libraries to create a knowledge document. To use the API, call the `create` method on the [`Document`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#documents) type.

### Web UI

Use the Dialogflow Console to create a knowledge document: 

  1. If you are not continuing from steps above, navigate to your knowledge base settings: 
     1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com)
     2. Select an agent
     3. Click **Knowledge** on the left sidebar menu
     4. Click your knowledge base name
  2. Click **New Document** or **Create the first one**
  3. Enter a document name
  4. Select **text/html** for **Mime Type**
  5. Select **FAQ** for **Knowledge Type**
  6. Select **URL** for **Data Source**
  7. Enter **https://cloud.google.com/storage/docs/faq** in the **URL** field
  8. Click **CREATE**



### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your GCP project ID
  * KNOWLEDGE_BASE_ID: your knowledge base ID returned from previous request
  * DOCUMENT_DISPLAY_NAME: desired knowledge document name



HTTP method and URL: 
    
    
    POST https://dialogflow.googleapis.com/v2beta1/projects/PROJECT_ID/knowledgeBases/KNOWLEDGE_BASE_ID/documents

Request JSON body: 
    
    
    {
      "displayName": "DOCUMENT_DISPLAY_NAME",
      "mimeType": "text/html",
      "knowledgeTypes": "FAQ",
      "contentUri": "https://cloud.google.com/storage/docs/faq"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dialogflow.googleapis.com/v2beta1/projects/PROJECT_ID/knowledgeBases/KNOWLEDGE_BASE_ID/documents"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dialogflow.googleapis.com/v2beta1/projects/PROJECT_ID/knowledgeBases/KNOWLEDGE_BASE_ID/documents" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/operations/**ks-add_document-MzA5NTY2MTc5Mzg2Mzc5NDY4OA** "
    }
    

The path segment after `operations` is your operation ID. 

### Java

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.dialogflow.v2.[CreateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateDocumentRequest.html);
    import com.google.cloud.dialogflow.v2.[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document.html);
    import com.google.cloud.dialogflow.v2.[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document.html).[KnowledgeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document.KnowledgeType.html);
    import com.google.cloud.dialogflow.v2.[DocumentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsClient.html);
    import com.google.cloud.dialogflow.v2.[KnowledgeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeOperationMetadata.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DocumentManagement {
    
      public static void createDocument(
          String knowledgeBaseName,
          String displayName,
          String mimeType,
          String knowledgeType,
          String contentUri)
          throws IOException, [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html), InterruptedException, ExecutionException, TimeoutException {
        // Instantiates a client
        try ([DocumentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsClient.html) documentsClient = [DocumentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsClient.html).create()) {
          [Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document.html) document =
              [Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document.html).newBuilder()
                  .setDisplayName(displayName)
                  .setContentUri(contentUri)
                  .setMimeType(mimeType)
                  .addKnowledgeTypes([KnowledgeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document.KnowledgeType.html).valueOf(knowledgeType))
                  .build();
          [CreateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateDocumentRequest.html) createDocumentRequest =
              [CreateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateDocumentRequest.html).newBuilder()
                  .setDocument(document)
                  .setParent(knowledgeBaseName)
                  .build();
          OperationFuture<Document, KnowledgeOperationMetadata> response =
              documentsClient.[createDocumentAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DocumentsClient.html#com_google_cloud_dialogflow_v2_DocumentsClient_createDocumentAsync__org_jspecify_annotations_Nullable_com_google_cloud_dialogflow_v2_KnowledgeBaseName_com_google_cloud_dialogflow_v2_Document_)(createDocumentRequest);
          [Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document.html) createdDocument = response.get(300, TimeUnit.SECONDS);
          System.out.format("Created Document:\n");
          System.out.format(" - Display Name: %s\n", createdDocument.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document.html#com_google_cloud_dialogflow_v2_Document_getDisplayName__)());
          System.out.format(" - Document Name: %s\n", createdDocument.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document.html#com_google_cloud_dialogflow_v2_Document_getName__)());
          System.out.format(" - MIME Type: %s\n", createdDocument.[getMimeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document.html#com_google_cloud_dialogflow_v2_Document_getMimeType__)());
          System.out.format(" - Knowledge Types:\n");
          for ([KnowledgeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document.KnowledgeType.html) knowledgeTypeId : document.[getKnowledgeTypesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document.html#com_google_cloud_dialogflow_v2_Document_getKnowledgeTypesList__)()) {
            System.out.format("  - %s \n", knowledgeTypeId.getValueDescriptor());
          }
          System.out.format(" - Source: %s \n", document.[getContentUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Document.html#com_google_cloud_dialogflow_v2_Document_getContentUri__)());
        }
      }
    }

### Node.js

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //   // Imports the Dialogflow client library
    //   const dialogflow = require('@google-cloud/dialogflow').v2beta1;
    
    //   // Instantiate a DialogFlow Documents client.
    //   const client = new dialogflow.DocumentsClient({
    //     projectId: projectId,
    //   });
    
    //   /**
    //    * TODO(developer): Uncomment the following lines before running the sample.
    //    */
    //   // const projectId = 'ID of GCP project associated with your Dialogflow agent';
    //   // const knowledgeBaseFullName = `the full path of your knowledge base, e.g my-Gcloud-project/myKnowledgeBase`;
    //   // const documentPath = `path of the document you'd like to add, e.g. https://dialogflow.com/docs/knowledge-connectors`;
    //   // const documentName = `displayed name of your document in knowledge base, e.g. myDoc`;
    //   // const knowledgeTypes = `The Knowledge type of the Document. e.g. FAQ`;
    //   // const mimeType = `The mime_type of the Document. e.g. text/csv, text/html,text/plain, text/pdf etc.`;
    
    //   const request = {
    //     parent: knowledgeBaseFullName,
    //     document: {
    //       knowledgeTypes: [knowledgeTypes],
    //       displayName: documentName,
    //       contentUri: documentPath,
    //       source: 'contentUri',
    //       mimeType: mimeType,
    //     },
    //   };
    
    //   const [operation] = await client.createDocument(request);
    //   const [response] = await operation.promise();
    
    //   console.log('Document created');
    //   console.log(`Content URI...${response.contentUri}`);
    //   console.log(`displayName...${response.displayName}`);
    //   console.log(`mimeType...${response.mimeType}`);
    //   console.log(`name...${response.name}`);
    //   console.log(`source...${response.source}`);
    

### Python

To authenticate to Dialogflow CX, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_document(
        project_id, knowledge_base_id, display_name, mime_type, knowledge_type, content_uri
    ):
        """Creates a Document.
    
        Args:
            project_id: The GCP project linked with the agent.
            knowledge_base_id: Id of the Knowledge base.
            display_name: The display name of the Document.
            mime_type: The mime_type of the Document. e.g. text/csv, text/html,
                text/plain, text/pdf etc.
            knowledge_type: The Knowledge type of the Document. e.g. FAQ,
                EXTRACTIVE_QA.
            content_uri: Uri of the document, e.g. gs://path/mydoc.csv,
                http://mypage.com/faq.html."""
        from google.cloud import dialogflow_v2beta1 as dialogflow
    
        client = dialogflow.DocumentsClient()
        knowledge_base_path = dialogflow.KnowledgeBasesClient.knowledge_base_path(
            project_id, knowledge_base_id
        )
    
        document = dialogflow.Document(
            display_name=display_name, mime_type=mime_type, content_uri=content_uri
        )
    
        document.knowledge_types.append(
            getattr(dialogflow.Document.KnowledgeType, knowledge_type)
        )
    
        response = client.create_document(parent=knowledge_base_path, document=document)
        print("Waiting for results...")
        document = response.result(timeout=120)
        print("Created Document:")
        print(" - Display Name: {}".format(document.display_name))
        print(" - Knowledge ID: {}".format(document.name))
        print(" - MIME Type: {}".format(document.mime_type))
        print(" - Knowledge Types:")
        for knowledge_type in document.knowledge_types:
            print("    - {}".format(KNOWLEDGE_TYPES[knowledge_type]))
        print(" - Source: {}\n".format(document.content_uri))
    
    

Creating a document is a long-running operation, so it may take a substantial amount of time to complete. You can poll the status of this operation to see if it has completed. Once completed, the operation contains the newly created document ID. Save this ID for future processing. For more information, see [Long-running operations](https://docs.cloud.google.com/dialogflow/docs/how/long-running-operations).

## Manage knowledge documents

### Update knowledge document content

If you update your content referenced by a knowledge document, your knowledge document may not automatically refresh. Your content is only automatically refreshed if it is provided as a public URL and you have checked the **Enable Automatic Reload** option for the document.

To manually refresh Cloud Storage or public URL document content, call the `reload` method on the [`Document`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#documents) type.

To manually refresh uploaded raw content, use the `delete` and `create` methods on the [`Document`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#documents) type to re-create your document.

### List knowledge documents

You can list all knowledge documents for your knowledge base. To use the API, call the `list` method on the [`Document`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#documents) type.

### Delete knowledge documents

You can delete knowledge documents for your knowledge base. To use the API, call the `delete` method on the [`Document`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#documents) type. If you do not have the document ID, you can list the documents as described above.

## Supported content

The following knowledge document types are supported:

  * **FAQ** : The document content contains question and answer pairs as either HTML or CSV. Typical FAQ HTML formats are parsed accurately, but unusual formats may fail to be parsed. CSV must have questions in the first column and answers in the second, with no header. Because of this explicit format, they are always parsed accurately.
  * **Extractive QA** : Documents for which unstructured text is extracted and used for question answering.



The following table shows the supported MIME types by _Knowledge Type_ and _Source_.

Knowledge Type \ Source | Uploaded file (Document.content) (_NOT_ recommended) | Uploaded file (Document.raw_content) (recommended) | File from Cloud Storage (Document.contentUri) | File from public URL (Document.contentUri)  
---|---|---|---|---  
FAQ | text/csv | text/csv | text/csv | text/html  
Extractive QA  | text/plain, text/html  | text/plain, text/html, application/pdf | text/plain, text/html, application/pdf | N/A   
  
Document content has the following known issues, limitations, and best practices:

General:

  * Files from public URLs must have been crawled by the Google search indexer, so that they exist in the search index. You can check this with the [Google Search Console](https://search.google.com/search-console). Note that the indexer does not keep your content fresh. You must explicitly update your knowledge document when the source content changes.
  * CSV files must use commas as delimiters.
  * Confidence scores are not yet calibrated between FAQs and Knowledge Base Articles, so if you use both FAQ and Knowledge Base Articles, the best result may not always be the highest.
  * Dialogflow removes HTML tags from content when creating responses. Because of this, it's best to avoid HTML tags and use plain text when possible.
  * Google Assistant responses have a 640 character limit per chat bubble, so long answers are truncated when integrating with Google Assistant.
  * The maximum document size is 50 MB.
  * When using Cloud Storage files, you should either use public URIs or private URIs that your user account or service account has access to.



Specific to FAQ:

  * CSV must have questions in the first column and answers in the second, with no header.
  * Use CSV whenever possible, because CSV is parsed most accurately.
  * Public HTML content with a single QA pair is not supported.
  * The number of QA pairs in one document should not exceed 2000.
  * Duplicate questions with different answers is not supported.
  * You can use any FAQ document; the FAQ parser is capable of handling most FAQ formats.



Specific to Extractive QA:

  * Extractive QA is currently experimental. It is based on similar technologies that have been tried and tested at Google in products like Search and Assistant. [Send us your feedback](https://docs.cloud.google.com/dialogflow/docs/support) on how well it works for Dialogflow.
  * Content with dense text works best. Avoid content with many single sentence paragraphs.
  * Tables and lists are not supported.
  * The number of paragraphs in one document should not exceed 2000.
  * If an article is long (> 1000 words), try to break it down into multiple, smaller articles. If the article covers multiple issues, it can be broken into shorter articles covering the individual issues. If the article only covers one issue, then focus the article on the issue description and keep the issue resolution short.
  * Ideally, only the core content of an article should be provided (issue description and resolution). Additional content like author name, modification history, related links, and ads are not important.
  * Try to include a description for the issues an article can help with and/or sample queries that this article can answer.



## Using Cloud Storage

If your content is not public, storing your content in [Cloud Storage](https://docs.cloud.google.com/storage/docs) is the recommended option. When creating knowledge documents, you provide the URLs for your Cloud Storage objects.

### Creating Cloud Storage buckets and objects

When creating the Cloud Storage bucket:

  * Be sure that you have selected the GCP project you use for Dialogflow.
  * Ensure that the user account or service account you normally use to access the Dialogflow API has [read permissions to the bucket objects](https://docs.cloud.google.com/storage/docs/access-control).
  * Use the [Standard Storage class](https://docs.cloud.google.com/storage/docs/storage-classes#standard).
  * Set the [bucket location](https://docs.cloud.google.com/storage/docs/locations) to a location nearest to your location. You will need the location ID (for example, `us-west1`) for some API calls, so take note of your choice.



Follow the [Cloud Storage quickstart](https://docs.cloud.google.com/storage/docs/quickstart-console) instructions to create a bucket and upload files.

### Supplying a Cloud Storage object to a knowledge base document

To supply your content:

  * Create a knowledge base as described above.
  * Create a knowledge document as described above. When calling the `create` method on the [`Document`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#documents) type, set the `contentUri` field to the URL of your Cloud Storage document. The format of this URL is `gs://bucket-name/object-name`.



[ Previous arrow_back  Manage intents with the API  ](https://docs.cloud.google.com/dialogflow/es/docs/how/manage-intents)

[ Next Update data with a FieldMask  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/how/field-mask)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
