from flask import Flask, request, render_template
import os

app = Flask(_name_)

# Set the path for file uploads
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template(r"C:\Users\boina\Desktop\hemesh\templates\index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        # Save the uploaded file to the upload folder
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return 'File uploaded successfully'

if _name_ == '_main_':
    app.run(debug=True)


from impedance import preprocessing
# Load data from the example EIS data
frequencies, Z = preprocessing.readCSV(UPLOAD_FOLDER+"./exampleData.csv")

# keep only the impedance data in the first quandrant
frequencies, Z = preprocessing.ignoreBelowX(frequencies, Z)


from impedance.models.circuits import CustomCircuit

circuit = 'R0-p(R1,C1)-p(R2-Wo1,C2)'
initial_guess = [.01, .01, 100, .01, .05, 100, 1]

circuit = CustomCircuit(circuit, initial_guess=initial_guess)


circuit.fit(frequencies, Z)
print(circuit)


Z_fit = circuit.predict(frequencies)


import matplotlib.pyplot as plt
from impedance.visualization import plot_nyquist

fig, ax = plt.subplots()
plot_nyquist(Z, fmt='o', scale=10, ax=ax)
plot_nyquist(Z_fit, fmt='-', scale=10, ax=ax)

plt.legend(['Data', 'Fit'])
plt.show()