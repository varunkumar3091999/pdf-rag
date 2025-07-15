from flask import Flask, request, jsonify
from flasgger import Swagger


from read_pdf import add_to_chroma, load_documents, split_documents

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    """
    A greeting endpoint
    ---
    parameters:
      - name: name
        in: path
        type: string
        required: true
        description: The name to greet
    responses:
      200:
        description: A greeting message
        examples:
          application/json: { "message": "Hello, John!" }
    """
    return jsonify({"message": f"Hello, {name}!"})



@app.route('/upload-pdf', methods=["POST"])
def upload_pdf():
  """
    Upload and index a PDF
    ---
    consumes:
      - multipart/form-data
    parameters:
      - name: file
        in: formData
        type: file
        required: true
        description: The PDF file to upload
    responses:
      200:
        description: Upload success message
        examples:
          application/json: {"message": "PDF uploaded and indexed successfully!"}
      400:
        description: Invalid request
        examples:
          application/json: {"error": "No file uploaded"}
  """
  print(request.files, "files")
  if 'file' not in request.files:
    return jsonify({"error": "No file uploaded"}), 400
  
  file = request.files['file']
  if not file.filename.endswith('.pdf'):
    return jsonify({"error": "File must be a pdf"}), 400
  
  pdf_path = f"./data/{file.filename}"
  file.save(pdf_path)
  
  documents = load_documents()
  chunks = split_documents(documents)
  result = add_to_chroma(chunks)
  
  print(result, "resulttt")
  return jsonify({"message": f"PDF uploaded and indexed successfully!,{result}"})

if __name__ == '__main__':
    app.run(debug=True)