---
url: https://docs.cloud.google.com/vision/docs/samples/vision-image-property-detection-gcs/
title: Detect image properties in a Cloud Storage file \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:25.273752+00:00
---

# Detect image properties in a Cloud Storage file  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-image-property-detection-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Detect image properties in a Cloud Storage file Stay organized with collections  Save and categorize content based on your preferences. 

Perform image properties detection on a file stored in Cloud Storage.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Detect image properties](https://docs.cloud.google.com/vision/docs/detecting-properties)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // detectProperties gets image properties from the Vision API for an image at the given file path.
    func detectPropertiesURI(w io.Writer, file string) error {
    	ctx := context.Background()
    
    	client, err := vision.NewImageAnnotatorClient(ctx)
    	if err != nil {
    		return err
    	}
    
    	image := vision.NewImageFromURI(file)
    	props, err := client.DetectImageProperties(ctx, image, nil)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintln(w, "Dominant colors:")
    	for _, quantized := range props.DominantColors.Colors {
    		color := quantized.Color
    		r := int(color.Red) & 0xff
    		g := int(color.Green) & 0xff
    		b := int(color.Blue) & 0xff
    		fmt.Fprintf(w, "%2.1f%% - #%02x%02x%02x\n", quantized.PixelFraction*100, r, g, b)
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.vision.v1.[AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html);
    import com.google.cloud.vision.v1.[AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html);
    import com.google.cloud.vision.v1.[BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html);
    import com.google.cloud.vision.v1.[ColorInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ColorInfo.html);
    import com.google.cloud.vision.v1.[DominantColorsAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.DominantColorsAnnotation.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.cloud.vision.v1.[ImageSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class DetectPropertiesGcs {
    
      public static void detectPropertiesGcs() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String filePath = "gs://your-gcs-bucket/path/to/image/file.jpg";
        detectPropertiesGcs(filePath);
      }
    
      // Detects image properties such as color frequency from the specified remote image on Google
      // Cloud Storage.
      public static void detectPropertiesGcs(String gcsPath) throws IOException {
        List<AnnotateImageRequest> requests = new ArrayList<>();
    
        [ImageSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html) imgSource = [ImageSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html).newBuilder().[setGcsImageUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.Builder.html#com_google_cloud_vision_v1_ImageSource_Builder_setGcsImageUri_java_lang_String_)(gcsPath).build();
        [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html) img = [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html).newBuilder().[setSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.Builder.html#com_google_cloud_vision_v1_Image_Builder_setSource_com_google_cloud_vision_v1_ImageSource_)(imgSource).build();
        [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html) feat = [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).newBuilder().setType([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).Type.IMAGE_PROPERTIES).build();
        [AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html) request =
            [AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html).newBuilder().addFeatures(feat).setImage(img).build();
        requests.add(request);
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html) client = [ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html).create()) {
          [BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html) response = client.batchAnnotateImages(requests);
          List<AnnotateImageResponse> responses = response.[getResponsesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html#com_google_cloud_vision_v1_BatchAnnotateImagesResponse_getResponsesList__)();
    
          for ([AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html) res : responses) {
            if (res.hasError()) {
              System.out.format("Error: %s%n", res.getError().getMessage());
              return;
            }
    
            // For full list of available annotations, see http://g.co/cloud/vision/docs
            [DominantColorsAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.DominantColorsAnnotation.html) colors = res.getImagePropertiesAnnotation().getDominantColors();
            for ([ColorInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ColorInfo.html) color : colors.[getColorsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.DominantColorsAnnotation.html#com_google_cloud_vision_v1_DominantColorsAnnotation_getColorsList__)()) {
              System.out.format(
                  "fraction: %f%nr: %f, g: %f, b: %f%n",
                  color.getPixelFraction(),
                  color.getColor().getRed(),
                  color.getColor().getGreen(),
                  color.getColor().getBlue());
            }
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client libraries
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const bucketName = 'Bucket where the file resides, e.g. my-bucket';
    // const fileName = 'Path to file within bucket, e.g. path/to/image.png';
    
    // Performs property detection on the gcs file
    const [result] = await client.imageProperties(
      `gs://${bucketName}/${fileName}`
    );
    const colors = result.imagePropertiesAnnotation.dominantColors.colors;
    colors.forEach(color => console.log(color));

### PHP

Before trying this sample, follow the PHP setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace Google\Cloud\Samples\Vision;
    
    use Google\Cloud\Vision\V1\Client\ImageAnnotatorClient;
    
    /**
     * @param string $path GCS path to the image, e.g. "gs://path/to/your/image.jpg"
     */
    function detect_image_property_gcs(string $path)
    {
        $imageAnnotator = new ImageAnnotatorClient();
    
        # annotate the image
        $response = $imageAnnotator->imagePropertiesDetection($path);
        $props = $response->getImagePropertiesAnnotation();
    
        if ($props) {
            print('Properties:' . PHP_EOL);
            foreach ($props->getDominantColors()->getColors() as $colorInfo) {
                printf('Fraction: %s' . PHP_EOL, $colorInfo->getPixelFraction());
                $color = $colorInfo->getColor();
                printf('Red: %s' . PHP_EOL, $color->getRed());
                printf('Green: %s' . PHP_EOL, $color->getGreen());
                printf('Blue: %s' . PHP_EOL, $color->getBlue());
                print(PHP_EOL);
            }
        } else {
            print('No Results.' . PHP_EOL);
        }
    
        $imageAnnotator->close();
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_properties_uri(uri):
        """Detects image properties in the file located in Google Cloud Storage or
        on the Web."""
        from google.cloud import vision
    
        client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)()
        image.source.image_uri = uri
    
        response = client.image_properties(image=image)
        props = response.image_properties_annotation
        print("Properties:")
    
        for color in props.dominant_colors.colors:
            print(f"frac: {color.pixel_fraction}")
            print(f"\tr: {color.color.red}")
            print(f"\tg: {color.color.green}")
            print(f"\tb: {color.color.blue}")
            print(f"\ta: {color.color.alpha}")
    
        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
