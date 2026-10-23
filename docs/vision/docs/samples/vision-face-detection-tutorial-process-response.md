---
url: https://docs.cloud.google.com/vision/docs/samples/vision-face-detection-tutorial-process-response/
title: Process the Cloud Vision API response \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:01:17.115313+00:00
---

# Process the Cloud Vision API response  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/samples/vision-face-detection-tutorial-process-response/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Samples ](https://docs.cloud.google.com/vision/docs/samples)



#  Process the Cloud Vision API response Stay organized with collections  Save and categorize content based on your preferences. 

Process the Cloud Vision API response when faces are detected in an image.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Face detection tutorial](https://docs.cloud.google.com/vision/docs/face-tutorial)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /** Reads image {@code inputPath} and writes {@code outputPath} with {@code faces} outlined. */
    private static void writeWithFaces(Path inputPath, Path outputPath, List<FaceAnnotation> faces)
        throws IOException {
      BufferedImage img = ImageIO.read(inputPath.toFile());
      annotateWithFaces(img, faces);
      ImageIO.write(img, "jpg", outputPath.toFile());
    }
    
    /** Annotates an image {@code img} with a polygon around each face in {@code faces}. */
    public static void annotateWithFaces(BufferedImage img, List<FaceAnnotation> faces) {
      for (FaceAnnotation face : faces) {
        annotateWithFace(img, face);
      }
    }
    
    /** Annotates an image {@code img} with a polygon defined by {@code face}. */
    private static void annotateWithFace(BufferedImage img, FaceAnnotation face) {
      Graphics2D gfx = img.createGraphics();
      Polygon poly = new Polygon();
      for (Vertex vertex : face.getFdBoundingPoly().getVertices()) {
        poly.addPoint(vertex.getX(), vertex.getY());
      }
      gfx.setStroke(new BasicStroke(5));
      gfx.setColor(new Color(0x00ff00));
      gfx.draw(poly);
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function highlightFaces(inputFile, faces, outputFile, PImage) {
      // Open the original image
      const stream = fs.createReadStream(inputFile);
      let promise;
      if (inputFile.match(/\.jpg$/)) {
        promise = PImage.decodeJPEGFromStream(stream);
      } else if (inputFile.match(/\.png$/)) {
        promise = PImage.decodePNGFromStream(stream);
      } else {
        throw new Error(`Unknown filename extension ${inputFile}`);
      }
      const img = await promise;
      const context = img.getContext('2d');
      context.drawImage(img, 0, 0, img.width, img.height, 0, 0);
    
      // Now draw boxes around all the faces
      context.strokeStyle = 'rgba(0,255,0,0.8)';
      context.lineWidth = '5';
    
      faces.forEach(face => {
        context.beginPath();
        let origX = 0;
        let origY = 0;
        face.boundingPoly.vertices.forEach((bounds, i) => {
          if (i === 0) {
            origX = bounds.x;
            origY = bounds.y;
            context.moveTo(bounds.x, bounds.y);
          } else {
            context.lineTo(bounds.x, bounds.y);
          }
        });
        context.lineTo(origX, origY);
        context.stroke();
      });
    
      // Write the result to a file
      console.log(`Writing to file ${outputFile}`);
      const writeStream = fs.createWriteStream(outputFile);
      await PImage.encodePNGToStream(img, writeStream);
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # draw box around faces
    if ($faces->count() && $outFile) {
        $imageCreateFunc = [
            'png' => 'imagecreatefrompng',
            'gd' => 'imagecreatefromgd',
            'gif' => 'imagecreatefromgif',
            'jpg' => 'imagecreatefromjpeg',
            'jpeg' => 'imagecreatefromjpeg',
        ];
        $imageWriteFunc = [
            'png' => 'imagepng',
            'gd' => 'imagegd',
            'gif' => 'imagegif',
            'jpg' => 'imagejpeg',
            'jpeg' => 'imagejpeg',
        ];
    
        copy($path, $outFile);
        $ext = strtolower(pathinfo($path, PATHINFO_EXTENSION));
        if (!array_key_exists($ext, $imageCreateFunc)) {
            throw new \Exception('Unsupported image extension');
        }
        $outputImage = call_user_func($imageCreateFunc[$ext], $outFile);
    
        foreach ($faces as $face) {
            $vertices = $face->getBoundingPoly()->getVertices();
            if ($vertices) {
                $x1 = $vertices[0]->getX();
                $y1 = $vertices[0]->getY();
                $x2 = $vertices[2]->getX();
                $y2 = $vertices[2]->getY();
                imagerectangle($outputImage, $x1, $y1, $x2, $y2, 0x00ff00);
            }
        }

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def highlight_faces(image, faces, output_filename):
        """Draws a polygon around the faces, then saves to output_filename.
    
        Args:
          image: a file containing the image with the faces.
          faces: a list of faces found in the file. This should be in the format
              returned by the Vision API.
          output_filename: the name of the image file to be created, where the
              faces have polygons drawn around them.
        """
        im = Image.open(image)
        draw = ImageDraw.Draw(im)
        # Sepecify the font-family and the font-size
        for face in faces:
            box = [(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices]
            draw.line(box + [box[0]], width=5, fill="#00ff00")
            # Place the confidence value/score of the detected faces above the
            # detection box in the output image
            draw.text(
                (
                    (face.bounding_poly.vertices)[0].x,
                    (face.bounding_poly.vertices)[0].y - 30,
                ),
                str(format(face.detection_confidence, ".3f")) + "%",
                fill="#FF0000",
            )
        im.save(output_filename)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvision). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
