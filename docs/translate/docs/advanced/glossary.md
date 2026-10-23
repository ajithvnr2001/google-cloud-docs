---
url: https://docs.cloud.google.com/translate/docs/advanced/glossary/
title: Creating and using glossaries (Advanced) \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:39:52.062407+00:00
---

# Creating and using glossaries (Advanced)  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/glossary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating and using glossaries (Advanced)

A _glossary_ is a custom dictionary the Cloud Translation API uses to consistently translate the customer's domain-specific terminology. This typically involves specifying how to translate a named entity.

You might use a glossary for the following use cases: 

  * **Product names** : For example, "Google Home" must translate to "Google Home".
  * **Ambiguous words** : For example, the word "bat" can mean a piece of sports equipment or an animal. If you know that you are translating words about sports, you might want to use a glossary to feed the Cloud Translation API the sports translation of "bat", not the translation for the animal.
  * **Borrowed words** : For example, "bouillabaisse" in French translates to "bouillabaisse" in English. English borrowed the word "bouillabaisse" from French in the 19th century. An English speaker lacking French cultural context might not know that bouillabaisse is a fish stew dish. Glossaries can override a translation so that "bouillabaisse" in French translates to "fish stew" in English.

**Note:** The maximum number of glossaries is listed on the [Quotas and limits](https://docs.cloud.google.com/translate/quotas#limits) page. If you reach this limit, you must delete existing glossaries to create new ones.

## Before you begin

Before you can start using the Cloud Translation API, you should complete the [Cloud Translation setup](https://docs.cloud.google.com/translate/docs/setup) page, which includes creating a project, enabling the Cloud Translation API, and setting up authentication. The setup page also provides instructions for installing client libraries for common programming languages, which is optional.

### Required permissions

To work with glossaries, your service account requires glossary-specific permissions. You can grant a role to your service account by using one of the [pre-defined IAM roles](https://docs.cloud.google.com/translate/docs/intro-to-v3#iam), such as Cloud Translation API Editor (`roles/cloudtranslate.editor`), or you can [create a custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that grants the necessary permissions. You can view all of the Cloud Translation API permissions in the [IAM permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference). Cloud Translation permissions begin with `cloudtranslate`.

For creating glossaries, you also need permissions to read objects in the Cloud Storage bucket where your glossary file is located. You can grant a role to your service account by using one of the [pre-defined IAM roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles), such as Storage Object Viewer (`roles/storage.objectViewer`), or you can [create a custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that grants permissions to read objects.

For information on adding an account to a role, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant_access).

## Create a glossary

The terms in a glossary can be single tokens (words) or short phrases (usually fewer than five words). The main steps for using a glossary are:

  1. Create a glossary file
  2. Create the glossary resource with our Cloud Translation API
  3. Specify which glossary to use when you request a translation



A project can have multiple glossaries. You can get a list of the available glossaries and can delete glossaries that you no longer need.

### Stopwords

Cloud Translation ignores some terms that are included in a glossary; these terms are known as _stopwords_. When translating stopwords, Cloud Translation ignores any matching glossary entries. For a list of all stopwords, see [Glossary stopwords](https://docs.cloud.google.com/translate/docs/advanced/stopwords).

### Creating a glossary file

Fundamentally, a glossary is a text file in which each line contains corresponding terms in multiple languages. The Cloud Translation API supports both _unidirectional_ glossaries, which specify the desired translation for a single pair of source and target languages, and _equivalent term sets_ , which identify the equivalent terms in multiple languages.

The total number of terms in a glossary input file can't exceed 10.4 million (10,485,760) UTF-8 bytes for all terms in all the languages combined. Any single glossary term must be less than 1024 UTF-8 bytes. Terms longer than 1024 bytes are ignored.

By default, glossary matches are case sensitive. When you apply a glossary, you can ignore case for all entries. If you have a mix of case-sensitive and case-insensitive terms, use the default behavior and, for case-insensitive terms, include both forms in your glossary.

**Important:** We recommend that you keep your glossary files even after you create a glossary resource. Cloud Translation doesn't support version control on glossary resources. If you modify a glossary and then need to rollback the changes, you must use the original glossary file to replace the modified glossary.

#### Unidirectional glossaries

The Cloud Translation API accepts TSV, CSV or TMX files.

##### TSV and CSV

For tab-separated values (TSV) and comma separated values (CSV), each row contains a pair of terms separated by a tab (`\t`) or comma (`,`). The first column includes the term in the source language and the second column includes the term in the target language, as shown in the following example:

![Unidirectional
glossary](https://docs.cloud.google.com/static/translate/docs/images/translate-glossary-unidirectional.png)

**Important:** **Do not include a header row** in the TSV or CSV file to identify the source and target languages. You identify them when you create the glossary.

##### Translation Memory eXchange (TMX)

Translation Memory eXchange (TMX) is a standard XML format for providing source and target translations. The Cloud Translation API supports input files in a format based on [TMX version 1.4](https://www.gala-global.org/lisa-oscar-standards). This example illustrates the required structure:
    
    
    <?xml version='1.0' encoding=>&<#39;utf-8'?
    !DOCTYPE tmx SY>S<TEM "tmx14.d>td&<quot;
    tmx version="1.4"
      header segtype="sentence" o-tmf="UTF-8&q>uot<;
      >admin<la>ng=&quo<t;en" srclan>g="e<n&q>uot; da<taty>pe=&quo<t;Pl>ainText<"/
      body
      >  tu
        <  <>/span>tuv xml<:lan>g="<;en&>quot;<
      >     < <>/span>segaccou<nt/seg
          /tuv>
          tu<v x>ml:lang=&q<uot;>es"<;
      >      s<egcuenta/seg
        >  /tuv
      <  <>/span>/tu
        tu
      <    >tuv xml<:lan>g=&qu<ot;>en&<quot;>
    <    >    segdirections/seg
          /tuv
          tuv xml:lang="es"
            segindicaciones/seg
          /tuv
        /tu
      /body
    /tmx
    

The `<header>` element of a well-formed TMX file must identify the source language using the `srclang` attribute, and every `<tuv>` element must identify the language of the contained text using the `xml:lang` attribute. You identify the source and target languages using their [ISO-639](https://wikipedia.org/wiki/ISO_639) codes.

All `<tu>` elements must contain a pair of `<tuv>` elements with the same source and target languages. If a `<tu>` element contains more than two `<tuv>` elements, the Cloud Translation API processes only the first `<tuv>` matching the source language and the first matching the target language and ignores the rest. If a `<tu>` element does not have a matching pair of `<tuv>` elements, the Cloud Translation API skips over the invalid `<tu>` element.

The Cloud Translation API strips the markup tags from around a `<seg>` element before processing it. If a `<tuv>` element contains more than one `<seg>` element, the Cloud Translation API concatenates their text into a single element with a space between them.

If the file contains XML tags other than those shown above, the Cloud Translation API ignores them.

If the file does not conform to proper XML and TMX format – for example, if it is missing an end tag or a `<tmx>` element – the Cloud Translation API aborts processing it. The Cloud Translation API also aborts processing if it skips more than 1024 invalid `<tu>` elements.

#### Equivalent term sets (CSV)

For equivalent term sets, Cloud Translation API only accepts files in the CSV format. To define equivalent term sets, create a multi-column CSV file in which each row lists a single glossary term in multiple languages.

The first row in the file is a header row identifying the language for each column, using its [ISO-639](https://wikipedia.org/wiki/ISO_639) or [BCP-47](https://tools.ietf.org/html/bcp47) language code. You can also include optional columns for part of speech (**pos**) and a description (**description**). The algorithm does not currently use **pos** information, and specific **pos** values are not validated.

Each subsequent row contains equivalent glossary terms in the languages identified in the header. You can leave columns blank if the term is not available in all languages.

![Equivalent terms set](https://docs.cloud.google.com/static/translate/docs/images/translate-glossary.png)

### Create a glossary resource

After you have the equivalent glossary terms identified, make the glossary file available to the Cloud Translation API by creating a glossary resource.

#### Unidirectional glossary

When creating a unidirectional glossary, you must indicate the language pair (`language_pair`), by specifying the source language (`source_language_code`), and the target language (`target_language_code`). The following example uses the REST API and command line, but you can also use the [client libraries](https://docs.cloud.google.com/translate/docs/reference/libraries/v3/overview-v3) to create a unidirectional glossary.

### REST

When you create a new glossary, you supply a glossary id (a resource name). For example:   

    
    
    projects/my-project/locations/us-central1/glossaries/my-en-to-ru-glossary

where `my-project` is the PROJECT_NUMBER_OR_ID, and `my-en-ru-glossary` is the glossary-id provided by you. **Note:** project-id works as well, but project-number is preferred going forward.

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
  * glossary-id: your glossary ID, for example., my_en_ru_glossary
  * bucket-name: name of bucket where your glossary file is located
  * glossary-filename: filename of your glossary



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries

Request JSON body: 
    
    
    {
      "name":"projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries/glossary-id",
      "languagePair": {
        "sourceLanguageCode": "en",
        "targetLanguageCode": "ru"
        },
      "inputConfig": {
        "gcsSource": {
          "inputUri": "gs://bucket-name/glossary-filename"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-number/locations/us-central1/operations/operation-id",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.translation.v3beta1.CreateGlossaryMetadata",
        "name": "projects/project-number/locations/us-central1/glossaries/glossary-id",
        "state": "RUNNING",
        "submitTime": "2019-11-19T19:05:10.650047636Z"
      }
    }
    

#### Equivalent term sets glossary

Once you have the glossary terms identified in your equivalent term set, make the glossary file available to the Cloud Translation API by creating a glossary resource.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
  * glossary-id: your glossary ID
  * bucket-name: name of bucket where your glossary file is located
  * glossary-filename: filename of your glossary



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries

Request JSON body: 
    
    
    {
      "name":"projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries/glossary-id",
      "languageCodesSet": {
        "languageCodes": ["en", "en-GB", "ru", "fr", "pt-BR", "pt-PT", "es"]
      },
      "inputConfig": {
        "gcsSource": {
    "inputUri": "gs://bucket-name/glossary-file-name"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-number/locations/us-central1/operations/20191103-09061569945989-5d937985-0000-21ac-816d-f4f5e80782d4",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.translation.v3beta1.CreateGlossaryMetadata",
        "name": "projects/project-number/locations/us-central1/glossaries/glossary-id",
        "state": "RUNNING",
        "submitTime": "2019-11-03T16:06:29.134496675Z"
      }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Go API reference documentation](https://godoc.org/cloud.google.com/go/translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	translate "cloud.google.com/go/translate/apiv3"
    	"cloud.google.com/go/translate/apiv3/translatepb"
    )
    
    // createGlossary creates a glossary to use for other operations.
    func createGlossary(w io.Writer, projectID string, location string, glossaryID string, glossaryInputURI string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// glossaryID := "my-glossary-display-name"
    	// glossaryInputURI := "gs://cloud-samples-da[ta/translation/gloss](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_NewTranslationClient)ary.csv"
    
    	ctx := context.Background()
    	client, err := translate.NewTranslationClient(ct[x](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_Close))
    	if err != nil& {
    		return fmt.Errorf("NewTranslationClient: %w", err)
    	}
    	defer client.Close()
    
    	req := translatepb.CreateG&lossaryRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		Glossary: translatepb.Glossary{
    	&		Name: fmt.Sprintf("projects/%s/locations/%s/glossaries/&%s", projectID, location, glossaryID),
    			Languages: translatepb.Glossary_LanguageCodesSet_{
    				Language&CodesSet: translatepb.Glossary_LanguageCodesS&et{
    					LanguageCodes: []string{"en", "ja&q&uot;},
    				},
    			},
    			InputConfig: translatepb.GlossaryInputConfig{
    				Source: translatepb.GlossaryInputConfig_GcsSource{
    					GcsSource: translatepb.GcsSource{
    						InputUri: glossaryInputURI,
    					},
    				},
    			},
    		},
    	}
    
    	// The CreateGlossary operation is async.
    	op, err := client.CreateGlossary(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateGlossary: %w", err)
    	}
    	fmt.Fprintf(w, "Processing operation name: %q\n", op.Name())
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created: %v\n", resp.GetName())
    	fmt.Fprintf(w, "Input URI: %v\n", resp.InputConfig.GetGcsSource().GetInputUri())
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.translate.v3.[CreateGlossaryMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.CreateGlossaryMetadata.html);
    import com.google.cloud.translate.v3.[CreateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.CreateGlossaryRequest.html);
    import com.google.cloud.translate.v3.[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsSource.html);
    import com.google.cloud.translate.v3.[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html);
    import com.google.cloud.translate.v3.[GlossaryInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryInputConfig.html);
    import com.google.cloud.translate.v3.[GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html);
    import com.google.cloud.translate.v3.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    
    public class CreateGlossary {
    
      public static void createGlossary() throws InterruptedException, ExecutionException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        String glossaryId = "your-glossary-display-<name&q>uot;;
        ListString languageC<>odes = new ArrayList();
        languageCodes.add("your-language-code");
        String inputUri = "gs://your-gcs-bucket/path/to/input/file.txt";
        createGlossary(projectId, glossaryId, languageCodes, inputUri);
      }
    
      // Create a equivalent term sets glossary
      // https://cloud.google.com/translate/docs/advanced/glossary#format-glossary
      public static void createGlossary(
          S<tring >projectId, String glossaryId, ListString languageCodes, String inputUri)
          throws IOException, ExecutionException, InterruptedException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clea[n up any remaining backg](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html)round reso[urces.](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html)
        try (TranslationServiceClient client = TranslationServiceClient.create()) {
          // Supported Locations: `global`, [glossary location], or [model location]
          // Glossaries must be hosted in `us-central1`
          // Custom Models must use the same location as your model. (us-centr[al1)](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html)
          String loca[tion](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html) = ";us-central1";
          Locati[onName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html) parent = LocationName[.of(projectI](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html)d, location);
          GlossaryName glossaryName = GlossaryName.of(projectId, location, glossaryId);
    
          // Supported Languag[es: http](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html)s[://cloud.google.](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.LanguageCodesSet.html)com/translate/docs/languages
     [     ](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html)Glossary.LanguageCodesSet language[CodesSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.LanguageCodesSet.Builder.html#com_google_cloud_translate_v3_Glossary_LanguageCodesSet_Builder_addAllLanguageCodes_java_lang_Iterable_java_lang_String__) =
              Glossary.LanguageCodesSet.newBuilder().addAllLanguageCodes(languageCodes).build();
    
          [// Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsSource.html)ure the sourc[e of the ](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GcsSource.html)file from a GCS bucket
          GcsSource gcsSource = [GcsSource.newBuilde](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryInputConfig.html)r().setInputUri(inputUri)[.](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryInputConfig.html)build();
          GlossaryInputConfig inputConfig =
              GlossaryInput[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html).newBuilder().setGcsSour[ce](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html)(gcsSource).build();
    
          Glossary glossary =
            [  ](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html#com_google_cloud_translate_v3_GlossaryName_toString__)Glossary.newBuilder()
       [           ](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.Builder.html#com_google_cloud_translate_v3_Glossary_Builder_setLanguageCodesSet_com_google_cloud_translate_v3_Glossary_LanguageCodesSet_).setName(glossaryName.toString())
                  .setLanguageCodesSet(languageCodesSet)
                  [.setInputConfig(input](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.CreateGlossaryRequest.html)Config)
                 [ ](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.CreateGlossaryRequest.html).build();
    
          CreateGlossaryRequest request =
              CreateG[lossaryR](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html#com_google_cloud_translate_v3_LocationName_toString__)equest.newBuilder()
                  .setParent(parent.toString())
                  .setGlossary(glossary)
                  .build();
    
    <      // Start an asynchronous r>equest
          OperationFutur[eGlossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html#com_google_cloud_translate_v3_TranslationServiceClient_createGlossaryAsync__org_jspecify_annotations_Nullable_com_google_cloud_translate_v3_LocationName_com_google_cloud_translate_v3_Glossary_), CreateGlossaryMetadata future =
              client.createGlossaryAsync(request);
    
          System[.out.pri](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html)ntln("Waiting [for](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__) operation to complete...");
          Glossary response = future.get();
          System.out.println("Cr[eated G](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html#com_google_cloud_translate_v3_Glossary_getName__)lossary.");
          System.out.printf("Glossary nam[e: %s\n"](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html#com_google_cloud_translate_v3_Glossary_getEntryCount__), response.getName());
          System.out.printf("Entr[y count: %s\n&](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html#com_google_cloud_translate_v3_Glossary_getInputConfig__)quot;, response.getEntryCount());
          System.out.printf("Input URI: %s\n", response.getInputConfig().getGcsSource().getInputUri());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const location = 'global';
    // const glossaryId = 'your-glossary-display-name';
    
    // Imports the Google Cloud Translation library
    const {TranslationSe[rviceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)} = require('@google-cloud/translate');
    
    // Instantiates a clien[t](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)
    const translationClient = new TranslationServiceClient();
    
    async function createGlossary() {
      // Construct glossary
      const glossary = {
        languageCodesSet: {
          languageCodes: ['en', 'es'],
        },
        inputConfig: {
          gcsSource: {
            inputUri: 'gs://cloud-samples-data/translation/glossary.csv',
          },
        },
        name: `projects/${projectId}/locations/${location}/glossaries/${glossaryId}`,
      };
    
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        glossary: glossary,
      };
    
      // Create glossary using a long-running operation
      const [operation] = await translationClient.createGlossary(request);
    
      // Wait for the operation to complete
      await operation.promise();
    
      cons[ole](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/v2.translate.html).log('Created glossary:');
      console.log(`InputUri ${request.glossary.inputConfig.gcsSource.inputUri}`);
    }
    
    createGlossary();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import translate_v3 as translate
    
    
    def create_glossary(
        project_id: str = "YOUR_PROJECT_ID",
        input_uri: str = "YOUR_INPUT_URI",
        glossary_id: str = "YOUR_GLOSSARY_ID">;,
        timeout: int = 180,
    ) - translate.Glossary:
        """
        Create a equivalent term sets glossary. Glossary can be words or
        short phrases (usually fewer than five words).
        https://cloud.google.com/translate/docs/advanced/glossary#format-glossary
        """
        client = translate.TranslationServiceClient()
    
        # Supported language codes: https://cloud.google.com/translate/docs/languages
        source_lang_code = "en"
        target_lang_code = "ja"
        location = "us-central1"  # The location of the glossary
    
        name = client.glossary_path(project_id, location, glossary_id)
        language_codes_set = translate.types.Glossary.LanguageCodesSet(
            language_codes=[source_lang_code, target_lang_code]
        )
    
        gcs_source = translate.types.GcsSource(input_uri=input_uri)
    
        input_config = translate.types.GlossaryInputConfig(gcs_source=gcs_source)
    
        glossary = translate.types.Glossary(
            name=name, language_codes_set=language_codes_set, input_config=input_config
        )
    
        parent = f"projects/{project_id}/locations/{location}"
        # glossary is a custom dictionary Translation API uses
        # to translate the domain-specific terminology.
        operation = client.create_glossary(parent=parent, glossary=glossary)
    
        result = operation.result(timeout)
        print(f"Created: {result.name}")
        print(f"Input Uri: {result.input_config.gcs_source.input_uri}")
    
        return result
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

### Operation status

Creating a glossary resource is a long-running operation, so it may take a substantial amount of time to complete. You can poll the status of this operation to see if it has completed, or you can cancel the operation.

For more information, see [Long-running operations](https://docs.cloud.google.com/translation/docs/advanced/long-running-operation).

## Use glossaries

### Translate text with a glossary

In Cloud Translation - Advanced, you explicitly specify [which translation model](https://docs.cloud.google.com/translation/docs/advanced/translating-text-v3#model-parameter) to use for translating the text. Translation LLM, NMT, and customized NMT models can be called in combination with glossary, but only Translation LLM supports the latest quality enhancement with contextual glossary. To apply this feature, set BOOLEAN_CONTEXTUAL: to TRUE. You can also identify a glossary to use for domain-specific terminology.

**Note:** The specified glossary must be associated with the current Google Cloud project.

### REST

This example translates text using the default NMT model and a glossary.

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project.
  * GLOSSARY_ID: Your glossary ID, such as `my-en-ru-glossary`.
  * BOOLEAN: Whether matches are case insensitive. By default this value is `false`.
  * BOOLEAN_CONTEXTUAL: Whether considers context in glossary translation. By default this value is `false`.



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:translateText

Request JSON body: 
    
    
    {
      "sourceLanguageCode": "en",
      "targetLanguageCode": "ru",
      "contents": "Dr. Watson, please discard your trash. You've shared unsolicited email with me. Let's talk about spam and importance ranking in a confidential mode.",
      "glossaryConfig": {
        "glossary": "projects/project-number/locations/us-central1/glossaries/GLOSSARY_ID",
        "ignoreCase": BOOLEAN,
        "contextual_translation_enabled": BOOLEAN_CONTEXTUAL
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:translateText"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1:translateText" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "glossaryTranslations": {
        "translatedText": "Доктор Ватсон, пожалуйста, откажитесь от своего мусора. Вы поделились нежелательной электронной почтой со я . Давайте поговорим о спаме и важности рейтинга в конфиденциальном режиме.",
        "glossaryConfig": {
          "glossary": "projects/project-number/locations/us-central1/glossaries/GLOSSARY_ID",
          "ignoreCase": BOOLEAN,
          "contextual_translation_enabled": BOOLEAN_CONTEXTUAL
        }
      },
      "translations": {
        "translatedText": "Доктор Ватсон, пожалуйста, откажитесь от своего мусора. Вы поделились нежелательной электронной почтой со мной. Давайте поговорим о спаме и важности рейтинга в конфиденциальном режиме.",
      }
    }
    

The `translations` field contains the regular machine translation before the glossary is applied; the `glossaryTranslations` field contains the translation after the glossary is applied. When you set the `contextual_translation_enabled` field to `true`, the response will only contain the `glossaryTranslations` field and not the `translations` field. 

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Go API reference documentation](https://godoc.org/cloud.google.com/go/translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	translate "cloud.google.com/go/translate/apiv3"
    	"cloud.google.com/go/translate/apiv3/translatepb"
    )
    
    // translateTextWithGlossary translates input text and returns translated text.
    func translateTextWithGlossary(w io.Writer, projectID string, location string, sourceLang string, targetLang string, text string, glossaryID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// sourceLang := "en"
    	// targetLang := "ja"
    	// text := "Hello world["](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_NewTranslationClient)
    	// glossaryID := "your-glossary-id"
    
    	ctx := context.Background()
    	client, err := translate.New[Trans](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_Close)lationClient&(ctx)
    	if err != nil {
    		return fmt.Errorf("NewTranslationClient: %w", err)
    	}
    	defer client.Close()
    
    	req := translatepb.TranslateTextRequest{
    		Parent:             fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		SourceLanguageCode: sourceLang,
    		TargetLanguageCode: targetLang,
    		M&imeType:           "text/plain", // Mime types: "text/plain", "text/html"
    		Contents:           []string{text},
    		GlossaryConfig: translatepb.TranslateTextGlossaryConfig{
    			Glossary: fmt.Sprintf("projects/%s/locations/%s/glossaries/%s", projectID, location, glossaryID),
    		},
    	}
    
    	resp, err := client.TranslateText(ctx, req)
    	if err != nil {
    		return fmt.Errorf("TranslateText: %w", err)
    	}
    
    	// Display the translation for each input text provided
    	for _, translation := range resp.GetGlossaryTranslations() {
    		fmt.Fprintf(w, "Translated text: %v\n", translation.GetTranslatedText())
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.translate.v3.[GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html);
    import com.google.cloud.translate.v3.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html);
    import com.google.cloud.translate.v3.[TranslateTextGlossaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextGlossaryConfig.html);
    import com.google.cloud.translate.v3.[TranslateTextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextRequest.html);
    import com.google.cloud.translate.v3.[TranslateTextResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextResponse.html);
    import com.google.cloud.translate.v3.[Translation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Translation.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import java.io.IOException;
    
    public class TranslateTextWithGlossary {
    
      public static void translateTextWithGlossary() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        // Supported Languages: https://cloud.google.com/translate/docs/languages
        String sourceLanguage = "your-source-language";
        String targetLanguage = "your-target-language";
        String text = "your-text";
        String glossaryId = "your-glossary-display-name";
        translateTextWithGlossary(projectId, sourceLanguage, targetLanguage, text, glossaryId);
      }
    
      // Translates a given text using a glossary.
      public static void translateTextWithGlossary(
          String projectId,
          String sourceLanguage,
          String targetLanguage,
          String text,
          String glossaryId)
          throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to s[afely clean up any remai](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html)ning backg[round resources.](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html)
        try (TranslationServiceClient client = TranslationServiceClient.create()) {
          // Supported Locations: `global`, [glossary location], or [model location]
          // Glossaries must be hosted in `us-central1`
          // Custom Models must use the same location as your model.[ (us-central](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html)1)
          S[tring](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html) location = "us-central1";
       [   ](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html)LocationName parent = Loc[ationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html).of(projectId, location);
    
          GlossaryName g[lossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextGlossaryConfig.html) = GlossaryName.of(projectId, location, glos[saryId](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextGlossaryConfig.html));
          TranslateTextGlossaryConfig glossaryConfig =
          [    ](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html#com_google_cloud_translate_v3_GlossaryName_toString__)TranslateTextGlossaryConfig.newBuilder().setGlossary(glossaryName.toString()).build();
    
          // Supported Mime T[ypes: https://cloud.](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextRequest.html)google.com/translate/[docs/supported-forma](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextRequest.html)ts
          TranslateTextRequest request =
          [    ](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html#com_google_cloud_translate_v3_LocationName_toString__)TranslateTextRequest.newBuilder()
                  .setParent(parent.toString())
                  .setMimeType("text/plain")
                  .setSourceLanguageCode(sourceLanguage)
                  .setTargetLanguageCode(targetLanguage)
                  .addContents(text)
    [              .setGlo](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextResponse.html)ssaryConfig(glossaryConfig)
                  .build();
    
          TranslateTextResponse response = client.translateText(requ[est](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Translation.html));
    
          // Display the transla[tion for each input text pr](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslateTextResponse.html#com_google_cloud_translate_v3_TranslateTextResponse_getGlossaryTranslationsList__)ovided
          for (Translation translation : response.getGlossaryTranslationsList()) {
            System.out.printf("Translated text: %s\n", translation.getTranslatedText());
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const location = 'global';
    // const glossaryId = 'YOUR_GLOSSARY_ID';
    // const text = 'text to translate';
    
    // Imports the Google Cloud Translation library
    const {Trans[lationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)} = require('@google-cloud/translate');
    
    // Instantiates[ a client](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)
    const translationClient = new TranslationServiceClient();
    async function translateTextWithGlossary() {
      const glossaryConfig = {
        glossary: `projects/${projectId}/locations/${location}/glossaries/${glossaryId}`,
      };
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        contents: [text],
        mimeType: 'text/plain', // mime types: text/plain, text/html
        sourceLanguageCode: 'en',
        targetLanguageCode: 'es',
        glossaryConfig: glossaryConfig,
      };
    
      // Run request
      const [response] = await translationClient.translateText(request);
    
      for (const translation of response.glossaryTranslations) {
        console.log(`Translation: ${translation.translatedText}`);
      }
    }
    
    translateTextWithGlossary();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [translate](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)
    
    
    def translate_text_with_glossary(
        text: str = "YOUR_TEXT_TO_TRANSLATE",
        project_id: str = "YOUR_PROJECT_ID",
        glossary_id: str = &qu>ot;YOUR_GLOSSARY_ID",
    ) - translate.TranslateTextResponse:
        """Translates a given text using a glossary.
    
        Args:
            text: The text to translate.
            project_id: The ID of the GCP project that owns the glossary.
            glossary_id: The ID of the glossary to use.
    
        Returns:
    [        T](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)h[e translated text."](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html)""
        client = translate.TranslationServiceClient()
        location = "us-central1"
        p[arent<](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html)/span> =[ f"proje](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_glossary_path)cts/{project_id}/locations/{location}"
    
        glossary = client.glossary_path(
            project_id, "us[-central1](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client.html)&[quot;](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.types.TranslateTextGlossaryConfig.html), glossary_id  # The location of the glossary
        )
    
        glossary_config = translate.TranslateTextGlossaryConfig(glossary=glossary)
    
        # S[upport](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.html)e[d language cod](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3.services.translation_service.TranslationServiceClient.html#google_cloud_translate_v3_services_translation_service_TranslationServiceClient_translate_text)es: https://cloud.google.com/translate/docs/languages
        response = client.translate_text(
            request={
                "contents": [text],
                "target_language_code": "ja",
                "source_language_code": "en",
                "parent": parent,
                "glossary_config": glossary_config,
            }
        )
    
        print("Translated text: \n")
        for translation in response.glossary_translations:
            print(f"\t {translation.translated_text}")
    
        return response
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

### Adaptive translations with glossary

To use a glossary with an [adaptive translation](https://docs.cloud.google.com/translate/docs/advanced/adaptive_translation/api-adaptivemttranslate) request, include a glossary configuration with your request.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
  * LOCATION: The region where your source dataset is located, such as `us-central1`.
  * DATASET_NAME: The name of the dataset that Cloud Translation uses to customize your translations, formatted as `projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID`. You can get dataset names by [listing all datasets](https://docs.cloud.google.com/translate/docs/advanced/adaptive-translation-data) in your project.
  * SOURCE_TEXT: The text to translate.
  * MIME_TYPE (Optional): The format of the source text, such as `text/html` or `text/plain`. By default, the MIME type is set to `text/plain`.
  * GLOSSARY_ID: Your glossary ID, such as `my-en-ru-glossary`.
  * BOOLEAN (Optional): Whether matches are case insensitive. By default this value is `false`.
  * BOOLEAN_CONTEXTUAL (Optional): Whether to consider context in glossary translation. By default this value is `false`.



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION:adaptiveMtTranslate

Request JSON body: 
    
    
    {
      "dataset": "DATASET_NAME",
      "content": ["SOURCE_TEXT"],
      "mimeType": "MIME_TYPE",
      "glossaryConfig": {
        "glossary": "projects/project-number/locations/LOCATION/glossaries/GLOSSARY_ID",
        "ignoreCase": BOOLEAN,
        "contextual_translation_enabled": BOOLEAN_CONTEXTUAL
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION:adaptiveMtTranslate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION:adaptiveMtTranslate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "translations": [
        {
          "translatedText": "TRANSLATED_TEXT"
        }
      ],
      "languageCode": "TARGET_LANGUAGE",
      "glossaryTranslations": {
        "translatedText": "TRANSLATED_TEXT",
        "glossaryConfig": {
          "glossary": "projects/project-number/locations/LOCATION/glossaries/GLOSSARY_ID",
          "ignoreCase": BOOLEAN,
          "contextual_translation_enabled": BOOLEAN_CONTEXTUAL
        }
      },
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
      {% setvar launch_stage %}preview{% endsetvar %}
    {% setvar launch_type %}feature{% endsetvar %}
    {% include "cloud/_shared/_info_launch_stage_disclaimer.html" %}
    
    /** Translates using AdaptiveMt. */
    private static void adaptiveMtTranslate(
        TranslationServiceClient translationServiceClient, String projectId, String datasetId) {
      String adaptiveMtDatasetName =
          String.format(
              "projects/%s/locations/LOCATION/adaptiveMtDatasets/%s", projectId, datasetId);
      String glossaryId = "your-glossary-display-name";
      GlossaryName glossaryName = GlossaryName.of(projectId, location, glossaryId);
      GlossaryConfig glossaryConfig =
          GlossaryConfig.newBuilder().setGlossary(glossaryName.toString()).build();
    
      AdaptiveMtTranslateRequest request =
          AdaptiveMtTranslateRequest.newBuilder()
              .setParent(LocationName.of(projectId, "us-central1").toString())
              .setDataset(adaptiveMtDatasetName)
              .addContent("Sample translation text")
              .setGlossaryConfig(glossaryConfig)
              .build();
      AdaptiveMtTranslateResponse response = translationServiceClient.adaptiveMtTranslate(request);
    
      System.out.println("Translating using AdaptiveMt");
      System.out.println(response);
    }
    
    
    
      

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
      async function translate() {
      /**
      * TODO(developer): Uncomment these variables before running the sample.
      */
      // const projectId = 'YOUR_PROJECT_ID';
      // const location = 'global';
      // const glossaryId = 'YOUR_GLOSSARY_ID';
    
      const glossaryConfig = {
        glossary: `projects/${projectId}/locations/${location}/glossaries/${glossaryId}`,
      };
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        dataset: `projects/${projectId}/locations/${location}/adaptiveMtDatasets/${
            adaptiveMtDatasetName}`,
        content: ['Sample translate query'],
        glossaryConfig: glossaryConfig,
      } const [response] = await translationClient.adaptiveMtTranslate(request)
      console.log('Translating')
      console.log(response)
    }
      

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
      def adaptive_mt_translate(
        project_id: str = "YOUR_PROJECT_ID",
        glossary_id: str = "YOUR_GLOSSARY_ID"):
        # Create a client
        client = translate.TranslationServiceClient()
        # Create a glossary
        glossary = client.glossary_path(
            project_id, "us-central1", glossary_id  # The location of the glossary
        )
    
        glossary_config = translate.GlossaryConfig(glossary=glossary)
        # Initialize the request
        request = translate.AdaptiveMtTranslateRequest(
            parent="projects/PROJECT_ID/locations/LOCATION",
            dataset="projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID",
            content=["Sample translation request"]
            glossary_config=glossary_config,
        )
        # Make the request
        response = client.adaptive_mt_translate(request)
        # Handle the response
        print(response)
      

### Get information about a glossary

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
  * glossary-id: your glossary ID, for example, "my-en-to-ru-glossary" 



HTTP method and URL: 
    
    
    GET https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries/glossary-id

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries/glossary-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries/glossary-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-number/locations/us-central1/glossaries/glossary-id",
      "languagePair": {
        "sourceLanguageCode": "en",
        "targetLanguageCode": "ru"
      },
      "inputConfig": {
        "gcsSource": {
      "inputUri": "gs://bucket-name/glossary-file-name"
        }
      },
      "entryCount": 9603
    }
    
    
    

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Go API reference documentation](https://godoc.org/cloud.google.com/go/translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	translate "cloud.google.com/go/translate/apiv3"
    	"cloud.google.com/go/translate/apiv3/translatepb"
    )
    
    // getGlossary gets the specified glossary.
    func getGlossary(w io.Writer, projectID string, location string, glossaryID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// glossaryID := ["glossary-id&qu](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_NewTranslationClient)ot;
    
    	ctx := context.Background()
    	client, err := translate.NewTranslationClient(ctx)
    	if err[ != n](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_Close)il {
    		retur&n fmt.Errorf("NewTranslationClient: %w", err)
    	}
    	defer client.Close()
    
    	req := translatepb.GetGlossaryRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/glossaries/%s", projectID, location, glossaryID),
    	}
    
    	resp, err := client.GetGlossary(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetGlossary: %w", err)
    	}
    
    	fmt.Fprintf(w, "Glossary name: %v\n", resp.GetName())
    	fmt.Fprintf(w, "Entry count: %v\n&quot;, resp.GetEntryCount())
    	fmt.Fprintf(w, "Input URI: %v\n", resp.GetInputConfig().GetGcsSource().GetInputUri())
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.translate.v3.[GetGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetGlossaryRequest.html);
    import com.google.cloud.translate.v3.[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html);
    import com.google.cloud.translate.v3.[GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import java.io.IOException;
    
    public class GetGlossary {
    
      public static void getGlossary() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        String glossaryId = "your-glossary-display-name";
        getGlossary(projectId, glossaryId);
      }
    
      // Get a particular glossary based on the glossary ID
      public static void getGlossary(String projectId, String glossaryId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining b[ackground resources.](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html)
        try (Tran[slationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client = TranslationServiceClient.create()) {
          // Supported Locations: `global`, [glossary location], or [model location]
          // Glossaries must be hosted in `us-central1`
          // Custom Models must use the same location as yo[ur model. (u](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html)s-central1)
        [  ](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html)GlossaryName glossaryName = GlossaryName.of(projectId, &quo[t;us-central1"](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetGlossaryRequest.html);, glossaryId);
         [ ](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GetGlossaryRequest.html)GetGlossaryRequest request =
              GetGlossaryRe[quest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html#com_google_cloud_translate_v3_GlossaryName_toString__).newBuilder().setName(g[lossaryN](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html)ame.toString()).build();
    
          Glossary response = client.getGlossary(request);
    
          System.out[.printf](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html#com_google_cloud_translate_v3_Glossary_getName__)("Glossary name: %s\n", response.getName());
        [  ](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html#com_google_cloud_translate_v3_Glossary_getEntryCount__)System.out.printf("Entry count: %s\n", response.getEntryCo[unt](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html#com_google_cloud_translate_v3_Glossary_getInputConfig__)());
          System.out.printf("Input URI: %s\n", response.getInputConfig().getGcsSource().getInputUri());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const location = 'global';
    // const glossaryId = 'YOUR_GLOSSARY_ID';
    
    // Imports the Google Cloud Translation library
    const {TranslationSe[rviceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)} = require('@google-cloud/translate');
    
    // Instantiates a clien[t](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)
    const translationClient = new TranslationServiceClient();
    
    async function getGlossary() {
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        name: `projects/${projectId}/locations/${location}/glossaries/${glossaryId}`,
      };
    
      // Get glossary
      const [response] = await translationClient.getGlossary(request);
    
      console.log(`Glossary name: ${response.name}`);
      console.log(`Entry count: ${response.entryCount}`);
      console.log(`Input URI: ${response.inputConfig.gcsSource.inputUri}`);
    }
    
    getGlossary();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import translate_v3 as translate
    
    
    def get_glossary(
        project_id: str = "YOUR_PROJECT_ID", glossary_id: str = "YOUR_G>LOSSARY_ID"
    ) - translate.Glossary:
        """Get a particular glossary based on the glossary ID.
    
        Args:
            project_id: The GCP project ID.
            glossary_id: The ID of the glossary to retrieve.
    
        Returns:
            The glossary.
        """
        client = translate.TranslationServiceClient()
    
        name = client.glossary_path(project_id, "us-central1", glossary_id)
    
        response = client.get_glossary(name=name)
        print(f"Glossary name: {response.name}")
        print(f"Entry count: {response.entry_count}")
        print(f&quot;Input URI: {response.input_config.gcs_source.input_uri}")
    
        return response
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

### List glossaries

A project can include numerous glossaries. This section describes how to retrieve a list of the available glossaries for a particular project.

### REST

This example lists all glossaries associated with the specified project. 

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project



HTTP method and URL: 
    
    
    GET https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "glossaries": [
        {
          "name": "projects/project-number/locations/us-central1/glossaries/glossary-id",
          "languagePair": {
            "sourceLanguageCode": "en",
            "targetLanguageCode": "ru"
          },
          "inputConfig": {
            "gcsSource": {
              "inputUri": "gs://bucket-name/glossary-file-name"
            }
          },
          "entryCount": 9603
        },
        ...
      ]
    }
    
    

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Go API reference documentation](https://godoc.org/cloud.google.com/go/translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	translate "cloud.google.com/go/translate/apiv3"
    	"cloud.google.com/go/translate/apiv3/translatepb"
    	"google.golang.org/api/iterator"
    )
    
    // listGlossaries gets the specified glossary.
    func listGlossaries(w io.Writer, projectID string, location string) error {
    	// projectID := "my-project-id"
    	// location := ["us-central1&qu](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_NewTranslationClient)ot;
    
    	ctx := context.Background()
    	client, err := translate.NewTranslationClient(ctx)
    	if err[ != n](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_Close)il {
    		retur&n fmt.Errorf("NewTranslationClient: %w", err)
    	}
    	defer client.Close()
    
    	req := translatepb.ListGlossariesRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    	}
    
    	it := client.ListGlossaries(ctx, req)
    
    	// Iterate over all results
    	for {
    		glossary, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("ListGlossaries.Next: %w", err)
    		}
    		fmt.Fprintf(w, "Name: %v\n", glossary.GetName())
    		fmt.Fprintf(w, "Entry count: %v\n", glossary.GetEntryCount())
    		fmt.Fprintf(w, "Input URI: %v\n", glossary.GetInputConfig().GetGcsSource().GetInputUri())
    		for _, languageCode := range glossary.GetLanguageCodesSet().GetLanguageCodes() {
    			fmt.Fprintf(w, "Language code: %v\n", languageCode)
    		}
    		if languagePair := glossary.GetLanguagePair(); languagePair != nil {
    			fmt.Fprintf(w, "Language pair: %v, %v\n",
    				languagePair.GetSourceLanguageCode(), languagePair.GetTargetLanguageCode())
    		}
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.translate.v3.[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html);
    import com.google.cloud.translate.v3.[ListGlossariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListGlossariesRequest.html);
    import com.google.cloud.translate.v3.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import java.io.IOException;
    
    public class ListGlossaries {
    
      public static void listGlossaries() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        listGlossaries(projectId);
      }
    
      // List all the glossaries in a specified location
      public static void listGlossaries(String projectId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background [resources.](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html)
        try (TranslationSer[viceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client = TranslationServiceClient.create()) {
          // Supported Locations: `global`, [glossary location], or [model location]
          // Glossaries must be hosted in `us-central1`
          // Custom Models must use the same location as your model. [(us-central1](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html))
          Lo[cationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html) parent = LocationName.of(projectId, &q[uot;us-central1"](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListGlossariesRequest.html));
          ListGlossari[esRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.ListGlossariesRequest.html) request =
              ListGlossariesRequest.[newBuild](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.LocationName.html#com_google_cloud_translate_v3_LocationName_toString__)er().setParent(parent.toS[tring](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.Glossary.html)()).build();
    
          for (Glossary responseItem : client.listGlossaries(request).iterateAll()) {
            System.out.printf("Glossary name: %s\n", responseItem.getName());
            System.out.printf("Entry count: %s\n", responseItem.getEntryCount());
            System.out.printf(
                "Input URI: %s\n", responseItem.getInputConfig().getGcsSource().getInputUri());
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const location = 'global';
    
    // Imports the Google Cloud Translation library
    const {TranslationServiceCli[ent](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)} = require('@google-cloud/translate');
    
    // Instantiates a client
    const [translationClient = new ](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)TranslationServiceClient();
    
    async function listGlossaries() {
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
      };
    
      // Run request
      const [response] = await translationClient.listGlossaries(request);
    
      for (const glossary of response) {
        console.log(`Name: ${glossary.name}`);
        console.log(`Entry count: ${glossary.entryCount}`);
        console.log(`Input uri: ${glossary.inputConfig.gcsSource.inputUri}`);
        for (const languageCode of glossary.languageCodesSet.languageCodes) {
          console.log(`Language code: ${languageCode}`);
        }
      }
    }
    
    listGlossaries();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import translate
    
    
    def list_glossaries(project_id: str = "YOUR_PROJECT_I>D") - translate.Glossary:
        """List Glossaries.
    
        Args:
            project_id: The GCP project ID.
    
        Returns:
            The glossary.
        """
        client = translate.TranslationServiceClient()
    
        location = "us-central1"
    
        parent = f"projects/{project_id}/locations/{location}"
    
        # Iterate over all results
        for glossary in client.list_glossaries(parent=parent):
            print(f"Name: {glossary.name}")
            print(f"Entry count: {glossary.entry_count}")
            print(f"Input uri: {glossary.input_config.gcs_source.input_uri}")
    
            # Note: You can create a glossary using one of two modes:
            # language_code_set or language_pair. When listing the information for
            # a glossary, you can only get information for the mode you used
            # when creating the glossary.
            for language_code in glossary.language_codes_set.language_codes:
                print(f"Language code: {language_code}")
    
        return glossary
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

### Update a glossary

You can update a glossary to change its name or replace all of its entries with a new glossary input file. If you need to rollback changes to the glossary entries, you must use the original glossary file to replace the modified glossary.

### REST

To update a glossary, send a PATCH request with the [glossary.patch](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.glossaries/patch) method. The following example updates an equivalent term set glossary. Use the list method to find the ID of a particular glossary. 

The `update_mask` query parameter specifies if you're updating the glossary input file, glossary display name, or both. At least one update mask parameter is required. 

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project.
  * LOCATION: The region where the glossary to update is located, such as `us-central1`.
  * GLOSSARY_ID: The ID of an existing glossary.
  * LANGUAGE_CODE: The [language code](https://docs.cloud.google.com/translate/docs/languages) that specifies the languages for this equivalent term set glossary.
  * GLOSSARY_FILE_PATH: The location and filename of your glossary input file.



HTTP method and URL: 
    
    
    PATCH https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID?update_mask=input_config&update_mask=display_name

Request JSON body: 
    
    
    {
      "name":"projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID",
      "languageCodesSet": {
        "languageCodes": ["LANGUAGE_CODE", ...]
      },
      "inputConfig": {
        "gcsSource": {
          "inputUri": "gs://GLOSSARY_FILE_PATH"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID?update_mask=input_config&update_mask=display_name"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID?update_mask=input_config&update_mask=display_name" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.translation.v3.UpdateGlossaryMetadata",
        "glossary": {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/glossaries/GLOSSARY_ID",
          "languageCodesSet": {
            "languageCodes": ["LANGUAGE_CODE", ...]
          },
          "inputConfig": {
            "gcsSource": {
            "inputUri": "gs://GLOSSARY_FILE_PATH"
            }
          },
          "entryCount": NUMBER_OF_ENTRIES,
          "submitTime": "2022-04-22T23:16:30.628806944Z",
          "endTime": "2022-04-22T23:41:15.115797Z",
          "displayName": "GLOSSARY_ID"
        },
        "state": "RUNNING",
        "submitTime": "2022-04-22T23:50:24.337964527Z"
      }
    }
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

### Delete a glossary

The following example deletes a glossary.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
  * glossary-id: your glossary ID



HTTP method and URL: 
    
    
    DELETE https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries/glossary-id

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries/glossary-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/us-central1/glossaries/glossary-id" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Go API reference documentation](https://godoc.org/cloud.google.com/go/translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	translate "cloud.google.com/go/translate/apiv3"
    	"cloud.google.com/go/translate/apiv3/translatepb"
    )
    
    // deleteGlossary deletes a glossary.
    func deleteGlossary(w io.Writer, projectID string, location string, glossaryID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// glossaryID := ["glossary-id&qu](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_NewTranslationClient)ot;
    
    	ctx := context.Background()
    	client, err := translate.NewTranslationClient(ctx)
    	if err[ != n](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/apiv3.html#cloud_google_com_go_translate_apiv3_TranslationClient_Close)il {
    		retur&n fmt.Errorf("NewTranslationClient: %w", err)
    	}
    	defer client.Close()
    
    	req := translatepb.DeleteGlossaryRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/glossaries/%s", projectID, location, glossaryID),
    	}
    
    	// The DeleteGlossary operation is async.
    	op, err := client.DeleteGlossary(ctx, req)
    	if err != nil {
    		return fmt.Errorf("DeleteGlossary: %w", err)
    	}
    	fmt.Fprintf(w, "Processing operation name: %q\n", op.Name())
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    
    	fmt.Fprintf(w, "Deleted: %v\n", resp.GetName())
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.translate.v3.[DeleteGlossaryMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DeleteGlossaryMetadata.html);
    import com.google.cloud.translate.v3.[DeleteGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DeleteGlossaryRequest.html);
    import com.google.cloud.translate.v3.[DeleteGlossaryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DeleteGlossaryResponse.html);
    import com.google.cloud.translate.v3.[GlossaryName](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html);
    import com.google.cloud.translate.v3.[TranslationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class DeleteGlossary {
    
      public static void deleteGlossary() throws InterruptedException, ExecutionException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "YOUR-PROJECT-ID";
        String glossaryId = "your-glossary-display-name";
        deleteGlossary(projectId, glossaryId);
      }
    
      // Delete a specific glossary based on the glossary ID
      public static void deleteGlossary(String projectId, String glossaryId)
          throws InterruptedException, ExecutionException, IOException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining b[ackground resources.](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html)
        try (Tran[slationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html) client = TranslationServiceClient.create()) {
          // Supported Locations: `global`, [glossary location], or [model location]
          // Glossaries must be hosted in `us-central1`
          // Custom Models must use the same location as yo[ur model. (u](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html)s-central1)
        [  ](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html)GlossaryName glossaryName = GlossaryName.of(projectId, &quo[t;us-central1"](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DeleteGlossaryRequest.html), glossaryId);
          De[leteGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DeleteGlossaryRequest.html) request =
              DeleteGlossaryRe[quest](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.GlossaryName.html#com_google_cloud_translate_v3_GlossaryName_toString__).newBuilder().setName(glossaryName.toString()).build();
    
          // Start an as<ynchronous request
          OperationFutureDelete>GlossaryResponse, DeleteGlo[ssaryMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.TranslationServiceClient.html#com_google_cloud_translate_v3_TranslationServiceClient_deleteGlossaryAsync__org_jspecify_annotations_Nullable_com_google_cloud_translate_v3_GlossaryName_) future =
              client.deleteGlossaryAsync(request);
    
          System.out.println("W[aiting for operation t](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DeleteGlossaryResponse.html)o complete..."[);
    ](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)      DeleteGlossaryResponse response = future.get();
          Sys[tem](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3.DeleteGlossaryResponse.html#com_google_cloud_translate_v3_DeleteGlossaryResponse_getName__).out.format("Deleted Glossary: %s\n", response.getName());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const location = 'global';
    // const glossaryId = 'YOUR_GLOSSARY_ID';
    
    // Imports the Google Cloud Translation library
    const {TranslationSe[rviceClient](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)} = require('@google-cloud/translate');
    
    // Instantiates a clien[t](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)
    const translationClient = new TranslationServiceClient();
    
    async function deleteGlossary() {
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        name: `projects/${projectId}/locations/${location}/glossaries/${glossaryId}`,
      };
    
      // Delete glossary using a long-running operation
      const [operation] = await translationClient.deleteGlossary(request);
    
      // Wait for operation to complete.
      const [response] = await operation.promise();
    
      console.log(`Deleted glossary: ${response.name}`);
    }
    
    deleteGlossary();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import translate_v3 as translate
    
    
    def delete_glossary(
        project_id: str = "YOUR_PROJECT_ID",
        glossary_id: str = "YOUR_GLOSSARY_ID",
        tim>eout: int = 180,
    ) - translate.Glossary:
        """Delete a specific glossary based on the glossary ID.
    
        Args:
            project_id: The ID of the GCP project that owns the glossary.
            glossary_id: The ID of the glossary to delete.
            timeout: The timeout for this request.
    
        Returns:
            The glossary that was deleted.
        """
        client = translate.TranslationServiceClient()
    
        name = client.glossary_path(project_id, "us-central1", glossary_id)
    
        operation = client.delete_glossary(name=name)
        result = operation.result(timeout)
        print(f"Deleted: {result.name}")
    
        return result
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

## Manage glossary entries

A glossary entry maps a term in one language to a term in another language. You can add new entries to a glossary, list all of the entries for an existing glossary, or modify existing entries.

### Create new entries

Create new entries to add terms to an existing glossary. For unidirectional glossaries, provide a term pair, where one term is in the source language and the other is in the target language. For equivalent term set glossaries, provide a term set, where each item in the set specifies a term and its language code.

### REST

The following examples creates an entry for an equivalent term set glossary. You can create only one entry per request. For more information, see the [glossaryEntries.create](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.glossaries.glossaryEntries/create) method. 

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project.
  * LOCATION: The region where the glossary to update is located, such as `us-central1`.
  * GLOSSARY_ID: The ID of an existing glossary.
  * LANGUAGE_CODE: The [language code](https://docs.cloud.google.com/translate/docs/languages) that specifies the term's language.
  * TERM: The term to add to the glossary.
  * DESCRIPTION: Information about the glossary entry.



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries

Request JSON body: 
    
    
    {
      termsSet: {
       terms: {
         languageCode: "LANGUAGE_CODE",
         text: "TERM"
        },
        ...
      },
      description: "DESCRIPTION"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries/GLOSSARY_ENTRY_ID",
      "termsSet": {
        "terms": [
          {
            "languageCode": "LANGUAGE_CODE",
            "text": "TERM"
          },
          ...
        ]
      },
      "description": "DESCRIPTION"
    }
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

### List glossary entries

List all entries for an existing glossary. This is useful if, for example, you want to check which terms and which languages are in a particular glossary.

### REST

To list all glossary entries, send a GET request with the [glossaryEntries.list](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.glossaries.glossaryEntries/list) method. 

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project.
  * LOCATION: The region where the glossary to update is located, such as `us-central1`.
  * GLOSSARY_ID: The ID of an existing glossary.



HTTP method and URL: 
    
    
    GET https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "glossaryEntries": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries/GLOSSARY_ENTRY_ID",
          "termsSet": {
            "terms": [
              {
                "languageCode": "LANGUAGE_CODE",
                "text": "TERM"
              },
            ...
            ]
          },
          "description": "DESCRIPTION"
        },
        ...
      ]
    }
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

### Get a glossary entry

Get a single entry to view its information.

### REST

To get a single glossary entry, send a GET request with the [glossaryEntries.get](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.glossaries.glossaryEntries/get) method. Use the list method to find the ID of a particular entry. 

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project.
  * LOCATION: The region where the glossary to update is located, such as `us-central1`.
  * GLOSSARY_ID: The ID of an existing glossary.
  * GLOSSARY_ENTRY_ID: The ID of an existing glossary entry.



HTTP method and URL: 
    
    
    GET https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries/GLOSSARY_ENTRY_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries/GLOSSARY_ENTRY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries/GLOSSARY_ENTRY_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries/GLOSSARY_ENTRY_ID",
      "termsSet": {
        "terms": [
          {
            "languageCode": "LANGUAGE_CODE",
            "text": "TERM"
          },
          ...
        ]
      },
      "description": "DESCRIPTION"
    }
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

### Update glossary entries

You can update a single entry or replace all entries in a glossary. To replace all entries, see update a glossary.

To modify an entry in a unidirectional glossary, provide a term pair, where one term is in the source language and the other is in the target language. For equivalent term set glossaries, provide a term set, where each item in the set specifies a term and its language code.

### REST

The following examples updates an entry for an equivalent term set glossary. For more information, see the [glossaryEntries.patch](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.glossaries.glossaryEntries/patch) method. 

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project.
  * LOCATION: The region where the glossary to update is located, such as `us-central1`.
  * GLOSSARY_ID: The ID of an existing glossary that contains the entry to update.
  * GLOSSARY_ENTRY_ID: The ID of the glossary entry to update.
  * LANGUAGE_CODE: The [language code](https://docs.cloud.google.com/translate/docs/languages) that specifies the term's language.
  * TERM: The term to update.
  * DESCRIPTION: Information about the glossary entry.



HTTP method and URL: 
    
    
    PATCH https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries/GLOSSARY_ENTRY_ID

Request JSON body: 
    
    
    {
      termsSet: {
       terms: {
         languageCode: "LANGUAGE_CODE",
         text: "TERM"
        },
        ...
      },
      description: "DESCRIPTION"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries/GLOSSARY_ENTRY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries/GLOSSARY_ENTRY_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries/GLOSSARY_ENTRY_ID",
      "termsSet": {
        "terms": [
          {
            "languageCode": "LANGUAGE_CODE",
            "text": "TERM"
          },
          ...
        ]
      },
      "description": "DESCRIPTION"
    }
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

### Delete a glossary entry

Remove a single glossary entry.

### REST

To delete a single glossary entry, send a DELETE request with the [glossaryEntries.delete](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.glossaries.glossaryEntries/delete) method. Use the list method to find the ID of a particular entry. 

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project.
  * LOCATION: The region where the glossary to update is located, such as `us-central1`.
  * GLOSSARY_ID: The ID of an existing glossary that contains the entry to delete.
  * GLOSSARY_ENTRY_ID: The ID of the glossary entry to delete.



HTTP method and URL: 
    
    
    DELETE https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries/GLOSSARY_ENTRY_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries/GLOSSARY_ENTRY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/LOCATION/glossaries/GLOSSARY_ID/glossaryEntries/GLOSSARY_ENTRY_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

## Additional resources

  * For help on resolving common issues or errors, see the [Troubleshooting](https://docs.cloud.google.com/translate/troubleshooting) page. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
