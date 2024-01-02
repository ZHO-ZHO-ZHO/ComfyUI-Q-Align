from q_align.evaluate.scorer import QAlignScorer
from q_align.evaluate.scorer import QAlignAestheticScorer
from PIL import Image

class QAlign_Zho:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",), 
            },
        }

    RETURN_TYPES = ("FLOAT", "STRING", "FLOAT", "STRING")
    RETURN_NAMES = ("Image Quality Score (IQA)", "IQA Rating", "Image Aesthetics Score (IAA)", "IAA Rating")
    FUNCTION = "evaluate_images"

    CATEGORY = "💯Q-Align"

    def evaluate_images(self, image):
        IQA_scorer = QAlignScorer()
        IQA_scores = IQA_scorer(image)

        IAA_scorer = QAlignAestheticScorer()
        IAA_scores = IAA_scorer(image)

        IQA_rating = self.get_rating(IQA_scores)
        IAA_rating = self.get_rating(IAA_scores)
      
        return (IQA_scores, IQA_rating, IAA_scores, IAA_rating,)

    def get_rating(self, score):
        if score < 1.5:
            return "bad"
        elif score < 2.5:
            return "poor"
        elif score < 3.5:
            return "fair"
        elif score < 4.5:
            return "good"
        else:
            return "excellent"



NODE_CLASS_MAPPINGS = {
    "QAlign_Zho": QAlign_Zho
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "QAlign_Zho": "💯 Q-Align Scoring"
}
