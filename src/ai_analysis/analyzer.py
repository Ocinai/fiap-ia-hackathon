
from pathlib import Path
from PIL import Image

class AIAnalyzer:

    def analyze_diagram(self, image_path: Path) -> str:
        """
        Analyzes the diagram image using a two-step AI process.

        Args:
            image_path: The path to the image file.

        Returns:
            A string containing the AI's analysis of the diagram.
        """
        try:
            # Step 1: Image-to-text
            image = Image.open(image_path)
            caption = self.captioner(image)[0]['generated_text']

            # Step 2: Text-to-threats
            prompt = f"Based on the following architecture diagram description, identify potential security threats and suggest mitigations:\n\n{caption}\n\nThreats:"
            threats = self.text_generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
            
            return threats
        except Exception as e:
            return f"Error analyzing image: {e}"

