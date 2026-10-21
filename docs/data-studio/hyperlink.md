---
url: https://docs.cloud.google.com/data-studio/hyperlink/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:40.666889+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/hyperlink/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# HYPERLINK

Use the `HYPERLINK` function to create clickable text and image links in tables. Report viewers can click these links to navigate to other pages in your report or on the web.

## Sample usage

Create a link to a product catalog page and display the item name as the anchor text:

`HYPERLINK(Item URL, Item Name)`

Display an image of a product and link to that item's page in your catalog:

`HYPERLINK(Item URL, Item Image)`

## Syntax
    
    
        HYPERLINK(URL, anchor_text)
        HYPERLINK(URL, image)
    

### Parameters

  * `URL` \- A field or an expression that evaluates to the **URL** data type
  * `anchor_text` \- A field or an expression that evaluates to the **Text** data type
  * `image` \- A field or an expression that evaluates to the **Image** data type



## How the `HYPERLINK` function works

The `HYPERLINK` function has two forms: The first form creates a text link field, and the second form creates an image link field. Text link fields have the **Hyperlink** data type, while image link fields have the **Image Link** data type in your data source. You can add these fields to tables in your reports to give users a way to navigate to other pages.

The `HYPERLINK` function requires two parameters: the first parameter _must_ be a **URL**. If the second parameter is a **Text** field or expression, the function creates a **Hyperlink** field. If the second parameter is an **Image** field or expression, the function creates an **Image Link** field.

The `URL` parameter provides the link target (the `href` portion of the link). The `URL` parameter can come from existing [URL fields](https://docs.cloud.google.com/data-studio/hyperlinks-in-data) in the data source, or the parameter can be an expression that builds URLs from other fields and functions.

The `anchor_text` parameter specifies the linked text to display. The `anchor_text` parameter can be from a **Text** data type dimension in your data source or any other expression that evaluates to the **Text** data type.

To create an **Image Link** field, provide an **Image** dimension in your data source or any other expression that evaluates to the **Image** data type in place of the `image` parameter.

**Tips** : 

  * Use the [`IMAGE` function](https://docs.cloud.google.com/data-studio/image) to create **Image** fields.
  * To display a clickable link in a table that displays the full URL as the anchor text, you can also use the [URL field type](https://docs.cloud.google.com/data-studio/hyperlinks-in-data).



### Supported protocols

The `HYPERLINK` function supports the following protocols:

  * `http`
  * `https`
  * `mailto`
  * `ftp`



If you specify an unsupported protocol, the link opens a blank page. If you don't specify a protocol, the `HYPERLINK` function prepends `http:` to the URL.

## Examples

Use `HYPERLINK` to create a product catalog with pictures of the items that have been sold and links to individual product description pages.

Suppose you have a dataset with the following fields:

  * **Item** \- The name of the product
  * **SKU** \- The product identifier
  * **Product Page** \- The URL of the product's description page
  * **Product Image** \- The URL of the picture of the product that you want to display



For example:

Item  |  SKU  |  Product Page  |  Product Image   
---|---|---|---  
Pen  |  123  |  https://example.com/products/product123.html  |  https://example.com/images/product123.jpg   
Notebook  |  456  |  https://example.com/products/product456.html  |  https://example.com/images/product456.jpg   
Coffee Cup  |  789  |  https://example.com/products/product789.html  |  https://example.com/images/product789.jpg   
  
Creating a data source from the previous example gives you the following fields:

Field  |  Type   
---|---  
Item  |  Text   
SKU  |  Text   
Product Page  |  URL   
Product Image  |  URL   
  
### Example 1: Create text links to product pages

To display links to the product description pages, create a **Product Link** calculated field with this formula:

`HYPERLINK (Product Page, SKU )`

The data source now looks like this:

Field  |  Type   
---|---  
Item  |  Text   
SKU  |  Text   
Product Page  |  URL   
Product Image  |  URL   
Product Link  |  Hyperlink   
  
You can then add the **Product Link** field to a table in your report. This displays the data as clickable links.

### Example 2: Build URLs using `CONCAT`

Building URLs with the `CONCAT` function is useful when only part of the link path is present in a field or when you want to override or add more information to the link.

For example, you could use `CONCAT` to combine a hardcoded page path with a product SKU to form a complete URL to your product description page:

`HYPERLINK(CONCAT("http://example.com/productpages/product", SKU, ".html"), Item)`

### Example 3: Create clickable images

To add clickable images to a table, you also use the `HYPERLINK` function but provide a URL as the first parameter and an **Image** field, or an `IMAGE` function with a valid link to an image, as the second parameter. This creates an **Image Link** field.

In this example, the **Product Page** dimension holds the URL, and the `IMAGE` function generates an Image field using a single hard-coded value:

`HYPERLINK(Product Page, IMAGE("https://example.com/images/product789.jpg", "Coffee cup")`

As a more realistic example, you might either create the **Image** field ahead of time and store it in your data source or use the `CONCAT` function to build the `IMAGE` parameter:

`HYPERLINK(Product Page, IMAGE(CONCAT("https://example.com/images/"), SKU, ".jpg", Item))`

## Links and thumbnail images from YouTube

The [YouTube Analytics connector](https://docs.cloud.google.com/data-studio/connect-to-youtube-analytics) automatically provides links and thumbnail image fields you can add directly to tables in your reports:

Field  |  Type  |  Description   
---|---|---  
Video Link  |  URL  |  The link to the video on YouTube   
Thumbnail Link  |  URL  |  The link to the video thumbnail image   
Thumbnail  |  Image  |  The thumbnail image   
Linked Thumbnail  |  Image Link  |  The thumbnail image formatted as a link to the video on YouTube   
  
## Notes and limitations

  * Important: When users click an external link, Data Studio displays a redirect notice. This is a security feature to warn users that they are leaving Data Studio. It cannot be disabled or bypassed.
  * You can't change the data type of **Hyperlink** fields.
  * If you've enabled [Viewer's credentials](https://docs.cloud.google.com/data-studio/data-credentials-article#viewers-credentials) for a data source, Data Studio won't render hyperlinks. This limitation does not apply if the report creator and the viewer are members of the same Data Studio Pro team workspace.



## Related resources

  * [Hyperlinks in data](https://docs.cloud.google.com/data-studio/hyperlinks-in-data)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
