---
url: https://docs.cloud.google.com/data-studio/create-a-thumbnail-image-of-your-report/
title: Create a thumbnail image of your report \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:08.173990+00:00
---

# Create a thumbnail image of your report  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/create-a-thumbnail-image-of-your-report/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Create a thumbnail image of your report Stay organized with collections  Save and categorize content based on your preferences. 

A thumbnail image is a smaller scale snapshot of your report. Thumbnails are useful for showing people a preview of the report's first page. Thumbnail images are stored in the cloud, so you can link to them with no need to download or upload.

**Tip:** See also: [Share reports on social media](https://docs.cloud.google.com/data-studio/share-reports-on-social-media)

## How thumbnails work

To display a thumbnail, append the `/thumbnail` endpoint to the URL of your report. This will create a scaled image of the first page of that report. For example, here's the thumbnail URL for the Google Ads report template:
    
    
    https://datastudio.google.com/reporting/0B5FF6JBKbNJxOWItcWo2SVVVeGc/page/DjD/thumbnail
    

The resulting thumbnail image shows the Google Ads report template.

![Google Ads report template](https://datastudio.google.com/c/reporting/0B_U5RNpwhcE6ckdmZEJ0ZDJXUnM/page/VgD/thumbnail)

Thumbnails are scaled to 320 px x 240 px. For long reports, the thumbnail will try to include the entire report page in those dimensions. For reports with a wide aspect ratio, such 16:9, the thumbnail will try to fit the entire height.

### Update the thumbnail image

To generate a new thumbnail image, edit and then view the report.

### Who can see the thumbnail?

Only people with View or Edit access to the report can see its thumbnail. In addition, any data sources for the report must be set to owner's or service account [credentials](https://docs.cloud.google.com/data-studio/data-credentials). People without proper access see a default Data Studio logo image instead.

![](https://docs.cloud.google.com/static/data-studio/images/looker-studio-logo-svg.svg)

You'll also see this icon for deleted reports.

## Use the thumbnail image

You can use thumbnail images in web pages by providing the report's `/thumbnail` URL as the `src` parameter of the HTML `<img>` tag.

## Troubleshooting thumbnails

Having trouble displaying a thumbnail image? Check the following:

  * Be sure you can view the report. Thumbnails are only available for reports you can see.

  * Edit the report, then view it again. This will generate a new thumbnail image.

**Note:** If you try to access a thumbnail for an older report that hasn't been edited in a while, you may see the default logo image. You can edit the report, and then view that report.
  * All the data sources added to the report must use Owner's Credentials. Thumbnails can't be shown for reports whose data source uses Viewer's Credentials.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
