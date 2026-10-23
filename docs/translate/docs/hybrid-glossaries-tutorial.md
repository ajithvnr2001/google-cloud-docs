---
url: https://docs.cloud.google.com/translate/docs/hybrid-glossaries-tutorial/
title: Translating text from a photo \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:14.211293+00:00
---

# Translating text from a photo  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/hybrid-glossaries-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback 

#  Translating text from a photo Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to detect text in an image, how to personalize translations, and how to generate synthetic speech from text. This tutorial uses Cloud Vision to detect text in an image file. Then, this tutorial shows how to use Cloud Translation to provide a custom translation of the detected text. Finally, this tutorial uses Text-to-Speech to provide machine dictation of the translated text. 

## Objectives

  1. Pass text recognized by the Cloud Vision API to the Cloud Translation API.

  2. Create and use Cloud Translation glossaries to personalize Cloud Translation API translations.

  3. Create an audio representation of translated text using the Text-to-Speech API. 




## Costs

Each Google Cloud API uses a separate pricing structure. 

For pricing details, refer to the [Cloud Vision pricing guide](https://cloud.google.com/vision/pricing/), the [Cloud Translation pricing guide](https://cloud.google.com/translate/pricing), and the [Text-to-Speech pricing guide](https://cloud.google.com/text-to-speech/pricing). 

## Before you begin

Make sure that you have: 

  * A project in the [Google Cloud console](https://console.cloud.google.com/) with the Vision API, the Cloud Translation API, and the Text-to-Speech API [enabled](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis)
  * A basic familiarity with [Python](https://www.python.org/) or [NodeJS](https://nodejs.org/) programming 



## Setting up client libraries

This tutorial uses [Vision](https://docs.cloud.google.com/vision/docs/reference/libraries), [Translation](https://docs.cloud.google.com/translate/docs/reference/libraries), and [Text-to-Speech](https://docs.cloud.google.com/text-to-speech/docs/reference/libraries) client libraries.

To install the relevant client libraries, run the following commands from the terminal.

### Python
    
    
      pip install --upgrade google-cloud-vision
      pip install --upgrade google-cloud-translate
      pip install --upgrade google-cloud-texttospeech
      

### Node.js
    
    
      npm install @google-cloud/vision
      npm install @google-cloud/translate
      npm install @google-cloud/text-to-speech
      

## Setting up permissions for glossary creation

Creating Translation glossaries requires using a service account key with ["Cloud Translation API Editor"](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtranslate) permissions.

To set up a service account key with Cloud Translation API Editor permissions, do the following:

  1. Create a service account:

     1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. Select your project.

     3. Click add**Create Service Account**.

     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name.

     5. Optional: In the **Service account description** field, enter a description for the service account.

     6. Click **Create and continue**.

     7. Click the **Select a role** field and select **Cloud Translation > Cloud Translation API Editor**

     8. Click **Done** to finish creating the service account.

Do not close your browser window. You will use it in the next step.

  2. Download a JSON key for the service account you just created:

     1. In the Google Cloud console, click the email address for the service account that you created.
     2. Click **Keys**.
     3. Click **Add key** , then click **Create new key**.
     4. Click **Create**. A JSON key file is downloaded to your computer.

Make sure to store the key file securely, because it can be used to authenticate as your service account. You can move and rename this file however you would like.

     5. Click **Close**.

  3. In your terminal, set the GOOGLE_APPLICATION_CREDENTIALS variable using the following command. Replace path_to_key with the path to the downloaded JSON file containing your new service account key. 

### Linux or macOS
         
         export GOOGLE_APPLICATION_CREDENTIALS=path_to_key

### Windows
         
         set GOOGLE_APPLICATION_CREDENTIALS=path_to_key




## Importing libraries

This tutorial uses the following system imports and client library imports.

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import html
    import os
    
    # Imports the Google Cloud client libraries
    from google.api_core.exceptions import AlreadyExists
    from google.cloud import texttospeech
    from google.cloud import translate_v3beta1 as translate
    from google.cloud import vision
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const textToSpeech = require('[@google-cloud/text-to-speech](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)');
    const translate = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)').v3beta1;
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Import other required libraries
    const fs = require('fs');
    //const escape = require('escape-html');
    const util = require('util');

## Setting your project ID

You must associate a Google Cloud project with each request to a Google Cloud API. Designate your Google Cloud project by setting the `GCLOUD_PROJECT` environment variable from the terminal.

In the following command, replace project-id with your Google Cloud project ID. Run the following command from the terminal.

### Linux or macOS
    
    
    export GCLOUD_PROJECT=project-id

### Windows
    
    
    set GCLOUD_PROJECT=project-id

## Using Vision to detect text from an image

Use the Vision API to detect and extract text from an image. The Vision API uses [Optical Character Recognition (OCR)](https://docs.cloud.google.com/vision/docs/ocr) to support two text-detection features: detection of dense text, or [`DOCUMENT_TEXT_DETECTION`](https://docs.cloud.google.com/vision/docs/features-list#text-detection), and sparse text detection, or [`TEXT_DETECTION`](https://docs.cloud.google.com/vision/docs/features-list#document-text-detection-dense------------------text--handwriting).

The following code shows how to use the Vision API [`DOCUMENT_TEXT_DETECTION`](https://docs.cloud.google.com/vision/docs/features-list#text-detection) feature to detect text in a photo with dense text.

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def pic_to_text(infile: str) -> str:
        """Detects text in an image file
    
        Args:
        infile: path to image file
    
        Returns:
        String of text detected in image
        """
    
        # Instantiates a client
        client = vision.ImageAnnotatorClient()
    
        # Opens the input image file
        with open(infile, "rb") as image_file:
            content = image_file.read()
    
        image = vision.Image(content=content)
    
        # For dense text, use document_text_detection
        # For less dense text, use text_detection
        response = client.document_text_detection(image=image)
        text = response.full_text_annotation.text
        print(f"Detected text: {text}")
    
        return text

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Detects text in an image file
     *
     * ARGS
     * inputFile: path to image file
     * RETURNS
     * string of text detected in the input image
     **/
    async function picToText(inputFile) {
      // Creates a client
      const client = new vision.ImageAnnotatorClient();
    
      // Performs text detection on the local file
      const [result] = await client.textDetection(inputFile);
      return result.fullTextAnnotation.text;
    }

## Using Translation with glossaries

After extracting text from an image, use [Translation glossaries](https://docs.cloud.google.com/translate/docs/glossary) to personalize the translation of the extracted text. Glossaries provide pre-defined translations that override the Cloud Translation API translations of designated terms.

Glossary use cases include:

  * **Product names:** For example, 'Google Home' must translate to 'Google Home'.

  * **Ambiguous words:** For example, the word 'bat' can mean a piece of sports equipment or an animal. If you know that you are translating words about sports, you might want to use a glossary to feed the Cloud Translation API the sports translation of 'bat', not the animal translation.

  * **Borrowed words:** For example, 'bouillabaisse' in French translates to 'bouillabaisse' in English; the English language borrowed the word 'bouillabaisse' from the French language. An English speaker lacking French cultural context might not know that bouillabaisse is a French fish stew dish. Glossaries can override a translation so that 'bouillabaisse' in French translates to 'fish stew' in English.




### Making a glossary file

The Cloud Translation API accepts TSV, CSV, or TMX glossary files. This tutorial uses a CSV file uploaded to Cloud Storage to define sets of equivalent terms.

To make a glossary CSV file:

  1. **Designate the language of a column** using either [ISO-639](https://wikipedia.org/wiki/ISO_639) or [BCP-47](https://tools.ietf.org/html/bcp47) language codes in the first row of the CSV file. 
         
         fr,en,

  2. **List pairs of equivalent terms** in each row of the CSV file. Separate terms with commas. The following example defines the English translation for several culinary French words. 
         
         fr,en,
         chèvre,goat cheese,
         crème brulée,crème brulée,
         bouillabaisse,fish stew,
         steak frites,steak with french fries,
         

  3. **Define variants of a word**. The Cloud Translation API is case-sensitive and sensitive to special characters such as accented words. Ensure that your glossary handles variations on a word by explicitly defining different spellings of the word. 
         
         fr,en,
         chevre,goat cheese,
         Chevre,Goat cheese,
         chèvre,goat cheese,
         Chèvre,Goat cheese,
         crème brulée,crème brulée,
         Crème brulée,Crème brulée,
         Crème Brulée,Crème Brulée,
         bouillabaisse,fish stew,
         Bouillabaisse,Fish stew,
         steak frites,steak with french fries,
         Steak frites,Steak with french fries,
         Steak Frites,Steak with French Fries,
         

  4. [Upload](https://docs.cloud.google.com/storage/docs/uploading-objects) the glossary to a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets). For the purposes of this tutorial, you do not need to upload a glossary file to a Cloud Storage bucket nor do you need to create a Cloud Storage bucket. Instead, use the publicly-available glossary file created for this tutorial to avoid incurring any Cloud Storage costs. Send the URI of a glossary file in Cloud Storage to the Cloud Translation API to create a glossary resource. The URI of the publicly-available glossary file for this tutorial is [gs://cloud-samples-data/translation/bistro_glossary.csv](https://storage.cloud.google.com/cloud-samples-data/translation/bistro_glossary.csv). To download the glossary, click on the above URI link, but do not open it in a new tab.




### Creating a glossary resource

In order to use a glossary, you must create a glossary resource with the Cloud Translation API. To create a glossary resource, send the URI of a glossary file in Cloud Storage to the Cloud Translation API.

Make sure that you are using a service account key with "Cloud Translation API Editor" permissions and make sure that you have set your project ID from the terminal.

The following function creates a glossary resource. With this glossary resource, you can personalize the translation request in the next step of this tutorial.

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_glossary(
        languages: list,
        project_id: str,
        glossary_name: str,
        glossary_uri: str,
    ) -> str:
        """Creates a GCP glossary resource
        Assumes you've already manually uploaded a glossary to Cloud Storage
    
        Args:
        languages: list of languages in the glossary
        project_id: GCP project id
        glossary_name: name you want to give this glossary resource
        glossary_uri: the uri of the glossary you uploaded to Cloud Storage
    
        Returns:
        name of the created or existing glossary
        """
    
        # Instantiates a client
        client = translate.TranslationServiceClient()
    
        # Designates the data center location that you want to use
        location = "us-central1"
    
        # Set glossary resource name
        name = client.glossary_path(project_id, location, glossary_name)
    
        # Set language codes
        language_codes_set = translate.Glossary.LanguageCodesSet(language_codes=languages)
    
        gcs_source = translate.GcsSource(input_uri=glossary_uri)
    
        input_config = translate.GlossaryInputConfig(gcs_source=gcs_source)
    
        # Set glossary resource information
        glossary = translate.Glossary(
            name=name, language_codes_set=language_codes_set, input_config=input_config
        )
    
        parent = f"projects/{project_id}/locations/{location}"
    
        # Create glossary resource
        # Handle exception for case in which a glossary
        #  with glossary_name already exists
        try:
            operation = client.create_glossary(parent=parent, glossary=glossary)
            operation.result(timeout=90)
            print("Created glossary " + glossary_name + ".")
        except AlreadyExists:
            print(
                "The glossary "
                + glossary_name
                + " already exists. No new glossary was created."
            )
    
        return glossary_name

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /** Creates a GCP glossary resource
     * Assumes you've already manually uploaded a glossary to Cloud Storage
     *
     * ARGS
     * languages: list of languages in the glossary
     * projectId: GCP project id
     * glossaryName: name you want to give this glossary resource
     * glossaryUri: the uri of the glossary you uploaded to Cloud Storage
     * RETURNS
     * nothing
     **/
    async function createGlossary(
      languages,
      projectId,
      glossaryName,
      glossaryUri
    ) {
      // Instantiates a client
      const translationClient = await new translate.TranslationServiceClient();
    
      // Construct glossary
      const glossary = {
        languageCodesSet: {
          languageCodes: languages,
        },
        inputConfig: {
          gcsSource: {
            inputUri: glossaryUri,
          },
        },
        name: translationClient.glossaryPath(
          projectId,
          'us-central1',
          glossaryName
        ),
      };
    
      // Construct request
      const request = {
        parent: translationClient.locationPath(projectId, 'us-central1'),
        glossary: glossary,
      };
    
      // Create glossary using a long-running operation.
      try {
        const [operation] = await translationClient.createGlossary(request);
        // Wait for operation to complete.
        await operation.promise();
        console.log('Created glossary ' + glossaryName + '.');
      } catch (AlreadyExists) {
        console.log(
          'The glossary ' +
            glossaryName +
            ' already exists. No new glossary was created.'
        );
      }
    }

### Translating with glossaries

Once you create a glossary resource, you can use the glossary resource to personalize translations of text that you send to the Cloud Translation API.

The following function uses your previously-created glossary resource to personalize the translation of text.

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def translate_text(
        text: str,
        source_language_code: str,
        target_language_code: str,
        project_id: str,
        glossary_name: str,
    ) -> str:
        """Translates text to a given language using a glossary
    
        Args:
        text: String of text to translate
        source_language_code: language of input text
        target_language_code: language of output text
        project_id: GCP project id
        glossary_name: name you gave your project's glossary
            resource when you created it
    
        Return:
        String of translated text
        """
    
        # Instantiates a client
        client = translate.TranslationServiceClient()
    
        # Designates the data center location that you want to use
        location = "us-central1"
    
        glossary = client.glossary_path(project_id, location, glossary_name)
    
        glossary_config = translate.TranslateTextGlossaryConfig(glossary=glossary)
    
        parent = f"projects/{project_id}/locations/{location}"
    
        result = client.translate_text(
            request={
                "parent": parent,
                "contents": [text],
                "mime_type": "text/plain",  # mime types: text/plain, text/html
                "source_language_code": source_language_code,
                "target_language_code": target_language_code,
                "glossary_config": glossary_config,
            }
        )
    
        # Extract translated text from API response
        return result.glossary_translations[0].translated_text

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Translates text to a given language using a glossary
     *
     * ARGS
     * text: String of text to translate
     * sourceLanguageCode: language of input text
     * targetLanguageCode: language of output text
     * projectId: GCP project id
     * glossaryName: name you gave your project's glossary
     *     resource when you created it
     * RETURNS
     * String of translated text
     **/
    async function translateText(
      text,
      sourceLanguageCode,
      targetLanguageCode,
      projectId,
      glossaryName
    ) {
      // Instantiates a client
      const translationClient = new translate.TranslationServiceClient();
      const glossary = translationClient.glossaryPath(
        projectId,
        'us-central1',
        glossaryName
      );
      const glossaryConfig = {
        glossary: glossary,
      };
      // Construct request
      const request = {
        parent: translationClient.locationPath(projectId, 'us-central1'),
        contents: [text],
        mimeType: 'text/plain', // mime types: text/plain, text/html
        sourceLanguageCode: sourceLanguageCode,
        targetLanguageCode: targetLanguageCode,
        glossaryConfig: glossaryConfig,
      };
    
      // Run request
      const [response] = await translationClient.translateText(request);
      // Extract the string of translated text
      return response.glossaryTranslations[0].translatedText;
    }

## Using Text-to-Speech with Speech Synthesis Markup Language

Now that you have personalized a translation of image-detected text, you are ready to use the Text-to-Speech API. The Text-to-Speech API can create synthetic audio of your translated text.

The Text-to-Speech API generates synthetic audio from either a string of plain text or a string of text marked up with [Speech Synthesis Markup Language (SSML)](https://docs.cloud.google.com/text-to-speech/docs/ssml). SSML is a markup language which supports annotating text with [SSML tags](https://docs.cloud.google.com/text-to-speech/docs/ssml#support-for-ssml-elements). You can use SSML tags to influence how the Text-to-Speech API [formats synthetic speech creation](https://docs.cloud.google.com/text-to-speech/docs/ssml-tutorial).

The following function converts a string of SSML to an MP3 file of synthetic speech.

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def text_to_speech(text: str, outfile: str) -> str:
        """Converts plaintext to SSML and
        generates synthetic audio from SSML
    
        Args:
    
        text: text to synthesize
        outfile: filename to use to store synthetic audio
    
        Returns:
        String of synthesized audio
        """
    
        # Replace special characters with HTML Ampersand Character Codes
        # These Codes prevent the API from confusing text with
        # SSML commands
        # For example, '<' --> '&lt;' and '&' --> '&amp;'
        escaped_lines = html.escape(text)
    
        # Convert plaintext to SSML in order to wait two seconds
        #   between each line in synthetic speech
        ssml = "<speak>{}</speak>".format(
            escaped_lines.replace("\n", '\n<break time="2s"/>')
        )
    
        # Instantiates a client
        client = texttospeech.TextToSpeechClient()
    
        # Sets the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(ssml=ssml)
    
        # Builds the voice request, selects the language code ("en-US") and
        # the SSML voice gender ("MALE")
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE
        )
    
        # Selects the type of audio file to return
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
    
        # Performs the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
    
        request = texttospeech.SynthesizeSpeechRequest(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
    
        response = client.synthesize_speech(request=request)
    
        # Writes the synthetic audio to the output file.
        with open(outfile, "wb") as out:
            out.write(response.audio_content)
            print("Audio content written to file " + outfile)

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Generates synthetic audio from plaintext tagged with SSML.
     *
     * Given the name of a text file and an output file name, this function
     * tags the text in the text file with SSML. This function then
     * calls the Text-to-Speech API. The API returns a synthetic audio
     * version of the text, formatted according to the SSML commands. This
     * function saves the synthetic audio to the designated output file.
     *
     * ARGS
     * text: String of plaintext
     * outFile: String name of file under which to save audio output
     * RETURNS
     * nothing
     *
     */
    async function syntheticAudio(text, outFile) {
      // Replace special characters with HTML Ampersand Character Codes
      // These codes prevent the API from confusing text with SSML tags
      // For example, '<' --> '&lt;' and '&' --> '&amp;'
      let escapedLines = text.replace(/&/g, '&amp;');
      escapedLines = escapedLines.replace(/"/g, '&quot;');
      escapedLines = escapedLines.replace(/</g, '&lt;');
      escapedLines = escapedLines.replace(/>/g, '&gt;');
    
      // Convert plaintext to SSML
      // Tag SSML so that there is a 2 second pause between each address
      const expandedNewline = escapedLines.replace(/\n/g, '\n<break time="2s"/>');
      const ssmlText = '<speak>' + expandedNewline + '</speak>';
    
      // Creates a client
      const client = new textToSpeech.TextToSpeechClient();
    
      // Constructs the request
      const request = {
        // Select the text to synthesize
        input: {ssml: ssmlText},
        // Select the language and SSML Voice Gender (optional)
        voice: {languageCode: 'en-US', ssmlGender: 'MALE'},
        // Select the type of audio encoding
        audioConfig: {audioEncoding: 'MP3'},
      };
    
      // Performs the Text-to-Speech request
      const [response] = await client.synthesizeSpeech(request);
      // Write the binary audio content to a local file
      const writeFile = util.promisify(fs.writeFile);
      await writeFile(outFile, response.audioContent, 'binary');
      console.log('Audio content written to file ' + outFile);
    }

## Putting it all together

In the previous steps, you defined functions in `hybrid_glossaries.py` that use Vision, Translation, and Text-to-Speech. Now, you are ready to use these functions to generate synthetic speech of translated text from the following photo.

![](https://docs.cloud.google.com/static/translate/images/hybrid_glossaries_example.png)

The following code calls functions defined in `hybrid_glossaries.py` to:

  * create a Cloud Translation API glossary resource

  * use the Vision API to detect text in the above image

  * perform a Cloud Translation API glossary translation of the detected text

  * generate Text-to-Speech synthetic speech of the translated text




### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def main() -> None:
        """This method is called when the tutorial is run in the Google Cloud
        Translation API. It creates a glossary, translates text to
        French, and speaks the translated text.
    
        Args:
        None
    
        Returns:
        None
        """
        # Photo from which to extract text
        infile = "resources/example.png"
        # Name of file that will hold synthetic speech
        outfile = "resources/example.mp3"
    
        # Defines the languages in the glossary
        # This list must match the languages in the glossary
        #   Here, the glossary includes French and English
        glossary_langs = ["fr", "en"]
        # Name that will be assigned to your project's glossary resource
        glossary_name = "bistro-glossary"
        # uri of .csv file uploaded to Cloud Storage
        glossary_uri = "gs://cloud-samples-data/translation/bistro_glossary.csv"
    
        created_glossary_name = create_glossary(
            glossary_langs, PROJECT_ID, glossary_name, glossary_uri
        )
    
        # photo -> detected text
        text_to_translate = pic_to_text(infile)
        # detected text -> translated text
        text_to_speak = translate_text(
            text_to_translate, "fr", "en", PROJECT_ID, created_glossary_name
        )
        # translated text -> synthetic audio
        text_to_speech(text_to_speak, outfile)

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    await createGlossary(glossaryLangs, projectId, glossaryName, glossaryUri);
    const text = await picToText(inFile);
    const translatedText = await translateText(
      text,
      'fr',
      'en',
      projectId,
      glossaryName
    );
    syntheticAudio(translatedText, outFile);

### Running the code

To run the code, enter the following command in terminal in the directory where your code is located: 

### Python
    
    
    python hybrid_tutorial.py
      

### Node.js
    
    
      node hybridGlossaries.js
      

The following output appears: 
    
    
    Created glossary bistro-glossary.
    Audio content written to file resources/example.mp3

After running the code, navigate into the resources directory from the hybrid_glossaries directory. Check the resources directory for an `example.mp3` file.

Listen to the following audio clip to check that your `example.mp3` file sounds the same.

Your browser does not support the audio element.   


## Troubleshooting error messages

  * 403 IAM permission 'cloudtranslate.glossaries.create' denied.

Using a service account key without "Cloud Translation API Editor" permissions raises this exception.

  * KeyError: 'GCLOUD_PROJECT'

Not setting your GCLOUD_PROJECT variable generates this error.

  * 400 Invalid resource name project id

Either using a glossary name which contains characters other than lowercase letters, digits, periods, a colon, or hyphens, or using a service account key without "Cloud Translation API Editor" permissions raises this exception.

  * File filename was not found.

Setting the GOOGLE_APPLICATION_CREDENTIALS variable to an invalid filepath raises this exception.

  * Could not automatically determine credentials. Please set GOOGLE_APPLICATION_CREDENTIALS or explicitly create credentials and re-run the application

Not setting the GOOGLE_APPLICATION_CREDENTIALS variable raises this exception.

  * Forbidden: 403 POST API has not been used or is disabled

Calling the Cloud Translation API, the Cloud Vision API, or the Text-to-Speech API without [enabling their APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) generates this warning.

  * AttributeError: 'module' object has no attribute 'escape'

Python 2.7.10 or earlier is not compatible with `HTML`. To fix this error, use a [Python virtual environment](https://docs.python.org/3/library/venv.html). The virtual environment will use the newest version of Python.

  * UnicodeEncodeError

Python 2.7.10 or earlier is not compatible with `HTML`. To fix this error, use a [Python virtual environment](https://docs.python.org/3/library/venv.html). The virtual environment will use the newest version of Python.




## Cleaning up

Use the [Google Cloud console](https://console.cloud.google.com/) to delete your project if you do not need it. Deleting your project prevents incurring additional charges to your Cloud Billing account for the resources used in this tutorial.

### Deleting your project

  1. In the [Google Cloud console](https://console.cloud.google.com/), go to the Projects page.
  2. In the project list, select the project you want to delete and click **Delete**.
  3. In the dialog box, type the project ID, and click **Shut down** to delete the project.



## What's next

Congratulations! You just used Vision OCR to detect text in an image. Then, you created a Translation glossary and performed a translated with that glossary. Afterwards, you used Text-to-Speech to generate synthetic audio of the translated text.

To build on your knowledge of Vision, Translation, and Text-to-Speech:

  * Make your own glossary. Learn how to [create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) and to [upload your glossary CSV file to the bucket](https://docs.cloud.google.com/storage/docs/uploading-objects).
  * Experiment with other ways to use [Translation glossaries](https://docs.cloud.google.com/translate/docs/glossary).
  * Learn how to [use Cloud Storage with Cloud Vision OCR](https://docs.cloud.google.com/functions/docs/tutorials/ocr).
  * Learn more about how to [use SSML with Text-to-Speech](https://docs.cloud.google.com/text-to-speech/docs/ssml-tutorial).
  * Learn how to use the Vision API [`imageContext` field](https://docs.cloud.google.com/vision/docs/handwriting#specify_the_language_optional) to pass along additional context about a photo when using Vision OCR.
  * Explore [community tutorials](https://docs.cloud.google.com/community/tutorials).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
