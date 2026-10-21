---
url: https://docs.cloud.google.com/vision/docs/detecting-web/
title: Detect Web entities and pages \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:34.938101+00:00
---

# Detect Web entities and pages  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/detecting-web/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/docs/features-list)



Send feedback 

#  Detect Web entities and pages Stay organized with collections  Save and categorize content based on your preferences. 

**Web Detection** detects Web references to an image.

**Note:** We've recently added new features or fields to Web Detection. See the [release notes](https://docs.cloud.google.com/vision/docs/release-notes#march2018) for details.**Note:** The Vision API now supports offline **asynchronous batch image annotation** for all features. This asynchronous request supports up to 2000 image files and returns response JSON files that are stored in your Cloud Storage bucket. For more information about this feature, refer to [Offline batch image annotation](https://docs.cloud.google.com/vision/docs/batch). 

![Carnaval image](https://docs.cloud.google.com/static/vision/docs/images/carnaval_small.jpeg)_Image credit_ : [Quinten de Graaf](https://unsplash.com/photos/KB0Ipylp7dc) on [Unsplash](https://unsplash.com/). 

Category | Responses  
---|---  
**Web entities** | 

  * **_entityId_** : /m/02p7_j8, **_score_** : 1.3225499, **_description_** : Carnival in Rio de Janeiro
  * **_entityId_** : /m/06gmr, **_score_** : 1.1684971, **_description_** : Rio de Janeiro
  * **_entityId_** : /m/04cx88, **_score_** : 1.05945, **_description_** : Brazilian Carnival

...  
**Full matching images** | 

  * **_url_** : https://1000lugaresparair.files.wordpress.com/2017/11/quinten-de-graaf-278848.jpg
  * **_url_** : https://freewalkingtourrotterdam.com/wp-content/uploads/2017/07/quinten-de-graaf-278848.jpg

...  
**Partial matching images** | 

  * **_url_** : https://www.linnanneito.fi/wp-content/uploads/sambakarnevaali-riossa.jpg
  * **_url_** : https://static.airhelp.com/wp-content/uploads/2019/02/26105557/two-women-in-carnival-costumes.jpg

...  
**Pages with matching images** | 

  * **_url_** : https://travelnoire.com/best-carnival-celebrations-around-the-world/,   
**_pageTitle_** : Best \u003cb\u003eCarnival\u003c/b\u003e Celebrations Around The World - Travel Noire,   
**_fullMatchingImages_** : [{**_url_** : https://travelnoire.com/wp-content/uploads/2019/02/quinten-de-graaf-278848-unsplash.jpg}]
  * **_url_** : https://bespokebrazil.com/rio-carnival-2019/,   
**_pageTitle_** : Visit \u003cb\u003eRio Carnival 2019\u003c/b\u003e with the Brazil Specialists - Bespoke Brazil,   
**_partialMatchingImages_** : [{ **_url_** : https://bespoke-brazil-2018-bespokebrazil.netdna-ssl.com/wp-content/uploads/2019/01/Carnival-1.jpg}]

...  
**Visually similar images** | 

  * **_url_** : https://www.brazilbookers.com/_images/photos/rio-carnival-images/rio-carnival-2016-carnival-date.jpg
  * **_url_** : https://image.redbull.com/rbcom/010/2017-02-08/1331843859949_3/0100/0/1/watch-rio-carnival-2017-live-on-red-bull-tv.jpg

...  
**Best guess labels** | rio carnival 2019 dancers  
  
## Web detection requests

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




### Detect Web entities with a local image

You can use the Vision API to perform feature detection on a local image file.

For REST requests, send the contents of the image file as a [base64 encoded](https://docs.cloud.google.com/vision/docs/base64) string in the body of your request.

For `gcloud` and client library requests, specify the path to a local image in your request. 

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
              "type": "WEB_DETECTION"
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
          "webDetection": {
            "**webEntities** ": [
              {
                "entityId": "/m/02p7_j8",
                "score": 1.44225,
                "description": "Carnival in Rio de Janeiro"
              },
              {
                "entityId": "/m/06gmr",
                "score": 1.2913725,
                "description": "Rio de Janeiro"
              },
              {
                "entityId": "/m/04cx88",
                "score": 0.78465,
                "description": "Brazilian Carnival"
              },
              {
                "entityId": "/m/09l9f",
                "score": 0.7166,
                "description": "Carnival"
              },
              ...
            ],
            "**fullMatchingImages** ": [
              {
                "url": "https://1000lugaresparair.files.wordpress.com/2017/11/quinten-de-graaf-278848.jpg"
              },
              ...
            ],
            "**partialMatchingImages** ": [
              {
                "url": "https://www.linnanneito.fi/wp-content/uploads/sambakarnevaali-riossa.jpg"
              },
              ...
            ],
            "**pagesWithMatchingImages** ": [
              {
                "url": "https://www.intrepidtravel.com/us/brazil/rio-carnival-122873",
                "pageTitle": "\u003cb\u003eRio Carnival\u003c/b\u003e | Intrepid Travel US",
                "partialMatchingImages": [
                  {
                    "url": "https://www.intrepidtravel.com/sites/intrepid/files/styles/large/public/elements/product/hero/GGSR-Brazil-rio-carnival-ladies.jpg"
                  },
                  ...
            ],
            "**visuallySimilarImages** ": [
              {
                "url": "https://pbs.twimg.com/media/DVoQOx6WkAIpHKF.jpg"
              },
              ...
            ],
            "**bestGuessLabels** ": [
              {
                "label": "rio carnival",
                "languageCode": "en"
              }
            ]
          }
        }
      ]
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // detectWeb gets image properties from the Vision API for an image at the given file path.
    func detectWeb(w io.Writer, file string) error {
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
    	web, err := client.DetectWeb(ctx, image, nil)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintln(w, "Web properties:")
    	if len(web.FullMatchingImages) != 0 {
    		fmt.Fprintln(w, "\tFull image matches:")
    		for _, full := range web.FullMatchingImages {
    			fmt.Fprintf(w, "\t\t%s\n", full.Url)
    		}
    	}
    	if len(web.PagesWithMatchingImages) != 0 {
    		fmt.Fprintln(w, "\tPages with this image:")
    		for _, page := range web.PagesWithMatchingImages {
    			fmt.Fprintf(w, "\t\t%s\n", page.Url)
    		}
    	}
    	if len(web.WebEntities) != 0 {
    		fmt.Fprintln(w, "\tEntities:")
    		fmt.Fprintln(w, "\t\tEntity\t\tScore\tDescription")
    		for _, entity := range web.WebEntities {
    			fmt.Fprintf(w, "\t\t%-14s\t%-2.4f\t%s\n", entity.EntityId, entity.Score, entity.Description)
    		}
    	}
    	if len(web.BestGuessLabels) != 0 {
    		fmt.Fprintln(w, "\tBest guess labels:")
    		for _, label := range web.BestGuessLabels {
    			fmt.Fprintf(w, "\t\t%s\n", label.Label)
    		}
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vision API Quickstart Using Client Libraries](https://docs.cloud.google.com/vision/docs/detect-labels-image-client-libraries). For more information, see the [ Vision API Java reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview).

**Note:** For Java **Spring framework** users, [Spring Cloud Google Cloud](https://docs.cloud.google.com/vision/docs/adding-spring) offers a way to automatically configure authentication settings and client objects to use Vision API. 
    
    
    import com.google.cloud.vision.v1.[AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html);
    import com.google.cloud.vision.v1.[AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html);
    import com.google.cloud.vision.v1.[BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).[Type](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Type.html);
    import com.google.cloud.vision.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.cloud.vision.v1.[WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html);
    import com.google.cloud.vision.v1.[WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html).[WebEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebEntity.html);
    import com.google.cloud.vision.v1.[WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html).[WebImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebImage.html);
    import com.google.cloud.vision.v1.[WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html).[WebLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebLabel.html);
    import com.google.cloud.vision.v1.[WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html).[WebPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebPage.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.FileInputStream;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class DetectWebDetections {
    
      public static void detectWebDetections() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String filePath = "path/to/your/image/file.jpg";
        detectWebDetections(filePath);
      }
    
      // Finds references to the specified image on the web.
      public static void detectWebDetections(String filePath) throws IOException {
        List<AnnotateImageRequest> requests = new ArrayList<>();
    
        [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) imgBytes = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[readFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_readFrom_java_io_InputStream_)(new FileInputStream(filePath));
    
        [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html) img = [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html).newBuilder().setContent(imgBytes).build();
        [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html) feat = [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).newBuilder().setType([Type](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Type.html).WEB_DETECTION).build();
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
    
            // Search the web for usages of the image. You could use these signals later
            // for user input moderation or linking external references.
            // For a full list of available annotations, see http://g.co/cloud/vision/docs
            [WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html) annotation = res.getWebDetection();
            System.out.println("Entity:Id:Score");
            System.out.println("===============");
            for ([WebEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebEntity.html) entity : annotation.[getWebEntitiesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getWebEntitiesList__)()) {
              System.out.println(
                  entity.getDescription() + " : " + entity.getEntityId() + " : " + entity.getScore());
            }
            for ([WebLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebLabel.html) label : annotation.[getBestGuessLabelsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getBestGuessLabelsList__)()) {
              System.out.format("%nBest guess label: %s", label.getLabel());
            }
            System.out.println("%nPages with matching images: Score%n==");
            for ([WebPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebPage.html) page : annotation.[getPagesWithMatchingImagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getPagesWithMatchingImagesList__)()) {
              System.out.println(page.getUrl() + " : " + page.getScore());
            }
            System.out.println("%nPages with partially matching images: Score%n==");
            for ([WebImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebImage.html) image : annotation.[getPartialMatchingImagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getPartialMatchingImagesList__)()) {
              System.out.println(image.getUrl() + " : " + image.getScore());
            }
            System.out.println("%nPages with fully matching images: Score%n==");
            for ([WebImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebImage.html) image : annotation.[getFullMatchingImagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getFullMatchingImagesList__)()) {
              System.out.println(image.getUrl() + " : " + image.getScore());
            }
            System.out.println("%nPages with visually similar images: Score%n==");
            for ([WebImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebImage.html) image : annotation.[getVisuallySimilarImagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getVisuallySimilarImagesList__)()) {
              System.out.println(image.getUrl() + " : " + image.getScore());
            }
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const fileName = 'Local image file, e.g. /path/to/image.png';
    
    // Detect similar images on the web to a local file
    const [result] = await client.webDetection(fileName);
    const webDetection = result.webDetection;
    if (webDetection.fullMatchingImages.length) {
      console.log(
        `Full matches found: ${webDetection.fullMatchingImages.length}`
      );
      webDetection.fullMatchingImages.forEach(image => {
        console.log(`  URL: ${image.url}`);
        console.log(`  Score: ${image.score}`);
      });
    }
    
    if (webDetection.partialMatchingImages.length) {
      console.log(
        `Partial matches found: ${webDetection.partialMatchingImages.length}`
      );
      webDetection.partialMatchingImages.forEach(image => {
        console.log(`  URL: ${image.url}`);
        console.log(`  Score: ${image.score}`);
      });
    }
    
    if (webDetection.webEntities.length) {
      console.log(`Web entities found: ${webDetection.webEntities.length}`);
      webDetection.webEntities.forEach(webEntity => {
        console.log(`  Description: ${webEntity.description}`);
        console.log(`  Score: ${webEntity.score}`);
      });
    }
    
    if (webDetection.bestGuessLabels.length) {
      console.log(
        `Best guess labels found: ${webDetection.bestGuessLabels.length}`
      );
      webDetection.bestGuessLabels.forEach(label => {
        console.log(`  Label: ${label.label}`);
      });
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_web(path):
        """Detects web annotations given an image."""
        from google.cloud import vision
    
        client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        with open(path, "rb") as image_file:
            content = image_file.read()
    
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)(content=content)
    
        response = client.web_detection(image=image)
        annotations = response.web_detection
    
        if annotations.best_guess_labels:
            for label in annotations.best_guess_labels:
                print(f"\nBest guess label: {label.label}")
    
        if annotations.pages_with_matching_images:
            print(
                "\n{} Pages with matching images found:".format(
                    len(annotations.pages_with_matching_images)
                )
            )
    
            for page in annotations.pages_with_matching_images:
                print(f"\n\tPage url   : {page.url}")
    
                if page.full_matching_images:
                    print(
                        "\t{} Full Matches found: ".format(len(page.full_matching_images))
                    )
    
                    for image in page.full_matching_images:
                        print(f"\t\tImage url  : {image.url}")
    
                if page.partial_matching_images:
                    print(
                        "\t{} Partial Matches found: ".format(
                            len(page.partial_matching_images)
                        )
                    )
    
                    for image in page.partial_matching_images:
                        print(f"\t\tImage url  : {image.url}")
    
        if annotations.web_entities:
            print("\n{} Web entities found: ".format(len(annotations.web_entities)))
    
            for entity in annotations.web_entities:
                print(f"\n\tScore      : {entity.score}")
                print(f"\tDescription: {entity.description}")
    
        if annotations.visually_similar_images:
            print(
                "\n{} visually similar images found:\n".format(
                    len(annotations.visually_similar_images)
                )
            )
    
            for image in annotations.visually_similar_images:
                print(f"\tImage url    : {image.url}")
    
        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for .NET.](https://googleapis.dev/dotnet/Google.Apis.Vision.v1/latest/api/Google.Apis.Vision.v1.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

### Detect Web entities with a remote image

You can use the Vision API to perform feature detection on a remote image file that is located in Cloud Storage or on the Web. To send a remote file request, specify the file's Web URL or Cloud Storage URI in the request body. 

**Caution:** When fetching images from HTTP/HTTPS URLs, Google cannot guarantee that the request will be completed. Your request might fail if the specified host denies the request (for example, due to request throttling or [DoS](https://en.wikipedia.org/wiki/Denial-of-service_attack) prevention), or if Google throttles requests to the site for abuse prevention. **As a best practice, don't depend on externally-hosted images for production applications**. 

### REST

Before using any of the request data, make the following replacements: 

  * CLOUD_STORAGE_IMAGE_URI: the path to a valid image file in a Cloud Storage bucket. You must at least have read privileges to the file. Example: 
    * gs://cloud-samples-data/vision/web/carnaval.jpeg

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
              "type": "WEB_DETECTION"
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
          "webDetection": {
            "**webEntities** ": [
              {
                "entityId": "/m/02p7_j8",
                "score": 1.44225,
                "description": "Carnival in Rio de Janeiro"
              },
              {
                "entityId": "/m/06gmr",
                "score": 1.2913725,
                "description": "Rio de Janeiro"
              },
              {
                "entityId": "/m/04cx88",
                "score": 0.78465,
                "description": "Brazilian Carnival"
              },
              {
                "entityId": "/m/09l9f",
                "score": 0.7166,
                "description": "Carnival"
              },
              ...
            ],
            "**fullMatchingImages** ": [
              {
                "url": "https://1000lugaresparair.files.wordpress.com/2017/11/quinten-de-graaf-278848.jpg"
              },
              ...
            ],
            "**partialMatchingImages** ": [
              {
                "url": "https://www.linnanneito.fi/wp-content/uploads/sambakarnevaali-riossa.jpg"
              },
              ...
            ],
            "**pagesWithMatchingImages** ": [
              {
                "url": "https://www.intrepidtravel.com/us/brazil/rio-carnival-122873",
                "pageTitle": "\u003cb\u003eRio Carnival\u003c/b\u003e | Intrepid Travel US",
                "partialMatchingImages": [
                  {
                    "url": "https://www.intrepidtravel.com/sites/intrepid/files/styles/large/public/elements/product/hero/GGSR-Brazil-rio-carnival-ladies.jpg"
                  },
                  ...
            ],
            "**visuallySimilarImages** ": [
              {
                "url": "https://pbs.twimg.com/media/DVoQOx6WkAIpHKF.jpg"
              },
              ...
            ],
            "**bestGuessLabels** ": [
              {
                "label": "rio carnival",
                "languageCode": "en"
              }
            ]
          }
        }
      ]
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // detectWeb gets image properties from the Vision API for an image at the given file path.
    func detectWebURI(w io.Writer, file string) error {
    	ctx := context.Background()
    
    	client, err := vision.NewImageAnnotatorClient(ctx)
    	if err != nil {
    		return err
    	}
    
    	image := vision.NewImageFromURI(file)
    	web, err := client.DetectWeb(ctx, image, nil)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintln(w, "Web properties:")
    	if len(web.FullMatchingImages) != 0 {
    		fmt.Fprintln(w, "\tFull image matches:")
    		for _, full := range web.FullMatchingImages {
    			fmt.Fprintf(w, "\t\t%s\n", full.Url)
    		}
    	}
    	if len(web.PagesWithMatchingImages) != 0 {
    		fmt.Fprintln(w, "\tPages with this image:")
    		for _, page := range web.PagesWithMatchingImages {
    			fmt.Fprintf(w, "\t\t%s\n", page.Url)
    		}
    	}
    	if len(web.WebEntities) != 0 {
    		fmt.Fprintln(w, "\tEntities:")
    		fmt.Fprintln(w, "\t\tEntity\t\tScore\tDescription")
    		for _, entity := range web.WebEntities {
    			fmt.Fprintf(w, "\t\t%-14s\t%-2.4f\t%s\n", entity.EntityId, entity.Score, entity.Description)
    		}
    	}
    	if len(web.BestGuessLabels) != 0 {
    		fmt.Fprintln(w, "\tBest guess labels:")
    		for _, label := range web.BestGuessLabels {
    			fmt.Fprintf(w, "\t\t%s\n", label.Label)
    		}
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.vision.v1.[AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html);
    import com.google.cloud.vision.v1.[AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html);
    import com.google.cloud.vision.v1.[BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.cloud.vision.v1.[ImageSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html);
    import com.google.cloud.vision.v1.[WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class DetectWebDetectionsGcs {
    
      public static void detectWebDetectionsGcs() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String filePath = "gs://your-gcs-bucket/path/to/image/file.jpg";
        detectWebDetectionsGcs(filePath);
      }
    
      // Detects whether the remote image on Google Cloud Storage has features you would want to
      // moderate.
      public static void detectWebDetectionsGcs(String gcsPath) throws IOException {
        List<AnnotateImageRequest> requests = new ArrayList<>();
    
        [ImageSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html) imgSource = [ImageSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html).newBuilder().[setGcsImageUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.Builder.html#com_google_cloud_vision_v1_ImageSource_Builder_setGcsImageUri_java_lang_String_)(gcsPath).build();
        [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html) img = [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html).newBuilder().[setSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.Builder.html#com_google_cloud_vision_v1_Image_Builder_setSource_com_google_cloud_vision_v1_ImageSource_)(imgSource).build();
        [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html) feat = [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).newBuilder().setType([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).Type.WEB_DETECTION).build();
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
    
            // Search the web for usages of the image. You could use these signals later
            // for user input moderation or linking external references.
            // For a full list of available annotations, see http://g.co/cloud/vision/docs
            [WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html) annotation = res.getWebDetection();
            System.out.println("Entity:Id:Score");
            System.out.println("===============");
            for ([WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html).[WebEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebEntity.html) entity : annotation.[getWebEntitiesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getWebEntitiesList__)()) {
              System.out.println(
                  entity.getDescription() + " : " + entity.getEntityId() + " : " + entity.getScore());
            }
            for ([WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html).[WebLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebLabel.html) label : annotation.[getBestGuessLabelsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getBestGuessLabelsList__)()) {
              System.out.format("%nBest guess label: %s", label.getLabel());
            }
            System.out.println("%nPages with matching images: Score%n==");
            for ([WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html).[WebPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebPage.html) page : annotation.[getPagesWithMatchingImagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getPagesWithMatchingImagesList__)()) {
              System.out.println(page.getUrl() + " : " + page.getScore());
            }
            System.out.println("%nPages with partially matching images: Score%n==");
            for ([WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html).[WebImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebImage.html) image : annotation.[getPartialMatchingImagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getPartialMatchingImagesList__)()) {
              System.out.println(image.getUrl() + " : " + image.getScore());
            }
            System.out.println("%nPages with fully matching images: Score%n==");
            for ([WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html).[WebImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebImage.html) image : annotation.[getFullMatchingImagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getFullMatchingImagesList__)()) {
              System.out.println(image.getUrl() + " : " + image.getScore());
            }
            System.out.println("%nPages with visually similar images: Score%n==");
            for ([WebDetection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html).[WebImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.WebImage.html) image : annotation.[getVisuallySimilarImagesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetection.html#com_google_cloud_vision_v1_WebDetection_getVisuallySimilarImagesList__)()) {
              System.out.println(image.getUrl() + " : " + image.getScore());
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
    
    // Detect similar images on the web to a remote file
    const [result] = await client.webDetection(`gs://${bucketName}/${fileName}`);
    const webDetection = result.webDetection;
    if (webDetection.fullMatchingImages.length) {
      console.log(
        `Full matches found: ${webDetection.fullMatchingImages.length}`
      );
      webDetection.fullMatchingImages.forEach(image => {
        console.log(`  URL: ${image.url}`);
        console.log(`  Score: ${image.score}`);
      });
    }
    
    if (webDetection.partialMatchingImages.length) {
      console.log(
        `Partial matches found: ${webDetection.partialMatchingImages.length}`
      );
      webDetection.partialMatchingImages.forEach(image => {
        console.log(`  URL: ${image.url}`);
        console.log(`  Score: ${image.score}`);
      });
    }
    
    if (webDetection.webEntities.length) {
      console.log(`Web entities found: ${webDetection.webEntities.length}`);
      webDetection.webEntities.forEach(webEntity => {
        console.log(`  Description: ${webEntity.description}`);
        console.log(`  Score: ${webEntity.score}`);
      });
    }
    
    if (webDetection.bestGuessLabels.length) {
      console.log(
        `Best guess labels found: ${webDetection.bestGuessLabels.length}`
      );
      webDetection.bestGuessLabels.forEach(label => {
        console.log(`  Label: ${label.label}`);
      });
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_web_uri(uri):
        """Detects web annotations in the file located in Google Cloud Storage."""
        from google.cloud import vision
    
        client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)()
        image.source.image_uri = uri
    
        response = client.web_detection(image=image)
        annotations = response.web_detection
    
        if annotations.best_guess_labels:
            for label in annotations.best_guess_labels:
                print(f"\nBest guess label: {label.label}")
    
        if annotations.pages_with_matching_images:
            print(
                "\n{} Pages with matching images found:".format(
                    len(annotations.pages_with_matching_images)
                )
            )
    
            for page in annotations.pages_with_matching_images:
                print(f"\n\tPage url   : {page.url}")
    
                if page.full_matching_images:
                    print(
                        "\t{} Full Matches found: ".format(len(page.full_matching_images))
                    )
    
                    for image in page.full_matching_images:
                        print(f"\t\tImage url  : {image.url}")
    
                if page.partial_matching_images:
                    print(
                        "\t{} Partial Matches found: ".format(
                            len(page.partial_matching_images)
                        )
                    )
    
                    for image in page.partial_matching_images:
                        print(f"\t\tImage url  : {image.url}")
    
        if annotations.web_entities:
            print("\n{} Web entities found: ".format(len(annotations.web_entities)))
    
            for entity in annotations.web_entities:
                print(f"\n\tScore      : {entity.score}")
                print(f"\tDescription: {entity.description}")
    
        if annotations.visually_similar_images:
            print(
                "\n{} visually similar images found:\n".format(
                    len(annotations.visually_similar_images)
                )
            )
    
            for image in annotations.visually_similar_images:
                print(f"\tImage url    : {image.url}")
    
        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )
    
    

### gcloud

To perform Web detection, use the [`gcloud ml vision detect-web`](https://docs.cloud.google.com/sdk/gcloud/reference/ml/vision/detect-web) command as shown in the following example:
    
    
    gcloud ml vision detect-web gs://cloud-samples-data/vision/web/carnaval.jpeg
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for .NET.](https://googleapis.dev/dotnet/Google.Apis.Vision.v1/latest/api/Google.Apis.Vision.v1.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

## Try it

Try Web entities detection below. You can use the image specified already (`gs://cloud-samples-data/vision/web/carnaval.jpeg`) or specify your own image in its place. Send the request by selecting **Execute**.

![Carnaval image](https://docs.cloud.google.com/static/vision/docs/images/carnaval_small.jpeg)_Image credit_ : [Quinten de Graaf](https://unsplash.com/photos/KB0Ipylp7dc) on [Unsplash](https://unsplash.com/). 

**Request body:**
    
    
    {
      "requests": [
        {
          "features": [
            {
              "type": "WEB_DETECTION"
            }
          ],
          "image": {
            "source": {
              "gcsImageUri": "gs://cloud-samples-data/vision/web/carnaval.jpeg"
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
