# 🌟 RLHF-PPO-DPO-GRPO-KTO-Implementation 🌟

## 📖 Overview

This repository contains educational, theoretical implementations of:

- **Reinforcement Learning with Human Feedback (RLHF)**
- **Proximal Policy Optimization (PPO)**
- **Direct Preference Optimization (DPO)**
- **Generalized Reward Policy Optimization (GRPO)**
- **Odds Ratio Preference Optimization (ORPO)**
- **Kullback–Leibler-based Training Objective (KTO)**

The project is intended as a showcase of my understanding of these algorithms, both theoretically and practically. I have recently learned their theory and am now implementing them to demonstrate my ability to apply them to use cases. The code is for educational purposes only.

---

## 🚀 Features

- **RLHF, PPO, DPO, GRPO, ORPO, KTO Implementations**: Educational, theoretical implementations of popular RL algorithms for language model alignment.
- **Sentiment Analysis Example**: Demonstrates use on the IMDB dataset.
- **Hugging Face Integration**: Utilizes state-of-the-art libraries like `transformers` and `datasets`.
- **Customizable Training**: Easily modify configurations for different datasets and models.

---

## 🛠️ Installation

To get started, clone the repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/AmenallahBouhachem/RLHF-PPO-DPO-GRPO-KTO-Implementation.git
cd RLHF-PPO-DPO-GRPO-KTO-Implementation
```

---

## 📂 Project Structure

```
RLHF-PPO-DPO-GRPO-KTO-Implementation
├── RLHF_PPO_ON_IMDB.ipynb   # Main notebook for training and evaluation
├── DPO_Implementation.ipynb  # DPO implementation notebook
├── GRPO-Implementation.ipynb # GRPO implementation notebook
├── ORPO-IMPlmeNTATION.ipynb  # ORPO implementation notebook
├── KTO-Implementation.ipynb  # KTO implementation notebook
├── loss_computation.py      # Custom loss computation logic
├── LICENSE                  # License information
└── README.md                # Project documentation
```

---

## 📊 Example Use Case: Sentiment Analysis

### Sentiment Analysis Examples

- **Input**: "This movie was really bad!!"
  - **Sentiment**: Negative
- **Input**: "This movie was really good!!"
  - **Sentiment**: Positive

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

---

## 📚 Disclaimer

This repository is for educational purposes only. The implementations are intended to demonstrate my understanding of RLHF, PPO, DPO, GRPO,ORPO and KTO, both in theory and in practice. The code is not intended for production use.
