from flask import Flask, request, jsonify
import numpy as np
import torch
import torch.nn as nn

app = Flask(__name__)

# Neural network architecture 
class NeuralNet(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(NeuralNet, self).__init__()
        self.fc_layer1 = nn.Linear(input_dim, hidden_dim)    
        self.fc_layer2 = nn.Linear(hidden_dim, output_dim)   

    def forward(self, x):
        x = torch.relu(self.fc_layer1(x))   
        x = self.fc_layer2(x)               
        return x

# Load the model
model_path = "./models/model.pt"
checkpoint = torch.load(model_path)
scaler_params = checkpoint['scaler_params']

torch.manual_seed(42)
model  = NeuralNet(1, 12, 1)
model.load_state_dict(checkpoint['model_state_dict'])
model.eval() 

@app.route('/predict', methods=['POST'])
def predict():
    """
    This POST endpoint takes a 'month' and returns the predicted number of scanned receipts for that month.
    
    Params: 
        - 'month<str>' : can be a month name or a month number (1-12)
    Returns: 
        - JSON response with the prediction of number of scanned receipts for that month
    Errors: 
        - JSON reponse indicating errors; could be because of invalid data types, missing parameters, etc.
    """
    try:
        all_months = [
            "january", "february", "march", "april", "may", "june",
            "july", "august", "september", "october", "november", "december"
        ]
        data = request.json
        if 'month' not in data or not isinstance(data['month'], str):
            return jsonify({'error': 'You need a month field and it needs to be a string'}), 400

        month = request.json['month']

        if month.lower() in all_months:
            month = all_months.index(month.lower()) + 1   
        elif month.isdigit() and int(month) in range(1, 13):
            month = int(month)
        else:
            return jsonify({'error': 'Please enter a valid month number or valid month (1, March, June, 7, etc)'}), 400
        
        scaled_month = ((int(month) + 12) - scaler_params["X_min"]) / (scaler_params["X_max"] - scaler_params["X_min"])

        input_tensor = torch.tensor(scaled_month, dtype=torch.float32).unsqueeze(0)  

        with torch.no_grad():
            output = model(input_tensor)
                
        unscaled_output = output * (scaler_params["y_max"] - scaler_params["y_min"]) + scaler_params["y_min"]
        total_receipts_predicted = int(unscaled_output.item())
        return jsonify({'prediction': total_receipts_predicted}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
