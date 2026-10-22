---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/image-utilities/
title: Image utilities \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:51.890628+00:00
---

# Image utilities  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/image-utilities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Image utilities 

A set of utility actions to assist with analyzing, extracting, and converting image and file content during investigations. Key functions include optical character recognition (OCR) for text extraction, rasterization (converting web content to static images), and file format conversion. All actions require a Remote Agent.

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Convert File

Use the **Convert File** action to change the format of a specified file.

**Important:** This action requires a Remote Agent to function correctly.

#### Action inputs

The **Convert File** action requires the following parameters:

Parameter | Description  
---|---  
`Input File Format` | Required. The original format of the file that the action converts. The possible values are as follows:

  * `PNG`
  * `PDF`

The default value is `PNG`.  
`Input File Path` | Required. The path to the file that the action converts.  
`Output File Format` | Required. The resulting format of the file after the conversion process. The possible values are as follows:

  * `PNG`
  * `PDF`

The default value is `PDF`.  
  
#### Action outputs

The **Convert File** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result outputs received when using the **Convert File** action:
    
    
    [
       {
           "output_format": ""  
           "file_path": ""
       }
    ]
    

##### Output messages

The **Convert File** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully converted file.` | The action succeeded.  
`Error executing action "Convert File". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Convert File** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### OCR Image

Use the **OCR Image** action to perform OCR and extract text from an image file.

**Important:** This action requires a Remote Agent with the `tesseract-ocr` package installed to function correctly.

#### Action inputs

The **OCR Image** action requires the following parameters:

Parameter | Description  
---|---  
`Base64 Encoded Image` | Optional. The base64 encoded string of the image file.  
`File Path` | Required. The path to the image file. **Note:** If both `Base64 Encoded Image` and `File Path` are provided, `Base64 Encoded Image` is processed.   
  
#### Action outputs

The **OCR Image** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result outputs received when using the **OCR Image** action:
    
    
    { 
      "extracted_text": "",
    }
    

##### Output messages

The **OCR Image** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully performed OCR on the provided image.` | The action succeeded.  
`Error executing action "OCR Image". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **OCR Image** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Rasterize Content

Use the **Rasterize Content** action to convert vector or complex content into a fixed, bitmap image format.

**Important:** This action requires a Remote Agent with the `playwright` package installed to function correctly.

#### Remote Agent prerequisites (Debian)

To ensure the **Rasterize Content** action runs successfully on a Debian-based Remote Agent, you must install the following packages and dependencies:

##### Playwright Python Library

Install the Playwright Python Library using the following command:
    
    
    python3.11 -m pip install playwright
    

##### Browser dependencies

Install the necessary Chromium browser dependencies for Playwright to function correctly:
    
    
    playwright install --with-deps chromium
    

#### Action inputs

Parameter | Description  
---|---  
`Input Type` | Required. The type of content that the action uses as its primary input. The possible values are as follows:

  * `URL`
  * `Email`
  * `HTML`

The default value is `URL`.  
`URLs or Body` | Required. The input content to be rasterized, based on the selected `Input Type`. If `URL` is selected, provide a comma-separated list of URLs. If `Email` or `HTML` is selected, provide the full content body of that input type.  
`Output Type` | Optional. The resulting output format for the rasterized content. The possible values are as follows:

  * `PNG`
  * `PDF`
  * `Both`

The default value is `PNG`.  
`Export Method` | Optional. The method used to output the generated content. The possible values are as follows:

  * `Case Attachment`
  * `File Path`
  * `Both`

The default value is `Case Attachment`.  
`Width` | Required. The width (in pixels) used for the generated raster content. The default value is `1920`.  
`Height` | Required. The height (in pixels) used for the generated raster content. The default value is `1080`.  
`Full Screen` | Optional. If selected, the content is rendered across the entire browser window before being rasterized. Disabled by default.  
`Timeout` | Optional. The maximum time (in seconds) the browser dedicates to rendering the content before rasterization begins. The maximum value is `60`. The default value is `120`.  
`Wait For` | Optional. The specific state the browser must reach before the action proceeds with rasterization or content extraction. The `NETWORK_IDLE` state is generally the most reliable. The possible values are as follows:

  * `LOAD`
  * `DOM_CONTENT_LOADED`
  * `NETWORK_IDLE COMMIT`

The default value is `NETWORK_IDLE`.  
`Wait for Selector` | Optional. A CSS selector that the action waits for to appear on the page before capturing the screenshot. **Note:** This setting is highly recommended for pages where content loads dynamically, as it confirms all elements are present before the action executes.   
  
#### Action outputs

The **Rasterize Content** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result outputs received when using the **Rasterize Content** action:
    
    
    [
       {
           "attachment_name": "",
           "file_path": ""
       }
    ]
    

##### Output messages

The **Rasterize Content** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully rasterized content based on the provided input.` `Successfully rasterized content based on the following URLs: URLS` `Action wasn't able to rasterize content for the following URLs: URLS` `Action wasn't able to rasterize content for the provided URLs.` | The action succeeded.  
`Error executing action "Rasterize Content". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Rasterize Content** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
