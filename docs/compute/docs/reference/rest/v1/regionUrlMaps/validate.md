---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/validate/
title: Method: regionUrlMaps.validate \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:43.185102+00:00
---

# Method: regionUrlMaps.validate  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/validate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: regionUrlMaps.validate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
      * JSON representation
      * JSON representation
        * JSON representation
          * JSON representation
          * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
          * JSON representation
        * JSON representation
        * JSON representation
          * JSON representation
        * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
          * JSON representation
          * JSON representation
        * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
          * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
      * JSON representation
      * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Response body
    * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Runs static validation for the UrlMap. In particular, the tests of the provided UrlMap will be run. Calling this method does NOT create the UrlMap.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`POST https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/urlMaps/{urlMap}/validate`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region scoping this request.  
`urlMap` |  `string` Name of the UrlMap resource to be validated as.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "resource": {
        "kind": string,
        "id": string,
        "creationTimestamp": string,
        "name": string,
        "description": string,
        "selfLink": string,
        "hostRules": [
          {
            "description": string,
            "hosts": [
              string
            ],
            "pathMatcher": string
          }
        ],
        "pathMatchers": [
          {
            "name": string,
            "description": string,
            "defaultService": string,
            "defaultRouteAction": {
              "weightedBackendServices": [
                {
                  "backendService": string,
                  "weight": integer,
                  "headerAction": {
                    "requestHeadersToRemove": [
                      string
                    ],
                    "requestHeadersToAdd": [
                      {
                        "headerName": string,
                        "headerValue": string,
                        "replace": boolean
                      }
                    ],
                    "responseHeadersToRemove": [
                      string
                    ],
                    "responseHeadersToAdd": [
                      {
                        "headerName": string,
                        "headerValue": string,
                        "replace": boolean
                      }
                    ]
                  }
                }
              ],
              "urlRewrite": {
                "pathPrefixRewrite": string,
                "hostRewrite": string,
                "pathTemplateRewrite": string,
                "regexRewrite": {
                  "pathPattern": string,
                  "pathSubstitution": string
                }
              },
              "timeout": {
                "seconds": string,
                "nanos": integer
              },
              "retryPolicy": {
                "retryConditions": [
                  string
                ],
                "numRetries": integer,
                "perTryTimeout": {
                  "seconds": string,
                  "nanos": integer
                }
              },
              "requestMirrorPolicy": {
                "backendService": string,
                "mirrorPercent": number
              },
              "corsPolicy": {
                "allowOrigins": [
                  string
                ],
                "allowOriginRegexes": [
                  string
                ],
                "allowMethods": [
                  string
                ],
                "allowHeaders": [
                  string
                ],
                "exposeHeaders": [
                  string
                ],
                "maxAge": integer,
                "allowCredentials": boolean,
                "disabled": boolean
              },
              "faultInjectionPolicy": {
                "delay": {
                  "fixedDelay": {
                    "seconds": string,
                    "nanos": integer
                  },
                  "percentage": number
                },
                "abort": {
                  "httpStatus": integer,
                  "percentage": number
                }
              },
              "maxStreamDuration": {
                "seconds": string,
                "nanos": integer
              },
              "cachePolicy": {
                "cacheKeyPolicy": {
                  "includeProtocol": boolean,
                  "includeHost": boolean,
                  "includeQueryString": boolean,
                  "includedQueryParameters": [
                    string
                  ],
                  "excludedQueryParameters": [
                    string
                  ],
                  "includedHeaderNames": [
                    string
                  ],
                  "includedCookieNames": [
                    string
                  ]
                },
                "requestCoalescing": boolean,
                "cacheMode": enum,
                "defaultTtl": {
                  "seconds": string,
                  "nanos": integer
                },
                "maxTtl": {
                  "seconds": string,
                  "nanos": integer
                },
                "clientTtl": {
                  "seconds": string,
                  "nanos": integer
                },
                "negativeCaching": boolean,
                "negativeCachingPolicy": [
                  {
                    "code": integer,
                    "ttl": {
                      "seconds": string,
                      "nanos": integer
                    }
                  }
                ],
                "cacheBypassRequestHeaderNames": [
                  string
                ],
                "serveWhileStale": {
                  "seconds": string,
                  "nanos": integer
                }
              }
            },
            "defaultUrlRedirect": {
              "hostRedirect": string,
              "pathRedirect": string,
              "prefixRedirect": string,
              "redirectResponseCode": enum,
              "httpsRedirect": boolean,
              "stripQuery": boolean
            },
            "pathRules": [
              {
                "service": string,
                "routeAction": {
                  "weightedBackendServices": [
                    {
                      "backendService": string,
                      "weight": integer,
                      "headerAction": {
                        "requestHeadersToRemove": [
                          string
                        ],
                        "requestHeadersToAdd": [
                          {
                            "headerName": string,
                            "headerValue": string,
                            "replace": boolean
                          }
                        ],
                        "responseHeadersToRemove": [
                          string
                        ],
                        "responseHeadersToAdd": [
                          {
                            "headerName": string,
                            "headerValue": string,
                            "replace": boolean
                          }
                        ]
                      }
                    }
                  ],
                  "urlRewrite": {
                    "pathPrefixRewrite": string,
                    "hostRewrite": string,
                    "pathTemplateRewrite": string,
                    "regexRewrite": {
                      "pathPattern": string,
                      "pathSubstitution": string
                    }
                  },
                  "timeout": {
                    "seconds": string,
                    "nanos": integer
                  },
                  "retryPolicy": {
                    "retryConditions": [
                      string
                    ],
                    "numRetries": integer,
                    "perTryTimeout": {
                      "seconds": string,
                      "nanos": integer
                    }
                  },
                  "requestMirrorPolicy": {
                    "backendService": string,
                    "mirrorPercent": number
                  },
                  "corsPolicy": {
                    "allowOrigins": [
                      string
                    ],
                    "allowOriginRegexes": [
                      string
                    ],
                    "allowMethods": [
                      string
                    ],
                    "allowHeaders": [
                      string
                    ],
                    "exposeHeaders": [
                      string
                    ],
                    "maxAge": integer,
                    "allowCredentials": boolean,
                    "disabled": boolean
                  },
                  "faultInjectionPolicy": {
                    "delay": {
                      "fixedDelay": {
                        "seconds": string,
                        "nanos": integer
                      },
                      "percentage": number
                    },
                    "abort": {
                      "httpStatus": integer,
                      "percentage": number
                    }
                  },
                  "maxStreamDuration": {
                    "seconds": string,
                    "nanos": integer
                  },
                  "cachePolicy": {
                    "cacheKeyPolicy": {
                      "includeProtocol": boolean,
                      "includeHost": boolean,
                      "includeQueryString": boolean,
                      "includedQueryParameters": [
                        string
                      ],
                      "excludedQueryParameters": [
                        string
                      ],
                      "includedHeaderNames": [
                        string
                      ],
                      "includedCookieNames": [
                        string
                      ]
                    },
                    "requestCoalescing": boolean,
                    "cacheMode": enum,
                    "defaultTtl": {
                      "seconds": string,
                      "nanos": integer
                    },
                    "maxTtl": {
                      "seconds": string,
                      "nanos": integer
                    },
                    "clientTtl": {
                      "seconds": string,
                      "nanos": integer
                    },
                    "negativeCaching": boolean,
                    "negativeCachingPolicy": [
                      {
                        "code": integer,
                        "ttl": {
                          "seconds": string,
                          "nanos": integer
                        }
                      }
                    ],
                    "cacheBypassRequestHeaderNames": [
                      string
                    ],
                    "serveWhileStale": {
                      "seconds": string,
                      "nanos": integer
                    }
                  }
                },
                "urlRedirect": {
                  "hostRedirect": string,
                  "pathRedirect": string,
                  "prefixRedirect": string,
                  "redirectResponseCode": enum,
                  "httpsRedirect": boolean,
                  "stripQuery": boolean
                },
                "paths": [
                  string
                ],
                "customErrorResponsePolicy": {
                  "errorResponseRules": [
                    {
                      "matchResponseCodes": [
                        string
                      ],
                      "path": string,
                      "overrideResponseCode": integer
                    }
                  ],
                  "errorService": string
                }
              }
            ],
            "routeRules": [
              {
                "priority": integer,
                "description": string,
                "matchRules": [
                  {
                    "prefixMatch": string,
                    "fullPathMatch": string,
                    "regexMatch": string,
                    "ignoreCase": boolean,
                    "headerMatches": [
                      {
                        "headerName": string,
                        "exactMatch": string,
                        "regexMatch": string,
                        "rangeMatch": {
                          "rangeStart": string,
                          "rangeEnd": string
                        },
                        "presentMatch": boolean,
                        "prefixMatch": string,
                        "suffixMatch": string,
                        "invertMatch": boolean
                      }
                    ],
                    "queryParameterMatches": [
                      {
                        "name": string,
                        "presentMatch": boolean,
                        "exactMatch": string,
                        "regexMatch": string
                      }
                    ],
                    "metadataFilters": [
                      {
                        "filterMatchCriteria": enum,
                        "filterLabels": [
                          {
                            "name": string,
                            "value": string
                          }
                        ]
                      }
                    ],
                    "pathTemplateMatch": string
                  }
                ],
                "service": string,
                "routeAction": {
                  "weightedBackendServices": [
                    {
                      "backendService": string,
                      "weight": integer,
                      "headerAction": {
                        "requestHeadersToRemove": [
                          string
                        ],
                        "requestHeadersToAdd": [
                          {
                            "headerName": string,
                            "headerValue": string,
                            "replace": boolean
                          }
                        ],
                        "responseHeadersToRemove": [
                          string
                        ],
                        "responseHeadersToAdd": [
                          {
                            "headerName": string,
                            "headerValue": string,
                            "replace": boolean
                          }
                        ]
                      }
                    }
                  ],
                  "urlRewrite": {
                    "pathPrefixRewrite": string,
                    "hostRewrite": string,
                    "pathTemplateRewrite": string,
                    "regexRewrite": {
                      "pathPattern": string,
                      "pathSubstitution": string
                    }
                  },
                  "timeout": {
                    "seconds": string,
                    "nanos": integer
                  },
                  "retryPolicy": {
                    "retryConditions": [
                      string
                    ],
                    "numRetries": integer,
                    "perTryTimeout": {
                      "seconds": string,
                      "nanos": integer
                    }
                  },
                  "requestMirrorPolicy": {
                    "backendService": string,
                    "mirrorPercent": number
                  },
                  "corsPolicy": {
                    "allowOrigins": [
                      string
                    ],
                    "allowOriginRegexes": [
                      string
                    ],
                    "allowMethods": [
                      string
                    ],
                    "allowHeaders": [
                      string
                    ],
                    "exposeHeaders": [
                      string
                    ],
                    "maxAge": integer,
                    "allowCredentials": boolean,
                    "disabled": boolean
                  },
                  "faultInjectionPolicy": {
                    "delay": {
                      "fixedDelay": {
                        "seconds": string,
                        "nanos": integer
                      },
                      "percentage": number
                    },
                    "abort": {
                      "httpStatus": integer,
                      "percentage": number
                    }
                  },
                  "maxStreamDuration": {
                    "seconds": string,
                    "nanos": integer
                  },
                  "cachePolicy": {
                    "cacheKeyPolicy": {
                      "includeProtocol": boolean,
                      "includeHost": boolean,
                      "includeQueryString": boolean,
                      "includedQueryParameters": [
                        string
                      ],
                      "excludedQueryParameters": [
                        string
                      ],
                      "includedHeaderNames": [
                        string
                      ],
                      "includedCookieNames": [
                        string
                      ]
                    },
                    "requestCoalescing": boolean,
                    "cacheMode": enum,
                    "defaultTtl": {
                      "seconds": string,
                      "nanos": integer
                    },
                    "maxTtl": {
                      "seconds": string,
                      "nanos": integer
                    },
                    "clientTtl": {
                      "seconds": string,
                      "nanos": integer
                    },
                    "negativeCaching": boolean,
                    "negativeCachingPolicy": [
                      {
                        "code": integer,
                        "ttl": {
                          "seconds": string,
                          "nanos": integer
                        }
                      }
                    ],
                    "cacheBypassRequestHeaderNames": [
                      string
                    ],
                    "serveWhileStale": {
                      "seconds": string,
                      "nanos": integer
                    }
                  }
                },
                "urlRedirect": {
                  "hostRedirect": string,
                  "pathRedirect": string,
                  "prefixRedirect": string,
                  "redirectResponseCode": enum,
                  "httpsRedirect": boolean,
                  "stripQuery": boolean
                },
                "headerAction": {
                  "requestHeadersToRemove": [
                    string
                  ],
                  "requestHeadersToAdd": [
                    {
                      "headerName": string,
                      "headerValue": string,
                      "replace": boolean
                    }
                  ],
                  "responseHeadersToRemove": [
                    string
                  ],
                  "responseHeadersToAdd": [
                    {
                      "headerName": string,
                      "headerValue": string,
                      "replace": boolean
                    }
                  ]
                },
                "customErrorResponsePolicy": {
                  "errorResponseRules": [
                    {
                      "matchResponseCodes": [
                        string
                      ],
                      "path": string,
                      "overrideResponseCode": integer
                    }
                  ],
                  "errorService": string
                }
              }
            ],
            "headerAction": {
              "requestHeadersToRemove": [
                string
              ],
              "requestHeadersToAdd": [
                {
                  "headerName": string,
                  "headerValue": string,
                  "replace": boolean
                }
              ],
              "responseHeadersToRemove": [
                string
              ],
              "responseHeadersToAdd": [
                {
                  "headerName": string,
                  "headerValue": string,
                  "replace": boolean
                }
              ]
            },
            "defaultCustomErrorResponsePolicy": {
              "errorResponseRules": [
                {
                  "matchResponseCodes": [
                    string
                  ],
                  "path": string,
                  "overrideResponseCode": integer
                }
              ],
              "errorService": string
            }
          }
        ],
        "tests": [
          {
            "description": string,
            "host": string,
            "path": string,
            "headers": [
              {
                "name": string,
                "value": string
              }
            ],
            "service": string,
            "expectedOutputUrl": string,
            "expectedRedirectResponseCode": integer
          }
        ],
        "defaultService": string,
        "defaultRouteAction": {
          "weightedBackendServices": [
            {
              "backendService": string,
              "weight": integer,
              "headerAction": {
                "requestHeadersToRemove": [
                  string
                ],
                "requestHeadersToAdd": [
                  {
                    "headerName": string,
                    "headerValue": string,
                    "replace": boolean
                  }
                ],
                "responseHeadersToRemove": [
                  string
                ],
                "responseHeadersToAdd": [
                  {
                    "headerName": string,
                    "headerValue": string,
                    "replace": boolean
                  }
                ]
              }
            }
          ],
          "urlRewrite": {
            "pathPrefixRewrite": string,
            "hostRewrite": string,
            "pathTemplateRewrite": string,
            "regexRewrite": {
              "pathPattern": string,
              "pathSubstitution": string
            }
          },
          "timeout": {
            "seconds": string,
            "nanos": integer
          },
          "retryPolicy": {
            "retryConditions": [
              string
            ],
            "numRetries": integer,
            "perTryTimeout": {
              "seconds": string,
              "nanos": integer
            }
          },
          "requestMirrorPolicy": {
            "backendService": string,
            "mirrorPercent": number
          },
          "corsPolicy": {
            "allowOrigins": [
              string
            ],
            "allowOriginRegexes": [
              string
            ],
            "allowMethods": [
              string
            ],
            "allowHeaders": [
              string
            ],
            "exposeHeaders": [
              string
            ],
            "maxAge": integer,
            "allowCredentials": boolean,
            "disabled": boolean
          },
          "faultInjectionPolicy": {
            "delay": {
              "fixedDelay": {
                "seconds": string,
                "nanos": integer
              },
              "percentage": number
            },
            "abort": {
              "httpStatus": integer,
              "percentage": number
            }
          },
          "maxStreamDuration": {
            "seconds": string,
            "nanos": integer
          },
          "cachePolicy": {
            "cacheKeyPolicy": {
              "includeProtocol": boolean,
              "includeHost": boolean,
              "includeQueryString": boolean,
              "includedQueryParameters": [
                string
              ],
              "excludedQueryParameters": [
                string
              ],
              "includedHeaderNames": [
                string
              ],
              "includedCookieNames": [
                string
              ]
            },
            "requestCoalescing": boolean,
            "cacheMode": enum,
            "defaultTtl": {
              "seconds": string,
              "nanos": integer
            },
            "maxTtl": {
              "seconds": string,
              "nanos": integer
            },
            "clientTtl": {
              "seconds": string,
              "nanos": integer
            },
            "negativeCaching": boolean,
            "negativeCachingPolicy": [
              {
                "code": integer,
                "ttl": {
                  "seconds": string,
                  "nanos": integer
                }
              }
            ],
            "cacheBypassRequestHeaderNames": [
              string
            ],
            "serveWhileStale": {
              "seconds": string,
              "nanos": integer
            }
          }
        },
        "defaultUrlRedirect": {
          "hostRedirect": string,
          "pathRedirect": string,
          "prefixRedirect": string,
          "redirectResponseCode": enum,
          "httpsRedirect": boolean,
          "stripQuery": boolean
        },
        "headerAction": {
          "requestHeadersToRemove": [
            string
          ],
          "requestHeadersToAdd": [
            {
              "headerName": string,
              "headerValue": string,
              "replace": boolean
            }
          ],
          "responseHeadersToRemove": [
            string
          ],
          "responseHeadersToAdd": [
            {
              "headerName": string,
              "headerValue": string,
              "replace": boolean
            }
          ]
        },
        "defaultCustomErrorResponsePolicy": {
          "errorResponseRules": [
            {
              "matchResponseCodes": [
                string
              ],
              "path": string,
              "overrideResponseCode": integer
            }
          ],
          "errorService": string
        },
        "fingerprint": string,
        "region": string
      }
    }  
  
Fields  
---  
`resource` |  `object` Content of the UrlMap to be validated.  
`resource.kind` |  `string` Output only. Type of the resource. Always `compute#urlMaps` for url maps.  
`resource.id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`resource.creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`resource.name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`resource.description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`resource.selfLink` |  `string` Output only. Server-defined URL for the resource.  
`resource.hostRules[]` |  `object` The list of host rules to use against the URL.  
`resource.hostRules[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`resource.hostRules[].hosts[]` |  `string` The list of host patterns to match. They must be valid hostnames with optional port numbers in the format `host`:`port`. `*` matches any string of `([a-z0-9-.]*)`. In that case, `*` must be the first character, and if followed by anything, the immediate following character must be either `-` or `.`. `*` based matching is not supported when the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`.  
`resource.hostRules[].pathMatcher` |  `string` The name of the `PathMatcher` to use to match the path portion of the URL if the `hostRule` matches the URL's host portion.  
`resource.pathMatchers[]` |  `object` The list of named `PathMatchers` to use against the URL.  
`resource.pathMatchers[].name` |  `string` The name to which this `PathMatcher` is referred by the `HostRule`.  
`resource.pathMatchers[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`resource.pathMatchers[].defaultService` |  `string` The full or partial URL to the `BackendService` resource. This URL is used if none of the `pathRules` or `routeRules` defined by this `PathMatcher` are matched. For example, the following are all valid URLs to a `BackendService` resource: 

  * `<https://www.googleapis.com/compute/v1/projects/>project/global/backendServices/backendService`
  * `compute/v1/projects/project/global/backendServices/backendService`
  * `global/backendServices/backendService`

If `defaultRouteAction` is also specified, advanced routing actions, such as URL rewrites, take effect before sending the request to the backend.Only one of `defaultUrlRedirect`, `defaultService` or `defaultRouteAction.weightedBackendService` can be set.Authorization requires one or more of the following [Google IAM](https://cloud.google.com/iam) permissions on the specified resource defaultService: 

  * `compute.backendBuckets.use`
  * `compute.backendServices.use`

Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `defaultService`:

  * `compute.regionBackendBuckets.use`
  * `compute.regionBackendServices.use`

  
`resource.pathMatchers[].defaultRouteAction` |  `object` `defaultRouteAction` takes effect when none of the ` pathRules` or `routeRules` match. The load balancer performs advanced routing actions, such as URL rewrites and header transformations, before forwarding the request to the selected backend.Only one of `defaultUrlRedirect`, `defaultService` or `defaultRouteAction.weightedBackendService` can be set.URL maps for classic Application Load Balancers only support the `urlRewrite` action within a path matcher's `defaultRouteAction`.  
`resource.pathMatchers[].defaultRouteAction.weightedBackendServices[]` |  `object` A list of weighted backend services to send traffic to when a route match occurs. The weights determine the fraction of traffic that flows to their corresponding `backend service`. If all traffic needs to go to a single backend service, there must be one `weightedBackendService` with weight set to a non-zero number. After a backend service is identified and before forwarding the request to the backend service, advanced routing actions such as URL rewrites and header transformations are applied depending on additional settings specified in this `HttpRouteAction`.  
`resource.pathMatchers[].defaultRouteAction.weightedBackendServices[].backendService` |  `string` The full or partial URL to the default `BackendService` resource. Before forwarding the request to `backendService`, the load balancer applies any relevant `headerActions` specified as part of this `backendServiceWeight`. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `backendService`:

  * `compute.regionBackendBuckets.use`
  * `compute.regionBackendServices.use`

  
`resource.pathMatchers[].defaultRouteAction.weightedBackendServices[].weight` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Specifies the fraction of traffic sent to a backend service, computed as `weight / (sum of all weightedBackendService weights in routeAction) `. The selection of a backend service is determined only for new traffic. Once a user's request has been directed to a backend service, subsequent requests are sent to the same backend service as determined by the backend service's session affinity policy. Don't configure session affinity if you're using weighted traffic splitting. If you do, the weighted traffic splitting configuration takes precedence. The value must be from 0 to 1000.  
`resource.pathMatchers[].defaultRouteAction.weightedBackendServices[].headerAction` |  `object` Specifies changes to request and response headers that need to take effect for the selected `backendService`. `headerAction` specified here take effect before `headerAction` in the enclosing `HttpRouteRule`, `PathMatcher` and `UrlMap`. `headerAction` is not supported for load balancers that have their `loadBalancingScheme` set to `EXTERNAL`. Not supported when the URL map is bound to a target gRPC proxy that has `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].defaultRouteAction.weightedBackendServices[].headerAction.requestHeadersToRemove[]` |  `string` A list of header names for headers that need to be removed from the request before forwarding the request to the `backendService`.  
`resource.pathMatchers[].defaultRouteAction.weightedBackendServices[].headerAction.requestHeadersToAdd[]` |  `object` Headers to add to a matching request before forwarding the request to the `backendService`.  
`resource.pathMatchers[].defaultRouteAction.weightedBackendServices[].headerAction.requestHeadersToAdd[].headerName` |  `string` The name of the header.  
`resource.pathMatchers[].defaultRouteAction.weightedBackendServices[].headerAction.requestHeadersToAdd[].headerValue` |  `string` The value of the header to add.  
`resource.pathMatchers[].defaultRouteAction.weightedBackendServices[].headerAction.requestHeadersToAdd[].replace` |  `boolean` If `false`, `headerValue` is appended to any values that already exist for the header. If true, `headerValue` is set for the header, discarding any values that were set for that header. The default value is `true`, unless a variable is present in `headerValue`, in which case the default value is `false`..   
`resource.pathMatchers[].defaultRouteAction.weightedBackendServices[].headerAction.responseHeadersToRemove[]` |  `string` A list of header names for headers that need to be removed from the response before sending the response back to the client.  
`resource.pathMatchers[].defaultRouteAction.weightedBackendServices[].headerAction.responseHeadersToAdd[]` |  `object` Headers to add the response before sending the response back to the client.  
`resource.pathMatchers[].defaultRouteAction.weightedBackendServices[].headerAction.responseHeadersToAdd[].headerName` |  `string` The name of the header.  
`resource.pathMatchers[].defaultRouteAction.weightedBackendServices[].headerAction.responseHeadersToAdd[].headerValue` |  `string` The value of the header to add.  
`resource.pathMatchers[].defaultRouteAction.weightedBackendServices[].headerAction.responseHeadersToAdd[].replace` |  `boolean` If `false`, `headerValue` is appended to any values that already exist for the header. If true, `headerValue` is set for the header, discarding any values that were set for that header. The default value is `true`, unless a variable is present in `headerValue`, in which case the default value is `false`..   
`resource.pathMatchers[].defaultRouteAction.urlRewrite` |  `object` The spec to modify the URL of the request, before forwarding the request to the matched service.  `urlRewrite` is the only action supported in UrlMaps for classic Application Load Balancers. Not supported when the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].defaultRouteAction.urlRewrite.pathPrefixRewrite` |  `string` Before forwarding the request to the selected backend service, the matching portion of the request's path is replaced by `pathPrefixRewrite`. The value must be from 1 to 1024 characters.  
`resource.pathMatchers[].defaultRouteAction.urlRewrite.hostRewrite` |  `string` Before forwarding the request to the selected service, the request's host header is replaced with contents of `hostRewrite`. The value must be from 1 to 255 characters.  
`resource.pathMatchers[].defaultRouteAction.urlRewrite.pathTemplateRewrite` |  `string` If specified, the pattern rewrites the URL path (based on the :path header) using the HTTP template syntax. A corresponding pathTemplateMatch must be specified. Any template variables must exist in the pathTemplateMatch field. 

  * -At least one variable must be specified in the pathTemplateMatch field
  * You can omit variables from the rewritten URL
  * The `*` and `**` operators cannot be matched unless they have a corresponding variable name - e.g. `{format=*}` or `{var=**}`.

For example, a pathTemplateMatch of `/static/{format=**}` could be rewritten as `/static/content/{format}` to prefix `/content` to the URL. Variables can also be re-ordered in a rewrite, so that `/{country}/{format}/{suffix=**}` can be rewritten as `/content/{format}/{country}/{suffix}`. At least one non-empty `routeRules[].matchRules[].path_template_match` is required. Only one of `pathPrefixRewrite` or `pathTemplateRewrite` may be specified.  
`resource.pathMatchers[].defaultRouteAction.urlRewrite.regexRewrite` |  `object` The regex rewrite to be applied to the URL. Only one of `pathPrefixRewrite`, `pathTemplateRewrite`, or `regexRewrite` may be specified.  
`resource.pathMatchers[].defaultRouteAction.urlRewrite.regexRewrite.pathPattern` |  `string` Required. The regular expression used to match against the URL path. It uses RE2 syntax with the following constraints: 

  * Any single character operators
  * Groups are allowed to have only submatch operator inside
  * Groups are allowed only without any char repetition, e.g. `.*`
  * Any char repetition, e.g. `.*`, is only allowed to be used in a single regex together with: 
    * Empty string operators
    * Other repetitions
    * Ranges
    * Repetitions of ranges
  * Ranges are only allowed to have: 
    * Character range
    * Digits range
    * Symbols listed in characters allowed for ranges

  
`resource.pathMatchers[].defaultRouteAction.urlRewrite.regexRewrite.pathSubstitution` |  `string` Required. Required when path pattern is specified. Used to rewrite matching parts of the path.  
`resource.pathMatchers[].defaultRouteAction.timeout` |  `object` Specifies the timeout for the selected route. Timeout is computed from the time the request has been fully processed (known as _end-of-stream_) up until the response has been processed. Timeout includes all retries. If not specified, this field uses the largest timeout among all backend services associated with the route. Not supported when the URL map is bound to a target gRPC proxy that has `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].defaultRouteAction.timeout.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].defaultRouteAction.timeout.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].defaultRouteAction.retryPolicy` |  `object` Specifies the retry policy associated with this route.  
`resource.pathMatchers[].defaultRouteAction.retryPolicy.retryConditions[]` |  `string` Specifies one or more conditions when this retry policy applies. Valid values are: 

  * `5xx`: retry is attempted if the instance or endpoint responds with any `5xx` response code, or if the instance or endpoint does not respond at all. For example, disconnects, reset, read timeout, connection failure, and refused streams.
  * `gateway-error`: Similar to `5xx`, but only applies to response codes `502`, `503` or `504`.
  * `connect-failure`: a retry is attempted on failures connecting to the instance or endpoint. For example, connection timeouts.
  * `retriable-4xx`: a retry is attempted if the instance or endpoint responds with a `4xx` response code. The only error that you can retry is error code `409`.
  * `refused-stream`: a retry is attempted if the instance or endpoint resets the stream with a `REFUSED_STREAM` error code. This reset type indicates that it is safe to retry.
  * `cancelled`: a retry is attempted if the gRPC status code in the response header is set to `cancelled`.
  * `deadline-exceeded`: a retry is attempted if the gRPC status code in the response header is set to `deadline-exceeded`.
  * `internal`: a retry is attempted if the gRPC status code in the response header is set to `internal`.
  * `resource-exhausted`: a retry is attempted if the gRPC status code in the response header is set to `resource-exhausted`.
  * `unavailable`: a retry is attempted if the gRPC status code in the response header is set to `unavailable`.

Only the following codes are supported when the URL map is bound to target gRPC proxy that has validateForProxyless field set to true. 

  * `cancelled`
  * `deadline-exceeded`
  * `internal`
  * `resource-exhausted`
  * `unavailable`

  
`resource.pathMatchers[].defaultRouteAction.retryPolicy.numRetries` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Specifies the allowed number retries. This number must be > 0\. If not specified, defaults to 1.  
`resource.pathMatchers[].defaultRouteAction.retryPolicy.perTryTimeout` |  `object` Specifies a non-zero timeout per retry attempt. If not specified, will use the timeout set in the `HttpRouteAction` field. If timeout in the `HttpRouteAction` field is not set, this field uses the largest timeout among all backend services associated with the route. Not supported when the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].defaultRouteAction.retryPolicy.perTryTimeout.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].defaultRouteAction.retryPolicy.perTryTimeout.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].defaultRouteAction.requestMirrorPolicy` |  `object` Specifies the policy on how requests intended for the route's backends are shadowed to a separate mirrored backend service. The load balancer does not wait for responses from the shadow service. Before sending traffic to the shadow service, the host / authority header is suffixed with `-shadow`. Not supported when the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].defaultRouteAction.requestMirrorPolicy.backendService` |  `string` The full or partial URL to the `BackendService` resource being mirrored to. The backend service configured for a mirroring policy must reference backends that are of the same type as the original backend service matched in the URL map. Serverless NEG backends are not currently supported as a mirrored backend service. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `backendService`:

  * `compute.regionBackendBuckets.use`
  * `compute.regionBackendServices.use`

  
`resource.pathMatchers[].defaultRouteAction.requestMirrorPolicy.mirrorPercent` |  `number` The percentage of requests to be mirrored to `backendService`.  
`resource.pathMatchers[].defaultRouteAction.corsPolicy` |  `object` The specification for allowing client-side cross-origin requests. For more information about the W3C recommendation for cross-origin resource sharing (CORS), see [Fetch API Living Standard](https://www.w3.org/TR/cors/). Not supported when the URL map is bound to a target gRPC proxy.  
`resource.pathMatchers[].defaultRouteAction.corsPolicy.allowOrigins[]` |  `string` Specifies the list of origins that is allowed to do CORS requests. An origin is allowed if it matches either an item in `allowOrigins` or an item in `allowOriginRegexes`.  
`resource.pathMatchers[].defaultRouteAction.corsPolicy.allowOriginRegexes[]` |  `string` Specifies a regular expression that matches allowed origins. For more information, see [regular expression syntax ](https://github.com/google/re2/wiki/Syntax). An origin is allowed if it matches either an item in `allowOrigins` or an item in `allowOriginRegexes`. Regular expressions can only be used when the loadBalancingScheme is set to `INTERNAL_SELF_MANAGED`.  
`resource.pathMatchers[].defaultRouteAction.corsPolicy.allowMethods[]` |  `string` Specifies the content for the `Access-Control-Allow-Methods` header.  
`resource.pathMatchers[].defaultRouteAction.corsPolicy.allowHeaders[]` |  `string` Specifies the content for the `Access-Control-Allow-Headers` header.  
`resource.pathMatchers[].defaultRouteAction.corsPolicy.exposeHeaders[]` |  `string` Specifies the content for the `Access-Control-Expose-Headers` header.  
`resource.pathMatchers[].defaultRouteAction.corsPolicy.maxAge` |  `integer` Specifies how long results of a preflight request can be cached in seconds. This field translates to the `Access-Control-Max-Age` header.  
`resource.pathMatchers[].defaultRouteAction.corsPolicy.allowCredentials` |  `boolean` In response to a preflight request, setting this to `true` indicates that the actual request can include user credentials. This field translates to the `Access-Control-Allow-Credentials` header. Default is `false`.  
`resource.pathMatchers[].defaultRouteAction.corsPolicy.disabled` |  `boolean` If `true`, disables the CORS policy. The default value is `false`, which indicates that the CORS policy is in effect.  
`resource.pathMatchers[].defaultRouteAction.faultInjectionPolicy` |  `object` The specification for fault injection introduced into traffic to test the resiliency of clients to backend service failure. As part of fault injection, when clients send requests to a backend service, delays can be introduced by a load balancer on a percentage of requests before sending those requests to the backend service. Similarly requests from clients can be aborted by the load balancer for a percentage of requests. `timeout` and `retryPolicy` is ignored by clients that are configured with a `faultInjectionPolicy` if: 1. The traffic is generated by fault injection AND 2. The fault injection is not a delay fault injection. Fault injection is not supported with the classic Application Load Balancer . To see which load balancers support fault injection, see [Load balancing: Routing and traffic management features](https://cloud.google.com/load-balancing/docs/features#routing-traffic-management).  
`resource.pathMatchers[].defaultRouteAction.faultInjectionPolicy.delay` |  `object` The specification for how client requests are delayed as part of fault injection, before being sent to a backend service.  
`resource.pathMatchers[].defaultRouteAction.faultInjectionPolicy.delay.fixedDelay` |  `object` Specifies the value of the fixed delay interval.  
`resource.pathMatchers[].defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].defaultRouteAction.faultInjectionPolicy.delay.percentage` |  `number` The percentage of traffic for connections, operations, or requests for which a delay is introduced as part of fault injection. The value must be from 0.0 to 100.0 inclusive.  
`resource.pathMatchers[].defaultRouteAction.faultInjectionPolicy.abort` |  `object` The specification for how client requests are aborted as part of fault injection.  
`resource.pathMatchers[].defaultRouteAction.faultInjectionPolicy.abort.httpStatus` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The HTTP status code used to abort the request. The value must be from 200 to 599 inclusive. For gRPC protocol, the gRPC status code is mapped to HTTP status code according to this [ mapping table](https://github.com/grpc/grpc/blob/master/doc/http-grpc-status-mapping.md). HTTP status 200 is mapped to gRPC status UNKNOWN. Injecting an OK status is currently not supported by Traffic Director.  
`resource.pathMatchers[].defaultRouteAction.faultInjectionPolicy.abort.percentage` |  `number` The percentage of traffic for connections, operations, or requests that is aborted as part of fault injection. The value must be from 0.0 to 100.0 inclusive.  
`resource.pathMatchers[].defaultRouteAction.maxStreamDuration` |  `object` Specifies the maximum duration (timeout) for streams on the selected route. Unlike the `timeout` field where the timeout duration starts from the time the request has been fully processed (known as _end-of-stream_), the duration in this field is computed from the beginning of the stream until the response has been processed, including all retries. A stream that does not complete in this duration is closed. If not specified, this field uses the maximum `maxStreamDuration` value among all backend services associated with the route. This field is only allowed if the Url map is used with backend services with `loadBalancingScheme` set to `INTERNAL_SELF_MANAGED`.  
`resource.pathMatchers[].defaultRouteAction.maxStreamDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].defaultRouteAction.maxStreamDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy` |  `object` Specifies the cache policy configuration for matched traffic. Available only for Global `EXTERNAL_MANAGED` load balancer schemes. At least one property must be specified. This policy cannot be specified if any target backend has Identity-Aware Proxy enabled.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.cacheKeyPolicy` |  `object` The cache key configuration. If not specified, the default behavior depends on the backend type: for Backend Services, the complete request URI is used; for Backend Buckets, the request URI is used without the protocol or host, and only query parameters known to Cloud Storage are included.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.cacheKeyPolicy.includeProtocol` |  `boolean` If true, http and https requests will be cached separately.Note: This setting is only applicable to routes that use a Backend Service. It does not affect requests served by a Backend Bucket, as the protocol is never included in a Backend Bucket's cache key. Attempting to set on a route that points exclusively to Backend Buckets will result in a configuration error.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.cacheKeyPolicy.includeHost` |  `boolean` If true, requests to different hosts will be cached separately.Note: This setting is only applicable to routes that use a Backend Service. It does not affect requests served by a Backend Bucket, as the host is never included in a Backend Bucket's cache key. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.cacheKeyPolicy.includeQueryString` |  `boolean` If true, include query string parameters in the cache key according to `includedQueryParameters` and `excludedQueryParameters`. If neither is set, the entire query string will be included. If false, the query string will be excluded from the cache key entirely.Note: This field applies to routes that use backend services. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error. For routes that point to a Backend Bucket, use `includedQueryParameters` to define which parameters should be part of the cache key.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.cacheKeyPolicy.includedQueryParameters[]` |  `string` Names of query string parameters to include in cache keys. All other parameters will be excluded. Either specify `includedQueryParameters` or `excludedQueryParameters`, not both. '&' and '=' will be percent encoded and not treated as delimiters.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.cacheKeyPolicy.excludedQueryParameters[]` |  `string` Names of query string parameters to exclude in cache keys. All other parameters will be included. Either specify `excludedQueryParameters` or `includedQueryParameters`, not both. '&' and '=' will be percent encoded and not treated as delimiters.Note: This field applies to routes that use backend services. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error. For routes that point to a Backend Bucket, use `includedQueryParameters` to define which parameters should be part of the cache key.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.cacheKeyPolicy.includedHeaderNames[]` |  `string` Allows HTTP request headers (by name) to be used in the cache key.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.cacheKeyPolicy.includedCookieNames[]` |  `string` Allows HTTP cookies (by name) to be used in the cache key. The name=value pair will be used in the cache key Cloud CDN generates.Note: This setting is only applicable to routes that use a Backend Service. It does not affect requests served by a Backend Bucket. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error. Up to 5 cookie names can be specified.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.requestCoalescing` |  `boolean` If true then Cloud CDN will combine multiple concurrent cache fill requests into a small number of requests to the origin. If not specified, Cloud CDN applies request coalescing by default.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.cacheMode` |  `enum` Specifies the cache setting for all responses from this route. If not specified, Cloud CDN uses `CACHE_ALL_STATIC` mode.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.defaultTtl` |  `object` Specifies the default TTL for cached content for responses that do not have an existing valid TTL (max-age or s-maxage). Setting a TTL of "0" means "always revalidate". The value of `defaultTtl` cannot be set to a value greater than that of `maxTtl`. When the `cacheMode` is set to `FORCE_CACHE_ALL`, the `defaultTtl` will overwrite the TTL set in all responses. The maximum allowed value is 31,622,400s (1 year). Infrequently accessed objects may be evicted from the cache before the defined TTL. If not specified, Cloud CDN uses 3600s (1 hour) for `CACHE_ALL_STATIC` and `FORCE_CACHE_ALL` modes. Cannot be specified when `cacheMode` is `USE_ORIGIN_HEADERS`.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.defaultTtl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.defaultTtl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.maxTtl` |  `object` Specifies the maximum allowed TTL for cached content. Cache directives that attempt to set a max-age or s-maxage higher than this, or an Expires header more than `maxTtl` seconds in the future will be capped at the value of `maxTtl`, as if it were the value of an s-maxage Cache-Control directive. Headers sent to the client will not be modified. Setting a TTL of "0" means "always revalidate". The maximum allowed value is 31,622,400s (1 year). Infrequently accessed objects may be evicted from the cache before the defined TTL. If not specified, Cloud CDN uses 86400s (1 day) for `CACHE_ALL_STATIC` mode. Can be specified only for `CACHE_ALL_STATIC` cache mode.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.maxTtl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.maxTtl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.clientTtl` |  `object` Specifies a separate client (e.g. browser client) maximum TTL for cached content. This is used to clamp the max-age (or Expires) value sent to the client. With `FORCE_CACHE_ALL`, the lesser of `clientTtl` and `defaultTtl` is used for the response max-age directive, along with a "public" directive. For cacheable content in `CACHE_ALL_STATIC` mode, `clientTtl` clamps the max-age from the origin (if specified), or else sets the response max-age directive to the lesser of the `clientTtl` and `defaultTtl`, and also ensures a "public" cache-control directive is present. The maximum allowed value is 31,622,400s (1 year). If not specified, Cloud CDN uses 3600s (1 hour) for `CACHE_ALL_STATIC` mode. Cannot exceed `maxTtl`. Cannot be specified when `cacheMode` is `USE_ORIGIN_HEADERS`.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.clientTtl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.clientTtl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.negativeCaching` |  `boolean` Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects. This can reduce the load on your origin and improve end-user experience by reducing response latency. When the `cacheMode` is set to `CACHE_ALL_STATIC` or `USE_ORIGIN_HEADERS`, negative caching applies to responses with the specified response code that lack any Cache-Control, Expires, or Pragma: no-cache directives. When the `cacheMode` is set to `FORCE_CACHE_ALL`, negative caching applies to all responses with the specified response code, and overrides any caching headers. By default, Cloud CDN applies the following TTLs to these HTTP status codes:

  * 300 (Multiple Choice), 301, 308 (Permanent Redirects): 10m
  * 404 (Not Found), 410 (Gone), 451 (Unavailable For Legal Reasons): 120s
  * 405 (Method Not Found), 501 (Not Implemented): 60s

These defaults can be overridden in `negativeCachingPolicy`. If not specified, Cloud CDN applies negative caching by default.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.negativeCachingPolicy[]` |  `object` Sets a cache TTL for the specified HTTP status code. `negativeCaching` must be enabled to configure `negativeCachingPolicy`. Omitting the policy and leaving `negativeCaching` enabled will use Cloud CDN's default cache TTLs. Note that when specifying an explicit `negativeCachingPolicy`, you should take care to specify a cache TTL for all response codes that you wish to cache. Cloud CDN will not apply any default negative caching when a policy exists.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.negativeCachingPolicy[].code` |  `integer` The HTTP status code to define a TTL against. Only HTTP status codes 300, 301, 302, 307, 308, 404, 405, 410, 421, 451 and 501 can be specified as values, and you cannot specify a status code more than once.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.negativeCachingPolicy[].ttl` |  `object` The TTL (in seconds) for which to cache responses with the corresponding status code. The maximum allowed value is 1800s (30 minutes). Infrequently accessed objects may be evicted from the cache before the defined TTL.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.negativeCachingPolicy[].ttl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.negativeCachingPolicy[].ttl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.cacheBypassRequestHeaderNames[]` |  `string` Bypass the cache when the specified request headers are matched by name, e.g. Pragma or Authorization headers. Values are case-insensitive. Up to 5 header names can be specified. The cache is bypassed for all `cacheMode` values.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.serveWhileStale` |  `object` Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache. This setting defines the default "max-stale" duration for any cached responses that do not specify a max-stale directive. Stale responses that exceed the TTL configured here will not be served. The default limit (max-stale) is 86400s (1 day), which will allow stale content to be served up to this limit beyond the max-age (or s-maxage) of a cached response. The maximum allowed value is 604800 (1 week). Set this to zero (0) to disable serve-while-stale.  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.serveWhileStale.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].defaultRouteAction.cachePolicy.serveWhileStale.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].defaultUrlRedirect` |  `object` When none of the specified `pathRules` or `routeRules` match, the request is redirected to a URL specified by `defaultUrlRedirect`.Only one of `defaultUrlRedirect`, `defaultService` or `defaultRouteAction.weightedBackendService` can be set.Not supported when the URL map is bound to a target gRPC proxy.  
`resource.pathMatchers[].defaultUrlRedirect.hostRedirect` |  `string` The host that is used in the redirect response instead of the one that was supplied in the request. The value must be from 1 to 255 characters.  
`resource.pathMatchers[].defaultUrlRedirect.pathRedirect` |  `string` The path that is used in the redirect response instead of the one that was supplied in the request. `pathRedirect` cannot be supplied together with `prefixRedirect`. Supply one alone or neither. If neither is supplied, the path of the original request is used for the redirect. The value must be from 1 to 1024 characters.  
`resource.pathMatchers[].defaultUrlRedirect.prefixRedirect` |  `string` The prefix that replaces the `prefixMatch` specified in the `HttpRouteRuleMatch`, retaining the remaining portion of the URL before redirecting the request. `prefixRedirect` cannot be supplied together with `pathRedirect`. Supply one alone or neither. If neither is supplied, the path of the original request is used for the redirect. The value must be from 1 to 1024 characters.  
`resource.pathMatchers[].defaultUrlRedirect.redirectResponseCode` |  `enum` The HTTP Status code to use for this RedirectAction. Supported values are: 

  * MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301.
  * FOUND, which corresponds to 302.
  * SEE_OTHER which corresponds to 303.
  * TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method is retained.
  * PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method is retained.

  
`resource.pathMatchers[].defaultUrlRedirect.httpsRedirect` |  `boolean` If set to `true`, the URL scheme in the redirected request is set to `HTTPS`. If set to `false`, the URL scheme of the redirected request remains the same as that of the request. This must only be set for URL maps used in `TargetHttpProxy`s. Setting this true for `TargetHttpsProxy` is not permitted. The default is set to `false`.  
`resource.pathMatchers[].defaultUrlRedirect.stripQuery` |  `boolean` If set to `true`, any accompanying query portion of the original URL is removed before redirecting the request. If set to `false`, the query portion of the original URL is retained. The default is set to `false`.   
`resource.pathMatchers[].pathRules[]` |  `object` The list of path rules. Use this list instead of `routeRules` when routing based on simple path matching is all that's required. A path rule can only include a wildcard character (`*`) after a forward slash character ("/"). The order by which path rules are specified does not matter. Matches are always done on the longest-path-first basis. For example: a `pathRule` with a path /a/b/c/* will match before /a/b/* irrespective of the order in which those paths appear in this list. Within a given `pathMatcher`, only one of `pathRules` or `routeRules` must be set.  
`resource.pathMatchers[].pathRules[].service` |  `string` The full or partial URL of the backend service resource to which traffic is directed if this rule is matched. If `routeAction` is also specified, advanced routing actions, such as URL rewrites, take effect before sending the request to the backend.Only one of `urlRedirect`, `service` or `routeAction.weightedBackendService` can be set. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `service`:

  * `compute.regionBackendBuckets.use`
  * `compute.regionBackendServices.use`

  
`resource.pathMatchers[].pathRules[].routeAction` |  `object` In response to a matching `path`, the load balancer performs advanced routing actions, such as URL rewrites and header transformations, before forwarding the request to the selected backend.Only one of `urlRedirect`, `service` or `routeAction.weightedBackendService` can be set.URL maps for classic Application Load Balancers only support the `urlRewrite` action within a path rule's `routeAction`.  
`resource.pathMatchers[].pathRules[].routeAction.weightedBackendServices[]` |  `object` A list of weighted backend services to send traffic to when a route match occurs. The weights determine the fraction of traffic that flows to their corresponding `backend service`. If all traffic needs to go to a single backend service, there must be one `weightedBackendService` with weight set to a non-zero number. After a backend service is identified and before forwarding the request to the backend service, advanced routing actions such as URL rewrites and header transformations are applied depending on additional settings specified in this `HttpRouteAction`.  
`resource.pathMatchers[].pathRules[].routeAction.weightedBackendServices[].backendService` |  `string` The full or partial URL to the default `BackendService` resource. Before forwarding the request to `backendService`, the load balancer applies any relevant `headerActions` specified as part of this `backendServiceWeight`. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `backendService`:

  * `compute.regionBackendBuckets.use`
  * `compute.regionBackendServices.use`

  
`resource.pathMatchers[].pathRules[].routeAction.weightedBackendServices[].weight` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Specifies the fraction of traffic sent to a backend service, computed as `weight / (sum of all weightedBackendService weights in routeAction) `. The selection of a backend service is determined only for new traffic. Once a user's request has been directed to a backend service, subsequent requests are sent to the same backend service as determined by the backend service's session affinity policy. Don't configure session affinity if you're using weighted traffic splitting. If you do, the weighted traffic splitting configuration takes precedence. The value must be from 0 to 1000.  
`resource.pathMatchers[].pathRules[].routeAction.weightedBackendServices[].headerAction` |  `object` Specifies changes to request and response headers that need to take effect for the selected `backendService`. `headerAction` specified here take effect before `headerAction` in the enclosing `HttpRouteRule`, `PathMatcher` and `UrlMap`. `headerAction` is not supported for load balancers that have their `loadBalancingScheme` set to `EXTERNAL`. Not supported when the URL map is bound to a target gRPC proxy that has `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].pathRules[].routeAction.weightedBackendServices[].headerAction.requestHeadersToRemove[]` |  `string` A list of header names for headers that need to be removed from the request before forwarding the request to the `backendService`.  
`resource.pathMatchers[].pathRules[].routeAction.weightedBackendServices[].headerAction.requestHeadersToAdd[]` |  `object` Headers to add to a matching request before forwarding the request to the `backendService`.  
`resource.pathMatchers[].pathRules[].routeAction.weightedBackendServices[].headerAction.requestHeadersToAdd[].headerName` |  `string` The name of the header.  
`resource.pathMatchers[].pathRules[].routeAction.weightedBackendServices[].headerAction.requestHeadersToAdd[].headerValue` |  `string` The value of the header to add.  
`resource.pathMatchers[].pathRules[].routeAction.weightedBackendServices[].headerAction.requestHeadersToAdd[].replace` |  `boolean` If `false`, `headerValue` is appended to any values that already exist for the header. If true, `headerValue` is set for the header, discarding any values that were set for that header. The default value is `true`, unless a variable is present in `headerValue`, in which case the default value is `false`..   
`resource.pathMatchers[].pathRules[].routeAction.weightedBackendServices[].headerAction.responseHeadersToRemove[]` |  `string` A list of header names for headers that need to be removed from the response before sending the response back to the client.  
`resource.pathMatchers[].pathRules[].routeAction.weightedBackendServices[].headerAction.responseHeadersToAdd[]` |  `object` Headers to add the response before sending the response back to the client.  
`resource.pathMatchers[].pathRules[].routeAction.weightedBackendServices[].headerAction.responseHeadersToAdd[].headerName` |  `string` The name of the header.  
`resource.pathMatchers[].pathRules[].routeAction.weightedBackendServices[].headerAction.responseHeadersToAdd[].headerValue` |  `string` The value of the header to add.  
`resource.pathMatchers[].pathRules[].routeAction.weightedBackendServices[].headerAction.responseHeadersToAdd[].replace` |  `boolean` If `false`, `headerValue` is appended to any values that already exist for the header. If true, `headerValue` is set for the header, discarding any values that were set for that header. The default value is `true`, unless a variable is present in `headerValue`, in which case the default value is `false`..   
`resource.pathMatchers[].pathRules[].routeAction.urlRewrite` |  `object` The spec to modify the URL of the request, before forwarding the request to the matched service.  `urlRewrite` is the only action supported in UrlMaps for classic Application Load Balancers. Not supported when the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].pathRules[].routeAction.urlRewrite.pathPrefixRewrite` |  `string` Before forwarding the request to the selected backend service, the matching portion of the request's path is replaced by `pathPrefixRewrite`. The value must be from 1 to 1024 characters.  
`resource.pathMatchers[].pathRules[].routeAction.urlRewrite.hostRewrite` |  `string` Before forwarding the request to the selected service, the request's host header is replaced with contents of `hostRewrite`. The value must be from 1 to 255 characters.  
`resource.pathMatchers[].pathRules[].routeAction.urlRewrite.pathTemplateRewrite` |  `string` If specified, the pattern rewrites the URL path (based on the :path header) using the HTTP template syntax. A corresponding pathTemplateMatch must be specified. Any template variables must exist in the pathTemplateMatch field. 

  * -At least one variable must be specified in the pathTemplateMatch field
  * You can omit variables from the rewritten URL
  * The `*` and `**` operators cannot be matched unless they have a corresponding variable name - e.g. `{format=*}` or `{var=**}`.

For example, a pathTemplateMatch of `/static/{format=**}` could be rewritten as `/static/content/{format}` to prefix `/content` to the URL. Variables can also be re-ordered in a rewrite, so that `/{country}/{format}/{suffix=**}` can be rewritten as `/content/{format}/{country}/{suffix}`. At least one non-empty `routeRules[].matchRules[].path_template_match` is required. Only one of `pathPrefixRewrite` or `pathTemplateRewrite` may be specified.  
`resource.pathMatchers[].pathRules[].routeAction.urlRewrite.regexRewrite` |  `object` The regex rewrite to be applied to the URL. Only one of `pathPrefixRewrite`, `pathTemplateRewrite`, or `regexRewrite` may be specified.  
`resource.pathMatchers[].pathRules[].routeAction.urlRewrite.regexRewrite.pathPattern` |  `string` Required. The regular expression used to match against the URL path. It uses RE2 syntax with the following constraints: 

  * Any single character operators
  * Groups are allowed to have only submatch operator inside
  * Groups are allowed only without any char repetition, e.g. `.*`
  * Any char repetition, e.g. `.*`, is only allowed to be used in a single regex together with: 
    * Empty string operators
    * Other repetitions
    * Ranges
    * Repetitions of ranges
  * Ranges are only allowed to have: 
    * Character range
    * Digits range
    * Symbols listed in characters allowed for ranges

  
`resource.pathMatchers[].pathRules[].routeAction.urlRewrite.regexRewrite.pathSubstitution` |  `string` Required. Required when path pattern is specified. Used to rewrite matching parts of the path.  
`resource.pathMatchers[].pathRules[].routeAction.timeout` |  `object` Specifies the timeout for the selected route. Timeout is computed from the time the request has been fully processed (known as _end-of-stream_) up until the response has been processed. Timeout includes all retries. If not specified, this field uses the largest timeout among all backend services associated with the route. Not supported when the URL map is bound to a target gRPC proxy that has `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].pathRules[].routeAction.timeout.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].pathRules[].routeAction.timeout.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].pathRules[].routeAction.retryPolicy` |  `object` Specifies the retry policy associated with this route.  
`resource.pathMatchers[].pathRules[].routeAction.retryPolicy.retryConditions[]` |  `string` Specifies one or more conditions when this retry policy applies. Valid values are: 

  * `5xx`: retry is attempted if the instance or endpoint responds with any `5xx` response code, or if the instance or endpoint does not respond at all. For example, disconnects, reset, read timeout, connection failure, and refused streams.
  * `gateway-error`: Similar to `5xx`, but only applies to response codes `502`, `503` or `504`.
  * `connect-failure`: a retry is attempted on failures connecting to the instance or endpoint. For example, connection timeouts.
  * `retriable-4xx`: a retry is attempted if the instance or endpoint responds with a `4xx` response code. The only error that you can retry is error code `409`.
  * `refused-stream`: a retry is attempted if the instance or endpoint resets the stream with a `REFUSED_STREAM` error code. This reset type indicates that it is safe to retry.
  * `cancelled`: a retry is attempted if the gRPC status code in the response header is set to `cancelled`.
  * `deadline-exceeded`: a retry is attempted if the gRPC status code in the response header is set to `deadline-exceeded`.
  * `internal`: a retry is attempted if the gRPC status code in the response header is set to `internal`.
  * `resource-exhausted`: a retry is attempted if the gRPC status code in the response header is set to `resource-exhausted`.
  * `unavailable`: a retry is attempted if the gRPC status code in the response header is set to `unavailable`.

Only the following codes are supported when the URL map is bound to target gRPC proxy that has validateForProxyless field set to true. 

  * `cancelled`
  * `deadline-exceeded`
  * `internal`
  * `resource-exhausted`
  * `unavailable`

  
`resource.pathMatchers[].pathRules[].routeAction.retryPolicy.numRetries` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Specifies the allowed number retries. This number must be > 0\. If not specified, defaults to 1.  
`resource.pathMatchers[].pathRules[].routeAction.retryPolicy.perTryTimeout` |  `object` Specifies a non-zero timeout per retry attempt. If not specified, will use the timeout set in the `HttpRouteAction` field. If timeout in the `HttpRouteAction` field is not set, this field uses the largest timeout among all backend services associated with the route. Not supported when the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].pathRules[].routeAction.retryPolicy.perTryTimeout.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].pathRules[].routeAction.retryPolicy.perTryTimeout.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].pathRules[].routeAction.requestMirrorPolicy` |  `object` Specifies the policy on how requests intended for the route's backends are shadowed to a separate mirrored backend service. The load balancer does not wait for responses from the shadow service. Before sending traffic to the shadow service, the host / authority header is suffixed with `-shadow`. Not supported when the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].pathRules[].routeAction.requestMirrorPolicy.backendService` |  `string` The full or partial URL to the `BackendService` resource being mirrored to. The backend service configured for a mirroring policy must reference backends that are of the same type as the original backend service matched in the URL map. Serverless NEG backends are not currently supported as a mirrored backend service. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `backendService`:

  * `compute.regionBackendBuckets.use`
  * `compute.regionBackendServices.use`

  
`resource.pathMatchers[].pathRules[].routeAction.requestMirrorPolicy.mirrorPercent` |  `number` The percentage of requests to be mirrored to `backendService`.  
`resource.pathMatchers[].pathRules[].routeAction.corsPolicy` |  `object` The specification for allowing client-side cross-origin requests. For more information about the W3C recommendation for cross-origin resource sharing (CORS), see [Fetch API Living Standard](https://www.w3.org/TR/cors/). Not supported when the URL map is bound to a target gRPC proxy.  
`resource.pathMatchers[].pathRules[].routeAction.corsPolicy.allowOrigins[]` |  `string` Specifies the list of origins that is allowed to do CORS requests. An origin is allowed if it matches either an item in `allowOrigins` or an item in `allowOriginRegexes`.  
`resource.pathMatchers[].pathRules[].routeAction.corsPolicy.allowOriginRegexes[]` |  `string` Specifies a regular expression that matches allowed origins. For more information, see [regular expression syntax ](https://github.com/google/re2/wiki/Syntax). An origin is allowed if it matches either an item in `allowOrigins` or an item in `allowOriginRegexes`. Regular expressions can only be used when the loadBalancingScheme is set to `INTERNAL_SELF_MANAGED`.  
`resource.pathMatchers[].pathRules[].routeAction.corsPolicy.allowMethods[]` |  `string` Specifies the content for the `Access-Control-Allow-Methods` header.  
`resource.pathMatchers[].pathRules[].routeAction.corsPolicy.allowHeaders[]` |  `string` Specifies the content for the `Access-Control-Allow-Headers` header.  
`resource.pathMatchers[].pathRules[].routeAction.corsPolicy.exposeHeaders[]` |  `string` Specifies the content for the `Access-Control-Expose-Headers` header.  
`resource.pathMatchers[].pathRules[].routeAction.corsPolicy.maxAge` |  `integer` Specifies how long results of a preflight request can be cached in seconds. This field translates to the `Access-Control-Max-Age` header.  
`resource.pathMatchers[].pathRules[].routeAction.corsPolicy.allowCredentials` |  `boolean` In response to a preflight request, setting this to `true` indicates that the actual request can include user credentials. This field translates to the `Access-Control-Allow-Credentials` header. Default is `false`.  
`resource.pathMatchers[].pathRules[].routeAction.corsPolicy.disabled` |  `boolean` If `true`, disables the CORS policy. The default value is `false`, which indicates that the CORS policy is in effect.  
`resource.pathMatchers[].pathRules[].routeAction.faultInjectionPolicy` |  `object` The specification for fault injection introduced into traffic to test the resiliency of clients to backend service failure. As part of fault injection, when clients send requests to a backend service, delays can be introduced by a load balancer on a percentage of requests before sending those requests to the backend service. Similarly requests from clients can be aborted by the load balancer for a percentage of requests. `timeout` and `retryPolicy` is ignored by clients that are configured with a `faultInjectionPolicy` if: 1. The traffic is generated by fault injection AND 2. The fault injection is not a delay fault injection. Fault injection is not supported with the classic Application Load Balancer . To see which load balancers support fault injection, see [Load balancing: Routing and traffic management features](https://cloud.google.com/load-balancing/docs/features#routing-traffic-management).  
`resource.pathMatchers[].pathRules[].routeAction.faultInjectionPolicy.delay` |  `object` The specification for how client requests are delayed as part of fault injection, before being sent to a backend service.  
`resource.pathMatchers[].pathRules[].routeAction.faultInjectionPolicy.delay.fixedDelay` |  `object` Specifies the value of the fixed delay interval.  
`resource.pathMatchers[].pathRules[].routeAction.faultInjectionPolicy.delay.fixedDelay.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].pathRules[].routeAction.faultInjectionPolicy.delay.fixedDelay.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].pathRules[].routeAction.faultInjectionPolicy.delay.percentage` |  `number` The percentage of traffic for connections, operations, or requests for which a delay is introduced as part of fault injection. The value must be from 0.0 to 100.0 inclusive.  
`resource.pathMatchers[].pathRules[].routeAction.faultInjectionPolicy.abort` |  `object` The specification for how client requests are aborted as part of fault injection.  
`resource.pathMatchers[].pathRules[].routeAction.faultInjectionPolicy.abort.httpStatus` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The HTTP status code used to abort the request. The value must be from 200 to 599 inclusive. For gRPC protocol, the gRPC status code is mapped to HTTP status code according to this [ mapping table](https://github.com/grpc/grpc/blob/master/doc/http-grpc-status-mapping.md). HTTP status 200 is mapped to gRPC status UNKNOWN. Injecting an OK status is currently not supported by Traffic Director.  
`resource.pathMatchers[].pathRules[].routeAction.faultInjectionPolicy.abort.percentage` |  `number` The percentage of traffic for connections, operations, or requests that is aborted as part of fault injection. The value must be from 0.0 to 100.0 inclusive.  
`resource.pathMatchers[].pathRules[].routeAction.maxStreamDuration` |  `object` Specifies the maximum duration (timeout) for streams on the selected route. Unlike the `timeout` field where the timeout duration starts from the time the request has been fully processed (known as _end-of-stream_), the duration in this field is computed from the beginning of the stream until the response has been processed, including all retries. A stream that does not complete in this duration is closed. If not specified, this field uses the maximum `maxStreamDuration` value among all backend services associated with the route. This field is only allowed if the Url map is used with backend services with `loadBalancingScheme` set to `INTERNAL_SELF_MANAGED`.  
`resource.pathMatchers[].pathRules[].routeAction.maxStreamDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].pathRules[].routeAction.maxStreamDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy` |  `object` Specifies the cache policy configuration for matched traffic. Available only for Global `EXTERNAL_MANAGED` load balancer schemes. At least one property must be specified. This policy cannot be specified if any target backend has Identity-Aware Proxy enabled.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.cacheKeyPolicy` |  `object` The cache key configuration. If not specified, the default behavior depends on the backend type: for Backend Services, the complete request URI is used; for Backend Buckets, the request URI is used without the protocol or host, and only query parameters known to Cloud Storage are included.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.cacheKeyPolicy.includeProtocol` |  `boolean` If true, http and https requests will be cached separately.Note: This setting is only applicable to routes that use a Backend Service. It does not affect requests served by a Backend Bucket, as the protocol is never included in a Backend Bucket's cache key. Attempting to set on a route that points exclusively to Backend Buckets will result in a configuration error.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.cacheKeyPolicy.includeHost` |  `boolean` If true, requests to different hosts will be cached separately.Note: This setting is only applicable to routes that use a Backend Service. It does not affect requests served by a Backend Bucket, as the host is never included in a Backend Bucket's cache key. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.cacheKeyPolicy.includeQueryString` |  `boolean` If true, include query string parameters in the cache key according to `includedQueryParameters` and `excludedQueryParameters`. If neither is set, the entire query string will be included. If false, the query string will be excluded from the cache key entirely.Note: This field applies to routes that use backend services. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error. For routes that point to a Backend Bucket, use `includedQueryParameters` to define which parameters should be part of the cache key.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.cacheKeyPolicy.includedQueryParameters[]` |  `string` Names of query string parameters to include in cache keys. All other parameters will be excluded. Either specify `includedQueryParameters` or `excludedQueryParameters`, not both. '&' and '=' will be percent encoded and not treated as delimiters.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.cacheKeyPolicy.excludedQueryParameters[]` |  `string` Names of query string parameters to exclude in cache keys. All other parameters will be included. Either specify `excludedQueryParameters` or `includedQueryParameters`, not both. '&' and '=' will be percent encoded and not treated as delimiters.Note: This field applies to routes that use backend services. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error. For routes that point to a Backend Bucket, use `includedQueryParameters` to define which parameters should be part of the cache key.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.cacheKeyPolicy.includedHeaderNames[]` |  `string` Allows HTTP request headers (by name) to be used in the cache key.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.cacheKeyPolicy.includedCookieNames[]` |  `string` Allows HTTP cookies (by name) to be used in the cache key. The name=value pair will be used in the cache key Cloud CDN generates.Note: This setting is only applicable to routes that use a Backend Service. It does not affect requests served by a Backend Bucket. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error. Up to 5 cookie names can be specified.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.requestCoalescing` |  `boolean` If true then Cloud CDN will combine multiple concurrent cache fill requests into a small number of requests to the origin. If not specified, Cloud CDN applies request coalescing by default.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.cacheMode` |  `enum` Specifies the cache setting for all responses from this route. If not specified, Cloud CDN uses `CACHE_ALL_STATIC` mode.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.defaultTtl` |  `object` Specifies the default TTL for cached content for responses that do not have an existing valid TTL (max-age or s-maxage). Setting a TTL of "0" means "always revalidate". The value of `defaultTtl` cannot be set to a value greater than that of `maxTtl`. When the `cacheMode` is set to `FORCE_CACHE_ALL`, the `defaultTtl` will overwrite the TTL set in all responses. The maximum allowed value is 31,622,400s (1 year). Infrequently accessed objects may be evicted from the cache before the defined TTL. If not specified, Cloud CDN uses 3600s (1 hour) for `CACHE_ALL_STATIC` and `FORCE_CACHE_ALL` modes. Cannot be specified when `cacheMode` is `USE_ORIGIN_HEADERS`.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.defaultTtl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.defaultTtl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.maxTtl` |  `object` Specifies the maximum allowed TTL for cached content. Cache directives that attempt to set a max-age or s-maxage higher than this, or an Expires header more than `maxTtl` seconds in the future will be capped at the value of `maxTtl`, as if it were the value of an s-maxage Cache-Control directive. Headers sent to the client will not be modified. Setting a TTL of "0" means "always revalidate". The maximum allowed value is 31,622,400s (1 year). Infrequently accessed objects may be evicted from the cache before the defined TTL. If not specified, Cloud CDN uses 86400s (1 day) for `CACHE_ALL_STATIC` mode. Can be specified only for `CACHE_ALL_STATIC` cache mode.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.maxTtl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.maxTtl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.clientTtl` |  `object` Specifies a separate client (e.g. browser client) maximum TTL for cached content. This is used to clamp the max-age (or Expires) value sent to the client. With `FORCE_CACHE_ALL`, the lesser of `clientTtl` and `defaultTtl` is used for the response max-age directive, along with a "public" directive. For cacheable content in `CACHE_ALL_STATIC` mode, `clientTtl` clamps the max-age from the origin (if specified), or else sets the response max-age directive to the lesser of the `clientTtl` and `defaultTtl`, and also ensures a "public" cache-control directive is present. The maximum allowed value is 31,622,400s (1 year). If not specified, Cloud CDN uses 3600s (1 hour) for `CACHE_ALL_STATIC` mode. Cannot exceed `maxTtl`. Cannot be specified when `cacheMode` is `USE_ORIGIN_HEADERS`.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.clientTtl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.clientTtl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.negativeCaching` |  `boolean` Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects. This can reduce the load on your origin and improve end-user experience by reducing response latency. When the `cacheMode` is set to `CACHE_ALL_STATIC` or `USE_ORIGIN_HEADERS`, negative caching applies to responses with the specified response code that lack any Cache-Control, Expires, or Pragma: no-cache directives. When the `cacheMode` is set to `FORCE_CACHE_ALL`, negative caching applies to all responses with the specified response code, and overrides any caching headers. By default, Cloud CDN applies the following TTLs to these HTTP status codes:

  * 300 (Multiple Choice), 301, 308 (Permanent Redirects): 10m
  * 404 (Not Found), 410 (Gone), 451 (Unavailable For Legal Reasons): 120s
  * 405 (Method Not Found), 501 (Not Implemented): 60s

These defaults can be overridden in `negativeCachingPolicy`. If not specified, Cloud CDN applies negative caching by default.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.negativeCachingPolicy[]` |  `object` Sets a cache TTL for the specified HTTP status code. `negativeCaching` must be enabled to configure `negativeCachingPolicy`. Omitting the policy and leaving `negativeCaching` enabled will use Cloud CDN's default cache TTLs. Note that when specifying an explicit `negativeCachingPolicy`, you should take care to specify a cache TTL for all response codes that you wish to cache. Cloud CDN will not apply any default negative caching when a policy exists.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.negativeCachingPolicy[].code` |  `integer` The HTTP status code to define a TTL against. Only HTTP status codes 300, 301, 302, 307, 308, 404, 405, 410, 421, 451 and 501 can be specified as values, and you cannot specify a status code more than once.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.negativeCachingPolicy[].ttl` |  `object` The TTL (in seconds) for which to cache responses with the corresponding status code. The maximum allowed value is 1800s (30 minutes). Infrequently accessed objects may be evicted from the cache before the defined TTL.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.negativeCachingPolicy[].ttl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.negativeCachingPolicy[].ttl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.cacheBypassRequestHeaderNames[]` |  `string` Bypass the cache when the specified request headers are matched by name, e.g. Pragma or Authorization headers. Values are case-insensitive. Up to 5 header names can be specified. The cache is bypassed for all `cacheMode` values.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.serveWhileStale` |  `object` Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache. This setting defines the default "max-stale" duration for any cached responses that do not specify a max-stale directive. Stale responses that exceed the TTL configured here will not be served. The default limit (max-stale) is 86400s (1 day), which will allow stale content to be served up to this limit beyond the max-age (or s-maxage) of a cached response. The maximum allowed value is 604800 (1 week). Set this to zero (0) to disable serve-while-stale.  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.serveWhileStale.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].pathRules[].routeAction.cachePolicy.serveWhileStale.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].pathRules[].urlRedirect` |  `object` When a path pattern is matched, the request is redirected to a URL specified by `urlRedirect`.Only one of `urlRedirect`, `service` or `routeAction.weightedBackendService` can be set.Not supported when the URL map is bound to a target gRPC proxy.  
`resource.pathMatchers[].pathRules[].urlRedirect.hostRedirect` |  `string` The host that is used in the redirect response instead of the one that was supplied in the request. The value must be from 1 to 255 characters.  
`resource.pathMatchers[].pathRules[].urlRedirect.pathRedirect` |  `string` The path that is used in the redirect response instead of the one that was supplied in the request. `pathRedirect` cannot be supplied together with `prefixRedirect`. Supply one alone or neither. If neither is supplied, the path of the original request is used for the redirect. The value must be from 1 to 1024 characters.  
`resource.pathMatchers[].pathRules[].urlRedirect.prefixRedirect` |  `string` The prefix that replaces the `prefixMatch` specified in the `HttpRouteRuleMatch`, retaining the remaining portion of the URL before redirecting the request. `prefixRedirect` cannot be supplied together with `pathRedirect`. Supply one alone or neither. If neither is supplied, the path of the original request is used for the redirect. The value must be from 1 to 1024 characters.  
`resource.pathMatchers[].pathRules[].urlRedirect.redirectResponseCode` |  `enum` The HTTP Status code to use for this RedirectAction. Supported values are: 

  * MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301.
  * FOUND, which corresponds to 302.
  * SEE_OTHER which corresponds to 303.
  * TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method is retained.
  * PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method is retained.

  
`resource.pathMatchers[].pathRules[].urlRedirect.httpsRedirect` |  `boolean` If set to `true`, the URL scheme in the redirected request is set to `HTTPS`. If set to `false`, the URL scheme of the redirected request remains the same as that of the request. This must only be set for URL maps used in `TargetHttpProxy`s. Setting this true for `TargetHttpsProxy` is not permitted. The default is set to `false`.  
`resource.pathMatchers[].pathRules[].urlRedirect.stripQuery` |  `boolean` If set to `true`, any accompanying query portion of the original URL is removed before redirecting the request. If set to `false`, the query portion of the original URL is retained. The default is set to `false`.   
`resource.pathMatchers[].pathRules[].paths[]` |  `string` The list of path patterns to match. Each must start with `/` and the only place a `*` is allowed is at the end following a `/`. The string fed to the path matcher does not include any text after the first `?` or `#`, and those chars are not allowed here.  
`resource.pathMatchers[].pathRules[].customErrorResponsePolicy` |  `object` `customErrorResponsePolicy` specifies how the Load Balancer returns error responses when `BackendService`or `BackendBucket` responds with an error. If a policy for an error code is not configured for the `PathRule`, a policy for the error code configured in `pathMatcher.defaultCustomErrorResponsePolicy` is applied. If one is not specified in `pathMatcher.defaultCustomErrorResponsePolicy`, the policy configured in `UrlMap.defaultCustomErrorResponsePolicy` takes effect. For example, consider a UrlMap with the following configuration: 

  * `UrlMap.defaultCustomErrorResponsePolicy` are configured with policies for `5xx` and `4xx` errors
  * A PathRule for `/coming_soon/` is configured for the error code `404`.

If the request is for `www.myotherdomain.com` and a `404` is encountered, the policy under `UrlMap.defaultCustomErrorResponsePolicy` takes effect. If a `404` response is encountered for the request `www.example.com/current_events/`, the pathMatcher's policy takes effect. If however, the request for `www.example.com/coming_soon/` encounters a `404`, the policy in `PathRule.customErrorResponsePolicy` takes effect. If any of the requests in this example encounter a `500` error code, the policy at `UrlMap.defaultCustomErrorResponsePolicy` takes effect. `customErrorResponsePolicy` is supported only for global external Application Load Balancers.  
`resource.pathMatchers[].pathRules[].customErrorResponsePolicy.errorResponseRules[]` |  `object` Specifies rules for returning error responses. In a given policy, if you specify rules for both a range of error codes as well as rules for specific error codes then rules with specific error codes have a higher priority. For example, assume that you configure a rule for `401` (Un-authorized) code, and another for all 4 series error codes `(4XX)`. If the backend service returns a `401`, then the rule for `401` will be applied. However if the backend service returns a `403`, the rule for `4xx` takes effect.  
`resource.pathMatchers[].pathRules[].customErrorResponsePolicy.errorResponseRules[].matchResponseCodes[]` |  `string` Valid values include: 

  * `A number between 400 and 599`: For example `401` or `503`, in which case the load balancer applies the policy if the error code exactly matches this value.
  * `5xx`: Load Balancer will apply the policy if the backend service responds with any response code in the range of `500` to `599`.
  * `4xx`: Load Balancer will apply the policy if the backend service responds with any response code in the range of `400` to `499`.

Values must be unique within matchResponseCodes and across all `errorResponseRules` of `CustomErrorResponsePolicy`.  
`resource.pathMatchers[].pathRules[].customErrorResponsePolicy.errorResponseRules[].path` |  `string` The full path to a file within `backendBucket` . For example: `/errors/defaultError.html` `path` must start with a leading slash. `path` cannot have trailing slashes. If the file is not available in `backendBucket` or the load balancer cannot reach the `BackendBucket`, a simple `Not Found Error` is returned to the client. The value must be from `1` to `1024` characters  
`resource.pathMatchers[].pathRules[].customErrorResponsePolicy.errorResponseRules[].overrideResponseCode` |  `integer` The HTTP status code returned with the response containing the custom error content. If `overrideResponseCode` is not supplied, the same response code returned by the original backend bucket or backend service is returned to the client.  
`resource.pathMatchers[].pathRules[].customErrorResponsePolicy.errorService` |  `string` The full or partial URL to the `BackendBucket` resource that contains the custom error content. Examples are: 

  * `<https://www.googleapis.com/compute/v1/projects/project/global/backendBuckets/myBackendBucket>`
  * `compute/v1/projects/project/global/backendBuckets/myBackendBucket`
  * `global/backendBuckets/myBackendBucket`

If `errorService` is not specified at lower levels like `pathMatcher`, `pathRule` and `routeRule`, an `errorService` specified at a higher level in the `UrlMap` will be used. If `UrlMap.defaultCustomErrorResponsePolicy` contains one or more `errorResponseRules[]`, it must specify `errorService`. If `load balancer` cannot reach the `backendBucket`, a simple `Not Found Error` will be returned, with the original response code (or `overrideResponseCode` if configured). `errorService` is not supported for internal or regional `HTTP/HTTPS` load balancers.  
`resource.pathMatchers[].routeRules[]` |  `object` The list of HTTP route rules. Use this list instead of `pathRules` when advanced route matching and routing actions are desired. `routeRules` are evaluated in order of priority, from the lowest to highest number. Within a given `pathMatcher`, you can set only one of `pathRules` or `routeRules`.  
`resource.pathMatchers[].routeRules[].priority` |  `integer` For `routeRules` within a given `pathMatcher`, priority determines the order in which a load balancer interprets `routeRules`. `RouteRules` are evaluated in order of priority, from the lowest to highest number. The priority of a rule decreases as its number increases (1, 2, 3, N+1). The first rule that matches the request is applied.  You cannot configure two or more routeRules with the same priority. Priority for each rule must be set to a number from 0 to 2147483647 inclusive.  Priority numbers can have gaps, which enable you to add or remove rules in the future without affecting the rest of the rules. For example, 1, 2, 3, 4, 5, 9, 12, 16 is a valid series of priority numbers to which you could add rules numbered from 6 to 8, 10 to 11, and 13 to 15 in the future without any impact on existing rules.  
`resource.pathMatchers[].routeRules[].description` |  `string` The short description conveying the intent of this `routeRule`.  The description can have a maximum length of 1024 characters.  
`resource.pathMatchers[].routeRules[].matchRules[]` |  `object` The list of criteria for matching attributes of a request to this `routeRule`. This list has OR semantics: the request matches this `routeRule` when any of the `matchRules` are satisfied. However predicates within a given `matchRule` have AND semantics. All predicates within a `matchRule` must match for the request to match the rule.  
`resource.pathMatchers[].routeRules[].matchRules[].prefixMatch` |  `string` For satisfying the `matchRule` condition, the request's path must begin with the specified `prefixMatch`. `prefixMatch` must begin with a `/`. The value must be from 1 to 1024 characters. The `*` character inside a prefix match is treated as a literal character, not as a wildcard. Only one of `prefixMatch`, `fullPathMatch`, `regexMatch` or `pathTemplateMatch` can be used within a `matchRule`.  
`resource.pathMatchers[].routeRules[].matchRules[].fullPathMatch` |  `string` For satisfying the `matchRule` condition, the path of the request must exactly match the value specified in `fullPathMatch` after removing any query parameters and anchor that may be part of the original URL. `fullPathMatch` must be from 1 to 1024 characters. Only one of `prefixMatch`, `fullPathMatch`, `regexMatch` or `pathTemplateMatch` must be specified.  
`resource.pathMatchers[].routeRules[].matchRules[].regexMatch` |  `string` For satisfying the `matchRule` condition, the path of the request must satisfy the regular expression specified in `regexMatch` after removing any query parameters and anchor supplied with the original URL. For more information about regular expression syntax, see [](https://github.com/google/re2/wiki/Syntax)Syntax. Only one of `prefixMatch`, `fullPathMatch`, `regexMatch` or `pathTemplateMatch` must be specified. Regular expressions can only be used when the loadBalancingScheme is set to `INTERNAL_SELF_MANAGED`, `EXTERNAL_MANAGED` (regional scope) or `INTERNAL_MANAGED`.  
`resource.pathMatchers[].routeRules[].matchRules[].ignoreCase` |  `boolean` Specifies that `prefixMatch` and `fullPathMatch` matches are case sensitive. The default value is false. ignoreCase must not be used with regexMatch. Not supported when the URL map is bound to a target gRPC proxy.  
`resource.pathMatchers[].routeRules[].matchRules[].headerMatches[]` |  `object` Specifies a list of header match criteria, all of which must match corresponding headers in the request.  
`resource.pathMatchers[].routeRules[].matchRules[].headerMatches[].headerName` |  `string` The name of the HTTP header to match. For matching against the HTTP request's authority, use a headerMatch with the header name ":authority". For matching a request's method, use the headerName ":method". When the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`, only non-binary user-specified custom metadata and the `content-type` header are supported. The following transport-level headers cannot be used in header matching rules: `:authority`, `:method`, `:path`, `:scheme`, `user-agent`, `accept-encoding`, `content-encoding`, `grpc-accept-encoding`, `grpc-encoding`, `grpc-previous-rpc-attempts`, `grpc-tags-bin`, `grpc-timeout` and `grpc-trace-bin`.  
`resource.pathMatchers[].routeRules[].matchRules[].headerMatches[].exactMatch` |  `string` The value should exactly match contents of `exactMatch`. Only one of `exactMatch`, `prefixMatch`, `suffixMatch`, `regexMatch`, `presentMatch` or `rangeMatch` must be set.  
`resource.pathMatchers[].routeRules[].matchRules[].headerMatches[].regexMatch` |  `string` The value of the header must match the regular expression specified in `regexMatch`. For more information about regular expression syntax, see [](https://github.com/google/re2/wiki/Syntax)Syntax. For matching against a port specified in the HTTP request, use a headerMatch with headerName set to PORT and a regular expression that satisfies the RFC2616 Host header's port specifier. Only one of `exactMatch`, `prefixMatch`, `suffixMatch`, `regexMatch`, `presentMatch` or `rangeMatch` must be set. Regular expressions can only be used when the loadBalancingScheme is set to `INTERNAL_SELF_MANAGED`, `EXTERNAL_MANAGED` (regional scope) or `INTERNAL_MANAGED`.  
`resource.pathMatchers[].routeRules[].matchRules[].headerMatches[].rangeMatch` |  `object` The header value must be an integer and its value must be in the range specified in `rangeMatch`. If the header does not contain an integer, number or is empty, the match fails. For example for a range [-5, 0] 

  * -3 will match.
  * 0 will not match.
  * 0.25 will not match.
  * -3someString will not match.

Only one of `exactMatch`, `prefixMatch`, `suffixMatch`, `regexMatch`, `presentMatch` or `rangeMatch` must be set. `rangeMatch` is not supported for load balancers that have `loadBalancingScheme` set to `EXTERNAL`.  
`resource.pathMatchers[].routeRules[].matchRules[].headerMatches[].rangeMatch.rangeStart` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The start of the range (inclusive) in signed long integer format.  
`resource.pathMatchers[].routeRules[].matchRules[].headerMatches[].rangeMatch.rangeEnd` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The end of the range (exclusive) in signed long integer format.  
`resource.pathMatchers[].routeRules[].matchRules[].headerMatches[].presentMatch` |  `boolean` A header with the contents of `headerName` must exist. The match takes place whether or not the request's header has a value. Only one of `exactMatch`, `prefixMatch`, `suffixMatch`, `regexMatch`, `presentMatch` or `rangeMatch` must be set.  
`resource.pathMatchers[].routeRules[].matchRules[].headerMatches[].prefixMatch` |  `string` The value of the header must start with the contents of `prefixMatch`. Only one of `exactMatch`, `prefixMatch`, `suffixMatch`, `regexMatch`, `presentMatch` or `rangeMatch` must be set.  
`resource.pathMatchers[].routeRules[].matchRules[].headerMatches[].suffixMatch` |  `string` The value of the header must end with the contents of `suffixMatch`. Only one of `exactMatch`, `prefixMatch`, `suffixMatch`, `regexMatch`, `presentMatch` or `rangeMatch` must be set.  
`resource.pathMatchers[].routeRules[].matchRules[].headerMatches[].invertMatch` |  `boolean` If set to `false`, the `headerMatch` is considered a match if the preceding match criteria are met. If set to `true`, the `headerMatch` is considered a match if the preceding match criteria are NOT met. The default setting is `false`.  
`resource.pathMatchers[].routeRules[].matchRules[].queryParameterMatches[]` |  `object` Specifies a list of query parameter match criteria, all of which must match corresponding query parameters in the request. Not supported when the URL map is bound to a target gRPC proxy.  
`resource.pathMatchers[].routeRules[].matchRules[].queryParameterMatches[].name` |  `string` The name of the query parameter to match. The query parameter must exist in the request, in the absence of which the request match fails.  
`resource.pathMatchers[].routeRules[].matchRules[].queryParameterMatches[].presentMatch` |  `boolean` Specifies that the `queryParameterMatch` matches if the request contains the query parameter, irrespective of whether the parameter has a value or not. Only one of `presentMatch`, `exactMatch`, or `regexMatch` must be set.  
`resource.pathMatchers[].routeRules[].matchRules[].queryParameterMatches[].exactMatch` |  `string` The `queryParameterMatch` matches if the value of the parameter exactly matches the contents of `exactMatch`. Only one of `presentMatch`, `exactMatch`, or `regexMatch` must be set.  
`resource.pathMatchers[].routeRules[].matchRules[].queryParameterMatches[].regexMatch` |  `string` The `queryParameterMatch` matches if the value of the parameter matches the regular expression specified by `regexMatch`. For more information about regular expression syntax, see [](https://github.com/google/re2/wiki/Syntax)Syntax. Only one of `presentMatch`, `exactMatch`, or `regexMatch` must be set. Regular expressions can only be used when the loadBalancingScheme is set to `INTERNAL_SELF_MANAGED`, `EXTERNAL_MANAGED` (regional scope) or `INTERNAL_MANAGED`.  
`resource.pathMatchers[].routeRules[].matchRules[].metadataFilters[]` |  `object` Opaque filter criteria used by the load balancer to restrict routing configuration to a limited set of [xDS](https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol) compliant clients. In their xDS requests to the load balancer, xDS clients present [node metadata](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/core/v3/base.proto.html#config-core-v3-node). When there is a match, the relevant routing configuration is made available to those proxies. For each `metadataFilter` in this list, if its `filterMatchCriteria` is set to MATCH_ANY, at least one of the `filterLabels` must match the corresponding label provided in the metadata. If its `filterMatchCriteria` is set to MATCH_ALL, then all of its `filterLabels` must match with corresponding labels provided in the metadata. If multiple metadata filters are specified, all of them need to be satisfied in order to be considered a match. `metadataFilters` specified here is applied after those specified in `ForwardingRule` that refers to the `UrlMap` this `HttpRouteRuleMatch` belongs to. `metadataFilters` only applies to load balancers that have `loadBalancingScheme` set to `INTERNAL_SELF_MANAGED`. Not supported when the URL map is bound to a target gRPC proxy that has `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].routeRules[].matchRules[].metadataFilters[].filterMatchCriteria` |  `enum` Specifies how individual filter label matches within the list of `filterLabels` and contributes toward the overall `metadataFilter` match.  Supported values are: 

  * `MATCH_ANY`: at least one of the `filterLabels` must have a matching label in the provided metadata.
  * `MATCH_ALL`: all `filterLabels` must have matching labels in the provided metadata.

  
`resource.pathMatchers[].routeRules[].matchRules[].metadataFilters[].filterLabels[]` |  `object` The list of label value pairs that must match labels in the provided metadata based on `filterMatchCriteria` This list must not be empty and can have at the most 64 entries.  
`resource.pathMatchers[].routeRules[].matchRules[].metadataFilters[].filterLabels[].name` |  `string` Name of metadata label.  The name can have a maximum length of 1024 characters and must be at least 1 character long.  
`resource.pathMatchers[].routeRules[].matchRules[].metadataFilters[].filterLabels[].value` |  `string` The value of the label must match the specified value. value can have a maximum length of 1024 characters.  
`resource.pathMatchers[].routeRules[].matchRules[].pathTemplateMatch` |  `string` If specified, this field defines a path template pattern that must match the :path header after the query string is removed. A path template pattern can include variables and wildcards. Variables are enclosed in curly braces, for example `{variable_name}`. Wildcards include `*` that matches a single path segment, and `**` that matches zero or more path segments. The pattern must follow these rules:

  * The value must be between 1 and 1024 characters.
  * The pattern must start with a leading slash ("/").
  * No more than 5 operators (variables or wildcards) may appear in the pattern.

Precisely one of `prefixMatch`, `fullPathMatch`, `regexMatch`, or `pathTemplateMatch` must be set.  
`resource.pathMatchers[].routeRules[].service` |  `string` The full or partial URL of the backend service resource to which traffic is directed if this rule is matched. If `routeAction` is also specified, advanced routing actions, such as URL rewrites, take effect before sending the request to the backend.Only one of `urlRedirect`, `service` or `routeAction.weightedBackendService` can be set. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `service`:

  * `compute.regionBackendBuckets.use`
  * `compute.regionBackendServices.use`

  
`resource.pathMatchers[].routeRules[].routeAction` |  `object` In response to a matching `matchRule`, the load balancer performs advanced routing actions, such as URL rewrites and header transformations, before forwarding the request to the selected backend.Only one of `urlRedirect`, `service` or `routeAction.weightedBackendService` can be set.URL maps for classic Application Load Balancers only support the `urlRewrite` action within a route rule's `routeAction`.  
`resource.pathMatchers[].routeRules[].routeAction.weightedBackendServices[]` |  `object` A list of weighted backend services to send traffic to when a route match occurs. The weights determine the fraction of traffic that flows to their corresponding `backend service`. If all traffic needs to go to a single backend service, there must be one `weightedBackendService` with weight set to a non-zero number. After a backend service is identified and before forwarding the request to the backend service, advanced routing actions such as URL rewrites and header transformations are applied depending on additional settings specified in this `HttpRouteAction`.  
`resource.pathMatchers[].routeRules[].routeAction.weightedBackendServices[].backendService` |  `string` The full or partial URL to the default `BackendService` resource. Before forwarding the request to `backendService`, the load balancer applies any relevant `headerActions` specified as part of this `backendServiceWeight`. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `backendService`:

  * `compute.regionBackendBuckets.use`
  * `compute.regionBackendServices.use`

  
`resource.pathMatchers[].routeRules[].routeAction.weightedBackendServices[].weight` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Specifies the fraction of traffic sent to a backend service, computed as `weight / (sum of all weightedBackendService weights in routeAction) `. The selection of a backend service is determined only for new traffic. Once a user's request has been directed to a backend service, subsequent requests are sent to the same backend service as determined by the backend service's session affinity policy. Don't configure session affinity if you're using weighted traffic splitting. If you do, the weighted traffic splitting configuration takes precedence. The value must be from 0 to 1000.  
`resource.pathMatchers[].routeRules[].routeAction.weightedBackendServices[].headerAction` |  `object` Specifies changes to request and response headers that need to take effect for the selected `backendService`. `headerAction` specified here take effect before `headerAction` in the enclosing `HttpRouteRule`, `PathMatcher` and `UrlMap`. `headerAction` is not supported for load balancers that have their `loadBalancingScheme` set to `EXTERNAL`. Not supported when the URL map is bound to a target gRPC proxy that has `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].routeRules[].routeAction.weightedBackendServices[].headerAction.requestHeadersToRemove[]` |  `string` A list of header names for headers that need to be removed from the request before forwarding the request to the `backendService`.  
`resource.pathMatchers[].routeRules[].routeAction.weightedBackendServices[].headerAction.requestHeadersToAdd[]` |  `object` Headers to add to a matching request before forwarding the request to the `backendService`.  
`resource.pathMatchers[].routeRules[].routeAction.weightedBackendServices[].headerAction.requestHeadersToAdd[].headerName` |  `string` The name of the header.  
`resource.pathMatchers[].routeRules[].routeAction.weightedBackendServices[].headerAction.requestHeadersToAdd[].headerValue` |  `string` The value of the header to add.  
`resource.pathMatchers[].routeRules[].routeAction.weightedBackendServices[].headerAction.requestHeadersToAdd[].replace` |  `boolean` If `false`, `headerValue` is appended to any values that already exist for the header. If true, `headerValue` is set for the header, discarding any values that were set for that header. The default value is `true`, unless a variable is present in `headerValue`, in which case the default value is `false`..   
`resource.pathMatchers[].routeRules[].routeAction.weightedBackendServices[].headerAction.responseHeadersToRemove[]` |  `string` A list of header names for headers that need to be removed from the response before sending the response back to the client.  
`resource.pathMatchers[].routeRules[].routeAction.weightedBackendServices[].headerAction.responseHeadersToAdd[]` |  `object` Headers to add the response before sending the response back to the client.  
`resource.pathMatchers[].routeRules[].routeAction.weightedBackendServices[].headerAction.responseHeadersToAdd[].headerName` |  `string` The name of the header.  
`resource.pathMatchers[].routeRules[].routeAction.weightedBackendServices[].headerAction.responseHeadersToAdd[].headerValue` |  `string` The value of the header to add.  
`resource.pathMatchers[].routeRules[].routeAction.weightedBackendServices[].headerAction.responseHeadersToAdd[].replace` |  `boolean` If `false`, `headerValue` is appended to any values that already exist for the header. If true, `headerValue` is set for the header, discarding any values that were set for that header. The default value is `true`, unless a variable is present in `headerValue`, in which case the default value is `false`..   
`resource.pathMatchers[].routeRules[].routeAction.urlRewrite` |  `object` The spec to modify the URL of the request, before forwarding the request to the matched service.  `urlRewrite` is the only action supported in UrlMaps for classic Application Load Balancers. Not supported when the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].routeRules[].routeAction.urlRewrite.pathPrefixRewrite` |  `string` Before forwarding the request to the selected backend service, the matching portion of the request's path is replaced by `pathPrefixRewrite`. The value must be from 1 to 1024 characters.  
`resource.pathMatchers[].routeRules[].routeAction.urlRewrite.hostRewrite` |  `string` Before forwarding the request to the selected service, the request's host header is replaced with contents of `hostRewrite`. The value must be from 1 to 255 characters.  
`resource.pathMatchers[].routeRules[].routeAction.urlRewrite.pathTemplateRewrite` |  `string` If specified, the pattern rewrites the URL path (based on the :path header) using the HTTP template syntax. A corresponding pathTemplateMatch must be specified. Any template variables must exist in the pathTemplateMatch field. 

  * -At least one variable must be specified in the pathTemplateMatch field
  * You can omit variables from the rewritten URL
  * The `*` and `**` operators cannot be matched unless they have a corresponding variable name - e.g. `{format=*}` or `{var=**}`.

For example, a pathTemplateMatch of `/static/{format=**}` could be rewritten as `/static/content/{format}` to prefix `/content` to the URL. Variables can also be re-ordered in a rewrite, so that `/{country}/{format}/{suffix=**}` can be rewritten as `/content/{format}/{country}/{suffix}`. At least one non-empty `routeRules[].matchRules[].path_template_match` is required. Only one of `pathPrefixRewrite` or `pathTemplateRewrite` may be specified.  
`resource.pathMatchers[].routeRules[].routeAction.urlRewrite.regexRewrite` |  `object` The regex rewrite to be applied to the URL. Only one of `pathPrefixRewrite`, `pathTemplateRewrite`, or `regexRewrite` may be specified.  
`resource.pathMatchers[].routeRules[].routeAction.urlRewrite.regexRewrite.pathPattern` |  `string` Required. The regular expression used to match against the URL path. It uses RE2 syntax with the following constraints: 

  * Any single character operators
  * Groups are allowed to have only submatch operator inside
  * Groups are allowed only without any char repetition, e.g. `.*`
  * Any char repetition, e.g. `.*`, is only allowed to be used in a single regex together with: 
    * Empty string operators
    * Other repetitions
    * Ranges
    * Repetitions of ranges
  * Ranges are only allowed to have: 
    * Character range
    * Digits range
    * Symbols listed in characters allowed for ranges

  
`resource.pathMatchers[].routeRules[].routeAction.urlRewrite.regexRewrite.pathSubstitution` |  `string` Required. Required when path pattern is specified. Used to rewrite matching parts of the path.  
`resource.pathMatchers[].routeRules[].routeAction.timeout` |  `object` Specifies the timeout for the selected route. Timeout is computed from the time the request has been fully processed (known as _end-of-stream_) up until the response has been processed. Timeout includes all retries. If not specified, this field uses the largest timeout among all backend services associated with the route. Not supported when the URL map is bound to a target gRPC proxy that has `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].routeRules[].routeAction.timeout.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].routeRules[].routeAction.timeout.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].routeRules[].routeAction.retryPolicy` |  `object` Specifies the retry policy associated with this route.  
`resource.pathMatchers[].routeRules[].routeAction.retryPolicy.retryConditions[]` |  `string` Specifies one or more conditions when this retry policy applies. Valid values are: 

  * `5xx`: retry is attempted if the instance or endpoint responds with any `5xx` response code, or if the instance or endpoint does not respond at all. For example, disconnects, reset, read timeout, connection failure, and refused streams.
  * `gateway-error`: Similar to `5xx`, but only applies to response codes `502`, `503` or `504`.
  * `connect-failure`: a retry is attempted on failures connecting to the instance or endpoint. For example, connection timeouts.
  * `retriable-4xx`: a retry is attempted if the instance or endpoint responds with a `4xx` response code. The only error that you can retry is error code `409`.
  * `refused-stream`: a retry is attempted if the instance or endpoint resets the stream with a `REFUSED_STREAM` error code. This reset type indicates that it is safe to retry.
  * `cancelled`: a retry is attempted if the gRPC status code in the response header is set to `cancelled`.
  * `deadline-exceeded`: a retry is attempted if the gRPC status code in the response header is set to `deadline-exceeded`.
  * `internal`: a retry is attempted if the gRPC status code in the response header is set to `internal`.
  * `resource-exhausted`: a retry is attempted if the gRPC status code in the response header is set to `resource-exhausted`.
  * `unavailable`: a retry is attempted if the gRPC status code in the response header is set to `unavailable`.

Only the following codes are supported when the URL map is bound to target gRPC proxy that has validateForProxyless field set to true. 

  * `cancelled`
  * `deadline-exceeded`
  * `internal`
  * `resource-exhausted`
  * `unavailable`

  
`resource.pathMatchers[].routeRules[].routeAction.retryPolicy.numRetries` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Specifies the allowed number retries. This number must be > 0\. If not specified, defaults to 1.  
`resource.pathMatchers[].routeRules[].routeAction.retryPolicy.perTryTimeout` |  `object` Specifies a non-zero timeout per retry attempt. If not specified, will use the timeout set in the `HttpRouteAction` field. If timeout in the `HttpRouteAction` field is not set, this field uses the largest timeout among all backend services associated with the route. Not supported when the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].routeRules[].routeAction.retryPolicy.perTryTimeout.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].routeRules[].routeAction.retryPolicy.perTryTimeout.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].routeRules[].routeAction.requestMirrorPolicy` |  `object` Specifies the policy on how requests intended for the route's backends are shadowed to a separate mirrored backend service. The load balancer does not wait for responses from the shadow service. Before sending traffic to the shadow service, the host / authority header is suffixed with `-shadow`. Not supported when the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].routeRules[].routeAction.requestMirrorPolicy.backendService` |  `string` The full or partial URL to the `BackendService` resource being mirrored to. The backend service configured for a mirroring policy must reference backends that are of the same type as the original backend service matched in the URL map. Serverless NEG backends are not currently supported as a mirrored backend service. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `backendService`:

  * `compute.regionBackendBuckets.use`
  * `compute.regionBackendServices.use`

  
`resource.pathMatchers[].routeRules[].routeAction.requestMirrorPolicy.mirrorPercent` |  `number` The percentage of requests to be mirrored to `backendService`.  
`resource.pathMatchers[].routeRules[].routeAction.corsPolicy` |  `object` The specification for allowing client-side cross-origin requests. For more information about the W3C recommendation for cross-origin resource sharing (CORS), see [Fetch API Living Standard](https://www.w3.org/TR/cors/). Not supported when the URL map is bound to a target gRPC proxy.  
`resource.pathMatchers[].routeRules[].routeAction.corsPolicy.allowOrigins[]` |  `string` Specifies the list of origins that is allowed to do CORS requests. An origin is allowed if it matches either an item in `allowOrigins` or an item in `allowOriginRegexes`.  
`resource.pathMatchers[].routeRules[].routeAction.corsPolicy.allowOriginRegexes[]` |  `string` Specifies a regular expression that matches allowed origins. For more information, see [regular expression syntax ](https://github.com/google/re2/wiki/Syntax). An origin is allowed if it matches either an item in `allowOrigins` or an item in `allowOriginRegexes`. Regular expressions can only be used when the loadBalancingScheme is set to `INTERNAL_SELF_MANAGED`.  
`resource.pathMatchers[].routeRules[].routeAction.corsPolicy.allowMethods[]` |  `string` Specifies the content for the `Access-Control-Allow-Methods` header.  
`resource.pathMatchers[].routeRules[].routeAction.corsPolicy.allowHeaders[]` |  `string` Specifies the content for the `Access-Control-Allow-Headers` header.  
`resource.pathMatchers[].routeRules[].routeAction.corsPolicy.exposeHeaders[]` |  `string` Specifies the content for the `Access-Control-Expose-Headers` header.  
`resource.pathMatchers[].routeRules[].routeAction.corsPolicy.maxAge` |  `integer` Specifies how long results of a preflight request can be cached in seconds. This field translates to the `Access-Control-Max-Age` header.  
`resource.pathMatchers[].routeRules[].routeAction.corsPolicy.allowCredentials` |  `boolean` In response to a preflight request, setting this to `true` indicates that the actual request can include user credentials. This field translates to the `Access-Control-Allow-Credentials` header. Default is `false`.  
`resource.pathMatchers[].routeRules[].routeAction.corsPolicy.disabled` |  `boolean` If `true`, disables the CORS policy. The default value is `false`, which indicates that the CORS policy is in effect.  
`resource.pathMatchers[].routeRules[].routeAction.faultInjectionPolicy` |  `object` The specification for fault injection introduced into traffic to test the resiliency of clients to backend service failure. As part of fault injection, when clients send requests to a backend service, delays can be introduced by a load balancer on a percentage of requests before sending those requests to the backend service. Similarly requests from clients can be aborted by the load balancer for a percentage of requests. `timeout` and `retryPolicy` is ignored by clients that are configured with a `faultInjectionPolicy` if: 1. The traffic is generated by fault injection AND 2. The fault injection is not a delay fault injection. Fault injection is not supported with the classic Application Load Balancer . To see which load balancers support fault injection, see [Load balancing: Routing and traffic management features](https://cloud.google.com/load-balancing/docs/features#routing-traffic-management).  
`resource.pathMatchers[].routeRules[].routeAction.faultInjectionPolicy.delay` |  `object` The specification for how client requests are delayed as part of fault injection, before being sent to a backend service.  
`resource.pathMatchers[].routeRules[].routeAction.faultInjectionPolicy.delay.fixedDelay` |  `object` Specifies the value of the fixed delay interval.  
`resource.pathMatchers[].routeRules[].routeAction.faultInjectionPolicy.delay.fixedDelay.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].routeRules[].routeAction.faultInjectionPolicy.delay.fixedDelay.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].routeRules[].routeAction.faultInjectionPolicy.delay.percentage` |  `number` The percentage of traffic for connections, operations, or requests for which a delay is introduced as part of fault injection. The value must be from 0.0 to 100.0 inclusive.  
`resource.pathMatchers[].routeRules[].routeAction.faultInjectionPolicy.abort` |  `object` The specification for how client requests are aborted as part of fault injection.  
`resource.pathMatchers[].routeRules[].routeAction.faultInjectionPolicy.abort.httpStatus` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The HTTP status code used to abort the request. The value must be from 200 to 599 inclusive. For gRPC protocol, the gRPC status code is mapped to HTTP status code according to this [ mapping table](https://github.com/grpc/grpc/blob/master/doc/http-grpc-status-mapping.md). HTTP status 200 is mapped to gRPC status UNKNOWN. Injecting an OK status is currently not supported by Traffic Director.  
`resource.pathMatchers[].routeRules[].routeAction.faultInjectionPolicy.abort.percentage` |  `number` The percentage of traffic for connections, operations, or requests that is aborted as part of fault injection. The value must be from 0.0 to 100.0 inclusive.  
`resource.pathMatchers[].routeRules[].routeAction.maxStreamDuration` |  `object` Specifies the maximum duration (timeout) for streams on the selected route. Unlike the `timeout` field where the timeout duration starts from the time the request has been fully processed (known as _end-of-stream_), the duration in this field is computed from the beginning of the stream until the response has been processed, including all retries. A stream that does not complete in this duration is closed. If not specified, this field uses the maximum `maxStreamDuration` value among all backend services associated with the route. This field is only allowed if the Url map is used with backend services with `loadBalancingScheme` set to `INTERNAL_SELF_MANAGED`.  
`resource.pathMatchers[].routeRules[].routeAction.maxStreamDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].routeRules[].routeAction.maxStreamDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy` |  `object` Specifies the cache policy configuration for matched traffic. Available only for Global `EXTERNAL_MANAGED` load balancer schemes. At least one property must be specified. This policy cannot be specified if any target backend has Identity-Aware Proxy enabled.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.cacheKeyPolicy` |  `object` The cache key configuration. If not specified, the default behavior depends on the backend type: for Backend Services, the complete request URI is used; for Backend Buckets, the request URI is used without the protocol or host, and only query parameters known to Cloud Storage are included.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.cacheKeyPolicy.includeProtocol` |  `boolean` If true, http and https requests will be cached separately.Note: This setting is only applicable to routes that use a Backend Service. It does not affect requests served by a Backend Bucket, as the protocol is never included in a Backend Bucket's cache key. Attempting to set on a route that points exclusively to Backend Buckets will result in a configuration error.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.cacheKeyPolicy.includeHost` |  `boolean` If true, requests to different hosts will be cached separately.Note: This setting is only applicable to routes that use a Backend Service. It does not affect requests served by a Backend Bucket, as the host is never included in a Backend Bucket's cache key. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.cacheKeyPolicy.includeQueryString` |  `boolean` If true, include query string parameters in the cache key according to `includedQueryParameters` and `excludedQueryParameters`. If neither is set, the entire query string will be included. If false, the query string will be excluded from the cache key entirely.Note: This field applies to routes that use backend services. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error. For routes that point to a Backend Bucket, use `includedQueryParameters` to define which parameters should be part of the cache key.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.cacheKeyPolicy.includedQueryParameters[]` |  `string` Names of query string parameters to include in cache keys. All other parameters will be excluded. Either specify `includedQueryParameters` or `excludedQueryParameters`, not both. '&' and '=' will be percent encoded and not treated as delimiters.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.cacheKeyPolicy.excludedQueryParameters[]` |  `string` Names of query string parameters to exclude in cache keys. All other parameters will be included. Either specify `excludedQueryParameters` or `includedQueryParameters`, not both. '&' and '=' will be percent encoded and not treated as delimiters.Note: This field applies to routes that use backend services. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error. For routes that point to a Backend Bucket, use `includedQueryParameters` to define which parameters should be part of the cache key.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.cacheKeyPolicy.includedHeaderNames[]` |  `string` Allows HTTP request headers (by name) to be used in the cache key.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.cacheKeyPolicy.includedCookieNames[]` |  `string` Allows HTTP cookies (by name) to be used in the cache key. The name=value pair will be used in the cache key Cloud CDN generates.Note: This setting is only applicable to routes that use a Backend Service. It does not affect requests served by a Backend Bucket. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error. Up to 5 cookie names can be specified.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.requestCoalescing` |  `boolean` If true then Cloud CDN will combine multiple concurrent cache fill requests into a small number of requests to the origin. If not specified, Cloud CDN applies request coalescing by default.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.cacheMode` |  `enum` Specifies the cache setting for all responses from this route. If not specified, Cloud CDN uses `CACHE_ALL_STATIC` mode.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.defaultTtl` |  `object` Specifies the default TTL for cached content for responses that do not have an existing valid TTL (max-age or s-maxage). Setting a TTL of "0" means "always revalidate". The value of `defaultTtl` cannot be set to a value greater than that of `maxTtl`. When the `cacheMode` is set to `FORCE_CACHE_ALL`, the `defaultTtl` will overwrite the TTL set in all responses. The maximum allowed value is 31,622,400s (1 year). Infrequently accessed objects may be evicted from the cache before the defined TTL. If not specified, Cloud CDN uses 3600s (1 hour) for `CACHE_ALL_STATIC` and `FORCE_CACHE_ALL` modes. Cannot be specified when `cacheMode` is `USE_ORIGIN_HEADERS`.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.defaultTtl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.defaultTtl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.maxTtl` |  `object` Specifies the maximum allowed TTL for cached content. Cache directives that attempt to set a max-age or s-maxage higher than this, or an Expires header more than `maxTtl` seconds in the future will be capped at the value of `maxTtl`, as if it were the value of an s-maxage Cache-Control directive. Headers sent to the client will not be modified. Setting a TTL of "0" means "always revalidate". The maximum allowed value is 31,622,400s (1 year). Infrequently accessed objects may be evicted from the cache before the defined TTL. If not specified, Cloud CDN uses 86400s (1 day) for `CACHE_ALL_STATIC` mode. Can be specified only for `CACHE_ALL_STATIC` cache mode.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.maxTtl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.maxTtl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.clientTtl` |  `object` Specifies a separate client (e.g. browser client) maximum TTL for cached content. This is used to clamp the max-age (or Expires) value sent to the client. With `FORCE_CACHE_ALL`, the lesser of `clientTtl` and `defaultTtl` is used for the response max-age directive, along with a "public" directive. For cacheable content in `CACHE_ALL_STATIC` mode, `clientTtl` clamps the max-age from the origin (if specified), or else sets the response max-age directive to the lesser of the `clientTtl` and `defaultTtl`, and also ensures a "public" cache-control directive is present. The maximum allowed value is 31,622,400s (1 year). If not specified, Cloud CDN uses 3600s (1 hour) for `CACHE_ALL_STATIC` mode. Cannot exceed `maxTtl`. Cannot be specified when `cacheMode` is `USE_ORIGIN_HEADERS`.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.clientTtl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.clientTtl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.negativeCaching` |  `boolean` Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects. This can reduce the load on your origin and improve end-user experience by reducing response latency. When the `cacheMode` is set to `CACHE_ALL_STATIC` or `USE_ORIGIN_HEADERS`, negative caching applies to responses with the specified response code that lack any Cache-Control, Expires, or Pragma: no-cache directives. When the `cacheMode` is set to `FORCE_CACHE_ALL`, negative caching applies to all responses with the specified response code, and overrides any caching headers. By default, Cloud CDN applies the following TTLs to these HTTP status codes:

  * 300 (Multiple Choice), 301, 308 (Permanent Redirects): 10m
  * 404 (Not Found), 410 (Gone), 451 (Unavailable For Legal Reasons): 120s
  * 405 (Method Not Found), 501 (Not Implemented): 60s

These defaults can be overridden in `negativeCachingPolicy`. If not specified, Cloud CDN applies negative caching by default.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.negativeCachingPolicy[]` |  `object` Sets a cache TTL for the specified HTTP status code. `negativeCaching` must be enabled to configure `negativeCachingPolicy`. Omitting the policy and leaving `negativeCaching` enabled will use Cloud CDN's default cache TTLs. Note that when specifying an explicit `negativeCachingPolicy`, you should take care to specify a cache TTL for all response codes that you wish to cache. Cloud CDN will not apply any default negative caching when a policy exists.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.negativeCachingPolicy[].code` |  `integer` The HTTP status code to define a TTL against. Only HTTP status codes 300, 301, 302, 307, 308, 404, 405, 410, 421, 451 and 501 can be specified as values, and you cannot specify a status code more than once.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.negativeCachingPolicy[].ttl` |  `object` The TTL (in seconds) for which to cache responses with the corresponding status code. The maximum allowed value is 1800s (30 minutes). Infrequently accessed objects may be evicted from the cache before the defined TTL.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.negativeCachingPolicy[].ttl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.negativeCachingPolicy[].ttl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.cacheBypassRequestHeaderNames[]` |  `string` Bypass the cache when the specified request headers are matched by name, e.g. Pragma or Authorization headers. Values are case-insensitive. Up to 5 header names can be specified. The cache is bypassed for all `cacheMode` values.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.serveWhileStale` |  `object` Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache. This setting defines the default "max-stale" duration for any cached responses that do not specify a max-stale directive. Stale responses that exceed the TTL configured here will not be served. The default limit (max-stale) is 86400s (1 day), which will allow stale content to be served up to this limit beyond the max-age (or s-maxage) of a cached response. The maximum allowed value is 604800 (1 week). Set this to zero (0) to disable serve-while-stale.  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.serveWhileStale.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.pathMatchers[].routeRules[].routeAction.cachePolicy.serveWhileStale.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.pathMatchers[].routeRules[].urlRedirect` |  `object` When this rule is matched, the request is redirected to a URL specified by `urlRedirect`.Only one of `urlRedirect`, `service` or `routeAction.weightedBackendService` can be set.Not supported when the URL map is bound to a target gRPC proxy.  
`resource.pathMatchers[].routeRules[].urlRedirect.hostRedirect` |  `string` The host that is used in the redirect response instead of the one that was supplied in the request. The value must be from 1 to 255 characters.  
`resource.pathMatchers[].routeRules[].urlRedirect.pathRedirect` |  `string` The path that is used in the redirect response instead of the one that was supplied in the request. `pathRedirect` cannot be supplied together with `prefixRedirect`. Supply one alone or neither. If neither is supplied, the path of the original request is used for the redirect. The value must be from 1 to 1024 characters.  
`resource.pathMatchers[].routeRules[].urlRedirect.prefixRedirect` |  `string` The prefix that replaces the `prefixMatch` specified in the `HttpRouteRuleMatch`, retaining the remaining portion of the URL before redirecting the request. `prefixRedirect` cannot be supplied together with `pathRedirect`. Supply one alone or neither. If neither is supplied, the path of the original request is used for the redirect. The value must be from 1 to 1024 characters.  
`resource.pathMatchers[].routeRules[].urlRedirect.redirectResponseCode` |  `enum` The HTTP Status code to use for this RedirectAction. Supported values are: 

  * MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301.
  * FOUND, which corresponds to 302.
  * SEE_OTHER which corresponds to 303.
  * TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method is retained.
  * PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method is retained.

  
`resource.pathMatchers[].routeRules[].urlRedirect.httpsRedirect` |  `boolean` If set to `true`, the URL scheme in the redirected request is set to `HTTPS`. If set to `false`, the URL scheme of the redirected request remains the same as that of the request. This must only be set for URL maps used in `TargetHttpProxy`s. Setting this true for `TargetHttpsProxy` is not permitted. The default is set to `false`.  
`resource.pathMatchers[].routeRules[].urlRedirect.stripQuery` |  `boolean` If set to `true`, any accompanying query portion of the original URL is removed before redirecting the request. If set to `false`, the query portion of the original URL is retained. The default is set to `false`.   
`resource.pathMatchers[].routeRules[].headerAction` |  `object` Specifies changes to request and response headers that need to take effect for the selected `backendService`. The `headerAction` value specified here is applied before the matching `pathMatchers[].headerAction` and after `pathMatchers[].routeRules[].routeAction.weightedBackendService.backendServiceWeightAction[].headerAction` `HeaderAction` is not supported for load balancers that have their `loadBalancingScheme` set to `EXTERNAL`. Not supported when the URL map is bound to a target gRPC proxy that has `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].routeRules[].headerAction.requestHeadersToRemove[]` |  `string` A list of header names for headers that need to be removed from the request before forwarding the request to the `backendService`.  
`resource.pathMatchers[].routeRules[].headerAction.requestHeadersToAdd[]` |  `object` Headers to add to a matching request before forwarding the request to the `backendService`.  
`resource.pathMatchers[].routeRules[].headerAction.requestHeadersToAdd[].headerName` |  `string` The name of the header.  
`resource.pathMatchers[].routeRules[].headerAction.requestHeadersToAdd[].headerValue` |  `string` The value of the header to add.  
`resource.pathMatchers[].routeRules[].headerAction.requestHeadersToAdd[].replace` |  `boolean` If `false`, `headerValue` is appended to any values that already exist for the header. If true, `headerValue` is set for the header, discarding any values that were set for that header. The default value is `true`, unless a variable is present in `headerValue`, in which case the default value is `false`..   
`resource.pathMatchers[].routeRules[].headerAction.responseHeadersToRemove[]` |  `string` A list of header names for headers that need to be removed from the response before sending the response back to the client.  
`resource.pathMatchers[].routeRules[].headerAction.responseHeadersToAdd[]` |  `object` Headers to add the response before sending the response back to the client.  
`resource.pathMatchers[].routeRules[].headerAction.responseHeadersToAdd[].headerName` |  `string` The name of the header.  
`resource.pathMatchers[].routeRules[].headerAction.responseHeadersToAdd[].headerValue` |  `string` The value of the header to add.  
`resource.pathMatchers[].routeRules[].headerAction.responseHeadersToAdd[].replace` |  `boolean` If `false`, `headerValue` is appended to any values that already exist for the header. If true, `headerValue` is set for the header, discarding any values that were set for that header. The default value is `true`, unless a variable is present in `headerValue`, in which case the default value is `false`..   
`resource.pathMatchers[].routeRules[].customErrorResponsePolicy` |  `object` `customErrorResponsePolicy` specifies how the Load Balancer returns error responses when `BackendService`or `BackendBucket` responds with an error. If a policy for an error code is not configured for the `RouteRule`, a policy for the error code configured in `pathMatcher.defaultCustomErrorResponsePolicy` is applied. If one is not specified in `pathMatcher.defaultCustomErrorResponsePolicy`, the policy configured in `UrlMap.defaultCustomErrorResponsePolicy` takes effect. For example, consider a UrlMap with the following configuration: 

  * `UrlMap.defaultCustomErrorResponsePolicy` are configured with policies for `5xx` and `4xx` errors
  * A RouteRule for `/coming_soon/` is configured for the error code `404`.

If the request is for `www.myotherdomain.com` and a `404` is encountered, the policy under `UrlMap.defaultCustomErrorResponsePolicy` takes effect. If a `404` response is encountered for the request `www.example.com/current_events/`, the pathMatcher's policy takes effect. If however, the request for `www.example.com/coming_soon/` encounters a `404`, the policy in `RouteRule.customErrorResponsePolicy` takes effect. If any of the requests in this example encounter a `500` error code, the policy at `UrlMap.defaultCustomErrorResponsePolicy` takes effect. When used in conjunction with `routeRules.routeAction.retryPolicy`, retries take precedence. Only once all retries are exhausted, the `customErrorResponsePolicy` is applied. While attempting a retry, if `load balancer` is successful in reaching the service, the `customErrorResponsePolicy` is ignored and the response from the service is returned to the client. `customErrorResponsePolicy` is supported only for global external Application Load Balancers.  
`resource.pathMatchers[].routeRules[].customErrorResponsePolicy.errorResponseRules[]` |  `object` Specifies rules for returning error responses. In a given policy, if you specify rules for both a range of error codes as well as rules for specific error codes then rules with specific error codes have a higher priority. For example, assume that you configure a rule for `401` (Un-authorized) code, and another for all 4 series error codes `(4XX)`. If the backend service returns a `401`, then the rule for `401` will be applied. However if the backend service returns a `403`, the rule for `4xx` takes effect.  
`resource.pathMatchers[].routeRules[].customErrorResponsePolicy.errorResponseRules[].matchResponseCodes[]` |  `string` Valid values include: 

  * `A number between 400 and 599`: For example `401` or `503`, in which case the load balancer applies the policy if the error code exactly matches this value.
  * `5xx`: Load Balancer will apply the policy if the backend service responds with any response code in the range of `500` to `599`.
  * `4xx`: Load Balancer will apply the policy if the backend service responds with any response code in the range of `400` to `499`.

Values must be unique within matchResponseCodes and across all `errorResponseRules` of `CustomErrorResponsePolicy`.  
`resource.pathMatchers[].routeRules[].customErrorResponsePolicy.errorResponseRules[].path` |  `string` The full path to a file within `backendBucket` . For example: `/errors/defaultError.html` `path` must start with a leading slash. `path` cannot have trailing slashes. If the file is not available in `backendBucket` or the load balancer cannot reach the `BackendBucket`, a simple `Not Found Error` is returned to the client. The value must be from `1` to `1024` characters  
`resource.pathMatchers[].routeRules[].customErrorResponsePolicy.errorResponseRules[].overrideResponseCode` |  `integer` The HTTP status code returned with the response containing the custom error content. If `overrideResponseCode` is not supplied, the same response code returned by the original backend bucket or backend service is returned to the client.  
`resource.pathMatchers[].routeRules[].customErrorResponsePolicy.errorService` |  `string` The full or partial URL to the `BackendBucket` resource that contains the custom error content. Examples are: 

  * `<https://www.googleapis.com/compute/v1/projects/project/global/backendBuckets/myBackendBucket>`
  * `compute/v1/projects/project/global/backendBuckets/myBackendBucket`
  * `global/backendBuckets/myBackendBucket`

If `errorService` is not specified at lower levels like `pathMatcher`, `pathRule` and `routeRule`, an `errorService` specified at a higher level in the `UrlMap` will be used. If `UrlMap.defaultCustomErrorResponsePolicy` contains one or more `errorResponseRules[]`, it must specify `errorService`. If `load balancer` cannot reach the `backendBucket`, a simple `Not Found Error` will be returned, with the original response code (or `overrideResponseCode` if configured). `errorService` is not supported for internal or regional `HTTP/HTTPS` load balancers.  
`resource.pathMatchers[].headerAction` |  `object` Specifies changes to request and response headers that need to take effect for the selected backend service. HeaderAction specified here are applied after the matching `HttpRouteRule` `HeaderAction` and before the `HeaderAction` in the `UrlMap` `HeaderAction` is not supported for load balancers that have their `loadBalancingScheme` set to `EXTERNAL`. Not supported when the URL map is bound to a target gRPC proxy that has `validateForProxyless` field set to `true`.  
`resource.pathMatchers[].headerAction.requestHeadersToRemove[]` |  `string` A list of header names for headers that need to be removed from the request before forwarding the request to the `backendService`.  
`resource.pathMatchers[].headerAction.requestHeadersToAdd[]` |  `object` Headers to add to a matching request before forwarding the request to the `backendService`.  
`resource.pathMatchers[].headerAction.requestHeadersToAdd[].headerName` |  `string` The name of the header.  
`resource.pathMatchers[].headerAction.requestHeadersToAdd[].headerValue` |  `string` The value of the header to add.  
`resource.pathMatchers[].headerAction.requestHeadersToAdd[].replace` |  `boolean` If `false`, `headerValue` is appended to any values that already exist for the header. If true, `headerValue` is set for the header, discarding any values that were set for that header. The default value is `true`, unless a variable is present in `headerValue`, in which case the default value is `false`..   
`resource.pathMatchers[].headerAction.responseHeadersToRemove[]` |  `string` A list of header names for headers that need to be removed from the response before sending the response back to the client.  
`resource.pathMatchers[].headerAction.responseHeadersToAdd[]` |  `object` Headers to add the response before sending the response back to the client.  
`resource.pathMatchers[].headerAction.responseHeadersToAdd[].headerName` |  `string` The name of the header.  
`resource.pathMatchers[].headerAction.responseHeadersToAdd[].headerValue` |  `string` The value of the header to add.  
`resource.pathMatchers[].headerAction.responseHeadersToAdd[].replace` |  `boolean` If `false`, `headerValue` is appended to any values that already exist for the header. If true, `headerValue` is set for the header, discarding any values that were set for that header. The default value is `true`, unless a variable is present in `headerValue`, in which case the default value is `false`..   
`resource.pathMatchers[].defaultCustomErrorResponsePolicy` |  `object` `defaultCustomErrorResponsePolicy` specifies how the Load Balancer returns error responses when `BackendService`or `BackendBucket` responds with an error. This policy takes effect at the `PathMatcher` level and applies only when no policy has been defined for the error code at lower levels like `RouteRule` and `PathRule` within this `PathMatcher`. If an error code does not have a policy defined in `defaultCustomErrorResponsePolicy`, then a policy defined for the error code in `UrlMap.defaultCustomErrorResponsePolicy` takes effect. For example, consider a UrlMap with the following configuration: 

  * `UrlMap.defaultCustomErrorResponsePolicy` is configured with policies for `5xx` and `4xx` errors
  * A RouteRule for `/coming_soon/` is configured for the error code `404`.

If the request is for `www.myotherdomain.com` and a `404` is encountered, the policy under `UrlMap.defaultCustomErrorResponsePolicy` takes effect. If a `404` response is encountered for the request `www.example.com/current_events/`, the pathMatcher's policy takes effect. If however, the request for `www.example.com/coming_soon/` encounters a `404`, the policy in `RouteRule.customErrorResponsePolicy` takes effect. If any of the requests in this example encounter a `500` error code, the policy at `UrlMap.defaultCustomErrorResponsePolicy` takes effect. When used in conjunction with `pathMatcher.defaultRouteAction.retryPolicy`, retries take precedence. Only once all retries are exhausted, the `defaultCustomErrorResponsePolicy` is applied. While attempting a retry, if `load balancer` is successful in reaching the service, the `defaultCustomErrorResponsePolicy` is ignored and the response from the service is returned to the client. `defaultCustomErrorResponsePolicy` is supported only for global external Application Load Balancers.  
`resource.pathMatchers[].defaultCustomErrorResponsePolicy.errorResponseRules[]` |  `object` Specifies rules for returning error responses. In a given policy, if you specify rules for both a range of error codes as well as rules for specific error codes then rules with specific error codes have a higher priority. For example, assume that you configure a rule for `401` (Un-authorized) code, and another for all 4 series error codes `(4XX)`. If the backend service returns a `401`, then the rule for `401` will be applied. However if the backend service returns a `403`, the rule for `4xx` takes effect.  
`resource.pathMatchers[].defaultCustomErrorResponsePolicy.errorResponseRules[].matchResponseCodes[]` |  `string` Valid values include: 

  * `A number between 400 and 599`: For example `401` or `503`, in which case the load balancer applies the policy if the error code exactly matches this value.
  * `5xx`: Load Balancer will apply the policy if the backend service responds with any response code in the range of `500` to `599`.
  * `4xx`: Load Balancer will apply the policy if the backend service responds with any response code in the range of `400` to `499`.

Values must be unique within matchResponseCodes and across all `errorResponseRules` of `CustomErrorResponsePolicy`.  
`resource.pathMatchers[].defaultCustomErrorResponsePolicy.errorResponseRules[].path` |  `string` The full path to a file within `backendBucket` . For example: `/errors/defaultError.html` `path` must start with a leading slash. `path` cannot have trailing slashes. If the file is not available in `backendBucket` or the load balancer cannot reach the `BackendBucket`, a simple `Not Found Error` is returned to the client. The value must be from `1` to `1024` characters  
`resource.pathMatchers[].defaultCustomErrorResponsePolicy.errorResponseRules[].overrideResponseCode` |  `integer` The HTTP status code returned with the response containing the custom error content. If `overrideResponseCode` is not supplied, the same response code returned by the original backend bucket or backend service is returned to the client.  
`resource.pathMatchers[].defaultCustomErrorResponsePolicy.errorService` |  `string` The full or partial URL to the `BackendBucket` resource that contains the custom error content. Examples are: 

  * `<https://www.googleapis.com/compute/v1/projects/project/global/backendBuckets/myBackendBucket>`
  * `compute/v1/projects/project/global/backendBuckets/myBackendBucket`
  * `global/backendBuckets/myBackendBucket`

If `errorService` is not specified at lower levels like `pathMatcher`, `pathRule` and `routeRule`, an `errorService` specified at a higher level in the `UrlMap` will be used. If `UrlMap.defaultCustomErrorResponsePolicy` contains one or more `errorResponseRules[]`, it must specify `errorService`. If `load balancer` cannot reach the `backendBucket`, a simple `Not Found Error` will be returned, with the original response code (or `overrideResponseCode` if configured). `errorService` is not supported for internal or regional `HTTP/HTTPS` load balancers.  
`resource.tests[]` |  `object` The list of expected URL mapping tests. Request to update the `UrlMap` succeeds only if all test cases pass. You can specify a maximum of 100 tests per `UrlMap`. Not supported when the URL map is bound to a target gRPC proxy that has `validateForProxyless` field set to `true`.  
`resource.tests[].description` |  `string` Description of this test case.  
`resource.tests[].host` |  `string` Host portion of the URL. If `headers` contains a host header, then `host` must also match the header value.  
`resource.tests[].path` |  `string` Path portion of the URL.  
`resource.tests[].headers[]` |  `object` HTTP headers for this request. If `headers` contains a host header, then `host` must also match the header value.  
`resource.tests[].headers[].name` |  `string` Header name.  
`resource.tests[].headers[].value` |  `string` Header value.  
`resource.tests[].service` |  `string` Expected `BackendService` or `BackendBucket` resource the given URL should be mapped to. The `service` field cannot be set if `expectedRedirectResponseCode` is set.  
`resource.tests[].expectedOutputUrl` |  `string` The expected output URL evaluated by the load balancer containing the scheme, host, path and query parameters. For rules that forward requests to backends, the test passes only when `expectedOutputUrl` matches the request forwarded by the load balancer to backends. For rules with `urlRewrite`, the test verifies that the forwarded request matches `hostRewrite` and `pathPrefixRewrite` in the `urlRewrite` action. When `service` is specified, `expectedOutputUrl``s scheme is ignored. For rules with `urlRedirect`, the test passes only if `expectedOutputUrl` matches the URL in the load balancer's redirect response. If `urlRedirect` specifies `httpsRedirect`, the test passes only if the scheme in `expectedOutputUrl` is also set to `HTTPS`. If `urlRedirect` specifies `stripQuery`, the test passes only if `expectedOutputUrl` does not contain any query parameters. `expectedOutputUrl` is optional when `service` is specified.  
`resource.tests[].expectedRedirectResponseCode` |  `integer` For rules with `urlRedirect`, the test passes only if `expectedRedirectResponseCode` matches the HTTP status code in load balancer's redirect response. `expectedRedirectResponseCode` cannot be set when `service` is set.  
`resource.defaultService` |  `string` The full or partial URL of the `defaultService` resource to which traffic is directed if none of the `hostRules` match. If `defaultRouteAction` is also specified, advanced routing actions, such as URL rewrites, take effect before sending the request to the backend.Only one of `defaultUrlRedirect`, `defaultService` or `defaultRouteAction.weightedBackendService` can be set.`defaultService` has no effect when the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `defaultService`:

  * `compute.regionBackendBuckets.use`
  * `compute.regionBackendServices.use`

  
`resource.defaultRouteAction` |  `object` `defaultRouteAction` takes effect when none of the ` hostRules` match. The load balancer performs advanced routing actions, such as URL rewrites and header transformations, before forwarding the request to the selected backend.Only one of `defaultUrlRedirect`, `defaultService` or `defaultRouteAction.weightedBackendService` can be set. URL maps for classic Application Load Balancers only support the `urlRewrite` action within `defaultRouteAction`.`defaultRouteAction` has no effect when the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`.  
`resource.defaultRouteAction.weightedBackendServices[]` |  `object` A list of weighted backend services to send traffic to when a route match occurs. The weights determine the fraction of traffic that flows to their corresponding `backend service`. If all traffic needs to go to a single backend service, there must be one `weightedBackendService` with weight set to a non-zero number. After a backend service is identified and before forwarding the request to the backend service, advanced routing actions such as URL rewrites and header transformations are applied depending on additional settings specified in this `HttpRouteAction`.  
`resource.defaultRouteAction.weightedBackendServices[].backendService` |  `string` The full or partial URL to the default `BackendService` resource. Before forwarding the request to `backendService`, the load balancer applies any relevant `headerActions` specified as part of this `backendServiceWeight`. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `backendService`:

  * `compute.regionBackendBuckets.use`
  * `compute.regionBackendServices.use`

  
`resource.defaultRouteAction.weightedBackendServices[].weight` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Specifies the fraction of traffic sent to a backend service, computed as `weight / (sum of all weightedBackendService weights in routeAction) `. The selection of a backend service is determined only for new traffic. Once a user's request has been directed to a backend service, subsequent requests are sent to the same backend service as determined by the backend service's session affinity policy. Don't configure session affinity if you're using weighted traffic splitting. If you do, the weighted traffic splitting configuration takes precedence. The value must be from 0 to 1000.  
`resource.defaultRouteAction.weightedBackendServices[].headerAction` |  `object` Specifies changes to request and response headers that need to take effect for the selected `backendService`. `headerAction` specified here take effect before `headerAction` in the enclosing `HttpRouteRule`, `PathMatcher` and `UrlMap`. `headerAction` is not supported for load balancers that have their `loadBalancingScheme` set to `EXTERNAL`. Not supported when the URL map is bound to a target gRPC proxy that has `validateForProxyless` field set to `true`.  
`resource.defaultRouteAction.weightedBackendServices[].headerAction.requestHeadersToRemove[]` |  `string` A list of header names for headers that need to be removed from the request before forwarding the request to the `backendService`.  
`resource.defaultRouteAction.weightedBackendServices[].headerAction.requestHeadersToAdd[]` |  `object` Headers to add to a matching request before forwarding the request to the `backendService`.  
`resource.defaultRouteAction.weightedBackendServices[].headerAction.requestHeadersToAdd[].headerName` |  `string` The name of the header.  
`resource.defaultRouteAction.weightedBackendServices[].headerAction.requestHeadersToAdd[].headerValue` |  `string` The value of the header to add.  
`resource.defaultRouteAction.weightedBackendServices[].headerAction.requestHeadersToAdd[].replace` |  `boolean` If `false`, `headerValue` is appended to any values that already exist for the header. If true, `headerValue` is set for the header, discarding any values that were set for that header. The default value is `true`, unless a variable is present in `headerValue`, in which case the default value is `false`..   
`resource.defaultRouteAction.weightedBackendServices[].headerAction.responseHeadersToRemove[]` |  `string` A list of header names for headers that need to be removed from the response before sending the response back to the client.  
`resource.defaultRouteAction.weightedBackendServices[].headerAction.responseHeadersToAdd[]` |  `object` Headers to add the response before sending the response back to the client.  
`resource.defaultRouteAction.weightedBackendServices[].headerAction.responseHeadersToAdd[].headerName` |  `string` The name of the header.  
`resource.defaultRouteAction.weightedBackendServices[].headerAction.responseHeadersToAdd[].headerValue` |  `string` The value of the header to add.  
`resource.defaultRouteAction.weightedBackendServices[].headerAction.responseHeadersToAdd[].replace` |  `boolean` If `false`, `headerValue` is appended to any values that already exist for the header. If true, `headerValue` is set for the header, discarding any values that were set for that header. The default value is `true`, unless a variable is present in `headerValue`, in which case the default value is `false`..   
`resource.defaultRouteAction.urlRewrite` |  `object` The spec to modify the URL of the request, before forwarding the request to the matched service.  `urlRewrite` is the only action supported in UrlMaps for classic Application Load Balancers. Not supported when the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`.  
`resource.defaultRouteAction.urlRewrite.pathPrefixRewrite` |  `string` Before forwarding the request to the selected backend service, the matching portion of the request's path is replaced by `pathPrefixRewrite`. The value must be from 1 to 1024 characters.  
`resource.defaultRouteAction.urlRewrite.hostRewrite` |  `string` Before forwarding the request to the selected service, the request's host header is replaced with contents of `hostRewrite`. The value must be from 1 to 255 characters.  
`resource.defaultRouteAction.urlRewrite.pathTemplateRewrite` |  `string` If specified, the pattern rewrites the URL path (based on the :path header) using the HTTP template syntax. A corresponding pathTemplateMatch must be specified. Any template variables must exist in the pathTemplateMatch field. 

  * -At least one variable must be specified in the pathTemplateMatch field
  * You can omit variables from the rewritten URL
  * The `*` and `**` operators cannot be matched unless they have a corresponding variable name - e.g. `{format=*}` or `{var=**}`.

For example, a pathTemplateMatch of `/static/{format=**}` could be rewritten as `/static/content/{format}` to prefix `/content` to the URL. Variables can also be re-ordered in a rewrite, so that `/{country}/{format}/{suffix=**}` can be rewritten as `/content/{format}/{country}/{suffix}`. At least one non-empty `routeRules[].matchRules[].path_template_match` is required. Only one of `pathPrefixRewrite` or `pathTemplateRewrite` may be specified.  
`resource.defaultRouteAction.urlRewrite.regexRewrite` |  `object` The regex rewrite to be applied to the URL. Only one of `pathPrefixRewrite`, `pathTemplateRewrite`, or `regexRewrite` may be specified.  
`resource.defaultRouteAction.urlRewrite.regexRewrite.pathPattern` |  `string` Required. The regular expression used to match against the URL path. It uses RE2 syntax with the following constraints: 

  * Any single character operators
  * Groups are allowed to have only submatch operator inside
  * Groups are allowed only without any char repetition, e.g. `.*`
  * Any char repetition, e.g. `.*`, is only allowed to be used in a single regex together with: 
    * Empty string operators
    * Other repetitions
    * Ranges
    * Repetitions of ranges
  * Ranges are only allowed to have: 
    * Character range
    * Digits range
    * Symbols listed in characters allowed for ranges

  
`resource.defaultRouteAction.urlRewrite.regexRewrite.pathSubstitution` |  `string` Required. Required when path pattern is specified. Used to rewrite matching parts of the path.  
`resource.defaultRouteAction.timeout` |  `object` Specifies the timeout for the selected route. Timeout is computed from the time the request has been fully processed (known as _end-of-stream_) up until the response has been processed. Timeout includes all retries. If not specified, this field uses the largest timeout among all backend services associated with the route. Not supported when the URL map is bound to a target gRPC proxy that has `validateForProxyless` field set to `true`.  
`resource.defaultRouteAction.timeout.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.defaultRouteAction.timeout.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.defaultRouteAction.retryPolicy` |  `object` Specifies the retry policy associated with this route.  
`resource.defaultRouteAction.retryPolicy.retryConditions[]` |  `string` Specifies one or more conditions when this retry policy applies. Valid values are: 

  * `5xx`: retry is attempted if the instance or endpoint responds with any `5xx` response code, or if the instance or endpoint does not respond at all. For example, disconnects, reset, read timeout, connection failure, and refused streams.
  * `gateway-error`: Similar to `5xx`, but only applies to response codes `502`, `503` or `504`.
  * `connect-failure`: a retry is attempted on failures connecting to the instance or endpoint. For example, connection timeouts.
  * `retriable-4xx`: a retry is attempted if the instance or endpoint responds with a `4xx` response code. The only error that you can retry is error code `409`.
  * `refused-stream`: a retry is attempted if the instance or endpoint resets the stream with a `REFUSED_STREAM` error code. This reset type indicates that it is safe to retry.
  * `cancelled`: a retry is attempted if the gRPC status code in the response header is set to `cancelled`.
  * `deadline-exceeded`: a retry is attempted if the gRPC status code in the response header is set to `deadline-exceeded`.
  * `internal`: a retry is attempted if the gRPC status code in the response header is set to `internal`.
  * `resource-exhausted`: a retry is attempted if the gRPC status code in the response header is set to `resource-exhausted`.
  * `unavailable`: a retry is attempted if the gRPC status code in the response header is set to `unavailable`.

Only the following codes are supported when the URL map is bound to target gRPC proxy that has validateForProxyless field set to true. 

  * `cancelled`
  * `deadline-exceeded`
  * `internal`
  * `resource-exhausted`
  * `unavailable`

  
`resource.defaultRouteAction.retryPolicy.numRetries` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Specifies the allowed number retries. This number must be > 0\. If not specified, defaults to 1.  
`resource.defaultRouteAction.retryPolicy.perTryTimeout` |  `object` Specifies a non-zero timeout per retry attempt. If not specified, will use the timeout set in the `HttpRouteAction` field. If timeout in the `HttpRouteAction` field is not set, this field uses the largest timeout among all backend services associated with the route. Not supported when the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`.  
`resource.defaultRouteAction.retryPolicy.perTryTimeout.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.defaultRouteAction.retryPolicy.perTryTimeout.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.defaultRouteAction.requestMirrorPolicy` |  `object` Specifies the policy on how requests intended for the route's backends are shadowed to a separate mirrored backend service. The load balancer does not wait for responses from the shadow service. Before sending traffic to the shadow service, the host / authority header is suffixed with `-shadow`. Not supported when the URL map is bound to a target gRPC proxy that has the `validateForProxyless` field set to `true`.  
`resource.defaultRouteAction.requestMirrorPolicy.backendService` |  `string` The full or partial URL to the `BackendService` resource being mirrored to. The backend service configured for a mirroring policy must reference backends that are of the same type as the original backend service matched in the URL map. Serverless NEG backends are not currently supported as a mirrored backend service. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `backendService`:

  * `compute.regionBackendBuckets.use`
  * `compute.regionBackendServices.use`

  
`resource.defaultRouteAction.requestMirrorPolicy.mirrorPercent` |  `number` The percentage of requests to be mirrored to `backendService`.  
`resource.defaultRouteAction.corsPolicy` |  `object` The specification for allowing client-side cross-origin requests. For more information about the W3C recommendation for cross-origin resource sharing (CORS), see [Fetch API Living Standard](https://www.w3.org/TR/cors/). Not supported when the URL map is bound to a target gRPC proxy.  
`resource.defaultRouteAction.corsPolicy.allowOrigins[]` |  `string` Specifies the list of origins that is allowed to do CORS requests. An origin is allowed if it matches either an item in `allowOrigins` or an item in `allowOriginRegexes`.  
`resource.defaultRouteAction.corsPolicy.allowOriginRegexes[]` |  `string` Specifies a regular expression that matches allowed origins. For more information, see [regular expression syntax ](https://github.com/google/re2/wiki/Syntax). An origin is allowed if it matches either an item in `allowOrigins` or an item in `allowOriginRegexes`. Regular expressions can only be used when the loadBalancingScheme is set to `INTERNAL_SELF_MANAGED`.  
`resource.defaultRouteAction.corsPolicy.allowMethods[]` |  `string` Specifies the content for the `Access-Control-Allow-Methods` header.  
`resource.defaultRouteAction.corsPolicy.allowHeaders[]` |  `string` Specifies the content for the `Access-Control-Allow-Headers` header.  
`resource.defaultRouteAction.corsPolicy.exposeHeaders[]` |  `string` Specifies the content for the `Access-Control-Expose-Headers` header.  
`resource.defaultRouteAction.corsPolicy.maxAge` |  `integer` Specifies how long results of a preflight request can be cached in seconds. This field translates to the `Access-Control-Max-Age` header.  
`resource.defaultRouteAction.corsPolicy.allowCredentials` |  `boolean` In response to a preflight request, setting this to `true` indicates that the actual request can include user credentials. This field translates to the `Access-Control-Allow-Credentials` header. Default is `false`.  
`resource.defaultRouteAction.corsPolicy.disabled` |  `boolean` If `true`, disables the CORS policy. The default value is `false`, which indicates that the CORS policy is in effect.  
`resource.defaultRouteAction.faultInjectionPolicy` |  `object` The specification for fault injection introduced into traffic to test the resiliency of clients to backend service failure. As part of fault injection, when clients send requests to a backend service, delays can be introduced by a load balancer on a percentage of requests before sending those requests to the backend service. Similarly requests from clients can be aborted by the load balancer for a percentage of requests. `timeout` and `retryPolicy` is ignored by clients that are configured with a `faultInjectionPolicy` if: 1. The traffic is generated by fault injection AND 2. The fault injection is not a delay fault injection. Fault injection is not supported with the classic Application Load Balancer . To see which load balancers support fault injection, see [Load balancing: Routing and traffic management features](https://cloud.google.com/load-balancing/docs/features#routing-traffic-management).  
`resource.defaultRouteAction.faultInjectionPolicy.delay` |  `object` The specification for how client requests are delayed as part of fault injection, before being sent to a backend service.  
`resource.defaultRouteAction.faultInjectionPolicy.delay.fixedDelay` |  `object` Specifies the value of the fixed delay interval.  
`resource.defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.defaultRouteAction.faultInjectionPolicy.delay.percentage` |  `number` The percentage of traffic for connections, operations, or requests for which a delay is introduced as part of fault injection. The value must be from 0.0 to 100.0 inclusive.  
`resource.defaultRouteAction.faultInjectionPolicy.abort` |  `object` The specification for how client requests are aborted as part of fault injection.  
`resource.defaultRouteAction.faultInjectionPolicy.abort.httpStatus` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The HTTP status code used to abort the request. The value must be from 200 to 599 inclusive. For gRPC protocol, the gRPC status code is mapped to HTTP status code according to this [ mapping table](https://github.com/grpc/grpc/blob/master/doc/http-grpc-status-mapping.md). HTTP status 200 is mapped to gRPC status UNKNOWN. Injecting an OK status is currently not supported by Traffic Director.  
`resource.defaultRouteAction.faultInjectionPolicy.abort.percentage` |  `number` The percentage of traffic for connections, operations, or requests that is aborted as part of fault injection. The value must be from 0.0 to 100.0 inclusive.  
`resource.defaultRouteAction.maxStreamDuration` |  `object` Specifies the maximum duration (timeout) for streams on the selected route. Unlike the `timeout` field where the timeout duration starts from the time the request has been fully processed (known as _end-of-stream_), the duration in this field is computed from the beginning of the stream until the response has been processed, including all retries. A stream that does not complete in this duration is closed. If not specified, this field uses the maximum `maxStreamDuration` value among all backend services associated with the route. This field is only allowed if the Url map is used with backend services with `loadBalancingScheme` set to `INTERNAL_SELF_MANAGED`.  
`resource.defaultRouteAction.maxStreamDuration.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.defaultRouteAction.maxStreamDuration.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.defaultRouteAction.cachePolicy` |  `object` Specifies the cache policy configuration for matched traffic. Available only for Global `EXTERNAL_MANAGED` load balancer schemes. At least one property must be specified. This policy cannot be specified if any target backend has Identity-Aware Proxy enabled.  
`resource.defaultRouteAction.cachePolicy.cacheKeyPolicy` |  `object` The cache key configuration. If not specified, the default behavior depends on the backend type: for Backend Services, the complete request URI is used; for Backend Buckets, the request URI is used without the protocol or host, and only query parameters known to Cloud Storage are included.  
`resource.defaultRouteAction.cachePolicy.cacheKeyPolicy.includeProtocol` |  `boolean` If true, http and https requests will be cached separately.Note: This setting is only applicable to routes that use a Backend Service. It does not affect requests served by a Backend Bucket, as the protocol is never included in a Backend Bucket's cache key. Attempting to set on a route that points exclusively to Backend Buckets will result in a configuration error.  
`resource.defaultRouteAction.cachePolicy.cacheKeyPolicy.includeHost` |  `boolean` If true, requests to different hosts will be cached separately.Note: This setting is only applicable to routes that use a Backend Service. It does not affect requests served by a Backend Bucket, as the host is never included in a Backend Bucket's cache key. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error.  
`resource.defaultRouteAction.cachePolicy.cacheKeyPolicy.includeQueryString` |  `boolean` If true, include query string parameters in the cache key according to `includedQueryParameters` and `excludedQueryParameters`. If neither is set, the entire query string will be included. If false, the query string will be excluded from the cache key entirely.Note: This field applies to routes that use backend services. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error. For routes that point to a Backend Bucket, use `includedQueryParameters` to define which parameters should be part of the cache key.  
`resource.defaultRouteAction.cachePolicy.cacheKeyPolicy.includedQueryParameters[]` |  `string` Names of query string parameters to include in cache keys. All other parameters will be excluded. Either specify `includedQueryParameters` or `excludedQueryParameters`, not both. '&' and '=' will be percent encoded and not treated as delimiters.  
`resource.defaultRouteAction.cachePolicy.cacheKeyPolicy.excludedQueryParameters[]` |  `string` Names of query string parameters to exclude in cache keys. All other parameters will be included. Either specify `excludedQueryParameters` or `includedQueryParameters`, not both. '&' and '=' will be percent encoded and not treated as delimiters.Note: This field applies to routes that use backend services. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error. For routes that point to a Backend Bucket, use `includedQueryParameters` to define which parameters should be part of the cache key.  
`resource.defaultRouteAction.cachePolicy.cacheKeyPolicy.includedHeaderNames[]` |  `string` Allows HTTP request headers (by name) to be used in the cache key.  
`resource.defaultRouteAction.cachePolicy.cacheKeyPolicy.includedCookieNames[]` |  `string` Allows HTTP cookies (by name) to be used in the cache key. The name=value pair will be used in the cache key Cloud CDN generates.Note: This setting is only applicable to routes that use a Backend Service. It does not affect requests served by a Backend Bucket. Attempting to set it on a route that points exclusively to Backend Buckets will result in a configuration error. Up to 5 cookie names can be specified.  
`resource.defaultRouteAction.cachePolicy.requestCoalescing` |  `boolean` If true then Cloud CDN will combine multiple concurrent cache fill requests into a small number of requests to the origin. If not specified, Cloud CDN applies request coalescing by default.  
`resource.defaultRouteAction.cachePolicy.cacheMode` |  `enum` Specifies the cache setting for all responses from this route. If not specified, Cloud CDN uses `CACHE_ALL_STATIC` mode.  
`resource.defaultRouteAction.cachePolicy.defaultTtl` |  `object` Specifies the default TTL for cached content for responses that do not have an existing valid TTL (max-age or s-maxage). Setting a TTL of "0" means "always revalidate". The value of `defaultTtl` cannot be set to a value greater than that of `maxTtl`. When the `cacheMode` is set to `FORCE_CACHE_ALL`, the `defaultTtl` will overwrite the TTL set in all responses. The maximum allowed value is 31,622,400s (1 year). Infrequently accessed objects may be evicted from the cache before the defined TTL. If not specified, Cloud CDN uses 3600s (1 hour) for `CACHE_ALL_STATIC` and `FORCE_CACHE_ALL` modes. Cannot be specified when `cacheMode` is `USE_ORIGIN_HEADERS`.  
`resource.defaultRouteAction.cachePolicy.defaultTtl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.defaultRouteAction.cachePolicy.defaultTtl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.defaultRouteAction.cachePolicy.maxTtl` |  `object` Specifies the maximum allowed TTL for cached content. Cache directives that attempt to set a max-age or s-maxage higher than this, or an Expires header more than `maxTtl` seconds in the future will be capped at the value of `maxTtl`, as if it were the value of an s-maxage Cache-Control directive. Headers sent to the client will not be modified. Setting a TTL of "0" means "always revalidate". The maximum allowed value is 31,622,400s (1 year). Infrequently accessed objects may be evicted from the cache before the defined TTL. If not specified, Cloud CDN uses 86400s (1 day) for `CACHE_ALL_STATIC` mode. Can be specified only for `CACHE_ALL_STATIC` cache mode.  
`resource.defaultRouteAction.cachePolicy.maxTtl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.defaultRouteAction.cachePolicy.maxTtl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.defaultRouteAction.cachePolicy.clientTtl` |  `object` Specifies a separate client (e.g. browser client) maximum TTL for cached content. This is used to clamp the max-age (or Expires) value sent to the client. With `FORCE_CACHE_ALL`, the lesser of `clientTtl` and `defaultTtl` is used for the response max-age directive, along with a "public" directive. For cacheable content in `CACHE_ALL_STATIC` mode, `clientTtl` clamps the max-age from the origin (if specified), or else sets the response max-age directive to the lesser of the `clientTtl` and `defaultTtl`, and also ensures a "public" cache-control directive is present. The maximum allowed value is 31,622,400s (1 year). If not specified, Cloud CDN uses 3600s (1 hour) for `CACHE_ALL_STATIC` mode. Cannot exceed `maxTtl`. Cannot be specified when `cacheMode` is `USE_ORIGIN_HEADERS`.  
`resource.defaultRouteAction.cachePolicy.clientTtl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.defaultRouteAction.cachePolicy.clientTtl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.defaultRouteAction.cachePolicy.negativeCaching` |  `boolean` Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects. This can reduce the load on your origin and improve end-user experience by reducing response latency. When the `cacheMode` is set to `CACHE_ALL_STATIC` or `USE_ORIGIN_HEADERS`, negative caching applies to responses with the specified response code that lack any Cache-Control, Expires, or Pragma: no-cache directives. When the `cacheMode` is set to `FORCE_CACHE_ALL`, negative caching applies to all responses with the specified response code, and overrides any caching headers. By default, Cloud CDN applies the following TTLs to these HTTP status codes:

  * 300 (Multiple Choice), 301, 308 (Permanent Redirects): 10m
  * 404 (Not Found), 410 (Gone), 451 (Unavailable For Legal Reasons): 120s
  * 405 (Method Not Found), 501 (Not Implemented): 60s

These defaults can be overridden in `negativeCachingPolicy`. If not specified, Cloud CDN applies negative caching by default.  
`resource.defaultRouteAction.cachePolicy.negativeCachingPolicy[]` |  `object` Sets a cache TTL for the specified HTTP status code. `negativeCaching` must be enabled to configure `negativeCachingPolicy`. Omitting the policy and leaving `negativeCaching` enabled will use Cloud CDN's default cache TTLs. Note that when specifying an explicit `negativeCachingPolicy`, you should take care to specify a cache TTL for all response codes that you wish to cache. Cloud CDN will not apply any default negative caching when a policy exists.  
`resource.defaultRouteAction.cachePolicy.negativeCachingPolicy[].code` |  `integer` The HTTP status code to define a TTL against. Only HTTP status codes 300, 301, 302, 307, 308, 404, 405, 410, 421, 451 and 501 can be specified as values, and you cannot specify a status code more than once.  
`resource.defaultRouteAction.cachePolicy.negativeCachingPolicy[].ttl` |  `object` The TTL (in seconds) for which to cache responses with the corresponding status code. The maximum allowed value is 1800s (30 minutes). Infrequently accessed objects may be evicted from the cache before the defined TTL.  
`resource.defaultRouteAction.cachePolicy.negativeCachingPolicy[].ttl.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.defaultRouteAction.cachePolicy.negativeCachingPolicy[].ttl.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.defaultRouteAction.cachePolicy.cacheBypassRequestHeaderNames[]` |  `string` Bypass the cache when the specified request headers are matched by name, e.g. Pragma or Authorization headers. Values are case-insensitive. Up to 5 header names can be specified. The cache is bypassed for all `cacheMode` values.  
`resource.defaultRouteAction.cachePolicy.serveWhileStale` |  `object` Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache. This setting defines the default "max-stale" duration for any cached responses that do not specify a max-stale directive. Stale responses that exceed the TTL configured here will not be served. The default limit (max-stale) is 86400s (1 day), which will allow stale content to be served up to this limit beyond the max-age (or s-maxage) of a cached response. The maximum allowed value is 604800 (1 week). Set this to zero (0) to disable serve-while-stale.  
`resource.defaultRouteAction.cachePolicy.serveWhileStale.seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Span of time at a resolution of a second. Must be from 0 to 315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`resource.defaultRouteAction.cachePolicy.serveWhileStale.nanos` |  `integer` Span of time that's a fraction of a second at nanosecond resolution. Durations less than one second are represented with a 0 `seconds` field and a positive `nanos` field. Must be from 0 to 999,999,999 inclusive.  
`resource.defaultUrlRedirect` |  `object` When none of the specified `hostRules` match, the request is redirected to a URL specified by `defaultUrlRedirect`.Only one of `defaultUrlRedirect`, `defaultService` or `defaultRouteAction.weightedBackendService` can be set.Not supported when the URL map is bound to a target gRPC proxy.  
`resource.defaultUrlRedirect.hostRedirect` |  `string` The host that is used in the redirect response instead of the one that was supplied in the request. The value must be from 1 to 255 characters.  
`resource.defaultUrlRedirect.pathRedirect` |  `string` The path that is used in the redirect response instead of the one that was supplied in the request. `pathRedirect` cannot be supplied together with `prefixRedirect`. Supply one alone or neither. If neither is supplied, the path of the original request is used for the redirect. The value must be from 1 to 1024 characters.  
`resource.defaultUrlRedirect.prefixRedirect` |  `string` The prefix that replaces the `prefixMatch` specified in the `HttpRouteRuleMatch`, retaining the remaining portion of the URL before redirecting the request. `prefixRedirect` cannot be supplied together with `pathRedirect`. Supply one alone or neither. If neither is supplied, the path of the original request is used for the redirect. The value must be from 1 to 1024 characters.  
`resource.defaultUrlRedirect.redirectResponseCode` |  `enum` The HTTP Status code to use for this RedirectAction. Supported values are: 

  * MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301.
  * FOUND, which corresponds to 302.
  * SEE_OTHER which corresponds to 303.
  * TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method is retained.
  * PERMANENT_REDIRECT, which corresponds to 308. In this case, the request method is retained.

  
`resource.defaultUrlRedirect.httpsRedirect` |  `boolean` If set to `true`, the URL scheme in the redirected request is set to `HTTPS`. If set to `false`, the URL scheme of the redirected request remains the same as that of the request. This must only be set for URL maps used in `TargetHttpProxy`s. Setting this true for `TargetHttpsProxy` is not permitted. The default is set to `false`.  
`resource.defaultUrlRedirect.stripQuery` |  `boolean` If set to `true`, any accompanying query portion of the original URL is removed before redirecting the request. If set to `false`, the query portion of the original URL is retained. The default is set to `false`.   
`resource.headerAction` |  `object` Specifies changes to request and response headers that need to take effect for the selected `backendService`. The `headerAction` specified here take effect after `headerAction` specified under `pathMatcher`. `headerAction` is not supported for load balancers that have their `loadBalancingScheme` set to `EXTERNAL`. Not supported when the URL map is bound to a target gRPC proxy that has `validateForProxyless` field set to `true`.  
`resource.headerAction.requestHeadersToRemove[]` |  `string` A list of header names for headers that need to be removed from the request before forwarding the request to the `backendService`.  
`resource.headerAction.requestHeadersToAdd[]` |  `object` Headers to add to a matching request before forwarding the request to the `backendService`.  
`resource.headerAction.requestHeadersToAdd[].headerName` |  `string` The name of the header.  
`resource.headerAction.requestHeadersToAdd[].headerValue` |  `string` The value of the header to add.  
`resource.headerAction.requestHeadersToAdd[].replace` |  `boolean` If `false`, `headerValue` is appended to any values that already exist for the header. If true, `headerValue` is set for the header, discarding any values that were set for that header. The default value is `true`, unless a variable is present in `headerValue`, in which case the default value is `false`..   
`resource.headerAction.responseHeadersToRemove[]` |  `string` A list of header names for headers that need to be removed from the response before sending the response back to the client.  
`resource.headerAction.responseHeadersToAdd[]` |  `object` Headers to add the response before sending the response back to the client.  
`resource.headerAction.responseHeadersToAdd[].headerName` |  `string` The name of the header.  
`resource.headerAction.responseHeadersToAdd[].headerValue` |  `string` The value of the header to add.  
`resource.headerAction.responseHeadersToAdd[].replace` |  `boolean` If `false`, `headerValue` is appended to any values that already exist for the header. If true, `headerValue` is set for the header, discarding any values that were set for that header. The default value is `true`, unless a variable is present in `headerValue`, in which case the default value is `false`..   
`resource.defaultCustomErrorResponsePolicy` |  `object` `defaultCustomErrorResponsePolicy` specifies how the Load Balancer returns error responses when `BackendService`or `BackendBucket` responds with an error. This policy takes effect at the load balancer level and applies only when no policy has been defined for the error code at lower levels like PathMatcher, RouteRule and PathRule within this UrlMap. For example, consider a UrlMap with the following configuration: 

  * `defaultCustomErrorResponsePolicy` containing policies for responding to `5xx` and `4xx` errors
  * A PathMatcher configured for `*.example.com` has `defaultCustomErrorResponsePolicy` for `4xx`.

If a request for `<http://www.example.com/>` encounters a `404`, the policy in `pathMatcher.defaultCustomErrorResponsePolicy` will be enforced. When the request for `<http://www.example.com/>` encounters a `502`, the policy in `UrlMap.defaultCustomErrorResponsePolicy` will be enforced. When a request that does not match any host in `*.example.com` such as `<http://www.myotherexample.com/>`, encounters a `404`, `UrlMap.defaultCustomErrorResponsePolicy` takes effect. When used in conjunction with `defaultRouteAction.retryPolicy`, retries take precedence. Only once all retries are exhausted, the `defaultCustomErrorResponsePolicy` is applied. While attempting a retry, if `load balancer` is successful in reaching the service, the `defaultCustomErrorResponsePolicy` is ignored and the response from the service is returned to the client. `defaultCustomErrorResponsePolicy` is supported only for global external Application Load Balancers.  
`resource.defaultCustomErrorResponsePolicy.errorResponseRules[]` |  `object` Specifies rules for returning error responses. In a given policy, if you specify rules for both a range of error codes as well as rules for specific error codes then rules with specific error codes have a higher priority. For example, assume that you configure a rule for `401` (Un-authorized) code, and another for all 4 series error codes `(4XX)`. If the backend service returns a `401`, then the rule for `401` will be applied. However if the backend service returns a `403`, the rule for `4xx` takes effect.  
`resource.defaultCustomErrorResponsePolicy.errorResponseRules[].matchResponseCodes[]` |  `string` Valid values include: 

  * `A number between 400 and 599`: For example `401` or `503`, in which case the load balancer applies the policy if the error code exactly matches this value.
  * `5xx`: Load Balancer will apply the policy if the backend service responds with any response code in the range of `500` to `599`.
  * `4xx`: Load Balancer will apply the policy if the backend service responds with any response code in the range of `400` to `499`.

Values must be unique within matchResponseCodes and across all `errorResponseRules` of `CustomErrorResponsePolicy`.  
`resource.defaultCustomErrorResponsePolicy.errorResponseRules[].path` |  `string` The full path to a file within `backendBucket` . For example: `/errors/defaultError.html` `path` must start with a leading slash. `path` cannot have trailing slashes. If the file is not available in `backendBucket` or the load balancer cannot reach the `BackendBucket`, a simple `Not Found Error` is returned to the client. The value must be from `1` to `1024` characters  
`resource.defaultCustomErrorResponsePolicy.errorResponseRules[].overrideResponseCode` |  `integer` The HTTP status code returned with the response containing the custom error content. If `overrideResponseCode` is not supplied, the same response code returned by the original backend bucket or backend service is returned to the client.  
`resource.defaultCustomErrorResponsePolicy.errorService` |  `string` The full or partial URL to the `BackendBucket` resource that contains the custom error content. Examples are: 

  * `<https://www.googleapis.com/compute/v1/projects/project/global/backendBuckets/myBackendBucket>`
  * `compute/v1/projects/project/global/backendBuckets/myBackendBucket`
  * `global/backendBuckets/myBackendBucket`

If `errorService` is not specified at lower levels like `pathMatcher`, `pathRule` and `routeRule`, an `errorService` specified at a higher level in the `UrlMap` will be used. If `UrlMap.defaultCustomErrorResponsePolicy` contains one or more `errorResponseRules[]`, it must specify `errorService`. If `load balancer` cannot reach the `backendBucket`, a simple `Not Found Error` will be returned, with the original response code (or `overrideResponseCode` if configured). `errorService` is not supported for internal or regional `HTTP/HTTPS` load balancers.  
`resource.fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field is ignored when inserting a `UrlMap`. An up-to-date fingerprint must be provided in order to update the `UrlMap`, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve a UrlMap.A base64-encoded string.  
`resource.region` |  `string` Output only. URL of the region where the regional URL map resides. This field is not applicable to global URL maps. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
  
### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "result": {
        "loadSucceeded": boolean,
        "loadErrors": [
          string
        ],
        "testPassed": boolean,
        "testFailures": [
          {
            "host": string,
            "path": string,
            "headers": [
              {
                "name": string,
                "value": string
              }
            ],
            "expectedService": string,
            "actualService": string,
            "expectedOutputUrl": string,
            "actualOutputUrl": string,
            "expectedRedirectResponseCode": integer,
            "actualRedirectResponseCode": integer
          }
        ]
      }
    }  
  
Fields  
---  
`result` |  `object`  
`result.loadSucceeded` |  `boolean` Whether the given UrlMap can be successfully loaded. If false, 'loadErrors' indicates the reasons.  
`result.loadErrors[]` |  `string`  
`result.testPassed` |  `boolean` If successfully loaded, this field indicates whether the test passed. If false, 'testFailures's indicate the reason of failure.  
`result.testFailures[]` |  `object`  
`result.testFailures[].host` |  `string` Host portion of the URL.  
`result.testFailures[].path` |  `string` Path portion including query parameters in the URL.  
`result.testFailures[].headers[]` |  `object` HTTP headers of the request.  
`result.testFailures[].headers[].name` |  `string` Header name.  
`result.testFailures[].headers[].value` |  `string` Header value.  
`result.testFailures[].expectedService` |  `string` Expected `BackendService` or `BackendBucket` resource the given URL should be mapped to.  
`result.testFailures[].actualService` |  `string` `BackendService` or `BackendBucket` returned by load balancer.  
`result.testFailures[].expectedOutputUrl` |  `string` The expected output URL evaluated by a load balancer containing the scheme, host, path and query parameters.  
`result.testFailures[].actualOutputUrl` |  `string` The actual output URL evaluated by a load balancer containing the scheme, host, path and query parameters.  
`result.testFailures[].expectedRedirectResponseCode` |  `integer` Expected HTTP status code for rule with `urlRedirect` calculated by load balancer  
`result.testFailures[].actualRedirectResponseCode` |  `integer` Actual HTTP status code for rule with `urlRedirect` calculated by load balancer  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.regionUrlMaps.validate`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
