---
url: https://docs.cloud.google.com/data-studio/image/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:08.495604+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/image/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# IMAGE

The `IMAGE` function creates **Image** fields in your data source. **Image** fields display images in tables. Use this to show product images, video thumbnails, and other graphical information in your reports.

## Sample usage

Create a link to a product catalog page and display the product SKU as the link label:

`IMAGE("www.example.com/cat-pictures/pic100.jpg", "A cute kitten playing with string.")`

## Syntax

`IMAGE( image_URL, [ alt_text ])`

### Parameters

  * `image_URL` \- a field or expression that evaluates to a **URL**.
  * `alt_text` \- (optional) a field or expression that evaluates to **Text**.



## How the `IMAGE` function works

The `IMAGE` function takes a URL as input. The `image_URL` parameter can come from existing [URL fields](https://docs.cloud.google.com/data-studio/hyperlinks-in-data) in the data source, or the parameter can be an expression that builds URLs from other fields and functions.

The optional `alt_text` parameter provides the image's alternative text, which can be used by screen readers to assist vision-impaired users.

To display images in a report, add the **Image** field created by the `IMAGE` function to a table in your report. The size of the image displayed depends on the width of the column containing the image. If the URL is incorrect, or the image type is not supported, a broken image icon is displayed instead.

You can't change the data type of **Image Link** fields.

## Examples

### Example 1: Display YouTube thumbnails

  1. Edit your YouTube Analytics data source
  2. Create a calculated field (for example, **Thumbnail** )
  3. Use this formula to create an **Image** field:

`IMAGE(CONCAT('https://i.ytimg.com/vi/', External Video Id, '/hqdefault.jpg'), Video Title)`

  4. Add the **Thumbnail** field as a dimension in a table:




![A table chart with Video Title, Thumbnail, and Views columns displays image thumbnails in the Thumbnail column.](https://docs.cloud.google.com/static/data-studio/images/images-in-tables-example-2017-11-14.png)

### Example 2: Create clickable images with HYPERLINK

The images displayed in **Image** fields are static, but you can generate clickable images by providing an **Image** field as the `image` parameter to the [`HYPERLINK` function](https://docs.cloud.google.com/data-studio/hyperlink).

## Limits of the  IMAGE  function

### Images in tables only

**Image** fields only work in tables. If you change the visualization type, any **Image** fields in the chart will be ignored, or the `image_URL` will appear as the dimension value.

### Images and your data

In addition to the name of a file you want view, hyperlinks and image URLs can also send information, in the form of query parameters appended to the URL path. For example:

`http://some.domain.com/a/b/c/somefile.jpg?foo=bar&baz=bat`

This URL is requesting the JPEG image `somefile.jpg`. It is also sending data using the `foo` and `bar` parameters.

When reports or data sources contain hyperlinks or image URLs, you should make sure that these point to trusted domains, and that any additional data being sent makes sense to you.

To help with this, images in Data Studio have the following limits:

#### Images and the data control

When a report includes a data control, images appear when:

  * the data control is showing the default dataset
  * the data control is showing a different (non-default) dataset and the **Image** field is serving images from a trusted domain. This includes most Google domains.



If the data control is showing a different (non-default) dataset and images are requested from an untrusted domain, images won't appear. Instead, the table will display the image URL. Report viewers can click the URL to view the image, and are shown a dialog asking them to make sure the link goes to a trusted domain.

#### Images in copied data sources

When you copy a data source, all **Image** fields are disabled in the copy. You can re-enable images by doing the following:

  1. Edit the data source
  2. For each field you want to enable, click ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png)
  3. Select **Enable**.



![](https://docs.cloud.google.com/static/data-studio/images/enable-field-2017-11-28.png)

#### Images in data sources using Viewer's Credentials

If you've enabled [Viewer's Credentials](https://docs.cloud.google.com/data-studio/data-credentials-article#viewers-credentials) for a data source, Data Studio won't render **Image** fields.

## Related resources

  * [Hyperlinks in data](https://docs.cloud.google.com/data-studio/hyperlinks-in-data)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)
  * [Table reference](https://docs.cloud.google.com/data-studio/table-reference)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
