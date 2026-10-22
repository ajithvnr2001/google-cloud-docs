---
url: https://docs.cloud.google.com/artifact-analysis/docs/create-notes-occurrences/
title: Create custom notes and occurrences \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:08.367533+00:00
---

# Create custom notes and occurrences  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/create-notes-occurrences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Create custom notes and occurrences Stay organized with collections  Save and categorize content based on your preferences. 

You can choose to provide your own metadata to Artifact Analysis to satisfy a specific business need. For example, an organization that provides security management for their customers' Docker containers can use Artifact Analysis to store and retrieve security-related metadata for those images.

**Note:** You are not required to provide your own metadata to use Artifact Analysis.

The following steps show how to provide attestation metadata for your images using the Artifact Analysis API. You can use the same instructions to store and retrieve any [kind of metadata](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/NoteKind) that Artifact Analysis supports.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Enable the Container Analysis API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=containeranalysis.googleapis.com&redirect=https%3A//cloud.google.com%7B%7Bdynamic_data.request.path%7D%7D)

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. Enable the Container Analysis API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=containeranalysis.googleapis.com&redirect=https%3A//cloud.google.com%7B%7Bdynamic_data.request.path%7D%7D)

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Learn [how to set up access control](https://docs.cloud.google.com/artifact-analysis/docs/ca-access-control) for metadata in your project. Skip this step if you only consume metadata from occurrences created by Artifact Analysis container scanning.



## Create notes and occurrences for projects

This section explains how you can create notes and occurrences. For this example, you will be using the `ATTESTATION` kind.

As a provider, you will create a note in your project for each attestation, and you will create an occurrence in your customer's project for an occurrence of that attestation.

### Create notes

Use the following steps to create a note and give it a note ID.

**Note:** Your note ID can't exceed 100 characters.

###  API 

  1. Create a file named `note.json` with attestation description and details. The following code shows an example `note.json` file:
         
         {
           "shortDescription": "A brief Description of the note",
           "longDescription": "A longer description of the note",
           "kind": "ATTESTATION",
           "attestation": {
             "hint": {
               "humanReadableName": "my-attestation-authority"
             }
           }
         }
         

See the [notes API documentation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.notes) for more information about the notes JSON representation.

  2. Run the following curl command to create a note:
         
         curl -v -H "Content-Type: application/json" -H \
           "Authorization: Bearer $(gcloud auth print-access-token)" \
           https://containeranalysis.googleapis.com/v1/projects/PROVIDER_PROJECT_ID/notes?note_id=NOTE_ID -d @note.json
         

Where:

     * PROVIDER_PROJECT_ID is your project ID.
     * NOTE_ID specifies an identifier for your note. Use a string with a maximum length of 100 characters.



###  Java 

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/overview).

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.cloud.devtools.containeranalysis.v1.[ContainerAnalysisClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/com.google.cloud.devtools.containeranalysis.v1.ContainerAnalysisClient.html);
    import io.grafeas.v1.[GrafeasClient](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.GrafeasClient.html);
    import io.grafeas.v1.[Note](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Note.html);
    import io.grafeas.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.ProjectName.html);
    import io.grafeas.v1.[Version](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Version.html);
    import io.grafeas.v1.[AttestationNote](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.AttestationNote.html);
    import java.io.IOException;
    import java.lang.InterruptedException;
    
    public class CreateNote {
    
      // Creates and returns a new Note
      public static [Note](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Note.html) createNote(String noteId, String projectId)
          throws IOException, InterruptedException {
        // String noteId = "my-note";
        // String projectId = "my-project-id";
        final String projectName = [ProjectName](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.ProjectName.html).format(projectId);
    
        [Note](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Note.html) newNote =
            [Note](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Note.html).newBuilder()
                // Associate the Note with the metadata type
                // https://docs.cloud.google.com/artifact-registry/docs/analysis
                // Here, we use the type "attestation"
                .setAttestation(
                    [AttestationNote](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.AttestationNote.html).newBuilder()
                        .setHint(
                            [AttestationNote](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.AttestationNote.html).Hint.newBuilder()
                                .setHumanReadableName("my-attestation-authority")))
                .build();
    
        // Initialize client that will be used to send requests. After completing all of your requests,
        // call the "close" method on the client to safely clean up any remaining background resources.
        [GrafeasClient](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.GrafeasClient.html) client = [ContainerAnalysisClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/com.google.cloud.devtools.containeranalysis.v1.ContainerAnalysisClient.html).create().[getGrafeasClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/com.google.cloud.devtools.containeranalysis.v1.ContainerAnalysisClient.html#com_google_cloud_devtools_containeranalysis_v1_ContainerAnalysisClient_getGrafeasClient__)();
        [Note](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Note.html) result = client.[createNote](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.GrafeasClient.html#io_grafeas_v1_GrafeasClient_createNote__org_jspecify_annotations_Nullable_io_grafeas_v1_ProjectName_java_lang_String_io_grafeas_v1_Note_)(projectName, noteId, newNote);
        return result;
      }
    }
    

###  Go 

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/containeranalysis/apiv1).

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import (
      "context"
      "fmt"
    
      containeranalysis "cloud.google.com/go/containeranalysis/apiv1"
      grafeaspb "google.golang.org/genproto/googleapis/grafeas/v1"
    )
    
    // createNote creates and returns a new attestation Note.
    func createNote(noteID, projectID string) (*grafeaspb.[Note](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1beta1/grafeas/grafeaspb.html#cloud_google_com_go_containeranalysis_apiv1beta1_grafeas_grafeaspb_Note), error) {
      ctx := context.Background()
      client, err := containeranalysis.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1.html#cloud_google_com_go_containeranalysis_apiv1_Client_NewClient)(ctx)
      if err != nil {
        return nil, fmt.Errorf("NewClient: %w", err)
      }
      defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1.html#cloud_google_com_go_containeranalysis_apiv1_Client_Close)()
    
      projectName := fmt.Sprintf("projects/%s", projectID)
    
      req := &grafeaspb.[CreateNoteRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1beta1/grafeas/grafeaspb.html#cloud_google_com_go_containeranalysis_apiv1beta1_grafeas_grafeaspb_CreateNoteRequest){
        Parent: projectName,
        NoteId: noteID,
        Note: &grafeaspb.[Note](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1beta1/grafeas/grafeaspb.html#cloud_google_com_go_containeranalysis_apiv1beta1_grafeas_grafeaspb_Note){
          Type: &grafeaspb.Note_Attestation{
            Attestation: &grafeaspb.AttestationNote{
              Hint: &grafeaspb.AttestationNote_Hint{
                HumanReadableName: "my-attestation-authority",
              },
            },
          },
        },
      }
    
      return client.[GetGrafeasClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1.html#cloud_google_com_go_containeranalysis_apiv1_Client_GetGrafeasClient)().CreateNote(ctx, req)
    }
    

###  Node.js 

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Node.js API reference documentation](https://googleapis.dev/nodejs/containeranalysis/latest/index.html).

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    /**
    * TODO(developer): Uncomment these variables before running the sample
    */
    // const projectId = 'your-project-id', // Your Google Cloud Project ID
    // const noteId = 'my-note-id' // Id of the note
    
    // Import the library and create a client
    const {ContainerAnalysisClient} = require('[@google-cloud/containeranalysis](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)');
    const client = new [ContainerAnalysisClient](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)();
    
    // Construct request
    // Associate the Note with a metadata type
    // https://docs.cloud.google.com/artifact-registry/docs/analysis
    // Here, we use the type "attestation"
    const formattedParent = client.[getGrafeasClient](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/v1.containeranalysisclient.html)().[projectPath](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/v1.containeranalysisclient.html)(projectId);
    
    // Creates and returns a new Note
    const [note] = await client.[getGrafeasClient](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/v1.containeranalysisclient.html)().createNote({
      parent: formattedParent,
      noteId: noteId,
      note: {
        attestation: {
          hint: {
            humanReadableName: 'my-attestation-authority',
          },
        },
      },
    });
    
    console.log(`Note ${note.name} created.`);
    

###  Ruby 

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis/latest).

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    # note_id = "A user-specified identifier for the note"
    # project_id = "Your Google Cloud project ID"
    
    require "google/cloud/container_analysis"
    
    # Initialize the client
    client = Google::Cloud::[ContainerAnalysis](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis.html).[container_analysis](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis/latest/Google-Cloud-ContainerAnalysis.html).[grafeas_client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis-V1-ContainerAnalysis-Client.html)
    
    parent = client.[project_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis-V1-ContainerAnalysis-Paths.html) project: project_id
    note = {
      attestation: {
        hint: {
          human_readable_name: "attestation-authority"
        }
      }
    }
    response = client.create_note parent: parent, note_id: note_id, note: note
    puts response.[name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis-V1-ExportSBOMRequest.html)
    

###  Python 

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/containeranalysis/latest).

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    from google.cloud.devtools import containeranalysis_v1
    from grafeas.grafeas_v1 import types, Version
    
    def create_note(note_id: str, project_id: str) -> types.grafeas.Note:
        """Creates and returns a new attestation note."""
        # note_id = 'my-note'
        # project_id = 'my-gcp-project'
    
        client = containeranalysis_v1.ContainerAnalysisClient()
        grafeas_client = client.get_grafeas_client()
        project_name = f"projects/{project_id}"
        note = {
          "attestation": {
            "hint": {
              "human_readable_name": "attestation-authority",
            }
          }
        }
        response = grafeas_client.create_note(
            parent=project_name, note_id=note_id, note=note
        )
        return response
    

### Create occurrences for the notes

To create occurrences for a note:

###  API 

  1. Create a file named `occurrence.json` with attestation description and details. The following code shows an example `occurrence.json` file:
         
         {
           "resourceUri": "your-resource-uri-here",
           "noteName": "projects/your-note-project/notes/your-note-id",
           "kind": "ATTESTATION",
           "attestation": {
             "serializedPayload": "eW91ci1wYXlsb2FkLWhlcmU=",
             "signatures": [
               {
                 "publicKeyId": "your-key-id-here",
                 "signature": "eW91ci1zaWduYXR1cmUtaGVyZQ=="
               }
             ]
           }
         }
         

See the [notes API documentation](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.notes) for more information about the notes JSON representation.

  2. Run the following curl command to create an occurrence:
         
         curl -v -H "Content-Type: application/json" -H \
           "Authorization: Bearer $(gcloud auth print-access-token)" \
           https://containeranalysis.googleapis.com/v1/projects/PROVIDER_PROJECT_ID/occurrences/ -d @occurrence.json
         

Where:

     * PROVIDER_PROJECT_ID is your project ID.
     * NOTE_ID specifies an identifier for your note. Use a string with a maximum length of 100 characters.



###  Java 

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/overview).

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import com.google.cloud.devtools.containeranalysis.v1.[ContainerAnalysisClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/com.google.cloud.devtools.containeranalysis.v1.ContainerAnalysisClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import io.grafeas.v1.[AttestationOccurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.AttestationOccurrence.html);
    import io.grafeas.v1.[GrafeasClient](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.GrafeasClient.html);
    import io.grafeas.v1.[NoteName](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.NoteName.html);
    import io.grafeas.v1.[Occurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Occurrence.html);
    import io.grafeas.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.ProjectName.html);
    import io.grafeas.v1.[Signature](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Signature.html);
    import java.io.IOException;
    
    public class CreateOccurrence {
      // Creates and returns a new attestation Occurrence associated with an existing Note
      public static [Occurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Occurrence.html) createOccurrence(
          String resourceUrl, String noteId, String occProjectId, String noteProjectId)
          throws IOException {
        // String resourceUrl = "https://gcr.io/project/image@sha256:123";
        // String noteId = "my-note";
        // String occProjectId = "my-project-id";
        // String noteProjectId = "my-project-id";
        final [NoteName](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.NoteName.html) noteName = [NoteName](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.NoteName.html).of(noteProjectId, noteId);
        final String occProjectName = [ProjectName](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.ProjectName.html).format(occProjectId);
    
        [Occurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Occurrence.html) newOcc =
            [Occurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Occurrence.html).newBuilder()
                .setNoteName(noteName.[toString](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.NoteName.html#io_grafeas_v1_NoteName_toString__)())
                .setResourceUri(resourceUrl)
                .setAttestation(
                    [AttestationOccurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.AttestationOccurrence.html).newBuilder()
                        .[setSerializedPayload](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.AttestationOccurrence.Builder.html#io_grafeas_v1_AttestationOccurrence_Builder_setSerializedPayload_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)("your-payload-here", "UTF-8"))
                        .addSignatures(
                            [Signature](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Signature.html).newBuilder()
                                .[setPublicKeyId](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Signature.Builder.html#io_grafeas_v1_Signature_Builder_setPublicKeyId_java_lang_String_)("your-key-id-here")
                                .[setSignature](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Signature.Builder.html#io_grafeas_v1_Signature_Builder_setSignature_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)("your-signature-here", "UTF-8"))))
                .build();
    
        // Initialize client that will be used to send requests. After completing all of your requests,
        // call the "close" method on the client to safely clean up any remaining background
        // resources.
        [GrafeasClient](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.GrafeasClient.html) client = [ContainerAnalysisClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/com.google.cloud.devtools.containeranalysis.v1.ContainerAnalysisClient.html).create().[getGrafeasClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/com.google.cloud.devtools.containeranalysis.v1.ContainerAnalysisClient.html#com_google_cloud_devtools_containeranalysis_v1_ContainerAnalysisClient_getGrafeasClient__)();
        [Occurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Occurrence.html) result = client.[createOccurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.GrafeasClient.html#io_grafeas_v1_GrafeasClient_createOccurrence__org_jspecify_annotations_Nullable_io_grafeas_v1_ProjectName_io_grafeas_v1_Occurrence_)(occProjectName, newOcc);
        return result;
      }
    }
    

###  Go 

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/containeranalysis/apiv1).

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import (
      "context"
      "fmt"
    
      containeranalysis "cloud.google.com/go/containeranalysis/apiv1"
      grafeaspb "google.golang.org/genproto/googleapis/grafeas/v1"
    )
    
    // createsOccurrence creates and returns a new Occurrence of a previously created attestation note.
      // Use this style of URL when you use Google Artifact Registry.
      // resourceURL := "https://LOCATION-docker.pkg.dev/my-project/my-repo/my-image"
      // noteID := "my-note"
      ctx := context.Background()
      client, err := containeranalysis.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1.html#cloud_google_com_go_containeranalysis_apiv1_Client_NewClient)(ctx)
      if err != nil {
        return nil, fmt.Errorf("NewClient: %w", err)
      }
      defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1.html#cloud_google_com_go_containeranalysis_apiv1_Client_Close)()
    
      req := &grafeaspb.[CreateOccurrenceRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1beta1/grafeas/grafeaspb.html#cloud_google_com_go_containeranalysis_apiv1beta1_grafeas_grafeaspb_CreateOccurrenceRequest){
        Parent: fmt.Sprintf("projects/%s", occProjectID),
        Occurrence: &grafeaspb.[Occurrence](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1beta1/grafeas/grafeaspb.html#cloud_google_com_go_containeranalysis_apiv1beta1_grafeas_grafeaspb_Occurrence){
          NoteName: fmt.Sprintf("projects/%s/notes/%s", noteProjectID, noteID),
          // Attach the occurrence to the associated resource uri.
          ResourceUri: resourceURL,
          // Details about the attestation can be added here.
          Details: &grafeaspb.[Occurrence_Attestation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1beta1/grafeas/grafeaspb.html#cloud_google_com_go_containeranalysis_apiv1beta1_grafeas_grafeaspb_Occurrence_Attestation){
            Attestation: &grafeaspb.AttestationOccurrence{
              SerializedPayload: []byte("..."),
              Signatures: []*grafeaspb.Signature{
                {
                  PublicKeyId: "...",
                  Signature:   []byte("..."),
                },
              },
            },
          },
        },
      }
      return client.[GetGrafeasClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1.html#cloud_google_com_go_containeranalysis_apiv1_Client_GetGrafeasClient)().CreateOccurrence(ctx, req)
    }
    

###  Node.js 

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Node.js API reference documentation](https://googleapis.dev/nodejs/containeranalysis/latest/index.html).

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample
     */
    // const noteProjectId = 'your-project-id', // Your Google Cloud Project ID
    // const noteId = 'my-note-id', // Id of the note
    // const occurrenceProjectId = 'your-project-id', // The Google Cloud Project ID of the occurrence
    // If you are using Google Artifact Registry
    // const imageUrl = 'https://LOCATION-docker.pkg.dev/my-project/my-repo/my-image:123' // Image to attach metadata to
    
    // Import the library and create a client
    const {ContainerAnalysisClient} = require('[@google-cloud/containeranalysis](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)');
    const client = new [ContainerAnalysisClient](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)();
    
    // Construct request
    const formattedParent = client
    .[getGrafeasClient](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/v1.containeranalysisclient.html)()
    .[projectPath](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/v1.containeranalysisclient.html)(occurrenceProjectId);
    const formattedNote = client
    .[getGrafeasClient](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/v1.containeranalysisclient.html)()
    .[notePath](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/v1.containeranalysisclient.html)(noteProjectId, noteId);
    
    // Creates and returns a new Occurrence associated with an existing Note
    const [occurrence] = await client.[getGrafeasClient](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/v1.containeranalysisclient.html)().createOccurrence({
    parent: formattedParent,
    occurrence: {
      noteName: formattedNote,
      resourceUri: imageUrl,
      attestation: {
        serializedPayload: Buffer.from('your-payload-here').toString('base64'),
        signatures: [
          {
            publicKeyId: 'your-key-id-here',
            signature: Buffer.from('your-signature-here').toString('base64'),
          },
        ],
      },
    },
    });
    console.log(`Occurrence created ${occurrence.name}.`);
    return occurrence;
    

###  Ruby 

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Ruby API reference documentation](https://cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest).

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    # note_id    = "A user-specified identifier for the note"
    # project_id = "Your Google Cloud project ID"
    # note_project = "The project that contains the note"
    # occurrence_project = "The project that contains the occurrence"
    
    require "google/cloud/container_analysis"
    require "base64"
    
    # Initialize the client
    client = Google::Cloud::[ContainerAnalysis](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis.html).[container_analysis](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis/latest/Google-Cloud-ContainerAnalysis.html).[grafeas_client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis-V1-ContainerAnalysis-Client.html)
    note_path = client.note_path project: note_project, note: note_id
    project_path = client.[project_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis-V1-ContainerAnalysis-Paths.html) project: occurrence_project
    
    occurrence = {
      note_name:    note_path,
      resource_uri: resource_url,
      attestation:  {
        serialized_payload: Base64.encode64("your-payload-here"),
        signatures:         [
          {
            public_key_id: "your-key-id-here",
            signature:     Base64.encode64("your-signature-here")
          }
        ]
      }
    }
    
    response = client.create_occurrence parent: project_path, occurrence: occurrence
    puts response.[name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis-V1-ExportSBOMRequest.html)
    

###  Python 

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/containeranalysis/latest).

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).
    
    
    import base64
    from google.cloud.devtools import containeranalysis_v1
    from grafeas.grafeas_v1 import types
    
    def create_occurrence(
        resource_url: str, note_id: str, occurrence_project: str, note_project: str
    ) -> types.grafeas.Occurrence:
        """Creates and returns a new occurrence of a previously
        created attestation note."""
        # note_id = 'my-note'
        # project_id = 'my-gcp-project'
    
        client = containeranalysis_v1.ContainerAnalysisClient()
        grafeas_client = client.get_grafeas_client()
        formatted_note = f"projects/{note_project}/notes/{note_id}"
        formatted_project = f"projects/{occurrence_project}"
    
        occurrence = {
            "note_name": formatted_note,
            "resource_uri": resource_url,
            "attestation": {
                "serialized_payload": base64.b64encode(b"your-payload-here").decode("utf-8"),
                "signatures": [
                    {
                        "public_key_id": "your-key-id-here",
                        "signature": base64.b64encode(b"your-signature-here").decode("utf-8"),
                    }
                ],
            },
        }
    
        return grafeas_client.create_occurrence(
            parent=formatted_project, occurrence=occurrence
        )
    

## Get all occurrences for a specific note

You can view all occurrences of a specific attestation across your customer's projects using [`notes.occurrences.list()`](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.notes.occurrences/list).

### API

To list all the occurrences for a note, send a GET request as follows:
    
    
    GET https://containeranalysis.googleapis.com/v1/projects/PROJECT_ID/notes/NOTE_ID/occurrences
    

Refer to the [`projects.notes.occurrences.list`](https://docs.cloud.google.com/artifact-analysis/docs/reference/rest/v1/projects.notes.occurrences/list) API endpoint for complete details.

### Java

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/overview). 

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import static java.lang.Thread.sleep;
    
    import com.google.cloud.devtools.containeranalysis.v1.[ContainerAnalysisClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/com.google.cloud.devtools.containeranalysis.v1.ContainerAnalysisClient.html);
    import io.grafeas.v1.[GrafeasClient](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.GrafeasClient.html);
    import io.grafeas.v1.[ListNoteOccurrencesRequest](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.ListNoteOccurrencesRequest.html);
    import io.grafeas.v1.[NoteName](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.NoteName.html);
    import io.grafeas.v1.[Occurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Occurrence.html);
    import java.io.IOException;
    import java.lang.InterruptedException;
    
    public class OccurrencesForNote {  
      // Retrieves all the Occurrences associated with a specified Note
      // Here, all Occurrences are printed and counted
      public static int getOccurrencesForNote(String noteId, String projectId) 
          throws IOException, InterruptedException {
        // String noteId = "my-note";
        // String projectId = "my-project-id";
        final [NoteName](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.NoteName.html) noteName = [NoteName](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.NoteName.html).of(projectId, noteId);
    
        [ListNoteOccurrencesRequest](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.ListNoteOccurrencesRequest.html) request = [ListNoteOccurrencesRequest](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.ListNoteOccurrencesRequest.html).newBuilder()
                                                                       .setName(noteName.[toString](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.NoteName.html#io_grafeas_v1_NoteName_toString__)())
                                                                       .build();
    
        // Initialize client that will be used to send requests. After completing all of your requests, 
        // call the "close" method on the client to safely clean up any remaining background resources.
        [GrafeasClient](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.GrafeasClient.html) client = [ContainerAnalysisClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/com.google.cloud.devtools.containeranalysis.v1.ContainerAnalysisClient.html).create().[getGrafeasClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-containeranalysis/latest/com.google.cloud.devtools.containeranalysis.v1.ContainerAnalysisClient.html#com_google_cloud_devtools_containeranalysis_v1_ContainerAnalysisClient_getGrafeasClient__)();
        int i = 0;
        for ([Occurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Occurrence.html) o : client.[listNoteOccurrences](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.GrafeasClient.html#io_grafeas_v1_GrafeasClient_listNoteOccurrences__org_jspecify_annotations_Nullable_io_grafeas_v1_NoteName_java_lang_String_)(request).iterateAll()) {
          // Write custom code to process each Occurrence here
          System.out.println(o.getName());
          i = i + 1;
        }
        return i;
      }
    }

### Go

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Go API reference documentation](https://godoc.org/cloud.google.com/go/containeranalysis/apiv1). 

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	containeranalysis "cloud.google.com/go/containeranalysis/apiv1"
    	"google.golang.org/api/iterator"
    	grafeaspb "google.golang.org/genproto/googleapis/grafeas/v1"
    )
    
    // getOccurrencesForNote retrieves all the Occurrences associated with a specified Note.
    // Here, all Occurrences are printed and counted.
    func getOccurrencesForNote(w io.Writer, noteID, projectID string) (int, error) {
    	// noteID := fmt.Sprintf("my-note")
    	ctx := context.Background()
    	client, err := containeranalysis.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1.html#cloud_google_com_go_containeranalysis_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return -1, fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1.html#cloud_google_com_go_containeranalysis_apiv1_Client_Close)()
    
    	req := &grafeaspb.[ListNoteOccurrencesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1beta1/grafeas/grafeaspb.html#cloud_google_com_go_containeranalysis_apiv1beta1_grafeas_grafeaspb_ListNoteOccurrencesRequest){
    		Name: fmt.Sprintf("projects/%s/notes/%s", projectID, noteID),
    	}
    	it := client.[GetGrafeasClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/containeranalysis/latest/apiv1.html#cloud_google_com_go_containeranalysis_apiv1_Client_GetGrafeasClient)().ListNoteOccurrences(ctx, req)
    	count := 0
    	for {
    		occ, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return -1, fmt.Errorf("occurrence iteration error: %w", err)
    		}
    		// Write custom code to process each Occurrence here.
    		fmt.Fprintln(w, occ)
    		count = count + 1
    	}
    	return count, nil
    }
    

### Node.js

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Node.js API reference documentation](https://googleapis.dev/nodejs/containeranalysis/latest/index.html). 

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample
     */
    // const projectId = 'your-project-id', // Your GCP Project ID
    // const noteId = 'my-note-id' // Id of the note
    
    // Import the library and create a client
    const {ContainerAnalysisClient} = require('[@google-cloud/containeranalysis](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)');
    const client = new [ContainerAnalysisClient](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/overview.html)();
    
    // Get path to Note
    const formattedNote = client.[notePath](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/v1.containeranalysisclient.html)(projectId, noteId);
    
    // Retrieves all the Occurrences associated with a specified Note
    const [occurrences] = await client.[getGrafeasClient](https://docs.cloud.google.com/nodejs/docs/reference/containeranalysis/latest/containeranalysis/v1.containeranalysisclient.html)().listNoteOccurrences({
      name: formattedNote,
    });
    
    if (occurrences.length) {
      console.log('Occurrences:');
      occurrences.forEach(occurrence => {
        console.log(`${occurrence.name}:`);
      });
    } else {
      console.log('No occurrences found.');
    }

### Ruby

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis/latest). 

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
      # note_id    = "The identifier for the note to query"
      # project_id = "The Google Cloud project ID of the occurrences to retrieve"
    
      require "google/cloud/container_analysis"
    
      # Initialize the client
      client = Google::Cloud::[ContainerAnalysis](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis.html).[container_analysis](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis/latest/Google-Cloud-ContainerAnalysis.html).[grafeas_client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis-V1-ContainerAnalysis-Client.html)
    
      name = client.note_path project: project_id, note: note_id
      count = 0
      client.list_note_occurrences(name: name).each do |occurrence|
        # Process occurrence here
        puts occurrence
        count += 1
      end
      puts "Found #{count} occurrences"
      count
    end
    
    def get_discovery_info resource_url:, project_id:
      # resource_url = "The URL of the resource associated with the occurrence."
      #                # e.g. https://gcr.io/project/image@sha256:123
      # project_id   = "The Google Cloud project ID of the occurrences to retrieve"
    
      require "google/cloud/container_analysis"
    
      # Initialize the client
      client = Google::Cloud::[ContainerAnalysis](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis.html).[container_analysis](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis/latest/Google-Cloud-ContainerAnalysis.html).[grafeas_client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis-V1-ContainerAnalysis-Client.html)
    
      parent = client.project_path project: project_id
      filter = "kind = \"DISCOVERY\" AND resourceUrl = \"#{resource_url}\""
      client.list_occurrences(parent: parent, filter: filter).each do |occurrence|
        # Process discovery occurrence here
        puts occurrence
      end
    end
    
    def occurrence_pubsub subscription_id:, timeout_seconds:, project_id:
      # subscription_id = "A user-specified identifier for the new subscription"
      # timeout_seconds = "The number of seconds to listen for new Pub/Sub messages"
      # project_id      = "Your Google Cloud project ID"
    
      require "google/cloud/pubsub"
    
      pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) project_id: project_id
      subscription_admin = pubsub.[subscription_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
      subscription = subscription_admin.create_subscription \
        name: pubsub.subscription_path(subscription_id),
        topic: pubsub.topic_path("container-analysis-occurrences-v1")
    
      subscriber = pubsub.[subscriber](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) subscription.name
      count = 0
      listener = subscriber.[listen](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Subscriber.html) do |received_message|
        count += 1
        # Process incoming occurrence here
        puts "Message #{count}: #{received_message.data}"
        received_message.[acknowledge!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-ReceivedMessage.html)
      end
    
      listener.[start](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-MessageListener.html)
      # Wait for incoming occurrences
      sleep timeout_seconds
      listener.stop.wait!
    
      subscription_admin.delete_subscription subscription: subscription.name
    
      # Print and return the total number of Pub/Sub messages received
      puts "Total Messages Received: #{count}"
      count
    end
    
    # rubocop:disable Metrics/MethodLength
    
    def poll_discovery_finished resource_url:, timeout_seconds:, project_id:
      # resource_url    = "The URL of the resource associated with the occurrence."
      #                   # e.g. https://gcr.io/project/image@sha256:123
      # timeout_seconds = "The number of seconds to wait for the discovery occurrence"
      # project_id      = "Your Google Cloud project ID"
    
      require "google/cloud/container_analysis"
    
      deadline = Time.now + timeout_seconds
    
      # Initialize the client
      client = Google::Cloud::[ContainerAnalysis](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis.html).[container_analysis](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis/latest/Google-Cloud-ContainerAnalysis.html).[grafeas_client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis-V1-ContainerAnalysis-Client.html)
      parent = client.project_path project: project_id
    
      # Find the discovery occurrence using a filter string
      discovery_occurrence = nil
      while discovery_occurrence.nil?
        begin
          filter = "resourceUrl=\"#{resource_url}\" " \
                   'AND noteProjectId="goog-analysis" ' \
                   'AND noteId="PACKAGE_VULNERABILITY"'
          # The above filter isn't testable, since it looks for occurrences in a
          # locked down project. Fall back to a more permissive filter for testing
          filter = "kind = \"DISCOVERY\" AND resourceUrl = \"#{resource_url}\""
          # Only the discovery occurrence should be returned for the given filter
          discovery_occurrence = client.list_occurrences(parent: parent, filter: filter).first
        rescue StandardError # If there is an error, keep trying until the deadline
          puts "discovery occurrence not yet found"
        ensure
          # check for timeout
          sleep 1
          raise "Timeout while retrieving discovery occurrence." if Time.now > deadline
        end
      end
    
      # Wait for the discovery occurrence to enter a terminal state
      status = Grafeas::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis-V1.html)::DiscoveryOccurrence::AnalysisStatus::PENDING
      until [:FINISHED_SUCCESS, :FINISHED_FAILED, :FINISHED_UNSUPPORTED].include? status
        # Update occurrence
        begin
          updated = client.get_occurrence name: discovery_occurrence.name
          status = updated.discovery.analysis_status
        rescue StandardError # If there is an error, keep trying until the deadline
          puts "discovery occurrence not yet in terminal state"
        ensure
          # check for timeout
          sleep 1
          raise "Timeout while retrieving discovery occurrence." if Time.now > deadline
        end
      end
      puts "Found discovery occurrence #{updated.name}."
      puts "Status: #{updated.discovery.analysis_status}"
      updated
    end
    
    # rubocop:enable Metrics/MethodLength
    
    def find_vulnerabilities_for_image resource_url:, project_id:
      # resource_url = "The URL of the resource associated with the occurrence
      #                e.g. https://gcr.io/project/image@sha256:123"
      # project_id   = "The Google Cloud project ID of the vulnerabilities to find"
    
      require "google/cloud/container_analysis"
    
      # Initialize the client
      client = Google::Cloud::[ContainerAnalysis](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis.html).[container_analysis](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis/latest/Google-Cloud-ContainerAnalysis.html).[grafeas_client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis-V1-ContainerAnalysis-Client.html)
    
      parent = client.project_path project: project_id
      filter = "resourceUrl = \"#{resource_url}\" AND kind = \"VULNERABILITY\""
      client.list_occurrences parent: parent, filter: filter
    end
    
    def find_high_severity_vulnerabilities_for_image resource_url:, project_id:
      # resource_url       = "The URL of the resource associated with the occurrence."
      #                      # If you are using Google Container Registry
      #                      # e.g. https://gcr.io/project/repo/image@sha256:123
      #                      # If you are using Google Artifact Registry
      #                      # e.g. https://LOCATION-docker.pkg.dev/project/repo/image@sha256:123
      # project_id   = "The Google Cloud project ID of the vulnerabilities to find"
    
      require "google/cloud/container_analysis"
    
      # Initialize the client
      client = Google::Cloud::[ContainerAnalysis](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis.html).[container_analysis](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis/latest/Google-Cloud-ContainerAnalysis.html).[grafeas_client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container_analysis-v1/latest/Google-Cloud-ContainerAnalysis-V1-ContainerAnalysis-Client.html)
    
      parent = client.project_path project: project_id
      filter = "resourceUrl = \"#{resource_url}\" AND kind = \"VULNERABILITY\""
      vulnerability_list = client.list_occurrences parent: parent, filter: filter
      # Filter the list to include only "high" and "critical" vulnerabilities
      vulnerability_list.select do |item|
        [:HIGH, :CRITICAL].include? item.vulnerability.effective_severity
      end
    end
    

### Python

To learn how to install and use the client library for Artifact Analysis, see [Artifact Analysis client libraries](https://docs.cloud.google.com/artifact-analysis/docs/reference/libraries). For more information, see the [Artifact Analysis Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/containeranalysis/latest). 

To authenticate to Artifact Analysis, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud.devtools import [containeranalysis_v1](https://docs.cloud.google.com/python/docs/reference/containeranalysis/latest)
    
    
    def get_occurrences_for_note(note_id: str, project_id: str) -> int:
        """Retrieves all the occurrences associated with a specified Note.
        Here, all occurrences are printed and counted."""
        # note_id = 'my-note'
        # project_id = 'my-gcp-project'
    
        client = [containeranalysis_v1](https://docs.cloud.google.com/python/docs/reference/containeranalysis/latest).[ContainerAnalysisClient](https://docs.cloud.google.com/python/docs/reference/containeranalysis/latest/google.cloud.devtools.containeranalysis_v1.services.container_analysis.ContainerAnalysisClient.html)()
        grafeas_client = client.get_grafeas_client()
        note_name = f"projects/{project_id}/notes/{note_id}"
    
        response = grafeas_client.list_note_occurrences(name=note_name)
        count = 0
        for o in response:
            # do something with the retrieved occurrence
            # in this sample, we will simply count each one
            count += 1
        return count
    
    

## What's next

  * For instructions on how to view and filter notes and occurrences for container images, see [Viewing vulnerability occurrences](https://docs.cloud.google.com/artifact-analysis/docs/os-scanning-automatically#viewing_vulnerability_occurrences).

  * For instructions on how to set up notifications, see [Pub/Sub notifications](https://docs.cloud.google.com/artifact-analysis/docs/pub-sub-notifications).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
