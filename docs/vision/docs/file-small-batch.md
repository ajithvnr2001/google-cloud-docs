---
url: https://docs.cloud.google.com/vision/docs/file-small-batch/
title: Small batch file annotation online \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:48.098819+00:00
---

# Small batch file annotation online  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/file-small-batch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/docs/features-list)



Send feedback 

#  Small batch file annotation online Stay organized with collections  Save and categorize content based on your preferences. 

If you are detecting text in scanned documents, try [Document AI](https://docs.cloud.google.com/document-ai/docs/overview) for optical character recognition, structured form parsing, and entity extraction. You can use the [Document AI Toolbox](https://docs.cloud.google.com/document-ai/docs/handle-response#toolbox) to convert output from the Document AI format to the Cloud Vision format. 

  * **online (synchronous)** requests - An online annotation request (`images:annotate` or `files:annotate`) immediately returns inline annotations to the user. Online annotation requests limit the number of files you can annotate in a single request. With an `images:annotate` request you can only specify a small number of images (<=16) to be annotated ; with a `files:annotate` request you can only specify a single file and specify a small number of pages (<=5) in that file to be annotated. 
  * **offline (asynchronous)** requests - An offline annotation request (`images:asyncBatchAnnotate` or `files:asyncBatchAnnotate`) starts a long-running operation (LRO) and does not immediately return a response to the caller. When the LRO completes, annotations are stored as files in a Cloud Storage bucket you specify. A `images:asyncBatchAnnotate` request allows you to specify up to 2000 images per request ; a `files:asyncBatchAnnotate` request allows you to specify larger batches of files and can specify more pages (<=2000) per file for annotation at a single time than you are able to with online requests. 



The Vision API can provide online (immediate) annotation of multiple pages or frames from PDF, TIFF, or GIF files stored in Cloud Storage.

You can request online feature detection and annotation of 5 frames (GIF; "image/gif") or pages (PDF; "application/pdf", or TIFF; "image/tiff") of your choosing for each file.

The example annotations on this page are for `DOCUMENT_TEXT_DETECTION`, but online small batch annotation is available for all Vision features.

**Note:** Vision API also supports **offline asynchronous PDF/TIFF file annotation** , currently only for the `DOCUMENT_TEXT_DETECTION` feature type. 

Offline asynchronous requests return response JSON files in your Cloud Storage bucket and supports files up to 2000 pages. For more information, refer to [Detect text in files (PDF/TIFF)](https://docs.cloud.google.com/vision/docs/pdf).

![first five pages of a pdf file](https://docs.cloud.google.com/static/vision/docs/images/combined_small_batch.png)[gs://cloud-samples-data/vision/document_understanding/custom_0773375000.pdf](https://storage.cloud.google.com/cloud-samples-data/vision/document_understanding/custom_0773375000.pdf)

### Page 1

![page 1 of example pdf](https://docs.cloud.google.com/static/vision/docs/images/small_batch_page1.jpg)
    
    
    ...
    "text": "á\n7.1.15\nOIL, GAS AND MINERAL LEASE
    \nNORVEL J. CHITTIM, ET AL\n.\n.
    \nTO\nW. L. SCHEIG\n"
    },
    "context": {"pageNumber": 1}
    ...  
  
---  
  
### Page 2

![page 2 \(top\) of example pdf](https://docs.cloud.google.com/static/vision/docs/images/small_batch_page2_TOP.jpg)
    
    
    ...
    "text": "...\n.\n*\n.\n.\n.\nA\nNY\nALA...\n7
    \n| THE STATE OF TEXAS
    \nOIL, GAS AND MINERAL LEASE
    \nCOUNTY OF MAVERICK ]
    \nTHIS AGREEMENT made this 14 day of_June
    \n1954, between Norvel J. Chittim and his wife, Lieschen G. Chittim;
    \nMary Anne Chittim Parker, joined herein pro forma by her husband,
    \nJoseph Bright Parker; Dorothea Chittim Oppenheimer, joined herein
    \npro forma by her husband, Fred J. Oppenheimer; Tuleta Chittim
    \nWright, joined herein pro forma by her husband, Gilbert G. Wright,
    \nJr.; Gilbert G. Wright, III; Dela Wright White, joined herein pro
    \nforma by her husband, John H. White; Anne Wright Basse, joined
    \nherein pro forma by her husband, E. A. Basse, Jr.; Norvel J.
    \nChittim, Independent Executor and Trustee for Estate of Marstella
    \nChittim, Deceased; Mary Louise Roswell, joined herein pro forma by
    \nher husband, Charles M. 'Roswell; and James M. Chittim and his wife,
    \nThelma Neal Chittim; as LESSORS, and W. L. Scheig of San Antonio,
    \nTexas, as LESSEE,  
  
---  
![page 2 \(bottom\) of example pdf](https://docs.cloud.google.com/static/vision/docs/images/small_batch_page2_BTM.jpg)
    
    
    \nW I T N E s s E T H:
    \n1. Lessors, in consideration of $10.00, cash in hand paid,
    \nof the royalties herein provided, and of the agreement of Lessee
    \nherein contained, hereby grant, lease and let exclusively unto
    \nLessee the tracts of land hereinafter described for the purpose of
    \ntesting for mineral indications, and in such tests use the Seismo-
    \ngraph, Torsion Balance, Core Drill, or any other tools, machinery,
    \nequipment or explosive necessary and proper; and also prospecting,
    \ndrilling and mining for and producing oil, gas and other minerals
    \n(except metallic minerals), laying pipe lines, building tanks,
    \npower stations, telephone lines and other structures thereon to
    \nproduce, save, take care of, treat, transport and own said pro-
    \nducts and housing its employees (Lessee to conduct its geophysical
    \nwork in such manner as not to damage the buildings, water tanks
    \nor wells of Lessors, or the livestock of Lessors or Lessors' ten- !
    \nants, )said lands being situated in Maverick, Zavalla and Dimmit
    \nCounties, Texas, to-wit:\n3-1.\n"
    },
    "context": {"pageNumber": 2}
    ...  
  
### Page 3

![page 3 \(top\) of example pdf](https://docs.cloud.google.com/static/vision/docs/images/small_batch_page3_TOP.jpg)
    
    
    ...
    "text": "Being a tract consisting of 140,769.86 acres, more or
    \nless, out of what is known as the \"Chittim Ranch\" in said counties,
    \nas designated and described in Exhibit \"A\" hereto attached and
    \nmade a part hereof as if fully written herein. It being under-
    \nstood that the acreage intended to be included in this lease aggre-
    \ngates approximately 140,769.86 acres whether it actually comprises
    \nmore or less, but for the purpose of calculating the payments
    \nhereinafter provided for, it is agreed that the land included with-
    \nin the terms of this lease is One hundred forty thousand seven
    \nhundred sixty-nine and eighty-six one hundredths (140,769.86) acres,
    \nand that each survey listed above contains the acreage stated above.
    \nIt is understood that tract designated \"TRACT II\" in
    \nExhibit \"A\" is subject to a one-sixteenth (1/16) royalty reserved.
    \nto the State of Texas, and the rights of the State of Texas must
    \nbe respected in the development of the said property.  
  
---  
![page 3 \(bottom\) of example pdf](https://docs.cloud.google.com/static/vision/docs/images/small_batch_page3_BTM.jpg)
    
    
    \n2. Subject to the other provisions hereof, this lease shall
    \nbe for a term of ten (10) years from date hereof (called \"Primary
    \nTerm\"), and as long thereafter as oil, gas or other minerals
    \n(except metallic minerals) are produced from said land hereunder
    \nin paying quantities, subject, however, to all of the terms and
    \nprovisions of this lease. After expiration of the primary term,
    \nthis lease shall terminate as to all lands included herein, save
    \nand except as to those tracts which lessee maintains in force and
    \neffect according to the requirements hereof.
    \n3. The royalties to be paid by Lessee are (a) on oil, one-
    \neighth (1/8) of that produced and saved from said land, the same to
    \nbe delivered at the well or to the credit of Lessors into the pipe i
    \nline to which the well may be connected; (b) on gas, including
    \ni casinghead gas or other gaseous or vaporous substance, produced
    \nfrom the leased premises and sold or used by Lessee off the leased
    \npremises or in the manufacture of gasoline or other products, the
    \nmarket value, at the mouth of the well, of one-eighth (1/8) of
    \n.\n3-2-\n?\n"
    },
    "context": {"pageNumber": 3}
    ...  
  
### Page 4

![page 4 \(top\) of example pdf](https://docs.cloud.google.com/static/vision/docs/images/small_batch_page4_TOP.jpg)
    
    
    ...
    "text": "•\n:\n.\nthe gas or casinghead gas so used or sold. On all gas or casing-
    \nhead gas sold at the well, the royalty shall be one-eighth (1/8)
    \nof the amounts realized from such sales. While gas from any well
    \nproducing gas only is being used or sold by. Lessee, Lessor may have
    \nenough of said gas for all stoves and inside lights in the prin-
    \ncipal dwelling house on the leased premises by making Lessors' own
    \nconnections with the well and by assuming all risk and paying all
    \nexpenses. And (c) on all other minerals (except metallic minerals)
    \nmined and marketed, one tenth (1/10). either in kind or value at the
    \nwell or mine at Lessee's election.
    \nFor the purpose of royalty payments under 3 (b) hereof,
    \nall liquid hydrocarbons (including distillate) recovered and saved
    n| by Lessee in separators or traps on the leased premises shall be
    \nconsidered as oil. Should such a plant be constructed by another
    \nthan Lessee to whom Lessee should sell or deliver the gas or cas-
    \ninghead gas produced from the leased premises for processing, then
    \nthe royalty thereon shall be one-eighth (1/8) of the amounts
    \nrealized by Lessee from such sales or deliveries.  
  
---  
![page 4 \(bottom\) of example pdf](https://docs.cloud.google.com/static/vision/docs/images/small_batch_page4_BTM.jpg)
    
    
    \nOr if such plant is owned or constructed or operated by
    \nLessee, then the royalty shall be on the basis of one-eighth (1/8) |
    \nof the prevailing price in the area for such products..
    \nThe provisions of this paragraph shall control as to any
    \nconflict with Paragraph 3 (b). Lessors shall also be entitled to
    \nsaid royalty interest in all residue gas .obtained, saved and mar-
    \nketed from said premises, or used off the premises, or that may be
    \nreplaced in the reservoir by 'any recycling process, settlement
    \ntherefor to be made to Lessors when such gas is marketed or used
    \noff the premises. !
    \nIf at the expiration of the primary term of this lease
    \nLessee has not found and produced oil or gas in paying quantities
    \nin any formation lying fifty (50) feet below the base of what is
    \nknown as the Rhodessa section at the particular point where the
    \nwell is drilled, then, subject to the further provisions hereof,
    \nthis lease shall terminate as to all horizons below fifty (50)
    \nI feet below the Rhodessa section. And if at the expiration of the
    \n3 -3-\n"
    },
    "context": {"pageNumber": 4}
    ...  
  
### Page 5

![page 5 \(top\) of example pdf](https://docs.cloud.google.com/static/vision/docs/images/small_batch_page5_TOP.jpg)
    
    
    ...
    "text": ".\n.\n:\nI\n.\n.\n.:250:-....\n.\n...\n.\n....\n....\n..\n..\n. ..
    \n.\n..\n.\n...\n...\n.-\n.\n.\n..\n..\n17\n.\n:\n-\n-\n-\n.\n..\n.
    \nprimary term production of oil or gas in paying quantities is not
    \nfound in the Jurassic, then this lease shall terminate as to the
    \nJurassic and lower formations unless Lessee shall have completed
    \nat least two (2) tests in the Jurassic. And after the primary
    \nterm Lessee shall complete at least one (1) Jurassic test each
    \nthree years on said property as to which this lease is still in
    \neffect, until paying production is obtained in or below the
    \nJurassic, or upon failure so to do Lessee shall release this
    \nlease as to all formations below the top of the Jurassic. Upon
    \ncompliance with the above provisions as to Jurassic tests, and
    \nif production is found in the Jurassic, then, subject to the
    \nother provisions hereof, this lease shall be effective as to all
    \nhorizons, including the Jurassic..
    \n5. It is understood and expressly agreed that the consider-
    \niation first recited in this lease, the down cash payment, receipt
    \nof which is hereby acknowledged by Lessors, is full and adequate
    \nconsideration to maintain this lease in full force and effect for
    \na period of one year from the date hereof, and does not impose
    \nany obligation on the part of Lessee to drill and develop this
    \nlease during the said term of one year from date of this lease.  
  
---  
![page 5 \(bottom\) of example pdf](https://docs.cloud.google.com/static/vision/docs/images/small_batch_page5_BTM.jpg)
    
    
    \n6. This lease shall terminate as to both parties unless
    \non or before one year from this date, Lessee shall pay to or ten- !
    \nder to Lessors or to the credit of Lessors, in the National Bank
    \nof Commerce, at San Antonio, Texas, (which bank and its successors
    \nare Lessors' agent, and shall continue as the depository for all \"
    \nrental payable hereunder regardless of changes in ownership of
    \nsaid land or the rental), the sum of One Dollar ($1.00) per acre
    \nas to all acreage then covered by this lease, and not surrendered,
    \nor maintained by production of oil, gas or other minerals, or by
    \ndrilling-reworking operations, all as hereinafter fully set out, :
    \nwhich shall maintain this lease in full force and effect for
    \nanother twelve-month period, without imposing any obligation on
    \nthe part of Lessee to drill and develop this lease. In like
    \nmanner, and upon like payment or tender annually, Lessee may
    \nmaintain this lease .in full force and effect for successive
    \ntwelve-month periods during the primary term, without imposing
    \n.\n--.\n.\n.\n.\n-\n::\n---
    \n-\n3\n.\n..-\n-\n-\n:.\n.\n::\n.
    \n3-4-\n"
    },
    "context": {"pageNumber": 5}
    ...  
  
## Limitations

At most 5 pages will be annotated. Users can specify the specific 5 pages to be annotated.

## Authentication

API keys are not supported for `files:annotate` requests. 

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




## Currently supported feature types

Feature type  
---  
[`CROP_HINTS`](https://docs.cloud.google.com/vision/docs/detecting-crop-hints) | Determine suggested vertices for a crop region on an image.  
[`DOCUMENT_TEXT_DETECTION`](https://docs.cloud.google.com/vision/docs/pdf) | Perform OCR on dense text images, such as documents (PDF/TIFF), and images with handwriting. `TEXT_DETECTION` can be used for sparse text images. Takes precedence when both `DOCUMENT_TEXT_DETECTION` and `TEXT_DETECTION` are present.   
[`FACE_DETECTION`](https://docs.cloud.google.com/vision/docs/detecting-faces) | Detect faces within the image.  
[`IMAGE_PROPERTIES`](https://docs.cloud.google.com/vision/docs/detecting-properties) | Compute a set of image properties, such as the image's dominant colors.  
[`LABEL_DETECTION`](https://docs.cloud.google.com/vision/docs/labels) | Add labels based on image content.  
[`LANDMARK_DETECTION`](https://docs.cloud.google.com/vision/docs/detecting-landmarks) | Detect geographic landmarks within the image.  
[`LOGO_DETECTION`](https://docs.cloud.google.com/vision/docs/detecting-logos) | Detect company logos within the image.  
[`OBJECT_LOCALIZATION`](https://docs.cloud.google.com/vision/docs/object-localizer) | Detect and extract multiple objects in an image.  
[`SAFE_SEARCH_DETECTION`](https://docs.cloud.google.com/vision/docs/detecting-safe-search) | Run SafeSearch to detect potentially unsafe or undesirable content.  
[`TEXT_DETECTION`](https://docs.cloud.google.com/vision/docs/ocr) | Perform Optical Character Recognition (OCR) on text within the image. Text detection is optimized for areas of sparse text within a larger image. If the image is a document (PDF/TIFF), has dense text, or contains handwriting, use `DOCUMENT_TEXT_DETECTION` instead.   
[`WEB_DETECTION`](https://docs.cloud.google.com/vision/docs/detecting-web) | Detect topical entities such as news, events, or celebrities within the image, and find similar images on the web using the power of Google Image Search.   
  
## Sample code

You can either send an annotation request with a locally stored file, or use a file that is stored on Cloud Storage.

### Using a locally stored file

Use the following code samples to get any [feature](https://docs.cloud.google.com/vision/docs/reference/rest/v1/Feature#type) annotation for a locally stored file.

### REST

To perform online PDF/TIFF/GIF feature detection for a small batch of files, make a POST request and provide the appropriate request body:

Before using any of the request data, make the following replacements: 

  * BASE64_ENCODED_FILE: The base64 representation (ASCII string) of your binary file data. This string should look similar to the following string: 
    * `JVBERi0xLjUNCiW1tbW1...ydHhyZWYNCjk5NzM2OQ0KJSVFT0Y=`
Visit the [base64 encode](https://docs.cloud.google.com/vision/docs/base64) topic for more information.
  * PROJECT_ID: Your Google Cloud project ID.



**Field-specific considerations:**

  * `inputConfig.mimeType` \- One of the following: "application/pdf", "image/tiff" or "image/gif". 
  * ` [pages](https://docs.cloud.google.com/vision/docs/reference/rest/v1/files/annotate#annotatefilerequest) ` \- specifies the specific pages of the file to perform feature detection. 



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/files:annotate

Request JSON body: 
    
    
    {
      "requests": [
        {
          "inputConfig": {
            "content": "BASE64_ENCODED_FILE",
            "mimeType": "application/pdf"
          },
          "features": [
            {
              "type": "DOCUMENT_TEXT_DETECTION"
            }
          ],
          "pages": [
            1,2,3,4,5
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
         "https://vision.googleapis.com/v1/files:annotate"

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
        -Uri "https://vision.googleapis.com/v1/files:annotate" | Select-Object -Expand Content

**Response:**

A successful `annotate` request immediately returns a JSON response.

For this feature (`DOCUMENT_TEXT_DETECTION`), the JSON response is similar to that of an image's [document text detection request](https://docs.cloud.google.com/vision/docs/handwriting). The response contains bounding boxes for blocks broken down by paragraphs, words, and individual symbols. The full text is also detected. The response also contains a `context` field showing the location of the PDF or TIFF that was specified and the result's page number in the file. 

The following response JSON is only for a single page (page 2) and has been shortened for clarity.

#### Response
    
    
    {
      "responses": [
        {
          "responses": [
            {
              "fullTextAnnotation": {
                "pages": [
                  {
                    "property": {
                      "detectedLanguages": [
                        {
                          "languageCode": "en",
                          "confidence": 0.99
                        },
                        {
                          "languageCode": "pl",
                          "confidence": 0.01
                        }
                      ]
                    },
                    "width": 1342,
                    "height": 2234,
                    "blocks": [
                      {
                        "boundingBox": {
                          "vertices": [
                          ...
                          ]
                        },
                        "paragraphs": [
                          {
                            "boundingBox": {
                              "vertices": [
                              ...
                              ]
                            },
                            "words": [
                              {
                                "property": {
                                  "detectedLanguages": [
                                    {
                                      "languageCode": "en"
                                    }
                                  ]
                                },
                                "boundingBox": {
                                  "vertices": [
                                  ...
                                  ]
                                },
                                "symbols": [
                                  {
                                    "property": {
                                      "detectedLanguages": [
                                        {
                                          "languageCode": "en"
                                        }
                                      ],
                                      "detectedBreak": {
                                        "type": "SPACE"
                                      }
                                    },
                                    "boundingBox": {
                                      "vertices": [
                                    ...
                                      ]
                                    },
                                    "text": "#",
                                    "confidence": 0.07
                                  }
                                ],
                                "confidence": 0.07
                              },
                              ...
                        ],
                        "blockType": "TEXT",
                        "confidence": 0.88
                      },
                      ...
                ...
                "text": "# THE STATE OF TEXAS\n0\nOIL, GAS AND MINERAL LEASE\n
                COUNTY OF MAVERICK\nTHIS AGREEMENT made this 14 day of_June\n1954,
                between Norvel J. Chittim and his wife, Lieschen G. Chittim;\nMary
                Anne Chittim Parker, joined herein pro forma by her husband,\nJoseph
                Bright Parker; Dorothea Chittim Oppenheimer, joined herein\nji pro
                forma by her husband, Fred J. Oppenheimer; Tuleta Chittim\nWright,
                joined herein pro forma by her husband, Gilbert G. Wright,\nJr.;
                Gilbert G. Wright, III; Delă Wright White, joined herein pro\nforma
                by her husband, John H. White; Anne Wright Basse, joined\nherein
                pro forma by her husband, E. A. Basse, Jr.; Norvel J.\nChittim,
                Independent Executor and Trustee for Estate of Marstella\nChittim,
                Deceased; Mary Louise Roswell, joined herein pro forma by\nher
                husband, Charles M. 'Roswell; and James M. Chittim and his wife\n
                Thelma Neal Chittim; as LESSORS, and W. L. Scheig of San Antonio,\n
                Texas, as LESSEE,\n10\nW ITNESS ETH:\nLessors, in consideration of
                $10.00, cash in hand paid, i\nof the royalties herein provided,
                and of the agreement of Lessee\nherein contained, hereby grant,
                lease and let exclusively unto\nLessee the tracts of land
                hereinafter described for the purpose of\ntesting for mineral
                indications, and in such tests use the Seismo-\ngraph, Torsion
                Balance, Core Drill, or any other tools, machinery,\nequipment
                or explosive necessary and proper; and also prospecting,\ndrilling
                and mining for and producing oil, gas and other minerals i\n
                (except metallic minerals), laying pipe lines, building tanks,\n
                power stations, telephone lines and other structures thereon to\n
                produce, save, take care of, treat, transport and own said pro-\n
                ducts and housing its employees (Lessee to conduct its geophysical\n
                work in such manner as not to damage the buildings, water tanks\n
                or wells of Lessors, or the livestock of Lessors or Lessors' ten-\n
                ants, ) said lands being situated in Maverick, Zavalla and Dimmit\n
                Counties, Texas, to-wit:\n3 -1.\n"
              },
              "context": {
                "pageNumber": 2
              }
            }
          ]
        }
      ]
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vision API Quickstart Using Client Libraries](https://docs.cloud.google.com/vision/docs/detect-labels-image-client-libraries). For more information, see the [ Vision API Java reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview).

**Note:** For Java **Spring framework** users, [Spring Cloud Google Cloud](https://docs.cloud.google.com/vision/docs/adding-spring) offers a way to automatically configure authentication settings and client objects to use Vision API. 
    
    
    import com.google.cloud.vision.v1.[AnnotateFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateFileRequest.html);
    import com.google.cloud.vision.v1.[AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html);
    import com.google.cloud.vision.v1.[BatchAnnotateFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesRequest.html);
    import com.google.cloud.vision.v1.[BatchAnnotateFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesResponse.html);
    import com.google.cloud.vision.v1.[Block](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Block.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.cloud.vision.v1.[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.InputConfig.html);
    import com.google.cloud.vision.v1.[Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Page.html);
    import com.google.cloud.vision.v1.[Paragraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Paragraph.html);
    import com.google.cloud.vision.v1.[Symbol](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Symbol.html);
    import com.google.cloud.vision.v1.[Word](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Word.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.nio.file.Paths;
    
    public class BatchAnnotateFiles {
    
      public static void batchAnnotateFiles() throws IOException {
        String filePath = "path/to/your/file.pdf";
        batchAnnotateFiles(filePath);
      }
    
      public static void batchAnnotateFiles(String filePath) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html) imageAnnotatorClient = [ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html).create()) {
          // You can send multiple files to be annotated, this sample demonstrates how to do this with
          // one file. If you want to use multiple files, you have to create a `AnnotateImageRequest`
          // object for each file that you want annotated.
          // First read the files contents
          Path path = Paths.get(filePath);
          byte[] data = Files.readAllBytes(path);
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) content = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(data);
    
          // Specify the input config with the file's contents and its type.
          // Supported mime_type: application/pdf, image/tiff, image/gif
          // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#inputconfig
          [InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.InputConfig.html) inputConfig =
              [InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.InputConfig.html).newBuilder().[setMimeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.InputConfig.Builder.html#com_google_cloud_vision_v1_InputConfig_Builder_setMimeType_java_lang_String_)("application/pdf").setContent(content).build();
    
          // Set the type of annotation you want to perform on the file
          // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Feature.Type
          [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html) feature = [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).newBuilder().setType([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).Type.DOCUMENT_TEXT_DETECTION).build();
    
          // Build the request object for that one file. Note: for additional file you have to create
          // additional `AnnotateFileRequest` objects and store them in a list to be used below.
          // Since we are sending a file of type `application/pdf`, we can use the `pages` field to
          // specify which pages to process. The service can process up to 5 pages per document file.
          // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.AnnotateFileRequest
          [AnnotateFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateFileRequest.html) fileRequest =
              [AnnotateFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateFileRequest.html).newBuilder()
                  .setInputConfig(inputConfig)
                  .addFeatures(feature)
                  .addPages(1) // Process the first page
                  .addPages(2) // Process the second page
                  .addPages(-1) // Process the last page
                  .build();
    
          // Add each `AnnotateFileRequest` object to the batch request.
          [BatchAnnotateFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesRequest.html) request =
              [BatchAnnotateFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesRequest.html).newBuilder().addRequests(fileRequest).build();
    
          // Make the synchronous batch request.
          [BatchAnnotateFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesResponse.html) response = imageAnnotatorClient.batchAnnotateFiles(request);
    
          // Process the results, just get the first result, since only one file was sent in this
          // sample.
          for ([AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html) imageResponse :
              response.[getResponsesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesResponse.html#com_google_cloud_vision_v1_BatchAnnotateFilesResponse_getResponsesList__)().get(0).getResponsesList()) {
            System.out.format("Full text: %s%n", imageResponse.getFullTextAnnotation().getText());
            for ([Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Page.html) page : imageResponse.getFullTextAnnotation().getPagesList()) {
              for ([Block](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Block.html) block : page.getBlocksList()) {
                System.out.format("%nBlock confidence: %s%n", block.getConfidence());
                for ([Paragraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Paragraph.html) par : block.getParagraphsList()) {
                  System.out.format("\tParagraph confidence: %s%n", par.getConfidence());
                  for ([Word](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Word.html) word : par.getWordsList()) {
                    System.out.format("\t\tWord confidence: %s%n", word.getConfidence());
                    for ([Symbol](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Symbol.html) symbol : word.getSymbolsList()) {
                      System.out.format(
                          "\t\t\tSymbol: %s, (confidence: %s)%n",
                          symbol.getText(), symbol.getConfidence());
                    }
                  }
                }
              }
            }
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const fileName = 'path/to/your/file.pdf';
    
    // Imports the Google Cloud client libraries
    const {ImageAnnotatorClient} = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)').v1;
    const fs = require('fs').promises;
    
    // Instantiates a client
    const client = new [ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    // You can send multiple files to be annotated, this sample demonstrates how to do this with
    // one file. If you want to use multiple files, you have to create a request object for each file that you want annotated.
    async function batchAnnotateFiles() {
      // First Specify the input config with the file's path and its type.
      // Supported mime_type: application/pdf, image/tiff, image/gif
      // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#inputconfig
      const inputConfig = {
        mimeType: 'application/pdf',
        content: await fs.readFile(fileName),
      };
    
      // Set the type of annotation you want to perform on the file
      // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Feature.Type
      const features = [{type: 'DOCUMENT_TEXT_DETECTION'}];
    
      // Build the request object for that one file. Note: for additional files you have to create
      // additional file request objects and store them in a list to be used below.
      // Since we are sending a file of type `application/pdf`, we can use the `pages` field to
      // specify which pages to process. The service can process up to 5 pages per document file.
      // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.AnnotateFileRequest
      const fileRequest = {
        inputConfig: inputConfig,
        features: features,
        // Annotate the first two pages and the last one (max 5 pages)
        // First page starts at 1, and not 0. Last page is -1.
        pages: [1, 2, -1],
      };
    
      // Add each `AnnotateFileRequest` object to the batch request.
      const request = {
        requests: [fileRequest],
      };
    
      // Make the synchronous batch request.
      const [result] = await client.batchAnnotateFiles(request);
    
      // Process the results, just get the first result, since only one file was sent in this
      // sample.
      const responses = result.responses[0].responses;
    
      for (const response of responses) {
        console.log(`Full text: ${response.fullTextAnnotation.text}`);
        for (const page of response.fullTextAnnotation.pages) {
          for (const block of page.blocks) {
            console.log(`Block confidence: ${block.confidence}`);
            for (const paragraph of block.paragraphs) {
              console.log(` Paragraph confidence: ${paragraph.confidence}`);
              for (const word of paragraph.words) {
                const symbol_texts = word.symbols.map(symbol => symbol.text);
                const word_text = symbol_texts.join('');
                console.log(
                  `  Word text: ${word_text} (confidence: ${word.confidence})`
                );
                for (const symbol of word.symbols) {
                  console.log(
                    `   Symbol: ${symbol.text} (confidence: ${symbol.confidence})`
                  );
                }
              }
            }
          }
        }
      }
    }
    
    batchAnnotateFiles();

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    
    from google.cloud import vision_v1
    
    
    def sample_batch_annotate_files(file_path="path/to/your/document.pdf"):
        """Perform batch file annotation."""
        client = vision_v1.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        # Supported mime_type: application/pdf, image/tiff, image/gif
        mime_type = "application/pdf"
        with open(file_path, "rb") as f:
            content = f.read()
        input_config = {"mime_type": mime_type, "content": content}
        features = [{"type_": vision_v1.[Feature](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Feature.html).Type.DOCUMENT_TEXT_DETECTION}]
    
        # The service can process up to 5 pages per document file. Here we specify
        # the first, second, and last page of the document to be processed.
        pages = [1, 2, -1]
        requests = [{"input_config": input_config, "features": features, "pages": pages}]
    
        response = client.[batch_annotate_files](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html#google_cloud_vision_v1_services_image_annotator_ImageAnnotatorClient_batch_annotate_files)(requests=requests)
        for image_response in response.responses[0].responses:
            print(f"Full text: {image_response.full_text_annotation.text}")
            for page in image_response.full_text_annotation.pages:
                for block in page.blocks:
                    print(f"\nBlock confidence: {block.confidence}")
                    for par in block.paragraphs:
                        print(f"\tParagraph confidence: {par.confidence}")
                        for word in par.words:
                            print(f"\t\tWord confidence: {word.confidence}")
                            for symbol in word.symbols:
                                print(
                                    "\t\t\tSymbol: {}, (confidence: {})".format(
                                        symbol.text, symbol.confidence
                                    )
                                )
    
    

### Using a file on Cloud Storage

Use the following code samples to get any [feature](https://docs.cloud.google.com/vision/docs/reference/rest/v1/Feature#type) annotation for a file on Cloud Storage.

### REST

To perform online PDF/TIFF/GIF feature detection for a small batch of files, make a `POST` request and provide the appropriate request body:

Before using any of the request data, make the following replacements: 

  * CLOUD_STORAGE_FILE_URI: the path to a valid file (PDF/TIFF) in a Cloud Storage bucket. You must at least have read privileges to the file. Example: 
    * gs://cloud-samples-data/vision/document_understanding/custom_0773375000.pdf

  * PROJECT_ID: Your Google Cloud project ID.



**Field-specific considerations:**

  * `inputConfig.mimeType` \- One of the following: "application/pdf", "image/tiff" or "image/gif". 
  * ` [pages](https://docs.cloud.google.com/vision/docs/reference/rest/v1/files/annotate#annotatefilerequest) ` \- specifies the specific pages of the file to perform feature detection. 



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/files:annotate

Request JSON body: 
    
    
    {
      "requests": [
        {
          "inputConfig": {
            "gcsSource": {
              "uri": "CLOUD_STORAGE_FILE_URI"
            },
            "mimeType": "application/pdf"
          },
          "features": [
            {
              "type": "DOCUMENT_TEXT_DETECTION"
            }
          ],
          "pages": [
            1,2,3,4,5
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
         "https://vision.googleapis.com/v1/files:annotate"

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
        -Uri "https://vision.googleapis.com/v1/files:annotate" | Select-Object -Expand Content

**Response:**

A successful `annotate` request immediately returns a JSON response.

For this feature (`DOCUMENT_TEXT_DETECTION`), the JSON response is similar to that of an image's [document text detection request](https://docs.cloud.google.com/vision/docs/handwriting). The response contains bounding boxes for blocks broken down by paragraphs, words, and individual symbols. The full text is also detected. The response also contains a `context` field showing the location of the PDF or TIFF that was specified and the result's page number in the file. 

The following response JSON is only for a single page (page 2) and has been shortened for clarity.

#### Response
    
    
    {
      "responses": [
        {
          "responses": [
            {
              "fullTextAnnotation": {
                "pages": [
                  {
                    "property": {
                      "detectedLanguages": [
                        {
                          "languageCode": "en",
                          "confidence": 0.99
                        },
                        {
                          "languageCode": "pl",
                          "confidence": 0.01
                        }
                      ]
                    },
                    "width": 1342,
                    "height": 2234,
                    "blocks": [
                      {
                        "boundingBox": {
                          "vertices": [
                          ...
                          ]
                        },
                        "paragraphs": [
                          {
                            "boundingBox": {
                              "vertices": [
                              ...
                              ]
                            },
                            "words": [
                              {
                                "property": {
                                  "detectedLanguages": [
                                    {
                                      "languageCode": "en"
                                    }
                                  ]
                                },
                                "boundingBox": {
                                  "vertices": [
                                  ...
                                  ]
                                },
                                "symbols": [
                                  {
                                    "property": {
                                      "detectedLanguages": [
                                        {
                                          "languageCode": "en"
                                        }
                                      ],
                                      "detectedBreak": {
                                        "type": "SPACE"
                                      }
                                    },
                                    "boundingBox": {
                                      "vertices": [
                                    ...
                                      ]
                                    },
                                    "text": "#",
                                    "confidence": 0.07
                                  }
                                ],
                                "confidence": 0.07
                              },
                              ...
                        ],
                        "blockType": "TEXT",
                        "confidence": 0.88
                      },
                      ...
                ...
                "text": "# THE STATE OF TEXAS\n0\nOIL, GAS AND MINERAL LEASE\n
                COUNTY OF MAVERICK\nTHIS AGREEMENT made this 14 day of_June\n1954,
                between Norvel J. Chittim and his wife, Lieschen G. Chittim;\nMary
                Anne Chittim Parker, joined herein pro forma by her husband,\nJoseph
                Bright Parker; Dorothea Chittim Oppenheimer, joined herein\nji pro
                forma by her husband, Fred J. Oppenheimer; Tuleta Chittim\nWright,
                joined herein pro forma by her husband, Gilbert G. Wright,\nJr.;
                Gilbert G. Wright, III; Delă Wright White, joined herein pro\nforma
                by her husband, John H. White; Anne Wright Basse, joined\nherein
                pro forma by her husband, E. A. Basse, Jr.; Norvel J.\nChittim,
                Independent Executor and Trustee for Estate of Marstella\nChittim,
                Deceased; Mary Louise Roswell, joined herein pro forma by\nher
                husband, Charles M. 'Roswell; and James M. Chittim and his wife\n
                Thelma Neal Chittim; as LESSORS, and W. L. Scheig of San Antonio,\n
                Texas, as LESSEE,\n10\nW ITNESS ETH:\nLessors, in consideration of
                $10.00, cash in hand paid, i\nof the royalties herein provided,
                and of the agreement of Lessee\nherein contained, hereby grant,
                lease and let exclusively unto\nLessee the tracts of land
                hereinafter described for the purpose of\ntesting for mineral
                indications, and in such tests use the Seismo-\ngraph, Torsion
                Balance, Core Drill, or any other tools, machinery,\nequipment
                or explosive necessary and proper; and also prospecting,\ndrilling
                and mining for and producing oil, gas and other minerals i\n
                (except metallic minerals), laying pipe lines, building tanks,\n
                power stations, telephone lines and other structures thereon to\n
                produce, save, take care of, treat, transport and own said pro-\n
                ducts and housing its employees (Lessee to conduct its geophysical\n
                work in such manner as not to damage the buildings, water tanks\n
                or wells of Lessors, or the livestock of Lessors or Lessors' ten-\n
                ants, ) said lands being situated in Maverick, Zavalla and Dimmit\n
                Counties, Texas, to-wit:\n3 -1.\n"
              },
              "context": {
                "pageNumber": 2
              }
            }
          ]
        }
      ]
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vision API Quickstart Using Client Libraries](https://docs.cloud.google.com/vision/docs/detect-labels-image-client-libraries). For more information, see the [ Vision API Java reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview).

**Note:** For Java **Spring framework** users, [Spring Cloud Google Cloud](https://docs.cloud.google.com/vision/docs/adding-spring) offers a way to automatically configure authentication settings and client objects to use Vision API. 
    
    
    import com.google.cloud.vision.v1.[AnnotateFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateFileRequest.html);
    import com.google.cloud.vision.v1.[AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html);
    import com.google.cloud.vision.v1.[BatchAnnotateFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesRequest.html);
    import com.google.cloud.vision.v1.[BatchAnnotateFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesResponse.html);
    import com.google.cloud.vision.v1.[Block](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Block.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.GcsSource.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.cloud.vision.v1.[InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.InputConfig.html);
    import com.google.cloud.vision.v1.[Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Page.html);
    import com.google.cloud.vision.v1.[Paragraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Paragraph.html);
    import com.google.cloud.vision.v1.[Symbol](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Symbol.html);
    import com.google.cloud.vision.v1.[Word](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Word.html);
    import java.io.IOException;
    
    public class BatchAnnotateFilesGcs {
    
      public static void batchAnnotateFilesGcs() throws IOException {
        String gcsUri = "gs://cloud-samples-data/vision/document_understanding/kafka.pdf";
        batchAnnotateFilesGcs(gcsUri);
      }
    
      public static void batchAnnotateFilesGcs(String gcsUri) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html) imageAnnotatorClient = [ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html).create()) {
          // You can send multiple files to be annotated, this sample demonstrates how to do this with
          // one file. If you want to use multiple files, you have to create a `AnnotateImageRequest`
          // object for each file that you want annotated.
          // First specify where the vision api can find the image
          [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.GcsSource.html) gcsSource = [GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.GcsSource.html).newBuilder().setUri(gcsUri).build();
    
          // Specify the input config with the file's uri and its type.
          // Supported mime_type: application/pdf, image/tiff, image/gif
          // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#inputconfig
          [InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.InputConfig.html) inputConfig =
              [InputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.InputConfig.html).newBuilder().[setMimeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.InputConfig.Builder.html#com_google_cloud_vision_v1_InputConfig_Builder_setMimeType_java_lang_String_)("application/pdf").setGcsSource(gcsSource).build();
    
          // Set the type of annotation you want to perform on the file
          // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Feature.Type
          [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html) feature = [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).newBuilder().setType([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).Type.DOCUMENT_TEXT_DETECTION).build();
    
          // Build the request object for that one file. Note: for additional file you have to create
          // additional `AnnotateFileRequest` objects and store them in a list to be used below.
          // Since we are sending a file of type `application/pdf`, we can use the `pages` field to
          // specify which pages to process. The service can process up to 5 pages per document file.
          // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.AnnotateFileRequest
          [AnnotateFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateFileRequest.html) fileRequest =
              [AnnotateFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateFileRequest.html).newBuilder()
                  .setInputConfig(inputConfig)
                  .addFeatures(feature)
                  .addPages(1) // Process the first page
                  .addPages(2) // Process the second page
                  .addPages(-1) // Process the last page
                  .build();
    
          // Add each `AnnotateFileRequest` object to the batch request.
          [BatchAnnotateFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesRequest.html) request =
              [BatchAnnotateFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesRequest.html).newBuilder().addRequests(fileRequest).build();
    
          // Make the synchronous batch request.
          [BatchAnnotateFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesResponse.html) response = imageAnnotatorClient.batchAnnotateFiles(request);
    
          // Process the results, just get the first result, since only one file was sent in this
          // sample.
          for ([AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html) imageResponse :
              response.[getResponsesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateFilesResponse.html#com_google_cloud_vision_v1_BatchAnnotateFilesResponse_getResponsesList__)().get(0).getResponsesList()) {
            System.out.format("Full text: %s%n", imageResponse.getFullTextAnnotation().getText());
            for ([Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Page.html) page : imageResponse.getFullTextAnnotation().getPagesList()) {
              for ([Block](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Block.html) block : page.getBlocksList()) {
                System.out.format("%nBlock confidence: %s%n", block.getConfidence());
                for ([Paragraph](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Paragraph.html) par : block.getParagraphsList()) {
                  System.out.format("\tParagraph confidence: %s%n", par.getConfidence());
                  for ([Word](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Word.html) word : par.getWordsList()) {
                    System.out.format("\t\tWord confidence: %s%n", word.getConfidence());
                    for ([Symbol](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Symbol.html) symbol : word.getSymbolsList()) {
                      System.out.format(
                          "\t\t\tSymbol: %s, (confidence: %s)%n",
                          symbol.getText(), symbol.getConfidence());
                    }
                  }
                }
              }
            }
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const gcsSourceUri = 'gs://cloud-samples-data/vision/document_understanding/kafka.pdf';
    
    // Imports the Google Cloud client libraries
    const {ImageAnnotatorClient} = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)').v1;
    
    // Instantiates a client
    const client = new [ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    // You can send multiple files to be annotated, this sample demonstrates how to do this with
    // one file. If you want to use multiple files, you have to create a request object for each file that you want annotated.
    async function batchAnnotateFiles() {
      // First Specify the input config with the file's uri and its type.
      // Supported mime_type: application/pdf, image/tiff, image/gif
      // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#inputconfig
      const inputConfig = {
        mimeType: 'application/pdf',
        gcsSource: {
          uri: gcsSourceUri,
        },
      };
    
      // Set the type of annotation you want to perform on the file
      // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.Feature.Type
      const features = [{type: 'DOCUMENT_TEXT_DETECTION'}];
    
      // Build the request object for that one file. Note: for additional files you have to create
      // additional file request objects and store them in a list to be used below.
      // Since we are sending a file of type `application/pdf`, we can use the `pages` field to
      // specify which pages to process. The service can process up to 5 pages per document file.
      // https://cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.AnnotateFileRequest
      const fileRequest = {
        inputConfig: inputConfig,
        features: features,
        // Annotate the first two pages and the last one (max 5 pages)
        // First page starts at 1, and not 0. Last page is -1.
        pages: [1, 2, -1],
      };
    
      // Add each `AnnotateFileRequest` object to the batch request.
      const request = {
        requests: [fileRequest],
      };
    
      // Make the synchronous batch request.
      const [result] = await client.batchAnnotateFiles(request);
    
      // Process the results, just get the first result, since only one file was sent in this
      // sample.
      const responses = result.responses[0].responses;
    
      for (const response of responses) {
        console.log(`Full text: ${response.fullTextAnnotation.text}`);
        for (const page of response.fullTextAnnotation.pages) {
          for (const block of page.blocks) {
            console.log(`Block confidence: ${block.confidence}`);
            for (const paragraph of block.paragraphs) {
              console.log(` Paragraph confidence: ${paragraph.confidence}`);
              for (const word of paragraph.words) {
                const symbol_texts = word.symbols.map(symbol => symbol.text);
                const word_text = symbol_texts.join('');
                console.log(
                  `  Word text: ${word_text} (confidence: ${word.confidence})`
                );
                for (const symbol of word.symbols) {
                  console.log(
                    `   Symbol: ${symbol.text} (confidence: ${symbol.confidence})`
                  );
                }
              }
            }
          }
        }
      }
    }
    
    batchAnnotateFiles();

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision_v1
    
    
    def sample_batch_annotate_files(
        storage_uri="gs://cloud-samples-data/vision/document_understanding/kafka.pdf",
    ):
        """Perform batch file annotation."""
        mime_type = "application/pdf"
    
        client = vision_v1.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        gcs_source = {"uri": storage_uri}
        input_config = {"gcs_source": gcs_source, "mime_type": mime_type}
        features = [{"type_": vision_v1.[Feature](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Feature.html).Type.DOCUMENT_TEXT_DETECTION}]
    
        # The service can process up to 5 pages per document file.
        # Here we specify the first, second, and last page of the document to be
        # processed.
        pages = [1, 2, -1]
        requests = [{"input_config": input_config, "features": features, "pages": pages}]
    
        response = client.[batch_annotate_files](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html#google_cloud_vision_v1_services_image_annotator_ImageAnnotatorClient_batch_annotate_files)(requests=requests)
        for image_response in response.responses[0].responses:
            print(f"Full text: {image_response.full_text_annotation.text}")
            for page in image_response.full_text_annotation.pages:
                for block in page.blocks:
                    print(f"\nBlock confidence: {block.confidence}")
                    for par in block.paragraphs:
                        print(f"\tParagraph confidence: {par.confidence}")
                        for word in par.words:
                            print(f"\t\tWord confidence: {word.confidence}")
                            for symbol in word.symbols:
                                print(
                                    "\t\t\tSymbol: {}, (confidence: {})".format(
                                        symbol.text, symbol.confidence
                                    )
                                )
    
    

## Try it

Try small batch online feature detection below.

You can use the PDF file specified already or specify your own file in its place.

![first five pages of a pdf file](https://docs.cloud.google.com/static/vision/docs/images/combined_small_batch.png)[gs://cloud-samples-data/vision/document_understanding/custom_0773375000.pdf](https://storage.cloud.google.com/cloud-samples-data/vision/document_understanding/custom_0773375000.pdf)

There are three feature types specified for this request:

  * `DOCUMENT_TEXT_DETECTION`
  * `LABEL_DETECTION`
  * `CROP_HINTS`



You can add or remove other feature types by changing the appropriate object in the request (`{"type": "FEATURE_NAME"}`).

Send the request by selecting **Execute**.

**Request body:**
    
    
    {
      "requests": [
        {
          "inputConfig": {
            "gcsSource": {
              "uri": "gs://cloud-samples-data/vision/document_understanding/custom_0773375000.pdf"
            },
            "mimeType": "application/pdf"
          },
          "features": [
            {
              "type": "DOCUMENT_TEXT_DETECTION"
            },
            {
              "type": "LABEL_DETECTION"
            },
            {
              "type": "CROP_HINTS"
            }
          ],
          "pages": [
            1,
            2,
            3,
            4,
            5
          ]
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

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
