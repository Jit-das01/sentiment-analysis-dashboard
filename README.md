# 🎭 SentimentScope - AI-Powered Sentiment Analysis Dashboard

A beautiful, real-time sentiment analysis dashboard powered by state-of-the-art NLP models (BERT & TextBlob).

![Status](https://img.shields.io/badge/Status-MVP-success)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![React](https://img.shields.io/badge/React-18-blue)
![ML](https://img.shields.io/badge/ML-NLP-orange)

## ✨ Features

### 🤖 **Dual AI Models**
- **BERT (Transformers)** - State-of-the-art deep learning model
- **TextBlob** - Fast, rule-based analysis
- Compare both methods side-by-side

### 📊 **Interactive Dashboard**
- Real-time sentiment analysis
- Beautiful visualizations
- Confidence score display
- Quick example texts
- Character counter

### 🎨 **Beautiful UI/UX**
- Gradient design
- Smooth animations
- Responsive layout
- Loading states
- Error handling

## 🛠️ Tech Stack

### Backend
- **Python 3.10+**
- **Flask** - REST API framework
- **Transformers** (Hugging Face) - BERT models
- **TextBlob** - NLP library
- **NLTK** - Natural language toolkit

### Frontend
- **React 18** - UI library
- **Vanilla CSS** - Styling
- **Chart.js** - Ready for visualizations

### ML Models
- **DistilBERT** - Efficient BERT variant
- **Fine-tuned on SST-2** - Sentiment analysis dataset

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Modern web browser

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/sentiment-dashboard.git
cd sentiment-dashboard
```

### Step 2: Set Up Backend

```bash
# Navigate to backend
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download NLTK data (required for TextBlob)
python -c "import nltk; nltk.download('brown'); nltk.download('punkt')"

# Run the backend server
python app.py
```

The backend will start on `http://localhost:5000`

### Step 3: Open Frontend

```bash
# In a new terminal, navigate to frontend
cd frontend

# Simply open index.html in your browser
# On Mac:
open index.html

# On Linux:
xdg-open index.html

# On Windows:
start index.html
```

Or just double-click `index.html` to open it!

## 📖 How to Use

1. **Enter Text**: Type or paste any text into the text area
2. **Choose Method**: Select either Transformers (BERT) or TextBlob
3. **Analyze**: Click "Analyze Sentiment"
4. **View Results**: See sentiment label, confidence score, and emoji

### Quick Examples
Click any of the example buttons to instantly analyze pre-written texts!

## 🎯 API Endpoints

### Health Check
```bash
GET /api/health
```

### Analyze Single Text
```bash
POST /api/analyze
Content-Type: application/json

{
  "text": "This is amazing!",
  "method": "transformers"  // or "textblob"
}
```

### Batch Analysis
```bash
POST /api/batch-analyze
Content-Type: application/json

{
  "texts": ["Text 1", "Text 2", "Text 3"],
  "method": "transformers"
}
```

### Compare Methods
```bash
POST /api/compare-methods
Content-Type: application/json

{
  "text": "This is great!"
}
```

## 💡 How It Works

### BERT (Transformers)
1. Text is cleaned and preprocessed
2. Passed through DistilBERT model
3. Model outputs sentiment probability
4. Returns label (POSITIVE/NEGATIVE) + confidence score

### TextBlob
1. Text is cleaned
2. Polarity score calculated (-1 to 1)
3. Categorized as positive/neutral/negative
4. Returns label + score

## 📊 Model Details

### DistilBERT
- **Model**: `distilbert-base-uncased-finetuned-sst-2-english`
- **Parameters**: 66M
- **Training**: Stanford Sentiment Treebank (SST-2)
- **Accuracy**: ~91% on SST-2 test set

### TextBlob
- **Type**: Rule-based
- **Speed**: Very fast
- **Use Case**: Quick analysis, real-time applications

## 🔮 Roadmap

### Phase 2: Live Data (Next)
- [ ] Twitter API integration
- [ ] Reddit API integration
- [ ] Real-time trending topics
- [ ] Database storage

### Phase 3: Advanced Features
- [ ] Time-series visualization
- [ ] Word clouds
- [ ] Sentiment trends over time
- [ ] Export data as CSV/JSON
- [ ] Dark mode

### Phase 4: Deployment
- [ ] Deploy backend to Heroku/Railway
- [ ] Deploy frontend to Netlify/Vercel
- [ ] Add authentication
- [ ] Rate limiting
- [ ] Caching

## 🎓 What I Learned

Building this project taught me:
- **NLP Fundamentals** - Text preprocessing, sentiment analysis
- **Transformers** - Working with pre-trained BERT models
- **API Development** - Building RESTful APIs with Flask
- **Model Deployment** - Serving ML models in production
- **Full-Stack Integration** - Connecting React to Flask
- **Error Handling** - Graceful failures and user feedback

## 🧪 Testing

### Test the Backend API

```bash
# Health check
curl http://localhost:5000/api/health

# Analyze sentiment
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "This is amazing!", "method": "transformers"}'
```

### Example Texts to Try
- "This product exceeded all my expectations! Absolutely love it!"
- "Worst purchase ever. Complete waste of money."
- "It's okay, nothing special."
- "The service was terrible and the staff was rude."
- "I'm so happy with this decision!"

## 🐛 Troubleshooting

### Backend won't start
- Make sure Python 3.10+ is installed
- Check if all dependencies are installed
- Try: `pip install --upgrade pip` then reinstall dependencies

### "Failed to connect to API" error
- Ensure backend is running on port 5000
- Check if Flask server started successfully
- Verify CORS is enabled

### Model loading is slow
- First time loading downloads the model (~250MB)
- Subsequent starts will be faster
- Consider using TextBlob for faster startup

## 📄 License

MIT License - Free to use!

## 👨‍💻 Author

**Jit Das** - 3rd Year CS Student

Connect with me:
- GitHub: [@Jit-das01](https://github.com/Jit-das01)
- LinkedIn: [Your LinkedIn]
- Email: your.email@example.com

## 🙏 Acknowledgments

- Hugging Face for Transformers library
- Flask team for amazing framework
- TextBlob developers
- Stanford NLP Group for SST-2 dataset

---

⭐ **If you find this project useful, please give it a star!** ⭐

**Built with ❤️ using Python, React, and BERT**

---

## 📸 Screenshots

### Main Dashboard
![Dashboard](screenshots/dashboard.png)

### Analysis Results
![Results](screenshots/results.png)

## 🔗 Links

- [Live Demo](https://your-demo-url.com) *(Coming Soon)*
- [Documentation](https://github.com/YOUR_USERNAME/sentiment-dashboard/wiki)
- [Report Bug](https://github.com/YOUR_USERNAME/sentiment-dashboard/issues)
