# 🌟 RLHF-PPO Implementation 🌟

## 📖 Overview

This repository contains a theoretical implementation of **Reinforcement Learning with Human Feedback (RLHF)** using **Proximal Policy Optimization (PPO)**. The project is applied to the IMDB dataset for sentiment analysis, showcasing the alignment of language models with human preferences.

---

## 🚀 Features

- **RLHF with PPO**: Train language models with human feedback.
- **Sentiment Analysis**: Fine-tuned on the IMDB dataset.
- **Hugging Face Integration**: Utilizes state-of-the-art libraries like `transformers` and `datasets`.
- **Customizable Training**: Easily modify configurations for different datasets and models.

---

## 🛠️ Installation

To get started, clone the repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/AmenallahBouhachem/RLHF-PPO-Implementation.git
cd RLHF-PPO-Implementation
```

---

## 📂 Project Structure

```
RLHF-PPO-Theoretical-Implementation
├── RLHF_PPO_ON_IMDB.ipynb   # Main notebook for training and evaluation
├── loss_computation.py      # Custom loss computation logic
├── LICENSE                  # License information
└── README.md                # Project documentation
```

---

## 📊 Results

### Sentiment Analysis Examples

- **Input**: "This movie was really bad!!"

  - **Sentiment**: Negative
- **Input**: "This movie was really good!!"

  - **Sentiment**: Positive

---

## 📈 Training Pipeline

1. **Data Preparation**: Preprocess the IMDB dataset for training.
2. **Model Initialization**: Load GPT-2 and reward models.
3. **Training**: Use PPO to align the model with human feedback.
4. **Evaluation**: Test the model on unseen data.

---

## 📦 Dependencies

- `transformers`
- `datasets`
- `trl`
- `torch`
- `tqdm`

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
