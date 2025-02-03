# Import required libraries
from transformers import pipeline


def main():
    try:
        # Create a text classification pipeline using a pre-trained model
        # 'distilbert-base-uncased-finetuned-sst-2-english' is a lightweight but effective model
        classifier = pipeline(
            task="text-classification",
            model="cardiffnlp/twitter-roberta-base-sentiment-latest",  # 3-class model
            framework="pt",  # Use PyTorch
        )

        # Different model with explicit neutral support
        neutral_classifier = pipeline(
            task="text-classification",
            model="finiteautomata/bertweet-base-sentiment-analysis",  # Explicit neutral label
            framework="pt",
        )

        # Example texts for analysis
        sample_texts = [
            "I absolutely love this new feature!",
            "The service was terrible and slow.",
            "This is a neutral statement with no strong sentiment.",
            "how are you doing?",
        ]

        # Process each text through the pipeline
        for text in sample_texts:
            result = classifier(text)
            print(f"Text: {text}")
            print(f"Label: {result[0]['label']} (Confidence: {result[0]['score']:.4f})")
            print("-" * 50)

            # Add after getting result
            confidence = result[0]["score"]
            if 0.3 < confidence < 0.7:  # Wider confidence range
                label = "NEUTRAL"
                confidence = abs(confidence - 0.5) * 2  # Normalize to 0-1 scale
                print(f"Adjusted Label: {label} (Confidence: {confidence:.4f})")
            else:
                print(
                    f"Original Label: {result[0]['label']} (Confidence: {confidence:.4f})"
                )

    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    main()
