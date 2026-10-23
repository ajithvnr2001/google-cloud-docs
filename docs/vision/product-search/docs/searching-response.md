---
url: https://docs.cloud.google.com/vision/product-search/docs/searching-response/
title: Understanding search responses & multi-detection \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:47.852426+00:00
---

# Understanding search responses & multi-detection  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/searching-response/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/product-search/docs/create-product-set-search-products)



Send feedback 

#  Understanding search responses & multi-detection Stay organized with collections  Save and categorize content based on your preferences. 

Vision API Product Search can detect and find matching products for a single product in a search image, or identify and list matching products for multiple products if they are present in your image.

## Single-product images & response

This search image contains a single product.

![dress image in cloud storage bucket](https://docs.cloud.google.com/static/vision/product-search/docs/images/quickstart-search_for_matching_images_SML.jpg)`gs://cloud-ai-vision-data/product-search-tutorial/images/468f782e70ba11e8941fd20059124800.jpg`

Searching for similar products with Vision API Product Search returns a response that indicates two bounding boxes in the image, one box around the product and another box around the entire image.

Expand the section below to view the entire response.

**Full response**

**Note: Zero coordinate values omitted.** When the API detects a coordinate ("x" or "y") value of 0, **_that coordinate is omitted in the JSON response_**. Thus, a response with a bounding poly around the entire image would be   
**[{},{"x": 1},{"x": 1,"y": 1},{"y": 1}]**. For more information, see the [API Reference documentation](https://cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.products.referenceImages#boundingpoly). 
    
    {
      "responses": [
        {
          "productSearchResults": {
            "indexTime": "2018-12-04T22:33:53.673600055Z",
            "results": [
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/product_id16",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 1,
                "image": "projects/project-id/locations/location-id/products/product_id16/referenceImages/image16"
              },
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/product_id29",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.34263745,
                "image": "projects/project-id/locations/location-id/products/product_id29/referenceImages/image29"
              },
              ...
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/product_id89",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.20485385,
                "image": "projects/project-id/locations/location-id/products/product_id89/referenceImages/image89"
              }
            ],
            "productGroupedResults": [
              {
                **"boundingPoly" : {
                  "normalizedVertices": [
                    {
                      "x": 0.25610325,
                      "y": 0.1357359
                    },
                    {
                      "x": 0.77213204,
                      "y": 0.1357359
                    },
                    {
                      "x": 0.77213204,
                      "y": 0.9287346
                    },
                    {
                      "x": 0.25610325,
                      "y": 0.9287346
                    }
                  ]
                }**,
                "results": [
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/product_id16",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 1,
                    "image": "projects/project-id/locations/location-id/products/product_id16/referenceImages/image16"
                  },
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/product_id29",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.3345438,
                    "image": "projects/project-id/locations/location-id/products/product_id29/referenceImages/image29"
                  },
                  ...
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/product_id76",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "shoe"
                        }
                      ]
                    },
                    "score": 0.20218614,
                    "image": "projects/project-id/locations/location-id/products/product_id76/referenceImages/image76"
                  }
                ]
              },
              {
                **"boundingPoly" : {
                  "normalizedVertices": [
                    {},
                    {
                      "x": 1
                    },
                    {
                      "x": 1,
                      "y": 1
                    },
                    {
                      "y": 1
                    }
                  ]
                }**,
                "results": [
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/product_id16",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 1,
                    "image": "projects/project-id/locations/location-id/products/product_id16/referenceImages/image16"
                  },
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/product_id29",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.3507311,
                    "image": "projects/project-id/locations/location-id/products/product_id29/referenceImages/image29"
                  },
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/product_id8",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.26709077,
                    "image": "projects/project-id/locations/location-id/products/product_id8/referenceImages/image8"
                  },
                  ...
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/product_id51",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.21597815,
                    "image": "projects/project-id/locations/location-id/products/product_id51/referenceImages/image51"
                  }
                ]
              }
            ]
          }
        }
      ]
    }




### Bounding boxes & matching products

The following two products (bounding boxes) in the image are specified by the two sets of vertices returned from the request.

Matching products are listed for _each box_ identified by Vision API Product Search.

![image with 3 dresses in cloud storage bucket](https://docs.cloud.google.com/static/vision/product-search/docs/images/searching-response-bounding_boxes_and_matching_products.jpg)`gs://cloud-samples-data/product_search/multiple_dresses.jpg`

In the API response bounding boxes and matching products results are listed in the `productGroupedResults` field. They are grouped by products detected in an image. Each `boundingPoly` entry lists the region specified with normalized vertices (on a 0 to 1 scale, not corresponding to the actual pixel values of the image). Matching products for that specific region are then listed.

The following section from the response corresponds to the bounding box around the dress.

**Single product box response section**
    
    ....
            "productGroupedResults": [
              {
                **"boundingPoly" : {
                  "normalizedVertices": [
                    {
                      "x": 0.25610325,
                      "y": 0.1357359
                    },
                    {
                      "x": 0.77213204,
                      "y": 0.1357359
                    },
                    {
                      "x": 0.77213204,
                      "y": 0.9287346
                    },
                    {
                      "x": 0.25610325,
                      "y": 0.9287346
                    }
                  ]
                }**,
                "results": [
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/product_id16",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels":...
                    "score": 1,
                    ...




Matching products are listed after the `results` field, and are ranked by matching score in descending order. Scores range from 0 (no confidence) to 1 (full confidence).

![image of 5 matching products](https://docs.cloud.google.com/static/vision/product-search/docs/images/single_product_matches.jpg)`Several matching products for the dress`

The other `boundingPoly` returned in the response is around the entire image. Its normalized vertices are listed as:

  * `[{},{"x": 1},{"x": 1,"y": 1},{"y": 1}]`



**When coordinate values are 0 they are omitted**. Thus, the bounding poly specified above corresponds to:

  * `[{"x": 0,"y": 0},{"x": 1, "y": 0},{"x": 1,"y": 1},{"y": 1}]`



Matching products are then similarly listed for this bounding box (the entire image).

## Multiple-product images (multi-detection) & response

The following search image contains multiple products.

![image with 3 dresses in cloud storage bucket](https://docs.cloud.google.com/static/vision/product-search/docs/images/searching-response-search_response_multi_detection.jpg)`gs://cloud-samples-data/product_search/multiple_dresses.jpg`

Using Vision API Product Search to search for similar products returns a response that identifies multiple bounding boxes in the image, one for the entire image and also three boxes for each of the three dresses.

Expand the section below to view the entire response.

**Full response**

**Note: Zero coordinate values omitted.** When the API detects a coordinate ("x" or "y") value of 0, **_that coordinate is omitted in the JSON response_**. Thus, a response with a bounding poly around the entire image would be   
**[{},{"x": 1},{"x": 1,"y": 1},{"y": 1}]**. For more information, see the [API Reference documentation](https://cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.products.referenceImages#boundingpoly). 
    
    {
      "responses": [
        {
          "productSearchResults": {
            "indexTime": "2018-12-05T18:34:22.231193168Z",
            "results": [
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/product_id89",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.40636745,
                "image": "projects/project-id/locations/location-id/products/product_id89/referenceImages/image89"
              },
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/product_id56",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.35433072,
                "image": "projects/project-id/locations/location-id/products/product_id56/referenceImages/image56"
              },
              ...
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/product_id92",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.30736163,
                "image": "projects/project-id/locations/location-id/products/product_id92/referenceImages/image92"
              }
            ],
            **"productGroupedResults" : [
              {
                "boundingPoly": {
                  "normalizedVertices": [
                    {
                      "x": 0.38727918,
                      "y": 0.10391616
                    },
                    {
                      "x": 0.57177967,
                      "y": 0.10391616
                    },
                    {
                      "x": 0.57177967,
                      "y": 0.94973093
                    },
                    {
                      "x": 0.38727918,
                      "y": 0.94973093
                    }
                  ]
                }**,
                "results": [
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/product_id39",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.36689043,
                    "image": "projects/project-id/locations/location-id/products/product_id39/referenceImages/image39"
                  },
                  {
                    **"boundingPoly" : {
                      "normalizedVertices": [
                        {
                          "x": 0.63010275,
                          "y": 0.08650439
                        },
                        {
                          "x": 0.88989735,
                          "y": 0.08650439
                        },
                        {
                          "x": 0.88989735,
                          "y": 0.9285545
                        },
                        {
                          "x": 0.63010275,
                          "y": 0.9285545
                        }
                      ]
                    }**,
                    "results": [
                      {
                        "product": {
                          "name": "projects/project-id/locations/location-id/products/product_id89",
                          "displayName": " ",
                          "productCategory": "apparel",
                          "productLabels": [
                            {
                              "key": "style",
                              "value": "women"
                            },
                            {
                              "key": "category",
                              "value": "dress"
                            }
                          ]
                        },
                        "score": 0.4007347,
                        "image": "projects/project-id/locations/location-id/products/product_id89/referenceImages/image89"
                      },
                      ...
                      {
                        "product": {
                          "name": "projects/project-id/locations/location-id/products/product_id30",
                          "displayName": " ",
                          "productCategory": "apparel",
                          "productLabels": [
                            {
                              "key": "style",
                              "value": "women"
                            },
                            {
                              "key": "category",
                              "value": "dress"
                            }
                          ]
                        },
                        "score": 0.27045864,
                        "image": "projects/project-id/locations/location-id/products/product_id30/referenceImages/image30"
                      },
                      ...
                      {
                        "product": {
                          "name": "projects/project-id/locations/location-id/products/product_id63",
                          "displayName": " ",
                          "productCategory": "apparel",
                          "productLabels": [
                            {
                              "key": "style",
                              "value": "women"
                            },
                            {
                              "key": "category",
                              "value": "dress"
                            }
                          ]
                        },
                        "score": 0.23139484,
                        "image": "projects/project-id/locations/location-id/products/product_id63/referenceImages/image63"
                      }
                    ]
                  },
                  ...
                  {
                    **"boundingPoly" : {
                      "normalizedVertices": [
                        {},
                        {
                          "x": 1
                        },
                        {
                          "x": 1,
                          "y": 1
                        },
                        {
                          "y": 1
                        }
                      ]
                    }**,
                    "results": [
                      {
                        "product": {
                          "name": "projects/project-id/locations/location-id/products/product_id30",
                          "displayName": " ",
                          "productCategory": "apparel",
                          "productLabels": [
                            {
                              "key": "style",
                              "value": "women"
                            },
                            {
                              "key": "category",
                              "value": "dress"
                            }
                          ]
                        },
                        "score": 0.39522344,
                        "image": "projects/project-id/locations/location-id/products/product_id30/referenceImages/image30"
                      },
                      ...
                      {
                        "product": {
                          "name": "projects/project-id/locations/location-id/products/product_id4",
                          "displayName": " ",
                          "productCategory": "apparel",
                          "productLabels": [
                            {
                              "key": "style",
                              "value": "women"
                            },
                            {
                              "key": "category",
                              "value": "dress"
                            }
                          ]
                        },
                        "score": 0.34226564,
                        "image": "projects/project-id/locations/location-id/products/product_id4/referenceImages/image4"
                      }
                    ]
                  },
                  {
                    **"boundingPoly" : {
                      "normalizedVertices": [
                        {
                          "x": 0.030102689,
                          "y": 0.067680866
                        },
                        {
                          "x": 0.28942674,
                          "y": 0.067680866
                        },
                        {
                          "x": 0.28942674,
                          "y": 0.94973093
                        },
                        {
                          "x": 0.030102689,
                          "y": 0.94973093
                        }
                      ]
                    }**,
                    "results": [
                      {
                        "product": {
                          "name": "projects/project-id/locations/location-id/products/product_id89",
                          "displayName": " ",
                          "productCategory": "apparel",
                          "productLabels": [
                            {
                              "key": "style",
                              "value": "women"
                            },
                            {
                              "key": "category",
                              "value": "dress"
                            }
                          ]
                        },
                        "score": 0.42439392,
                        "image": "projects/project-id/locations/location-id/products/product_id89/referenceImages/image89"
                      },
                      ...
                      {
                        "product": {
                          "name": "projects/project-id/locations/location-id/products/product_id51",
                          "displayName": " ",
                          "productCategory": "apparel",
                          "productLabels": [
                            {
                              "key": "style",
                              "value": "women"
                            },
                            {
                              "key": "category",
                              "value": "dress"
                            }
                          ]
                        },
                        "score": 0.26797917,
                        "image": "projects/project-id/locations/location-id/products/product_id51/referenceImages/image51"
                      }
                    ]
                  }
                ]
              }
            }
          ]
    }




### Bounding boxes & matching products

The following image shows all bounding boxes identified by Vision API Product Search in this multi-product image.

![image with 3 dresses in cloud storage bucket](https://docs.cloud.google.com/static/vision/product-search/docs/images/searching-response_multidetection_bounding_boxes_and_matching_products_MED.jpg)`gs://cloud-samples-data/product_search/multiple_dresses.jpg`

Similar to a single-product image, a multi-product image's response lists bounding boxes and matching products results in the `productGroupedResults` field. Each product is identified by a bounding poly, and matches are grouped by each product detected.

The following section from the response corresponds to the bounding box around the **middle dress**.

**Product box response section (middle dress)**
    
    **"productGroupedResults" : [
              {
                "boundingPoly": {
                  "normalizedVertices": [
                    {
                      "x": 0.38727918,
                      "y": 0.10391616
                    },
                    {
                      "x": 0.57177967,
                      "y": 0.10391616
                    },
                    {
                      "x": 0.57177967,
                      "y": 0.94973093
                    },
                    {
                      "x": 0.38727918,
                      "y": 0.94973093
                    }
                  ]
                }**,
                "results": [
                  {
                    "product": {
                      "name":...
                    "score": 0.36689043,
                    ...




The following image shows some of the matches for the middle dress returned by Vision API Product Search.

![image of 5 matching products](https://docs.cloud.google.com/static/vision/product-search/docs/images/multi_product_matches.jpg)`Several matching products for the middle dress`

The following other bounding boxes are found in the image, each with their own list of matching products (not included here):

  * left dress: `{"x":0.03, "y":0.07},{"x":0.29, "y":0.07},{"x":0.29, "y":0.95},{"x":0.03, "y":0.95}`
  * right dress: `{"x":0.63, "y":0.09},{"x":0.89, "y":0.09},{"x":0.89, "y":0.93},{"x":0.63, "y":0.93}`
  * whole image: 
    * `{},{"x": 1},{"x": 1,"y": 1},{"y": 1}`, also expressed as:
    * `{"x": 0, "y": 0},{"x": 1,"y:0"},{"x": 1,"y": 1},{"x": 0,"y": 1}`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
