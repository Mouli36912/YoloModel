# from flask import Flask, request, jsonify, render_template, send_file
# import cv2
# import numpy as np
# import os

# app = Flask(__name__)

# # Load YOLO
# yolo = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
# classes = []
# with open("coco.names", "r") as file:
#     classes = [line.strip() for line in file.readlines()]

# layer_names = yolo.getLayerNames()
# output_layers = [layer_names[i - 1] for i in yolo.getUnconnectedOutLayers()]

# colorRed = (0, 0, 255)
# colorGreen = (0, 255, 0)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/upload', methods=['GET,POST'])
# def detect():
#     if 'file' not in request.files:
#         return "No file part"
#     file = request.files['file']    
#     if file.filename == '':
#         return "No selected file"
#     if file:
#         file_path = os.path.join("uploads", file.filename)
#         file.save(file_path)
#         print(file_path)

#         # Load image
#         img = cv2.imread(file_path)
#         height, width, channels = img.shape

#         # Detecting objects
#         blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
#         yolo.setInput(blob)
#         outputs = yolo.forward(output_layers)

#         class_ids = []
#         confidences = []
#         boxes = []
#         for output in outputs:
#             for detection in output:
#                 scores = detection[5:]
#                 class_id = np.argmax(scores)
#                 confidence = scores[class_id]
#                 if confidence > 0.5:
#                     center_x = int(detection[0] * width)
#                     center_y = int(detection[1] * height)
#                     w = int(detection[2] * width)
#                     h = int(detection[3] * height)

#                     x = int(center_x - w / 2)
#                     y = int(center_y - h / 2)

#                     boxes.append([x, y, w, h])
#                     confidences.append(float(confidence))
#                     class_ids.append(class_id)

#         indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
#         for i in range(len(boxes)):
#             if i in indexes:
#                 x, y, w, h = boxes[i]
#                 label = str(classes[class_ids[i]])
#                 cv2.rectangle(img, (x, y), (x + w, y + h), colorGreen, 3)
#                 cv2.putText(img, label, (x, y + 10), cv2.FONT_HERSHEY_PLAIN, 2, colorRed, 2)

#         output_path = os.path.join("static", "output.jpg")
#         cv2.imwrite(output_path, img)

#         return send_file(output_path, mimetype='image/jpeg')

# if __name__ == '__main__':
#     if not os.path.exists('uploads'):
#         os.makedirs('uploads')
#         print(os.makedirs('uploads'))   
#     app.run(debug=True)

#---------------------------------------------------------------------------------------------------------------------

# from flask import Flask, request, render_template, send_file
# import cv2
# import numpy as np
# import os

# app = Flask(__name__)

# # Load YOLO
# yolo = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
# classes = []
# with open("coco.names", "r") as file:
#     classes = [line.strip() for line in file.readlines()]

# layer_names = yolo.getLayerNames()
# output_layers = [layer_names[i - 1] for i in yolo.getUnconnectedOutLayers()]

# colorRed = (0, 0, 255)
# colorGreen = (0, 255, 0)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def detect():
#     if 'file' not in request.files:
#         return "No file part"
#     file = request.files['file']
#     if file.filename == '':
#         return "No selected file"
#     if file:
#         file_path = os.path.join("uploads", file.filename)
#         file.save(file_path)
#         print(file_path)

#         # Load image
#         img = cv2.imread(file_path)
#         height, width, channels = img.shape

#         # Detecting objects
#         blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
#         yolo.setInput(blob)
#         outputs = yolo.forward(output_layers)

#         class_ids = []
#         confidences = []
#         boxes = []
#         for output in outputs:
#             for detection in output:
#                 scores = detection[5:]
#                 class_id = np.argmax(scores)
#                 confidence = scores[class_id]
#                 if confidence > 0.5:
#                     center_x = int(detection[0] * width)
#                     center_y = int(detection[1] * height)
#                     w = int(detection[2] * width)
#                     h = int(detection[3] * height)

#                     x = int(center_x - w / 2)
#                     y = int(center_y - h / 2)

#                     boxes.append([x, y, w, h])
#                     confidences.append(float(confidence))
#                     class_ids.append(class_id)

#         indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
#         for i in range(len(boxes)):
#             if i in indexes:
#                 x, y, w, h = boxes[i]
#                 label = str(classes[class_ids[i]])
#                 cv2.rectangle(img, (x, y), (x + w, y + h), colorGreen, 3)
#                 cv2.putText(img, label, (x, y + 10), cv2.FONT_HERSHEY_PLAIN, 2, colorRed, 2)

#         output_path = os.path.join("static", "output.jpg")
#         cv2.imwrite(output_path, img)

#         return send_file(output_path, mimetype='image/jpeg')

# if __name__ == '__main__':
#     if not os.path.exists('uploads'):
#         os.makedirs('uploads')
#     app.run(debug=True)

#--------------------------------------------------------------------------------------------------------------

# Working version of flask appication, don't disturb this version

# from flask import Flask, request, render_template, jsonify
# import cv2
# import numpy as np
# import os

# app = Flask(__name__)

# # Load YOLO
# yolo = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
# classes = []
# with open("coco.names", "r") as file:
#     classes = [line.strip() for line in file.readlines()]

# layer_names = yolo.getLayerNames()
# output_layers = [layer_names[i - 1] for i in yolo.getUnconnectedOutLayers()]

# colorRed = (0, 0, 255)
# colorGreen = (0, 255, 0)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def detect():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file part"})
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({"error": "No selected file"})
#     if file:
#         file_path = os.path.join("uploads", file.filename)
#         file.save(file_path)
#         print(file_path)

#         # Load image
#         img = cv2.imread(file_path)
#         height, width, channels = img.shape

#         # Detecting objects
#         blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
#         yolo.setInput(blob)
#         outputs = yolo.forward(output_layers)

#         class_ids = []
#         confidences = []
#         boxes = []
#         for output in outputs:
#             for detection in output:
#                 scores = detection[5:]
#                 class_id = np.argmax(scores)
#                 confidence = scores[class_id]
#                 if confidence > 0.5:
#                     center_x = int(detection[0] * width)
#                     center_y = int(detection[1] * height)
#                     w = int(detection[2] * width)
#                     h = int(detection[3] * height)

#                     x = int(center_x - w / 2)
#                     y = int(center_y - h / 2)

#                     boxes.append([x, y, w, h])
#                     confidences.append(float(confidence))
#                     class_ids.append(class_id)

#         indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
#         for i in range(len(boxes)):
#             if i in indexes:
#                 x, y, w, h = boxes[i]
#                 label = str(classes[class_ids[i]])
#                 cv2.rectangle(img, (x, y), (x + w, y + h), colorGreen, 3)
#                 cv2.putText(img, label, (x, y + 10), cv2.FONT_HERSHEY_PLAIN, 8, colorRed, 8)

#         output_filename = file.filename.rsplit('.', 1)[0] + '_output.jpg'
#         output_path = os.path.join("static", output_filename)
#         cv2.imwrite(output_path, img)

#         return jsonify({"url": f"/static/{output_filename}"})

# if __name__ == '__main__':
#     if not os.path.exists('uploads'):
#         os.makedirs('uploads')
#     if not os.path.exists('static'):
#         os.makedirs('static')
#     app.run(debug=True)

#--------------------------------------------------------------------------------------------------------------

from flask import Flask, request, jsonify, render_template, send_file
import cv2
import numpy as np
import os
import uuid  # Import UUID for generating unique filenames

app = Flask(__name__)

# Load YOLO
yolo = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as file:
    classes = [line.strip() for line in file.readlines()]

layer_names = yolo.getLayerNames()
output_layers = [layer_names[i - 1] for i in yolo.getUnconnectedOutLayers()]

colorRed = (0, 0, 255)
colorGreen = (0, 255, 0)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def detect():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']    
    if file.filename == '':
        return "No selected file"
    
    # Generate a unique filename
    unique_filename = str(uuid.uuid4()) + '.jpg'  # Example: 'fd3a1841-3b09-4f55-a0d4-79a3a9b1b40e.jpg'
    file_path = os.path.join("uploads", unique_filename)

    if file:
        file.save(file_path)
        print("Saved as:", file_path)

        # Load image
        img = cv2.imread(file_path)
        height, width, channels = img.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        yolo.setInput(blob)
        outputs = yolo.forward(output_layers)

        class_ids = []
        confidences = []
        boxes = []
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                cv2.rectangle(img, (x, y), (x + w, y + h), colorGreen, 3)
                cv2.putText(img, label, (x, y + 10), cv2.FONT_HERSHEY_PLAIN, 8, colorRed, 8)

        output_path = os.path.join("static", unique_filename)
        cv2.imwrite(output_path, img)

        return jsonify({'url': '/' + output_path})  # Return the URL to access the processed image

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)




