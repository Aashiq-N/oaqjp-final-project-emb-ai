import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        # Input text designed to evoke "joy"
        text = "I am so happy and excited!"
        result = emotion_detector(text)
        # Compute the dominant emotion
        dominant_emotion = max(result, key=result.get)
        self.assertEqual(dominant_emotion, 'joy')

    def test_anger(self):
        # Input text designed to evoke "anger"
        text = "I am furious about what just happened!"
        result = emotion_detector(text)
        dominant_emotion = max(result, key=result.get)
        self.assertEqual(dominant_emotion, 'anger')

    def test_sadness(self):
        # Input text designed to evoke "sadness"
        text = "I feel so sad and heartbroken."
        result = emotion_detector(text)
        dominant_emotion = max(result, key=result.get)
        self.assertEqual(dominant_emotion, 'sadness')

    def test_fear(self):
        # Input text designed to evoke "fear"
        text = "I am really scared and afraid of what might happen."
        result = emotion_detector(text)
        dominant_emotion = max(result, key=result.get)
        self.assertEqual(dominant_emotion, 'fear')

    def test_disgust(self):
        # Input text designed to evoke "disgust"
        text = "This situation is absolutely disgusting."
        result = emotion_detector(text)
        dominant_emotion = max(result, key=result.get)
        self.assertEqual(dominant_emotion, 'disgust')

if __name__ == '__main__':
    unittest.main()
