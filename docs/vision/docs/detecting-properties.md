---
url: https://docs.cloud.google.com/vision/docs/detecting-properties/
title: Detect image properties \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:38.143853+00:00
---

# Detect image properties  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/detecting-properties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/docs/features-list)



Send feedback 

#  Detect image properties Stay organized with collections  Save and categorize content based on your preferences. 

The **Image Properties** feature detects general attributes of the image, such as dominant color.

**Note:** The Vision API now supports offline **asynchronous batch image annotation** for all features. This asynchronous request supports up to 2000 image files and returns response JSON files that are stored in your Cloud Storage bucket. For more information about this feature, refer to [Offline batch image annotation](https://docs.cloud.google.com/vision/docs/batch). 

![Bali image](https://docs.cloud.google.com/static/vision/docs/images/bali_small.jpeg)_Image credit_ : [Jeremy Bishop](https://unsplash.com/photos/QUwLZNchflk) on [Unsplash](https://unsplash.com/). 

**Dominant colors detected:**

![dominant colors detected in Bali image](https://docs.cloud.google.com/static/vision/docs/images/bali_colors.png)

## Image property detection requests

### Set up your Google Cloud project and authentication

If you have not created a Google Cloud project, do so now. Expand this section for instructions. 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Vision API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=vision.googleapis.com)

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

  10. Enable the Vision API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=vision.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




### Detect Image Properties in a local image

You can use the Vision API to perform feature detection on a local image file.

For REST requests, send the contents of the image file as a [base64 encoded](https://docs.cloud.google.com/vision/docs/base64) string in the body of your request.

For `gcloud` and client library requests, specify the path to a local image in your request. 

The [ `ColorInfo`](https://docs.cloud.google.com/vision/docs/reference/rest/v1/images/annotate#colorinfo) field does not carry information about the [absolute color space](https://en.wikipedia.org/wiki/Color_space) that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB, DCI-P3, BT.2020, etc.). By default, applications should assume the [sRGB](https://en.wikipedia.org/wiki/SRGB) color space. 

### REST

Before using any of the request data, make the following replacements: 

  * BASE64_ENCODED_IMAGE: The base64 representation (ASCII string) of your binary image data. This string should look similar to the following string: 
    * `/9j/4QAYRXhpZgAA...9tAVx/zDQDlGxn//2Q==`
Visit the [base64 encode](https://docs.cloud.google.com/vision/docs/base64) topic for more information.
  * RESULTS_INT: (Optional) An integer value of results to return. If you omit the `"maxResults"` field and its value, the API returns the default value of 10 results. This field does not apply to the following feature types: `TEXT_DETECTION`, `DOCUMENT_TEXT_DETECTION`, or `CROP_HINTS`. 
  * PROJECT_ID: Your Google Cloud project ID.



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/images:annotate

Request JSON body: 
    
    
    {
      "requests": [
        {
          "image": {
            "content": "BASE64_ENCODED_IMAGE"
          },
          "features": [
            {
              "maxResults": RESULTS_INT,
              "type": "IMAGE_PROPERTIES"
            },
          ]
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://vision.googleapis.com/v1/images:annotate"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://vision.googleapis.com/v1/images:annotate" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

**Response:**

**Note: Zero coordinate values omitted.** When the API detects a coordinate ("x" or "y") value of 0, **_that coordinate is omitted in the JSON response_**. Thus, a response with a bounding poly around the entire image would be   
**[{},{"x": 100},{"x": 100,"y": 100},{"y": 100}] for an image that is 100 pixels by 100 pixels**. For more information, see the [API Reference documentation](https://cloud.google.com/vision/docs/reference/rest/v1/images/annotate#boundingpoly). 

#### Response
    
    
    {
      "responses": [
        {
          "imagePropertiesAnnotation": {
            "dominantColors": {
              "colors": [
                {
                  "color": {
                    "red": 243,
                    "green": 177,
                    "blue": 133
                  },
                  "score": 0.18074834,
                  "pixelFraction": 0.013533333
                },
                {
                  "color": {
                    "red": 204,
                    "green": 205,
                    "blue": 213
                  },
                  "score": 0.092455424,
                  "pixelFraction": 0.19266666
                },
                {
                  "color": {
                    "red": 114,
                    "green": 77,
                    "blue": 64
                  },
                  "score": 0.090447456,
                  "pixelFraction": 0.034133334
                },
                {
                  "color": {
                    "red": 224,
                    "green": 57,
                    "blue": 64
                  },
                  "score": 0.010952942,
                  "pixelFraction": 0.014266667
                },
                {
                  "color": {
                    "red": 248,
                    "green": 125,
                    "blue": 130
                  },
                  "score": 0.006984347,
                  "pixelFraction": 0.0057333335
                },
                {
                  "color": {
                    "red": 150,
                    "green": 107,
                    "blue": 92
                  },
                  "score": 0.081589326,
                  "pixelFraction": 0.019666666
                },
                {
                  "color": {
                    "red": 233,
                    "green": 185,
                    "blue": 158
                  },
                  "score": 0.08035342,
                  "pixelFraction": 0.0122
                },
                {
                  "color": {
                    "red": 221,
                    "green": 221,
                    "blue": 226
                  },
                  "score": 0.045200635,
                  "pixelFraction": 0.202
                },
                {
                  "color": {
                    "red": 105,
                    "green": 77,
                    "blue": 75
                  },
                  "score": 0.030223774,
                  "pixelFraction": 0.013866667
                },
                {
                  "color": {
                    "red": 189,
                    "green": 145,
                    "blue": 123
                  },
                  "score": 0.028689377,
                  "pixelFraction": 0.0069333334
                }
              ]
            }
          },
          "cropHintsAnnotation": {
            "cropHints": [
              {
                "boundingPoly": {
                  "vertices": [
                    {},
                    {
                      "x": 2549
                    },
                    {
                      "x": 2549,
                      "y": 1699
                    },
                    {
                      "y": 1699
                    }
                  ]
                },
                "confidence": 0.79999995,
                "importanceFraction": 1
              }
            ]
          }
        }
      ]
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // detectProperties gets image properties from the Vision API for an image at the given file path.
    func detectProperties(w io.Writer, file string) error {
    	ctx := context.Background()
    
    	client, err := vision.NewImageAnnotatorClient(ctx)
    	if err != nil {
    		return err
    	}
    
    	f, err := os.Open(file)
    	if err != nil {
    		return err
    	}
    	defer f.Close()
    
    	image, err := vision.NewImageFromReader(f)
    	if err != nil {
    		return err
    	}
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

Before trying this sample, follow the Java setup instructions in the [Vision API Quickstart Using Client Libraries](https://docs.cloud.google.com/vision/docs/detect-labels-image-client-libraries). For more information, see the [ Vision API Java reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview).

**Note:** For Java **Spring framework** users, [Spring Cloud Google Cloud](https://docs.cloud.google.com/vision/docs/adding-spring) offers a way to automatically configure authentication settings and client objects to use Vision API. 
    
    
    import com.google.cloud.vision.v1.[AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html);
    import com.google.cloud.vision.v1.[AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html);
    import com.google.cloud.vision.v1.[BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html);
    import com.google.cloud.vision.v1.[ColorInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ColorInfo.html);
    import com.google.cloud.vision.v1.[DominantColorsAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.DominantColorsAnnotation.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.FileInputStream;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class DetectProperties {
      public static void detectProperties() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String filePath = "path/to/your/image/file.jpg";
        detectProperties(filePath);
      }
    
      // Detects image properties such as color frequency from the specified local image.
      public static void detectProperties(String filePath) throws IOException {
        List<AnnotateImageRequest> requests = new ArrayList<>();
    
        [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) imgBytes = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[readFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_readFrom_java_io_InputStream_)(new FileInputStream(filePath));
    
        [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html) img = [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html).newBuilder().setContent(imgBytes).build();
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
    
    
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const fileName = 'Local image file, e.g. /path/to/image.png';
    
    // Performs property detection on the local file
    const [result] = await client.imageProperties(fileName);
    const colors = result.imagePropertiesAnnotation.dominantColors.colors;
    colors.forEach(color => console.log(color));

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_properties(path):
        """Detects image properties in the file."""
        from google.cloud import vision
    
        client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        with open(path, "rb") as image_file:
            content = image_file.read()
    
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)(content=content)
    
        response = client.image_properties(image=image)
        props = response.image_properties_annotation
        print("Properties:")
    
        for color in props.dominant_colors.colors:
            print(f"fraction: {color.pixel_fraction}")
            print(f"\tr: {color.color.red}")
            print(f"\tg: {color.color.green}")
            print(f"\tb: {color.color.blue}")
            print(f"\ta: {color.color.alpha}")
    
        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for .NET.](https://googleapis.dev/dotnet/Google.Apis.Vision.v1/latest/api/Google.Apis.Vision.v1.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

### Detect Image Properties in a remote image

You can use the Vision API to perform feature detection on a remote image file that is located in Cloud Storage or on the Web. To send a remote file request, specify the file's Web URL or Cloud Storage URI in the request body. 

The [ `ColorInfo`](https://docs.cloud.google.com/vision/docs/reference/rest/v1/images/annotate#colorinfo) field does not carry information about the [absolute color space](https://en.wikipedia.org/wiki/Color_space) that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB, DCI-P3, BT.2020, etc.). By default, applications should assume the [sRGB](https://en.wikipedia.org/wiki/SRGB) color space. 

**Caution:** When fetching images from HTTP/HTTPS URLs, Google cannot guarantee that the request will be completed. Your request might fail if the specified host denies the request (for example, due to request throttling or [DoS](https://en.wikipedia.org/wiki/Denial-of-service_attack) prevention), or if Google throttles requests to the site for abuse prevention. **As a best practice, don't depend on externally-hosted images for production applications**. 

### REST

Before using any of the request data, make the following replacements: 

  * CLOUD_STORAGE_IMAGE_URI: the path to a valid image file in a Cloud Storage bucket. You must at least have read privileges to the file. Example: 
    * gs://cloud-samples-data/vision/image_properties/bali.jpeg

  * RESULTS_INT: (Optional) An integer value of results to return. If you omit the `"maxResults"` field and its value, the API returns the default value of 10 results. This field does not apply to the following feature types: `TEXT_DETECTION`, `DOCUMENT_TEXT_DETECTION`, or `CROP_HINTS`. 
  * PROJECT_ID: Your Google Cloud project ID.



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/images:annotate

Request JSON body: 
    
    
    {
      "requests": [
        {
          "image": {
            "source": {
              "gcsImageUri": "CLOUD_STORAGE_IMAGE_URI"
            }
          },
          "features": [
            {
              "maxResults": RESULTS_INT,
              "type": "IMAGE_PROPERTIES"
            },
          ]
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://vision.googleapis.com/v1/images:annotate"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://vision.googleapis.com/v1/images:annotate" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

**Response:**

**Note: Zero coordinate values omitted.** When the API detects a coordinate ("x" or "y") value of 0, **_that coordinate is omitted in the JSON response_**. Thus, a response with a bounding poly around the entire image would be   
**[{},{"x": 100},{"x": 100,"y": 100},{"y": 100}] for an image that is 100 pixels by 100 pixels**. For more information, see the [API Reference documentation](https://cloud.google.com/vision/docs/reference/rest/v1/images/annotate#boundingpoly). 

#### Response
    
    
    {
      "responses": [
        {
          "imagePropertiesAnnotation": {
            "dominantColors": {
              "colors": [
                {
                  "color": {
                    "red": 243,
                    "green": 177,
                    "blue": 133
                  },
                  "score": 0.18074834,
                  "pixelFraction": 0.013533333
                },
                {
                  "color": {
                    "red": 204,
                    "green": 205,
                    "blue": 213
                  },
                  "score": 0.092455424,
                  "pixelFraction": 0.19266666
                },
                {
                  "color": {
                    "red": 114,
                    "green": 77,
                    "blue": 64
                  },
                  "score": 0.090447456,
                  "pixelFraction": 0.034133334
                },
                {
                  "color": {
                    "red": 224,
                    "green": 57,
                    "blue": 64
                  },
                  "score": 0.010952942,
                  "pixelFraction": 0.014266667
                },
                {
                  "color": {
                    "red": 248,
                    "green": 125,
                    "blue": 130
                  },
                  "score": 0.006984347,
                  "pixelFraction": 0.0057333335
                },
                {
                  "color": {
                    "red": 150,
                    "green": 107,
                    "blue": 92
                  },
                  "score": 0.081589326,
                  "pixelFraction": 0.019666666
                },
                {
                  "color": {
                    "red": 233,
                    "green": 185,
                    "blue": 158
                  },
                  "score": 0.08035342,
                  "pixelFraction": 0.0122
                },
                {
                  "color": {
                    "red": 221,
                    "green": 221,
                    "blue": 226
                  },
                  "score": 0.045200635,
                  "pixelFraction": 0.202
                },
                {
                  "color": {
                    "red": 105,
                    "green": 77,
                    "blue": 75
                  },
                  "score": 0.030223774,
                  "pixelFraction": 0.013866667
                },
                {
                  "color": {
                    "red": 189,
                    "green": 145,
                    "blue": 123
                  },
                  "score": 0.028689377,
                  "pixelFraction": 0.0069333334
                }
              ]
            }
          },
          "cropHintsAnnotation": {
            "cropHints": [
              {
                "boundingPoly": {
                  "vertices": [
                    {},
                    {
                      "x": 2549
                    },
                    {
                      "x": 2549,
                      "y": 1699
                    },
                    {
                      "y": 1699
                    }
                  ]
                },
                "confidence": 0.79999995,
                "importanceFraction": 1
              }
            ]
          }
        }
      ]
    }
    

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
    
    

### gcloud

To perform image property detection, use the [`gcloud ml vision detect-image-properties`](https://docs.cloud.google.com/sdk/gcloud/reference/ml/vision/detect-image-properties) command as shown in the following example:
    
    
    gcloud ml vision detect-image-properties gs://cloud-samples-data/vision/image_properties/bali.jpeg
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for .NET.](https://googleapis.dev/dotnet/Google.Apis.Vision.v1/latest/api/Google.Apis.Vision.v1.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

## Try it

Try image property detection below. You can use the image specified already (`gs://cloud-samples-data/vision/image_properties/bali.jpeg`) or specify your own image in its place. Send the request by selecting **Execute**.

![Bali image](https://docs.cloud.google.com/static/vision/docs/images/bali_small.jpeg)_Image credit_ : [Jeremy Bishop](https://unsplash.com/photos/QUwLZNchflk) on [Unsplash](https://unsplash.com/). 

**Request body:**
    
    
    {
      "requests": [
        {
          "features": [
            {
              "maxResults": 10,
              "type": "IMAGE_PROPERTIES"
            }
          ],
          "image": {
            "source": {
              "imageUri": "gs://cloud-samples-data/vision/image_properties/bali.jpeg"
            }
          }
        }
      ]
    }

### Open the Google APIs Explorer and send the request

  1. To open the Google APIs Explorer, click **Try it!**.

Try it!

  2. Optional. Modify the existing request body.

  3. To send the request, click **Execute**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
