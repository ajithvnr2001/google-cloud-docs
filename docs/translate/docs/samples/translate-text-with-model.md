---
url: https://docs.cloud.google.com/translate/docs/samples/translate-text-with-model/
title: Translate strings (Basic edition) \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:41.620840+00:00
---

# Translate strings (Basic edition)  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/samples/translate-text-with-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Samples ](https://docs.cloud.google.com/translate/docs/samples)



#  Translate strings (Basic edition) Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates translating strings by using Cloud Translation - Basic (v2).

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Go API reference documentation](https://godoc.org/cloud.google.com/go/translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/translate"
    	"golang.org/x/text/language"
    )
    
    func translateTextWithModel(targetLanguage, text, model string) (string, error) {
    	// targetLanguage := "ja"
    	// text := "The Go Gopher is cute"
    	// model := "nmt"
    
    	ctx := context.Background()
    
    	lang, err := language.Parse(targetLanguage)
    	if err != nil {
    		return "", fmt.Errorf("language.Parse: %w", err)
    	}
    
    	client, err := translate.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_Client_NewClient)(ctx)
    	if err != nil {
    		return "", fmt.Errorf("translate.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	resp, err := client.[Translate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_Client_Translate)(ctx, []string{text}, lang, &translate.[Options](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_Options){
    		Model: model, // Either "nmt" or "base".
    	})
    	if err != nil {
    		return "", fmt.Errorf("Translate: %w", err)
    	}
    	if len(resp) == 0 {
    		return "", nil
    	}
    	return resp[0].[Text](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/translate/latest/index.html#cloud_google_com_go_translate_HTML_Text), nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Translation translation =
        translate.translate(
            "Hola Mundo!",
            Translate.TranslateOption.sourceLanguage("es"),
            Translate.TranslateOption.targetLanguage("de"),
            // Use "base" for standard edition, "nmt" for the premium model.
            Translate.TranslateOption.model("nmt"));
    
    System.out.printf("TranslatedText:\nText: %s\n", translation.getTranslatedText());

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
    // const model = 'The model to use, e.g. nmt';
    
    async function translateTextWithModel() {
      const options = {
        // The target language, e.g. "ru"
        to: target,
        // Make sure your project is on the allow list.
        // Possible values are "base" and "nmt"
        model: model,
      };
    
      // Translates the text into the target language. "text" can be a string for
      // translating a single piece of text, or an array of strings for translating
      // multiple texts.
      let [translations] = await [translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/v2.translate.html).[translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/v2.translate.html)(text, options);
      translations = Array.isArray(translations) ? translations : [translations];
      console.log('Translations:');
      translations.forEach((translation, i) => {
        console.log(`${text[i]} => (${target}) ${translation}`);
      });
    }
    
    translateTextWithModel();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/translate/v2/translateclient). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Translate\TranslateClient;
    
    /**
     * @param string $text The text to translate.
     * @param string $targetLanguage Language to translate to.
     */
    function translate_with_model(string $text, string $targetLanguage): void
    {
        $model = 'nmt';  // "base" for standard edition, "nmt" for premium
        $translate = new TranslateClient();
        $result = $translate->translate($text, [
            'target' => $targetLanguage,
            'model' => $model,
        ]);
        print("Source language: $result[source]\n");
        print("Translation: $result[text]\n");
        print("Model: $result[model]\n");
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def translate_text_with_model(target: str, text: str, model: str = "nmt") -> dict:
        """Translates text into the target language.
    
        Make sure your project is allowlisted.
    
        Target must be an ISO 639-1 language code.
        See https://g.co/cloud/translate/v2/translate-reference#supported_languages
        """
        from google.cloud import translate_v2 as translate
    
        translate_client = translate.Client()
    
        if isinstance(text, bytes):
            text = text.decode("utf-8")
    
        # Text can also be a sequence of strings, in which case this method
        # will return a sequence of results for each text.
        result = translate_client.translate(text, target_language=target, model=model)
    
        print("Text: {}".format(result["input"]))
        print("Translation: {}".format(result["translatedText"]))
        print("Detected source language: {}".format(result["detectedSourceLanguage"]))
    
        return result
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudtranslation). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
