"""
SentimentScope - Backend API
Sentiment Analysis using Transformers and TextBlob
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
from textblob import TextBlob
import re
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Initialize sentiment analysis pipeline
# Using distilbert-base-uncased-finetuned-sst-2-english (fast & accurate)
print("Loading sentiment analysis model...")
sentiment_analyzer = pipeline("sentiment-analysis", 
                              model="distilbert-base-uncased-finetuned-sst-2-english")
print("Model loaded successfully!")

def clean_text(text):
    """Clean and preprocess text"""
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove user mentions and hashtags
    text = re.sub(r'@\w+|#\w+', '', text)
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text

def analyze_with_textblob(text):
    """Analyze sentiment using TextBlob (simpler, faster)"""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # -1 to 1
    
    if polarity > 0.1:
        sentiment = "POSITIVE"
        score = (polarity + 1) / 2  # Convert to 0-1 scale
    elif polarity < -0.1:
        sentiment = "NEGATIVE"
        score = 1 - ((polarity + 1) / 2)
    else:
        sentiment = "NEUTRAL"
        score = 0.5
    
    return {
        "label": sentiment,
        "score": round(score, 4),
        "polarity": round(polarity, 4)
    }

def analyze_with_transformers(text):
    """Analyze sentiment using Transformers (more accurate)"""
    result = sentiment_analyzer(text[:512])[0]  # Limit to 512 chars for model
    
    # Map model labels to our format
    label_map = {
        "POSITIVE": "POSITIVE",
        "NEGATIVE": "NEGATIVE",
        "NEUTRAL": "NEUTRAL"
    }
    
    return {
        "label": label_map.get(result['label'], result['label']),
        "score": round(result['score'], 4)
    }

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "SentimentScope API is running",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/analyze', methods=['POST'])
def analyze_sentiment():
    """Analyze sentiment of provided text"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400
        
        text = data['text']
        method = data.get('method', 'transformers')  # 'transformers' or 'textblob'
        
        if not text or len(text.strip()) == 0:
            return jsonify({"error": "Text cannot be empty"}), 400
        
        # Clean text
        cleaned_text = clean_text(text)
        
        # Analyze based on method
        if method == 'textblob':
            result = analyze_with_textblob(cleaned_text)
        else:
            result = analyze_with_transformers(cleaned_text)
        
        return jsonify({
            "success": True,
            "text": text,
            "cleaned_text": cleaned_text,
            "sentiment": result,
            "method": method,
            "timestamp": datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/batch-analyze', methods=['POST'])
def batch_analyze():
    """Analyze sentiment of multiple texts"""
    try:
        data = request.get_json()
        
        if not data or 'texts' not in data:
            return jsonify({"error": "No texts provided"}), 400
        
        texts = data['texts']
        method = data.get('method', 'transformers')
        
        if not isinstance(texts, list):
            return jsonify({"error": "texts must be an array"}), 400
        
        results = []
        sentiment_counts = {"POSITIVE": 0, "NEGATIVE": 0, "NEUTRAL": 0}
        
        for text in texts[:100]:  # Limit to 100 texts
            if text and len(text.strip()) > 0:
                cleaned = clean_text(text)
                
                if method == 'textblob':
                    sentiment = analyze_with_textblob(cleaned)
                else:
                    sentiment = analyze_with_transformers(cleaned)
                
                results.append({
                    "text": text,
                    "sentiment": sentiment
                })
                
                sentiment_counts[sentiment['label']] += 1
        
        # Calculate percentages
        total = len(results)
        sentiment_percentages = {
            label: round((count / total * 100), 2) if total > 0 else 0
            for label, count in sentiment_counts.items()
        }
        
        return jsonify({
            "success": True,
            "total_analyzed": total,
            "results": results,
            "summary": {
                "counts": sentiment_counts,
                "percentages": sentiment_percentages
            },
            "timestamp": datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/compare-methods', methods=['POST'])
def compare_methods():
    """Compare sentiment analysis methods"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400
        
        text = data['text']
        cleaned = clean_text(text)
        
        # Analyze with both methods
        textblob_result = analyze_with_textblob(cleaned)
        transformers_result = analyze_with_transformers(cleaned)
        
        return jsonify({
            "success": True,
            "text": text,
            "textblob": textblob_result,
            "transformers": transformers_result,
            "timestamp": datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"\n🚀 SentimentScope API running on http://localhost:{port}")
    print("📊 Ready to analyze sentiment!\n")
    app.run(debug=True, host='0.0.0.0', port=port)
