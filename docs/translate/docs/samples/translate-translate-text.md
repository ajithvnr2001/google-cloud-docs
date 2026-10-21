---
url: https://docs.cloud.google.com/translate/docs/samples/translate-translate-text/
title: Translating text \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:11.903130+00:00
---

# Translating text  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/samples/translate-translate-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Samples ](https://docs.cloud.google.com/translate/docs/samples)



#  Translating text Stay organized with collections  Save and categorize content based on your preferences. 

This example demonstrates how to use the Google Cloud Translation API to translate text from one language to another. The code shows how to create a client, set the target language, and translate a given text string. Error handling is included to manage potential issues such as invalid language codes and API errors. The function returns the translated text or an error if the translation fails. To use this code, you will need to set up authentication with the Google Cloud Translation API and have the necessary credentials configured in your environment. Remember to replace with your own text to translate.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Translation client libraries](https://docs.cloud.google.com/translate/docs/reference/libraries/v2/overview-v2)
  * [Translate text with Cloud Translation](https://docs.cloud.google.com/translate/docs/translate-text)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Go API reference documentation](https://godoc.org/cloud.google.com/go/translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/translate"
    	"golang.org/x/text/language"
    )
    
    // translateText translates the given text into the specified targetLanguage. sourceLanguage
    // is optional. If empty, the API will attempt to detect the source language automatically.
    // targetLanguage and sourceLanguage should follow ISO 639 language code of the input text
    // (e.g., 'fr' for French)
    //
    // Find a list of supported languages and codes here:
    // https://cloud.google.com/translate/docs/languages#nmt
    func translateText(w io.Writer, targetLanguage, sourceLanguage, text string) error {
    	ctx := context.Background()
    
    	// Create new Translate client.
    	client, err := translate.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("translate.NewClient error: %w", err)
    	}
    	defer client.Close()
    
    	// Get required tag by parsing the target language.
    	targetLang, err := language.Parse(targetLanguage)
    	if err != nil {
    		return fmt.Errorf("language.Parse: %w", err)
    	}
    
    	options := &translate.[Options](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_Options){}
    
    	if sourceLanguage != "" {
    		sourceLang, err := language.Parse(sourceLanguage)
    		if err != nil {
    			return fmt.Errorf("language.Parse: %w", err)
    		}
    		options = &translate.[Options](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_Options){
    			Source: sourceLang,
    		}
    	}
    
    	// Find more information about translate function here:
    	// https://pkg.go.dev/cloud.google.com/go/translate#Client.Translate
    	resp, err := client.[Translate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_Client_Translate)(ctx, []string{text}, targetLang, options)
    	if err != nil {
    		return fmt.Errorf("client.Translate error: %w", err)
    	}
    	if len(resp) == 0 {
    		return fmt.Errorf("client.Translate returned empty response to text: %s", text)
    	}
    
    	// Print results to buffer.
    	fmt.Fprintf(w, "Input Text: %s\n", resp[0].[Text](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_HTML_Text))
    	fmt.Fprintf(w, "Translated Test: %s\n", text)
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // TODO(developer): Uncomment these lines.
    // import com.google.cloud.translate.*;
    // Translate translate = TranslateOptions.getDefaultInstance().getService();
    
    Translation translation = translate.translate("¡Hola Mundo!");
    System.out.printf("Translated Text:\n\t%s\n", translation.getTranslatedText());

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const {Translate} = require('[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)').v2;
    
    // Creates a client
    const translate = new [Translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/v2.translate.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const text = 'The text to translate, e.g. Hello, world!';
    // const target = 'The target language, e.g. ru';
    
    async function translateText() {
      // Translates the text into the target language. "text" can be a string for
      // translating a single piece of text, or an array of strings for translating
      // multiple texts.
      let [translations] = await [translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/v2.translate.html).[translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/v2.translate.html)(text, target);
      translations = Array.isArray(translations) ? translations : [translations];
      console.log('Translations:');
      translations.forEach((translation, i) => {
        console.log(`${text[i]} => (${target}) ${translation}`);
      });
    }
    
    translateText();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/translate/v2/translateclient). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Translate\TranslateClient;
    
    /**
     * @param string $text The text to translate.
     * @param string $targetLanguage Language to translate to.
     */
    function translate(string $text, string $targetLanguage): void
    {
        /** Uncomment and populate these variables in your code */
        // $text = 'The text to translate.';
        // $targetLanguage = 'ja';  // Language to translate to
    
        $translate = new TranslateClient();
        $result = $translate->translate($text, [
            'target' => $targetLanguage,
        ]);
        print("Source language: $result[source]\n");
        print("Translation: $result[text]\n");
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def translate_text(
        text: str | bytes | list[str] = "¡Hola amigos y amigas!",
        target_language: str = "en",
        source_language: str | None = None,
    ) -> dict:
        """Translates a given text into the specified target language.
    
        Find a list of supported languages and codes here:
        https://cloud.google.com/translate/docs/languages#nmt
    
        Args:
            text: The text to translate. Can be a string, bytes or a list of strings.
                  If bytes, it will be decoded as UTF-8.
            target_language: The ISO 639 language code to translate the text into
                             (e.g., 'en' for English, 'es' for Spanish).
            source_language: Optional. The ISO 639 language code of the input text
                             (e.g., 'fr' for French). If None, the API will attempt
                             to detect the source language automatically.
    
        Returns:
            A dictionary containing the translation results.
        """
    
        from google.cloud import translate_v2 as translate
    
        translate_client = translate.Client()
    
        if isinstance(text, bytes):
            text = [text.decode("utf-8")]
    
        if isinstance(text, str):
            text = [text]
    
        # If a string is supplied, a single dictionary will be returned.
        # In case a list of strings is supplied, this method
        # will return a list of dictionaries.
    
        # Find more information about translate function here:
        # https://cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client#google_cloud_translate_v2_client_Client_translate
        results = translate_client.translate(
            values=text,
            target_language=target_language,
            source_language=source_language
        )
    
        for result in results:
            if "detectedSourceLanguage" in result:
                print(f"Detected source language: {result['detectedSourceLanguage']}")
    
            print(f"Input text: {result['input']}")
            print(f"Translated text: {result['translatedText']}")
            print()
    
        return results

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtranslation). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
