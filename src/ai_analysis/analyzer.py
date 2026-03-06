
import torch
from torchvision import transforms
from pathlib import Path
from PIL import Image
from src.supervised_model.model import SimpleCNN, load_model

class AIAnalyzer:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = SimpleCNN(num_classes=10).to(self.device)
        self.model = load_model(self.model, "model/supervised_model.pth")
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        # placeholder for existing models
        self.captioner = None
        self.text_generator = None


    def analyze_diagram(self, image_path: Path) -> str:
        """
        Analyzes the diagram image using a two-step AI process.

        Args:
            image_path: The path to the image file.

        Returns:
            A string containing the AI's analysis of the diagram.
        """
        try:
            # Supervised model classification
            image = Image.open(image_path).convert('RGB')
            image_tensor = self.transform(image).unsqueeze(0).to(self.device)
            with torch.no_grad():
                outputs = self.model(image_tensor)
                _, predicted = torch.max(outputs.data, 1)
                predicted_class = predicted.item()

            # Step 1: Image-to-text
            caption = self.captioner(image)[0]['generated_text'] if self.captioner else "No captioner model found"

            # Step 2: Text-to-threats
            prompt = f"Based on the following architecture diagram description, identify potential security threats and suggest mitigations:\n\n{caption}\n\nThreats:"
            threats = self.text_generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text'] if self.text_generator else "No text generator model found"
            
            return f"Predicted Diagram Type: {predicted_class}\n\n" + threats
        except Exception as e:
            return f"Error analyzing image: {e}"

